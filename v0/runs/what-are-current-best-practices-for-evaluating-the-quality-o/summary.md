# What are current best practices for evaluating the quality of LLM-based research agents?

# Evaluating LLM-Based Research Agents: Current Best Practices

## Bottom line

No single benchmark or metric is adequate for evaluating research agents. The sources converge on five practices:

- **Decompose quality** into separately graded dimensions: factual grounding, citation validity, coverage, synthesis/reasoning, and source quality.
- **Verify claims against the actual cited sources.** Surface signals such as working links or citation counts are not enough.
- **Use LLM judges with expert-written rubrics**, and calibrate them against human experts.
- **Account for non-determinism and robustness**, not just single-run accuracy.
- **Treat evals as buggy software.** Read transcripts, isolate trials, and supplement offline evals with production signals.

The evidence base is young. Most sources are 2025–2026 preprints, often by benchmark authors or evaluation vendors, and several were read only at the abstract level.

---

## 1. Why research agents are hard to evaluate

Research outputs are long, open-ended, and admit many valid answers. They also often depend on dynamic information, so short-answer QA benchmarks don't capture them [s006].

- **Quality is task-relative.** What counts as "comprehensive," "well-sourced," or even "correct" depends on context. Experts may disagree, and ground truth shifts as reference content changes [s003].
- **Binary judgments fail.** Long-form generations mix supported and unsupported information, so binary correctness judgments are inadequate [s002].
- **Human evaluation is costly.** It is labor-intensive [s001][s002], which motivates automated methods validated against human judgment [s001][s002].

## 2. Decompose quality into multiple graded dimensions

All the high-relevance sources recommend multi-dimensional evaluation over a single score, though they slice the dimensions differently.

- **Anthropic's practitioner guidance [s003]** recommends combining grader types:
  - groundedness checks, meaning claims are supported by retrieved sources;
  - coverage checks, meaning key facts a good answer must include;
  - source-quality checks, meaning consulted sources are authoritative;
  - exact match where answers are objective;
  - LLM checks for synthesis.
- **DeepResearch Bench [s001]** separates report quality, assessed with a reference-based method using adaptive criteria, from retrieval ability, measured by effective citation count and citation accuracy.
- **ResearchRubrics [s006]** scores six dimensions: Explicit Requirements, Implicit Reasoning, Synthesis of Information, References, Communication Quality, and Instruction Following. It also separates mandatory from optional criteria.
- **TRACE [s007]** adds process dimensions (efficiency and "cognitive quality," including evidence grounding) alongside accuracy. It reports that multi-dimensional ranking reveals accuracy/efficiency/robustness trade-offs that single metrics miss.

**Evidence strength:** There is broad agreement on the principle. However, there is no shared taxonomy of dimensions, and the trade-off claims in [s007] are self-reported from an abstract.

## 3. Verify factuality and citations at the claim level

### Atomic-fact scoring

FActScore breaks output into atomic facts and reports the percentage supported by a reliable knowledge source [s002].

- Its automated estimator, built on retrieval plus a strong LM, reportedly tracks human scores with under 2% error.
- It was applied to 6,500 generations that would have cost about $26K to evaluate by hand [s002].
- It is a peer-reviewed building block, but it was developed on biography generation, not research agents. It also measures precision only, not coverage [s002].

### "Closing the loop" on citations

A 2026 preprint parses inline citations from Markdown reports, retrieves the cited content, and judges each citation on three dimensions: Link Works, Relevant Content, and Fact Check [s005]. Its central finding is that **surface citation quality masks factual failure**:

| Metric (frontier models) | Result [s005] |
|---|---|
| Link validity | above 94% |
| Relevance | above 80% |
| Factual accuracy | only 39–77% |

Fact Check was therefore the most discriminating dimension [s005]. The paper also cites prior work documenting citation hallucination rates of 11–57% in deployed models [s005].

### Citation counts are a poor proxy, which creates tension with [s001]

