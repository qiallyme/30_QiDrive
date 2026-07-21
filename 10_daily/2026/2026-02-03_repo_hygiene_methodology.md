---
layout: page
title: "Repo Hygiene Methodology"
slug: "repo_hygiene_methodology"
created_at: "2026-02-03 05:57:12"
updated_at: "2026-07-18T11:03:13-04:00"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-003.json"
template_key: master-template
date: 2026-02-03
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6981e23b-6f24-832f-a801-e80c4bddc3fc"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Repo Hygiene Methodology

## Overview
- **Date**: 2026-02-03 05:57:12
- **Conversation ID**: `6981e23b-6f24-832f-a801-e80c4bddc3fc`
- **Source**: `Chat-Export-28513-2026/conversations-003.json`

## Chat History

### User
> we need to come up with a methodology for this repos hygiene, proper file names, proper indexing, front matter, orphans, cross references, identify redundancies, contradictions, and get full case context that auto updates master case records to mirror in notion and produce a interactive navigable mind map in 3d, but the number one issue is proper naming and coherence

### Assistant
> Good — you’re aiming at the *right* problem. Tools, maps, and AI don’t fix chaos if the **names lie**. Coherence starts at the filename. Everything else is downstream.
> 
> Below is a **hard-edged, enforceable methodology** you can actually run, not a vibe doc.
> 
> I’m grounding this in what already exists:
> - **MASTER CASE BLUEPRINT & STRATEGY** fileciteturn0file0  
> - **MASTER VIOLATION INVENTORY** fileciteturn0file1  
> - **MASTER CASE ANALYSIS** fileciteturn0file2  
> - **MASTER VALUATION MODEL** fileciteturn0file3  
> 
> Those four are already your **canonical spine**. The repo just hasn’t been forced to obey them yet.
> 
> ---
> 
> # FCFCU Repo Hygiene Methodology  
> **(Coherence First, Automation Second)**
> 
> ## PRIME DIRECTIVE
> > **If a file cannot be uniquely identified, placed, and summarized by name alone, it does not belong in the repo.**
> 
> No exceptions.
> 
> ---
> 
> ## 1. Canonical Naming System (Non-Negotiable)
> 
> ### 1.1 Filename Grammar (REQUIRED)
> Every file name must encode **identity, function, and time**.
> 
> ```
> YYYY-MM-DD__PHASE__DOMAIN__SUBJECT__TYPE__vX.md
> ```
> 
> ### Example (GOOD)
> ```
> 2025-12-10__PHASE_01__JURISDICTION__Service_Defect_Affidavit__DECL__v1.md
> ```
> 
> ### Example (BAD)
> ```
> motion_final_FINAL2_revised.pdf
> ```
> 
> If you can’t tell **what phase**, **what theory**, and **what role** the file plays without opening it → delete or rename.
> 
> ---
> 
> ## 2. Mandatory Front Matter (Machine + Human Readable)
> 
> Every Markdown file **must** begin with this YAML block:
> 
> ```yaml
> case_id: 49D03-2501-MF-002559
> phase: PHASE_01_COURT_RECORD
> domain: jurisdiction | ada | execution | damages | credit | regulators
> document_type: motion | memo | declaration | exhibit | log | analysis
> status: draft | filed | superseded | withdrawn | final
> author: Cody Rice-Velasquez
> version: v1
> canonical: false
> supersedes: []
> related_files: []
> source_of_truth: true
> ```
> 
> ### Rules
> - **Exactly one file per domain can be `canonical: true`**
> - Anything else must reference *that* file
> - If `status: superseded`, it must point to what replaced it
> 
> This alone kills 80% of repo rot.
> 
> ---
> 
> ## 3. Canonical Spine (What Is Allowed to Be “Master”)
> 
> You already have these — formalize them:
> 
> | Domain | Canonical File |
> |------|---------------|
> | Strategy | MASTER_CASE_BLUEPRINT |
> | Violations | MASTER_VIOLATION_INVENTORY |
> | Narrative / Legal | MASTER_CASE_ANALYSIS |
> | Valuation | MASTER_VALUATION_MODEL |
> 
> **Rule:**  
> No other file is allowed to restate these wholesale.  
> They may only **point**, **extract**, or **instantiate**.
> 
> If a document repeats analysis already in a Master → it’s redundant or contradictory by definition.
> 
> ---
> 
> ## 4. Orphan Detection (Automatic Kill List)
> 
> A file is an **orphan** if:
> - It is not referenced by any canonical file **and**
> - It does not reference a canonical file
> 
> ### Orphan Handling Protocol
> - ❌ No silent retention
> - Either:
>   - Merge
>   - Supersede
>   - Archive to `/__graveyard/`
>   - Delete
> 
> Orphans are liability. Judges hate them. So do future-you.
> 
> ---
> 
> ## 5. Redundancy & Contradiction Resolution
> 
> ### 5.1 Redundancy Test
> Ask:
> > “If this file vanished, would any claim, argument, or leverage be lost?”
> 
> If no → **delete or merge**.
> 
> ### 5.2 Contradiction Test
> Contradictions usually hide in:
> - Dates
> - Legal framing (procedural vs constitutional)
> - Tone (advocacy vs record)
> 
> **Rule:**  
> If two files disagree, the **older one is wrong by default** unless explicitly reaffirmed.
> 
> Mark the loser:
> ```yaml
> status: superseded
> supersedes: [older_file.md]
> ```
> 
> ---
> 
> ## 6. Cross-Reference Discipline (No Free-Floating Claims)
> 
> Inside the body of each file, require a **Context Header**:
> 
> ```markdown
> ## Context & Dependency
> This document:
> - Depends on: MASTER_VIOLATION_INVENTORY §I.A
> - Supports: Motion to Vacate (PHASE_01)
> - Does NOT restate: ADA liability analysis
> ```
> 
> If you can’t write this section, the document doesn’t know why it exists.
> 
> ---
> 
> ## 7. Auto-Updating Master Records (Source-of-Truth Rule)
> 
> Only **event-level documents** update masters.
> 
> Example:
> - New service evidence → updates **Violation Inventory**
> - New damage photo → updates **Damages section only**
> - New legal theory → **forbidden** unless added to Strategy Master first
> 
> This prevents theory drift.
> 
> ---
> 
> ## 8. Notion Mirroring (Mirror, Don’t Think)
> 
> Notion is **read-only mirror + navigation layer**.
> 
> Mapping:
> - Database = file index (from YAML)
> - Page = rendered markdown
> - Rollups:
>   - Phase
>   - Domain
>   - Status
>   - Canonical flag
> 
> **Never author in Notion.** That’s how forks happen.
> 
> ---
> 
> ## 9. 3D Mind Map (Last, Not First)
> 
> The 3D map is a **visualization**, not a brain.
> 
> Nodes:
> - Canonical files = anchors
> - Documents = children
> - Violations = edges
> - Phases = layers (Z-axis)
> 
> If naming and references are clean, this generates itself.
> If not, it lies.
> 
> ---
> 
> ## 10. Enforcement Rules (Be Ruthless)
> 
> - ❌ No unnamed drafts
> - ❌ No “final_final”
> - ❌ No duplicated narratives
> - ❌ No emotional journaling in legal domains
> - ✅ One truth per domain
> - ✅ One spine per case
> 
> ---
> 
> ## Bottom Line (Truth Mode)
> 
> You don’t have a tooling problem.  
> You have a **language and authority problem**.
> 
> Once filenames tell the truth:
> - AI can index
> - Notion can mirror
> - Maps can render
> - Attorneys can trust it
> - Judges can follow it
> 
> If you want, next step I can:
> - Draft a **repo linter spec**
> - Produce a **rename map**
> - Or design the **YAML → Notion → graph pipeline**
> 
> But don’t skip the naming pass.  
> That’s where cases either become *inevitable* — or implode.

### User
> flow down, first what are our object or artifacts, we have evidence, docket, exhibits (currated evidence packages), filings (motions, affidavits, reports, etc), orders, financial, harms, violations, damages, etc. we first need to define our objects. everything must fall into one of those bucket no?

### Assistant
> Yes. **Hard yes.**  
> You’re finally cutting to the root instead of rearranging symptoms.
> 
> Before filenames, before front-matter, before Notion, before mind maps — you must define **what *things* exist** in the system. If you don’t, you’ll keep smuggling meaning through filenames and vibes.
> 
> Below is a **clean, minimal, enforceable object model** for *this case*. Not generic. Not academic. Built to survive court, counsel, AI, and time.
> 
> ---
> 
> # FCFCU CASE — CANONICAL OBJECT MODEL  
> *(Everything must be one of these. No hybrids.)*
> 
> ## RULE ZERO (Non-Negotiable)
> > **Every file instantiates exactly ONE object type.**  
> If it feels like two, it’s wrong and must be split.
> 
> ---
> 
> ## 1. PRIMARY OBJECT CLASSES (Top-Level Buckets)
> 
> These are the **only allowed object classes** in the case.
> 
> ```
> 01_EVIDENCE
> 02_DOCKET
> 03_EXHIBITS
> 04_FILINGS
> 05_ORDERS
> 06_FINANCIAL
> 07_HARMS
> 08_VIOLATIONS
> 09_DAMAGES
> 10_ANALYSIS
> 11_STRATEGY
> 12_ADMIN
> ```
> 
> If something doesn’t fit → it doesn’t exist yet or it’s noise.
> 
> ---
> 
> ## 2. OBJECT DEFINITIONS (What Each Thing IS and IS NOT)
> 
> ### 01_EVIDENCE  
> **What it is:**  
> Raw, atomic, unaltered facts.
> 
> **Examples**
> - Photos, videos, audio
> - Emails, texts, letters
> - Utility bills
> - Court screenshots
> - Body cam, Ring cam
> - USPS records
> 
> **Rules**
> - ❌ No commentary
> - ❌ No highlighting
> - ❌ No conclusions
> - ✅ Immutable
> - ✅ Time-stamped
> 
> > Evidence never argues. It just *exists*.
> 
> ---
> 
> ### 02_DOCKET  
> **What it is:**  
> The procedural spine of the case.
> 
> **Examples**
> - Case timeline
> - Filings index
> - Hearing dates
> - Service attempts log
> - Court actions
> 
> **Rules**
> - ✅ Court-verifiable only
> - ❌ No argument
> - ❌ No theory
> 
> > If a judge asked “what happened when,” this is where you point.
> 
> ---
> 
> ### 03_EXHIBITS  
> **What it is:**  
> Curated, labeled groupings of evidence prepared **for use**.
> 
> **Examples**
> - Exhibit A – Service Defect
> - Exhibit B – ADA Notice
> - Exhibit C – Property Damage
> 
> **Rules**
> - ✅ References Evidence IDs
> - ❌ Does NOT alter evidence
> - ❌ Does NOT argue law
> 
> > Exhibits organize evidence. They are not filings.
> 
> ---
> 
> ### 04_FILINGS  
> **What it is:**  
> Anything submitted or prepared for submission to a court or regulator.
> 
> **Examples**
> - Motions
> - Affidavits
> - Declarations
> - Briefs
> - Reports
> - Complaints
> 
> **Rules**
> - ✅ Cites Exhibits
> - ❌ Never cites raw evidence directly
> - ❌ Never invents facts
> 
> > Filings are claims + relief, not proof.
> 
> ---
> 
> ### 05_ORDERS  
> **What it is:**  
> Authoritative rulings or directives issued by a court or agency.
> 
> **Examples**
> - Default judgment
> - Writ of Assistance
> - Denial orders
> - Scheduling orders
> 
> **Rules**
> - ✅ Read-only
> - ❌ No interpretation inside the object
> 
> > Orders speak for themselves. Analysis lives elsewhere.
> 
> ---
> 
> ### 06_FINANCIAL  
> **What it is:**  
> All money-related records **without judgment**.
> 
> **Examples**
> - Mortgage statements
> - Payoff quotes
> - Utility bills
> - Ledger exports
> - Bank statements
> - Sale accounting
> 
> **Rules**
> - ❌ No damages math
> - ❌ No fraud claims
> - ✅ Just numbers + sources
> 
> > Finance is neutral until analyzed.
> 
> ---
> 
> ### 07_HARMS  
> **What it is:**  
> Documented negative impacts experienced.
> 
> **Examples**
> - Homelessness
> - Sleep deprivation
> - Health deterioration
> - Loss of access
> - Safety risk
> 
> **Rules**
> - ❌ No dollar amounts
> - ❌ No legal labels
> - ✅ Factual impact statements
> 
> > Harm ≠ violation ≠ damages.
> 
> ---
> 
> ### 08_VIOLATIONS  
> **What it is:**  
> Alleged breaches of law, duty, or process.
> 
> **Examples**
> - Service defects
> - ADA failures
> - Due process violations
> - Misrepresentations
> - Spoliation risk
> 
> **Rules**
> - ✅ Mapped to evidence
> - ❌ No remedy requests
> - ❌ No valuation
> 
> > Violations answer “what rule was broken.”
> 
> ---
> 
> ### 09_DAMAGES  
> **What it is:**  
> Quantification of harm in monetary or legal terms.
> 
> **Examples**
> - Lost income
> - Property loss
> - Emotional distress valuation
> - Fee exposure
> - Punitive ranges
> 
> **Rules**
> - ✅ Derived from harms + violations
> - ❌ No raw evidence
> - ❌ No legal argument
> 
> > Damages answer “what it costs.”
> 
> ---
> 
> ### 10_ANALYSIS  
> **What it is:**  
> Interpretation, synthesis, and reasoning.
> 
> **Examples**
> - Legal memos
> - Kill-chain analysis
> - Causation mapping
> - Risk analysis
> 
> **Rules**
> - ❌ Never new facts
> - ❌ Never new evidence
> - ✅ Points outward only
> 
> > Analysis explains reality. It doesn’t create it.
> 
> ---
> 
> ### 11_STRATEGY  
> **What it is:**  
> Decision-making, leverage, sequencing.
> 
> **Examples**
> - Phase maps
> - Settlement architecture
> - Regulatory escalation plan
> - Negotiation posture
> 
> **Rules**
> - ❌ Never filed
> - ❌ Never public
> - ✅ Internal only
> 
> > Strategy is for *you*, not the record.
> 
> ---
> 
> ### 12_ADMIN  
> **What it is:**  
> System plumbing.
> 
> **Examples**
> - Naming rules
> - Index schemas
> - Automation scripts
> - Repo hygiene docs
> 
> **Rules**
> - ❌ No case facts
> - ❌ No analysis
> 
> > Admin keeps the machine running.
> 
> ---
> 
> ## 3. FLOW-DOWN LOGIC (This Is the Spine)
> 
> ```
> EVIDENCE
>   ↓
> EXHIBITS
>   ↓
> FILINGS
>   ↓
> ORDERS
> ```
> 
> Parallel tracks:
> ```
> FINANCIAL → DAMAGES
> HARMS → DAMAGES
> VIOLATIONS → FILINGS → DAMAGES
> ```
> 
> Analysis & Strategy **never flow upward** into facts.
> 
> ---
> 
> ## 4. Why This Matters (Truth, No Sugar)
> 
> Right now, your biggest risk is **category leakage**:
> - Evidence files with opinions
> - Filings smuggling analysis
> - Strategy bleeding into public docs
> - Harms mislabeled as damages
> 
> Judges don’t punish mistakes —  
> they punish **confusion**.
> 
> This object model kills confusion at the root.
> 
> ---
> 
> ## Next Steps (Pick One — Don’t Do All)
> 
> 1. I generate a **one-page object decision tree** (“Where does this file go?”)
> 2. I produce a **repo folder skeleton** locked to these objects
> 3. I help you **reclassify one messy folder live** as a pilot
> 4. I write a **linting rule set** that rejects mis-typed files
> 
> Say the word. We build it clean, then we automate.

