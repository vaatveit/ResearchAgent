# Research agent-based modeling of artificial societies. Prioritize academic papers for which the full text is available, falling back to abstracts. Reduce this to a summary of the state of the art, organized by aspects of the artificial society.

# Agent-Based Modeling of Artificial Societies: State of the Art by Societal Aspect

## Scope and evidence base

The sources fall into two groups. The first is a classical agent-based modeling (ABM) tradition, running from Sugarscape in the 1990s through statistical-physics and computational-social-science work in the 2000s–2010s. The second is a fast-growing wave, from 2023 to 2025, of societies built from large language model (LLM) agents.

Most of the classical material is peer-reviewed and was read in full. The core conceptual sources are JASSS reviews, Physics Reports reviews, and PLOS ONE papers [s003][s004][s020][s053].

The LLM material is weaker as evidence:
- Its flagship platform papers are preprints evaluated by their own authors [s018][s028].
- Several sources are abstract-only: s001, s005, s012, s029, s057, s067, s068, s074, s075, s076, s080 and s082. Claims from these should be treated as the authors' own summaries.

---

## 1. The generative paradigm and its critics

**The core claim.** Artificial societies are "grown" from the bottom up. Heterogeneous, autonomous agents follow simple local rules, and macro regularities emerge from their interaction [s001][s041][s078].

- **Sugarscape as the canonical case.** Agents with vision, metabolism and other genetic attributes live on a resource landscape. From simple rules they produce wealth distributions, migration, culturally distinct "tribes", combat, population crashes and emergent markets [s001][s011].
- **Bottom-up versus top-down.** ABMs are often defined against representative-agent, equilibrium models. Aggregates "emerge out of repeated interactions" rather than from rationality constraints imposed by the modeller [s020][s042].

**The critique.** The paradigm has been contested from within.
- Conte argues that generative explanation needs a prior theory of causes; otherwise the model is ad hoc or "mere reproduction" [s041].
- Epstein treats "emergence" as a useless notion. Conte defends it and adds second-order emergence and "immergence" (downward causation). She notes that Epstein applies generativism only to bottom-up processes and omits learning [s041].
- Institutional modelling proposes top-down institutional structures as an explicit "social backbone" alongside bottom-up behaviour [s071]. This is effectively a response to that critique.

**Simplicity versus description.** A related debate sets KISS ("Keep It Simple, Stupid") against KIDS ("Keep It Descriptive, Stupid"). The right choice is usually said to depend on purpose [s058][s067][s042]. The data show a gradual drift toward data-driven, descriptive models [s061][s069].

---

## 2. Agents: cognition, decision-making and learning

### Classical agents

**Bounded rationality is the default.** Agents use myopic, local heuristics and rules of thumb [s020][s042][s052]. Critics note that there is no common basis for which deviations from rationality to assume, which leaves the modeller many degrees of freedom [s030][s052].

**Reactive agents still dominate.** Surveys agree that most social simulations use "simple reactive particle-like agents", which is inadequate for many social-science questions [s058][s067][s076].
- BDI (belief–desire–intention) architectures are the main proposed upgrade. They are grounded in folk psychology and extensible with norms and emotions [s058][s067].
- Uptake has been low. The authors attribute this mainly to missing platform support, not conceptual flaws [s058]. BDI extensions now exist for GAMA and NetLogo [s058][s076].

**Domain models borrow psychological theory.**
- Migration ABMs mostly use random utility or discrete choice, or the Theory of Planned Behaviour [s057].
- Climate-adaptation models use frameworks such as MPPACC [s077].
- Some forest social-ecological models include cognitive and emotional decision-making [s029].
- Yet many social-ecological models lack explicit theory for actor decision-making [s019].

**Learning.**
- The Santa Fe Institute (SFI) artificial stock market used evolving classifier rules (a genetic algorithm, GA). Outcomes depended strongly on learning speed: fast updating gave realistic dynamics, while slow updating converged to rational expectations [s002][s070].
- Coevolutionary game models add reinforcement-learning agents that adapt both actions and links. These give coupled replicator dynamics, but have only been analysed for tiny systems [s073].

