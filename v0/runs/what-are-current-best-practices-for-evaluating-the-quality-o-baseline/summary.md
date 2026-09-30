# What are current best practices for evaluating the quality of LLM-based research agents?

# Evaluating LLM-Based Research Agents: Current Best Practices

## Summary

There is no settled standard for evaluating research agents. The six sources are one paper (DeepResearch Bench) seen twice, two other benchmarks, a factuality method, one piece of vendor documentation, and a meta-evaluation of LLM judges. Across them, a consistent practice emerges:

- Evaluate along several separate axes: report quality, factual and citation grounding, retrieval ability, and process or trajectory.
- Build tasks from realistic, expert-authored material.
- Use LLM judges, but anchor them with references and task-specific criteria.
- Validate those judges against expert humans before trusting them.

The biggest unresolved tension is how reliable LLM judges are for long, realistic research reports. One benchmark reports judge agreement above human inter-annotator agreement [s002]. An independent meta-evaluation finds judges only slightly better than chance on realistic long documents [s006].

## 1. What to evaluate: final output, process, or both

- **The final report as the main interface.** DeepResearch Bench argues that agents' internal processes are opaque. That makes the final report "the primary interface" for assessing performance. For complex research queries, a definitive ground truth is "almost impossible" [s002].
- **The trajectory.** LangChain's guidance argues the opposite emphasis. Many agent behaviours, such as tool choice or the downstream effects of a prompt change, only appear with a real LLM in the loop, so the full sequence of messages and tool calls should be evaluated [s003].
- **End-to-end rather than isolated skills.** Earlier benchmarks tested isolated capabilities: browsing or retrieval alone, or generation without live information gathering. They did not test integrated research [s002]. Those older retrieval benchmarks are also now saturated [s004].

These positions are complementary rather than contradictory. Output evaluation captures what users receive. Trajectory evaluation captures efficiency and correct procedure. However, only the vendor source [s003] addresses trajectories, and it gives no research-agent-specific evidence. Its examples use generic tool-calling agents [s003].

## 2. Task and benchmark design

**Realism of the task distribution**
- DeepResearch Bench derived its topic mix from 96,147 real user queries. It filtered these to 44,019 deep-research queries across 22 domains, then compressed them proportionally into 100 tasks (50 Chinese, 50 English) [s002].
- Tasks were proposed by PhD holders or practitioners with more than five years of domain experience, then screened manually [s001][s002].

**Verifiable short-answer tasks as a complementary design**
- BrowseComp uses 1,266 hard questions with short reference answers that are easy to verify [s004].
- Questions are "inverted": authors start from a known fact, so answers are hard to find but easy to check. The trade-off is that alternative valid answers cannot be fully ruled out [s004].
- The authors say plainly that BrowseComp skips realistic query distributions, long answers and ambiguity. It is a useful but partial proxy [s004].

**Disagreement on QA-style evaluation.** DeepResearch Bench criticises prior research-agent evaluations that rely on QA datasets, saying they don't reflect real use [s002]. BrowseComp defends short-answer QA as a clean measure of persistence and creativity in finding information [s004]. A reasonable reading is that both are needed. Short-answer benchmarks measure retrieval depth reliably. Report-based benchmarks measure synthesis.

**Difficulty calibration and hygiene** [s004]
- Adversarial filtering: current models had to fail each question, the answer could not appear on the first page of five Google searches, and another person should not solve it within 10 minutes. Tasks solved more than 40% of the time were sent back for revision.
- Auditing: tasks the model always failed were reviewed. 21 of 118 had faulty labels and were removed.
- Contamination control: the paper includes a canary string and asks readers not to post examples online, so browsing agents cannot simply look up answers.

## 3. Scoring report quality with LLM judges

DeepResearch Bench's RACE framework makes several design choices, each backed by an ablation or argument. All come from [s002] unless noted.

- **Adaptive, task-specific criteria within fixed dimensions.** Fixed checklists and static rubrics adapt poorly to diverse tasks. Letting the LLM invent criteria from scratch drifts from the intended assessment goals. RACE therefore fixes four top-level dimensions (Comprehensiveness, Insight/Depth, Instruction-Following, Readability) and has the judge generate task-specific criteria and weights beneath them.
- **Reference-based relative scoring.** Judges scoring reports in isolation give uniformly high scores. RACE instead scores each report against a high-quality reference report, computing S_tgt/(S_tgt+S_ref). In the ablation, removing the reference caused the largest drop in agreement with humans (71.33% to 66.56%).
- **Interpret rankings, not absolute values.** Relative scores are compressed, so the authors advise focusing on rankings and proportional differences rather than absolute scores.
- **Pre-processing.** Strip citation formatting before judging, because long or complex citation styles hurt the judge's scoring.

