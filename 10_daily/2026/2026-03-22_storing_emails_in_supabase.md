---
layout: page
title: "Storing Emails in Supabase"
slug: "storing_emails_in_supabase"
created_at: "2026-03-22 04:07:14"
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
date: 2026-03-22
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69bfb141-035c-8326-97e1-9dfe5498e5af"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Storing Emails in Supabase

## Overview
- **Date**: 2026-03-22 04:07:14
- **Conversation ID**: `69bfb141-035c-8326-97e1-9dfe5498e5af`
- **Source**: `Chat-Export-28513-2026/conversations-005.json`

## Chat History

### User
> what is the best way to store emails in my supabase.

### Assistant
> Best way? **Don’t store emails as one giant blob table and call it a day.**  
> Use a **hybrid model** in Supabase:
> 
> 1. **Structured columns for the fields you query all the time**
> 2. **`jsonb` for provider-specific/raw metadata**
> 3. **Separate tables for bodies, attachments, participants, and threads**
> 4. **Full-text search on normalized text**
> 5. **Optional embeddings only if you actually need semantic search**
> 
> Supabase is just Postgres underneath, so lean into Postgres properly: `jsonb` is the recommended JSON type for most cases, full-text search is built in, pgvector is available for embeddings, and RLS should be used to protect tenant/user data. citeturn426602search4turn426602search2turn426602search0turn426602search1turn426602search5
> 
> ## The clean architecture
> 
> ### 1) `email_accounts`
> One row per connected mailbox.
> 
> Fields:
> - `id`
> - `tenant_id`
> - `user_id`
> - `provider` (`gmail`, `outlook`, `imap`, etc.)
> - `provider_account_id`
> - `email_address`
> - `sync_state`
> - `last_synced_at`
> 
> ### 2) `email_threads`
> Conversation-level object.
> 
> Fields:
> - `id`
> - `tenant_id`
> - `account_id`
> - `provider_thread_id`
> - `subject_canonical`
> - `snippet`
> - `last_message_at`
> - `message_count`
> - `unread_count`
> - `labels jsonb`
> 
> ### 3) `emails`
> One row per message. This is the core table.
> 
> Fields I’d keep as first-class columns:
> - `id`
> - `tenant_id`
> - `account_id`
> - `thread_id`
> - `provider_message_id` **unique**
> - `message_id_header` (`Message-ID`)
> - `in_reply_to`
> - `references_header`
> - `subject`
> - `from_name`
> - `from_email`
> - `sent_at`
> - `received_at`
> - `direction` (`inbound`, `outbound`)
> - `status` (`draft`, `sent`, `received`, `failed`)
> - `has_attachments`
> - `is_read`
> - `is_starred`
> - `is_archived`
> - `labels jsonb`
> - `headers jsonb`
> - `raw_meta jsonb`
> 
> Why: these are the fields you’ll filter/sort on constantly. Do **not** bury them in JSON unless you enjoy slow, annoying queries.
> 
> ### 4) `email_participants`
> For `to`, `cc`, `bcc`, and optionally normalized senders.
> 
> Fields:
> - `id`
> - `email_id`
> - `role` (`from`, `to`, `cc`, `bcc`, `reply_to`)
> - `display_name`
> - `email_address`
> 
> This avoids ugly array hacks and makes analytics/search cleaner.
> 
> ### 5) `email_bodies`
> Keep body content separate from the message row.
> 
> Fields:
> - `email_id`
> - `text_plain`
> - `text_html`
> - `body_search` (`tsvector`)
> - maybe `body_preview`
> 
> Why: email bodies get big fast. Keeping them separate keeps your hot query path lighter.
> 
> ### 6) `email_attachments`
> Metadata in Postgres, files in Supabase Storage.
> 
> Fields:
> - `id`
> - `email_id`
> - `filename`
> - `mime_type`
> - `size_bytes`
> - `storage_path`
> - `content_hash`
> - `is_inline`
> - `cid`
> - `ocr_text` if you plan to search PDFs/images later
> 
> Use Supabase Storage for the actual binary files, not bytea in Postgres, unless you enjoy self-inflicted pain.
> 
> ---
> 
> ## What I’d avoid
> 
> ### Bad option 1: one table with raw JSON only
> Fast to start, ugly forever.
> 
> Problem:
> - hard to index
> - hard to enforce consistency
> - hard to join across participants/threads/attachments
> - turns every query into gross JSON extraction logic
> 
> ### Bad option 2: over-normalizing every RFC field
> That’s the opposite trap. You do not need 27 tables for MIME boundaries and every weird header.
> 
> Store:
> - important/queryable fields as columns
> - weird provider/rfc leftovers in `jsonb`
> 
> That’s the sweet spot.
> 
> ---
> 
> ## Best practical schema pattern
> 
> ### Use columns for:
> - tenant/account/thread/message IDs
> - subject
> - sender
> - dates
> - booleans like read/starred/has_attachments
> - direction/status
> - dedupe keys
> 
> ### Use `jsonb` for:
> - raw headers
> - provider payloads
> - labels/categories that vary by provider
> - sync/debug metadata
> 
> Supabase recommends `jsonb` over `json` for most use cases because it is generally much faster to process. citeturn426602search4
> 
> ---
> 
> ## Search strategy
> 
> ### Minimum viable
> Use Postgres full-text search on:
> - subject
> - sender name/email
> - plain text body
> - attachment OCR text if available
> 
> Postgres full-text search is built in and works well for keyword/document-style search. citeturn426602search2
> 
> ### Only add embeddings if you actually need:
> - “find the email where they vaguely mentioned the quote issue”
> - semantic similarity
> - AI recall across email + docs + notes
> 
> Supabase supports pgvector for embeddings, and they also document automatic embedding pipelines using queues/functions/cron. citeturn426602search0turn426602search13
> 
> Real talk: start with full-text search first. It’s cheaper, simpler, and often enough.
> 
> ---
> 
> ## Security / multi-tenant
> 
> This part matters more than people admit.
> 
> If these emails belong to different clients, businesses, or family/work contexts, use:
> - `tenant_id` on every table
> - RLS on every exposed table
> - indexes on columns used in RLS predicates
> 
> Supabase recommends RLS for protecting data in the Data API, and indexing RLS predicate columns is a major performance best practice. citeturn426602search5turn426602search1turn426602search3
> 
> So yes:
> - `tenant_id`
> - `account_id`
> - `user_id` where needed
> - indexes on those
> 
> ---
> 
> ## My blunt recommendation for you
> 
> Given how you build systems, I’d do this:
> 
> **Store email like a document system, not like a mail client clone.**
> 
> That means:
> - normalize enough for filtering and cross-linking
> - preserve raw source in `jsonb`
> - store attachments in Storage
> - index aggressively
> - add embeddings later, not on day one
> 
> ## Recommended starting schema
> If this were your stack, I’d start with exactly these tables:
> 
> - `email_accounts`
> - `email_threads`
> - `emails`
> - `email_participants`
> - `email_bodies`
> - `email_attachments`
> 
> And I’d add these indexes immediately:
> - `emails(tenant_id, received_at desc)`
> - `emails(account_id, received_at desc)`
> - `emails(thread_id, received_at asc)`
> - `emails(provider_message_id)` unique
> - `email_threads(provider_thread_id)`
> - `email_participants(email_address)`
> - GIN index on `emails.labels`
> - GIN index on `email_bodies.body_search`
> 
> ---
> 
> ## Decision rule
> 
> If your goal is:
> 
> **Just archive/search emails**  
> → hybrid relational + `jsonb` + full-text
> 
> **Power an inbox UI**  
> → same as above, plus thread/account state tables
> 
> **AI memory / case management / client ops**  
> → same foundation, then embeddings on body + attachments later
> 
> That’s the cleanest path without building a mess you’ll hate in a month.
> 
> If you want, I’ll draft you the actual Supabase SQL schema next.

### User
> am ready for the sql please im using the exact info you gave above yes, lets add the s3 bucket and the other stuff for ai to be ready.

### Assistant
> Yep. Here’s the clean version.
> 
> One correction first: in Supabase, the “S3 bucket” part is **Supabase Storage with S3 compatibility**, not a raw AWS S3 bucket living inside Postgres. Storage is S3-compatible, but the actual file/object operations should go through the Storage API, and Supabase warns against treating the `storage` schema like a normal writable app schema. citeturn252025search0turn833674view1
> 
> For AI readiness, Supabase’s documented building blocks are:
> - `pgvector` for embeddings
> - full-text search with `tsvector` + GIN
> - and, if you want automatic embedding generation later, `pgmq`, `pg_net`, `pg_cron`, triggers, and an Edge Function. citeturn411027search1turn252025search1turn252025search5turn833674view2
> 
> ## What this migration gives you
> 
> This SQL sets up:
> 
> - multi-tenant email schema
> - thread/message/participant/body/attachment tables
> - full-text search
> - vector-ready columns
> - attachment metadata pointing to Supabase Storage
> - RLS scaffolding
> - indexes you’ll actually need
> - queue table + trigger hooks so AI/embeddings can be wired in cleanly
> 
> ## Recommended storage path convention
> 
> Use a **private** Supabase Storage bucket named:
> 
> `email-attachments`
> 
> Object path convention:
> 
> `tenant/{tenant_id}/account/{account_id}/email/{email_id}/{filename}`
> 
> That gives you sane scoping for RLS and cleanup.
> 
> ## SQL migration
> 
> ```sql
> -- =========================================================
> -- EMAIL FOUNDATION FOR SUPABASE
> -- Multi-tenant, search-ready, AI-ready
> -- =========================================================
> 
> begin;
> 
> -- ---------------------------------------------------------
> -- 0) EXTENSIONS
> -- ---------------------------------------------------------
> create extension if not exists pgcrypto;
> create extension if not exists unaccent;
> create extension if not exists vector with schema extensions;
> 
> -- Optional now, useful later for automated embeddings
> -- create extension if not exists pgmq;
> -- create extension if not exists pg_net with schema extensions;
> -- create extension if not exists pg_cron;
> 
> -- ---------------------------------------------------------
> -- 1) SCHEMA
> -- ---------------------------------------------------------
> create schema if not exists app;
> 
> -- ---------------------------------------------------------
> -- 2) HELPER FUNCTIONS
> -- ---------------------------------------------------------
> 
> create or replace function app.normalize_email(input text)
> returns text
> language sql
> immutable
> as $$
>   select lower(trim(coalesce(input, '')));
> $$;
> 
> create or replace function app.safe_unaccent(input text)
> returns text
> language sql
> immutable
> as $$
>   select unaccent(coalesce(input, ''));
> $$;
> 
> create or replace function app.emails_search_document(
>   p_subject text,
>   p_from_name text,
>   p_from_email text,
>   p_body_text text
> )
> returns tsvector
> language sql
> immutable
> as $$
>   select
>       setweight(to_tsvector('english', app.safe_unaccent(coalesce(p_subject, ''))), 'A')
>     || setweight(to_tsvector('english', app.safe_unaccent(coalesce(p_from_name, ''))), 'B')
>     || setweight(to_tsvector('english', app.safe_unaccent(coalesce(p_from_email, ''))), 'B')
>     || setweight(to_tsvector('english', app.safe_unaccent(coalesce(p_body_text, ''))), 'C');
> $$;
> 
> -- For app-side RLS. Your app should set this per request:
> -- select set_config('request.jwt.claim.tenant_id', '<tenant-uuid>', true);
> create or replace function app.current_tenant_id()
> returns uuid
> language sql
> stable
> as $$
>   select nullif(current_setting('request.jwt.claim.tenant_id', true), '')::uuid;
> $$;
> 
> -- ---------------------------------------------------------
> -- 3) CORE TABLES
> -- ---------------------------------------------------------
> 
> create table if not exists app.email_accounts (
>   id uuid primary key default gen_random_uuid(),
>   tenant_id uuid not null,
>   user_id uuid null references auth.users(id) on delete set null,
> 
>   provider text not null check (provider in ('gmail', 'outlook', 'imap', 'smtp', 'other')),
>   provider_account_id text not null,
>   email_address text not null,
>   display_name text null,
> 
>   sync_state text not null default 'active'
>     check (sync_state in ('active', 'paused', 'error', 'revoked')),
>   last_synced_at timestamptz null,
>   sync_cursor text null,
> 
>   raw_meta jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now(),
> 
>   unique (tenant_id, provider, provider_account_id),
>   unique (tenant_id, email_address)
> );
> 
> create table if not exists app.email_threads (
>   id uuid primary key default gen_random_uuid(),
>   tenant_id uuid not null,
>   account_id uuid not null references app.email_accounts(id) on delete cascade,
> 
>   provider_thread_id text null,
>   subject_canonical text null,
>   snippet text null,
> 
>   last_message_at timestamptz null,
>   first_message_at timestamptz null,
> 
>   message_count integer not null default 0,
>   unread_count integer not null default 0,
> 
>   labels jsonb not null default '[]'::jsonb,
>   raw_meta jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now(),
> 
>   unique (account_id, provider_thread_id)
> );
> 
> create table if not exists app.emails (
>   id uuid primary key default gen_random_uuid(),
>   tenant_id uuid not null,
>   account_id uuid not null references app.email_accounts(id) on delete cascade,
>   thread_id uuid null references app.email_threads(id) on delete set null,
> 
>   provider_message_id text not null,
>   internet_message_id text null, -- Message-ID header
>   in_reply_to text null,
>   references_header text[] not null default '{}',
> 
>   subject text null,
> 
>   from_name text null,
>   from_email text null,
>   reply_to jsonb not null default '[]'::jsonb,
> 
>   sent_at timestamptz null,
>   received_at timestamptz not null default now(),
> 
>   direction text not null default 'inbound'
>     check (direction in ('inbound', 'outbound', 'internal')),
>   status text not null default 'received'
>     check (status in ('draft', 'queued', 'sent', 'received', 'failed')),
> 
>   has_attachments boolean not null default false,
>   is_read boolean not null default false,
>   is_starred boolean not null default false,
>   is_archived boolean not null default false,
> 
>   labels jsonb not null default '[]'::jsonb,
>   headers jsonb not null default '{}'::jsonb,
>   raw_meta jsonb not null default '{}'::jsonb,
> 
>   body_text text null,
>   body_html text null,
>   snippet text null,
> 
>   search_tsv tsvector generated always as (
>     app.emails_search_document(subject, from_name, from_email, body_text)
>   ) stored,
> 
>   embedding_status text not null default 'pending'
>     check (embedding_status in ('pending', 'queued', 'complete', 'failed', 'skipped')),
>   embedding_model text null,
>   embedding_updated_at timestamptz null,
> 
>   -- Change dimension if you standardize on another model
>   embedding extensions.vector(1536) null,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now(),
> 
>   unique (account_id, provider_message_id)
> );
> 
> create table if not exists app.email_participants (
>   id uuid primary key default gen_random_uuid(),
>   tenant_id uuid not null,
>   email_id uuid not null references app.emails(id) on delete cascade,
> 
>   role text not null
>     check (role in ('from', 'to', 'cc', 'bcc', 'reply_to')),
> 
>   display_name text null,
>   email_address text not null,
>   email_address_normalized text generated always as (app.normalize_email(email_address)) stored,
> 
>   raw_meta jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now()
> );
> 
> create table if not exists app.email_attachments (
>   id uuid primary key default gen_random_uuid(),
>   tenant_id uuid not null,
>   email_id uuid not null references app.emails(id) on delete cascade,
> 
>   filename text not null,
>   mime_type text null,
>   size_bytes bigint null check (size_bytes is null or size_bytes >= 0),
> 
>   is_inline boolean not null default false,
>   content_id text null,
>   content_hash text null,
> 
>   storage_bucket text not null default 'email-attachments',
>   storage_path text not null,
> 
>   extracted_text text null,
> 
>   search_tsv tsvector generated always as (
>     setweight(to_tsvector('english', app.safe_unaccent(coalesce(filename, ''))), 'A')
>     || setweight(to_tsvector('english', app.safe_unaccent(coalesce(extracted_text, ''))), 'C')
>   ) stored,
> 
>   embedding_status text not null default 'pending'
>     check (embedding_status in ('pending', 'queued', 'complete', 'failed', 'skipped')),
>   embedding_model text null,
>   embedding_updated_at timestamptz null,
>   embedding extensions.vector(1536) null,
> 
>   raw_meta jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now(),
> 
>   unique (storage_bucket, storage_path)
> );
> 
> -- Optional audit / workflow table for AI jobs
> create table if not exists app.embedding_jobs (
>   id uuid primary key default gen_random_uuid(),
>   tenant_id uuid not null,
> 
>   source_table text not null check (source_table in ('emails', 'email_attachments')),
>   source_id uuid not null,
> 
>   job_type text not null default 'embed'
>     check (job_type in ('embed', 'reembed', 'extract_text', 'classify', 'summarize')),
>   status text not null default 'queued'
>     check (status in ('queued', 'processing', 'complete', 'failed', 'cancelled')),
> 
>   attempts integer not null default 0,
>   last_error text null,
> 
>   payload jsonb not null default '{}'::jsonb,
>   result jsonb not null default '{}'::jsonb,
> 
>   available_at timestamptz not null default now(),
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now()
> );
> 
> -- ---------------------------------------------------------
> -- 4) TRIGGER: updated_at
> -- ---------------------------------------------------------
> 
> create or replace function app.set_updated_at()
> returns trigger
> language plpgsql
> as $$
> begin
>   new.updated_at = now();
>   return new;
> end;
> $$;
> 
> drop trigger if exists trg_email_accounts_updated_at on app.email_accounts;
> create trigger trg_email_accounts_updated_at
> before update on app.email_accounts
> for each row execute function app.set_updated_at();
> 
> drop trigger if exists trg_email_threads_updated_at on app.email_threads;
> create trigger trg_email_threads_updated_at
> before update on app.email_threads
> for each row execute function app.set_updated_at();
> 
> drop trigger if exists trg_emails_updated_at on app.emails;
> create trigger trg_emails_updated_at
> before update on app.emails
> for each row execute function app.set_updated_at();
> 
> drop trigger if exists trg_email_attachments_updated_at on app.email_attachments;
> create trigger trg_email_attachments_updated_at
> before update on app.email_attachments
> for each row execute function app.set_updated_at();
> 
> drop trigger if exists trg_embedding_jobs_updated_at on app.embedding_jobs;
> create trigger trg_embedding_jobs_updated_at
> before update on app.embedding_jobs
> for each row execute function app.set_updated_at();
> 
> -- ---------------------------------------------------------
> -- 5) THREAD ROLLUP
> -- ---------------------------------------------------------
> 
> create or replace function app.refresh_thread_stats(p_thread_id uuid)
> returns void
> language plpgsql
> as $$
> begin
>   update app.email_threads t
>   set
>     first_message_at = s.first_message_at,
>     last_message_at  = s.last_message_at,
>     message_count    = s.message_count,
>     unread_count     = s.unread_count,
>     snippet          = s.snippet,
>     updated_at       = now()
>   from (
>     select
>       e.thread_id,
>       min(e.received_at) as first_message_at,
>       max(e.received_at) as last_message_at,
>       count(*)::int as message_count,
>       count(*) filter (where not e.is_read)::int as unread_count,
>       (
>         select e2.snippet
>         from app.emails e2
>         where e2.thread_id = e.thread_id
>         order by e2.received_at desc nulls last, e2.created_at desc
>         limit 1
>       ) as snippet
>     from app.emails e
>     where e.thread_id = p_thread_id
>     group by e.thread_id
>   ) s
>   where t.id = s.thread_id;
> end;
> $$;
> 
> create or replace function app.trg_refresh_thread_stats()
> returns trigger
> language plpgsql
> as $$
> begin
>   if new.thread_id is not null then
>     perform app.refresh_thread_stats(new.thread_id);
>   end if;
> 
>   if tg_op = 'UPDATE' and old.thread_id is distinct from new.thread_id and old.thread_id is not null then
>     perform app.refresh_thread_stats(old.thread_id);
>   end if;
> 
>   if tg_op = 'DELETE' and old.thread_id is not null then
>     perform app.refresh_thread_stats(old.thread_id);
>   end if;
> 
>   return coalesce(new, old);
> end;
> $$;
> 
> drop trigger if exists trg_refresh_thread_stats_ins on app.emails;
> create trigger trg_refresh_thread_stats_ins
> after insert on app.emails
> for each row execute function app.trg_refresh_thread_stats();
> 
> drop trigger if exists trg_refresh_thread_stats_upd on app.emails;
> create trigger trg_refresh_thread_stats_upd
> after update of thread_id, is_read, received_at, snippet on app.emails
> for each row execute function app.trg_refresh_thread_stats();
> 
> drop trigger if exists trg_refresh_thread_stats_del on app.emails;
> create trigger trg_refresh_thread_stats_del
> after delete on app.emails
> for each row execute function app.trg_refresh_thread_stats();
> 
> -- ---------------------------------------------------------
> -- 6) AI JOB ENQUEUE HELPERS
> -- ---------------------------------------------------------
> 
> create or replace function app.enqueue_email_embedding_job()
> returns trigger
> language plpgsql
> as $$
> begin
>   if tg_op = 'INSERT'
>      or new.subject is distinct from old.subject
>      or new.from_name is distinct from old.from_name
>      or new.from_email is distinct from old.from_email
>      or new.body_text is distinct from old.body_text then
> 
>     new.embedding := null;
>     new.embedding_status := 'pending';
>     new.embedding_updated_at := null;
> 
>     insert into app.embedding_jobs (
>       tenant_id,
>       source_table,
>       source_id,
>       job_type,
>       status,
>       payload
>     )
>     values (
>       new.tenant_id,
>       'emails',
>       new.id,
>       'embed',
>       'queued',
>       jsonb_build_object(
>         'email_id', new.id,
>         'tenant_id', new.tenant_id
>       )
>     );
>   end if;
> 
>   return new;
> end;
> $$;
> 
> drop trigger if exists trg_enqueue_email_embedding_job on app.emails;
> create trigger trg_enqueue_email_embedding_job
> before insert or update of subject, from_name, from_email, body_text
> on app.emails
> for each row execute function app.enqueue_email_embedding_job();
> 
> create or replace function app.enqueue_attachment_embedding_job()
> returns trigger
> language plpgsql
> as $$
> begin
>   if tg_op = 'INSERT'
>      or new.filename is distinct from old.filename
>      or new.extracted_text is distinct from old.extracted_text then
> 
>     new.embedding := null;
>     new.embedding_status := 'pending';
>     new.embedding_updated_at := null;
> 
>     insert into app.embedding_jobs (
>       tenant_id,
>       source_table,
>       source_id,
>       job_type,
>       status,
>       payload
>     )
>     values (
>       new.tenant_id,
>       'email_attachments',
>       new.id,
>       'embed',
>       'queued',
>       jsonb_build_object(
>         'attachment_id', new.id,
>         'tenant_id', new.tenant_id
>       )
>     );
>   end if;
> 
>   return new;
> end;
> $$;
> 
> drop trigger if exists trg_enqueue_attachment_embedding_job on app.email_attachments;
> create trigger trg_enqueue_attachment_embedding_job
> before insert or update of filename, extracted_text
> on app.email_attachments
> for each row execute function app.enqueue_attachment_embedding_job();
> 
> -- ---------------------------------------------------------
> -- 7) SEARCH FUNCTIONS
> -- ---------------------------------------------------------
> 
> create or replace function app.search_emails(
>   p_tenant_id uuid,
>   p_query text,
>   p_limit integer default 25
> )
> returns table (
>   email_id uuid,
>   thread_id uuid,
>   subject text,
>   from_name text,
>   from_email text,
>   snippet text,
>   received_at timestamptz,
>   rank real
> )
> language sql
> stable
> as $$
>   select
>     e.id,
>     e.thread_id,
>     e.subject,
>     e.from_name,
>     e.from_email,
>     e.snippet,
>     e.received_at,
>     ts_rank(e.search_tsv, websearch_to_tsquery('english', app.safe_unaccent(p_query))) as rank
>   from app.emails e
>   where e.tenant_id = p_tenant_id
>     and e.search_tsv @@ websearch_to_tsquery('english', app.safe_unaccent(p_query))
>   order by rank desc, e.received_at desc
>   limit greatest(coalesce(p_limit, 25), 1);
> $$;
> 
> create or replace function app.match_email_embeddings(
>   p_tenant_id uuid,
>   p_query_embedding extensions.vector(1536),
>   p_match_count integer default 20
> )
> returns table (
>   email_id uuid,
>   subject text,
>   from_email text,
>   received_at timestamptz,
>   similarity float
> )
> language sql
> stable
> as $$
>   select
>     e.id,
>     e.subject,
>     e.from_email,
>     e.received_at,
>     1 - (e.embedding <=> p_query_embedding) as similarity
>   from app.emails e
>   where e.tenant_id = p_tenant_id
>     and e.embedding is not null
>   order by e.embedding <=> p_query_embedding
>   limit greatest(coalesce(p_match_count, 20), 1);
> $$;
> 
> -- ---------------------------------------------------------
> -- 8) INDEXES
> -- ---------------------------------------------------------
> 
> create index if not exists idx_email_accounts_tenant on app.email_accounts (tenant_id);
> create index if not exists idx_email_accounts_user on app.email_accounts (user_id);
> 
> create index if not exists idx_email_threads_tenant on app.email_threads (tenant_id);
> create index if not exists idx_email_threads_account_last_message
>   on app.email_threads (account_id, last_message_at desc);
> 
> create index if not exists idx_emails_tenant_received
>   on app.emails (tenant_id, received_at desc);
> 
> create index if not exists idx_emails_account_received
>   on app.emails (account_id, received_at desc);
> 
> create index if not exists idx_emails_thread_received
>   on app.emails (thread_id, received_at asc);
> 
> create index if not exists idx_emails_from_email
>   on app.emails (from_email);
> 
> create index if not exists idx_emails_internet_message_id
>   on app.emails (internet_message_id);
> 
> create index if not exists idx_emails_labels_gin
>   on app.emails using gin (labels);
> 
> create index if not exists idx_emails_headers_gin
>   on app.emails using gin (headers);
> 
> create index if not exists idx_emails_raw_meta_gin
>   on app.emails using gin (raw_meta);
> 
> create index if not exists idx_emails_search_tsv
>   on app.emails using gin (search_tsv);
> 
> create index if not exists idx_email_participants_email_id
>   on app.email_participants (email_id);
> 
> create index if not exists idx_email_participants_address
>   on app.email_participants (email_address_normalized);
> 
> create index if not exists idx_email_participants_role
>   on app.email_participants (role);
> 
> create index if not exists idx_email_attachments_email_id
>   on app.email_attachments (email_id);
> 
> create index if not exists idx_email_attachments_storage
>   on app.email_attachments (storage_bucket, storage_path);
> 
> create index if not exists idx_email_attachments_search_tsv
>   on app.email_attachments using gin (search_tsv);
> 
> create index if not exists idx_embedding_jobs_status_available
>   on app.embedding_jobs (status, available_at);
> 
> create index if not exists idx_embedding_jobs_source
>   on app.embedding_jobs (source_table, source_id);
> 
> -- Optional vector indexes.
> -- Build these only once you actually start filling embeddings.
> -- Pick one operator and keep it consistent.
> create index if not exists idx_emails_embedding_hnsw
>   on app.emails
>   using hnsw (embedding vector_cosine_ops);
> 
> create index if not exists idx_email_attachments_embedding_hnsw
>   on app.email_attachments
>   using hnsw (embedding vector_cosine_ops);
> 
> -- ---------------------------------------------------------
> -- 9) RLS
> -- ---------------------------------------------------------
> 
> alter table app.email_accounts enable row level security;
> alter table app.email_threads enable row level security;
> alter table app.emails enable row level security;
> alter table app.email_participants enable row level security;
> alter table app.email_attachments enable row level security;
> alter table app.embedding_jobs enable row level security;
> 
> -- Basic tenant isolation.
> -- Assumes your JWT includes tenant_id and your app sets it correctly.
> create policy "tenant can read email_accounts"
> on app.email_accounts
> for select
> to authenticated
> using (tenant_id = app.current_tenant_id());
> 
> create policy "tenant can manage email_accounts"
> on app.email_accounts
> for all
> to authenticated
> using (tenant_id = app.current_tenant_id())
> with check (tenant_id = app.current_tenant_id());
> 
> create policy "tenant can read email_threads"
> on app.email_threads
> for select
> to authenticated
> using (tenant_id = app.current_tenant_id());
> 
> create policy "tenant can manage email_threads"
> on app.email_threads
> for all
> to authenticated
> using (tenant_id = app.current_tenant_id())
> with check (tenant_id = app.current_tenant_id());
> 
> create policy "tenant can read emails"
> on app.emails
> for select
> to authenticated
> using (tenant_id = app.current_tenant_id());
> 
> create policy "tenant can manage emails"
> on app.emails
> for all
> to authenticated
> using (tenant_id = app.current_tenant_id())
> with check (tenant_id = app.current_tenant_id());
> 
> create policy "tenant can read email_participants"
> on app.email_participants
> for select
> to authenticated
> using (tenant_id = app.current_tenant_id());
> 
> create policy "tenant can manage email_participants"
> on app.email_participants
> for all
> to authenticated
> using (tenant_id = app.current_tenant_id())
> with check (tenant_id = app.current_tenant_id());
> 
> create policy "tenant can read email_attachments"
> on app.email_attachments
> for select
> to authenticated
> using (tenant_id = app.current_tenant_id());
> 
> create policy "tenant can manage email_attachments"
> on app.email_attachments
> for all
> to authenticated
> using (tenant_id = app.current_tenant_id())
> with check (tenant_id = app.current_tenant_id());
> 
> create policy "tenant can read embedding_jobs"
> on app.embedding_jobs
> for select
> to authenticated
> using (tenant_id = app.current_tenant_id());
> 
> create policy "tenant can manage embedding_jobs"
> on app.embedding_jobs
> for all
> to authenticated
> using (tenant_id = app.current_tenant_id())
> with check (tenant_id = app.current_tenant_id());
> 
> commit;
> ```
> 
> ## Storage bucket setup
> 
> Do **not** manually jam file rows into `storage.objects`. Supabase explicitly says to treat the `storage` schema as read-only for normal object operations, because that schema stores metadata and the actual objects live in the storage backend. citeturn833674view1
> 
> Create the bucket in the Dashboard or with the Storage API/client. Buckets can be private/public and support restrictions like allowed MIME types and file-size limits. citeturn833674view0turn411027search0
> 
> Use:
> 
> - bucket name: `email-attachments`
> - access: **private**
> - allowed MIME types: broad docs/images if needed
> - file size limit: whatever fits your ingestion plan
> 
> Also important: Supabase’s S3 access keys bypass RLS, so server-only for S3 credentials. Do not stick those in the client. citeturn252025search13
> 
> ## Storage RLS idea
> 
> For uploads/downloads, put policies on `storage.objects` based on bucket and path prefix. Storage access control is enforced with RLS policies on `storage.objects`, and Supabase exposes helper functions like `storage.foldername()` / `storage.filename()` / `storage.extension()` for policy logic. citeturn411027search9turn411027search17
> 
> Example pattern:
> 
> - only allow bucket `email-attachments`
> - require first folder to be `tenant`
> - require second folder to equal current tenant id
> 
> I did **not** hardcode that policy here because storage path parsing gets brittle if your folder convention changes. Better to lock your path convention first, then I’ll write the exact policy cleanly.
> 
> ## AI-ready path from here
> 
> This schema is ready for:
> - keyword search now via Postgres full-text search (`tsvector` + GIN) citeturn252025search1turn252025search5
> - semantic search later via `pgvector` and HNSW indexes citeturn411027search1turn252025search5
> - automated embedding jobs later via triggers + queue + Edge Function, which matches Supabase’s documented pattern using `pgmq`, `pg_net`, `pg_cron`, and an Edge Function. citeturn833674view2
> 
> ## My blunt advice before you run this
> 
> Three things to decide now so you don’t create future cleanup:
> 
> 1. **Tenant model**  
>    If you have one human user across multiple businesses/clients, keep `tenant_id` everywhere exactly like this.
> 
> 2. **Embedding dimension**  
>    I set `vector(1536)` as a sane default. If you already know your embedding model will use a different dimension, change it now before loading data.
> 
> 3. **Body storage**  
>    I folded `body_text` and `body_html` into `app.emails` instead of a separate `email_bodies` table to keep the first migration simpler. That is the one shortcut I took. It’s fine unless you expect very heavy volume very fast. If you want the stricter split, I’ll refactor it.
> 
> The next move is either:
> - I give you the **storage RLS policies + path rules**, or
> - I give you the **Edge Function + queue processor + embedding updater** so AI is actually wired end-to-end.