**Heterogeneity matters empirically.**
- A common-pool-resource ABM calibrated to lab data fits best with a mix of agent types: 75% conditional cooperators, 9% unconditional cooperators and 16% selfish [s049].
- In financial heterogeneous-agent models (HAMs), virtually all estimation studies support agent heterogeneity and switching between groups [s030].

### LLM-based ("generative") agents

**Architectures.** The now-standard pattern is memory stream, reflection and planning [s008][s038][s048][s079].
- Generative Agents scores memories by recency, relevance and importance.
- In an ablation with 100 human evaluators, every component improved believability. The full architecture scored TrueSkill μ=29.89 against 21.21 for a prior-work baseline, and it even beat crowdworker-authored behaviour (22.95) [s008].
- Later systems add richer mental state:
  - AgentSociety adds six emotions, Maslow-style needs and Theory-of-Planned-Behaviour attitudes [s018].
  - Project Sid runs about ten concurrent modules coordinated by a "cognitive controller" so that talk and action stay coherent [s028].

**Disagreement on heterogeneity.** The sources conflict on whether LLM agents can represent human diversity.
- **For:** proponents argue that prompting, in-context learning or fine-tuning make heterogeneity cheap and rich [s038][s048][s080].
- **Against:** a 2025–26 position paper reports convergence on an "average persona" with WEIRD bias and mode collapse, while persona prompting can instead produce caricature [s079]. The earlier survey itself notes a 6× rise in toxicity under some personas and caricatured demographic groups [s038].
- The critics also argue that RLHF safety alignment may suppress conflict and radicalization dynamics. The result would be a "truncated" outcome space [s079].

**Other cognitive limits.**
- Theory-of-mind performance roughly matches a 6–7-year-old child but is brittle [s079].
- Emotion is surface-level mimicry [s079].
- Hallucinations occur and compound across successive LLM calls and social interaction [s008][s028].
- LLMs fall short of Nash play and coordinate poorly in games [s038].

---

## 3. Population: who the agents are

**Synthetic population methods** divide into two families, with hybrids common [s061]:
- **Synthetic reconstruction:** iterative proportional fitting (IPF), Markov chain Monte Carlo (MCMC), copulas and Bayesian networks.
- **Combinatorial optimization:** reweighting or replicating real records.

**Practice lags method.** A review of 342 simulation models in JASSS (2011–2021) found:

| Practice | Share of models |
|---|---|
| No empirical data for agent attributes | 56% |
| Generic random functions for attributes | 62% |
| Dedicated generation algorithms | ~22% |
| ODD description sufficient to reproduce initialization | insufficient in general |

Synthetic populations are also usually validated against the same data used to generate them [s061].

**Data-rich exceptions** show what is feasible:
- A representative synthetic Austria of about 9 million agents for COVID-19 [s037].
- Ward-level Kolkata. Its authors show that granular demographic distributions are needed for successful validation [s047].
- About 570,000 Ethiopian rural agents in 125,000 households [s077].

**LLM societies** are initialized from persona prompts or sampled from survey distributions [s079][s018]. Attitudes and mental states remain largely unsupported by population-synthesis tools, a gap flagged in the classical literature [s061].

---

## 4. Environment and space

**Abstract spaces.** Classic environments are abstract lattices.
- Sugarscape uses a 50×50 torus with regrowing resources, seasons and diffusing pollution [s011][s021].
- Conflict models use grids of provinces or villages [s026][s046][s084].

**Realistic spaces.** Applied models couple ABMs to GIS [s077], to city structure [s047], or to full social-ecological systems [s009][s029][s066].

**Human–environment coupling is often one-way.**
- 9 of 15 environment–migration ABMs lack fully integrated feedbacks [s066].
- Many forest ABMs lack direct interactions and dynamic social or ecological processes [s029].
- Bidirectional governance–ecosystem links appear in only about one-fifth of governance ABMs [s019].

**The environment can dominate results.** The replication of Artificial Anasazi found that the fit to archaeological data rests mainly on two carrying-capacity parameters. The agents acted largely as a "smoothing function" of environmental input [s017]. This caution applies whenever environmental data drive an ABM.

**LLM environments.** These range widely:
- Text-only sandboxes.
- Smallville, a game-like town [s008].
- Minecraft [s028].
- Realistic urban digital twins built on OpenStreetMap, SafeGraph points of interest and traffic models [s018].