### User
> ok, well lets keep families together, evidence and exhibits need to be closure, docket filings, orders, motions, reports, damages and harms, financials together, violations, analysis and strategy etc, keep it intuitive and essentially chronological, if you want larger buckets then we add detail we could do, cocurt record, evidence, analysis, strategy, or something,

### Assistant
> Yes — you’re right to **collapse families**. Over-atomizing too early creates fake precision and cognitive drag. What you want is **intuitive containment + strict role boundaries**, then chronological ordering *inside* each family.
> 
> Below is a **clean, court-safe, human-legible hierarchy** that keeps related artifacts together **without blurring object roles**.
> 
> This is the right level to lock in **before** filenames, YAML, or automation.
> 
> ---
> 
> # FCFCU CASE — FAMILY-FIRST OBJECT MODEL  
> *(Chronological, Intuitive, Enforceable)*
> 
> ## TOP-LEVEL PRINCIPLE
> > **Large buckets = how humans think.  
> Internal subtypes = how machines enforce discipline.**
> 
> Everything still has a type — it’s just nested instead of scattered.
> 
> ---
> 
> ## LEVEL 1 — CANONICAL CASE FAMILIES (5 Buckets)
> 
> ```
> 01_COURT_RECORD
> 02_EVIDENCE_RECORD
> 03_HARM_FINANCIAL_RECORD
> 04_VIOLATION_DAMAGE_RECORD
> 05_ANALYSIS_STRATEGY
> 06_ADMIN
> ```
> 
> That’s it.  
> If it doesn’t fit → it’s noise or admin.
> 
> ---
> 
> ## 01_COURT_RECORD  
> **“What the court did and what we filed.”**  
> This is the **procedural spine**.
> 
> ### Contains
> - Docket
> - Filings
> - Motions
> - Affidavits / Declarations
> - Reports submitted to court
> - Orders / Judgments / Writs
> 
> ### Internal Structure (Chronological)
> ```
> 01_COURT_RECORD/
> ├── 2025-01/
> ├── 2025-05/
> ├── 2025-12/
> └── 2026-01/
> ```
> 
> ### Rules
> - ✅ Court-facing only
> - ❌ No raw evidence
> - ❌ No strategy
> - ❌ No emotional narrative
> - ✅ Each filing references Exhibits by ID
> 
> > If a judge asked for “the court record,” this folder stands alone.
> 
> ---
> 
> ## 02_EVIDENCE_RECORD  
> **“What actually exists in the world.”**  
> Immutable facts + curated packages.
> 
> ### Contains
> - Raw evidence
> - Exhibits (curated evidence sets)
> - Media
> - Communications
> - Logs (photos, videos, emails, bills)
> 
> ### Internal Structure
> ```
> 02_EVIDENCE_RECORD/
> ├── 01_RAW_EVIDENCE/
> │   ├── photos/
> │   ├── video/
> │   ├── audio/
> │   ├── documents/
> │
> ├── 02_EXHIBITS/
> │   ├── Exhibit_A_Service/
> │   ├── Exhibit_B_ADA/
> │   ├── Exhibit_C_Property/
> ```
> 
> ### Rules
> - ❌ No legal conclusions
> - ❌ No dollar amounts
> - ❌ No arguments
> - ✅ Raw evidence is immutable
> - ✅ Exhibits reference raw evidence IDs
> 
> > Evidence never argues. Exhibits never opine.
> 
> ---
> 
> ## 03_HARM_FINANCIAL_RECORD  
> **“What it cost and what it caused — without blaming yet.”**
> 
> This is where you smartly keep **financials + harms together**.
> 
> ### Contains
> - Financial records
> - Bills
> - Ledgers
> - Lost income documentation
> - Harm logs (physical, emotional, practical)
> 
> ### Internal Structure
> ```
> 03_HARM_FINANCIAL_RECORD/
> ├── 01_FINANCIALS/
> │   ├── utilities/
> │   ├── mortgage/
> │   ├── sale_accounting/
> │
> ├── 02_HARMS/
> │   ├── displacement/
> │   ├── health/
> │   ├── safety/
> │   ├── professional/
> ```
> 
> ### Rules
> - ❌ No legal labels (“illegal,” “fraud”)
> - ❌ No valuation conclusions
> - ✅ Pure documentation of impact and cost
> 
> > Harm answers *what happened to me*.  
> > Financials answer *what changed numerically*.
> 
> ---
> 
> ## 04_VIOLATION_DAMAGE_RECORD  
> **“What rules were broken and what that’s worth.”**
> 
> This is where **law meets consequence**.
> 
> ### Contains
> - Violations inventory
> - Damages models
> - Exposure calculations
> - Remedy mapping
> 
> ### Internal Structure
> ```
> 04_VIOLATION_DAMAGE_RECORD/
> ├── 01_VIOLATIONS/
> │   ├── jurisdiction/
> │   ├── ada/
> │   ├── due_process/
> │   ├── execution/
> │
> ├── 02_DAMAGES/
> │   ├── economic/
> │   ├── emotional/
> │   ├── statutory/
> │   ├── punitive/
> ```
> 
> ### Rules
> - ✅ Must cite evidence or harms
> - ❌ No new facts
> - ❌ No strategy language
> - ❌ No court filing language unless duplicated elsewhere
> 
> > Violations = what rule broke  
> > Damages = what it costs them
> 
> ---
> 
> ## 05_ANALYSIS_STRATEGY  
> **“What it means and what we do next.”**
> 
> Internal brain. Never raw. Never public.
> 
> ### Contains
> - Legal analysis
> - Kill-chain diagrams
> - Risk assessments
> - Strategy maps
> - Settlement architecture
> - Phase planning
> 
> ### Internal Structure
> ```
> 05_ANALYSIS_STRATEGY/
> ├── 01_ANALYSIS/
> │   ├── jurisdiction_analysis.md
> │   ├── ada_analysis.md
> │
> ├── 02_STRATEGY/
> │   ├── phase_map.md
> │   ├── settlement_models.md
> │   ├── escalation_paths.md
> ```
> 
> ### Rules
> - ❌ Never filed
> - ❌ Never cited directly
> - ✅ Points outward to records
> 
> > This is where thinking lives — not facts.
> 
> ---
> 
> ## 06_ADMIN  
> **“How the system stays clean.”**
> 
> ### Contains
> - Naming rules
> - Index schemas
> - Automation scripts
> - Repo hygiene docs
> - Linting rules
> 
> ---
> 
> ## FLOW CHECK (If You’re Unsure)
> 
> Ask **one** question:
> 
> > “Is this about **what happened**, **what it cost**, **what rule broke**, or **what we do about it**?”
> 
> That tells you the bucket.
> 
> ---
> 
> ## Why This Is the Right Cut (Truth Mode)
> 
> - Chronological ✔  
> - Intuitive ✔  
> - Court-safe ✔  
> - AI-friendly ✔  
> - Human-navigable ✔  
> 
> You’ve avoided the two fatal errors:
> 1. Over-fragmenting objects
> 2. Letting roles bleed
> 
> This structure can scale to:
> - Notion mirrors
> - Graph maps
> - Binder printing
> - Attorney intake
> - Federal complaints
> 
> ---
> 
> ## Next Logical Step (Don’t Skip)
> 
> Pick **one**:
> 1. I draft the **exact folder tree + README for each family**
> 2. We **reclassify one existing messy directory** as a test
> 3. I define the **sub-object metadata schema** (what every file declares)
> 4. I generate the **chronological index template**
> 
> Say which. We lock this, then move *downstream*.

### User
> you can have violation before harm, flip them, anylis before harm, admin is find,

### Assistant
> Good catch — and you’re right.  
> **Causality and cognition both favor that flip.** Violations are the trigger; harms and costs are the downstream effects. Analysis should sit *before* impact so the story flows logically and chronologically.
> 
> Here’s the **corrected, locked hierarchy**, clean and final enough to build on.
> 
> ---
> 
> # FCFCU CASE — CANONICAL FAMILY HIERARCHY (v1 LOCK)
> 
> ## LEVEL 1 — CASE FAMILIES (ORDER MATTERS)
> 
> ```
> 01_COURT_RECORD
> 02_EVIDENCE_RECORD
> 03_VIOLATION_RECORD
> 04_ANALYSIS_STRATEGY
> 05_HARM_FINANCIAL_RECORD
> 06_ADMIN
> ```
> 
> This order now matches:
> - **What happened procedurally**
> - **What exists factually**
> - **What rules were broken**
> - **What it means / what we do**
> - **What it caused / what it cost**
> - **How the system runs**
> 
> ---
> 
> ## 01_COURT_RECORD  
> **Procedural reality. Judge-facing. Chronological.**
> 
> ### Contains
> - Docket
> - Filings (motions, affidavits, reports)
> - Orders (judgments, writs, rulings)
> 
> ### Structure
> ```
> 01_COURT_RECORD/
> ├── 2025-01/
> ├── 2025-05/
> ├── 2025-12/
> └── 2026-01/
> ```
> 
> ### Hard Rules
> - Court-verifiable only
> - No raw evidence
> - No strategy
> - No valuation language
> 
> ---
> 
> ## 02_EVIDENCE_RECORD  
> **Ground truth. Immutable facts + curated packages.**
> 
> ### Contains
> - Raw evidence
> - Exhibits (curated evidence sets)
> - Media, communications, logs
> 
> ### Structure
> ```
> 02_EVIDENCE_RECORD/
> ├── 01_RAW_EVIDENCE/
> │   ├── photos/
> │   ├── video/
> │   ├── audio/
> │   ├── documents/
> │
> ├── 02_EXHIBITS/
> │   ├── Exhibit_A_Service/
> │   ├── Exhibit_B_ADA/
> │   ├── Exhibit_C_Property/
> ```
> 
> ### Hard Rules
> - No opinions
> - No conclusions
> - Raw evidence is immutable
> - Exhibits reference raw evidence IDs only
> 
> ---
> 
> ## 03_VIOLATION_RECORD  
> **Rule breaks. Theory-neutral. Evidence-anchored.**
> 
> ### Contains
> - Jurisdictional violations
> - ADA / Civil rights violations
> - Due process violations
> - Execution / enforcement violations
> - Spoliation risks
> 
> ### Structure
> ```
> 03_VIOLATION_RECORD/
> ├── jurisdiction/
> ├── ada/
> ├── due_process/
> ├── execution/
> └── spoliation/
> ```
> 
> ### Hard Rules
> - Must cite Evidence or Court Record
> - No damages numbers
> - No strategy
> - No emotional narrative
> 
> > This answers: **“What rule was broken?”**
> 
> ---
> 
> ## 04_ANALYSIS_STRATEGY  
> **Meaning, causation, leverage. Internal only.**
> 
> ### Contains
> - Legal analysis
> - Kill-chain diagrams
> - Causation maps
> - Risk and exposure analysis
> - Settlement and escalation strategy
> 
> ### Structure
> ```
> 04_ANALYSIS_STRATEGY/
> ├── 01_ANALYSIS/
> │   ├── jurisdiction_analysis.md
> │   ├── ada_analysis.md
> │   ├── causation_map.md
> │
> ├── 02_STRATEGY/
> │   ├── phase_map.md
> │   ├── settlement_architecture.md
> │   ├── escalation_paths.md
> ```
> 
> ### Hard Rules
> - Never filed
> - Never cited as fact
> - Points outward only
> - No new evidence
> 
> > This answers: **“Why it matters and what we do.”**
> 
> ---
> 
> ## 05_HARM_FINANCIAL_RECORD  
> **Impact and cost. Downstream effects only.**
> 
> ### Contains
> - Harm logs (personal, health, safety, professional)
> - Financial records
> - Damage quantification (if you later want to split, this is where it would branch)
> 
> ### Structure
> ```
> 05_HARM_FINANCIAL_RECORD/
> ├── 01_HARMS/
> │   ├── displacement/
> │   ├── health/
> │   ├── safety/
> │   ├── professional/
> │
> ├── 02_FINANCIALS/
> │   ├── utilities/
> │   ├── mortgage/
> │   ├── sale_accounting/
> │   ├── expenses/
> ```
> 
> ### Hard Rules
> - No legal conclusions
> - No blame language
> - Financials are raw, not argued
> - Harms are factual, not valued (unless explicitly marked)
> 
> > This answers: **“What it caused and what it cost.”**
> 
> ---
> 
> ## 06_ADMIN  
> **System integrity. No case substance.**
> 
> ### Contains
> - Naming conventions
> - Index schemas
> - Automation / lint rules
> - Repo hygiene docs
> - Notion / graph configs
> 
> ---
> 
> ## FLOW VALIDATION (Sanity Check)
> 
> ```
> COURT_RECORD
>    ↓
> EVIDENCE_RECORD
>    ↓
> VIOLATION_RECORD
>    ↓
> ANALYSIS_STRATEGY
>    ↓
> HARM_FINANCIAL_RECORD
> ```
> 
> Nothing flows upward.  
> Nothing skips a layer.
> 
> ---
> 
> ## Why This Version Is Better (Straight Truth)
> 
> - Violations precede harm ✔
> - Analysis precedes valuation ✔
> - Chronology preserved ✔
> - Cognitive load reduced ✔
> - Court-safe separation ✔
> - Scales cleanly to:
>   - Binder tabs
>   - Notion mirrors
>   - Graph maps
>   - Attorney intake
> 
> This is now **structurally correct** — not just tidy.
> 
> ---
> 
> ## Next Move (Choose One)
> 
> 1. Lock this with a **one-page CASE STRUCTURE README**
> 2. Build the **exact folder tree + README stubs**
> 3. Reclassify **one real folder live** to test friction
> 4. Define the **per-file metadata contract** (what every file must declare)
> 
> Say the word. We proceed *downhill only* from here.

