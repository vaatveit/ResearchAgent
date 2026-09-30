# Research agent-based modeling of artificial societies. Prioritize academic papers for which the full text is available, falling back to abstracts. Reduce this to a summary of the state of the art, organized by aspects of the artificial society.

# Agent-Based Modelling of Artificial Societies: State of the Art, Organized by Aspect of the Society

## Scope and strength of the evidence

The sources fall into two groups.

- **The classical tradition.** This includes Sugarscape, the Santa Fe artificial stock market, Artificial Anasazi, evolutionary games on networks, opinion dynamics, and models of social-ecological systems and conflict. It is mature and mostly peer-reviewed. However, many of its results come from stylized simulations that were never validated against data.
- **LLM-driven societies.** This newer strand dates from 2023 onward. It is fast-moving and relies heavily on preprints. Examples include Project Sid [s028] and AgentSociety [s018]. These studies use few replicate runs and mostly qualitative validation.

Several sources were read only as abstracts or publisher blurbs. These are flagged where they matter: s001, s005, s012, s029, s057, s067, s068, s074, s075, s076, s080, s082. For s010 and s060, only the abstracts were read.

---

## 1. The paradigm: growing societies from the bottom up

**The core idea.** Collective phenomena emerge from local interactions among heterogeneous agents following simple rules. Sugarscape showed that group formation, cultural transmission, combat and trade can emerge from such rules [s001][s011][s021]. The paper specifying Sugarscape argues that bottom-up simulation is the only workable approach when the population's overall behaviour, or its causes, are unknown [s021].

**How ABMs differ from equilibrium models.** ABMs are defined in contrast to representative-agent, equilibrium models. Their agents are boundedly rational, with local and partial rationality [s020][s052]. The line between ABMs and traditional heterogeneous-agent models is becoming fuzzy [s030].

**Simple versus descriptive models.** A long-running methodological split sets Axelrod's KISS ("Keep It Simple, Stupid") against KIDS ("Keep It Descriptive, Stupid"). The survey sources say the right choice depends on the simulation's goal [s058][s067].

- Population-synthesis practice shows a drift toward data-driven KIDS models [s061].
- Janssen's replication of Artificial Anasazi pushes the other way. He argues for stylized, theory-based models rather than fitting models to material culture [s017].

**The LLM turn.** Recent work presents LLM agents as a fix for the thin cognition of rule- or equation-based agents, for example agents whose opinion is a single scalar [s018]. Surveys argue that no single traditional method supports description, explanation, prediction and scenario exploration at once:

- rule-based models describe,
- symbolic and stochastic models explain,
- machine-learning models predict but are less interpretable [s038][s048].

These are claims by LLM-ABM advocates. None of the sources tests them head-to-head against mature classical models.

---

## 2. Agents

### 2.1 Decision-making and cognition

The field uses a spectrum of agent architectures.

| Architecture | Examples | Notes |
|---|---|---|
| Simple local rules | Sugarscape greedy movement [s011][s021]; insurgency anger/fear thresholds [s084] | Transparent; can be formally analysed [s011] |
| Bounded-rational heuristics | Macro ABMs [s052]; fundamentalist/chartist switching [s030] | No agreed basis for bounded rationality [s052]; many degrees of freedom [s030] |
| Evolutionary / learning | Genetic algorithms and classifier systems in the SFI market [s002]; genetic programming (Chen & Yeh) [s002]; Q-learning [s073] | Outcomes depend on learning details (see §7) |
| Strategy-update rules in games | Imitation, logit, Fermi, richest-following [s003][s023] | The choice of rule can change qualitative outcomes, e.g. a Hopf bifurcation under logit dynamics [s003] |
| Cognitive / psychological | BDI [s058][s067][s076]; Theory of Planned Behaviour and random utility in migration models [s057]; MPPACC in climate adaptation [s077] | Uptake limited by tooling and computational cost [s058][s076] |
| LLM-based | Memory/reflection/planning [s008]; needs and emotions plus TPB [s018]; concurrent modules [s028]; perception and memory modules in EconAgent [s080] | Costly; prone to hallucination [s008][s028] |

**The critique of thin cognition.** A recurring claim is that social simulation mostly assumes rudimentary, reactive, particle-like cognition, and that this limits realism [s058][s067][s076].

