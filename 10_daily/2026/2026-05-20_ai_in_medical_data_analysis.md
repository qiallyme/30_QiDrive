---
layout: page
title: "AI in Medical Data Analysis"
slug: "ai_in_medical_data_analysis"
created_at: "2026-05-20 21:43:33"
updated_at: "2026-05-20 21:43:33"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-007.json"
template_key: master-template
date: 2026-05-20
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a0e711a-4100-83ea-9d3b-a9910fab8671"
canonical_ref: ""
---

# AI in Medical Data Analysis

## Overview
- **Date**: 2026-05-20 21:43:33
- **Conversation ID**: `6a0e711a-4100-83ea-9d3b-a9910fab8671`
- **Source**: `Chat-Export-28513-2026/conversations-007.json`

## Chat History

### User
> how do you use ai to analyze medical or health data of a patient to systematically and accuractly identify the underlying issues, interactions ect, that effect a pesons health or may reveal insights overlooks or patterns missed.

### Assistant
> I’ll frame this as a practical system, not “throw symptoms into ChatGPT and hope.” The key is separating data intake, clinical validation, pattern detection, and escalation so AI supports judgment instead of hallucinating over someone’s health.

### Assistant
> Yes — this is exactly where AI can be useful **if you build the workflow correctly**.
> 
> The mistake is using AI like an oracle: “Here are symptoms, what’s wrong?”  
> The better model is: **AI as a clinical pattern engine + documentation analyst + interaction checker + timeline builder + question generator.**
> 
> It does **not replace a clinician**, but it can absolutely help identify overlooked patterns, contradictions, medication interactions, timing triggers, and gaps in the record.
> 
> ## The core system
> 
> ### 1. Build a clean patient timeline
> 
> Start with time, not diagnosis.
> 
> Create one chronological record with:
> 
> | Category | Examples |
> |---|---|
> | Symptoms | shortness of breath, anxiety, dizziness, rash, swelling, confusion |
> | Vitals | oxygen, heart rate, BP, temp, glucose, weight |
> | Medications | name, dose, time taken, missed doses, PRN use |
> | Conditions | COPD, diabetes, heart issues, kidney issues, allergies |
> | Events | ER visits, falls, infections, med changes, stress episodes |
> | Labs/imaging | CBC, CMP, glucose, BNP, troponin, X-ray, CT, EKG |
> | Environment | heat, cold, dust, smoke, exertion, sleep, food, hydration |
> | Behavior/context | talking nonstop, panic, refusal of meds, poor sleep, eating patterns |
> 
> This is the foundation. No clean timeline = garbage analysis.
> 
> AI is good at turning scattered notes into structured timelines, but humans must verify the facts.
> 
> ---
> 
> ### 2. Separate facts from interpretation
> 
> This matters big time.
> 
> Bad note:
> 
> > “She was acting anxious and making herself worse.”
> 
> Better note:
> 
> > “At 3:20 PM, HR 150, O2 95%, talking continuously, reported air hunger, refused hydroxyzine, had used albuterol earlier, symptoms worsened during prolonged talking and improved when quiet.”
> 
> That lets AI compare patterns without getting emotionally contaminated.
> 
> You can still include observations — just label them:
> 
> | Type | Example |
> |---|---|
> | Objective | HR 150, O2 95%, BP 107/56 |
> | Subjective | “Patient says she cannot breathe” |
> | Observed behavior | “Talking continuously despite dyspnea” |
> | Inference | “Anxiety may be worsening breathing pattern” |
> | Question | “Could albuterol/prednisone be increasing anxiety/tachycardia?” |
> 
> That structure is how you stop the AI from spiraling.
> 
> ---
> 
> ### 3. Use AI for pattern detection, not final diagnosis
> 
> AI can look across the timeline and ask:
> 
> - Do symptoms worsen after certain meds?
> - Does heart rate spike after albuterol, prednisone, caffeine, pain, panic, exertion, low oxygen, dehydration, infection, or missed anxiety meds?
> - Are glucose spikes tied to steroids or meals?
> - Are symptoms worse at certain times of day?
> - Are there medication interactions?
> - Are multiple drugs causing the same side effect?
> - Are “COPD symptoms” actually overlapping with anxiety, cardiac strain, infection, reflux, anemia, dehydration, or medication effects?
> - Are clinicians treating individual episodes but missing the whole pattern?
> 
> That last one is the gold.
> 
> Clinical decision support systems are already used for things like dose suggestions, drug allergy checks, and drug–drug interaction alerts, but they can malfunction or be poorly implemented, so they should support—not replace—clinical judgment. citeturn792440search6turn792440search17
> 
> ---
> 
> ## The actual AI workflow I’d use
> 
> ### Layer 1 — Data capture
> 
> Use a simple form or spreadsheet:
> 
> | Time | Vital | Symptom | Med taken | Food | Trigger | Notes |
> |---|---|---|---|---|---|---|
> 
> Example:
> 
> | Time | HR | O2 | BP | Symptom | Med | Context |
> |---|---:|---:|---|---|---|---|
> | 8:10 AM | 113 | 95 | — | air hunger | prednisone | talking a lot |
> | 12:45 PM | 150 | 95 | — | panic/dyspnea | refused hydroxyzine | continuous talking |
> | 1:20 PM | 164 | — | — | distress | albuterol earlier | EMS called |
> 
> The AI can then summarize:
> 
> > “Oxygen remained acceptable while heart rate was high, suggesting distress may not be purely oxygen-driven. Consider medication effects, anxiety/panic physiology, dehydration, infection, cardiac load, pain, or steroid/albuterol effects.”
> 
> That is not a diagnosis. It is a better clinical question.
> 
> ---
> 
> ### Layer 2 — Medication and interaction map
> 
> Feed AI a verified medication list:
> 
> | Medication | Dose | Schedule | Purpose | Side effects to watch |
> |---|---|---|---|---|
> 
> Then ask it to flag:
> 
> - duplicate effects  
> - interactions  
> - timing conflicts  
> - meds that raise heart rate  
> - meds that raise glucose  
> - meds that worsen anxiety  
> - meds that cause sedation/falls  
> - meds that interact with COPD, heart disease, kidneys, diabetes, etc.
> 
> This is one of the highest-value uses.
> 
> For example, in a COPD-type situation, AI should know to ask about:
> 
> - rescue inhaler frequency  
> - steroid timing  
> - anxiety meds taken or refused  
> - oxygen saturation trend  
> - heart rate trend  
> - infection signs  
> - glucose elevation from steroids  
> - sedating meds increasing fall risk  
> - whether “air hunger” matches oxygen readings  
> 
> But every medication conclusion should be verified by a pharmacist or prescribing clinician.
> 
> ---
> 
> ### Layer 3 — Differential hypothesis table
> 
> You want AI to produce a ranked table like this:
> 
> | Possible issue | Evidence supporting | Evidence against | What to check next | Urgency |
> |---|---|---|---|---|
> | COPD flare | dyspnea, rescue meds, congestion | O2 stable at 95 | wheeze, sputum, fever, response to neb | medium/high |
> | Anxiety/panic overlay | talking nonstop, refuses hydroxyzine, HR spikes | still has real COPD | timing, calming response, med triggers | medium |
> | Medication effect | prednisone/albuterol can increase jitteriness/HR/glucose | not enough timing data | exact dose/time log | medium |
> | Infection | congestion, flare pattern | no fever so far | temp trend, sputum color, WBC if labs | medium |
> | Cardiac strain/arrhythmia | HR 150–164 | unknown EKG | EKG, chest pain, BNP/troponin if acute | high |
> 
> This is the clinical reasoning structure. The point is not “AI says it’s anxiety.” The point is **AI shows what evidence points where and what data is missing**.
> 
> ---
> 
> ### Layer 4 — Red flag detection
> 
> AI should be configured to stop analysis and escalate when red flags appear.
> 
> Examples:
> 
> - oxygen persistently below prescribed safe range
> - heart rate sustained over 130–150, especially with distress
> - chest pain, blue lips, confusion, fainting
> - one-sided weakness, slurred speech
> - severe allergic reaction
> - new severe swelling
> - severe blood pressure drop
> - uncontrolled glucose with symptoms
> - repeated falls
> - worsening breathing despite treatment
> 
> This is where AI should say: **“This is not a pattern-analysis moment. This needs urgent medical evaluation.”**
> 
> For AI in health, WHO emphasizes governance, safety, transparency, privacy, and human oversight, especially for large multimodal models used in health contexts. citeturn792440search2turn792440search12
> 
> ---
> 
> ## Best prompt structure
> 
> Use this kind of prompt:
> 
> > Analyze the following patient timeline as a clinical reasoning assistant, not as a diagnosing physician.  
> > Separate objective facts from subjective reports and caregiver observations.  
> > Identify recurring patterns, possible medication effects, possible interactions, missing data, red flags, and questions to ask the clinician.  
> > Rank hypotheses by urgency and evidence strength.  
> > Do not invent facts. If data is missing, say what is missing.  
> > Output: timeline summary, pattern findings, medication concerns, red flags, clinician questions, and next tracking steps.
> 
> That prompt is strong because it forces the AI to show its work in a structured way without pretending to be a doctor.
> 
> ---
> 
> ## What data gives the best signal
> 
> Highest-value inputs:
> 
> 1. **Medication list with exact times**
> 2. **Vitals over time**
> 3. **Symptom onset and offset**
> 4. **Recent med changes**
> 5. **ER discharge papers**
> 6. **Labs**
> 7. **Imaging reports**
> 8. **Diagnosis list**
> 9. **Allergies**
> 10. **What improved or worsened symptoms**
> 
> Lowest-value inputs:
> 
> - emotional summaries only
> - vague “she was bad today”
> - screenshots without dates
> - unverified med names/doses
> - mixing multiple days together
> 
> The brutal truth: AI is only as useful as the structure you give it.
> 
> ---
> 
> ## Best tools for this
> 
> You can use different levels:
> 
> ### Basic
> 
> - Google Sheet / Excel
> - ChatGPT for summaries
> - Medisafe or phone reminders
> - PDF folder for discharge papers
> 
> ### Better
> 
> - Airtable / NocoDB
> - Structured forms for vitals/meds/events
> - PDF OCR through Paperless-ngx
> - AI summarizer over the records
> 
> ### Strongest
> 
> - Local health knowledge base
> - Timeline database
> - Medication table
> - Lab result table
> - Visit note table
> - RAG search over medical documents
> - AI-generated weekly clinical summary
> 
> For your kind of systems brain, the right model is basically:
> 
> > **Patient Event Ledger + Medication Graph + Clinical Timeline + AI Pattern Review**
> 
> That’s the architecture.
> 
> ---
> 
> ## What AI should produce for a doctor
> 
> Do **not** bring a 40-page emotional log.
> 
> Bring a one-page clinical summary:
> 
> **1. Main concern:**  
> Repeated episodes of dyspnea/air hunger with high heart rate.
> 
> **2. Pattern noticed:**  
> Oxygen sometimes remains acceptable while heart rate spikes, especially during anxiety/talking/exertion/medication periods.
> 
> **3. Medication concerns:**  
> Need review of steroid, rescue inhaler, anxiety med, glucose, sedation/fall risk.
> 
> **4. Data attached:**  
> Vitals table, medication timing, ER visits, symptom timeline.
> 
> **5. Questions:**  
> - Could this be COPD flare plus anxiety/panic overlay?
> - Could prednisone or albuterol be worsening tachycardia/anxiety/glucose?
> - Should there be a clear action plan for when HR rises but oxygen is stable?
> - What vitals require ER vs home management?
> - Should cardiology, pulmonology, pharmacy, or home health review the full med list?
> 
> That gets taken seriously.
> 
> ---
> 
> ## Guardrails
> 
> Use AI for:
> 
> - organizing records
> - detecting patterns
> - generating questions
> - summarizing visits
> - checking medication interaction possibilities
> - preparing doctor-facing documentation
> 
> Do **not** use AI for:
> 
> - independently diagnosing
> - changing medication doses
> - deciding not to seek emergency care
> - overriding discharge instructions
> - interpreting dangerous symptoms casually
> - assuming “it’s anxiety” just because anxiety is present
> 
> FDA distinguishes between general clinical decision support and software that may qualify as a regulated medical device, and it maintains a public list of AI-enabled medical devices authorized for marketing in the U.S. citeturn792440search0turn792440search10 ONC also now has transparency requirements for predictive algorithms in certified health IT, which matters because clinicians need to know what an algorithm is doing and whether it is valid, fair, and safe. citeturn792440search4
> 
> ## The cleanest answer
> 
> AI can help uncover overlooked health patterns by turning messy patient data into:
> 
> 1. a verified timeline  
> 2. a medication-interaction map  
> 3. a symptom/vitals correlation table  
> 4. a ranked hypothesis list  
> 5. red-flag alerts  
> 6. doctor-ready questions  
> 7. concise clinical summaries  
> 
> The win is not “AI finds the disease.”  
> The win is **AI makes the invisible pattern visible enough that a human clinician can act on it.**

### User
> i want the schema for a clinical analytical ai agent take the normalized data in the database, create the graphs and analyze, predict, or find solutions. big big issue is medicaiton interaction along site otcs and foods but not forgetting environment and behavior. This is a private project so regularoty concerns are not an issue and this will be provided as a place to start with the doctors not the diagnosis just where to look.

### Assistant
> Yes — this is the right architecture: not a diagnosis bot, but a **clinical intelligence layer** that converts normalized records into graphs, interaction maps, risk signals, and doctor-facing leads. I’ll give you a usable schema spine with entities, relationships, scoring tables, and agent outputs.