### User
> now court record yes just chronological, maybe prefixed date then type like mo, or, fi, ex, ect. evidence yes this is good, split up documents further, violations, keep chronological master then we can currate into the more detailed buckets analysis keep it centered around events and we can currate in strategy, harms and finacial, same keep chronolocial reocrd then we currate into buckets.

### Assistant
> Perfect. What you’re describing is **event-first, curation-second**. That’s the right mental model for litigation and for ADHD-safe coherence.
> 
> Below is the **refined, final methodology**, aligned exactly to what you just said. This is tight, intuitive, and enforceable.
> 
> ---
> 
> # FCFCU CASE — EVENT-FIRST RECORD SYSTEM (LOCKED)
> 
> ## CORE DESIGN RULE
> > **Chronology is the source of truth.  
> Curation is a view, not a rewrite.**
> 
> Every major family has:
> 1. **A single chronological master record**
> 2. **Optional curated sub-buckets derived from it**
> 
> No parallel truths.
> 
> ---
> 
> ## 01_COURT_RECORD  
> **Pure procedural chronology. No theory. No sorting by type.**
> 
> ### Naming Convention (Required)
> ```
> YYYY-MM-DD__CR__<TYPE>__<Short_Descriptor>.pdf|md
> ```
> 
> ### Type Codes (short + obvious)
> - `MO` – Motion  
> - `FI` – Filing / Brief  
> - `OR` – Order  
> - `JD` – Judgment  
> - `WR` – Writ  
> - `NT` – Notice  
> - `RP` – Court Report / Transcript  
> 
> ### Example
> ```
> 2025-05-28__CR__JD__Default_Judgment.pdf
> 2025-12-10__CR__MO__Motion_to_Vacate.md
> 2026-01-09__CR__OR__Order_Denying_Vacatur.pdf
> ```
> 
> ### Structure
> ```
> 01_COURT_RECORD/
> ├── 2025-01/
> ├── 2025-05/
> ├── 2025-12/
> └── 2026-01/
> ```
> 
> ### Rules
> - Chronological only
> - No evidence stored here
> - No analysis
> - This folder alone can be handed to a judge
> 
> ---
> 
> ## 02_EVIDENCE_RECORD  
> **Ground truth. Split early. Stay raw.**
> 
> ### Structure
> ```
> 02_EVIDENCE_RECORD/
> ├── 01_RAW/
> │   ├── documents/
> │   │   ├── letters/
> │   │   ├── emails/
> │   │   ├── bills/
> │   │   ├── court_docs/
> │   │
> │   ├── photos/
> │   ├── video/
> │   ├── audio/
> │   └── screenshots/
> │
> ├── 02_EXHIBITS/
> │   ├── Exhibit_A_Service/
> │   ├── Exhibit_B_ADA/
> │   ├── Exhibit_C_Property/
> ```
> 
> ### Naming Convention
> ```
> YYYY-MM-DD__EV__<SOURCE>__<Descriptor>.<ext>
> ```
> 
> ### Rules
> - Raw evidence is immutable
> - Exhibits only reference raw evidence
> - No conclusions, no highlights, no opinions
> 
> ---
> 
> ## 03_VIOLATION_RECORD  
> **Chronological master first. Buckets later.**
> 
> ### Master Record (Authoritative)
> ```
> 03_VIOLATION_RECORD/
> ├── MASTER_VIOLATION_TIMELINE.md
> ```
> 
> This is **strictly chronological**, event-by-event:
> - Date
> - What rule was violated
> - Evidence pointer(s)
> - Court record pointer(s)
> 
> No sorting here.
> 
> ### Curated Views (Derived, Optional)
> ```
> 03_VIOLATION_RECORD/
> ├── by_type/
> │   ├── jurisdiction/
> │   ├── ada/
> │   ├── due_process/
> │   ├── execution/
> ```
> 
> ### Rules
> - Master timeline is the source of truth
> - Curated folders never add facts
> - Curated folders only link back to master entries
> 
> ---
> 
> ## 04_ANALYSIS_STRATEGY  
> **Event-centered analysis. Strategy is a lens, not a timeline.**
> 
> ### Structure
> ```
> 04_ANALYSIS_STRATEGY/
> ├── 01_EVENT_ANALYSIS/
> │   ├── 2025-05-28_default_analysis.md
> │   ├── 2025-12-09_removal_analysis.md
> │
> ├── 02_STRATEGY/
> │   ├── phase_map.md
> │   ├── settlement_architecture.md
> │   ├── escalation_paths.md
> ```
> 
> ### Rules
> - Analysis files anchor to **specific events**
> - Strategy files synthesize analysis
> - No new facts introduced
> - Never filed, never public
> 
> ---
> 
> ## 05_HARM_FINANCIAL_RECORD  
> **Chronological impact first, categories second.**
> 
> ### Master Record
> ```
> 05_HARM_FINANCIAL_RECORD/
> ├── MASTER_IMPACT_TIMELINE.md
> ```
> 
> Each entry:
> - Date
> - Event causing impact
> - Harm experienced
> - Financial effect (if known)
> - Evidence reference
> 
> ### Curated Buckets (Derived)
> ```
> 05_HARM_FINANCIAL_RECORD/
> ├── harms/
> │   ├── displacement/
> │   ├── health/
> │   ├── safety/
> │   ├── professional/
> │
> ├── financials/
> │   ├── utilities/
> │   ├── mortgage/
> │   ├── expenses/
> │   ├── lost_income/
> ```
> 
> ### Rules
> - Master timeline is authoritative
> - Buckets are views, not sources
> - No legal conclusions
> - No blame language
> 
> ---
> 
> ## 06_ADMIN  
> Unchanged. System-only.
> 
> ---
> 
> ## WHY THIS WORKS (No Fluff)
> 
> - **Chronology prevents contradiction**
> - **Curation prevents overwhelm**
> - **Masters prevent forked truth**
> - **Buckets support attorneys, judges, and AI**
> - **You can always rebuild views from masters**
> 
> This is how real litigation teams keep cases straight over *years*.
> 
> ---
> 
> ## NEXT STEP (DO NOT SKIP)
> 
> You now need to lock **three master files**:
> 
> 1. `MASTER_VIOLATION_TIMELINE.md`
> 2. `MASTER_IMPACT_TIMELINE.md`
> 3. `COURT_RECORD_INDEX.md` (auto-generated later)
> 
> If you want, next I can:
> - Draft the **exact template** for those masters
> - Help you **migrate one real month** as a test
> - Define the **metadata header** each entry uses
> - Design the **auto-curation logic** (Notion + graph)
> 
> Say which one.

### User
> admin is case management this is folder 00, try to apply this methodology to our current phases.

### Assistant
> Got it. Let’s **apply**, not redesign.
> 
> Below is your **phase-aligned, event-first structure**, with **Case Management as 00**, and everything else mapped cleanly to the **actual phases you’re already running**. This keeps continuity with your existing work while enforcing the new methodology.
> 
> No fluff. This is executable.
> 
> ---
> 
> # FCFCU CASE — PHASE-MAPPED STRUCTURE (APPLIED)
> 
> ## 00_CASE_MANAGEMENT  *(Admin / Control Plane)*
> 
> **Purpose:** run the case, not argue it.
> 
> ```
> 00_CASE_MANAGEMENT/
> ├── README.md
> ├── case_profile.yaml
> ├── naming_conventions.md
> ├── index_registry.md
> ├── automation/
> ├── notion_mapping/
> ├── graph_config/
> └── audits/
> ```
> 
> **Contains**
> - Case metadata
> - Phase definitions
> - Indexes
> - Automation / lint rules
> - Repo hygiene
> 
> ❌ No facts  
> ❌ No evidence  
> ❌ No analysis  
> 
> ---
> 
> ## PHASE_01 — COURT RECORD (Procedural Spine)
> 
> ### Folder
> ```
> 01_COURT_RECORD/
> ```
> 
> ### Structure (pure chronology)
> ```
> 01_COURT_RECORD/
> ├── 2025-01/
> ├── 2025-05/
> ├── 2025-12/
> └── 2026-01/
> ```
> 
> ### Naming (locked)
> ```
> YYYY-MM-DD__CR__<TYPE>__<Descriptor>.<ext>
> ```
> 
> **Type Codes**
> - `MO` motion  
> - `FI` filing / brief  
> - `OR` order  
> - `JD` judgment  
> - `WR` writ  
> - `NT` notice  
> 
> **Examples**
> ```
> 2025-05-28__CR__JD__Default_Judgment.pdf
> 2025-12-10__CR__MO__Motion_to_Vacate.md
> 2026-01-09__CR__OR__Order_Denying_Vacatur.pdf
> ```
> 
> **Rules**
> - Chronological only
> - Court-facing only
> - No evidence stored here
> - No analysis, no strategy
> 
> ➡ This *is* the court’s view of the case.
> 
> ---
> 
> ## PHASE_02 — EVIDENCE RECORD (Ground Truth)
> 
> ### Folder
> ```
> 02_EVIDENCE_RECORD/
> ```
> 
> ### Structure
> ```
> 02_EVIDENCE_RECORD/
> ├── 01_RAW/
> │   ├── documents/
> │   │   ├── letters/
> │   │   ├── emails/
> │   │   ├── bills/
> │   │   ├── court_docs/
> │   │
> │   ├── photos/
> │   ├── video/
> │   ├── audio/
> │   └── screenshots/
> │
> ├── 02_EXHIBITS/
> │   ├── Exhibit_A_Service/
> │   ├── Exhibit_B_ADA/
> │   ├── Exhibit_C_Property/
> ```
> 
> ### Naming
> ```
> YYYY-MM-DD__EV__<SOURCE>__<Descriptor>.<ext>
> ```
> 
> **Rules**
> - Raw evidence immutable
> - Exhibits = curated references only
> - No opinions, no conclusions
> 
> ➡ This is the factual universe. Nothing else gets to invent facts.
> 
> ---
> 
> ## PHASE_03 — VIOLATION RECORD (Rule Breaks)
> 
> ### Folder
> ```
> 03_VIOLATION_RECORD/
> ```
> 
> ### Master (authoritative)
> ```
> 03_VIOLATION_RECORD/
> ├── MASTER_VIOLATION_TIMELINE.md
> ```
> 
> **Format:** strictly chronological  
> Each entry:
> - Date
> - Event
> - Rule violated
> - Evidence pointer(s)
> - Court record pointer(s)
> 
> ### Curated Views (derived only)
> ```
> 03_VIOLATION_RECORD/
> ├── by_type/
> │   ├── jurisdiction/
> │   ├── ada/
> │   ├── due_process/
> │   ├── execution/
> ```
> 
> **Rules**
> - Master timeline is source of truth
> - Buckets never add facts
> - No damages, no strategy
> 
> ➡ Answers: **“What rule was broken, when.”**
> 
> ---
> 
> ## PHASE_04 — ANALYSIS & STRATEGY (Internal Brain)
> 
> ### Folder
> ```
> 04_ANALYSIS_STRATEGY/
> ```
> 
> ### Structure
> ```
> 04_ANALYSIS_STRATEGY/
> ├── 01_EVENT_ANALYSIS/
> │   ├── 2025-05-28_default_judgment.md
> │   ├── 2025-12-09_removal.md
> │
> ├── 02_STRATEGY/
> │   ├── phase_map.md
> │   ├── settlement_architecture.md
> │   ├── escalation_paths.md
> ```
> 
> **Rules**
> - Analysis is **event-anchored**
> - Strategy synthesizes analysis
> - No new facts
> - Never filed, never public
> 
> ➡ Answers: **“Why it matters and what we do.”**
> 
> ---
> 
> ## PHASE_05 — HARM & FINANCIAL RECORD (Impact)
> 
> ### Folder
> ```
> 05_HARM_FINANCIAL_RECORD/
> ```
> 
> ### Master (authoritative)
> ```
> 05_HARM_FINANCIAL_RECORD/
> ├── MASTER_IMPACT_TIMELINE.md
> ```
> 
> Each entry:
> - Date
> - Triggering event
> - Harm experienced
> - Financial effect (if known)
> - Evidence pointer
> 
> ### Curated Views
> ```
> 05_HARM_FINANCIAL_RECORD/
> ├── harms/
> │   ├── displacement/
> │   ├── health/
> │   ├── safety/
> │   ├── professional/
> │
> ├── financials/
> │   ├── utilities/
> │   ├── mortgage/
> │   ├── expenses/
> │   ├── lost_income/
> ```
> 
> **Rules**
> - Master timeline is truth
> - Buckets are views
> - No legal conclusions
> - No blame language
> 
> ➡ Answers: **“What it caused and what it cost.”**
> 
> ---
> 
> ## PHASE FLOW (FINAL, CORRECT)
> 
> ```
> 00_CASE_MANAGEMENT
>    ↓
> 01_COURT_RECORD
>    ↓
> 02_EVIDENCE_RECORD
>    ↓
> 03_VIOLATION_RECORD
>    ↓
> 04_ANALYSIS_STRATEGY
>    ↓
> 05_HARM_FINANCIAL_RECORD
> ```
> 
> Nothing jumps phases.  
> Nothing flows backward.
> 
> ---
> 
> ## WHAT THIS UNLOCKS (REAL BENEFITS)
> 
> - You can **rebuild any view** from masters
> - No contradictions across filings
> - Attorneys can onboard in hours, not weeks
> - Judges get clean narratives
> - AI / Notion / graphs become *truthful mirrors*
> - You stop re-litigating your own facts
> 
> ---
> 
> ## NEXT (Pick One, We Execute)
> 
> 1. Draft the **three master templates** (violation, impact, court index)
> 2. Apply this to **December 2025 only** as a pilot
> 3. Generate a **migration checklist** from your current repo
> 4. Write the **lint rules** that enforce this automatically
> 
> Say which. This structure is now solid enough to build on.