### User
> read the project sources, and tell me exactly how this needs to be setup and if so what to add to the master blueprint to include this new schema.

### Assistant
> Yes. The new email schema **fits**, but not as a random sidecar. It needs to be treated as a **first-class integration path into the Spine**, with a clear split between:
> 
> - **canonical archive/ingest truth in `qiarchive`**
> - **AI/session/memory in `qially`**
> - **tenant/auth/RBAC in `qione`**
> - **secure long-lived file/object storage in `qivault`**
> - **jobs/events/retries in `qisys`**
> 
> That setup is already implied by the project sources: QiArchive is the registration spine, qially is for AI sessions and memory embeddings, qione is the tenant/RBAC platform layer, qivault is secure document storage, and qisys owns jobs and workers. fileciteturn2file0
> 
> ## The blunt answer
> 
> Your earlier standalone `email_*` schema draft is **directionally right**, but it is **architecturally wrong for QiOS** unless you fold it into the existing domain model.
> 
> Why:
> 
> 1. **QiOS already has a placement law**: every object gets exactly one canonical home, and placement is based on lifecycle ownership, not convenience. fileciteturn2file0
> 2. **All external inputs must pass through the registration pipeline**; email is explicitly listed as a future connector intake. fileciteturn2file0
> 3. **Derived layers cannot become truth sources**; vector/graph/AI must stay downstream. fileciteturn2file0
> 4. **File-derived objects must carry `archive_id`**, and domain-scoped objects must carry `tenant_id`. fileciteturn2file0
> 
> So the right move is **not** “add an email blob store somewhere.”  
> The right move is:
> 
> ## Exact setup I’d use
> 
> ### 1) Keep email as an integration + domain object, not a rogue subsystem
> 
> Use this ownership split:
> 
> - **`qione`**
>   - mailbox/account ownership
>   - tenant linkage
>   - provider credentials metadata only if you must track account registration state
> - **`qiarchive`**
>   - canonical registration of every ingested email message and attachment that enters the Spine
>   - extraction/chunking metadata
>   - provenance, checksums, status, lineage
> - **`qially`**
>   - embeddings, memory records, retrieval/session artifacts, summarization artifacts
> - **`qivault`**
>   - secure retained attachment/file objects when they are treated as durable tenant documents
> - **`qisys`**
>   - sync jobs, retry jobs, extraction jobs, embedding jobs, classifier jobs, connector state events
> 
> That follows the project’s stated component boundaries and keeps canonical truth in the archive, not in AI or retrieval layers. fileciteturn2file0
> 
> ---
> 
> ## 2) Do **not** make email a separate top-level schema yet
> 
> Right now, your blueprint only has 12 live schemas and no `qiemail` schema. New schemas require ADR-level discipline, band assignment, and registry updates. fileciteturn2file0
> 
> So unless you want email to become a major standalone product/domain later, **don’t create `qiemail` yet**.
> 
> Use:
> 
> - `qiarchive` for the canonical email record
> - optional domain tables in `qivault` or `qicase` when an email/attachment becomes part of a case, vault record, or document workflow
> - `qially` for AI-ready enrichment and memory
> 
> That is cleaner and more aligned with the doctrine.
> 
> ---
> 
> ## 3) Model email as two layers: connector layer + archive layer
> 
> ### A. Connector layer
> This is operational, sync-focused, mutable.
> 
> Put in **`qisys`** or **`qione`** depending on whether you treat accounts as tenant-owned config or worker-owned config.
> 
> Recommended:
> 
> - `qione.email_accounts`
> - `qione.email_account_members` if shared access matters
> - `qisys.email_sync_jobs`
> - `qisys.email_sync_cursors`
> - `qisys.email_connector_events`
> 
> Why:
> - account ownership is platform/tenant-ish
> - sync state and retries are system/job-ish
> 
> ### B. Archive layer
> This is canonical, Spine-aligned, provenance-first.
> 
> Put in **`qiarchive`**:
> 
> - `qiarchive.archive_files` — one row per canonical ingested email object
> - `qiarchive.archive_chunks` — extracted body/attachment chunks
> - `qiarchive.ingest_jobs` — existing pipeline state
> - `qiarchive.file_history` — rename/move/lineage history
> - **new:** `qiarchive.archive_messages`
> - **new:** `qiarchive.archive_message_participants`
> - **new:** `qiarchive.archive_message_attachments`
> - **new:** `qiarchive.archive_message_threads`
> 
> This gives you email-aware metadata without breaking the archive-first rule.
> 
> ---
> 
> ## 4) Canonical email design inside QiArchive
> 
> This is the part you need to lock.
> 
> ### `qiarchive.archive_files`
> Still remains the top-level canonical record.
> 
> For an email message, `archive_files` should store the universal archive stuff already required by the blueprint:
> 
> - `canonical_id`
> - `tenant_id`
> - `domain_prefix`
> - `short_code`
> - `checksum`
> - `source_type`
> - `source_path`
> - `origin_event`
> - `original_filename`
> - `normalized_filename`
> - `mime_type`
> - `status`
> - `storage_path`
> - `created_at`
> - `updated_at`
> 
> That matches the blueprint’s minimum metadata and storage rules. fileciteturn2file0
> 
> For email-specific entries, I’d set:
> 
> - `source_type = 'email_connector'`
> - `mime_type = 'message/rfc822'` or provider-normalized logical type
> - `origin_event = 'gmail_sync' | 'outlook_sync' | 'imap_sync'`
> - `normalized_filename = {domain}_{subject_slug}_{QXXXXXX}.eml`
> 
> ### `qiarchive.archive_messages`
> New table. One row per email message, keyed back to `archive_files`.
> 
> Core fields:
> 
> - `id uuid`
> - `archive_id uuid not null references qiarchive.archive_files`
> - `tenant_id uuid not null`
> - `account_id uuid not null` → references platform config table
> - `provider text`
> - `provider_message_id text`
> - `provider_thread_id text`
> - `internet_message_id text`
> - `subject text`
> - `sent_at timestamptz`
> - `received_at timestamptz`
> - `direction text`
> - `status text`
> - `from_name text`
> - `from_email text`
> - `reply_to jsonb`
> - `headers jsonb`
> - `labels jsonb`
> - `has_attachments boolean`
> - `is_read boolean`
> - `is_starred boolean`
> - `is_archived boolean`
> - `body_text text`
> - `body_html text`
> - `snippet text`
> - `review_state text`
> - `route_state text`
> - `created_at`
> - `updated_at`
> 
> This table is the **message metadata view**, but the canonical anchor is still `archive_id`.
> 
> ### `qiarchive.archive_message_participants`
> - `id`
> - `archive_message_id`
> - `tenant_id`
> - `role` (`from`, `to`, `cc`, `bcc`, `reply_to`)
> - `display_name`
> - `email_address`
> - `email_address_normalized`
> 
> ### `qiarchive.archive_message_threads`
> - `id`
> - `tenant_id`
> - `account_id`
> - `provider_thread_id`
> - `subject_canonical`
> - `last_message_at`
> - `message_count`
> - `unread_count`
> 
> ### `qiarchive.archive_message_attachments`
> This is key.
> 
> - `id`
> - `archive_message_id`
> - `tenant_id`
> - `attachment_archive_id uuid references qiarchive.archive_files`
> - `filename`
> - `mime_type`
> - `size_bytes`
> - `content_hash`
> - `is_inline`
> - `content_id`
> - `storage_path`
> - `extracted_text`
> - `created_at`
> 
> Every real attachment should also become its **own registered `archive_files` record** if it enters canonical processing. That is the right Spine move, because file-derived things need archive lineage. fileciteturn2file0
> 
> ---
> 
> ## 5) Where the actual file/object bytes live
> 
> Your blueprint says:
> 
> - local filesystem is physical truth for files
> - Supabase Postgres is canonical metadata/index
> - exports are non-canonical and belong outside canonical tables
> - qivault is the secure document store domain. fileciteturn2file0
> 
> So for email attachments:
> 
> ### Use this storage pattern
> - **raw downloaded attachments**: local staging under `C:/QiData/processing/email/...`
> - **registered canonical storage path**: either a managed storage bucket or your secure retained store
> - **durable sensitive docs**: surface them through `qivault.documents`
> 
> What to add:
> - a dedicated **private storage bucket/path convention** for email connector objects
> - path example:
>   - `tenant/{tenant_id}/email/{account_id}/{archive_id}/raw.eml`
>   - `tenant/{tenant_id}/email/{account_id}/{archive_id}/attachments/{attachment_archive_id}_{filename}`
> 
> That satisfies the storage-path requirement without muddying canonical DB truth. The blueprint explicitly says storage-path metadata belongs on the archive record. fileciteturn2file0
> 
> ---
> 
> ## 6) AI readiness: where embeddings and memory actually go
> 
> This is where people build garbage by mixing everything.
> 
> Your project already says:
> - `qially` owns AI sessions, messages, memory embeddings
> - vector is derived
> - graph is derived
> - archive/chunk provenance must stay intact. fileciteturn2file0
> 
> So do **not** store “email embeddings” as the source of truth in the email/message tables.
> 
> Do this instead:
> 
> ### canonical extraction path
> 1. email message registered in `qiarchive.archive_files`
> 2. body extracted
> 3. body chunked into `qiarchive.archive_chunks`
> 4. attachments extracted and chunked as their own archive-linked records
> 5. embeddings generated from chunks
> 6. AI memory or retrieval artifacts written in `qially`
> 
> ### add to `qially`
> You need explicit provenance-aware AI tables, if not already defined beyond “memory_embeddings”:
> 
> - `qially.memory_embeddings`
>   - `id`
>   - `tenant_id`
>   - `archive_id`
>   - `chunk_id`
>   - `source_schema`
>   - `source_table`
>   - `source_record_id`
>   - `embedding vector`
>   - `embedding_model`
>   - `embedding_status`
>   - `created_at`
> 
> - `qially.memory_records`
>   - durable AI-readable memory summaries or recall units
>   - must reference `archive_id` / `chunk_id` / source provenance
> 
> This matches the blueprint’s “memories should reference source provenance where possible” and “chatbot evidence must reference archive/chunk/entity IDs.” fileciteturn2file0
> 
> ---
> 
> ## 7) The sync + job model you need
> 
> The blueprint already defines workers, retries, and integration contracts, plus the rule that workers write state to `qisys.jobs` and must always operate on canonical IDs. fileciteturn2file0
> 
> So for email, add:
> 
> ### `qisys.jobs` job types
> - `email_sync`
> - `email_message_register`
> - `email_attachment_register`
> - `email_extract`
> - `email_chunk`
> - `email_embed`
> - `email_route`
> - `email_case_link`
> - `email_repair`
> 
> ### `qisys.system_events`
> Event types:
> - `email_account_connected`
> - `email_sync_started`
> - `email_sync_completed`
> - `email_sync_failed`
> - `email_message_registered`
> - `email_attachment_registered`
> - `email_message_routed`
> - `email_message_linked_to_case`
> 
> ### sync cursor table
> If not folded into `email_accounts`, add:
> - `qisys.email_sync_cursors`
>   - `account_id`
>   - `provider`
>   - `cursor_value`
>   - `last_synced_at`
>   - `sync_status`
>   - `last_error`
> 
> That keeps operational sync state out of the canonical archive tables.
> 
> ---
> 
> ## 8) RLS / tenancy rules for this schema
> 
> This part is non-optional.
> 
> The blueprint is clear:
> - every domain-scoped table gets `tenant_id`
> - RLS is universal
> - Supabase Auth + `qione.tenant_members` is the identity mapping
> - no service may bypass the platform boundary. fileciteturn2file0
> 
> So all new email-related tables should carry `tenant_id`, including:
> 
> - `qione.email_accounts`
> - `qiarchive.archive_messages`
> - `qiarchive.archive_message_threads`
> - `qiarchive.archive_message_participants`
> - `qiarchive.archive_message_attachments`
> - `qially.memory_embeddings`
> - all relevant `qisys` job/event rows
> 
> And all frontend reads must happen through JWT/RLS-safe app APIs, not direct service-role abuse. The blueprint explicitly forbids bypassing the pipeline and tenant boundaries. fileciteturn2file0
> 
> ---
> 
> ## 9) What to add to the Master Blueprint
> 
> This is the part you asked for directly.
> 
> You need to update the blueprint in **five places**.
> 
> ### A. 03 Structure / Object Model
> Add **email objects** explicitly to the canonical object families.
> 
> Add:
> - email_accounts
> - email_messages
> - email_threads
> - email_participants
> - email_attachments
> - connector_events
> - sync_cursors
> 
> And define their homes:
> 
> - `qione` → email account ownership/config
> - `qiarchive` → canonical message/archive representation
> - `qisys` → sync jobs/events
> - `qially` → memory/embedding artifacts
> - `qivault` → promoted secure document retention for attachments/documents
> 
> Why: right now email is only implied as a future connector, not modeled as an object family.
> 
> ### B. 04 Data / Schema
> Add a dedicated subsection like:
> 
> **“Email Connector Data Model”**
> 
> Lock these decisions:
> - email intake is an integration path, not a standalone truth source
> - every ingested message registers in `qiarchive`
> - every file attachment that enters processing gets its own `archive_id`
> - canonical message metadata lives in `qiarchive.archive_messages`
> - AI/session/memory artifacts live in `qially`
> - sync cursors and connector jobs live in `qisys`
> - secure long-retained attachments may be promoted to `qivault.documents`
> 
> ### C. 04 Data / Storage
> Add storage path rules for email:
> 
> - raw message object path
> - attachment object path
> - promotion rule from attachment → vault doc
> - explicit statement that raw provider payloads and exports are non-canonical unless registered
> 
> The blueprint already says storage-path rules must be locked and exports are non-canonical. This just makes email obey that law instead of floating. fileciteturn2file0
> 
> ### D. 05 Compute / Integrations
> Expand “future email intake” into a real integration contract.
> 
> Add:
> - provider sources: Gmail / Outlook / IMAP
> - trigger types: scheduled sync, webhook, manual pull
> - intake path: `connector → qisys job → qiarchive registration → extraction → chunk → embed → route`
> - failure handling: retryable, stateful, canonical-ID based
> - requirement that connector-created records always carry `tenant_id`
> 
> This is directly consistent with the project’s integration rules. fileciteturn2file0
> 
> ### E. 07 Governance & Working Memory
> Move email from “unstated future thing” into the **Immediate Next Decisions** or **Open Design Areas** as a concrete item:
> 
> Add open decisions:
> - lock email connector ownership model (`qione` vs `qisys`)
> - lock `qiarchive.archive_messages*` table family
> - lock attachment promotion rule into `qivault`
> - lock AI memory contract for email-derived chunks in `qially`
> - lock email sync cursor and retry contract
> - lock provider normalization rules for Gmail/Outlook/IMAP
> 
> ---
> 
> ## 10) Specific blueprint language I would add
> 
> Use this as the actual content to insert.
> 
> ### Add under Object Model
> **Email Objects**
> - `email_accounts` → platform-owned mailbox/account registrations
> - `email_messages` → canonical archive-linked email message records
> - `email_threads` → provider/thread grouping metadata
> - `email_participants` → normalized sender/recipient records
> - `email_attachments` → archive-linked attachment records
> - `email_sync_jobs` / `email_connector_events` → integration and worker-state records
> 
> ### Add under Placement Rules
> - Email connector account ownership belongs to `qione` when tied to tenant/platform configuration.
> - Canonical email message and attachment records belong to `qiarchive` once ingested.
> - AI summaries, memory embeddings, and retrieval artifacts derived from email belong to `qially`.
> - Sync jobs, retries, cursors, and connector event logs belong to `qisys`.
> - Promoted secure attachment documents belong to `qivault`.
> 
> ### Add under Storage Rules
> - Raw email messages and attachments may exist in connector/object storage, but are not canonical until registered in `qiarchive`.
> - Every processed attachment must either:
>   - remain an archive-linked attachment object, or
>   - be promoted into `qivault.documents` with preserved `archive_id` lineage.
> - Email-derived exports and summaries are non-canonical and must never overwrite archive truth.
> 
> ### Add under Integrations
> **Email Intake Contract**
> - Entry sources: Gmail, Outlook, IMAP, or future provider adapters
> - Flow: connector pull/webhook → `qisys` job → `qiarchive` registration → extraction → chunking → embedding → routing
> - Every created record must include `tenant_id`
> - No provider connector may write directly to final canonical records without passing through the registration pipeline
> 
> ### Add under Open Design Areas
> - Email connector account model
> - Canonical email thread/message/attachment schema
> - Attachment-to-vault promotion rules
> - Email-specific route confidence model
> - Email summarization vs durable memory policy
> - Provider normalization contract
> 
> ---
> 
> ## 11) The thing you should **not** do
> 
> Do **not** leave email bodies and attachments only in a loose `emails` table outside QiArchive.
> 
> That would violate your own rules:
> - no important file enters without registration
> - derived systems can’t become truth
> - file-derived objects need archive lineage
> - placement is by lifecycle ownership. fileciteturn2file0
> 
> That setup would work for a cheap inbox clone.  
> It does **not** work for QiOS.
> 
> ---
> 
> ## 12) Final call
> 
> ### Recommended architecture
> - **No new `qiemail` schema yet**
> - **Add email account config in `qione`**
> - **Add canonical email message family in `qiarchive`**
> - **Add sync/retry/event support in `qisys`**
> - **Add AI memory/embedding provenance in `qially`**
> - **Use `qivault` when attachments become durable secure docs**
> 
> ### Blueprint changes needed right now
> You should add:
> 1. email object family definitions
> 2. placement rules for email records
> 3. email connector data model section
> 4. storage path and promotion rules
> 5. integration contract for email intake
> 6. new open decisions list for email schema + AI memory contract
> 
> That is the clean setup. Everything else is asking for schema drift and future cleanup.
> 
> If you want, next I’ll turn this into a **blueprint-ready patch block** with exact section headings and copy-paste text for the Master Blueprint.

### User
> or we can have the antigravity ide do it. just give me the full complete prompt and a way to check its work.

