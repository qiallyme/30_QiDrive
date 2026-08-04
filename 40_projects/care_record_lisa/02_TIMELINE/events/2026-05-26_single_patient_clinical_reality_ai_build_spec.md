---
layout: page
title: Single Patient Clinical Reality Ai Build Spec
slug: single-patient-clinical-reality-ai-build-spec
summary: ""
status: publish
created_at: "2026-07-16T06:19:39-04:00"
updated_at: "2026-07-18T11:03:19-04:00"
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: 0b74351bb0644743938ae4a6d50cc845
canonical_ref: ""
source_type: manual
template_key: master-template
type: note
---

# Single-Patient Clinical Reality + AI Analysis System

## Build Specification for Developers and AI Agents

**Version:** v0.1  
**Purpose:** Private single-patient clinical truth-reconciliation, pattern detection, medication reconciliation, and doctor-facing insight generation.  
**Primary User:** Caregiver/operator managing one complex patient.  
**System Type:** Single-patient clinical reality ledger + AI analysis layer.  

---

# 1. Executive Summary

This system is designed to help analyze one patient’s health reality over time by combining:

- what happened,
- what was measured,
- what was claimed,
- what was prescribed,
- what was actually taken or refused,
- what the care plan said,
- what the environment and behavior suggest,
- what the AI can infer,
- and what should be asked of clinicians.

The system is **not a diagnosis engine**. It is a **truth-reconciliation and pattern-detection engine**.

Its core job is to identify mismatches between:

- the chart,
- the body,
- the patient’s lived reality,
- the medication list,
- the care plan,
- the home environment,
- caregiver observations,
- and clinical claims.

The central design rule:

> No source is truth. Every source is evidence. Truth emerges from time-aware, patient-specific reconciliation.

---

# 2. System Doctrine

## 2.1 What the System Must Do

The system must:

1. Capture messy real-world patient data quickly.
2. Preserve source provenance.
3. Convert messy notes into structured timeline events.
4. Separate prescribed/intended care from actual lived behavior.
5. Track active, stopped, uncertain, and conflicting medications.
6. Identify medication, OTC, supplement, food, behavior, environment, and device interactions.
7. Treat doctor notes, discharge summaries, patient statements, and caregiver observations as claims/evidence, not automatic truth.
8. Detect contradictions, missing data, vague instructions, stale assumptions, and care gaps.
9. Generate doctor/pharmacist-facing questions.
10. Produce concise clinical-pattern summaries without diagnosing.

## 2.2 What the System Must Not Do

The system must not:

1. Diagnose the patient.
2. Replace clinicians.
3. Assume doctor notes are always correct.
4. Assume patient statements are always clinically complete.
5. Assume caregiver interpretations are always correct.
6. Treat AI inference as fact.
7. Generate unsupported conclusions.
8. Bury uncertainty.
9. Create table sprawl.
10. Build a complex app before the ledger works.

## 2.3 Required Output Framing

The system should avoid saying:

> “The doctor was wrong.”

Instead, it should say:

> “This claim appears incomplete, context-limited, or contradicted by later ledger events. Clinician review is recommended.”

The output should be calm, evidence-linked, and doctor-facing.

---

# 3. Core Architecture

The final v0 schema uses **9 tables**.

```text
profile
concepts
sources
med_list
care_plan
ledger
relationships
ai_runs
ai_findings
```

Do not add more tables unless real usage proves the need.

## 3.1 Table Roles

| Table | Purpose |
|---|---|
| `profile` | The one patient: baseline, context, known risks, thresholds. |
| `concepts` | Dictionary of reusable clinical/life concepts. |
| `sources` | Raw source material and provenance. |
| `med_list` | Prescribed/current/available/stopped/uncertain medications and therapies. |
| `care_plan` | Intended care strategy, instructions, thresholds, goals. |
| `ledger` | Universal time-based reality stream. |
| `relationships` | Known, observed, or AI-derived connections between things. |
| `ai_runs` | Metadata for AI processing runs. |
| `ai_findings` | AI outputs: patterns, contradictions, missing data, questions, risks. |

---

# 4. Database Schema

PostgreSQL is recommended.

Enable UUID support:

```sql
CREATE EXTENSION IF NOT EXISTS pgcrypto;
```

---

## 4.1 `profile`

The patient and stable context. This table should normally contain exactly one row.

```sql
CREATE TABLE profile (
  profile_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  display_name TEXT,
  dob DATE,
  sex_at_birth TEXT,

  baseline_json JSONB DEFAULT '{}'::jsonb,
  risk_json JSONB DEFAULT '{}'::jsonb,
  context_json JSONB DEFAULT '{}'::jsonb,

  notes TEXT,
  updated_at TIMESTAMPTZ DEFAULT now()
);
```

### Use `baseline_json` For

- usual SpO2 range,
- usual resting HR,
- usual BP notes,
- usual glucose context,
- patient-specific normal ranges,
- clinician thresholds if known.

Example:

```json
{
  "spo2_usual": "94-96",
  "hr_usual_resting": "90-110",
  "bp_notes": "Right arm often lower",
  "clinician_thresholds": {
    "spo2": "unknown",
    "heart_rate": "unknown",
    "glucose": "unknown"
  }
}
```

### Use `risk_json` For

- fall risk,
- oxygen dependence,
- steroid sensitivity,
- medication refusal risk,
- polypharmacy risk,
- sedating medication risk,
- rescue inhaler overuse concern.

### Use `context_json` For

- home context,
- stable environmental triggers,
- mobility context,
- caregiver context,
- routine sensitivity,
- equipment setup.

Example:

```json
{
  "home_context": {
    "known_environment_triggers": ["dust", "cold room", "routine disruption"],
    "routine_sensitivity": "Routine changes may worsen anxiety, sleep, medication adherence, and symptom perception.",
    "oxygen_equipment": "Home oxygen equipment present; exact setup should be verified."
  }
}
```

---

## 4.2 `concepts`

The reusable dictionary of meaningful things.

```sql
CREATE TABLE concepts (
  concept_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  name TEXT NOT NULL,
  type TEXT NOT NULL,

  aliases TEXT[] DEFAULT '{}',
  standard_code TEXT,
  code_system TEXT,

  parent_concept_id UUID REFERENCES concepts(concept_id),
  properties_json JSONB DEFAULT '{}'::jsonb,

  review_status TEXT DEFAULT 'approved',
  active BOOLEAN DEFAULT true,
  created_at TIMESTAMPTZ DEFAULT now()
);
```

### Recommended `type` Values

```text
medication
otc
supplement
food
beverage
vital
symptom
condition
behavior
environment
device
treatment
care_context
claim_topic
lab
instruction
```

### Recommended `review_status` Values

```text
approved
ai_suggested
needs_review
merged
deprecated
```

### Examples

| Name | Type | Aliases |
|---|---|---|
| Prednisone | medication | `{pred, steroid}` |
| Albuterol | medication | `{rescue inhaler, inhaler}` |
| Hydroxyzine | medication | `{hydrox, anxiety med}` |
| SpO2 | vital | `{oxygen level, O2}` |
| Heart rate | vital | `{pulse, HR}` |
| Air hunger | symptom | `{can't breathe, dyspnea}` |
| Talking continuously | behavior | `{talking nonstop}` |
| Moving / relocation | care_context | `{move, moved, packing}` |
| Dust | environment | `{dusty, dust exposure}` |
| Oxygen concentrator | device | `{oxygen machine}` |

---

## 4.3 `sources`

Raw material and provenance.

```sql
CREATE TABLE sources (
  source_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  source_type TEXT NOT NULL,
  title TEXT,
  source_time TIMESTAMPTZ,

  storage_uri TEXT,
  raw_text TEXT,
  summary TEXT,

  reliability TEXT,
  processed_status TEXT DEFAULT 'new',

  metadata_json JSONB DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ DEFAULT now()
);
```

### Recommended `source_type` Values

```text
manual_entry
voice_transcript
caregiver_note
patient_statement
doctor_note
discharge_paper
med_list
pharmacy_label
lab_report
photo
screenshot
vitals_device
portal_message
ai_extraction
```

### Recommended `processed_status` Values

```text
new
processed
needs_review
failed
ignored
```

---

## 4.4 `med_list`

The standing medication and therapy list.

This table exists because prescribed/current/available medication truth is not the same thing as actual medication behavior.

```sql
CREATE TABLE med_list (
  med_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  concept_id UUID REFERENCES concepts(concept_id),

  med_name TEXT NOT NULL,
  generic_name TEXT,
  brand_name TEXT,

  status TEXT DEFAULT 'active',
  reconciliation_status TEXT DEFAULT 'unknown',
  med_type TEXT,

  dose_amount NUMERIC,
  dose_unit TEXT,
  route TEXT,
  frequency TEXT,

  prn BOOLEAN DEFAULT false,
  prn_reason TEXT,
  max_daily_amount NUMERIC,
  max_daily_unit TEXT,

  indication TEXT,
  prescriber TEXT,
  pharmacy TEXT,

  start_date DATE,
  end_date DATE,
  stopped_reason TEXT,

  source_id UUID REFERENCES sources(source_id),

  available_at_home BOOLEAN,
  needs_reconciliation BOOLEAN DEFAULT false,

  notes TEXT,
  metadata_json JSONB DEFAULT '{}'::jsonb,

  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);
```

### Recommended `status` Values

```text
active
inactive
stopped
paused
expired
unknown
duplicate_possible
needs_reconciliation
not_available
```

### Recommended `reconciliation_status` Values

```text
verified
bottle_seen
pharmacy_verified
doctor_list_only
discharge_paper_only
patient_reported
caregiver_reported
conflicting
unknown
needs_review
```

### Recommended `med_type` Values

```text
prescription
otc
supplement
oxygen
inhaler
nebulizer_solution
unknown
```

### Rule

- `med_list` = what is prescribed, active, available, stopped, uncertain, or needs reconciliation.
- `ledger` = what was actually taken, refused, missed, delayed, or observed.

---

## 4.5 `care_plan`

What is supposed to happen.

```sql
CREATE TABLE care_plan (
  care_plan_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  concept_id UUID REFERENCES concepts(concept_id),

  plan_type TEXT NOT NULL,
  status TEXT DEFAULT 'active',

  instructions TEXT,

  dose_amount NUMERIC,
  dose_unit TEXT,
  route TEXT,
  frequency TEXT,
  max_daily_amount NUMERIC,
  max_daily_unit TEXT,

  threshold_json JSONB DEFAULT '{}'::jsonb,

  start_date DATE,
  end_date DATE,

  source_id UUID REFERENCES sources(source_id),

  notes TEXT,
  metadata_json JSONB DEFAULT '{}'::jsonb,

  created_at TIMESTAMPTZ DEFAULT now()
);
```

### Recommended `plan_type` Values

```text
medication_order
oxygen_order
monitoring_instruction
emergency_threshold
follow_up
diet_instruction
device_instruction
treatment_plan
behavior_instruction
home_care_goal
```

### Example `threshold_json`

```json
{
  "call_doctor_if": ["HR over 130 sustained", "glucose over clinician threshold"],
  "go_to_er_if": ["SpO2 below prescribed threshold", "confusion", "chest pain"],
  "unknown_thresholds": ["heart rate", "rescue inhaler max use"]
}
```

### Rule

- Treatment plan = `care_plan`.
- Treatment execution = `ledger`.