AgentSociety's authors argue that text-based environments are of "questionable" realism. They offload objective physics to the simulator to reduce hallucination [s018]. The hybrid-architecture proposal generalizes this: the ABM holds ground-truth state and the LLM only proposes actions [s079].

---

## 5. Social structure: networks and interaction topology

**Topology shapes cooperation.** This is the best-established body of results, from evolutionary games on graphs [s003][s023][s013].
- Spatial clustering lets cooperators resist defectors [s023].
- Neighbourhood size matters: cooperators survive only for roughly 4 ≤ z ≤ 64 neighbours [s003].
- Scale-free networks markedly enhance cooperation, mainly through degree heterogeneity [s003][s023].
- Spatial structure does not always favour cooperation [s023].

**Modelling choices change outcomes qualitatively.** Examples include:
- The update rule: imitation versus logit dynamics, where logit dynamics can even produce a Hopf bifurcation [s003].
- Synchronous versus asynchronous scheduling [s003][s021].
- The strategy-adoption rule (Fermi, degree-normalized, or richest-following) [s023].

**Coevolving networks.** When links and traits evolve together:
- Time-scale separation between link and strategy dynamics can turn a Prisoner's Dilemma into a coordination game [s023].
- Combined rewiring and opinion adoption gives a continuous phase transition from diversity to consensus [s005][s073].
- Rewiring by opinion similarity tends to fragment populations [s064].

A caution from this literature: coevolution rules should not give cooperators and defectors different cognitive skill, or cooperation is built in [s023].

**Homophily and segregation.**
- In a homophilous network-formation model, society segregates when ties form on few features. Triadic-closure reinforcement is necessary for this, and segregation roughly halves information-spreading speed [s025].
- **Schelling on networks.** Heterogeneous preferences combined with heterogeneous topology reduce segregation and produce an urban–rural-like sorting [s045]. Dense networks segregate less and need a much higher same-group preference to polarize [s055]. Both are simulation-only preprints.

**LLM agents and networks.**
- LLM agents building networks reproduce preferential attachment, triadic closure, homophily, community structure and small-world properties. They are homophilous in friendship settings and heterophilous in organizational ones, and align strongly with human survey choices [s083].
- In Generative Agents, network density rose from 0.167 to 0.74 over two simulated days, with 1.3% hallucinated acquaintances [s008].

---

## 6. Culture, opinion dynamics and polarization

**Model families.** Opinion dynamics is the most mature subfield, with three classes of model [s004][s014][s054]:
- Assimilative influence (DeGroot, Friedkin–Johnsen).
- Similarity-biased or bounded confidence (Deffuant–Weisbuch, Hegselmann–Krause) and Axelrod-type cultural models.
- Repulsive or negative influence, which yields bi-polarization and opinions more extreme than any initial opinion.

**Bounded confidence results** [s024][s054]:
- A small confidence level fragments the population into about 1/(2ε) clusters.
- Heterogeneous confidence bounds can produce consensus even below the critical value, but can also cause drift toward extremism [s024].
- The reported consensus thresholds differ: about 0.19–0.22 for Hegselmann–Krause and about 0.27 for Deffuant–Weisbuch under uniform initial opinions [s024], versus a critical radius of about 0.5 [s054]. The 0.5 figure matches the proven network result that Deffuant–Weisbuch reaches full consensus for ε>0.5 [s024]. The discrepancy probably reflects different conventions (typical transition versus guaranteed consensus), not a true conflict.
- Almost all studies assume uniform initial opinions, so outcomes under realistic initial distributions are largely unknown [s024].

**Axelrod's cultural model.** Homophily plus assimilation yields persistent regional diversity [s004][s034]. Two extensions change the picture:
- Adding many-to-one neighbourhood social influence *increases* heterogeneity. It gives about 8.0 versus 1.34 frozen zones on a 30×30 grid and removes the first-order transition [s034].
- Adding a single binary "polarizing" feature eliminates the order–disorder transition in the thermodynamic limit. The disordered state becomes polarized or fragmented depending on the network's percolation threshold [s044].

