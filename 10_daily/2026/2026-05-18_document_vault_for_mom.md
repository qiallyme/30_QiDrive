---
layout: page
title: "Document Vault for Mom"
slug: "document_vault_for_mom"
created_at: "2026-05-18 22:26:45"
updated_at: "2026-07-16T06:49:32-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-007.json"
template_key: master-template
date: 2026-05-18
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a0bd864-9fb0-83ea-90fd-75506c3f4f52"
canonical_ref: ""
---

# Document Vault for Mom

## Overview
- **Date**: 2026-05-18 22:26:45
- **Conversation ID**: `6a0bd864-9fb0-83ea-90fd-75506c3f4f52`
- **Source**: `Chat-Export-28513-2026/conversations-007.json`

## Chat History

### User
> how should we store the pdf documents in the app a document vault for mom

### Assistant
> Yes — a document vault is the right move. I’d treat PDFs as **source-of-truth assets**, not just attachments, so the app can organize, audit, search, and connect them to care events.

### Assistant
> Absolutely yes: build a **Document Vault** for Mom.
> 
> Do **not** just dump PDFs into random attachments. That becomes a graveyard. The clean version is:
> 
> > **PDF file lives in Supabase Storage.  
> > Document record lives in Postgres.  
> > Events, meds, visits, labs, and notes link back to that document record.**
> 
> That gives you security, search, audit, and context.
> 
> ## Recommended structure
> 
> ### 1. Supabase Storage bucket
> 
> Create one private bucket:
> 
> ```text
> care-documents
> ```
> 
> Keep it **private**, not public. Supabase Storage supports private files with access controlled by RLS, and signed URLs can be generated when the app needs temporary access to view/download a file. citeturn759663search0turn759663search5
> 
> Suggested file path pattern:
> 
> ```text
> patients/{patient_id}/documents/{document_id}/{original_filename}
> ```
> 
> Example:
> 
> ```text
> patients/c5c16555-10b9-45f3-a5a3-d7528600cd47/documents/8a7.../hospital-discharge-2026-05-05.pdf
> ```
> 
> Do **not** rely on the storage path as your database. Storage is the file cabinet. Postgres is the index.
> 
> ---
> 
> ## 2. Add a `care.documents` table
> 
> This is the master vault index.
> 
> ```sql
> create table if not exists care.documents (
>   id uuid primary key default gen_random_uuid(),
> 
>   patient_id uuid not null references care.patients(id) on delete cascade,
> 
>   title text not null,
>   document_type text not null,
>   document_date date,
>   source_name text,
>   source_org text,
> 
>   storage_bucket text not null default 'care-documents',
>   storage_path text not null,
>   original_filename text,
>   mime_type text default 'application/pdf',
>   file_size_bytes bigint,
> 
>   status text not null default 'active',
>   is_sensitive boolean not null default true,
>   is_legal_document boolean not null default false,
>   is_medical_record boolean not null default true,
> 
>   summary text,
>   notes text,
>   tags text[] default '{}',
> 
>   uploaded_by uuid,
>   uploaded_at timestamptz not null default now(),
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now(),
> 
>   metadata_json jsonb not null default '{}'::jsonb
> );
> ```
> 
> Suggested `document_type` values:
> 
> ```text
> discharge_summary
> lab_report
> imaging_report
> medication_list
> visit_summary
> insurance
> legal
> advance_directive
> poa_medical
> poa_financial
> hipaa_release
> care_plan
> therapy_note
> oxygen_equipment
> prescription
> other
> ```
> 
> That gives you the big buckets without making the app stupidly complicated.
> 
> ---
> 
> ## 3. Add document links instead of duplicating files everywhere
> 
> You need a flexible join table so one PDF can connect to multiple things.
> 
> ```sql
> create table if not exists care.document_links (
>   id uuid primary key default gen_random_uuid(),
> 
>   patient_id uuid not null references care.patients(id) on delete cascade,
>   document_id uuid not null references care.documents(id) on delete cascade,
> 
>   linked_table text not null,
>   linked_id uuid not null,
> 
>   link_type text default 'related',
>   notes text,
> 
>   created_at timestamptz not null default now(),
>   metadata_json jsonb not null default '{}'::jsonb
> );
> ```
> 
> Examples:
> 
> A discharge PDF links to:
> 
> ```text
> care.events
> care.medications
> care.treatment_plans
> care.care_notes
> care.vitals
> ```
> 
> A POA document links to:
> 
> ```text
> care.patients
> care.contacts
> care.legal_documents
> ```
> 
> This keeps the system modular. One document, many relationships. Clean.
> 
> ---
> 
> ## 4. Add document OCR/extraction later, not in MVP
> 
> For MVP, store PDFs and manually enter title/type/date/tags/summary.
> 
> Later, add:
> 
> ```sql
> create table if not exists care.document_extractions (
>   id uuid primary key default gen_random_uuid(),
> 
>   document_id uuid not null references care.documents(id) on delete cascade,
>   patient_id uuid not null references care.patients(id) on delete cascade,
> 
>   extraction_type text not null default 'ocr',
>   extracted_text text,
>   extracted_json jsonb not null default '{}'::jsonb,
> 
>   model_name text,
>   confidence_score numeric,
> 
>   created_at timestamptz not null default now()
> );
> ```
> 
> That becomes the future AI/search layer. But don’t start there. That’s how projects get bloated and die in a ditch.
> 
> ---
> 
> ## 5. App UI: simple vault sections
> 
> The admin view should have a **Documents / Vault** section with:
> 
> ### Main document table
> 
> Columns:
> 
> ```text
> Title
> Type
> Date
> Source
> Tags
> Sensitive?
> Linked To
> Uploaded At
> Actions
> ```
> 
> Actions:
> 
> ```text
> View
> Download
> Edit Metadata
> Link to Event
> Link to Med
> Link to Visit
> Archive
> ```
> 
> ### Upload form
> 
> Fields:
> 
> ```text
> File
> Title
> Document Type
> Document Date
> Source / Provider
> Tags
> Summary / Notes
> Sensitive toggle
> Legal document toggle
> Medical record toggle
> ```
> 
> ### Filters
> 
> ```text
> Medical
> Legal
> Insurance
> Medication
> Labs
> Hospital
> Oxygen / Equipment
> Needs Review
> ```
> 
> This is the part that matters most: **the vault must answer “what is this, why do we care, and where does it connect?”**
> 
> ---
> 
> ## 6. Security rules
> 
> Use private storage and RLS. Supabase recommends enabling RLS for exposed tables, and Supabase Storage integrates with Postgres RLS for access control. citeturn759663search9turn759663search0
> 
> Minimum approach:
> 
> ```sql
> alter table care.documents enable row level security;
> alter table care.document_links enable row level security;
> alter table care.document_extractions enable row level security;
> ```
> 
> Then policy direction:
> 
> ```text
> Only authenticated authorized caregivers can view Mom's documents.
> Only admin/primary caregiver can upload, edit, archive, or delete.
> Signed URLs should expire quickly.
> Never use public URLs for medical/legal PDFs.
> ```
> 
> Also: don’t store sensitive medical document metadata only in `storage.objects`. Use your own `care.documents` table because it gives you stable relational control and richer metadata. Supabase upload supports file options like content type and metadata, but for this app your real metadata belongs in Postgres. citeturn759663search4
> 
> ---
> 
> ## 7. Best MVP version
> 
> Build only this first:
> 
> ```text
> Private Storage Bucket
> care.documents
> care.document_links
> Admin upload page
> Document list/table
> View/download with signed URL
> Manual summary + tags
> Link document to event/med/visit/patient
> ```
> 
> Skip for now:
> 
> ```text
> AI extraction
> OCR
> Vector search
> Auto-classification
> Document versioning
> Complex permissions
> ```
> 
> Those are useful later, but right now they are shiny-object tax.
> 
> ---
> 
> ## Codex prompt
> 
> Use this:
> 
> ```text
> Update the Mom Care app to add a Document Vault for storing and managing PDF documents.
> 
> Goal:
> Create a secure document vault for Mom's medical, legal, insurance, equipment, medication, hospital, and care-plan documents. Files should be stored in Supabase Storage, while document metadata and relationships should be stored in Postgres under the care schema.
> 
> Requirements:
> 
> 1. Supabase Storage
> - Use a private Supabase Storage bucket named care-documents.
> - Store files using this path pattern:
>   patients/{patient_id}/documents/{document_id}/{original_filename}
> - Do not use public URLs.
> - Use signed URLs for viewing/downloading documents.
> 
> 2. Database tables
> Create or support these tables if they do not already exist:
> 
> care.documents:
> - id uuid primary key default gen_random_uuid()
> - patient_id uuid references care.patients(id) on delete cascade
> - title text not null
> - document_type text not null
> - document_date date
> - source_name text
> - source_org text
> - storage_bucket text default 'care-documents'
> - storage_path text not null
> - original_filename text
> - mime_type text default 'application/pdf'
> - file_size_bytes bigint
> - status text default 'active'
> - is_sensitive boolean default true
> - is_legal_document boolean default false
> - is_medical_record boolean default true
> - summary text
> - notes text
> - tags text[] default '{}'
> - uploaded_by uuid
> - uploaded_at timestamptz default now()
> - created_at timestamptz default now()
> - updated_at timestamptz default now()
> - metadata_json jsonb default '{}'::jsonb
> 
> care.document_links:
> - id uuid primary key default gen_random_uuid()
> - patient_id uuid references care.patients(id) on delete cascade
> - document_id uuid references care.documents(id) on delete cascade
> - linked_table text not null
> - linked_id uuid not null
> - link_type text default 'related'
> - notes text
> - created_at timestamptz default now()
> - metadata_json jsonb default '{}'::jsonb
> 
> Optional future table, scaffold only if easy:
> care.document_extractions:
> - id uuid primary key default gen_random_uuid()
> - document_id uuid references care.documents(id) on delete cascade
> - patient_id uuid references care.patients(id) on delete cascade
> - extraction_type text default 'ocr'
> - extracted_text text
> - extracted_json jsonb default '{}'::jsonb
> - model_name text
> - confidence_score numeric
> - created_at timestamptz default now()
> 
> 3. UI
> Add a new Admin section called Document Vault.
> 
> The Document Vault page should include:
> - document table/list
> - upload form
> - edit metadata form
> - view/download action using signed URL
> - archive action
> - filters by document_type, tags, source, date, and status
> 
> Table columns:
> - Title
> - Type
> - Date
> - Source
> - Tags
> - Sensitive
> - Legal
> - Medical
> - Uploaded At
> - Actions
> 
> Upload form fields:
> - file
> - title
> - document_type
> - document_date
> - source_name
> - source_org
> - tags
> - summary
> - notes
> - is_sensitive
> - is_legal_document
> - is_medical_record
> 
> 4. Document types
> Use these initial document_type options:
> - discharge_summary
> - lab_report
> - imaging_report
> - medication_list
> - visit_summary
> - insurance
> - legal
> - advance_directive
> - poa_medical
> - poa_financial
> - hipaa_release
> - care_plan
> - therapy_note
> - oxygen_equipment
> - prescription
> - other
> 
> 5. Linking
> Allow a document to be linked to other app records using care.document_links.
> At minimum, support linking to:
> - patient
> - care event
> - medication
> - treatment plan
> - care note
> - oxygen equipment/tank record if available
> 
> 6. Security
> - Assume care-documents is private.
> - Do not expose public URLs.
> - Generate signed URLs only when the user clicks view/download.
> - Respect existing auth/session patterns.
> - Do not weaken existing RLS or permissions.
> 
> 7. Implementation style
> - Keep the UI simple and admin-focused.
> - Reuse existing Supabase client, types, components, layouts, and admin patterns.
> - Add/update TypeScript types as needed.
> - Do not break existing attachments/events functionality.
> - If an attachments table already exists, do not delete it. The Document Vault should either coexist with it or use it only if that is already the app pattern.
> - Prefer additive changes over destructive migrations.
> 
> Deliverables:
> - SQL migration for new tables if needed.
> - Supabase storage integration.
> - Admin Document Vault route/page.
> - Upload, list, edit, archive, view/download actions.
> - Updated types.
> - Basic error handling.
> - Clear comments where future OCR/vector search can be added.
> ```
> 
> ## My blunt recommendation
> 
> Use **Document Vault** as the official system.
> 
> Keep `attachments` as lightweight files tied to events if it already exists, but don’t let it become the main medical record system. That’s the wrong abstraction.
> 
> The hierarchy should be:
> 
> ```text
> Document Vault = official PDFs and records
> Attachments = incidental supporting files
> Events = what happened
> Document Links = how PDFs connect to what happened
> ```
> 
> That’s clean, scalable, and won’t make future-you want to throw the laptop.

