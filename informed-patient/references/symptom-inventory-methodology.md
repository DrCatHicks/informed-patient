# Symptom Inventory Methodology: A Reference for Elicitation Best Practice

This reference grounds the skill's Phase 1 interview in measurement science. Use it to make better decisions about how to ask, when to press, when to use structured dimensions, and when to preserve the patient's own language.

---

## Why this matters

Symptom inventories are the foundation of clinical reasoning, but most are poorly designed. The majority of symptom instruments in clinical use were developed by clinicians without systematic input from patients, validated in narrow populations, and then applied universally. The result is instruments that are legible to clinicians but frequently miss what patients actually experience.

For this skill specifically, poor elicitation has two failure modes:
1. **Under-capture:** The patient describes something in their own words that doesn't map to the structured dimensions Claude collects, so important information is lost before it reaches the clinician
2. **Leading:** Asking about structured dimensions first anchors patients to the categories Claude offers rather than their own experience — this is the most common methodological error in survey design

The research on this is unambiguous: do open-ended elicitation first, and create structured dimensions second.

---

## The core tension: standardized vs. patient-generated

**Standardized symptom inventories** (structured dimensions: severity 0-10, frequency, duration, etc.) are valuable because:
- They're legible to clinicians who see many patients and need to make fast comparisons
- They map to validated outcome measures and diagnostic criteria
- They reduce recall error by giving patients concrete anchors

**Patient-generated descriptions** are valuable because:
- Patients experience symptoms in ways that don't map neatly to pre-defined categories
- The words a patient uses to describe a symptom can be diagnostically significant (e.g., "electric" vs. "aching" vs. "stabbing" pain)
- Forcing patients into pre-defined categories can cause them to omit or distort information that doesn't fit
- Many conditions, especially underdocumented, understudied, or rare conditions, have symptom presentations that standard inventories weren't designed to capture

**Best practice resolves this tension sequentially:** elicit freely first, then map to structured dimensions. This is the approach the skill uses, and it is empirically supported.

---

## Key principles with methodological grounding

### 1. Open-ended elicitation before structured dimensions

**Why:** Cognitive interviewing research shows that presenting response categories before asking for open description anchors respondents to those categories — they describe their experience in terms of the options they've been shown rather than their actual experience. This is a well-documented source of measurement error in survey design.

**In practice:** "What symptoms are you experiencing?" (free description first) before "On a scale of 0-10, how severe is the pain?" This is the correct sequence. Do not invert it.

**Source:** 

Willis, G. B. (2004). Cognitive interviewing: A tool for improving questionnaire design. sage publications.

---

### 2. Functional anchors are more reliable than abstract numeric scales

**Why:** The 0-10 numerical rating scale (NRS) for pain is widely used but has documented reliability problems: patients interpret the same number differently, and the same patient uses numbers differently across contexts. Functional anchors ("0 = no pain at all, 10 = worst pain imaginable, like breaking a bone") improve inter-rater and test-retest reliability.

The more clinically useful question is often not "rate your pain 0-10" but "what can't you do because of this?" This is a functional impact question. This is also what clinicians weight heavily in time-limited appointments, because it converts subjective experience into an observable, actionable problem.

**In practice:** Use numeric scales as a rough orientation, but always pair them with a functional anchor. The skill's required "one concrete functional impact statement" is grounded in this evidence.

**Source:** 

Farrar, J. T., Young Jr, J. P., LaMoreaux, L., Werth, J. L., & Poole, R. M. (2001). Clinical importance of changes in chronic pain intensity measured on an 11-point numerical pain rating scale. Pain, 94(2), 149-158. PMID: 11690728. This landmark paper established the concept of the Minimum Clinically Important Difference (MCID) for the NRS and demonstrated the limits of treating numeric pain ratings as continuous, interval-level data.

---

### 3. Content validity: does your inventory capture what matters to this patient?

**Why:** An inventory has *content validity* if it covers the domains that are actually relevant to the patient's experience. Standard instruments frequently fail content validity for understudied conditions, for conditions with heterogeneous presentations, and for patients whose demographics differ from the instrument's development population. The FDA has made content validity a regulatory requirement for patient-reported outcome instruments used in drug development — meaning this is not a theoretical concern.

**In practice:** After collecting structured dimensions, ask: "Is there anything about how this affects you that we haven't captured?" This is not a throwaway question — it is a content validity check. For conditions with unusual presentations or limited research, this question is especially important because standard categories may miss the most diagnostically significant aspects of the patient's experience.

**Source:** Patrick DL, Burke LB, Gwaltney CJ, et al. "Content validity—establishing and reporting the evidence in newly developed patient-reported outcomes (PRO) instruments for medical product evaluation." *Value in Health.* 2011;14(8):977-988. PMID: 21995957. 

---

### 4. Patient-generated measures capture things standardized instruments miss

**Why:** Patients often have symptom concerns or functional impacts that fall outside the domains any standard instrument assesses. The MYMOP (Measure Yourself Medical Outcome Profile) was developed specifically to address this: rather than asking patients to rate pre-defined domains, it asks patients to name the two symptoms or problems that matter most to them and rate those. Studies consistently show that patient-nominated items capture different, and often more important, concerns than clinician-generated items. In general, Patient-Centered Outcomes Measures (PCOMs) have the potential to systematically incorporate patient perspectives to measure those outcomes that matter most to patients.

**In practice:** This principle supports the skill's "co-occurrence" branching question. Patients often mentally file related symptoms as separate, unrelated problems. Asking "is there anything else going on, even things that seem unrelated?" is not optional. This provides a mechanism by which patient-generated symptom data surfaces alongside clinician-generated categories.

