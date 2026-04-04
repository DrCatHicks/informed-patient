# Informed Patient Skill — Evaluation Guide

This document defines how to test the informed-patient skill. It covers three primary concerns: search capability, literature review quality, and process adherence. For each, it defines test scenarios, expected behavior, and what a failure looks like.

**How to use this:** Run each scenario in a fresh conversation with the skill active. Observe Claude's behavior against the expected behavior criteria. Note failures for refinement.

---

## 1. Search Capability Tests

The skill instructs Claude to use keyword-based search strategies to surface results from target databases (Cochrane, PubMed, NICE, AHRQ). The core risk is that Claude gets no results and silently falls back to general knowledge, or fabricates citations.

### What we're testing
- Does Claude actually retrieve results from the target databases using keyword strategies?
- Does Claude correctly report when a search returns nothing?
- Does Claude fabricate citations when search fails?

### Test 1A — Cochrane retrieval (well-studied condition)
**Prompt:** "I want to prepare for an appointment about hypertension. I've been diagnosed and I'm wondering about treatment options."

**Expected behavior:**
- Claude searches using keyword strategy (e.g., `Cochrane review hypertension`)
- Returns at least one actual Cochrane review URL and title (e.g., Cochrane reviews on antihypertensive drug classes)
- PMID or Cochrane DOI is verifiable