- BDI is proposed because its folk-psychology concepts are easy for modellers and users to understand.
- BDI can be extended with norms and emotions [s058].
- The low uptake of BDI is attributed to missing platform support, not to fundamental flaws [s058]. BDI extensions now exist for GAMA and NetLogo [s058][s076].
- Forest social-ecological ABMs include some advanced cognitive and emotional decision-making [s029].
- Migration ABMs mostly use random utility theory or the Theory of Planned Behaviour [s057].
- Innovation-diffusion ABMs span six decision-model families: optimization, economic, cognitive, heuristic, statistical and social influence [s069].

**The counter-evidence.** Simple cognition can be enough for rich outcomes.

- In Bravo's commons model, imitation plus random exploration was sufficient for well-adapted institutions to emerge [s062].
- Social conventions emerge in minimal naming-game settings [s081].

The disagreement is less about the facts than about the modelling purpose: explaining a mechanism versus representing a specific population.

**LLM agent architectures.** These centre on planning, memory and reflection [s038][s048].

- Generative Agents score memories by relevance, recency and LLM-rated importance [s008].
  - In an ablation with 100 human evaluators, every architectural component improved believability.
  - The full architecture scored TrueSkill μ=29.89 against 21.21 for a prior-work baseline (d=8.16). It also beat crowdworker-authored behaviour (μ=22.95) [s008].
  - This measures *believability*, not predictive validity.
- AgentSociety adds six emotions rated 0–10, Maslow-style needs, and TPB-grounded attitudes [s018].
- Project Sid's PIANO architecture runs about 10 modules concurrently under a bottlenecked cognitive controller. The goal is to keep talk and action coherent [s028].

**Documented LLM failure modes:**

- Embellishing hallucinations. Generative Agents rarely fabricated knowledge outright, but 1.3% of agents' reports about their acquaintances were hallucinated [s008].
- Hallucinations that compound over successive calls and spread socially [s028].
- Lack of domain knowledge, leading to irrational decisions [s048].
- Falling short of Nash equilibrium and coordinating poorly [s038].
- Strong dependence on the base model. Only GPT-4o performed well in Project Sid [s028], and AgentSociety's results depend on DeepSeek-V3 [s018].

### 2.2 Heterogeneity and synthetic populations

Heterogeneity repeatedly turns out to drive results.

- In the SFI market, memory length is the key heterogeneity [s002].
- In fitted heterogeneous-agent market models, "virtually all studies" find that heterogeneity matters, and letting agents switch groups improves fit [s030].
- In a lab-calibrated commons model, the best fit was 75% conditional cooperators, 9% unconditional cooperators and 16% selfish agents. Heterogeneity was "key" [s049].
- Heterogeneous tolerance reduces Schelling segregation [s045].
- Heterogeneous confidence bounds change opinion outcomes [s024].

**Data use in practice is weak.** A review of 342 JASSS models from 2011–2021 found:

- 55.85% used no data to generate agent attributes,
- 62% used generic random functions,
- only about 22% used dedicated generation algorithms [s061].

**Population-synthesis methods** split into two families [s061]:

- *synthetic reconstruction*, which draws attributes from estimated distributions (e.g. iterative proportional fitting, MCMC, copulas),
- *combinatorial optimization*, which reweights or replicates real records.

Hybrids of the two are common. Synthetic populations are usually validated against the same data used to generate them. The ODD protocol alone is insufficient to document how populations are initialized [s061].

**Application examples.** Epidemic ABMs need a synthetic population, a geo-located network and a disease model. A Kolkata study showed that ward-level granularity was necessary for successful simulation [s047].

**Heterogeneity in LLM agents.** LLM agents make heterogeneity cheap through prompting, in-context learning or fine-tuning [s038][s048]. The risks are that assigned personas raised toxicity about sixfold and caricatured demographic groups [s038].

---

## 3. Environment, space and time

### Space

**Classical environments** are usually lattices:

- Sugarscape: a 50×50 torus with growback, seasons and pollution [s011][s021][s001],
- Cederman's war model: a 50×50 grid [s026],
- Johnson et al.'s overconfidence model: a 30×30 grid [s036],
- Gavrilets et al.'s chiefdom model: a hexagonal array of villages [s046],
- Bennett's insurgency model: a bounded 50×50 grid with Moore-distance-3 neighbourhoods [s084].

**Newer models use GIS and realistic data:**

- a household climate-adaptation model covering about 570,000 people [s077],
- city digital twins [s047],
- OpenStreetMap roads plus SafeGraph points of interest in AgentSociety [s018].

AgentSociety argues that realistic environments offload objective computation from the LLM and reduce hallucination. It judges text-based environments to be of questionable realism [s018]. Other LLM societies use a sandbox town [s008] or Minecraft [s028].

