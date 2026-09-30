# Research agent-based modeling of artificial societies. Prioritize academic papers for which the full text is available, falling back to abstracts. Reduce this to a summary of the state of the art, organized by aspects of the artificial society.

# Agent-Based Modelling of Artificial Societies: State of the Art

## Scope and strength of the evidence

An "artificial society" in agent-based modelling (ABM) is a population of heterogeneous, autonomous agents. The agents interact locally with each other and with an environment, and macro-level social patterns emerge from those interactions rather than being imposed by the modeller [s020][s078]. The founding demonstration is Sugarscape. In it, group formation, cultural transmission, combat, trade, migration and wealth inequality all emerge from simple local rules on a resource landscape [s001][s011].

This summary draws on two very different bodies of work:

- **The "classical" tradition** consists of rule-based and evolutionary-learning agents, mostly published 1996–2022. Much of the synthesis here rests on peer-reviewed reviews read in full, but several are dated: evolutionary games (2007), validation (2007), and BDI agents (2016) [s003][s020][s058].
- **LLM-driven "generative" agent societies** date from 2023 onward. This evidence is newer and thinner. It consists of one widely cited primary system [s008], a survey available as both preprint and journal version [s038][s048], and a few 2024–25 primary studies, several read only as abstracts [s080][s082].

Many notes on domain models are also abstract-only [s012][s029][s074][s075]. Claims based on those sources should be treated as weaker.

---

## 1. Agents: cognition and decision-making

**Simple rule-based agents still dominate.**
- Sugarscape agents have vision, metabolism and a greedy "move to the richest visible cell" rule [s011].
- Reviews repeatedly note that most social simulations still assume "very rudimentary cognition" or "simple reactive particle-like agents" [s058][s067][s076].
- Economic ABMs replace rational expectations with boundedly rational heuristics or rules of thumb [s020][s052]. The macro-ABM literature, however, still lacks a common basis for which bounded-rationality rules to use [s052].

**Learning agents.**
- Evolutionary learning (genetic algorithms, classifier systems, genetic programming) was the classic route to adaptive agents in artificial markets [s002].
- Results are sensitive to how learning is implemented. In the Santa Fe Institute (SFI) market, fast rule updating produced realistic market dynamics, while slow updating collapsed to the rational-expectations equilibrium [s002].
- A later reanalysis found that an upwardly biased mutation operator had distorted evidence of technical trading. It also found genetic drift, not only selection, to be an important force [s012].
- Reinforcement learning (Q-learning with Boltzmann exploration) has been used to co-evolve strategies and network links, but only analytically for tiny (3-agent) systems [s073].

**Cognitive architectures.**
- The Belief-Desire-Intention (BDI) architecture is promoted because it maps onto folk psychology and is understandable to stakeholders. It can be extended with norms and emotions [s058][s067].
- BDI's known weaknesses are scalability, expressivity and learning [s058].
- Its low uptake is attributed mainly to missing platform support rather than conceptual flaws. BDI extensions now exist for GAMA and NetLogo [s058][s076].
- Domain models increasingly use explicit psychological frameworks:
  - the MPPACC framework for climate adaptation [s077];
  - random utility or discrete choice and the Theory of Planned Behaviour for migration [s057];
  - cognitive and emotional decision-making in some forest-management ABMs [s029].

**LLM-based agents.**
- Generative Agents give each agent a natural-language memory stream. Memories are retrieved by recency, importance and relevance, then synthesised into reflections and plans [s008].
- The surveys frame planning, memory and reflection as the core of LLM agent architecture [s038][s048].
- They argue LLM agents overcome the traditional trade-off between reactive and deliberative agents, since classical symbolic planners were intractable [s048].
- They also note that LLM agents lack domain knowledge and can make irrational decisions [s048].
- In game-theoretic settings, LLMs fall short of Nash play and coordinate poorly [s038].

**Disagreement: how much cognition is needed (KISS vs KIDS).** The field remains split between "Keep It Simple" and "Keep It Descriptive" [s058][s067]. Evidence cuts both ways:
- *For simplicity:* imitation plus random exploration suffices for sustainable commons institutions to emerge [s062]. In Artificial Anasazi, agent behaviour adds only modest improvement over what the carrying-capacity inputs already explain [s017].
- *For richer cognition:* critics argue that rudimentary cognition limits realism and the study of micro–macro links [s058]. LLM advocates argue rich internal complexity is the main benefit [s048].
- The reviews conclude that the right choice depends on the model's goal [s058].

