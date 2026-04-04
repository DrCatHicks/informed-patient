# Informed Patient

This Claude Skill provides a framework to help you use Claude to research medical evidence to inform specific health questions, primarily designed around use cases like trying to understand and organize questions about symptoms, preparing for an upcoming medical appointment, and gathering evidence for either differential diagnosis questions or condition progression. 

When you ask a medical question, Claude will walk you through a semi-structured cognitive interview to elicit context for its search, then conduct a search following a set of guidelines for evidence robustness. The skill provides two potential search "modes": by default it uses a more structured search across a defined evidence source hierarchy, but can use an open search mode for scenarios where you raise a more complex questions that falls between conditions, when you want a more exploratory mode, or when the opinionated search results are thin. 

Alongside searching and synthesizing sources, Claude will weigh the strength of evidence or relevant concerns according to a set of evidence "red flags." The results will be shared in a "health evidence review," including sources, search terms, and evidence red flags to be aware of, and questions generated from the exercise to bring to your healthcare team. 

The aim of this skill is not to replace your healthcare team, but to guide your use of AI as a structured search tool around health information, help you advocate for yourself and your needs, and help you become an "informed patient." 

---

## Installation

This repository is [a Claude Code plugin marketplace](https://code.claude.com/docs/en/plugins). To install:

Add the marketplace:

/plugin marketplace add https://github.com/DrCatHicks/informed-patient.git
Install the plugin:

/plugin install informed-patient@informed-patient 
Restart Claude Code to activate

For more on Claude Code plugins, see [the plugin documentation](https://code.claude.com/docs/en/plugins).

---

## How to use it

This skill is **opt-in only** — it won't activate automatically when you ask health questions. To use it, explicitly tell Claude you'd like to use the informed-patient skill, then describe your situation.

Claude will ask questions before searching. This interview is the foundation for the evidence review. The more specific and accurate your inputs, the more useful the search will be.

---

## What it does

**This is a thinking tool, not a diagnostic tool.** 

Using AI for health is consistently one of the top use cases documented for emerging AI tools. Many people turn to AI for help when trying to make sense of a diagnosis, prepare for a specialist appointment, or understand what the research actually says about a condition. [People also struggle with recognized risks of using AI, such as inaccurate results, encouragement of overly confirmatory thinking, and lack of source clarity](https://www.nytimes.com/2026/04/02/well/live/ai-illness-claude-chatgpt.html).

The Informed-Patient Skill runs a structured process to help you use Claude with evidence science-informed instructions to create an "evidence review" around a specific health question. Using this Skill, Claude will dialogue with you to create a guided symptom/or medical scenario overview, will design a literature search according to a structured evidence hierarchy, and will create a structured document you can bring to your next medical appointment or use to document your questions. 

At the end of the exercise, output is saved in a **Health Evidence Review** that includes:

- A structured symptom inventory (frequency, severity, functional impact, timeline)
- A literature search with transparent search terms 
- A verification note so you can check the sources yourself
- An Evidence Snapshot with 1-3 bullets on how well-studied a condition is, the strongest relevant finding(s), and clinical challenges
- Competing scenarios or hypotheses for your symptom picture, with evidence for and against each
- Epistemic red flags relevant to your situation (e.g., understudied condition, long time-to-diagnosis, self-report as primary evidence)
- A prioritized question list for your appointment, ranked by you


## Scenarios where this Skill could be useful

- You're preparing for a first appointment with a new doctor
- You're mid-diagnostic-journey and trying to make sense of what you've been told
- You're curious about a diagnosis and want to get a starting place to evaluate the evidence behind treatment options
- You're curious about the evidence about a new medicine and how it's been studied
- You want to track and consider the possible connections between disparate symptoms 

It is impossible to anticipate every possible medical scenario. This Skill has complex instructions, and is meant to provide useful instructions to Claude, but the quality and depth of the information you give it will change how specific and helpful its search will be. In particular, being specific, depthful and accurate in the symptom/question dialogue will make the search more useful. 

You can actively experiment with adapting this skill to your needs. You may want to consider: 

- Combining this skill with structured access to full-text scientific libraries, if available, such as the PubMed Connector (https://claude.com/resources/tutorials/using-the-pubmed-connector-in-claude) 
- Setting specific evidence flags that you are concerned about such as evaluating evidence in light of personalized context (for instance, "I want to know if this condition has been studied in people with high blood pressure")
- Designing your own symptom inventory tracking prior to using the Skill, and re-using it for continuing searches, or providing a previous log of symptoms as context to Claude (see privacy notes; you should make your own intentional choice about what you are comfortable sharing)

---

## More detail on the choices in this Skill Design

This skill is opinionatedly designed to use evidence science guardrails in the background, as well as take advantage of Claude's ability to help you create your own personalized patient inventory. It is also structured to push Claude against speculating or "fill in the answer" defaults, to be honest about what it found, what it couldn't find, to provide evidence for how much confidence you should have in competing hypotheses, as well as suggest directions that would confirm or deny working hypotheses or scenarios. 

My aim was to provide a practical thinking tool that strikes a balance between giving you assistance that lightens the load in searching complex literature, but also provides you with clarity and directions for investigation. You are centered as the decision-maker: you control the symptom description, rank questions, and have access to records for further searching or your own cross-verification. I wanted to create a tool that would help people who aren't researchers, scientists or doctors, and who are dealing with something hard may have limited time and energy to wade through complex medical details. Therefore, you can expand or contract your use of the Skill; a quick session of 10 minutes is enough for a review, but you can also run multiple reviews in a row to continue investigating. 

The skill also gives Claude with a structured set of instructions for assessing and flagging key evidence quality indicators, such as missing evidence, understudied conditions, or barriers in care. These are currently set as background references, but you may 

Thinking about your health is high stakes, and we are often cognitively biased toward wanting to find a single answer. To help you get better answers, this Skill is opinionated about holding a high standard of evidence and instructs Claude to try to counter some of the aggressively confirmatory patterns in AI chatbots used for health. In the case of trying to explain symptoms, Claude should explicitly push you to consider multiple hypotheses and evaluate the strength of evidence, as well as generate suggestions of evidence that would strengthen or weaken confidence in the hypothesis.  

This Skill is meant to help you organize your experience and evaluate evidence. It should not be used to tell you what you have or what to do about it.

While I have continually tested the sources this Skill produces and refined the Skill across many disparate searches, it is always possible for AI to be inaccurate. 

You can use the EVALUATION.md file as a starting place to check that this Skill is performing as expected across different scenarios. 


## How I thought about guarding against risks

The aim of this skill is not to provide "the answer" or end of a question, but to sharpen your investigatory skills and give you support to advocate for yourself as a patient or on behalf of a patient.

In keeping with that vision, in this Skill, I have used opinionated evidence-based principles to design for eliciting diverse and functionally-relevant descriptions of symptomology, for assessing the clinical literature, and for keeping in mind the complex causality of healthcare decision-making. Going through an iterative process (intake, search for sources, source summaries, evidence red flag evaluation, synthesis) introduces step-by-step thinking and more reflection, while still letting you take advantage of AI assistance. Running multiple reviews will strengthen this process further.

One key risk in using AI for healthcare questions is the model defaults to provide "helpful" confirmatory information and to summarize on behalf of users. Additionally, the models frequently encode poor metascience practices, such as over-extrapolating from a single study, or taking findings as "proven" merely by statistical significance without considering multiple factors such as the type of people studied, the quality and depth of data, and the accuracy of measurements. 

When users simply ask AI models about health in basic prompts, this can lead to models generating answers that overstate evidence, or encourage Claude to try to "read tea leaves" in the symptomology and user descriptions of symptoms. Taking the patient inventory seriously (and the ways that clinical practice fails to include patient accounts) helps deepen the model's search.

Causality (what leads to what) in health is multivariate, and complex, and difficult to figure out. Many symptoms can look similar but be caused by different things, and the same condition can present differently for different individuals. 

Drawing from the research literature around complex patient care and my experience with evidence thinking, I've made design choices in this skill to push Claude to help you think about competing possibilities, assess the strength of evidence, and generate questions for your healthcare team. It should not generate confirmatory statements or "tell you what you have." In keeping with scientific evidence principles for careful diagnosis, it should help you notice things such as when you are "anchoring" on an initial hypothesis or explanation, and encourage testing alternative hypotheses. 

These design choices are reflected in: 

- instructions in the patient inventory step to probe for multidimensional and grounded descriptions of symptomology, such as functional impact
- sources and context in the symptom-inventory-methodology that acknowledge the gaps frequently seen between patient descriptions of their experience and symptoms, and non-personalized measures which fail to incorporate patient pov 
- instructions in the evidence assessment step to flag when a user is assuming a diagnosis that has not been clinically confirmed 
- instructions to suggest that a user rank their most important questions for their healthcare team 
- instructions to provide the user with clear documentation of the literature search, to encourage source checking and traceability

---

## Privacy

Using AI for health questions is a contentious topic. As noted above, I believe any use of AI for health questions carries risk of receiving misleading errors. On the other hand, patients facing delay of care, complex diagnoses and difficulty accessing scientific literature suffer from this lack of access, and struggle in the face of great need. I decided to write this Skill because I found that trade-off worth it, and you may decide it is worth it too. 

However, I am mindful of the privacy risks with AI that remain unsolved. My aim in providing this Skill is to give you an example of choices I have made myself, in the hopes that it might help more people get higher quality care and reduce their suffering. I cannot make a privacy and personal data decision for you, but here are some aspects that I think are important to think about:

You should make an informed choice about all information you give to Claude. This skill can be used to ask generic medical questions without giving specific dates or condition details. However using this skill maximally for most people likely involves sharing health information with an AI system. The steps below won't eliminate privacy risks, but they might be steps you can think about as you weigh your decision. Read through and make the choices that are right for your situation.

### This is not a HIPAA-covered tool

Connecting AI to existing healthcare systems and healthcare records is a rapidly evolving space. Some users may have access to Claude for Healthcare (https://claude.com/solutions/healthcare). I do not, so I have been unable to vet this skill in that particular context. To my knowledge as of publishing this skill Claude is not a HIPAA compliant tool by default. That means you should know that data you share in a conversation does not receive HIPAA protections (the US legal framework that governs how healthcare providers and insurers handle your medical records). 

### Consider opting out of training data use

Before using this skill, consider whether you want your conversation used to train Anthropic's models.

More detail: [Anthropic Privacy Center](https://privacy.claude.com) · [Is my data used for model training?](https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training)

### Consider sharing your health situation, not your identity

Many questions don't require personal information. This skill doesn't need your name, date of birth, location, employer, insurance information, or any other identifying details. It can work on symptoms, history, and medical context alone.

Conditions that might carry real-world stigma warrant extra care. Consider how specific you need to be and what information you are trying to get help with. The skill can work with "a condition that affects my immune system" rather than a named diagnosis if you prefer. 

### Consider using a personal account, not a work account

If you access Claude through an employer's Teams or Enterprise plan, your employer may have administrative visibility into your conversations. You may want to consider only using a personal Claude account for health conversations. 

### Consider deleting conversations after you have your document

Once the output file is written, you could consider deleting the conversation. 

---

## Known limitations

Specific limitations to be aware of:

- **Citation hallucination risk.** The skill instructs Claude to include source URLs and flag unverifiable identifiers, but hallucinated citations remain possible. Always click the links in the Sources Reviewed section and verify that the title and finding match what's described.
- **Search stops when evidence is solid.** The skill works through a source hierarchy (Cochrane → guidelines → primary research → FDA → patient advocacy) but stops when the evidence base is sufficient to support the user's questions. For well-studied conditions with strong Cochrane and guideline coverage, lower-priority sources may be skipped. If you want to force a complete search through all source types, tell Claude explicitly: "Search all source types in the hierarchy even if you find strong evidence early."
- **Search tool limitations — PubMed site: queries.** The skill instructs Claude to run `site:pubmed.ncbi.nlm.nih.gov` queries, but web search tools don't reliably honor `site:` operators. Claude will fall back to general queries that return PubMed/PMC results, but this is less precise than a native PubMed search. **Users with a PubMed MCP connector** can layer that in for more reliable and comprehensive PubMed retrieval — tell Claude to use it when searching medical literature.
- **Other site-specific queries (Cochrane, NICE)** are subject to the same tool limitation. Results have been verified for well-studied conditions (e.g., hypertension), but reliability across all conditions is not guaranteed.
- **Not clinically validated.** This skill has not been reviewed by clinicians or evaluated in a clinical context. It is a structured reasoning aid, not a clinical instrument.
- **Evidence sources are primarily US and UK-based.** The search hierarchy prioritizes sources I am most familiar with, Cochrane, NICE, AHRQ, the USPSTF, and PubMed. These are high-quality, widely used bodies, but they reflect a particular slice of the global clinical evidence landscape. Guidelines from the European Medicines Agency, WHO, or national health bodies in other countries may differ and may be equally or more relevant depending on where you receive care. If you have specific sources you want prioritized, tell Claude explicitly at the start of the session: "Also search [source] as part of the evidence hierarchy." The skill is designed to be adaptable.


---

## Files

| File | Purpose |
|---|---|
| `informed-patient/skills/informed-patient/SKILL.md` | The skill itself |
| `informed-patient/references/evidence-hierarchy.md` | How to explain study types in plain language |
| `informed-patient/references/red-flags.md` | The 10 epistemic red flags |
| `informed-patient/references/symptom-inventory-methodology.md` | Measurement science grounding for Phase 1 symptom elicitation |
| `LICENSE.txt` | CC-BY-4.0 license |

---

## Sharing, Contributing & Author 

I have put a lot of work into making this skill work the way I like, so I may not accept suggestions with different visions for the skill. However if you find an error, have an idea for an extension, or have a suggestion for improvement I am more than happy to review. 

If it helps you, I would love to hear about it. I am deeply interested in how we design better tooling for AI in complex social contexts. I always appreciate a shout-out or share of my work in public. You can find more of my writing about psychology and tech, and AI, at my newsletter: [Fight for the Human](https://www.fightforthehuman.com/).

Dr. Cat Hicks

Relevant to this skill and its design, I have significant personal experience navigating complex chronic health conditions, and have personally used this skill to advocate for my own health. 

In my work life I'm a psychological scientist studying software teams and technology work, an author, a public speaker, a research architect, and an empirical interventionist who builds radical research teams that put answers behind questions everyone is asking but few people are gathering real evidence about.

- Website: [drcathicks.com](https://www.drcathicks.com/)
- Software Team & Eng Leadership Consulting: [catharsisinsight.com](https://catharsisinsight.com/)
- Upcoming Book: [The Psychology of Software Teams (Available July 2026)](https://www.routledge.com/The-Psychology-of-Software-Teams/Hicks/p/book/9781032963389%20%20%20)

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).