"""End-to-end test of research.py with a fake Anthropic client (no network, no cost).

Run: python test_fake_run.py   (or: pytest test_fake_run.py)

Covers: pause_turn resume, running a client tool (arxiv_search), re-prompting when Claude doesn't submit, URL dedupe (utm params,
arXiv abs/pdf/html variants), stopping at the target, unusable sources, API errors, per-stage
model/effort choice, the appended source list, and resume making no new calls.
"""
import asyncio
import json
import os
import sys
import tempfile
from pathlib import Path
from types import SimpleNamespace as NS

sys.path.insert(0, str(Path(__file__).parent))
import research

calls = {"create": 0, "pause": 0, "nudge": 0, "arxiv": 0}
seen_models = {}


def usage():
    return NS(input_tokens=1000, output_tokens=100, cache_read_input_tokens=0, cache_creation_input_tokens=0,
              server_tool_use=NS(web_search_requests=1, web_fetch_requests=0))


def resp(stop, content, model):
    return NS(stop_reason=stop, stop_details=None, content=content, usage=usage(), model=model)


def tool(name, inp):
    return NS(type="tool_use", name=name, input=inp)


class Messages:
    async def create(self, **kw):
        calls["create"] += 1
        assert kw["fallbacks"] == "default"
        submit = kw["tools"][-1]["name"]
        seen_models[submit] = (kw["model"], kw["output_config"]["effort"])
        prompt = kw["messages"][0]["content"]
        model = kw["model"]
        if submit == "submit_plan":
            subtopics = [{"name": f"t{i}", "search_focus": "x"} for i in range(4)]
            return resp("tool_use", [tool(submit, {"subtopics": subtopics})], model)
        if submit == "submit_sources":
            assert kw["tools"][0]["blocked_domains"] == research.UNFETCHABLE
            # the first call for t0 pauses, to exercise pause_turn resume
            if "Subtopic: t0" in prompt and len(kw["messages"]) == 1:
                calls["pause"] += 1
                return resp("pause_turn", [NS(type="server_tool_use")], model)
            # t1 calls arxiv_search first, to exercise running a client tool and returning its result
            if "Subtopic: t1" in prompt and len(kw["messages"]) == 1:
                return resp("tool_use", [NS(type="tool_use", id="tu1", name="arxiv_search",
                                            input={"query": "all:x", "max_results": 3})], model)
            if "Subtopic: t1" in prompt:
                result = kw["messages"][-1]["content"][0]
                assert result == {"type": "tool_result", "tool_use_id": "tu1", "content": "arxiv results for all:x"}
            t = prompt.split("Subtopic: ")[1].split("\n")[0]
            srcs = [{"url": f"https://Ex.com/{t}/{j}/?utm_source=z", "title": f"{t}-{j}", "why_relevant": "r"}
                    for j in range(3)]
            srcs.append({"url": "https://ex.com/shared/", "title": "dup", "why_relevant": "r"})
            return resp("tool_use", [tool(submit, {"sources": srcs})], model)
        if submit == "submit_notes":
            url = prompt.split("Source URL: ")[1].split("\n")[0]
            if url.endswith("/1/?utm_source=z") and len(kw["messages"]) == 1:
                calls["nudge"] += 1  # ends the turn without submitting -> should get re-prompted
                return resp("end_turn", [NS(type="text", text="done")], model)
            if "t3/2" in url:
                raise RuntimeError("simulated API error")
            ok = "t2/0" not in url
            return resp("tool_use", [tool(submit, {
                "fetched_ok": ok, "failure_reason": "" if ok else "paywall", "title": "T", "publisher": "P",
                "published_date": "", "relevance": "high", "reliability_notes": "",
                "key_points": [{"claim": "c", "evidence_quote": "q"}]})], model)
        raise AssertionError(submit)

    def stream(self, **kw):
        n = kw["messages"][0]["content"].count('"id"')

        class Stream:
            async def __aenter__(s):
                return s

            async def __aexit__(s, *a):
                return False

            async def get_final_message(s):
                return resp("end_turn", [NS(type="text", text=f"Summary of {n} sources [s001]")], kw["model"])
        return Stream()


class FakeClient:
    def __init__(self, **kw):
        self.beta = NS(messages=Messages())


def run_main(*args):
    saved = sys.argv
    sys.argv = ["research.py", "Test Task!", *args]
    try:
        asyncio.run(research.main())
    finally:
        sys.argv = saved


def test_url_helpers():
    variants = ["https://arxiv.org/abs/2506.11763", "https://arxiv.org/pdf/2506.11763v2",
                "https://arxiv.org/html/2506.11763v1", "https://export.arxiv.org/abs/2506.11763",
                "https://arxiv.org/pdf/2506.11763.pdf"]
    assert {research.normalize_url(u) for u in variants} == {"https://arxiv.org/abs/2506.11763"}
    assert research.fetch_url("https://arxiv.org/abs/2506.11763") == "https://arxiv.org/pdf/2506.11763"
    assert research.fetch_url("https://example.com/a") == "https://example.com/a"
    assert research.normalize_url("https://Ex.com/a/?utm_source=z") == research.normalize_url("https://ex.com/a")


async def fake_arxiv_search(query, max_results=10):
    calls["arxiv"] += 1
    return f"arxiv results for {query}"


def test_pipeline_end_to_end():
    real_client, real_arxiv, cwd = research.anthropic.AsyncAnthropic, research.arxiv_search, os.getcwd()
    research.anthropic.AsyncAnthropic = FakeClient
    research.arxiv_search = fake_arxiv_search
    try:
        with tempfile.TemporaryDirectory() as tmp:
            os.chdir(tmp)
            run_main("--max-sources", "8", "--concurrency", "3")
            run = Path(tmp) / "runs" / "test-task"

            sources = json.loads((run / "sources.json").read_text(encoding="utf-8"))
            urls = [s["url"] for s in sources]
            assert len(sources) == 12  # 13 unique candidates, trimmed to ceil(8 * OVERCOLLECT)
            assert len({research.normalize_url(u) for u in urls}) == len(urls)

            notes = [json.loads(p.read_text(encoding="utf-8")) for p in (run / "notes").glob("*.json")]
            usable = [n for n in notes if n["fetched_ok"]]
            assert len(usable) >= 8
            assert any(n["id"] == "s003" and not n["fetched_ok"] for n in notes)  # the "paywall" source

            assert calls["pause"] == 1 and calls["nudge"] >= 1 and calls["arxiv"] == 1
            assert seen_models["submit_plan"][0] == research.MODEL
            assert seen_models["submit_sources"][0] == research.MODEL
            assert seen_models["submit_notes"] == (research.EXTRACT_MODEL, research.EXTRACT_EFFORT)

            summary = (run / "summary.md").read_text(encoding="utf-8")
            source_list = summary.split("## Sources")[1]
            assert "[s001]" in source_list and "[s003]" not in source_list

            calls["create"] = 0
            run_main("--max-sources", "8")  # resume: nothing left to search or read
            assert calls["create"] == 0
            os.chdir(cwd)
    finally:
        research.anthropic.AsyncAnthropic = real_client
        research.arxiv_search = real_arxiv
        os.chdir(cwd)


if __name__ == "__main__":
    test_url_helpers()
    test_pipeline_end_to_end()
    print("\nall checks passed")