## 2. Population: heterogeneity and synthetic populations

**Heterogeneity often drives the results.**
- A commons ABM calibrated to lab data reproduced the observed patterns only with a mixed population: 75% conditional cooperators, 9% unconditional cooperators and 16% selfish agents [s049].
- Heterogeneous confidence radii make consensus easier in bounded-confidence models [s054].
- Combining heterogeneous tolerance with heterogeneous network topology reduces Schelling segregation [s045].
- Memory length is the key heterogeneity in the second-generation SFI market [s002].

**Empirical grounding of populations is weak.** A review of 342 simulation models in JASSS (2011–2021) found that [s061]:
- 55.85% used no data for agent attributes;
- about 62% initialised attributes with generic random functions and 33% with constants;
- only about 12.6% used synthetic reconstruction and 0.6% used combinatorial optimisation.

Reasons given are that generation tools are hard to find and poorly integrated into platforms, and that there are no data on abstract attributes such as attitudes [s061]. Synthetic populations are also usually validated against the same data used to generate them [s061]. Data-rich exceptions exist:
- epidemic ABMs require a demographically realistic synthetic population plus a geo-located contact network [s047];
- a climate-adaptation model covers about 570,000 people in 125,000 households [s077].

**LLM approach.** LLM surveys pitch prompting, in-context learning and fine-tuning as a remedy for the calibration burden of heterogeneity [s038][s048]. EconAgent uses a "perception module" to create heterogeneous decision-makers [s080]. The same surveys flag controllable heterogeneity as an unsolved challenge [s048]. They also report that persona prompting can caricature demographic groups and raise toxicity about sixfold [s038].

## 3. Environment and space

**Spatial representations.**
- Classical artificial societies use lattices: Sugarscape's 50×50 torus with resource growback [s011], hexagonal village grids for polity formation [s046], and bounded 50×50 grids with Moore neighbourhoods for insurgency [s084].
- Modern frameworks support grids, hex grids, networks, Voronoi meshes, continuous space and cell-level property layers, with tick-based or experimental discrete-event time [s078].
- NetLogo is characterised as the most accessible platform but limited to small models, and MASON as faster but less accessible [s078]. These comparisons were not benchmarked.

**Environment shapes emergent society.**
- Seasons produce migration in Sugarscape, and twin resource peaks produce distinct "tribes" [s001].
- In Artificial Anasazi, the historical fit comes mainly from two carrying-capacity parameters. The ABM acts largely as a "smoothing function" of environmental inputs [s017].

**Social-ecological coupling is often one-way.**
- 9 of 15 environment–migration ABMs lack fully integrated two-way feedbacks. Agents rarely affect climate drivers [s066].
- Many of 31 forest ABMs lack direct interactions and dynamic social or ecological processes [s029].

**LLM environments.** These are either sandboxes such as Smallville, or "real" environments such as economies, websites and urban digital twins. Interaction is mostly text-based [s038][s048].

## 4. Social structure and networks

**Topology changes collective outcomes.**
- In evolutionary games, cooperators on regular lattices survive only within a band of neighbourhood sizes (about 4 ≤ z ≤ 64) [s003].
- Scale-free networks markedly enhance cooperation compared with lattices [s003].
- The update rule matters too. Logit dynamics can produce qualitatively different results from imitation dynamics [s003].
- In Axelrod's culture model with a polarising binary feature, the network's percolation threshold decides the outcome [s044]:
  - below 1/2, the population polarises into two dominant cultures;
  - above 1/2, it fragments into many cultures.

**Co-evolving (adaptive) networks.**
- The field distinguishes influence-on-network from network-formation-by-similarity models. Coupling the two yields a phase transition from opinion diversity to consensus [s005][s073].
- Rewiring by opinion similarity tends to fragment populations [s064].
- Newer models couple social mobility and opinion through stochastic differential equations and fit them to General Social Survey data [s064].

**Segregation.**
- On dense, non-spatial social networks, Schelling dynamics segregate less. Agents do not overshoot their desired share of similar neighbours, and polarisation requires much higher preferences than classic tipping points [s055].
- This suggests online networks may be structurally harder to polarise [s055]. The finding is simulation-only and from a preprint.

**Information asymmetry.** Highly visible hubs create a "majority illusion" in common-pool resource (CPR) games. This makes outcomes bistable: the population ends in either an abundant or a depleted state [s059].