### Assistant
> Absolutely. The clean build is:
> 
> > **Normalized clinical database → interaction graph → temporal pattern engine → risk scoring → doctor-facing leads.**
> 
> Not “AI diagnosis.”  
> More like: **medical systems analyst that says, “These are the 7 places worth looking, and here’s why.”**
> 
> Below is the schema spine I’d use.
> 
> ---
> 
> # Clinical Analytical AI Agent Schema
> 
> ## 0. Design principle
> 
> You need **three layers**:
> 
> 1. **Relational normalized data**  
>    Clean tables for patient, meds, vitals, symptoms, labs, behaviors, environment, food, events.
> 
> 2. **Graph layer**  
>    Connects medications, OTCs, foods, symptoms, conditions, labs, behaviors, environments, and timing.
> 
> 3. **Analytical output layer**  
>    Stores hypotheses, risk flags, interaction findings, confidence, evidence, and doctor questions.
> 
> Use standard vocabularies where possible: **RxNorm** for medications, **LOINC** for labs/observations, and **SNOMED CT** for clinical findings/conditions. RxNorm provides normalized drug names and links across pharmacy vocabularies; LOINC is widely used for health measurements and lab observations; SNOMED CT is designed as a broad clinical terminology standard. citeturn779112search8turn779112search17turn779112search13
> 
> ---
> 
> # 1. Core entities
> 
> ## `patients`
> 
> One row per person.
> 
> | Field | Type | Notes |
> |---|---|---|
> | patient_id | uuid | primary key |
> | display_name | text | internal/private |
> | dob | date | optional |
> | sex_at_birth | text | optional but clinically relevant |
> | height_cm | numeric | optional |
> | baseline_weight_kg | numeric | optional |
> | baseline_o2_range | text | useful for COPD/pulmonary |
> | primary_conditions_summary | text | human-readable |
> | created_at | timestamptz |  |
> 
> ---
> 
> ## `conditions`
> 
> Known diagnoses or suspected conditions.
> 
> | Field | Type | Notes |
> |---|---|---|
> | condition_id | uuid |
> | patient_id | uuid |
> | condition_name | text |
> | snomed_code | text | optional |
> | status | text | active, resolved, suspected, ruled_out |
> | onset_date | date |
> | severity | text |
> | source | text | doctor, discharge paper, caregiver observation |
> | evidence_ref | uuid | link to document/event |
> | notes | text |
> 
> Examples:
> 
> - COPD
> - anxiety disorder
> - diabetes
> - hypertension
> - kidney disease
> - heart failure
> - medication allergy
> - fall risk
> 
> ---
> 
> ## `allergies_intolerances`
> 
> This needs to be separate from regular conditions.
> 
> | Field | Type | Notes |
> |---|---|---|
> | allergy_id | uuid |
> | patient_id | uuid |
> | substance_name | text |
> | substance_type | text | drug, food, environmental, latex, unknown |
> | rxnorm_code | text | if drug |
> | reaction | text |
> | severity | text |
> | certainty | text | confirmed, suspected, historical |
> | source | text |
> | last_reaction_date | date |
> 
> ---
> 
> # 2. Medication schema
> 
> This is the heart of the system.
> 
> ## `substances`
> 
> Master table for anything consumed or exposed to.
> 
> | Field | Type | Notes |
> |---|---|---|
> | substance_id | uuid |
> | name | text |
> | substance_type | text | prescription, OTC, supplement, food, beverage, environmental, chemical |
> | rxnorm_code | text |
> | ingredient_name | text |
> | ingredient_rxnorm_code | text |
> | drug_class | text |
> | known_stimulant | boolean |
> | known_sedating | boolean |
> | known_glucose_effect | text | raises, lowers, variable, unknown |
> | known_bp_effect | text |
> | known_hr_effect | text |
> | notes | text |
> 
> This lets you treat **prednisone, albuterol, hydroxyzine, caffeine, grapefruit, alcohol, nicotine, Benadryl, peanut butter, oxygen, cleaning fumes, dust, heat** as comparable graph objects.
> 
> That matters because the body does not care whether something came from a prescription bottle, a grocery bag, or the air vent. Exactly.
> 
> ---
> 
> ## `medication_orders`
> 
> What the patient is supposed to take.
> 
> | Field | Type | Notes |
> |---|---|---|
> | med_order_id | uuid |
> | patient_id | uuid |
> | substance_id | uuid |
> | prescribed_name | text |
> | dose_amount | numeric |
> | dose_unit | text |
> | route | text | oral, inhaled, topical, injection |
> | frequency | text |
> | start_date | date |
> | end_date | date |
> | prescribing_provider | text |
> | indication | text | why prescribed |
> | prn | boolean |
> | max_daily_dose | text |
> | instructions | text |
> | active_status | text |
> 
> ---
> 
> ## `medication_administrations`
> 
> What actually happened.
> 
> | Field | Type | Notes |
> |---|---|---|
> | med_admin_id | uuid |
> | patient_id | uuid |
> | substance_id | uuid |
> | med_order_id | uuid nullable |
> | taken_at | timestamptz |
> | dose_amount | numeric |
> | dose_unit | text |
> | route | text |
> | taken_status | text | taken, refused, missed, vomited, unknown |
> | reason_given | text |
> | observed_effect | text |
> | source | text | self-report, caregiver, pillbox, device |
> | confidence | numeric | 0–1 |
> | notes | text |
> 
> This table is where the real truth lives. The prescription list is theory. This table is reality.
> 
> ---
> 
> ## `medication_effect_windows`
> 
> Expected effect timing.
> 
> | Field | Type | Notes |
> |---|---|---|
> | effect_window_id | uuid |
> | substance_id | uuid |
> | effect_type | text | onset, peak, duration |
> | min_minutes | int |
> | max_minutes | int |
> | evidence_source | text |
> | notes | text |
> 
> This lets the agent ask:
> 
> > “Did HR rise within the plausible window after albuterol?”  
> > “Did glucose rise after prednisone?”  
> > “Did sedation/fall risk increase after hydroxyzine or diphenhydramine?”
> 
> ---
> 
> # 3. OTC, food, supplement, and exposure schema
> 
> Do **not** bury these in notes. Make them first-class.
> 
> ## `intake_events`
> 
> Anything consumed.
> 
> | Field | Type | Notes |
> |---|---|---|
> | intake_id | uuid |
> | patient_id | uuid |
> | substance_id | uuid |
> | consumed_at | timestamptz |
> | amount | numeric |
> | unit | text |
> | intake_type | text | food, drink, supplement, OTC, recreational, unknown |
> | meal_context | text | breakfast, snack, bedtime |
> | carbs_estimate | numeric |
> | sodium_estimate | numeric |
> | caffeine_mg | numeric |
> | sugar_g | numeric |
> | notes | text |
> 
> Examples:
> 
> - peanut butter
> - milk
> - cake
> - beefaroni
> - coffee
> - grapefruit juice
> - electrolyte drink
> - OTC cold medicine
> - Benadryl
> - magnesium
> - vitamin D
> - cannabis/CBD if relevant
> - alcohol if relevant
> 
> ---
> 
> ## `environment_events`
> 
> External context.
> 
> | Field | Type | Notes |
> |---|---|---|
> | env_event_id | uuid |
> | patient_id | uuid |
> | occurred_at | timestamptz |
> | environment_type | text | temperature, humidity, allergen, smoke, dust, chemical, mold, altitude, crowding |
> | value | numeric |
> | unit | text |
> | severity | text |
> | location | text |
> | exposure_duration_minutes | int |
> | notes | text |
> 
> Examples:
> 
> - house very cold
> - room overheated
> - smoke exposure
> - dust exposure
> - cleaning chemicals
> - high pollen
> - oxygen equipment issue
> - power outage
> - poor sleep environment
> 
> ---
> 
> ## `behavior_events`
> 
> Behavior is not “blame.” It is physiology.
> 
> | Field | Type | Notes |
> |---|---|---|
> | behavior_event_id | uuid |
> | patient_id | uuid |
> | occurred_at | timestamptz |
> | behavior_type | text | talking, exertion, lying_position, sleep, refusal, agitation, panic, pacing, scooter_use |
> | intensity | int | 1–10 |
> | duration_minutes | int |
> | observed_by | text |
> | notes | text |
> 
> Examples:
> 
> - talking continuously for 30 minutes
> - refused hydroxyzine
> - repeatedly checking symptoms
> - unable to sit still
> - slept poorly
> - exerted self walking to bathroom
> - lay flat despite dyspnea
> - panic spiral
> 
> This is where the system gets powerful because it can detect **behavior–vital loops**.
> 
> ---
> 
> # 4. Vitals, symptoms, observations
> 
> ## `vital_observations`
> 
> | Field | Type | Notes |
> |---|---|---|
> | vital_id | uuid |
> | patient_id | uuid |
> | measured_at | timestamptz |
> | vital_type | text | HR, SpO2, BP_SYS, BP_DIA, Temp, Glucose, RespRate, Weight |
> | value | numeric |
> | unit | text |
> | body_site | text | right arm, finger, oral, etc. |
> | device | text |
> | posture | text | sitting, lying, standing |
> | oxygen_flow_lpm | numeric nullable |
> | confidence | numeric |
> | notes | text |
> 
> Do not store BP as one field. Store systolic and diastolic separately or use a linked pair.
> 
> ---
> 
> ## `symptom_observations`
> 
> | Field | Type | Notes |
> |---|---|---|
> | symptom_id | uuid |
> | patient_id | uuid |
> | observed_at | timestamptz |
> | symptom_name | text |
> | snomed_code | text |
> | severity | int | 0–10 |
> | duration_minutes | int |
> | onset_type | text | sudden, gradual, recurring |
> | patient_reported | boolean |
> | caregiver_observed | boolean |
> | objective_support | text |
> | improved_by | text |
> | worsened_by | text |
> | notes | text |
> 
> Examples:
> 
> - air hunger
> - wheeze
> - cough
> - congestion
> - anxiety
> - tremor
> - rash
> - dizziness
> - confusion
> - swelling
> - pain
> - fatigue
> 
> ---
> 
> ## `clinical_events`
> 
> Bigger episodes.
> 
> | Field | Type | Notes |
> |---|---|---|
> | event_id | uuid |
> | patient_id | uuid |
> | event_at | timestamptz |
> | event_type | text | flare, fall, ER_visit, EMS_call, med_change, abnormal_vital, panic_episode |
> | title | text |
> | summary | text |
> | severity | text |
> | outcome | text |
> | linked_document_id | uuid |
> | notes | text |
> 
> This is where “the episode” lives. Everything else attaches to it.
> 
> ---
> 
> # 5. Labs, imaging, notes, documents
> 
> ## `lab_results`
> 
> | Field | Type | Notes |
> |---|---|---|
> | lab_id | uuid |
> | patient_id | uuid |
> | collected_at | timestamptz |
> | resulted_at | timestamptz |
> | test_name | text |
> | loinc_code | text |
> | value | numeric |
> | unit | text |
> | reference_low | numeric |
> | reference_high | numeric |
> | abnormal_flag | text |
> | source_document_id | uuid |
> | notes | text |
> 
> LOINC is specifically built for observations, measurements, and lab-type data, so use it here rather than inventing your own lab naming chaos. citeturn779112search17turn779112search16
> 
> ---
> 
> ## `imaging_reports`
> 
> | Field | Type | Notes |
> |---|---|---|
> | imaging_id | uuid |
> | patient_id | uuid |
> | performed_at | timestamptz |
> | modality | text | X-ray, CT, MRI, ultrasound |
> | body_part | text |
> | impression | text |
> | findings | text |
> | abnormal_flag | boolean |
> | source_document_id | uuid |
> 
> ---
> 
> ## `documents`
> 
> | Field | Type | Notes |
> |---|---|---|
> | document_id | uuid |
> | patient_id | uuid |
> | doc_type | text | discharge, lab, med_list, visit_note, imaging, instruction |
> | title | text |
> | document_date | date |
> | source | text |
> | storage_uri | text |
> | extracted_text | text |
> | ocr_confidence | numeric |
> | processed_status | text |
> 
> ---
> 
> # 6. Interaction knowledge base
> 
> You need two interaction systems:
> 
> 1. **Known interaction rules** from references.
> 2. **Patient-specific observed interaction patterns** from timeline analysis.
> 
> That distinction is critical.
> 
> ---
> 
> ## `interaction_rules`
> 
> Known or imported interaction possibilities.
> 
> | Field | Type | Notes |
> |---|---|---|
> | rule_id | uuid |
> | source_substance_id | uuid |
> | target_substance_id | uuid nullable |
> | target_condition_id | uuid nullable |
> | target_food_pattern | text nullable |
> | interaction_type | text | drug_drug, drug_food, drug_condition, drug_lab, drug_behavior, drug_environment |
> | mechanism | text |
> | expected_effect | text |
> | severity | text | minor, moderate, major, contraindicated |
> | evidence_level | text |
> | source_name | text |
> | source_url | text |
> | review_required | boolean |
> | notes | text |
> 
> Sources can include RxNorm mapping, FDA labels, drug databases, pharmacist review, manually entered clinician knowledge, or your own curated references. RxNorm is a strong normalization backbone, while openFDA provides APIs for drug labels and adverse-event data; openFDA labels include prescription and OTC labels with sections such as adverse reactions and other safety information, but openFDA itself cautions not to use its data as direct medical decision-making authority. citeturn779112search8turn779112search11turn779112search10
> 
> ---
> 
> ## `patient_interaction_findings`
> 
> Observed or suspected interactions for this specific person.
> 
> | Field | Type | Notes |
> |---|---|---|
> | finding_id | uuid |
> | patient_id | uuid |
> | rule_id | uuid nullable |
> | primary_factor_id | uuid | substance/event/etc. |
> | secondary_factor_id | uuid nullable |
> | finding_type | text |
> | hypothesis | text |
> | evidence_summary | text |
> | confidence | numeric | 0–1 |
> | severity | text |
> | first_seen_at | timestamptz |
> | last_seen_at | timestamptz |
> | recurrence_count | int |
> | status | text | open, confirmed, dismissed, clinician_reviewed |
> | clinician_question | text |
> 
> Example finding:
> 
> > “Episodes of tachycardia appear temporally associated with rescue inhaler use plus prolonged talking/anxiety behavior, while SpO2 remains 94–96%. Ask clinician whether bronchodilator side effects, anxiety overlay, or cardiac rhythm evaluation should be reviewed.”
> 
> That is the right tone.
> 
> ---
> 
> # 7. Graph schema
> 
> I would use Neo4j or another graph DB for relationship reasoning.
> 
> ## Nodes
> 
> ### Person-level
> 
> - `Patient`
> - `Condition`
> - `Allergy`
> - `Provider`
> - `ClinicalEvent`
> 
> ### Clinical state
> 
> - `Symptom`
> - `VitalObservation`
> - `LabResult`
> - `ImagingFinding`
> 
> ### Inputs/exposures
> 
> - `Medication`
> - `OTC`
> - `Supplement`
> - `Food`
> - `Beverage`
> - `EnvironmentalExposure`
> - `Behavior`
> 
> ### Knowledge
> 
> - `DrugClass`
> - `InteractionRule`
> - `SideEffect`
> - `Contraindication`
> - `Mechanism`
> - `ClinicalQuestion`
> - `Hypothesis`
> 
> ---
> 
> ## Edges
> 
> | Relationship | Meaning |
> |---|---|
> | `HAS_CONDITION` | patient → condition |
> | `HAS_ALLERGY` | patient → allergy |
> | `TOOK` | patient → medication administration |
> | `REFUSED` | patient → medication administration |
> | `CONSUMED` | patient → food/OTC/supplement |
> | `EXPOSED_TO` | patient → environment |
> | `DISPLAYED` | patient → symptom |
> | `MEASURED` | patient → vital/lab |
> | `OCCURRED_DURING` | observation → clinical event |
> | `PRECEDED` | medication/food/behavior → symptom/vital |
> | `FOLLOWED_BY` | event → observation |
> | `MAY_CAUSE` | substance → side effect |
> | `MAY_WORSEN` | substance/environment/behavior → condition/symptom |
> | `MAY_INTERACT_WITH` | substance → substance |
> | `CONTRAINDICATED_WITH` | substance → condition/allergy |
> | `TREATS` | medication → condition/symptom |
> | `MASKS` | medication → symptom |
> | `AMPLIFIES` | behavior/environment → symptom |
> | `CORRELATED_WITH` | any event → any outcome |
> | `GENERATED_HYPOTHESIS` | pattern → hypothesis |
> | `NEEDS_REVIEW_BY` | hypothesis → provider type |
> 
> SNOMED CT can support clinical concept consistency and graph-style clinical relationships; recent research also describes using SNOMED CT with Neo4j-style graphs for structured clinical reasoning, though that is still research context rather than a turnkey medical product. citeturn779112academia85turn779112search13
> 
> ---
> 
> # 8. Analytical tables
> 
> ## `analysis_runs`
> 
> Every time the AI analyzes data.
> 
> | Field | Type | Notes |
> |---|---|---|
> | analysis_run_id | uuid |
> | patient_id | uuid |
> | started_at | timestamptz |
> | completed_at | timestamptz |
> | analysis_type | text | daily_review, interaction_scan, flare_review, doctor_packet |
> | model_used | text |
> | data_window_start | timestamptz |
> | data_window_end | timestamptz |
> | status | text |
> | summary | text |
> 
> ---
> 
> ## `risk_signals`
> 
> Machine-detected concerns.
> 
> | Field | Type | Notes |
> |---|---|---|
> | risk_signal_id | uuid |
> | analysis_run_id | uuid |
> | patient_id | uuid |
> | signal_type | text | interaction, red_flag, trend, contradiction, missing_data, worsening_pattern |
> | severity | text | low, medium, high, urgent |
> | title | text |
> | explanation | text |
> | evidence_strength | numeric |
> | confidence | numeric |
> | recommended_action_type | text | monitor, ask_doctor, pharmacist_review, urgent_eval |
> | status | text |
> 
> ---
> 
> ## `hypotheses`
> 
> Do not let the AI produce floating conclusions. Store hypotheses as objects.
> 
> | Field | Type | Notes |
> |---|---|---|
> | hypothesis_id | uuid |
> | analysis_run_id | uuid |
> | patient_id | uuid |
> | hypothesis_text | text |
> | category | text | medication_effect, disease_progression, behavior_loop, environmental_trigger, nutrition, care_gap |
> | evidence_for | jsonb |
> | evidence_against | jsonb |
> | missing_data | jsonb |
> | confidence | numeric |
> | urgency | text |
> | doctor_question | text |
> | status | text | open, reviewed, rejected, confirmed |
> 
> ---
> 
> ## `evidence_links`
> 
> Every AI conclusion needs receipts.
> 
> | Field | Type | Notes |
> |---|---|---|
> | evidence_link_id | uuid |
> | hypothesis_id | uuid nullable |
> | risk_signal_id | uuid nullable |
> | source_table | text |
> | source_id | uuid |
> | evidence_role | text | supports, contradicts, context, missing |
> | explanation | text |
> 
> No evidence link = no trust. Period.
> 
> ---
> 
> # 9. Pattern detection schema
> 
> ## `temporal_correlations`
> 
> | Field | Type | Notes |
> |---|---|---|
> | correlation_id | uuid |
> | patient_id | uuid |
> | analysis_run_id | uuid |
> | factor_type | text | medication, food, behavior, environment |
> | factor_id | uuid |
> | outcome_type | text | symptom, vital, lab, event |
> | outcome_id | uuid nullable |
> | time_lag_minutes_min | int |
> | time_lag_minutes_max | int |
> | recurrence_count | int |
> | correlation_score | numeric |
> | confidence | numeric |
> | interpretation | text |
> 
> Example:
> 
> > Factor: albuterol  
> > Outcome: HR > 130  
> > Lag: 0–90 min  
> > Recurrence: 5  
> > Interpretation: recurrent tachycardia episodes within plausible post-use window
> 
> ---
> 
> ## `baseline_profiles`
> 
> The system needs “normal for this person.”
> 
> | Field | Type | Notes |
> |---|---|---|
> | baseline_id | uuid |
> | patient_id | uuid |
> | metric_type | text | HR, SpO2, BP, glucose, sleep, symptom_score |
> | context | text | resting, post-med, morning, evening, on oxygen |
> | baseline_low | numeric |
> | baseline_high | numeric |
> | calculated_from_start | date |
> | calculated_from_end | date |
> | sample_count | int |
> | notes | text |
> 
> This matters because “normal” population ranges are not enough. A COPD patient’s baseline may be different from a healthy adult’s baseline, and trend deviation may matter more than one isolated value.
> 
> ---
> 
> # 10. Agent modules
> 
> Build the AI as separate agents/functions, not one giant brain blob.
> 
> ## A. Medication Interaction Agent
> 
> Inputs:
> 
> - medication orders
> - actual administrations
> - OTCs
> - supplements
> - foods
> - allergies
> - conditions
> - vitals/labs after use
> 
> Outputs:
> 
> - drug-drug concerns
> - drug-food concerns
> - duplicate side-effect burden
> - sedation/fall risk
> - stimulant/tachycardia risk
> - glucose impact
> - BP impact
> - respiratory impact
> - clinician/pharmacist questions
> 
> ---
> 
> ## B. Symptom-Vital Correlation Agent
> 
> Looks for:
> 
> - symptom with normal vital
> - abnormal vital without reported symptom
> - HR spikes with stable SpO2
> - glucose spikes after steroid/food
> - BP drops after meds/position change
> - oxygen changes after exertion/environment
> - rash after medication/food/exposure
> 
> ---
> 
> ## C. Environment/Behavior Agent
> 
> Looks for:
> 
> - cold/heat/humidity → breathing symptoms
> - dust/smoke/chemical exposure → respiratory symptoms
> - talking/exertion → dyspnea/HR
> - refusal/missed meds → symptom escalation
> - poor sleep → anxiety/HR/glucose
> - lying position → breathing discomfort
> 
> ---
> 
> ## D. Red Flag Agent
> 
> Hard-coded rules. Less “AI,” more deterministic.
> 
> Examples:
> 
> - HR sustained > threshold
> - SpO2 below patient-specific threshold
> - confusion + respiratory symptoms
> - chest pain + HR/BP abnormality
> - fall + anticoagulant use
> - glucose extreme + symptoms
> - rash + swelling/breathing issues
> 
> This agent should be boring and strict.
> 
> ---
> 
> ## E. Doctor Packet Agent
> 
> Creates:
> 
> - one-page summary
> - med list
> - recent episodes
> - risk findings
> - top hypotheses
> - questions by specialty
> - evidence timeline
> 
> ---
> 
> # 11. Example graph query logic
> 
> ## Medication → vital spike
> 
> Plain-English logic:
> 
> > Find all medication administrations followed by heart rate above patient baseline within the medication’s expected effect window.
> 
> Output:
> 
> | Medication | Episodes | Avg HR rise | Window | Confidence |
> |---|---:|---:|---|---:|
> | Albuterol | 6 | +38 bpm | 0–90 min | 0.74 |
> | Prednisone | 4 | +22 bpm | same day | 0.52 |
> 
> ---
> 
> ## Food/med/glucose interaction
> 
> > Find glucose readings above baseline within 4–12 hours after steroid use and high-carb intake.
> 
> Output:
> 
> | Factor combo | Episodes | Pattern |
> |---|---:|---|
> | prednisone + high-carb snack | 5 | glucose above baseline |
> | prednisone without high-carb | 2 | mild rise only |
> 
> That is useful. That’s a doctor conversation.
> 
> ---
> 
> ## Behavior loop
> 
> > Find dyspnea reports where SpO2 remained stable but HR increased and talking/agitation was present.
> 
> Output:
> 
> | Pattern | Count | Interpretation |
> |---|---:|---|
> | dyspnea + SpO2 94–96 + HR >130 + talking | 7 | possible anxiety/behavioral respiratory load overlay |
> | dyspnea + SpO2 <90 | 1 | true oxygenation concern |
> 
> That distinction is money.
> 
> ---
> 
> # 12. Minimum viable schema
> 
> If you want to start lean, build only these first:
> 
> 1. `patients`
> 2. `conditions`
> 3. `substances`
> 4. `medication_orders`
> 5. `medication_administrations`
> 6. `intake_events`
> 7. `environment_events`
> 8. `behavior_events`
> 9. `vital_observations`
> 10. `symptom_observations`
> 11. `clinical_events`
> 12. `interaction_rules`
> 13. `patient_interaction_findings`
> 14. `analysis_runs`
> 15. `hypotheses`
> 16. `evidence_links`
> 
> That is enough to build the first serious version.
> 
> Do **not** overbuild FHIR on day one. Use FHIR concepts later if needed, but for your private project, your immediate need is a clean event ledger and interaction graph.
> 
> ---
> 
> # 13. Suggested PostgreSQL-style skeleton
> 
> ```sql
> CREATE TABLE patients (
>   patient_id UUID PRIMARY KEY,
>   display_name TEXT NOT NULL,
>   dob DATE,
>   sex_at_birth TEXT,
>   height_cm NUMERIC,
>   baseline_weight_kg NUMERIC,
>   baseline_o2_range TEXT,
>   primary_conditions_summary TEXT,
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> 
> CREATE TABLE substances (
>   substance_id UUID PRIMARY KEY,
>   name TEXT NOT NULL,
>   substance_type TEXT NOT NULL,
>   rxnorm_code TEXT,
>   ingredient_name TEXT,
>   ingredient_rxnorm_code TEXT,
>   drug_class TEXT,
>   known_stimulant BOOLEAN DEFAULT false,
>   known_sedating BOOLEAN DEFAULT false,
>   known_glucose_effect TEXT,
>   known_bp_effect TEXT,
>   known_hr_effect TEXT,
>   notes TEXT
> );
> 
> CREATE TABLE medication_orders (
>   med_order_id UUID PRIMARY KEY,
>   patient_id UUID REFERENCES patients(patient_id),
>   substance_id UUID REFERENCES substances(substance_id),
>   prescribed_name TEXT,
>   dose_amount NUMERIC,
>   dose_unit TEXT,
>   route TEXT,
>   frequency TEXT,
>   start_date DATE,
>   end_date DATE,
>   prescribing_provider TEXT,
>   indication TEXT,
>   prn BOOLEAN DEFAULT false,
>   max_daily_dose TEXT,
>   instructions TEXT,
>   active_status TEXT DEFAULT 'active'
> );
> 
> CREATE TABLE medication_administrations (
>   med_admin_id UUID PRIMARY KEY,
>   patient_id UUID REFERENCES patients(patient_id),
>   substance_id UUID REFERENCES substances(substance_id),
>   med_order_id UUID REFERENCES medication_orders(med_order_id),
>   taken_at TIMESTAMPTZ NOT NULL,
>   dose_amount NUMERIC,
>   dose_unit TEXT,
>   route TEXT,
>   taken_status TEXT,
>   reason_given TEXT,
>   observed_effect TEXT,
>   source TEXT,
>   confidence NUMERIC DEFAULT 1.0,
>   notes TEXT
> );
> 
> CREATE TABLE intake_events (
>   intake_id UUID PRIMARY KEY,
>   patient_id UUID REFERENCES patients(patient_id),
>   substance_id UUID REFERENCES substances(substance_id),
>   consumed_at TIMESTAMPTZ NOT NULL,
>   amount NUMERIC,
>   unit TEXT,
>   intake_type TEXT,
>   meal_context TEXT,
>   carbs_estimate NUMERIC,
>   sodium_estimate NUMERIC,
>   caffeine_mg NUMERIC,
>   sugar_g NUMERIC,
>   notes TEXT
> );
> 
> CREATE TABLE environment_events (
>   env_event_id UUID PRIMARY KEY,
>   patient_id UUID REFERENCES patients(patient_id),
>   occurred_at TIMESTAMPTZ NOT NULL,
>   environment_type TEXT,
>   value NUMERIC,
>   unit TEXT,
>   severity TEXT,
>   location TEXT,
>   exposure_duration_minutes INT,
>   notes TEXT
> );
> 
> CREATE TABLE behavior_events (
>   behavior_event_id UUID PRIMARY KEY,
>   patient_id UUID REFERENCES patients(patient_id),
>   occurred_at TIMESTAMPTZ NOT NULL,
>   behavior_type TEXT,
>   intensity INT,
>   duration_minutes INT,
>   observed_by TEXT,
>   notes TEXT
> );
> 
> CREATE TABLE vital_observations (
>   vital_id UUID PRIMARY KEY,
>   patient_id UUID REFERENCES patients(patient_id),
>   measured_at TIMESTAMPTZ NOT NULL,
>   vital_type TEXT NOT NULL,
>   value NUMERIC NOT NULL,
>   unit TEXT,
>   body_site TEXT,
>   device TEXT,
>   posture TEXT,
>   oxygen_flow_lpm NUMERIC,
>   confidence NUMERIC DEFAULT 1.0,
>   notes TEXT
> );
> 
> CREATE TABLE symptom_observations (
>   symptom_id UUID PRIMARY KEY,
>   patient_id UUID REFERENCES patients(patient_id),
>   observed_at TIMESTAMPTZ NOT NULL,
>   symptom_name TEXT NOT NULL,
>   snomed_code TEXT,
>   severity INT,
>   duration_minutes INT,
>   onset_type TEXT,
>   patient_reported BOOLEAN DEFAULT true,
>   caregiver_observed BOOLEAN DEFAULT false,
>   objective_support TEXT,
>   improved_by TEXT,
>   worsened_by TEXT,
>   notes TEXT
> );
> 
> CREATE TABLE clinical_events (
>   event_id UUID PRIMARY KEY,
>   patient_id UUID REFERENCES patients(patient_id),
>   event_at TIMESTAMPTZ NOT NULL,
>   event_type TEXT,
>   title TEXT,
>   summary TEXT,
>   severity TEXT,
>   outcome TEXT,
>   linked_document_id UUID,
>   notes TEXT
> );
> 
> CREATE TABLE interaction_rules (
>   rule_id UUID PRIMARY KEY,
>   source_substance_id UUID REFERENCES substances(substance_id),
>   target_substance_id UUID REFERENCES substances(substance_id),
>   target_condition_id UUID,
>   target_food_pattern TEXT,
>   interaction_type TEXT,
>   mechanism TEXT,
>   expected_effect TEXT,
>   severity TEXT,
>   evidence_level TEXT,
>   source_name TEXT,
>   source_url TEXT,
>   review_required BOOLEAN DEFAULT true,
>   notes TEXT
> );
> 
> CREATE TABLE analysis_runs (
>   analysis_run_id UUID PRIMARY KEY,
>   patient_id UUID REFERENCES patients(patient_id),
>   started_at TIMESTAMPTZ DEFAULT now(),
>   completed_at TIMESTAMPTZ,
>   analysis_type TEXT,
>   model_used TEXT,
>   data_window_start TIMESTAMPTZ,
>   data_window_end TIMESTAMPTZ,
>   status TEXT,
>   summary TEXT
> );
> 
> CREATE TABLE hypotheses (
>   hypothesis_id UUID PRIMARY KEY,
>   analysis_run_id UUID REFERENCES analysis_runs(analysis_run_id),
>   patient_id UUID REFERENCES patients(patient_id),
>   hypothesis_text TEXT,
>   category TEXT,
>   evidence_for JSONB,
>   evidence_against JSONB,
>   missing_data JSONB,
>   confidence NUMERIC,
>   urgency TEXT,
>   doctor_question TEXT,
>   status TEXT DEFAULT 'open'
> );
> 
> CREATE TABLE risk_signals (
>   risk_signal_id UUID PRIMARY KEY,
>   analysis_run_id UUID REFERENCES analysis_runs(analysis_run_id),
>   patient_id UUID REFERENCES patients(patient_id),
>   signal_type TEXT,
>   severity TEXT,
>   title TEXT,
>   explanation TEXT,
>   evidence_strength NUMERIC,
>   confidence NUMERIC,
>   recommended_action_type TEXT,
>   status TEXT DEFAULT 'open'
> );
> 
> CREATE TABLE evidence_links (
>   evidence_link_id UUID PRIMARY KEY,
>   hypothesis_id UUID REFERENCES hypotheses(hypothesis_id),
>   risk_signal_id UUID REFERENCES risk_signals(risk_signal_id),
>   source_table TEXT NOT NULL,
>   source_id UUID NOT NULL,
>   evidence_role TEXT,
>   explanation TEXT
> );
> ```
> 
> ---
> 
> # 14. Agent output format
> 
> Make every analysis return this JSON shape:
> 
> ```json
> {
>   "patient_id": "...",
>   "analysis_window": {
>     "start": "...",
>     "end": "..."
>   },
>   "summary": "Brief clinical-pattern summary, not diagnosis.",
>   "top_risk_signals": [
>     {
>       "title": "Possible medication-related tachycardia pattern",
>       "severity": "medium",
>       "confidence": 0.72,
>       "evidence": [
>         {
>           "source_table": "medication_administrations",
>           "source_id": "...",
>           "reason": "Albuterol taken within 60 minutes before HR spike"
>         },
>         {
>           "source_table": "vital_observations",
>           "source_id": "...",
>           "reason": "Heart rate rose to 150 while SpO2 stayed 95"
>         }
>       ],
>       "doctor_question": "Could rescue inhaler frequency, steroid use, anxiety, or rhythm issues be contributing to tachycardia?"
>     }
>   ],
>   "interaction_findings": [
>     {
>       "type": "drug_behavior_vital",
>       "factors": ["albuterol", "prolonged talking", "anxiety behavior"],
>       "possible_effect": "tachycardia and perceived air hunger",
>       "confidence": 0.68,
>       "needs_review_by": ["primary care", "pulmonology", "pharmacist"]
>     }
>   ],
>   "missing_data": [
>     "Exact inhaler/nebulizer administration times",
>     "Respiratory rate during episodes",
>     "Medication reconciliation from pharmacy",
>     "Recent EKG or cardiac evaluation"
>   ],
>   "not_diagnosis_statement": "This analysis identifies patterns and questions for clinician review, not a diagnosis."
> }
> ```
> 
> ---
> 
> # 15. The actual intelligence stack
> 
> For the first version:
> 
> ## Store
> 
> - PostgreSQL for normalized records
> - Neo4j for graph relationships
> - Qdrant for document embeddings
> - Paperless-ngx for document intake/OCR
> - LLM for summarization and hypothesis generation
> - deterministic rules for red flags
> 
> ## Analyze
> 
> Run scheduled jobs:
> 
> | Job | Frequency |
> |---|---|
> | medication interaction scan | every new medication/intake |
> | daily patient summary | daily |
> | episode review | after clinical event |
> | doctor packet | before appointment |
> | baseline recalculation | weekly |
> | missing data audit | weekly |
> 
> ---
> 
> # 16. Final architecture name
> 
> For your system, I’d name this module:
> 
> **QiClinical Graph Agent**
> 
> Or more technically:
> 
> **Clinical Event Graph + Medication Interaction Intelligence Layer**
> 
> Its job:
> 
> > Transform normalized patient records into evidence-linked clinical hypotheses, interaction warnings, trend signals, and doctor-facing questions.
> 
> That’s the clean lane. Powerful, but not pretending to be a doctor. And yes — meds + OTCs + foods + environment + behavior all need to sit in the same graph, because that is where the overlooked patterns are hiding.

### User
> your making too many tables you cannot have 7 different events tables, things will get lost, you need a more generalized spine with supporting tables. there is something elegant when efficency and simplicity is used