**Social-ecological coupling remains weak:**

- 9 of 15 environment-migration ABMs lack fully integrated two-way feedbacks. Agents rarely affect environmental drivers such as climate [s066].
- Many forest ABMs lack direct interactions and dynamic social and ecological processes [s029].

### Time and scheduling

Update scheduling is a consequential and often under-reported choice.

- Asynchronous and synchronous updating give different results. How far they diverge in complex ABMs is unknown [s021][s003].
- The original Sugarscape rules give no conflict-resolution rule, for example when two agents choose the same site [s021].
- Cederman uses quasi-parallel activation so conflicts can spread [s026].
- Johnson et al. use five synchronous phases [s036].
- Mesa 3 dropped fixed schedulers in favour of flexible activation and added experimental discrete-event time [s078].
- Project Sid criticizes turn-based execution in earlier LLM systems [s028].
- Time scales in migration ABMs range from 3 years in daily steps to 10,000 years in yearly steps [s066].

---

## 4. Social structure and networks

### Network topology and cooperation

This is a well-studied result, though mostly in stylized models.

- Scale-free networks markedly enhance cooperation compared with lattices [s003][s023]. This is attributed mainly to degree heterogeneity [s023].
- On regular structures, cooperators survive only within a window of neighbourhood sizes (4 ≤ z ≤ about 64) [s003].
- Spatial clustering helps cooperators, but "does not always" favour cooperation [s023].

### Co-evolving networks

When links and behaviour evolve together, outcomes change qualitatively.

- **Rewiring speed.** How fast links change relative to strategies matters. Fast active linking effectively turns a prisoner's dilemma into a coordination game [s023].
- **Who rewires.** Cooperation benefits when defectors switch partners often and cooperators stay loyal [s023].
- **A modelling caution.** Rules should not give cooperators better cognitive skills than defectors, or cooperation is built in [s023].
- **Learning-based analysis.** Reinforcement-learning agents adapting both actions and links yield coupled replicator equations. The analysis so far covers only 3 agents [s073].

For opinions:

- A single parameter balancing opinion adoption against rewiring produces a continuous transition from diversity to majority agreement [s005] (abstract only).
- Rewiring by opinion similarity tends to cause fragmentation rather than consensus [s064].

### Homophily and segregation

- When ties form on few features or trait values, society segregates into homogeneous communities. This happens without any change in agents' traits.
- Triadic closure with link reinforcement is essential to this effect.
- Information spreads about 2× faster in the overlapping (non-segregated) phase [s025].

Schelling-type results on networks are mixed:

- Heterogeneous topology alone does not reduce segregation. Combined with heterogeneous preferences, it does, and produces an urban–rural-like sorting [s045].
- Dense networks segregate less. Polarizing them requires much higher same-group preferences than classic tipping points suggest [s055].
- Highly visible hubs can create a "majority illusion" that tips commons users into abundant or depleted states [s059].

### LLM networks

- LLM agents reproduce, at the micro level, preferential attachment, triadic closure and homophily. At the macro level they reproduce community structure and small-world properties [s083].
- Their homophily is context-dependent: homophily in friendship settings, heterophily in organizational ones.
- A survey showed strong alignment with human link choices [s083]. These results rely mainly on GPT-family models.
- In Generative Agents, network density rose from 0.167 to 0.74 over two game days [s008].
- In Project Sid:
  - perceived likeability tracked true likeability (r=0.81 with social modules, 0.62 without),
  - extroverts gained more incoming ties [s028].

---

## 5. Culture, opinion and information

### Model families and their core results

- **Assimilative models** (DeGroot, Friedkin–Johnsen) predict consensus on any connected network [s054][s063].
- **Bounded-confidence models** (Deffuant–Weisbuch, Hegselmann–Krause) fragment into clusters when confidence is low [s004][s024][s054]. The number of clusters is roughly 1/(2ε) [s024][s054].
- **Axelrod-style cultural-trait models** preserve diversity because neighbours with nothing in common stop interacting [s004].
- **Repulsive-influence models** generate bi-polarization and opinions more extreme than any starting opinion [s004].

### Disagreement on consensus thresholds

The sources report different thresholds, and the difference is largely about setting, not a real conflict.

- Lorenz reports, for uniform initial opinions in density-based models, consensus above about ε≈0.19–0.22 for HK and about 0.27 for DW. On networks, DW reaches full consensus for ε > 0.5 [s024].
- Noorazar cites 0.5 as "the" critical radius [s054].