---

## 4.6 `ledger`

The universal time-based patient reality stream.

```sql
CREATE TABLE ledger (
  ledger_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  event_time TIMESTAMPTZ NOT NULL,
  event_end_time TIMESTAMPTZ,

  event_type TEXT NOT NULL,
  event_subtype TEXT,

  concept_id UUID REFERENCES concepts(concept_id),

  value_numeric NUMERIC,
  value_text TEXT,
  unit TEXT,

  status TEXT,
  severity TEXT,
  confidence NUMERIC DEFAULT 1.0,

  location_label TEXT,

  source_id UUID REFERENCES sources(source_id),
  linked_ledger_id UUID REFERENCES ledger(ledger_id),
  episode_key TEXT,

  claim_text TEXT,
  claim_status TEXT,

  observed_by TEXT,
  notes TEXT,
  context_json JSONB DEFAULT '{}'::jsonb,

  derived_from_ai_run_id UUID,
  tags TEXT[] DEFAULT '{}',

  created_at TIMESTAMPTZ DEFAULT now()
);
```

After `ai_runs` is created, add the foreign key:

```sql
ALTER TABLE ledger
ADD CONSTRAINT fk_ledger_ai_run
FOREIGN KEY (derived_from_ai_run_id)
REFERENCES ai_runs(ai_run_id);
```

### Recommended `event_type` Values

```text
medication
intake
vital
symptom
behavior
environment
device
treatment
care_action
clinical_contact
instruction
claim
note
```

### Recommended `status` Values

```text
taken
refused
missed
measured
reported
observed
absent
normal
abnormal
worsened
improved
resolved
ongoing
unavailable
unknown
completed
started
ended
```

### Recommended `claim_status` Values

```text
observed
reported
documented
inferred
supported
contradicted
incomplete
stale
unverified
context_limited
biased_language
needs_review
```

### Rule

If it happened, was measured, was claimed, was refused, was missed, was observed, was instructed, changed over time, or affected the patient’s reality, it belongs in `ledger`.

---

## 4.7 `relationships`

Graph edges between concepts and/or specific events.

```sql
CREATE TABLE relationships (
  relationship_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  source_concept_id UUID REFERENCES concepts(concept_id),
  target_concept_id UUID REFERENCES concepts(concept_id),

  source_ledger_id UUID REFERENCES ledger(ledger_id),
  target_ledger_id UUID REFERENCES ledger(ledger_id),

  relationship_type TEXT NOT NULL,

  relationship_origin TEXT NOT NULL,
  direction TEXT DEFAULT 'directed',
  status TEXT DEFAULT 'active',

  strength NUMERIC,
  confidence NUMERIC,

  severity TEXT,
  time_delta_minutes INT,

  evidence_summary TEXT,
  source_id UUID REFERENCES sources(source_id),

  metadata_json JSONB DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ DEFAULT now()
);
```

### Recommended `relationship_type` Values

```text
may_cause
may_worsen
may_improve
treats
interacts_with
contraindicated_with
raises
lowers
masks
duplicates_effect
triggered_by
associated_with
requires_monitoring_of
preceded
followed_by
co_occurred_with
contradicts
supports
```

### Recommended `relationship_origin` Values

```text
known_reference
doctor_statement
caregiver_observed
patient_reported
ai_derived
pharmacist_review
manual_review
```

### Recommended `status` Values

```text
active
suspected
confirmed
dismissed
stale
needs_review
```

---

## 4.8 `ai_runs`

Metadata for each AI process.

```sql
CREATE TABLE ai_runs (
  ai_run_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  run_time TIMESTAMPTZ DEFAULT now(),
  analysis_type TEXT NOT NULL,

  window_start TIMESTAMPTZ,
  window_end TIMESTAMPTZ,

  model_used TEXT,
  prompt_version TEXT,

  input_summary TEXT,
  output_summary TEXT,

  status TEXT DEFAULT 'completed',
  metadata_json JSONB DEFAULT '{}'::jsonb
);
```

### Recommended `analysis_type` Values

```text
intake_extract
episode_review
daily_review
interaction_scan
truth_reconciliation
med_reconciliation
doctor_packet
baseline_review
context_inference
```

---

## 4.9 `ai_findings`

AI output table.

```sql
CREATE TABLE ai_findings (
  finding_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  ai_run_id UUID REFERENCES ai_runs(ai_run_id),

  finding_type TEXT NOT NULL,
  title TEXT NOT NULL,
  description TEXT,

  severity TEXT,
  confidence NUMERIC,

  actionability_score NUMERIC,
  priority_score NUMERIC,

  status TEXT DEFAULT 'open',

  related_ledger_ids UUID[] DEFAULT '{}',
  related_concept_ids UUID[] DEFAULT '{}',
  related_source_ids UUID[] DEFAULT '{}',
  related_relationship_ids UUID[] DEFAULT '{}',
  linked_finding_ids UUID[] DEFAULT '{}',

  doctor_question TEXT,
  suggested_next_step TEXT,

  evidence_json JSONB DEFAULT '[]'::jsonb,
  metadata_json JSONB DEFAULT '{}'::jsonb,

  created_at TIMESTAMPTZ DEFAULT now()
);
```

### Recommended `finding_type` Values

```text
pattern
interaction
contradiction
missing_data
care_gap
red_flag
baseline_deviation
med_reconciliation_issue
instruction_gap
doctor_question
equipment_issue
behavior_loop
environment_trigger
claim_review
context_inference
```

### Recommended `status` Values

```text
open
reviewed
confirmed
dismissed
needs_more_data
clinician_reviewed
```

---

# 5. Required Indexes

Create indexes immediately.