### Assistant
> You’re right. I over-normalized it.
> 
> That schema was clinically thorough but operationally ugly. Too many event tables means the exact failure you named: **the truth gets scattered.** For your use case, the elegant version is:
> 
> > **One event spine. Everything that happens goes into one ledger. Supporting tables define what the event means. Graphs and AI read from the ledger.**
> 
> That is the move.
> 
> # Corrected architecture
> 
> ## Core idea
> 
> Every meaningful thing is an **event**:
> 
> - medication taken
> - medication refused
> - food eaten
> - OTC taken
> - symptom reported
> - vital measured
> - behavior observed
> - environmental exposure
> - ER visit
> - fall
> - anxiety episode
> - rash
> - oxygen change
> - glucose reading
> - doctor instruction
> - caregiver note
> 
> All of it goes into one table:
> 
> ## `clinical_events`
> 
> This becomes the universal health ledger.
> 
> | Field | Purpose |
> |---|---|
> | `event_id` | unique ID |
> | `patient_id` | who it belongs to |
> | `event_time` | when it happened |
> | `event_type` | medication, vital, symptom, food, behavior, environment, visit, note |
> | `event_subtype` | HR, SpO2, prednisone, talking, cold_room, rash, EMS_call |
> | `subject_id` | optional link to substance, condition, metric, document, etc. |
> | `value_numeric` | number if applicable |
> | `value_text` | text value if applicable |
> | `unit` | mg, bpm, %, mmHg, etc. |
> | `severity` | low, medium, high, urgent or 0–10 |
> | `status` | taken, refused, observed, resolved, ongoing, missed |
> | `source` | caregiver, patient, device, document, doctor |
> | `confidence` | 0–1 |
> | `context_json` | flexible details |
> | `notes` | human note |
> | `created_at` | system timestamp |
> 
> That’s the spine.
> 
> No separate `medication_administrations`, `intake_events`, `behavior_events`, `environment_events`, `symptom_observations`, and `vital_observations`.
> 
> One table. One timeline. No hunting.
> 
> ---
> 
> # Minimal supporting tables
> 
> You only need a few strong reference tables.
> 
> ## 1. `patients`
> 
> Basic patient identity and baseline profile.
> 
> | Field | Purpose |
> |---|---|
> | `patient_id` | primary key |
> | `display_name` | internal name |
> | `dob` | optional |
> | `sex_at_birth` | clinically relevant if known |
> | `baseline_profile_json` | baseline oxygen, HR, glucose, BP, etc. |
> | `notes` | general summary |
> 
> ---
> 
> ## 2. `clinical_concepts`
> 
> This is your master dictionary.
> 
> Everything meaningful gets a concept:
> 
> - prednisone
> - albuterol
> - hydroxyzine
> - Benadryl
> - peanut butter
> - caffeine
> - oxygen
> - heart rate
> - SpO2
> - air hunger
> - anxiety
> - talking
> - cold room
> - smoke exposure
> - COPD
> - diabetes
> - rash
> - fall risk
> 
> | Field | Purpose |
> |---|---|
> | `concept_id` | primary key |
> | `name` | human name |
> | `concept_type` | medication, otc, food, supplement, vital, symptom, behavior, environment, condition, lab |
> | `standard_code` | RxNorm, LOINC, SNOMED, etc. |
> | `code_system` | rxnorm, loinc, snomed, local |
> | `parent_concept_id` | optional hierarchy |
> | `properties_json` | flexible metadata |
> 
> This replaces a pile of category-specific tables.
> 
> Example:
> 
> | name | concept_type | properties_json |
> |---|---|---|
> | Albuterol | medication | raises_hr: true, stimulant_like: true |
> | Prednisone | medication | raises_glucose: true, may_worsen_anxiety: true |
> | SpO2 | vital | unit: %, lower_is_worse: true |
> | Talking continuously | behavior | respiratory_load: true |
> | Cold room | environment | may_trigger_breathing_discomfort: true |
> 
> Beautiful. Clean. Expandable.
> 
> ---
> 
> ## 3. `care_plans`
> 
> What the person is supposed to be doing.
> 
> This stores prescriptions, routines, action plans, doctor instructions.
> 
> | Field | Purpose |
> |---|---|
> | `plan_id` | primary key |
> | `patient_id` | patient |
> | `concept_id` | med, oxygen, monitoring, diet, behavior, etc. |
> | `plan_type` | medication_order, oxygen_order, monitoring_plan, action_plan |
> | `instructions` | human-readable |
> | `dose_amount` | optional |
> | `dose_unit` | optional |
> | `frequency` | optional |
> | `start_date` | optional |
> | `end_date` | optional |
> | `status` | active, paused, stopped |
> | `source_document_id` | optional |
> | `metadata_json` | flexible |
> 
> This lets you compare:
> 
> > “What was supposed to happen?”  
> > vs  
> > “What actually happened?”
> 
> That is clinically valuable.
> 
> ---
> 
> ## 4. `relationships`
> 
> This is the graph edge table.
> 
> It stores known and observed relationships.
> 
> | Field | Purpose |
> |---|---|
> | `relationship_id` | primary key |
> | `source_concept_id` | from concept |
> | `target_concept_id` | to concept |
> | `relationship_type` | may_cause, may_worsen, treats, interacts_with, contraindicated_with, associated_with |
> | `strength` | 0–1 |
> | `severity` | low, medium, high |
> | `evidence_level` | known, suspected, observed, clinician_confirmed |
> | `source` | drug label, pharmacist, AI finding, caregiver observation |
> | `notes` | explanation |
> | `metadata_json` | flexible |
> 
> Examples:
> 
> | Source | Relationship | Target |
> |---|---|---|
> | Albuterol | may_cause | tachycardia |
> | Prednisone | may_worsen | anxiety |
> | Prednisone | may_raise | blood glucose |
> | Hydroxyzine | may_cause | sedation |
> | Talking continuously | may_worsen | dyspnea |
> | Cold air | may_trigger | breathing discomfort |
> | Benadryl | interacts_with | hydroxyzine |
> | Grapefruit | interacts_with | certain meds |
> 
> This table can be mirrored into Neo4j, but it also works inside Postgres.
> 
> ---
> 
> ## 5. `documents`
> 
> For discharge papers, med lists, labs, notes, screenshots.
> 
> | Field | Purpose |
> |---|---|
> | `document_id` | primary key |
> | `patient_id` | patient |
> | `document_type` | discharge, lab, prescription, instruction, visit_note |
> | `document_date` | when from |
> | `title` | name |
> | `storage_uri` | file path |
> | `extracted_text` | OCR/text |
> | `summary` | AI summary |
> | `metadata_json` | flexible |
> 
> ---
> 
> ## 6. `analysis_runs`
> 
> Each AI review session.
> 
> | Field | Purpose |
> |---|---|
> | `analysis_run_id` | primary key |
> | `patient_id` | patient |
> | `run_time` | when analysis ran |
> | `analysis_type` | daily, episode, interaction_scan, doctor_packet |
> | `window_start` | data start |
> | `window_end` | data end |
> | `model_used` | optional |
> | `summary` | run summary |
> | `status` | completed, failed, needs_review |
> 
> ---
> 
> ## 7. `findings`
> 
> The AI’s conclusions, warnings, and questions.
> 
> | Field | Purpose |
> |---|---|
> | `finding_id` | primary key |
> | `analysis_run_id` | parent run |
> | `patient_id` | patient |
> | `finding_type` | interaction, pattern, red_flag, missing_data, hypothesis, care_gap |
> | `title` | short finding |
> | `description` | explanation |
> | `severity` | low, medium, high, urgent |
> | `confidence` | 0–1 |
> | `status` | open, reviewed, dismissed, confirmed |
> | `doctor_question` | what to ask |
> | `recommendation_type` | monitor, ask_doctor, pharmacist_review, urgent_eval |
> | `metadata_json` | flexible |
> 
> ---
> 
> ## 8. `finding_evidence`
> 
> Receipts. Every finding must link back to events, documents, concepts, or relationships.
> 
> | Field | Purpose |
> |---|---|
> | `evidence_id` | primary key |
> | `finding_id` | parent finding |
> | `source_type` | event, document, concept, relationship, care_plan |
> | `source_id` | ID of source |
> | `evidence_role` | supports, contradicts, context, missing |
> | `explanation` | why it matters |
> 
> This is non-negotiable.  
> AI without evidence links becomes medical fan fiction.
> 
> ---
> 
> # The cleaner schema
> 
> So the real minimal schema is:
> 
> 1. `patients`
> 2. `clinical_concepts`
> 3. `clinical_events`
> 4. `care_plans`
> 5. `relationships`
> 6. `documents`
> 7. `analysis_runs`
> 8. `findings`
> 9. `finding_evidence`
> 
> That’s it.
> 
> Nine tables. Strong spine. Flexible enough for expansion.
> 
> ---
> 
> # How events work
> 
> Instead of multiple event tables, use `event_type`.
> 
> ## Example: medication taken
> 
> | Field | Value |
> |---|---|
> | event_type | medication |
> | event_subtype | taken |
> | subject_id | Albuterol concept ID |
> | value_numeric | 2 |
> | unit | puffs |
> | status | taken |
> | context_json | `{ "route": "inhaled", "reason": "shortness of breath" }` |
> 
> ---
> 
> ## Example: medication refused
> 
> | Field | Value |
> |---|---|
> | event_type | medication |
> | event_subtype | refused |
> | subject_id | Hydroxyzine concept ID |
> | status | refused |
> | context_json | `{ "reason_given": "did not want it" }` |
> 
> ---
> 
> ## Example: heart rate
> 
> | Field | Value |
> |---|---|
> | event_type | vital |
> | event_subtype | heart_rate |
> | subject_id | Heart Rate concept ID |
> | value_numeric | 150 |
> | unit | bpm |
> | severity | high |
> | context_json | `{ "posture": "sitting", "device": "pulse_ox" }` |
> 
> ---
> 
> ## Example: oxygen
> 
> | Field | Value |
> |---|---|
> | event_type | vital |
> | event_subtype | spo2 |
> | subject_id | SpO2 concept ID |
> | value_numeric | 95 |
> | unit | % |
> | context_json | `{ "oxygen_flow_lpm": 2 }` |
> 
> ---
> 
> ## Example: behavior
> 
> | Field | Value |
> |---|---|
> | event_type | behavior |
> | event_subtype | talking_continuously |
> | subject_id | Talking continuously concept ID |
> | severity | medium |
> | context_json | `{ "duration_minutes": 30, "observed_by": "caregiver" }` |
> 
> ---
> 
> ## Example: food
> 
> | Field | Value |
> |---|---|
> | event_type | intake |
> | event_subtype | food |
> | subject_id | Peanut butter concept ID |
> | value_text | “large amount” |
> | context_json | `{ "meal_context": "snack", "carbs_estimate": null }` |
> 
> ---
> 
> ## Example: environment
> 
> | Field | Value |
> |---|---|
> | event_type | environment |
> | event_subtype | cold_room |
> | subject_id | Cold room concept ID |
> | severity | medium |
> | context_json | `{ "location": "bedroom", "patient_report": "too cold" }` |
> 
> ---
> 
> # Why this is better
> 
> Because now the AI can query one timeline:
> 
> > “Show me everything that happened 3 hours before the heart rate hit 150.”
> 
> That returns:
> 
> - albuterol taken
> - prednisone taken
> - hydroxyzine refused
> - talking continuously
> - room cold
> - SpO2 stable
> - anxiety reported
> - food intake
> - glucose level
> - caregiver note
> - EMS called
> 
> One stream. One truth. No table hopping nonsense.
> 
> ---
> 
> # SQL skeleton
> 
> ```sql
> CREATE TABLE patients (
>   patient_id UUID PRIMARY KEY,
>   display_name TEXT NOT NULL,
>   dob DATE,
>   sex_at_birth TEXT,
>   baseline_profile_json JSONB,
>   notes TEXT,
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> 
> CREATE TABLE clinical_concepts (
>   concept_id UUID PRIMARY KEY,
>   name TEXT NOT NULL,
>   concept_type TEXT NOT NULL,
>   standard_code TEXT,
>   code_system TEXT,
>   parent_concept_id UUID REFERENCES clinical_concepts(concept_id),
>   properties_json JSONB DEFAULT '{}'::jsonb,
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> 
> CREATE TABLE clinical_events (
>   event_id UUID PRIMARY KEY,
>   patient_id UUID REFERENCES patients(patient_id),
>   event_time TIMESTAMPTZ NOT NULL,
>   event_type TEXT NOT NULL,
>   event_subtype TEXT,
>   subject_id UUID REFERENCES clinical_concepts(concept_id),
>   value_numeric NUMERIC,
>   value_text TEXT,
>   unit TEXT,
>   severity TEXT,
>   status TEXT,
>   source TEXT,
>   confidence NUMERIC DEFAULT 1.0,
>   context_json JSONB DEFAULT '{}'::jsonb,
>   notes TEXT,
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> 
> CREATE TABLE care_plans (
>   plan_id UUID PRIMARY KEY,
>   patient_id UUID REFERENCES patients(patient_id),
>   concept_id UUID REFERENCES clinical_concepts(concept_id),
>   plan_type TEXT NOT NULL,
>   instructions TEXT,
>   dose_amount NUMERIC,
>   dose_unit TEXT,
>   frequency TEXT,
>   start_date DATE,
>   end_date DATE,
>   status TEXT DEFAULT 'active',
>   source_document_id UUID,
>   metadata_json JSONB DEFAULT '{}'::jsonb,
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> 
> CREATE TABLE relationships (
>   relationship_id UUID PRIMARY KEY,
>   source_concept_id UUID REFERENCES clinical_concepts(concept_id),
>   target_concept_id UUID REFERENCES clinical_concepts(concept_id),
>   relationship_type TEXT NOT NULL,
>   strength NUMERIC,
>   severity TEXT,
>   evidence_level TEXT,
>   source TEXT,
>   notes TEXT,
>   metadata_json JSONB DEFAULT '{}'::jsonb,
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> 
> CREATE TABLE documents (
>   document_id UUID PRIMARY KEY,
>   patient_id UUID REFERENCES patients(patient_id),
>   document_type TEXT,
>   document_date DATE,
>   title TEXT,
>   storage_uri TEXT,
>   extracted_text TEXT,
>   summary TEXT,
>   metadata_json JSONB DEFAULT '{}'::jsonb,
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> 
> CREATE TABLE analysis_runs (
>   analysis_run_id UUID PRIMARY KEY,
>   patient_id UUID REFERENCES patients(patient_id),
>   run_time TIMESTAMPTZ DEFAULT now(),
>   analysis_type TEXT,
>   window_start TIMESTAMPTZ,
>   window_end TIMESTAMPTZ,
>   model_used TEXT,
>   summary TEXT,
>   status TEXT
> );
> 
> CREATE TABLE findings (
>   finding_id UUID PRIMARY KEY,
>   analysis_run_id UUID REFERENCES analysis_runs(analysis_run_id),
>   patient_id UUID REFERENCES patients(patient_id),
>   finding_type TEXT NOT NULL,
>   title TEXT NOT NULL,
>   description TEXT,
>   severity TEXT,
>   confidence NUMERIC,
>   status TEXT DEFAULT 'open',
>   doctor_question TEXT,
>   recommendation_type TEXT,
>   metadata_json JSONB DEFAULT '{}'::jsonb,
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> 
> CREATE TABLE finding_evidence (
>   evidence_id UUID PRIMARY KEY,
>   finding_id UUID REFERENCES findings(finding_id),
>   source_type TEXT NOT NULL,
>   source_id UUID NOT NULL,
>   evidence_role TEXT,
>   explanation TEXT,
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> ---
> 
> # The event-type registry
> 
> Keep the allowed event types tight:
> 
> | Event Type | Meaning |
> |---|---|
> | `medication` | prescribed med taken/refused/missed/changed |
> | `intake` | food, drink, OTC, supplement |
> | `vital` | HR, BP, SpO2, glucose, temp, weight |
> | `symptom` | patient-reported or observed symptom |
> | `behavior` | activity, refusal, talking, agitation, sleep, exertion |
> | `environment` | heat, cold, smoke, dust, oxygen equipment, allergens |
> | `clinical_visit` | ER, EMS, doctor, hospital, telehealth |
> | `instruction` | doctor instruction, discharge instruction |
> | `care_action` | oxygen changed, helped sit up, gave water, cleaned rash |
> | `note` | general caregiver/patient note |
> 
> That’s plenty.
> 
> ---
> 
> # The real intelligence pattern
> 
> The AI does not need tons of tables. It needs clean event windows.
> 
> Example query:
> 
> > “For every HR over 130, pull all events from 4 hours before to 1 hour after.”
> 
> Then the agent checks:
> 
> - meds taken before
> - meds refused before
> - food before
> - glucose before/after
> - SpO2 at same time
> - symptoms nearby
> - behavior nearby
> - environment nearby
> - care actions nearby
> - whether this has happened before
> 
> Then it writes findings.
> 
> ---
> 
> # Graph model from the simple schema
> 
> You can derive graph nodes from:
> 
> - `patients`
> - `clinical_concepts`
> - `clinical_events`
> - `findings`
> 
> And graph edges from:
> 
> - `relationships`
> - event proximity
> - finding evidence
> - care plan instructions
> 
> ## Graph edges
> 
> | Edge | Source |
> |---|---|
> | Patient → HAS_EVENT → Event | clinical_events |
> | Event → ABOUT → Concept | subject_id |
> | Concept → MAY_CAUSE → Concept | relationships |
> | Finding → SUPPORTED_BY → Event | finding_evidence |
> | Medication Event → PRECEDED → Symptom Event | generated temporal relation |
> | Behavior Event → CO_OCCURS_WITH → Vital Event | generated temporal relation |
> | Care Plan → EXPECTS → Concept | care_plans |
> 
> You do not need to manually store every graph edge up front. Generate many of them during analysis.
> 
> ---
> 
> # Better name for the core table
> 
> Honestly, I would not call it `clinical_events`.
> 
> I’d call it:
> 
> ## `patient_ledger`
> 
> Because that’s what it is.
> 
> Every entry is a debit/credit against the patient’s state.
> 
> Cleaner schema:
> 
> 1. `patients`
> 2. `concepts`
> 3. `patient_ledger`
> 4. `care_plans`
> 5. `concept_relationships`
> 6. `documents`
> 7. `analysis_runs`
> 8. `findings`
> 9. `finding_evidence`
> 
> That’s the one.
> 
> ---
> 
> # Final structure
> 
> ## The elegant version
> 
> ```text
> patients
> concepts
> patient_ledger
> care_plans
> concept_relationships
> documents
> analysis_runs
> findings
> finding_evidence
> ```
> 
> That’s lean, flexible, and powerful.
> 
> The main rule:
> 
> > If it happened, it goes in `patient_ledger`.  
> > If it is a thing, it goes in `concepts`.  
> > If things relate, it goes in `concept_relationships`.  
> > If AI notices something, it goes in `findings`.  
> > If AI claims something, it must have `finding_evidence`.
> 
> That’s the architecture. Clean. Efficient. Much less dumb.

### User
> thats much better, but what are we missing, or didnt think about that is relevant to all this, go deep but dont add just to add, look for the value added data source we might have forgotten, then provide the final spine, core supporting tables, and resource tables like dictionary, glossaris or options (for the other tables if applicable) then of course the ai tables derived from these tables, how ingestion must take place, what the workflow is and how we get to something functional in hours not days, does not have to be pretty but must provide value insights now. GO, we will use my server for data storage, and hosting and a local llm we can install but fall back to openai api for speed if the server takes too long.

### Assistant
> Good correction path. I’m going to tighten this into a buildable v0: what data actually adds signal, what to exclude, the final table spine, ingestion rules, AI workflow, and a same-day implementation path on your server.

### Assistant
> You’re aiming for the correct thing now:
> 
> > **A patient-state intelligence system, not a medical database cosplay project.**
> 
> The goal is not to model all of medicine. The goal is to catch **patterns, risks, interactions, contradictions, and useful doctor questions** fast.
> 
> The v0 should answer questions like:
> 
> - “What tends to happen before her heart rate spikes?”
> - “What meds, OTCs, foods, behaviors, or environments may be interacting?”
> - “What changed before this flare?”
> - “What is real COPD signal vs anxiety overlay vs medication side effect vs environment?”
> - “What do we need to ask the doctor/pharmacist?”
> - “What are we missing that blocks clarity?”
> 
> That requires a simple spine, but we need a few things we almost forgot.
> 
> ---
> 
> # 1. What we were missing
> 
> ## A. Negative events
> 
> This is huge.
> 
> Most systems only log what happened. But health patterns often depend on what **did not happen**.
> 
> Examples:
> 
> - medication refused
> - medication missed
> - oxygen not picked up
> - patient did not sleep
> - did not eat
> - did not drink water
> - did not use prescribed device
> - did not calm/rest despite symptoms
> - did not have fever
> - oxygen was not low despite air hunger
> 
> These are not side notes. They are signal.
> 
> So the ledger must support:
> 
> | Concept | Example |
> |---|---|
> | `status = refused` | hydroxyzine refused |
> | `status = missed` | dose not taken |
> | `status = absent` | no fever observed |
> | `status = unavailable` | oxygen tanks not available |
> | `status = normal` | SpO2 stable despite distress |
> 
> That lets the AI reason correctly.
> 
> ---
> 
> ## B. Baseline and “normal for this person”
> 
> A raw value means less than a deviation.
> 
> For one patient:
> 
> - HR 110 may be normal-ish during stress
> - SpO2 94 may be baseline
> - glucose 186 may be explainable after steroids/food
> - BP 107/56 may be normal for one arm but low for another
> 
> So the system needs a **baseline layer**, but not a separate overbuilt table per metric.
> 
> Use a simple profile table or patient-level JSON baseline.
> 
> Value-added baselines:
> 
> - resting HR
> - stress HR
> - baseline SpO2 on/off oxygen
> - usual BP by arm if relevant
> - usual glucose fasting/non-fasting
> - usual respiratory comfort level
> - normal mental status
> - normal sleep pattern
> - known triggers
> - known “false alarms”
> - known “real emergency pattern”
> 
> ---
> 
> ## C. Source reliability
> 
> Not all data is equal.
> 
> A pulse ox reading during movement is weaker than a stable reading. A caregiver observation may be strong for behavior but weaker for hidden symptoms. A hospital discharge paper is strong for medication changes but can still be incomplete.
> 
> Each event needs:
> 
> - source
> - confidence
> - device/method
> - whether patient-reported, caregiver-observed, device-measured, document-extracted, or doctor-confirmed
> 
> This prevents the AI from treating “she felt hot” the same as “temp 103.1 oral thermometer.”
> 
> ---
> 
> ## D. “Care action → response” tracking
> 
> This is where insight hides.
> 
> You need to know what helped, what failed, and what made things worse.
> 
> Examples:
> 
> - sat upright → breathing improved
> - stopped talking → HR dropped
> - albuterol → dyspnea improved but HR rose
> - hydroxyzine refused → anxiety continued
> - prednisone → breathing improved but glucose/HR/anxiety worsened
> - oxygen applied → SpO2 improved or no change
> - cool room/warm room → symptoms changed
> 
> The event ledger should support response tracking through linked events.
> 
> Add:
> 
> - `parent_event_id`
> - `episode_id`
> 
> So an intervention and its outcome can be grouped.
> 
> ---
> 
> ## E. Episodes
> 
> A health event is usually not one row. It is a cluster.
> 
> Example:
> 
> > COPD/anxiety/tachycardia episode on May 20.
> 
> That episode might include:
> 
> - prednisone taken
> - food eaten
> - albuterol used
> - hydroxyzine refused
> - talking continuously
> - HR 150
> - SpO2 95
> - EMS called
> - hospital visit
> - eventual outcome
> 
> So you need an **episode table**, but keep it lean. It gives the AI a bucket to analyze.
> 
> ---
> 
> ## F. Medication reconciliation
> 
> This is probably the highest-value forgotten piece.
> 
> You need to compare:
> 
> 1. what the doctor says she should take  
> 2. what the pharmacy filled  
> 3. what is physically in the house  
> 4. what she actually takes  
> 5. what she refuses or delays  
> 6. what OTCs/foods/supplements are mixed in  
> 
> Most medical chaos lives in the gap between those six.
> 
> The system needs to track:
> 
> - prescribed meds
> - active vs stopped meds
> - duplicate meds
> - PRN meds
> - max daily dose
> - last taken
> - refused/missed doses
> - OTCs and supplements
> - “old bottle still in house”
> - “hospital changed this but home list still wrong”
> 
> That is pure value.
> 
> ---
> 
> ## G. Device and equipment context
> 
> Especially for COPD/respiratory care.
> 
> You may need concepts/events for:
> 
> - oxygen concentrator
> - oxygen tank
> - flow rate
> - nebulizer
> - inhaler
> - pulse ox
> - CPAP/BiPAP if relevant
> - spacer
> - wheelchair/scooter
> - thermometer
> - glucose meter
> 
> Because sometimes the problem is not the body. It is the equipment, supply, setting, or usage.
> 
> Examples:
> 
> - oxygen unavailable
> - oxygen flow changed
> - pulse ox reading unreliable
> - inhaler technique poor
> - tank empty
> - concentrator disliked
> - device not used because uncomfortable
> 
> That belongs in the ledger.
> 
> ---
> 
> ## H. Instructions and thresholds from doctors
> 
> This is massively important.
> 
> The system should store:
> 
> - “Go to ER if SpO2 below X”
> - “Use nebulizer every X hours”
> - “Take prednisone with food”
> - “Call doctor if glucose over X”
> - “Do not exceed X rescue inhaler doses”
> - “Use oxygen at X LPM”
> 
> Otherwise AI is guessing. The doctor’s instructions should become rules.
> 
> ---
> 
> ## I. Missing-data findings
> 
> The AI should not only say what it sees. It should say what it **cannot determine**.
> 
> Examples:
> 
> - exact albuterol time missing
> - respiratory rate missing during episode
> - no recent EKG available
> - no med reconciliation after discharge
> - glucose not tracked after prednisone
> - no oxygen flow rate recorded with SpO2
> - no pharmacy interaction review documented
> 
> This may be one of the most useful outputs.
> 
> ---
> 
> ## J. Temporal windows
> 
> The body is time-based.
> 
> The agent needs to reason in windows:
> 
> | Window | Use |
> |---|---|
> | 0–15 min | immediate reaction, panic spike, inhaler response |
> | 15–90 min | rescue inhaler effect, anxiety escalation |
> | 1–6 hrs | food/glucose, med side effects |
> | 6–24 hrs | steroid effects, infection progression, sleep impact |
> | 1–7 days | med changes, flares, antibiotics, prednisone course |
> | 30+ days | trend/baseline drift |
> 
> This does not require more tables. It requires analysis logic.
> 
> ---
> 
> # 2. Final schema architecture
> 
> The elegant version:
> 
> ## Spine tables
> 
> These are the core.
> 
> 1. `patients`
> 2. `episodes`
> 3. `concepts`
> 4. `patient_ledger`
> 
> ## Core supporting tables
> 
> 5. `care_plans`
> 6. `concept_relationships`
> 7. `documents`
> 8. `source_records`
> 
> ## Resource/dictionary tables
> 
> 9. `option_sets`
> 10. `option_values`
> 11. `concept_aliases`
> 12. `unit_mappings`
> 
> ## AI/derived tables
> 
> 13. `analysis_runs`
> 14. `findings`
> 15. `finding_evidence`
> 16. `derived_relationships`
> 17. `patient_baselines`
> 
> That is the full v0/v1.  
> Still lean. No seven event tables. No schema confetti.
> 
> ---
> 
> # 3. Final table design
> 
> ## 1. `patients`
> 
> Stores the human and baseline summary.
> 
> ```sql
> CREATE TABLE patients (
>   patient_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   display_name TEXT NOT NULL,
>   dob DATE,
>   sex_at_birth TEXT,
>   baseline_profile_json JSONB DEFAULT '{}'::jsonb,
>   risk_profile_json JSONB DEFAULT '{}'::jsonb,
>   notes TEXT,
>   created_at TIMESTAMPTZ DEFAULT now(),
>   updated_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> Use `baseline_profile_json` for:
> 
> ```json
> {
>   "spo2_baseline": "94-96 on oxygen",
>   "resting_hr_baseline": "90-110",
>   "right_arm_bp_note": "often lower",
>   "known_conditions": ["COPD", "anxiety overlay", "steroid-related glucose elevation suspected"],
>   "known_triggers": ["talking continuously", "cold room", "rescue inhaler overuse", "poor sleep"],
>   "emergency_thresholds": {
>     "spo2": "<90 sustained or per clinician instruction",
>     "hr": ">130 sustained with distress"
>   }
> }
> ```
> 
> ---
> 
> ## 2. `episodes`
> 
> Groups related ledger entries.
> 
> ```sql
> CREATE TABLE episodes (
>   episode_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   patient_id UUID REFERENCES patients(patient_id),
>   episode_start TIMESTAMPTZ NOT NULL,
>   episode_end TIMESTAMPTZ,
>   episode_type TEXT,
>   title TEXT,
>   summary TEXT,
>   severity TEXT,
>   outcome TEXT,
>   status TEXT DEFAULT 'open',
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> Examples:
> 
> - `respiratory_distress_episode`
> - `tachycardia_episode`
> - `medication_refusal_episode`
> - `er_visit`
> - `fall`
> - `rash_flare`
> - `glucose_spike`
> 
> ---
> 
> ## 3. `concepts`
> 
> The master dictionary of things.
> 
> ```sql
> CREATE TABLE concepts (
>   concept_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   name TEXT NOT NULL,
>   concept_type TEXT NOT NULL,
>   standard_code TEXT,
>   code_system TEXT,
>   parent_concept_id UUID REFERENCES concepts(concept_id),
>   properties_json JSONB DEFAULT '{}'::jsonb,
>   active BOOLEAN DEFAULT true,
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> Concept types:
> 
> - `medication`
> - `otc`
> - `supplement`
> - `food`
> - `beverage`
> - `vital`
> - `symptom`
> - `condition`
> - `behavior`
> - `environment`
> - `device`
> - `lab`
> - `instruction`
> - `care_action`
> - `body_system`
> - `risk_factor`
> 
> Examples:
> 
> | Name | Type |
> |---|---|
> | Albuterol | medication |
> | Prednisone | medication |
> | Hydroxyzine | medication |
> | Diphenhydramine | otc |
> | Peanut butter | food |
> | Caffeine | beverage |
> | SpO2 | vital |
> | Heart rate | vital |
> | Air hunger | symptom |
> | Talking continuously | behavior |
> | Cold room | environment |
> | Oxygen concentrator | device |
> | COPD | condition |
> | Anxiety | condition/symptom |
> | Rash | symptom |
> 
> ---
> 
> ## 4. `patient_ledger`
> 
> The universal timeline.
> 
> ```sql
> CREATE TABLE patient_ledger (
>   ledger_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   patient_id UUID REFERENCES patients(patient_id),
>   episode_id UUID REFERENCES episodes(episode_id),
>   parent_ledger_id UUID REFERENCES patient_ledger(ledger_id),
> 
>   event_time TIMESTAMPTZ NOT NULL,
>   event_type TEXT NOT NULL,
>   event_subtype TEXT,
>   concept_id UUID REFERENCES concepts(concept_id),
> 
>   value_numeric NUMERIC,
>   value_text TEXT,
>   unit TEXT,
> 
>   status TEXT,
>   severity TEXT,
>   confidence NUMERIC DEFAULT 1.0,
> 
>   source_type TEXT,
>   source_id UUID,
>   observed_by TEXT,
> 
>   context_json JSONB DEFAULT '{}'::jsonb,
>   notes TEXT,
> 
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> This is the table.
> 
> The rule:
> 
> > If it happened, almost happened, should have happened, did not happen, was measured, was refused, was observed, or was instructed — it goes here.
> 
> Examples:
> 
> | event_type | event_subtype | concept | status |
> |---|---|---|---|
> | medication | taken | Prednisone | taken |
> | medication | refused | Hydroxyzine | refused |
> | vital | heart_rate | Heart rate | measured |
> | vital | spo2 | SpO2 | measured |
> | symptom | air_hunger | Air hunger | reported |
> | behavior | talking | Talking continuously | observed |
> | intake | food | Peanut butter | consumed |
> | environment | temperature | Cold room | observed |
> | device | oxygen | Oxygen tank | unavailable |
> | care_action | reposition | Sitting upright | completed |
> | instruction | doctor_order | Use oxygen at X LPM | active |
> | note | caregiver_note | General note | observed |
> 
> ---
> 
> # 4. Core supporting tables
> 
> ## 5. `care_plans`
> 
> What should happen.
> 
> ```sql
> CREATE TABLE care_plans (
>   plan_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   patient_id UUID REFERENCES patients(patient_id),
>   concept_id UUID REFERENCES concepts(concept_id),
>   plan_type TEXT NOT NULL,
> 
>   instructions TEXT,
>   dose_amount NUMERIC,
>   dose_unit TEXT,
>   frequency TEXT,
>   route TEXT,
>   max_daily_amount NUMERIC,
>   max_daily_unit TEXT,
> 
>   start_date DATE,
>   end_date DATE,
>   status TEXT DEFAULT 'active',
> 
>   source_document_id UUID,
>   provider_name TEXT,
>   metadata_json JSONB DEFAULT '{}'::jsonb,
> 
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> Plan types:
> 
> - `medication_order`
> - `oxygen_order`
> - `monitoring_plan`
> - `diet_instruction`
> - `activity_instruction`
> - `emergency_action_plan`
> - `follow_up_plan`
> - `device_use_plan`
> 
> This lets AI detect care gaps:
> 
> > “Hydroxyzine is ordered PRN but repeatedly refused during anxiety/tachycardia episodes.”
> 
> ---
> 
> ## 6. `concept_relationships`
> 
> Known relationships.
> 
> ```sql
> CREATE TABLE concept_relationships (
>   relationship_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   source_concept_id UUID REFERENCES concepts(concept_id),
>   target_concept_id UUID REFERENCES concepts(concept_id),
> 
>   relationship_type TEXT NOT NULL,
>   strength NUMERIC,
>   severity TEXT,
>   evidence_level TEXT,
> 
>   source TEXT,
>   notes TEXT,
>   metadata_json JSONB DEFAULT '{}'::jsonb,
> 
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> Relationship types:
> 
> - `may_cause`
> - `may_worsen`
> - `may_improve`
> - `treats`
> - `interacts_with`
> - `contraindicated_with`
> - `raises`
> - `lowers`
> - `masks`
> - `duplicates_effect`
> - `triggered_by`
> - `associated_with`
> - `requires_monitoring_of`
> 
> Examples:
> 
> | Source | Relationship | Target |
> |---|---|---|
> | Albuterol | may_cause | Tachycardia |
> | Albuterol | may_worsen | Anxiety |
> | Prednisone | raises | Blood glucose |
> | Prednisone | may_worsen | Anxiety |
> | Hydroxyzine | may_cause | Sedation |
> | Diphenhydramine | duplicates_effect | Hydroxyzine |
> | Talking continuously | may_worsen | Dyspnea |
> | Cold room | may_trigger | Breathing discomfort |
> | COPD | requires_monitoring_of | SpO2 |
> | Prednisone | requires_monitoring_of | Glucose |
> 
> ---
> 
> ## 7. `documents`
> 
> Raw source material.
> 
> ```sql
> CREATE TABLE documents (
>   document_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   patient_id UUID REFERENCES patients(patient_id),
> 
>   document_type TEXT,
>   document_date DATE,
>   title TEXT,
>   storage_uri TEXT,
> 
>   extracted_text TEXT,
>   summary TEXT,
>   metadata_json JSONB DEFAULT '{}'::jsonb,
> 
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> Document types:
> 
> - `discharge_summary`
> - `medication_list`
> - `lab_report`
> - `imaging_report`
> - `visit_note`
> - `pharmacy_label`
> - `after_visit_summary`
> - `insurance_or_care_doc`
> - `photo`
> - `screenshot`
> - `caregiver_note`
> 
> ---
> 
> ## 8. `source_records`
> 
> Optional but useful. This tracks ingestion batches.
> 
> ```sql
> CREATE TABLE source_records (
>   source_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   source_type TEXT NOT NULL,
>   source_name TEXT,
>   imported_at TIMESTAMPTZ DEFAULT now(),
>   raw_payload JSONB,
>   processing_status TEXT DEFAULT 'new',
>   notes TEXT
> );
> ```
> 
> Examples:
> 
> - manual form entry
> - voice note transcript
> - Paperless document
> - CSV import
> - OCR batch
> - device export
> - AI extraction batch
> 
> This gives you traceability without bloating the ledger.
> 
> ---
> 
> # 5. Resource / dictionary tables
> 
> These prevent chaos without creating fifty tables.
> 
> ## 9. `option_sets`
> 
> ```sql
> CREATE TABLE option_sets (
>   option_set_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   name TEXT UNIQUE NOT NULL,
>   description TEXT
> );
> ```
> 
> Examples:
> 
> - `event_type`
> - `event_status`
> - `severity`
> - `source_type`
> - `concept_type`
> - `relationship_type`
> - `finding_type`
> - `recommendation_type`
> - `plan_type`
> 
> ---
> 
> ## 10. `option_values`
> 
> ```sql
> CREATE TABLE option_values (
>   option_value_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   option_set_id UUID REFERENCES option_sets(option_set_id),
>   value TEXT NOT NULL,
>   label TEXT,
>   sort_order INT,
>   active BOOLEAN DEFAULT true,
>   metadata_json JSONB DEFAULT '{}'::jsonb
> );
> ```
> 
> This lets you control dropdowns in NocoDB or a quick UI.
> 
> ---
> 
> ## 11. `concept_aliases`
> 
> Critical for ingestion.
> 
> People do not say things consistently.
> 
> ```sql
> CREATE TABLE concept_aliases (
>   alias_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   concept_id UUID REFERENCES concepts(concept_id),
>   alias TEXT NOT NULL,
>   source TEXT,
>   confidence NUMERIC DEFAULT 1.0
> );
> ```
> 
> Examples:
> 
> | Alias | Concept |
> |---|---|
> | pred | Prednisone |
> | prednisone pill | Prednisone |
> | rescue inhaler | Albuterol |
> | breathing treatment | Nebulizer treatment |
> | oxygen | Oxygen therapy |
> | air hunger | Dyspnea |
> | can’t breathe | Dyspnea |
> | talking nonstop | Talking continuously |
> | hydrox | Hydroxyzine |
> 
> This is one of the most valuable tables. It lets messy human input become structured data.
> 
> ---
> 
> ## 12. `unit_mappings`
> 
> For normalization.
> 
> ```sql
> CREATE TABLE unit_mappings (
>   unit_mapping_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   raw_unit TEXT NOT NULL,
>   normalized_unit TEXT NOT NULL,
>   conversion_factor NUMERIC DEFAULT 1,
>   notes TEXT
> );
> ```
> 
> Examples:
> 
> - `mg → mg`
> - `mcg → mcg`
> - `puffs → puff`
> - `% → percent`
> - `bpm → bpm`
> - `LPM → lpm`
> - `tabs → tablet`
> 
> ---
> 
> # 6. AI / derived tables
> 
> ## 13. `analysis_runs`
> 
> ```sql
> CREATE TABLE analysis_runs (
>   analysis_run_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   patient_id UUID REFERENCES patients(patient_id),
> 
>   run_time TIMESTAMPTZ DEFAULT now(),
>   analysis_type TEXT,
>   window_start TIMESTAMPTZ,
>   window_end TIMESTAMPTZ,
> 
>   model_used TEXT,
>   prompt_version TEXT,
>   status TEXT,
>   summary TEXT,
>   metadata_json JSONB DEFAULT '{}'::jsonb
> );
> ```
> 
> Analysis types:
> 
> - `episode_review`
> - `daily_review`
> - `interaction_scan`
> - `med_reconciliation`
> - `doctor_packet`
> - `missing_data_audit`
> - `baseline_update`
> - `red_flag_scan`
> 
> ---
> 
> ## 14. `findings`
> 
> ```sql
> CREATE TABLE findings (
>   finding_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   analysis_run_id UUID REFERENCES analysis_runs(analysis_run_id),
>   patient_id UUID REFERENCES patients(patient_id),
> 
>   finding_type TEXT NOT NULL,
>   title TEXT NOT NULL,
>   description TEXT,
> 
>   severity TEXT,
>   confidence NUMERIC,
>   status TEXT DEFAULT 'open',
> 
>   doctor_question TEXT,
>   recommendation_type TEXT,
> 
>   metadata_json JSONB DEFAULT '{}'::jsonb,
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> Finding types:
> 
> - `interaction`
> - `pattern`
> - `red_flag`
> - `care_gap`
> - `missing_data`
> - `hypothesis`
> - `contradiction`
> - `trend`
> - `baseline_deviation`
> - `medication_reconciliation_issue`
> 
> ---
> 
> ## 15. `finding_evidence`
> 
> ```sql
> CREATE TABLE finding_evidence (
>   evidence_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   finding_id UUID REFERENCES findings(finding_id),
> 
>   source_type TEXT NOT NULL,
>   source_id UUID NOT NULL,
> 
>   evidence_role TEXT,
>   explanation TEXT,
> 
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> Evidence roles:
> 
> - `supports`
> - `contradicts`
> - `context`
> - `missing`
> - `trigger`
> - `outcome`
> - `baseline`
> 
> Again: no evidence, no trust.
> 
> ---
> 
> ## 16. `derived_relationships`
> 
> AI-generated relationships from observed data.
> 
> ```sql
> CREATE TABLE derived_relationships (
>   derived_relationship_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   patient_id UUID REFERENCES patients(patient_id),
>   analysis_run_id UUID REFERENCES analysis_runs(analysis_run_id),
> 
>   source_ledger_id UUID REFERENCES patient_ledger(ledger_id),
>   target_ledger_id UUID REFERENCES patient_ledger(ledger_id),
> 
>   source_concept_id UUID REFERENCES concepts(concept_id),
>   target_concept_id UUID REFERENCES concepts(concept_id),
> 
>   relationship_type TEXT,
>   time_delta_minutes INT,
>   strength NUMERIC,
>   confidence NUMERIC,
> 
>   explanation TEXT,
>   metadata_json JSONB DEFAULT '{}'::jsonb,
> 
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> Examples:
> 
> - Albuterol event preceded HR spike by 42 minutes.
> - Talking continuously co-occurred with air hunger and HR spike.
> - Hydroxyzine refusal preceded unresolved anxiety episode.
> - Prednisone + high-carb food preceded glucose elevation.
> 
> This is how you get graphs without manually entering graph edges all day.
> 
> ---
> 
> ## 17. `patient_baselines`
> 
> Optional but worth it.
> 
> ```sql
> CREATE TABLE patient_baselines (
>   baseline_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   patient_id UUID REFERENCES patients(patient_id),
>   concept_id UUID REFERENCES concepts(concept_id),
> 
>   context_label TEXT,
>   baseline_low NUMERIC,
>   baseline_high NUMERIC,
>   baseline_avg NUMERIC,
>   unit TEXT,
> 
>   sample_count INT,
>   window_start TIMESTAMPTZ,
>   window_end TIMESTAMPTZ,
> 
>   confidence NUMERIC,
>   notes TEXT,
> 
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> Examples:
> 
> - SpO2 resting on oxygen
> - HR resting
> - HR during anxiety
> - glucose after meals
> - BP right arm
> - BP left arm
> - sleep duration baseline
> 
> ---
> 
> # 7. Final schema map
> 
> ## Spine
> 
> ```text
> patients
> episodes
> concepts
> patient_ledger
> ```
> 
> ## Core supporting
> 
> ```text
> care_plans
> concept_relationships
> documents
> source_records
> ```
> 
> ## Resource/dictionary
> 
> ```text
> option_sets
> option_values
> concept_aliases
> unit_mappings
> ```
> 
> ## AI/derived
> 
> ```text
> analysis_runs
> findings
> finding_evidence
> derived_relationships
> patient_baselines
> ```
> 
> That is the final clean architecture.
> 
> Not too many tables.  
> Not too few.  
> Each table earns its place.
> 
> ---
> 
> # 8. Ingestion rules
> 
> This is where the system either works or becomes junk.
> 
> ## Rule 1: Everything becomes a ledger event
> 
> A voice note like:
> 
> > “She took prednisone at 8, refused hydroxyzine, O2 95, HR 150, talking nonstop, says she can’t breathe.”
> 
> Should become:
> 
> | Time | Type | Concept | Status/Value |
> |---|---|---|---|
> | 8:00 | medication | Prednisone | taken |
> | unknown | medication | Hydroxyzine | refused |
> | current | vital | SpO2 | 95% |
> | current | vital | Heart rate | 150 bpm |
> | current | behavior | Talking continuously | observed |
> | current | symptom | Air hunger | reported |
> 
> No paragraph blob only. Paragraph can remain in notes, but structured events must be extracted.
> 
> ---
> 
> ## Rule 2: Never overwrite raw data
> 
> Store raw text/source in `source_records` or `documents`.
> 
> Then extract structured rows into `patient_ledger`.
> 
> Raw stays raw. Structured gets analyzed.
> 
> ---
> 
> ## Rule 3: Uncertainty is allowed
> 
> If time is unclear, use best estimate but mark lower confidence.
> 
> Example:
> 
> | Field | Value |
> |---|---|
> | event_time | approximate current time |
> | confidence | 0.6 |
> | notes | “Exact time not provided; inferred from entry time.” |
> 
> Do not block ingestion because something is imperfect.
> 
> ---
> 
> ## Rule 4: Refusals and missed actions are first-class
> 
> If a med was refused, log it.
> 
> If oxygen was supposed to be picked up but was not, log it.
> 
> If a doctor instruction was not followed, log it.
> 
> This is not about blame. It is about causality.
> 
> ---
> 
> ## Rule 5: Every extraction should map to concepts
> 
> If no concept exists, create one.
> 
> Example:
> 
> “talking like a meth head on a scooter” should not be stored as the concept. The concept is:
> 
> > `Talking continuously / psychomotor agitation`
> 
> The colorful note can stay in notes. The clinical structure gets normalized.
> 
> ---
> 
> ## Rule 6: Episodes can be created automatically
> 
> If the system sees clustered events within a time window:
> 
> - HR high
> - dyspnea
> - anxiety
> - medication event
> - EMS/ER
> 
> Create or suggest an episode.
> 
> ---
> 
> # 9. Functional workflow
> 
> ## Input sources
> 
> Fastest useful sources:
> 
> 1. Manual quick entry form
> 2. Voice note → transcript → ledger extraction
> 3. Photo/screenshot of discharge papers
> 4. Medication bottle photo
> 5. Existing notes copied into an intake box
> 6. Vitals typed manually
> 7. Food/OTC quick log
> 8. Environment/behavior quick log
> 
> Later sources:
> 
> - Paperless-ngx OCR
> - pharmacy exports
> - glucose meter exports
> - pulse ox/BP device exports
> - weather/pollen API
> - hospital portal downloads
> 
> Do not start with device integrations. That is a trap. Start with manual/voice/document ingestion.
> 
> ---
> 
> # 10. AI workflow
> 
> ## Step 1: Intake parser
> 
> Input: messy text.
> 
> Output:
> 
> - proposed ledger rows
> - proposed concepts
> - uncertainty flags
> - questions only if truly needed
> 
> Example output:
> 
> ```json
> {
>   "ledger_events": [
>     {
>       "event_type": "medication",
>       "event_subtype": "taken",
>       "concept_name": "Prednisone",
>       "event_time": "2026-05-20T08:00:00-05:00",
>       "status": "taken",
>       "confidence": 0.9
>     },
>     {
>       "event_type": "medication",
>       "event_subtype": "refused",
>       "concept_name": "Hydroxyzine",
>       "status": "refused",
>       "confidence": 0.8
>     },
>     {
>       "event_type": "vital",
>       "event_subtype": "heart_rate",
>       "concept_name": "Heart rate",
>       "value_numeric": 150,
>       "unit": "bpm",
>       "severity": "high",
>       "confidence": 0.95
>     }
>   ]
> }
> ```
> 
> ---
> 
> ## Step 2: Normalizer
> 
> Takes parsed items and:
> 
> - maps aliases to concepts
> - creates missing concepts
> - normalizes units
> - attaches to episode if relevant
> - stores in `patient_ledger`
> 
> ---
> 
> ## Step 3: Rule scanner
> 
> Runs deterministic checks:
> 
> - HR above threshold
> - SpO2 below threshold
> - dangerous med duplication
> - repeated rescue inhaler use
> - missed/refused medication during episode
> - glucose high after steroid/food
> - fall risk + sedating meds
> - rash + med/food exposure
> - missing oxygen supply
> - missing doctor thresholds
> 
> This should not rely entirely on the LLM.
> 
> ---
> 
> ## Step 4: Interaction scanner
> 
> Checks:
> 
> - concept relationships
> - recent meds
> - OTCs
> - foods
> - supplements
> - conditions
> - behaviors
> - environment
> - lab/vital changes after exposure
> 
> Looks for:
> 
> - drug-drug
> - drug-food
> - drug-condition
> - drug-behavior
> - drug-environment
> - duplicate side effects
> - masked symptoms
> - response failure
> 
> ---
> 
> ## Step 5: Temporal graph builder
> 
> Creates `derived_relationships`.
> 
> Examples:
> 
> - `Prednisone → preceded → glucose 186`
> - `Albuterol → preceded → HR 150`
> - `Talking continuously → co_occurred_with → air hunger`
> - `Hydroxyzine refusal → preceded → ongoing anxiety`
> - `SpO2 95 → contradicts → severe oxygen desaturation`
> 
> This is where the intelligence starts.
> 
> ---
> 
> ## Step 6: Finding generator
> 
> Writes doctor-facing insights:
> 
> - pattern
> - evidence
> - confidence
> - what to ask
> - missing data
> - urgency
> 
> Example:
> 
> > **Finding:** Recurrent high-HR dyspnea episodes with stable SpO2  
> > **Evidence:** HR 150–164 while SpO2 recorded around 95; prolonged talking/anxiety behavior observed; hydroxyzine refused; bronchodilator/steroid exposure nearby.  
> > **Question:** Ask pulmonology/PCP whether rescue med side effects, anxiety overlay, or cardiac rhythm evaluation should be reviewed.
> 
> That is useful and not pretending to diagnose.
> 
> ---
> 
> # 11. What to build in hours, not days
> 
> You already have the right server mindset. Do this ugly and useful first.
> 
> ## Fastest stack
> 
> Use:
> 
> - **Postgres** for storage
> - **NocoDB** for quick forms/tables
> - **Python script** for ingestion + analysis
> - **OpenAI API fallback** for fast extraction/analysis
> - **Ollama/local LLM later** for private/offline processing
> - **Paperless-ngx later** for document ingestion
> 
> Do not build a custom frontend first. That is how we lose three days. Use NocoDB or a basic Streamlit page.
> 
> ---
> 
> # 12. Same-day build plan
> 
> ## Hour 0–1: Create database tables
> 
> On QiServer:
> 
> - create Postgres database: `qiclinical`
> - run schema
> - expose through NocoDB if you want a UI
> 
> Tables needed today:
> 
> ```text
> patients
> episodes
> concepts
> patient_ledger
> care_plans
> concept_relationships
> documents
> source_records
> analysis_runs
> findings
> finding_evidence
> derived_relationships
> concept_aliases
> option_sets
> option_values
> unit_mappings
> patient_baselines
> ```
> 
> If rushing, create only:
> 
> ```text
> patients
> episodes
> concepts
> patient_ledger
> concept_relationships
> analysis_runs
> findings
> finding_evidence
> concept_aliases
> ```
> 
> That is enough for value.
> 
> ---
> 
> ## Hour 1–2: Seed concepts
> 
> Seed only high-value concepts first.
> 
> ### Meds
> 
> - Prednisone
> - Albuterol
> - Hydroxyzine
> - Guaifenesin
> - Oxygen therapy
> - Any current daily meds
> - Any OTCs in house
> - Benadryl/diphenhydramine
> - Tylenol/acetaminophen
> - ibuprofen
> - caffeine
> 
> ### Vitals
> 
> - Heart rate
> - SpO2
> - Blood pressure systolic
> - Blood pressure diastolic
> - Temperature
> - Blood glucose
> - Respiratory rate
> - Weight
> 
> ### Symptoms
> 
> - Dyspnea
> - Air hunger
> - Wheezing
> - Cough
> - Congestion
> - Anxiety
> - Panic
> - Tremor
> - Rash
> - Dizziness
> - Confusion
> - Fatigue
> - Chest pain
> - Swelling
> 
> ### Behaviors
> 
> - Talking continuously
> - Pacing/restlessness
> - Refused medication
> - Missed medication
> - Poor sleep
> - Exertion
> - Lying flat
> - Symptom checking
> - Agitation
> 
> ### Environment/devices
> 
> - Cold room
> - Hot room
> - Dust
> - Smoke
> - Cleaning fumes
> - Oxygen tank
> - Oxygen concentrator
> - Nebulizer
> - Pulse oximeter
> - Glucose meter
> - BP cuff
> 
> ---
> 
> ## Hour 2–3: Create quick-entry form
> 
> In NocoDB, create a view for `patient_ledger` called:
> 
> > **Quick Health Log**
> 
> Fields shown:
> 
> - event_time
> - event_type
> - event_subtype
> - concept_id
> - value_numeric
> - value_text
> - unit
> - status
> - severity
> - notes
> 
> Make it frictionless.
> 
> Do not make it perfect.
> 
> ---
> 
> ## Hour 3–4: Create messy-text ingestion script
> 
> One input:
> 
> > Paste messy note.
> 
> Script does:
> 
> 1. sends note to LLM
> 2. extracts structured events
> 3. maps concepts by alias
> 4. inserts into `patient_ledger`
> 5. creates missing concepts if needed
> 6. stores raw note in `source_records`
> 
> This gives value immediately.
> 
> ---
> 
> ## Hour 4–5: Create first analysis script
> 
> Run:
> 
> > Analyze last 24 hours.
> 
> It should produce:
> 
> 1. episode summary
> 2. med/OTC/food/environment/behavior timeline
> 3. abnormal vitals
> 4. interactions to consider
> 5. missing data
> 6. doctor questions
> 7. red flags
> 
> Store output in:
> 
> - `analysis_runs`
> - `findings`
> - `finding_evidence`
> 
> ---
> 
> ## Hour 5–6: Create doctor packet
> 
> A simple Markdown export:
> 
> ```text
> Clinical Pattern Summary
> Patient:
> Window:
> Main concern:
> Key timeline:
> Vitals:
> Meds/OTCs/Food:
> Behavior/Environment:
> Patterns noticed:
> Medication/interaction concerns:
> Missing data:
> Questions for doctor/pharmacist:
> Not a diagnosis.
> ```
> 
> This is the first useful artifact.
> 
> ---
> 
> # 13. First analysis prompts
> 
> ## Intake extraction prompt
> 
> Use this with OpenAI first because speed matters.
> 
> ```text
> You are a clinical data extraction assistant.
> 
> Convert the messy caregiver/patient note into structured patient ledger events.
> 
> Rules:
> - Do not diagnose.
> - Extract only what is stated or strongly implied.
> - Separate medications, vitals, symptoms, behaviors, environment, food/intake, care actions, instructions, and notes.
> - Include refused, missed, unavailable, absent, and normal findings.
> - If time is missing, use null and explain uncertainty.
> - If exact concept name is unclear, use the closest plain clinical concept.
> - Preserve the original wording in notes when helpful.
> - Output valid JSON only.
> 
> Required JSON:
> {
>   "events": [
>     {
>       "event_time": null,
>       "event_type": "",
>       "event_subtype": "",
>       "concept_name": "",
>       "value_numeric": null,
>       "value_text": null,
>       "unit": null,
>       "status": "",
>       "severity": "",
>       "confidence": 0.0,
>       "notes": "",
>       "context_json": {}
>     }
>   ],
>   "possible_episode": {
>     "title": "",
>     "episode_type": "",
>     "severity": "",
>     "summary": ""
>   },
>   "missing_or_uncertain": []
> }
> ```
> 
> ---
> 
> ## Analysis prompt
> 
> ```text
> You are a clinical pattern analysis assistant.
> 
> Analyze the patient ledger events below. Do not diagnose. Identify patterns, interactions to review, contradictions, missing data, and doctor/pharmacist questions.
> 
> Prioritize:
> 1. medication, OTC, supplement, and food interactions
> 2. medication timing versus symptoms/vitals
> 3. behavior and environment effects
> 4. patient-specific baseline deviations
> 5. care gaps and refused/missed actions
> 6. urgent red flags
> 7. useful next data to collect
> 
> Output valid JSON:
> {
>   "summary": "",
>   "findings": [
>     {
>       "finding_type": "",
>       "title": "",
>       "description": "",
>       "severity": "",
>       "confidence": 0.0,
>       "recommendation_type": "",
>       "doctor_question": "",
>       "evidence": [
>         {
>           "source": "",
>           "event_time": "",
>           "reason": ""
>         }
>       ],
>       "missing_data": []
>     }
>   ],
>   "doctor_packet_bullets": [],
>   "not_diagnosis_statement": "This identifies patterns and questions for clinician review, not a diagnosis."
> }
> ```
> 
> ---
> 
> # 14. First real insights this should catch
> 
> Based on the type of situation you’ve been describing, your v0 should immediately be able to flag:
> 
> ## Medication/physiology patterns
> 
> - bronchodilator use near tachycardia
> - prednisone near anxiety/glucose elevation
> - sedating meds refused during anxiety escalation
> - OTC cold meds that may worsen HR/BP/anxiety
> - duplicate sedating meds
> - missed meds before flare
> - PRN rescue med overuse
> - food + steroid + glucose spikes
> 
> ## Behavior/environment patterns
> 
> - prolonged talking near air hunger and HR spikes
> - cold/hot room worsening distress
> - poor sleep preceding symptom spirals
> - exertion before dyspnea
> - lying position worsening breathing
> - refusal loops causing escalation
> 
> ## Contradictions
> 
> - “Cannot breathe” while SpO2 stable
> - high HR with normal oxygen
> - severe distress but no fever
> - glucose high after steroids/food
> - medication prescribed but not taken
> - discharge instructions conflict with home routine
> 
> ## Missing data
> 
> - respiratory rate
> - oxygen flow rate
> - exact albuterol/nebulizer times
> - exact prednisone dose/time
> - current complete med list
> - recent EKG/cardiac workup
> - pharmacist interaction review
> - doctor thresholds for ER vs home management
> 
> ---
> 
> # 15. What not to build yet
> 
> Do **not** start with:
> 
> - full FHIR implementation
> - custom mobile app
> - fancy graph UI
> - multi-agent dashboard
> - perfect ontology
> - wearable/device integrations
> - full document OCR automation
> - Neo4j-first design
> - complex permission model
> 
> That is day-two brain candy. Useful later, but today it slows you down.
> 
> Today’s win:
> 
> > paste messy health log → structured ledger → AI pattern findings → doctor questions
> 
> That’s it.
> 
> ---
> 
> # 16. Local LLM vs OpenAI
> 
> ## Fast path
> 
> Use OpenAI API for:
> 
> - messy text extraction
> - doctor-packet summaries
> - reasoning over small windows
> 
> Use local rules/Python for:
> 
> - thresholds
> - time windows
> - basic correlations
> - finding evidence
> - database insert/query
> 
> ## Local path
> 
> Install/use Ollama for:
> 
> - lightweight summarization
> - private offline analysis
> - fallback extraction once tested
> 
> Likely models to try:
> 
> - `llama3.1:8b`
> - `qwen2.5:7b`
> - `qwen2.5-coder` for code tasks
> - `mistral` if you want smaller/faster
> 
> But don’t let local model setup block function. OpenAI first, local later. Speed wins today.
> 
> ---
> 
> # 17. Immediate v0 commands conceptually
> 
> You need four scripts:
> 
> ```text
> 01_create_schema.py
> 02_seed_concepts.py
> 03_ingest_note.py
> 04_analyze_window.py
> ```
> 
> Then later:
> 
> ```text
> 05_export_doctor_packet.py
> 06_ingest_document.py
> 07_update_baselines.py
> 08_build_graph_edges.py
> ```
> 
> This is enough.
> 
> ---
> 
> # 18. The actual system loop
> 
> ## Daily
> 
> 1. Enter messy notes / vitals / meds.
> 2. Ingest to ledger.
> 3. Run daily analysis.
> 4. Review findings.
> 5. Export doctor packet if needed.
> 
> ## During episode
> 
> 1. Log vitals and what happened.
> 2. Log meds taken/refused.
> 3. Log food/OTC/environment/behavior.
> 4. Run episode analysis.
> 5. Decide: monitor, call doctor, pharmacist review, urgent care/EMS based on red flags and clinical instructions.
> 
> ## Before doctor appointment
> 
> 1. Run `doctor_packet`.
> 2. Include top 5 findings only.
> 3. Include supporting timeline.
> 4. Include med reconciliation issues.
> 5. Include exact questions.
> 
> ---
> 
> # 19. Final doctrine
> 
> This is the system rule:
> 
> > The ledger is truth.  
> > Concepts define meaning.  
> > Relationships define known risk.  
> > Derived relationships reveal observed patterns.  
> > Findings must cite evidence.  
> > Doctor packets translate chaos into useful clinical questions.
> 
> That’s the architecture.
> 
> And yes, this can be functional in hours.
> 
> Ugly v0, but useful:
> 
> - Postgres
> - NocoDB quick forms
> - Python ingestion
> - OpenAI extraction
> - simple analysis script
> - Markdown doctor packet
> 
> Then once it proves value, we can bolt on:
> 
> - Paperless OCR
> - Neo4j graph
> - Qdrant document search
> - local LLM
> - voice capture
> - Family Wall / QiNexus integration
> - prettier UI
> 
> But the first version should do one thing brutally well:
> 
> > **Turn messy health reality into a structured timeline that exposes medication, behavior, environment, and symptom patterns worth reviewing with a clinician.**

### User
> i dont wnat this to just create the organization of the mess but find what is wrong, what is contradictory, what the doctor forgot to say or did not account for, with 100s of people touchign this one person each decision each half spoken reality or ego driven dcomment or assumptions made all converge into her reality which is not the rturth just an interpratation fo all the inputs, so i want the ai to know and account for what the doctor said but never take it as the absolute accurate reality.

### Assistant
> Exactly. That is the real problem.
> 
> You are not building a filing cabinet.
> 
> You are building a **truth-reconciliation engine** for a human being whose reality has been filtered through:
> 
> - doctors
> - nurses
> - EMS
> - family
> - caregivers
> - discharge papers
> - medication lists
> - pharmacy substitutions
> - patient fear
> - patient memory
> - caregiver stress
> - assumptions
> - rushed clinical visits
> - ego
> - liability language
> - copy-pasted notes
> - outdated diagnoses
> - half-heard instructions
> - “normal” values that are not normal for her
> - one specialist not seeing what another specialist changed
> 
> So yes: the AI must **respect clinical authority without worshiping it**.
> 
> That is the doctrine.
> 
> ## The core correction
> 
> Do **not** model doctor statements as “truth.”
> 
> Model them as **claims**.
> 
> That is the missing table/class.
> 
> A doctor note is not reality.  
> A caregiver note is not reality.  
> A patient statement is not reality.  
> A vital reading is not always reality.  
> A discharge summary is not always reality.
> 
> They are all **observations, claims, measurements, interpretations, or instructions** with different levels of reliability.
> 
> The system needs to separate:
> 
> 1. **Observed reality**  
>    What was measured, seen, timed, or documented.
> 
> 2. **Reported reality**  
>    What someone said happened.
> 
> 3. **Interpreted reality**  
>    What someone thinks it means.
> 
> 4. **Ordered reality**  
>    What someone instructed should happen.
> 
> 5. **Contradicted reality**  
>    Where claims conflict.
> 
> 6. **Missing reality**  
>    What nobody checked, asked, measured, reconciled, or explained.
> 
> That is how the AI starts finding what is wrong.
> 
> ---
> 
> # The better model
> 
> ## Add one essential concept: `claims`
> 
> Not more event tables. A claim layer.
> 
> A claim is anything someone asserts:
> 
> - “This is anxiety.”
> - “This is COPD.”
> - “Take this medication this way.”
> - “Her oxygen is fine.”
> - “She refused treatment.”
> - “She was stable.”
> - “No medication interactions.”
> - “Follow up with PCP.”
> - “Use oxygen as needed.”
> - “She is noncompliant.”
> - “No acute distress.”
> - “Patient understands discharge instructions.”
> - “Vitals normal.”
> - “This medication is safe.”
> - “This symptom is expected.”
> 
> The AI’s job is to ask:
> 
> > “Compared to the ledger, is this claim supported, contradicted, incomplete, stale, biased, or unverified?”
> 
> That is the engine.
> 
> ---
> 
> # Final doctrine
> 
> Use this as the core principle:
> 
> > **No source is truth. Every source is evidence. Truth emerges from cross-checked, time-aware, patient-specific evidence.**
> 
> That’s the whole system.
> 
> The doctor’s note matters.  
> The patient’s body matters more.  
> The timeline adjudicates.
> 
> ---
> 
> # Revised final spine
> 
> Keep the elegant structure, but add the missing intelligence layer.
> 
> ## Spine tables
> 
> 1. `patients`
> 2. `episodes`
> 3. `concepts`
> 4. `patient_ledger`
> 5. `claims`
> 
> ## Supporting tables
> 
> 6. `care_plans`
> 7. `concept_relationships`
> 8. `documents`
> 9. `source_records`
> 
> ## Dictionary/resource tables
> 
> 10. `option_sets`
> 11. `option_values`
> 12. `concept_aliases`
> 13. `unit_mappings`
> 
> ## AI/derived tables
> 
> 14. `analysis_runs`
> 15. `findings`
> 16. `finding_evidence`
> 17. `derived_relationships`
> 18. `patient_baselines`
> 19. `contradictions`
> 20. `open_questions`
> 
> That is the real version.
> 
> Not bloated. Each addition earns its spot.
> 
> ---
> 
> # The key new table: `claims`
> 
> ## `claims`
> 
> ```sql
> CREATE TABLE claims (
>   claim_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   patient_id UUID REFERENCES patients(patient_id),
>   episode_id UUID REFERENCES episodes(episode_id),
> 
>   claim_time TIMESTAMPTZ,
>   claim_type TEXT NOT NULL,
>   claim_text TEXT NOT NULL,
> 
>   asserted_by_type TEXT,
>   asserted_by_name TEXT,
>   source_type TEXT,
>   source_id UUID,
> 
>   related_concept_id UUID REFERENCES concepts(concept_id),
> 
>   certainty_language TEXT,
>   clinical_weight TEXT,
>   status TEXT DEFAULT 'unreviewed',
> 
>   ai_interpretation TEXT,
>   metadata_json JSONB DEFAULT '{}'::jsonb,
> 
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> ## Claim types
> 
> | Claim Type | Example |
> |---|---|
> | `diagnosis` | “COPD exacerbation” |
> | `exclusion` | “No acute distress” |
> | `instruction` | “Use oxygen as needed” |
> | `medication_decision` | “Continue prednisone” |
> | `risk_assessment` | “Stable for discharge” |
> | `patient_statement` | “I cannot breathe” |
> | `caregiver_statement` | “Symptoms worsen when talking continuously” |
> | `clinical_observation` | “Wheezing noted” |
> | `assumption` | “Patient is noncompliant” |
> | `handoff_summary` | “Patient understands instructions” |
> | `missing_statement` | “No mention of medication interaction review” |
> 
> This is where the system gets sharp.
> 
> ---
> 
> # Add contradiction tracking
> 
> ## `contradictions`
> 
> ```sql
> CREATE TABLE contradictions (
>   contradiction_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   patient_id UUID REFERENCES patients(patient_id),
>   episode_id UUID REFERENCES episodes(episode_id),
>   analysis_run_id UUID REFERENCES analysis_runs(analysis_run_id),
> 
>   contradiction_type TEXT NOT NULL,
>   title TEXT NOT NULL,
>   description TEXT,
> 
>   claim_id UUID REFERENCES claims(claim_id),
>   conflicting_source_type TEXT,
>   conflicting_source_id UUID,
> 
>   severity TEXT,
>   confidence NUMERIC,
>   status TEXT DEFAULT 'open',
> 
>   doctor_question TEXT,
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> ## Contradiction types
> 
> | Type | Example |
> |---|---|
> | `claim_vs_vitals` | “No distress” but HR 164 and EMS called |
> | `claim_vs_behavior` | “Patient understands” but repeatedly misuses/refuses meds |
> | `claim_vs_med_list` | discharge med list conflicts with bottles at home |
> | `claim_vs_timeline` | “Symptoms began today” but ledger shows 5-day trend |
> | `claim_vs_baseline` | “Vitals normal” but abnormal for this patient |
> | `doctor_vs_doctor` | PCP plan conflicts with ER discharge instruction |
> | `instruction_gap` | “Use PRN” but no threshold for when/how much |
> | `unreviewed_interaction` | sedating/stimulant/glucose effects not addressed |
> | `missing_workup` | repeated HR spikes but no documented rhythm review |
> | `language_bias` | “noncompliant” without documenting barrier/refusal reason/context |
> 
> That last one matters. Many medical records smuggle judgment into the chart and then future clinicians inherit it as fact.
> 
> ---
> 
> # Add open questions
> 
> ## `open_questions`
> 
> These are not casual questions. They are unresolved clinical logic gaps.
> 
> ```sql
> CREATE TABLE open_questions (
>   question_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   patient_id UUID REFERENCES patients(patient_id),
>   episode_id UUID REFERENCES episodes(episode_id),
>   analysis_run_id UUID REFERENCES analysis_runs(analysis_run_id),
> 
>   question_type TEXT NOT NULL,
>   question_text TEXT NOT NULL,
> 
>   why_it_matters TEXT,
>   needed_data TEXT,
>   suggested_audience TEXT,
> 
>   priority TEXT,
>   status TEXT DEFAULT 'open',
> 
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> ## Examples
> 
> - “Has anyone reconciled current meds against OTCs and supplements?”
> - “What exact threshold should trigger ER for HR if SpO2 is stable?”
> - “Could albuterol/prednisone be contributing to tachycardia/anxiety/glucose elevation?”
> - “Was cardiac rhythm evaluated during repeated HR >150 episodes?”
> - “Is ‘anxiety’ primary, secondary to air hunger, medication-induced, or a feedback loop?”
> - “Are discharge instructions usable by this patient in the home environment?”
> - “Does the patient understand the medication plan, or is there an execution barrier?”
> - “Was oxygen access/equipment failure considered in the care plan?”
> - “Is the ‘noncompliance’ label hiding discomfort, fear, side effects, confusion, or lack of supplies?”
> 
> This is how you catch what the doctor forgot to say.
> 
> ---
> 
> # The AI’s actual job
> 
> The AI should not just organize.
> 
> It should interrogate the record.
> 
> ## The agent should ask:
> 
> ### 1. What is asserted?
> 
> > Who said what?
> 
> ### 2. What is observed?
> 
> > What did the body, devices, timeline, and behavior show?
> 
> ### 3. What is assumed?
> 
> > What was concluded without enough evidence?
> 
> ### 4. What is missing?
> 
> > What should have been checked but wasn’t documented?
> 
> ### 5. What conflicts?
> 
> > Do notes, vitals, meds, behavior, and outcomes agree?
> 
> ### 6. What changed?
> 
> > Was there a med change, food change, environment change, supply issue, or behavioral change before decline?
> 
> ### 7. What explanation best fits all evidence?
> 
> > Not diagnosis. Pattern logic.
> 
> ### 8. What should a clinician review next?
> 
> > Doctor-facing, not internet-doctor cosplay.
> 
> ---
> 
> # Important distinction: findings vs truth
> 
> The system should not say:
> 
> > “The doctor was wrong.”
> 
> It should say:
> 
> > “The claim ‘stable for discharge’ appears incomplete because the record also shows recurrent tachycardia, medication refusal, unclear home oxygen access, and no documented action threshold for HR spikes. Recommend clinician review.”
> 
> That is much harder to dismiss.
> 
> ---
> 
> # The real output types
> 
> Your AI should generate six classes of output.
> 
> ## 1. Pattern findings
> 
> Example:
> 
> > Recurrent dyspnea episodes occur with stable SpO2 but elevated HR and observed prolonged talking/restlessness.
> 
> ## 2. Interaction findings
> 
> Example:
> 
> > Prednisone and albuterol exposure overlap with anxiety/tachycardia/glucose elevation windows. Review with pharmacist/clinician.
> 
> ## 3. Contradictions
> 
> Example:
> 
> > Discharge note says “patient stable,” but home ledger shows EMS-level distress within X hours and unclear medication adherence plan.
> 
> ## 4. Care gaps
> 
> Example:
> 
> > PRN medication exists, but no clear written threshold explains when to use it, when to repeat it, or when to escalate.
> 
> ## 5. Missing data
> 
> Example:
> 
> > Respiratory rate, oxygen flow rate, exact inhaler timing, and cardiac rhythm evaluation are missing from repeated tachycardia episodes.
> 
> ## 6. Doctor questions
> 
> Example:
> 
> > “When oxygen is 94–96 but HR is 150+ with air hunger, what exact home action plan should we follow?”
> 
> That is gold.
> 
> ---
> 
> # The “doctor forgot” detector
> 
> You need an explicit AI module:
> 
> ## `Clinical Gap Auditor`
> 
> It reviews claims and ledger evidence.
> 
> It flags:
> 
> | Gap | Meaning |
> |---|---|
> | no threshold | instruction lacks action limits |
> | no reconciliation | med list not matched to actual home meds |
> | no interaction review | OTC/food/supplement risks not addressed |
> | no patient-specific baseline | generic “normal” applied |
> | no home feasibility check | plan assumes patient can/will execute it |
> | no behavioral loop accounted | anxiety/refusal/talking/exertion ignored |
> | no equipment/supply check | oxygen/device access ignored |
> | no follow-up owner | nobody assigned responsibility |
> | no escalation rule | unclear when to call doctor/EMS |
> | stale diagnosis inertia | old label reused without current evidence |
> | chart-copy inertia | old note copied forward as current fact |
> 
> That last one is real. Medical records often carry old assumptions forward.
> 
> ---
> 
> # The epistemic model
> 
> Fancy word, useful idea: the system needs “truth status.”
> 
> Every claim/finding should have a status:
> 
> | Status | Meaning |
> |---|---|
> | `observed` | directly seen/measured |
> | `reported` | someone said it |
> | `documented` | appears in record |
> | `inferred` | AI/human inference |
> | `supported` | evidence backs it |
> | `contradicted` | evidence conflicts |
> | `incomplete` | partly true but missing context |
> | `stale` | may have been true before, not verified now |
> | `unverified` | no supporting data |
> | `biased_language` | judgmental framing detected |
> | `needs_clinician_review` | unresolved and clinically relevant |
> 
> This prevents the system from confusing authority with accuracy.
> 
> ---
> 
> # Example
> 
> Doctor note:
> 
> > “Patient anxiety likely contributing to dyspnea. Continue meds. Stable.”
> 
> Patient ledger:
> 
> - HR 150–164
> - SpO2 95
> - talking continuously
> - refused hydroxyzine
> - prednisone taken
> - albuterol used
> - glucose 186
> - oxygen supply issue
> - EMS called
> 
> The AI should output:
> 
> ## Claim review
> 
> **Claim:** “Anxiety likely contributing to dyspnea.”  
> **Status:** supported but incomplete.  
> **Why:** Behavior and stable SpO2 support anxiety/air hunger overlay, but tachycardia, steroid/bronchodilator exposure, glucose elevation, and oxygen supply issue also need review.
> 
> ## Contradiction/gap
> 
> **Claim:** “Stable.”  
> **Status:** incomplete/context-limited.  
> **Why:** Stability may have applied at discharge/visit time, but home ledger shows recurrent escalation. No clear documented home thresholds for HR with stable SpO2.
> 
> ## Doctor question
> 
> > “Can we get a written action plan for episodes where SpO2 stays 94–96 but HR rises above 130/150 with air hunger?”
> 
> Now you’re not arguing. You’re showing structured reality.
> 
> ---
> 
> # Final intelligence workflow
> 
> ## 1. Ingest source
> 
> Sources:
> 
> - caregiver notes
> - patient statements
> - vitals
> - meds
> - foods
> - OTCs
> - environment
> - doctor documents
> - discharge instructions
> - pharmacy lists
> 
> ## 2. Extract into three things
> 
> Every source can produce:
> 
> 1. `patient_ledger` events  
> 2. `claims`  
> 3. `concepts/aliases`
> 
> Example from discharge paper:
> 
> - Ledger: ER visit occurred
> - Claim: “stable for discharge”
> - Claim: “take prednisone daily”
> - Care plan: prednisone order
> - Claim: “follow up with PCP”
> - Open question: no HR threshold documented
> 
> ---
> 
> ## 3. Compare claims to ledger
> 
> For each claim:
> 
> - What supports it?
> - What contradicts it?
> - What is missing?
> - Is it stale?
> - Is it copied language?
> - Does it account for meds, food, behavior, environment?
> - Does it reflect this patient’s baseline?
> 
> ---
> 
> ## 4. Generate contradictions and findings
> 
> Stored in:
> 
> - `findings`
> - `contradictions`
> - `open_questions`
> - `finding_evidence`
> 
> ---
> 
> ## 5. Produce doctor-facing packet
> 
> Not emotional. Not accusatory.
> 
> Format:
> 
> > “Here are the observed patterns and unresolved contradictions we need help reconciling.”
> 
> That wording matters.
> 
> ---
> 
> # Revised final schema list
> 
> ## Spine
> 
> ```text
> patients
> episodes
> concepts
> patient_ledger
> claims
> ```
> 
> ## Supporting
> 
> ```text
> care_plans
> concept_relationships
> documents
> source_records
> ```
> 
> ## Resource
> 
> ```text
> option_sets
> option_values
> concept_aliases
> unit_mappings
> ```
> 
> ## AI/derived
> 
> ```text
> analysis_runs
> findings
> finding_evidence
> derived_relationships
> patient_baselines
> contradictions
> open_questions
> ```
> 
> That’s the clean system.
> 
> ---
> 
> # The key prompt for the agent
> 
> Use this as the heart of the analytical AI:
> 
> ```text
> You are a clinical truth-reconciliation assistant.
> 
> Your job is not to diagnose and not to accept any source as automatically true.
> 
> Treat every doctor note, patient statement, caregiver observation, device reading, discharge instruction, and AI inference as a claim or evidence item with a reliability level.
> 
> Analyze the patient ledger, claims, care plans, concept relationships, baselines, and documents.
> 
> Identify:
> 1. What is directly observed.
> 2. What is reported but unverified.
> 3. What is clinically asserted.
> 4. What is contradicted by other evidence.
> 5. What is incomplete, stale, vague, or based on assumptions.
> 6. What medication, OTC, food, behavior, environment, or equipment factors may have been missed.
> 7. What instructions lack thresholds, ownership, timing, or home feasibility.
> 8. What patterns suggest a clinician should review a specific issue.
> 
> Do not diagnose.
> Do not say a doctor is wrong.
> Instead, produce evidence-linked findings, contradictions, missing data, and precise questions for clinicians.
> 
> Rank by urgency, confidence, and actionability.
> ```
> 
> ---
> 
> # The deeper truth
> 
> The patient is not living inside the doctor’s note.
> 
> The patient is living inside a messy convergence of:
> 
> - physiology
> - medications
> - behavior
> - environment
> - fear
> - equipment
> - access
> - interpretation
> - rushed care
> - incomplete handoffs
> - family execution
> - old assumptions
> 
> Your AI has to model **that convergence**.
> 
> So the true object is not “medical history.”
> 
> The true object is:
> 
> > **Patient reality under competing interpretations.**
> 
> That is what your system should reconstruct.
> 
> And yes — this is where AI actually shines, because humans are terrible at holding 200 small contradictory inputs in working memory.
> 
> The system’s north star:
> 
> > **Find the mismatch between the chart, the body, the home reality, and the care plan.**
> 
> That’s the thing.

### User
> this system is centerd around one individual fyi, so keep it clean we are only analyzing one patient. if two table are simliar merge them, if a need can be met with a couple more columns dont waste a table, the leaner the database the faster and more accurate the outcome, detail matter, unnessary columns create noise, too many table create a mess.

### Assistant
> Yes. That changes the design materially.
> 
> If this is **one patient only**, then I’d remove more structure. We do **not** need patient-centered multi-tenant design. We need a **single-person clinical reality ledger**.
> 
> You’re right: fewer tables, fewer joins, fewer places for truth to hide.
> 
> ## Corrected doctrine
> 
> > One person. One ledger. One concept dictionary. One source/claim layer. One AI findings layer.
> 
> That’s it.
> 
> No `patients` table required unless you want one profile row.  
> No separate `episodes` table required unless episodes become useful later.  
> No separate `open_questions`, `contradictions`, `findings` if one `ai_findings` table can handle all of that.
> 
> Lean wins.
> 
> # Final lean schema
> 
> ## Core tables
> 
> 1. `profile`
> 2. `concepts`
> 3. `ledger`
> 4. `sources`
> 5. `care_plan`
> 6. `relationships`
> 7. `ai_runs`
> 8. `ai_findings`
> 
> That’s the whole system.
> 
> Eight tables.
> 
> If we want to be even more brutal, `profile` can be a config file and `care_plan` can be ledger entries. But I’d keep both because they add real clarity.
> 
> ---
> 
> # 1. `profile`
> 
> One row only.
> 
> Stores the person’s baseline, known context, thresholds, and global notes.
> 
> ```sql
> CREATE TABLE profile (
>   profile_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   display_name TEXT,
>   dob DATE,
>   sex_at_birth TEXT,
> 
>   baseline_json JSONB DEFAULT '{}'::jsonb,
>   risk_json JSONB DEFAULT '{}'::jsonb,
>   preferences_json JSONB DEFAULT '{}'::jsonb,
> 
>   notes TEXT,
>   updated_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> Example `baseline_json`:
> 
> ```json
> {
>   "spo2_usual": "94-96",
>   "hr_usual_resting": "90-110",
>   "bp_notes": "Right arm often lower",
>   "known_conditions": ["COPD", "anxiety overlay suspected", "steroid glucose elevation suspected"],
>   "known_triggers": ["talking continuously", "cold room", "poor sleep", "albuterol", "prednisone"],
>   "clinician_thresholds": {
>     "spo2": "unknown",
>     "heart_rate": "unknown",
>     "glucose": "unknown"
>   }
> }
> ```
> 
> This replaces extra baseline/profile/risk tables.
> 
> ---
> 
> # 2. `concepts`
> 
> Everything meaningful is a concept.
> 
> Meds, OTCs, foods, symptoms, behaviors, environment, devices, vitals, conditions, instructions.
> 
> ```sql
> CREATE TABLE concepts (
>   concept_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
> 
>   name TEXT NOT NULL,
>   type TEXT NOT NULL,
> 
>   aliases TEXT[] DEFAULT '{}',
>   standard_code TEXT,
>   code_system TEXT,
> 
>   properties_json JSONB DEFAULT '{}'::jsonb,
> 
>   active BOOLEAN DEFAULT true,
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> This absorbs:
> 
> - `concept_aliases`
> - `unit_mappings`, mostly
> - dictionaries/glossary
> - concept metadata
> 
> Examples:
> 
> | name | type | aliases |
> |---|---|---|
> | Prednisone | medication | `{pred, steroid}` |
> | Albuterol | medication | `{rescue inhaler, inhaler}` |
> | Hydroxyzine | medication | `{hydrox, anxiety med}` |
> | SpO2 | vital | `{oxygen level, O2}` |
> | Heart rate | vital | `{pulse, HR}` |
> | Talking continuously | behavior | `{talking nonstop}` |
> | Cold room | environment | `{cold house, freezing room}` |
> | Air hunger | symptom | `{can't breathe, dyspnea}` |
> 
> This table is high-value. Keep it.
> 
> ---
> 
> # 3. `ledger`
> 
> The universal event spine.
> 
> This is the source of truth timeline.
> 
> ```sql
> CREATE TABLE ledger (
>   ledger_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
> 
>   event_time TIMESTAMPTZ NOT NULL,
>   event_end_time TIMESTAMPTZ,
> 
>   event_type TEXT NOT NULL,
>   event_subtype TEXT,
> 
>   concept_id UUID REFERENCES concepts(concept_id),
> 
>   value_numeric NUMERIC,
>   value_text TEXT,
>   unit TEXT,
> 
>   status TEXT,
>   severity TEXT,
>   confidence NUMERIC DEFAULT 1.0,
> 
>   source_id UUID,
>   linked_ledger_id UUID REFERENCES ledger(ledger_id),
>   episode_key TEXT,
> 
>   claim_text TEXT,
>   claim_status TEXT,
> 
>   observed_by TEXT,
>   notes TEXT,
>   context_json JSONB DEFAULT '{}'::jsonb,
> 
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> This is where we merge what used to be multiple tables.
> 
> ## Why `claim_text` and `claim_status` are inside `ledger`
> 
> Because for one patient, a separate `claims` table is probably overkill.
> 
> A doctor statement, caregiver statement, patient statement, or discharge instruction can be a ledger row:
> 
> | event_type | concept | claim_text | claim_status |
> |---|---|---|---|
> | claim | Anxiety | “Anxiety likely contributing to dyspnea” | unverified |
> | claim | Discharge | “Stable for discharge” | context_limited |
> | instruction | Oxygen therapy | “Use oxygen as needed” | vague |
> | claim | Noncompliance | “Patient refused medication” | supported/incomplete |
> 
> That keeps the truth-reconciliation logic inside the main timeline.
> 
> Good. Clean. No extra claim table.
> 
> ---
> 
> # 4. `sources`
> 
> Raw material and provenance.
> 
> This merges `documents` and `source_records`.
> 
> ```sql
> CREATE TABLE sources (
>   source_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
> 
>   source_type TEXT NOT NULL,
>   title TEXT,
>   source_time TIMESTAMPTZ,
> 
>   storage_uri TEXT,
>   raw_text TEXT,
>   summary TEXT,
> 
>   reliability TEXT,
>   processed_status TEXT DEFAULT 'new',
> 
>   metadata_json JSONB DEFAULT '{}'::jsonb,
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> Source types:
> 
> - `caregiver_note`
> - `patient_statement`
> - `doctor_note`
> - `discharge_paper`
> - `med_list`
> - `pharmacy_label`
> - `lab_report`
> - `vitals_device`
> - `photo`
> - `screenshot`
> - `voice_transcript`
> - `manual_entry`
> 
> This lets the AI say:
> 
> > “This claim came from discharge paperwork, but the home ledger later contradicts it.”
> 
> ---
> 
> # 5. `care_plan`
> 
> Keep this. It is not just another event.
> 
> This stores what is *supposed* to happen.
> 
> ```sql
> CREATE TABLE care_plan (
>   care_plan_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
> 
>   concept_id UUID REFERENCES concepts(concept_id),
> 
>   plan_type TEXT NOT NULL,
>   status TEXT DEFAULT 'active',
> 
>   instructions TEXT,
> 
>   dose_amount NUMERIC,
>   dose_unit TEXT,
>   route TEXT,
>   frequency TEXT,
>   max_daily_amount NUMERIC,
>   max_daily_unit TEXT,
> 
>   start_date DATE,
>   end_date DATE,
> 
>   source_id UUID REFERENCES sources(source_id),
> 
>   notes TEXT,
>   metadata_json JSONB DEFAULT '{}'::jsonb,
> 
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> Care plan types:
> 
> - `medication_order`
> - `oxygen_order`
> - `monitoring_instruction`
> - `emergency_threshold`
> - `follow_up`
> - `diet_instruction`
> - `device_instruction`
> - `behavior_instruction`
> 
> This table matters because AI needs to compare:
> 
> > planned reality vs lived reality.
> 
> ---
> 
> # 6. `relationships`
> 
> Known and observed relationships.
> 
> This merges `concept_relationships` and `derived_relationships`.
> 
> ```sql
> CREATE TABLE relationships (
>   relationship_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
> 
>   source_concept_id UUID REFERENCES concepts(concept_id),
>   target_concept_id UUID REFERENCES concepts(concept_id),
> 
>   source_ledger_id UUID REFERENCES ledger(ledger_id),
>   target_ledger_id UUID REFERENCES ledger(ledger_id),
> 
>   relationship_type TEXT NOT NULL,
> 
>   relationship_origin TEXT NOT NULL,
>   strength NUMERIC,
>   confidence NUMERIC,
> 
>   severity TEXT,
>   time_delta_minutes INT,
> 
>   evidence_summary TEXT,
>   source_id UUID REFERENCES sources(source_id),
> 
>   metadata_json JSONB DEFAULT '{}'::jsonb,
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> `relationship_origin`:
> 
> - `known_reference`
> - `doctor_statement`
> - `caregiver_observed`
> - `ai_derived`
> - `pharmacist_review`
> - `patient_reported`
> 
> Examples:
> 
> | source | relationship | target | origin |
> |---|---|---|---|
> | Albuterol | may_cause | Tachycardia | known_reference |
> | Prednisone | raises | Glucose | known_reference |
> | Talking continuously | may_worsen | Air hunger | caregiver_observed |
> | Hydroxyzine refusal event | preceded | HR spike event | ai_derived |
> | Cold room | associated_with | Breathing discomfort | ai_derived |
> 
> This table is your graph edge table.
> 
> No Neo4j required for v0. Postgres can do this.
> 
> ---
> 
> # 7. `ai_runs`
> 
> Every AI analysis session.
> 
> ```sql
> CREATE TABLE ai_runs (
>   ai_run_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
> 
>   run_time TIMESTAMPTZ DEFAULT now(),
>   analysis_type TEXT NOT NULL,
> 
>   window_start TIMESTAMPTZ,
>   window_end TIMESTAMPTZ,
> 
>   model_used TEXT,
>   prompt_version TEXT,
> 
>   input_summary TEXT,
>   output_summary TEXT,
> 
>   status TEXT DEFAULT 'completed',
>   metadata_json JSONB DEFAULT '{}'::jsonb
> );
> ```
> 
> Analysis types:
> 
> - `intake_extract`
> - `episode_review`
> - `daily_review`
> - `interaction_scan`
> - `truth_reconciliation`
> - `doctor_packet`
> - `baseline_review`
> 
> ---
> 
> # 8. `ai_findings`
> 
> This merges:
> 
> - findings
> - contradictions
> - open questions
> - missing data
> - care gaps
> - red flags
> 
> One table. Type column.
> 
> ```sql
> CREATE TABLE ai_findings (
>   finding_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
> 
>   ai_run_id UUID REFERENCES ai_runs(ai_run_id),
> 
>   finding_type TEXT NOT NULL,
>   title TEXT NOT NULL,
>   description TEXT,
> 
>   severity TEXT,
>   confidence NUMERIC,
> 
>   status TEXT DEFAULT 'open',
> 
>   related_ledger_ids UUID[] DEFAULT '{}',
>   related_concept_ids UUID[] DEFAULT '{}',
>   related_source_ids UUID[] DEFAULT '{}',
>   related_relationship_ids UUID[] DEFAULT '{}',
> 
>   doctor_question TEXT,
>   suggested_next_step TEXT,
> 
>   evidence_json JSONB DEFAULT '[]'::jsonb,
>   metadata_json JSONB DEFAULT '{}'::jsonb,
> 
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> Finding types:
> 
> - `pattern`
> - `interaction`
> - `contradiction`
> - `missing_data`
> - `care_gap`
> - `red_flag`
> - `baseline_deviation`
> - `med_reconciliation_issue`
> - `instruction_gap`
> - `doctor_question`
> - `equipment_issue`
> - `behavior_loop`
> - `environment_trigger`
> 
> This table is powerful because the evidence can be linked through arrays and JSON without a whole `finding_evidence` table.
> 
> For a one-patient system, that is acceptable and simpler.
> 
> ---
> 
> # Final table list
> 
> ## Keep
> 
> ```text
> profile
> concepts
> ledger
> sources
> care_plan
> relationships
> ai_runs
> ai_findings
> ```
> 
> ## Remove / merge
> 
> | Old table | Merge into |
> |---|---|
> | `patients` | `profile` |
> | `episodes` | `ledger.episode_key` |
> | `claims` | `ledger` |
> | `documents` | `sources` |
> | `source_records` | `sources` |
> | `concept_aliases` | `concepts.aliases` |
> | `unit_mappings` | `concepts.properties_json` or hardcoded parser |
> | `option_sets` | don’t need yet |
> | `option_values` | don’t need yet |
> | `concept_relationships` | `relationships` |
> | `derived_relationships` | `relationships` |
> | `findings` | `ai_findings` |
> | `finding_evidence` | `ai_findings.evidence_json` |
> | `contradictions` | `ai_findings` |
> | `open_questions` | `ai_findings` |
> | `patient_baselines` | `profile.baseline_json`, later maybe table |
> 
> This is much cleaner.
> 
> ---
> 
> # Event model
> 
> The ledger needs disciplined event types.
> 
> Keep the controlled list small:
> 
> ```text
> medication
> intake
> vital
> symptom
> behavior
> environment
> device
> care_action
> clinical_contact
> instruction
> claim
> note
> ```
> 
> That’s enough.
> 
> ## Status values
> 
> ```text
> taken
> refused
> missed
> measured
> reported
> observed
> absent
> normal
> abnormal
> worsened
> improved
> resolved
> ongoing
> unavailable
> unknown
> ```
> 
> ## Claim status values
> 
> ```text
> observed
> reported
> documented
> inferred
> supported
> contradicted
> incomplete
> stale
> unverified
> context_limited
> biased_language
> needs_review
> ```
> 
> ---
> 
> # What this system now does well
> 
> It can handle:
> 
> ## Doctor says:
> 
> > “Stable for discharge.”
> 
> Stored as:
> 
> | field | value |
> |---|---|
> | event_type | claim |
> | claim_text | Stable for discharge |
> | claim_status | documented |
> | source_id | discharge paper |
> 
> AI later evaluates:
> 
> | output | value |
> |---|---|
> | finding_type | contradiction |
> | title | Stability claim may be context-limited |
> | evidence | HR spikes, EMS call, unclear home oxygen plan |
> | doctor_question | What home thresholds should trigger escalation? |
> 
> ---
> 
> ## Patient says:
> 
> > “I can’t breathe.”
> 
> Stored as:
> 
> | field | value |
> |---|---|
> | event_type | symptom |
> | concept | Air hunger |
> | status | reported |
> | claim_text | I can’t breathe |
> 
> Then compared to:
> 
> - SpO2
> - HR
> - respiratory rate if present
> - behavior
> - meds
> - environment
> - anxiety
> - oxygen flow
> 
> So the system doesn’t dismiss it, but it doesn’t blindly accept the interpretation either.
> 
> ---
> 
> ## Caregiver observes:
> 
> > “She talks nonstop and HR rises while oxygen stays okay.”
> 
> Stored as:
> 
> - behavior event: talking continuously
> - vital event: HR high
> - vital event: SpO2 stable
> - claim/note: possible relationship
> 
> AI derives:
> 
> - relationship: talking continuously associated with HR elevation / air hunger
> - finding: behavior-respiratory feedback loop worth clinician review
> 
> ---
> 
> # What we still need to be careful about
> 
> Leaner schema means more discipline.
> 
> The danger is using `context_json` as a trash drawer.
> 
> So the rule is:
> 
> ## Put into columns when it is queried often
> 
> Use real columns for:
> 
> - time
> - type
> - concept
> - value
> - unit
> - status
> - severity
> - source
> - confidence
> - claim status
> - episode key
> 
> Use JSON only for extra details:
> 
> - posture
> - oxygen flow
> - device name
> - location
> - reason refused
> - meal context
> - route
> - body site
> - exact wording
> 
> Do not let JSON become the database. That’s the shadow mess.
> 
> ---
> 
> # The final system sentence
> 
> > This is a single-patient clinical reality ledger that compares lived events, medical claims, care instructions, known relationships, and AI-derived patterns to expose contradictions, risks, missing data, and doctor-facing questions.
> 
> That is exactly what you described.
> 
> And yes — this is lean enough to build fast without making a medical data junk drawer.

### User
> profile = the patient, ok, concepts?, ledger is our event and episodes our real backbone ok, source where it came from ok, care plan the goals and plan that lead to the events, ok, relationships how their connected, ok, ai runs or meta data on the processing of the inforamtion i assume, ai finding is the output from those runs, what about medications, treatments, claims are these in events, but we need a table for meds list to know whats been prescribed and whats active etc, what is actually taken is in events, treatments should be fine in events and can be pivoted in a view if needed by type or something that seems correct, double check this pelase.

### Assistant
> Yes — your understanding is correct, and your instinct about meds is also correct.
> 
> We need to split **medication definition/list** from **medication events**.
> 
> Because:
> 
> > “What is prescribed / active / available / intended” is not the same as “what actually happened.”
> 
> That distinction is non-negotiable.
> 
> # Corrected lean model
> 
> ## Keep the 8-table core, but add one table
> 
> Final lean schema should be:
> 
> 1. `profile`
> 2. `concepts`
> 3. `ledger`
> 4. `sources`
> 5. `care_plan`
> 6. `med_list`
> 7. `relationships`
> 8. `ai_runs`
> 9. `ai_findings`
> 
> So yes: **9 tables**.
> 
> That med table earns its place.
> 
> ---
> 
> # Table roles
> 
> ## 1. `profile`
> 
> The patient.
> 
> One row. Baseline, risks, normal ranges, global patient context.
> 
> Use for:
> 
> - baseline SpO2
> - usual HR range
> - known diagnoses
> - known triggers
> - emergency thresholds
> - general patient-specific context
> 
> ---
> 
> ## 2. `concepts`
> 
> The dictionary of “things.”
> 
> A concept is not an event. It is the reusable meaning.
> 
> Examples:
> 
> - Prednisone
> - Albuterol
> - Hydroxyzine
> - SpO2
> - Heart rate
> - Air hunger
> - Talking continuously
> - Oxygen concentrator
> - COPD
> - Anxiety
> - Cold room
> - Peanut butter
> 
> So yes: concepts are the controlled vocabulary.
> 
> Think:
> 
> > `concepts` = what the thing is  
> > `ledger` = when something happened with that thing
> 
> ---
> 
> ## 3. `ledger`
> 
> The backbone.
> 
> This stores:
> 
> - vitals
> - symptoms
> - meds taken/refused/missed
> - treatments done
> - behaviors
> - food/OTCs consumed
> - environment
> - claims
> - instructions heard
> - care actions
> - clinical contacts
> - episode markers
> 
> So yes, **treatments are events** unless you need an active standing treatment plan, in which case that belongs in `care_plan`.
> 
> Examples in `ledger`:
> 
> | event_type | concept | status |
> |---|---|---|
> | medication | Albuterol | taken |
> | medication | Hydroxyzine | refused |
> | treatment | Nebulizer treatment | completed |
> | vital | Heart rate | measured |
> | symptom | Air hunger | reported |
> | claim | Anxiety | documented |
> | behavior | Talking continuously | observed |
> | care_action | Sat upright | completed |
> 
> ---
> 
> ## 4. `sources`
> 
> Where the information came from.
> 
> Examples:
> 
> - caregiver note
> - discharge paper
> - med bottle photo
> - doctor portal note
> - pharmacy printout
> - text message
> - voice transcript
> - manual entry
> - vitals device
> 
> This preserves provenance.
> 
> ---
> 
> ## 5. `care_plan`
> 
> The intended plan or goal.
> 
> This is broader than medication.
> 
> Use for:
> 
> - oxygen instructions
> - monitoring instructions
> - emergency thresholds
> - diet goals
> - appointment follow-ups
> - behavior instructions
> - device instructions
> - home care plan
> - “when to call doctor”
> - “when to use rescue inhaler”
> - “when to go to ER”
> 
> Care plan answers:
> 
> > “What are we supposed to do?”
> 
> ---
> 
> # 6. `med_list`
> 
> Yes. Add this.
> 
> This is the current/historical medication registry.
> 
> It answers:
> 
> > “What meds are prescribed, active, stopped, PRN, available, duplicated, or unclear?”
> 
> Do **not** rely on `care_plan` alone for meds. Meds have too many special attributes: dose, route, schedule, PRN, active status, prescriber, pharmacy, fills, max dose, start/end, reason, etc.
> 
> ## `med_list`
> 
> ```sql
> CREATE TABLE med_list (
>   med_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
> 
>   concept_id UUID REFERENCES concepts(concept_id),
> 
>   med_name TEXT NOT NULL,
>   generic_name TEXT,
>   brand_name TEXT,
> 
>   status TEXT DEFAULT 'active',
>   med_type TEXT,
> 
>   dose_amount NUMERIC,
>   dose_unit TEXT,
>   route TEXT,
>   frequency TEXT,
> 
>   prn BOOLEAN DEFAULT false,
>   prn_reason TEXT,
>   max_daily_amount NUMERIC,
>   max_daily_unit TEXT,
> 
>   indication TEXT,
>   prescriber TEXT,
>   pharmacy TEXT,
> 
>   start_date DATE,
>   end_date DATE,
>   stopped_reason TEXT,
> 
>   source_id UUID REFERENCES sources(source_id),
> 
>   available_at_home BOOLEAN,
>   needs_reconciliation BOOLEAN DEFAULT false,
> 
>   notes TEXT,
>   metadata_json JSONB DEFAULT '{}'::jsonb,
> 
>   created_at TIMESTAMPTZ DEFAULT now(),
>   updated_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> ## Useful `status` values
> 
> ```text
> active
> inactive
> stopped
> paused
> expired
> unknown
> duplicate_possible
> needs_reconciliation
> not_available
> ```
> 
> ## Useful `med_type` values
> 
> ```text
> prescription
> otc
> supplement
> oxygen
> device_related
> unknown
> ```
> 
> Yes, I would include oxygen here **if it functions like a prescribed therapy**.
> 
> But oxygen use events still go in `ledger`.
> 
> ---
> 
> # Medication logic
> 
> ## `med_list` = intended / active / prescribed
> 
> Example:
> 
> | Field | Value |
> |---|---|
> | med_name | Prednisone |
> | status | active |
> | dose | 20 mg |
> | frequency | daily |
> | route | oral |
> | indication | COPD flare |
> | source | discharge paper |
> 
> ## `ledger` = what happened
> 
> Example:
> 
> | Field | Value |
> |---|---|
> | event_type | medication |
> | concept | Prednisone |
> | status | taken |
> | value_numeric | 20 |
> | unit | mg |
> | event_time | 8:00 AM |
> 
> Another:
> 
> | Field | Value |
> |---|---|
> | event_type | medication |
> | concept | Hydroxyzine |
> | status | refused |
> | notes | patient refused despite anxiety |
> 
> This gives the AI the critical comparison:
> 
> > prescribed vs available vs actually taken vs refused vs effect afterward
> 
> That is where the insight lives.
> 
> ---
> 
> # What about claims?
> 
> For this one-patient design, keep claims in `ledger`.
> 
> A separate `claims` table is too much unless this becomes legal/medical-record heavy later.
> 
> ## Claim in `ledger`
> 
> ```text
> event_type = claim
> event_subtype = diagnosis_statement / discharge_status / patient_statement / caregiver_statement / clinical_assumption
> concept_id = related concept if applicable
> claim_text = exact claim
> claim_status = documented / supported / contradicted / incomplete / stale / needs_review
> source_id = where it came from
> ```
> 
> Examples:
> 
> | event_type | event_subtype | claim_text | claim_status |
> |---|---|---|---|
> | claim | diagnosis_statement | “Anxiety likely contributing to dyspnea” | supported_incomplete |
> | claim | discharge_status | “Stable for discharge” | context_limited |
> | claim | assumption | “Patient noncompliant” | needs_review |
> | claim | patient_statement | “I can’t breathe” | reported |
> | claim | caregiver_statement | “Talking worsens symptoms” | observed_pattern |
> 
> Claims are events because they happened in time and came from a source.
> 
> Perfect.
> 
> ---
> 
> # What about treatments?
> 
> You were right.
> 
> Treatments mostly belong in `ledger`.
> 
> Examples:
> 
> | Treatment | Table |
> |---|---|
> | nebulizer treatment completed | `ledger` |
> | oxygen applied | `ledger` |
> | oxygen flow changed | `ledger` |
> | sat upright | `ledger` |
> | gave fluids | `ledger` |
> | wound/rash cleaned | `ledger` |
> | breathing exercise attempted | `ledger` |
> | EMS intervention | `ledger` |
> | long-term oxygen order | `care_plan` and/or `med_list` |
> | prescribed nebulizer schedule | `care_plan` |
> | actual nebulizer use | `ledger` |
> 
> So the split is:
> 
> > Treatment plan = `care_plan`  
> > Treatment execution = `ledger`
> 
> ---
> 
> # What about OTCs, foods, supplements?
> 
> ## OTCs
> 
> If regularly used or medically relevant: put in `med_list`.
> 
> Examples:
> 
> - Benadryl
> - ibuprofen
> - acetaminophen
> - Mucinex/guaifenesin
> - cold medicine
> - magnesium
> - vitamin D
> - melatonin
> 
> Actual use goes in `ledger`.
> 
> ## Foods
> 
> Foods do **not** need their own table.
> 
> Use:
> 
> - `concepts` for common relevant foods
> - `ledger` for actual intake
> 
> Examples:
> 
> - peanut butter
> - grapefruit
> - high-carb meal
> - caffeine
> - milk
> - salty food
> 
> ## Supplements
> 
> Supplements should be in `med_list` if recurring. They behave more like meds than food.
> 
> ---
> 
> # Correct final model
> 
> ```text
> profile
> concepts
> sources
> med_list
> care_plan
> ledger
> relationships
> ai_runs
> ai_findings
> ```
> 
> That’s the final lean schema.
> 
> # Mental model
> 
> ## The patient
> 
> `profile`
> 
> ## The vocabulary
> 
> `concepts`
> 
> ## The source material
> 
> `sources`
> 
> ## What meds/therapies are supposed to exist
> 
> `med_list`
> 
> ## What the care plan says to do
> 
> `care_plan`
> 
> ## What actually happened
> 
> `ledger`
> 
> ## How things connect
> 
> `relationships`
> 
> ## What the AI processed
> 
> `ai_runs`
> 
> ## What the AI found
> 
> `ai_findings`
> 
> Clean.
> 
> ---
> 
> # The most important distinction
> 
> ## `med_list`
> 
> Stable-ish truth:
> 
> - prescribed
> - active
> - stopped
> - dose
> - frequency
> - PRN
> - prescriber
> - available at home
> - source of truth
> - reconciliation status
> 
> ## `ledger`
> 
> Time-based reality:
> 
> - taken
> - refused
> - missed
> - delayed
> - side effect observed
> - symptom after dose
> - vitals after dose
> 
> ## `relationships`
> 
> Known or observed connection:
> 
> - prednisone raises glucose
> - albuterol may raise HR
> - hydroxyzine may sedate
> - Benadryl duplicates sedation with hydroxyzine
> - talking continuously worsens air hunger
> - cold room may worsen respiratory discomfort
> 
> ## `ai_findings`
> 
> Interpretation:
> 
> - “Prednisone + high-carb intake may be contributing to glucose elevation.”
> - “Albuterol use may be temporally associated with HR spikes.”
> - “Hydroxyzine is prescribed PRN but repeatedly refused during anxiety episodes.”
> - “Stable oxygen with high HR suggests dyspnea episodes may not be oxygen-desaturation-only.”
> 
> ---
> 
> # One thing I would add to `ledger`
> 
> Since episodes are not a table now, keep this:
> 
> ```sql
> episode_key TEXT
> ```
> 
> Examples:
> 
> ```text
> 2026-05-20_resp_distress_pm
> 2026-05-21_er_visit
> 2026-05-22_rash_flare
> ```
> 
> This lets you group events without creating an episode table.
> 
> If later episodes become complex, then we can promote them to a real table. Not now.
> 
> ---
> 
> # One thing I would add to `med_list`
> 
> Add:
> 
> ```sql
> reconciliation_status TEXT
> ```
> 
> Values:
> 
> ```text
> verified
> patient_reported
> doctor_list_only
> pharmacy_verified
> bottle_seen
> conflicting
> unknown
> needs_review
> ```
> 
> This is big.
> 
> Because with meds, the core question is often:
> 
> > “Do we actually know this list is real?”
> 
> So `med_list` should include both:
> 
> ```sql
> status TEXT
> reconciliation_status TEXT
> ```
> 
> Example:
> 
> | med | status | reconciliation_status |
> |---|---|---|
> | Prednisone | active | discharge_paper_only |
> | Hydroxyzine | active | bottle_seen |
> | Albuterol | active | patient_reported |
> | Old antibiotic | unknown | found_at_home_needs_review |
> 
> That will catch chaos.
> 
> ---
> 
> # One thing I would add to `care_plan`
> 
> Add:
> 
> ```sql
> threshold_json JSONB
> ```
> 
> Because care plans often need decision rules.
> 
> Example:
> 
> ```json
> {
>   "call_doctor_if": ["HR over 130 sustained", "glucose over clinician threshold"],
>   "go_to_er_if": ["SpO2 below prescribed threshold", "confusion", "chest pain"],
>   "unknown_thresholds": ["heart rate", "rescue inhaler max use"]
> }
> ```
> 
> This helps AI flag vague instructions.
> 
> ---
> 
> # Final answer
> 
> You had it almost exactly right:
> 
> - **Meds prescribed/active/available** need `med_list`.
> - **Meds actually taken/refused/missed** go in `ledger`.
> - **Treatments planned** go in `care_plan`.
> - **Treatments performed** go in `ledger`.
> - **Claims** go in `ledger` as claim events.
> - **Relationships** connect meds, foods, symptoms, vitals, behaviors, environment, and claims.
> - **AI runs** are processing metadata.
> - **AI findings** are output: contradictions, patterns, missing data, risks, doctor questions.
> 
> So the corrected schema is:
> 
> ```text
> profile
> concepts
> sources
> med_list
> care_plan
> ledger
> relationships
> ai_runs
> ai_findings
> ```
> 
> That is lean, but not stupidly lean. It preserves the distinctions that actually matter.

### User
> in profile how do we handle the environment is it there or sepearte how do we handle changing environment or ongoing events like moving to new home this data to this date which can explain flair ups becaue moves mean stress, dust, changed routine ect.

### Assistant
> Yes — this is exactly where **profile alone is not enough**.
> 
> The clean split:
> 
> > **Profile stores stable patient context. Ledger stores changing environment and life-context events. Concepts define reusable environment types.**
> 
> Do **not** create a separate environment table yet. That’s bloat. Use `ledger`.
> 
> # The rule
> 
> ## Stable environment context → `profile`
> 
> Use this for mostly stable background:
> 
> - current living situation summary
> - usual bedroom setup
> - known home triggers
> - pets/smoke/dust/mold exposure history
> - typical climate/temperature sensitivity
> - mobility setup
> - baseline routine
> - caregiver/home support context
> 
> Example in `profile.context_json` or `baseline_json`:
> 
> ```json
> {
>   "home_context": {
>     "usual_sleep_location": "bedroom",
>     "known_environment_triggers": ["dust", "cold room", "routine disruption", "moving stress"],
>     "oxygen_equipment_location": "home",
>     "mobility_context": "uses scooter/wheelchair at times",
>     "routine_sensitivity": "changes in routine may worsen anxiety, sleep, medication adherence, and symptom perception"
>   }
> }
> ```
> 
> That is the “background map.”
> 
> ---
> 
> # Changing environment → `ledger`
> 
> Anything that changes over time goes into `ledger`.
> 
> Moving homes, cleaning, dust exposure, oxygen setup changes, sleeping in a different room, disrupted routine — all of that is event/timeline data.
> 
> Use:
> 
> ```text
> event_type = environment
> event_subtype = move / dust_exposure / cold_room / routine_disruption / equipment_location_change
> ```
> 
> Examples:
> 
> ## Moving event starts
> 
> | Field | Value |
> |---|---|
> | `event_type` | environment |
> | `event_subtype` | move_started |
> | `concept_id` | Moving / relocation |
> | `event_time` | 2026-05-01 |
> | `event_end_time` | 2026-05-15 |
> | `severity` | high |
> | `status` | ongoing |
> | `notes` | Moving homes; dust, stress, disrupted sleep/routine likely increased. |
> 
> ## New home period
> 
> | Field | Value |
> |---|---|
> | `event_type` | environment |
> | `event_subtype` | new_home_transition |
> | `concept_id` | New home environment |
> | `event_time` | 2026-05-15 |
> | `event_end_time` | null |
> | `status` | ongoing |
> | `context_json` | `{ "routine_changed": true, "dust_possible": true, "sleep_disrupted": true }` |
> 
> ## Dust exposure during move
> 
> | Field | Value |
> |---|---|
> | `event_type` | environment |
> | `event_subtype` | dust_exposure |
> | `concept_id` | Dust |
> | `event_time` | 2026-05-12T14:00 |
> | `severity` | medium |
> | `status` | observed |
> | `notes` | Packing/unpacking dusty items. |
> 
> ## Routine disruption
> 
> | Field | Value |
> |---|---|
> | `event_type` | behavior |
> | `event_subtype` | routine_disruption |
> | `concept_id` | Routine disruption |
> | `event_time` | 2026-05-01 |
> | `event_end_time` | 2026-05-20 |
> | `severity` | high |
> | `status` | ongoing |
> | `notes` | Sleep, meals, medication timing, and rest schedule disrupted during move. |
> 
> That gives the AI time windows.
> 
> ---
> 
> # Important: use `event_end_time`
> 
> This is why `ledger` needs both:
> 
> ```sql
> event_time TIMESTAMPTZ NOT NULL,
> event_end_time TIMESTAMPTZ
> ```
> 
> Because some events are instant:
> 
> - HR measured
> - med taken
> - symptom reported
> 
> But others are periods:
> 
> - moving
> - high dust exposure week
> - no oxygen tanks available
> - poor sleep stretch
> - caregiver unavailable
> - new home adjustment
> - heat wave
> - illness recovery
> - medication course
> 
> So the AI can ask:
> 
> > “Did flare-ups increase during the move window?”
> 
> That is the whole point.
> 
> ---
> 
> # Add `location_label`
> 
> This one earns its place.
> 
> I’d add this column to `ledger`:
> 
> ```sql
> location_label TEXT
> ```
> 
> Because environment analysis needs place context.
> 
> Examples:
> 
> - `old_home`
> - `new_home`
> - `bedroom`
> - `living_room`
> - `hospital`
> - `car`
> - `doctor_office`
> - `pharmacy`
> - `outside`
> - `unknown`
> 
> This is better as a column than buried in JSON because you’ll query it often.
> 
> So updated `ledger` key fields:
> 
> ```sql
> event_time
> event_end_time
> event_type
> event_subtype
> concept_id
> value_numeric
> value_text
> unit
> status
> severity
> location_label
> confidence
> source_id
> linked_ledger_id
> episode_key
> claim_text
> claim_status
> observed_by
> notes
> context_json
> ```
> 
> ---
> 
> # Add environmental concepts
> 
> In `concepts`, create these:
> 
> | Concept | Type |
> |---|---|
> | Current home environment | environment |
> | Old home environment | environment |
> | New home environment | environment |
> | Moving / relocation | environment |
> | Dust | environment |
> | Mold | environment |
> | Smoke | environment |
> | Cold room | environment |
> | Hot room | environment |
> | Humidity | environment |
> | Routine disruption | behavior/environment |
> | Sleep disruption | behavior |
> | Caregiver disruption | care_context |
> | Oxygen access issue | device/environment |
> | Medication storage change | care_context |
> | High-stress household period | psychosocial_context |
> 
> I would allow `concept.type = context` or `environment` for broader things.
> 
> Actually, cleanest controlled types:
> 
> ```text
> medication
> otc
> supplement
> food
> vital
> symptom
> condition
> behavior
> environment
> device
> treatment
> claim_topic
> care_context
> ```
> 
> `care_context` is useful. It catches things like moving, caregiver disruption, access barriers, transportation, pharmacy pickup issues, supply issues.
> 
> ---
> 
> # Moving is not just environment
> 
> This is the key nuance.
> 
> A move affects multiple systems:
> 
> | Area | Why it matters |
> |---|---|
> | Environment | dust, allergens, temperature, layout |
> | Behavior | sleep disruption, more exertion, talking/stress |
> | Medication | missed doses, bottles misplaced, timing disrupted |
> | Equipment | oxygen moved, tanks unavailable, concentrator setup |
> | Food | irregular meals, glucose changes |
> | Stress | anxiety, heart rate, symptom focus |
> | Routine | less rest, less predictability |
> | Safety | fall risk, clutter, unfamiliar layout |
> 
> So don’t log “move” only once and call it done.
> 
> Log the move as an ongoing umbrella event, then log sub-events as they happen.
> 
> Use `linked_ledger_id`.
> 
> Example:
> 
> ## Main event
> 
> ```text
> ledger_id = MOVE001
> event_type = care_context
> event_subtype = relocation_period
> concept = Moving / relocation
> event_time = 2026-05-01
> event_end_time = 2026-05-20
> severity = high
> status = ongoing
> ```
> 
> ## Linked events
> 
> | Event | linked_ledger_id |
> |---|---|
> | dust exposure | MOVE001 |
> | missed medication | MOVE001 |
> | poor sleep | MOVE001 |
> | oxygen tanks unavailable | MOVE001 |
> | high exertion day | MOVE001 |
> | flare-up | MOVE001 |
> 
> That is elegant and powerful.
> 
> ---
> 
> # How AI should analyze it
> 
> The AI should not just say:
> 
> > “Patient moved.”
> 
> It should say:
> 
> > “During the relocation window, there were increased respiratory symptoms, high HR episodes, disrupted medication timing, dust exposure, sleep disruption, and oxygen access issues. The move may be a multi-factor trigger rather than a single environmental exposure.”
> 
> That’s the kind of insight you want.
> 
> ---
> 
> # Best schema answer
> 
> ## Environment does not get its own table yet.
> 
> Use:
> 
> - `profile` for stable home/environment baseline
> - `concepts` for environment/context types
> - `ledger` for actual changing events
> - `relationships` for known/observed effects
> - `ai_findings` for conclusions
> 
> # Example relationship entries
> 
> | Source concept | Relationship | Target concept |
> |---|---|---|
> | Dust | may_worsen | Dyspnea |
> | Cold room | may_trigger | Air hunger |
> | Moving / relocation | may_worsen | Anxiety |
> | Moving / relocation | may_disrupt | Medication adherence |
> | Sleep disruption | may_worsen | Anxiety |
> | Routine disruption | may_worsen | Medication adherence |
> | Oxygen access issue | may_worsen | Respiratory distress |
> 
> This lets the AI reason across body + life context.
> 
> ---
> 
> # Final answer
> 
> Handle environment like this:
> 
> ## `profile`
> 
> Stable background:
> 
> ```text
> Where she usually lives, known triggers, baseline home setup, known sensitivities.
> ```
> 
> ## `ledger`
> 
> Changing reality:
> 
> ```text
> Move started, move ended, dust exposure, new home transition, cold room, oxygen setup changed, routine disrupted, sleep disrupted, meds misplaced, flare happened.
> ```
> 
> ## `concepts`
> 
> Reusable meanings:
> 
> ```text
> Dust, cold room, moving, routine disruption, oxygen access issue, new home environment.
> ```
> 
> ## `relationships`
> 
> Known or observed effects:
> 
> ```text
> Dust may worsen breathing.
> Moving may disrupt meds/sleep.
> Cold may trigger air hunger.
> Routine disruption may worsen anxiety.
> ```
> 
> ## `ai_findings`
> 
> Actual insight:
> 
> ```text
> Flare-ups increased during move window; likely multi-factor contributor: dust + stress + disrupted routine + medication timing + equipment access.
> ```
> 
> So no, don’t make a separate environment table right now.  
> Add `event_end_time` and `location_label` to `ledger`, use `care_context/environment/behavior` event types, and let AI analyze overlapping windows.
> 
> That keeps it clean and still captures the truth.

### User
> while those can be entered into the timeline the ai shouls be smart enough to estrapulate that from the event moved into new home or started packing for move ect., i think after that we ahve something, give me the lean dev blueprint and manual for review

### Assistant
> Exactly — don’t force humans to log every downstream implication. The ledger should capture the anchor event, and the AI should infer likely consequence domains, then verify them against later data instead of pretending inference is fact.

### Assistant
> # Lean Dev Blueprint  
> ## Single-Patient Clinical Reality + AI Analysis System
> 
> ## 0. Purpose
> 
> Build a private, single-patient clinical intelligence system that turns messy health reality into:
> 
> - structured timeline
> - medication reconciliation
> - care-plan comparison
> - contradiction detection
> - environmental/context inference
> - interaction analysis
> - doctor-facing questions
> - evidence-linked AI findings
> 
> This is **not** a diagnosis engine.
> 
> It is a **truth-reconciliation and pattern-detection engine**.
> 
> The north star:
> 
> > Find the mismatch between the chart, the body, the home reality, the medication list, the care plan, and what actually happened.
> 
> ---
> 
> # 1. Core Doctrine
> 
> ## The system must not treat any source as absolute truth.
> 
> Doctor notes, discharge papers, patient statements, caregiver observations, device readings, and AI conclusions are all **evidence**.
> 
> The system should classify information as:
> 
> - observed
> - measured
> - reported
> - documented
> - inferred
> - contradicted
> - incomplete
> - stale
> - context-limited
> - needs review
> 
> The AI should never say:
> 
> > “The doctor was wrong.”
> 
> It should say:
> 
> > “This claim appears incomplete or context-limited based on later events, vitals, medication behavior, and home conditions.”
> 
> That wording matters.
> 
> ---
> 
> # 2. Final Lean Table Set
> 
> Use **9 tables**.
> 
> ```text
> profile
> concepts
> sources
> med_list
> care_plan
> ledger
> relationships
> ai_runs
> ai_findings
> ```
> 
> That’s the clean spine.
> 
> No separate episodes table.  
> No separate claims table.  
> No separate environment table.  
> No separate finding evidence table.  
> No unnecessary patient table because this is one person.
> 
> ---
> 
> # 3. Table Roles
> 
> ## 1. `profile`
> 
> The patient and stable context.
> 
> Stores:
> 
> - basic patient info
> - baseline ranges
> - known diagnoses/context
> - known triggers
> - home/environment baseline
> - clinician thresholds if known
> - risk notes
> - global summary
> 
> Use for stable or slow-changing truth.
> 
> Examples:
> 
> - usual SpO2 range
> - usual resting HR
> - oxygen baseline
> - known COPD/anxiety overlay
> - known sensitivity to dust/cold/routine disruption
> - known right-arm BP difference
> - known care limitations
> 
> ---
> 
> ## 2. `concepts`
> 
> The dictionary of meaningful things.
> 
> A concept can be:
> 
> - medication
> - OTC
> - supplement
> - food
> - vital
> - symptom
> - condition
> - behavior
> - environment
> - treatment
> - device
> - care context
> - claim topic
> 
> Examples:
> 
> - Prednisone
> - Albuterol
> - Hydroxyzine
> - SpO2
> - Heart rate
> - Air hunger
> - Talking continuously
> - Moving / relocation
> - Dust
> - Cold room
> - Oxygen concentrator
> - Medication refusal
> - COPD
> - Anxiety
> - Glucose elevation
> 
> This table prevents messy duplicate naming.
> 
> ---
> 
> ## 3. `sources`
> 
> Where information came from.
> 
> Stores:
> 
> - voice transcripts
> - caregiver notes
> - manual entries
> - discharge papers
> - doctor notes
> - medication bottle photos
> - pharmacy labels
> - screenshots
> - lab reports
> - device exports
> - portal messages
> 
> Raw source material stays here. Structured facts go into `ledger`.
> 
> ---
> 
> ## 4. `med_list`
> 
> The current and historical medication/therapy list.
> 
> This is required.
> 
> It answers:
> 
> > What is prescribed, active, stopped, available, PRN, uncertain, or needs reconciliation?
> 
> This includes:
> 
> - prescriptions
> - OTCs
> - supplements
> - oxygen therapy if prescribed
> - recurring treatments with medication-like behavior
> 
> Actual doses taken/refused/missed go in `ledger`.
> 
> ---
> 
> ## 5. `care_plan`
> 
> What is supposed to happen.
> 
> Stores:
> 
> - medication-related instructions if broader than the med itself
> - oxygen instructions
> - monitoring rules
> - ER/call-doctor thresholds
> - follow-up instructions
> - diet instructions
> - treatment plans
> - device-use instructions
> - home-care goals
> 
> This answers:
> 
> > What is the plan, and is reality following it?
> 
> ---
> 
> ## 6. `ledger`
> 
> The backbone.
> 
> The universal timeline of what happened, what was measured, what was said, what was refused, what changed, and what was observed.
> 
> Everything time-based goes here:
> 
> - vitals
> - symptoms
> - meds taken/refused/missed
> - food/OTC intake
> - treatment performed
> - environment changes
> - behavior observations
> - doctor claims
> - patient claims
> - caregiver claims
> - clinical visits
> - equipment issues
> - move/new-home context
> - care actions
> - episode markers
> 
> This is the most important table.
> 
> ---
> 
> ## 7. `relationships`
> 
> How things connect.
> 
> Stores both known and observed relationships.
> 
> Examples:
> 
> - Albuterol may cause tachycardia.
> - Prednisone may raise glucose.
> - Prednisone may worsen anxiety.
> - Dust may worsen dyspnea.
> - Moving may disrupt routine.
> - Routine disruption may increase missed medication.
> - Talking continuously may worsen air hunger.
> - Hydroxyzine may cause sedation.
> - Benadryl may duplicate sedation with hydroxyzine.
> - Oxygen access issue may worsen respiratory distress.
> 
> Relationships can be:
> 
> - known reference
> - doctor-stated
> - caregiver-observed
> - AI-derived
> - patient-reported
> - pharmacist-reviewed
> 
> This is the graph edge table.
> 
> ---
> 
> ## 8. `ai_runs`
> 
> Metadata for each AI process.
> 
> Stores:
> 
> - run type
> - time window
> - model used
> - prompt version
> - input summary
> - output summary
> - status
> 
> Examples:
> 
> - intake extraction
> - episode review
> - daily review
> - interaction scan
> - truth reconciliation
> - med reconciliation
> - doctor packet
> - baseline review
> 
> ---
> 
> ## 9. `ai_findings`
> 
> The output.
> 
> Stores:
> 
> - patterns
> - contradictions
> - missing data
> - medication concerns
> - interaction warnings
> - care gaps
> - red flags
> - doctor questions
> - environmental/context insights
> - baseline deviations
> 
> This table should contain evidence references through arrays/JSON, not a separate evidence table for v0.
> 
> ---
> 
> # 4. Recommended SQL Skeleton
> 
> ## `profile`
> 
> ```sql
> CREATE TABLE profile (
>   profile_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   display_name TEXT,
>   dob DATE,
>   sex_at_birth TEXT,
> 
>   baseline_json JSONB DEFAULT '{}'::jsonb,
>   risk_json JSONB DEFAULT '{}'::jsonb,
>   context_json JSONB DEFAULT '{}'::jsonb,
> 
>   notes TEXT,
>   updated_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> ---
> 
> ## `concepts`
> 
> ```sql
> CREATE TABLE concepts (
>   concept_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
> 
>   name TEXT NOT NULL,
>   type TEXT NOT NULL,
> 
>   aliases TEXT[] DEFAULT '{}',
>   standard_code TEXT,
>   code_system TEXT,
> 
>   properties_json JSONB DEFAULT '{}'::jsonb,
> 
>   active BOOLEAN DEFAULT true,
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> Recommended `type` values:
> 
> ```text
> medication
> otc
> supplement
> food
> beverage
> vital
> symptom
> condition
> behavior
> environment
> device
> treatment
> care_context
> claim_topic
> lab
> instruction
> ```
> 
> ---
> 
> ## `sources`
> 
> ```sql
> CREATE TABLE sources (
>   source_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
> 
>   source_type TEXT NOT NULL,
>   title TEXT,
>   source_time TIMESTAMPTZ,
> 
>   storage_uri TEXT,
>   raw_text TEXT,
>   summary TEXT,
> 
>   reliability TEXT,
>   processed_status TEXT DEFAULT 'new',
> 
>   metadata_json JSONB DEFAULT '{}'::jsonb,
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> Recommended `source_type` values:
> 
> ```text
> manual_entry
> voice_transcript
> caregiver_note
> patient_statement
> doctor_note
> discharge_paper
> med_list
> pharmacy_label
> lab_report
> photo
> screenshot
> vitals_device
> portal_message
> ai_extraction
> ```
> 
> ---
> 
> ## `med_list`
> 
> ```sql
> CREATE TABLE med_list (
>   med_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
> 
>   concept_id UUID REFERENCES concepts(concept_id),
> 
>   med_name TEXT NOT NULL,
>   generic_name TEXT,
>   brand_name TEXT,
> 
>   status TEXT DEFAULT 'active',
>   reconciliation_status TEXT DEFAULT 'unknown',
>   med_type TEXT,
> 
>   dose_amount NUMERIC,
>   dose_unit TEXT,
>   route TEXT,
>   frequency TEXT,
> 
>   prn BOOLEAN DEFAULT false,
>   prn_reason TEXT,
>   max_daily_amount NUMERIC,
>   max_daily_unit TEXT,
> 
>   indication TEXT,
>   prescriber TEXT,
>   pharmacy TEXT,
> 
>   start_date DATE,
>   end_date DATE,
>   stopped_reason TEXT,
> 
>   source_id UUID REFERENCES sources(source_id),
> 
>   available_at_home BOOLEAN,
>   needs_reconciliation BOOLEAN DEFAULT false,
> 
>   notes TEXT,
>   metadata_json JSONB DEFAULT '{}'::jsonb,
> 
>   created_at TIMESTAMPTZ DEFAULT now(),
>   updated_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> Recommended `status` values:
> 
> ```text
> active
> inactive
> stopped
> paused
> expired
> unknown
> duplicate_possible
> needs_reconciliation
> not_available
> ```
> 
> Recommended `reconciliation_status` values:
> 
> ```text
> verified
> bottle_seen
> pharmacy_verified
> doctor_list_only
> discharge_paper_only
> patient_reported
> caregiver_reported
> conflicting
> unknown
> needs_review
> ```
> 
> Recommended `med_type` values:
> 
> ```text
> prescription
> otc
> supplement
> oxygen
> inhaler
> nebulizer_solution
> unknown
> ```
> 
> ---
> 
> ## `care_plan`
> 
> ```sql
> CREATE TABLE care_plan (
>   care_plan_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
> 
>   concept_id UUID REFERENCES concepts(concept_id),
> 
>   plan_type TEXT NOT NULL,
>   status TEXT DEFAULT 'active',
> 
>   instructions TEXT,
> 
>   dose_amount NUMERIC,
>   dose_unit TEXT,
>   route TEXT,
>   frequency TEXT,
>   max_daily_amount NUMERIC,
>   max_daily_unit TEXT,
> 
>   threshold_json JSONB DEFAULT '{}'::jsonb,
> 
>   start_date DATE,
>   end_date DATE,
> 
>   source_id UUID REFERENCES sources(source_id),
> 
>   notes TEXT,
>   metadata_json JSONB DEFAULT '{}'::jsonb,
> 
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> Recommended `plan_type` values:
> 
> ```text
> medication_order
> oxygen_order
> monitoring_instruction
> emergency_threshold
> follow_up
> diet_instruction
> device_instruction
> treatment_plan
> behavior_instruction
> home_care_goal
> ```
> 
> ---
> 
> ## `ledger`
> 
> ```sql
> CREATE TABLE ledger (
>   ledger_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
> 
>   event_time TIMESTAMPTZ NOT NULL,
>   event_end_time TIMESTAMPTZ,
> 
>   event_type TEXT NOT NULL,
>   event_subtype TEXT,
> 
>   concept_id UUID REFERENCES concepts(concept_id),
> 
>   value_numeric NUMERIC,
>   value_text TEXT,
>   unit TEXT,
> 
>   status TEXT,
>   severity TEXT,
>   confidence NUMERIC DEFAULT 1.0,
> 
>   location_label TEXT,
> 
>   source_id UUID REFERENCES sources(source_id),
>   linked_ledger_id UUID REFERENCES ledger(ledger_id),
>   episode_key TEXT,
> 
>   claim_text TEXT,
>   claim_status TEXT,
> 
>   observed_by TEXT,
>   notes TEXT,
>   context_json JSONB DEFAULT '{}'::jsonb,
> 
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> Recommended `event_type` values:
> 
> ```text
> medication
> intake
> vital
> symptom
> behavior
> environment
> device
> treatment
> care_action
> clinical_contact
> instruction
> claim
> note
> ```
> 
> Recommended `status` values:
> 
> ```text
> taken
> refused
> missed
> measured
> reported
> observed
> absent
> normal
> abnormal
> worsened
> improved
> resolved
> ongoing
> unavailable
> unknown
> completed
> started
> ended
> ```
> 
> Recommended `claim_status` values:
> 
> ```text
> observed
> reported
> documented
> inferred
> supported
> contradicted
> incomplete
> stale
> unverified
> context_limited
> biased_language
> needs_review
> ```
> 
> ---
> 
> ## `relationships`
> 
> ```sql
> CREATE TABLE relationships (
>   relationship_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
> 
>   source_concept_id UUID REFERENCES concepts(concept_id),
>   target_concept_id UUID REFERENCES concepts(concept_id),
> 
>   source_ledger_id UUID REFERENCES ledger(ledger_id),
>   target_ledger_id UUID REFERENCES ledger(ledger_id),
> 
>   relationship_type TEXT NOT NULL,
> 
>   relationship_origin TEXT NOT NULL,
>   strength NUMERIC,
>   confidence NUMERIC,
> 
>   severity TEXT,
>   time_delta_minutes INT,
> 
>   evidence_summary TEXT,
>   source_id UUID REFERENCES sources(source_id),
> 
>   metadata_json JSONB DEFAULT '{}'::jsonb,
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> Recommended `relationship_type` values:
> 
> ```text
> may_cause
> may_worsen
> may_improve
> treats
> interacts_with
> contraindicated_with
> raises
> lowers
> masks
> duplicates_effect
> triggered_by
> associated_with
> requires_monitoring_of
> preceded
> followed_by
> co_occurred_with
> contradicts
> supports
> ```
> 
> Recommended `relationship_origin` values:
> 
> ```text
> known_reference
> doctor_statement
> caregiver_observed
> patient_reported
> ai_derived
> pharmacist_review
> manual_review
> ```
> 
> ---
> 
> ## `ai_runs`
> 
> ```sql
> CREATE TABLE ai_runs (
>   ai_run_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
> 
>   run_time TIMESTAMPTZ DEFAULT now(),
>   analysis_type TEXT NOT NULL,
> 
>   window_start TIMESTAMPTZ,
>   window_end TIMESTAMPTZ,
> 
>   model_used TEXT,
>   prompt_version TEXT,
> 
>   input_summary TEXT,
>   output_summary TEXT,
> 
>   status TEXT DEFAULT 'completed',
>   metadata_json JSONB DEFAULT '{}'::jsonb
> );
> ```
> 
> ---
> 
> ## `ai_findings`
> 
> ```sql
> CREATE TABLE ai_findings (
>   finding_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
> 
>   ai_run_id UUID REFERENCES ai_runs(ai_run_id),
> 
>   finding_type TEXT NOT NULL,
>   title TEXT NOT NULL,
>   description TEXT,
> 
>   severity TEXT,
>   confidence NUMERIC,
> 
>   status TEXT DEFAULT 'open',
> 
>   related_ledger_ids UUID[] DEFAULT '{}',
>   related_concept_ids UUID[] DEFAULT '{}',
>   related_source_ids UUID[] DEFAULT '{}',
>   related_relationship_ids UUID[] DEFAULT '{}',
> 
>   doctor_question TEXT,
>   suggested_next_step TEXT,
> 
>   evidence_json JSONB DEFAULT '[]'::jsonb,
>   metadata_json JSONB DEFAULT '{}'::jsonb,
> 
>   created_at TIMESTAMPTZ DEFAULT now()
> );
> ```
> 
> Recommended `finding_type` values:
> 
> ```text
> pattern
> interaction
> contradiction
> missing_data
> care_gap
> red_flag
> baseline_deviation
> med_reconciliation_issue
> instruction_gap
> doctor_question
> equipment_issue
> behavior_loop
> environment_trigger
> claim_review
> context_inference
> ```
> 
> ---
> 
> # 5. Environment Handling
> 
> Do **not** create an environment table.
> 
> Use:
> 
> - `profile` for stable home/environment context
> - `concepts` for environment/context concepts
> - `ledger` for changing environment and life events
> - `relationships` for known or inferred effects
> - `ai_findings` for conclusions
> 
> ## Example
> 
> A move gets logged once:
> 
> ```text
> event_type: care_context
> event_subtype: relocation_period
> concept: Moving / relocation
> event_time: 2026-05-01
> event_end_time: 2026-05-20
> status: ongoing
> severity: high
> notes: Started packing/moving into new home.
> ```
> 
> The AI should infer possible consequence domains:
> 
> - dust exposure
> - stress increase
> - routine disruption
> - sleep disruption
> - medication timing disruption
> - oxygen/equipment relocation
> - exertion
> - food inconsistency
> - increased anxiety
> - fall/clutter risk
> 
> But these are **not automatically facts**.
> 
> They become:
> 
> - inferred relationships
> - hypotheses
> - things to verify against later events
> - doctor-facing context if supported
> 
> The AI should phrase it like:
> 
> > “The relocation period may be a multi-factor stressor. Later flare-ups during this window should be reviewed against dust, exertion, sleep disruption, medication timing, oxygen access, and anxiety load.”
> 
> Not:
> 
> > “The move caused the flare.”
> 
> That distinction is everything.
> 
> ---
> 
> # 6. Claims Handling
> 
> Claims stay in `ledger`.
> 
> A claim is anything asserted by:
> 
> - doctor
> - nurse
> - EMS
> - caregiver
> - patient
> - discharge paper
> - portal note
> - AI
> - family member
> 
> Examples:
> 
> ```text
> event_type: claim
> event_subtype: diagnosis_statement
> claim_text: "Anxiety likely contributing to dyspnea."
> claim_status: documented
> source_id: doctor note
> concept_id: Anxiety
> ```
> 
> ```text
> event_type: claim
> event_subtype: discharge_status
> claim_text: "Stable for discharge."
> claim_status: context_limited
> source_id: discharge paper
> ```
> 
> ```text
> event_type: claim
> event_subtype: caregiver_observation
> claim_text: "Symptoms worsen when she talks continuously."
> claim_status: observed
> concept_id: Talking continuously
> ```
> 
> The AI reviews claims against:
> 
> - ledger events
> - vitals
> - med list
> - care plan
> - relationships
> - later outcomes
> - baseline profile
> 
> ---
> 
> # 7. Medication Handling
> 
> ## `med_list`
> 
> The standing medication truth:
> 
> - prescribed
> - active
> - inactive
> - stopped
> - PRN
> - available at home
> - dose
> - frequency
> - reconciliation status
> - source
> 
> ## `ledger`
> 
> Actual medication behavior:
> 
> - taken
> - refused
> - missed
> - delayed
> - vomited
> - unavailable
> - side effect noted
> - symptom after dose
> 
> ## `relationships`
> 
> Medication knowledge:
> 
> - may cause
> - may worsen
> - interacts with
> - duplicates effect
> - raises/lowers
> - requires monitoring
> 
> ## `ai_findings`
> 
> Medication insight:
> 
> - interaction concern
> - medication reconciliation issue
> - med timing pattern
> - missed/refused care gap
> - doctor/pharmacist question
> 
> This is the correct split.
> 
> ---
> 
> # 8. Ingestion Manual
> 
> ## Input types
> 
> Start with the fast useful inputs:
> 
> 1. messy caregiver note
> 2. voice transcript
> 3. manual vital entry
> 4. medication taken/refused
> 5. food/OTC entry
> 6. discharge/doctor note pasted text
> 7. med bottle/photo OCR later
> 8. lab report later
> 
> Do **not** begin with device integrations. That’s a trap.
> 
> ---
> 
> ## Ingestion rule
> 
> Every input becomes up to five things:
> 
> 1. `source` row  
> 2. `concept` rows if missing  
> 3. `ledger` rows  
> 4. `med_list` update if medication list information appears  
> 5. `care_plan` update if instruction/plan/threshold appears  
> 
> Then AI can create:
> 
> 6. `relationships`  
> 7. `ai_findings`
> 
> ---
> 
> ## Example messy note
> 
> > “She took prednisone around 8. Refused hydroxyzine. HR 150, oxygen 95. Talking nonstop saying she can’t breathe. We just moved and everything is dusty.”
> 
> Output:
> 
> ### `sources`
> 
> One raw source:
> 
> ```text
> source_type: caregiver_note
> raw_text: original note
> ```
> 
> ### `ledger`
> 
> Rows:
> 
> ```text
> medication / Prednisone / taken / approx 8
> medication / Hydroxyzine / refused
> vital / Heart rate / 150 bpm
> vital / SpO2 / 95 %
> behavior / Talking continuously / observed
> symptom / Air hunger / reported
> care_context / Moving relocation / ongoing
> environment / Dust / observed
> ```
> 
> ### `relationships`
> 
> Potential generated relationships:
> 
> ```text
> Prednisone preceded Heart rate elevation
> Talking continuously co_occurred_with Air hunger
> Dust associated_with Air hunger
> Moving relocation associated_with Dust / Routine disruption
> ```
> 
> ### `ai_findings`
> 
> Possible findings:
> 
> ```text
> High HR with stable oxygen.
> Hydroxyzine prescribed/available but refused during distress.
> Relocation/dust may be relevant context for respiratory flare.
> Need exact albuterol timing, oxygen flow, respiratory rate.
> Ask clinician for HR action threshold when SpO2 is stable.
> ```
> 
> ---
> 
> # 9. AI Inference Rules
> 
> The AI should infer context, but label inference.
> 
> ## Anchor events
> 
> Certain ledger events should trigger inferred context checks.
> 
> ### Moving / relocation
> 
> Potential inferred domains:
> 
> ```text
> dust
> stress
> routine disruption
> sleep disruption
> medication timing disruption
> equipment access issue
> oxygen setup change
> exertion
> food inconsistency
> fall/clutter risk
> anxiety load
> ```
> 
> ### Hospital discharge
> 
> Potential inferred domains:
> 
> ```text
> medication changes
> conflicting instructions
> follow-up needed
> red-flag thresholds missing
> home feasibility gap
> pharmacy pickup required
> patient understanding assumed
> ```
> 
> ### New medication started
> 
> Potential inferred domains:
> 
> ```text
> side effects
> drug interactions
> food interactions
> vital changes
> symptom changes
> adherence issues
> duplicate therapy
> ```
> 
> ### Symptom flare
> 
> Potential inferred domains:
> 
> ```text
> recent meds
> missed/refused meds
> OTCs/foods
> environment
> behavior
> equipment
> sleep
> infection signs
> baseline deviation
> ```
> 
> ---
> 
> ## Critical rule
> 
> Inference does **not** equal fact.
> 
> Store inferred relationships with:
> 
> ```text
> relationship_origin = ai_derived
> confidence = lower until supported
> evidence_summary = why AI thinks it may matter
> ```
> 
> If later ledger events support the inference, increase confidence.
> 
> ---
> 
> # 10. Analysis Workflow
> 
> ## A. Intake Extractor
> 
> Goal:
> 
> > Turn messy text into structured rows.
> 
> Output:
> 
> - source
> - concepts
> - ledger events
> - possible med/care-plan updates
> - uncertainty notes
> 
> ---
> 
> ## B. Medication Reconciliation Scanner
> 
> Goal:
> 
> > Compare med list against actual ledger behavior and sources.
> 
> Checks:
> 
> - active meds not taken
> - PRN meds repeatedly refused
> - meds found at home but not in care plan
> - doctor list conflicts with pharmacy/bottle
> - duplicate meds
> - stopped meds still used
> - OTC/supplement interactions
> - missing dose/frequency
> - missing max daily dose
> - oxygen/treatment unclear
> 
> ---
> 
> ## C. Interaction Scanner
> 
> Goal:
> 
> > Check medications, OTCs, foods, behaviors, environment, and conditions together.
> 
> Checks:
> 
> - drug-drug
> - drug-food
> - drug-condition
> - drug-behavior
> - drug-environment
> - duplicate side effects
> - stimulant load
> - sedation/fall risk
> - glucose elevation
> - HR elevation
> - BP change
> - respiratory symptom worsening
> 
> ---
> 
> ## D. Truth Reconciliation Scanner
> 
> Goal:
> 
> > Compare claims against reality.
> 
> Checks:
> 
> - doctor claim vs later events
> - discharge instruction vs home feasibility
> - patient statement vs vitals
> - caregiver observation vs repeated data
> - “stable” vs later escalation
> - “noncompliant” vs barriers/refusals/side effects/confusion
> - “normal” vs patient-specific baseline
> - vague instruction vs need for threshold
> 
> ---
> 
> ## E. Context Inference Scanner
> 
> Goal:
> 
> > Use anchor events to infer likely affected domains.
> 
> Example:
> 
> Moving event exists. AI checks:
> 
> - did symptoms rise during move window?
> - were meds missed?
> - did sleep worsen?
> - did food change?
> - did dust/environment appear?
> - did oxygen/device access change?
> - did anxiety/HR increase?
> 
> Output:
> 
> - inferred relationship
> - finding if supported
> - missing-data item if not enough evidence
> 
> ---
> 
> ## F. Doctor Packet Generator
> 
> Goal:
> 
> > Convert the mess into a useful clinician-facing summary.
> 
> Output:
> 
> 1. main concern
> 2. key timeline
> 3. medication reconciliation issues
> 4. pattern findings
> 5. contradictions / unclear claims
> 6. missing data
> 7. top doctor/pharmacist questions
> 8. evidence list
> 
> ---
> 
> # 11. First Useful AI Prompts
> 
> ## Intake extraction prompt
> 
> ```text
> You are a clinical data extraction assistant for a private single-patient health ledger.
> 
> Convert the messy note into structured data.
> 
> Do not diagnose.
> Do not treat any source as absolute truth.
> Extract events, claims, medication updates, care-plan instructions, and possible concepts.
> 
> Important:
> - Refused, missed, unavailable, absent, normal, and unclear events matter.
> - If an event implies broader context, label that as inference, not fact.
> - Preserve exact wording for claims.
> - Use approximate time only if clearly inferable; otherwise null.
> - Output valid JSON only.
> 
> Return:
> {
>   "source": {
>     "source_type": "",
>     "title": "",
>     "source_time": null,
>     "raw_text": ""
>   },
>   "concepts_to_create": [
>     {
>       "name": "",
>       "type": "",
>       "aliases": [],
>       "properties_json": {}
>     }
>   ],
>   "ledger_events": [
>     {
>       "event_time": null,
>       "event_end_time": null,
>       "event_type": "",
>       "event_subtype": "",
>       "concept_name": "",
>       "value_numeric": null,
>       "value_text": null,
>       "unit": null,
>       "status": "",
>       "severity": "",
>       "confidence": 0.0,
>       "location_label": null,
>       "episode_key": null,
>       "claim_text": null,
>       "claim_status": null,
>       "notes": "",
>       "context_json": {}
>     }
>   ],
>   "med_list_updates": [],
>   "care_plan_updates": [],
>   "inferred_context_checks": [],
>   "uncertainties": []
> }
> ```
> 
> ---
> 
> ## Truth reconciliation prompt
> 
> ```text
> You are a clinical truth-reconciliation assistant.
> 
> You are analyzing one patient.
> 
> Your job is not to diagnose. Your job is to compare:
> - what was claimed
> - what was measured
> - what was observed
> - what was instructed
> - what was actually done
> - what changed in the environment/context
> - what medications/OTCs/foods/treatments were involved
> 
> Treat every doctor note, discharge paper, patient statement, caregiver observation, device reading, and AI inference as evidence with reliability, not automatic truth.
> 
> Identify:
> 1. supported claims
> 2. contradicted claims
> 3. incomplete or vague claims
> 4. stale assumptions
> 5. missing data
> 6. medication/treatment issues
> 7. environmental/context triggers
> 8. behavior loops
> 9. care-plan gaps
> 10. doctor/pharmacist questions
> 
> Output valid JSON:
> {
>   "summary": "",
>   "findings": [
>     {
>       "finding_type": "",
>       "title": "",
>       "description": "",
>       "severity": "",
>       "confidence": 0.0,
>       "related_ledger_refs": [],
>       "related_concept_names": [],
>       "doctor_question": "",
>       "suggested_next_step": "",
>       "evidence": [
>         {
>           "source": "",
>           "reason": ""
>         }
>       ],
>       "missing_data": []
>     }
>   ]
> }
> ```
> 
> ---
> 
> # 12. Same-Day Build Plan
> 
> ## Goal
> 
> Functional in hours:
> 
> > paste messy note → database rows → AI analysis → doctor-facing findings
> 
> Not pretty. Useful.
> 
> ---
> 
> ## Phase 1 — Database
> 
> Create Postgres database:
> 
> ```text
> qiclinical
> ```
> 
> Run schema for:
> 
> ```text
> profile
> concepts
> sources
> med_list
> care_plan
> ledger
> relationships
> ai_runs
> ai_findings
> ```
> 
> ---
> 
> ## Phase 2 — Seed concepts
> 
> Seed only high-signal concepts.
> 
> ### Meds / therapies
> 
> ```text
> Prednisone
> Albuterol
> Hydroxyzine
> Guaifenesin
> Oxygen therapy
> Nebulizer treatment
> Acetaminophen
> Ibuprofen
> Diphenhydramine
> Caffeine
> ```
> 
> ### Vitals
> 
> ```text
> Heart rate
> SpO2
> Blood pressure systolic
> Blood pressure diastolic
> Temperature
> Blood glucose
> Respiratory rate
> Weight
> ```
> 
> ### Symptoms
> 
> ```text
> Dyspnea
> Air hunger
> Wheezing
> Cough
> Congestion
> Anxiety
> Panic
> Tremor
> Rash
> Dizziness
> Confusion
> Fatigue
> Chest pain
> Swelling
> Pain
> ```
> 
> ### Behavior / context
> 
> ```text
> Talking continuously
> Medication refusal
> Missed medication
> Poor sleep
> Routine disruption
> Exertion
> Lying flat
> Restlessness
> Agitation
> Symptom checking
> ```
> 
> ### Environment / devices
> 
> ```text
> Moving / relocation
> New home environment
> Dust
> Cold room
> Hot room
> Humidity
> Smoke
> Cleaning fumes
> Oxygen tank
> Oxygen concentrator
> Pulse oximeter
> BP cuff
> Glucose meter
> Medication storage change
> Oxygen access issue
> ```
> 
> ---
> 
> ## Phase 3 — Use NocoDB for quick UI
> 
> Create simple views:
> 
> ### `Quick Ledger Entry`
> 
> Fields:
> 
> - event_time
> - event_end_time
> - event_type
> - event_subtype
> - concept_id
> - value_numeric
> - value_text
> - unit
> - status
> - severity
> - location_label
> - episode_key
> - notes
> 
> ### `Medication List`
> 
> Fields:
> 
> - med_name
> - status
> - reconciliation_status
> - dose
> - route
> - frequency
> - PRN
> - indication
> - source
> - available_at_home
> - needs_reconciliation
> 
> ### `AI Findings Review`
> 
> Fields:
> 
> - finding_type
> - title
> - severity
> - confidence
> - doctor_question
> - suggested_next_step
> - status
> 
> ---
> 
> ## Phase 4 — Scripts
> 
> Create four scripts first.
> 
> ```text
> 01_create_schema.py
> 02_seed_concepts.py
> 03_ingest_note.py
> 04_analyze_window.py
> ```
> 
> Later:
> 
> ```text
> 05_export_doctor_packet.py
> 06_ingest_document.py
> 07_med_reconciliation.py
> 08_context_inference.py
> ```
> 
> ---
> 
> # 13. Processing Flow
> 
> ## Ingestion
> 
> 1. User enters note.
> 2. Raw note stored in `sources`.
> 3. LLM extracts structured events.
> 4. Concepts are matched by name/alias.
> 5. Missing concepts are created.
> 6. Ledger rows are inserted.
> 7. Med list/care plan updates are suggested or inserted.
> 8. AI run is logged.
> 
> ---
> 
> ## Analysis
> 
> 1. Pull ledger window.
> 2. Pull active med list.
> 3. Pull care plan.
> 4. Pull relationships.
> 5. Pull profile baselines.
> 6. Analyze:
>    - meds
>    - vitals
>    - symptoms
>    - behavior
>    - environment
>    - claims
>    - care plan gaps
> 7. Insert findings.
> 8. Generate doctor packet.
> 
> ---
> 
> # 14. What the AI Should Catch Early
> 
> ## Medication
> 
> - active med not taken
> - PRN med repeatedly refused
> - rescue med near HR spikes
> - steroid near anxiety/glucose elevation
> - OTC/supplement conflicts
> - missing max dose
> - conflicting med sources
> - old meds still in home
> 
> ## Claims
> 
> - “stable” but later escalation
> - “normal vitals” but abnormal for patient
> - “anxiety” supported but incomplete
> - “noncompliant” without barrier analysis
> - discharge instruction vague
> - no threshold for when to call/ER
> 
> ## Environment/context
> 
> - moving window overlaps flare-ups
> - dust/stress/routine disruption likely relevant
> - oxygen access/device setup changed
> - sleep/food/med timing disrupted
> - new home transition causing multi-factor stress
> 
> ## Behavior
> 
> - talking continuously with air hunger/high HR
> - refusal loop during anxiety episodes
> - exertion before dyspnea
> - poor sleep before symptom escalation
> - lying position worsening symptoms
> 
> ## Missing data
> 
> - respiratory rate
> - exact med timing
> - oxygen flow rate
> - current verified med list
> - pharmacist interaction review
> - EKG/rhythm review if HR repeatedly high
> - clear home action thresholds
> 
> ---
> 
> # 15. Manual Rules for Users
> 
> ## Log anchor events, not every implication.
> 
> Good entries:
> 
> ```text
> Started packing for move.
> Moved into new home.
> Oxygen tank unavailable.
> Prednisone taken.
> Hydroxyzine refused.
> HR 150, SpO2 95.
> Talking continuously.
> Room very dusty.
> ```
> 
> The AI can infer the consequence domains.
> 
> You do **not** need to manually write:
> 
> ```text
> Move may cause dust, stress, sleep disruption, med timing disruption...
> ```
> 
> That is the AI’s job.
> 
> ---
> 
> ## But log observed specifics when known.
> 
> If you know dust was present, log dust.
> 
> If you know sleep was bad, log sleep.
> 
> If you know meds were missed, log missed meds.
> 
> AI can infer possibilities, but real observations beat inference.
> 
> ---
> 
> ## Never hide uncertainty.
> 
> Use notes like:
> 
> ```text
> Exact time unknown.
> Dose unclear.
> Patient reported this.
> Caregiver observed this.
> From discharge paper only.
> Bottle seen at home.
> Not sure if current.
> ```
> 
> Uncertainty is not failure. It is signal.
> 
> ---
> 
> # 16. Doctor Packet Format
> 
> Simple Markdown output:
> 
> ```text
> Clinical Pattern Summary
> 
> Patient:
> Date range:
> Primary concern:
> 
> 1. Key timeline
> 2. Current medication list / reconciliation issues
> 3. Recent symptoms and vitals
> 4. Relevant environment/context changes
> 5. Patterns observed
> 6. Contradictions or unclear claims
> 7. Missing data
> 8. Questions for clinician/pharmacist
> 9. Evidence references
> 
> Note:
> This summary identifies patterns and questions for clinician review. It is not a diagnosis.
> ```
> 
> ---
> 
> # 17. Final Architecture Summary
> 
> ```text
> profile
>   = who this person is, baseline, stable context
> 
> concepts
>   = dictionary of meds, symptoms, vitals, behaviors, environment, devices, conditions
> 
> sources
>   = where information came from
> 
> med_list
>   = what meds/therapies are prescribed, active, stopped, available, uncertain
> 
> care_plan
>   = what is supposed to happen and when to escalate
> 
> ledger
>   = what actually happened, what was measured, what was claimed, what changed
> 
> relationships
>   = known, observed, or AI-derived connections
> 
> ai_runs
>   = processing metadata
> 
> ai_findings
>   = patterns, contradictions, risks, gaps, questions, insights
> ```
> 
> The clean operating rule:
> 
> > `ledger` records reality over time.  
> > `med_list` records intended/current medication truth.  
> > `care_plan` records expected action.  
> > `relationships` connect causes, risks, and patterns.  
> > `ai_findings` explain what may be wrong, missing, contradictory, or worth clinician review.
> 
> That’s the lean blueprint.

### Assistant
> Yes — the critique is solid, and it confirms the architecture is mostly right. The main changes worth accepting are **traceability, temporal support, concept control, and scoring** — without adding table bloat. The critique specifically supports the 9-table core, the ledger backbone, concept dictionary, med-list separation, and doctor-facing utility, while warning about temporal complexity, concept drift, relationship noise, and the need for indexes/review flows. fileciteturn0file0
> 
> Here’s the tightened final blueprint.
> 
> # Final Lean v0 Schema
> 
> Keep the 9 tables:
> 
> ```text
> profile
> concepts
> sources
> med_list
> care_plan
> ledger
> relationships
> ai_runs
> ai_findings
> ```
> 
> Add **only small column-level improvements**, not new tables.
> 
> ---
> 
> # 1. Accepted Improvements
> 
> ## Add to `ledger`
> 
> ```sql
> derived_from_ai_run_id UUID REFERENCES ai_runs(ai_run_id)
> tags TEXT[] DEFAULT '{}'
> ```
> 
> Why: lets us know whether an event was human-entered, extracted by AI, or inferred from an AI run.
> 
> Also keep:
> 
> ```sql
> linked_ledger_id UUID
> episode_key TEXT
> event_time
> event_end_time
> ```
> 
> That handles acute events and long-running contexts like moving, recovery, poor sleep stretch, oxygen access issue, steroid course, etc.
> 
> ---
> 
> ## Add to `relationships`
> 
> ```sql
> direction TEXT DEFAULT 'directed'
> status TEXT DEFAULT 'active'
> ```
> 
> Why: relationships can become noisy fast. We need to know whether something is current, dismissed, confirmed, or low-confidence.
> 
> Recommended `status`:
> 
> ```text
> active
> suspected
> confirmed
> dismissed
> stale
> needs_review
> ```
> 
> ---
> 
> ## Add to `ai_findings`
> 
> ```sql
> priority_score NUMERIC
> actionability_score NUMERIC
> linked_finding_ids UUID[] DEFAULT '{}'
> ```
> 
> Why: not all findings matter equally. The AI should rank by:
> 
> ```text
> severity × confidence × actionability
> ```
> 
> A scary but vague finding should not outrank a moderate, actionable medication issue.
> 
> ---
> 
> ## Add to `concepts`
> 
> ```sql
> parent_concept_id UUID REFERENCES concepts(concept_id)
> review_status TEXT DEFAULT 'approved'
> ```
> 
> Why: prevents concept drift.
> 
> Example:
> 
> ```text
> Air hunger → parent: Dyspnea
> Rescue inhaler → alias/concept relationship to Albuterol
> Talking nonstop → parent: Talking continuously
> ```
> 
> Recommended `review_status`:
> 
> ```text
> approved
> ai_suggested
> needs_review
> merged
> deprecated
> ```
> 
> ---
> 
> # 2. Do Not Add These Yet
> 
> Do **not** add:
> 
> ```text
> episodes table
> claims table
> environment table
> finding_evidence table
> patient_baselines table
> option_sets table
> option_values table
> ```
> 
> Not yet.
> 
> They are legitimate later, but for v0 they create friction.
> 
> Use:
> 
> | Need | Handle with |
> |---|---|
> | episodes | `ledger.episode_key` |
> | claims | `ledger.event_type = claim` |
> | environment | `ledger.event_type = environment/care_context` |
> | evidence | `ai_findings.evidence_json` |
> | baselines | `profile.baseline_json` |
> | dropdowns | app/constants first |
> 
> ---
> 
> # 3. Final Manual Rules
> 
> ## The ledger is the truth stream
> 
> Everything time-based goes into `ledger`:
> 
> ```text
> med taken
> med refused
> symptom reported
> vital measured
> doctor claim
> patient claim
> caregiver observation
> move started
> oxygen unavailable
> dust exposure
> ER visit
> treatment performed
> instruction received
> ```
> 
> ## The med list is not the ledger
> 
> `med_list` answers:
> 
> > What is supposed to exist?
> 
> `ledger` answers:
> 
> > What actually happened?
> 
> ## The care plan is the intended strategy
> 
> `care_plan` answers:
> 
> > What are we supposed to do, when, and under what threshold?
> 
> If no threshold exists, the AI should flag that as an `instruction_gap`.
> 
> ---
> 
> # 4. AI Must Infer, But Not Pretend
> 
> For anchor events like:
> 
> ```text
> moved into new home
> started packing
> hospital discharge
> new medication started
> oxygen not available
> ```
> 
> The AI should infer possible affected domains:
> 
> ```text
> dust
> stress
> sleep disruption
> routine disruption
> med timing disruption
> food inconsistency
> oxygen setup issue
> exertion
> anxiety load
> fall/clutter risk
> ```
> 
> But it must label them as:
> 
> ```text
> inferred_context_check
> ```
> 
> Not fact.
> 
> The correct output is:
> 
> > “The relocation period may be a multi-factor contributor. Check whether symptoms, med timing, sleep, dust exposure, oxygen access, or anxiety changed during this window.”
> 
> Not:
> 
> > “The move caused the flare.”
> 
> That’s the line.
> 
> ---
> 
> # 5. Immediate v0 Build Order
> 
> Do this in this order. Don’t wander.
> 
> ## Step 1 — Database
> 
> Create:
> 
> ```text
> profile
> concepts
> sources
> med_list
> care_plan
> ledger
> relationships
> ai_runs
> ai_findings
> ```
> 
> Add indexes immediately:
> 
> ```sql
> CREATE INDEX idx_ledger_time ON ledger(event_time);
> CREATE INDEX idx_ledger_concept ON ledger(concept_id);
> CREATE INDEX idx_ledger_type ON ledger(event_type);
> CREATE INDEX idx_ledger_episode ON ledger(episode_key);
> CREATE INDEX idx_ledger_source ON ledger(source_id);
> 
> CREATE INDEX idx_relationships_source_concept ON relationships(source_concept_id);
> CREATE INDEX idx_relationships_target_concept ON relationships(target_concept_id);
> 
> CREATE INDEX idx_findings_type ON ai_findings(finding_type);
> CREATE INDEX idx_findings_status ON ai_findings(status);
> CREATE INDEX idx_findings_priority ON ai_findings(priority_score);
> ```
> 
> ## Step 2 — Seed concepts
> 
> Seed meds, vitals, symptoms, behaviors, environments, devices, and care-context concepts.
> 
> ## Step 3 — Use NocoDB
> 
> Create three working views:
> 
> ```text
> Quick Ledger Entry
> Medication Reconciliation
> AI Findings Review
> ```
> 
> ## Step 4 — Build ingestion script
> 
> Input:
> 
> ```text
> messy note / voice transcript / pasted doctor note
> ```
> 
> Output:
> 
> ```text
> source row
> concept matches/creates
> ledger rows
> possible med_list updates
> possible care_plan updates
> ai_run metadata
> ```
> 
> ## Step 5 — Build analysis script
> 
> Run over:
> 
> ```text
> last 24 hours
> last 7 days
> episode_key
> custom date window
> ```
> 
> Output into `ai_findings`.
> 
> ---
> 
> # 6. Core AI Finding Types
> 
> Use this controlled list:
> 
> ```text
> pattern
> interaction
> contradiction
> missing_data
> care_gap
> red_flag
> baseline_deviation
> med_reconciliation_issue
> instruction_gap
> doctor_question
> equipment_issue
> behavior_loop
> environment_trigger
> claim_review
> context_inference
> ```
> 
> The most important early ones:
> 
> ```text
> med_reconciliation_issue
> instruction_gap
> interaction
> claim_review
> missing_data
> behavior_loop
> context_inference
> ```
> 
> Those will produce value fastest.
> 
> ---
> 
> # 7. Scoring Formula
> 
> Each finding should get:
> 
> ```text
> severity
> confidence
> actionability_score
> priority_score
> ```
> 
> Simple v0 scoring:
> 
> ```text
> priority_score = severity_score × confidence × actionability_score
> ```
> 
> Severity scores:
> 
> ```text
> urgent = 5
> high = 4
> medium = 3
> low = 2
> info = 1
> ```
> 
> Actionability:
> 
> ```text
> 1.0 = clear next action
> 0.7 = useful doctor question
> 0.4 = needs more data
> 0.2 = vague pattern
> ```
> 
> This prevents the AI from generating a pile of “interesting” nonsense.
> 
> ---
> 
> # 8. Final System Identity
> 
> The system is not a medical app.
> 
> It is:
> 
> > **A single-patient clinical reality ledger and truth-reconciliation engine.**
> 
> Its job:
> 
> ```text
> Capture what happened.
> Preserve where it came from.
> Compare reality against meds, claims, care plans, and baselines.
> Infer possible context effects.
> Find contradictions and missing data.
> Generate doctor/pharmacist questions.
> ```
> 
> That’s the clean lane.
> 
> # Final Verdict
> 
> The critique basically says: **build it, but add traceability, indexes, concept hygiene, scoring, and review flow.** I agree. fileciteturn0file0
> 
> So the final answer is:
> 
> ```text
> 9 tables.
> Ledger-centered.
> Med list separated.
> Claims inside ledger.
> Environment inside ledger/profile.
> Relationships as graph edges.
> AI findings as ranked, evidence-linked outputs.
> No new tables until real use proves the need.
> ```
> 
> That’s the version I’d actually build.

### User
> ok, creat the document any ai and developer can use to build this from scratch.

### Assistant
> I’ll turn this into a build-ready spec: clean enough for a developer, explicit enough for an AI agent, and strict enough to prevent schema drift or “AI doctor” nonsense.

### Assistant
> Created the build spec in canvas: **Single Patient Clinical Reality Ai Build Spec**.
> 
> It’s structured so a developer or AI agent can build from scratch: doctrine, schema, SQL, ingestion rules, AI prompts, scoring, workflow, queries, and same-day build order.

### User
> add ingestion, here is suggestions from grok.

### Assistant
> Got it. I’ll fold Grok’s ingestion strategy into the build spec without bloating the schema: source-first ingestion, Docling/OCR path, local LLM with API fallback, confidence thresholds, review queue, and post-ingestion automation.

### Assistant
> Added the ingestion section to the build spec.
> 
> It now includes Grok’s useful pieces: source-first ingestion, Docling/OCR path, local LLM with API fallback, structured validation, smart commit rules, conflict detection, review queue, few-shot corrections, post-ingestion automation, and edge-case handling — while keeping the 9-table schema intact. fileciteturn1file0