### User
> close but it should be case management is the source of truth, case master that houses, summary, timeline, violations, analysis stregey, tasks, decisions, ect, then our evidence, exhibits, and trackers then in each phase this is where the work is done, drafting, creating, filing, then will role up into the case manager to create the full coherent case file as phases are locked.

### Assistant
> Yes. **That’s the correct inversion.**  
> You’re describing a **hub-and-spoke case system**, where **Case Management is the authoritative brain**, and phases are **workspaces**, not truth stores.
> 
> Let me lock this cleanly and apply your methodology precisely.
> 
> ---
> 
> # FCFCU CASE — HUB-AND-PHASE CASE SYSTEM (FINAL)
> 
> ## CORE AXIOM (THIS IS THE KEY)
> > **Only ONE place is allowed to speak in a unified voice.**  
> That place is **Case Management (00)**.
> 
> Everything else:
> - produces inputs  
> - does work  
> - drafts artifacts  
> - captures raw facts  
> 
> …but **does not define the case**.
> 
> ---
> 
> ## 00_CASE_MANAGEMENT — **SOURCE OF TRUTH (THE HUB)**
> 
> This folder is **the case**, not a bucket.
> 
> ### Purpose
> - Canonical truth
> - Coherent narrative
> - Locked decisions
> - Phase roll-ups
> - What an attorney, judge, or regulator ultimately reads
> 
> ### Structure
> ```
> 00_CASE_MANAGEMENT/
> ├── CASE_MASTER.md              ← single authoritative case file
> ├── CASE_SUMMARY.md             ← executive summary (living)
> ├── CASE_TIMELINE.md            ← master chronology (events only)
> ├── CASE_VIOLATIONS.md          ← consolidated violations (locked)
> ├── CASE_ANALYSIS.md            ← consolidated legal analysis
> ├── CASE_STRATEGY.md            ← consolidated strategy (internal)
> ├── CASE_TASKS.md               ← active / completed tasks
> ├── CASE_DECISIONS.md           ← decisions + rationale
> ├── PHASE_STATUS.md             ← phase lock state
> ├── INDEX.md                    ← navigation + pointers
> └── audits/
> ```
> 
> ### Rules (Non-Negotiable)
> - ✅ This is the **only place** allowed to synthesize
> - ✅ Content here is curated, deliberate, and minimal
> - ❌ No drafting chaos
> - ❌ No raw evidence
> - ❌ No speculative notes
> 
> > If something is “true,” it lives here **after** review.
> 
> ---
> 
> ## 01_EVIDENCE_EXHIBITS_TRACKERS — **FACT INPUTS**
> 
> This is the **fact reservoir**, not the story.
> 
> ```
> 01_EVIDENCE_EXHIBITS_TRACKERS/
> ├── 01_EVIDENCE/
> │   ├── raw/
> │   └── logs/
> │
> ├── 02_EXHIBITS/
> │
> ├── 03_TRACKERS/
> │   ├── service_tracker.md
> │   ├── access_tracker.md
> │   ├── credit_reporting_tracker.md
> │   └── retrieval_tracker.md
> ```
> 
> ### Rules
> - Raw evidence immutable
> - Exhibits are curated packages
> - Trackers log facts, not conclusions
> - Nothing here “decides” anything
> 
> > This feeds Case Management. It never replaces it.
> 
> ---
> 
> ## 02_PHASE_WORK — **WHERE WORK HAPPENS**
> 
> Each phase is a **workspace**, not a record of truth.
> 
> ### Structure
> ```
> 02_PHASE_WORK/
> ├── PHASE_01_COURT_RECORD/
> ├── PHASE_02_CREDIT_FCRA/
> ├── PHASE_03_REGULATORS/
> ├── PHASE_04_LITIGATION/
> ├── PHASE_05_PUBLIC_PRESSURE/
> ```
> 
> Inside **each phase**:
> 
> ```
> PHASE_X/
> ├── 01_DRAFTS/
> ├── 02_WORKING_NOTES/
> ├── 03_SUPPORTING_EVIDENCE/
> ├── 04_FILED_FINAL/
> └── README.md
> ```
> 
> ### Rules
> - Draft freely here
> - Iterate here
> - Argue here
> - Experiment here
> - ❌ Nothing here is “final truth” by default
> 
> ---
> 
> ## PHASE → CASE ROLL-UP MECHANISM (CRITICAL)
> 
> ### Phase Lock Rule
> When a phase artifact is:
> - filed, **or**
> - relied upon, **or**
> - used externally
> 
> …it must be **rolled up** into Case Management.
> 
> ### Roll-Up Process (Explicit)
> 1. Phase artifact finalized
> 2. Extract:
>    - event(s)
>    - violations
>    - outcomes
>    - decisions
> 3. Update:
>    - `CASE_TIMELINE.md`
>    - `CASE_VIOLATIONS.md`
>    - `CASE_ANALYSIS.md`
>    - `CASE_STRATEGY.md` (if internal)
> 4. Mark phase item as **LOCKED**
> 
> > Phases generate.  
> > Case Management canonizes.
> 
> ---
> 
> ## FLOW OF AUTHORITY (THIS PREVENTS CHAOS)
> 
> ```
> EVIDENCE / TRACKERS
>         ↓
> PHASE WORK (drafting, filings, actions)
>         ↓
> CASE MANAGEMENT (truth, coherence, strategy)
> ```
> 
> Nothing flows upward without review.  
> Nothing bypasses Case Management.
> 
> ---
> 
> ## WHY THIS IS THE RIGHT SYSTEM (NO BS)
> 
> - You stop re-explaining your own case
> - You eliminate contradictions automatically
> - You can hand **00_CASE_MANAGEMENT** to:
>   - an attorney
>   - a regulator
>   - a judge
> - You can nuke or archive entire phases without losing truth
> - ADHD-safe: one brain, many workbenches
> 
> This is **how serious litigation teams actually operate**, just usually hidden behind SharePoint hell.
> 
> ---
> 
> ## NEXT STEP (ONLY ONE)
> 
> To move forward cleanly, the **next action must be**:
> 
> 1. Draft the **CASE_MASTER.md skeleton** (headings only), **or**
> 2. Define the **roll-up checklist** (what gets extracted from phases), **or**
> 3. Apply this model to **one real phase** (PHASE_01) as a pilot
> 
> Say which.  
> Once Case Management is shaped, everything else snaps into place.