```sql
CREATE INDEX idx_ledger_time ON ledger(event_time);
CREATE INDEX idx_ledger_concept ON ledger(concept_id);
CREATE INDEX idx_ledger_type ON ledger(event_type);
CREATE INDEX idx_ledger_episode ON ledger(episode_key);
CREATE INDEX idx_ledger_source ON ledger(source_id);
CREATE INDEX idx_ledger_tags ON ledger USING GIN(tags);

CREATE INDEX idx_concepts_name ON concepts(name);
CREATE INDEX idx_concepts_type ON concepts(type);
CREATE INDEX idx_concepts_aliases ON concepts USING GIN(aliases);

CREATE INDEX idx_med_list_status ON med_list(status);
CREATE INDEX idx_med_list_reconciliation ON med_list(reconciliation_status);

CREATE INDEX idx_care_plan_status ON care_plan(status);
CREATE INDEX idx_care_plan_type ON care_plan(plan_type);

CREATE INDEX idx_relationships_source_concept ON relationships(source_concept_id);
CREATE INDEX idx_relationships_target_concept ON relationships(target_concept_id);
CREATE INDEX idx_relationships_source_ledger ON relationships(source_ledger_id);
CREATE INDEX idx_relationships_target_ledger ON relationships(target_ledger_id);
CREATE INDEX idx_relationships_type ON relationships(relationship_type);

CREATE INDEX idx_findings_type ON ai_findings(finding_type);
CREATE INDEX idx_findings_status ON ai_findings(status);
CREATE INDEX idx_findings_priority ON ai_findings(priority_score);
```

---

# 6. Environment and Life Context Handling

Do not create a separate environment table.

Use:

- `profile` for stable home/environment context,
- `concepts` for environment and care-context concepts,
- `ledger` for time-based changes,
- `relationships` for inferred or known connections,
- `ai_findings` for actual conclusions.

## 6.1 Stable Environment

Store in `profile.context_json`.

Examples:

- known dust sensitivity,
- typical room setup,
- oxygen equipment location,
- baseline mobility setup,
- routine sensitivity.

## 6.2 Changing Environment

Store in `ledger`.

Examples:

```text
event_type: environment
event_subtype: dust_exposure
concept: Dust
```

```text
event_type: care_context
event_subtype: relocation_period
concept: Moving / relocation
```

Use `event_end_time` for ongoing periods.

## 6.3 Anchor Events

Certain events should trigger AI context checks.

### Moving / Relocation

Potential inferred domains:

```text
dust
stress
routine disruption
sleep disruption
medication timing disruption
equipment access issue
oxygen setup change
exertion
food inconsistency
fall/clutter risk
anxiety load
```

These are not automatically facts. They are inference targets.

Correct AI wording:

> “The relocation period may be a multi-factor contributor. Review whether symptoms, medication timing, sleep, dust exposure, oxygen access, or anxiety changed during this window.”

Incorrect AI wording:

> “The move caused the flare.”

---

# 7. Claims Handling

Claims stay in `ledger`.

A claim is any assertion made by:

- doctor,
- nurse,
- EMS,
- patient,
- caregiver,
- discharge paper,
- portal note,
- AI,
- family member.

## Example Doctor Claim

```text
event_type: claim
event_subtype: diagnosis_statement
concept: Anxiety
claim_text: "Anxiety likely contributing to dyspnea."
claim_status: documented
source_id: doctor_note_source_id
```

## Example Discharge Claim

```text
event_type: claim
event_subtype: discharge_status
claim_text: "Stable for discharge."
claim_status: context_limited
source_id: discharge_source_id
```

## Example Caregiver Observation Claim

```text
event_type: claim
event_subtype: caregiver_observation
claim_text: "Symptoms worsen when she talks continuously."
claim_status: observed
concept: Talking continuously
```

The AI should compare claims against:

- ledger events,
- vitals,
- med list,
- care plan,
- relationships,
- later outcomes,
- patient baseline.

---

# 8. Medication Handling

## 8.1 `med_list`

Use for:

- prescribed meds,
- active meds,
- stopped meds,
- PRN meds,
- OTCs,
- supplements,
- oxygen therapy if prescribed,
- recurring medication-like treatments,
- availability at home,
- reconciliation status.

## 8.2 `ledger`

Use for actual behavior:

- taken,
- refused,
- missed,
- delayed,
- vomited,
- unavailable,
- symptom after dose,
- vital change after dose.

## 8.3 `relationships`

Use for medication knowledge:

- may cause,
- may worsen,
- interacts with,
- duplicate effect,
- raises/lowers,
- requires monitoring.

## 8.4 `ai_findings`

Use for medication insight:

- interaction concern,
- med reconciliation issue,
- med timing pattern,
- refused/missed care gap,
- doctor/pharmacist question.

---

# 9. Ingestion Architecture

Ingestion is the primary data-entry mechanism for the system. It must be fast, low-friction, source-linked, and conservative.

Core principle:

> Every input starts as a raw, immutable `sources` record. Structured data is extracted from that source, linked back to it, and committed only with confidence and traceability.

The goal is not perfect automation. The goal is:

```text
upload/paste/speak → source row → structured extraction → smart commit → review exceptions → AI findings
```

The ingestion layer should support:

- typed caregiver notes,
- voice transcripts,
- discharge papers,
- visit summaries,
- medication lists,
- pharmacy labels,
- screenshots,
- photos,
- lab reports,
- portal messages,
- device exports later.

---

## 9.1 Overall Ingestion Flow

Every input should follow this pipeline:

```text
1. Receive input
2. Create `sources` row immediately
3. Parse/clean source text
4. Run structured extraction
5. Match or create concepts
6. Insert ledger events
7. Update med_list if appropriate
8. Update care_plan if appropriate
9. Create ai_runs record
10. Run lightweight post-ingestion analysis
11. Create ai_findings for clear issues
12. Send low-confidence/conflicting items to review
```