[s005] finds that providers generating more citations achieve lower factual accuracy. It argues that citation counts and task success are poor proxies for quality. This sits uneasily with DeepResearch Bench's use of "effective citation count" as a retrieval metric [s001].

The two are not necessarily contradictory, because "effective" may already filter for valid citations. Still, [s005] suggests any count-based metric should be paired with per-citation fact-checking.

### Other practices from [s005]

- **Depth ablations.** Increasing tool calls from 2 to 150 degraded factual accuracy while link and relevance scores stayed above 92%. GPT-5.4 fell from 79% to 17%, and Claude Opus 4.6 fell from 80% to 58%.
- **Report task success rates.** Fewer than half of open-source models produced cited reports one-shot; Pixtral Large succeeded only 16.7% of the time.
- **Error-analyze link failures by type**, such as 404s, paywalls or bot blocking, and timeouts.

**Evidence strength:** Moderate. [s005] is an unreviewed v1 preprint with apparently small samples (about 30 queries per model). Its explanation for the depth effect is a hypothesis.

## 4. Rubrics and LLM-as-judge: design and calibration

### Calibrate judges against human experts

This is the most consistent recommendation across sources [s003][s005][s006]. [s006] offers the most concrete validation data, measuring Macro F1 against 9 expert annotators on 303 responses:

- Binary grading reached 0.72–0.76 agreement.
- Gemini-2.5-Pro was the most reliable judge.
- A gap to human–human agreement remained.

### Specific judge practices from [s003]

- Grade each rubric dimension with an isolated judge rather than one judge for everything.
- Allow an "Unknown" escape option.
- Calibrate frequently.

### Rubric authorship: expert-written vs LLM-generated

[s006] criticizes benchmarks that use LLM-generated rubrics or LLM-generated reference reports as circular and lightly overseen. Its ablation supports the criticism:

- LLM-augmented or rephrased rubrics degraded human–LLM alignment by 15–20%.
- Adding concrete examples to criteria improved alignment by 3–4% under binary grading [s006].

DeepResearch Bench, by contrast, relies on a reference-based method with adaptive criteria and claims alignment with human judgment [s001]. From the abstract alone it is unclear how its references and criteria are produced. Whether it falls under [s006]'s critique cannot be determined here. Note also that [s006] comes from Scale AI, a vendor of expert data services, which has an interest in the "expert curation is irreplaceable" conclusion.

### Partial credit: a genuine tension

- [s003] recommends partial credit for multi-component tasks.
- [s006] found that ternary grading (with a partial verdict) dropped judge–human agreement to about 0.53–0.57. That is roughly 20 points below binary grading, so [s006] collapses partial verdicts to "not satisfied."

These can be reconciled. Partial credit can be awarded across many fine-grained binary criteria, rather than as a "partial" verdict within a single criterion. This reading is an inference, not something either source states.

### Known judge biases

- **Length.** Response length correlates moderately with score (r ≈ 0.24–0.28) [s006].
- **Position and self-enhancement.** These biases may persist despite human calibration [s005].

### Task design

[s003] advises that tasks be unambiguous, such that two experts would independently reach the same verdict. It also notes that a 0% pass rate usually signals a broken task. This standard is hard to meet for open-ended research, where [s003] itself acknowledges experts may disagree.

## 5. Outcome vs process evaluation

Sources partly disagree here.

- **[s003] favors outcomes.** It advises grading what the agent produced rather than the path it took.
- **[s007] favors trajectories.** It argues that outcome-only metrics like Pass@1 create a "high-score illusion" that ignores reasoning quality, efficiency, and soundness. It proposes whole-trajectory evaluation through a Hierarchical Trajectory Utility Function.
- **[s007] also measures latent capability** through a "Scaffolded Capability Assessment," defined as the minimum guidance needed for success.

The positions are compatible if process metrics measure properties such as efficiency and grounding rather than penalizing deviation from a prescribed path. [s005]'s depth ablation shows why process matters: more search can actively hurt accuracy [s005]. TRACE's claims, however, are unverified beyond its abstract.