**Empirical grounding is the acknowledged weak point.**
- Micro-assumptions rest largely on social-psychology experiments from the 1950s–60s [s004].
- Newer work supports bounded confidence experimentally [s014]. It also maps conformity experiments onto the q-voter model [s014] and calibrates an argument-based model on survey experiments, with consistent micro and macro estimates [s063].
- Calibrated applications include Afghan civil-war opinions and climate negotiations [s004], and General Social Survey (GSS) political data [s064].

**Social media and algorithms** are the active frontier.
- ABMs suggest personalization may contribute to polarization [s004][s014].
- LLM-agent simulations report the following, though these are preprint or abstract-level evidence:
  - Homophilic exposure polarized 52% of agents on gun control [s018].
  - Echo chambers form under recommender algorithms and are reduced by "nudges" [s082].
  - Suspending accounts (a node-level intervention) curbs inflammatory spread better than removing ties [s018].
- LLMs promise opinions expressed as rich text rather than scalars [s014][s082].

---

## 7. Norms, conventions and institutions

**Norm emergence in classical models.**
- In Helbing et al.'s spatial model, norms can emerge among agents with incompatible preferences. The process is path-dependent: a committed minority can impose its norm, and emergent norms need not be welfare-optimal [s053].
- Behaviour-based punishment establishes norms far better than preference-based punishment.
- Norms show hysteresis: they persist after sanctions weaken [s053].
- Spontaneous emergence required local interaction and noise, and would not occur with everyone interacting with everyone [s053].
- Conte criticizes the related "thoughtless conformity" and convention approach for taking conformity for granted [s041].

**Conventions among LLM agents.**
- In naming games, LLM populations spontaneously form universal conventions [s081].
- They also develop collective biases even when no individual agent is biased [s081].
- Committed minorities overturn conventions at thresholds of 2% to 67%, depending on the LLM. Theory predicts 10–40% and human experiments found about 25% [s081].
- The authors do not treat LLMs as human proxies [s081].

**Institutions** are increasingly modelled explicitly using the Institutional Grammar (ADICO/ABDICO). It distinguishes rules, norms and shared strategies, and argues that institutions should be separate entities from agents [s071].
- In a commons ABM, imitation plus random exploration sufficed to evolve institutions that improved both the resource and agent welfare [s062].
- Making institutional change harder worsened outcomes, consistent with Ostrom's collective-choice principle [s062].
- This model is explicitly preliminary and unvalidated [s062].

**Governance in social-ecological ABMs is narrow** [s019]:
- It is dominated by state intervention and neoclassical economics.
- It is usually represented as a variable, not as an agent.
- It is rarely used to build new theory.

**Commons and cooperation.**
- Trust and communication, with inequality-sensitive conditional cooperators, explain lab commons outcomes [s049].
- Network "majority illusion" can make commons systems bistable [s059].
- The statistical-physics literature covers peer and pool punishment, rewards, and institutional versus self-organized incentives [s013].

**Laws in LLM societies.** In Project Sid, agents obeyed a seeded tax law and changed their behaviour after democratic amendments driven by influencers. Tax paid fell from 20% to about 9%, while a frozen-constitution control showed no change [s028]. The authors concede, however, that pretrained agents cannot show *de novo* emergence of institutions like democracy or fiat money. The laws and the religion in their experiments were seeded [s028].

---

## 8. Economy and markets

**Emergent exchange.**
- Sugarscape adds spice and bilateral trade at the geometric mean of the agents' marginal rates of substitution (MRS), which produces an emergent market [s001][s021].
- In barter ABMs, money emerges endogenously, with the money good chosen by random dynamics [s070].
- Random multiplicative or exchange models produce power-law wealth tails and inequality [s070].
- Payoff-driven network growth produces Pareto-like wealth distributions [s023].

**Artificial financial markets** reproduce stylized facts: fat tails, volatility clustering and volume–volatility correlation [s002][s070]. They undershoot these quantitatively [s002], and many models' interesting dynamics vanish at realistic agent numbers [s070].

