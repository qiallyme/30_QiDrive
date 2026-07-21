---
layout: page
title: "Case Management Architecture"
slug: "case_management_architecture"
created_at: "2026-04-03 00:19:00"
updated_at: "2026-07-18T11:03:14-04:00"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-005.json"
template_key: master-template
date: 2026-04-03
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69cf4d91-1e7c-8332-993c-8dde1aa3b5ba"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Case Management Architecture

## Overview
- **Date**: 2026-04-03 00:19:00
- **Conversation ID**: `69cf4d91-1e7c-8332-993c-8dde1aa3b5ba`
- **Source**: `Chat-Export-28513-2026/conversations-005.json`

## Chat History

### User
> Gemini said
> Here is the database architecture to recreate the matter management system in Supabase. This schema normalizes the UI components into relational PostgreSQL tables.
> 
> Core Architecture & Schema Maps
> To support the application's structure, the database requires a central cases table to act as the primary foreign key for all related modules.
> 
> 
> Case Details: Captures Case Name , Case Number , Court , Judge , Trial Date , and whether a Jury Trial is Requested. It also requires JSONB or related tables to store Plaintiff information and Defense Counsel information.
> +4
> 
> 
> Facts: Requires fields for Title , Description , Date Occurred , Category , Importance , Status , Legal Theory , and Notes.
> +4
> 
> 
> Evidence: Requires fields for Title , Type , Description , Source Date , Court Readiness , and Notes.
> +4
> 
> 
> Tasks & Deadlines: Requires fields for Title , Description , Category , Status , Priority , and Due Date.
> +4
> 
> 
> Timeline Events: Requires fields for Title , Description , Date , Time , Event Type , and Importance.
> +4
> 
> 
> Documents: Requires fields for Title , Type , Description , Status , Due Date , Content , and Notes.
> +4
> 
> Trial Prep: Separates into Exhibits and Witnesses. Exhibits need Exhibit # , Description , Type , Pre-marked status , and Objections Anticipated. Witnesses need Name , Role , Summary of Testimony , and Subpoena status.
> +4
> 
> Supabase Implementation (PostgreSQL)
> SQL
> -- 1. Cases (The Central Hub)
> CREATE TABLE public.cases (
>     id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
>     user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
>     case_name TEXT NOT NULL,
>     case_number TEXT,
>     court TEXT,
>     judge TEXT,
>     trial_date DATE,
>     jury_trial_requested BOOLEAN DEFAULT false,
>     plaintiff_info JSONB, -- Stores Name, Email, Phone, Address, Pro Se status
>     defense_info JSONB,   -- Stores Defendants, Attorney, Law Firm, Email, Address
>     created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc', now())
> );
> 
> -- 2. Facts
> CREATE TABLE public.facts (
>     id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
>     case_id UUID REFERENCES public.cases(id) ON DELETE CASCADE,
>     title TEXT NOT NULL,
>     description TEXT,
>     date_occurred DATE,
>     category TEXT,
>     importance TEXT CHECK (importance IN ('Low', 'Medium', 'High', 'Critical')),
>     status TEXT CHECK (status IN ('Unverified', 'Verified')),
>     legal_theory TEXT,
>     notes TEXT,
>     created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc', now())
> );
> 
> -- 3. Evidence
> CREATE TABLE public.evidence (
>     id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
>     case_id UUID REFERENCES public.cases(id) ON DELETE CASCADE,
>     title TEXT NOT NULL,
>     type TEXT,
>     description TEXT,
>     source_date DATE,
>     court_readiness TEXT CHECK (court_readiness IN ('Needs Review', 'Ready')),
>     notes TEXT,
>     file_url TEXT, -- Link to Supabase Storage bucket
>     created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc', now())
> );
> 
> -- 4. Tasks & Deadlines
> CREATE TABLE public.tasks (
>     id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
>     case_id UUID REFERENCES public.cases(id) ON DELETE CASCADE,
>     title TEXT NOT NULL,
>     description TEXT,
>     category TEXT,
>     status TEXT CHECK (status IN ('Pending', 'Active', 'Completed')),
>     priority TEXT CHECK (priority IN ('Low', 'Medium', 'High', 'Critical')),
>     due_date DATE,
>     created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc', now())
> );
> 
> -- 5. Timeline Events
> CREATE TABLE public.events (
>     id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
>     case_id UUID REFERENCES public.cases(id) ON DELETE CASCADE,
>     title TEXT NOT NULL,
>     description TEXT,
>     event_date DATE,
>     event_time TIME,
>     event_type TEXT,
>     importance TEXT CHECK (importance IN ('Low', 'Medium', 'High', 'Critical')),
>     created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc', now())
> );
> 
> -- 6. Documents
> CREATE TABLE public.documents (
>     id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
>     case_id UUID REFERENCES public.cases(id) ON DELETE CASCADE,
>     title TEXT NOT NULL,
>     type TEXT,
>     description TEXT,
>     status TEXT CHECK (status IN ('Draft', 'Filed', 'Archived')),
>     due_date DATE,
>     content TEXT,
>     notes TEXT,
>     created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc', now())
> );
> 
> -- 7. Trial Prep: Exhibits
> CREATE TABLE public.trial_exhibits (
>     id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
>     case_id UUID REFERENCES public.cases(id) ON DELETE CASCADE,
>     exhibit_number TEXT,
>     description TEXT,
>     type TEXT,
>     is_pre_marked BOOLEAN DEFAULT false,
>     objections_anticipated TEXT,
>     evidence_id UUID REFERENCES public.evidence(id) ON DELETE SET NULL,
>     created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc', now())
> );
> 
> -- 8. Trial Prep: Witnesses
> CREATE TABLE public.trial_witnesses (
>     id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
>     case_id UUID REFERENCES public.cases(id) ON DELETE CASCADE,
>     name TEXT NOT NULL,
>     role TEXT,
>     summary_of_testimony TEXT,
>     subpoena_issued BOOLEAN DEFAULT false,
>     created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc', now())
> );
> Infrastructure Notes for the AI Agent
> The application features a "Talk to Your Case" assistant that manages conversations and actively reads case facts, evidence, and strategy.
> +1
> 
> To enable this in Supabase, you must activate the pgvector extension. You will need a case_embeddings table to vectorize the text inside the facts, evidence, and documents tables. When you interact with the agent, an Edge Function will execute a similarity search across that vector table to inject the exact procedural history into the LLM's context window.