### Assistant
> Yep. Here’s the **full Antigravity IDE prompt** and the **checklist to grade it afterward**.
> 
> This is grounded in the current blueprint rules: one canonical home per concern, no parallel schema drift without ADR, email intake must enter through the registration pipeline, every domain-scoped record needs `tenant_id`, every file-derived record needs `archive_id`, derived AI/graph layers stay downstream, and `public` must not get new tables. fileciteturn5file0
> 
> ## Antigravity IDE prompt
> 
> ```text
> You are updating the QiOS Master Blueprint doctrine to incorporate email intake and the new email/archive/AI-ready schema design.
> 
> Read the existing QiOS Master Blueprint carefully first and preserve its constitutional style, terminology, section structure, and doctrine-first tone.
> 
> Your job is NOT to invent a separate standalone email subsystem unless the existing blueprint rules require it.
> Your job IS to integrate email cleanly into the current QiOS architecture without violating the existing rules.
> 
> ==================================================
> PRIMARY ARCHITECTURAL DECISION TO IMPLEMENT
> ==================================================
> 
> Implement the following architecture decision across the blueprint:
> 
> 1. DO NOT create a new top-level qiemail schema in the blueprint at this time.
> 2. Email must be modeled as an integration/input path into the Spine.
> 3. Email account ownership/config belongs in qione if it is tenant/platform configuration.
> 4. Canonical email message registration belongs in qiarchive.
> 5. AI embeddings, retrieval memory, and provenance-aware AI artifacts belong in qially.
> 6. Sync jobs, retries, connector events, and cursor state belong in qisys.
> 7. Secure promoted attachment documents belong in qivault when an email attachment becomes a durable secure document.
> 8. Email is a future/planned integration that must pass through the canonical registration pipeline before downstream processing.
> 9. Every email-derived file/attachment that becomes canonical must receive archive_id lineage.
> 10. Every tenant-scoped email-related table must carry tenant_id and obey RLS doctrine.
> 11. Derived layers (graph/vector/AI) must never become truth sources.
> 
> ==================================================
> NON-NEGOTIABLE CONSTRAINTS
> ==================================================
> 
> Follow the existing blueprint law exactly:
> 
> - one canonical home per concern
> - one schema per domain
> - no new public schema tables
> - no schema drift from doctrine
> - no cross-boundary ownership confusion
> - no direct integration writes into canonical qiarchive records that bypass the pipeline
> - all integrations must carry tenant_id
> - all file-derived objects must reference archive_id
> - AI evidence/memory must preserve provenance
> - exports remain non-canonical
> - avoid creating parallel schemas without an ADR
> 
> If a brand-new schema would be required to do this correctly, do NOT create it silently. Instead, explicitly state that a future ADR would be required. For this patch, assume email can and should be integrated into existing schemas.
> 
> ==================================================
> WHAT TO CHANGE
> ==================================================
> 
> Update the blueprint so email becomes an explicitly modeled object family and integration path.
> 
> Make doctrine-level edits in the most appropriate existing sections. Preserve the current 7-section system and the v0.4 blueprint style.
> 
> At minimum, update these conceptual areas:
> 
> A. STRUCTURE / OBJECT MODEL
> - Add explicit email-related object families:
>   - email_accounts
>   - email_messages
>   - email_threads
>   - email_participants
>   - email_attachments
>   - email_sync_jobs
>   - email_connector_events
>   - email_sync_cursors
> - Clarify the canonical home for each:
>   - qione = email_accounts / platform ownership
>   - qiarchive = canonical email message and attachment registration layer
>   - qisys = jobs, retries, cursors, connector events
>   - qially = memory embeddings / AI recall artifacts / provenance-aware derived records
>   - qivault = promoted secure attachments/documents when durable retention is needed
> 
> B. PLACEMENT RULES
> Add explicit placement language for email:
> - Email account config belongs to qione
> - Ingested email messages are treated as ingested records and belong to qiarchive once registered
> - Email-derived AI memory belongs to qially
> - Email sync events/jobs belong to qisys
> - Durable secure email attachments may be promoted to qivault
> - Do not create qiemail unless future ADR explicitly approves it
> 
> C. DATA / SCHEMA
> Add a new doctrine subsection such as:
> - "Email Connector Data Model"
> or
> - "Email Intake Schema Contract"
> 
> Define the doctrine-level table family to be added conceptually:
> - qione.email_accounts
> - qiarchive.archive_messages
> - qiarchive.archive_message_threads
> - qiarchive.archive_message_participants
> - qiarchive.archive_message_attachments
> - qisys.email_sync_cursors OR equivalent worker-state placement
> - qially provenance-aware memory/embedding linkage for email-derived chunks
> 
> Do NOT write full SQL migrations in the blueprint unless that is already the blueprint style.
> This is doctrine/spec language, not runtime implementation.
> 
> D. DATA / STORAGE
> Add storage rules for email objects:
> - raw message payloads and attachments may land in connector/object storage or local staging
> - they are not canonical until registered in qiarchive
> - canonical storage path metadata must live on archive-linked records
> - attachments that become canonical files receive archive_id lineage
> - promoted secure attachments may be represented in qivault.documents while preserving archive lineage
> - exports/summaries remain non-canonical
> 
> Add example path conventions at doctrine level if appropriate, such as:
> - tenant/{tenant_id}/email/{account_id}/{archive_id}/raw.eml
> - tenant/{tenant_id}/email/{account_id}/{archive_id}/attachments/{attachment_archive_id}_{filename}
> 
> E. COMPUTE / INTEGRATIONS / PIPELINES
> Expand future email intake from a vague note into a real contract:
> - source: Gmail / Outlook / IMAP / future adapters
> - entry: integration API / connector worker
> - flow:
>   connector pull or webhook
>   -> qisys job/event
>   -> qiarchive registration
>   -> extract
>   -> chunk
>   -> embed
>   -> route/review/act
> - all worker inputs/outputs must reference canonical IDs
> - failures must be visible, stateful, retryable
> - integration must never bypass registration pipeline
> - email records must carry tenant_id
> 
> F. GOVERNANCE / OPEN DECISIONS
> Update the "Immediate Next Decisions" or "Open Design Areas" to include email-specific unresolved work:
> - lock email connector ownership model
> - lock archive_messages doctrine
> - lock attachment promotion rule into qivault
> - lock email sync cursor contract
> - lock provider normalization rules
> - lock memory vs retrieval policy for email-derived artifacts
> 
> ==================================================
> REQUIRED OUTPUT STYLE
> ==================================================
> 
> Return your work as:
> 
> 1. A concise summary of what changed
> 2. A file-by-file patch plan (which blueprint docs should be edited and why)
> 3. The exact markdown sections to insert/update
> 4. A final "consistency check" section explaining why the patch does NOT violate:
>    - single domain rule
>    - band model
>    - archive-first registration
>    - downstream-derived AI rule
>    - tenant isolation rule
> 
> ==================================================
> QUALITY BAR
> ==================================================
> 
> The result should feel like a native extension of the QiOS blueprint, not an afterthought.
> Do not write fluffy explanation.
> Do not duplicate existing doctrine unnecessarily.
> Do not create shadow concepts that already map cleanly to existing schemas.
> Prefer the minimum set of additions that make email fully legible in the architecture.
> 
> If a concept belongs in existing sections, patch those sections instead of inventing new blueprint sprawl.
> 
> At the end, include a short "Rejected Alternatives" note with:
> - why not qiemail right now
> - why not store email only in qially
> - why not let integrations write directly to canonical tables
> ```
> 
> ## How to check its work
> 
> Use this as the **acceptance test**. If it fails any of these, the patch is wrong.
> 
> ### 1. Schema discipline
> It should **not** create `qiemail` as if that’s already approved. The current blueprint says every new schema must be declared and schema/topology changes require ADR discipline, and placement is by lifecycle ownership, not convenience. fileciteturn5file0
> 
> Pass if:
> - it keeps email inside existing domains/schemas
> - it says a future `qiemail` would require ADR approval
> 
> Fail if:
> - it casually invents a new schema
> - it adds email stuff to `public`
> 
> ### 2. Archive-first rule
> It must explicitly say email intake goes through **integration → pipeline → QiArchive registration** before downstream processing, because the blueprint already says all external data must pass through the registration pipeline and email intake is a future connector service. fileciteturn5file1
> 
> Pass if:
> - email messages/attachments become canonical only after registration
> - it preserves canonical ID / short code / lineage language
> 
> Fail if:
> - connector writes directly into final business tables as truth
> - AI or search becomes the first storage layer
> 
> ### 3. Placement logic
> It must map ownership like this:
> 
> - `qione` = email account/platform ownership
> - `qiarchive` = registered message/attachment records
> - `qisys` = jobs/events/cursors/retries
> - `qially` = derived memory/embeddings
> - `qivault` = promoted secure retained docs
> 
> That matches the blueprint’s service ownership rules and placement rules. fileciteturn5file0
> 
> Pass if:
> - every email object has one clear home
> 
> Fail if:
> - same concept appears as truth in multiple schemas
> 
> ### 4. Tenant and archive lineage
> It must say:
> - tenant-scoped email records require `tenant_id`
> - file-derived records require `archive_id`
> 
> That is already blueprint law. fileciteturn5file0
> 
> Pass if:
> - it states both explicitly
> 
> Fail if:
> - email attachments are modeled canonically without archive lineage
> - cross-tenant ambiguity is left fuzzy
> 
> ### 5. Derived-layer discipline
> It must keep AI, vector, and graph downstream only. The blueprint is blunt that graph/vector/AI are derived, not canonical, and memories should preserve source provenance. fileciteturn5file0
> 
> Pass if:
> - embeddings/memory are described as derived from archive-linked chunks/messages
> - provenance is explicit
> 
> Fail if:
> - it stores canonical email truth in `qially`
> - it lets graph or vector redefine record truth
> 
> ### 6. Integration contract quality
> It should expand “future email intake” into a real contract:
> - trigger
> - format
> - entry point
> - output
> - failure handling
> - tenant handling
> 
> That’s already how the blueprint defines integrations. fileciteturn5file1
> 
> Pass if:
> - it makes email a concrete integration contract
> 
> Fail if:
> - it just adds “email intake” as a bullet and calls it done
> 
> ### 7. Open decisions updated
> The blueprint’s current open decisions are still broad and need locking around ingest schema, storage path rules, metadata gates, and retrieval contract. Email should now appear in those open decisions/open design areas. fileciteturn5file0
> 
> Pass if:
> - it adds email-specific unresolved decisions
> 
> Fail if:
> - it patches doctrine but leaves no tracked decision debt
> 
> ## Fast grading rubric
> 
> Give it a score out of 10:
> 
> - **2 points** if no rogue `qiemail`
> - **2 points** if email goes through QiArchive registration
> - **2 points** if ownership split is correct across `qione / qiarchive / qisys / qially / qivault`
> - **2 points** if `tenant_id` and `archive_id` rules are explicit
> - **2 points** if open decisions are updated
> 
> Anything under **9/10** means the patch still has structural drift.
> 
> ## The one sentence standard
> 
> If the result does **not** make email look like a native Spine input with archive lineage and downstream AI provenance, it’s wrong. That is the whole game. fileciteturn5file1
> 
> If you want, I can also give you the **expected ideal patch outline** so you can compare the IDE’s output against a target shape.

