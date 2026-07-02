# Health Evidence Review: Output Template

This is the exact structure for the output artifact described in the informed-patient skill. Fill in every section using the interview, search, and evaluation results, adapting depth to what the user provided. Use "Possible Explanations" for differential diagnosis questions or "Possible Scenarios" for confirmed diagnosis with progression/risk questions — include only the relevant one, not both.

```
# Health Evidence Review: [Condition/Symptoms]
Generated: [date]

## My Symptom Picture

### Current Symptoms
[Structured inventory with frequency, severity, duration, functional impact, patterns]

### Timeline
[When it started, how it's changed, key events]

### What's Been Tried
[Tests, treatments, specialists seen, results]

## What Our Search Covered

### Search Context
> **What we searched for:** [1-2 sentences describing the symptom picture and diagnostic territory that framed the search — e.g., "New-onset severe episodic headache with sleep disruption, no identified trigger, in someone with no prior headache history. Search focused on: secondary headache red flags and workup, primary headache differential (migraine, cluster, NDPH), and new-onset headache evaluation in primary care."]
>
> *A single search session cannot cover everything. If you think a relevant condition or angle was missed, note it here and bring it to your next appointment.*

### Evidence Snapshot
[1-3 bullets orienting the user to the research landscape: how well-studied is this, the strongest relevant finding, and — if research exists — how challenging this is clinically (misdiagnosis rates, common errors, diagnostic delays)]

### Sources Reviewed
[Each source with plain-language quality tag: study type and what it means, sample size and population, recency, and relevance to this user's specific situation. Include what couldn't be found.]

> **How to verify these sources:** Click each link below. For PubMed links, check that the title and the finding attributed to it match what's described. For guidelines (NICE, AAFP, etc.), check the publication date — if it's more than 5-10 years old, it may have been updated. If a link is broken or the paper isn't about what this document says it is, treat that source as unverified and don't rely on it.

> **Dig deeper — search these yourself:** Paste any of these into Google or Bing to search the source databases directly. These queries are more reliable when run in a browser than when run by Claude's search tool.
> - `site:cochranelibrary.com [condition]`
> - `site:pubmed.ncbi.nlm.nih.gov [condition] systematic review`
> - `site:nice.org.uk [condition]`
> - `site:effectivehealthcare.ahrq.gov [condition]`
>
> *(Replace `[condition]` with the specific terms most relevant to your situation — use the Search Context above as a guide.)*

## Possible Explanations

### Hypothesis 1: [Most likely / user's primary concern]
- How well it explains my symptoms:
- What it doesn't explain:
- What would confirm it:
- What would rule it out:

### Hypothesis 2: [Alternative]
[Same structure]

### Hypothesis 3: [Alternative]
[Same structure]

## Possible Scenarios

### Scenario 1: [Condition remains stable]
- What the evidence says about this likelihood:
- What factors in my profile support this:
- What monitoring would confirm stability:

### Scenario 2: [Condition progresses — early signs]
- What the evidence says about this likelihood:
- Risk factors that apply to me:
- What early detection looks like:
- What monitoring would catch this:

### Scenario 3: [Complication develops — intervention options]
- What the evidence says about treatment if this occurs:
- How early treatment changes outcomes:
- Questions for my medical team about prevention/monitoring:

## Evidence Evaluation
[Any specific studies, claims, or information the user wanted to evaluate, with plain-language quality assessment]

## Red Flags to Be Aware Of
[1-3 relevant flags with plain-language explanation and suggested actions]

## Questions for My Medical Team

### My Top Questions (for this appointment)
[The 2-3 questions the user selected as highest priority — surfaced prominently so they're impossible to miss during a time-limited appointment]

### Full Question Bank
[All specific questions generated from the hypotheses, evidence evaluation, and red flags. Concrete and actionable — not generic. Saved here for future appointments or if there's time.]

## References
[All references drawn on to for all pieces of information and all questions presented in this document, presented in alphabetical order by author name using National Library of Medicine (NLM) citation style]

---
*This document was created as a thinking tool, not medical advice. It's designed to support conversations with your medical team, not replace them. Bring it to your next appointment, or use it for your personal reference. Be aware that how you frame search terms, and describe your symptoms, and what information you emphasize, will change what is surfaced in the literature review. It may be useful to run this search multiple times for the same set of symptoms.*
```