### Assistant
> ## Verdict
> 
> Gemini got the **screen nouns** mostly right, but the **architecture is wrong for your stack**.
> 
> It modeled the app like a flat CRUD clone of the UI. Your blueprint does **not** want the portal defining canonical data shapes. It explicitly says the portal is a delivery surface only, while business logic and schema ownership live in the platform/domain/core layers. It also defines `qicase` for case management, `qichronicle` for events, `qivault` for secure documents, `qiarchive` for archive registration, `qially` for AI memory, and `qione` for tenants/RBAC. fileciteturn1file1 fileciteturn1file4
> 
> Your screenshots also show the product is broader than Gemini’s draft captured: the UI includes Facts, Evidence, Tasks, Timeline, Documents, Deadlines, Trial Prep, Legal Research, Updates, and a case agent, plus exhibit/witness management and voir dire planning. fileciteturn1file0
> 
> ## What Gemini got right
> 
> You do need a central case record with related modules for facts, evidence, tasks, events/timeline, documents, and trial prep. That general shape matches both the screenshots and your operational domain. The blueprint already treats cases as the top-level legal/operational unit and explicitly calls out phases, issues, deadlines, case documents, and document issues. fileciteturn1file3
> 
> It is also right that vector search should be enabled through `pgvector`, but in your blueprint embeddings and graph are **derived layers**, not canonical truth. Canonical file registration belongs in `qiarchive`, and AI memory/retrieval belongs downstream. fileciteturn1file2 fileciteturn1file4
> 
> ## Where Gemini is off
> 
> ### 1. It collapses domains that your blueprint keeps separate
> 
> Gemini puts everything into one generic app schema shape. Your blueprint does not. It separates:
> - `qione` for tenants, members, roles, modules
> - `qicase` for legal case management
> - `qichronicle` for events/calendar
> - `qivault` for secure documents
> - `qiarchive` for archive spine and chunks
> - `qially` for AI sessions/messages/memory
> - `qisys` for jobs/events/workers. fileciteturn1file4
> 
> That means a “case management system in Supabase” should be **cross-schema by design**, not one pile of tables.
> 
> ### 2. `plaintiff_info` and `defense_info` as JSONB is lazy and will bite you
> 
> Your own blueprint treats clients and contacts as first-class records, and says contacts should hang off clients, not exist as vague blobs. Counsel, counterparties, witnesses, and representatives are data records, not anonymous JSON stuffed into `cases`. fileciteturn1file3 fileciteturn1file5
> 
> JSONB is fine for snapshots or scraped metadata. It is not fine for core parties/counsel you need to search, relate, reuse, subpoena, or render cleanly.
> 
> ### 3. Evidence should not just be `file_url`
> 
> Your blueprint is explicit: file-derived objects must anchor to `qiarchive.archive_files`, and case documents must reference an `archive_id`. That means “evidence” in the case app is not the file itself. It is a **case-specific wrapper around a registered archive item**. fileciteturn1file3 fileciteturn1file4
> 
> So `file_url TEXT` by itself is too flimsy. You want `archive_id` as the canonical anchor, optionally plus a vault document reference.
> 
> ### 4. Timeline events belong in `qichronicle`, not as a random app-local table
> 
> Your blueprint explicitly maps events/calendar to `qichronicle`, while `qicase` owns deadlines and case logic. fileciteturn1file4
> 
> So the timeline should be one of two things:
> - `qichronicle.events` as the real time record
> - `qicase.case_deadlines` as the case-owned procedural milestone layer
> 
> Gemini’s single `events` table misses that distinction.
> 
> ### 5. The AI layer is underspecified
> 
> The screenshots show a real “Talk to Your Case” assistant. Your blueprint says chatbot/search must be provenance-aware, source-referenced, and downstream of canonical records. It should answer from metadata filters + semantic retrieval + optional graph expansion, then cite archive/chunk/entity references. fileciteturn1file0 fileciteturn1file2
> 
> A single `case_embeddings` table is too thin. You need retrieval contracts tied to `archive_id`, `chunk_id`, and optionally `entity_id`.
> 
> ### 6. The screenshot app itself already exposes why hardcoded UI-driven schema is dangerous
> 
> Your sample case is in **Marion Superior Court 3, Indiana**, but the Legal Research page in the screenshots shows **Utah** rules/resources. That is a classic sign of presentation logic bleeding into case truth. Research resources should be modular/reference data, not hardwired as if they are intrinsic case fields. fileciteturn1file0
> 
> ## The corrected QiOS-aligned architecture
> 
> ### Keep these schemas separate
> 
> | Schema | Owns |
> |---|---|
> | `qione` | tenants, tenant members, roles, enabled modules |
> | `qicase` | cases, parties, contacts, facts/issues, tasks, deadlines, trial prep |
> | `qichronicle` | timeline events, hearings, reminders tied to time |
> | `qiarchive` | canonical file registration, chunks, ingest jobs |
> | `qivault` | secure stored documents if you need managed tenant vault docs |
> | `qially` | case-agent sessions, messages, memory/retrieval artifacts |
> | `qisys` | notification jobs, worker state, automation logs |
> 
> That is the blueprint shape, and it matches the app you’re trying to rebuild better than Gemini’s flat schema. fileciteturn1file4
> 
> ## Recommended table map
> 
> ### `qicase`
> This should be the core domain.
> 
> - `clients`
> - `contacts`
> - `cases`
> - `case_parties`
> - `case_contacts`
> - `case_facts`
> - `case_tasks`
> - `case_deadlines`
> - `case_documents`
> - `document_issues`
> - `case_evidence`
> - `trial_exhibits`
> - `trial_witnesses`
> - `voir_dire_sets`
> - `voir_dire_questions`
> 
> This is consistent with the blueprint’s core case objects plus the trial-prep surfaces visible in the screenshots. fileciteturn1file3 fileciteturn1file0
> 
> ### `qichronicle`
> - `events`
> - optionally `event_reminders`
> 
> Use this for hearings, filings, service attempts, clean-out dates, retrieval windows, and other timeline items. The case domain can reference these through FKs. fileciteturn1file4
> 
> ### `qiarchive`
> - `archive_files`
> - `archive_chunks`
> - `ingest_jobs`
> - `file_history`
> 
> This is the canonical spine for uploaded PDFs, images, audio, video, transcripts, and exhibits. fileciteturn1file4
> 
> ### `qially`
> - `sessions`
> - `messages`
> - `memory_embeddings`
> - optional `case_retrieval_runs`
> 
> That keeps the case agent downstream and provenance-aware. fileciteturn1file4 fileciteturn1file2
> 
> ### `qisys`
> - `jobs`
> - `system_events`
> - optional `notification_rules`
> - optional `notification_deliveries`
> 
> That cleanly handles your Updates / reminder UI instead of jamming email preference logic into the case table. fileciteturn1file4 fileciteturn1file0
> 
> ## Concrete design decisions
> 
> ### Cases
> Put core case metadata here:
> 
> - `tenant_id`
> - `client_id`
> - `case_name`
> - `case_number`
> - `court`
> - `judge`
> - `case_type`
> - `status`
> - `opened_at`
> - `trial_date`
> - `jury_trial_requested`
> - `is_pro_se`
> - `summary`
> - `strategy`
> - `objectives`
> 
> That is much closer to both the screenshots and the blueprint than Gemini’s minimal case record. fileciteturn1file0 fileciteturn1file3
> 
> ### Parties and counsel
> Do **not** store these as JSON blobs.
> 
> Use:
> - `case_parties` for plaintiff/defendant/appellant/appellee/etc.
> - `contacts` for people/org records
> - `case_contacts` for role-on-case mappings like defense counsel, witness, opposing rep, process server
> 
> That gives you reusable records and clean joins.
> 
> ### Facts
> Use `case_facts`, not generic `facts`.
> 
> Suggested columns:
> - `tenant_id`
> - `case_id`
> - `title`
> - `description`
> - `date_occurred`
> - `fact_type`
> - `importance`
> - `verification_status`
> - `legal_theory`
> - `notes`
> - `sort_order`
> 
> This matches the modal in the screenshots almost exactly, but keeps it under the case domain. fileciteturn1file0
> 
> ### Evidence
> Use `case_evidence` as a **wrapper table** around archive/vault assets.
> 
> Suggested columns:
> - `tenant_id`
> - `case_id`
> - `archive_id` nullable but preferred
> - `vault_document_id` nullable
> - `title`
> - `evidence_type`
> - `description`
> - `source_date`
> - `court_readiness`
> - `notes`
> 
> That preserves canonical file lineage instead of pretending a URL is enough. fileciteturn1file3 fileciteturn1file4
> 
> ### Tasks vs deadlines
> Keep them separate.
> 
> - `case_tasks` = work to do
> - `case_deadlines` = procedural due dates, possibly sourced from tasks, docs, or events
> 
> Your screenshots clearly distinguish Task Tracker from Deadline Tracker, and the blueprint already gives deadlines first-class status in the case domain. fileciteturn1file0 fileciteturn1file3
> 
> ### Timeline
> Use `qichronicle.events`.
> 
> Suggested columns:
> - `tenant_id`
> - `case_id`
> - `title`
> - `description`
> - `event_date`
> - `event_time`
> - `event_type`
> - `importance`
> - `source_kind`
> - `source_id`
> 
> This gives you the timeline UI without muddying case-owned procedural tables.
> 
> ### Documents
> This needs two layers:
> 
> 1. **Case document metadata** in `qicase.case_documents`
> 2. **Actual registered file** in `qiarchive.archive_files` or managed document in `qivault.documents`
> 
> Suggested `case_documents` columns:
> - `tenant_id`
> - `case_id`
> - `archive_id` nullable
> - `title`
> - `document_type`
> - `description`
> - `filing_side`
> - `status`
> - `due_date`
> - `body_content`
> - `notes`
> 
> That supports both AI-generated draft docs and real filed artifacts. The screenshots show both. fileciteturn1file0
> 
> ### Trial prep
> This is bigger than Gemini modeled.
> 
> You need at least:
> - `trial_exhibits`
> - `trial_witnesses`
> - `voir_dire_sets`
> - `voir_dire_questions`
> - optionally `trial_checklist_items`
> 
> The screenshots show pre-trial checklist items, exhibit builder, witness list, and voir dire planner. fileciteturn1file0
> 
> ## The blunt version
> 
> Gemini’s version is okay for a toy clone.
> 
> It is **not** okay for your actual architecture because it:
> - ignores schema ownership
> - overuses JSONB
> - fails to anchor evidence/documents to `qiarchive`
> - puts timeline in the wrong place
> - treats AI retrieval like a bolt-on instead of a provenance-aware downstream system
> - does not model the full UI you actually showed. fileciteturn1file4 fileciteturn1file0
> 
> ## Recommended baseline SQL shape
> 
> Not the full migration, just the correct direction:
> 
> ```sql
> -- qicase.cases
> -- core matter record
> id uuid primary key default gen_random_uuid()
> tenant_id uuid not null references qione.tenants(id) on delete cascade
> client_id uuid not null references qicase.clients(id) on delete restrict
> case_name text not null
> case_number text
> court text
> judge text
> case_type text not null default 'civil'
> status text not null default 'open'
> opened_at timestamptz not null default now()
> trial_date date
> jury_trial_requested boolean not null default false
> is_pro_se boolean not null default false
> summary text
> strategy text
> objectives text
> created_at timestamptz not null default now()
> updated_at timestamptz not null default now()
> ```
> 
> ```sql
> -- qicase.case_facts
> id uuid primary key default gen_random_uuid()
> tenant_id uuid not null references qione.tenants(id) on delete cascade
> case_id uuid not null references qicase.cases(id) on delete cascade
> title text not null
> description text
> date_occurred date
> fact_type text
> importance text check (importance in ('low','medium','high','critical'))
> verification_status text check (verification_status in ('unverified','verified','disputed'))
> legal_theory text
> notes text
> sort_order integer not null default 100
> created_at timestamptz not null default now()
> updated_at timestamptz not null default now()
> ```
> 
> ```sql
> -- qicase.case_evidence
> id uuid primary key default gen_random_uuid()
> tenant_id uuid not null references qione.tenants(id) on delete cascade
> case_id uuid not null references qicase.cases(id) on delete cascade
> archive_id uuid references qiarchive.archive_files(id) on delete set null
> title text not null
> evidence_type text
> description text
> source_date date
> court_readiness text check (court_readiness in ('needs_review','ready','admitted'))
> notes text
> created_at timestamptz not null default now()
> updated_at timestamptz not null default now()
> ```
> 
> ```sql
> -- qicase.case_documents
> id uuid primary key default gen_random_uuid()
> tenant_id uuid not null references qione.tenants(id) on delete cascade
> case_id uuid not null references qicase.cases(id) on delete cascade
> archive_id uuid references qiarchive.archive_files(id) on delete set null
> title text not null
> document_type text
> filing_side text check (filing_side in ('plaintiff','defense','court','other'))
> description text
> status text check (status in ('draft','ready','filed','served','archived'))
> due_date date
> body_content text
> notes text
> created_at timestamptz not null default now()
> updated_at timestamptz not null default now()
> ```
> 
> ```sql
> -- qicase.case_deadlines
> id uuid primary key default gen_random_uuid()
> tenant_id uuid not null references qione.tenants(id) on delete cascade
> case_id uuid not null references qicase.cases(id) on delete cascade
> title text not null
> description text
> due_at timestamptz not null
> priority text check (priority in ('low','medium','high','critical'))
> status text check (status in ('pending','met','missed','canceled'))
> source_kind text
> source_id uuid
> created_at timestamptz not null default now()
> updated_at timestamptz not null default now()
> ```
> 
> ```sql
> -- qichronicle.events
> id uuid primary key default gen_random_uuid()
> tenant_id uuid not null references qione.tenants(id) on delete cascade
> case_id uuid references qicase.cases(id) on delete cascade
> title text not null
> description text
> event_date date not null
> event_time time
> event_type text
> importance text check (importance in ('low','medium','high','critical'))
> source_kind text
> source_id uuid
> created_at timestamptz not null default now()
> updated_at timestamptz not null default now()
> ```
> 
> ```sql
> -- qially memory remains downstream/derived
> -- store source provenance, not free-floating embeddings
> case_id uuid references qicase.cases(id)
> archive_id uuid references qiarchive.archive_files(id)
> chunk_id uuid references qiarchive.archive_chunks(id)
> embedding vector(...)
> ```
> 
> ## Best next move
> 
> Do **not** implement Gemini’s schema as-is.
> 
> Implement a **QiOS-aligned v1** with:
> 1. `qicase` for matter logic,
> 2. `qichronicle` for time,
> 3. `qiarchive` as the evidence/document spine,
> 4. `qially` for the case agent,
> 5. `qisys` for reminders/jobs.
> 
> Then layer the UI on top of that instead of letting the UI dictate the database.
> 
> Next move should be turning this into a single Supabase migration pack with RLS and indexes from day one.