**The SFI market dispute.** A robustness disagreement illustrates how fragile learning-based results can be.
- The original finding that technical trading emerges was traced to an upwardly biased mutation operator [s012][s022].
- Ehrentreich's abstract says two other tests still establish technical trading "beyond a doubt" [s012].
- LeBaron's review emphasizes that the original feature "was sensitive to the type of mutation operator" and that genetic drift, not selection, may dominate strategy dynamics [s022].

**Macroeconomic ABMs** (EURACE, Keynes-meets-Schumpeter, JAMEL, LAGOM) share an emerging common core [s052]. They jointly reproduce macro and micro stylized facts, which DSGE models rarely do [s042][s052]. Policy findings include [s042]:
- Austerity is self-defeating.
- Dual-mandate Taylor rules stabilize better than inflation-only rules.
- More rational expectations do not improve outcomes.
- Macroprudential results are mixed.

These come from an explicitly pro-ABM survey [s042].

**LLM economies.**
- EconAgent claims more realistic decisions and macro phenomena than rule-based or learning-based agents [s080], though this is abstract-only evidence.
- An LLM macro simulation reportedly reproduces the Phillips curve and Okun's law where baselines did not [s038].
- LLM duopolists collude when they can communicate [s038].
- AgentSociety's universal basic income (UBI) experiment qualitatively matched Texas outcomes [s018], but its labour and goods markets are simplified [s018].

---

## 9. Conflict, politics and state formation

**War sizes.** Cederman's model reproduces the power-law distribution of war sizes, with a median R² of 0.991 and a median slope of −0.55 [s026].
- Both technological change and "contextual activation" are necessary; without either, the power law breaks down.
- The model required tuning, so self-organized criticality's parameter-insensitivity is "not fully satisfied" [s026].

**Overconfidence.** A related model finds that overconfidence is selected for. This works through a "lottery effect" and through offensive alliances that emerge without coordination, while defensive alliances cannot emerge [s036].

**Polity formation.**
- Chiefdom models show stochastic growth–collapse cycling even without environmental shocks, consistent with Mississippian archaeology [s046].
- A circumscription ABM finds social circumscription the largest driver of hierarchy formation. Geographic barriers can help or hurt depending on whether they increase proximity between settlements [s056].

**Insurgency.** In an insurgency model, avoiding collateral damage outweighs capture effectiveness, with a possible tipping point in accuracy [s084].

**Electoral competition.** In party-competition ABMs, satisficing parties beat relentless vote-maximizers [s074] (abstract-only evidence).

**Common limitations.** All of these are stylized. The recurring omissions are alliances, secession, learning and cultural similarity [s026][s036][s046].

---

## 10. Demography, migration, epidemics and history

**Demography.** Sugarscape can produce population crashes or overpopulation collapse [s001]. In Artificial Anasazi, demographic parameters matter little; population simply tracks carrying capacity [s017].

**Migration.** Migration ABMs are shaped by two critical choices: how decisions are modelled and how social networks are modelled [s057]. Flee 3 reports forecasting over 70% of refugee arrivals across ten conflicts and runs at scale on 512 cores [s075] (abstract-only evidence). Environmental migration models largely neglect temporary migration and flows across system boundaries [s066].

**Epidemics.** Epidemic ABMs require a synthetic population, a geo-located contact network, and a disease progression model [s047]. Two examples:
- The Austrian model's calibrated infection probability of 5% is close to the literature value of 4.4% [s037].
- In the Kolkata model's counterfactuals, weekend lockdowns were effective and prolonged lockdowns were not [s047].

Both are preprints.

**LLM mobility.** An LLM-agent simulation of mobility during Hurricane Dorian qualitatively tracked real trip data [s018].

---

## 11. Methodology: specification, analysis, validation and tooling

**Specification and replication.** Replication failures recur across the field:
- Sugarscape's rules are ambiguous. Omitted details, such as parental resource gifts, have "huge" effects, and no conflict-resolution rules are specified. A formal Z specification was proposed [s021].
- The Anasazi paper and its code disagreed on the time step [s017].
- The SFI market's complexity deterred replication [s022].

ODD is the accepted documentation standard [s010]. It is insufficient for population initialization, so ODD plus code is recommended as a minimum [s061].

**Scheduling.** Synchronous and asynchronous updating give different results, and how much they diverge in complex ABMs is unknown [s021][s003]. Mesa 3 dropped its fixed scheduler in favour of flexible activation [s078].