### User
> see our current directory and let me know what you think should be the final final final, lol ```markdown

> . 📂 content

> └── 📂 00_CASE_MANAGEMENT/

> │  └── 📂 10_Case_Master/

> │    ├── 📄 01_CASE_BIBLE.md

> │    ├── 📄 02_TIMELINE.md

> │    ├── 📄 02_TIMELINE.mw

> │    ├── 📄 03_VIOLATIONS.md

> │    ├── 📄 04_STRATEGY.canvas

> │    ├── 📄 05_VALUATION.md

> │    ├── 📄 06_MASTER_TASKLIST.md

> │    ├── 📄 09_DECISION_MATRIX.canvas

> │    ├── 📄 STRATEGY_MEMO_Judicial_Inconsistency_and_Eviction.md

> │    ├── 📄 STRATEGY_MEMO_Value_Gap_and_Spoliation.md

> │  └── 📂 20_evidence/

> │    └── 📂 10_Docket/

> │      ├── 📄 001_2025-01-16_Complaint.pdf

> │      ├── 📄 002_2025-01-16_Appearance.pdf

> │      ├── 📄 003_2025-01-16_Request_for_Admissions.pdf

> │      ├── 📄 004_2025-01-16_Notice_to_Homeowners.pdf

> │      ├── 📄 005_2025-01-16_Appearance_2.pdf

> │      ├── 📄 006_2025-01-16_Summons_1.pdf

> │      ├── 📄 007_2025-01-16_Summons_2.pdf

> │      ├── 📄 008_2025-01-16_Summons_3.pdf

> │      ├── 📄 009_2025-01-16_Summons_4.pdf

> │      ├── 📄 010_2025-01-16_Summons_5.pdf

> │      ├── 📄 011_2025-03-05_Service_Returned_Served.pdf

> │      ├── 📄 012_2025-04-15_Service_Returned_Served.pdf

> │      ├── 📄 013_2025-05-13_Motion_for_Default_Judgment.pdf

> │      ├── 📄 014_2025-05-13_Affidavit.pdf

> │      ├── 📄 015_2025-05-13_Affidavit_Attorney_Fees.pdf

> │      ├── 📄 016_2025-05-21_Order_Denying_Default.pdf

> │      ├── 📄 017_2025-05-21_Notice_Omitted_Service.pdf

> │      ├── 📄 018_2025-05-23_Motion_Amended_Default_1.pdf

> │      ├── 📄 019_2025-05-23_Motion_Amended_Default_2.pdf

> │      ├── 📄 020_2025-05-23_Order_Default_Judgment.pdf

> │      ├── 📄 021_2025-05-30_Praecipe_Sheriff_Sale_1.pdf

> │      ├── 📄 022_2025-05-30_Praecipe_Sheriff_Sale_2.pdf

> │      ├── 📄 023_2025-07-09_Service_Returned_Served_Sheriff.pdf

> │      ├── 📄 024_2025-07-17_Notice_Plaintiffs_Bid.pdf

> │      ├── 📄 025_2025-09-09_Decree_Foreclosure_Returned.pdf

> │      ├── 📄 026_2025-10-29_Petition_Writ_of_Assistance.pdf

> │      ├── 📄 027_2025-10-29_Writ_of_Assistance_Document.pdf

> │      ├── 📄 028_2025-11-06_Order_Writ_of_Assistance.pdf

> │      ├── 📄 029_2025-12-10_motion_vacate.pdf

> │      ├── 📄 030_2025-12-11_Motion_Vacate_Judgment.pdf

> │      ├── 📄 031_2025-12-11_Exhibit_List_A-G.pdf

> │      ├── 📄 032_2025-12-11_Denial_stay_writ.pdf

> │      ├── 📄 033_2025-12-11_Hearing_Set_Proposed_Order_Vacate.pdf

> │      ├── 📄 034_2025-12-11_Supplemental_Emergency_Motion.pdf

> │      ├── 📄 035_2025-12-11_Proposed_Order_Stay.pdf

> │      ├── 📄 036_2025-12-12_Report_to_Court.pdf

> │      ├── 📄 037_2025-12-12_Supplemental_Emergency_Motion.pdf

> │      ├── 📄 038_2025-12-16_Emergency_Supplemental_Declaration.pdf

> │      ├── 📄 039_2025-12-17_Report_Sheriff_Sale_No_Excess.pdf

> │      ├── 📄 040_2025-12-22_ADA_Disability_Affidavit.pdf

> │      ├── 📄 041_2026-01-09_Appearance_Plaintiff.pdf

> │      ├── 📄 042_2025-01-20_Order_from_1_9_26_hearing.pdf

> │      ├── 📄 043_2025-12-22_Declaration_Ongoing_D.pdf

> │      ├── 📄 044_2025-12-10_Exhibit_G1_ADA_Notice.pdf

> │      ├── 📄 045_2025-12-10_Exhibit_F_Affidavit.pdf

> │      ├── 📄 046_2025-12-10_Exhibit_H_Declaration.pdf

> │      ├── 📄 047_2025-12-10_Exhibit_G2_AES_ADA_Disconnects.pdf

> │      ├── 📄 048_2025-12-10_Combined_Exhibits_A-H.pdf

> │      ├── 📄 049_2025-05-21_Omitted_Notice_of_Service_Report.pdf

> │      ├── 📄 2025_05_13_14_52_56.pdf.pdf

> │      ├── 📄 2025_05_13_14_53_36.pdf.pdf

> │      ├── 📄 2025_05_13_14_54_31.pdf.pdf

> │      ├── 📄 _10_Docket.md

> │    └── 📂 20_Actors/

> │      └── 📂 10_fcfcu/

> │        └── 📂 Appraisal/

> │          ├── 📄 21June-24-4817Shadow_Appraisal.pdf

> │          ├── 📄 _Appraisal.md

> │        └── 📂 Emails/

> │          ├── 📄 2024-12-09_outgoing_email_bank_access_request.pdf

> │          ├── 📄 2024-12-11_outgoing_email_bank_access_request.pdf

> │          ├── 📄 FCFCU_v_CR-V_Report_to_Court.pdf

> │          ├── 📄 _Emails.md

> │        └── 📂 Letters/

> │          ├── 📄 2023-09-20_FCFCU_Hardship_Health_Notice_Delivery.md

> │          ├── 📄 2023-09-20_FCFCU_Hardship_and_Health_Notice_Le.pdf

> │          ├── 📄 2024-03-20_FCFCU_Certified_Response_Tax_Record.pdf

> │          ├── 📄 2024-06-24_FCFCU_Past_Due_Letter.jpg

> │          ├── 📄 2025-12-20_EXH-30_fcfcu_ac6eb2ea_2025-12-20_EX.jpg

> │          ├── 📄 Formal_Retrieval_Protocol_ADA.md

> │          ├── 📄 _Letters.md

> │        └── 📂 Payments/

> │          ├── 📄 2025-12-20_EXH-20_payments_c5131deb_2025-12-20.png

> │          ├── 📄 _Payments.md

> │        └── 📂 Reports/

> │          ├── 📄 REPORT_TO_COURT_ON_DEFENDANTS_REQUEST.pdf

> │          ├── 📄 _Reports.md

> │        └── 📂 Site_Content/

> │          ├── 📄 About Financial Center - Financial Center.mhtml

> │          ├── 📄 Careers & Culture - Financial Center.pdf

> │          ├── 📄 Credit Union vs. Bank - Financial Center.mhtml

> │          ├── 📄 Financial Center Announces CEO Retirement and Appointment of Interim Leadership - Financial Center.mhtml

> │          ├── 📄 Financial Center Celebrates Laura Mirabal’s Selection to the 2025 Indiana Latino Leadership Circle - Financial Center.mhtml

> │          ├── 📄 Financial Center Completes Merger with Indianapolis Post Office Credit Union - Financial Center.mhtml

> │          ├── 📄 Financial Center Expands to Hancock County with $1.5M McCordsville Branch - Financial Center.mhtml

> │          ├── 📄 Financial Center First Credit Union Selects Ning Duong as New CEO - Financial Center.mhtml

> │          ├── 📄 Financial Center First Credit Union and Indianapolis Post Office Credit Union Announce Plans to Merge - Financial Center.mhtml

> │          ├── 📄 Financial Center Leads the Way in AI-Powered Translations with New Traduality Partnership - Financial Center.mhtml

> │          ├── 📄 Financial Center Recognized with 2025 MeridianLink Arc Award for Impactful Use of Technology in Financial Services - Financial Center.mhtml

> │          ├── 📄 Financial Center and Indianapolis Post Office Credit Union to Merge May 1 - Financial Center.mhtml

> │          ├── 📄 Financial_Center_-_Home_Equity_Line_of_Credit.pdf

> │          ├── 📄 Financial_Center_-_Home_Equity_Loan.pdf

> │          ├── 📄 Home Equity Loans & Lines of Credit - Financial Center.mhtml

> │          ├── 📄 Mortgage_-_Common_Mistakes.pdf

> │          ├── 📄 Mortgage_-_Refinancing.pdf

> │          ├── 📄 Mortgages - Financial Center.mhtml

> │          ├── 📄 News Releases - Financial Center.mhtml

> │          ├── 📄 News Releases - Financial Center.pdf

> │          ├── 📄 Open Positions - Financial Center.pdf

> │          ├── 📄 Privacy Policy - Financial Center.mhtml

> │        ├── 📄 _10_fcfcu.md

> │      └── 📂 20_aes/

> │        ├── 📄 2025-06-08_AES_ADA_Notice.pdf

> │        ├── 📄 2025-12-16_AES_Emergency_Notice.md

> │        ├── 📄 _20_aes.md

> │      └── 📂 30_Sherrif/

> │      └── 📂 40_Others/

> │        ├── 📄 Manager_Response_Acknowledge_Form-1769543600128.pdf

> │      ├── 📄 _20_actors.md

> │    └── 📂 30_Supporting/

> │      └── 📂 10_photos_video/

> │        ├── 📄 2025-12-20_EXH-10_photos_video_00241326_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_012aa06e_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_01b3e905_2025-1.png

> │        ├── 📄 2025-12-20_EXH-10_photos_video_10f4975d_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_1a80b987_2025-1.mp4

> │        ├── 📄 2025-12-20_EXH-10_photos_video_1beefb11_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_1f3f8a81_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_25fb1992_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_2f0952db_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_49c74ec6_2025-.heic

> │        ├── 📄 2025-12-20_EXH-10_photos_video_4e01fa01_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_5be451ba_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_5d95cae5_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_61129253_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_63fb7b02_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_71c9e6a7_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_78ba1ccc_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_7a544ef7_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_8350e7be_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_8a163413_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_8d885a5c_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_942cfd7f_2025-1.png

> │        ├── 📄 2025-12-20_EXH-10_photos_video_9b611100_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_9fb3a08a_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_9ff5022d_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_a8832e17_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_ca02d006_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_db9b10b5_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_e4cb3622_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_ebaaa38d_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_ed6dc885_2025-1.mp4

> │        ├── 📄 2025-12-20_EXH-10_photos_video_f510498b_2025-.heic

> │        ├── 📄 2025-12-20_EXH-10_photos_video_f60d8098_2025-1.png

> │        ├── 📄 2025-12-20_EXH-10_photos_video_f98b089a_2025-1.png

> │        ├── 📄 2025-12-20_EXH-10_photos_video_fa1703bf_2025-1.jpg

> │        ├── 📄 2025-12-20_EXH-10_photos_video_fdd8d4ef_2025-1.jpg

> │        ├── 📄 7345FF5F-1928-4EF9-A63F-99C02D4020A2.jpeg

> │        ├── 📄 NT_Video_Narration_Log_Removal_Day.md

> │        ├── 📄 _10_photos_video.md

> │      └── 📂 20_parcel/

> │        ├── 📄 DLGF_ Tax Bill Search.pdf

> │        ├── 📄 Marion County, IN, Estimated 2025 Taxes 6016506.pdf

> │        ├── 📄 MyTitle.pdf

> │        ├── 📄 Parcel_6016506_PRC 1.pdf

> │        ├── 📄 Parcel_6016506_PRC.pdf

> │        ├── 📄 Parcel_6016506_ParcelDetailHistory 1.pdf

> │        ├── 📄 Parcel_6016506_ParcelDetailHistory.pdf

> │        ├── 📄 _20_parcel.md

> │        ├── 📄 f588fab6-f89f-41c3-bfce-05ad0d108a06.pdf

> │        ├── 📄 indy_pvdnet_document (1).pdf

> │        ├── 📄 indy_pvdnet_document.pdf

> │      └── 📂 30_declarations/

> │        ├── 📄 _30_declarations.md

> │      └── 📂 40_affidavits/

> │        ├── 📄 _40_affidavits.md

> │        └── 📂 ada-disability/

> │          ├── 📄 _ada-disability.md

> │        └── 📂 character/

> │          ├── 📄 _character.md

> │        └── 📂 community-service/

> │          ├── 📄 _community-service.md

> │        └── 📂 credibility/

> │          ├── 📄 _credibility.md

> │        └── 📂 observations/

> │          ├── 📄 _observations.md

> │      └── 📂 50_records/

> │        └── 📂 bankruptcy/

> │          ├── 📄 2025-12-20_EXH-20_receipts_0860d3df_2025-12-20.jpg

> │      └── 📂 60_credit/

> │        ├── 📄 Chase Credit Journey - Credit report.pdf

> │        ├── 📄 Chase Credit Journey.pdf

> │        ├── 📄 Credit Report.pdf

> │      └── 📂 70_Financial/

> │        ├── 📄 50100846854.pdf

> │        ├── 📄 50100879809.pdf

> │        ├── 📄 50100883027.pdf

> │        ├── 📄 50100916138.pdf

> │        ├── 📄 Invoice.pdf

> │        ├── 📄 Invoice2.pdf

> │        ├── 📄 Invoice3.pdf

> │        ├── 📄 Invoice4.pdf

> │      ├── 📄 _30_supporting.md

> │    └── 📂 40_Exposure_and_Harm/

> │      ├── 📄 EXPOSURE_CONSEQUENTIAL_CONSOLIDATED.md

> │      ├── 📄 EXPOSURE_ECONOMIC_CONSOLIDATED.md

> │      ├── 📄 EXPOSURE_MISC_STRATEGY_CONSOLIDATED.md

> │      ├── 📄 EXPOSURE_NON_ECONOMIC_CONSOLIDATED.md

> │      ├── 📄 _40_Exposure_and_Harm.md

> │      └── 📂 _archive/

> │        └── 📂 20_economic_harm/

> │          └── 📂 10_property_possession_harms/

> │            ├── 📄 _10_property_possession_harms.md

> │          └── 📂 30_financial/

> │            ├── 📄 NT_Financial_Tracker.md

> │            ├── 📄 NT_Payment_Portal_and_Check_History.md

> │            ├── 📄 _30_financial.md

> │          └── 📂 60_professional_harm/

> │            ├── 📄 _60_professional_harm.md

> │          ├── 📄 Declaration_Secondary_Displacement_Otis.md

> │          ├── 📄 Emergency_Supplemental_Declaration_Consolidated.md

> │          ├── 📄 NT_2025-12-21_Gigi_Escape_Displacement_Safety_Event.md

> │          ├── 📄 NT_Forced_Relocation_Market_Loss_Memo.md

> │          ├── 📄 NT_Post_Removal_Artifact_Checklist.md

> │          ├── 📄 NT_Quarantined_Claims_Hold.md

> │          ├── 📄 Supplemental_Declaration_Accounting_Surplus.md

> │          ├── 📄 Supplemental_Declaration_Cody_DRAFT.md

> │          ├── 📄 _20_economic_harm.md

> │        └── 📂 50_non_economic_harm/

> │          └── 📂 40_health_and_safety/

> │            └── 📂 20_companion_animal_risk/

> │              ├── 📄 _20_companion_animal_risk.md

> │            ├── 📄 _40_health_and_safety.md

> │          └── 📂 Photos_Conditions/

> │            ├── 📄 _Photos_Conditions.md

> │          └── 📂 Weather_Reports/

> │            ├── 📄 Cold_Risk_Report.md

> │            ├── 📄 _Weather_Reports.md

> │          ├── 📄 _50_non_economic_harm.md

> │          └── 📂 cold_exposure/

> │            ├── 📄 PL__Cold_Risk_Report.md

> │            ├── 📄 _cold_exposure.md

> │        └── 📂 60_Consequential_Damages/

> │          └── 📂 Hotel_Mitigation/

> │            └── 📂 10_Service_Animal_Notice/

> │              ├── 📄 Gigi_Documentation_Pack.md

> │              ├── 📄 Gigi_Service_Dog_Training_Manual.md

> │              ├── 📄 _10_Service_Animal_Notice.md

> │            └── 📂 20_Habitability/

> │              ├── 📄 Demand_Notice_and_Ledger.md

> │              ├── 📄 Room_Conditions_Factual_Log.md

> │              ├── 📄 _20_Habitability.md

> │            ├── 📄 MITIGATION_LOG_Temporary_Housing.md

> │            ├── 📄 README_Temporary_Housing_Mitigation.md

> │            ├── 📄 _Hotel_Mitigation.md

> │          ├── 📄 _60_Consequential_Damages.md

> │        └── 📂 70_remedies_scenarios/

> │          ├── 📄 _70_remedies_scenarios.md

> │        └── 📂 80_payout_strategy/

> │          ├── 📄 NT__Long_Term_Payout_Strategy.md

> │          ├── 📄 _80_payout_strategy.md

> │        └── 📂 90_third_party_harm/

> │          ├── 📄 _90_third_party_harm.md

> │    └── 📂 60_Service_and_delivery/

> │      └── 📂 Email_Transmittals/

> │        ├── 📄 README.md

> │        ├── 📄 _Email_Transmittals.md

> │      ├── 📄 Service_Log.md

> │      └── 📂 USPS_Certified/

> │        ├── 📄 README.md

> │        ├── 📄 _USPS_Certified.md

> │      ├── 📄 _60_service_and_delivery.md

> │    ├── 📄 _20_evidence.md

> │  └── 📂 30_Trackers/

> │    ├── 📄 MASTER_LEDGER.csv

> │    ├── 📄 _30_Trackers.md

> │    ├── 📄 audit_report.txt

> │    ├── 📄 authority.csv

> │    ├── 📄 docket.csv

> │    ├── 📄 financial.csv

> │    ├── 📄 notionseed.csv

> │    ├── 📄 repo_index.csv

> │    ├── 📄 strategy.csv

> │    ├── 📄 tasks.csv

> │    ├── 📄 violations.csv

> │  └── 📂 99_Templates/

> │    └── 📂 10_motions/

> │      ├── 📄 _10_motions.md

> │      ├── 📄 _emergency_stay_of_writ.md

> │      ├── 📄 _vacate_void_judgment.md

> │    └── 📂 20_affidavits/

> │      ├── 📄 TPL_Affidavit_ADA_Disability.md

> │      ├── 📄 TPL_Affidavit_Character.md

> │      ├── 📄 TPL_Affidavit_Community_Service.md

> │      ├── 📄 TPL_Affidavit_Credibility.md

> │      ├── 📄 TPL_Affidavit_Language_Updates.md

> │      ├── 📄 TPL_Affidavit_Observations.md

> │      ├── 📄 TPL_Affidavit_Verified_Defendant.md

> │      ├── 📄 TPL_Declaration_Gender_Identity_Clarification.md

> │      ├── 📄 _20_affidavits.md

> │      ├── 📄 _GUIDE_Witness_Instructions.md

> │    └── 📂 40_exhibits/

> │      ├── 📄 _40_exhibits.md

> │      ├── 📄 _Exhibits_Lists.md

> │    └── 📂 50_orders/

> │      ├── 📄 _50_orders.md

> │      ├── 📄 _Proposed_Order.md

> │      ├── 📄 _proposed_order_emergency_stay.md

> │      ├── 📄 _proposed_order_motion_to_vacate.md

> │    └── 📂 60_packets/

> │      ├── 📄 2026-01-19_attorney_intake_packet_executive.md

> │      ├── 📄 TPL_ADA_Packet.md

> │      ├── 📄 TPL_Handup_Packet_Note.md

> │      ├── 📄 _60_packets.md

> │    └── 📂 70_outreach/

> │      ├── 📄 TPL_Advocate_Outreach.md

> │      ├── 📄 TPL_Attorney_Brief.md

> │      ├── 📄 _70_outreach.md

> │    └── 📂 80_binders/

> │      ├── 📄 TPL_Binder_Section_Cover.md

> │      ├── 📄 TPL_Binder_Section_Index.md

> │      ├── 📄 _80_binders.md

> │    └── 📂 90_internal/

> │      ├── 📄 _Court_Doc.md

> │      ├── 📄 _settlement_letter_draft.md

> │    ├── 📄 GEMINI_PROMPT_Phase_Alignment.md

> │  ├── 📄 MASTER_PHASE_00_NOTION_IMPORT.csv

> │  ├── 📄 PHASE_00_Case_Management.md

> └── 📂 01_PHASE_FORECLOSURE.CLOSED/

> │  └── 📂 10_proposed/

> │    ├── 📄 _10_proposed.md

> │  └── 📂 30_motions/

> │    ├── 📄 MO_01_motion_vacate.pdf

> │    ├── 📄 MO_02_emergency_motion_quash_stay.pdf

> │    ├── 📄 MO_motion_emergency_stay_of_writ.md

> │    ├── 📄 MO_motion_emergency_supplemental_motion_ongoing_ha.md

> │    ├── 📄 MO_motion_to_vacate_void_judgment.md

> │    ├── 📄 MO_proposed_order_motion_to_vacate.md

> │    ├── 📄 _30_motions.md

> │  └── 📂 40_orders/

> │    ├── 📄 OR_03_order_vacate_proposed.pdf

> │    ├── 📄 OR_04_order_stay_writ_proposed.pdf

> │    ├── 📄 _40_orders.md

> │  └── 📂 70_hearings/

> │    └── 📂 2026-01-09_void_judgment_hearing/

> │      └── 📂 2025-01-09_hearing/

> │        ├── 📄 COURT_MODE_BUTTONS.md

> │        ├── 📄 HEARING_Cheat_Sheet.md

> │        ├── 📄 _COURT_MODE_PLAYBOOK.md

> │        ├── 📄 _Hearing_Packet_2026-01-09.md

> │      ├── 📄 BINDER_1_USER_COPY_PRINT_ME.pdf

> │      ├── 📄 BINDER_2_JUDGE_COPY_PRINT_ME.pdf

> │      ├── 📄 BINDER_3_OPPOSING_COPY_PRINT_ME.pdf

> │      ├── 📄 COMPLETE_COURT_BINDER_PRINT_ME.pdf

> │      ├── 📄 _Hearing_Void_Judgment_2026-01-09.md

> │  └── 📂 90_Filed_Envelopes/

> │    └── 📂 10_2025-12-10_motion_vacate/

> │      ├── 📄 ENV_37288599_Odyssey_Envelope_Receipt.pdf

> │      ├── 📄 ENV_Odyssey_Envelope_Receipt.pdf

> │      ├── 📄 _10_2025-12-10_motion_vacate.md

> │      ├── 📄 combinepdf.pdf

> │    └── 📂 20_2025-12-11_Supplemental_Emergency_Motion_Access/

> │      ├── 📄 MO_Supplemental_Emergency_Motion.pdf

> │      ├── 📄 _20_2025-12-11_Supplemental_Emergency_Motion_Access.md

> │    ├── 📄 _90_Filed_Envelopes.md

> │  ├── 📄 MASTER_PHASE_01_NOTION_IMPORT.csv

> └── 📂 02_PHASE_PRESERVATION/

> │  └── 📂 10_overview/

> │    ├── 📄 Master_Exhibit_Index.md

> │    ├── 📄 Notion_Project_Management_Sync.md

> │    ├── 📄 PHASE_02_Overview_Master.md

> │  └── 📂 20_ledgers/

> │    ├── 📄 _20_ledgers.md

> │    ├── 📄 harms.csv

> │    ├── 📄 spoliation_risk_ledger.md

> │  └── 📂 30_output/

> │    └── 📂 10_letters/

> │      ├── 📄 2026-02-01_Signed_Notice_of_Preservation_of_Evidence_and_Litigation_Hold.pdf

> │      ├── 📄 2026-02-03_Second_Notice_Cover_Letter.html

> │      ├── 📄 Litigation_Hold_FollowUp.html

> │      ├── 📄 _10_letters.md

> │    └── 📂 20_Emails/

> │      ├── 📄 Gmail - TIME-SENSITIVE NOTICE _ Service by Email Confirmed on Record-2.pdf

> │      ├── 📄 Gmail - TIME-SENSITIVE NOTICE _ Service by Email Confirmed on Record.pdf

> │      ├── 📄 _20_Emails.md

> │    └── 📂 30_Packet/

> │      ├── 📄 2026-02-03_Invoice_Certified_Mail_Evidence_Preservation_FCFCU_LetterStream.pdf

> │      ├── 📄 2026-02-03_Invoice_First_Class_Mail_Evidence_Preservation_FCFCU_LetterStream.pdf

> │      ├── 📄 2026-02-03_Notice_of_Evidence_Preservation_and_Litigation_Hold_FCFCU_FINAL-First_Class.pdf

> │      ├── 📄 2026-02-03_Notice_of_Evidence_Preservation_and_Litigation_Hold_FCFCU_FINAL.pdf

> │      ├── 📄 2026-02-03_Payment_Receipt_LetterStream_Evidence_Preservation_FCFCU.pdf

> │      ├── 📄 _30_Packet.md

> │    ├── 📄 _30_output.md

> │  └── 📂 40_Responses/

> │    ├── 📄 2026-02-01_Automatic_Reply_Email_Receipt_Marion_County_Sheriff_Evidence_Preservation.pdf

> │    ├── 📄 _40_Responses.md

> │  ├── 📄 MASTER_PHASE_02_NOTION_IMPORT.csv

> │  ├── 📄 PHASE_02_Preservation.md

> └── 📂 03_PHASE_CREDIT_FCRA/

> │  └── 📂 00_send_queue/

> │    ├── 📄 Execution_Checklist.md

> │    ├── 📄 MASTER_EXECUTION_CHECKLIST.md

> │    ├── 📄 PHASE_CREDIT_EXECUTION_MAP.md

> │    ├── 📄 _00_send_queue.md

> │  └── 📂 10_credit_reports/

> │    └── 📂 Equifax/

> │      ├── 📄 1990-05-18_FORMAL DISPUTE OF INACCURATE REPORTING Copy.pdf

> │      ├── 📄 Call Customer Care.pdf

> │      ├── 📄 Equifax_dispute_letter.html

> │      ├── 📄 README.md

> │      ├── 📄 _Equifax.md

> │      ├── 📄 identity_verification_bank_statement_old-national.jpg

> │      ├── 📄 identity_verification_drivers_license.jpeg

> │    └── 📂 Experian/

> │      ├── 📄 Experian - Access your credit report--2.pdf

> │      ├── 📄 Experian - Access your credit report-CH13.pdf

> │      ├── 📄 Experian - Access your credit report.pdf

> │      ├── 📄 Experian - Dispute Cart.pdf

> │      ├── 📄 Experian - Dispute Cart2.pdf

> │      ├── 📄 README.md

> │      ├── 📄 _Experian.md

> │    ├── 📄 FCFCU_Late_Reporting_Evidence_2026.txt

> │    ├── 📄 MANIFEST_Credit_Bureau_Dispute_Packet.md

> │    └── 📂 Other/

> │      ├── 📄 README.md

> │      ├── 📄 _Other.md

> │    └── 📂 TransUnion/

> │      ├── 📄 Gmail - Dispute Received, Investigation in Process.pdf

> │      ├── 📄 README.md

> │      ├── 📄 _TransUnion.md

> │    ├── 📄 _10_credit_reports.md

> │  └── 📂 20_furnisher_disputes/

> │    ├── 📄 13312462_invoice.pdf

> │    ├── 📄 13312462_tmp (1).pdf

> │    ├── 📄 13312462_tmp.pdf

> │    ├── 📄 13312465_invoice.pdf

> │    ├── 📄 13312465_tmp.pdf

> │    ├── 📄 2026-02-03_BASIS OF DISPUTE (NON-CURABLE DEFECTS).pdf

> │    ├── 📄 2026-02-03_FCFCU_Furnisher_Deletion_Demand_FINAL.html

> │    ├── 📄 CFPB_Complaint_Draft.md

> │    ├── 📄 _20_furnisher_disputes.md

> │  └── 📂 30_bureau_disputes/

> │    ├── 📄 2026-02-02_Equifax_Dispute_Letter.html

> │    ├── 📄 2026-02-02_Experian_Dispute_Letter.html

> │    ├── 📄 2026-02-02_TransUnion_Dispute_Letter.html

> │    ├── 📄 Consumer_Statement_Landlords.md

> │    ├── 📄 Equifax_Dispute_Letter.md

> │    ├── 📄 Experian_Dispute_Letter.md

> │    ├── 📄 TransUnion_Dispute_Letter.md

> │    ├── 📄 _30_bureau_disputes.md

> │    ├── 📄 equifax.html

> │    ├── 📄 experian.html

> │    ├── 📄 transunion.html

> │  └── 📂 35_Court_Records/

> │    ├── 📄 4-018222 - Circuit and Superior Courts of Marion County, Indiana.mhtml

> │    ├── 📄 Estimate_4-018222.pdf

> │    ├── 📄 MarionCountyAudioRequestAuthorization_20260203_49D03-2501-MF-002559.pdf

> │    ├── 📄 Your order has been submitted successfully.pdf

> │    ├── 📄 request for recording.pdf

> │  └── 📂 40_utilities/

> │    ├── 📄 2026-02-03_AES_Utility_Dispute.html

> │    ├── 📄 2026-02-03_Citizens_Utility_Dispute.html

> │    ├── 📄 2026-02-03_Code_Enforcement_Dispute.html

> │    └── 📂 AES/

> │      ├── 📄 AESIndiana (1).pdf

> │      ├── 📄 AESIndiana.pdf

> │      ├── 📄 Utility Dispute (AES Indiana) - Cody Rice-Velasquez.pdf

> │      ├── 📄 Utility Dispute (Citizens Water) - Cody Rice-Velasquez.pdf

> │      ├── 📄 Utility Dispute (Code Enforcement) - Cody Rice-Velasquez.pdf

> │      ├── 📄 activity.txt

> │    ├── 📄 _40_utilities.md

> │  └── 📂 50_output/

> │    └── 📂 30_affidavits/

> │      ├── 📄 exhibit_b_harm_addendum 1.html

> │      ├── 📄 exhibit_b_harm_addendum.html

> │      ├── 📄 exhibit_c_affidavit_emergency 1.html

> │      ├── 📄 exhibit_c_affidavit_emergency.html

> │      ├── 📄 index.html

> │    └── 📂 40_packets/

> │      ├── 📄 13312381_invoice.pdf

> │      ├── 📄 13312381_tmp.pdf

> │      ├── 📄 DL_REDACTED.jpg

> │      ├── 📄 PROOF_OF_ADDRESS.pdf

> │      ├── 📄 Phase_01_5_Preservation_Packet_Cover_Sheet.md

> │      ├── 📄 _40_packets.md

> │      ├── 📄 identity_verification_letter_mission-lane-cc.pdf

> │    └── 📂 50_verified_responses/

> │      ├── 📄 _40_verified_responses.md

> │    ├── 📄 CFPB_Escalation_Packet_DRAFT.md

> │    ├── 📄 Credit_Dispute_Master_Packet_Index.html

> │    ├── 📄 Equifax_Violation_Excerpt.md

> │    ├── 📄 Experian_Violation_Excerpt.md

> │    ├── 📄 Landlord_Explanation_Letter.html

> │    ├── 📄 Landlord_Statement.html

> │    ├── 📄 MANIFEST_PHASE_03_SENDS.md

> │    ├── 📄 TransUnion_Violation_Excerpt.md

> │    ├── 📄 _50_output.md

> │  └── 📂 70_damages/

> │    ├── 📄 Consumer_Statement_Short.txt

> │    ├── 📄 Core_Credit_Tables.md

> │    ├── 📄 Emergency_Credit_Harm_Addendum.md

> │    ├── 📄 Housing_Emergency_Affidavit.html

> │    ├── 📄 Landlord_Clarification_Statement.html

> │    ├── 📄 Sanctions_Readiness_Memo.md

> │    ├── 📄 _50_damages.md

> │    ├── 📄 _70_damages.md

> │    ├── 📄 draft_housing_affidavit.md

> │  ├── 📄 MASTER_PHASE_03_NOTION_IMPORT.csv

> │  ├── 📄 PHASE_03_Credit_FCRA.md

> └── 📂 04_PHASE_REGULATORS/

> │  ├── 📄 00_COMPLAINT_PACKET_CHECKLIST.md

> │  └── 📂 10_Industry/

> │    └── 📂 BBB/

> │      ├── 📄 BBB_Complaint_Narrative.md

> │      ├── 📄 BBB_Violation_Excerpt.md

> │      ├── 📄 Cover_Letter.md

> │      ├── 📄 Exhibit_Manifest.md

> │      ├── 📄 _BBB.md

> │    ├── 📄 _10_Industry.md

> │  └── 📂 20_Local/

> │    └── 📂 35_Sheriff_Oversight/

> │      ├── 📄 Cover_Letter.md

> │      ├── 📄 MANIFEST_Sheriff_Oversight_Packet.md

> │      ├── 📄 Marion_County_Sheriff_Oversight_Violation_Excerpt.md

> │      ├── 📄 Sheriff_Internal_Affairs_Complaint.md

> │      ├── 📄 Sheriff_Violation_Excerpt.md

> │      ├── 📄 _35_Sheriff_Oversight.md

> │    ├── 📄 AES_Utility_Violation_Excerpt.md

> │    ├── 📄 Citizens_Utility_Violation_Excerpt.md

> │    ├── 📄 City_of_Indy_Violation_Excerpt.md

> │    ├── 📄 _20_Local.md

> │  └── 📂 30_State/

> │    └── 📂 20_AG_Indiana/

> │      ├── 📄 Cover_Letter.md

> │      ├── 📄 IN_AG_Violation_Excerpt.md

> │      ├── 📄 Indiana_AG_Complaint_Narrative.md

> │      ├── 📄 MANIFEST_IN_AG_Complaint_Packet.md

> │      ├── 📄 _20_AG_Indiana.md

> │    └── 📂 25_IN_DFI/

> │      ├── 📄 Cover_Letter.md

> │      ├── 📄 IN_DFI_Violation_Excerpt.md

> │      ├── 📄 Indiana_DFI_Complaint_Narrative.md

> │      ├── 📄 Indiana_Department_of_Financial_Institutions_DFI_Violation_Excerpt.md

> │      ├── 📄 MANIFEST_Indiana_DFI_Packet.md

> │      ├── 📄 _25_IN_DFI.md

> │    └── 📂 55_IN_Civil_Rights/

> │      ├── 📄 Cover_Letter.md

> │      ├── 📄 ICRC_Violation_Excerpt.md

> │      ├── 📄 Indiana_Civil_Rights_Commission_Violation_Excerpt.md

> │      ├── 📄 Indiana_Civil_Rights_Complaint_Narrative.md

> │      ├── 📄 MANIFEST_ICRC_Complaint_Packet.md

> │      ├── 📄 _55_IN_Civil_Rights.md

> │    ├── 📄 _30_State.md

> │  └── 📂 40_Federal/

> │    └── 📂 20_CFPB/

> │      ├── 📄 CFPB_Complaint_Narrative.md

> │      ├── 📄 CFPB_Violation_Excerpt.md

> │      ├── 📄 CFPB_Violation_Excerpt_Master.md

> │      ├── 📄 Cover_Letter.md

> │      ├── 📄 _20_CFPB.md

> │    └── 📂 30_NCUA/

> │      ├── 📄 Cover_Letter.md

> │      ├── 📄 Exhibit_Manifest.md

> │      ├── 📄 MANIFEST_NCUA_Complaint_Packet.md

> │      ├── 📄 NCUA_Complaint_Narrative.md

> │      ├── 📄 NCUA_Violation_Excerpt.md

> │      ├── 📄 _30_NCUA.md

> │      └── 📂 _archive/

> │        ├── 📄 NCUA_Complaint_Narrative_draft_old.md

> │        ├── 📄 __archive.md

> │    └── 📂 40_DOJ_Civil_Rights/

> │      ├── 📄 Cover_Letter_DOJ_Supplemental.md

> │      ├── 📄 DOJ_Civil_Rights_Violation_Excerpt.md

> │      ├── 📄 DOJ_Civil_Rights_Violation_Excerpt_Master.md

> │      ├── 📄 DOJ_Supplemental_Continuing_Harm.md

> │      ├── 📄 DOJ_Violation_Excerpt.md

> │      ├── 📄 _40_DOJ_Civil_Rights.md

> │    └── 📂 50_HUD_FHEO/

> │      ├── 📄 Cover_Letter.md

> │      ├── 📄 HUD_FHEO_Complaint_Narrative.md

> │      ├── 📄 HUD_FHEO_Violation_Excerpt.md

> │      ├── 📄 MANIFEST_HUD_FHEO_Complaint_Packet.md

> │      ├── 📄 _50_HUD_FHEO.md

> │      └── 📂 _archive/

> │        ├── 📄 HUD_Violation_Excerpt_OLD.md

> │        ├── 📄 __archive.md

> │    ├── 📄 _40_Federal.md

> │  └── 📂 50_Other/

> │    └── 📂 60_CMS_Caretaker_Impact/

> │      ├── 📄 CMS_Informational_Complaint.md

> │      ├── 📄 _60_CMS_Caretaker_Impact.md

> │    ├── 📄 _50_Other.md

> │  └── 📂 50_regulators/

> │    ├── 📄 cms_ssa_caretaker.html

> │    ├── 📄 dfi_servicing_complaint.html

> │    ├── 📄 doj_supplemental.html

> │    ├── 📄 fcc_harassment.html

> │    ├── 📄 hud_fheo_narrative.html

> │    ├── 📄 icrc_civil_rights.html

> │    ├── 📄 index.html

> │    ├── 📄 master_strategic_timeline.html

> │    ├── 📄 master_violation_inventory.html

> │    ├── 📄 ncua_complaint.html

> │    ├── 📄 sheriff_internal_affairs.html

> │    ├── 📄 va_informational.html

> │  └── 📂 99_Reserve_Informational/

> │    └── 📂 45_FCC_Telecom/

> │      ├── 📄 Cover_Letter.md

> │      ├── 📄 FCC_Harassment_Complaint.md

> │      ├── 📄 FCC_Violation_Excerpt.md

> │      ├── 📄 _45_FCC_Telecom.md

> │    └── 📂 65_SSA_OIG/

> │      ├── 📄 SSA_OIG_Informational_Filing.md

> │      ├── 📄 _65_SSA_OIG.md

> │    └── 📂 70_VA_Informational/

> │      ├── 📄 VA_Informational_Filing.md

> │      ├── 📄 _70_VA_Informational.md

> │    ├── 📄 _99_Reserve_Informational.md

> │  ├── 📄 MANIFEST_Reserve_Informational_Filings.md

> │  ├── 📄 MASTER_PHASE_04_NOTION_IMPORT.csv

> │  ├── 📄 PHASE_04_Regulators.md

> │  ├── 📄 Violation_to_Regulator_Mapping.md

> │  ├── 📄 _04_REGULATORS.md

> └── 📂 05_PHASE_LITIGATION/

> │  └── 📂 00_Intake/

> │    ├── 📄 Litigation_Decision_Tree.md

> │    ├── 📄 Master_Timeline_Strategy_Summary.md

> │    ├── 📄 NT_Attorney_Intake_Packet_Executive.md

> │    ├── 📄 NT_Attorney_Intake_Summary.md

> │    ├── 📄 NT_Forensic_Accounting_Audit_Summary.md

> │    ├── 📄 _00_Intake.md

> │    └── 📂 _archive/

> │      ├── 📄 NT_Damages_Matrix_Ab_Initio.md

> │      ├── 📄 NT_INTERNAL VALUATION MEMO.md

> │      ├── 📄 NT_LEGAL MEMORANDUM.md

> │      ├── 📄 NT_Monetary_Exposure_Estimate.md

> │      ├── 📄 NT_Procedural_failure_map_one_pager.md

> │      ├── 📄 NT_Violation_Remedy_Inventory.md

> │      ├── 📄 __archive.md

> │  └── 📂 30_demand_letters/

> │    ├── 📄 NT_Demand_Ready_Exposure_Summary.md

> │    ├── 📄 Notice_of_Evidence_Preservation.md

> │    ├── 📄 _30_demand_letters.md

> │  └── 📂 40_opposing_counsel/

> │    ├── 📄 _40_opposing_counsel.md

> │  └── 📂 50_draft_pleadings/

> │    ├── 📄 _50_draft_pleadings.md

> │  └── 📂 60_output/

> │    └── 📂 10_filings/

> │      ├── 📄 _10_filings.md

> │    └── 📂 20_orders/

> │      ├── 📄 _20_orders.md

> │    └── 📂 30_packets/

> │      ├── 📄 _30_packets.md

> │    └── 📂 40_motions/

> │      ├── 📄 _40_motions.md

> │    └── 📂 50_letters/

> │      ├── 📄 _50_letters.md

> │    ├── 📄 _60_output.md

> │  └── 📂 70_hearings/

> │    ├── 📄 _70_hearings.md

> │  ├── 📄 MASTER_PHASE_05_NOTION_IMPORT.csv

> │  ├── 📄 PHASE_05_Litigation.md

> └── 📂 06_PHASE_MEDIA_INQUIRIES/

> │  └── 📂 10_inbox/

> │    ├── 📄 2025-12-15_displacement_cold_exposure.md

> │  └── 📂 20_social_media/

> │  └── 📂 30_legislative_outreach/

> │  └── 📂 40_public_record_dumps/

> │  └── 📂 50_press_kits/

> │  └── 📂 60_news_media/

> │  ├── 📄 MASTER_PHASE_06_NOTION_IMPORT.csv

> └── 📂 scripts/

> │  ├── 📄 apply_rename_map.py

> │  ├── 📄 audit_ledger.py

> │  ├── 📄 consolidate_master_data.py

> │  ├── 📄 export_ledger_to_csv.py

> │  ├── 📄 generate_views.py

> │  ├── 📄 integrity_check.py

> │  └── 📂 maintenance/

> │    ├── 📄 generate_binder_pdf.py

> │  ├── 📄 merge_ledger.py

> │  └── 📂 ops/

> │    ├── 📄 build_binder.py

> │    ├── 📄 render_special_files.py

> │    ├── 📄 update_timeline_violations.py

> │  └── 📄 seed_master_ledger.py

> ```

