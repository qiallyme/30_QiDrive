---
layout: page
title: "Tax Return Storage Model"
slug: "tax_return_storage_model"
created_at: "2026-02-24 16:44:42"
updated_at: "2026-07-16T06:49:30-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-004.json"
template_key: master-template
date: 2026-02-24
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "699e29d8-d3a8-8325-85bc-67d75ef59265"
canonical_ref: ""
---

# Tax Return Storage Model

## Overview
- **Date**: 2026-02-24 16:44:42
- **Conversation ID**: `699e29d8-d3a8-8325-85bc-67d75ef59265`
- **Source**: `Chat-Export-28513-2026/conversations-004.json`

## Chat History

### User
> I need a conotical tax return storage in supabase, the key meta data and status and the copy of the file i can combine into one pdf all the docs and signed copies.

### Assistant
> You need **one canonical “TaxReturn” object** in Supabase that:
> 
> 1) tracks **metadata + workflow status**
> 2) stores **the final compiled PDF** (return + all supporting docs + signatures)
> 3) optionally stores **component/source files** (W-2s, 1099s, organizers, e-sign forms) and links them to the return
> 
> Below is a clean, scalable Supabase design (Postgres + Storage) that won’t paint you into a corner.
> 
> ---
> 
> ## Canonical object model
> 
> ### 1) `tax_returns` (the master record)
> One row per filed return per client per tax year (and per amendment, if any).
> 
> **Core identifiers**
> - `id` (uuid, PK)
> - `client_id` (uuid, FK to `clients`)
> - `tax_year` (int) — e.g., 2025
> - `jurisdiction` (text) — `federal`, `IN`, etc. (or store multiple via child table)
> - `return_type` (text) — `1040`, `1120S`, `1065`, `IT-40`, etc.
> - `filing_kind` (text) — `original` | `amended`
> - `version` (int) — increments when you recompile or refile
> - `canonical_slug` (text, unique-ish) — ex: `client123_2025_1040_v3_original`
> 
> **Workflow**
> - `status` (text enum) — recommended:
>   - `intake_pending`
>   - `info_requested`
>   - `prep_in_progress`
>   - `ready_for_review`
>   - `awaiting_signature`
>   - `ready_to_efile`
>   - `efile_submitted`
>   - `accepted`
>   - `rejected`
>   - `needs_correction`
>   - `paper_filed`
>   - `completed`
> - `status_at` (timestamptz)
> - `due_date` (date)
> - `priority` (int small) optional
> - `assigned_to` (uuid) optional
> 
> **Money + outcome**
> - `fee_total` (numeric)
> - `fee_paid` (numeric)
> - `payment_status` (text) — `unpaid|partial|paid|waived`
> - `refund_federal` (numeric, nullable)
> - `balance_due_federal` (numeric, nullable)
> - `refund_state` (numeric, nullable)
> - `balance_due_state` (numeric, nullable)
> - `direct_deposit_requested` (bool)
> - `bank_last4` (text, nullable) (do NOT store full routing/acct unless you truly need to)
> 
> **E-file tracking**
> - `efile_provider` (text) — `drake|proconnect|taxslayer|other`
> - `submission_id` (text)
> - `accepted_at` (timestamptz)
> - `rejected_at` (timestamptz)
> - `rejection_codes` (jsonb)
> 
> **Canonical PDF pointers**
> - `final_pdf_object_path` (text) — Supabase Storage path
> - `final_pdf_sha256` (text)
> - `final_pdf_pages` (int)
> - `final_pdf_bytes` (bigint)
> 
> **Audit**
> - `created_at`, `updated_at`
> - `created_by`, `updated_by`
> - `notes_internal` (text)
> 
> This table is the “truth.” Everything else hangs off `tax_returns.id`.
> 
> ---
> 
> ### 2) `tax_return_files` (all files linked to the return)
> Every upload/output is a row (W2 PDFs, signed 8879, organizer, compiled PDF, etc.).
> 
> Fields:
> - `id` (uuid, PK)
> - `tax_return_id` (uuid, FK)
> - `file_role` (text) — `source_doc|signed_form|supporting|workpaper|final_pdf|correspondence`
> - `doc_type` (text) — `W2|1099NEC|1099R|SSA1099|8879|IT40|ScheduleC|ID|Other`
> - `filename_original` (text)
> - `mime_type` (text)
> - `bytes` (bigint)
> - `page_count` (int, nullable)
> - `storage_bucket` (text) — e.g. `tax-returns`
> - `object_path` (text) — storage path
> - `sha256` (text) — for dedupe + integrity
> - `is_canonical` (bool) — true for the final compiled PDF and/or “official signed packet”
> - `visibility` (text) — `internal|client`
> - `received_at` (timestamptz)
> - `uploaded_by` (uuid)
> - `tags` (text[]) optional
> - `metadata` (jsonb) optional (issuer name, EIN masked, etc.)
> 
> Your “one PDF with everything” is simply the `tax_returns.final_pdf_object_path` and also a `tax_return_files` row where `file_role='final_pdf'` and `is_canonical=true`.
> 
> ---
> 
> ### 3) `tax_return_events` (status history)
> So you can see what happened without overwriting history.
> 
> - `id` uuid
> - `tax_return_id` uuid
> - `event_type` text — `status_change|note|efile_submitted|efile_accepted|efile_rejected|payment_update`
> - `from_status` text
> - `to_status` text
> - `message` text
> - `data` jsonb
> - `created_at` timestamptz
> - `created_by` uuid
> 
> ---
> 
> ## Supabase Storage layout (simple + deterministic)
> 
> **Bucket:** `tax-returns`
> 
> **Path pattern:**
> - `client/{client_id}/year/{tax_year}/{return_type}/{filing_kind}/v{version}/final/ReturnPacket.pdf`
> - `client/{client_id}/year/{tax_year}/{return_type}/{filing_kind}/v{version}/source/{sha256}_{origName}`
> - `client/{client_id}/year/{tax_year}/{return_type}/{filing_kind}/v{version}/signed/{sha256}_{origName}`
> 
> This makes exports and manual browsing painless.
> 
> ---
> 
> ## “Key metadata” checklist (what you actually need day-to-day)
> 
> Minimum viable fields that make this usable fast:
> 
> **On `tax_returns`:**
> - client_id
> - tax_year
> - return_type
> - filing_kind
> - status (+ status_at)
> - fee_total, fee_paid, payment_status
> - refund/balance_due federal + state
> - final_pdf_object_path (+ sha256)
> 
> **On `tax_return_files`:**
> - tax_return_id
> - file_role
> - doc_type
> - object_path
> - sha256
> - bytes
> - is_canonical
> 
> Everything else is nice-to-have.
> 
> ---
> 
> ## Dedupe rules (so you don’t store garbage twice)
> 
> When a file is uploaded:
> - compute `sha256`
> - if a file with same `sha256` already exists for that `tax_return_id`, don’t store a new object; just create a link row (or block it)
> - optionally global dedupe: same `sha256` across all returns (useful for repeated IDs), but be careful with access control
> 
> ---
> 
> ## Status rules (so your workflow is consistent)
> 
> Suggested “hard gates”:
> - can’t move to `awaiting_signature` unless `prep_in_progress` done and draft PDF exists
> - can’t move to `ready_to_efile` unless signed form file exists (8879 or equivalent)
> - can’t move to `completed` unless `final_pdf_object_path` set AND accepted/paper-filed noted
> 
> ---
> 
> ## RLS and security (non-negotiable)
> Tax returns contain extremely sensitive data.
> 
> - Put everything behind RLS.
> - Only `staff` role can read/write across clients.
> - Clients can read only their own `tax_returns` and only files marked `visibility='client'`.
> - Use **signed URLs** for file download; never expose public buckets.
> 
> ---
> 
> ## What you should build first (fastest path)
> 1) Create tables: `tax_returns`, `tax_return_files`, `tax_return_events`
> 2) Create bucket `tax-returns`
> 3) Add a single server action/edge function:
>    - “Create return” (makes the `tax_returns` row)
>    - “Upload file” (stores to bucket + creates `tax_return_files` row)
>    - “Set final packet” (marks canonical, sets `tax_returns.final_pdf_object_path`, bumps version if needed)
> 
> ---
> 
> If you want, paste:
> - your current `clients` table shape (or tell me if you don’t have one yet),
> - whether you want multi-jurisdiction returns (Fed + multiple states/cities),
> - and whether you’re using Supabase Auth roles for staff vs client,
> 
> …and I’ll output the **exact SQL migrations** (enums, indexes, RLS policies) plus the **storage path builder** and a minimal API flow.

