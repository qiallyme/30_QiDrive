---
layout: page
title: "Double Entry Accounting Schema"
slug: "double_entry_accounting_schema"
created_at: "2026-06-21 03:56:37"
updated_at: "2026-06-21 03:56:37"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-009.json"
template_key: master-template
date: 2026-06-21
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a37a714-6a8c-83ea-b9b7-903ab253bafb"
canonical_ref: ""
---

# Double Entry Accounting Schema

## Overview
- **Date**: 2026-06-21 03:56:37
- **Conversation ID**: `6a37a714-6a8c-83ea-b9b7-903ab253bafb`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> for a legit double entry accounting database that works well with many different types of exports what tables do i need, and the columsn, give me the sql, the schema is there just no tables or anything else the schema is qifinance.

### Assistant
> This is one of those places where the clean move is **not** to make every export fit your ledger directly. We’ll use a three-layer design: raw import rows → normalized imported transactions → real double-entry journal.

### Assistant
> The key truth: **bank/CSV exports are not accounting.** They’re evidence. Your actual accounting database should protect the ledger from messy Venmo/CSV/bank/PayPal/Stripe weirdness.

### Assistant
> Assuming this is **Supabase/Postgres**, here is the clean base.
> 
> The core idea:
> 
> **Exports are intake. Journal entries are truth.**
> 
> You need these layers:
> 
> | Layer | Tables |
> |---|---|
> | Books / setup | `books`, `accounts`, `counterparties`, `financial_institutions`, `external_accounts` |
> | Import pipeline | `import_profiles`, `import_files`, `raw_import_rows`, `imported_transactions` |
> | Double-entry ledger | `journal_entries`, `journal_lines`, `journal_source_links` |
> | Cleanup / automation | `posting_rules`, `tags`, `journal_entry_tags` |
> | Reconciliation | `reconciliation_sessions`, `reconciliation_items` |
> | Evidence | `documents`, `document_links` |
> | Reporting | views for balances, trial balance, unposted imports |
> 
> Here’s the migration.
> 
> ```sql
> -- =========================================================
> -- QiFinance Core Double-Entry Accounting Schema
> -- Target: Supabase / PostgreSQL
> -- Schema: qifinance
> -- =========================================================
> 
> create extension if not exists pgcrypto;
> 
> create schema if not exists qifinance;
> 
> -- ---------------------------------------------------------
> -- Enums
> -- ---------------------------------------------------------
> 
> do $$
> begin
>   create type qifinance.account_type as enum (
>     'asset',
>     'liability',
>     'equity',
>     'income',
>     'expense'
>   );
> exception when duplicate_object then null;
> end $$;
> 
> do $$
> begin
>   create type qifinance.normal_balance as enum (
>     'debit',
>     'credit'
>   );
> exception when duplicate_object then null;
> end $$;
> 
> do $$
> begin
>   create type qifinance.journal_status as enum (
>     'draft',
>     'posted',
>     'locked',
>     'void'
>   );
> exception when duplicate_object then null;
> end $$;
> 
> do $$
> begin
>   create type qifinance.import_tx_status as enum (
>     'new',
>     'reviewed',
>     'posted',
>     'ignored',
>     'duplicate',
>     'error'
>   );
> exception when duplicate_object then null;
> end $$;
> 
> do $$
> begin
>   create type qifinance.reconciliation_status as enum (
>     'open',
>     'reconciled',
>     'locked',
>     'void'
>   );
> exception when duplicate_object then null;
> end $$;
> 
> -- ---------------------------------------------------------
> -- Utility
> -- ---------------------------------------------------------
> 
> create or replace function qifinance.touch_updated_at()
> returns trigger
> language plpgsql
> as $$
> begin
>   new.updated_at = now();
>   return new;
> end;
> $$;
> 
> -- ---------------------------------------------------------
> -- Books
> -- One book = one accounting universe.
> -- Could be personal finances, business, project, estate, etc.
> -- ---------------------------------------------------------
> 
> create table if not exists qifinance.books (
>   id uuid primary key default gen_random_uuid(),
> 
>   name text not null,
>   legal_name text,
>   owner_user_id uuid,
> 
>   base_currency char(3) not null default 'USD',
>   timezone text not null default 'America/Chicago',
> 
>   start_date date,
>   end_date date,
> 
>   metadata jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now(),
> 
>   unique (name)
> );
> 
> drop trigger if exists books_touch_updated_at on qifinance.books;
> 
> create trigger books_touch_updated_at
> before update on qifinance.books
> for each row
> execute function qifinance.touch_updated_at();
> 
> -- ---------------------------------------------------------
> -- Chart of Accounts
> -- This is the real accounting structure.
> -- ---------------------------------------------------------
> 
> create table if not exists qifinance.accounts (
>   id uuid primary key default gen_random_uuid(),
> 
>   book_id uuid not null references qifinance.books(id) on delete cascade,
>   parent_account_id uuid references qifinance.accounts(id) on delete restrict,
> 
>   code text not null,
>   name text not null,
> 
>   account_type qifinance.account_type not null,
>   normal_balance qifinance.normal_balance not null,
> 
>   is_contra boolean not null default false,
>   is_cash_equivalent boolean not null default false,
> 
>   description text,
>   tax_line text,
> 
>   active boolean not null default true,
> 
>   metadata jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now(),
> 
>   unique (book_id, code),
>   unique (book_id, name),
> 
>   constraint accounts_normal_balance_check check (
>     is_contra = true
>     or (
>       account_type in ('asset', 'expense')
>       and normal_balance = 'debit'
>     )
>     or (
>       account_type in ('liability', 'equity', 'income')
>       and normal_balance = 'credit'
>     )
>   )
> );
> 
> drop trigger if exists accounts_touch_updated_at on qifinance.accounts;
> 
> create trigger accounts_touch_updated_at
> before update on qifinance.accounts
> for each row
> execute function qifinance.touch_updated_at();
> 
> create index if not exists accounts_book_idx
> on qifinance.accounts(book_id);
> 
> create index if not exists accounts_type_idx
> on qifinance.accounts(account_type);
> 
> -- ---------------------------------------------------------
> -- Counterparties
> -- Vendors, customers, employers, people, agencies, platforms.
> -- ---------------------------------------------------------
> 
> create table if not exists qifinance.counterparties (
>   id uuid primary key default gen_random_uuid(),
> 
>   book_id uuid not null references qifinance.books(id) on delete cascade,
> 
>   name text not null,
>   normalized_name text,
>   counterparty_type text,
> 
>   email text,
>   phone text,
>   website text,
> 
>   tax_id_last4 text,
> 
>   metadata jsonb not null default '{}'::jsonb,
> 
>   active boolean not null default true,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now(),
> 
>   unique (book_id, name)
> );
> 
> drop trigger if exists counterparties_touch_updated_at on qifinance.counterparties;
> 
> create trigger counterparties_touch_updated_at
> before update on qifinance.counterparties
> for each row
> execute function qifinance.touch_updated_at();
> 
> create index if not exists counterparties_book_idx
> on qifinance.counterparties(book_id);
> 
> create index if not exists counterparties_normalized_name_idx
> on qifinance.counterparties(normalized_name);
> 
> -- ---------------------------------------------------------
> -- Financial Institutions
> -- Banks, credit cards, PayPal, Stripe, Venmo, Cash App, etc.
> -- ---------------------------------------------------------
> 
> create table if not exists qifinance.financial_institutions (
>   id uuid primary key default gen_random_uuid(),
> 
>   name text not null,
>   institution_type text,
> 
>   website text,
> 
>   metadata jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now(),
> 
>   unique (name)
> );
> 
> drop trigger if exists financial_institutions_touch_updated_at on qifinance.financial_institutions;
> 
> create trigger financial_institutions_touch_updated_at
> before update on qifinance.financial_institutions
> for each row
> execute function qifinance.touch_updated_at();
> 
> -- ---------------------------------------------------------
> -- External Accounts
> -- These are export/feed accounts.
> -- They map to real ledger accounts.
> -- ---------------------------------------------------------
> 
> create table if not exists qifinance.external_accounts (
>   id uuid primary key default gen_random_uuid(),
> 
>   book_id uuid not null references qifinance.books(id) on delete cascade,
>   institution_id uuid references qifinance.financial_institutions(id) on delete set null,
> 
>   ledger_account_id uuid references qifinance.accounts(id) on delete restrict,
> 
>   name text not null,
>   account_kind text,
> 
>   source_system text,
>   source_account_id text,
> 
>   account_number_last4 text,
>   currency char(3) not null default 'USD',
> 
>   opened_on date,
>   closed_on date,
> 
>   active boolean not null default true,
> 
>   metadata jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now(),
> 
>   unique (book_id, name)
> );
> 
> drop trigger if exists external_accounts_touch_updated_at on qifinance.external_accounts;
> 
> create trigger external_accounts_touch_updated_at
> before update on qifinance.external_accounts
> for each row
> execute function qifinance.touch_updated_at();
> 
> create index if not exists external_accounts_book_idx
> on qifinance.external_accounts(book_id);
> 
> create index if not exists external_accounts_ledger_account_idx
> on qifinance.external_accounts(ledger_account_id);
> 
> -- ---------------------------------------------------------
> -- Import Profiles
> -- Defines how to interpret different exports.
> -- Example: Chase CSV, PayPal CSV, Stripe payout export, Uber CSV.
> -- ---------------------------------------------------------
> 
> create table if not exists qifinance.import_profiles (
>   id uuid primary key default gen_random_uuid(),
> 
>   book_id uuid not null references qifinance.books(id) on delete cascade,
> 
>   name text not null,
>   source_system text not null,
> 
>   file_type text,
>   date_format text,
>   amount_format text,
> 
>   column_map jsonb not null default '{}'::jsonb,
>   transform_rules jsonb not null default '{}'::jsonb,
> 
>   active boolean not null default true,
> 
>   metadata jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now(),
> 
>   unique (book_id, name)
> );
> 
> drop trigger if exists import_profiles_touch_updated_at on qifinance.import_profiles;
> 
> create trigger import_profiles_touch_updated_at
> before update on qifinance.import_profiles
> for each row
> execute function qifinance.touch_updated_at();
> 
> -- ---------------------------------------------------------
> -- Import Files
> -- Each uploaded/exported file gets recorded here.
> -- ---------------------------------------------------------
> 
> create table if not exists qifinance.import_files (
>   id uuid primary key default gen_random_uuid(),
> 
>   book_id uuid not null references qifinance.books(id) on delete cascade,
>   import_profile_id uuid references qifinance.import_profiles(id) on delete set null,
>   external_account_id uuid references qifinance.external_accounts(id) on delete set null,
> 
>   source_system text,
>   original_filename text not null,
>   storage_path text,
> 
>   checksum_sha256 text,
>   file_mime_type text,
> 
>   statement_start_date date,
>   statement_end_date date,
> 
>   row_count integer,
> 
>   imported_at timestamptz not null default now(),
> 
>   metadata jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
> 
>   unique (book_id, checksum_sha256)
> );
> 
> create index if not exists import_files_book_idx
> on qifinance.import_files(book_id);
> 
> create index if not exists import_files_external_account_idx
> on qifinance.import_files(external_account_id);
> 
> -- ---------------------------------------------------------
> -- Raw Import Rows
> -- Raw rows stay untouched.
> -- This lets you re-parse bad exports later.
> -- ---------------------------------------------------------
> 
> create table if not exists qifinance.raw_import_rows (
>   id uuid primary key default gen_random_uuid(),
> 
>   import_file_id uuid not null references qifinance.import_files(id) on delete cascade,
> 
>   row_number integer not null,
> 
>   raw_data jsonb not null,
>   raw_text text,
> 
>   row_hash text,
> 
>   parse_status text not null default 'new',
>   parse_error text,
> 
>   created_at timestamptz not null default now(),
> 
>   unique (import_file_id, row_number)
> );
> 
> create index if not exists raw_import_rows_file_idx
> on qifinance.raw_import_rows(import_file_id);
> 
> create index if not exists raw_import_rows_hash_idx
> on qifinance.raw_import_rows(row_hash);
> 
> create index if not exists raw_import_rows_raw_data_gin_idx
> on qifinance.raw_import_rows using gin(raw_data);
> 
> -- ---------------------------------------------------------
> -- Imported Transactions
> -- Normalized import layer.
> -- Still not the ledger.
> -- ---------------------------------------------------------
> 
> create table if not exists qifinance.imported_transactions (
>   id uuid primary key default gen_random_uuid(),
> 
>   book_id uuid not null references qifinance.books(id) on delete cascade,
>   external_account_id uuid not null references qifinance.external_accounts(id) on delete cascade,
>   raw_import_row_id uuid references qifinance.raw_import_rows(id) on delete set null,
> 
>   source_system text,
>   source_transaction_id text,
> 
>   transaction_date date not null,
>   posted_date date,
>   transaction_datetime timestamptz,
> 
>   description text not null,
>   memo text,
> 
>   counterparty_id uuid references qifinance.counterparties(id) on delete set null,
> 
>   -- Amount as normalized from the source.
>   -- Do not treat this as the final debit/credit.
>   amount numeric(20, 6) not null,
>   currency char(3) not null default 'USD',
> 
>   source_debit_amount numeric(20, 6),
>   source_credit_amount numeric(20, 6),
>   source_balance_after numeric(20, 6),
> 
>   check_number text,
>   category_text text,
>   transaction_type text,
> 
>   dedupe_key text not null,
> 
>   status qifinance.import_tx_status not null default 'new',
> 
>   metadata jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now(),
> 
>   unique (book_id, dedupe_key)
> );
> 
> drop trigger if exists imported_transactions_touch_updated_at on qifinance.imported_transactions;
> 
> create trigger imported_transactions_touch_updated_at
> before update on qifinance.imported_transactions
> for each row
> execute function qifinance.touch_updated_at();
> 
> create unique index if not exists imported_transactions_source_tx_unique_idx
> on qifinance.imported_transactions(book_id, external_account_id, source_transaction_id)
> where source_transaction_id is not null;
> 
> create index if not exists imported_transactions_book_idx
> on qifinance.imported_transactions(book_id);
> 
> create index if not exists imported_transactions_external_account_idx
> on qifinance.imported_transactions(external_account_id);
> 
> create index if not exists imported_transactions_date_idx
> on qifinance.imported_transactions(transaction_date);
> 
> create index if not exists imported_transactions_status_idx
> on qifinance.imported_transactions(status);
> 
> -- ---------------------------------------------------------
> -- Journal Entries
> -- Header row for double-entry transactions.
> -- ---------------------------------------------------------
> 
> create table if not exists qifinance.journal_entries (
>   id uuid primary key default gen_random_uuid(),
> 
>   book_id uuid not null references qifinance.books(id) on delete cascade,
> 
>   entry_no text,
> 
>   entry_date date not null,
>   description text not null,
> 
>   reference text,
>   source text not null default 'manual',
> 
>   status qifinance.journal_status not null default 'draft',
> 
>   posted_at timestamptz,
>   locked_at timestamptz,
> 
>   voided_at timestamptz,
>   void_reason text,
> 
>   metadata jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now(),
> 
>   unique (book_id, entry_no)
> );
> 
> drop trigger if exists journal_entries_touch_updated_at on qifinance.journal_entries;
> 
> create trigger journal_entries_touch_updated_at
> before update on qifinance.journal_entries
> for each row
> execute function qifinance.touch_updated_at();
> 
> create index if not exists journal_entries_book_idx
> on qifinance.journal_entries(book_id);
> 
> create index if not exists journal_entries_date_idx
> on qifinance.journal_entries(entry_date);
> 
> create index if not exists journal_entries_status_idx
> on qifinance.journal_entries(status);
> 
> -- ---------------------------------------------------------
> -- Journal Lines
> -- The actual debit/credit lines.
> -- This is the double-entry core.
> -- ---------------------------------------------------------
> 
> create table if not exists qifinance.journal_lines (
>   id uuid primary key default gen_random_uuid(),
> 
>   entry_id uuid not null references qifinance.journal_entries(id) on delete cascade,
> 
>   line_no integer not null,
> 
>   account_id uuid not null references qifinance.accounts(id) on delete restrict,
> 
>   counterparty_id uuid references qifinance.counterparties(id) on delete set null,
>   external_account_id uuid references qifinance.external_accounts(id) on delete set null,
> 
>   description text,
> 
>   debit_amount numeric(20, 6) not null default 0,
>   credit_amount numeric(20, 6) not null default 0,
> 
>   currency char(3) not null default 'USD',
> 
>   metadata jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
> 
>   unique (entry_id, line_no),
> 
>   constraint journal_lines_amounts_nonnegative_check check (
>     debit_amount >= 0
>     and credit_amount >= 0
>   ),
> 
>   constraint journal_lines_one_side_only_check check (
>     (
>       debit_amount > 0
>       and credit_amount = 0
>     )
>     or
>     (
>       credit_amount > 0
>       and debit_amount = 0
>     )
>   )
> );
> 
> create index if not exists journal_lines_entry_idx
> on qifinance.journal_lines(entry_id);
> 
> create index if not exists journal_lines_account_idx
> on qifinance.journal_lines(account_id);
> 
> create index if not exists journal_lines_counterparty_idx
> on qifinance.journal_lines(counterparty_id);
> 
> -- ---------------------------------------------------------
> -- Enforce Balanced Journal Entries
> -- Draft entries may be unbalanced.
> -- Posted / locked entries must balance.
> -- ---------------------------------------------------------
> 
> create or replace function qifinance.check_journal_entry_balanced(p_entry_id uuid)
> returns void
> language plpgsql
> as $$
> declare
>   v_status qifinance.journal_status;
>   v_debits numeric(20, 6);
>   v_credits numeric(20, 6);
>   v_line_count integer;
> begin
>   select status
>   into v_status
>   from qifinance.journal_entries
>   where id = p_entry_id;
> 
>   if v_status is null then
>     return;
>   end if;
> 
>   if v_status in ('draft', 'void') then
>     return;
>   end if;
> 
>   select
>     coalesce(sum(debit_amount), 0),
>     coalesce(sum(credit_amount), 0),
>     count(*)
>   into
>     v_debits,
>     v_credits,
>     v_line_count
>   from qifinance.journal_lines
>   where entry_id = p_entry_id;
> 
>   if v_line_count < 2 then
>     raise exception 'Posted journal entry % must have at least two lines', p_entry_id;
>   end if;
> 
>   if v_debits <> v_credits then
>     raise exception 'Journal entry % is not balanced. Debits: %, Credits: %',
>       p_entry_id,
>       v_debits,
>       v_credits;
>   end if;
> end;
> $$;
> 
> create or replace function qifinance.enforce_journal_lines_balanced()
> returns trigger
> language plpgsql
> as $$
> begin
>   if tg_op in ('INSERT', 'UPDATE') then
>     perform qifinance.check_journal_entry_balanced(new.entry_id);
>   end if;
> 
>   if tg_op in ('UPDATE', 'DELETE') then
>     perform qifinance.check_journal_entry_balanced(old.entry_id);
>   end if;
> 
>   if tg_op = 'DELETE' then
>     return old;
>   else
>     return new;
>   end if;
> end;
> $$;
> 
> drop trigger if exists journal_lines_balance_check on qifinance.journal_lines;
> 
> create constraint trigger journal_lines_balance_check
> after insert or update or delete on qifinance.journal_lines
> deferrable initially deferred
> for each row
> execute function qifinance.enforce_journal_lines_balanced();
> 
> create or replace function qifinance.enforce_journal_entry_status_balanced()
> returns trigger
> language plpgsql
> as $$
> begin
>   if new.status in ('posted', 'locked') then
>     perform qifinance.check_journal_entry_balanced(new.id);
>   end if;
> 
>   return new;
> end;
> $$;
> 
> drop trigger if exists journal_entries_status_balance_check on qifinance.journal_entries;
> 
> create constraint trigger journal_entries_status_balance_check
> after insert or update of status on qifinance.journal_entries
> deferrable initially deferred
> for each row
> execute function qifinance.enforce_journal_entry_status_balanced();
> 
> -- ---------------------------------------------------------
> -- Source Links
> -- Connects ledger truth back to imported evidence.
> -- ---------------------------------------------------------
> 
> create table if not exists qifinance.journal_source_links (
>   id uuid primary key default gen_random_uuid(),
> 
>   journal_entry_id uuid not null references qifinance.journal_entries(id) on delete cascade,
>   journal_line_id uuid references qifinance.journal_lines(id) on delete cascade,
> 
>   imported_transaction_id uuid references qifinance.imported_transactions(id) on delete set null,
>   raw_import_row_id uuid references qifinance.raw_import_rows(id) on delete set null,
> 
>   link_type text not null default 'posted_from',
>   confidence numeric(5, 4),
> 
>   metadata jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
> 
>   constraint journal_source_links_has_source_check check (
>     imported_transaction_id is not null
>     or raw_import_row_id is not null
>   )
> );
> 
> create index if not exists journal_source_links_entry_idx
> on qifinance.journal_source_links(journal_entry_id);
> 
> create index if not exists journal_source_links_imported_tx_idx
> on qifinance.journal_source_links(imported_transaction_id);
> 
> -- ---------------------------------------------------------
> -- Posting Rules
> -- For auto-categorizing imports.
> -- Keep flexible because every export is weird.
> -- ---------------------------------------------------------
> 
> create table if not exists qifinance.posting_rules (
>   id uuid primary key default gen_random_uuid(),
> 
>   book_id uuid not null references qifinance.books(id) on delete cascade,
> 
>   priority integer not null default 100,
>   name text not null,
> 
>   active boolean not null default true,
> 
>   -- Example match:
>   -- {"description_ilike": "%LYFT%", "amount_lt": 0}
>   match_conditions jsonb not null default '{}'::jsonb,
> 
>   -- Example action:
>   -- {"debit_account_code": "6100", "credit_account_code": "1000"}
>   posting_action jsonb not null default '{}'::jsonb,
> 
>   notes text,
> 
>   metadata jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now(),
> 
>   unique (book_id, name)
> );
> 
> drop trigger if exists posting_rules_touch_updated_at on qifinance.posting_rules;
> 
> create trigger posting_rules_touch_updated_at
> before update on qifinance.posting_rules
> for each row
> execute function qifinance.touch_updated_at();
> 
> create index if not exists posting_rules_book_priority_idx
> on qifinance.posting_rules(book_id, priority);
> 
> create index if not exists posting_rules_match_gin_idx
> on qifinance.posting_rules using gin(match_conditions);
> 
> -- ---------------------------------------------------------
> -- Tags
> -- Useful for projects, tax buckets, disputes, reimbursements.
> -- ---------------------------------------------------------
> 
> create table if not exists qifinance.tags (
>   id uuid primary key default gen_random_uuid(),
> 
>   book_id uuid not null references qifinance.books(id) on delete cascade,
> 
>   name text not null,
>   color text,
> 
>   metadata jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
> 
>   unique (book_id, name)
> );
> 
> create table if not exists qifinance.journal_entry_tags (
>   journal_entry_id uuid not null references qifinance.journal_entries(id) on delete cascade,
>   tag_id uuid not null references qifinance.tags(id) on delete cascade,
> 
>   created_at timestamptz not null default now(),
> 
>   primary key (journal_entry_id, tag_id)
> );
> 
> -- ---------------------------------------------------------
> -- Reconciliation
> -- Matches ledger lines/imports against statements.
> -- ---------------------------------------------------------
> 
> create table if not exists qifinance.reconciliation_sessions (
>   id uuid primary key default gen_random_uuid(),
> 
>   book_id uuid not null references qifinance.books(id) on delete cascade,
>   external_account_id uuid not null references qifinance.external_accounts(id) on delete cascade,
> 
>   statement_start_date date not null,
>   statement_end_date date not null,
> 
>   statement_ending_balance numeric(20, 6) not null,
>   currency char(3) not null default 'USD',
> 
>   status qifinance.reconciliation_status not null default 'open',
> 
>   notes text,
> 
>   reconciled_at timestamptz,
>   locked_at timestamptz,
> 
>   metadata jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now(),
> 
>   unique (external_account_id, statement_start_date, statement_end_date)
> );
> 
> drop trigger if exists reconciliation_sessions_touch_updated_at on qifinance.reconciliation_sessions;
> 
> create trigger reconciliation_sessions_touch_updated_at
> before update on qifinance.reconciliation_sessions
> for each row
> execute function qifinance.touch_updated_at();
> 
> create table if not exists qifinance.reconciliation_items (
>   id uuid primary key default gen_random_uuid(),
> 
>   reconciliation_session_id uuid not null references qifinance.reconciliation_sessions(id) on delete cascade,
> 
>   journal_line_id uuid references qifinance.journal_lines(id) on delete cascade,
>   imported_transaction_id uuid references qifinance.imported_transactions(id) on delete set null,
> 
>   cleared_date date,
>   cleared_amount numeric(20, 6),
> 
>   notes text,
> 
>   metadata jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
> 
>   constraint reconciliation_items_has_match_check check (
>     journal_line_id is not null
>     or imported_transaction_id is not null
>   )
> );
> 
> create index if not exists reconciliation_items_session_idx
> on qifinance.reconciliation_items(reconciliation_session_id);
> 
> create index if not exists reconciliation_items_journal_line_idx
> on qifinance.reconciliation_items(journal_line_id);
> 
> -- ---------------------------------------------------------
> -- Documents / Attachments
> -- Receipts, statements, invoices, export files, notices, etc.
> -- ---------------------------------------------------------
> 
> create table if not exists qifinance.documents (
>   id uuid primary key default gen_random_uuid(),
> 
>   book_id uuid not null references qifinance.books(id) on delete cascade,
> 
>   title text not null,
>   document_type text,
> 
>   original_filename text,
>   storage_path text,
>   mime_type text,
> 
>   checksum_sha256 text,
> 
>   document_date date,
> 
>   metadata jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now()
> );
> 
> drop trigger if exists documents_touch_updated_at on qifinance.documents;
> 
> create trigger documents_touch_updated_at
> before update on qifinance.documents
> for each row
> execute function qifinance.touch_updated_at();
> 
> create table if not exists qifinance.document_links (
>   id uuid primary key default gen_random_uuid(),
> 
>   document_id uuid not null references qifinance.documents(id) on delete cascade,
> 
>   journal_entry_id uuid references qifinance.journal_entries(id) on delete cascade,
>   journal_line_id uuid references qifinance.journal_lines(id) on delete cascade,
>   imported_transaction_id uuid references qifinance.imported_transactions(id) on delete cascade,
>   counterparty_id uuid references qifinance.counterparties(id) on delete cascade,
>   external_account_id uuid references qifinance.external_accounts(id) on delete cascade,
> 
>   link_type text not null default 'evidence',
> 
>   metadata jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
> 
>   constraint document_links_has_target_check check (
>     num_nonnulls(
>       journal_entry_id,
>       journal_line_id,
>       imported_transaction_id,
>       counterparty_id,
>       external_account_id
>     ) >= 1
>   )
> );
> 
> create index if not exists document_links_document_idx
> on qifinance.document_links(document_id);
> 
> -- ---------------------------------------------------------
> -- Reporting Views
> -- ---------------------------------------------------------
> 
> create or replace view qifinance.v_journal_entry_totals as
> select
>   je.id as journal_entry_id,
>   je.book_id,
>   je.entry_date,
>   je.description,
>   je.status,
>   coalesce(sum(jl.debit_amount), 0) as total_debits,
>   coalesce(sum(jl.credit_amount), 0) as total_credits,
>   coalesce(sum(jl.debit_amount), 0) - coalesce(sum(jl.credit_amount), 0) as imbalance
> from qifinance.journal_entries je
> left join qifinance.journal_lines jl
>   on jl.entry_id = je.id
> group by
>   je.id,
>   je.book_id,
>   je.entry_date,
>   je.description,
>   je.status;
> 
> create or replace view qifinance.v_account_balances as
> select
>   a.book_id,
>   a.id as account_id,
>   a.code,
>   a.name,
>   a.account_type,
>   a.normal_balance,
> 
>   coalesce(sum(jl.debit_amount), 0) as total_debits,
>   coalesce(sum(jl.credit_amount), 0) as total_credits,
> 
>   case
>     when a.normal_balance = 'debit'
>       then coalesce(sum(jl.debit_amount), 0) - coalesce(sum(jl.credit_amount), 0)
>     else
>       coalesce(sum(jl.credit_amount), 0) - coalesce(sum(jl.debit_amount), 0)
>   end as balance
> 
> from qifinance.accounts a
> left join qifinance.journal_lines jl
>   on jl.account_id = a.id
> left join qifinance.journal_entries je
>   on je.id = jl.entry_id
>   and je.status in ('posted', 'locked')
> group by
>   a.book_id,
>   a.id,
>   a.code,
>   a.name,
>   a.account_type,
>   a.normal_balance;
> 
> create or replace view qifinance.v_trial_balance as
> select
>   book_id,
>   account_type,
>   code,
>   name,
>   normal_balance,
>   total_debits,
>   total_credits,
>   balance
> from qifinance.v_account_balances
> order by
>   account_type,
>   code;
> 
> create or replace view qifinance.v_unposted_imported_transactions as
> select
>   it.*
> from qifinance.imported_transactions it
> where it.status in ('new', 'reviewed', 'error')
> order by
>   it.transaction_date desc,
>   it.created_at desc;
> ```
> 
> ## The practical posting flow
> 
> Use it like this:
> 
> 1. **Upload/export file**
>    - Insert into `import_files`.
> 
> 2. **Store untouched rows**
>    - Insert every original row into `raw_import_rows.raw_data`.
> 
> 3. **Normalize**
>    - Convert raw rows into `imported_transactions`.
> 
> 4. **Post**
>    - Create one `journal_entries` row.
>    - Create at least two `journal_lines`.
>    - Link the entry back to the import using `journal_source_links`.
> 
> 5. **Only mark as `posted` after it balances**
>    - The trigger will reject bad entries. Good. That is exactly what you want.
> 
> ## The rule I would not break
> 
> Do **not** make imported transactions your ledger.
> 
> Bad design:
> 
> ```text
> transactions
> - date
> - amount
> - category
> ```
> 
> That is budget-app logic, not accounting.
> 
> Good design:
> 
> ```text
> imported_transactions = messy outside-world evidence
> journal_entries + journal_lines = accounting truth
> ```
> 
> That distinction is what makes this scale across bank CSVs, credit cards, PayPal, Stripe, Uber, Lyft, Cash App, tax exports, weird PDFs, and whatever other financial goblin-scrolls you end up importing.