The raw input must always be preserved in `sources.raw_text`, `sources.storage_uri`, or both.

---

## 9.2 Source-First Rule

Before extraction, create a `sources` row.

Minimum fields:

```text
source_type
title
source_time
raw_text or storage_uri
processed_status = new
```

After extraction:

```text
processed_status = processed / needs_review / failed / ignored
summary = brief extraction summary
metadata_json = parser/model details, confidence summary, warnings
```

Never delete or overwrite raw source content during extraction.

---

## 9.3 Parsing Strategy

### Text Notes

For typed notes, voice transcripts, or pasted portal text:

```text
raw text → LLM structured extraction
```

### Documents

For PDFs, DOCX, screenshots, or scans:

```text
file upload → storage → parsing/OCR → cleaned Markdown/text → LLM structured extraction
```

Recommended parser stack:

```text
Primary parser: Docling
OCR fallback: Tesseract or Paperless-ngx OCR
Vision fallback: local vision model or API vision model for poor scans/screenshots
```

Recommended local vision models later:

```text
Qwen2-VL
LLaVA
```

Do not block v0 on OCR perfection. Start with pasted text and clean PDFs first.

---

## 9.4 LLM Strategy

Use a local LLM when practical, with API fallback for speed and reliability.

### v0 Recommendation

```text
Primary: OpenAI API for fast structured extraction and analysis
Fallback/Privacy path: Ollama local model
```

### Local Models to Test

```text
qwen2.5:7b
llama3.1:8b
mistral
qwen2.5-coder for development tasks
```

### Extraction Settings

Use deterministic settings:

```text
temperature = 0
structured JSON output required
schema validation required
```

The LLM should output a strict JSON object matching the intake schema. Use Pydantic or equivalent validation before committing rows.

---

## 9.5 Pydantic / Schema Validation Requirement

The extraction layer should validate AI output before database writes.

Minimum logical models:

```text
SourceExtract
ConceptExtract
LedgerEventExtract
MedListUpdateExtract
CarePlanUpdateExtract
RelationshipCandidateExtract
IntakeOutput
```

If validation fails:

```text
sources.processed_status = failed
create ai_findings row if useful: finding_type = missing_data or extraction_failure
store error details in metadata_json
```

Do not insert malformed AI output directly into tables.

---

## 9.6 Every Input Can Become Seven Things

Each input may produce:

1. `sources` row,
2. `concepts` rows if missing,
3. `ledger` rows,
4. `med_list` updates,
5. `care_plan` updates,
6. `relationships` candidates,
7. `ai_findings` for immediate issues.

Examples of immediate issues:

- medication conflict,
- vague discharge instruction,
- missing escalation threshold,
- active med not available at home,
- doctor claim contradicted by later events,
- low-confidence extraction requiring review.

---

## 9.7 Smart Commit Rules

The system should minimize human work without pretending uncertain data is certain.

### Auto-Commit

Auto-commit extracted rows when:

```text
confidence >= 0.85
no medication conflict detected
no major care-plan change detected
concept match is clear
source time is clear or event time is explicit
```

Usually safe to auto-commit:

- normal ledger events,
- vitals with clear values,
- symptoms clearly stated,
- medication taken/refused events,
- simple caregiver observations,
- source-linked doctor claims,
- clearly stated discharge instructions.

### Flag for Review

Flag when:

```text
confidence < 0.75
medication status changes
new high-risk medication appears
new steroid/antibiotic/controlled/sedating med appears
dose/frequency conflict exists
care-plan threshold changes
source conflicts with existing med_list or care_plan
ambiguous dates/times
non-empty uncertainties list
AI inferred something clinically important but weakly supported
```

Use:

```text
sources.processed_status = needs_review
ledger.confidence < 0.75 where applicable
med_list.needs_reconciliation = true where applicable
ai_findings.finding_type = missing_data / med_reconciliation_issue / instruction_gap
```

### Never Auto-Apply Without Review

Do not automatically overwrite:

- active medication status,
- stopped medication status,
- dose/frequency changes,
- emergency thresholds,
- oxygen instructions,
- major diagnosis claims,
- allergies/intolerances.

Instead, create proposed rows/findings and mark review needed.

---

## 9.8 Conflict Detection During Ingestion

Before committing med or care-plan updates, check existing records.

### Medication Conflict Examples

Flag when:

```text
same med exists with different dose
same med exists with different frequency
new discharge med conflicts with bottle/pharmacy record
med marked stopped but new source says active
med appears in home but not in active list
OTC/supplement overlaps with sedating/stimulant effects
```

Create `ai_findings`:

```text
finding_type = med_reconciliation_issue
severity = medium/high depending on risk
status = open
```

### Care Plan Conflict Examples

Flag when:

```text
discharge says follow up but no date/provider
oxygen says "as needed" with no threshold
rescue inhaler instructions lack max daily use
call/ER thresholds missing
plan assumes home equipment that may be unavailable
```

Create `ai_findings`:

```text
finding_type = instruction_gap
```

---

## 9.9 Human Review Queue

The review queue should be exception-only.

A row/item enters review if:

```text
source processed_status = needs_review
ledger confidence < 0.75
med_list needs_reconciliation = true
ai_findings status = open and finding_type in high-priority categories
```

Recommended review view fields:

```text
source title
source raw/parsed text
proposed extracted rows
confidence
conflict reason
approve/edit/reject controls
```

The human must be able to correct:

- wrong concept mapping,
- wrong time,
- wrong dose,
- wrong status,
- bad inference,
- duplicate concept,
- duplicate finding,
- overstated AI conclusion.

Human corrections should be saved and later used as few-shot examples.

---