### User
> by the way i added these files. # Project Structure
> 
> ```
> ├── _QiOne_MonoRepo_v0.4
> │   ├── __QiOS_Master_Blueprint_v0.4
> │   │   ├── assets
> │   │   │   ├── diagrams
> │   │   │   └── tables
> │   │   ├── docs
> │   │   │   ├── 01_governance
> │   │   │   │   ├── decisions.md
> │   │   │   │   ├── index.md
> │   │   │   │   ├── policies.md
> │   │   │   │   ├── principles.md
> │   │   │   │   ├── registry.md
> │   │   │   │   └── standards.md
> │   │   │   ├── 02_architecture
> │   │   │   │   ├── component_map.md
> │   │   │   │   ├── data_flow.md
> │   │   │   │   ├── identity.md
> │   │   │   │   ├── index.md
> │   │   │   │   ├── runtime_zones.md
> │   │   │   │   ├── service_boundaries.md
> │   │   │   │   └── system_model.md
> │   │   │   ├── 03_structure
> │   │   │   │   ├── bands.md
> │   │   │   │   ├── domains.md
> │   │   │   │   ├── index.md
> │   │   │   │   ├── object_model.md
> │   │   │   │   ├── placement_rules.md
> │   │   │   │   └── subdomains.md
> │   │   │   ├── 04_data
> │   │   │   │   ├── exports.md
> │   │   │   │   ├── index.md
> │   │   │   │   ├── metadata.md
> │   │   │   │   ├── objects.md
> │   │   │   │   ├── schema.md
> │   │   │   │   └── storage.md
> │   │   │   ├── 05_compute
> │   │   │   │   ├── apis.md
> │   │   │   │   ├── index.md
> │   │   │   │   ├── integrations.md
> │   │   │   │   ├── pipelines.md
> │   │   │   │   ├── runtime.md
> │   │   │   │   └── workers.md
> │   │   │   ├── 06_applications
> │   │   │   │   ├── admin.md
> │   │   │   │   ├── index.md
> │   │   │   │   ├── interfaces.md
> │   │   │   │   ├── portal.md
> │   │   │   │   ├── tools.md
> │   │   │   │   └── web.md
> │   │   │   ├── 07_operations
> │   │   │   │   ├── cases.md
> │   │   │   │   ├── clients.md
> │   │   │   │   ├── finance.md
> │   │   │   │   ├── index.md
> │   │   │   │   ├── products.md
> │   │   │   │   └── templates.md
> │   │   │   ├── adr
> │   │   │   │   ├── ADR-0000_template.md
> │   │   │   │   ├── ADR-0001_blueprint_scope.md
> │   │   │   │   ├── ADR-0002_single_domain_rule.md
> │   │   │   │   └── ADR-0003_band_model.md
> │   │   │   ├── appendices
> │   │   │   │   ├── changelog.md
> │   │   │   │   ├── glossary.md
> │   │   │   │   └── migration_notes.md
> │   │   │   ├── stylesheets
> │   │   │   │   └── extra.css
> │   │   │   └── index.md
> │   │   ├── overrides
> │   │   │   └── home.html
> │   │   ├── registry
> │   │   │   ├── band_registry.yaml
> │   │   │   ├── deprecation_registry.yaml
> │   │   │   ├── domain_registry.yaml
> │   │   │   └── subdomain_registry.yaml
> │   │   ├── schemas
> │   │   │   └── band_registry.schema.json
> │   │   ├── scripts
> │   │   │   └── enforce_structure.py
> │   │   ├── standards
> │   │   │   ├── metadata_rules.yaml
> │   │   │   ├── naming_rules.yaml
> │   │   │   ├── pdf_standards.yaml
> │   │   │   └── repo_rules.yaml
> │   │   ├── main.py
> │   │   ├── mkdocs.yml
> │   │   ├── QIO00001_00_QiOS_MASTER_README.MD
> │   │   └── README.md
> │   ├── _App_Experiments
> │   │   ├── Atrium-main
> │   │   ├── notion2pg
> │   │   │   ├── LICENSE
> │   │   │   ├── notion2pg.py
> │   │   │   ├── pyproject.toml
> │   │   │   └── README.rst
> │   │   ├── ns8-arkcase-main
> │   │   │   ├── ns8-arkcase-main
> │   │   │   │   ├── imageroot
> │   │   │   │   │   ├── actions
> │   │   │   │   │   ├── bin
> │   │   │   │   │   ├── etc
> │   │   │   │   │   ├── events
> │   │   │   │   │   ├── systemd
> │   │   │   │   │   └── update-module.d
> │   │   │   │   ├── tests
> │   │   │   │   │   ├── __init__.robot
> │   │   │   │   │   ├── kickstart.robot
> │   │   │   │   │   └── pythonreq.txt
> │   │   │   │   ├── ui
> │   │   │   │   │   ├── public
> │   │   │   │   │   ├── src
> │   │   │   │   │   ├── babel.config.js
> │   │   │   │   │   ├── container-entrypoint.sh
> │   │   │   │   │   ├── Containerfile
> │   │   │   │   │   ├── package.json
> │   │   │   │   │   ├── README.md
> │   │   │   │   │   ├── vue.config.js
> │   │   │   │   │   └── yarn.lock
> │   │   │   │   ├── build-images.sh
> │   │   │   │   ├── LICENSE
> │   │   │   │   ├── package.json
> │   │   │   │   ├── README.md
> │   │   │   │   └── test-module.sh
> │   │   │   └── install.sh
> │   │   ├── QiBP
> │   │   │   ├── public
> │   │   │   │   ├── _redirects
> │   │   │   │   ├── introvideo.mp4
> │   │   │   │   └── QiBPAppIcon.png
> │   │   │   ├── app.jsx
> │   │   │   ├── index.html
> │   │   │   ├── main.jsx
> │   │   │   ├── manifest.json
> │   │   │   ├── package-lock.json
> │   │   │   ├── package.json
> │   │   │   ├── README.md
> │   │   │   ├── tailwind.config.js
> │   │   │   └── vite.config.js
> │   │   ├── QiLauncher
> │   │   │   ├── api
> │   │   │   │   ├── adminClient.ts
> │   │   │   │   └── client.ts
> │   │   │   ├── components
> │   │   │   │   ├── chat
> │   │   │   │   │   ├── ChatHeader.tsx
> │   │   │   │   │   ├── ChatInput.tsx
> │   │   │   │   │   ├── ChatSidebar.tsx
> │   │   │   │   │   ├── MessageBubble.tsx
> │   │   │   │   │   └── MessageList.tsx
> │   │   │   │   ├── dashboard
> │   │   │   │   │   ├── DeploymentsTable.tsx
> │   │   │   │   │   ├── HealthWidget.tsx
> │   │   │   │   │   ├── PageHeader.tsx
> │   │   │   │   │   ├── QueueWidget.tsx
> │   │   │   │   │   ├── StatCard.tsx
> │   │   │   │   │   └── WorkersWidget.tsx
> │   │   │   │   ├── layout
> │   │   │   │   │   ├── AppLayout.tsx
> │   │   │   │   │   ├── MobileHeader.tsx
> │   │   │   │   │   └── Sidebar.tsx
> │   │   │   │   └── views
> │   │   │   │       ├── HealthView.tsx
> │   │   │   │       ├── IngestionQueueView.tsx
> │   │   │   │       ├── JobsView.tsx
> │   │   │   │       ├── QueueView.tsx
> │   │   │   │       ├── SettingsView.tsx
> │   │   │   │       └── WorkersView.tsx
> │   │   │   ├── hooks
> │   │   │   │   └── useSpeechRecognition.ts
> │   │   │   ├── public
> │   │   │   │   └── README.md
> │   │   │   ├── src
> │   │   │   │   ├── index.css
> │   │   │   │   ├── main.jsx
> │   │   │   │   └── tailwind.css
> │   │   │   ├── types
> │   │   │   │   └── speech.d.ts
> │   │   │   ├── utils
> │   │   │   │   └── speech.ts
> │   │   │   ├── _readme.md
> │   │   │   ├── App.tsx
> │   │   │   ├── index.html
> │   │   │   ├── package-lock.json
> │   │   │   ├── package.json
> │   │   │   ├── README.md
> │   │   │   ├── styles.css
> │   │   │   ├── tailwind.config.js
> │   │   │   ├── tsconfig.json
> │   │   │   ├── tsconfig.node.json
> │   │   │   ├── types.ts
> │   │   │   └── vite.config.js
> │   │   ├── QiNote
> │   │   │   ├── api
> │   │   │   │   └── qimind
> │   │   │   ├── legacy
> │   │   │   │   ├── src
> │   │   │   │   │   ├── components
> │   │   │   │   │   ├── core
> │   │   │   │   │   ├── features
> │   │   │   │   │   ├── hooks
> │   │   │   │   │   ├── lib
> │   │   │   │   │   ├── qidocs
> │   │   │   │   │   ├── routes
> │   │   │   │   │   ├── store
> │   │   │   │   │   ├── styles
> │   │   │   │   │   ├── types
> │   │   │   │   │   ├── App.tsx
> │   │   │   │   │   ├── main.tsx
> │   │   │   │   │   └── vite-env.d.ts
> │   │   │   │   ├── index.html
> │   │   │   │   ├── package-lock.json
> │   │   │   │   ├── package.json
> │   │   │   │   ├── QiNotePlan.md
> │   │   │   │   ├── README_INTEGRATION.md
> │   │   │   │   ├── README.md
> │   │   │   │   ├── tailwind.config.js
> │   │   │   │   ├── tsconfig.json
> │   │   │   │   └── vite.config.ts
> │   │   │   ├── src
> │   │   │   │   ├── components
> │   │   │   │   │   ├── common
> │   │   │   │   │   ├── AiActionsPanel.tsx
> │   │   │   │   │   ├── EditorShell.tsx
> │   │   │   │   │   ├── NoteMetadataPanel.tsx
> │   │   │   │   │   ├── NoteSidebar.tsx
> │   │   │   │   │   ├── RelatedNotesPanel.tsx
> │   │   │   │   │   └── RightPanel.tsx
> │   │   │   │   ├── hooks
> │   │   │   │   │   └── useNotes.ts
> │   │   │   │   ├── lib
> │   │   │   │   │   └── api.ts
> │   │   │   │   ├── routes
> │   │   │   │   │   ├── NoteEditorPage.tsx
> │   │   │   │   │   └── NoteListPage.tsx
> │   │   │   │   ├── styles
> │   │   │   │   │   └── index.css
> │   │   │   │   ├── types
> │   │   │   │   │   └── note.ts
> │   │   │   │   ├── App.tsx
> │   │   │   │   ├── main.tsx
> │   │   │   │   └── vite-env.d.ts
> │   │   │   ├── index.html
> │   │   │   ├── package-lock.json
> │   │   │   ├── package.json
> │   │   │   ├── README.md
> │   │   │   └── tailwind.config.js
> │   │   └── zlabs
> │   │       └── Atrium
> │   │           ├── apps
> │   │           │   ├── api
> │   │           │   └── web
> │   │           ├── docker
> │   │           │   ├── api-entrypoint.sh
> │   │           │   ├── api.Dockerfile
> │   │           │   ├── Caddyfile
> │   │           │   ├── DOCKERHUB.md
> │   │           │   ├── unified-entrypoint.sh
> │   │           │   ├── unified.Dockerfile
> │   │           │   └── web.Dockerfile
> │   │           ├── docs
> │   │           │   ├── configuration.md
> │   │           │   ├── development.md
> │   │           │   ├── docker.md
> │   │           │   ├── roadmap.md
> │   │           │   ├── security.md
> │   │           │   └── unraid.md
> │   │           ├── e2e
> │   │           │   ├── tests
> │   │           │   ├── global-setup.ts
> │   │           │   └── playwright.config.ts
> │   │           ├── packages
> │   │           │   ├── database
> │   │           │   ├── email
> │   │           │   └── shared
> │   │           ├── public
> │   │           │   ├── dashboard.png
> │   │           │   ├── icon.png
> │   │           │   └── landing.png
> │   │           ├── scripts
> │   │           │   ├── dev.ts
> │   │           │   ├── setup.ts
> │   │           │   ├── unraid-vm-snapshot.sh
> │   │           │   └── update-dockerhub-readme.sh
> │   │           ├── unraid
> │   │           ├── bun.lock
> │   │           ├── bunfig.toml
> │   │           ├── CHANGELOG.md
> │   │           ├── CLAUDE.md
> │   │           ├── docker-compose.dev.yml
> │   │           ├── docker-compose.yml
> │   │           ├── LICENSE
> │   │           ├── package.json
> │   │           ├── README.md
> │   │           ├── SECURITY_AUDIT.md
> │   │           ├── tsconfig.json
> │   │           └── turbo.json
> │   ├── _QiData
> │   │   ├── embeddings_cache
> │   │   ├── extracted_text
> │   │   ├── failed
> │   │   ├── inbox
> │   │   ├── logs
> │   │   ├── manifests
> │   │   ├── model_cache
> │   │   ├── processing
> │   │   └── reviewed
> │   ├── apps
> │   │   ├── admin-portal
> │   │   │   ├── src
> │   │   │   │   ├── assets
> │   │   │   │   │   └── index.css
> │   │   │   │   ├── components
> │   │   │   │   │   └── layout
> │   │   │   │   ├── features
> │   │   │   │   │   └── cases
> │   │   │   │   ├── lib
> │   │   │   │   │   └── supabase.ts
> │   │   │   │   ├── pages
> │   │   │   │   │   ├── admin
> │   │   │   │   │   └── SystemStatusPage.tsx
> │   │   │   │   ├── router
> │   │   │   │   │   └── index.tsx
> │   │   │   │   ├── store
> │   │   │   │   │   └── AuthContext.tsx
> │   │   │   │   ├── types
> │   │   │   │   │   └── database.types.ts
> │   │   │   │   ├── App.tsx
> │   │   │   │   ├── main.tsx
> │   │   │   │   └── vite-env.d.ts
> │   │   │   ├── index.html
> │   │   │   ├── package-lock.json
> │   │   │   ├── package.json
> │   │   │   ├── tailwind.config.js
> │   │   │   ├── tsconfig.json
> │   │   │   └── vite.config.ts
> │   │   ├── api
> │   │   │   ├── __pycache__
> │   │   │   │   ├── config.cpython-314.pyc
> │   │   │   │   └── main.cpython-314.pyc
> │   │   │   ├── routers
> │   │   │   │   ├── __init__.py
> │   │   │   │   ├── auth.py
> │   │   │   │   ├── objects.py
> │   │   │   │   ├── organizations.py
> │   │   │   │   └── users.py
> │   │   │   ├── schemas
> │   │   │   │   ├── __init__.py
> │   │   │   │   └── auth.py
> │   │   │   ├── services
> │   │   │   │   ├── __init__.py
> │   │   │   │   └── auth.py
> │   │   │   ├── venv
> │   │   │   │   ├── Include
> │   │   │   │   ├── Lib
> │   │   │   │   │   └── site-packages
> │   │   │   │   ├── Scripts
> │   │   │   │   │   ├── activate
> │   │   │   │   │   ├── activate.bat
> │   │   │   │   │   ├── activate.fish
> │   │   │   │   │   ├── Activate.ps1
> │   │   │   │   │   ├── deactivate.bat
> │   │   │   │   │   ├── pip.exe
> │   │   │   │   │   ├── pip3.14.exe
> │   │   │   │   │   ├── pip3.exe
> │   │   │   │   │   ├── python.exe
> │   │   │   │   │   └── pythonw.exe
> │   │   │   │   └── pyvenv.cfg
> │   │   │   ├── config.py
> │   │   │   ├── database.py
> │   │   │   ├── main.py
> │   │   │   ├── package.json
> │   │   │   └── requirements.txt
> │   │   ├── dashy
> │   │   │   ├── docker
> │   │   │   │   ├── hooks
> │   │   │   │   │   └── pre_build
> │   │   │   │   ├── docker-readme.md
> │   │   │   │   ├── Dockerfile-arm32v7
> │   │   │   │   ├── Dockerfile-arm64v8
> │   │   │   │   ├── Dockerfile-lite
> │   │   │   │   ├── Dockerfile-old
> │   │   │   │   └── nginx.conf
> │   │   │   ├── docs
> │   │   │   │   ├── assets
> │   │   │   │   │   ├── config-editor-demo.gif
> │   │   │   │   │   ├── CONTRIBUTORS.svg
> │   │   │   │   │   ├── logo.png
> │   │   │   │   │   ├── minimal-view-demo.gif
> │   │   │   │   │   ├── repo-visualization.svg
> │   │   │   │   │   ├── sponsor-button.svg
> │   │   │   │   │   ├── status-check-demo.gif
> │   │   │   │   │   ├── theme-config-demo.gif
> │   │   │   │   │   ├── theme-slideshow.gif
> │   │   │   │   │   └── workspace-demo.gif
> │   │   │   │   ├── showcase
> │   │   │   │   │   ├── 1-home-lab-material.png
> │   │   │   │   │   ├── 10-dashy-live.png
> │   │   │   │   │   ├── 11-ricky-cz.png
> │   │   │   │   │   ├── 12-evo-dashboard.png
> │   │   │   │   │   ├── 13-dragons-lair.png
> │   │   │   │   │   ├── 2-networking-services-minimal-dark.png
> │   │   │   │   │   ├── 3-cft-toolbox.png
> │   │   │   │   │   ├── 4-bookmarks-colourful.png
> │   │   │   │   │   ├── 5-project-management.png
> │   │   │   │   │   ├── 6-nas-home-dashboard.png
> │   │   │   │   │   ├── 7-ground-control-dtctek.png
> │   │   │   │   │   ├── 8-shadowking001s-dashy.png
> │   │   │   │   │   ├── 9-home-lab-oblivion.png
> │   │   │   │   │   └── readme.md
> │   │   │   │   ├── alternate-views.md
> │   │   │   │   ├── authentication.md
> │   │   │   │   ├── backup-restore.md
> │   │   │   │   ├── configuring.md
> │   │   │   │   ├── contributing.md
> │   │   │   │   ├── credits.md
> │   │   │   │   ├── deployment.md
> │   │   │   │   ├── developing.md
> │   │   │   │   ├── development-guides.md
> │   │   │   │   ├── icons.md
> │   │   │   │   ├── management.md
> │   │   │   │   ├── multi-language-support.md
> │   │   │   │   ├── pages-and-sections.md
> │   │   │   │   ├── privacy.md
> │   │   │   │   ├── quick-start.md
> │   │   │   │   ├── readme.md
> │   │   │   │   ├── release-workflow.md
> │   │   │   │   ├── searching.md
> │   │   │   │   ├── showcase.md
> │   │   │   │   ├── status-indicators.md
> │   │   │   │   ├── theming.md
> │   │   │   │   ├── troubleshooting.md
> │   │   │   │   └── widgets.md
> │   │   │   ├── public
> │   │   │   │   ├── fonts
> │   │   │   │   │   ├── Audiowide-Regular.ttf
> │   │   │   │   │   ├── CutiveMono-Regular.ttf
> │   │   │   │   │   ├── Digital-Regular.ttf
> │   │   │   │   │   ├── FrancoisOne-Regular.ttf
> │   │   │   │   │   ├── Podkova-Medium.ttf
> │   │   │   │   │   ├── Roboto-Light.ttf
> │   │   │   │   │   ├── Shrikhand-Regular.ttf
> │   │   │   │   │   ├── Sniglet-Regular.ttf
> │   │   │   │   │   └── VT323-Regular.ttf
> │   │   │   │   ├── item-icons
> │   │   │   │   ├── web-icons
> │   │   │   │   │   ├── dashy-logo.png
> │   │   │   │   │   ├── dashy-pwa_144x144.png
> │   │   │   │   │   ├── dashy-pwa_192x192.png
> │   │   │   │   │   ├── dashy-pwa_48x48.png
> │   │   │   │   │   ├── dashy-pwa_512x512.png
> │   │   │   │   │   ├── dashy-pwa_72x72.png
> │   │   │   │   │   ├── dashy-pwa_96x96.png
> │   │   │   │   │   ├── favicon-16x16.png
> │   │   │   │   │   ├── favicon-32x32.png
> │   │   │   │   │   └── favicon-64x64.png
> │   │   │   │   ├── widget-resources
> │   │   │   │   │   ├── WeatherIcons.eot
> │   │   │   │   │   ├── WeatherIcons.svg
> │   │   │   │   │   ├── WeatherIcons.ttf
> │   │   │   │   │   ├── WeatherIcons.woff
> │   │   │   │   │   └── WeatherIcons.woff2
> │   │   │   │   ├── favicon.ico
> │   │   │   │   ├── index.html
> │   │   │   │   ├── initialization.html
> │   │   │   │   ├── loading-screen.css
> │   │   │   │   ├── manifest.json
> │   │   │   │   ├── robots.txt
> │   │   │   │   └── theme-fonts.css
> │   │   │   ├── services
> │   │   │   │   ├── serverless-functions
> │   │   │   │   │   ├── cloud-status-check.js
> │   │   │   │   │   ├── netlify-cors.js
> │   │   │   │   │   └── not-supported.js
> │   │   │   │   ├── config-validator.js
> │   │   │   │   ├── cors-proxy.js
> │   │   │   │   ├── get-user.js
> │   │   │   │   ├── healthcheck.js
> │   │   │   │   ├── print-message.js
> │   │   │   │   ├── rebuild-app.js
> │   │   │   │   ├── save-config.js
> │   │   │   │   ├── ssl-server.js
> │   │   │   │   ├── status-check.js
> │   │   │   │   ├── system-info.js
> │   │   │   │   └── update-checker.js
> │   │   │   ├── src
> │   │   │   │   ├── assets
> │   │   │   │   │   ├── fonts
> │   │   │   │   │   ├── interface-icons
> │   │   │   │   │   └── locales
> │   │   │   │   ├── components
> │   │   │   │   │   ├── Charts
> │   │   │   │   │   ├── Configuration
> │   │   │   │   │   ├── FormElements
> │   │   │   │   │   ├── InteractiveEditor
> │   │   │   │   │   ├── LinkItems
> │   │   │   │   │   ├── MinimalView
> │   │   │   │   │   ├── PageStrcture
> │   │   │   │   │   ├── Settings
> │   │   │   │   │   ├── Widgets
> │   │   │   │   │   └── Workspace
> │   │   │   │   ├── directives
> │   │   │   │   │   ├── ClickOutside.js
> │   │   │   │   │   └── LongPress.js
> │   │   │   │   ├── mixins
> │   │   │   │   │   ├── ChartingMixin.js
> │   │   │   │   │   ├── ConfigSaving.js
> │   │   │   │   │   ├── GlancesMixin.js
> │   │   │   │   │   ├── HomeMixin.js
> │   │   │   │   │   ├── ItemMixin.js
> │   │   │   │   │   ├── NextcloudMixin.js
> │   │   │   │   │   ├── ThemingMixin.js
> │   │   │   │   │   └── WidgetMixin.js
> │   │   │   │   ├── styles
> │   │   │   │   │   ├── widgets
> │   │   │   │   │   ├── color-palette.scss
> │   │   │   │   │   ├── color-themes.scss
> │   │   │   │   │   ├── dimensions.scss
> │   │   │   │   │   ├── global-styles.scss
> │   │   │   │   │   ├── media-queries.scss
> │   │   │   │   │   ├── schema-editor.scss
> │   │   │   │   │   ├── style-helpers.scss
> │   │   │   │   │   ├── typography.scss
> │   │   │   │   │   ├── user-defined-themes.scss
> │   │   │   │   │   └── weather-icons.scss
> │   │   │   │   ├── utils
> │   │   │   │   │   ├── ArrowKeyNavigation.js
> │   │   │   │   │   ├── Auth.js
> │   │   │   │   │   ├── CheckItemVisibility.js
> │   │   │   │   │   ├── CheckPageVisibility.js
> │   │   │   │   │   ├── CheckSectionVisibility.js
> │   │   │   │   │   ├── CloudBackup.js
> │   │   │   │   │   ├── ConfigAccumalator.js
> │   │   │   │   │   ├── ConfigHelpers.js
> │   │   │   │   │   ├── ConfigSchema.json
> │   │   │   │   │   ├── CoolConsole.js
> │   │   │   │   │   ├── defaults.js
> │   │   │   │   │   ├── emojis.json
> │   │   │   │   │   ├── EmojiUnicodeRegex.js
> │   │   │   │   │   ├── ErrorHandler.js
> │   │   │   │   │   ├── ErrorReporting.js
> │   │   │   │   │   ├── HeaderAuth.js
> │   │   │   │   │   ├── InitServiceWorker.js
> │   │   │   │   │   ├── IsVisibleToUser.js
> │   │   │   │   │   ├── KeycloakAuth.js
> │   │   │   │   │   ├── languages.js
> │   │   │   │   │   ├── MiscHelpers.js
> │   │   │   │   │   ├── OidcAuth.js
> │   │   │   │   │   ├── Sanitizer.js
> │   │   │   │   │   ├── Search.js
> │   │   │   │   │   ├── SectionHelpers.js
> │   │   │   │   │   └── StoreMutations.js
> │   │   │   │   ├── views
> │   │   │   │   │   ├── 404.vue
> │   │   │   │   │   ├── About.vue
> │   │   │   │   │   ├── DownloadConfig.vue
> │   │   │   │   │   ├── Home.vue
> │   │   │   │   │   ├── Login.vue
> │   │   │   │   │   ├── Minimal.vue
> │   │   │   │   │   └── Workspace.vue
> │   │   │   │   ├── App.vue
> │   │   │   │   ├── main.js
> │   │   │   │   ├── router.js
> │   │   │   │   └── store.js
> │   │   │   ├── tests
> │   │   │   │   ├── components
> │   │   │   │   │   └── item.test.js
> │   │   │   │   ├── fixtures
> │   │   │   │   │   └── valid-config.yml
> │   │   │   │   ├── unit
> │   │   │   │   │   ├── config-helpers.test.js
> │   │   │   │   │   ├── config-validator.test.js
> │   │   │   │   │   ├── error-handler.test.js
> │   │   │   │   │   ├── healthcheck.test.js
> │   │   │   │   │   └── smoke.test.js
> │   │   │   │   ├── docker-smoke-test.sh
> │   │   │   │   └── setup.js
> │   │   │   ├── user-data
> │   │   │   │   └── conf.yml
> │   │   │   ├── app.json
> │   │   │   ├── CNAME
> │   │   │   ├── docker-compose.yml
> │   │   │   ├── Dockerfile
> │   │   │   ├── LICENSE
> │   │   │   ├── netlify.toml
> │   │   │   ├── package.json
> │   │   │   ├── Procfile
> │   │   │   ├── README.md
> │   │   │   ├── server.js
> │   │   │   ├── tsconfig.json
> │   │   │   ├── vitest.config.js
> │   │   │   ├── vue.config.js
> │   │   │   └── yarn.lock
> │   │   ├── qially-flows
> │   │   │   ├── assets
> │   │   │   │   ├── favicon.ico
> │   │   │   │   ├── logo.svg
> │   │   │   │   └── styles.css
> │   │   │   ├── index.html
> │   │   │   ├── privacy.html
> │   │   │   ├── README.md
> │   │   │   └── terms.html
> │   │   ├── qially-me
> │   │   │   ├── public
> │   │   │   │   ├── cards
> │   │   │   │   │   ├── fresh.png
> │   │   │   │   │   ├── fresh.webp
> │   │   │   │   │   ├── glass.png
> │   │   │   │   │   ├── glass.webp
> │   │   │   │   │   └── mermaid.svg
> │   │   │   │   ├── activity.svg
> │   │   │   │   ├── og.webp
> │   │   │   │   ├── placeholder.webp
> │   │   │   │   └── rss.svg
> │   │   │   ├── scripts
> │   │   │   │   └── build-pagefind-index.ts
> │   │   │   ├── site_QSaysIt_v1
> │   │   │   │   ├── posts
> │   │   │   │   │   ├── 2026
> │   │   │   │   │   └── index.md
> │   │   │   │   ├── qsaysit_blog
> │   │   │   │   │   └── templates
> │   │   │   │   └── templates
> │   │   │   │       ├── 2026-02-19_post-title
> │   │   │   │       └── post_template.md
> │   │   │   ├── src
> │   │   │   │   ├── assets
> │   │   │   │   │   └── creations.json
> │   │   │   │   ├── components
> │   │   │   │   │   ├── blog
> │   │   │   │   │   ├── knowledge-card
> │   │   │   │   │   ├── landing-page
> │   │   │   │   │   ├── navigation
> │   │   │   │   │   ├── slide
> │   │   │   │   │   ├── ui
> │   │   │   │   │   ├── BaseHead.astro
> │   │   │   │   │   ├── BetaBadge.astro
> │   │   │   │   │   ├── copy-button.tsx
> │   │   │   │   │   ├── FormattedDate.astro
> │   │   │   │   │   ├── HeaderLink.astro
> │   │   │   │   │   ├── image-viewer.tsx
> │   │   │   │   │   ├── OptimizedImage.astro
> │   │   │   │   │   ├── ProductCard.tsx
> │   │   │   │   │   ├── ProductSection.astro
> │   │   │   │   │   ├── ShareButtons.astro
> │   │   │   │   │   └── TagFilter.astro
> │   │   │   │   ├── content
> │   │   │   │   │   ├── blogs
> │   │   │   │   │   ├── cards
> │   │   │   │   │   ├── doodles
> │   │   │   │   │   └── slides
> │   │   │   │   ├── layouts
> │   │   │   │   │   ├── ContentIndexLayout.astro
> │   │   │   │   │   └── MainLayout.astro
> │   │   │   │   ├── lib
> │   │   │   │   │   ├── navigation.ts
> │   │   │   │   │   ├── pagination.ts
> │   │   │   │   │   └── utils.ts
> │   │   │   │   ├── pages
> │   │   │   │   │   ├── blogs
> │   │   │   │   │   ├── cards
> │   │   │   │   │   ├── doodles
> │   │   │   │   │   ├── slides
> │   │   │   │   │   ├── creations.astro
> │   │   │   │   │   ├── index.astro
> │   │   │   │   │   ├── og-enhanced.ts
> │   │   │   │   │   ├── rss.xml.ts
> │   │   │   │   │   └── search.astro
> │   │   │   │   ├── schemas
> │   │   │   │   │   ├── blog.ts
> │   │   │   │   │   ├── card.ts
> │   │   │   │   │   ├── doodle.ts
> │   │   │   │   │   └── slide.ts
> │   │   │   │   ├── styles
> │   │   │   │   │   ├── article.css
> │   │   │   │   │   ├── card.css
> │   │   │   │   │   ├── global.css
> │   │   │   │   │   └── scrolling-tags.css
> │   │   │   │   ├── themes
> │   │   │   │   │   ├── knowledge-card-themes.ts
> │   │   │   │   │   └── slide-card-themes.ts
> │   │   │   │   ├── types
> │   │   │   │   │   ├── product.ts
> │   │   │   │   │   └── reveal.js-mermaid-plugin.d.ts
> │   │   │   │   ├── consts.ts
> │   │   │   │   ├── content.config.ts
> │   │   │   │   └── env.ts
> │   │   │   ├── astro.config.mjs
> │   │   │   ├── biome.json
> │   │   │   ├── components.json
> │   │   │   ├── package-lock.json
> │   │   │   ├── pnpm-lock.yaml
> │   │   │   └── tsconfig.json
> │   │   ├── qially-web
> │   │   │   ├── assets
> │   │   │   │   ├── css
> │   │   │   │   │   ├── global_styles.css
> │   │   │   │   │   └── styles.css
> │   │   │   │   ├── files
> │   │   │   │   │   ├── forms
> │   │   │   │   │   ├── balance-sheet-template.xlsx
> │   │   │   │   │   ├── contact.json
> │   │   │   │   │   ├── emailsignature.html
> │   │   │   │   │   ├── income-statement-template.xlsx
> │   │   │   │   │   ├── index.md
> │   │   │   │   │   ├── payroll-calendar-2026.pdf
> │   │   │   │   │   ├── resume.pdf
> │   │   │   │   │   ├── services-full.json
> │   │   │   │   │   └── tax-prep-checklist.pdf
> │   │   │   │   ├── images
> │   │   │   │   │   ├── business_tools
> │   │   │   │   │   ├── allegaracasa.jpg
> │   │   │   │   │   ├── astrotext.png
> │   │   │   │   │   ├── back-master-small.jpg
> │   │   │   │   │   ├── business-performance-wins.png
> │   │   │   │   │   ├── cassie-boca-x-tbVqkfQCU-unsplash.jpg
> │   │   │   │   │   ├── cover.jpg
> │   │   │   │   │   ├── favicon.ico
> │   │   │   │   │   ├── favicon.png
> │   │   │   │   │   ├── favicon.webp
> │   │   │   │   │   ├── jesse-gardner-EqdpXeemf58-unsplash.jpg
> │   │   │   │   │   ├── jf-martin-Ofs3LjEUcrk-unsplash.jpg
> │   │   │   │   │   ├── josh-rose-trYl7JYATH0-unsplash.jpg
> │   │   │   │   │   ├── llegaracasa.jpg
> │   │   │   │   │   ├── logo.png
> │   │   │   │   │   ├── profile-nogb.jpg
> │   │   │   │   │   ├── profile.jpg
> │   │   │   │   │   └── tersius-van-rhyn-xcQWMPm9fG8-unsplash.jpg
> │   │   │   │   ├── js
> │   │   │   │   │   ├── i18n.js
> │   │   │   │   │   └── main.js
> │   │   │   │   ├── templates
> │   │   │   │   │   ├── detail.html
> │   │   │   │   │   ├── flow.html
> │   │   │   │   │   ├── hub.html
> │   │   │   │   │   └── promo.html
> │   │   │   │   ├── vids
> │   │   │   │   │   └── video-logo.mp4
> │   │   │   │   └── cody_rice_velasquez-fullstack.pdf
> │   │   │   ├── chat
> │   │   │   │   ├── index.html
> │   │   │   │   └── sales-iq-landing-page-qr-code.png
> │   │   │   ├── client-portals
> │   │   │   │   ├── dmejiasmartinez
> │   │   │   │   │   ├── docs
> │   │   │   │   │   ├── media
> │   │   │   │   │   ├── index.html
> │   │   │   │   │   └── README.md
> │   │   │   │   ├── letters
> │   │   │   │   │   ├── client.wiletvaldo_calderon-ramirez
> │   │   │   │   │   ├── engagement
> │   │   │   │   │   ├── evansville_inn
> │   │   │   │   │   └── index.html
> │   │   │   │   └── index.html
> │   │   │   ├── components
> │   │   │   │   ├── footer.html
> │   │   │   │   └── header.html
> │   │   │   ├── contact
> │   │   │   │   └── index.html
> │   │   │   ├── data
> │   │   │   │   ├── _redirects
> │   │   │   │   └── site_map.json
> │   │   │   ├── faq
> │   │   │   │   └── index.html
> │   │   │   ├── functions
> │   │   │   │   ├── [[path]].js
> │   │   │   │   └── index.html
> │   │   │   ├── modules
> │   │   │   │   ├── cody
> │   │   │   │   │   ├── ecard
> │   │   │   │   │   ├── helpcody
> │   │   │   │   │   ├── portfolio
> │   │   │   │   │   └── index.html
> │   │   │   │   ├── flows
> │   │   │   │   │   ├── estate-planning
> │   │   │   │   │   ├── index.html
> │   │   │   │   │   ├── privacy.html
> │   │   │   │   │   ├── README.md
> │   │   │   │   │   └── terms.html
> │   │   │   │   ├── legal
> │   │   │   │   │   ├── accessibility
> │   │   │   │   │   ├── compliance
> │   │   │   │   │   └── index.html
> │   │   │   │   ├── promo
> │   │   │   │   │   ├── cashapp_bonus
> │   │   │   │   │   ├── quickbooks
> │   │   │   │   │   ├── zoho
> │   │   │   │   │   └── index.html
> │   │   │   │   ├── referral
> │   │   │   │   │   └── index.html
> │   │   │   │   ├── review
> │   │   │   │   │   ├── index.html
> │   │   │   │   │   └── qrcode_www.google.com.png
> │   │   │   │   ├── tools
> │   │   │   │   │   ├── budgets
> │   │   │   │   │   ├── business-readiness-check
> │   │   │   │   │   ├── expense-tracker
> │   │   │   │   │   ├── receipt-organizer
> │   │   │   │   │   ├── tax-checklist
> │   │   │   │   │   └── index.html
> │   │   │   │   └── index.html
> │   │   │   ├── privacy
> │   │   │   │   └── index.html
> │   │   │   ├── public
> │   │   │   │   ├── favicon.ico
> │   │   │   │   └── favicon.svg
> │   │   │   ├── resources
> │   │   │   │   ├── compliance
> │   │   │   │   │   ├── data-inventory
> │   │   │   │   │   ├── incident-response
> │   │   │   │   │   ├── provider-agreements
> │   │   │   │   │   ├── risk-assessment
> │   │   │   │   │   ├── training-logs
> │   │   │   │   │   ├── wisp
> │   │   │   │   │   └── index.html
> │   │   │   │   ├── kb
> │   │   │   │   │   ├── accounting-cleanup
> │   │   │   │   │   ├── getting-started
> │   │   │   │   │   ├── irs-notices
> │   │   │   │   │   ├── tax-resolution
> │   │   │   │   │   └── index.html
> │   │   │   │   ├── msa
> │   │   │   │   │   └── index.html
> │   │   │   │   └── index.html
> │   │   │   ├── services
> │   │   │   │   ├── books
> │   │   │   │   │   ├── bookkeeping
> │   │   │   │   │   ├── year-end-process
> │   │   │   │   │   └── index.html
> │   │   │   │   ├── compliance
> │   │   │   │   │   ├── business-formation
> │   │   │   │   │   └── index.html
> │   │   │   │   ├── flows
> │   │   │   │   │   ├── immigration-forms
> │   │   │   │   │   ├── translations
> │   │   │   │   │   └── index.html
> │   │   │   │   ├── hr-ops
> │   │   │   │   │   └── index.html
> │   │   │   │   ├── it-ai
> │   │   │   │   │   ├── automation-ai
> │   │   │   │   │   └── index.html
> │   │   │   │   ├── marketing
> │   │   │   │   │   └── index.html
> │   │   │   │   ├── qisuite
> │   │   │   │   │   └── index.html
> │   │   │   │   ├── tax
> │   │   │   │   │   ├── prep
> │   │   │   │   │   └── index.html
> │   │   │   │   └── index.html
> │   │   │   ├── showcases
> │   │   │   │   ├── 20000-swing
> │   │   │   │   │   └── index.html
> │   │   │   │   ├── index.html
> │   │   │   │   └── videos.html
> │   │   │   ├── terms
> │   │   │   │   └── index.html
> │   │   │   ├── 404.html
> │   │   │   ├── build_nav.py
> │   │   │   ├── check_links.py
> │   │   │   ├── humans.txt
> │   │   │   ├── index.html
> │   │   │   ├── LICENSE
> │   │   │   ├── make_stubs.py
> │   │   │   ├── manifest.webmanifest
> │   │   │   ├── prepublish.py
> │   │   │   ├── README.md
> │   │   │   ├── robots.txt
> │   │   │   └── sitemap.xml
> │   │   ├── qione
> │   │   │   ├── app
> │   │   │   │   ├── (app)
> │   │   │   │   │   ├── admin
> │   │   │   │   │   ├── ai
> │   │   │   │   │   ├── care
> │   │   │   │   │   ├── chronicle
> │   │   │   │   │   ├── contracts
> │   │   │   │   │   ├── dashboard
> │   │   │   │   │   ├── documents
> │   │   │   │   │   ├── forms
> │   │   │   │   │   ├── notes
> │   │   │   │   │   ├── objects
> │   │   │   │   │   ├── settings
> │   │   │   │   │   ├── tax
> │   │   │   │   │   ├── _page.tsx
> │   │   │   │   │   └── layout.tsx
> │   │   │   │   ├── (portal)
> │   │   │   │   │   ├── objects
> │   │   │   │   │   ├── qichronicle
> │   │   │   │   │   ├── layout.tsx
> │   │   │   │   │   └── page.tsx
> │   │   │   │   ├── (public)
> │   │   │   │   │   ├── invite
> │   │   │   │   │   ├── login
> │   │   │   │   │   └── reset-password
> │   │   │   │   ├── api
> │   │   │   │   │   ├── admin
> │   │   │   │   │   ├── ai
> │   │   │   │   │   ├── archive
> │   │   │   │   │   ├── care
> │   │   │   │   │   ├── chat
> │   │   │   │   │   ├── chronicle
> │   │   │   │   │   ├── contracts
> │   │   │   │   │   ├── documents
> │   │   │   │   │   ├── forms
> │   │   │   │   │   ├── notes
> │   │   │   │   │   ├── objects
> │   │   │   │   │   ├── qichronicle
> │   │   │   │   │   ├── tax
> │   │   │   │   │   ├── users
> │   │   │   │   │   └── webhooks
> │   │   │   │   ├── auth
> │   │   │   │   │   └── callback
> │   │   │   │   └── layout.tsx
> │   │   │   ├── dist
> │   │   │   │   ├── assets
> │   │   │   │   │   ├── index-2c5Wfwmx.js
> │   │   │   │   │   └── index-CwEFQk_m.css
> │   │   │   │   ├── icons
> │   │   │   │   ├── images
> │   │   │   │   ├── _routes.json
> │   │   │   │   ├── favicon.ico
> │   │   │   │   └── index.html
> │   │   │   ├── public
> │   │   │   │   ├── icons
> │   │   │   │   ├── images
> │   │   │   │   ├── _routes.json
> │   │   │   │   └── favicon.ico
> │   │   │   ├── src
> │   │   │   │   ├── api
> │   │   │   │   │   └── client.ts
> │   │   │   │   ├── components
> │   │   │   │   │   ├── ui
> │   │   │   │   │   ├── AuthUI.tsx
> │   │   │   │   │   ├── GinaChat.tsx
> │   │   │   │   │   └── Launcher.tsx
> │   │   │   │   ├── features
> │   │   │   │   │   ├── admin
> │   │   │   │   │   ├── bookings
> │   │   │   │   │   ├── qiarchive
> │   │   │   │   │   ├── qiblogs
> │   │   │   │   │   ├── qicare
> │   │   │   │   │   ├── qicases
> │   │   │   │   │   ├── qichronicle
> │   │   │   │   │   ├── qicockpit
> │   │   │   │   │   ├── qicontacts
> │   │   │   │   │   ├── qidiary
> │   │   │   │   │   ├── qidocs
> │   │   │   │   │   ├── qiforms
> │   │   │   │   │   ├── qihome-hub
> │   │   │   │   │   ├── qihtmldocs
> │   │   │   │   │   ├── qina
> │   │   │   │   │   ├── qinotes
> │   │   │   │   │   ├── qisetting
> │   │   │   │   │   └── qitax
> │   │   │   │   ├── hooks
> │   │   │   │   │   └── useGina.ts
> │   │   │   │   ├── layouts
> │   │   │   │   │   └── PortalLayout.tsx
> │   │   │   │   ├── lib
> │   │   │   │   │   ├── ai
> │   │   │   │   │   ├── auth
> │   │   │   │   │   ├── db
> │   │   │   │   │   ├── integrations
> │   │   │   │   │   ├── permissions
> │   │   │   │   │   ├── storage
> │   │   │   │   │   ├── supabase
> │   │   │   │   │   ├── utils
> │   │   │   │   │   ├── constants.ts
> │   │   │   │   │   ├── env.ts
> │   │   │   │   │   ├── tools.ts
> │   │   │   │   │   └── utils.ts
> │   │   │   │   ├── pages
> │   │   │   │   │   └── Dashboard.tsx
> │   │   │   │   ├── qione
> │   │   │   │   │   ├── contracts
> │   │   │   │   │   ├── csv
> │   │   │   │   │   └── objects
> │   │   │   │   ├── rag-chatbot
> │   │   │   │   │   ├── app
> │   │   │   │   │   ├── README.md
> │   │   │   │   │   └── requirements.txt
> │   │   │   │   ├── styles
> │   │   │   │   │   └── globals.css
> │   │   │   │   ├── types
> │   │   │   │   │   ├── auth.ts
> │   │   │   │   │   ├── common.ts
> │   │   │   │   │   ├── database.ts
> │   │   │   │   │   └── permissions.ts
> │   │   │   │   ├── ui
> │   │   │   │   │   ├── components
> │   │   │   │   │   └── styles
> │   │   │   │   ├── App.tsx
> │   │   │   │   ├── main.tsx
> │   │   │   │   ├── middleware.ts
> │   │   │   │   └── vite-env.d.ts
> │   │   │   ├── components.json
> │   │   │   ├── index.html
> │   │   │   ├── package.json
> │   │   │   ├── pnpm-lock.yaml
> │   │   │   ├── postcss.config.js
> │   │   │   ├── qione_review_bundle.txt
> │   │   │   ├── README.md
> │   │   │   ├── tailwind.config.ts
> │   │   │   ├── tsconfig.json
> │   │   │   ├── tsconfig.node.json
> │   │   │   ├── tsconfig.tsbuildinfo
> │   │   │   ├── vite.config.ts
> │   │   │   └── wrangler.toml
> │   │   ├── qsaysit-blog
> │   │   └── qsaysit-web
> │   │       ├── assets
> │   │       │   ├── css
> │   │       │   │   └── styles.css
> │   │       │   ├── icons
> │   │       │   ├── img
> │   │       │   │   ├── og
> │   │       │   │   ├── posts
> │   │       │   │   └── series
> │   │       │   └── js
> │   │       │       ├── search.js
> │   │       │       └── site.js
> │   │       ├── content
> │   │       │   ├── data
> │   │       │   │   ├── featured.yaml
> │   │       │   │   ├── nav.yaml
> │   │       │   │   └── site.yaml
> │   │       │   ├── pages
> │   │       │   │   ├── about.md
> │   │       │   │   └── contact.md
> │   │       │   ├── posts
> │   │       │   │   └── 2026-03-24_first_post.md
> │   │       │   └── series
> │   │       │       ├── mirror-series.md
> │   │       │       ├── notebooklm-deep-dives.md
> │   │       │       └── the-onion-effect.md
> │   │       ├── public
> │   │       │   ├── favicon.ico
> │   │       │   ├── robots.txt
> │   │       │   └── social-preview.png
> │   │       ├── site
> │   │       │   ├── about
> │   │       │   │   └── index.html
> │   │       │   ├── assets
> │   │       │   │   ├── css
> │   │       │   │   ├── icons
> │   │       │   │   ├── img
> │   │       │   │   └── js
> │   │       │   ├── contact
> │   │       │   │   └── index.html
> │   │       │   ├── posts
> │   │       │   │   └── first-post
> │   │       │   ├── series
> │   │       │   │   ├── mirror-series
> │   │       │   │   ├── notebooklm-deep-dives
> │   │       │   │   ├── the-onion-effect
> │   │       │   │   └── index.html
> │   │       │   ├── favicon.ico
> │   │       │   ├── index.html
> │   │       │   ├── robots.txt
> │   │       │   └── social-preview.png
> │   │       ├── templates
> │   │       │   ├── components
> │   │       │   │   ├── footer.html
> │   │       │   │   ├── header.html
> │   │       │   │   ├── infographic-block.html
> │   │       │   │   ├── notebooklm-block.html
> │   │       │   │   ├── post-card.html
> │   │       │   │   └── youtube-embed.html
> │   │       │   ├── archive.html
> │   │       │   ├── base.html
> │   │       │   ├── index.html
> │   │       │   ├── page.html
> │   │       │   ├── post.html
> │   │       │   └── series.html
> │   │       ├── build.py
> │   │       ├── README.md
> │   │       └── requirements.txt
> │   ├── docs
> │   │   ├── architecture
> │   │   │   ├── atomic_entities.csv
> │   │   │   ├── atomic_entity_fields.csv
> │   │   │   └── target-architecture.csv
> │   │   ├── governance
> │   │   │   ├── active_mission.yaml
> │   │   │   ├── dns_map.yml
> │   │   │   ├── income_streams.yaml
> │   │   │   ├── life_goals.yaml
> │   │   │   └── system_constraints.yaml
> │   │   ├── QIO0001_00_QiOS_MASTER
> │   │   │   ├── QIO0001_01_genesis_and_constitution
> │   │   │   │   └── QIO0001_010_system
> │   │   │   │       ├── QIO0001_011_adr
> │   │   │   │       └── QIO0001_014_tables
> │   │   │   ├── QIO0001_02_ontology_and_structure
> │   │   │   │   ├── dev
> │   │   │   │   │   ├── dns_map.yml
> │   │   │   │   │   ├── qi_cloud_hybrid_dev_docs_3_d_directory_map.md
> │   │   │   │   │   └── QiSuite_Dev_Bible.md
> │   │   │   │   ├── Git
> │   │   │   │   │   └── GIT_LFS_SETUP.md
> │   │   │   │   ├── QiChronicle
> │   │   │   │   │   ├── 01_local_supabase_setup.md
> │   │   │   │   │   ├── 02_critical_gotchas.md
> │   │   │   │   │   ├── 03_patch_api_implementation.md
> │   │   │   │   │   ├── 04_collection_api_implementation.md
> │   │   │   │   │   ├── 05_frontend_integration.md
> │   │   │   │   │   ├── 06_sidebar_navigation.md
> │   │   │   │   │   ├── 07_database_schema.md
> │   │   │   │   │   └── 08_email_architecture.md
> │   │   │   │   ├── Qinote
> │   │   │   │   │   └── Quonote System Deep Dive and Reflection.md
> │   │   │   │   ├── Snippets
> │   │   │   │   │   ├── Context window construction.ts
> │   │   │   │   │   └── hybrid_rag.ts
> │   │   │   │   ├── Standards
> │   │   │   │   │   ├── pdf_standards.md
> │   │   │   │   │   ├── repo_rules.md
> │   │   │   │   │   └── RLS_POLICIES.md
> │   │   │   │   ├── Workspace
> │   │   │   │   │   └── REPO_INDEX_2026-03-19.md
> │   │   │   │   ├── ARCHITECTURE.md
> │   │   │   │   └── gina_chat_contract.ts
> │   │   │   ├── QIO0001_03_identity_and_naming
> │   │   │   │   └── content_identity.md
> │   │   │   ├── QIO0001_04_spine_and_runtime
> │   │   │   ├── QIO0001_05_flows_and_pipelines.md
> │   │   │   │   ├── noco-apis-doc
> │   │   │   │   │   ├── data-apis-v1
> │   │   │   │   │   ├── data-apis-v2
> │   │   │   │   │   ├── data-apis-v3
> │   │   │   │   │   ├── meta-apis-v1
> │   │   │   │   │   ├── meta-apis-v2
> │   │   │   │   │   ├── meta-apis-v3
> │   │   │   │   │   └── README.md
> │   │   │   │   ├── inbox_ingestion_pipeline.md
> │   │   │   │   └── INTEGRATION_LAYER_SUMMARY.md
> │   │   │   ├── QIO0001_06_build_surfaces
> │   │   │   ├── QIO0001_07_governance_and_working_memory
> │   │   │   │   ├── active_mission.yaml
> │   │   │   │   ├── dns_map.yml
> │   │   │   │   ├── income_streams.yaml
> │   │   │   │   ├── life_goals.yaml
> │   │   │   │   ├── repo_rules.md
> │   │   │   │   └── system_constraints.yaml
> │   │   │   ├── QIO0001_99_gina
> │   │   │   │   ├── GINA_MEMORY_MERGE_COMPLETE.md
> │   │   │   │   ├── gina_personality_prompt.md
> │   │   │   │   ├── GINA_V2_MERGE_ANALYSIS.md
> │   │   │   │   ├── GINA.md
> │   │   │   │   └── My personal AI Agent Template.md
> │   │   │   └── QIO00001_00_QiOS_MASTER_README.MD
> │   │   ├── references
> │   │   │   ├── pdf_standards.md
> │   │   │   └── repo_rules.md
> │   │   ├── system
> │   │   │   ├── adr
> │   │   │   │   ├── 2026-03-16_secrets_management_standard.md
> │   │   │   │   ├── ADR-0007-qione-architecture-lock.md
> │   │   │   │   ├── Canonical repo tree.md
> │   │   │   │   ├── content_identity.md
> │   │   │   │   └── inbox_ingestion_pipeline.md
> │   │   │   ├── schema
> │   │   │   │   └── life_dashboard.schema.json
> │   │   │   ├── sql
> │   │   │   │   └── schema.sql
> │   │   │   ├── tables
> │   │   │   │   ├── architecture_flow.tsv
> │   │   │   │   ├── decisions_log.tsv
> │   │   │   │   ├── non-negotiable-rules.csv
> │   │   │   │   ├── tool_decisions.csv
> │   │   │   │   └── tools_inventory.tsv
> │   │   │   └── gina_chat_contract.ts
> │   │   ├── todo
> │   │   │   └── 0001.md
> │   │   ├── _QiOS_Master_Document.jpg
> │   │   └── gina_personality_prompt.md
> │   ├── packages
> │   │   ├── ai
> │   │   │   ├── src
> │   │   │   │   ├── adapters
> │   │   │   │   ├── prompts
> │   │   │   │   ├── tools
> │   │   │   │   └── index.ts
> │   │   │   ├── package.json
> │   │   │   └── README.md
> │   │   ├── assets
> │   │   │   ├── public
> │   │   │   │   └── introvideo.mp4
> │   │   │   ├── src
> │   │   │   │   ├── bookings
> │   │   │   │   │   ├── book-now.js
> │   │   │   │   │   └── booking-inline.js
> │   │   │   │   ├── brand
> │   │   │   │   ├── icons
> │   │   │   │   │   └── home-40.svg
> │   │   │   │   └── index.ts
> │   │   │   ├── introvideo.mp4
> │   │   │   └── package.json
> │   │   ├── auth
> │   │   │   ├── src
> │   │   │   │   └── index.ts
> │   │   │   └── package.json
> │   │   ├── config
> │   │   │   ├── src
> │   │   │   │   ├── json
> │   │   │   │   │   ├── eos_frontmatter.schema.json
> │   │   │   │   │   ├── eos-frontmatter-mapping.json
> │   │   │   │   │   ├── frontmatter.schema.json
> │   │   │   │   │   ├── git_manifest.json
> │   │   │   │   │   ├── mapping.json
> │   │   │   │   │   ├── QiRealms_seed.json
> │   │   │   │   │   ├── QiTagClasses_schema.json
> │   │   │   │   │   ├── QiTags_seed.json
> │   │   │   │   │   ├── repo_naming_policy.json
> │   │   │   │   │   └── systemInfoCMD.json
> │   │   │   │   ├── rules
> │   │   │   │   │   ├── audit_repo_rules.ts
> │   │   │   │   │   ├── fix_repo_rules.ts
> │   │   │   │   │   ├── repoRules.ts
> │   │   │   │   │   └── rulesRegistry.ts
> │   │   │   │   ├── yaml
> │   │   │   │   │   ├── csv_to_md_mappings.yaml
> │   │   │   │   │   ├── fs_scan_config.yaml
> │   │   │   │   │   ├── housekeeping.yaml
> │   │   │   │   │   ├── qi_codex.config.yaml
> │   │   │   │   │   ├── qi_prefix_map.yaml
> │   │   │   │   │   ├── qicompiler_config.yaml
> │   │   │   │   │   ├── qione_rag_routes.yaml
> │   │   │   │   │   ├── slugs_mapping.yaml
> │   │   │   │   │   └── tree_compiler_config.yaml
> │   │   │   │   └── index.ts
> │   │   │   └── package.json
> │   │   ├── database
> │   │   │   ├── src
> │   │   │   │   ├── adapters
> │   │   │   │   │   ├── auth
> │   │   │   │   │   └── supabase
> │   │   │   │   ├── migrations
> │   │   │   │   │   ├── 0001_qione_core.sql
> │   │   │   │   │   ├── 0002_qiarchive_spine.sql
> │   │   │   │   │   ├── 0003_qisys_ops.sql
> │   │   │   │   │   ├── 0004_qigraph_index.sql
> │   │   │   │   │   ├── 0005_qiknowledge.sql
> │   │   │   │   │   ├── 0006_qially_comms.sql
> │   │   │   │   │   ├── 0007_qichronicle_time.sql
> │   │   │   │   │   ├── 0008_qihome_ledger.sql
> │   │   │   │   │   ├── 0009_qitax_returns.sql
> │   │   │   │   │   ├── 0010_qicase_matters.sql
> │   │   │   │   │   ├── 0011_qicrm_contacts.sql
> │   │   │   │   │   ├── 0012_qivault_docs.sql
> │   │   │   │   │   └── 0013_qicms_web.sql
> │   │   │   │   ├── queries
> │   │   │   │   ├── schemas
> │   │   │   │   │   ├── src
> │   │   │   │   │   ├── archive.ts
> │   │   │   │   │   ├── case.ts
> │   │   │   │   │   ├── client.ts
> │   │   │   │   │   ├── comms.ts
> │   │   │   │   │   ├── content.ts
> │   │   │   │   │   ├── core.ts
> │   │   │   │   │   ├── home.ts
> │   │   │   │   │   ├── system.ts
> │   │   │   │   │   ├── tax.ts
> │   │   │   │   │   └── vault.ts
> │   │   │   │   ├── types
> │   │   │   │   └── index.ts
> │   │   │   ├── utils
> │   │   │   │   └── supabase.ts
> │   │   │   ├── package.json
> │   │   │   ├── README.md
> │   │   │   └── scanner.js
> │   │   ├── email
> │   │   │   ├── partials
> │   │   │   │   ├── footer.html
> │   │   │   │   └── header.html
> │   │   │   ├── smtp
> │   │   │   │   └── config.yml
> │   │   │   ├── supabase-auth
> │   │   │   │   ├── change_email.html
> │   │   │   │   ├── confirmation.html
> │   │   │   │   ├── invite.html
> │   │   │   │   ├── magic_link.html
> │   │   │   │   ├── otp.html
> │   │   │   │   ├── README.md
> │   │   │   │   ├── reauthentication.html
> │   │   │   │   └── recovery.html
> │   │   │   ├── templates
> │   │   │   │   ├── billing
> │   │   │   │   │   └── invoice.html
> │   │   │   │   ├── general
> │   │   │   │   │   └── welcome.html
> │   │   │   │   ├── projects
> │   │   │   │   │   └── update.html
> │   │   │   │   └── tax
> │   │   │   │       └── return-accepted.html
> │   │   │   └── render.ts
> │   │   ├── qinode
> │   │   │   ├── src
> │   │   │   │   ├── dna
> │   │   │   │   ├── lineage
> │   │   │   │   ├── obsidian-engine
> │   │   │   │   ├── parser
> │   │   │   │   ├── reconstruction
> │   │   │   │   ├── registry
> │   │   │   │   ├── serializer
> │   │   │   │   └── index.ts
> │   │   │   ├── package.json
> │   │   │   └── README.md
> │   │   ├── sdk
> │   │   ├── ui
> │   │   │   ├── src
> │   │   │   │   ├── components
> │   │   │   │   ├── tokens
> │   │   │   │   │   └── assets
> │   │   │   │   └── index.ts
> │   │   │   ├── package.json
> │   │   │   └── README.md
> │   │   └── utils
> │   │       ├── src
> │   │       │   └── index.ts
> │   │       └── package.json
> │   ├── python
> │   │   ├── qiarchive
> │   │   │   ├── api
> │   │   │   │   └── main.py
> │   │   │   ├── extract
> │   │   │   ├── manifests
> │   │   │   ├── ocr
> │   │   │   ├── rename
> │   │   │   ├── repair
> │   │   │   │   └── repair.py
> │   │   │   └── scan
> │   │   │       └── scan.py
> │   │   └── requirements.txt
> │   ├── python_core
> │   │   ├── build
> │   │   │   └── QiOne_Tools
> │   │   │       ├── localpycs
> │   │   │       │   ├── pyimod01_archive.pyc
> │   │   │       │   ├── pyimod02_importers.pyc
> │   │   │       │   ├── pyimod03_ctypes.pyc
> │   │   │       │   ├── pyimod04_pywin32.pyc
> │   │   │       │   └── struct.pyc
> │   │   │       ├── Analysis-00.toc
> │   │   │       ├── base_library.zip
> │   │   │       ├── EXE-00.toc
> │   │   │       ├── PKG-00.toc
> │   │   │       ├── PYZ-00.pyz
> │   │   │       ├── PYZ-00.toc
> │   │   │       ├── QiOne_Tools.pkg
> │   │   │       ├── warn-QiOne_Tools.txt
> │   │   │       └── xref-QiOne_Tools.html
> │   │   ├── core
> │   │   │   └── base_tool.py
> │   │   ├── dist
> │   │   │   └── QiOne_Tools.exe
> │   │   ├── notion_pipeline
> │   │   │   ├── notion
> │   │   │   │   ├── helpers
> │   │   │   │   │   ├── __init__.py
> │   │   │   │   │   ├── client.py
> │   │   │   │   │   └── database.py
> │   │   │   │   ├── __init__.py
> │   │   │   │   ├── README.md
> │   │   │   │   └── settings.py
> │   │   │   ├── notion_pipeline.py
> │   │   │   └── requirements.txt
> │   │   ├── tools
> │   │   │   ├── __pycache__
> │   │   │   │   └── __init__.cpython-314.pyc
> │   │   │   ├── __init__.py
> │   │   │   ├── archive_router.py
> │   │   │   ├── blank_template.py
> │   │   │   ├── bloat_destroyer.py
> │   │   │   ├── bulk_pdf_splitter.py
> │   │   │   ├── dev_extractor.py
> │   │   │   ├── dev_git_push_tool.py
> │   │   │   ├── dev_git_push.py
> │   │   │   ├── dev_rule_tester.py
> │   │   │   ├── doc_pdf_splitter.py
> │   │   │   ├── doc_tax_compiler.py
> │   │   │   ├── downloads_inspector.py
> │   │   │   ├── filename_cleaner.py
> │   │   │   ├── git_push_tool.py
> │   │   │   ├── media_video_converter.py
> │   │   │   ├── push.py
> │   │   │   ├── router_archivist.py
> │   │   │   ├── router_downloads.py
> │   │   │   ├── router_vault.py
> │   │   │   ├── rule_tester.py
> │   │   │   ├── sys_bloat_destroyer.py
> │   │   │   ├── sys_file_cleaner.py
> │   │   │   ├── text_extractor_tool.py
> │   │   │   ├── unlock_downloads.py
> │   │   │   ├── vault_router.py
> │   │   │   └── z_template.py
> │   │   ├── build.bat
> │   │   ├── builder.py
> │   │   ├── file_version_info.txt
> │   │   ├── main_ui.py
> │   │   ├── QiOne_Tools.spec
> │   │   └── requirements.txt
> │   ├── python_local
> │   │   ├── agents
> │   │   ├── api
> │   │   │   ├── main.py
> │   │   │   ├── routes_health.py
> │   │   │   ├── routes_ingest.py
> │   │   │   ├── routes_jobs.py
> │   │   │   └── routes_search.py
> │   │   ├── audio
> │   │   │   ├── bin
> │   │   │   │   └── index.html
> │   │   │   ├── book_projects
> │   │   │   │   ├── paid_in_full
> │   │   │   │   │   ├── audio_final
> │   │   │   │   │   ├── audio_raw
> │   │   │   │   │   ├── licenses
> │   │   │   │   │   ├── logs
> │   │   │   │   │   ├── music_sfx
> │   │   │   │   │   ├── text
> │   │   │   │   │   └── index.html
> │   │   │   │   └── index.html
> │   │   │   ├── index.html
> │   │   │   ├── README.md
> │   │   │   ├── render.py
> │   │   │   ├── setup_piper.ps1
> │   │   │   ├── split_chapters.py
> │   │   │   └── voice_map.json
> │   │   ├── config
> │   │   │   ├── prefixes.yaml
> │   │   │   └── settings.yaml
> │   │   ├── document-ingestion
> │   │   │   ├── app.py
> │   │   │   ├── README.md
> │   │   │   └── requirements.txt
> │   │   ├── document-processors
> │   │   │   ├── pipeline
> │   │   │   │   ├── __init__.py
> │   │   │   │   ├── index.html
> │   │   │   │   ├── layout_detector.py
> │   │   │   │   ├── model_downloader.py
> │   │   │   │   ├── nanonets_processor.py
> │   │   │   │   ├── neural_document_processor.py
> │   │   │   │   └── ocr_service.py
> │   │   │   ├── processors
> │   │   │   │   ├── __init__.py
> │   │   │   │   ├── base.py
> │   │   │   │   ├── cloud_processor.py
> │   │   │   │   ├── docx_processor.py
> │   │   │   │   ├── excel_processor.py
> │   │   │   │   ├── gpu_processor.py
> │   │   │   │   ├── html_processor.py
> │   │   │   │   ├── image_processor.py
> │   │   │   │   ├── index.html
> │   │   │   │   ├── pdf_processor.py
> │   │   │   │   ├── pptx_processor.py
> │   │   │   │   ├── txt_processor.py
> │   │   │   │   └── url_processor.py
> │   │   │   ├── services
> │   │   │   │   ├── __init__.py
> │   │   │   │   ├── auth_service.py
> │   │   │   │   ├── index.html
> │   │   │   │   └── ollama_service.py
> │   │   │   ├── static
> │   │   │   │   ├── index.html
> │   │   │   │   ├── logo_clean.png
> │   │   │   │   ├── script.js
> │   │   │   │   └── styles.css
> │   │   │   ├── templates
> │   │   │   │   └── index.html
> │   │   │   ├── utils
> │   │   │   │   ├── __init__.py
> │   │   │   │   ├── gpu_utils.py
> │   │   │   │   └── index.html
> │   │   │   ├── __init__.py
> │   │   │   ├── cli.py
> │   │   │   ├── config.py
> │   │   │   ├── exceptions.py
> │   │   │   ├── extractor.py
> │   │   │   ├── index.html
> │   │   │   ├── result.py
> │   │   │   ├── web_app.py
> │   │   │   └── WEB_INTERFACE.md
> │   │   ├── file_pipeline
> │   │   │   ├── tests
> │   │   │   ├── __init__.py
> │   │   │   ├── api_client.py
> │   │   │   ├── archive.py
> │   │   │   ├── chunk.py
> │   │   │   ├── classify.py
> │   │   │   ├── config.py
> │   │   │   ├── embed.py
> │   │   │   ├── extract.py
> │   │   │   ├── graph_project.py
> │   │   │   ├── ingest.py
> │   │   │   ├── models.py
> │   │   │   ├── route.py
> │   │   │   ├── state_machine.py
> │   │   │   └── watcher.py
> │   │   ├── gina-ai
> │   │   │   ├── index.html
> │   │   │   ├── main.py
> │   │   │   └── requirements.txt
> │   │   ├── jobs
> │   │   │   └── runner.py
> │   │   ├── local_services
> │   │   │   ├── crawler
> │   │   │   │   ├── __init__.py
> │   │   │   │   └── vault_crawler.py
> │   │   │   ├── integrations
> │   │   │   │   ├── __init__.py
> │   │   │   │   ├── base.py
> │   │   │   │   ├── INTEGRATION_LAYER_SUMMARY.md
> │   │   │   │   └── README.md
> │   │   │   ├── scripts
> │   │   │   │   ├── api_dev_history.py
> │   │   │   │   ├── api_gina.py
> │   │   │   │   ├── api_ingest.py
> │   │   │   │   ├── api_query.py
> │   │   │   │   ├── check_status.py
> │   │   │   │   ├── check_workers.py
> │   │   │   │   ├── check-auth.ps1
> │   │   │   │   ├── check-secrets.ps1
> │   │   │   │   ├── db.py
> │   │   │   │   ├── deploy-all.ps1
> │   │   │   │   ├── deploy-critical.ps1
> │   │   │   │   ├── dev_error_helpers.py
> │   │   │   │   ├── frontmatter_utils.py
> │   │   │   │   ├── fs_scanner.py
> │   │   │   │   ├── gina_prompt.py
> │   │   │   │   ├── job_processor.py
> │   │   │   │   ├── jobs.py
> │   │   │   │   ├── memory.py
> │   │   │   │   ├── models.py
> │   │   │   │   ├── qios_local_core.py
> │   │   │   │   ├── rag.py
> │   │   │   │   ├── README.md
> │   │   │   │   ├── set-critical-secrets.ps1
> │   │   │   │   ├── set-secrets-from-env.ps1
> │   │   │   │   ├── start_worker.ps1
> │   │   │   │   ├── sync-secrets.ps1
> │   │   │   │   ├── test_debug_ingest.ps1
> │   │   │   │   ├── test_ingest.py
> │   │   │   │   ├── test_queue_admin.ps1
> │   │   │   │   ├── test-rag-system.ps1
> │   │   │   │   ├── test-with-curl.ps1
> │   │   │   │   ├── text_extractor.py
> │   │   │   │   ├── tools.py
> │   │   │   │   ├── verify-and-test.ps1
> │   │   │   │   └── worker.py
> │   │   │   ├── tests
> │   │   │   │   ├── README.md
> │   │   │   │   ├── run_tests.sh
> │   │   │   │   ├── test_db_sanity.sql
> │   │   │   │   ├── test_manual_failures.md
> │   │   │   │   └── test_sanity_checks.py
> │   │   │   ├── tools
> │   │   │   │   ├── append_to_vault_note.py
> │   │   │   │   ├── calendar_create_event.py
> │   │   │   │   ├── calendar_get_upcoming.py
> │   │   │   │   ├── check_worker_status.py
> │   │   │   │   ├── create_vault_note.py
> │   │   │   │   ├── crm_create_contact.py
> │   │   │   │   ├── crm_create_task.py
> │   │   │   │   ├── crm_list_recent_contacts.py
> │   │   │   │   ├── crm_search_person.py
> │   │   │   │   ├── list_realm_files.py
> │   │   │   │   ├── mail_get_recent.py
> │   │   │   │   ├── mail_send.py
> │   │   │   │   ├── run_agent_command.py
> │   │   │   │   ├── search_processed_documents.py
> │   │   │   │   ├── sms_send.py
> │   │   │   │   ├── start_agent_service.py
> │   │   │   │   ├── start_worker.py
> │   │   │   │   ├── web_get.py
> │   │   │   │   └── web_search.py
> │   │   │   ├── api_dev_history.py
> │   │   │   ├── api_gina.py
> │   │   │   ├── api_ingest.py
> │   │   │   ├── api_query.py
> │   │   │   ├── check_status.py
> │   │   │   ├── check_workers.py
> │   │   │   ├── db.py
> │   │   │   ├── dev_error_helpers.py
> │   │   │   ├── frontmatter_utils.py
> │   │   │   ├── fs_scan_config.yaml
> │   │   │   ├── fs_scanner.py
> │   │   │   ├── gina_chat_contract.md
> │   │   │   ├── gina_chat_contract.ts
> │   │   │   ├── gina_personality_prompt.md
> │   │   │   ├── gina_prompt.py
> │   │   │   ├── job_processor.py
> │   │   │   ├── jobs.py
> │   │   │   ├── memory.py
> │   │   │   ├── models.py
> │   │   │   ├── qios_local_core.py
> │   │   │   ├── QUICK_START.md
> │   │   │   ├── quick_start.ps1
> │   │   │   ├── rag.py
> │   │   │   ├── README_WORKER.md
> │   │   │   ├── README.md
> │   │   │   ├── requirements.txt
> │   │   │   ├── SETUP.md
> │   │   │   ├── start_worker.ps1
> │   │   │   ├── test_debug_ingest.ps1
> │   │   │   ├── test_ingest.py
> │   │   │   ├── test_queue_admin.ps1
> │   │   │   ├── TESTING_ROADMAP.md
> │   │   │   ├── text_extractor.py
> │   │   │   ├── tools_manifest.yaml
> │   │   │   ├── tools.py
> │   │   │   └── worker.py
> │   │   ├── services
> │   │   │   ├── fs_service.py
> │   │   │   ├── ocr_service.py
> │   │   │   └── ollama_client.py
> │   │   └── requirements.txt
> │   ├── qione-portal
> │   │   ├── dist
> │   │   │   ├── assets
> │   │   │   │   ├── index-CpNpP50y.css
> │   │   │   │   └── index-D1TDhRFo.js
> │   │   │   └── index.html
> │   │   ├── public
> │   │   ├── src
> │   │   │   ├── assets
> │   │   │   │   └── index.css
> │   │   │   ├── components
> │   │   │   │   ├── layout
> │   │   │   │   │   └── Sidebar.tsx
> │   │   │   │   └── ui
> │   │   │   ├── config
> │   │   │   ├── features
> │   │   │   │   ├── admin
> │   │   │   │   ├── cases
> │   │   │   │   │   └── CaseManager.tsx
> │   │   │   │   ├── documents
> │   │   │   │   └── tenants
> │   │   │   ├── hooks
> │   │   │   ├── lib
> │   │   │   │   └── supabase.ts
> │   │   │   ├── pages
> │   │   │   │   ├── admin
> │   │   │   │   │   ├── CaseManager.tsx
> │   │   │   │   │   ├── Dashboard.tsx
> │   │   │   │   │   └── TenantManager.tsx
> │   │   │   │   ├── auth
> │   │   │   │   └── errors
> │   │   │   ├── router
> │   │   │   │   └── index.tsx
> │   │   │   ├── store
> │   │   │   │   └── AuthContext.tsx
> │   │   │   ├── types
> │   │   │   │   └── database.types.ts
> │   │   │   ├── App.tsx
> │   │   │   ├── main.tsx
> │   │   │   └── vite-env.d.ts
> │   │   ├── index.html
> │   │   ├── package-lock.json
> │   │   ├── package.json
> │   │   ├── tailwind.config.js
> │   │   ├── tsconfig.json
> │   │   └── vite.config.ts
> │   ├── rag_env
> │   │   ├── Include
> │   │   ├── Lib
> │   │   │   └── site-packages
> │   │   │       ├── PIL
> │   │   │       │   ├── __pycache__
> │   │   │       │   ├── __init__.py
> │   │   │       │   ├── __main__.py
> │   │   │       │   ├── _avif.cp314-win_amd64.pyd
> │   │   │       │   ├── _avif.pyi
> │   │   │       │   ├── _binary.py
> │   │   │       │   ├── _deprecate.py
> │   │   │       │   ├── _imaging.cp314-win_amd64.pyd
> │   │   │       │   ├── _imaging.pyi
> │   │   │       │   ├── _imagingcms.cp314-win_amd64.pyd
> │   │   │       │   ├── _imagingcms.pyi
> │   │   │       │   ├── _imagingft.cp314-win_amd64.pyd
> │   │   │       │   ├── _imagingft.pyi
> │   │   │       │   ├── _imagingmath.cp314-win_amd64.pyd
> │   │   │       │   ├── _imagingmath.pyi
> │   │   │       │   ├── _imagingmorph.cp314-win_amd64.pyd
> │   │   │       │   ├── _imagingmorph.pyi
> │   │   │       │   ├── _imagingtk.cp314-win_amd64.pyd
> │   │   │       │   ├── _imagingtk.pyi
> │   │   │       │   ├── _tkinter_finder.py
> │   │   │       │   ├── _typing.py
> │   │   │       │   ├── _util.py
> │   │   │       │   ├── _version.py
> │   │   │       │   ├── _webp.cp314-win_amd64.pyd
> │   │   │       │   ├── _webp.pyi
> │   │   │       │   ├── AvifImagePlugin.py
> │   │   │       │   ├── BdfFontFile.py
> │   │   │       │   ├── BlpImagePlugin.py
> │   │   │       │   ├── BmpImagePlugin.py
> │   │   │       │   ├── BufrStubImagePlugin.py
> │   │   │       │   ├── ContainerIO.py
> │   │   │       │   ├── CurImagePlugin.py
> │   │   │       │   ├── DcxImagePlugin.py
> │   │   │       │   ├── DdsImagePlugin.py
> │   │   │       │   ├── EpsImagePlugin.py
> │   │   │       │   ├── ExifTags.py
> │   │   │       │   ├── features.py
> │   │   │       │   ├── FitsImagePlugin.py
> │   │   │       │   ├── FliImagePlugin.py
> │   │   │       │   ├── FontFile.py
> │   │   │       │   ├── FpxImagePlugin.py
> │   │   │       │   ├── FtexImagePlugin.py
> │   │   │       │   ├── GbrImagePlugin.py
> │   │   │       │   ├── GdImageFile.py
> │   │   │       │   ├── GifImagePlugin.py
> │   │   │       │   ├── GimpGradientFile.py
> │   │   │       │   ├── GimpPaletteFile.py
> │   │   │       │   ├── GribStubImagePlugin.py
> │   │   │       │   ├── Hdf5StubImagePlugin.py
> │   │   │       │   ├── IcnsImagePlugin.py
> │   │   │       │   ├── IcoImagePlugin.py
> │   │   │       │   ├── Image.py
> │   │   │       │   ├── ImageChops.py
> │   │   │       │   ├── ImageCms.py
> │   │   │       │   ├── ImageColor.py
> │   │   │       │   ├── ImageDraw.py
> │   │   │       │   ├── ImageDraw2.py
> │   │   │       │   ├── ImageEnhance.py
> │   │   │       │   ├── ImageFile.py
> │   │   │       │   ├── ImageFilter.py
> │   │   │       │   ├── ImageFont.py
> │   │   │       │   ├── ImageGrab.py
> │   │   │       │   ├── ImageMath.py
> │   │   │       │   ├── ImageMode.py
> │   │   │       │   ├── ImageMorph.py
> │   │   │       │   ├── ImageOps.py
> │   │   │       │   ├── ImagePalette.py
> │   │   │       │   ├── ImagePath.py
> │   │   │       │   ├── ImageQt.py
> │   │   │       │   ├── ImageSequence.py
> │   │   │       │   ├── ImageShow.py
> │   │   │       │   ├── ImageStat.py
> │   │   │       │   ├── ImageText.py
> │   │   │       │   ├── ImageTk.py
> │   │   │       │   ├── ImageTransform.py
> │   │   │       │   ├── ImageWin.py
> │   │   │       │   ├── ImImagePlugin.py
> │   │   │       │   ├── ImtImagePlugin.py
> │   │   │       │   ├── IptcImagePlugin.py
> │   │   │       │   ├── Jpeg2KImagePlugin.py
> │   │   │       │   ├── JpegImagePlugin.py
> │   │   │       │   ├── JpegPresets.py
> │   │   │       │   ├── McIdasImagePlugin.py
> │   │   │       │   ├── MicImagePlugin.py
> │   │   │       │   ├── MpegImagePlugin.py
> │   │   │       │   ├── MpoImagePlugin.py
> │   │   │       │   ├── MspImagePlugin.py
> │   │   │       │   ├── PaletteFile.py
> │   │   │       │   ├── PalmImagePlugin.py
> │   │   │       │   ├── PcdImagePlugin.py
> │   │   │       │   ├── PcfFontFile.py
> │   │   │       │   ├── PcxImagePlugin.py
> │   │   │       │   ├── PdfImagePlugin.py
> │   │   │       │   ├── PdfParser.py
> │   │   │       │   ├── PixarImagePlugin.py
> │   │   │       │   ├── PngImagePlugin.py
> │   │   │       │   ├── PpmImagePlugin.py
> │   │   │       │   ├── PsdImagePlugin.py
> │   │   │       │   ├── PSDraw.py
> │   │   │       │   ├── py.typed
> │   │   │       │   ├── QoiImagePlugin.py
> │   │   │       │   ├── report.py
> │   │   │       │   ├── SgiImagePlugin.py
> │   │   │       │   ├── SpiderImagePlugin.py
> │   │   │       │   ├── SunImagePlugin.py
> │   │   │       │   ├── TarIO.py
> │   │   │       │   ├── TgaImagePlugin.py
> │   │   │       │   ├── TiffImagePlugin.py
> │   │   │       │   ├── TiffTags.py
> │   │   │       │   ├── WalImageFile.py
> │   │   │       │   ├── WebPImagePlugin.py
> │   │   │       │   ├── WmfImagePlugin.py
> │   │   │       │   ├── XbmImagePlugin.py
> │   │   │       │   ├── XpmImagePlugin.py
> │   │   │       │   └── XVThumbImagePlugin.py
> │   │   │       ├── pillow-12.1.1.dist-info
> │   │   │       │   ├── licenses
> │   │   │       │   ├── INSTALLER
> │   │   │       │   ├── METADATA
> │   │   │       │   ├── RECORD
> │   │   │       │   ├── REQUESTED
> │   │   │       │   ├── top_level.txt
> │   │   │       │   ├── WHEEL
> │   │   │       │   └── zip-safe
> │   │   │       ├── pip
> │   │   │       │   ├── __pycache__
> │   │   │       │   ├── _internal
> │   │   │       │   ├── _vendor
> │   │   │       │   ├── __init__.py
> │   │   │       │   ├── __main__.py
> │   │   │       │   ├── __pip-runner__.py
> │   │   │       │   └── py.typed
> │   │   │       └── pip-25.2.dist-info
> │   │   │           ├── licenses
> │   │   │           ├── entry_points.txt
> │   │   │           ├── INSTALLER
> │   │   │           ├── METADATA
> │   │   │           ├── RECORD
> │   │   │           ├── REQUESTED
> │   │   │           ├── top_level.txt
> │   │   │           └── WHEEL
> │   │   ├── Scripts
> │   │   │   ├── activate
> │   │   │   ├── activate.bat
> │   │   │   ├── activate.fish
> │   │   │   ├── Activate.ps1
> │   │   │   ├── deactivate.bat
> │   │   │   ├── pip.exe
> │   │   │   ├── pip3.14.exe
> │   │   │   ├── pip3.exe
> │   │   │   ├── python.exe
> │   │   │   └── pythonw.exe
> │   │   └── pyvenv.cfg
> │   ├── scripts
> │   │   ├── ai
> │   │   │   ├── agents
> │   │   │   │   ├── agent_models.py
> │   │   │   │   └── agent_qios.py
> │   │   │   ├── memory
> │   │   │   │   └── memory_store.py
> │   │   │   ├── prompts
> │   │   │   │   └── prompt_gina.py
> │   │   │   └── rag
> │   │   │       └── rag_core.py
> │   │   ├── automate
> │   │   │   ├── core
> │   │   │   │   └── setup_antigravity.py
> │   │   │   ├── health
> │   │   │   │   ├── health_check_status.py
> │   │   │   │   ├── health_check_worker_status.py
> │   │   │   │   └── health_check_workers.py
> │   │   │   ├── jobs
> │   │   │   │   └── job_runner.py
> │   │   │   ├── logs
> │   │   │   │   ├── log_build_error.ps1
> │   │   │   │   └── log_error_supabase.py
> │   │   │   ├── movers
> │   │   │   │   └── move_chatgpt_audio_registry.py
> │   │   │   ├── runners
> │   │   │   │   ├── run_agent_command.py
> │   │   │   │   ├── run_agent_service.py
> │   │   │   │   └── run_worker.py
> │   │   │   └── schedulers
> │   │   │       ├── sched_install.ps1
> │   │   │       ├── sched_queue_load.py
> │   │   │       └── sched_windows_task.xml
> │   │   ├── core
> │   │   │   ├── auth
> │   │   │   │   ├── auth_check.ps1
> │   │   │   │   └── auth_secrets_check.ps1
> │   │   │   ├── docs
> │   │   │   │   └── usage.md
> │   │   │   ├── modules
> │   │   │   │   └── module_app_create.py
> │   │   │   ├── check_ffmpeg.py
> │   │   │   ├── core_base.py
> │   │   │   ├── core_qi_codex.py
> │   │   │   ├── core_qios_local.py
> │   │   │   └── ffmpeg_utils.py
> │   │   ├── deploy
> │   │   │   ├── scripts
> │   │   │   │   ├── deploy_all.ps1
> │   │   │   │   ├── deploy_critical.ps1
> │   │   │   │   └── deploy_git_autopush.ahk
> │   │   │   ├── sync
> │   │   │   │   ├── README.md
> │   │   │   │   ├── sync_dev_gdrive.py
> │   │   │   │   ├── sync_gdrive.ps1
> │   │   │   │   ├── sync_git_push.py
> │   │   │   │   ├── sync_index_content.ts
> │   │   │   │   ├── sync_lfs_disable.ps1
> │   │   │   │   └── sync_lfs_enable.ps1
> │   │   │   └── workers
> │   │   │       ├── worker_deploy_all.ps1
> │   │   │       ├── worker_deploy.ps1
> │   │   │       └── worker_urls_get.ps1
> │   │   ├── inbox
> │   │   │   ├── audit_inbox.ts
> │   │   │   ├── dedup_detect.ts
> │   │   │   ├── fix_inbox_names.ts
> │   │   │   ├── merge_plan.ts
> │   │   │   ├── normalize_inbox.ts
> │   │   │   └── run_inbox.ts
> │   │   ├── index
> │   │   │   ├── builders
> │   │   │   │   ├── index_build.ps1
> │   │   │   │   ├── index_immigration_example.py
> │   │   │   │   ├── index_timeline_713_build.js
> │   │   │   │   ├── index_timeline_build.js
> │   │   │   │   └── index_timeline_json_build.js
> │   │   │   ├── directory
> │   │   │   │   ├── compile
> │   │   │   │   │   ├── dir_code_compile_review.py
> │   │   │   │   │   ├── dir_timeline_load.js
> │   │   │   │   │   └── dir_tree_compile.py
> │   │   │   │   ├── create
> │   │   │   │   │   ├── dir_app_create.py
> │   │   │   │   │   ├── dir_canvas_create.py
> │   │   │   │   │   ├── dir_canvas_directory_create.py
> │   │   │   │   │   ├── dir_cloudflare_md_create.py
> │   │   │   │   │   ├── dir_node_new.bat
> │   │   │   │   │   ├── dir_registry_trash_summarize.py
> │   │   │   │   │   └── dir_stubs_create.py
> │   │   │   │   ├── flatten
> │   │   │   │   │   ├── dir_flatten.py
> │   │   │   │   │   └── dir_folders_ultra_clean.py
> │   │   │   │   ├── indices
> │   │   │   │   │   └── dir_indexes_generate.py
> │   │   │   │   └── maps
> │   │   │   │       ├── dir_map.py
> │   │   │   │       └── dir_slugs_map.py
> │   │   │   └── registry
> │   │   │       ├── reg_files_build.py
> │   │   │       └── reg_files_generate.ps1
> │   │   ├── ingest
> │   │   │   ├── audio
> │   │   │   │   └── audio_transcribe.py
> │   │   │   ├── files
> │   │   │   │   ├── file_large_move.ps1
> │   │   │   │   ├── file_md_body_move.py
> │   │   │   │   ├── file_media_tree_merge.bat
> │   │   │   │   ├── file_realm_list.py
> │   │   │   │   └── file_scan_fs.py
> │   │   │   ├── inbox
> │   │   │   │   ├── inbox_audit.ts
> │   │   │   │   ├── inbox_downloads_rename.py
> │   │   │   │   ├── inbox_flatten.ps1
> │   │   │   │   ├── inbox_merge_plan.ts
> │   │   │   │   ├── inbox_names_fix.ts
> │   │   │   │   └── inbox_run.ts
> │   │   │   └── video
> │   │   │       ├── video_media_tree_merge.py
> │   │   │       └── video_mkvs_merge.py
> │   │   ├── pdf
> │   │   │   ├── process_inbox_pdfs.ts
> │   │   │   ├── process_pdf.ts
> │   │   │   └── validate_pdfs.ts
> │   │   ├── process
> │   │   │   ├── clean
> │   │   │   │   ├── clean_analysis.ps1
> │   │   │   │   ├── clean_app_roots.py
> │   │   │   │   ├── clean_comprehensive.ps1
> │   │   │   │   ├── clean_continue.ps1
> │   │   │   │   ├── clean_dedup_detect.ts
> │   │   │   │   ├── clean_duplicates_find.ps1
> │   │   │   │   ├── clean_duplicates_find.py
> │   │   │   │   ├── clean_duplicates_move.ps1
> │   │   │   │   ├── clean_housekeeper_run.py
> │   │   │   │   ├── clean_inbox_organize.py
> │   │   │   │   ├── clean_intake_trash.py
> │   │   │   │   ├── clean_qi_prefixes.py
> │   │   │   │   ├── clean_storage_bloat.py
> │   │   │   │   ├── clean_stubs_detect.py
> │   │   │   │   └── clean_violations.py
> │   │   │   ├── convert
> │   │   │   │   ├── csv
> │   │   │   │   │   ├── csv_convert.js
> │   │   │   │   │   ├── csv_convert.ps1
> │   │   │   │   │   ├── csv_md_check.py
> │   │   │   │   │   ├── csv_to_md.py
> │   │   │   │   │   ├── README.md
> │   │   │   │   │   └── USAGE.md
> │   │   │   │   ├── folders
> │   │   │   │   │   ├── folder_flatten_finish.ps1
> │   │   │   │   │   ├── folder_flatten_organize.ps1
> │   │   │   │   │   └── folder_flatten.py
> │   │   │   │   ├── json
> │   │   │   │   │   └── json_kb_generate.py
> │   │   │   │   ├── text
> │   │   │   │   │   └── text_extract.py
> │   │   │   │   ├── video
> │   │   │   │   │   └── video_mkv_enhance.py
> │   │   │   │   ├── zip
> │   │   │   │   │   └── zip_downloads_extract.py
> │   │   │   │   ├── convert_code_extract.py
> │   │   │   │   └── convert_errors_to_markdown.py
> │   │   │   ├── docs
> │   │   │   │   └── _Convert_csv_to_md.md
> │   │   │   ├── normalize
> │   │   │   │   ├── norm_files_sort.py
> │   │   │   │   ├── norm_inbox.ts
> │   │   │   │   └── norm_spaces_fix.py
> │   │   │   ├── pdf
> │   │   │   │   ├── pdf_inbox_process.ts
> │   │   │   │   ├── pdf_process.ts
> │   │   │   │   └── pdf_validate.ts
> │   │   │   └── validate
> │   │   │       ├── valid_cloud.ps1
> │   │   │       ├── valid_compliance_check.py
> │   │   │       ├── valid_csv_md_compare.py
> │   │   │       ├── valid_csv_search.py
> │   │   │       ├── valid_db_examine.py
> │   │   │       ├── valid_drive_compare.py
> │   │   │       ├── valid_file_error_context.py
> │   │   │       ├── valid_housekeeping.ps1
> │   │   │       ├── valid_linter_run.py
> │   │   │       ├── valid_linter.py
> │   │   │       ├── valid_local.ps1
> │   │   │       └── valid_md_check.py
> │   │   ├── processing
> │   │   │   └── process_inbox_pdfs.ts
> │   │   ├── rules
> │   │   │   ├── audit_repo_rules.ts
> │   │   │   └── fix_repo_rules.ts
> │   │   ├── services
> │   │   │   ├── calendar
> │   │   │   │   ├── calendar_create_event.py
> │   │   │   │   └── calendar_get_upcoming.py
> │   │   │   ├── crm
> │   │   │   │   ├── crm_create_contact.py
> │   │   │   │   ├── crm_create_task.py
> │   │   │   │   ├── crm_list_recent_contacts.py
> │   │   │   │   └── crm_search_person.py
> │   │   │   ├── mail
> │   │   │   │   ├── mail_get_recent.py
> │   │   │   │   └── mail_send.py
> │   │   │   ├── sms
> │   │   │   │   └── sms_send.py
> │   │   │   ├── vault
> │   │   │   │   ├── vault_append_note.py
> │   │   │   │   └── vault_create_note.py
> │   │   │   └── web
> │   │   │       ├── web_get.py
> │   │   │       └── web_search.py
> │   │   ├── steps
> │   │   │   ├── step1_combine.py
> │   │   │   ├── step1_fast_combine.py
> │   │   │   ├── step2_convert.py
> │   │   │   ├── step2_flip.py
> │   │   │   ├── step3_enhance.py
> │   │   │   └── step3_filter.py
> │   │   ├── sync
> │   │   │   ├── index_content.ts
> │   │   │   └── windows_task_scheduler.xml
> │   │   ├── tests
> │   │   │   ├── test_abbreviations.py
> │   │   │   ├── test_gina_chat_simple.ps1
> │   │   │   └── test_pipeline.ps1
> │   │   ├── tools
> │   │   │   ├── debug
> │   │   │   │   └── debug_maps.py
> │   │   │   ├── frontmatter
> │   │   │   │   ├── frontmatter_add.py
> │   │   │   │   ├── frontmatter_enforce.py
> │   │   │   │   ├── frontmatter_utils.py
> │   │   │   │   └── frontmatter_validate.ts
> │   │   │   ├── maps
> │   │   │   │   ├── map_3d_mindmap_run.bat
> │   │   │   │   ├── map_3d_real_run.bat
> │   │   │   │   └── map_3d_simple_run.bat
> │   │   │   ├── misc
> │   │   │   │   ├── scripts_rename_manifest.json
> │   │   │   │   └── scripts_rename_pass1.py
> │   │   │   ├── search
> │   │   │   │   └── search_processed_docs.py
> │   │   │   ├── ai_video_filter.py
> │   │   │   ├── batch_processor.py
> │   │   │   ├── check_processed.py
> │   │   │   ├── enforce_fm.py
> │   │   │   ├── find_failed.py
> │   │   │   ├── flatten_enhance.py
> │   │   │   ├── flatten_trade.py
> │   │   │   ├── local_processor.py
> │   │   │   ├── pipeline_processor.py
> │   │   │   ├── tools_manifest.json
> │   │   │   └── unblock_all.bat
> │   │   ├── yaml
> │   │   │   ├── csv_to_md_mappings.yaml
> │   │   │   ├── housekeeping.yaml
> │   │   │   ├── qi_codex.config.yaml
> │   │   │   ├── qi_prefix_map.yaml
> │   │   │   ├── qicompiler_config.yaml
> │   │   │   ├── qione_rag_routes.yaml
> │   │   │   ├── slugs_mapping.yaml
> │   │   │   └── tree_compiler_config.yaml
> │   │   ├── master_pipeline.py
> │   │   ├── orchestrator.py
> │   │   └── update_imports.py
> │   ├── sites
> │   │   ├── qially-me
> │   │   │   ├── public
> │   │   │   │   ├── cards
> │   │   │   │   │   ├── fresh.png
> │   │   │   │   │   ├── fresh.webp
> │   │   │   │   │   ├── glass.png
> │   │   │   │   │   ├── glass.webp
> │   │   │   │   │   └── mermaid.svg
> │   │   │   │   ├── activity.svg
> │   │   │   │   ├── og.webp
> │   │   │   │   ├── placeholder.webp
> │   │   │   │   └── rss.svg
> │   │   │   ├── scripts
> │   │   │   │   └── build-pagefind-index.ts
> │   │   │   ├── site_QSaysIt_v1
> │   │   │   │   ├── posts
> │   │   │   │   │   ├── 2026
> │   │   │   │   │   └── index.md
> │   │   │   │   ├── qsaysit_blog
> │   │   │   │   │   └── templates
> │   │   │   │   └── templates
> │   │   │   │       ├── 2026-02-19_post-title
> │   │   │   │       └── post_template.md
> │   │   │   ├── src
> │   │   │   │   ├── assets
> │   │   │   │   │   ├── images
> │   │   │   │   │   └── creations.json
> │   │   │   │   ├── components
> │   │   │   │   │   ├── blog
> │   │   │   │   │   ├── knowledge-card
> │   │   │   │   │   ├── landing-page
> │   │   │   │   │   ├── navigation
> │   │   │   │   │   ├── slide
> │   │   │   │   │   ├── ui
> │   │   │   │   │   ├── BaseHead.astro
> │   │   │   │   │   ├── BetaBadge.astro
> │   │   │   │   │   ├── copy-button.tsx
> │   │   │   │   │   ├── FormattedDate.astro
> │   │   │   │   │   ├── HeaderLink.astro
> │   │   │   │   │   ├── image-viewer.tsx
> │   │   │   │   │   ├── OptimizedImage.astro
> │   │   │   │   │   ├── ProductCard.tsx
> │   │   │   │   │   ├── ProductSection.astro
> │   │   │   │   │   ├── ShareButtons.astro
> │   │   │   │   │   └── TagFilter.astro
> │   │   │   │   ├── content
> │   │   │   │   │   ├── blogs
> │   │   │   │   │   ├── cards
> │   │   │   │   │   ├── doodles
> │   │   │   │   │   └── slides
> │   │   │   │   ├── layouts
> │   │   │   │   │   ├── ContentIndexLayout.astro
> │   │   │   │   │   └── MainLayout.astro
> │   │   │   │   ├── lib
> │   │   │   │   │   ├── navigation.ts
> │   │   │   │   │   ├── pagination.ts
> │   │   │   │   │   └── utils.ts
> │   │   │   │   ├── pages
> │   │   │   │   │   ├── blogs
> │   │   │   │   │   ├── cards
> │   │   │   │   │   ├── doodles
> │   │   │   │   │   ├── slides
> │   │   │   │   │   ├── creations.astro
> │   │   │   │   │   ├── index.astro
> │   │   │   │   │   ├── og-enhanced.ts
> │   │   │   │   │   ├── rss.xml.ts
> │   │   │   │   │   └── search.astro
> │   │   │   │   ├── schemas
> │   │   │   │   │   ├── blog.ts
> │   │   │   │   │   ├── card.ts
> │   │   │   │   │   ├── doodle.ts
> │   │   │   │   │   └── slide.ts
> │   │   │   │   ├── styles
> │   │   │   │   │   ├── article.css
> │   │   │   │   │   ├── card.css
> │   │   │   │   │   ├── global.css
> │   │   │   │   │   └── scrolling-tags.css
> │   │   │   │   ├── themes
> │   │   │   │   │   ├── knowledge-card-themes.ts
> │   │   │   │   │   └── slide-card-themes.ts
> │   │   │   │   ├── types
> │   │   │   │   │   ├── product.ts
> │   │   │   │   │   └── reveal.js-mermaid-plugin.d.ts
> │   │   │   │   ├── consts.ts
> │   │   │   │   ├── content.config.ts
> │   │   │   │   └── env.ts
> │   │   │   ├── astro.config.mjs
> │   │   │   ├── biome.json
> │   │   │   ├── components.json
> │   │   │   ├── package-lock.json
> │   │   │   ├── package.json
> │   │   │   ├── pnpm-lock.yaml
> │   │   │   └── tsconfig.json
> │   │   └── qially-web
> │   │       ├── assets
> │   │       │   ├── css
> │   │       │   │   └── styles.css
> │   │       │   ├── files
> │   │       │   │   ├── forms
> │   │       │   │   ├── balance-sheet-template.xlsx
> │   │       │   │   ├── emailsignature.html
> │   │       │   │   ├── income-statement-template.xlsx
> │   │       │   │   ├── index.md
> │   │       │   │   ├── payroll-calendar-2026.pdf
> │   │       │   │   ├── resume.pdf
> │   │       │   │   └── tax-prep-checklist.pdf
> │   │       │   ├── imgs
> │   │       │   │   ├── business_tools
> │   │       │   │   ├── allegaracasa.jpg
> │   │       │   │   ├── astrotext.png
> │   │       │   │   ├── back-master-small.jpg
> │   │       │   │   ├── business-performance-wins.png
> │   │       │   │   ├── cassie-boca-x-tbVqkfQCU-unsplash.jpg
> │   │       │   │   ├── cover.jpg
> │   │       │   │   ├── favicon.ico
> │   │       │   │   ├── favicon.png
> │   │       │   │   ├── favicon.webp
> │   │       │   │   ├── jesse-gardner-EqdpXeemf58-unsplash.jpg
> │   │       │   │   ├── jf-martin-Ofs3LjEUcrk-unsplash.jpg
> │   │       │   │   ├── josh-rose-trYl7JYATH0-unsplash.jpg
> │   │       │   │   ├── llegaracasa.jpg
> │   │       │   │   ├── logo.png
> │   │       │   │   ├── profile.jpg
> │   │       │   │   ├── profile.png
> │   │       │   │   └── tersius-van-rhyn-xcQWMPm9fG8-unsplash.jpg
> │   │       │   ├── js
> │   │       │   │   ├── i18n.js
> │   │       │   │   └── main.js
> │   │       │   └── vids
> │   │       │       └── video-logo.mp4
> │   │       ├── cody
> │   │       │   └── index.html
> │   │       ├── functions
> │   │       │   └── [[path]].js
> │   │       ├── js
> │   │       │   └── main.js
> │   │       ├── kb
> │   │       │   ├── accounting-cleanup
> │   │       │   │   └── index.html
> │   │       │   ├── getting-started
> │   │       │   │   └── index.html
> │   │       │   ├── irs-notices
> │   │       │   │   └── index.html
> │   │       │   ├── tax-resolution
> │   │       │   │   └── index.html
> │   │       │   └── index.html
> │   │       ├── legal
> │   │       │   ├── msa
> │   │       │   │   └── index.html
> │   │       │   ├── privacy
> │   │       │   │   └── index.html
> │   │       │   └── terms
> │   │       │       └── index.html
> │   │       ├── modules
> │   │       │   ├── hr-ops
> │   │       │   │   └── index.html
> │   │       │   ├── it-ai
> │   │       │   │   └── index.html
> │   │       │   ├── qisuite
> │   │       │   │   └── index.html
> │   │       │   ├── taxes
> │   │       │   │   ├── tax-prep-2025
> │   │       │   │   ├── year-end-process
> │   │       │   │   └── index.html
> │   │       │   └── index.html
> │   │       ├── pages
> │   │       │   ├── budgets
> │   │       │   │   └── index.html
> │   │       │   ├── business_tools
> │   │       │   │   └── index.html
> │   │       │   ├── chat
> │   │       │   │   ├── index.html
> │   │       │   │   └── sales-iq-landing-page-qr-code.png
> │   │       │   ├── compliance
> │   │       │   │   ├── internal
> │   │       │   │   ├── service_animal_gigi
> │   │       │   │   ├── data-inventory.html
> │   │       │   │   ├── incident-response.html
> │   │       │   │   ├── index.html
> │   │       │   │   ├── risk-assessment.html
> │   │       │   │   └── wisp-core.html
> │   │       │   ├── ecard
> │   │       │   │   ├── cody.vcf
> │   │       │   │   └── index.html
> │   │       │   ├── estate-planning
> │   │       │   │   └── index.html
> │   │       │   ├── letters
> │   │       │   │   ├── client.wiletvaldo_calderon-ramirez
> │   │       │   │   ├── engagement
> │   │       │   │   └── evansville_inn
> │   │       │   ├── msa
> │   │       │   │   └── index.html
> │   │       │   ├── portfolio
> │   │       │   │   └── index.html
> │   │       │   ├── privacy
> │   │       │   │   └── index.html
> │   │       │   ├── referral
> │   │       │   │   ├── cashapp
> │   │       │   │   ├── quickbooks
> │   │       │   │   ├── zoho
> │   │       │   │   └── index.html
> │   │       │   ├── resources
> │   │       │   │   └── index.html
> │   │       │   ├── review
> │   │       │   │   ├── index.html
> │   │       │   │   └── qrcode_www.google.com.png
> │   │       │   ├── services
> │   │       │   │   └── index.html
> │   │       │   ├── showcases
> │   │       │   │   ├── 20000-swing
> │   │       │   │   └── videos.html
> │   │       │   └── terms
> │   │       │       └── index.html
> │   │       ├── portfolio
> │   │       │   └── index.html
> │   │       ├── public
> │   │       ├── resources
> │   │       │   ├── compliance
> │   │       │   │   ├── data-inventory
> │   │       │   │   ├── incident-response
> │   │       │   │   ├── provider-agreements
> │   │       │   │   ├── risk-assessment
> │   │       │   │   ├── training-logs
> │   │       │   │   ├── wisp
> │   │       │   │   └── index.html
> │   │       │   └── index.html
> │   │       ├── services
> │   │       │   ├── automation-ai
> │   │       │   │   └── index.html
> │   │       │   ├── client-portals
> │   │       │   │   └── index.html
> │   │       │   ├── hr-operations
> │   │       │   │   └── index.html
> │   │       │   ├── tax-preparation
> │   │       │   │   ├── email-templates
> │   │       │   │   ├── forms
> │   │       │   │   ├── intake
> │   │       │   │   ├── next-steps
> │   │       │   │   ├── index.html
> │   │       │   │   ├── qr-code.html
> │   │       │   │   └── tax-prep-2025-booking.html
> │   │       │   └── index.html
> │   │       ├── src
> │   │       │   ├── app
> │   │       │   ├── components
> │   │       │   ├── content
> │   │       │   ├── lib
> │   │       │   ├── styles
> │   │       │   └── types
> │   │       ├── _redirects
> │   │       ├── 404.html
> │   │       ├── contact.json
> │   │       ├── footer.html
> │   │       ├── header.html
> │   │       ├── humans.txt
> │   │       ├── index.html
> │   │       ├── LICENSE
> │   │       ├── main.js
> │   │       ├── manifest.webmanifest
> │   │       ├── orchestrate_clarity.py
> │   │       ├── package.json
> │   │       ├── README.md
> │   │       ├── robots.txt
> │   │       ├── service-worker.js
> │   │       ├── services-full.json
> │   │       ├── sitemap.xml
> │   │       └── tsconfig.json
> │   ├── templates
> │   │   ├── adr_template.md
> │   │   ├── artifact_template.md
> │   │   ├── note_template.md
> │   │   └── README.md
> │   ├── workers
> │   │   ├── _shared
> │   │   │   ├── constitution.ts
> │   │   │   ├── heartbeat.ts
> │   │   │   ├── ignore.ts
> │   │   │   ├── index (2).html
> │   │   │   ├── index (3).html
> │   │   │   └── index.html
> │   │   ├── embedder
> │   │   │   ├── src
> │   │   │   │   └── worker.ts
> │   │   │   ├── index.html
> │   │   │   ├── package.json
> │   │   │   ├── README.MD
> │   │   │   └── wrangler.toml
> │   │   ├── embedding
> │   │   │   ├── src
> │   │   │   │   └── worker.ts
> │   │   │   ├── package.json
> │   │   │   ├── README.MD
> │   │   │   └── wrangler.toml
> │   │   ├── graph
> │   │   │   ├── src
> │   │   │   │   └── worker.ts
> │   │   │   ├── package.json
> │   │   │   └── wrangler.toml
> │   │   ├── ingestion
> │   │   │   ├── src
> │   │   │   │   └── worker.ts
> │   │   │   ├── index (2).html
> │   │   │   ├── index (3).html
> │   │   │   ├── index.html
> │   │   │   ├── package.json
> │   │   │   ├── worker_ingestion.ts
> │   │   │   ├── wrangler (2).toml
> │   │   │   └── wrangler.toml
> │   │   ├── memory
> │   │   │   ├── src
> │   │   │   ├── tests
> │   │   │   ├── package.json
> │   │   │   ├── README_API.md
> │   │   │   ├── README_DEV.md
> │   │   │   ├── README_SECRETS.md
> │   │   │   ├── sync-secrets.sh
> │   │   │   ├── VERIFY_SETUP.md
> │   │   │   └── wrangler.toml
> │   │   ├── metadata_naming
> │   │   │   ├── src
> │   │   │   │   └── worker.ts
> │   │   │   ├── index.html
> │   │   │   ├── package.json
> │   │   │   ├── worker_metadata_naming.ts
> │   │   │   └── wrangler.toml
> │   │   ├── orchestrator
> │   │   │   ├── migrations
> │   │   │   ├── src
> │   │   │   │   ├── OrchestratorState.ts
> │   │   │   │   └── worker.ts
> │   │   │   ├── index (2).html
> │   │   │   ├── index (3).html
> │   │   │   ├── index.html
> │   │   │   ├── OrchestratorState (2).ts
> │   │   │   ├── OrchestratorState.ts
> │   │   │   ├── package.json
> │   │   │   ├── qios_06_workers_orchestrator (2).canvas
> │   │   │   ├── qios_06_workers_orchestrator.canvas
> │   │   │   ├── worker_orchestrator.ts
> │   │   │   └── wrangler.toml
> │   │   ├── repair
> │   │   │   ├── src
> │   │   │   │   └── worker.ts
> │   │   │   ├── package.json
> │   │   │   └── wrangler.toml
> │   │   ├── self_heal
> │   │   │   ├── src
> │   │   │   │   └── worker.ts
> │   │   │   ├── index (2).html
> │   │   │   ├── index (3).html
> │   │   │   ├── index.html
> │   │   │   ├── package.json
> │   │   │   ├── worker_self_heal.ts
> │   │   │   └── wrangler.toml
> │   │   ├── semantic_router
> │   │   │   ├── src
> │   │   │   │   └── worker.ts
> │   │   │   ├── index (2).html
> │   │   │   ├── index (3).html
> │   │   │   ├── index.html
> │   │   │   ├── package.json
> │   │   │   ├── worker_semantic_router.ts
> │   │   │   └── wrangler.toml
> │   │   ├── supabase
> │   │   │   ├── functions
> │   │   │   │   └── qivault-ingest
> │   │   │   │       └── index.ts
> │   │   │   ├── migrations
> │   │   │   │   └── qicase_meta
> │   │   │   │       ├── _journal.json
> │   │   │   │       └── 0000_snapshot.json
> │   │   │   ├── seed
> │   │   │   ├── snippets
> │   │   │   │   └── is_admin.sql
> │   │   │   └── config.toml
> │   │   ├── package.json
> │   │   ├── README.md
> │   │   └── worker.py
> │   ├── eslint.config.mjs
> │   ├── justfile
> │   ├── LICENSE
> │   ├── package-lock.json
> │   ├── package.json
> │   ├── postcss.config.js
> │   ├── README.md
> │   ├── repo.rules.json
> │   ├── tailwind.config.ts
> │   ├── tsconfig.base.json
> │   ├── tsconfig.root.json
> │   ├── turbo.json
> │   └── vizvibe.mmd
> └── QiLabs.code-workspace
> ```

