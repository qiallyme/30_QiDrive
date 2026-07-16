---
layout: page
title: "Firefly Transactions Architecture"
slug: "firefly_transactions_architecture"
created_at: "2026-06-14 15:10:39"
updated_at: "2026-07-16T06:49:33-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-009.json"
template_key: master-template
date: 2026-06-14
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a2f0aa9-96d0-83ea-be42-eea16992d4e4"
canonical_ref: ""
---

# Firefly Transactions Architecture

## Overview
- **Date**: 2026-06-14 15:10:39
- **Conversation ID**: `6a2f0aa9-96d0-83ea-be42-eea16992d4e4`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> this is how all transactions are exported from firefly for i guess one of our financial tables should mirror this no?

### Assistant
> I’m going to inspect the Firefly CSV shape first, then I’ll give you the sane database answer—not just “copy the export,” because that’s how schemas become haunted houses.

### Assistant
> I found the important shape: this export is **1,210 transactions with 53 headers**, but most of those headers are Firefly/import metadata. The actual app-worthy core is much smaller: date, type, amount, description, source/destination accounts, category, budget/bill, tags, notes, and Firefly IDs.

### Assistant
> Yes — **but only as a raw/staging table, not the main financial brain.**
> 
> The right architecture is:
> 
> ## 1. Mirror Firefly exactly as a raw import table
> 
> Call it something like:
> 
> `qifinance.firefly_transactions_raw`
> 
> Purpose:
> 
> - Preserve the Firefly export exactly.
> - Re-import safely.
> - De-dupe using `import_hash_v2`, `journal_id`, or `external_id`.
> - Debug weird Firefly behavior later.
> - Avoid losing metadata.
> 
> Your export has:
> 
> - **1,210 transaction rows**
> - **53 headers**
> - Main transaction types:
>   - `Withdrawal`: 933
>   - `Deposit`: 274
>   - `Opening balance`: 2
>   - `Transfer`: 1
> - Amounts are **already signed**:
>   - withdrawals are negative
>   - deposits are positive  
>   So do **not** double-negate withdrawals. That’s a classic “oops, my budget is possessed” bug.
> 
> ## 2. Then transform into a clean canonical transaction table
> 
> Call that:
> 
> `qifinance.transactions`
> 
> This is the table your app should actually use.
> 
> Core fields should be more like:
> 
> | Canonical field | From Firefly |
> |---|---|
> | `transaction_date` | `date` |
> | `posted_at` | maybe same as `date` |
> | `amount` | `amount` |
> | `currency_code` | `currency_code` |
> | `transaction_type` | `type` |
> | `description` | `description` |
> | `source_account_name` | `source_name` |
> | `source_account_type` | `source_type` |
> | `destination_account_name` | `destination_name` |
> | `destination_account_type` | `destination_type` |
> | `category_name` | `category` |
> | `budget_name` | `budget` |
> | `bill_name` | `bill` |
> | `notes` | `notes` |
> | `external_id` | `external_id` |
> | `firefly_journal_id` | `journal_id` |
> | `firefly_group_id` | `group_id` |
> | `firefly_import_hash_v2` | `import_hash_v2` |
> 
> ## The move
> 
> Do **not** make the main table 53 Firefly-shaped columns. That would lock your whole system to Firefly’s export format.
> 
> Instead:
> 
> ```sql
> qifinance.import_batches
> qifinance.firefly_transactions_raw
> qifinance.transactions
> qifinance.accounts
> qifinance.categories
> qifinance.tags
> qifinance.transaction_tags
> ```
> 
> That gives you the best of both worlds:
> 
> - Firefly compatibility
> - clean app logic
> - future imports from Cash App, Chase, Lyft, Hertz, CSVs, Plaid, etc.
> - less schema rot
> 
> ## Important cleanup note
> 
> The file has a `recurrence_date` header, but every row appears to be one value short, meaning that last column is effectively blank/missing. Not fatal, but your importer should either:
> 
> - pad missing trailing columns, or
> - import into a forgiving raw table first.
> 
> Do **not** trust direct Supabase CSV import blindly on this file. It may choke because the header has 53 fields and rows read as 52 fields.
> 
> ## My recommendation
> 
> Use this as the base:
> 
> ```sql
> create schema if not exists qifinance;
> 
> create table if not exists qifinance.firefly_transactions_raw (
>   id uuid primary key default gen_random_uuid(),
>   import_batch_id uuid,
>   raw_row jsonb not null,
> 
>   firefly_user_id text,
>   firefly_group_id text,
>   firefly_journal_id text,
>   firefly_import_hash_v2 text,
>   external_id text,
> 
>   transaction_type text,
>   transaction_date timestamptz,
>   amount numeric(14,2),
>   currency_code text,
> 
>   description text,
>   source_name text,
>   source_type text,
>   destination_name text,
>   destination_type text,
> 
>   category text,
>   budget text,
>   bill text,
>   tags text,
>   notes text,
> 
>   created_at timestamptz default now()
> );
> 
> create unique index if not exists firefly_raw_import_hash_v2_uidx
> on qifinance.firefly_transactions_raw (firefly_import_hash_v2)
> where firefly_import_hash_v2 is not null;
> ```
> 
> Then your real app table:
> 
> ```sql
> create table if not exists qifinance.transactions (
>   id uuid primary key default gen_random_uuid(),
> 
>   source_system text not null default 'firefly',
>   source_record_id text,
>   import_batch_id uuid,
> 
>   transaction_date timestamptz not null,
>   amount numeric(14,2) not null,
>   currency_code text not null default 'USD',
> 
>   transaction_type text not null,
>   description text not null,
> 
>   source_account_name text,
>   source_account_type text,
>   destination_account_name text,
>   destination_account_type text,
> 
>   category_name text,
>   budget_name text,
>   bill_name text,
> 
>   notes text,
>   raw_tags text,
> 
>   firefly_journal_id text,
>   firefly_group_id text,
>   firefly_import_hash_v2 text,
> 
>   created_at timestamptz default now(),
>   updated_at timestamptz default now()
> );
> ```
> 
> ## Bottom line
> 
> Yes, mirror Firefly — **as raw intake.**
> 
> But your actual financial table should be cleaner and system-owned. Firefly is one source. Your database is the truth layer. Don’t let the export format become the architecture.