### User
> ok we have a mess going on in momscare docs, # File Tree: docs
> 
> **Generated:** 5/18/2026, 10:55:46 PM
> **Root Path:** `c:\QiLabs\apps\MomsCare\docs`
> 
> ```
> ├── 10_holistic_care_binder
> │   ├── 10_fast_access
> │   │   ├── _index.md
> │   │   ├── emergency_contacts_and_safety.md
> │   │   ├── emergency_grab_sheet.md
> │   │   ├── executive_care_summary.md
> │   │   └── medication_list.md
> │   ├── 20_daily_operations
> │   │   ├── _index.md
> │   │   ├── daily_care_plan.md
> │   │   ├── medication_schedule.md
> │   │   └── mobility_hygiene_nutrition_and_logs.md
> │   ├── 30_medical
> │   │   ├── _index.md
> │   │   ├── medical_history_and_diagnoses.md
> │   │   ├── provider_directory_and_appointments.md
> │   │   └── treatments_health_education_and_visit_notes.md
> │   ├── 40_home_and_supplies
> │   │   ├── _index.md
> │   │   ├── equipment_and_supply_inventory.md
> │   │   └── station_map_restock_and_home_safety.md
> │   ├── 50_care_team
> │   │   ├── _index.md
> │   │   ├── care_team_directory_and_roles.md
> │   │   └── caregiver_onboarding_and_communication.md
> │   ├── 60_legal_admin_end_of_life
> │   │   ├── _index.md
> │   │   ├── administrative_access_and_after_death_checklist.md
> │   │   ├── advance_directive_last_wishes_summary.md
> │   │   └── legal_authority_hipaa_poa_summary.md
> │   ├── 70_goals_and_review
> │   │   ├── _index.md
> │   │   └── goals_progress_and_review.md
> │   ├── 00_start_here.md
> │   ├── 01_binder_cover_sheet.md
> │   ├── 02_print_assembly_and_tab_guide.md
> │   ├── 05_master_outline.md
> │   └── _index.md
> ├── 20_patient_record_archive
> │   ├── files
> │   │   └── template-patient
> │   │       ├── 00_intake
> │   │       │   └── .gitkeep
> │   │       ├── 10_pdf_packets
> │   │       │   └── .gitkeep
> │   │       ├── 20_ocr_text
> │   │       │   └── ocr_status.json
> │   │       ├── 30_clinical_history
> │   │       │   └── health_history_starter.txt
> │   │       ├── 40_rag_exports
> │   │       │   └── chunk_manifest.json
> │   │       ├── 50_archive
> │   │       │   └── .gitkeep
> │   │       └── manifest.json
> │   ├── _index.md
> │   ├── archive_operating_guide.md
> │   ├── ocr_and_rag_pipeline.md
> │   ├── patient_folder_template.md
> │   └── pdf_repo_rules.md
> ├── kb
> │   ├── 01_care
> │   │   ├── 02_healthcare_representative.html
> │   │   ├── 03_hipaa_living_will.html
> │   │   ├── 04202026_-_- aR Deaconess Health System.pdf
> │   │   ├── 08_caregiver.html
> │   │   ├── 09_labels.html
> │   │   ├── Clinical Care Guide_ COPD Stability & Biologic Therapy Initiation.md
> │   │   ├── contacts.html
> │   │   ├── daily-care.html
> │   │   └── medical.html
> │   ├── 02_legal_financial
> │   │   ├── 05_durable_poa_financial.html
> │   │   ├── 06_estate_interim_authority.html
> │   │   ├── 08_execution_notary.html
> │   │   ├── 10_executed_docs.html
> │   │   ├── finance.html
> │   │   └── legal.html
> │   ├── 04_housing
> │   │   └── index.html
> │   ├── 07_incident_log
> │   │   └── 07_incident_log.html
> │   ├── 07_safety
> │   │   ├── 01_emergency_protocol.html
> │   │   └── 04_emergency_access.html
> │   ├── assets
> │   │   ├── css
> │   │   │   └── manual.css
> │   │   └── imgs
> │   │       ├── COPD---Obstructive-Chronic-Bronchitis-or-Emphysema.jpg
> │   │       ├── COPD-ENHANCED.jpg
> │   │       ├── COPD-EXCERT.jpg
> │   │       └── COPD.jpg
> │   ├── 07_vault.html
> │   ├── index.html
> │   └── kb.html
> ├── reference
> │   ├── App.tsx
> │   ├── api.ts
> │   ├── index.css
> │   ├── index.html
> │   ├── index.tsx
> │   └── qicare.css
> ├── templates
> │   ├── components
> │   │   ├── CautionCard.tsx
> │   │   ├── NextDueCard.tsx
> │   │   ├── RightNowCard.tsx
> │   │   ├── TimerCard.tsx
> │   │   └── VoiceInput.tsx
> │   ├── engine
> │   │   ├── decisionEngine.ts
> │   │   ├── safetyEngine.ts
> │   │   ├── timerEngine.ts
> │   │   └── voiceParser.ts
> │   ├── hooks
> │   │   ├── useNotifications.ts
> │   │   ├── useTimers.ts
> │   │   └── useVoice.ts
> │   └── pages
> │       ├── ProtocolsPage.tsx
> │       ├── QuickLogPage.tsx
> │       └── SafetyPage.tsx
> ├── Caregiver Care Plan Wiki.html
> ├── TRAINING.md
> ├── _index.md
> ├── care_app_erd.mmd
> ├── frontend-feature-coverage.md
> ├── frontend-supabase-audit.md
> └── momcare-desktop-admin-schema-report.md
> ```
> 
> ---
> *Generated by FileTree Pro Extension*

### Assistant
> Yep, that tree is doing three different jobs at once: printable binder, patient archive, and app/dev docs. We need split by **audience + lifecycle**, not by whatever file happened to exist first.