### User
> ok this woukld be for future implementation, lets do a seperate project that all the files, docs, ect are in the folder already in the apps data self contained, and the ui is just the interface to interact with, add tasks, and such, and selft contained knowledge graph and ai case agent.

### Assistant
> Yes. That is a **different project shape**, and honestly it is the right one for this use case.
> 
> Do **not** force the full QiOS multi-schema cloud pattern onto a single self-contained case app.  
> For this one, build a **local case workspace app**:
> 
> - the **workspace folder** is the physical source of truth
> - the **local database** is the manifest, index, and state layer
> - the **knowledge graph and AI agent** are derived layers inside that same workspace
> - the **UI is just the operator surface**, not the truth source
> 
> That still follows the good parts of the blueprint: filesystem truth + DB index, derived graph/vector/AI layers, and UI as a surface instead of the owner of business logic. fileciteturn0file1
> 
> Your screenshots also make the target pretty clear: this app needs case info, facts, evidence, tasks, timeline, documents, deadlines, trial prep, updates, and a case agent in one operator-facing workspace. fileciteturn0file0
> 
> # The correct architecture
> 
> ## 1. One case workspace = one self-contained folder
> 
> Use a single workspace root per case, something like:
> 
> ```text
> %LOCALAPPDATA%\QiCaseLocal\workspaces\fcfcu_49d03_2501_mf_002559\
> ```
> 
> Inside it:
> 
> ```text
> workspace/
> ├── case.db                 # local relational database
> ├── case.json               # lightweight workspace manifest
> ├── files/
> │   ├── inbox/
> │   ├── evidence/
> │   ├── filings/
> │   ├── correspondence/
> │   ├── media/
> │   └── exports/
> ├── extracted/
> │   ├── text/
> │   ├── ocr/
> │   └── transcripts/
> ├── index/
> │   ├── chunks/
> │   ├── vectors/
> │   └── graph/
> ├── agent/
> │   ├── sessions/
> │   ├── prompts/
> │   └── cache/
> ├── reports/
> ├── logs/
> └── settings/
> ```
> 
> ## 2. Keep the files on disk, not inside the DB
> 
> Do **not** shove PDFs, video, images, and audio blobs into the database unless there is a very specific reason.
> 
> Use the database to store:
> 
> - file registry
> - metadata
> - extracted text
> - chunk records
> - graph nodes/edges
> - task state
> - agent conversation state
> - citations/provenance
> 
> That gives you a portable case bundle without turning the DB into a junk drawer.
> 
> ## 3. Use one local relational database
> 
> For this app, the database should own:
> 
> - case metadata
> - parties and contacts
> - facts
> - evidence records
> - tasks and deadlines
> - timeline events
> - document records
> - chunk index
> - graph entities/edges
> - agent sessions/messages/citations
> 
> No Supabase required for v1. No tenant/RLS complexity. No unnecessary distributed architecture.
> 
> # The local schema you actually want
> 
> ## Core tables
> 
> Keep these as real tables, not JSON blobs:
> 
> - `matter`
> - `parties`
> - `contacts`
> - `facts`
> - `evidence_items`
> - `tasks`
> - `deadlines`
> - `timeline_events`
> - `documents`
> - `witnesses`
> - `exhibits`
> - `checklist_items`
> 
> ## File and retrieval tables
> 
> - `file_registry`
> - `text_extractions`
> - `text_chunks`
> - `chunk_embeddings`
> - `entity_nodes`
> - `entity_edges`
> - `citations`
> 
> ## Agent tables
> 
> - `agent_sessions`
> - `agent_messages`
> - `agent_runs`
> - `agent_context_items`
> 
> That gives you a clean split:
> 
> - **case truth**
> - **file/index truth**
> - **derived AI/graph truth**
> 
> # What the UI should do
> 
> The UI should be an interface over the local workspace. Period.
> 
> It should:
> 
> - browse files already in the workspace
> - add/edit facts
> - add/edit tasks and deadlines
> - tag evidence
> - generate timeline views
> - open cited documents
> - run the case agent
> - produce reports and exports
> 
> It should **not** invent schema on the fly or become the place where truth only exists.
> 
> That also matches the blueprint principle that applications are surface area and business logic/data contracts live underneath. fileciteturn0file1
> 
> # The case agent contract
> 
> This part matters most.
> 
> Your self-contained AI case agent should answer in this order:
> 
> 1. **Structured records first**  
>    facts, tasks, deadlines, timeline events, exhibits, witnesses
> 
> 2. **File-backed evidence second**  
>    filings, emails, letters, screenshots, transcripts, photos, video notes
> 
> 3. **Derived graph expansion third**  
>    parties, dates, events, contradictions, missing links, repeated actors
> 
> 4. **Answer only with provenance**  
>    every response should point back to:
>    - fact id
>    - task id
>    - document id
>    - file id
>    - chunk id
>    - page/time reference where possible
> 
> No citation, no confident answer.
> 
> ## Minimum agent capabilities
> 
> The agent should be able to:
> 
> - summarize the case
> - find contradictions
> - build a chronology
> - suggest missing evidence
> - identify deadlines and prep gaps
> - draft task lists
> - answer “what supports this claim?”
> - answer “what are we missing?”
> - answer “what happened on X date?”
> - answer “show me all evidence tied to Y issue”
> 
> # Knowledge graph, but not the fake fancy version
> 
> Keep it simple.
> 
> Your local graph is not some giant enterprise Neo4j cosplay.  
> It is a **derived relationship layer** inside the workspace.
> 
> ## Graph nodes
> - people
> - organizations
> - locations
> - documents
> - filings
> - evidence items
> - events
> - legal issues
> - claims
> - statutes/rules
> - dates
> 
> ## Graph edges
> - `involves`
> - `mentions`
> - `occurred_on`
> - `contradicts`
> - `supports`
> - `responds_to`
> - `filed_by`
> - `served_on`
> - `linked_to_issue`
> - `cites`
> - `derived_from`
> 
> That is enough to power:
> - timeline clustering
> - contradiction detection
> - issue grouping
> - evidence linking
> - better agent context assembly
> 
> # One important correction from your screenshots
> 
> Your screenshots show a Marion Superior Court case, but the Legal Research page was showing Utah materials. That is exactly the kind of hardcoded nonsense that breaks trust. Research resources need to be **case-scoped reference packs**, not static UI copy. fileciteturn0file0
> 
> So for this local app:
> 
> - jurisdiction should be a matter setting
> - court/rules references should load from that setting
> - research links should be local reference records, not hardwired into the interface
> 
> # Best internal law for this project
> 
> Use these rules:
> 
> ## Canonical rules
> - files on disk are the physical truth
> - DB rows are the structured truth
> - graph/vector/agent layers are derived
> - every derived record must point back to source records
> - every answer from the agent must be citeable
> 
> ## Anti-chaos rules
> - no JSON dumping for core records
> - no magic inference without stored provenance
> - no document record without a file reference or explicit body text
> - no evidence record without source linkage
> - no timeline event without date precision level
> - no task without status and owner
> - no AI memory that cannot be traced back to source material
> 
> # Best build order
> 
> ## Phase 1 — spine
> Build:
> - workspace folder contract
> - local DB schema
> - file registry
> - document ingestion
> - text extraction/transcript storage
> - chunking
> - basic search
> 
> ## Phase 2 — operator system
> Build:
> - matter dashboard
> - facts
> - evidence
> - tasks
> - timeline
> - documents
> - deadlines
> - trial prep
> 
> That matches the UI you already showed. fileciteturn0file0
> 
> ## Phase 3 — agent
> Build:
> - agent sessions/messages
> - citation pipeline
> - retrieval composer
> - issue-aware context assembly
> - chronology builder
> - contradiction scanner
> 
> ## Phase 4 — graph
> Build:
> - entity extraction
> - node/edge tables
> - issue linking
> - visual graph explorer only after the underlying relationships are stable
> 
> # Bottom line
> 
> For **this** project, the right move is:
> 
> **a standalone local-first case workspace app**
> with:
> - one workspace folder per case
> - one local database
> - one self-contained file/index/graph/agent system
> - a UI that operates on that workspace instead of defining reality
> 
> That is cleaner, faster, more portable, and way less likely to turn into architectural sludge.
> 
> ## Recommendation
> 
> Next move is to lock three things before writing app code:
> 
> 1. the **workspace folder contract**  
> 2. the **local database schema**  
> 3. the **agent retrieval/citation contract**
> 
> Once those three are fixed, the UI becomes straightforward instead of chaotic.