**Independent evidence on references and rubrics is mixed** [s006]:
- Adding references raised average judge accuracy from 0.5313 to 0.5843.
- Rubrics substantially helped on a deep-research dataset labelled DR-Bench, raising accuracy from 0.5454 to 0.7075. DR-Bench is likely the plain-text DeepResearch Bench.
- The benefits were not additive. Reference plus rubric scored 0.5784, slightly below reference alone. Rubrics hurt accuracy on some tasks.

So references are fairly well supported. Rubrics look task-dependent rather than universally helpful. This partly qualifies [s002]'s claim that adaptive criteria beat static ones, though the two papers test different rubric designs.

## 4. Factuality, citation, and retrieval grounding

**Citation verification.** DeepResearch Bench's FACT framework works as follows [s002]:
1. Extract statement–URL pairs and remove duplicates.
2. Fetch each cited page.
3. Have an LLM make a binary judgment of whether the page supports the statement.

It reports two metrics:
- **Citation Accuracy:** the precision of the agent's citations.
- **Average Effective Citations per task:** the volume of verifiably supported information.

Because the verification step is token-heavy, a cheaper model (Gemini-2.5-flash) was used for it [s002].

**Atomic-fact checking.** SAFE splits a long response into individual facts and checks each one through multi-step Google Search reasoning [s005]. Its F1@K metric balances precision (the share of supported facts) against recall relative to a user-preferred response length K [s005].
- SAFE agreed with crowdsourced annotators on 72% of about 16k facts.
- It was judged correct in 76% of 100 sampled disagreement cases.
- It costs more than 20 times less than human annotation [s005].

SAFE was designed for general long-form LLM output rather than research agents. Its method still transfers naturally to research reports.

**Precision and volume together.** The results show these can diverge. Gemini-2.5-Pro Deep Research led on effective citations (111.21). Perplexity Deep Research had the highest citation accuracy (90.24%) [s002]. Evaluations should therefore report both precision and coverage, which is also the logic behind F1@K [s005].

## 5. Validating the judge (meta-evaluation)

This is where the sources most clearly converge on method but diverge on results.

**Recommended practices**
- **Measure agreement with humans using several metrics.** [s002] uses pairwise agreement, Pearson and Spearman correlations. [s006] uses accuracy, Spearman and Kendall's tau-b, computed per query group.
- **Filter out tasks where the humans themselves disagree.** [s002] removed tasks with ICC < 0, leaving 37.
- **Use expert gold labels rather than LLM-generated ones.** LLM-generated labels risk circularity; [s006] criticises Long-form RewardBench on this basis.
- **Run pairwise comparisons in both orders to reduce position bias.** Order-swap inconsistency ranged from 10.6% to 78.7% across models [s006].
- **Compare judge models on both quality and cost.** In [s002], Gemini 2.5 Pro Preview scored best (72.56 at $0.13 per query), and o4-mini came close (71.63 at $0.04).

**Conflicting findings on how reliable judges are**
- [s002] reports that full RACE reached 71.33% pairwise agreement. This exceeds agreement between human experts (68.44%) and beats a vanilla judge prompt (58.89%).
- [s006] finds judges on long-form outputs (averaging about 9,250 tokens) only moderately reliable:
  - The best configuration reached 0.6721 accuracy.
  - The mean across 32 model–setting combinations was 0.5627, against a 0.5 random baseline.
  - Realistic deep-research documents with DOCX structure and multilingual content were among the hardest, at 0.4393, compared with 0.6454 on plain-text DR-Bench.

These figures use different metrics and data, so they are not directly comparable. The pattern, though, suggests that judge reliability measured on a benchmark's own clean, plain-text reports may overstate reliability on realistic deliverables.

**Further cautions from [s006]**
- A stronger general-purpose model is not necessarily a better judge. GPT-5.2 and GPT-4o-mini underperformed Qwen3-Max and others. This is in some tension with [s002]'s finding that the strong Gemini 2.5 Pro was the best judge.
- Turning on the judge's thinking mode lowered its accuracy (Qwen3-32B: 0.5745 to 0.5241).
- Judges reward surface richness. A 12K-token response that barely addressed the question scored 9.26 from the judge versus 5.87 from humans.
- Judges confuse domain concepts and perform poorly in specialised fields.
- Context-window overflow and safety refusals cause outright failures.

**Possible self-preference bias in [s002].** All reference reports come from Gemini-2.5-pro Deep Research, and the judge is also Gemini-2.5-pro. The top-ranked agent is Gemini-2.5-Pro Deep Research. The paper doesn't discuss this, and it is an unaddressed confound in its headline ranking [s002].