### User
> you sure its not overkill?

### Assistant
> Not overkill if you actually want “canonical + auditable + retrievable without headaches.” But you can absolutely slim it down.
> 
> ### The truth
> - If you only need **“store one final PDF per client/year and track basic status”** → my design is heavier than necessary.
> - If you need **re-prints, re-file, amendments, staff handoff, “what did we send and when,” signature proof, and dedupe** → the “extra” tables stop you from building a messy second system later.
> 
> ---
> 
> ## Minimum viable (not overkill)
> You can do this with **2 tables + 1 bucket**.
> 
> ### `tax_returns` (master)
> Keep only:
> - `id` uuid
> - `client_id`
> - `tax_year`
> - `return_type`
> - `status`
> - `final_pdf_path` (storage path)
> - `final_pdf_sha256`
> - `created_at`, `updated_at`
> 
> Optional but useful:
> - `filing_kind` (`original|amended`)
> - `version` (int)
> - `refund_or_balance_summary` (jsonb)
> 
> ### `tax_return_files` (optional but recommended)
> If you want to keep source docs/signatures too:
> - `id`
> - `tax_return_id`
> - `file_role` (`source|signed|final`)
> - `object_path`
> - `sha256`
> - `created_at`
> 
> ### Storage bucket: `tax-returns`
> Paths:
> - `client/{client_id}/{tax_year}/{return_type}/final.pdf`
> - `client/{client_id}/{tax_year}/{return_type}/files/{sha256}.pdf`
> 
> That’s it. Clean and usable.
> 
> ---
> 
> ## What I’d cut first (to avoid overkill)
> Drop entirely (until you feel pain):
> - `tax_return_events` (status history) — nice but optional
> - detailed e-file fields (submission IDs, reject codes)
> - payment fields (unless you’re building billing inside Supabase)
> - granular doc typing (W2/1099/etc.) unless you truly search by it
> 
> ---
> 
> ## What I would NOT cut
> - `final_pdf_path` + `final_pdf_sha256` (integrity + “what is canonical?”)
> - `status` (even if it’s just 5 statuses)
> - `tax_year`, `return_type`, `client_id` (obvious, but people forget)
> 
> ---
> 
> ## Practical recommendation for you
> Start with the **Minimum viable** version above.
> Add `tax_return_events` later only if you catch yourself thinking:
> - “When did we send this?”
> - “Who changed the status?”
> - “Why does this say accepted?”
> 
> If you answer “yes” even once a week, you’ll want events.
> 
> If you tell me your real workflow (are you keeping source docs + signatures, or only the compiled packet?), I’ll give you the exact lean schema and status enum.