Other nuances from the same literature:

- Heterogeneous bounds can produce consensus even when every agent's bound is sub-critical [s024][s054]. But clusters of open-minded agents can drift toward closed-minded ones, producing extremism [s024].
- More budget-constrained issues lower the consensus threshold, while more independent issues raise it [s024].
- Adding a single binary "polarizing" feature to Axelrod's model removes its order–disorder transition in the infinite-size limit [s044].
- Sugarscape's tag-flipping culture yields spatially segregated, competing tribes [s001][s021].

### The empirical frontier

There is a strong imbalance: many theoretical studies, few empirical ones. Micro-assumptions rest largely on 1950s–60s social-psychology experiments [s004]. Recent grounding efforts include:

- experiments supporting bounded confidence [s014],
- conformity experiments that closely mirror the q-voter model [s014],
- an argument-based model calibrated at the micro level and matched to survey opinion distributions [s063],
- application of a co-evolution model to General Social Survey data [s064],
- calibrated applications to Afghan civil-war opinions and climate negotiations [s004].

### Feeds, personalization and LLM opinion models

Algorithmic feeds are an emerging target [s004][s014]. LLM agents let models handle opinions as text rather than scalars [s014][s082].

- An LLM echo-chamber simulation reproduced polarization relative to bounded-confidence and Friedkin–Johnsen baselines. Active and passive nudges reduced echo chambers [s082] (abstract only).
- In AgentSociety [s018]:
  - homophilic exposure made 52% of agents more polarized,
  - node-level moderation (suspending accounts) beat edge-level moderation (removing ties).
- LLM agents reproduce filter bubbles and echo human content biases [s038].

### Information and cultural diffusion

- In Generative Agents, awareness of a party spread from 1 to 13 of 25 agents without user intervention [s008].
- In a single 500-agent Project Sid run [s028]:
  - meme propagation needed a threshold of density and social interaction,
  - a seeded religion spread steadily,
  - conversion was measured by keyword proxies.

### Conventions in LLM populations

Universal conventions emerge in LLM populations through a naming game [s081].

- Collective bias arises even when individual agents are unbiased.
- A committed minority can overturn an established convention. The critical mass ranges from 2% to 67% depending on the model, against about 25% in human experiments.
- The authors explicitly decline to treat LLMs as human proxies [s081].

---

## 6. Cooperation, norms, institutions and governance

### Evolutionary-game tradition

- This tradition uses statistical-physics tools: mean-field, pair approximation and Monte Carlo methods [s003][s013].
- It studies incentives such as peer and pool punishment and rewards, with the public goods game as the null model [s013].
- Beyond links, other traits can co-evolve with strategies: reputation, mobility, age, teaching activity and noise.
- Examples from this work:
  - success-driven migration robustly promotes cooperation,
  - fast mobility approximates well-mixed conditions and hurts cooperators [s023].
- A gap: coevolution has rarely been applied to public goods, ultimatum or punishment games [s023].

### Commons and institutions

- In Bravo's model, institutions encoded in the ADICO grammar emerge and improve both the resource stock and agent welfare. Making institutions harder to change worsens outcomes, consistent with Ostrom's collective-choice principle [s062].
- A lab-calibrated model found that inequality, trust and communication must all enter decisions to reproduce observed patterns. Communication works by raising trust [s049].
- Ghorbani's institutional modelling recommends:
  - representing rules, norms and shared strategies as entities separate from agents,
  - using Institutional Grammar coding of legal and ethnographic data,
  - allowing institutions to be dynamic and emergent [s071].
- Participatory "companion" models are used as role-playing tools with stakeholders [s068] (abstract only).

### Disagreement on how to represent governance

- In practice, social-ecological ABMs mostly represent governance as a *variable*. Governance is dominated by state intervention and neoclassical foundations, with community- and market-based modes rare [s019].
- The same review recommends representing governance as an *agent* [s019]. This is consistent with the institutional-modelling position [s071].
- Forest ABM reviewers call for adaptive governance and feedback loops [s029].

### LLM institutions

- In Project Sid, agents followed a pre-seeded tax constitution and amended it democratically. Influencers shifted tax paid from 20% to about 9%, with no enforcement agents [s028].
- The same authors state that LLM agents cannot show *de novo* emergence of institutions such as democracy or fiat money [s028].
- This contrasts with emergent conventions in LLM populations [s081] and with institutional emergence in simple classical agents [s062][s071].
- The tension turns on what counts as "emergence". Selecting among or amending pre-specified rules is different from inventing institutional forms.

