# Literature Search Strategy: Source Hierarchy and Query Templates

This reference gives the exact search queries, source-by-source rationale, and warning conditions for the **structured search** mode described in the informed-patient skill's Phase 2. Use it when running the source hierarchy; refer back to the skill for when to use open search instead, and for how to present results (transparency, tagging, the Evidence Snapshot).

## Source hierarchy: query templates by source type

Use web search to find evidence across these source types, in priority order.

### 1. Systematic reviews — cast a wide net, not just Cochrane

Cochrane is the gold standard for systematic reviews because of its standardized methodology, but it has a meaningful blind spot: it tends to cover high-burden conditions with ample RCT evidence. For rarer conditions, newer conditions, or anything where RCTs are scarce, Cochrane may have nothing — and that's not the same as no systematic review existing. Search all of these:

- `Cochrane review [condition]` — Cochrane first. **If this returns no results, do not silently skip it.** Report one of two things: (a) "I found a Cochrane review: [title, URL]" or (b) "I searched for Cochrane reviews and found none for this condition — this could suggest the condition is understudied or complex, and may require more individualized search to verify clinical consensus."
- `[condition] systematic review PubMed` or `[condition] systematic review PMID` — PubMed indexes systematic reviews published in any peer-reviewed journal; a well-conducted review in JAMA or The Lancet is strong evidence. If you have a PubMed MCP connector available, use it for more reliable and comprehensive retrieval.
- `[condition] NICE guideline` — NICE (UK) produces high-quality evidence reviews as part of guideline development, often covering conditions Cochrane hasn't addressed.
- `[condition] AHRQ evidence review` — AHRQ (US) commissions systematic reviews via Evidence-Based Practice Centers. **Do not silently skip this** (see SKILL.md's Phase 2 for why). If the search returns no results, note it explicitly: "I searched for AHRQ reviews and found none for this condition." If strong Cochrane coverage already exists and you're stopping early, still note the skip: "AHRQ not searched — Cochrane and guideline coverage was sufficient."

**Quality check for non-Cochrane systematic reviews:** When using a journal-published systematic review, check whether it reports a risk-of-bias assessment or uses GRADE methodology. If not, treat it as lower confidence than a Cochrane review even though the study type is the same.

**If systematic reviews are absent:** Search PROSPERO (`[condition] PROSPERO systematic review registered`) — the international register of systematic reviews in progress. Finding a registered in-progress review is itself useful information: tell the user that research is underway but not yet published.

### 2. Clinical practice guidelines

Search for current guidelines from major bodies (ACP, NICE, WHO, relevant specialty societies). Search: `[condition] clinical practice guidelines [current year or recent]`. Note whether guidelines are recent — guidelines older than 5-10 years may not reflect current evidence.

### 3. Peer-reviewed primary research

If systematic reviews are thin, search PubMed for the best available primary studies, prioritizing RCTs and prospective cohorts over retrospective and case studies. Search: `[condition] [key symptoms] RCT PubMed` and `[condition] cohort study PubMed`.

### 4. FDA/regulatory information

If treatments are being discussed, check for FDA-approved indications, black box warnings, or recent safety communications. This applies to drug classes as well as specific drug names. Search: `FDA [drug class or drug name] [condition]` (e.g., `FDA ACE inhibitors hypertension` or `FDA lisinopril approval`).

### 5. Patient advocacy organizations

For time-to-diagnosis data, patient-reported experience, and practical information that doesn't appear in clinical literature. Search: `[condition] patient advocacy` or `[condition] foundation`. These are context, not clinical evidence.

## Source-level warning conditions (flag with ⚠️ inline)

When a source has a nuanced issue that affects how much weight to give it, flag it directly in the source entry with a ⚠️ and a one-sentence explanation. Do not bury these caveats in prose — make them impossible to miss.

- Guidelines older than 5-10 years: ⚠️ _Published [year] — check the link to see if an update has been issued._
- Abstract-only access: ⚠️ _Only the abstract was available — full methodology not reviewed._
- No risk-of-bias assessment in a non-Cochrane systematic review: ⚠️ _This review does not report a risk-of-bias assessment — treat as lower confidence than a Cochrane review._
- Small sample size relative to the claim being made: ⚠️ _[N] participants — findings may not generalize._
- Population mismatch with the user: ⚠️ _Study population was [X] — relevance to your situation is uncertain._