**LLM network formation.**
- LLM agents reproduce preferential attachment, triadic closure, homophily, community structure and small-world effects [s083].
- Their link choices are context-dependent: homophily in friendship settings, heterophily in organisations [s083].
- A survey found strong alignment with human link-formation decisions [s083], mainly for GPT-family models.
- Generative Agents' town network rose in density from 0.167 to 0.74 over two simulated days, with 1.3% of reported acquaintances hallucinated [s008].

## 5. Opinion dynamics, culture and polarisation

This is the most theoretically developed aspect.

**Model classes** [s004][s054]:
- assimilative models (DeGroot, Friedkin–Johnsen with stubborn agents);
- bounded confidence (Deffuant, Hegselmann–Krause), where a small confidence threshold fragments the population into clusters;
- Axelrod-type cultural models, where homophily preserves diversity;
- repulsive or negative influence models, which produce bi-polarisation beyond initial extremes.

**Organising schemes.** A 2025 review sorts models by macro phenomenon (consensus, fragmentation, polarisation, echo chambers) and by micro mechanism (assimilation, distancing, homophily) [s014]. Terminology remains inconsistent. For example, "stubborn", "inflexible" and "leader" are used for similar agents [s054].

**Degree of agreement.** The core findings are robust across model variants. Deffuant and Hegselmann–Krause differ in updating but share implications [s004]. Quantitative claims, such as a critical confidence radius of about 0.5 and about 1/(2r) clusters, come from a single-author, non-peer-reviewed survey citing earlier work [s054]. They should be treated as model-specific.

**Empirical grounding is the acknowledged weak point.**
- Micro assumptions rest largely on 1950s–60s social-psychology experiments [s004].
- Recent experiments support bounded confidence (perceived closeness predicts convergence) and closely mirror the q-voter model [s014].
- Argument-based models calibrated on survey experiments match observed opinion distributions where social influence and external noise are balanced. The macro-level estimates are consistent with the micro-level estimates [s063].
- Calibrated applications include Afghan civil-war opinions, farmer policy diffusion and climate negotiations [s004].

**Algorithms and LLMs.**
- ABMs suggest personalisation algorithms may contribute to polarisation. This topic was only beginning in 2017 [s004] and is now framed as a key need for predicting feed interventions [s014].
- LLM agents can handle textual opinions that numeric models cannot [s014][s082].
- An LLM social network with recommendation algorithms reproduced echo chambers comparable to bounded-confidence and Friedkin–Johnsen baselines. Active and passive nudges reduced them [s082] (abstract only).
- LLM recommender-system users reproduce filter bubbles [s038].

## 6. Cooperation, norms and conventions

**Evolutionary game theory.**
- Spatial evolutionary games, with the public goods game as the null model, are analysed with statistical-physics tools [s003][s013].
- These tools include mean-field and pair approximations and Monte Carlo methods.
- The literature covers incentive mechanisms such as peer and pool punishment, reward and institutionalised incentives [s013].
- This literature is analytically rich but models interaction more simply than full artificial societies. Human interactions involve groups and many states [s013].

**Commons dilemmas.**
- Communication raises trust, which explains better group performance in a lab-calibrated ABM [s049].
- Network visibility can drive the commons to either a sustainable or a depleted state [s059].

**Emergent conventions in LLM populations.**
- LLM agents playing a naming game with only local incentives spontaneously converge on universal conventions. This happens by about round 15 for most models and is robust up to N=200 [s081].
- Collective biases emerge even when individual agents are unbiased [s081].
- Committed minorities of 2% to 67%, depending on the model, can overturn conventions [s081].
- For comparison, theory predicts critical masses of 10–40% and human experiments suggest about 25% [s081].
- The authors explicitly do not treat LLMs as human proxies [s081]. This caution contrasts with claims of strong LLM–human alignment in network formation [s083] and survey-proxy uses [s038].

## 7. Institutions and governance

**Formal representation.**
- The Institutional Grammar (ABDICO/ADICO) is the main formalism. It distinguishes rules (with sanctions), norms, and shared strategies [s071].
- It has been used for both agent strategies and institutions [s062].
- One position is that institutions should be modelled as independent entities rather than embedded in agents. They can be static or can emerge through agents' deliberation and voting [s071]. This comes from a single-author methods paper centred on the author's own approach.

**Findings.**
- Commons institutions emerge from simple mechanisms when collective-choice arrangements exist. Making institutions harder to change worsens both resource and welfare outcomes, consistent with Ostrom's design principles [s062]. The model is preliminary and unvalidated.