### User
> ok can you give me future proof but on a diet.

### Assistant
> ### “Future-proof but on a diet” Supabase design
> 
> Goal: **one canonical return record + canonical final packet PDF + optional supporting files**, with integrity + minimal workflow + minimal history.
> 
> ---
> 
> ## 1) Tables (3 total, lean)
> 
> ### A) `tax_returns` (master record)
> One row per client per tax year per return type per filing kind.
> 
> **Required columns**
> - `id` uuid PK
> - `client_id` uuid (FK to `clients`)
> - `tax_year` int
> - `return_type` text (e.g., `1040`, `1120S`, `1065`, `IT-40`)
> - `filing_kind` text (`original` | `amended`)
> - `status` text (enum-ish)
> - `version` int default 1
> - `canonical_pdf_path` text (Supabase Storage object path)
> - `canonical_pdf_sha256` text
> - `canonical_pdf_bytes` bigint
> - `created_at` timestamptz
> - `updated_at` timestamptz
> 
> **Small but high-value optional columns**
> - `summary` jsonb (stores refund/balance due, DD yes/no, anything you want without schema churn)
> - `notes` text (internal)
> 
> **Indexes**
> - unique: (`client_id`,`tax_year`,`return_type`,`filing_kind`,`version`)
> - lookup: (`client_id`,`tax_year`), (`status`)
> 
> ---
> 
> ### B) `tax_return_files` (attachments + components)
> Any supporting doc, signed forms, drafts, etc. This is your “diet” version of a doc management system.
> 
> - `id` uuid PK
> - `tax_return_id` uuid FK
> - `role` text (`source` | `signed` | `draft` | `final`)  
>   - you’ll still use `tax_returns.canonical_pdf_path` as the “truth”; this table is the library
> - `object_path` text
> - `sha256` text
> - `bytes` bigint
> - `mime_type` text
> - `filename` text
> - `created_at` timestamptz
> - `metadata` jsonb (optional: doc_type=W2/1099, issuer, tags, etc.)
> 
> **Indexes**
> - (`tax_return_id`,`role`)
> - (`sha256`) (for dedupe)
> 
> ---
> 
> ### C) `tax_return_audit` (tiny history, not a full event system)
> Only log **status changes** (keeps you out of “what happened?” hell without bloat).
> 
> - `id` uuid PK
> - `tax_return_id` uuid FK
> - `from_status` text
> - `to_status` text
> - `message` text (optional)
> - `created_at` timestamptz
> - `created_by` uuid (auth user)
> 
> That’s your “future proof” layer without the full workflow engine.
> 
> ---
> 
> ## 2) Statuses (keep it tight)
> Use 7 statuses. Enough to run ops, not enough to become a religion.
> 
> - `intake`
> - `prep`
> - `review`
> - `signature`
> - `ready_to_file`
> - `filed`
> - `accepted` (or `completed` if you don’t track acceptance)
> 
> (If you get rejections, store that in `summary` jsonb: `{ "efile": { "result": "rejected", "codes": [...] } }`.)
> 
> ---
> 
> ## 3) Storage bucket + paths (deterministic)
> Bucket: `tax-returns`
> 
> **Canonical packet**
> - `client/{client_id}/{tax_year}/{return_type}/{filing_kind}/v{version}/ReturnPacket.pdf`
> 
> **Other files**
> - `client/{client_id}/{tax_year}/{return_type}/{filing_kind}/v{version}/{role}/{sha256}_{filename}`
> 
> This gives you:
> - human navigable structure
> - supports versions/amendments
> - supports dedupe via sha256
> 
> ---
> 
> ## 4) Canonical rules (simple)
> - `tax_returns.canonical_pdf_path` is the authoritative “final packet”
> - When you rebuild the packet:
>   - either overwrite same path **and bump version** (recommended)
>   - or keep version same and overwrite only if you do not care about historical reproduction
> 
> Diet future-proof choice: **bump version** when you recompile anything that matters.
> 
> ---
> 
> ## 5) Dedupe (cheap win)
> On upload:
> - compute `sha256`
> - if exists in `tax_return_files` for same `tax_return_id` → skip storing again (or just link)
> - optional global dedupe later (don’t start there)
> 
> ---
> 
> ## 6) RLS (keep it safe but minimal)
> Two access modes:
> - **staff**: full access
> - **client**: only their returns + only their downloadable files (if you expose any)
> 
> Minimum:
> - RLS on all 3 tables
> - Storage access via signed URLs from an edge function (don’t make bucket public)
> 
> ---
> 
> ## 7) What this buys you later
> Without schema rewrites you can add:
> - e-file provider fields (if needed)
> - payment tracking (if you decide to)
> - richer doc typing (use `metadata->>'doc_type'`)
> - multi-state returns (add a `jurisdictions` array in `summary` or a new table later)
> 
> ---
> 
> ## If you want the exact SQL
> Tell me what your `clients` identifier is:
> - do you already have a `clients` table with `id uuid`?
> - or are clients Supabase `auth.users`?
> 
> I’ll output:
> - `CREATE TABLE` statements
> - constraints + indexes
> - RLS policies (staff vs client)
> - a trigger to auto-write `tax_return_audit` on status change