### User
> # strict-compliance

> 

> Before planning or writing any code, you MUST review our core QiOS Blueprint documentation to ensure strict alignment. All blueprint files are located within the `__QiOS_Master_Blueprint_v0.4` directory:

> 

> - @/__QiOS_Master_Blueprint_v0.4/docs/01_governance/policies.md (Merge & Placement Policies)

> - @/__QiOS_Master_Blueprint_v0.4/docs/01_governance/standards.md (Namespace & Metadata Standards)

> - @/__QiOS_Master_Blueprint_v0.4/docs/03_structure/placement_rules.md (The Primary Rule: One canonical domain per object)

> - @/__QiOS_Master_Blueprint_v0.4/docs/04_data/schema.md (Supabase Migrations as canonical truth)

> 

> You must adhere to the QiOS constraints:

> 1. Respect the 3-Band Model (Core, Platform, Domain).

> 2. Do not write domain logic or new tables into the `public` schema.

> 3. Ensure every domain table carries a `tenant_id` for RLS isolation.

> 4. Do not bypass the "Spine" ingestion flow for file tracking.

> 

> If your proposed solution falls OUTSIDE the bounds of these documents, HALT coding. Provide an "Out-of-Bounds Alert" containing:

> 

> 1. **The Deviation:** Explain exactly which policy, standard, or placement rule is being broken.