### User
> ok i have the ide make it of of the usb workspace we made and its basically working this only tooka  couple hours. and its exactly what i wanted, now how do we do that with qilabs or at the very least with the home hub app accesible by online supabase auth or even cloudflare zero trust and use supabase as the database, the translation from what we have working locally and that should not be so difficult.

### Assistant
> Yes. This is mostly a **translation problem**, not a rebuild.
> 
> The clean way to think about it:
> 
> ## What changes, what stays
> 
> ### Stays the same
> - domain model
> - UI flows
> - task/fact/document logic
> - agent logic
> - graph/retrieval logic
> - workspace contract
> 
> ### Changes
> - persistence adapter
> - auth layer
> - file storage backend
> - background job runner
> - multi-user access control
> 
> So the real move is:
> 
> **keep the app model, swap the local adapters for cloud adapters.**
> 
> That lines up with your blueprint too: apps are surfaces, while the underlying data contracts and service boundaries live underneath. fileciteturn0file1
> 
> ---
> 
> # The simplest correct answer
> 
> For **Home Hub online**, use:
> 
> - **Cloudflare** for frontend hosting
> - **Supabase Auth** for user login
> - **Supabase Postgres** for structured data
> - **Supabase Storage** for files
> - **Cloudflare Zero Trust** only for admin/internal surfaces, not as the main family-user auth model
> 
> That is the sane split.
> 
> ## Why
> Zero Trust is great for:
> - internal admin tools
> - staging
> - dev surfaces
> - operator panels
> - private docs/apps you do not want public at all
> 
> It is **not** the best replacement for app-level user auth and row-level household permissions.
> 
> For a real Home Hub with mom / Zai / you / invited users, you want:
> - app accounts
> - roles
> - per-household membership
> - database row security
> 
> That is **Supabase Auth + RLS territory**, not just Zero Trust.
> 
> ---
> 
> # Translation pattern from local app → online app
> 
> Your local app probably has something like:
> 
> - local workspace folder
> - local DB
> - local files
> - local graph
> - local agent state
> 
> The cloud translation is:
> 
> | Local | Cloud |
> |---|---|
> | workspace folder | workspace record + storage prefix |
> | local DB | Supabase Postgres |
> | files on disk | Supabase Storage |
> | local auth / none | Supabase Auth |
> | local graph tables | Postgres graph/edge tables |
> | local embeddings/index | pgvector tables |
> | local agent sessions | agent session/message tables |
> | local filesystem permissions | RLS + membership roles |
> 
> That is why this should not be too difficult.
> 
> ---
> 
> # The key architectural move
> 
> Do **not** rewrite the app around Supabase directly.
> 
> Instead, create a thin service boundary in the app:
> 
> ```ts
> WorkspaceRepository
> FileRepository
> TaskRepository
> DocumentRepository
> AgentRepository
> SearchRepository
> AuthRepository
> ```
> 
> Then give each one two implementations:
> 
> ```ts
> LocalWorkspaceRepository
> SupabaseWorkspaceRepository
> ```
> 
> That way:
> - the **same UI** can run local or cloud
> - the **same domain logic** survives
> - only the backend adapter changes
> 
> That is the adult way to do it.
> 
> If the current local build is hardwired directly into local file APIs everywhere, then you need one cleanup pass first. Not fatal, just messier.
> 
> ---
> 
> # Best deployment pattern for Home Hub
> 
> ## v1 online shape
> 
> ### Frontend
> - Cloudflare Pages or Workers-hosted app
> - same UI concept you already have
> 
> ### Auth
> - Supabase Auth
> - magic link or email/password
> - later social login if needed
> 
> ### Database
> Use two schemas if you want it QiLabs-aligned without getting stupid about it:
> 
> - `qione` = membership/container layer
> - `qihome` = actual home hub data
> 
> ### Storage
> Use a bucket pattern like:
> 
> ```text id="xtsws1"
> homehub/{household_id}/documents/
> homehub/{household_id}/photos/
> homehub/{household_id}/exports/
> homehub/{household_id}/uploads/
> ```
> 
> ### Roles
> At minimum:
> 
> - owner
> - admin
> - member
> - read_only
> 
> ---
> 
> # Minimal online schema for Home Hub
> 
> ## `qione`
> - `tenants` or `households`
> - `tenant_members`
> - `member_roles`
> 
> ## `qihome`
> - `hub_pages`
> - `quick_links`
> - `tasks`
> - `task_assignments`
> - `requests`
> - `bills`
> - `payments`
> - `expenses`
> - `expense_shares`
> - `wiki_entries`
> - `documents`
> - `calendar_items`
> - `notifications`
> 
> That gets you the online Home Hub without overengineering it.
> 
> ---
> 
> # If you want the same “self-contained workspace” feeling online
> 
> Then mimic the local workspace contract in cloud form.
> 
> ## Concept
> Each household or project gets a **workspace root**:
> 
> ### Database record
> ```text id="ij8sdq"
> workspace_id
> tenant_id
> slug
> title
> settings
> storage_prefix
> status
> ```
> 
> ### Storage prefix
> ```text id="e4jlwm"
> homehub/{tenant_id}/{workspace_id}/...
> ```
> 
> ### Data rows
> Every row in the domain tables carries:
> - `tenant_id`
> - `workspace_id`
> 
> That gives you the same mental model as the USB workspace:
> one container, one context, one searchable body of stuff.
> 
> ---
> 
> # How to do this for QiLabs more broadly
> 
> For **QiLabs internal tools**, you have two different patterns.
> 
> ## Pattern A — internal operator tools
> Use:
> - Cloudflare Zero Trust
> - Supabase DB
> - maybe no public signup at all
> 
> This is good for:
> - admin panels
> - internal ops dashboards
> - ingestion tools
> - private control planes
> 
> ## Pattern B — real user-facing apps
> Use:
> - Cloudflare frontend
> - Supabase Auth
> - RLS
> - optional Zero Trust only around internal/admin routes
> 
> This is good for:
> - Home Hub
> - client portals
> - member dashboards
> - user-owned workspaces
> 
> That split matters. Don’t blur them.
> 
> ---
> 
> # Where the AI agent lives online
> 
> Same rule as local:
> 
> - structured records are canonical
> - files are canonical source artifacts
> - graph/vector/agent are derived
> 
> So online:
> 
> ## Canonical
> - Postgres rows
> - Storage objects
> 
> ## Derived
> - extracted text
> - chunks
> - embeddings
> - graph edges
> - agent sessions
> - summaries
> - suggestions
> 
> That is straight blueprint logic: derived AI/graph/vector layers do not become truth sources. fileciteturn0file1
> 
> ---
> 
> # Online agent stack
> 
> For Home Hub, you probably do **not** need the full legal-case graph complexity first.
> 
> ## Start with:
> - `documents`
> - `wiki_entries`
> - `tasks`
> - `requests`
> - `calendar_items`
> 
> Then derive:
> - chunks
> - embeddings
> - agent context citations
> 
> So the assistant can answer:
> - what bills are due this week
> - what did mom ask for
> - what tasks are assigned to Zai
> - what are the house rules
> - where is the trash schedule
> - what documents are attached to the car issue
> 
> That is useful immediately.
> 
> ---
> 
> # The ingestion translation
> 
> Local app likely does:
> - add file
> - extract text
> - index it
> - attach to records
> 
> Online version does the same, just with cloud plumbing.
> 
> ## Flow
> 1. user uploads file to Supabase Storage
> 2. create `documents` row
> 3. enqueue extraction/index job
> 4. extract text
> 5. chunk
> 6. embed
> 7. store citations/provenance
> 8. agent/search can now use it
> 
> That is it.
> 
> Do not make the browser do the heavy lifting if files get large.
> 
> ---
> 
> # Where Cloudflare fits best
> 
> ## Best use of Cloudflare here
> - host frontend
> - cache public/static assets
> - protect admin/internal routes
> - run lightweight API/edge middleware if needed
> 
> ## Best use of Supabase
> - auth
> - relational DB
> - row security
> - storage
> - vector index if you want in-DB retrieval
> 
> That is a clean split.
> 
> ---
> 
> # What not to do
> 
> ## Don’t do this
> - use Zero Trust as the only permission model for a real multi-user household app
> - put business truth only in UI state
> - dump core records into giant JSON blobs
> - make AI memory canonical
> - hardcode “research/resources” style content into the UI instead of table-driven records
> - fork the local and cloud apps into two totally separate codebases unless you absolutely have to
> 
> That last one is the big trap.
> 
> ---
> 
> # The practical migration plan
> 
> ## Phase 1 — freeze the domain contract
> Lock:
> - tables
> - storage prefixes
> - role model
> - workspace model
> 
> ## Phase 2 — add repository adapters
> Refactor local app so UI talks to interfaces, not directly to local file calls.
> 
> ## Phase 3 — implement Supabase adapters
> Build:
> - auth adapter
> - DB adapter
> - storage adapter
> - search/agent adapter
> 
> ## Phase 4 — deploy Home Hub online
> - Cloudflare frontend
> - Supabase backend
> - RLS enabled
> - invited users only
> 
> ## Phase 5 — add agent/retrieval
> Only after the records and storage are stable.
> 
> ---
> 
> # My blunt recommendation
> 
> ## For Home Hub
> Do this first.
> 
> It is the easiest proof:
> - smaller stakes
> - simpler schema
> - obvious user roles
> - clear usefulness
> - clean online testbed for the local→cloud translation pattern
> 
> ## For QiLabs broadly
> Once Home Hub works, reuse the same pattern:
> 
> - local-first workspace model
> - repository abstraction
> - cloud adapter layer
> - Supabase auth/data/storage
> - Cloudflare hosting/protection
> - derived agent/index layer on top
> 
> That becomes your reusable deployment pattern across apps.
> 
> ---
> 
> # Bottom line
> 
> You are right: the translation from the working local app to an online app **should not be that difficult**.
> 
> The correct framing is:
> 
> **same domain, same UI logic, new persistence/auth/storage adapters**
> 
> For **Home Hub online**, use:
> - **Supabase Auth** for actual users
> - **Supabase DB + Storage** for app state/files
> - **Cloudflare** for hosting
> - **Zero Trust** for admin/internal surfaces only
> 
> That is the cleanest path with the least nonsense.
> 
> ## Next move
> Lock the **Home Hub cloud data contract** first:
> 1. membership model
> 2. workspace model
> 3. storage path contract
> 4. RLS rules
> 5. repository interface layer
> 
> Then the port becomes mechanical instead of philosophical.