### User
> ok that went through just fine, look i dont get directurs at all, and ya,

### Assistant
> Good — the hard part is installed. Now we do **orientation**, not more schema dumping. You need the mental map first, otherwise this turns into database soup fast.

### Assistant
> Yep. So here’s the plain-English map.
> 
> ## What you just created
> 
> Think of Postgres like this:
> 
> | Thing | Plain meaning |
> |---|---|
> | **Database** | The whole building |
> | **Schema** | A room inside the building |
> | **Table** | A filing cabinet |
> | **Column** | A labeled field on every file |
> | **Row** | One actual record |
> | **View** | A saved report/query |
> | **Function** | A reusable action |
> | **Trigger** | An automatic guardrail that runs when data changes |
> 
> So:
> 
> ```text
> qifinance = the accounting room
> accounts = chart of accounts cabinet
> journal_entries = transaction header cabinet
> journal_lines = debit/credit line cabinet
> imported_transactions = messy CSV/import cabinet
> ```
> 
> ## The one concept that matters
> 
> A real accounting transaction is **not** just:
> 
> ```text
> Date | Description | Amount | Category
> ```
> 
> That’s budget-app baby food.
> 
> A real double-entry transaction is:
> 
> ```text
> Journal Entry
>   Line 1: Debit something
>   Line 2: Credit something
> ```
> 
> And this must always be true:
> 
> ```text
> Total debits = total credits
> ```
> 
> Example: you spend $20 at McDonald’s from checking.
> 
> ```text
> Debit:  Meals Expense     $20
> Credit: Checking Account  $20
> ```
> 
> Example: Lyft pays you $100.
> 
> ```text
> Debit:  Checking Account  $100
> Credit: Gig Income        $100
> ```
> 
> That’s it. That’s the whole engine.
> 
> ## What the triggers are doing
> 
> The triggers are not magical business logic. They are just guards.
> 
> They say:
> 
> > “If you try to mark a journal entry as posted, I’m checking that debit equals credit. If not, I’m blocking your nonsense.”
> 
> Good. We want that.
> 
> ## What you need next
> 
> Right now you have empty filing cabinets.
> 
> Next, you need a **starter book** and a **starter chart of accounts**.
> 
> Run this next:
> 
> ```sql
> -- =========================================================
> -- QiFinance Starter Book + Chart of Accounts
> -- =========================================================
> 
> with book as (
>   insert into qifinance.books (
>     name,
>     legal_name,
>     base_currency,
>     timezone
>   )
>   values (
>     'QiFinance Personal',
>     'Cody J. Rice-Velasquez',
>     'USD',
>     'America/Chicago'
>   )
>   on conflict (name)
>   do update set updated_at = now()
>   returning id
> )
> 
> insert into qifinance.accounts (
>   book_id,
>   code,
>   name,
>   account_type,
>   normal_balance,
>   is_cash_equivalent,
>   description
> )
> 
> select
>   book.id,
>   account_data.code,
>   account_data.name,
>   account_data.account_type::qifinance.account_type,
>   account_data.normal_balance::qifinance.normal_balance,
>   account_data.is_cash_equivalent,
>   account_data.description
> 
> from book
> 
> cross join (
>   values
> 
>   -- Assets
>   ('1000', 'Cash & Bank', 'asset', 'debit', true, 'Main cash and bank category'),
>   ('1010', 'Checking Account', 'asset', 'debit', true, 'Primary checking account'),
>   ('1020', 'Savings Account', 'asset', 'debit', true, 'Savings account'),
>   ('1030', 'Cash on Hand', 'asset', 'debit', true, 'Physical cash'),
>   ('1100', 'Accounts Receivable', 'asset', 'debit', false, 'Money owed to you'),
>   ('1200', 'Prepaid Expenses', 'asset', 'debit', false, 'Expenses paid in advance'),
>   ('1300', 'Equipment & Property', 'asset', 'debit', false, 'Long-term owned assets'),
> 
>   -- Liabilities
>   ('2000', 'Liabilities', 'liability', 'credit', false, 'Main liabilities category'),
>   ('2010', 'Credit Cards', 'liability', 'credit', false, 'Credit card balances'),
>   ('2020', 'Loans Payable', 'liability', 'credit', false, 'Loans owed'),
>   ('2030', 'Rent / Housing Payable', 'liability', 'credit', false, 'Housing obligations owed'),
>   ('2040', 'Taxes Payable', 'liability', 'credit', false, 'Taxes owed'),
> 
>   -- Equity
>   ('3000', 'Equity', 'equity', 'credit', false, 'Owner equity'),
>   ('3010', 'Opening Balance Equity', 'equity', 'credit', false, 'Starting account balances'),
>   ('3020', 'Owner Contributions', 'equity', 'credit', false, 'Money personally added'),
>   ('3030', 'Owner Draws', 'equity', 'credit', false, 'Money personally removed'),
> 
>   -- Income
>   ('4000', 'Income', 'income', 'credit', false, 'Main income category'),
>   ('4010', 'Gig Income', 'income', 'credit', false, 'Uber, Lyft, DoorDash, delivery, rideshare'),
>   ('4020', 'Consulting Income', 'income', 'credit', false, 'Business operations or consulting income'),
>   ('4030', 'Reimbursements', 'income', 'credit', false, 'Reimbursed expenses'),
>   ('4040', 'Refunds & Credits', 'income', 'credit', false, 'Refunds, credits, adjustments'),
> 
>   -- Expenses
>   ('5000', 'Expenses', 'expense', 'debit', false, 'Main expense category'),
>   ('5010', 'Food & Meals', 'expense', 'debit', false, 'Food, restaurants, groceries'),
>   ('5020', 'Fuel', 'expense', 'debit', false, 'Gasoline and charging'),
>   ('5030', 'Vehicle Rental', 'expense', 'debit', false, 'Rental vehicle costs'),
>   ('5040', 'Vehicle Maintenance', 'expense', 'debit', false, 'Repairs, maintenance, parts'),
>   ('5050', 'Insurance', 'expense', 'debit', false, 'Insurance costs'),
>   ('5060', 'Phone & Internet', 'expense', 'debit', false, 'Phone, hotspot, internet'),
>   ('5070', 'Software & Subscriptions', 'expense', 'debit', false, 'Apps, SaaS, subscriptions'),
>   ('5080', 'Office Supplies', 'expense', 'debit', false, 'Supplies and small equipment'),
>   ('5090', 'Housing', 'expense', 'debit', false, 'Rent, utilities, housing costs'),
>   ('5100', 'Medical & Health', 'expense', 'debit', false, 'Health-related expenses'),
>   ('5110', 'Pet / ESA Expenses', 'expense', 'debit', false, 'Gigi, pet food, care, supplies'),
>   ('5120', 'Bank Fees', 'expense', 'debit', false, 'Bank charges and fees'),
>   ('5130', 'Legal & Professional', 'expense', 'debit', false, 'Legal, filing, professional fees'),
>   ('5140', 'Taxes & Licenses', 'expense', 'debit', false, 'Taxes, permits, licenses'),
>   ('5999', 'Uncategorized Expense', 'expense', 'debit', false, 'Temporary holding account for unknown expenses')
> 
> ) as account_data (
>   code,
>   name,
>   account_type,
>   normal_balance,
>   is_cash_equivalent,
>   description
> )
> 
> on conflict (book_id, code)
> do nothing;
> ```
> 
> ## After that, the system has a skeleton
> 
> Then the real workflow becomes:
> 
> ```text
> 1. Add external bank/credit/card accounts
> 2. Import CSV/export files
> 3. Store raw rows
> 4. Normalize them into imported_transactions
> 5. Review/categorize
> 6. Post into journal_entries + journal_lines
> 7. Reconcile
> 8. Report
> ```
> 
> ## Simple version
> 
> You only need to understand **three tables first**:
> 
> ### `accounts`
> 
> Your buckets.
> 
> Examples:
> 
> ```text
> Checking
> Gig Income
> Food & Meals
> Fuel
> Vehicle Rental
> Credit Cards
> ```
> 
> ### `journal_entries`
> 
> The transaction wrapper.
> 
> Example:
> 
> ```text
> 2026-06-21 | McDonald’s
> ```
> 
> ### `journal_lines`
> 
> The real accounting.
> 
> Example:
> 
> ```text
> Debit  Food & Meals       12.50
> Credit Checking Account   12.50
> ```
> 
> Everything else is support structure.
> 
> The next SQL you probably want after the chart of accounts is a helper function like:
> 
> ```text
> post_simple_cash_transaction()
> ```
> 
> So you can feed it:
> 
> ```text
> date, description, amount, bank account, category account
> ```
> 
> And it automatically creates the balanced journal entry. That’s the bridge between “normal human transaction” and “proper double-entry accounting.”