### Assistant
> You’re right: this is messy, but it’s not hopeless. The problem is **not the content**. The problem is that `docs/` currently contains:
> 
> 1. **Mom-facing printable care binder**
> 2. **Patient record archive / PDF vault**
> 3. **Knowledge base HTML/manual content**
> 4. **Developer docs**
> 5. **Reference app code**
> 6. **Templates / prototype components**
> 
> That is too many meanings for one folder. Future-you will absolutely get lost.
> 
> ## The clean structure I’d use
> 
> Restructure `docs` like this:
> 
> ```text
> docs
> ├── 00_README.md
> ├── 01_product
> │   ├── app_goals.md
> │   ├── mvp_scope.md
> │   ├── roadmap.md
> │   └── workflow_codex_gemini_aider.md
> ├── 02_architecture
> │   ├── database
> │   │   ├── care_schema_overview.md
> │   │   ├── care_app_erd.mmd
> │   │   ├── frontend-supabase-audit.md
> │   │   └── momcare-desktop-admin-schema-report.md
> │   ├── frontend
> │   │   ├── frontend-feature-coverage.md
> │   │   └── ui_navigation_model.md
> │   └── integrations
> │       ├── supabase_storage.md
> │       ├── document_vault.md
> │       └── notifications.md
> ├── 03_care_binder
> │   ├── 00_start_here.md
> │   ├── 01_binder_cover_sheet.md
> │   ├── 02_print_assembly_and_tab_guide.md
> │   ├── 05_master_outline.md
> │   ├── 10_fast_access
> │   ├── 20_daily_operations
> │   ├── 30_medical
> │   ├── 40_home_and_supplies
> │   ├── 50_care_team
> │   ├── 60_legal_admin_end_of_life
> │   └── 70_goals_and_review
> ├── 04_patient_record_archive
> │   ├── _index.md
> │   ├── archive_operating_guide.md
> │   ├── ocr_and_rag_pipeline.md
> │   ├── patient_folder_template.md
> │   ├── pdf_repo_rules.md
> │   └── files
> ├── 05_knowledge_base
> │   ├── care
> │   ├── legal_financial
> │   ├── housing
> │   ├── safety
> │   ├── incident_log
> │   ├── assets
> │   └── index.md
> ├── 06_templates
> │   ├── components
> │   ├── engine
> │   ├── hooks
> │   └── pages
> ├── 07_reference_app
> │   ├── App.tsx
> │   ├── api.ts
> │   ├── index.css
> │   ├── index.html
> │   ├── index.tsx
> │   └── qicare.css
> ├── 90_archive
> │   └── old_unsorted
> └── TRAINING.md
> ```
> 
> ## What moves where
> 
> ### Current `10_holistic_care_binder`
> 
> Move to:
> 
> ```text
> docs/03_care_binder
> ```
> 
> This is the printable / human-readable care binder.
> 
> Keep its internal structure mostly the same. That part is actually decent.
> 
> ---
> 
> ### Current `20_patient_record_archive`
> 
> Move to:
> 
> ```text
> docs/04_patient_record_archive
> ```
> 
> This is the offline/source-file archive system.
> 
> It should support:
> 
> ```text
> raw PDFs
> OCR text
> RAG exports
> clinical history extraction
> manifest files
> archive rules
> ```
> 
> This is related to the app vault, but it is **not the same thing** as the app vault.
> 
> The distinction:
> 
> ```text
> App Document Vault = live app feature
> Patient Record Archive = repo/file-system source archive
> ```
> 
> Do not blur those. That’s how chaos sneaks back in wearing a fake mustache.
> 
> ---
> 
> ### Current `kb`
> 
> Move to:
> 
> ```text
> docs/05_knowledge_base
> ```
> 
> This is education/reference content.
> 
> But I’d eventually convert the scattered `.html` files into `.md` unless they are intentionally designed web pages.
> 
> Example:
> 
> ```text
> kb/01_care/daily-care.html
> ```
> 
> should probably become:
> 
> ```text
> docs/05_knowledge_base/care/daily_care.md
> ```
> 
> Not urgent, but that’s the long-term cleanup.
> 
> ---
> 
> ### Current `reference`
> 
> Move to:
> 
> ```text
> docs/07_reference_app
> ```
> 
> These are not docs. They’re reference implementation files. Keep them separate so Codex doesn’t confuse them with active app code.
> 
> ---
> 
> ### Current `templates`
> 
> Move to:
> 
> ```text
> docs/06_templates
> ```
> 
> These look like reusable UI/logic templates. That’s fine, but they need a README explaining:
> 
> ```text
> Are these active?
> Are these examples?
> Are these meant to be copied into src/?
> Are these deprecated?
> ```
> 
> Without that, they are zombie code.
> 
> ---
> 
> ### Current root docs
> 
> Move these:
> 
> ```text
> care_app_erd.mmd
> frontend-feature-coverage.md
> frontend-supabase-audit.md
> momcare-desktop-admin-schema-report.md
> ```
> 
> to:
> 
> ```text
> docs/02_architecture/database
> ```
> 
> or:
> 
> ```text
> docs/02_architecture/frontend
> ```
> 
> Specifically:
> 
> ```text
> care_app_erd.mmd
> → docs/02_architecture/database/care_app_erd.mmd
> 
> frontend-supabase-audit.md
> → docs/02_architecture/database/frontend-supabase-audit.md
> 
> momcare-desktop-admin-schema-report.md
> → docs/02_architecture/database/momcare-desktop-admin-schema-report.md
> 
> frontend-feature-coverage.md
> → docs/02_architecture/frontend/frontend-feature-coverage.md
> ```
> 
> Move:
> 
> ```text
> Caregiver Care Plan Wiki.html
> ```
> 
> to either:
> 
> ```text
> docs/05_knowledge_base/care/caregiver_care_plan_wiki.html
> ```
> 
> or archive it if it’s old.
> 
> Keep:
> 
> ```text
> TRAINING.md
> ```
> 
> at root if it is a repo-wide training file. Otherwise move it to:
> 
> ```text
> docs/01_product/workflow_codex_gemini_aider.md
> ```
> 
> ---
> 
> ## The key rule
> 
> Every folder needs to answer one question:
> 
> ```text
> Who is this for?
> ```
> 
> Use this map:
> 
> ```text
> 01_product              = you, Codex, planning
> 02_architecture         = developer / database / app structure
> 03_care_binder          = Mom, caregivers, printable binder
> 04_patient_record_archive = source PDFs, OCR, record management
> 05_knowledge_base       = reference education and policies
> 06_templates            = reusable code/design templates
> 07_reference_app        = prototype/reference code
> 90_archive              = old stuff we do not trust yet
> ```
> 
> That’s the spine.
> 
> ## Add this root README
> 
> Create:
> 
> ```text
> docs/00_README.md
> ```
> 
> With this:
> 
> ```md
> # MomsCare Documentation Map
> 
> This docs folder is organized by audience and purpose.
> 
> ## 01_product
> Product goals, MVP scope, roadmap, and development workflow notes.
> 
> ## 02_architecture
> Technical documentation for database schema, frontend structure, app modules, Supabase, storage, and integrations.
> 
> ## 03_care_binder
> Printable and caregiver-facing holistic care binder for Mom. This is the human-readable care packet.
> 
> ## 04_patient_record_archive
> Offline/source-file archive for PDFs, OCR text, RAG exports, manifests, and patient document processing.
> 
> ## 05_knowledge_base
> Reference material, care education, safety guides, legal/financial info, and supporting web/manual content.
> 
> ## 06_templates
> Reusable UI, logic, hooks, and page templates. These are not necessarily active production files.
> 
> ## 07_reference_app
> Reference app/prototype files used for design or implementation inspiration.
> 
> ## 90_archive
> Old, duplicate, deprecated, or unsorted files that should not be treated as current without review.
> 
> ## Rule
> Do not add loose files to docs root unless they explain the documentation system itself.
> ```
> 
> ## Codex prompt to clean this up safely
> 
> Use this:
> 
> ```text
> We need to reorganize the MomsCare docs folder because it currently mixes the care binder, patient record archive, knowledge base, developer docs, reference app code, and templates.
> 
> Goal:
> Reorganize docs by audience and purpose without deleting content.
> 
> Current root:
> docs/
> 
> Target structure:
> 
> docs/
> ├── 00_README.md
> ├── 01_product/
> ├── 02_architecture/
> │   ├── database/
> │   ├── frontend/
> │   └── integrations/
> ├── 03_care_binder/
> ├── 04_patient_record_archive/
> ├── 05_knowledge_base/
> ├── 06_templates/
> ├── 07_reference_app/
> ├── 90_archive/
> │   └── old_unsorted/
> └── TRAINING.md
> 
> Move rules:
> 
> 1. Move current docs/10_holistic_care_binder to:
>    docs/03_care_binder
> 
> 2. Move current docs/20_patient_record_archive to:
>    docs/04_patient_record_archive
> 
> 3. Move current docs/kb to:
>    docs/05_knowledge_base
> 
> 4. Move current docs/templates to:
>    docs/06_templates
> 
> 5. Move current docs/reference to:
>    docs/07_reference_app
> 
> 6. Move database/schema/dev docs:
>    docs/care_app_erd.mmd
>    → docs/02_architecture/database/care_app_erd.mmd
> 
>    docs/frontend-supabase-audit.md
>    → docs/02_architecture/database/frontend-supabase-audit.md
> 
>    docs/momcare-desktop-admin-schema-report.md
>    → docs/02_architecture/database/momcare-desktop-admin-schema-report.md
> 
>    docs/frontend-feature-coverage.md
>    → docs/02_architecture/frontend/frontend-feature-coverage.md
> 
> 7. Move docs/Caregiver Care Plan Wiki.html to:
>    docs/05_knowledge_base/care/caregiver_care_plan_wiki.html
> 
> 8. Keep TRAINING.md at docs/TRAINING.md for now unless there is a better existing workflow location.
> 
> 9. Create docs/00_README.md explaining the documentation map.
> 
> 10. Create placeholder README.md files in:
>    docs/01_product/
>    docs/02_architecture/
>    docs/02_architecture/database/
>    docs/02_architecture/frontend/
>    docs/02_architecture/integrations/
>    docs/03_care_binder/
>    docs/04_patient_record_archive/
>    docs/05_knowledge_base/
>    docs/06_templates/
>    docs/07_reference_app/
>    docs/90_archive/
> 
> Important:
> - Do not delete any files.
> - Preserve git history as much as possible using git mv where possible.
> - Do not modify app source code.
> - Do not rename content files internally yet except the moved Caregiver Care Plan Wiki.html if safe.
> - After moving files, search for broken relative links inside markdown/html files and report them.
> - Update links only where obvious and safe.
> - Provide a final summary of moved files and any broken links that need manual review.
> ```
> 
> ## Optional PowerShell move script
> 
> Run from:
> 
> ```text
> c:\QiLabs\apps\MomsCare
> ```
> 
> ```powershell
> mkdir docs\01_product -Force
> mkdir docs\02_architecture\database -Force
> mkdir docs\02_architecture\frontend -Force
> mkdir docs\02_architecture\integrations -Force
> mkdir docs\90_archive\old_unsorted -Force
> 
> git mv docs\10_holistic_care_binder docs\03_care_binder
> git mv docs\20_patient_record_archive docs\04_patient_record_archive
> git mv docs\kb docs\05_knowledge_base
> git mv docs\templates docs\06_templates
> git mv docs\reference docs\07_reference_app
> 
> git mv docs\care_app_erd.mmd docs\02_architecture\database\care_app_erd.mmd
> git mv docs\frontend-supabase-audit.md docs\02_architecture\database\frontend-supabase-audit.md
> git mv docs\momcare-desktop-admin-schema-report.md docs\02_architecture\database\momcare-desktop-admin-schema-report.md
> git mv docs\frontend-feature-coverage.md docs\02_architecture\frontend\frontend-feature-coverage.md
> 
> mkdir docs\05_knowledge_base\care -Force
> git mv "docs\Caregiver Care Plan Wiki.html" "docs\05_knowledge_base\care\caregiver_care_plan_wiki.html"
> ```
> 
> Then add the README:
> 
> ```powershell
> @"
> # MomsCare Documentation Map
> 
> This docs folder is organized by audience and purpose.
> 
> ## 01_product
> Product goals, MVP scope, roadmap, and development workflow notes.
> 
> ## 02_architecture
> Technical documentation for database schema, frontend structure, app modules, Supabase, storage, and integrations.
> 
> ## 03_care_binder
> Printable and caregiver-facing holistic care binder for Mom. This is the human-readable care packet.
> 
> ## 04_patient_record_archive
> Offline/source-file archive for PDFs, OCR text, RAG exports, manifests, and patient document processing.
> 
> ## 05_knowledge_base
> Reference material, care education, safety guides, legal/financial info, and supporting web/manual content.
> 
> ## 06_templates
> Reusable UI, logic, hooks, and page templates. These are not necessarily active production files.
> 
> ## 07_reference_app
> Reference app/prototype files used for design or implementation inspiration.
> 
> ## 90_archive
> Old, duplicate, deprecated, or unsorted files that should not be treated as current without review.
> 
> ## Rule
> Do not add loose files to docs root unless they explain the documentation system itself.
> "@ | Set-Content docs\00_README.md
> ```
> 
> ## The bigger strategic point
> 
> You actually have **two systems** that should stay separate:
> 
> ```text
> Care Binder
> ```
> 
> This is for humans. It should be printable, readable, and calm.
> 
> ```text
> Document Vault / Patient Archive
> ```
> 
> This is for records, PDFs, OCR, search, app ingestion, and evidence.
> 
> Do not merge those.
> 
> The binder can reference vault documents, but the binder should not become the vault.
> 
> Clean relationship:
> 
> ```text
> 03_care_binder
> = summary, instructions, daily care, emergency sheets
> 
> 04_patient_record_archive
> = PDFs, OCR, source files, manifests, RAG exports
> 
> App Document Vault
> = database-backed live version inside the app
> ```
> 
> That’s the right architecture. Everything else is folder goblin behavior.

### User
> go ahead and give me the vault built out with purposeful folder my goal is not to make new folder only add docs