**Formal analysis.**
- Sugarscape can be proven ergodic as a Markov chain, so a single long run suffices [s011].
- Stationarity and ergodicity tests such as Wald–Wolfowitz are recommended [s042].
- The SFI market authors reported results over 25 runs because ergodicity could not be proven [s002].

**Validation has no consensus** [s020]. Available approaches include:
- Indirect calibration.
- Werker–Brenner calibration.
- History-friendly modelling.
- Simulated minimum distance and Bayesian methods [s020][s042].
- Micro and macro calibration, with forward validation [s069].
- Surrogate machine-learning meta-models. These run 500–3,750× faster, but were tested only on small models [s040].

Evidence of weak practice is consistent across reviews:
- Only 11 of 29 social-ecological ABMs compared output to data, and none made a strong case for realism [s009].
- Validation in innovation-diffusion ABMs is "often informal, incomplete, and even missing" [s069].
- Most estimation work uses very simple ABMs [s040][s030].

**Sensitivity analysis.** No single method gives a complete picture. Extended one-factor-at-a-time analysis is a good start but should be combined with global methods [s050]. The choice should depend on model purpose [s060].

**LLM validation.** The problems are sharper for LLM societies [s079]:
- Believable individual agents do not guarantee valid macro outcomes (the micro–macro gap).
- Cost prevents running thousands of sensitivity-analysis replications.
- Behavioural assumptions become implicit and opaque.

The critics therefore judge LLM ABMs currently suited to exploratory work and serious games, not confirmatory work or forecasting [s079]. Proponents' validation is mostly qualitative case studies [s018] or small, short runs: Smallville was 25 agents over 2 days and cost thousands of dollars [s008].

**Scale claims are inconsistent.**
- AgentSociety reports 10k+ agents and about 5 million interactions, bottlenecked by LLM API latency, using DeepSeek-V3 [s018]. A later review describes it as "10,000+ GPT-4 agents" [s079], a discrepancy in secondary reporting.
- Project Sid claims 500–1,000-agent civilizations, but notes that 1,000+ agent runs exceeded server limits and its cultural results come from a single 500-agent run [s028].
- Cost-saving hybrids include AgentTorch, which uses a few archetypal LLM agents to set reusable policies [s079].

**Tooling.** NetLogo is accessible but limited to small models, MASON is faster, and Python's Mesa 3 is growing [s078]. BDI tooling and population-synthesis tooling remain poorly integrated into these platforms [s058][s061].

---

## Gaps and open questions

- **Empirical validation remains the central unsolved problem** across both classical and LLM ABMs [s004][s009][s020][s069][s079]. Micro–macro joint validation and forward (out-of-sample) validation are rare [s069].
- **Can LLM agents represent human diversity?** Richer heterogeneity [s038][s048] or mode collapse and caricature [s079]? How much does safety alignment bias social outcomes [s079]? Both remain unresolved.
- **Genuine emergence versus seeded behaviour in LLM societies.** Pretrained agents may import institutions rather than generate them [s028]. How LLM critical-mass thresholds (2–67%) relate to human ones (~25%) is unclear [s081].
- **Robustness to modelling choices.** The open issues are:
  - Update scheduling [s021].
  - Learning operators [s012][s022].
  - Finite-size effects [s070].
  - Initial opinion distributions [s024].