> 2. **The Ripple-Check:** Detail how this impacts the rest of the project (e.g., how it affects Supabase RLS policies, the 3-Band Model, or Python workers).

> 3. **Pros & Cons:** Objective breakdown of making this exception versus sticking to the established docs.

> 4. **Approval Request:** Ask the user if they wish to proceed. Instruct them to run `/update-adr` if approved. 
> # update-adr

> Description: Formalizes an approved architectural deviation by updating the QiOS Blueprint, creating an ADR, and modifying the changelog.

> 

> Step 1: Identify the approved out-of-bounds change from our current conversation context.

> Step 2: Update the relevant governance files (e.g., `@/__QiOS_Master_Blueprint_v0.4/docs/01_governance/standards.md` or `@/__QiOS_Master_Blueprint_v0.4/docs/03_structure/placement_rules.md`) to officially incorporate this new rule.

> Step 3: Check the `@/__QiOS_Master_Blueprint_v0.4/docs/adr/` folder to determine the next sequential four-digit number.

> Step 4: Read `@/__QiOS_Master_Blueprint_v0.4/docs/adr/ADR-0000_template.md` to get the required formatting.

> Step 5: Generate the new Architecture Decision Record in the `@/__QiOS_Master_Blueprint_v0.4/docs/adr/` folder using the exact structure from the template. Format the filename as `ADR-XXXX_brief_description.md`.