### Assistant
> Got it. Don’t create a brand-new “vault” top-level monster. Use the existing archive area and **add purpose-built docs inside it**.
> 
> Use this as the target:
> 
> ```text
> docs/20_patient_record_archive
> ├── _index.md
> ├── 00_document_vault_overview.md
> ├── 01_folder_map.md
> ├── 02_document_type_taxonomy.md
> ├── 03_file_naming_rules.md
> ├── 04_ingestion_workflow.md
> ├── 05_pdf_storage_and_supabase_mapping.md
> ├── 06_ocr_and_ai_extraction_rules.md
> ├── 07_document_review_checklist.md
> ├── 08_legal_medical_sensitivity_rules.md
> ├── 09_document_linking_model.md
> ├── 10_archive_operating_guide.md
> ├── 11_document_vault_mvp_spec.md
> ├── 12_future_rag_search_plan.md
> ├── files
> │   └── template-patient
> │       ├── 00_intake
> │       ├── 10_pdf_packets
> │       ├── 20_ocr_text
> │       ├── 30_clinical_history
> │       ├── 40_rag_exports
> │       ├── 50_archive
> │       └── manifest.json
> ├── archive_operating_guide.md
> ├── ocr_and_rag_pipeline.md
> ├── patient_folder_template.md
> └── pdf_repo_rules.md
> ```
> 
> This keeps the current folder and adds a real vault brain to it.
> 
> ## Copy/paste Codex prompt
> 
> ```text
> We are not creating a new top-level folder. We are keeping the existing docs/20_patient_record_archive folder and building out the Document Vault documentation inside it.
> 
> Goal:
> Add purposeful markdown documentation files that define how the MomCare Document Vault should work, both for the local repo archive and for the future Supabase-backed app vault.
> 
> Do not delete existing files.
> Do not move existing files.
> Do not rename existing files.
> Only add new markdown docs inside docs/20_patient_record_archive.
> 
> Create these files:
> 
> docs/20_patient_record_archive/00_document_vault_overview.md
> docs/20_patient_record_archive/01_folder_map.md
> docs/20_patient_record_archive/02_document_type_taxonomy.md
> docs/20_patient_record_archive/03_file_naming_rules.md
> docs/20_patient_record_archive/04_ingestion_workflow.md
> docs/20_patient_record_archive/05_pdf_storage_and_supabase_mapping.md
> docs/20_patient_record_archive/06_ocr_and_ai_extraction_rules.md
> docs/20_patient_record_archive/07_document_review_checklist.md
> docs/20_patient_record_archive/08_legal_medical_sensitivity_rules.md
> docs/20_patient_record_archive/09_document_linking_model.md
> docs/20_patient_record_archive/10_archive_operating_guide.md
> docs/20_patient_record_archive/11_document_vault_mvp_spec.md
> docs/20_patient_record_archive/12_future_rag_search_plan.md
> 
> Also update docs/20_patient_record_archive/_index.md to link to the new files.
> 
> Content requirements:
> 
> 1. 00_document_vault_overview.md
> Explain the purpose of the Document Vault.
> Clarify that this folder is the local/repo documentation and archive model, while the app Document Vault will store metadata in Supabase and PDFs in Supabase Storage.
> Explain the difference between:
> - Care Binder
> - Patient Record Archive
> - App Document Vault
> - Knowledge Base
> 
> 2. 01_folder_map.md
> Document the existing patient archive folder structure:
> files/template-patient/00_intake
> files/template-patient/10_pdf_packets
> files/template-patient/20_ocr_text
> files/template-patient/30_clinical_history
> files/template-patient/40_rag_exports
> files/template-patient/50_archive
> Explain what belongs in each folder.
> Include examples.
> 
> 3. 02_document_type_taxonomy.md
> Define document types:
> - discharge_summary
> - lab_report
> - imaging_report
> - medication_list
> - visit_summary
> - insurance
> - legal
> - advance_directive
> - poa_medical
> - poa_financial
> - hipaa_release
> - care_plan
> - therapy_note
> - oxygen_equipment
> - prescription
> - billing
> - equipment_manual
> - caregiver_note
> - other
> For each type include:
> - description
> - examples
> - whether medical/legal/sensitive
> - suggested tags
> 
> 4. 03_file_naming_rules.md
> Define clear file naming rules.
> Recommended format:
> YYYY-MM-DD__source__document-type__short-description.pdf
> 
> Examples:
> 2026-05-05__deaconess__discharge-summary__copd-exacerbation.pdf
> 2026-05-04__deaconess__lab-report__renal-profile.pdf
> 2026-05-01__walmart-pharmacy__medication-list__current-meds.pdf
> 
> Include rules:
> - lowercase preferred
> - use hyphens instead of spaces
> - no special characters
> - preserve original if uncertain
> - never overwrite original files
> - if duplicate, append __v2 or __duplicate-review
> 
> 5. 04_ingestion_workflow.md
> Define workflow:
> Step 1: receive/download PDF
> Step 2: place in intake
> Step 3: rename if safe
> Step 4: classify document type
> Step 5: add to manifest
> Step 6: OCR if needed
> Step 7: extract summary
> Step 8: link to app records
> Step 9: archive original
> Step 10: review status
> 
> Include status values:
> - new
> - needs_review
> - classified
> - ocr_complete
> - summarized
> - linked
> - archived
> - rejected_duplicate
> 
> 6. 05_pdf_storage_and_supabase_mapping.md
> Document future app storage:
> Supabase Storage private bucket:
> care-documents
> 
> Path:
> patients/{patient_id}/documents/{document_id}/{original_filename}
> 
> Metadata table:
> care.documents
> 
> Relationship table:
> care.document_links
> 
> Extraction table:
> care.document_extractions
> 
> Explain that the file is stored in Storage and the searchable metadata is stored in Postgres.
> Include the recommended columns for care.documents and care.document_links.
> 
> 7. 06_ocr_and_ai_extraction_rules.md
> Document OCR and AI extraction rules.
> Explain that OCR text should not replace the original PDF.
> OCR output goes in 20_ocr_text.
> Summaries/extractions should identify:
> - document date
> - provider/source
> - diagnoses
> - medications
> - orders/instructions
> - follow-up dates
> - abnormal findings
> - risks/warnings
> - caregiver action items
> 
> Include warning:
> AI summaries are support tools, not the legal/medical source of truth.
> 
> 8. 07_document_review_checklist.md
> Create a checklist for reviewing each document:
> - Is the document readable?
> - Is the date clear?
> - Is the provider/source clear?
> - Is the patient name visible?
> - Is this duplicate?
> - Is it medical/legal/financial?
> - Does it require caregiver action?
> - Does it affect medications?
> - Does it affect oxygen/treatments?
> - Does it need to be linked to a care event?
> - Does it belong in the care binder summary?
> 
> 9. 08_legal_medical_sensitivity_rules.md
> Document sensitivity rules.
> Legal, HIPAA, POA, advance directives, insurance, billing, diagnoses, medication, and hospital docs are sensitive.
> Never make public URLs.
> Never commit real private PDFs unless repo privacy is confirmed.
> Use placeholders for template examples.
> Access should be role-based in the app.
> Signed URLs only for viewing/downloading.
> 
> 10. 09_document_linking_model.md
> Explain how documents should link to app records.
> Examples:
> A discharge summary can link to:
> - care event
> - medication changes
> - treatment plan
> - provider visit
> - oxygen change
> - follow-up task
> 
> A POA document can link to:
> - patient
> - caregiver/contact
> - legal authority section
> 
> A lab report can link to:
> - lab event
> - abnormal result
> - care note
> - provider follow-up
> 
> 11. 10_archive_operating_guide.md
> Create a practical operating guide for the archive.
> This should be a daily/weekly workflow document for Cody.
> Keep it simple and direct.
> Include:
> - what to do when a new PDF arrives
> - what not to overthink
> - what needs review
> - what belongs in the care binder
> - what belongs only in the vault
> - weekly cleanup checklist
> 
> 12. 11_document_vault_mvp_spec.md
> Create the MVP product spec for the in-app Document Vault.
> Include:
> - purpose
> - user stories
> - required database tables
> - storage bucket
> - upload flow
> - document list
> - filters
> - signed download/view
> - edit metadata
> - archive document
> - link to records
> - non-goals for MVP
> 
> 13. 12_future_rag_search_plan.md
> Document the future plan for search/RAG.
> Include:
> - OCR text
> - chunking
> - embeddings
> - local-first option
> - Supabase structured metadata remains source of truth
> - AI assistant can answer questions using citations back to document records
> - do not build this before the basic vault works
> 
> Index update:
> Update docs/20_patient_record_archive/_index.md with links to all new docs and a short explanation of the archive/vault purpose.
> 
> Tone:
> Clear, practical, structured, direct.
> This is caregiver/admin documentation, not corporate fluff.
> Use markdown headings, checklists, and tables where useful.
> ```
> 
> ## Starter content for `_index.md`
> 
> Use this if you want Codex to overwrite or clean the current index:
> 
> ```md
> # Patient Record Archive & Document Vault
> 
> This folder defines the local archive and future app-backed Document Vault for MomCare.
> 
> The goal is to keep medical, legal, insurance, equipment, medication, hospital, and care-plan documents organized, searchable, reviewable, and connected to actual care activity.
> 
> ## Core Docs
> 
> - [00 Document Vault Overview](00_document_vault_overview.md)
> - [01 Folder Map](01_folder_map.md)
> - [02 Document Type Taxonomy](02_document_type_taxonomy.md)
> - [03 File Naming Rules](03_file_naming_rules.md)
> - [04 Ingestion Workflow](04_ingestion_workflow.md)
> - [05 PDF Storage and Supabase Mapping](05_pdf_storage_and_supabase_mapping.md)
> - [06 OCR and AI Extraction Rules](06_ocr_and_ai_extraction_rules.md)
> - [07 Document Review Checklist](07_document_review_checklist.md)
> - [08 Legal and Medical Sensitivity Rules](08_legal_medical_sensitivity_rules.md)
> - [09 Document Linking Model](09_document_linking_model.md)
> - [10 Archive Operating Guide](10_archive_operating_guide.md)
> - [11 Document Vault MVP Spec](11_document_vault_mvp_spec.md)
> - [12 Future RAG Search Plan](12_future_rag_search_plan.md)
> 
> ## Existing Archive Docs
> 
> - [Archive Operating Guide](archive_operating_guide.md)
> - [OCR and RAG Pipeline](ocr_and_rag_pipeline.md)
> - [Patient Folder Template](patient_folder_template.md)
> - [PDF Repo Rules](pdf_repo_rules.md)
> 
> ## Folder Purpose
> 
> This folder is not the care binder.
> 
> The care binder summarizes what humans need to know quickly.
> 
> This archive stores and governs the source documents, extracted text, manifests, OCR outputs, and future search/RAG material.
> 
> ## System Relationship
> 
> ```text
> Care Binder
> = human-facing summary and printable packet
> 
> Patient Record Archive
> = local/repo source document system
> 
> App Document Vault
> = Supabase-backed document storage, metadata, and linking
> 
> Knowledge Base
> = general education, reference, and care guidance
> ```
> 
> ## Rule
> 
> Original documents are source-of-truth assets. Summaries, OCR text, and AI extractions support review, but they do not replace the original PDF.
> ```
> 
> ## The important decision
> 
> This is the right call:
> 
> ```text
> Do not create more folders just because things feel messy.
> ```
> 
> The vault belongs inside:
> 
> ```text
> docs/20_patient_record_archive
> ```
> 
> because that folder already means:
> 
> ```text
> source records, PDFs, OCR, archive, RAG prep
> ```
> 
> So we don’t sprawl. We add the missing operating system.

### User
> no i mean like it would have eobs, vist summaries, discharges, test results ect.