**Sources:** 

Paterson C. "Measuring outcomes in primary care: a patient generated measure, MYMOP, compared with the SF-36 health survey." *BMJ.* 1996;312(7037):1016-1020. PMID: 8616351. Paterson's development and validation of MYMOP is a foundational work on patient-generated outcome measures and demonstrates empirically that what patients most want to track is systematically different from what standard instruments measure.

Morel, T., & Cano, S. J. (2017). Measuring what matters to rare disease patients–reflections on the work by the IRDiRC taskforce on patient-centered outcome measures. Orphanet journal of rare diseases, 12(1), 171. Argues for argue for greater multi-stakeholder collaboration to develop PCOMs, with rare disease patients and families at the center, and proposes propose mixed methods psychometric research as the best route to deliver fit-for-purpose PCOMs in rare diseases, as this methodology brings together qualitative and quantitative research methods in tandem with the explicit aim to efficiently utilise data from small samples.

Garratt, A., Schmidt, L., Mackintosh, A., & Fitzpatrick, R. (2002). Quality of life measurement: bibliographic study of patient assessed health outcome measures. Bmj, 324(7351), 1417.  PMID: 12065262. PMC: PMC115850.
Key finding: Of 3,921 reports on PRO instruments, only 1% covered individualized measures. Directly states individualized measures "have measurement properties that are not captured by generic and specific measures based on summed rating scales."

Wiering, B., de Boer, D., & Delnoij, D. (2017). Asking what matters: the relevance and use of patient‐reported outcome measures that were developed without patient involvement. Health Expectations, 20(6), 1330-1341. What patients rate as highly important can be underweighted in standardized outcome measures that are developed without patient involvement.

---

### 5. The PROMIS framework: what validated patient-reported outcomes look like

The Patient-Reported Outcomes Measurement Information System (PROMIS) is a rigorously developed and validated bank of PRO instruments. Developed with NIH funding over 15+ years, PROMIS item banks cover physical function, pain interference, fatigue, sleep disturbance, anxiety, depression, and other domains, all developed with extensive patient input, cognitive interviewing, and large-scale psychometric validation across diverse populations.

PROMIS is relevant to this skill not as an instrument to administer directly, but as a benchmark for what *good* symptom measurement looks like:
- Items were developed with patient input (content validity)
- Items were cognitively tested before finalization
- Items use functional language, not just abstract ratings
- The same constructs are measured consistently across conditions
- Normative data allows comparison to general population

**Why this matters for elicitation:** When Claude helps a patient describe symptoms, the PROMIS domain framework is a useful reference for what dimensions matter. Pain *intensity* and pain *interference* (how much pain affects daily activities) are separate constructs. Both matter, and conflating them is a common error.

**Source:** Cella D, Riley W, Stone A, et al. "The Patient-Reported Outcomes Measurement Information System (PROMIS) developed and tested its first wave of adult self-reported health outcome item banks: 2005–2008." *Journal of Clinical Epidemiology.* 2010;63(11):1179-1194. PMID: 20685078. This is the primary development paper for PROMIS. Instruments are freely available at healthmeasures.net.

---

### 6. Symptom elicitation and the explanatory model

Patients come to medical encounters with their own theory of what is happening and why. Eliciting this model strengthens understanding and exchange, but it is not just about building rapport. Elicitation of patients' own mental models and theories about their health can directly change what information the patient volunteers and what they withhold. Patients who believe their symptom is caused by stress may minimize physical details they consider "irrelevant." Patients anchored on a specific diagnosis may omit symptoms that don't fit that diagnosis.

Arthur Kleinman's explanatory model framework — developed in medical anthropology but now widely used in clinical communication research — provides a theoretical grounding for why patient-centered elicitation matters. The key questions from Kleinman's model: What do you think is causing this? Why did it start when it did? What does it do to you? What do you fear most about it?

These are not questions the skill asks directly, but they represent the underlying information structure that free elicitation surfaces. Claude's instruction to ask "what prompted you to look into this now?" is a partial application of this principle. 

**Source:** Kleinman A, Eisenberg L, Good B. "Culture, illness, and care: clinical lessons from anthropologic and cross-cultural research." *Annals of Internal Medicine.* 1978;88(2):251-258. PMID: 626456. This is one of the most cited papers in clinical communication research and the foundational text for explanatory model elicitation in medicine.

---

## What this means for how Claude conducts Phase 1

**Do:**
- Start with free description before introducing any structured dimensions
- Use functional language: "what can't you do" before "rate your pain 0-10"
- Always close with an open check: "Is there anything about how this affects you that we haven't captured yet?"
- Preserve the patient's exact words in the symptom inventory where they're diagnostically or contextually significant — don't always translate into clinical language
- Treat the co-occurrence question as a patient-generated measure check, not an afterthought

**Don't:**
- Present structured dimensions (severity scale, frequency categories) before the patient has described freely
- Treat a 0-10 rating as the primary severity data — always pair it with a functional anchor
- Assume standard inventory dimensions cover everything — especially for understudied, rare, or complex conditions
- Rephrase the patient's symptom language into clinical terminology without noting the original description

**The content validity check (required):**
After collecting structured dimensions, always ask: "Is there anything about how this affects you that we haven't captured?" This is a mechanism by which important symptom information that falls outside standard categories can get surfaced. For conditions with heterogeneous presentations or limited research, this question frequently returns the most diagnostically significant data in the entire interview.