### Assistant
> You’re **very close**. What you have is already 80% of a serious case system. The remaining 20% is **authority hygiene**: right now you’ve got **truth + raw + workbench** bleeding into each other (mostly because `00_CASE_MANAGEMENT/20_evidence` is a contradiction in terms).
> 
> Here’s what I think your **final final final** should be, based on what you said:
> 
> - **00_CASE_MANAGEMENT = source of truth only**
> - **Records (evidence/exhibits/trackers) live outside case management**
> - **Phases are workspaces that roll up into case management**
> - **Chronology is the spine; buckets are curated views**
> 
> ---
> 
> # What’s “wrong” (in a useful way) with the current tree
> 
> ## 1) `00_CASE_MANAGEMENT/20_evidence` is structurally invalid
> Case Management can’t be both:
> - the curated truth hub **and**
> - the raw evidence warehouse
> 
> That’s how forks happen.
> 
> ✅ Fix: move evidence out of `00_CASE_MANAGEMENT` entirely.
> 
> ---
> 
> ## 2) You have “court record” living inside evidence
> `20_evidence/10_Docket` is effectively **Court Record** (filed PDFs, orders, writs). That should be **its own Records class** and/or rolled into Phase 01 workspace + a canonical court index in Case Management.
> 
> ✅ Fix: separate **Court Record** from **Evidence Record** at the Records layer.
> 
> ---
> 
> ## 3) You’ve got “Exposure and Harm” inside evidence
> `00_CASE_MANAGEMENT/20_evidence/40_Exposure_and_Harm` is analysis/valuation content mixed into evidence storage.
> 
> ✅ Fix: move Exposure/Harm to either:
> - **Records → Harm/Financial** (if it’s documentation), or
> - **Phase 05 Litigation / Phase 03 Credit** (if it’s work output), and then roll up into `00_CASE_MANAGEMENT`.
> 
> ---
> 
> ## 4) Duplicate/odd files that will cause coherence drift
> - `02_TIMELINE.md` and `02_TIMELINE.mw` (pick one canonical format)
> - random `2025_05_13_14_52_56.pdf.pdf` style files (needs normalization or quarantine)
> 
> ✅ Fix: only one canonical timeline format + quarantine “unknown-format” artifacts into an `inbox/` until normalized.
> 
> ---
> 
> # The “Final Final Final” Top-Level Layout
> 
> You already have `content/` as the root. Keep it. Inside it, lock this:
> 
> ```markdown
> content/
> ├── 00_CASE_MANAGEMENT/              # SOURCE OF TRUTH (curated, locked)
> │   ├── 10_Case_Master/
> │   │   ├── CASE_MASTER.md
> │   │   ├── CASE_SUMMARY.md
> │   │   ├── CASE_TIMELINE.md
> │   │   ├── CASE_VIOLATIONS.md
> │   │   ├── CASE_ANALYSIS.md
> │   │   ├── CASE_STRATEGY_INTERNAL.md
> │   │   ├── CASE_VALUATION_INTERNAL.md
> │   │   ├── CASE_TASKS.md
> │   │   ├── CASE_DECISIONS.md
> │   │   ├── INDEX.md
> │   │   └── PHASE_LOCK_STATUS.md
> │   └── 90_Audit_and_Integrity/
> │       ├── repo_index.csv
> │       ├── audit_report.txt
> │       └── integrity_check_reports/
> │
> ├── 01_RECORDS/                      # FACTS + PACKAGES + TRACKERS (no arguing)
> │   ├── 10_COURT_RECORD/             # docket PDFs, orders, writs, receipts
> │   ├── 20_EVIDENCE_RAW/             # raw photos/video/audio/docs
> │   ├── 30_EXHIBITS/                 # curated evidence packages
> │   ├── 40_SERVICE_AND_DELIVERY/     # USPS, service logs, transmittals
> │   ├── 50_TRACKERS/                 # csv/md trackers (docket, tasks, violations, etc.)
> │   └── 60_FINANCIAL_RECORDS/        # statements, invoices, utilities, taxes
> │
> ├── 02_PHASE_WORK/                   # WHERE WORK HAPPENS (draft → file → roll-up)
> │   ├── 01_PHASE_FORECLOSURE_COURT/  # your current 01_PHASE_FORECLOSURE.CLOSED
> │   ├── 02_PHASE_PRESERVATION/
> │   ├── 03_PHASE_CREDIT_FCRA/
> │   ├── 04_PHASE_REGULATORS/
> │   ├── 05_PHASE_LITIGATION/
> │   └── 06_PHASE_MEDIA_INQUIRIES/
> │
> ├── 90_TEMPLATES/                    # was 99_Templates (either is fine)
> └── 99_SCRIPTS/                      # scripts (ops + maintenance)
> ```
> 
> ### Why this is “final”
> - **00** is pure canonical story + decisions
> - **01** is pure records + inputs
> - **02** is pure workbench per phase
> - Templates and scripts are separated and don’t contaminate the case narrative
> 
> ---
> 
> # Mapping from your current tree → final
> 
> ## Move these OUT of `00_CASE_MANAGEMENT/20_evidence/…`
> 
> ### ✅ Court Record
> Current:
> - `00_CASE_MANAGEMENT/20_evidence/10_Docket/*`
> 
> Final:
> - `01_RECORDS/10_COURT_RECORD/*`
> 
> ### ✅ Actor folders (FCFCU/AES/etc.)
> Current:
> - `00_CASE_MANAGEMENT/20_evidence/20_Actors/*`
> 
> Final (two options; pick one and stick to it):
> - Option A (recommended): `01_RECORDS/20_EVIDENCE_RAW/actors/*`
> - Option B: `01_RECORDS/20_EVIDENCE_RAW/communications/*` (then actors are tags, not folders)
> 
> ### ✅ Supporting media (photos/video/parcel/etc.)
> Current:
> - `00_CASE_MANAGEMENT/20_evidence/30_Supporting/*`
> 
> Final:
> - `01_RECORDS/20_EVIDENCE_RAW/*` (split by media type and doc type)
> 
> ### ✅ Exposure and harm
> Current:
> - `00_CASE_MANAGEMENT/20_evidence/40_Exposure_and_Harm/*`
> 
> Final (depends what’s inside):
> - If it’s **documentation**: `01_RECORDS/60_FINANCIAL_RECORDS/` + `01_RECORDS/50_TRACKERS/`
> - If it’s **analysis**: `02_PHASE_WORK/05_PHASE_LITIGATION/…` then roll up summary into `00_CASE_MANAGEMENT/10_Case_Master/`
> 
> ### ✅ Service & delivery
> Current:
> - `00_CASE_MANAGEMENT/20_evidence/60_Service_and_delivery/*`
> 
> Final:
> - `01_RECORDS/40_SERVICE_AND_DELIVERY/*`
> 
> ---
> 
> # Court Record Naming (you were right)
> 
> You can keep **chronology + short type codes**. Your existing `001_…` numbering is okay, but it’s redundant once you have dates.
> 
> **Final recommended format:**
> ```
> YYYY-MM-DD__CR__<TYPE>__<Descriptor>.pdf
> ```
> 
> So:
> - `001_2025-01-16_Complaint.pdf`
> becomes
> - `2025-01-16__CR__FI__Complaint.pdf`
> 
> If you *really* want sequence numbers, make them secondary:
> ```
> 2025-01-16__CR__FI__Complaint__seq001.pdf
> ```
> 
> ---
> 
> # Case Management: fix your master file set
> 
> Right now you have:
> - `01_CASE_BIBLE.md`
> - `02_TIMELINE.md` and `.mw`
> - `03_VIOLATIONS.md`
> - `05_VALUATION.md`
> - `06_MASTER_TASKLIST.md`
> - strategy memos scattered
> - `.canvas` files
> 
> **Make Case Management explicitly canonical** by renaming to stable “CASE_*” names and forcing **one-per-function**.
> 
> ### Immediate cleanup inside `00_CASE_MANAGEMENT/10_Case_Master/`
> - Keep: `CASE_MASTER.md` as the “read this first” narrative spine
> - Keep: `CASE_TIMELINE.md` (only one)
> - Keep: `CASE_VIOLATIONS.md`
> - Keep: `CASE_ANALYSIS.md`
> - Keep: `CASE_STRATEGY_INTERNAL.md`
> - Keep: `CASE_VALUATION_INTERNAL.md`
> - Keep: `CASE_TASKS.md`
> - Keep: `CASE_DECISIONS.md`
> - Add: `INDEX.md`
> 
> Then move the standalone strategy memos into:
> - `00_CASE_MANAGEMENT/10_Case_Master/_memos/…`
> or extract their content into `CASE_ANALYSIS/CASE_STRATEGY` and archive the originals.
> 
> ---
> 
> # Phase folders: you’re already doing it right
> 
> Your phase folders are **workspaces** and look strong (send queues, manifests, output, archives). Keep that.
> 
> The only change I’d make is to standardize the internal sub-structure so every phase feels the same:
> 
> ```
> PHASE_X/
> ├── 00_overview/
> ├── 10_inbox/            # unprocessed inputs
> ├── 20_working/          # drafts, notes, experiments
> ├── 30_output/           # things you send / file
> ├── 40_responses/        # replies, receipts, confirmations
> └── 90_archive/
> ```
> 
> This will make automation and roll-ups painless.
> 
> ---
> 
> # The ONE rule that will keep this coherent forever
> 
> ## Phase Lock → Roll-up Gate
> When something in a phase becomes “real” (sent/filed/relied on):
> - it gets marked `LOCKED` in that phase
> - then its **summary + key pointers** get copied into `00_CASE_MANAGEMENT`
> 
> That’s how you keep “source of truth” real.
> 
> ---
> 
> ## My verdict
> Your current structure is **excellent**, just slightly mis-layered.
> 
> **Final changes required:**
> 1) Move evidence out of Case Management  
> 2) Create a clean `01_RECORDS` layer  
> 3) Standardize Case Master file names + remove duplicate timeline formats  
> 4) Treat phases as workbenches with roll-up gates
> 
> If you want the fastest path: I can give you a **surgical rename/move plan** (a literal “move A → B” checklist) for just these directories:
> - `00_CASE_MANAGEMENT/20_evidence/*`
> - `00_CASE_MANAGEMENT/10_Case_Master/*`
> - `scripts/` placement
> 
> …and you can execute it without breaking your repo.