---

## 7. Economy and markets

### Sugarscape

- A second resource plus bilateral trade yields an emergent market. Trade uses a marginal-rate-of-substitution geometric-mean price [s001][s021].
- Resource accumulation always produces a wealth distribution. That distribution is provably independent of initial conditions in the ergodic basic model [s011].
- Credit and inheritance rules exist, but are ambiguously specified [s021].

### Artificial stock markets

- The SFI market reproduces fat tails, weak autocorrelation, volatility persistence and the volume–volatility correlation. It is "qualitatively right" but under-shoots volatility and kurtosis quantitatively [s002].
- Fast learning produces realistic dynamics and trend-following. Slow learning converges to the rational-expectations equilibrium [s002].

**Disputed: does technical trading really emerge?** The original mutation operator was biased upward.

- Ehrentreich shows that an alternative mutation operator shows no technical trading at the aggregate bit level. However, two other tests still establish that it exists. Genetic drift is an important force, and weak selection can reconcile technical trading with market efficiency [s012] (abstract only).
- LeBaron's review reads the result as overturning the dominance of technical trading. He suggests convergence to rational expectations may hold broadly, and that drift rather than selection dominates [s022].

Other points from the market literature:

- Many market ABMs ignore long-run wealth dynamics [s022].
- Heterogeneous-agent models with fundamentalists and chartists are the estimable workhorse [s030].
- In the Brock–Hommes model, trend and bias parameters matter most for fitting S&P 500 returns [s040].

### Macroeconomic ABMs

- An emerging common core spans the EURACE, Keynes-meets-Schumpeter, JAMEL, LAGOM and other model families [s052].
- These models jointly reproduce time-series and distributional stylized facts. They generate crises endogenously through feedback and path dependence [s052].
- An endogenous-growth model needs exploration–exploitation balance and threshold levels of opportunity and diffusion [s040].

### LLM economies

- EconAgent reports more realistic decisions and macro phenomena than rule-based or learning agents [s080] (abstract only).
- A survey reports that only LLM agents reproduced the Phillips curve and Okun's law in one hybrid macro simulation [s038].
  - This compares against that paper's own baselines, not against mature macro ABMs, which already claim to reproduce stylized facts [s052].
- LLM duopolists collude when they can communicate and approach Bertrand prices when they cannot [s038].
- AgentSociety's universal-basic-income experiment qualitatively matched the Texas UBI results: consumption rose and depression fell. However, its labour and goods markets are simplified [s018].

---

## 8. Conflict, polity formation and politics

### Interstate war and state formation (Cederman)

- About 200 state agents on a grid generate the power-law distribution of war sizes: median R² 0.991, median slope −0.55. Empirical slopes are −0.41 to −0.57.
- Ablations show both technological change and contextual activation are necessary.
- Calibration required tuning, so the parameter-insensitivity expected of self-organized criticality was not fully met [s026].

### Overconfidence (Johnson et al.)

- Overconfidence becomes the predominant strategy through two mechanisms: a "lottery effect" and spontaneous offensive alliances.
- The advantage is limited by war costs [s036].

### Early complex societies

- Gavrilets et al.: chiefdoms cycle stochastically, growing and then collapsing quickly, even without environmental shocks. Stability depends on how deterministic conflict is and on succession rules [s046].
- A circumscription model finds *social* circumscription is the largest driver of hierarchy formation, while environmental circumscription has mixed effects [s056].

### Insurgency and party competition

- Avoiding collateral damage matters more than capturing insurgents. There may be a tipping point in accuracy [s084].
- Satisficing parties outperform relentless vote-maximizers [s074] (publisher blurb only).

**Evidence strength.** All of these models are stylized. Validation consists of matching a distribution or qualitative archaeological patterns. LLM equivalents such as WarAgent exist but are only mentioned in surveys [s038].

---

## 9. Demography, migration, epidemics and disasters

**Sugarscape demography.** Sexual reproduction can crash the population or cause overshoot collapse [s001]. The formal specification notes that the book's rule text omits the parents' resource gift to offspring, which has "a huge effect" on mating [s021].

**Artificial Anasazi.** A cautionary tale.

- The model's fit to history comes mainly from two carrying-capacity parameters. The model acts as a smoothing function, and agent behaviour adds little.
- Social ties are missing [s017].

**Migration.**