### Assistant
> Yes — exactly. You mean the **actual document categories Mom’s vault should contain**, not more meta-docs. Good catch. I was over-documenting the documentation. Classic folder goblin trap.
> 
> For Mom’s app, the vault should be organized by **real-world record type**:
> 
> ```text
> Document Vault
> ├── 00_inbox_needs_review
> ├── 01_emergency_and_identity
> ├── 02_visit_summaries
> ├── 03_discharge_and_hospital
> ├── 04_test_results
> ├── 05_imaging_and_procedures
> ├── 06_medications_and_prescriptions
> ├── 07_treatment_plans_and_orders
> ├── 08_oxygen_equipment_and_supplies
> ├── 09_insurance_billing_and_eobs
> ├── 10_legal_hipaa_and_poa
> ├── 11_care_team_and_contacts
> ├── 12_home_health_pt_ot_nursing
> ├── 13_symptom_logs_and_care_notes
> ├── 14_education_and_reference
> └── 90_archive_duplicates_old
> ```
> 
> ## What belongs in each section
> 
> ### `00_inbox_needs_review`
> 
> Temporary holding area.
> 
> Use for anything newly downloaded, scanned, photographed, or exported from MyChart before it is classified.
> 
> Examples:
> 
> ```text
> new MyChart PDF
> photo of discharge papers
> pharmacy printout
> insurance letter
> unread EOB
> lab result not reviewed yet
> ```
> 
> Rule: nothing should live here forever.
> 
> ---
> 
> ### `01_emergency_and_identity`
> 
> Fast-access documents that prove who she is, what matters in an emergency, or what someone needs immediately.
> 
> Examples:
> 
> ```text
> face sheet
> emergency grab sheet
> patient demographics
> photo ID copy
> insurance card copy
> allergy list
> diagnosis summary
> emergency contacts
> preferred hospital
> DNR/POLST/MOST if applicable
> ```
> 
> This is the “oh shit folder.”
> 
> ---
> 
> ### `02_visit_summaries`
> 
> Regular outpatient appointment notes.
> 
> Examples:
> 
> ```text
> primary care visit summary
> pulmonology visit summary
> cardiology visit summary
> pain management visit summary
> specialist notes
> follow-up instructions
> appointment after-visit summary
> ```
> 
> Use this when she went somewhere and came home with a summary, but it was **not** a hospital admission/discharge.
> 
> ---
> 
> ### `03_discharge_and_hospital`
> 
> Hospital, ER, inpatient, observation, and discharge documents.
> 
> Examples:
> 
> ```text
> ER visit summary
> hospital discharge summary
> inpatient discharge instructions
> observation stay notes
> admission paperwork
> transition of care summary
> hospital medication reconciliation
> post-hospital follow-up packet
> ```
> 
> This deserves its own section because discharge docs often contain medication changes, oxygen changes, follow-ups, and red flags.
> 
> ---
> 
> ### `04_test_results`
> 
> Labs and diagnostic results that are mostly text/numbers.
> 
> Examples:
> 
> ```text
> CBC
> CMP
> renal profile
> A1C
> procalcitonin
> urinalysis
> blood gas
> culture results
> pathology report
> pulmonary function test result
> sleep study result
> ```
> 
> For Mom, this is where renal profiles, CBCs, A1C, and procalcitonin results go.
> 
> ---
> 
> ### `05_imaging_and_procedures`
> 
> Imaging reports and procedure documentation.
> 
> Examples:
> 
> ```text
> x-ray report
> CT report
> MRI report
> ultrasound report
> echocardiogram report
> EKG report
> procedure note
> biopsy report
> surgery report
> wound procedure note
> ```
> 
> Actual image files can be referenced here, but the app MVP should focus on PDFs/reports first.
> 
> ---
> 
> ### `06_medications_and_prescriptions`
> 
> Medication lists, pharmacy paperwork, prescriptions, and med changes.
> 
> Examples:
> 
> ```text
> current medication list
> pharmacy printout
> prescription instructions
> prednisone taper sheet
> antibiotic instructions
> controlled medication paperwork
> medication reconciliation
> allergy/adverse reaction notes
> refill history
> ```
> 
> For Mom, this section matters a lot because prednisone, antibiotics, pain meds, breathing meds, and daily meds need clean tracking.
> 
> ---
> 
> ### `07_treatment_plans_and_orders`
> 
> Doctor orders and active care plans.
> 
> Examples:
> 
> ```text
> oxygen order
> nebulizer order
> home health order
> PT order
> OT order
> wound care order
> diet order
> fluid restriction order
> care plan
> COPD action plan
> biologic therapy plan
> follow-up care instructions
> ```
> 
> This is where “what are we supposed to do?” documents live.
> 
> ---
> 
> ### `08_oxygen_equipment_and_supplies`
> 
> Oxygen, durable medical equipment, supply vendors, and home equipment docs.
> 
> Examples:
> 
> ```text
> oxygen tank instructions
> concentrator manual
> portable oxygen paperwork
> DME supplier agreement
> tank refill/delivery records
> equipment serial numbers
> supply order forms
> Powerade/intake support notes if tied to care plan
> gloves/chucks/wipes supply docs
> wheelchair/power chair paperwork
> hospital bed paperwork
> ```
> 
> This can connect directly to your oxygen inventory and station/restock system.
> 
> ---
> 
> ### `09_insurance_billing_and_eobs`
> 
> Insurance, billing, EOBs, claims, approvals, denials.
> 
> Examples:
> 
> ```text
> EOB
> insurance approval
> insurance denial
> prior authorization
> billing statement
> payment receipt
> Medicare/Medicaid paperwork
> benefits summary
> claim status letter
> pharmacy insurance letter
> DME coverage letter
> ```
> 
> This section should be separate from medical docs because the workflow is different: review, dispute, pay, file, ignore, or follow up.
> 
> ---
> 
> ### `10_legal_hipaa_and_poa`
> 
> Legal authority and end-of-life documents.
> 
> Examples:
> 
> ```text
> HIPAA release
> medical power of attorney
> financial power of attorney
> advance directive
> living will
> last wishes
> will/trust summary
> notary/execution documents
> authorized representative forms
> estate/interim authority docs
> after-death checklist
> ```
> 
> This folder should be treated as highly sensitive.
> 
> ---
> 
> ### `11_care_team_and_contacts`
> 
> Provider, caregiver, agency, and contact documentation.
> 
> Examples:
> 
> ```text
> provider directory
> home health agency contacts
> caregiver role sheet
> pharmacy contacts
> DME supplier contacts
> transportation contacts
> case manager notes
> care team instructions
> communication preferences
> ```
> 
> This is not the place for every visit summary. It’s for “who do we contact and what is their role?”
> 
> ---
> 
> ### `12_home_health_pt_ot_nursing`
> 
> Home health, PT, OT, nursing visits, therapy notes.
> 
> Examples:
> 
> ```text
> home health admission packet
> nursing visit note
> PT evaluation
> OT evaluation
> therapy progress note
> caregiver training note
> fall risk assessment
> mobility assessment
> home safety assessment
> discharge from home health
> ```
> 
> This gets its own section because those documents often impact daily operations.
> 
> ---
> 
> ### `13_symptom_logs_and_care_notes`
> 
> Human-generated logs and care notes.
> 
> Examples:
> 
> ```text
> daily care notes
> symptom timeline
> breathing episode note
> pain flare note
> fall/near-fall note
> bowel/urine log export
> food/fluid intake export
> Powerade intake log
> oxygen use log
> prednisone dose log
> caregiver observation
> incident report
> ```
> 
> These may be generated by the app, not uploaded from MyChart.
> 
> ---
> 
> ### `14_education_and_reference`
> 
> General reference material.
> 
> Examples:
> 
> ```text
> COPD education
> medication education sheets
> oxygen safety guide
> fall prevention handout
> nutrition guidance
> home care instructions
> disease education
> therapy exercise handouts
> equipment manuals
> ```
> 
> This should not be mixed with Mom-specific test results. Reference docs are useful, but they are not patient-specific source records unless a provider gave them as part of her plan.
> 
> ---
> 
> ### `90_archive_duplicates_old`
> 
> Old, superseded, duplicate, or questionable documents.
> 
> Examples:
> 
> ```text
> duplicate EOBs
> old medication lists
> outdated care plans
> superseded POA drafts
> bad scans
> uncertain documents
> replaced summaries
> ```
> 
> Never delete medical/legal docs casually. Archive them and mark status.
> 
> ---
> 
> ## App-side document types
> 
> In the database, I would not use folder names exactly. I’d use clean `document_type` values:
> 
> ```text
> emergency_identity
> visit_summary
> discharge_summary
> hospital_record
> test_result
> lab_result
> imaging_report
> procedure_report
> medication_list
> prescription
> medication_reconciliation
> treatment_plan
> provider_order
> oxygen_equipment
> dme_supply
> insurance
> billing
> eob
> prior_authorization
> legal
> hipaa_release
> poa_medical
> poa_financial
> advance_directive
> care_team
> home_health
> pt_ot_therapy
> nursing_note
> symptom_log
> care_note
> incident_report
> education_reference
> other
> ```
> 
> ## Suggested database category field
> 
> I’d use both:
> 
> ```text
> vault_category
> document_type
> ```
> 
> Example:
> 
> ```text
> vault_category = 09_insurance_billing_and_eobs
> document_type = eob
> ```
> 
> Another:
> 
> ```text
> vault_category = 03_discharge_and_hospital
> document_type = discharge_summary
> ```
> 
> Another:
> 
> ```text
> vault_category = 04_test_results
> document_type = lab_result
> ```
> 
> That gives you clean UI grouping **and** precise document classification.
> 
> ## Add this to `care.documents`
> 
> If the table doesn’t already have it:
> 
> ```sql
> alter table care.documents
> add column if not exists vault_category text,
> add column if not exists document_type text,
> add column if not exists document_subtype text,
> add column if not exists document_date date,
> add column if not exists service_start_date date,
> add column if not exists service_end_date date,
> add column if not exists source_org text,
> add column if not exists source_provider text,
> add column if not exists payer_name text,
> add column if not exists claim_number text,
> add column if not exists review_status text default 'needs_review',
> add column if not exists action_required boolean default false,
> add column if not exists action_due_date date,
> add column if not exists binder_relevant boolean default false,
> add column if not exists metadata_json jsonb default '{}'::jsonb;
> ```
> 
> ## Review statuses
> 
> Use these:
> 
> ```text
> needs_review
> classified
> ocr_needed
> ocr_complete
> summary_needed
> summarized
> linked
> action_required
> filed
> archived
> duplicate
> superseded
> ```
> 
> ## File naming rule
> 
> Use this:
> 
> ```text
> YYYY-MM-DD__category__source__document-type__short-description.pdf
> ```
> 
> Examples:
> 
> ```text
> 2026-05-05__discharge-hospital__deaconess__discharge-summary__copd-exacerbation.pdf
> 
> 2026-05-04__test-results__deaconess__renal-profile__abnormal.pdf
> 
> 2026-05-03__test-results__deaconess__procalcitonin__abnormal.pdf
> 
> 2026-05-01__medications__walmart-pharmacy__medication-list__current-meds.pdf
> 
> 2026-05-12__insurance-billing__anthem__eob__hospital-claim.pdf
> 
> 2026-05-14__legal__notary__poa-medical__executed.pdf
> ```
> 
> ## Better Codex prompt
> 
> Use this one instead of the previous over-meta version:
> 
> ```text
> We need to define the actual Document Vault categories for MomCare. Do not create a new top-level folder. Work inside the existing docs/20_patient_record_archive area.
> 
> Goal:
> Create documentation that defines the real document categories the MomCare app vault should support, including EOBs, visit summaries, discharges, test results, medication records, legal docs, oxygen/equipment docs, home health notes, and care logs.
> 
> Do not move existing files.
> Do not delete existing files.
> Only add/update docs inside docs/20_patient_record_archive.
> 
> Create or update this file:
> 
> docs/20_patient_record_archive/document_vault_category_model.md
> 
> Content should define these vault sections:
> 
> 00_inbox_needs_review
> 01_emergency_and_identity
> 02_visit_summaries
> 03_discharge_and_hospital
> 04_test_results
> 05_imaging_and_procedures
> 06_medications_and_prescriptions
> 07_treatment_plans_and_orders
> 08_oxygen_equipment_and_supplies
> 09_insurance_billing_and_eobs
> 10_legal_hipaa_and_poa
> 11_care_team_and_contacts
> 12_home_health_pt_ot_nursing
> 13_symptom_logs_and_care_notes
> 14_education_and_reference
> 90_archive_duplicates_old
> 
> For each section include:
> - Purpose
> - What belongs here
> - Examples
> - What does NOT belong here
> - Suggested document_type values
> - Sensitivity level
> - Whether it is binder-relevant
> - Whether it may require action/follow-up
> 
> Also define app database fields:
> - vault_category
> - document_type
> - document_subtype
> - document_date
> - service_start_date
> - service_end_date
> - source_org
> - source_provider
> - payer_name
> - claim_number
> - review_status
> - action_required
> - action_due_date
> - binder_relevant
> - metadata_json
> 
> Define document_type values:
> - emergency_identity
> - visit_summary
> - discharge_summary
> - hospital_record
> - test_result
> - lab_result
> - imaging_report
> - procedure_report
> - medication_list
> - prescription
> - medication_reconciliation
> - treatment_plan
> - provider_order
> - oxygen_equipment
> - dme_supply
> - insurance
> - billing
> - eob
> - prior_authorization
> - legal
> - hipaa_release
> - poa_medical
> - poa_financial
> - advance_directive
> - care_team
> - home_health
> - pt_ot_therapy
> - nursing_note
> - symptom_log
> - care_note
> - incident_report
> - education_reference
> - other
> 
> Define review_status values:
> - needs_review
> - classified
> - ocr_needed
> - ocr_complete
> - summary_needed
> - summarized
> - linked
> - action_required
> - filed
> - archived
> - duplicate
> - superseded
> 
> Define file naming convention:
> YYYY-MM-DD__category__source__document-type__short-description.pdf
> 
> Include examples:
> 2026-05-05__discharge-hospital__deaconess__discharge-summary__copd-exacerbation.pdf
> 2026-05-04__test-results__deaconess__renal-profile__abnormal.pdf
> 2026-05-03__test-results__deaconess__procalcitonin__abnormal.pdf
> 2026-05-01__medications__walmart-pharmacy__medication-list__current-meds.pdf
> 2026-05-12__insurance-billing__anthem__eob__hospital-claim.pdf
> 2026-05-14__legal__notary__poa-medical__executed.pdf
> 
> Also update:
> docs/20_patient_record_archive/_index.md
> 
> Add a link to:
> document_vault_category_model.md
> 
> Tone:
> Practical, direct, caregiver/admin focused.
> Avoid corporate fluff.
> This should be usable by Codex and by a human caregiver.
> ```
> 
> ## Blunt architecture call
> 
> The app should show the vault like this:
> 
> ```text
> Inbox
> Emergency / Identity
> Visits
> Hospital / Discharge
> Tests
> Imaging / Procedures
> Meds / Prescriptions
> Orders / Treatment Plans
> Oxygen / Equipment
> Insurance / EOBs / Billing
> Legal / HIPAA / POA
> Care Team
> Home Health / Therapy
> Logs / Care Notes
> Education
> Archive
> ```
> 
> That is the UI. Clean enough for a human. Structured enough for the database. Not over-engineered.