### User
> give me the ai prompt to build the module and the migrations and seed and spin up some thign for me to be able to use it stat, or should i just wait until the dashboard is working.

### Assistant
> Do **not** wait for the dashboard. If you wait, you’ll keep dumping files into chaos. Build the storage + schema now; the dashboard can sit on top later.
> 
> Below is:
> 1) an **AI prompt** you can paste into Cursor/IDE agent to build the module end-to-end
> 2) **SQL migrations** (tables, indexes, audit trigger, RLS-ready)
> 3) **seed SQL**
> 4) a **minimal “use it now” CLI** (Python) to create a return + upload canonical PDF + attach files
> 5) the **Supabase commands** to run it
> 
> ---
> 
> ## 1) AI PROMPT (paste into Cursor/IDE agent)
> 
> ```text
> You are building a “Tax Return Storage” module for a Supabase-backed app.
> 
> Goal: future-proof but minimal (“on a diet”):
> - One canonical tax return record in Postgres
> - Canonical compiled PDF stored in Supabase Storage
> - Optional supporting files stored and linked
> - Lightweight status audit history
> - Minimal API + CLI to use immediately (no dashboard required)
> 
> Tech constraints:
> - Prefer Python for tooling/CLI.
> - Supabase Postgres + Supabase Storage.
> - Use deterministic storage paths:
>   Canonical: client/{client_id}/{tax_year}/{return_type}/{filing_kind}/v{version}/ReturnPacket.pdf
>   Other:     client/{client_id}/{tax_year}/{return_type}/{filing_kind}/v{version}/{role}/{sha256}_{filename}
> 
> Deliverables:
> A) SQL migration files:
>   - Create tables: tax_returns, tax_return_files, tax_return_audit
>   - Add indexes and constraints
>   - Add trigger to insert into tax_return_audit on status changes
>   - Provide RLS policies placeholders (enabled, but policies can be permissive for service role usage)
> B) Seed script:
>   - Insert a demo client (if clients table exists, otherwise create a stub table just for local dev)
>   - Insert 2 tax_return rows with different statuses
> C) Python module:
>   - src/tax_returns/__init__.py
>   - src/tax_returns/storage.py (path builder + sha256)
>   - src/tax_returns/service.py (create_return, set_status, upload_file, set_canonical_pdf)
>   - scripts/tax_return_cli.py:
>       Commands:
>         create-return --client-id --tax-year --return-type --filing-kind
>         upload-canonical --return-id --pdf path/to.pdf
>         upload-file --return-id --role source|signed|draft --file path/to.file
>         set-status --return-id --status
>   - Use supabase-py; read SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY from env.
>   - For uploads: store file in Storage bucket “tax-returns”.
>   - After upload: write db row in tax_return_files; if canonical, also update tax_returns canonical fields.
> 
> Assume:
> - There is a clients table with id uuid (if not present locally, create a minimal one in the seed/migration guarded for dev).
> - Keep statuses to: intake, prep, review, signature, ready_to_file, filed, accepted.
> - Use jsonb summary field in tax_returns for flexible values.
> 
> Output:
> - Exact file tree with code blocks for each file.
> - Exact SQL migrations.
> - A short “Run it now” section with commands.
> ```
> 
> ---
> 
> ## 2) SQL MIGRATIONS (single migration file)
> 
> Save as: `supabase/migrations/20260224_tax_return_storage.sql`
> 
> ```sql
> -- Tax Return Storage (future-proof but on a diet)
> 
> -- Optional: if you don't already have pgcrypto for gen_random_uuid
> create extension if not exists pgcrypto;
> 
> -- 1) Master return record
> create table if not exists public.tax_returns (
>   id uuid primary key default gen_random_uuid(),
>   client_id uuid not null,
>   tax_year int not null check (tax_year >= 1900 and tax_year <= 3000),
>   return_type text not null,
>   filing_kind text not null check (filing_kind in ('original','amended')),
>   status text not null check (status in ('intake','prep','review','signature','ready_to_file','filed','accepted')),
>   version int not null default 1 check (version >= 1),
> 
>   canonical_pdf_path text,
>   canonical_pdf_sha256 text,
>   canonical_pdf_bytes bigint,
> 
>   summary jsonb not null default '{}'::jsonb,
>   notes text,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now()
> );
> 
> create unique index if not exists tax_returns_unique_version
>   on public.tax_returns (client_id, tax_year, return_type, filing_kind, version);
> 
> create index if not exists tax_returns_client_year
>   on public.tax_returns (client_id, tax_year);
> 
> create index if not exists tax_returns_status
>   on public.tax_returns (status);
> 
> -- 2) Attached files
> create table if not exists public.tax_return_files (
>   id uuid primary key default gen_random_uuid(),
>   tax_return_id uuid not null references public.tax_returns(id) on delete cascade,
> 
>   role text not null check (role in ('source','signed','draft','final')),
>   object_path text not null,
>   sha256 text not null,
>   bytes bigint not null,
>   mime_type text,
>   filename text,
>   metadata jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now()
> );
> 
> create index if not exists tax_return_files_return_role
>   on public.tax_return_files (tax_return_id, role);
> 
> create index if not exists tax_return_files_sha256
>   on public.tax_return_files (sha256);
> 
> -- Prevent exact duplicates within the same return (same hash + same role + same path)
> create unique index if not exists tax_return_files_nodup
>   on public.tax_return_files (tax_return_id, role, sha256, object_path);
> 
> -- 3) Lightweight status audit
> create table if not exists public.tax_return_audit (
>   id uuid primary key default gen_random_uuid(),
>   tax_return_id uuid not null references public.tax_returns(id) on delete cascade,
> 
>   from_status text,
>   to_status text not null,
>   message text,
> 
>   created_at timestamptz not null default now(),
>   created_by uuid
> );
> 
> create index if not exists tax_return_audit_return
>   on public.tax_return_audit (tax_return_id, created_at desc);
> 
> -- updated_at trigger
> create or replace function public.set_updated_at()
> returns trigger language plpgsql as $$
> begin
>   new.updated_at = now();
>   return new;
> end $$;
> 
> drop trigger if exists trg_tax_returns_updated_at on public.tax_returns;
> create trigger trg_tax_returns_updated_at
> before update on public.tax_returns
> for each row execute function public.set_updated_at();
> 
> -- status audit trigger
> create or replace function public.tax_returns_status_audit()
> returns trigger language plpgsql as $$
> begin
>   if (tg_op = 'INSERT') then
>     insert into public.tax_return_audit (tax_return_id, from_status, to_status, message, created_by)
>     values (new.id, null, new.status, 'created', auth.uid());
>     return new;
>   end if;
> 
>   if (tg_op = 'UPDATE' and new.status is distinct from old.status) then
>     insert into public.tax_return_audit (tax_return_id, from_status, to_status, message, created_by)
>     values (new.id, old.status, new.status, null, auth.uid());
>   end if;
> 
>   return new;
> end $$;
> 
> drop trigger if exists trg_tax_returns_status_audit on public.tax_returns;
> create trigger trg_tax_returns_status_audit
> after insert or update on public.tax_returns
> for each row execute function public.tax_returns_status_audit();
> 
> -- RLS (enable now; policies can be tightened later)
> alter table public.tax_returns enable row level security;
> alter table public.tax_return_files enable row level security;
> alter table public.tax_return_audit enable row level security;
> 
> -- Minimal policies:
> -- For now: allow service role to do everything (service role bypasses RLS).
> -- If you have authenticated staff users and want a permissive start:
> -- (Adjust these later; do NOT expose to end-clients as-is.)
> 
> drop policy if exists "tax_returns_auth_all" on public.tax_returns;
> create policy "tax_returns_auth_all"
> on public.tax_returns
> for all
> to authenticated
> using (true)
> with check (true);
> 
> drop policy if exists "tax_return_files_auth_all" on public.tax_return_files;
> create policy "tax_return_files_auth_all"
> on public.tax_return_files
> for all
> to authenticated
> using (true)
> with check (true);
> 
> drop policy if exists "tax_return_audit_auth_all" on public.tax_return_audit;
> create policy "tax_return_audit_auth_all"
> on public.tax_return_audit
> for select
> to authenticated
> using (true);
> ```
> 
> ---
> 
> ## 3) SEED SQL
> 
> Save as: `supabase/seed.sql`
> 
> ```sql
> -- Seed: assumes you already have at least one client id.
> -- If you have a clients table, insert one. If not, skip and use an existing UUID manually.
> 
> -- Example only:
> -- insert into public.clients (id, name) values ('00000000-0000-0000-0000-000000000001', 'Demo Client');
> 
> insert into public.tax_returns (
>   client_id, tax_year, return_type, filing_kind, status, version, summary, notes
> ) values
>   ('00000000-0000-0000-0000-000000000001', 2025, '1040', 'original', 'intake', 1, '{"jurisdiction":"federal"}', 'seed demo'),
>   ('00000000-0000-0000-0000-000000000001', 2024, '1040', 'original', 'accepted', 1, '{"jurisdiction":"federal","efile":{"result":"accepted"}}', 'seed demo');
> ```
> 
> If you don’t have a `clients` table yet: don’t create one just for this. Use whatever identifier you actually use for clients (auth user id, CRM id, etc.) and treat `client_id` as “your canonical client uuid.”
> 
> ---
> 
> ## 4) “USE IT NOW” Python CLI (minimal)
> 
> ### Install
> ```bash
> pip install supabase python-dotenv
> ```
> 
> ### `scripts/tax_return_cli.py`
> ```python
> import argparse
> import hashlib
> import mimetypes
> import os
> from pathlib import Path
> 
> from supabase import create_client
> 
> 
> BUCKET = "tax-returns"
> 
> 
> def sha256_file(p: Path) -> str:
>     h = hashlib.sha256()
>     with p.open("rb") as f:
>         for chunk in iter(lambda: f.read(1024 * 1024), b""):
>             h.update(chunk)
>     return h.hexdigest()
> 
> 
> def build_paths(client_id: str, tax_year: int, return_type: str, filing_kind: str, version: int):
>     base = f"client/{client_id}/{tax_year}/{return_type}/{filing_kind}/v{version}"
>     canonical = f"{base}/ReturnPacket.pdf"
>     return base, canonical
> 
> 
> def get_sb():
>     url = os.environ["SUPABASE_URL"]
>     key = os.environ["SUPABASE_SERVICE_ROLE_KEY"]  # use service role for immediate use
>     return create_client(url, key)
> 
> 
> def create_return(sb, client_id: str, tax_year: int, return_type: str, filing_kind: str):
>     payload = {
>         "client_id": client_id,
>         "tax_year": tax_year,
>         "return_type": return_type,
>         "filing_kind": filing_kind,
>         "status": "intake",
>         "version": 1,
>     }
>     res = sb.table("tax_returns").insert(payload).execute()
>     return res.data[0]
> 
> 
> def set_status(sb, return_id: str, status: str):
>     res = sb.table("tax_returns").update({"status": status}).eq("id", return_id).execute()
>     return res.data[0] if res.data else None
> 
> 
> def upload_object(sb, object_path: str, file_path: Path, content_type: str | None):
>     with file_path.open("rb") as f:
>         data = f.read()
>     # upsert=True so you can re-upload in dev
>     return sb.storage.from_(BUCKET).upload(
>         path=object_path,
>         file=data,
>         file_options={"content-type": content_type or "application/octet-stream", "upsert": "true"},
>     )
> 
> 
> def attach_file_row(sb, return_id: str, role: str, object_path: str, p: Path, sha: str):
>     mime, _ = mimetypes.guess_type(str(p))
>     payload = {
>         "tax_return_id": return_id,
>         "role": role,
>         "object_path": object_path,
>         "sha256": sha,
>         "bytes": p.stat().st_size,
>         "mime_type": mime,
>         "filename": p.name,
>     }
>     res = sb.table("tax_return_files").insert(payload).execute()
>     return res.data[0]
> 
> 
> def set_canonical(sb, return_row: dict, canonical_path: str, sha: str, bytes_: int):
>     upd = {
>         "canonical_pdf_path": canonical_path,
>         "canonical_pdf_sha256": sha,
>         "canonical_pdf_bytes": bytes_,
>     }
>     res = sb.table("tax_returns").update(upd).eq("id", return_row["id"]).execute()
>     return res.data[0]
> 
> 
> def main():
>     ap = argparse.ArgumentParser()
>     sub = ap.add_subparsers(dest="cmd", required=True)
> 
>     c = sub.add_parser("create-return")
>     c.add_argument("--client-id", required=True)
>     c.add_argument("--tax-year", type=int, required=True)
>     c.add_argument("--return-type", required=True)
>     c.add_argument("--filing-kind", choices=["original", "amended"], required=True)
> 
>     s = sub.add_parser("set-status")
>     s.add_argument("--return-id", required=True)
>     s.add_argument("--status", required=True, choices=["intake","prep","review","signature","ready_to_file","filed","accepted"])
> 
>     u = sub.add_parser("upload-canonical")
>     u.add_argument("--return-id", required=True)
>     u.add_argument("--pdf", required=True)
> 
>     f = sub.add_parser("upload-file")
>     f.add_argument("--return-id", required=True)
>     f.add_argument("--role", required=True, choices=["source","signed","draft"])
>     f.add_argument("--file", required=True)
> 
>     args = ap.parse_args()
>     sb = get_sb()
> 
>     if args.cmd == "create-return":
>         row = create_return(sb, args.client_id, args.tax_year, args.return_type, args.filing_kind)
>         print(row)
>         return
> 
>     if args.cmd == "set-status":
>         row = set_status(sb, args.return_id, args.status)
>         print(row)
>         return
> 
>     # fetch return row for path building
>     r = sb.table("tax_returns").select("*").eq("id", args.return_id).single().execute()
>     return_row = r.data
>     base, canonical_path = build_paths(
>         return_row["client_id"],
>         int(return_row["tax_year"]),
>         return_row["return_type"],
>         return_row["filing_kind"],
>         int(return_row["version"]),
>     )
> 
>     if args.cmd == "upload-canonical":
>         p = Path(args.pdf)
>         if not p.exists():
>             raise SystemExit(f"Missing file: {p}")
>         sha = sha256_file(p)
>         mime, _ = mimetypes.guess_type(str(p))
>         upload_object(sb, canonical_path, p, mime or "application/pdf")
>         attach_file_row(sb, return_row["id"], "final", canonical_path, p, sha)
>         updated = set_canonical(sb, return_row, canonical_path, sha, p.stat().st_size)
>         print(updated)
>         return
> 
>     if args.cmd == "upload-file":
>         p = Path(args.file)
>         if not p.exists():
>             raise SystemExit(f"Missing file: {p}")
>         sha = sha256_file(p)
>         safe_name = p.name.replace(" ", "_")
>         object_path = f"{base}/{args.role}/{sha}_{safe_name}"
>         mime, _ = mimetypes.guess_type(str(p))
>         upload_object(sb, object_path, p, mime)
>         row = attach_file_row(sb, return_row["id"], args.role, object_path, p, sha)
>         print(row)
>         return
> 
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> ---
> 
> ## 5) Run it now
> 
> ### A) Apply migrations
> If you’re using Supabase CLI:
> ```bash
> supabase db reset
> # or
> supabase migration up
> ```
> 
> ### B) Create Storage bucket
> Do this once in Supabase Dashboard: Storage → New bucket → **tax-returns** (private).
> 
> ### C) Use the CLI
> Set env:
> ```bash
> export SUPABASE_URL="..."
> export SUPABASE_SERVICE_ROLE_KEY="..."
> ```
> 
> Create a return:
> ```bash
> python scripts/tax_return_cli.py create-return \
>   --client-id 00000000-0000-0000-0000-000000000001 \
>   --tax-year 2025 \
>   --return-type 1040 \
>   --filing-kind original
> ```
> 
> Upload the canonical compiled packet:
> ```bash
> python scripts/tax_return_cli.py upload-canonical \
>   --return-id <uuid> \
>   --pdf /path/to/ReturnPacket.pdf
> ```
> 
> Attach a supporting doc:
> ```bash
> python scripts/tax_return_cli.py upload-file \
>   --return-id <uuid> \
>   --role source \
>   --file /path/to/W2.pdf
> ```
> 
> ---
> 
> ## Dashboard question (answer you actually need)
> Waiting for the dashboard is a trap. You only need:
> - schema
> - storage bucket
> - a tiny CLI/script
> 
> That gets you operational immediately. The dashboard can be “phase 2” and just reads these tables.
> 
> If you tell me your repo layout (where you want `scripts/` and whether you’re using FastAPI vs just scripts), I’ll adapt the prompt/file tree to match your QiOne_Mono_Repo conventions.