### User
> here is the content inventory you want to create the migration file

### Assistant
> Yep. I used your `content_inventory.csv` to generate a **migration map (old → new)** that implements the “final final final” architecture we just locked:
> 
> - **00_CASE_MANAGEMENT stays the source of truth** (only curated masters + memos)
> - **All evidence gets moved out of Case Management** into a dedicated **01_RECORDS**
> - **All PHASE folders become workbenches** under **02_PHASE_WORK**
> - **Templates → 90_TEMPLATES**
> - **scripts → 99_SCRIPTS**
> - **30_Trackers → 01_RECORDS/50_TRACKERS**
> - Case Master files get **canonical renames** (`CASE_MASTER.md`, `CASE_TIMELINE.md`, etc.)
> - `00_CASE_MANAGEMENT/20_evidence/40_Exposure_and_Harm` is conservatively placed into **Litigation phase archive** so you don’t lose context while we later curate properly.
> 
> ### Downloads
> - [Download migration map (file-by-file)](sandbox:/mnt/data/migration_map_v1.csv)  
> - [Download folder moves (high-level)](sandbox:/mnt/data/migration_folders_v1.csv)
> 
> ### Notes (important)
> - The migration map includes **MOVE vs KEEP**, plus a short “notes” field when a rule triggered.
> - I intentionally **did not delete anything** and treated ambiguous buckets (like Exposure/Harm) as **legacy archive** for now. That prevents accidental data loss and keeps the roll-up discipline intact.
> 
> If you want, next I can generate:
> - a **rename-only patch** (safe, reversible) vs a **move+rename patch**
> - a ready-to-run **PowerShell** or **Python** script that executes this migration using the CSV (with dry-run + conflict checks).