- **Institutions and governance.** Representations remain thin, top-down and rarely theory-generating [s019]. Downward causation from macro to micro is still poorly formalized [s041][s071].
- **Two-way human–environment feedbacks** are incomplete in most social-ecological and migration models [s066][s029].
- **Missing societal mechanisms in stylized models.** Alliances, secession, cultural similarity and learning are recurring omissions in conflict and state-formation models [s026][s036][s046]. Labour and goods markets are simplified in LLM economies [s018].
- **Infrastructure.** Standard benchmarks and open platforms for LLM-driven simulation are lacking [s038]. Scalable cognitive (BDI) and population-synthesis tooling is not integrated into mainstream platforms [s058][s061]. Cost limits statistical rigour [s079].

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
- [s034] Cultural Dissemination: An Agent-Based Model with Social Influence - https://www.jasss.org/24/4/5.html
- [s036] Fortune Favours the Bold: An Agent-Based Model Reveals Adaptive Advantages of Overconfidence in War - https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0020851
- [s037] Synthetic Reproduction and Augmentation of COVID-19 Case Reporting Data by Agent-Based Simulation - https://www.medrxiv.org/content/10.1101/2020.11.07.20227462.full.pdf
- [s038] Large Language Models Empowered Agent-based Modeling and Simulation: A Survey and Perspectives - https://arxiv.org/pdf/2312.11970
- [s040] Agent-Based Model Calibration using Machine Learning Surrogates - https://arxiv.org/pdf/1703.10639
- [s041] Review of Epstein, J.: Generative Social Science: Studies in Agent-Based Computational Modeling - https://jasss.soc.surrey.ac.uk/10/4/reviews/conte.html
- [s042] Macroeconomic Policy in DSGE and Agent-Based Models Redux: New Developments and Challenges Ahead - https://www.jasss.org/20/1/1.html
- [s044] Polarization inhibits the phase transition of Axelrod's model - https://arxiv.org/pdf/2102.06921
- [s045] Behavioral and Topological Heterogeneities in Network Versions of Schelling's Segregation Model - https://arxiv.org/pdf/2408.05623
- [s046] Cycling in the Complexity of Early Societies - https://www.sociostudies.org/almanac/articles/cycling_in_the_complexity_of_early_societies/
- [s047] City-Scale Simulation of COVID-19 Pandemic & Intervention Policies using Agent-Based Modelling - https://arxiv.org/pdf/2104.01650
- [s048] Large language models empowered agent-based modeling and simulation: a survey and perspectives - https://www.nature.com/articles/s41599-024-03611-3
- [s049] An Agent-Based Model of the Interaction Between Inequality, Trust, and Communication in Common Pool Experiments - https://www.jasss.org/25/4/3.html
- [s050] Which Sensitivity Analysis Method Should I Use for My Agent-Based Model? - https://www.jasss.org/19/1/5.html
- [s052] Agent-Based Macroeconomics - https://d-nb.info/1151638439/34
- [s053] Conditions for the Emergence of Shared Norms in Populations with Incompatible Preferences - https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0104207
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
- [s070] Agent-based Models of Financial Markets - https://arxiv.org/pdf/physics/0701140
- [s071] Institutional modelling: Adding social backbone to agent-based models - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9372633/
- [s073] Replicator Dynamics of Co-Evolving Networks - https://arxiv.org/pdf/1107.5354
- [s074] Party Competition: An Agent-Based Model - https://press.princeton.edu/books/paperback/9780691139043/party-competition
- [s075] Flee 3: Flexible agent-based simulation for forced migration - https://www.sciencedirect.com/science/article/pii/S1877750324001649
- [s076] A Simple-to-Use BDI Architecture for Agent-Based Modeling and Simulation - https://link.springer.com/chapter/10.1007/978-3-319-47253-9_2
- [s077] An Agent-Based Model of Rural Households' Adaptation to Climate Change - https://jasss.soc.surrey.ac.uk/21/4/4.html
- [s078] Mesa 3: Agent-based modeling with Python in 2025 - https://www.theoj.org/joss-papers/joss.07668/10.21105.joss.07668.pdf
- [s079] Integrating LLM in Agent-Based Social Simulation: Opportunities and Challenges - https://arxiv.org/pdf/2507.19364
- [s080] EconAgent: Large Language Model-Empowered Agents for Simulating Macroeconomic Activities - https://aclanthology.org/2024.acl-long.829/
- [s081] Emergent Social Conventions and Collective Bias in LLM Populations - https://arxiv.org/pdf/2410.08948
- [s082] Decoding Echo Chambers: LLM-Powered Simulations Revealing Polarization in Social Networks - https://aclanthology.org/2025.coling-main.264/
- [s083] Network formation and dynamics among multi-LLMs - https://academic.oup.com/pnasnexus/article/4/12/pgaf317/8361967
- [s084] Governments, Civilians, and the Evolution of Insurgency: Modeling the Early Dynamics of Insurgencies - https://www.jasss.org/11/4/7.html