### User
> ok you want to make me a quick command or script to build out this vault and where does it go at root or inside docs

### Assistant
> Put it **inside `docs/20_patient_record_archive/files/template-patient/`**, not at repo root.
> 
> Why: this is a **patient document archive template**, not app source code and not general docs.
> 
> Target:
> 
> ```text
> docs/20_patient_record_archive/files/template-patient/
> ├── 00_inbox_needs_review
> ├── 01_emergency_and_identity
> ├── 02_visit_summaries
> ├── 03_discharge_and_hospital
> ├── 04_test_results
> ├── 05_imaging_and_procedures
> ├── 06_medications_and_prescriptions
> ├── 07_treatment_plans_and_orders
> ├── 08_oxygen_equipment_and_supplies
> ├── 09_insurance_billing_and_eobs
> ├── 10_legal_hipaa_and_poa
> ├── 11_care_team_and_contacts
> ├── 12_home_health_pt_ot_nursing
> ├── 13_symptom_logs_and_care_notes
> ├── 14_education_and_reference
> └── 90_archive_duplicates_old
> ```
> 
> ## PowerShell command
> 
> Run this from:
> 
> ```powershell
> cd C:\QiLabs\apps\MomsCare
> ```
> 
> Then:
> 
> ```powershell
> $vaultRoot = "docs\20_patient_record_archive\files\template-patient"
> 
> $folders = @(
>   "00_inbox_needs_review",
>   "01_emergency_and_identity",
>   "02_visit_summaries",
>   "03_discharge_and_hospital",
>   "04_test_results",
>   "05_imaging_and_procedures",
>   "06_medications_and_prescriptions",
>   "07_treatment_plans_and_orders",
>   "08_oxygen_equipment_and_supplies",
>   "09_insurance_billing_and_eobs",
>   "10_legal_hipaa_and_poa",
>   "11_care_team_and_contacts",
>   "12_home_health_pt_ot_nursing",
>   "13_symptom_logs_and_care_notes",
>   "14_education_and_reference",
>   "90_archive_duplicates_old"
> )
> 
> foreach ($folder in $folders) {
>   $path = Join-Path $vaultRoot $folder
>   New-Item -ItemType Directory -Force -Path $path | Out-Null
>   New-Item -ItemType File -Force -Path (Join-Path $path ".gitkeep") | Out-Null
> }
> 
> @"
> # Template Patient Document Vault
> 
> This folder is the template structure for a patient's document vault.
> 
> Use this structure for organizing real-world documents such as visit summaries, discharge papers, test results, EOBs, medication records, legal documents, oxygen/equipment paperwork, home health notes, and care logs.
> 
> ## Folder Map
> 
> - 00_inbox_needs_review: New documents waiting to be classified.
> - 01_emergency_and_identity: Emergency, demographic, identity, allergy, and critical-access documents.
> - 02_visit_summaries: Outpatient and specialist visit summaries.
> - 03_discharge_and_hospital: ER, hospital, observation, and discharge documents.
> - 04_test_results: Labs and diagnostic test results.
> - 05_imaging_and_procedures: Imaging reports, EKGs, procedures, surgeries, and related reports.
> - 06_medications_and_prescriptions: Medication lists, prescriptions, pharmacy paperwork, tapers, and med reconciliation.
> - 07_treatment_plans_and_orders: Provider orders, treatment plans, oxygen orders, home health orders, and care plans.
> - 08_oxygen_equipment_and_supplies: Oxygen, DME, supplies, equipment records, manuals, deliveries, and vendors.
> - 09_insurance_billing_and_eobs: EOBs, claims, bills, approvals, denials, prior authorizations, and receipts.
> - 10_legal_hipaa_and_poa: HIPAA, POA, advance directive, living will, legal authority, and end-of-life documents.
> - 11_care_team_and_contacts: Provider, caregiver, agency, pharmacy, DME, transportation, and case manager contacts.
> - 12_home_health_pt_ot_nursing: Home health, nursing, PT, OT, therapy, evaluations, and progress notes.
> - 13_symptom_logs_and_care_notes: Symptom logs, care notes, incident notes, oxygen logs, bowel/urine logs, intake logs, and caregiver observations.
> - 14_education_and_reference: Education sheets, disease guides, medication handouts, safety guides, and reference material.
> - 90_archive_duplicates_old: Duplicates, superseded versions, unclear scans, old documents, and items retained for audit only.
> 
> ## Naming Rule
> 
> Use:
> 
> YYYY-MM-DD__category__source__document-type__short-description.pdf
> 
> Examples:
> 
> 2026-05-05__discharge-hospital__deaconess__discharge-summary__copd-exacerbation.pdf
> 
> 2026-05-04__test-results__deaconess__renal-profile__abnormal.pdf
> 
> 2026-05-12__insurance-billing__anthem__eob__hospital-claim.pdf
> 
> ## Rule
> 
> Do not delete original documents casually. If unsure, place the document in 00_inbox_needs_review or 90_archive_duplicates_old.
> "@ | Set-Content (Join-Path $vaultRoot "README.md")
> 
> Write-Host "Document vault folders created at $vaultRoot"
> ```
> 
> ## Also add the model doc
> 
> Create this file:
> 
> ```text
> docs/20_patient_record_archive/document_vault_category_model.md
> ```
> 
> PowerShell:
> 
> ```powershell
> @"
> # Document Vault Category Model
> 
> The Document Vault organizes Mom's real-world records by practical care category.
> 
> This model applies to both:
> 
> 1. The local patient archive under docs/20_patient_record_archive/files/
> 2. The future app-backed Document Vault using Supabase Storage and care.documents metadata.
> 
> ## Vault Categories
> 
> | Category | Purpose | Examples |
> |---|---|---|
> | 00_inbox_needs_review | New unclassified documents | New MyChart PDFs, scans, photos, unread insurance letters |
> | 01_emergency_and_identity | Critical identity and emergency docs | ID, insurance cards, allergy list, emergency sheet, demographics |
> | 02_visit_summaries | Outpatient visit summaries | PCP, pulmonology, cardiology, pain management, follow-up visits |
> | 03_discharge_and_hospital | ER, hospital, observation, discharge docs | ER summary, discharge instructions, admission paperwork |
> | 04_test_results | Labs and diagnostic results | CBC, CMP, renal profile, A1C, procalcitonin, cultures, urinalysis |
> | 05_imaging_and_procedures | Imaging and procedure reports | X-ray, CT, MRI, ultrasound, EKG, surgery note, procedure note |
> | 06_medications_and_prescriptions | Medication and pharmacy records | Med lists, prescriptions, prednisone taper, refill history |
> | 07_treatment_plans_and_orders | Provider orders and care plans | Oxygen order, PT order, home health order, COPD action plan |
> | 08_oxygen_equipment_and_supplies | Oxygen, DME, and supply records | Tank paperwork, concentrator manual, DME delivery, supply orders |
> | 09_insurance_billing_and_eobs | Insurance and money paperwork | EOBs, bills, claims, denials, prior auths, receipts |
> | 10_legal_hipaa_and_poa | Legal authority and end-of-life docs | HIPAA, medical POA, financial POA, advance directive, living will |
> | 11_care_team_and_contacts | People and organizations | Providers, caregivers, agencies, pharmacies, DME vendors |
> | 12_home_health_pt_ot_nursing | Home care and therapy notes | Home health notes, nursing notes, PT/OT evals, progress notes |
> | 13_symptom_logs_and_care_notes | Care observations and app-generated logs | Oxygen log, bowel/urine log, symptom timeline, incident notes |
> | 14_education_and_reference | General education and reference | COPD education, oxygen safety, fall prevention, med handouts |
> | 90_archive_duplicates_old | Old, duplicate, or superseded docs | Duplicate scans, old med lists, outdated care plans |
> 
> ## App Fields
> 
> Recommended care.documents fields:
> 
> - vault_category
> - document_type
> - document_subtype
> - document_date
> - service_start_date
> - service_end_date
> - source_org
> - source_provider
> - payer_name
> - claim_number
> - review_status
> - action_required
> - action_due_date
> - binder_relevant
> - metadata_json
> 
> ## Document Types
> 
> - emergency_identity
> - visit_summary
> - discharge_summary
> - hospital_record
> - test_result
> - lab_result
> - imaging_report
> - procedure_report
> - medication_list
> - prescription
> - medication_reconciliation
> - treatment_plan
> - provider_order
> - oxygen_equipment
> - dme_supply
> - insurance
> - billing
> - eob
> - prior_authorization
> - legal
> - hipaa_release
> - poa_medical
> - poa_financial
> - advance_directive
> - care_team
> - home_health
> - pt_ot_therapy
> - nursing_note
> - symptom_log
> - care_note
> - incident_report
> - education_reference
> - other
> 
> ## Review Statuses
> 
> - needs_review
> - classified
> - ocr_needed
> - ocr_complete
> - summary_needed
> - summarized
> - linked
> - action_required
> - filed
> - archived
> - duplicate
> - superseded
> 
> ## File Naming Convention
> 
> Use:
> 
> YYYY-MM-DD__category__source__document-type__short-description.pdf
> 
> Examples:
> 
> 2026-05-05__discharge-hospital__deaconess__discharge-summary__copd-exacerbation.pdf
> 
> 2026-05-04__test-results__deaconess__renal-profile__abnormal.pdf
> 
> 2026-05-03__test-results__deaconess__procalcitonin__abnormal.pdf
> 
> 2026-05-01__medications__walmart-pharmacy__medication-list__current-meds.pdf
> 
> 2026-05-12__insurance-billing__anthem__eob__hospital-claim.pdf
> 
> 2026-05-14__legal__notary__poa-medical__executed.pdf
> 
> ## Rule
> 
> The original PDF is the source of truth.
> 
> OCR, summaries, AI extraction, and app metadata are support layers. They do not replace the original record.
> "@ | Set-Content "docs\20_patient_record_archive\document_vault_category_model.md"
> ```
> 
> ## Then update the existing index
> 
> Append this:
> 
> ```powershell
> @"
> 
> ## Document Vault Category Model
> 
> - [Document Vault Category Model](document_vault_category_model.md)
> 
> The vault categories define where real-world documents belong, including EOBs, visit summaries, discharges, test results, medications, legal documents, oxygen/equipment records, home health notes, and care logs.
> 
> Template folder:
> 
> docs/20_patient_record_archive/files/template-patient/
> "@ | Add-Content "docs\20_patient_record_archive\_index.md"
> ```
> 
> ## Blunt answer
> 
> It goes here:
> 
> ```text
> docs/20_patient_record_archive/files/template-patient/
> ```
> 
> Not root. Not `docs/kb`. Not care binder.
> 
> The **care binder summarizes**.  
> The **document vault stores records**.  
> The **app database indexes and links them**.