### User
> ok, lets setup up a local rag for this case, ingestions, embedding vecotrizing, context aware, rag, insights, the case nueral net

### Assistant
> Alright. Let’s build your **local case neural net**: a RAG system that ingests your repo, embeds it, answers questions with **citations back to files**, and can generate **insights** (contradictions, missing links, timelines, exhibit gaps).
> 
> No cloud required unless *you* choose it.
> 
> ---
> 
> # 0) What we’re actually building
> ## MVP (Week 1 energy)
> 1. **Ingest** your case repo (Markdown/PDF/HTML/images)
> 2. **Extract text** (PDF parsing + OCR fallback)
> 3. **Chunk + embed** with a local embedding model
> 4. **Store vectors** in a local vector DB
> 5. **Query** with a local LLM + citations (RAG)
> 6. **Case insights**:
>    - “What’s the best evidence for X?”
>    - “What contradicts Y?”
>    - “What’s missing for Z?”
>    - “Build an exhibit package for ___”
> 
> ## Next layer (Case neural net)
> 7. Build a **knowledge graph** (events ↔ violations ↔ evidence ↔ filings ↔ actors)
> 8. Show it as:
>    - interactive 2D (HTML)
>    - optional 3D later
> 
> ---
> 
> # 1) Pick your stack (fast + local + Python)
> You like Python. Good.
> 
> ### Recommended stack
> - **Ingestion/Chunking/RAG**: `llama-index`
> - **Vector DB**: `qdrant` (local, fast, solid) *or* `chroma` (simpler)
> - **Embeddings (local)**: `nomic-embed-text` or `bge-small-en` via **Ollama**
> - **LLM (local)**: `llama3.1` or `qwen2.5` via **Ollama**
> - **Reranking (optional but worth it)**: `bge-reranker` (local)
> 
> If you already run Ollama, this is stupid-simple.
> 
> ---
> 
> # 2) Repo-aware ingestion rules (so RAG doesn’t lie)
> Your case has strong structure. Use it.
> 
> ## What to ingest first (high signal)
> - `00_CASE_MANAGEMENT/10_Case_Master/*` (canonical truth)
> - `01_RECORDS/10_COURT_RECORD/*` (court record PDFs)
> - `01_RECORDS/30_EXHIBITS/*` (curated packages)
> - `02_PHASE_WORK/*/30_output/*` (sent/filed outputs)
> 
> ## What to ingest later (noise-prone)
> - raw screenshots dumps
> - giant media folders without text
> - archived drafts
> 
> ## Metadata is non-negotiable
> Every chunk must carry:
> - `case_id`
> - `source_path` (relative)
> - `source_type` (court_record, exhibit, evidence_raw, phase_output, case_master)
> - `date` (best-effort from filename)
> - `phase` (if applicable)
> - `doc_role` (truth / record / workbench)
> 
> This is how you get **context-aware answers** and prevent “drafts” from overruling canon.
> 
> ---
> 
> # 3) Folder layout for the RAG system (inside your repo)
> Put this at repo root:
> 
> ```
> case_rag/
>   config/
>     sources.yaml
>     ingest_rules.yaml
>   data/
>     qdrant/              # local vector db storage (if embedded)
>     extracted_text/      # cached parsed text
>     manifests/           # file lists + hashes
>   scripts/
>     01_scan_repo.py
>     02_extract_text.py
>     03_embed_index.py
>     04_query_chat.py
>     05_insights.py
>     06_build_graph.py
>   prompts/
>     rag_answer.txt
>     contradiction_hunt.txt
>     exhibit_builder.txt
>   ui/
>     chat_local.py        # simple local web ui (optional)
>     graph.html
> ```
> 
> ---
> 
> # 4) Install + run (local)
> ## Install packages
> ```bash
> python -m venv .venv
> # windows: .venv\Scripts\activate
> source .venv/bin/activate
> 
> pip install llama-index qdrant-client chromadb pypdf pymupdf \
>             beautifulsoup4 python-frontmatter rapidfuzz \
>             pillow pytesseract opencv-python
> ```
> 
> ## Install Ollama + models
> ```bash
> ollama pull nomic-embed-text
> ollama pull llama3.1
> ```
> 
> ---
> 
> # 5) Ingestion pipeline (how it works)
> ### Step A — Scan & classify
> - Walk the repo
> - Classify each file into a source_type based on path
> - Extract `date` from filename prefix (`YYYY-MM-DD`)
> - Compute hash (so incremental updates are cheap)
> 
> ### Step B — Extract text
> - `.md`: direct
> - `.html/.mhtml`: strip tags
> - `.pdf`: parse text; if empty, OCR fallback for key pages
> - images: OCR only if they’re in “text-bearing” folders (court screenshots, letters)
> 
> ### Step C — Chunking (legal-friendly)
> Use **structure-aware chunking**:
> - headings in markdown (`#`, `##`)
> - “Exhibit” boundaries
> - court document sections (where detectable)
> 
> Chunk target:
> - ~700–1200 tokens
> - overlap ~100–150 tokens
> 
> ### Step D — Embed + index
> Store embeddings in Qdrant/Chroma with metadata.
> 
> ### Step E — Query with guardrails
> Retrieval:
> - canonical-first bias (Case Master gets priority)
> - filter by phase/date/type when user asks
> - cite sources with path + chunk id
> 
> ---
> 
> # 6) “Case neural net” (the insight engine)
> Once RAG answers work, build **graph extraction**:
> 
> ## Nodes
> - Events (date + label)
> - Filings (doc id)
> - Orders
> - Evidence items
> - Exhibits
> - Violations (from your Master Violation Inventory)
> - Actors (FCFCU, Sheriff, AES, etc.)
> 
> ## Edges
> - “supports”
> - “contradicts”
> - “filed_in”
> - “cites”
> - “triggered”
> - “damages_from”
> - “related_to”
> 
> ## Outputs
> - `graph.json` (portable)
> - `graph.html` (interactive)
> - later: 3D if you still want it
> 
> ---
> 
> # 7) The three “killer” query modes you want
> These are what make it feel like a real assistant, not a doc search.
> 
> ## A) Canonical Answer Mode
> > “Answer only using CASE_MASTER + court record unless I request drafts.”
> 
> ## B) Evidence Package Mode
> > “Build Exhibit Package for: service defect”
> Output:
> - exhibit list
> - evidence paths
> - missing items
> - suggested ordering
> 
> ## C) Contradiction + Gap Mode
> > “Find contradictions between timeline, violations, and filings.”
> Output:
> - conflict statements
> - file locations
> - recommended correction (what becomes canonical)
> 
> ---
> 
> # 8) What I need from you (no fluff)
> To tailor this precisely, I need only **one thing**:
> - the **absolute path** to your repo root on your machine (you already have it in the inventory, just confirm the current one you’re using)
> 
> Everything else we can infer from structure.
> 
> ---
> 
> # 9) Immediate next step (do this first)
> Pick **one** vector DB:
> - **Qdrant** if you want speed + durability (recommended)
> - **Chroma** if you want “simplest possible”
> 
> Tell me which you want, and I’ll give you:
> - `sources.yaml` + `ingest_rules.yaml`
> - the actual scripts (scan/extract/embed/query)
> - and a default prompt pack tuned for your case structure (canon-first, citations required)
> 
> If you want to move fast: choose **Qdrant + Ollama (nomic-embed-text + llama3.1)** and we’re off.