## 9.10 Few-Shot Learning From Corrections

After a few manual corrections, store examples for prompt injection.

Each example should include:

```text
raw input
incorrect extraction if useful
corrected extraction
notes about why correction was made
```

Use 2–4 patient-specific examples in the intake prompt.

This helps the model learn patient-specific language, such as:

```text
"rescue inhaler" = Albuterol
"hydrox" = Hydroxyzine
"oxygen" may refer to oxygen tank, concentrator, SpO2, or oxygen therapy depending on context
"talking nonstop" = Talking continuously
"can't breathe" = Air hunger/Dyspnea claim, not automatically low SpO2
```

---

## 9.11 Post-Ingestion Automation

After successful ingestion, automatically run lightweight analysis.

Create `ai_runs` record:

```text
analysis_type = intake_extract
model_used = model name
input_summary = source summary
output_summary = extraction summary
```

Then run lightweight scanners:

```text
medication reconciliation scan
context inference scan
truth reconciliation scan if claims were extracted
interaction scan if meds/OTCs/supplements/foods were extracted
```

Create `ai_findings` only when the issue is clear enough to be useful.

Do not flood the findings table with weak speculation.

---

## 9.12 Ingestion Interfaces

### Fastest v0

```text
CLI script + watched folder + pasted text
```

### Recommended v0.1

```text
Simple Streamlit or Gradio app
```

Features:

- text box for messy note,
- file uploader,
- source type selector,
- submit button,
- extraction summary,
- review queue.

### Later

```text
phone voice note → Whisper → same ingestion pipeline
Paperless-ngx consume folder → OCR → same ingestion pipeline
Supabase/NocoDB file upload → same ingestion pipeline
```

---

## 9.13 Edge Cases

### Scanned or Poor Quality Docs

Route to OCR/vision. Mark lower confidence.

### Long Documents

Chunk by clinical sections:

```text
medications
discharge instructions
history
assessment/plan
labs
imaging
follow-up
```

Then reconcile chunk outputs before committing.

### Ambiguous Time

Use null or approximate time with low confidence.

Do not invent precise times.

### Conflicting Sources

Do not overwrite. Insert new source-linked claim/update and create finding.

### Major Clinical Change

Never auto-commit as final truth. Flag for review.

---

## 9.14 Ingestion Rule Summary

```text
Raw source first.
Extract second.
Validate third.
Commit high-confidence rows.
Flag uncertain/conflicting rows.
Link everything to source_id.
Label inference as inference.
Trigger lightweight analysis.
Generate only useful findings.
```

# 10. AI Processing Modules

Implement these as separate functions/scripts. Do not build one giant opaque AI call.

## 10.1 Intake Extractor

Input:

- messy note,
- voice transcript,
- pasted doctor note,
- OCR text,
- manual entry.

Output:

- source,
- concepts,
- ledger events,
- possible med_list updates,
- possible care_plan updates,
- uncertainties.

## 10.2 Medication Reconciliation Scanner

Checks:

- active meds not taken,
- PRN meds repeatedly refused,
- meds found at home but absent from med list,
- doctor list conflicts with pharmacy/bottle,
- duplicate meds,
- stopped meds still used,
- OTC/supplement interactions,
- missing dose/frequency,
- missing max daily dose,
- unclear oxygen/treatment instructions.

## 10.3 Interaction Scanner

Checks:

- drug-drug,
- drug-food,
- drug-condition,
- drug-behavior,
- drug-environment,
- duplicate side effects,
- stimulant load,
- sedation/fall risk,
- glucose elevation,
- HR elevation,
- BP changes,
- respiratory worsening.

## 10.4 Truth Reconciliation Scanner

Compares claims against reality.

Checks:

- doctor claim vs later events,
- discharge instruction vs home feasibility,
- patient statement vs vitals,
- caregiver observation vs repeated data,
- “stable” vs later escalation,
- “noncompliant” vs barriers/refusals/side effects/confusion,
- “normal” vs patient-specific baseline,
- vague instruction vs need for threshold.

## 10.5 Context Inference Scanner

Uses anchor events to infer possible affected domains.

Example:

If `Moving / relocation` exists, check:

- symptoms during move window,
- missed meds,
- sleep changes,
- food changes,
- dust/environment logs,
- oxygen/device access,
- anxiety/HR increase,
- falls/clutter.

## 10.6 Doctor Packet Generator

Produces:

1. main concern,
2. key timeline,
3. medication reconciliation issues,
4. pattern findings,
5. contradictions or unclear claims,
6. missing data,
7. top doctor/pharmacist questions,
8. evidence references,
9. “not a diagnosis” statement.

---

# 11. AI Prompts

## 11.1 Intake Extraction Prompt

```text
You are a clinical data extraction assistant for a private single-patient health ledger.

Convert the messy note into structured data.

Do not diagnose.
Do not treat any source as absolute truth.
Extract events, claims, medication updates, care-plan instructions, and possible concepts.

Important:
- Refused, missed, unavailable, absent, normal, and unclear events matter.
- If an event implies broader context, label that as inference, not fact.
- Preserve exact wording for claims.
- Use approximate time only if clearly inferable; otherwise null.
- Output valid JSON only.

Return:
{
  "source": {
    "source_type": "",
    "title": "",
    "source_time": null,
    "raw_text": ""
  },
  "concepts_to_create": [
    {
      "name": "",
      "type": "",
      "aliases": [],
      "parent_concept_name": null,
      "properties_json": {}
    }
  ],
  "ledger_events": [
    {
      "event_time": null,
      "event_end_time": null,
      "event_type": "",
      "event_subtype": "",
      "concept_name": "",
      "value_numeric": null,
      "value_text": null,
      "unit": null,
      "status": "",
      "severity": "",
      "confidence": 0.0,
      "location_label": null,
      "episode_key": null,
      "claim_text": null,
      "claim_status": null,
      "notes": "",
      "context_json": {}
    }
  ],
  "med_list_updates": [],
  "care_plan_updates": [],
  "relationship_candidates": [],
  "inferred_context_checks": [],
  "uncertainties": []
}
```