### User
> basically i was trying to create a mini inventory of the stuff i bout for the house, then imma put the price and deduct it from my rent payment.

### Assistant
> That makes sense. You do **not** need the full accounting monster for that first. You need a clean **house purchase ledger** that can later post into double-entry when you’re ready.

### Assistant
> Exactly. Then don’t overcomplicate it.
> 
> You need a **house purchase / rent credit tracker**, not “full inventory accounting” yet.
> 
> But important legal/common-sense warning: **do not silently deduct it from rent unless you have written agreement or a clear legal basis.** Indiana is not friendly to “repair and deduct” rent withholding; tenant-rights sources say Indiana generally does **not** give tenants a clear right to withhold rent or deduct repairs from rent without going through proper process. So in the database, call it a **proposed rent credit** until approved. Paper trail beats vibes. citeturn365217search0turn365217search8turn365217search14
> 
> ## Clean structure
> 
> You need to track:
> 
> ```text
> What I bought
> Why I bought it
> Where it is in the house
> How much it cost
> Whether it is safety / repair / improvement / convenience
> Whether I want reimbursement or rent credit
> Whether the rent credit was approved
> Which rent month it applies to
> ```
> 
> ## Add this SQL
> 
> This creates a small house purchase tracker inside `qifinance`.
> 
> ```sql
> -- =========================================================
> -- QiFinance House Purchases / Rent Credit Tracker
> -- Schema: qifinance
> -- =========================================================
> 
> do $$
> begin
>   create type qifinance.house_purchase_status as enum (
>     'planned',
>     'purchased',
>     'submitted',
>     'approved',
>     'partially_approved',
>     'denied',
>     'applied_to_rent',
>     'kept_personal',
>     'returned'
>   );
> exception when duplicate_object then null;
> end $$;
> 
> do $$
> begin
>   create type qifinance.house_purchase_category as enum (
>     'safety',
>     'security',
>     'repair',
>     'pest_control',
>     'cleaning',
>     'maintenance',
>     'fixture',
>     'tool',
>     'convenience',
>     'other'
>   );
> exception when duplicate_object then null;
> end $$;
> 
> do $$
> begin
>   create type qifinance.rent_credit_status as enum (
>     'draft',
>     'sent',
>     'approved',
>     'partially_approved',
>     'denied',
>     'applied',
>     'void'
>   );
> exception when duplicate_object then null;
> end $$;
> 
> -- ---------------------------------------------------------
> -- House Purchase Items
> -- Each row = one thing bought for the house.
> -- ---------------------------------------------------------
> 
> create table if not exists qifinance.house_purchase_items (
>   id uuid primary key default gen_random_uuid(),
> 
>   book_id uuid not null references qifinance.books(id) on delete cascade,
> 
>   purchase_date date not null default current_date,
> 
>   item_name text not null,
>   category qifinance.house_purchase_category not null default 'other',
> 
>   vendor text,
>   brand text,
>   model text,
> 
>   quantity numeric(12, 2) not null default 1,
>   unit_price numeric(12, 2) not null default 0,
>   tax_amount numeric(12, 2) not null default 0,
>   shipping_amount numeric(12, 2) not null default 0,
>   discount_amount numeric(12, 2) not null default 0,
> 
>   total_amount numeric(12, 2) generated always as (
>     round(
>       ((quantity * unit_price) + tax_amount + shipping_amount - discount_amount)::numeric,
>       2
>     )
>   ) stored,
> 
>   house_location text,
>   reason_needed text,
>   safety_issue boolean not null default false,
> 
>   purchased_by text default 'Cody',
>   payment_method text,
>   external_account_id uuid references qifinance.external_accounts(id) on delete set null,
>   imported_transaction_id uuid references qifinance.imported_transactions(id) on delete set null,
>   journal_entry_id uuid references qifinance.journal_entries(id) on delete set null,
> 
>   receipt_document_id uuid references qifinance.documents(id) on delete set null,
> 
>   -- This is the amount you are asking to count against rent.
>   requested_rent_credit_amount numeric(12, 2),
> 
>   -- This is the amount actually approved.
>   approved_rent_credit_amount numeric(12, 2),
> 
>   status qifinance.house_purchase_status not null default 'purchased',
> 
>   notes text,
> 
>   metadata jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now(),
> 
>   constraint house_purchase_amounts_nonnegative_check check (
>     quantity >= 0
>     and unit_price >= 0
>     and tax_amount >= 0
>     and shipping_amount >= 0
>     and discount_amount >= 0
>   ),
> 
>   constraint house_purchase_requested_credit_check check (
>     requested_rent_credit_amount is null
>     or requested_rent_credit_amount >= 0
>   ),
> 
>   constraint house_purchase_approved_credit_check check (
>     approved_rent_credit_amount is null
>     or approved_rent_credit_amount >= 0
>   )
> );
> 
> drop trigger if exists house_purchase_items_touch_updated_at
> on qifinance.house_purchase_items;
> 
> create trigger house_purchase_items_touch_updated_at
> before update on qifinance.house_purchase_items
> for each row
> execute function qifinance.touch_updated_at();
> 
> create index if not exists house_purchase_items_book_idx
> on qifinance.house_purchase_items(book_id);
> 
> create index if not exists house_purchase_items_purchase_date_idx
> on qifinance.house_purchase_items(purchase_date);
> 
> create index if not exists house_purchase_items_status_idx
> on qifinance.house_purchase_items(status);
> 
> create index if not exists house_purchase_items_category_idx
> on qifinance.house_purchase_items(category);
> 
> -- ---------------------------------------------------------
> -- Rent Credit Claims
> -- One claim = one batch you want to apply to rent.
> -- Example: June 2026 house safety supplies.
> -- ---------------------------------------------------------
> 
> create table if not exists qifinance.rent_credit_claims (
>   id uuid primary key default gen_random_uuid(),
> 
>   book_id uuid not null references qifinance.books(id) on delete cascade,
> 
>   claim_name text not null,
> 
>   rent_period_start date not null,
>   rent_period_end date not null,
> 
>   monthly_rent_amount numeric(12, 2),
> 
>   status qifinance.rent_credit_status not null default 'draft',
> 
>   submitted_to text,
>   submitted_at timestamptz,
> 
>   approved_by text,
>   approved_at timestamptz,
> 
>   applied_to_rent_date date,
> 
>   notes text,
> 
>   metadata jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now(),
> 
>   unique (book_id, claim_name)
> );
> 
> drop trigger if exists rent_credit_claims_touch_updated_at
> on qifinance.rent_credit_claims;
> 
> create trigger rent_credit_claims_touch_updated_at
> before update on qifinance.rent_credit_claims
> for each row
> execute function qifinance.touch_updated_at();
> 
> create index if not exists rent_credit_claims_book_idx
> on qifinance.rent_credit_claims(book_id);
> 
> create index if not exists rent_credit_claims_rent_period_idx
> on qifinance.rent_credit_claims(rent_period_start, rent_period_end);
> 
> create index if not exists rent_credit_claims_status_idx
> on qifinance.rent_credit_claims(status);
> 
> -- ---------------------------------------------------------
> -- Claim Items
> -- Connects purchase items to rent credit claims.
> -- ---------------------------------------------------------
> 
> create table if not exists qifinance.rent_credit_claim_items (
>   id uuid primary key default gen_random_uuid(),
> 
>   rent_credit_claim_id uuid not null references qifinance.rent_credit_claims(id) on delete cascade,
>   house_purchase_item_id uuid not null references qifinance.house_purchase_items(id) on delete cascade,
> 
>   claimed_amount numeric(12, 2) not null,
>   approved_amount numeric(12, 2),
> 
>   notes text,
> 
>   created_at timestamptz not null default now(),
> 
>   unique (rent_credit_claim_id, house_purchase_item_id),
> 
>   constraint rent_credit_claim_items_amounts_check check (
>     claimed_amount >= 0
>     and (
>       approved_amount is null
>       or approved_amount >= 0
>     )
>   )
> );
> 
> create index if not exists rent_credit_claim_items_claim_idx
> on qifinance.rent_credit_claim_items(rent_credit_claim_id);
> 
> create index if not exists rent_credit_claim_items_purchase_item_idx
> on qifinance.rent_credit_claim_items(house_purchase_item_id);
> 
> -- ---------------------------------------------------------
> -- Views
> -- ---------------------------------------------------------
> 
> create or replace view qifinance.v_house_purchase_items as
> select
>   hpi.id,
>   hpi.book_id,
>   hpi.purchase_date,
>   hpi.item_name,
>   hpi.category,
>   hpi.vendor,
>   hpi.quantity,
>   hpi.unit_price,
>   hpi.tax_amount,
>   hpi.shipping_amount,
>   hpi.discount_amount,
>   hpi.total_amount,
>   hpi.house_location,
>   hpi.reason_needed,
>   hpi.safety_issue,
>   hpi.requested_rent_credit_amount,
>   hpi.approved_rent_credit_amount,
>   hpi.status,
>   hpi.notes,
>   hpi.created_at
> from qifinance.house_purchase_items hpi
> order by
>   hpi.purchase_date desc,
>   hpi.created_at desc;
> 
> create or replace view qifinance.v_rent_credit_claim_totals as
> select
>   rcc.id as rent_credit_claim_id,
>   rcc.book_id,
>   rcc.claim_name,
>   rcc.rent_period_start,
>   rcc.rent_period_end,
>   rcc.monthly_rent_amount,
>   rcc.status,
> 
>   coalesce(sum(rcci.claimed_amount), 0) as total_claimed_amount,
>   coalesce(sum(rcci.approved_amount), 0) as total_approved_amount,
> 
>   case
>     when rcc.monthly_rent_amount is null then null
>     else greatest(
>       rcc.monthly_rent_amount - coalesce(sum(rcci.approved_amount), 0),
>       0
>     )
>   end as remaining_rent_due_after_approved_credit
> 
> from qifinance.rent_credit_claims rcc
> left join qifinance.rent_credit_claim_items rcci
>   on rcci.rent_credit_claim_id = rcc.id
> group by
>   rcc.id,
>   rcc.book_id,
>   rcc.claim_name,
>   rcc.rent_period_start,
>   rcc.rent_period_end,
>   rcc.monthly_rent_amount,
>   rcc.status;
> ```
> 
> ## Add the stuff you bought
> 
> Based on what you said earlier, here’s the type of data you’d enter:
> 
> ```sql
> -- Replace the book name if yours is different.
> 
> with book as (
>   select id
>   from qifinance.books
>   where name = 'QiFinance Personal'
>   limit 1
> )
> 
> insert into qifinance.house_purchase_items (
>   book_id,
>   purchase_date,
>   item_name,
>   category,
>   vendor,
>   quantity,
>   unit_price,
>   house_location,
>   reason_needed,
>   safety_issue,
>   requested_rent_credit_amount,
>   status,
>   notes
> )
> 
> select
>   book.id,
>   current_date,
>   item_data.item_name,
>   item_data.category::qifinance.house_purchase_category,
>   item_data.vendor,
>   item_data.quantity,
>   item_data.unit_price,
>   item_data.house_location,
>   item_data.reason_needed,
>   item_data.safety_issue,
>   item_data.requested_rent_credit_amount,
>   'purchased'::qifinance.house_purchase_status,
>   item_data.notes
> 
> from book
> 
> cross join (
>   values
> 
>   (
>     'Back door / back area light solution',
>     'safety',
>     null,
>     1,
>     0.00,
>     'Back of house',
>     'No working light in back area; safety issue at night.',
>     true,
>     0.00,
>     'Enter exact price from receipt.'
>   ),
> 
>   (
>     'Carbon monoxide detector',
>     'safety',
>     null,
>     1,
>     0.00,
>     'House interior',
>     'No carbon monoxide detector in the house.',
>     true,
>     0.00,
>     'Safety item. Enter exact price from receipt.'
>   ),
> 
>   (
>     'Smoke detector',
>     'safety',
>     null,
>     1,
>     0.00,
>     'House interior',
>     'No smoke detector; food burned previously without adequate alert.',
>     true,
>     0.00,
>     'Safety item. Enter exact price from receipt.'
>   ),
> 
>   (
>     'Fruit fly trap / fly control item',
>     'pest_control',
>     null,
>     1,
>     0.00,
>     'Kitchen / house interior',
>     'Fruit flies present inside the house.',
>     false,
>     0.00,
>     'Enter exact price from receipt.'
>   ),
> 
>   (
>     'Yard flea and tick treatment',
>     'pest_control',
>     null,
>     1,
>     0.00,
>     'Yard',
>     'Ticks and fleas in the yard getting on Gigi.',
>     false,
>     0.00,
>     'Could be household pest control / pet safety issue.'
>   ),
> 
>   (
>     'Smart deadbolt for front door',
>     'security',
>     null,
>     1,
>     0.00,
>     'Front door',
>     'Keyless access for front door; improves access control and security.',
>     true,
>     0.00,
>     'Enter exact price from receipt.'
>   ),
> 
>   (
>     'Hooks / hanging hardware',
>     'fixture',
>     null,
>     1,
>     0.00,
>     'House interior',
>     'Additional hanging/storage support.',
>     false,
>     0.00,
>     'Maybe convenience unless specifically needed for house function.'
>   ),
> 
>   (
>     'Wall hole filler / sealant',
>     'repair',
>     null,
>     1,
>     0.00,
>     'Interior walls',
>     'Wall holes allowing bugs to enter.',
>     false,
>     0.00,
>     'Repair / pest prevention.'
>   ),
> 
>   (
>     'Bedroom door lock',
>     'security',
>     null,
>     1,
>     0.00,
>     'Bedroom door',
>     'Personal room security.',
>     false,
>     0.00,
>     'This may be personal unless agreed as house security.'
>   )
> 
> ) as item_data (
>   item_name,
>   category,
>   vendor,
>   quantity,
>   unit_price,
>   house_location,
>   reason_needed,
>   safety_issue,
>   requested_rent_credit_amount,
>   notes
> );
> ```
> 
> ## Then update prices
> 
> Once you have receipts, update each item.
> 
> Example:
> 
> ```sql
> update qifinance.house_purchase_items
> set
>   unit_price = 24.99,
>   requested_rent_credit_amount = 24.99,
>   vendor = 'Walmart',
>   notes = 'Receipt available.'
> where item_name = 'Carbon monoxide detector';
> ```
> 
> ## Create the rent credit claim
> 
> Example for June rent:
> 
> ```sql
> with book as (
>   select id
>   from qifinance.books
>   where name = 'QiFinance Personal'
>   limit 1
> )
> 
> insert into qifinance.rent_credit_claims (
>   book_id,
>   claim_name,
>   rent_period_start,
>   rent_period_end,
>   monthly_rent_amount,
>   status,
>   notes
> )
> 
> select
>   book.id,
>   'June 2026 House Safety and Repair Purchases',
>   date '2026-06-01',
>   date '2026-06-30',
>   426.00,
>   'draft',
>   'Household safety, pest control, repair, and security purchases proposed as rent credit.'
> from book
> 
> on conflict (book_id, claim_name)
> do nothing;
> ```
> 
> ## Attach all eligible purchases to the claim
> 
> This grabs anything where you entered a requested credit amount.
> 
> ```sql
> with claim as (
>   select id
>   from qifinance.rent_credit_claims
>   where claim_name = 'June 2026 House Safety and Repair Purchases'
>   limit 1
> )
> 
> insert into qifinance.rent_credit_claim_items (
>   rent_credit_claim_id,
>   house_purchase_item_id,
>   claimed_amount,
>   notes
> )
> 
> select
>   claim.id,
>   hpi.id,
>   hpi.requested_rent_credit_amount,
>   hpi.reason_needed
> 
> from claim
> join qifinance.house_purchase_items hpi
>   on hpi.requested_rent_credit_amount is not null
>   and hpi.requested_rent_credit_amount > 0
> 
> on conflict (rent_credit_claim_id, house_purchase_item_id)
> do nothing;
> ```
> 
> ## View the rent credit total
> 
> ```sql
> select *
> from qifinance.v_rent_credit_claim_totals
> where claim_name = 'June 2026 House Safety and Repair Purchases';
> ```
> 
> ## The strategic wording
> 
> Don’t frame it as:
> 
> > “I deducted this from rent.”
> 
> Frame it as:
> 
> > “I purchased necessary household safety/repair items. I am requesting these be credited against the rent balance. Receipts and itemized list are available.”
> 
> Cleaner. Less fighty. More evidence-based.
> 
> ## Accounting truth
> 
> For anything you expect to be credited back, treat it as:
> 
> ```text
> Reimbursable House Purchase / Rent Credit Receivable
> ```
> 
> Not as a normal personal expense.
> 
> Because if the house owes you credit, then it is not just “money spent.” It is a claim. That distinction matters.