> Step 6: Append a new entry to `@/__QiOS_Master_Blueprint_v0.4/docs/appendices/changelog.md` detailing what was changed, linking to the new ADR, and explaining exactly why.

> Step 7: Provide a brief summary confirming all QiOS Blueprint documentation has been successfully synchronized.

### Assistant
> Perfect. With the actual repo tree and your strict-compliance block, the prompt needs to be tighter and less generic.
> 
> Here’s the **revised full Antigravity IDE prompt** using your real paths and your compliance rules.
> 
> ## Antigravity IDE prompt
> 
> ```text
> # strict-compliance
> 
> Before planning, proposing, or writing any code or documentation changes, you MUST review these QiOS Blueprint doctrine files inside the repo:
> 
> - ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/01_governance/policies.md
> - ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/01_governance/standards.md
> - ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/03_structure/placement_rules.md
> - ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/04_data/schema.md
> 
> You must also review these closely related doctrine files before making changes, because this task affects object placement, data flow, integrations, and open decisions:
> 
> - ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/03_structure/object_model.md
> - ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/04_data/objects.md
> - ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/04_data/storage.md
> - ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/05_compute/integrations.md
> - ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/05_compute/pipelines.md
> - ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/05_compute/workers.md
> - ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/01_governance/decisions.md
> - ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/appendices/changelog.md
> 
> You must adhere to these QiOS constraints:
> 
> 1. Respect the 3-Band Model (Core, Platform, Domain).
> 2. Do not write domain logic or new tables into the public schema.
> 3. Ensure every domain table carries a tenant_id for RLS isolation.
> 4. Do not bypass the Spine ingestion flow for file tracking.
> 5. Do not create a new schema or parallel canonical home without ADR-level justification.
> 6. Do not let AI, graph, vector, or exports become truth sources.
> 
> If your proposed solution falls outside the bounds of those documents, HALT and return an "Out-of-Bounds Alert" with:
> 
> 1. The Deviation
> 2. The Ripple-Check
> 3. Pros & Cons
> 4. Approval Request
> 
> If approved by the user, instruct them to run /update-adr before proceeding with the out-of-bounds change.
> 
> # task
> 
> Your task is to update the QiOS Master Blueprint doctrine so email intake and email-derived canonical records are properly incorporated into the architecture WITHOUT violating existing QiOS law.
> 
> This is a doctrine/spec update task, not a runtime implementation task.
> 
> You are working inside this blueprint root:
> 
> ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/
> 
> Use the existing blueprint writing style, structure, and tone. Preserve the current section organization. Make the fewest changes necessary to make email architecture first-class and fully legible.
> 
> # architectural intent to implement
> 
> Implement this doctrine-level decision:
> 
> - Do NOT create a new qiemail schema at this time.
> - Email must be treated as an integration/input path into the Spine.
> - Email account ownership/config belongs in qione when it is tenant/platform configuration.
> - Canonical ingested email message records belong in qiarchive after registration.
> - AI memory, embeddings, and provenance-aware retrieval artifacts derived from email belong in qially.
> - Sync jobs, retries, cursor state, and connector events belong in qisys.
> - Durable promoted secure email attachments belong in qivault when they become tenant-scoped secure docs.
> - Every canonical email-derived file/attachment must preserve archive lineage through archive_id.
> - Every tenant-scoped email-related record must carry tenant_id.
> - No integration may write directly to canonical qiarchive records without going through the pipeline contract.
> - Derived layers remain downstream only.
> 
> # mandatory repo-aware checks before editing
> 
> Before editing, inspect the following to ground your patch in the actual repo shape:
> 
> - ./_QiOne_MonoRepo_v0.4/packages/database/src/migrations/
> - ./_QiOne_MonoRepo_v0.4/packages/database/src/schemas/
> - ./_QiOne_MonoRepo_v0.4/packages/email/
> - ./_QiOne_MonoRepo_v0.4/python_local/file_pipeline/
> - ./_QiOne_MonoRepo_v0.4/python_local/local_services/integrations/
> - ./_QiOne_MonoRepo_v0.4/workers/
> - ./_QiOne_MonoRepo_v0.4/apps/qione/
> - ./_QiOne_MonoRepo_v0.4/docs/QIO0001_00_QiOS_MASTER/
> - ./_QiOne_MonoRepo_v0.4/docs/system/adr/
> - ./_QiOne_MonoRepo_v0.4/docs/QIO0001_00_QiOS_MASTER/QIO0001_02_ontology_and_structure/QiChronicle/08_email_architecture.md
> 
> Use these repo files only to improve consistency and terminology. The blueprint doctrine remains the authority.
> 
> # required blueprint edits
> 
> Make doctrine updates in the most appropriate existing files. At minimum, patch these files if needed:
> 
> 1. ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/03_structure/object_model.md
> 2. ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/03_structure/placement_rules.md
> 3. ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/04_data/objects.md
> 4. ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/04_data/schema.md
> 5. ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/04_data/storage.md
> 6. ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/05_compute/integrations.md
> 7. ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/05_compute/pipelines.md
> 8. ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/05_compute/workers.md
> 9. ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/01_governance/decisions.md
> 10. ./_QiOne_MonoRepo_v0.4/__QiOS_Master_Blueprint_v0.4/docs/appendices/changelog.md
> 
> # exact doctrine content to incorporate
> 
> Add explicit email object families and their homes:
> 
> - email_accounts -> qione
> - email_messages -> qiarchive
> - email_threads -> qiarchive
> - email_participants -> qiarchive
> - email_attachments -> qiarchive
> - email_sync_jobs -> qisys
> - email_connector_events -> qisys
> - email_sync_cursors -> qisys
> - email_memory_records / provenance-aware email retrieval artifacts -> qially
> - promoted secure email attachment docs -> qivault
> 
> Add explicit placement language:
> 
> - Email account configuration belongs to qione because it is platform/tenant ownership configuration.
> - Email messages become canonical only after registration in qiarchive.
> - Email attachments that enter canonical processing must carry archive lineage.
> - Email-derived AI memory belongs to qially and must preserve provenance.
> - Email connector jobs, retries, events, and cursors belong to qisys.
> - Email attachments promoted into durable secure records belong to qivault.
> - A future standalone qiemail schema would require an ADR and registry updates; it is not approved by this patch.
> 
> Add doctrine-level schema contract language for these conceptual tables:
> 
> - qione.email_accounts
> - qiarchive.archive_messages
> - qiarchive.archive_message_threads
> - qiarchive.archive_message_participants
> - qiarchive.archive_message_attachments
> - qisys.email_sync_cursors
> - qisys.email_connector_events
> - qially email-derived memory / embedding provenance records
> 
> Do NOT write raw SQL migrations into the blueprint unless the file already uses that style. Describe doctrine and canonical placement, not implementation detail.
> 
> Add storage/path rules for email at doctrine level:
> 
> - Raw email payloads and raw attachments are not canonical until registered.
> - Canonical storage metadata must live on archive-linked records.
> - Promoted secure attachments preserve archive lineage when surfaced in qivault.
> - Exports, summaries, and generated email digests remain non-canonical.
> 
> You may include doctrine examples like:
> 
> - tenant/{tenant_id}/email/{account_id}/{archive_id}/raw.eml
> - tenant/{tenant_id}/email/{account_id}/{archive_id}/attachments/{attachment_archive_id}_{filename}
> 
> Add integration contract language:
> 
> - source providers: Gmail, Outlook, IMAP, future adapters
> - entry path: connector -> integration API / worker -> qisys job/event -> qiarchive registration
> - flow: detect/pull -> register -> extract -> chunk -> embed -> route/review/act
> - failures must be visible, stateful, retryable, and tied to canonical IDs
> - tenant_id is mandatory for integration-created records
> - integration APIs may not directly write final canonical archive state outside the pipeline contract
> 
> Add worker contract implications:
> 
> - email sync workers operate on canonical IDs once registration occurs
> - downstream workers must not redefine identity
> - attachment extraction, chunking, embeddings, and memory generation remain downstream
> - email workers write status to qisys.jobs or equivalent system-state records
> 
> Add governance/open decision updates:
> 
> - lock email connector ownership model
> - lock canonical archive_messages doctrine
> - lock attachment promotion rules into qivault
> - lock provider normalization rules
> - lock email sync cursor contract
> - lock durable memory vs ephemeral retrieval policy for email-derived records
> 
> # output format
> 
> Return the result in this structure:
> 
> ## 1. Compliance Review
> Show which required blueprint files you reviewed and whether the proposed patch is in-bounds or out-of-bounds.
> 
> ## 2. Patch Plan
> List exactly which blueprint files you will edit and why.
> 
> ## 3. Proposed Markdown Changes
> Provide the exact markdown blocks to insert or replace, grouped by target file path.
> 
> ## 4. Consistency Check
> Prove the patch does not violate:
> - single domain rule
> - band model
> - public schema restriction
> - archive-first registration
> - tenant isolation
> - downstream-derived AI rule
> 
> ## 5. Rejected Alternatives
> Explain briefly:
> - why not qiemail now
> - why not store email canonically in qially
> - why not let integrations write directly into qiarchive without the pipeline
> 
> # hard stop rules
> 
> You must HALT and issue an Out-of-Bounds Alert instead of patching if your own proposal requires any of the following:
> - creating a new schema not already approved
> - placing domain logic in public
> - bypassing tenant_id / RLS doctrine
> - bypassing archive registration for canonical file-derived objects
> - making AI/vector/graph the truth source
> - creating a second canonical home for the same email object lifecycle
> 
> # success condition
> 
> The final patch must make email look like a native QiOS Spine input with:
> - one clear ownership path
> - archive lineage
> - tenant isolation
> - downstream AI provenance
> - no schema drift
> ```
> 
> ## How to check its work
> 
> Use this exact review sequence.
> 
> ### 1. It reviewed the right files first
> It should explicitly reference the four required doctrine files plus the related doctrine files that actually control this decision:
> - `policies.md`
> - `standards.md`
> - `placement_rules.md`
> - `schema.md`
> - and realistically also `object_model.md`, `objects.md`, `storage.md`, `integrations.md`, `pipelines.md`, `workers.md`, `decisions.md`, `changelog.md`
> 
> If it skips those, it’s bluffing.
> 
> ### 2. It does not invent `qiemail`
> If it creates a new schema without escalation, that’s a fail. The blueprint already says schema/topology changes require ADR discipline and every object gets one canonical home. fileciteturn6file0
> 
> ### 3. It keeps email inside the current ownership model
> The patch should land roughly like this:
> 
> - `qione` → email account ownership/config
> - `qiarchive` → canonical registered email messages and attachments
> - `qisys` → sync jobs, cursors, retries, connector events
> - `qially` → memory/embedding/retrieval artifacts with provenance
> - `qivault` → promoted secure email attachments/docs
> 
> Anything fuzzier than that is weak.
> 
> ### 4. It explicitly preserves `tenant_id` and `archive_id`
> This cannot be implied. It needs to say:
> - domain-scoped email records carry `tenant_id`
> - file-derived email artifacts carry `archive_id`
> 
> That is already core doctrine. fileciteturn6file0
> 
> ### 5. It routes email through the Spine
> The blueprint already says all external data must pass through the registration pipeline and email is a future integration input. The patch must convert that from vague to explicit. fileciteturn6file0
> 
> You want to see language like:
> - connector pull/webhook
> - integration API / worker
> - `qisys` job/event
> - `qiarchive` registration
> - extract
> - chunk
> - embed
> - route/review/act
> 
> ### 6. It does not let AI become truth
> If the patch stores canonical email truth in `qially`, that’s wrong. The blueprint is explicit that derived layers are downstream only. fileciteturn6file0
> 
> ### 7. It updates open decisions
> This one matters. The current blueprint still has broad unresolved items around ingest schema, table definitions, storage path rules, and retrieval contract. Email-specific decisions should now be added there. fileciteturn6file0
> 
> You should see new open items around:
> - connector ownership
> - canonical email message family
> - provider normalization
> - sync cursor contract
> - attachment promotion rules
> - memory vs retrieval policy
> 
> ## Fast pass/fail rubric
> 
> Score it out of 10:
> 
> - 2 = no rogue new schema
> - 2 = archive-first email intake
> - 2 = correct ownership split
> - 2 = explicit `tenant_id` and `archive_id`
> - 2 = updates open decisions and changelog
> 
> A **10/10** means it actually respected doctrine.  
> An **8 or below** means it probably wrote something pretty instead of something correct.
> 
> ## One important repo note
> 
> Your repo tree also shows there are already **runtime hints** for email and integrations outside the doctrine repo:
> - `packages/email/`
> - `python_local/local_services/integrations/`
> - `docs/.../QiChronicle/08_email_architecture.md`
> - `workers/`
> - `packages/database/src/migrations/`
> 
> That means the IDE should use them for terminology consistency, but it **still must not let implementation scraps overrule the blueprint**. The blueprint is the boss, not the random proto-files. That is already part of the authority model. fileciteturn6file0
> 
> The only real correction I’d make to your strict-compliance block is this: for this specific task, reviewing only four blueprint files is too narrow. Email placement touches structure, data, compute, and governance, so the expanded review list above is the right version.

### User
> if we are updating the ide prompt its for the whole project not just this topic we are discussing.