### User
> better yet can you help me use the importer exporter firefly see what all tags and cats and group and tables in there so we can use that as the starting base for our tags tables, cat tables, ect, and i have a few coas too i want to merge into one conocial system.

### Assistant
> Yes. This is the right move: **extract Firefly’s current vocabulary first**, then turn it into your canonical finance taxonomy instead of inventing a clean system in a vacuum. I’ll inspect the export for categories, tags, accounts, account groups, budgets, bills, and useful Firefly IDs, then map that into a merge-ready schema.

### Assistant
> The extraction already shows a useful truth: your Firefly file does **not** contain full Firefly master tables; it contains the values actually used on transactions. That’s still a strong starting base, but unused categories/tags/accounts would need Firefly’s API/exporter/DB to catch everything.

### Assistant
> Yes — and I went ahead and built the starter extract.
> 
> ## Files ready
> 
> - [Download the Excel workbook](sandbox:/mnt/data/firefly_qifinance_taxonomy_extract.xlsx)
> - [Download the CSV + SQL bundle](sandbox:/mnt/data/firefly_qifinance_taxonomy_extract_bundle.zip)
> 
> ## What I extracted from your Firefly export
> 
> Your file gave us the **used** vocabulary:
> 
> | Object | Found |
> |---|---:|
> | Transactions | 1,210 |
> | Categories used | 20 |
> | Tags used | 19 |
> | Accounts / counterparties used | 21 |
> | Budgets used | 1 |
> | Bills used | 1 |
> | Transaction group titles | 0 |
> 
> Important: this transaction export does **not** prove we captured every unused Firefly category, tag, account group, budget, bill, or rule. Firefly’s basic export page exports transactions, and the docs say command-line export options give more fine-grained control / other files. Firefly also has a JSON API, which is the better route for pulling master objects cleanly. citeturn336509search2turn336509search4
> 
> ## Workbook sheets included
> 
> - **Dashboard** — quick counts and top category usage.
> - **Categories** — current Firefly categories + canonical suggestions.
> - **Tags** — tag cleanup map.
> - **Accounts** — account/counterparty extraction.
> - **Account_Pairs** — source → destination patterns.
> - **Budgets_Bills** — budget and bill objects found.
> - **Transaction_Types** — withdrawal/deposit/transfer/opening balance summary.
> - **Field_Map** — where each Firefly export column should land.
> - **COA_Crosswalk** — the big one: starter crosswalk table for merging your other COAs.
> - **Canonical_Model** — rules for how QiFinance should treat accounts, tags, categories, budgets, bills.
> - **Table_Catalog** — starter canonical table list.
> 
> ## My read: the taxonomy is usable but dirty
> 
> The export confirms the current structure is partly good:
> 
> - `01_Income-Caregiver`
> - `06_Debt-Loans`
> - `04_FoodHousehold-Restaurants`
> - `10_Transfers-BankTransfer`
> 
> That matches your `##_Domain-Subcategory` direction.
> 
> But some legacy/noisy objects need mapping:
> 
> - `Fuel` → probably `03_Transportation-Gas`
> - `Rent Payment` → probably `02_Housing-RentMortgage`
> - `Transfer` → probably `10_Transfers-BankTransfer`
> - `Multiple` → needs split/review
> - `Uncategorized` → needs cleanup
> - `Data Import on 2026-05-24 @ 06:40` and `cash_app_report_1779621043015.csv` should **not** stay as semantic tags. They belong in import metadata.
> 
> Firefly categories, budgets, and tags are metadata attached to transactions/journals; budgets are specifically used to link withdrawals/spending, not income or transfers. So don’t make budget = category. That would be duplicate nonsense. citeturn336509search18turn336509search6
> 
> ## The canonical move
> 
> Use this order:
> 
> 1. **Firefly export → raw table**
> 2. **Extract used categories/tags/accounts**
> 3. **Load your other COAs into `COA_Crosswalk`**
> 4. **Map old COA names into canonical QiFinance objects**
> 5. **Only then seed `qifinance.categories`, `qifinance.tags`, `qifinance.accounts`, etc.**
> 
> The bundle includes a draft SQL file:
> 
> `qifinance_taxonomy_schema_draft.sql`
> 
> That gives you starter tables for:
> 
> ```text
> qifinance.import_batches
> qifinance.firefly_transactions_raw
> qifinance.transactions
> qifinance.accounts
> qifinance.counterparties
> qifinance.categories
> qifinance.tags
> qifinance.transaction_tags
> qifinance.budgets
> qifinance.bills
> qifinance.coa_crosswalk
> ```
> 
> Bottom line: **yes, Firefly becomes the starting seed — not the final truth.** The canonical system lives in the crosswalk. That’s how we avoid letting old imports, random tags, and Cash App chaos become your accounting architecture.