- Decision theory and social networks are the critical design choices, and validation evidence is hard to select [s057] (abstract only).
- Flee 3 forecasts over 70% of refugee arrivals across ten conflicts and runs Ukraine 2022 in under an hour on 512 cores [s075] (abstract only).
- A climate-adaptation household model finds that mixed herding–farming strategies survive best. It passes only face-validity tests [s077].

**Epidemics.** A Kolkata COVID model found that prolonged lockdowns were ineffective, weekend lockdowns effective, and compliance mattered [s047]. These are unverifiable counterfactuals. Sugarscape encodes disease and immunity as bit-strings [s021].

**Disasters.** AgentSociety's Hurricane Dorian run reproduced the fall and recovery in mobility, with small deviations at the peak [s018].

---

## 10. Methodology: specification, analysis, validation and tooling

### Specification and replication

- ODD is the accepted documentation standard. It still often lacks enough detail for reimplementation, and its 2020 update added sections on rationale and evaluation [s010].
- Replication keeps exposing gaps:
  - Sugarscape's rules suffer from lack of clarity, missing information and sequential biases [s021],
  - the Anasazi code and paper disagree on the time step [s017],
  - the SFI market's complexity deterred replication [s022].

### Formal analysis

Formal analysis is possible but rare.

- The basic Sugarscape model is a provably ergodic Markov chain, so one long run suffices to estimate its long-run behaviour [s011].
- By contrast, SFI results were averaged over 25 runs because ergodicity could not be proven [s002].

### Sensitivity analysis

- No single method gives a complete picture. Extended one-factor-at-a-time analysis is a cheap start that reveals tipping points, but it should be supplemented with global methods [s050].
- The choice of method should follow the model's purpose [s060].
- Machine-learning surrogates (XGBoost with active learning) cut calibration cost 500–3750× on small models [s040].

### Validation

- There is no consensus [s020]. Recognized approaches include indirect calibration, the Werker–Brenner approach and "history-friendly" modelling [s020], along with reduced-form or simulated-moments estimation [s030].
- Actual practice lags:
  - only 11 of 29 social-ecological ABMs compared output with data, and none made a strong case for realism [s009],
  - innovation-diffusion validation is "often informal, incomplete, and even missing" [s069].
- Recommended remedies:
  - validating at both micro and macro level,
  - forward validation on held-out future data,
  - maximum-likelihood calibration [s069],
  - participatory approaches [s009].
- LLM-ABM evaluation distinguishes micro-level behaviour prediction from macro-level regularities, but benchmarks for simulation fidelity are lacking [s038].

### Tooling and scale

- **Classical platforms.** NetLogo is accessible but limited to small models. MASON is faster. Mesa 3 offers Python, flexible activation, many space types and seeded reproducibility [s078].
- **LLM costs.** 25 agents over two game days cost thousands of dollars [s008].
- **LLM bottlenecks.**
  - AgentSociety reaches over 10,000 agents and about 5 million interactions, with LLM API latency as the bottleneck [s018].
  - Project Sid's 1,000+-agent runs exceeded server limits [s028].
  - Batch prompting gives up to 5× efficiency [s038].
- **Parallelism.** Sugarscape is proposed as a parallel-computing benchmark, because GPU work tends to skip the hard rules: combat, trade and inheritance [s021].

---

## Gaps and open questions

- **Validation is the dominant gap across every aspect** [s004][s009][s020][s069]. This applies to classical models and even more to LLM societies, where evidence rests on believability ratings, a few case studies and small numbers of runs [s008][s018][s028].
- **LLM agents as human proxies.** Alignment in network formation [s083] contrasts with caricature, toxicity and non-Nash play [s038]. Whether LLM societies can produce genuinely novel institutions is contested [s028][s081].
- **Mechanism versus input.** Anasazi [s017] and the SFI mutation-operator debate [s012][s022] show that headline results can come from environmental inputs or learning-operator artefacts. Robustness across implementation choices is rarely tested.
- **Scheduling and concurrency.** The effects of update order and conflict resolution in complex models remain unquantified [s021].
- **Integration across aspects.** Only a minority of models couple social and ecological processes both ways [s066][s019]. Few combine economy, culture, conflict and demography. Integrating competing opinion models remains open [s004].
- **Coverage gaps within single aspects:**
  - behaviour under non-uniform initial opinion profiles [s024],
  - coevolution in public-goods and punishment games [s023],
  - long-run wealth dynamics in markets [s022],
  - data for abstract agent attributes such as attitudes [s061].
- **Scale and cost.** Scale and cost still bound LLM societies [s008][s018][s028], and cheap, rigorous calibration of large classical ABMs is also unsolved [s040].

## Sources