**State of practice in social-ecological models** [s019]:
- governance is mostly modelled as state intervention;
- about two-thirds of models are grounded in neoclassical economics;
- community- and market-based modes are rare;
- bidirectional governance–system links appear in only about one-fifth of models;
- governance is usually a variable rather than an agent.

The review recommends representing governance as an agent [s019], which aligns with calls for adaptive governance and feedback loops [s029].

## 8. Economy and markets

**Emergent markets.**
- Sugarscape's spice trade yields an emergent market [s001].
- The SFI artificial stock market reproduces qualitative stylized facts: fat tails, weak autocorrelation, volatility clustering and volume–volatility correlation [s002].
- It undershoots real volatility and kurtosis [s002].
- Its first-generation price mechanism was fragile [s002].

**Macroeconomic ABMs.** Families such as EURACE and Keynes-meets-Schumpeter [s052]:
- jointly reproduce time-series and distributional stylized facts;
- generate endogenous crises through non-linear feedbacks;
- are converging on a "common core" [s052].

**Calibration.** Large macro ABMs are described as poorly calibrated [s040]. Machine-learning surrogates cut calibration cost dramatically, running 500–3750× faster than the full ABM, but were tested only on small models [s040].

**LLM economies.**
- LLM agents reproduce behavioural-economics findings and largely rational budget choices [s038].
- Duopoly LLM agents collude when allowed to communicate [s038].
- EconAgent reports more realistic macro phenomena than rule-based or learning agents [s080] (abstract only).

**Disagreement: LLM vs rule-based macro ABMs.** A survey reports that only an LLM-agent simulation produced the correct Phillips curve and Okun's law, compared with rule-based and RL baselines [s038]. Established macro ABMs, however, are credited with reproducing a wide range of stylized facts [s052]. The LLM claim is a secondhand summary judged against selected baselines. It should not be read as showing that the macro-ABM tradition in general fails.

## 9. Conflict, politics and the evolution of social complexity

**Polity formation.**
- Warfare-driven models of chiefdoms produce stochastic cycles of polity growth and rapid collapse [s046].
- Large polities are stabilised by wealth-determined conflict outcomes, accepted succession and specialised control [s046].
- Collapse can occur without environmental shocks, consistent with short-lived Mississippian chiefdoms [s046].
- A 2024 formal test of Carneiro's circumscription theory found social circumscription to be the largest driver of hierarchy. Geographic circumscription helps or hurts depending on whether it increases proximity between settlements [s056]. Only the paper's opening sections were read.

**Contrast with environmental drivers.** These results sit against Artificial Anasazi, where environmental carrying capacity explains most of the fit [s017]. The two are not strictly contradictory, since they concern different societies and questions. Together they show that the field has not settled how much endogenous social dynamics, as opposed to environmental forcing, explain societal trajectories. The Anasazi replication itself notes that missing social ties are a limitation [s017].

**Interstate and intrastate conflict.**
- In a states-on-a-grid model, moderate overconfidence dominates via a "lottery effect". Offensive alliances emerge spontaneously, while defensive alliances cannot without commitment mechanisms [s036].
- In an insurgency model, avoiding collateral damage matters more than capture effectiveness, and there is a tipping point in accuracy [s084].
- Both models are stylized and unvalidated.

**Politics.**
- In party-competition ABMs, satisficing parties outperform relentless vote-maximisers [s074] (publisher summary only).
- LLM agents have been used to re-simulate historical wars [s038].

## 10. Demography, migration and epidemics

**Demography.** Sugarscape shows population crash or overshoot [s001]. Anasazi demographic parameters matter little once households last over 30 years and reproduce every 6–8 years [s017].

**Migration.**
- Migration ABMs mostly use random utility or planned-behaviour rules. Operationalising theory and choosing validation data are the main obstacles [s057].
- Temporary migration and migration into and out of the system are neglected [s066].
- The Flee 3 forced-migration model forecasts over 70% of refugee arrivals across ten conflicts. It runs Ukraine 2022 in under an hour on 512 cores [s075]. This is one of the stronger quantitative validation claims, but it is based on the abstract only.
- Climate-adaptation ABMs find mixed herding and farming strategies most resilient, but pass only face validity [s077].

**Epidemics.**
- City-scale epidemic ABMs require synthetic populations, geo-located networks and disease models [s047].
- One Kolkata model argues granular spatial data are necessary for successful simulation [s047].
- Its policy counterfactuals are unverifiable, for example that weekend lockdowns work better than prolonged ones [s047].