### User
> i feel like these are too many categories, give me max 7 top vault folders, and no more than 3 subfolders if needed.

### Assistant
> Yes. You’re right. The previous version was too many buckets. That becomes “where the hell does this go?” instead of helping.
> 
> Use **7 top folders max**:
> 
> ```text
> docs/20_patient_record_archive/files/template-patient/
> ├── 00_inbox_needs_review
> ├── 01_critical_identity_legal
> ├── 02_visits_hospital_care
> ├── 03_tests_imaging_results
> ├── 04_meds_treatments_orders
> ├── 05_insurance_billing_eobs
> ├── 06_equipment_supplies_homecare
> └── 90_archive_old_duplicates
> ```
> 
> ## Folder meaning
> 
> ### `00_inbox_needs_review`
> 
> Everything new goes here first.
> 
> Examples:
> 
> ```text
> new MyChart PDFs
> scanned papers
> photos of paperwork
> unread EOBs
> unknown documents
> ```
> 
> This is the triage pile.
> 
> ---
> 
> ### `01_critical_identity_legal`
> 
> Fast-access identity, emergency, and legal authority docs.
> 
> Optional subfolders:
> 
> ```text
> identity_insurance_cards
> emergency_contacts_safety
> legal_hipaa_poa
> ```
> 
> Examples:
> 
> ```text
> ID
> insurance cards
> allergy list
> emergency grab sheet
> HIPAA release
> medical POA
> financial POA
> advance directive
> living will
> DNR/POLST/MOST if applicable
> ```
> 
> ---
> 
> ### `02_visits_hospital_care`
> 
> Anything that explains what happened during care encounters.
> 
> Optional subfolders:
> 
> ```text
> visit_summaries
> hospital_discharge_er
> home_health_pt_ot
> ```
> 
> Examples:
> 
> ```text
> PCP visit summary
> pulmonology visit summary
> ER paperwork
> hospital discharge summary
> admission paperwork
> home health visit note
> PT evaluation
> OT progress note
> nursing visit note
> ```
> 
> ---
> 
> ### `03_tests_imaging_results`
> 
> Anything diagnostic.
> 
> Optional subfolders:
> 
> ```text
> labs
> imaging
> procedures_studies
> ```
> 
> Examples:
> 
> ```text
> CBC
> renal profile
> A1C
> procalcitonin
> urinalysis
> cultures
> x-ray
> CT
> MRI
> ultrasound
> EKG
> echo
> sleep study
> pulmonary function test
> procedure report
> ```
> 
> ---
> 
> ### `04_meds_treatments_orders`
> 
> Anything that tells you what she takes or what care should be done.
> 
> Optional subfolders:
> 
> ```text
> medications
> provider_orders
> care_plans
> ```
> 
> Examples:
> 
> ```text
> current medication list
> prescriptions
> prednisone taper
> antibiotic instructions
> pharmacy printout
> med reconciliation
> oxygen order
> nebulizer order
> COPD action plan
> wound care order
> diet/fluid instructions
> treatment plan
> ```
> 
> ---
> 
> ### `05_insurance_billing_eobs`
> 
> Money and coverage docs.
> 
> Optional subfolders:
> 
> ```text
> eobs_claims
> bills_receipts
> approvals_denials
> ```
> 
> Examples:
> 
> ```text
> EOB
> claim letter
> billing statement
> payment receipt
> prior authorization
> insurance denial
> coverage approval
> DME coverage letter
> pharmacy insurance letter
> ```
> 
> ---
> 
> ### `06_equipment_supplies_homecare`
> 
> Stuff, supplies, vendors, and practical home setup.
> 
> Optional subfolders:
> 
> ```text
> oxygen_dme
> supplies_inventory
> home_safety
> ```
> 
> Examples:
> 
> ```text
> oxygen tank paperwork
> concentrator manual
> DME delivery records
> wheelchair paperwork
> hospital bed paperwork
> gloves/chucks/wipes supply lists
> station maps
> restock sheets
> home safety assessment
> equipment manuals
> ```
> 
> ---
> 
> ### `90_archive_old_duplicates`
> 
> Stuff you don’t trust but don’t want to delete.
> 
> Examples:
> 
> ```text
> duplicates
> old med lists
> outdated care plans
> bad scans
> superseded legal drafts
> unclear documents
> ```
> 
> ## Better database categories
> 
> Use these as `vault_category` values:
> 
> ```text
> inbox_needs_review
> critical_identity_legal
> visits_hospital_care
> tests_imaging_results
> meds_treatments_orders
> insurance_billing_eobs
> equipment_supplies_homecare
> archive_old_duplicates
> ```
> 
> Then use `document_type` for detail:
> 
> ```text
> visit_summary
> discharge_summary
> lab_result
> imaging_report
> medication_list
> prescription
> provider_order
> eob
> billing
> poa_medical
> hipaa_release
> oxygen_equipment
> home_health
> care_plan
> other
> ```
> 
> That’s the better architecture:
> 
> ```text
> vault_category = broad folder
> document_type = specific classification
> ```
> 
> ## Quick PowerShell rebuild script
> 
> This version creates only the 7-folder vault plus optional subfolders.
> 
> Run from:
> 
> ```powershell
> cd C:\QiLabs\apps\MomsCare
> ```
> 
> ```powershell
> $vaultRoot = "docs\20_patient_record_archive\files\template-patient"
> 
> $folders = @(
>   "00_inbox_needs_review",
> 
>   "01_critical_identity_legal",
>   "01_critical_identity_legal\identity_insurance_cards",
>   "01_critical_identity_legal\emergency_contacts_safety",
>   "01_critical_identity_legal\legal_hipaa_poa",
> 
>   "02_visits_hospital_care",
>   "02_visits_hospital_care\visit_summaries",
>   "02_visits_hospital_care\hospital_discharge_er",
>   "02_visits_hospital_care\home_health_pt_ot",
> 
>   "03_tests_imaging_results",
>   "03_tests_imaging_results\labs",
>   "03_tests_imaging_results\imaging",
>   "03_tests_imaging_results\procedures_studies",
> 
>   "04_meds_treatments_orders",
>   "04_meds_treatments_orders\medications",
>   "04_meds_treatments_orders\provider_orders",
>   "04_meds_treatments_orders\care_plans",
> 
>   "05_insurance_billing_eobs",
>   "05_insurance_billing_eobs\eobs_claims",
>   "05_insurance_billing_eobs\bills_receipts",
>   "05_insurance_billing_eobs\approvals_denials",
> 
>   "06_equipment_supplies_homecare",
>   "06_equipment_supplies_homecare\oxygen_dme",
>   "06_equipment_supplies_homecare\supplies_inventory",
>   "06_equipment_supplies_homecare\home_safety",
> 
>   "90_archive_old_duplicates"
> )
> 
> foreach ($folder in $folders) {
>   $path = Join-Path $vaultRoot $folder
>   New-Item -ItemType Directory -Force -Path $path | Out-Null
>   New-Item -ItemType File -Force -Path (Join-Path $path ".gitkeep") | Out-Null
> }
> 
> @"
> # Template Patient Document Vault
> 
> This folder is the template structure for a patient's document vault.
> 
> ## Top-Level Folders
> 
> - 00_inbox_needs_review: New or unknown documents waiting to be reviewed.
> - 01_critical_identity_legal: Identity, emergency, insurance cards, HIPAA, POA, advance directives, and legal authority.
> - 02_visits_hospital_care: Visit summaries, hospital/ER records, discharge papers, home health, nursing, PT, and OT notes.
> - 03_tests_imaging_results: Labs, imaging reports, procedures, studies, and diagnostic results.
> - 04_meds_treatments_orders: Medication lists, prescriptions, tapers, treatment plans, provider orders, and care plans.
> - 05_insurance_billing_eobs: EOBs, claims, bills, receipts, prior authorizations, approvals, and denials.
> - 06_equipment_supplies_homecare: Oxygen, DME, equipment, supplies, vendors, inventory, and home safety.
> - 90_archive_old_duplicates: Old, duplicate, superseded, unclear, or retained-for-audit documents.
> 
> ## Rule
> 
> When unsure, put the document in 00_inbox_needs_review.
> 
> Do not delete original medical, legal, or insurance documents casually.
> "@ | Set-Content (Join-Path $vaultRoot "README.md")
> 
> Write-Host "Simplified 7-folder document vault created at $vaultRoot"
> ```
> 
> ## Codex prompt
> 
> ```text
> Simplify the MomCare patient document vault structure.
> 
> Work inside:
> docs/20_patient_record_archive/files/template-patient
> 
> Do not create a new top-level docs folder.
> Do not delete existing archive files.
> Do not move real patient documents if any exist.
> If old unused vault category folders exist and are empty except .gitkeep, move them to:
> docs/20_patient_record_archive/files/template-patient/90_archive_old_duplicates/old_folder_model_review
> 
> Create this simplified vault structure:
> 
> 00_inbox_needs_review
> 
> 01_critical_identity_legal
> - identity_insurance_cards
> - emergency_contacts_safety
> - legal_hipaa_poa
> 
> 02_visits_hospital_care
> - visit_summaries
> - hospital_discharge_er
> - home_health_pt_ot
> 
> 03_tests_imaging_results
> - labs
> - imaging
> - procedures_studies
> 
> 04_meds_treatments_orders
> - medications
> - provider_orders
> - care_plans
> 
> 05_insurance_billing_eobs
> - eobs_claims
> - bills_receipts
> - approvals_denials
> 
> 06_equipment_supplies_homecare
> - oxygen_dme
> - supplies_inventory
> - home_safety
> 
> 90_archive_old_duplicates
> 
> Add .gitkeep files to empty folders.
> 
> Create or update:
> docs/20_patient_record_archive/files/template-patient/README.md
> 
> The README should explain what belongs in each top-level folder, what belongs in each subfolder, and the rule:
> When unsure, place the document in 00_inbox_needs_review.
> 
> Also create or update:
> docs/20_patient_record_archive/document_vault_category_model.md
> 
> Use these vault_category values:
> - inbox_needs_review
> - critical_identity_legal
> - visits_hospital_care
> - tests_imaging_results
> - meds_treatments_orders
> - insurance_billing_eobs
> - equipment_supplies_homecare
> - archive_old_duplicates
> 
> Explain that vault_category is broad and document_type is specific.
> 
> Recommended document_type values:
> - emergency_identity
> - insurance_card
> - legal
> - hipaa_release
> - poa_medical
> - poa_financial
> - advance_directive
> - visit_summary
> - discharge_summary
> - er_record
> - home_health
> - nursing_note
> - pt_ot_therapy
> - lab_result
> - imaging_report
> - procedure_report
> - diagnostic_study
> - medication_list
> - prescription
> - medication_reconciliation
> - provider_order
> - treatment_plan
> - care_plan
> - oxygen_equipment
> - dme_supply
> - inventory
> - home_safety
> - insurance
> - eob
> - billing
> - prior_authorization
> - approval_denial
> - other
> 
> Keep the tone practical, direct, and caregiver/admin focused.
> ```
> 
> This is the sweet spot. Seven folders. Three subfolders max. Enough structure to avoid chaos, not so much structure that you need a PhD in filing papers.