- [s001] Growing Artificial Societies: Social Science From the Bottom Up - https://www.brookings.edu/books/growing-artificial-societies/
- [s002] Building the Santa Fe Artificial Stock Market - https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/blake.sfisum.pdf
- [s003] Evolutionary games on graphs - https://arxiv.org/pdf/cond-mat/0607344
- [s004] Models of Social Influence: Towards the Next Frontiers - https://www.jasss.org/20/4/2/2.pdf
- [s005] Models of opinion formation combining network adaptation and opinion adoption (arXiv physics/0603023) - https://arxiv.org/abs/physics/0603023
- [s008] Generative Agents: Interactive Simulacra of Human Behavior - https://arxiv.org/pdf/2304.03442
- [s009] Agent-Based Modelling of Social-Ecological Systems: Achievements, Challenges, and a Way Forward - https://www.jasss.org/20/2/8.html
- [s010] The ODD Protocol for Describing Agent-Based and Other Simulation Models: A Second Update to Improve Clarity, Replication, and Structural Realism - https://www.jasss.org/23/2/7.html
- [s011] Epstein and Axtell's Sugarscape (Appendix B to Izquierdo et al., JASSS 12(1)6) - https://jasss.soc.surrey.ac.uk/12/1/6/appendixB/EpsteinAxtell1996.html
- [s012] Technical trading in the Santa Fe Institute Artificial Stock Market revisited - https://www.sciencedirect.com/science/article/abs/pii/S0167268106001545
- [s013] Statistical physics of human cooperation - https://arxiv.org/pdf/1705.07161
- [s014] Opinion dynamics: Statistical physics and beyond - https://arxiv.org/pdf/2507.11521
- [s017] Understanding Artificial Anasazi - https://jasss.soc.surrey.ac.uk/12/4/13.html
- [s018] AgentSociety: Large-Scale Simulation of LLM-Driven Generative Agents Advances Understanding of Human Behaviors and Society - https://arxiv.org/pdf/2502.08691
- [s019] Governance in social-ecological agent-based models: a review - https://www.ecologyandsociety.org/vol26/iss2/art38/
- [s020] Empirical Validation of Agent-Based Models: Alternatives and Prospects - https://jasss.soc.surrey.ac.uk/10/2/8.html
- [s021] The Specification of Sugarscape - https://arxiv.org/pdf/1505.06012
- [s022] Review of Ehrentreich: Agent-Based Modeling: the Santa Fe Institute Artificial Stock Market Model Revisited - https://jasss.soc.surrey.ac.uk/12/2/reviews/lebaron.html
- [s023] Coevolutionary games – a mini review - https://arxiv.org/pdf/0910.0826
- [s024] Continuous Opinion Dynamics under Bounded Confidence: A Survey - https://arxiv.org/pdf/0707.1762
- [s025] Structural transition in social networks: The role of homophily - https://arxiv.org/pdf/1808.05035
- [s026] Modeling the Size of Wars: From Billiard Balls to Sandpiles - https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/LarsErikCederman.ModelingSizeOfWars.pdf
- [s028] Project Sid: Many-agent simulations toward AI civilization - https://arxiv.org/pdf/2411.00114
- [s029] Modelling forests as social-ecological systems: A systematic comparison of agent-based approaches - https://www.sciencedirect.com/science/article/pii/S1364815224000598
- [s030] Empirical Validation of Agent-Based Models (Chapter 8, Handbook of Computational Economics vol. 4) - https://www.sciencedirect.com/science/article/pii/S1574002118300030
- [s036] Fortune Favours the Bold: An Agent-Based Model Reveals Adaptive Advantages of Overconfidence in War - https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0020851
- [s038] Large Language Models Empowered Agent-based Modeling and Simulation: A Survey and Perspectives - https://arxiv.org/pdf/2312.11970
- [s040] Agent-Based Model Calibration using Machine Learning Surrogates - https://arxiv.org/pdf/1703.10639
- [s044] Polarization inhibits the phase transition of Axelrod's model - https://arxiv.org/pdf/2102.06921
- [s045] Behavioral and Topological Heterogeneities in Network Versions of Schelling's Segregation Model - https://arxiv.org/pdf/2408.05623
- [s046] Cycling in the Complexity of Early Societies - https://www.sociostudies.org/almanac/articles/cycling_in_the_complexity_of_early_societies/
- [s047] City-Scale Simulation of COVID-19 Pandemic & Intervention Policies using Agent-Based Modelling - https://arxiv.org/pdf/2104.01650
- [s048] Large language models empowered agent-based modeling and simulation: a survey and perspectives - https://www.nature.com/articles/s41599-024-03611-3
- [s049] An Agent-Based Model of the Interaction Between Inequality, Trust, and Communication in Common Pool Experiments - https://www.jasss.org/25/4/3.html
- [s050] Which Sensitivity Analysis Method Should I Use for My Agent-Based Model? - https://www.jasss.org/19/1/5.html
- [s052] Agent-Based Macroeconomics - https://d-nb.info/1151638439/34
- [s054] Recent advances in opinion propagation dynamics: A 2020 Survey - https://arxiv.org/pdf/2004.05286
- [s055] Schelling segregation dynamics in densely-connected social network graphs - https://arxiv.org/pdf/2504.16307
- [s056] A formal test using agent-based models of the circumscription theory for the evolution of social complexity - https://www.alexmesoudi.com/publication/williams-formal-2024/Williams_Mesoudi_JAS_2024.pdf
- [s057] Decision-Making in Agent-Based Models of Migration: State of the Art and Challenges - https://link.springer.com/article/10.1007/s10680-015-9362-0
- [s058] BDI agents in social simulations: a survey - http://rr.liglab.fr/research_report/RR-LIG-050_orig.pdf
- [s059] Majority illusion drives the spontaneous emergence of alternative states in common-pool resource games with network-based information - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12226385/
- [s060] 'One Size Does Not Fit All': A Roadmap of Purpose-Driven Mixed-Method Pathways for Sensitivity Analysis of Agent-Based Models - https://jasss.soc.surrey.ac.uk/23/1/6.html
- [s061] Generation of Synthetic Populations in Social Simulations: A Review of Methods and Practices - https://www.jasss.org/25/2/6/6.pdf
- [s062] Managing the commons: a simple model of the emergence of institutions through collective action - https://thecommonsjournal.org/articles/10.18352/ijc.606
- [s063] Validating argument-based opinion dynamics with survey experiments - https://arxiv.org/pdf/2212.10143
- [s064] Co-evolving networks for opinion and social dynamics in agent-based models - https://arxiv.org/pdf/2407.00145
- [s066] Agent-based modeling of environment-migration linkages: a review - https://www.ecologyandsociety.org/vol23/iss2/art41/
- [s067] BDI agents in social simulations: a survey - https://www.cambridge.org/core/journals/knowledge-engineering-review/article/abs/bdi-agents-in-social-simulations-a-survey/ADBACF4B23F625D42A7DB45E0D7556C4
- [s068] An agent-based model to support community forest management and non-timber forest product harvesting in northern Thailand - https://sesmo.org/article/view/17894
- [s069] Empirically Grounded Agent-Based Models of Innovation Diffusion: A Critical Review - https://arxiv.org/pdf/1608.08517
- [s071] Institutional modelling: Adding social backbone to agent-based models - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9372633/
- [s073] Replicator Dynamics of Co-Evolving Networks - https://arxiv.org/pdf/1107.5354
- [s074] Party Competition: An Agent-Based Model - https://press.princeton.edu/books/paperback/9780691139043/party-competition
- [s075] Flee 3: Flexible agent-based simulation for forced migration - https://www.sciencedirect.com/science/article/pii/S1877750324001649
- [s076] A Simple-to-Use BDI Architecture for Agent-Based Modeling and Simulation - https://link.springer.com/chapter/10.1007/978-3-319-47253-9_2
- [s077] An Agent-Based Model of Rural Households' Adaptation to Climate Change - https://jasss.soc.surrey.ac.uk/21/4/4.html
- [s078] Mesa 3: Agent-based modeling with Python in 2025 - https://www.theoj.org/joss-papers/joss.07668/10.21105.joss.07668.pdf
- [s080] EconAgent: Large Language Model-Empowered Agents for Simulating Macroeconomic Activities - https://aclanthology.org/2024.acl-long.829/
- [s081] Emergent Social Conventions and Collective Bias in LLM Populations - https://arxiv.org/pdf/2410.08948
- [s082] Decoding Echo Chambers: LLM-Powered Simulations Revealing Polarization in Social Networks - https://aclanthology.org/2025.coling-main.264/
- [s083] Network formation and dynamics among multi-LLMs - https://academic.oup.com/pnasnexus/article/4/12/pgaf317/8361967
- [s084] Governments, Civilians, and the Evolution of Insurgency: Modeling the Early Dynamics of Insurgencies - https://www.jasss.org/11/4/7.html