## 6. Reliability, variance, and compute reporting

BrowseComp models several practices beyond a single accuracy number [s004]:

- **Calibration.** Elicit a confidence score and measure calibration error. Browsing-enabled models were worse calibrated (Deep Research: 91% calibration error), suggesting web tools may inflate confidence in wrong answers.
- **Scaling with test-time compute.** Report performance as a function of compute. Accuracy rose smoothly with browsing effort.
- **Multi-sample aggregation.** With 64 samples per question, majority voting, confidence-weighted voting and best-of-N each improved accuracy by 15–25% over a single attempt. Best-of-N did best.
- **Per-task pass-rate distributions.** Deep Research solved 16% of tasks every time and failed 14% every time, showing a wide spread in task difficulty.
- **Ablating capabilities.** Browsing alone barely helped (GPT-4o: 0.6%; with browsing: 1.9%). Reasoning plus tool use mattered: o1 reached 9.9% and Deep Research 51.5%.
  - Deep Research was trained on BrowseComp-style data, and OpenAI built both the model and the benchmark [s004].

## 7. Trajectory evaluation techniques

For process evaluation, [s003] describes two approaches.

**Deterministic reference-trajectory matching** is fast, cheap and suited to well-defined workflows. It has four modes:

| Mode | What it checks | Typical use |
|---|---|---|
| Strict | Same tool calls in the same order | Enforcing required ordering, such as a policy lookup before authorising an action |
| Unordered | Same tool calls, any order | Multi-source retrieval where order doesn't matter |
| Subset | No tool calls outside the reference | Efficiency |
| Superset | All required calls happened; extras allowed | Minimum required actions |

By default, two tool calls match only if they call the same tool with the same arguments. How strictly arguments must match is configurable [s003].

**An LLM trajectory judge** is more flexible and can assess efficiency and appropriateness. It costs an extra LLM call, gives less deterministic results, and can optionally use a reference trajectory [s003].

This is practical vendor guidance with no empirical validation [s003].

## Strength of the evidence

- **Mostly preprints.** Four of the five distinct works are non-peer-reviewed arXiv preprints [s002][s004][s006]. The LongJudgeBench date (June 2026) is inferred from its arXiv ID [s006]. Only SAFE is peer-reviewed (NeurIPS 2024) [s005], and it predates the current generation of research agents.
- **Self-assessment.** Benchmark creators validate their own frameworks [s002], or evaluate their own models [s004].
- **Small human-validation samples.** DeepResearch Bench validated on the 50 Chinese tasks, four agents and 600 reports, which the authors themselves call modest. Expert review takes 30–60 minutes per report [s002]. SAFE's claim of beating humans rests on 100 disagreement cases judged against crowdworkers, not experts [s005]. BrowseComp's LLM grader was not validated against humans in the paper [s004].
- **Snapshot results.** Commercial agents were evaluated at a point in time [s002], and judge results are tied to specific model versions [s006].

## Gaps and open questions

- **Realistic reports.** How reliable are LLM judges on realistic, formatted, multilingual reports? The contrast between [s002] and [s006] is unresolved, and the RealDR result (0.4393) is concerning [s006].
- **Untested judge designs.** Retrieval-augmented, multi-agent and calibration-based judges have not been tested for long-form research outputs [s006].
- **Judge–reference–agent overlap.** No source controls for same-family bias when the reference, the judge and a top agent share a model family [s002].
- **Trajectory evaluation for research agents.** There is no empirical evidence here on whether process metrics predict report quality. The only trajectory source is vendor documentation [s003].
- **Recall and coverage.** How should "what the agent missed" be measured without ground truth? F1@K uses a length proxy rather than true coverage [s005], and effective-citation counts measure volume rather than completeness [s002].
- **Calibration in long-form reports.** Calibration is measured only for short answers [s004]. How to assess overconfidence in long-form reports is open.
- **Multimodal and interactive research.** Research over images, video, audio or interactive pages is flagged but not benchmarked [s004].
- **Contamination and shelf life.** Both are ongoing risks for public benchmarks that live agents can browse to [s004].

## Sources

- [s001] DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents - https://arxiv.org/abs/2506.11763
- [s002] DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents - https://arxiv.org/pdf/2506.11763
- [s003] How to evaluate your agent with trajectory evaluations - https://docs.langchain.com/langsmith/trajectory-evals
- [s004] BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents - https://arxiv.org/pdf/2504.12516
- [s005] Long-form factuality in large language models - https://neurips.cc/virtual/2024/poster/96675
- [s006] Benchmarking LLM-as-a-Judge for Long-Form Output Evaluation (LongJudgeBench) - https://arxiv.org/html/2606.01629v1