## 11. LLM-based generative agent societies (cross-cutting)

**What they can do.**
- Generative Agents produced emergent information diffusion without intervention. Knowledge of a party spread from 1 agent to 13 of 25 [s008].
- They also produced partial coordination: 5 of 12 invitees attended the party [s008].
- The full architecture far outperformed ablated versions in human believability ratings (TrueSkill μ=29.89 vs 21.21) [s008].

**Limitations.** Believability is not validity. The evaluation covered 25 agents over two simulated days, cost thousands of dollars, and hallucinated embellishments [s008].

**Open problems identified by the surveys** [s038]:
- computational cost of scaling;
- lack of fidelity benchmarks and open platforms;
- robustness and adversarial propagation;
- bias amplification along agent chains;
- the need for both micro-level (individual behaviour) and macro-level (emergent regularity) evaluation.

## 12. Methodology: documentation, replication, validation and analysis

**Documentation and replication.**
- The ODD protocol is the accepted documentation standard. Its 2020 update adds sections on rationale and evaluation, because many ODDs were insufficient for reimplementation [s010].
- ODD alone cannot convey population initialisation, so ODD plus code is recommended [s061].
- Replication exposes discrepancies. Artificial Anasazi's paper and code differed in time step and household composition [s017].
- Formal analysis is sometimes possible. Basic Sugarscape is an ergodic Markov chain, so a single long run approximates the long-run wealth distribution [s011]. In contrast, the SFI market results were averaged over 25 runs because ergodicity could not be shown [s002].

**Validation: no consensus.**
- Early practice was "cursory comparison" with stylized facts. Competing approaches include indirect calibration, Werker–Brenner and history-friendly modelling, and there is no consensus [s020].
- In social-ecological ABMs, 11 of 29 compared output to data, and none made a strong case for realism [s009].
- Innovation-diffusion ABMs have progressed further on reporting standards but still rarely validate on independent data or at both micro and macro levels [s069]. Proposed remedies are forward validation and maximum-likelihood calibration [s069].
- These differing assessments reflect domain differences rather than a direct contradiction.
- Participatory or companion modelling offers an alternative, stakeholder-based form of validation [s068][s009].

**Sensitivity analysis.**
- One study recommends starting with cheap extended one-factor-at-a-time analysis, which reveals tipping points, then supplementing it with global methods because no single method is complete [s050].
- Another argues that the choice of method should depend on the model's purpose, and advocates routine global methods for policy models [s060].
- These positions differ in emphasis but are compatible.

---

## Gaps and open questions

- **Empirical validation remains the central unsolved problem** across opinion dynamics, social-ecological systems, macroeconomics, migration and synthetic populations [s004][s009][s020][s061][s069]. Micro–macro joint validation and out-of-sample forecasting are rare [s069].
- **Cognition trade-off unresolved.** It is unclear when richer cognition (BDI, LLM) improves explanatory or predictive power relative to simple rules. Evidence that simple rules suffice [s062][s017] has not been systematically weighed against gains from richer cognition [s008][s080].
- **Validity of LLM agents as social actors.** Human alignment claims [s083] coexist with evidence of caricature, bias and non-equilibrium play [s038], and with authors who reject the proxy framing [s081]. There are no fidelity benchmarks, and scale is limited by cost [s038][s008].
- **Integration of aspects.** Most models study one aspect in isolation, such as opinion, segregation, conflict or markets. Institutions, co-evolving networks and two-way environmental feedbacks are under-represented [s019][s066][s064][s029]. Theory comparison and integration across model families is an explicit frontier [s004].
- **Data on abstract attributes.** Attitudes, trust and mental states lack data sources for population synthesis [s061]. Institutional data are qualitative and hard to encode [s071].
- **Recency of this evidence base.** Several core reviews predate 2020, and much LLM-era evidence is preprint or abstract-only. A more current synthesis would need, in particular, the full text of recent LLM-society and macro-ABM work [s014][s048][s080].

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
- [s019] Governance in social-ecological agent-based models: a review - https://www.ecologyandsociety.org/vol26/iss2/art38/
- [s020] Empirical Validation of Agent-Based Models: Alternatives and Prospects - https://jasss.soc.surrey.ac.uk/10/2/8.html
- [s029] Modelling forests as social-ecological systems: A systematic comparison of agent-based approaches - https://www.sciencedirect.com/science/article/pii/S1364815224000598
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