### User
> ok, yes all that makes sense so what am i putting in supabase. girl, should we maybe use the ide to populate and normalize categories, tags, ect, also found in the repo.

### Assistant
> Yes. Use the IDE, but with guardrails: let it **harvest and draft normalization**, not silently invent your accounting system. Supabase should get the canonical tables + raw import tables + crosswalks; the repo scan should feed those tables.

### Assistant
> Girl yes — **this is exactly where the IDE should help.** But don’t let it “freestyle accountant” your database. That’s how we end up with `Fuel`, `gas`, `Gas Money`, `transportation`, and `car stuff` all pretending to be different things. Absolutely not.
> 
> ## What goes in Supabase now
> 
> For now, put **three layers** in Supabase:
> 
> ```text
> qifinance
> ├─ raw import layer
> ├─ canonical finance layer
> └─ crosswalk / normalization layer
> ```
> 
> ## Layer 1 — Raw import layer
> 
> This preserves Firefly exactly.
> 
> Put these in Supabase:
> 
> ```text
> qifinance.import_batches
> qifinance.firefly_transactions_raw
> ```
> 
> Purpose:
> 
> - Track each CSV/API/Firefly import.
> - Preserve the original row as `jsonb`.
> - Keep Firefly IDs like `journal_id`, `group_id`, `import_hash_v2`.
> - Let us re-run normalization without re-importing everything.
> 
> This is your “do not lose evidence” layer.
> 
> ## Layer 2 — Canonical finance layer
> 
> This is the actual system your app should use.
> 
> Put these in Supabase:
> 
> ```text
> qifinance.transactions
> qifinance.accounts
> qifinance.counterparties
> qifinance.categories
> qifinance.tags
> qifinance.transaction_tags
> qifinance.budgets
> qifinance.bills
> ```
> 
> ### How they should behave
> 
> | Table | Meaning |
> |---|---|
> | `transactions` | Clean ledger entries |
> | `accounts` | Your money containers: Cash App, Chase, Cash, Lyft rental liability, etc. |
> | `counterparties` | People/vendors/entities: Lisa, Hertz, Cash App, Zech, restaurants |
> | `categories` | Main accounting bucket: income, debt, food, housing, transport |
> | `tags` | Flexible labels: `cashappborrow`, `lisa`, `hotel`, `repayment-overdraft` |
> | `transaction_tags` | Many-to-many bridge |
> | `budgets` | Spending control buckets |
> | `bills` | Recurring obligations |
> 
> Hard rule:
> 
> > **Category = primary accounting bucket. Tag = flexible context. Counterparty = who/what it involved. Account = where the money moved.**
> 
> Do not mix those, or the system turns into soup.
> 
> ## Layer 3 — Crosswalk / normalization layer
> 
> This is where your other COAs merge in.
> 
> Put these in Supabase:
> 
> ```text
> qifinance.coa_sources
> qifinance.coa_items_raw
> qifinance.coa_crosswalk
> qifinance.normalization_rules
> ```
> 
> This lets us say:
> 
> | Source value | Canonical object |
> |---|---|
> | `Fuel` | `03_Transportation-Gas` |
> | `Gas` | `03_Transportation-Gas` |
> | `Rent Payment` | `02_Housing-RentMortgage` |
> | `cash_app_report_1779621043015.csv` | import metadata, not a real tag |
> | `Data Import on 2026-05-24 @ 06:40` | import metadata, not a real tag |
> 
> That crosswalk is the boss. Not Firefly. Not old spreadsheets. Not random CSV chaos.
> 
> ## What to seed first
> 
> From the Firefly extract bundle, seed these first:
> 
> ```text
> categories.csv
> tags.csv
> accounts.csv
> budgets_bills.csv
> coa_crosswalk_template.csv
> ```
> 
> But I would **not** seed all tags as final canonical tags yet.
> 
> These should be downgraded to import metadata:
> 
> ```text
> Data Import on 2026-05-24 @ 06:40
> cash_app_report_1779621043015.csv
> ```
> 
> Those are not tags. Those are receipts of chaos. Useful, but not semantic.
> 
> ## Should the IDE populate and normalize from the repo?
> 
> Yes.
> 
> The IDE should scan the repo for:
> 
> ```text
> categories
> tags
> budgets
> bills
> COA
> chart of accounts
> Firefly
> MMEX
> Cash App
> income
> expense
> debt
> liability
> transfer
> ```
> 
> Then it should create **draft seed files and normalization reports**, not directly mutate the database.
> 
> The clean flow:
> 
> ```text
> Repo scan
> → extracted taxonomy candidates
> → normalization report
> → reviewed seed CSVs
> → Supabase seed files
> → migration/import script
> ```
> 
> Do **not** let the IDE connect to production Supabase and start writing live data. That’s too much power for a half-known taxonomy.
> 
> ## Folder structure I’d use in your Supabase repo
> 
> Inside:
> 
> ```text
> C:\QiLabs\20_QiSystem\50_data\supabase\qisupabase
> ```
> 
> Use:
> 
> ```text
> supabase/
> ├─ migrations/
> │  ├─ 20260614_create_qifinance_core.sql
> │  └─ 20260614_create_qifinance_taxonomy.sql
> ├─ seed/
> │  └─ qifinance/
> │     ├─ categories.csv
> │     ├─ tags.csv
> │     ├─ accounts.csv
> │     ├─ budgets.csv
> │     ├─ bills.csv
> │     ├─ coa_sources.csv
> │     ├─ coa_items_raw.csv
> │     ├─ coa_crosswalk.csv
> │     └─ normalization_rules.csv
> ├─ scripts/
> │  └─ qifinance/
> │     ├─ import_firefly_export.ts
> │     ├─ normalize_taxonomy.ts
> │     └─ load_seed_data.ts
> └─ docs/
>    └─ qifinance/
>       ├─ taxonomy_report.md
>       ├─ category_rules.md
>       └─ coa_merge_notes.md
> ```
> 
> ## My recommendation
> 
> Do this in this order:
> 
> ### Step 1 — Add schema migrations
> 
> Use the SQL draft from the bundle as the starter, but improve it with:
> 
> ```text
> coa_sources
> coa_items_raw
> normalization_rules
> ```
> 
> ### Step 2 — Add seed CSVs
> 
> Use the Firefly extract as the first seed source.
> 
> ### Step 3 — Have IDE scan repo
> 
> The IDE should find any other category/tag/COA systems already hiding in the repo.
> 
> ### Step 4 — Produce a normalization report
> 
> The report should say:
> 
> ```text
> Keep
> Merge
> Rename
> Move to metadata
> Needs review
> Delete / deprecated
> ```
> 
> ### Step 5 — Load reviewed seeds into Supabase
> 
> Only after that do we load canonical records.
> 
> ## Paste this into your IDE agent
> 
> ```text
> You are working inside the QiSystem Supabase project.
> 
> Project folder:
> C:\QiLabs\20_QiSystem\50_data\supabase\qisupabase
> 
> Goal:
> Create the starter QiFinance taxonomy and import structure for Supabase using Firefly export-derived categories, tags, accounts, budgets, bills, and future COA merge support.
> 
> Important rules:
> 1. Do not add real secrets, API keys, database URLs, service-role keys, passwords, or private credentials.
> 2. Do not connect to production Supabase.
> 3. Do not delete or rename existing migrations.
> 4. Do not rewrite existing migrations unless there is a syntax-breaking issue; report first.
> 5. Create safe migrations, seed files, scripts, and docs only.
> 6. Treat Firefly as one source system, not the final canonical truth.
> 7. Keep this GitHub-safe and migration-first.
> 
> Create or update the following structure:
> 
> supabase/migrations/
> supabase/seed/qifinance/
> supabase/scripts/qifinance/
> supabase/docs/qifinance/
> 
> Create draft migrations for the qifinance schema with these tables:
> 
> 1. qifinance.import_batches
> 2. qifinance.firefly_transactions_raw
> 3. qifinance.transactions
> 4. qifinance.accounts
> 5. qifinance.counterparties
> 6. qifinance.categories
> 7. qifinance.tags
> 8. qifinance.transaction_tags
> 9. qifinance.budgets
> 10. qifinance.bills
> 11. qifinance.coa_sources
> 12. qifinance.coa_items_raw
> 13. qifinance.coa_crosswalk
> 14. qifinance.normalization_rules
> 
> Design principles:
> 
> - firefly_transactions_raw should preserve raw rows as jsonb.
> - transactions should be the clean canonical ledger table.
> - categories should represent the primary accounting bucket.
> - tags should represent flexible contextual labels.
> - accounts should represent money containers.
> - counterparties should represent people, vendors, merchants, employers, agencies, or other entities.
> - coa_crosswalk should map old source category/tag/account/COA names into canonical objects.
> - normalization_rules should support rename, merge, ignore, metadata_only, and review actions.
> - Do not use PostgreSQL enums yet; use text fields plus indexes/check constraints where useful.
> - Add created_at and updated_at where appropriate.
> - Add normalized_key fields where useful.
> - Add uniqueness constraints that prevent duplicate canonical names/keys without blocking future imports.
> 
> Also scan the repository for existing finance/taxonomy/COA/category/tag references.
> 
> Search for terms including:
> - Firefly
> - MMEX
> - cash app
> - cashapp
> - transaction
> - category
> - categories
> - tag
> - tags
> - budget
> - bill
> - COA
> - chart of accounts
> - income
> - expense
> - debt
> - liability
> - transfer
> - rent
> - fuel
> - gas
> - loan
> - repayment
> 
> Output files:
> 
> 1. supabase/docs/qifinance/taxonomy_repo_scan.md
>    - List files inspected.
>    - List category/tag/account/COA-like values found.
>    - Mark likely duplicates.
>    - Mark values that should become import metadata instead of tags.
> 
> 2. supabase/seed/qifinance/categories.csv
>    - code
>    - domain
>    - subcategory
>    - canonical_name
>    - parent_code
>    - source_system
>    - status
>    - notes
> 
> 3. supabase/seed/qifinance/tags.csv
>    - tag_key
>    - display_name
>    - tag_type
>    - source_system
>    - status
>    - notes
> 
> 4. supabase/seed/qifinance/accounts.csv
>    - canonical_name
>    - account_type
>    - institution_name
>    - owner_scope
>    - source_system
>    - source_name
>    - status
>    - notes
> 
> 5. supabase/seed/qifinance/coa_sources.csv
>    - source_key
>    - display_name
>    - source_type
>    - notes
> 
> 6. supabase/seed/qifinance/coa_items_raw.csv
>    - source_key
>    - source_object_type
>    - source_code
>    - source_name
>    - parent_source_code
>    - notes
> 
> 7. supabase/seed/qifinance/coa_crosswalk.csv
>    - source_key
>    - source_object_type
>    - source_code
>    - source_name
>    - canonical_object_type
>    - canonical_key
>    - action
>    - confidence
>    - notes
> 
> 8. supabase/seed/qifinance/normalization_rules.csv
>    - source_system
>    - source_field
>    - raw_value
>    - normalized_value
>    - action
>    - canonical_object_type
>    - canonical_key
>    - confidence
>    - notes
> 
> 9. supabase/docs/qifinance/category_rules.md
>    Explain:
>    - Category = primary accounting bucket.
>    - Tag = flexible context.
>    - Account = money container.
>    - Counterparty = who/what the transaction involved.
>    - Budget = planning/control bucket.
>    - Bill = recurring obligation.
> 
> Use these initial known Firefly cleanup rules:
> 
> - "Data Import on 2026-05-24 @ 06:40" should be metadata_only, not a canonical tag.
> - "cash_app_report_1779621043015.csv" should be metadata_only, not a canonical tag.
> - "Fuel" should map to "03_Transportation-Gas" unless better evidence appears.
> - "Rent Payment" should map to "02_Housing-RentMortgage" unless better evidence appears.
> - "Transfer" should map to "10_Transfers-BankTransfer" unless better evidence appears.
> - "Multiple" should be marked review.
> - "Uncategorized" should be marked review.
> 
> Do not run database migrations.
> Do not run destructive commands.
> After creating files, print a summary of:
> - files created
> - tables defined
> - seed rows created
> - taxonomy conflicts found
> - values needing human review
> ```
> 
> ## The actual strategic answer
> 
> Yes, put this in Supabase.
> 
> Yes, use the IDE.
> 
> But the IDE’s job is **extraction + draft normalization**, not final judgment.
> 
> Your canonical taxonomy should come from the merge of:
> 
> ```text
> Firefly used values
> + repo-discovered values
> + your existing COAs
> + real-world transaction behavior
> ```
> 
> That becomes:
> 
> ```text
> QiFinance canonical taxonomy
> ```
> 
> Not “whatever Firefly happened to call it on June 14.”