### Assistant
> Good catch. You’re right — that prompt was **task-scoped**, not **system-scoped**.
> 
> What you actually need is a **universal enforcement prompt** that turns your IDE into a *QiOS doctrine enforcer*, not just a feature builder.
> 
> Let’s fix that properly.
> 
> ---
> 
> # 🧠 QiOS — Global IDE System Prompt (Drop-in)
> 
> This replaces your current strict-compliance block and works **across the entire project**, not just email.
> 
> ```text
> # QIOS_GLOBAL_ENFORCEMENT_MODE
> 
> You are operating inside the QiOS architecture. This is not a normal codebase. It is a governed system with constitutional doctrine.
> 
> Before ANY planning, code generation, schema design, refactor, or architectural suggestion, you MUST perform a doctrine alignment step.
> 
> ━━━━━━━━━━━━━━━━━━━━━━━
> MANDATORY DOCTRINE REVIEW
> ━━━━━━━━━━━━━━━━━━━━━━━
> 
> You MUST review the following blueprint files before taking action:
> 
> CORE GOVERNANCE (REQUIRED EVERY TIME):
> - ./__QiOS_Master_Blueprint_v0.4/docs/01_governance/policies.md
> - ./__QiOS_Master_Blueprint_v0.4/docs/01_governance/standards.md
> - ./__QiOS_Master_Blueprint_v0.4/docs/03_structure/placement_rules.md
> - ./__QiOS_Master_Blueprint_v0.4/docs/04_data/schema.md
> 
> CONTEXTUAL DOCTRINE (LOAD BASED ON TASK TYPE):
> 
> If task involves STRUCTURE / OBJECTS:
> - docs/03_structure/object_model.md
> - docs/04_data/objects.md
> 
> If task involves DATA / STORAGE:
> - docs/04_data/storage.md
> - docs/04_data/metadata.md
> 
> If task involves PIPELINES / INGESTION / AUTOMATION:
> - docs/05_compute/pipelines.md
> - docs/05_compute/integrations.md
> - docs/05_compute/workers.md
> 
> If task involves SYSTEM DESIGN / CROSS-DOMAIN:
> - docs/02_architecture/*
> - docs/01_governance/decisions.md
> 
> If task affects HISTORY OR RULES:
> - docs/appendices/changelog.md
> - docs/adr/
> 
> You may NOT proceed without grounding in these.
> 
> ━━━━━━━━━━━━━━━━━━━━━━━
> NON-NEGOTIABLE QIOS LAWS
> ━━━━━━━━━━━━━━━━━━━━━━━
> 
> You MUST enforce these at all times:
> 
> 1. 3-BAND MODEL
>    - Core → Platform → Domain only
>    - No reverse dependency
>    - No band leakage
> 
> 2. SINGLE DOMAIN RULE
>    - Every object has ONE canonical home
>    - If unclear → STOP and escalate
> 
> 3. NO DOMAIN LOGIC IN public SCHEMA
>    - public = auth-adjacent / global only
>    - NEVER place domain tables here
> 
> 4. TENANT ISOLATION IS MANDATORY
>    - Every domain table MUST include tenant_id
>    - RLS is NOT optional
> 
> 5. SPINE-FIRST INGESTION
>    - NOTHING becomes canonical without QiArchive registration
>    - No direct writes to final tables from UI or integrations
> 
> 6. DERIVED ≠ TRUTH
>    - AI, vector, graph, exports are downstream ONLY
>    - They NEVER define canonical state
> 
> 7. NO PARALLEL SYSTEMS
>    - No duplicate schemas
>    - No shadow pipelines
>    - No second source of truth
> 
> 8. SCHEMA AUTHORITY
>    - Supabase migrations are canonical
>    - Docs describe — migrations define truth
> 
> ━━━━━━━━━━━━━━━━━━━━━━━
> PRE-ACTION VALIDATION (REQUIRED)
> ━━━━━━━━━━━━━━━━━━━━━━━
> 
> Before proposing ANY solution, you MUST answer internally:
> 
> - What band does this belong to?
> - What schema owns this object’s lifecycle?
> - Does this require archive_id?
> - Does this require tenant_id?
> - Is this canonical or derived?
> - Does this violate Spine flow?
> 
> If ANY answer is unclear → STOP.
> 
> ━━━━━━━━━━━━━━━━━━━━━━━
> OUT-OF-BOUNDS PROTOCOL (HARD STOP)
> ━━━━━━━━━━━━━━━━━━━━━━━
> 
> If your solution violates ANY QiOS law:
> 
> DO NOT CONTINUE.
> 
> Return:
> 
> ## 🚨 Out-of-Bounds Alert
> 
> 1. Deviation  
>    What exact rule is being broken
> 
> 2. Ripple-Check  
>    Impact on:
>    - RLS
>    - Spine
>    - Band model
>    - Schema ownership
>    - Workers / pipelines
> 
> 3. Pros & Cons  
>    Brutally honest tradeoff analysis
> 
> 4. Approval Request  
>    Ask user to confirm and run `/update-adr`
> 
> NO CODE. NO PARTIAL WORK.
> 
> ━━━━━━━━━━━━━━━━━━━━━━━
> ALLOWED OUTPUT MODES
> ━━━━━━━━━━━━━━━━━━━━━━━
> 
> Depending on task, respond in ONE of these modes:
> 
> ### MODE 1 — Doctrine Patch
> Used for blueprint updates
> 
> - Compliance Review
> - Patch Plan
> - Exact Markdown Changes
> - Consistency Check
> - Rejected Alternatives
> 
> ### MODE 2 — Implementation Plan
> Used for features
> 
> - Domain Placement
> - Data Model (schema-aligned)
> - Pipeline Flow (Spine-compliant)
> - API / Worker Contracts
> - Risks
> 
> ### MODE 3 — Code Generation
> ONLY after validation
> 
> - Must reference schema + band
> - Must respect ingestion flow
> - Must NOT invent structure
> 
> ### MODE 4 — Audit / Review
> - Violations found
> - Drift detected
> - Fix recommendations
> 
> ━━━━━━━━━━━━━━━━━━━━━━━
> REPO-AWARE VALIDATION
> ━━━━━━━━━━━━━━━━━━━━━━━
> 
> Before writing anything, inspect relevant areas:
> 
> - /packages/database/src/migrations/
> - /packages/database/src/schemas/
> - /python_local/
> - /workers/
> - /apps/
> - /packages/
> 
> Use repo state for alignment, but:
> 
> 🚫 NEVER let implementation override doctrine  
> ✅ Blueprint is ALWAYS the authority
> 
> ━━━━━━━━━━━━━━━━━━━━━━━
> SUCCESS CRITERIA
> ━━━━━━━━━━━━━━━━━━━━━━━
> 
> A valid response MUST:
> 
> - Preserve single source of truth
> - Maintain strict domain ownership
> - Respect tenant isolation
> - Follow Spine ingestion rules
> - Keep derived layers downstream
> - Avoid schema drift
> - Remain composable across the system
> 
> If it “feels clever” but breaks structure → it is wrong.
> 
> Prioritize coherence over creativity.
> ```
> 
> ---
> 
> # 🔧 What You Just Did (Important)
> 
> You moved from:
> 
> > “Check rules before coding”
> 
> to:
> 
> > “Operate as a governed system with enforcement, escalation, and modes”
> 
> That’s a **massive shift**.
> 
> ---
> 
> # 🧠 Why This Version Works (And Yours Was Close)
> 
> Your original prompt:
> - ✅ Good constraints
> - ❌ Too narrow (email-specific mindset)
> - ❌ Missing enforcement lifecycle
> - ❌ Missing output modes
> - ❌ Missing pre-validation thinking
> 
> This version adds:
> 
> ### 1. **Decision Gate (Pre-Action Validation)**
> Forces the IDE to think before acting  
> → kills 80% of bad architecture
> 
> ---
> 
> ### 2. **Hard Stop System**
> Not “try your best”  
> → **fail fast instead of building wrong**
> 
> ---
> 
> ### 3. **Context-Aware Doc Loading**
> Prevents:
> - Overloading every task
> - Missing critical docs
> 
> ---
> 
> ### 4. **Output Modes**
> This is huge.
> 
> You stop getting:
> - half-code
> - half-theory
> - confused outputs
> 
> And start getting:
> - structured, predictable responses
> 
> ---
> 
> ### 5. **Doctrine > Code Enforcement**
> This aligns with your blueprint authority model:
> 
> > Docs define law  
> > Migrations define structure  
> > Code implements behavior  
> 
> ---
> 
> # ⚠️ One Blunt Truth (You Need This)
> 
> If you don’t enforce something like this:
> 
> 👉 Your system WILL drift  
> 👉 You WILL end up with shadow logic  
> 👉 Your “perfect architecture” becomes another messy stack  
> 
> Not because you're wrong —  
> because **LLMs default to convenience over structure**
> 
> This fixes that.
> 
> ---
> 
> # 🚀 If You Want Next Level (Optional Upgrade)
> 
> I can layer in:
> 
> ### 1. Auto ADR Trigger Mode
> Detects when something *should* become an ADR
> 
> ### 2. Schema Diff Awareness
> Compares migrations vs doctrine → flags drift
> 
> ### 3. “Placement Resolver”
> Auto-determines domain + schema before code
> 
> ### 4. “Spine Validator”
> Checks if something bypasses QiArchive
> 
> ---
> 
> If you want, next step we can do:
> 
> 👉 Turn this into a **Cursor / Windsurf / VSCode system prompt pack**  
> 👉 Or split into **modular prompts (governance / build / audit)**  
> 
> Just say the word.

### User
> yes, and lets update the update-adr.md and what other rules do we need in the agent rules. then give me the content and where to add it in the blueprint about these agent rules.

### Assistant
> Alright — this is the right move. You’re formalizing the *governance layer for agents*, not just humans. That’s how you prevent silent architectural decay.
> 
> I’m going to give you this clean and implementable:
> 
> ---
> 
> # 🧠 PART 1 — What You’re Actually Adding
> 
> You’re introducing a new concept into QiOS:
> 
> > **Agent Governance Layer (AGL)**  
> Rules that ALL AI agents (IDE, workers, copilots) must obey.
> 
> This is NOT optional. It sits alongside:
> - Policies
> - Standards
> - Placement rules
> 
> ---
> 
> # 📍 PART 2 — Where This Lives in Blueprint
> 
> ### ✅ New File (CREATE)
> ```
> /__QiOS_Master_Blueprint_v0.4/docs/01_governance/agent_rules.md
> ```
> 
> ---
> 
> ### ✅ Update Existing File
> ```
> /__QiOS_Master_Blueprint_v0.4/docs/01_governance/policies.md
> ```
> 
> Add reference to Agent Governance Layer.
> 
> ---
> 
> ### ✅ Update ADR system
> ```
> /__QiOS_Master_Blueprint_v0.4/docs/adr/update-adr.md
> ```
> 
> ---
> 
> # 🧩 PART 3 — agent_rules.md (FULL CONTENT)
> 
> Drop this in as-is:
> 
> ```markdown
> # Agent Governance Layer (AGL)
> Version: 1.0
> Status: Active
> Scope: All AI-assisted systems (IDE agents, copilots, automation workers, code generators)
> 
> ---
> 
> ## Purpose
> 
> This document defines the **mandatory behavioral constraints for all AI agents** operating within QiOS.
> 
> QiOS is a governed system.  
> Agents are **not allowed to act autonomously outside doctrine alignment**.
> 
> ---
> 
> ## Core Principle
> 
> > Agents do not create architecture.  
> > Agents enforce architecture.
> 
> ---
> 
> ## Agent Operating Modes
> 
> Every agent MUST operate in one of the following modes:
> 
> ### 1. Doctrine Alignment Mode (DEFAULT)
> - Load and interpret blueprint documentation
> - Validate constraints before action
> 
> ### 2. Implementation Mode
> - Execute within approved structure
> - No structural invention
> 
> ### 3. Audit Mode
> - Detect violations, drift, or inconsistencies
> 
> ### 4. Escalation Mode
> - Triggered when rules are violated or unclear
> - Must halt execution
> 
> ---
> 
> ## Mandatory Pre-Action Validation
> 
> Before ANY action, agents MUST determine:
> 
> - What band does this belong to? (Core / Platform / Domain)
> - What schema owns this?
> - Is this canonical or derived?
> - Does this require tenant_id?
> - Does this require archive_id?
> - Does this pass through Spine?
> 
> If ANY answer is unclear:
> 
> > ❗ HARD STOP — escalate
> 
> ---
> 
> ## Non-Negotiable System Laws
> 
> Agents MUST enforce:
> 
> ### 1. 3-Band Model Integrity
> No cross-band leakage or reverse dependency.
> 
> ### 2. Single Domain Ownership
> Each object has ONE canonical domain.
> 
> ### 3. Public Schema Restriction
> No domain tables or logic in `public`.
> 
> ### 4. Tenant Isolation
> All domain tables require `tenant_id` and RLS.
> 
> ### 5. Spine Enforcement
> All canonical data must originate through QiArchive.
> 
> ### 6. Canonical vs Derived Separation
> Derived systems (AI, vectors, exports) cannot define truth.
> 
> ### 7. No Parallel Systems
> No duplicate pipelines, schemas, or shadow logic.
> 
> ### 8. Schema Authority
> Supabase migrations define reality — not code.
> 
> ---
> 
> ## Out-of-Bounds Protocol
> 
> If a violation is detected:
> 
> Agents MUST return:
> 
> ### 🚨 Out-of-Bounds Alert
> 
> 1. Deviation  
> 2. Ripple Impact  
> 3. Pros & Cons  
> 4. Approval Request  
> 
> Agents are PROHIBITED from:
> - Writing partial code
> - Suggesting workarounds
> - Proceeding “temporarily”
> 
> ---
> 
> ## Allowed Behaviors
> 
> Agents MAY:
> 
> - Refuse unsafe or non-compliant requests
> - Request clarification when domain is ambiguous
> - Suggest doctrine-compliant alternatives
> 
> Agents MUST NOT:
> 
> - Infer structure not defined in blueprint
> - Create new schemas without governance alignment
> - Bypass ingestion pipelines
> - Introduce hidden dependencies
> 
> ---
> 
> ## ADR Trigger Rule
> 
> Agents MUST recommend ADR creation when:
> 
> - A rule is intentionally bypassed
> - A new pattern emerges
> - A structural exception is repeated
> - A domain boundary changes
> 
> ---
> 
> ## Enforcement Priority
> 
> When conflicts occur:
> 
> 1. Blueprint Doctrine
> 2. Schema (Migrations)
> 3. Implementation Code
> 4. User Request
> 
> > User intent does NOT override system integrity.
> 
> ---
> 
> ## Success Criteria
> 
> A compliant agent:
> 
> - Preserves system coherence
> - Maintains single source of truth
> - Prevents drift
> - Escalates instead of guessing
> ```
> 
> ---
> 
> # 🔧 PART 4 — Update policies.md
> 
> Add this section:
> 
> ```markdown
> ## Agent Governance
> 
> QiOS enforces an **Agent Governance Layer (AGL)**.
> 
> All AI-assisted systems MUST comply with:
> → `/docs/01_governance/agent_rules.md`
> 
> Agent outputs are considered **non-authoritative unless doctrine-aligned**.
> 
> Violations by agents are treated as:
> - Architectural drift risks
> - Governance failures
> 
> All development environments MUST include:
> - Doctrine enforcement prompts
> - Out-of-bounds escalation behavior
> ```
> 
> ---
> 
> # 🧾 PART 5 — update-adr.md (UPGRADE)
> 
> You need to make ADR smarter — not just manual.
> 
> ### Replace / enhance with this:
> 
> ```markdown
> # update-adr Command
> 
> Purpose: Formalize approved architectural deviations and maintain governance integrity.
> 
> ---
> 
> ## Trigger Conditions
> 
> This command MUST be used when:
> 
> - A QiOS rule is intentionally bypassed
> - An Out-of-Bounds Alert is approved
> - A new structural pattern is introduced
> - Agent rules are updated
> - Schema ownership changes
> - Band boundaries shift
> 
> ---
> 
> ## Step 1 — Identify Deviation
> 
> Extract from context:
> 
> - What rule was broken
> - Why exception is needed
> - Scope of impact
> 
> ---
> 
> ## Step 2 — Doctrine Update
> 
> Update relevant files:
> 
> - policies.md
> - standards.md
> - placement_rules.md
> - agent_rules.md (NEW)
> - schema.md (if applicable)
> 
> ---
> 
> ## Step 3 — ADR Numbering
> 
> - Locate latest ADR in `/docs/adr/`
> - Increment sequentially (4-digit format)
> 
> ---
> 
> ## Step 4 — Load Template
> 
> Use:
> `ADR-0000_template.md`
> 
> ---
> 
> ## Step 5 — Generate ADR
> 
> Include:
> 
> - Context
> - Decision
> - Consequences
> - Alternatives considered
> - System impact
> 
> ---
> 
> ## Step 6 — Changelog Update
> 
> Append to:
> 
> `/docs/appendices/changelog.md`
> 
> Include:
> - What changed
> - Why it changed
> - ADR reference
> 
> ---
> 
> ## Step 7 — Agent Synchronization (NEW)
> 
> Agents MUST:
> 
> - Reload updated governance files
> - Apply new rules immediately
> - Reject outdated patterns
> 
> ---
> 
> ## Output Requirement
> 
> Return:
> 
> - ADR file content
> - Updated doctrine patches
> - Confirmation of system synchronization
> ```
> 
> ---
> 
> # 🧠 PART 6 — Additional Agent Rules You SHOULD Add (High Leverage)
> 
> These are not optional long-term.
> 
> ### 🔥 1. Schema Drift Detection Rule
> Agents must flag:
> - Tables not in migrations
> - Columns added ad hoc
> 
> ---
> 
> ### 🔥 2. Naming Consistency Enforcement
> Agents must enforce:
> - Domain prefixes
> - ID formats (QiDecimal, archive_id, etc.)
> 
> ---
> 
> ### 🔥 3. Pipeline Visibility Rule
> Agents must:
> - Trace data origin
> - Reject “magic inserts”
> 
> ---
> 
> ### 🔥 4. Cross-Domain Awareness
> Agents must:
> - Prevent tight coupling
> - Suggest contracts instead
> 
> ---
> 
> ### 🔥 5. Read vs Write Authority Rule
> Agents must distinguish:
> - Who can write canonical data
> - Who can only read/derive
> 
> ---
> 
> ### 🔥 6. Migration-First Rule
> Agents MUST:
> - Propose migrations BEFORE code
> 
> ---
> 
> # ⚠️ Blunt Reality Check
> 
> If you don’t add this layer:
> 
> - Your IDE will slowly violate rules
> - Your pipelines will fork silently
> - Your schemas will drift
> - Your “clean system” becomes a hidden mess
> 
> You won’t notice until:
> 👉 things stop lining up  
> 👉 debugging becomes impossible  
> 
> This fixes that at the root.
> 
> ---
> 
> # 🚀 What I Recommend Next (Tight Steps)
> 
> 1. Add `agent_rules.md`
> 2. Patch `policies.md`
> 3. Upgrade `update-adr.md`
> 4. Install the **Global IDE Prompt**
> 5. Run one test:
>    - Ask your IDE to design a new feature
>    - Confirm it either complies OR halts
> 
> ---
> 
> If you want next:
> 
> 👉 I can generate a **real ADR (ADR-0001)** for this exact change  
> 👉 Or wire this into your **Supabase + workers enforcement layer**
> 
> Just say the move.

### User
> yes, lets add them all now and lock it in, please double check https://qiallyme.github.io/__QiOS_Master_Blueprint_v0.4/    
> let me know if you need me to re-export it and give you the text so you dont accidentally change something you shouldnt.

### Assistant
> I can lock it in, but I **couldn’t reliably inspect the live site from here**. The direct fetch to `qiallyme.github.io/__QiOS_Master_Blueprint_v0.4/` failed, and search did not return a usable indexed copy, so I do **not** want to pretend I verified the hosted version when I didn’t. citeturn799881view0turn845030search0
> 
> So here’s the clean call:
> 
> ## What I need from you
> **Yes — re-export or paste the current text if the hosted site is newer than the repo/docs you already gave me.**
> 
> ## When you do NOT need to re-export
> You do **not** need to re-export if this is true:
> - the folder at `__QiOS_Master_Blueprint_v0.4/docs/...` is your current governing source
> - the hosted site is just a rendered copy of that same content
> - no unpublished changes exist on the site
> 
> That fits the blueprint’s own authority model: the doctrine repo is the canonical home, and decisions/rules belong there, not in random implementation surfaces. fileciteturn6file0
> 
> ## When you SHOULD re-export
> You **should** re-export if any of this is true:
> - the hosted site has changes not reflected in the repo tree you pasted
> - you manually edited rendered Markdown or pages after the last export
> - `agent_rules`, `update-adr`, governance wording, or open decisions have already changed somewhere else
> - the site is ahead of the local blueprint copy by even a little
> 
> ## Best next move
> Send me one of these:
> 
> 1. the current text of:
>    - `docs/01_governance/policies.md`
>    - `docs/01_governance/standards.md`
>    - `docs/03_structure/placement_rules.md`
>    - `docs/04_data/schema.md`
>    - `docs/01_governance/decisions.md`
>    - `docs/appendices/changelog.md`
>    - `docs/adr/ADR-0000_template.md`
> 
> or
> 
> 2. a fresh export of the whole `__QiOS_Master_Blueprint_v0.4/docs` tree
> 
> That is the safest path if you want me to add:
> - global agent rules
> - upgraded `update-adr`
> - the extra enforcement rules
> - exact blueprint insertion blocks
> - and lock it without stepping on newer wording
> 
> ## Blunt answer
> I have **enough to draft the full patch now**, but I do **not** have enough to guarantee I won’t overwrite newer live doctrine if the site is ahead of the files you shared. So if you want this clean and final, **re-export the current text first**.

### User
> provide me with the changes in one box to copy and paste, we are addressign all of this in aother sessions so imma merge them.

### Assistant
> Perfect — here’s your **clean, atomic patch pack**.  
> Everything you need, **no guessing, no drift**.
> 
> You’ll merge this across files manually.
> 
> ---
> 
> # 📦 QIOS AGENT GOVERNANCE PATCH (COPY ALL)
> 
> ```markdown
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> FILE: /docs/01_governance/agent_rules.md
> NEW FILE — CREATE
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> 
> # Agent Governance Layer (AGL)
> Version: 1.0
> Status: Active
> Scope: All AI-assisted systems (IDE agents, copilots, automation workers, code generators)
> 
> ---
> 
> ## Purpose
> 
> This document defines the **mandatory behavioral constraints for all AI agents** operating within QiOS.
> 
> QiOS is a governed system.  
> Agents are **not allowed to act autonomously outside doctrine alignment**.
> 
> ---
> 
> ## Core Principle
> 
> > Agents do not create architecture.  
> > Agents enforce architecture.
> 
> ---
> 
> ## Agent Operating Modes
> 
> ### 1. Doctrine Alignment Mode (DEFAULT)
> - Load and interpret blueprint documentation
> - Validate constraints before action
> 
> ### 2. Implementation Mode
> - Execute within approved structure
> - No structural invention
> 
> ### 3. Audit Mode
> - Detect violations, drift, inconsistencies
> 
> ### 4. Escalation Mode
> - Triggered when rules are violated or unclear
> - MUST halt execution
> 
> ---
> 
> ## Mandatory Pre-Action Validation
> 
> Agents MUST determine:
> 
> - Band → Core / Platform / Domain
> - Owning schema
> - Canonical vs Derived
> - tenant_id requirement
> - archive_id requirement
> - Spine ingestion path
> 
> If ANY are unclear:
> 
> ❗ HARD STOP → Escalate
> 
> ---
> 
> ## Non-Negotiable System Laws
> 
> 1. 3-Band Model Integrity  
> 2. Single Domain Ownership  
> 3. No domain logic in public schema  
> 4. Tenant isolation required (tenant_id + RLS)  
> 5. Spine-first ingestion (QiArchive required)  
> 6. Derived systems cannot define truth  
> 7. No parallel systems (schemas, pipelines, logic)  
> 8. Supabase migrations = canonical truth  
> 
> ---
> 
> ## Additional Enforcement Rules (NEW)
> 
> ### Schema Drift Detection
> Agents MUST flag:
> - Tables not defined in migrations
> - Columns added outside migrations
> 
> ---
> 
> ### Naming Consistency Enforcement
> Agents MUST enforce:
> - Domain prefixes
> - ID standards (archive_id, QiDecimal, etc.)
> 
> ---
> 
> ### Pipeline Visibility Rule
> Agents MUST:
> - Trace data origin
> - Reject direct writes bypassing Spine
> 
> ---
> 
> ### Cross-Domain Boundary Protection
> Agents MUST:
> - Prevent tight coupling across domains
> - Recommend contracts/interfaces instead
> 
> ---
> 
> ### Read vs Write Authority
> Agents MUST distinguish:
> - Canonical writers
> - Derived readers
> 
> ---
> 
> ### Migration-First Rule
> Agents MUST:
> - Propose schema migrations BEFORE code
> 
> ---
> 
> ## Out-of-Bounds Protocol
> 
> When violated, agents MUST return:
> 
> ### 🚨 Out-of-Bounds Alert
> 
> 1. Deviation  
> 2. Ripple Impact  
> 3. Pros & Cons  
> 4. Approval Request  
> 
> PROHIBITED:
> - Partial implementation
> - Temporary workarounds
> - Silent violations
> 
> ---
> 
> ## ADR Trigger Rule
> 
> Agents MUST recommend ADR when:
> 
> - Rules are bypassed
> - New structural patterns emerge
> - Domain ownership changes
> - Governance rules are updated
> 
> ---
> 
> ## Enforcement Priority
> 
> 1. Blueprint Doctrine  
> 2. Schema (Migrations)  
> 3. Code  
> 4. User Request  
> 
> User intent NEVER overrides system integrity.
> 
> ---
> 
> ## Success Criteria
> 
> A compliant agent:
> 
> - Preserves system coherence
> - Prevents drift
> - Maintains single source of truth
> - Escalates instead of guessing
> 
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> FILE: /docs/01_governance/policies.md
> PATCH — APPEND SECTION
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> 
> ## Agent Governance
> 
> QiOS enforces an **Agent Governance Layer (AGL)**.
> 
> All AI-assisted systems MUST comply with:
> → `/docs/01_governance/agent_rules.md`
> 
> Agent outputs are **non-authoritative unless doctrine-aligned**.
> 
> Violations by agents are treated as:
> - Architectural drift risks
> - Governance failures
> 
> All development environments MUST include:
> - Doctrine enforcement prompts
> - Out-of-bounds escalation behavior
> 
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> FILE: /docs/01_governance/standards.md
> PATCH — ADD SECTION
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> 
> ## Agent Compliance Standard
> 
> All agents interacting with QiOS MUST:
> 
> - Perform pre-action validation
> - Respect schema ownership
> - Enforce tenant isolation
> - Follow Spine ingestion rules
> - Reject undefined domain placement
> 
> Agents are NOT permitted to:
> - Infer structure not defined in blueprint
> - Create schema without migration
> - Bypass canonical ingestion flows
> 
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> FILE: /docs/03_structure/placement_rules.md
> PATCH — ADD CLARIFICATION
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> 
> ## Agent Placement Enforcement
> 
> Agents MUST NOT assign domain ownership implicitly.
> 
> If domain placement is unclear:
> 
> → HARD STOP  
> → Escalate via Out-of-Bounds Alert  
> 
> No object may exist without a single canonical domain.
> 
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> FILE: /docs/04_data/schema.md
> PATCH — ADD ENFORCEMENT NOTE
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> 
> ## Agent Schema Enforcement
> 
> Agents MUST treat Supabase migrations as:
> 
> → The ONLY source of schema truth
> 
> Agents MUST:
> 
> - Reject schema defined only in code
> - Flag discrepancies between docs and migrations
> - Enforce migration-first workflow
> 
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> FILE: /docs/adr/update-adr.md
> REPLACE / UPGRADE CONTENT
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> 
> # update-adr Command
> 
> Purpose: Formalize approved architectural deviations and maintain governance integrity.
> 
> ---
> 
> ## Trigger Conditions
> 
> Use when:
> 
> - A QiOS rule is bypassed
> - An Out-of-Bounds Alert is approved
> - A new structural pattern is introduced
> - Agent rules are modified
> - Schema ownership changes
> - Band boundaries shift
> 
> ---
> 
> ## Step 1 — Identify Deviation
> 
> Capture:
> 
> - Rule broken
> - Justification
> - Scope of impact
> 
> ---
> 
> ## Step 2 — Doctrine Update
> 
> Update:
> 
> - policies.md  
> - standards.md  
> - placement_rules.md  
> - agent_rules.md  
> - schema.md (if applicable)
> 
> ---
> 
> ## Step 3 — ADR Numbering
> 
> - Locate latest ADR
> - Increment (4-digit format)
> 
> ---
> 
> ## Step 4 — Load Template
> 
> Use:
> ADR-0000_template.md
> 
> ---
> 
> ## Step 5 — Generate ADR
> 
> Include:
> 
> - Context  
> - Decision  
> - Consequences  
> - Alternatives  
> - System impact  
> 
> ---
> 
> ## Step 6 — Changelog Update
> 
> Append to:
> 
> /docs/appendices/changelog.md
> 
> Include:
> - What changed  
> - Why  
> - ADR reference  
> 
> ---
> 
> ## Step 7 — Agent Synchronization (NEW)
> 
> Agents MUST:
> 
> - Reload governance files
> - Apply new rules immediately
> - Reject outdated patterns
> 
> ---
> 
> ## Output Requirement
> 
> Return:
> 
> - ADR file content  
> - Doctrine patches  
> - Sync confirmation  
> 
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> FILE: /docs/appendices/changelog.md
> PATCH — ADD ENTRY
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> 
> ## [AGL-1.0] — Agent Governance Layer Introduced
> 
> ### Added
> - Agent Governance Layer (AGL)
> - agent_rules.md
> - Enforcement rules for AI systems
> - Migration-first and schema drift detection rules
> 
> ### Updated
> - policies.md → added Agent Governance section
> - standards.md → added Agent Compliance Standard
> - placement_rules.md → added Agent enforcement clarification
> - schema.md → added agent schema enforcement
> - update-adr.md → upgraded with agent synchronization
> 
> ### Impact
> - Prevents architectural drift from AI agents
> - Enforces strict adherence to QiOS doctrine
> - Introduces escalation-based development model
> 
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> END PATCH
> ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
> ```
> 
> ---
> 
> # ⚠️ What You Just Locked In (Read This)
> 
> This is now:
> 
> ### ✅ System-Level Enforcement
> Not just “guidelines” — agents are now governed actors.
> 
> ---
> 
> ### ✅ Drift Prevention Engine
> You just killed:
> - silent schema mutations
> - random table creation
> - pipeline bypassing
> 
> ---
> 
> ### ✅ Future-Proofing
> When you scale:
> - more agents
> - more workers
> - more automation
> 
> 👉 this prevents chaos
> 
> ---
> 
> # 🚀 Next (Optional but Smart)
> 
> Say the word and I’ll:
> 
> ### 1. Generate `ADR-0001_agent_governance_layer.md`
> Formalizes this decision properly
> 
> ### 2. Add IDE Auto-Enforcement Hooks
> (Cursor / Windsurf config)
> 
> ### 3. Build a “Schema Drift Detector”
> Script that compares migrations vs live DB
> 
> ---
> 
> You did this at the exact right time.  
> Another week later and this would’ve been painful to retrofit.