## 11.2 Truth Reconciliation Prompt

```text
You are a clinical truth-reconciliation assistant.

You are analyzing one patient.

Your job is not to diagnose. Your job is to compare:
- what was claimed
- what was measured
- what was observed
- what was instructed
- what was actually done
- what changed in the environment/context
- what medications/OTCs/foods/treatments were involved

Treat every doctor note, discharge paper, patient statement, caregiver observation, device reading, and AI inference as evidence with reliability, not automatic truth.

Identify:
1. supported claims
2. contradicted claims
3. incomplete or vague claims
4. stale assumptions
5. missing data
6. medication/treatment issues
7. environmental/context triggers
8. behavior loops
9. care-plan gaps
10. doctor/pharmacist questions

Output valid JSON:
{
  "summary": "",
  "findings": [
    {
      "finding_type": "",
      "title": "",
      "description": "",
      "severity": "",
      "confidence": 0.0,
      "actionability_score": 0.0,
      "priority_score": 0.0,
      "related_ledger_refs": [],
      "related_concept_names": [],
      "doctor_question": "",
      "suggested_next_step": "",
      "evidence": [
        {
          "source": "",
          "reason": ""
        }
      ],
      "missing_data": []
    }
  ]
}
```

## 11.3 Doctor Packet Prompt

```text
You are preparing a clinician-facing summary for one patient.

Do not diagnose.
Do not accuse clinicians.
Do not overstate AI conclusions.

Create a concise doctor-facing packet using the ledger, medication list, care plan, relationships, claims, and AI findings.

Focus on:
- key timeline
- medication reconciliation issues
- repeated patterns
- contradictions or unclear claims
- missing data
- practical questions for doctor/pharmacist
- urgent red flags if present

Use clear clinical wording.
Label all inference as inference.

Output Markdown with these sections:
1. Patient Context
2. Main Concern
3. Relevant Timeline
4. Current Medication / Therapy Questions
5. Patterns Observed
6. Contradictions or Unclear Claims
7. Missing Data
8. Questions for Clinician / Pharmacist
9. Evidence Notes
10. Not a Diagnosis Statement
```

---

# 12. Scoring Rules

Each AI finding should receive:

- `severity`,
- `confidence`,
- `actionability_score`,
- `priority_score`.

## 12.1 Severity Score

```text
urgent = 5
high = 4
medium = 3
low = 2
info = 1
```

## 12.2 Actionability Score

```text
1.0 = clear next action
0.7 = useful doctor/pharmacist question
0.4 = needs more data
0.2 = vague pattern
```

## 12.3 Priority Score

```text
priority_score = severity_score × confidence × actionability_score
```

The system should sort findings by `priority_score` descending.

---

# 13. Same-Day Build Plan

## Phase 1: Database

Create database:

```text
qiclinical
```

Create all 9 tables and indexes.

## Phase 2: Seed Concepts

Seed only high-signal concepts.

### Medications / Therapies

```text
Prednisone
Albuterol
Hydroxyzine
Guaifenesin
Oxygen therapy
Nebulizer treatment
Acetaminophen
Ibuprofen
Diphenhydramine
Caffeine
```

### Vitals

```text
Heart rate
SpO2
Blood pressure systolic
Blood pressure diastolic
Temperature
Blood glucose
Respiratory rate
Weight
```

### Symptoms

```text
Dyspnea
Air hunger
Wheezing
Cough
Congestion
Anxiety
Panic
Tremor
Rash
Dizziness
Confusion
Fatigue
Chest pain
Swelling
Pain
```

### Behavior / Context

```text
Talking continuously
Medication refusal
Missed medication
Poor sleep
Routine disruption
Exertion
Lying flat
Restlessness
Agitation
Symptom checking
```

### Environment / Devices

```text
Moving / relocation
New home environment
Dust
Cold room
Hot room
Humidity
Smoke
Cleaning fumes
Oxygen tank
Oxygen concentrator
Pulse oximeter
BP cuff
Glucose meter
Medication storage change
Oxygen access issue
```

## Phase 3: Quick UI

Use NocoDB or a simple admin UI.

Create views:

```text
Quick Ledger Entry
Medication Reconciliation
Care Plan Review
AI Findings Review
Source Inbox
```

## Phase 4: Scripts

Create these first:

```text
01_create_schema.py
02_seed_concepts.py
03_ingest_note.py
04_analyze_window.py
05_export_doctor_packet.py
```

Later:

```text
06_ingest_document.py
07_med_reconciliation.py
08_context_inference.py
09_update_relationships.py
```

---

# 14. Script Responsibilities

## `01_create_schema.py`

- Connect to Postgres.
- Create extension.
- Create tables.
- Create indexes.
- Safe to rerun if possible.

## `02_seed_concepts.py`

- Insert initial concepts.
- Avoid duplicates by case-insensitive name matching.
- Add aliases.
- Mark as `approved`.

## `03_ingest_note.py`

- Accept raw note from CLI/file/form.
- Insert source row.
- Call LLM extraction.
- Match/create concepts.
- Insert ledger rows.
- Suggest or apply med/care-plan updates.
- Log AI run.

## `04_analyze_window.py`

- Accept time window or episode key.
- Pull ledger, med_list, care_plan, relationships, profile.
- Run truth reconciliation and interaction analysis.
- Insert `ai_findings`.
- Insert AI-derived relationships where appropriate.

## `05_export_doctor_packet.py`