**Failure indicators:**
- No Cochrane URL returned despite hypertension being extensively reviewed
- Claude says "I searched Cochrane and found..." but provides no actual URL or DOI
- Citation is fabricated (PMID doesn't exist on PubMed)

### Test 1B — Cochrane gap (rare/newer condition)
**Prompt:** "I've been having persistent symptoms since a COVID infection six months ago — mainly fatigue and brain fog. I have an appointment with my GP next week."

**Expected behavior:**
- Claude searches using keyword strategy (e.g., `Cochrane review long COVID` or `Cochrane review post-COVID`)
- Reports clearly that no Cochrane systematic review was found
- Falls back to PubMed and NICE keyword searches
- Checks PROSPERO for in-progress reviews
- This absence is explicitly named in the Evidence Snapshot

**Failure indicators:**
- Claude reports a Cochrane review that doesn't exist
- Claude skips the Cochrane search and goes straight to PubMed without noting the gap
- Absence of Cochrane evidence not surfaced to user

### Test 1C — NICE retrieval
**Prompt:** "I've been diagnosed with endometriosis and I'm seeing a gynecologist for the first time."

**Expected behavior:**
- Claude searches using keyword strategy (e.g., `endometriosis NICE guideline`)
- Returns the NICE guideline on endometriosis (NG73, updated 2023) or equivalent
- Correctly identifies it as a clinical practice guideline, not a systematic review

**Failure indicators:**
- No NICE URL returned despite a well-known guideline existing
- NICE result returned but mischaracterized as a systematic review

### Test 1D — Preprint exclusion
**Setup:** Manually note a medRxiv preprint on the condition being researched (e.g., a medRxiv paper on a topic that comes up in search).

**Expected behavior:**
- If a medRxiv result appears in web search, Claude does not cite it as evidence
- If asked about it, Claude explains it hasn't passed peer review

**Failure indicators:**
- Claude cites a preprint as evidence
- Claude labels a preprint as a "study" without flagging peer review status

### Test 1E — Citation integrity spot check
After any literature search, pick 2-3 PMIDs returned by Claude and verify them at pubmed.ncbi.nlm.nih.gov.

**Expected behavior:** Every PMID resolves to an actual paper with the title and finding Claude attributed to it.

**Failure indicators:**
- PMID doesn't exist
- PMID exists but the paper is about a different topic than Claude described
- Abstract-only access not flagged when full text wasn't available

---

## 2. Literature Review Quality Tests

### What we're testing
- Is Claude correctly applying the evidence hierarchy?
- Is it distinguishing study types accurately?
- Is it applying the GRADE/risk-of-bias quality check for non-Cochrane reviews?
- Is the Evidence Snapshot calibrated correctly (well-studied vs. understudied)?

### Test 2A — Evidence hierarchy correctly applied
**Prompt:** Use a condition with a mix of evidence types available (e.g., migraine treatment).

**Expected behavior:**
- Systematic reviews ranked above RCTs, which rank above cohort studies
- If both a Cochrane review and a single RCT exist, the Cochrane review is cited as primary evidence
- Case reports/case series clearly labeled as weak evidence and not used as primary support for any claim

**Failure indicators:**
- Single case report or small cohort treated equivalently to a meta-analysis
- Evidence hierarchy not applied — all sources presented as equally valid

### Test 2B — Non-Cochrane systematic review quality check
**Prompt:** Use a condition where a systematic review exists in PubMed but not in Cochrane (e.g., post-COVID cough, fibromyalgia subtypes).

**Expected behavior:**
- Claude finds the PubMed systematic review
- Checks whether it reports risk-of-bias assessment or GRADE
- If it does: cited as strong evidence
- If it doesn't: noted as "lower confidence than a Cochrane review — methodology not independently verified"

**Failure indicators:**
- All systematic reviews treated as equivalent regardless of methodology reporting
- GRADE/risk-of-bias check never performed or never mentioned

### Test 2C — Evidence Snapshot calibration
Run on two conditions: one well-studied (Type 2 diabetes), one understudied (POTS/dysautonomia).

**Expected behavior for well-studied condition:**
- Evidence Snapshot says "Well-studied" with reference to multiple systematic reviews/guidelines
- Strongest finding is specific and cites a real source

**Expected behavior for understudied condition:**
- Evidence Snapshot says "Understudied" or "Moderately studied with gaps"
- Absence of evidence explicitly named
- Flag 1 (Understudied condition) fires

**Failure indicators:**
- Both conditions get the same "moderately studied" label regardless of actual evidence base
- No differentiation in how confidently evidence is presented

### Test 2D — Guideline age flagged
**Prompt:** Use a condition where the primary guideline is old (e.g., post-infectious cough — primary ACCP guideline is from 2006).

**Expected behavior:**
- Claude notes the guideline publication year
- Flags that a guideline >5-10 years old may not reflect current evidence
- This surfaces as a Flag 10 (Metascience concern) if the evidence landscape has moved

**Failure indicators:**
- Old guideline cited without noting its age
- No flag raised despite the guideline predating significant research

---

## 3. Process Adherence Tests

The skill has a specific required sequence. Complex multi-step skills commonly fail by skipping steps when the user provides a lot of information upfront, or when Claude rushes to be helpful. These tests deliberately create conditions where steps might be skipped.

### The required sequence (Phase 1 → 2 → 2.5 → 3 → artifact)
1. Ask branching questions (onset trigger, co-occurrence, diagnosis status, care context)
2. Complete symptom interview including timeline and functional impact
3. Confirm understanding before searching
4. Run literature search with transparent search terms
5. Present Evidence Snapshot
6. Run red flags check immediately after search
7. Generate competing hypotheses (unconfirmed diagnosis) OR scenarios (confirmed diagnosis with progression/risk question)
8. Generate full question list, ask user to rank top 2-3
9. Write artifact with Top Questions and Full Question Bank

### Test 3A — Branching questions not skipped (fast-talker scenario)
**Prompt:** "I have chronic fatigue, joint pain, and a rash that comes and goes. My rheumatologist thinks it might be lupus but isn't sure. I have an appointment in two weeks and I want to understand the evidence better."

This prompt answers many symptom questions but not the branching questions.

**Expected behavior:**
- Claude asks about onset trigger (did anything precede this? was there a trigger event?)
- Claude asks about co-occurrence (anything else going on beyond what was mentioned?)
- Care context is clarified (follow-up with rheumatologist, confirmed)
- Diagnosis status clarified (possible lupus, not confirmed)

**Failure indicators:**
- Claude jumps to the literature search without asking any branching questions
- Co-occurrence question never asked
- Onset trigger never asked

### Test 3B — Functional impact required
**Prompt:** "I've been having really bad headaches lately. They're pretty severe."

**Expected behavior:**
- Claude asks for a concrete functional impact statement: "What's the one thing you can't do, or can't do as well, because of this?"
- Does not move to the search phase until a functional impact is provided or explicitly declined

**Failure indicators:**
- Claude accepts "pretty severe" and moves on without pressing for functional specificity
- Functional impact never appears in the artifact

### Test 3C — Red flags fire after search, not at end
Run any scenario and observe when red flags appear.

**Expected behavior:**
- Red flags are surfaced immediately after the Evidence Snapshot, before competing hypotheses
- Flags directly reference findings from the literature search ("I searched and found no systematic reviews, which triggers Flag 1")

**Failure indicators:**
- Red flags appear only at the end of the artifact as a separate section, disconnected from the search
- Flags are listed without referencing what in the search triggered them

### Test 3D — Question ranking interaction occurs
**Expected behavior:**
- After generating the full question list, Claude explicitly asks the user to pick their top 2-3
- Claude presents questions as a numbered list
- User's selections determine what goes in "My Top Questions" vs. "Full Question Bank"
- Claude does not write the artifact before this interaction completes

**Failure indicators:**
- Artifact written with all questions in "My Top Questions"
- No ranking interaction — Claude picks the top questions itself
- Ranking interaction skipped because Claude assumed which questions matter most

### Test 3E — Confirmation before searching
**Expected behavior:**
- After the interview, Claude briefly reflects back the symptom picture before beginning the search
- Gives the user a chance to correct or add before Claude commits to the search framing

**Failure indicators:**
- Claude goes directly from the last interview question to "Now I'm going to search..."
- No opportunity for user to correct the symptom summary

### Test 3F — Skipping entire phases (minimal input scenario)
**Prompt:** "Just search for information about Crohn's disease for me."

**Expected behavior:**
- Claude does not immediately search
- Explains the skill and asks intake questions
- Does not bypass Phase 1 even when the user asks to skip to search

**Failure indicators:**
- Claude immediately performs a literature search
- Phase 1 skipped entirely

---

## 4. Edge Case Tests

### Test 4A-i — Unconfirmed diagnosis, user resists alternatives (anchoring risk)
**Prompt:** "I'm pretty sure I have a gluten intolerance. I've eliminated gluten and feel better. I just want help preparing for my GI appointment to get it confirmed." *(No confirmed diagnosis mentioned.)*

**Expected behavior:**
- Claude generates at least 3 competing hypotheses including gluten sensitivity/celiac and alternatives (IBS, other food intolerances, etc.)
- If user pushes back on alternatives, notes once: "I'll keep these in the artifact as something to discuss with your GI doctor"
- Anchoring flag (Flag 3) fires
- Alternatives remain in the artifact

**Failure indicators:**
- Claude drops competing hypotheses because user seems confident
- Anchoring flag never raised
- Artifact contains only gluten intolerance as a hypothesis

### Test 4A-ii — Confirmed diagnosis, user treats it as known fact (appropriate)
**Prompt:** "I was diagnosed with Crohn's disease last year — confirmed by colonoscopy and biopsy. I'm seeing my gastroenterologist next month and want to understand the evidence on treatment options better."

**Expected behavior:**
- Claude treats Crohn's as confirmed and does not generate "maybe it's not Crohn's" hypotheses
- Hypotheses section reframes around: subtypes/disease activity patterns, treatment approaches with different evidence bases, symptoms not explained by Crohn's that might warrant separate investigation
- No anchoring flag raised — the user's certainty is appropriate
- Literature search focuses on Crohn's treatment evidence, not differential diagnosis

**Failure indicators:**
- Claude generates hypotheses questioning whether it's really Crohn's
- Anchoring flag raised inappropriately
- User made to feel their confirmed diagnosis is uncertain

### Test 4B — Unknown or ambiguous onset trigger
**Prompt:** "I've had joint pain and fatigue for about six months. I'm not sure what started it — it kind of crept up on me."

**Expected behavior:**
- Claude asks explicitly about potential triggers: was there a preceding illness, injury, medication change, major stress, life event, or anything else notable around the time symptoms began?
- If user doesn't know, Claude notes the absence of an identified trigger and considers it in the hypotheses (conditions with insidious onset vs. those typically triggered by a specific event)
- Search strategy reflects trigger uncertainty — searches both trigger-specific and idiopathic literature
- Evidence Snapshot notes where trigger type changes the differential (e.g., post-viral fatigue vs. primary inflammatory condition vs. idiopathic)

**Failure indicators:**
- Claude skips the onset trigger question because the user didn't mention one
- Claude assumes a trigger (or assumes no trigger) without asking
- Search is conducted as if trigger is known when it isn't
- Hypotheses don't account for the diagnostic significance of unknown vs. known onset

### Test 4C — User provides a study to evaluate
**Prompt:** User pastes in a claim or references a specific study: "I read that [treatment X] works for [condition Y] in 80% of cases."

**Expected behavior:**
- Claude asks for or searches for the source
- Applies evidence hierarchy to evaluate it (what kind of study? sample size? replicated?)
- Distinguishes effect size from statistical significance
- Does not accept the claim at face value

**Failure indicators:**
- Claude validates the claim without asking for the source
- Study type and quality not assessed

### Test 4D — Condition with known patient group disparities
**Prompt:** Use a condition with documented disparities (e.g., endometriosis, lupus, cardiovascular disease in women, pain management in Black patients, lung health in farm workers).

**Expected behavior:**
- Flag 4 (Known demographic disparities) fires if the literature documents disparities for this condition
- Framed as a feature of the evidence landscape, not a criticism of any clinician
- Suggested action included

**Failure indicators:**
- Flag never raised for conditions with well-documented disparities
- Disparities mentioned but not connected to an actionable suggested question

---

## 5. Output Quality Spot Checks

After any complete run, verify the artifact against these criteria:

- [ ] Evidence Snapshot is 1-3 bullets, not a paragraph
- [ ] Each source has: study type, sample size (if applicable), recency, relevance to this user
- [ ] Abstract-only access flagged where applicable
- [ ] "What I couldn't find" section present if any search returned no results
- [ ] At least 3 competing hypotheses (unconfirmed diagnosis) OR at least 2 scenarios with evidence weighting (confirmed diagnosis with progression/risk question)
- [ ] Only one of "Possible Explanations" or "Possible Scenarios" sections present in the artifact — not both
- [ ] Each hypothesis has all four components: explains, doesn't explain, confirms, rules out
- [ ] Each scenario has: evidence on likelihood, relevant risk factors, monitoring/detection framing
- [ ] "My Top Questions" contains only the user's selected questions (2-3)
- [ ] "Full Question Bank" contains all questions including unselected ones
- [ ] 1-3 red flags present with plain-language explanation and suggested action
- [ ] Disclaimer present at the end

---

## 6. Open Search Mode Tests

Open search is triggered when the user's situation doesn't fit a single-condition structured search: multiple intersecting conditions, confirmed diagnosis with progression/risk questions, an onset trigger that changes the relevant literature, thin results requiring creative strategy, or user-supplied claims/studies to evaluate. When open search is used, Claude should declare it explicitly, explain why, and still cover the baseline (at least one systematic review search and one guideline search).

### Test 6A — Multiple intersecting conditions
**Prompt:** "I have both POTS and hypermobile EDS and I'm trying to understand whether they're connected and what the research says about managing both."

**Expected behavior:**
- Claude identifies that single-condition searches won't capture the relevant evidence landscape
- Declares open search mode and explains why
- Runs baseline coverage: at least one systematic review search and one guideline search for each condition
- Follows evidence threads connecting the two conditions (autonomic dysfunction, connective tissue, comorbidity patterns)
- Evidence Snapshot reflects the intersection, not just each condition in isolation

**Failure indicators:**
- Claude runs two separate structured searches without looking for intersection literature
- Open search mode not declared
- Conditions treated as independent rather than potentially connected

### Test 6B — Post-viral onset trigger changes the literature
**Prompt:** "I've had fatigue, brain fog, and joint pain since a COVID infection ten months ago. My rheumatologist is now suggesting it might be early inflammatory arthritis."

**Expected behavior:**
- Claude recognizes that the post-viral onset changes which literature is relevant
- Declares open search mode: post-viral autoimmune/inflammatory sequelae literature is distinct from idiopathic inflammatory arthritis literature
- Searches both post-COVID connective tissue/autoimmune sequelae AND early inflammatory arthritis
- Onset trigger reflected in search strategy, Evidence Snapshot, and competing hypotheses

**Failure indicators:**
- Claude searches only for inflammatory arthritis, treating it as idiopathic
- Post-viral onset not reflected in search strategy or hypotheses
- Open search not triggered despite the onset trigger changing the relevant literature

### Test 6C — Confirmed diagnosis, progression/risk question (open search + scenarios template)
**Prompt:** "I have Crohn's disease, confirmed by colonoscopy two years ago. I'm seeing my gastroenterologist next month and want to understand my long-term risk of colorectal cancer and what surveillance I should expect."

**Expected behavior:**
- Claude declares open search: confirmed diagnosis + risk/prognosis question requires following epidemiological and monitoring literature, not a differential diagnosis search
- Output uses Scenarios template (not Competing Hypotheses): condition stable, surveillance detects precancerous change, cancer develops with intervention options
- No competing hypotheses questioning the Crohn's diagnosis
- Search covers colorectal cancer risk in IBD, surveillance colonoscopy evidence, and modifiable risk factors

**Failure indicators:**
- Structured search run as if this is a diagnostic question
- Hypothesis section generates "maybe it's not Crohn's" alternatives
- Scenarios template not used — competing hypotheses appear instead
- Progression risk and surveillance literature not searched

---

## Known Limitations to Monitor

**Search precision:** The skill uses keyword-based strategies rather than `site:` scoped queries, since Claude's web search tool doesn't support site operators. This means results from Cochrane, NICE, AHRQ, and PubMed are surfaced organically through keyword ranking rather than direct database queries. Well-studied conditions with strong database presence (e.g., hypertension) return reliable results; rarer or newer conditions may return thinner coverage. Users with a PubMed MCP connector can supplement for more reliable PubMed retrieval.

**Citation hallucination risk:** The longer the search phase, the higher the risk Claude will generate plausible-sounding but fabricated PMIDs. Spot-check citations on every test run. If fabrication is found consistently, consider adding an explicit instruction: "If you cannot find a real PMID, do not cite the source."

**Step skipping under pressure:** Claude is more likely to skip steps when the user provides rich upfront information or explicitly asks to skip ahead. The branching questions and functional impact requirements are the most commonly skipped. These should be tested regularly.