## 6. Short-answer vs long-form benchmarks

BrowseComp takes the verifiable-answer route. Its 1,266 questions require persistent navigation for hard-to-find information, with short answers easily checked against references [s004]. Its authors call it "incomplete but useful." It deliberately sidesteps long answers, ambiguity resolution, and realistic query distributions [s004].

This matches [s006]'s view that short-answer benchmarks don't capture deep research. It also fits [s003]'s advice to use exact match only where answers are objective. The best practice is to use such benchmarks for search persistence, alongside long-form rubric evaluation.

## 7. Non-determinism and robustness

- **Report both pass@k and pass^k** [s003]. Use pass@k when one success suffices, and pass^k when consistency is essential.
- **Measure robustness directly.** [s007] argues that static benchmarks fail to quantify robustness and latent capability.
- **Run ablations over agent settings**, such as search depth, to expose robustness differences [s005].

## 8. Eval hygiene

Practitioner guidance from [s003] stresses that graders and harnesses are error-prone.

- **Grader bugs can dominate results.** On CORE-Bench, Opus 4.5 went from 42% to 95% after grader bugs were fixed and the scaffold was loosened [s003].
- **Isolate trials.** Shared state let an agent inspect git history from previous trials [s003].
- **Read transcripts** before trusting scores [s003].
- **Build balanced sets** that test when a behavior should and shouldn't occur, such as searching vs. answering from knowledge [s003].
- **Start small.** Begin with 20–50 tasks drawn from real failures [s003].
- **Watch for saturation.** A 100% eval tracks regressions but provides no improvement signal [s003].
- **Open-source benchmarks and components** for reproducibility, as done in [s001] and aimed for by [s005]'s parser framework.

## 9. Beyond offline benchmarks

Offline evals should be complemented by production monitoring, A/B tests, user feedback, manual transcript review, and systematic human evaluation. They should be maintained as living artifacts with clear owners [s003]. This is practitioner experience rather than empirically tested guidance.

---

## Gaps and open questions

- **Coverage/recall measurement.** Factuality metrics measure precision [s002][s005]. Coverage relies on expert-defined key facts or rubrics [s003][s006], which are expensive and not validated at scale.
- **Shifting ground truth.** Several sources name dynamic information and link rot as problems [s003][s005][s006], but none offers a solution for keeping benchmarks valid over time.
- **Judge reliability ceiling.** Best judge–human agreement (about 0.72–0.76 Macro F1) still trails human–human agreement [s006]. The effect of length, position, and self-enhancement biases on rankings is not well quantified [s005][s006].
- **Reference-based vs rubric-based evaluation.** No source directly compares DeepResearch Bench-style reference methods [s001] with expert-rubric methods [s006] on the same outputs.
- **Validity of process metrics.** Whether trajectory metrics [s007] predict user-valued outcomes is unshown in the material reviewed.
- **Small, vendor-authored samples.** Examples include 101 prompts and three agents in [s006], about 30 queries per model in [s005], and several abstract-only readings [s001][s004][s007]. Independent replication is lacking.
- **Naming ambiguity.** [s007] describes an accompanying "DeepResearch-Bench." It is unclear whether this is the same benchmark as [s001] or a distinct one.
- **Cost and efficiency reporting.** Efficiency appears as a dimension in [s007], but no source proposes standard reporting of cost or latency alongside quality.

## Sources

- [s001] DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents - https://arxiv.org/abs/2506.11763
- [s002] FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation - https://arxiv.org/abs/2305.14251
- [s003] Demystifying evals for AI agents - https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- [s004] BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents - https://arxiv.org/abs/2504.12516
- [s005] Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents - https://arxiv.org/html/2605.06635v1
- [s006] ResearchRubrics: A Benchmark of Prompts and Rubrics For Evaluating Deep Research Agents - https://arxiv.org/pdf/2511.07685
- [s007] TRACE: Trajectory-Aware Comprehensive Evaluation for Deep Research Agents - https://arxiv.org/abs/2602.21230