- Pull selected findings and ledger window.
- Produce Markdown.
- Optional PDF later.

---

# 15. Minimum Useful Queries

## 15.1 Last 24 Hours

```sql
SELECT *
FROM ledger
WHERE event_time >= now() - interval '24 hours'
ORDER BY event_time;
```

## 15.2 Events Around High Heart Rate

```sql
SELECT l2.*
FROM ledger l1
JOIN ledger l2
  ON l2.event_time BETWEEN l1.event_time - interval '4 hours'
                       AND l1.event_time + interval '1 hour'
WHERE l1.event_type = 'vital'
  AND l1.value_numeric >= 130
ORDER BY l1.event_time, l2.event_time;
```

## 15.3 Active Medications Needing Reconciliation

```sql
SELECT *
FROM med_list
WHERE status IN ('active', 'unknown', 'needs_reconciliation')
   OR needs_reconciliation = true
ORDER BY med_name;
```

## 15.4 Claims Needing Review

```sql
SELECT *
FROM ledger
WHERE event_type = 'claim'
  AND claim_status IN ('contradicted', 'incomplete', 'unverified', 'context_limited', 'needs_review')
ORDER BY event_time DESC;
```

## 15.5 Highest Priority Findings

```sql
SELECT *
FROM ai_findings
WHERE status = 'open'
ORDER BY priority_score DESC NULLS LAST, created_at DESC;
```

---

# 16. Doctor Packet Format

The doctor packet should be short, structured, and evidence-based.

```text
Clinical Pattern Summary

Patient:
Date range:
Primary concern:

1. Patient Context
2. Key Timeline
3. Current Medication / Therapy Questions
4. Recent Symptoms and Vitals
5. Relevant Environment / Context Changes
6. Patterns Observed
7. Contradictions or Unclear Claims
8. Missing Data
9. Questions for Clinician / Pharmacist
10. Evidence Notes

Note:
This summary identifies patterns and questions for clinician review. It is not a diagnosis.
```

---

# 17. Operational Manual

## 17.1 What to Log

Log anchor events and known specifics.

Good entries:

```text
Started packing for move.
Moved into new home.
Oxygen tank unavailable.
Prednisone taken.
Hydroxyzine refused.
HR 150, SpO2 95.
Talking continuously.
Room dusty.
Patient says she can’t breathe.
Discharge paper says stable.
Doctor said anxiety likely contributing.
```

Do not force the human to log every downstream implication. The AI should infer likely consequence domains and then verify them against later data.

## 17.2 What Not to Do

Do not build a giant form requiring every detail.

Do not require perfect data.

Do not bury everything in JSON.

Do not make the caregiver choose between 100 event types.

Do not let AI findings appear without evidence references.

## 17.3 Human Review Flow

Every AI extraction or finding should be reviewable.

Recommended statuses:

```text
open
reviewed
confirmed
dismissed
needs_more_data
clinician_reviewed
```

The caregiver/operator should be able to correct:

- wrong concept mapping,
- wrong time,
- wrong status,
- wrong inference,
- duplicate finding,
- overstated conclusion.

---

# 18. Development Guardrails

## 18.1 Avoid Table Sprawl

Do not add tables for:

- episodes,
- claims,
- environment,
- finding evidence,
- baselines,
- options,
- dictionaries.

Handle them with existing tables unless repeated pain proves otherwise.

## 18.2 JSONB Rule

Use real columns for frequently queried fields:

- time,
- type,
- concept,
- value,
- unit,
- status,
- severity,
- confidence,
- source,
- episode key,
- claim status,
- location.

Use JSONB only for extras:

- posture,
- oxygen flow,
- device name,
- location details,
- reason refused,
- meal context,
- route details,
- body site,
- original wording.

## 18.3 Inference Rule

Every AI inference must be labeled as inference unless directly supported.

## 18.4 Evidence Rule

Every AI finding should include:

- linked ledger IDs,
- linked concepts,
- linked sources if applicable,
- evidence JSON explaining why.

## 18.5 Single-Patient Rule

Do not add multi-patient complexity unless the project explicitly changes scope.

---

# 19. Recommended Initial Stack

## Storage

- PostgreSQL

## Quick UI

- NocoDB, or
- simple Streamlit/FastAPI admin page

## AI

- OpenAI API for speed in v0,
- Ollama/local LLM later for privacy/offline fallback.

## Document Intake Later

- Paperless-ngx for OCR and document storage.

## Optional Later

- Qdrant for document embeddings,
- Neo4j for graph visualization,
- voice capture UI,
- PDF doctor packet export.

Do not start with Neo4j or a custom mobile app. Start with ledger value.

---

# 20. Final Build Order

1. Create Postgres schema.
2. Seed concepts.
3. Create quick ledger entry UI.
4. Create raw note ingestion.
5. Create AI extraction.
6. Insert structured ledger rows.
7. Build medication reconciliation scanner.
8. Build truth reconciliation scanner.
9. Build context inference scanner.
10. Build doctor packet export.

The first valuable loop is:

```text
messy note → source → ledger → AI findings → doctor questions
```

That is the v0 win.

---

# 21. Final System Identity

This system is:

> A single-patient clinical reality ledger and truth-reconciliation engine.

Its purpose:

```text
Capture what happened.
Preserve where it came from.
Compare reality against medications, claims, care plans, relationships, and baselines.
Infer possible context effects without treating them as fact.
Find contradictions and missing data.
Generate doctor/pharmacist questions.
```

The final operating rule:

> `ledger` records reality over time.  
> `med_list` records medication truth.  
> `care_plan` records intended action.  
> `relationships` connect causes, risks, and patterns.  
> `ai_findings` explain what may be wrong, missing, contradictory, or worth clinician review.  

Build this first. Make it useful before making it pretty.