### User
> there is still some more clean up to do.

### Assistant
> Yep, now I see the new state. The vault folders got created, but they landed directly under `20_patient_record_archive`, while the older archive docs/files template got partially displaced. Tiny mess, fixable.

### Assistant
> Yes — cleanup target is clear now.
> 
> Right now `docs/20_patient_record_archive` is mixing two things:
> 
> ```text
> 1. Vault category folders
> 2. Archive documentation files
> ```
> 
> The vault folders should be under:
> 
> ```text
> docs/20_patient_record_archive/files/template-patient/
> ```
> 
> But currently they are directly under:
> 
> ```text
> docs/20_patient_record_archive/
> ```
> 
> That’s the cleanup. The uploaded file tree confirms the vault folders are sitting directly inside `20_patient_record_archive`, and root docs still has loose archive files like `ocr_and_rag_pipeline.md` and `pdf_repo_rules.md`. fileciteturn0file0
> 
> ## Correct structure
> 
> Use this:
> 
> ```text
> docs/20_patient_record_archive
> ├── _index.md
> ├── README.md
> ├── archive_operating_guide.md
> ├── ocr_and_rag_pipeline.md
> ├── pdf_repo_rules.md
> ├── document_vault_category_model.md
> └── files
>     └── template-patient
>         ├── 00_inbox_needs_review
>         ├── 01_critical_identity_legal
>         ├── 02_visits_hospital_care
>         ├── 03_tests_imaging_results
>         ├── 04_meds_treatments_orders
>         ├── 05_insurance_billing_eobs
>         ├── 06_equipment_supplies_homecare
>         ├── 90_archive_old_duplicates
>         └── README.md
> ```
> 
> ## Run this from repo root
> 
> ```powershell
> cd C:\QiLabs\apps\MomsCare
> ```
> 
> Then run:
> 
> ```powershell
> $archiveRoot = "docs\20_patient_record_archive"
> $templateRoot = "$archiveRoot\files\template-patient"
> 
> # Ensure correct template root exists
> New-Item -ItemType Directory -Force -Path $templateRoot | Out-Null
> 
> # Vault folders that were accidentally created at archive root
> $vaultFolders = @(
>   "00_inbox_needs_review",
>   "01_critical_identity_legal",
>   "02_visits_hospital_care",
>   "03_tests_imaging_results",
>   "04_meds_treatments_orders",
>   "05_insurance_billing_eobs",
>   "06_equipment_supplies_homecare",
>   "90_archive_old_duplicates"
> )
> 
> foreach ($folder in $vaultFolders) {
>   $src = Join-Path $archiveRoot $folder
>   $dst = Join-Path $templateRoot $folder
> 
>   if (Test-Path $src) {
>     if (!(Test-Path $dst)) {
>       Move-Item -Path $src -Destination $dst
>     } else {
>       # Merge contents if destination already exists
>       Get-ChildItem -Path $src -Force | ForEach-Object {
>         $target = Join-Path $dst $_.Name
>         if (!(Test-Path $target)) {
>           Move-Item -Path $_.FullName -Destination $target
>         }
>       }
> 
>       # Remove source folder if empty
>       if ((Get-ChildItem -Path $src -Force | Measure-Object).Count -eq 0) {
>         Remove-Item -Path $src -Force
>       }
>     }
>   }
> }
> 
> # Move loose archive docs from docs root into patient archive if present
> $looseDocs = @(
>   "ocr_and_rag_pipeline.md",
>   "pdf_repo_rules.md"
> )
> 
> foreach ($doc in $looseDocs) {
>   $src = Join-Path "docs" $doc
>   $dst = Join-Path $archiveRoot $doc
> 
>   if ((Test-Path $src) -and !(Test-Path $dst)) {
>     Move-Item -Path $src -Destination $dst
>   }
> }
> 
> # Move misplaced archive operating guide if it ended up inside archive folder
> $misplacedGuide = Join-Path $templateRoot "90_archive_old_duplicates\archive_operating_guide.md"
> $correctGuide = Join-Path $archiveRoot "archive_operating_guide.md"
> 
> if ((Test-Path $misplacedGuide) -and !(Test-Path $correctGuide)) {
>   Move-Item -Path $misplacedGuide -Destination $correctGuide
> }
> 
> # Recreate .gitkeep files in empty folders
> Get-ChildItem -Path $templateRoot -Directory -Recurse | ForEach-Object {
>   if ((Get-ChildItem -Path $_.FullName -Force | Measure-Object).Count -eq 0) {
>     New-Item -ItemType File -Force -Path (Join-Path $_.FullName ".gitkeep") | Out-Null
>   }
> }
> 
> # Add/update template README
> @"
> # Template Patient Document Vault
> 
> This folder is the template structure for a patient's document vault.
> 
> ## Top-Level Folders
> 
> - 00_inbox_needs_review: New or unknown documents waiting to be reviewed.
> - 01_critical_identity_legal: Identity, emergency, insurance cards, HIPAA, POA, advance directives, and legal authority.
> - 02_visits_hospital_care: Visit summaries, hospital/ER records, discharge papers, home health, nursing, PT, and OT notes.
> - 03_tests_imaging_results: Labs, imaging reports, procedures, studies, and diagnostic results.
> - 04_meds_treatments_orders: Medication lists, prescriptions, tapers, treatment plans, provider orders, and care plans.
> - 05_insurance_billing_eobs: EOBs, claims, bills, receipts, prior authorizations, approvals, and denials.
> - 06_equipment_supplies_homecare: Oxygen, DME, equipment, supplies, vendors, inventory, and home safety.
> - 90_archive_old_duplicates: Old, duplicate, superseded, unclear, or retained-for-audit documents.
> 
> ## Rule
> 
> When unsure, put the document in 00_inbox_needs_review.
> 
> Do not delete original medical, legal, or insurance documents casually.
> "@ | Set-Content (Join-Path $templateRoot "README.md")
> 
> Write-Host "Patient document vault cleanup complete."
> ```
> 
> ## Then check it
> 
> Run:
> 
> ```powershell
> tree docs\20_patient_record_archive /F
> ```
> 
> You should **not** see these directly under `docs\20_patient_record_archive` anymore:
> 
> ```text
> 00_inbox_needs_review
> 01_critical_identity_legal
> 02_visits_hospital_care
> 03_tests_imaging_results
> 04_meds_treatments_orders
> 05_insurance_billing_eobs
> 06_equipment_supplies_homecare
> 90_archive_old_duplicates
> ```
> 
> You should see them under:
> 
> ```text
> docs\20_patient_record_archive\files\template-patient
> ```
> 
> ## Codex prompt version
> 
> ```text
> Clean up the MomCare document vault folder placement.
> 
> Problem:
> The simplified vault category folders were created directly under:
> docs/20_patient_record_archive/
> 
> They should be inside:
> docs/20_patient_record_archive/files/template-patient/
> 
> Do not delete real documents.
> Do not move the care binder.
> Do not move kb/reference/templates in this task.
> 
> Move these folders from docs/20_patient_record_archive/ into docs/20_patient_record_archive/files/template-patient/:
> 
> 00_inbox_needs_review
> 01_critical_identity_legal
> 02_visits_hospital_care
> 03_tests_imaging_results
> 04_meds_treatments_orders
> 05_insurance_billing_eobs
> 06_equipment_supplies_homecare
> 90_archive_old_duplicates
> 
> If destination folders already exist, merge safely and do not overwrite real files.
> 
> Also move loose archive docs from docs root into docs/20_patient_record_archive if they exist:
> - ocr_and_rag_pipeline.md
> - pdf_repo_rules.md
> 
> If archive_operating_guide.md is inside:
> docs/20_patient_record_archive/files/template-patient/90_archive_old_duplicates/
> 
> move it back to:
> docs/20_patient_record_archive/archive_operating_guide.md
> 
> Create or update:
> docs/20_patient_record_archive/files/template-patient/README.md
> 
> Add a clear folder map explaining the seven-folder vault model.
> 
> After cleanup, report the final tree for:
> docs/20_patient_record_archive
> ```
> 
> Bluntly: don’t do the bigger docs re-org yet. Fix this placement first. One clean incision, not open-heart folder surgery.
