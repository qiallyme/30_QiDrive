---
layout: page
title: "Finzytrack Overview and Caution"
slug: "finzytrack_overview_and_caution"
created_at: "2026-06-18 17:42:14"
updated_at: "2026-07-18T11:03:16-04:00"
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
date: 2026-06-18
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a347443-00dc-83ea-a5aa-53406bcd2229"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Finzytrack Overview and Caution

## Overview
- **Date**: 2026-06-18 17:42:14
- **Conversation ID**: `6a347443-00dc-83ea-a5aa-53406bcd2229`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> https://finzytrack.com/

### Assistant
> I’ll treat this like a quick site triage: what it appears to be, whether it looks legitimate/safe, and what I’d avoid doing until verified.

### Assistant
> ## Finzytrack looks relevant — but don’t marry it yet.
> 
> It’s an **open-source desktop personal finance app** focused on privacy, local data, import, search, dashboards, SQL/Beancount queries, and optional AI. The big selling point is that your financial data lives locally in a **plain-text Beancount ledger**, not some locked SaaS database. citeturn754310view0turn716234view1
> 
> ### Why it fits your world
> 
> For **your personal finance / expense / dispute tracking**, this is very aligned:
> 
> | Need | Finzytrack fit |
> |---|---|
> | Import bank statements | Yes: OFX/QFX, CSV, Excel, PDF statements, emails, manual entry citeturn716234view1 |
> | Query finances | Yes: SQL + Beancount queries, plus AI assistant if configured citeturn716234view1 |
> | Avoid vendor lock-in | Strong: plain-text ledger file citeturn754310view0 |
> | Privacy | Strong claim: runs locally; no outbound requests unless you initiate email import or AI features citeturn716234view1 |
> | AI compatibility | Bring-your-own model, OpenAI-compatible, Anthropic, or local model citeturn754310view0 |
> 
> ### The catch
> 
> It is **young**. The GitHub repo shows only **12 stars**, **1 fork**, and latest release **v0.1.4 on June 18, 2026**. That screams “interesting project,” not “mission-critical accounting system.” citeturn716234view0
> 
> So: **good candidate, not your source of truth yet.**
> 
> ## Where it fits in QiLabs
> 
> I’d classify it like this:
> 
> ```text
> QiLabs
> └── 60_QiApp_QiLife
>     └── Finance
>         └── Finzytrack_Prototype
> ```
> 
> Or, if you are only studying it:
> 
> ```text
> QiLabs
> └── 20_QiSystem
>     └── 70_research
>         └── finance_tools
>             └── finzytrack_review.md
> ```
> 
> ## Strategic call
> 
> Use it as a **finance ledger layer**, not as the whole life database.
> 
> ### Keep Supabase/Directus as the real system truth
> 
> Finzytrack is for:
> 
> - bank transactions
> - expenses
> - income
> - reimbursement evidence
> - category analysis
> - dispute math
> - personal finance dashboards
> 
> Supabase/Directus is still for:
> 
> - people
> - cases/matters
> - evidence records
> - care logs
> - task/state tracking
> - system-wide memory/querying
> - cross-project source of truth
> 
> Don’t let a cute finance app hijack the architecture. It solves one slice.
> 
> ## My recommendation
> 
> **Yes, test it. Do not put real banking data into it first.**
> 
> Do this order:
> 
> 1. Install or clone it.
> 2. Create a fake/sample ledger.
> 3. Import a small sanitized CSV.
> 4. Test search, categories, dashboards, AI query behavior.
> 5. Only then decide whether it becomes your finance module.
> 
> The power move would be:
> 
> ```text
> Bank exports → Finzytrack/Beancount ledger → parsed summaries → Supabase finance tables → Directus interface
> ```
> 
> That gives you local-first finance plus your larger QiLabs query system. That is actually clean.

### User
> problem is how do i start inputing my transactions and debtsa nd accounts and stuff i have no ui to get started with supabase

### Assistant
> You’re hitting the exact gap: **Supabase is the engine, not the desk where you type receipts like a normal person.** The missing layer is an input/admin UI. That should be **Directus first**, not Supabase Studio.

### Assistant
> ## The answer: **Directus is your input UI. Supabase is not.**
> 
> You are correct: trying to start inside Supabase feels awful because Supabase is mostly:
> 
> - database
> - auth
> - API
> - storage
> - edge functions
> - SQL/backend stuff
> 
> It is **not** a comfortable day-to-day finance entry screen.
> 
> So the stack should be:
> 
> ```text
> Supabase = source-of-truth database
> Directus = human-friendly admin/input UI
> Finzytrack / Beancount = optional finance ledger/import layer
> Qi apps = future custom polished UI
> ```
> 
> Do **not** sit in Supabase SQL editor entering transactions. That is goblin behavior. We are not doing that.
> 
> ---
> 
> # What you need first
> 
> You need a **Finance Module** in Directus with a few clean collections.
> 
> Start with this, not some giant accounting monster:
> 
> ## 1. `finance_accounts`
> 
> This is where money lives or debt sits.
> 
> Examples:
> 
> | Account | Type |
> |---|---|
> | Chase Checking | checking |
> | Old National Checking | checking |
> | CashApp | cash_app |
> | Lyft/Hertz Rental | liability/vendor |
> | Credit Card | credit_card |
> | Mom Ledger | personal_ledger |
> | Comfort Keepers Claim | receivable/claim |
> 
> Fields:
> 
> ```text
> account_name
> account_type
> institution
> last_4
> owner
> current_balance
> currency
> status
> notes
> ```
> 
> ---
> 
> ## 2. `finance_transactions`
> 
> This is every money movement.
> 
> Examples:
> 
> | Date | Description | Amount | Account |
> |---|---:|---:|---|
> | 2026-06-18 | Check deposit | 7521.37 | Old National |
> | 2026-06-17 | Hertz charge | -296.00 | Lyft/Hertz Rental |
> | 2026-06-12 | Hotel | -84.00 | Chase |
> 
> Fields:
> 
> ```text
> transaction_date
> posted_date
> account
> merchant
> description
> amount
> direction
> category
> status
> source
> evidence_url
> notes
> is_disputed
> is_reimbursable
> related_case
> ```
> 
> Important: use **negative amounts for money out** and **positive amounts for money in**.
> 
> ---
> 
> ## 3. `finance_debts_obligations`
> 
> This is not individual transactions. This is the thing owed.
> 
> Examples:
> 
> | Obligation | Who Owes | Amount | Status |
> |---|---:|---:|---|
> | Hertz/Lyft disputed charges | Hertz/Lyft owes Cody | TBD | disputed |
> | Comfort Keepers unpaid wages | Employer owes Cody | TBD | claim |
> | Mom rent claim | disputed | 426.00 | disputed |
> | Jeep/title issue | asset/ownership issue | TBD | active |
> 
> Fields:
> 
> ```text
> obligation_name
> obligation_type
> owed_by
> owed_to
> original_amount
> current_amount
> due_date
> status
> priority
> related_account
> related_transactions
> evidence_url
> notes
> ```
> 
> This keeps debts clean instead of mixing them into transactions like spaghetti.
> 
> ---
> 
> ## 4. `finance_categories`
> 
> Simple categories for now.
> 
> Start with:
> 
> ```text
> income
> deposit
> rent
> food
> gas
> hotel
> car_rental
> insurance
> medical
> caregiving
> legal
> business
> utilities
> debt_payment
> reimbursement
> disputed_charge
> unknown
> ```
> 
> Do not overthink the chart of accounts yet. Get the data in. We can refine later.
> 
> ---
> 
> ## 5. `finance_import_batches`
> 
> This tracks where imported data came from.
> 
> Examples:
> 
> ```text
> Chase_June_2026_CSV
> Old_National_Deposit_2026-06-18
> Hertz_Lyft_Dispute_Charges
> Comfort_Keepers_Paychecks
> ```
> 
> Fields:
> 
> ```text
> batch_name
> source_account
> source_file
> import_date
> status
> notes
> ```
> 
> This matters because later when AI reviews your records, it can say:
> 
> > “This transaction came from Chase CSV batch June 2026, not manual memory.”
> 
> That is how you avoid future chaos.
> 
> ---
> 
> # Your immediate workflow
> 
> ## Step 1: Create the tables in Directus
> 
> In Directus:
> 
> ```text
> Settings → Data Model → Create Collection
> ```
> 
> Create these first:
> 
> ```text
> finance_accounts
> finance_transactions
> finance_debts_obligations
> finance_categories
> finance_import_batches
> ```
> 
> Do not create 40 tables yet. Five is enough.
> 
> ---
> 
> ## Step 2: Enter accounts first
> 
> Before transactions, add your accounts:
> 
> ```text
> Chase Checking
> Old National Checking
> CashApp
> Lyft/Hertz Rental
> Comfort Keepers Claim
> Mom Personal Ledger
> Cash
> ```
> 
> The account list becomes the dropdown for transactions.
> 
> ---
> 
> ## Step 3: Enter your first 10 transactions manually
> 
> Do not try to backfill your whole life today. That is how the system becomes another guilt pit.
> 
> Start with:
> 
> ```text
> Old National check deposit: 7521.37
> Any Chase recent charges
> Lyft/Hertz rental charges
> Hotel charges
> Comfort Keepers paychecks
> Money sent to mom
> Money received from mom
> ```
> 
> The goal is not perfection. The goal is to prove the workflow.
> 
> ---
> 
> ## Step 4: Add statuses
> 
> Every transaction should have a review state:
> 
> ```text
> unreviewed
> confirmed
> needs_receipt
> disputed
> reimbursable
> ignored
> ```
> 
> This is critical. You need to be able to dump messy data in without pretending it is clean.
> 
> ---
> 
> # The real model
> 
> Think of it like this:
> 
> ```text
> Accounts = containers
> Transactions = money movements
> Debts/Obligations = claims or balances
> Categories = meaning
> Import Batches = source trail
> Evidence = proof
> ```
> 
> That is the finance brain.
> 
> ---
> 
> # What I would **not** do
> 
> Do **not** start with:
> 
> - full double-entry accounting
> - giant chart of accounts
> - tax-grade bookkeeping
> - trying to reconcile every bank account perfectly
> - importing three years of statements immediately
> - building a custom app before Directus works
> 
> That is overbuilding. Directus is the training wheels and the admin cockpit. Use it.
> 
> ---
> 
> # The better path
> 
> ## Phase 1: Directus Manual Entry
> 
> Use Directus as the UI.
> 
> ```text
> You type accounts, debts, and important transactions manually.
> ```
> 
> ## Phase 2: CSV Import
> 
> Bank CSVs go into `finance_import_batches`, then transactions get reviewed.
> 
> ```text
> Bank CSV → staging/import batch → reviewed transactions
> ```
> 
> ## Phase 3: Rules
> 
> Create fuzzy rules later:
> 
> ```text
> If description contains “HERTZ” → category car_rental → disputed maybe
> If description contains “COMFORT KEEPERS” → category income
> If merchant = “LYFT” → category gig_income/platform
> ```
> 
> ## Phase 4: AI Layer
> 
> AI can query:
> 
> ```text
> Show all disputed Hertz charges.
> Show money sent to mom.
> Show unpaid Comfort Keepers wages.
> Show deposits over $1,000.
> Show transactions missing evidence.
> ```
> 
> That is the actual win.
> 
> ---
> 
> # The clean instruction for Codex / IDE
> 
> Give Codex this:
> 
> ```text
> Create a Directus-backed finance module using the existing Supabase Postgres database as the source of truth.
> 
> Build these collections:
> 
> 1. finance_accounts
> 2. finance_transactions
> 3. finance_debts_obligations
> 4. finance_categories
> 5. finance_import_batches
> 
> Use simple human-friendly fields first. Prioritize Directus usability over complex accounting purity.
> 
> Requirements:
> - finance_transactions must relate to finance_accounts.
> - finance_transactions must optionally relate to finance_categories and finance_import_batches.
> - finance_debts_obligations must optionally relate to finance_accounts and finance_transactions.
> - Add status fields for review workflow.
> - Add booleans for is_disputed and is_reimbursable.
> - Add notes and evidence_url fields.
> - Use positive amounts for money in and negative amounts for money out.
> - Keep the schema migration-friendly for later Supabase/AI querying.
> - Do not build a custom frontend yet.
> - The goal is immediate manual entry through Directus, then later CSV import and rule-based categorization.
> ```
> 
> ---
> 
> ## My blunt call
> 
> You were trying to use the **database like an app**.
> 
> That is why it felt blocked.
> 
> The correct move is:
> 
> ```text
> Directus first.
> Supabase underneath.
> Custom QiFinance app later.
> ```
> 
> Start with accounts and debts. Then enter only the most important current transactions. Backfill history after the workflow proves itself.

### User
> give me a prompt for google to build the app using supabase backend cloudflare frontend behind zerio trust for the accounting app i need, its not too complicated, accounts, categories, reports, dashboards, general ledger, bills, debts, assets, double entry accounting, shouldnt be too hard. also who owes me and who i owe like a ledger for personal debts too.

### Assistant
> You’re right that the feature set is “normal accounting app” territory, but **double-entry is where people casually build garbage**. The MVP needs one hard rule: every journal entry must balance before it saves.

### Assistant
> Here’s the prompt I’d give Gemini / Google AI Studio / Jules / whatever “Google builder” you’re using.
> 
> Copy this as the main build prompt:
> 
> :::writing{variant="standard" id="48291"}
> Build a private accounting and personal ledger web app called QiFinance.
> 
> The app should use:
> 
> - Supabase Postgres as the backend database
> - Supabase Storage for optional receipt/evidence uploads
> - Cloudflare Pages for the frontend
> - Cloudflare Workers for the API layer if needed
> - Cloudflare Zero Trust / Cloudflare Access protecting the app before login
> - TypeScript throughout
> - React + Vite for the frontend
> - Tailwind CSS for styling
> - Clean, simple dashboard UI
> - Mobile-friendly layout
> 
> Primary goal:
> Create a simple but correct accounting app for personal finances, debts, bills, assets, and double-entry bookkeeping. This is not a full enterprise ERP. Prioritize correctness, clarity, and usability.
> 
> Core modules:
> 
> 1. Dashboard
> - Net worth summary
> - Cash balance summary
> - Total debts owed by me
> - Total debts owed to me
> - Bills due soon
> - Recent transactions
> - Income vs expenses
> - Unreviewed items
> - Disputed/reimbursable items
> 
> 2. Accounts
> Support account types:
> - checking
> - savings
> - cash
> - credit_card
> - loan
> - asset
> - liability
> - income
> - expense
> - equity
> - receivable
> - payable
> 
> Fields:
> - id
> - name
> - account_type
> - institution
> - last_4
> - currency
> - opening_balance
> - current_balance
> - status
> - notes
> - created_at
> - updated_at
> 
> 3. Categories
> Support simple categories for transaction classification:
> - income
> - food
> - rent
> - utilities
> - gas
> - car
> - insurance
> - medical
> - legal
> - caregiving
> - debt_payment
> - reimbursement
> - disputed_charge
> - business
> - personal
> - unknown
> 
> Fields:
> - id
> - name
> - parent_category_id
> - category_type
> - notes
> 
> 4. General Ledger / Double Entry
> Use a real double-entry model.
> 
> Create:
> - journal_entries
> - journal_lines
> 
> journal_entries fields:
> - id
> - entry_date
> - description
> - memo
> - source
> - status: draft, posted, voided
> - related_person_id
> - related_bill_id
> - related_debt_id
> - related_asset_id
> - evidence_url
> - created_at
> - updated_at
> 
> journal_lines fields:
> - id
> - journal_entry_id
> - account_id
> - category_id
> - debit_amount
> - credit_amount
> - memo
> - created_at
> 
> Hard accounting rule:
> A journal entry cannot be posted unless total debit_amount equals total credit_amount.
> 
> Validation requirements:
> - debit_amount and credit_amount cannot both be positive on the same line
> - each journal entry must have at least two journal lines
> - total debits must equal total credits before posting
> - posted entries should not be directly edited; instead allow reversal or adjustment entries
> - draft entries can be edited
> 
> 5. Simple Transactions View
> Even though the backend uses double-entry, provide a user-friendly transaction form.
> 
> The simple transaction form should allow:
> - date
> - from account
> - to account
> - amount
> - merchant/person
> - category
> - description
> - status
> - receipt/evidence
> - disputed flag
> - reimbursable flag
> - notes
> 
> When saved, the app should automatically create a balanced journal entry with two journal lines.
> 
> Examples:
> - Spending $25 from Chase on food:
>   Debit Food Expense $25
>   Credit Chase Checking $25
> 
> - Receiving $500 income into Chase:
>   Debit Chase Checking $500
>   Credit Income $500
> 
> - Paying $100 toward a credit card:
>   Debit Credit Card Liability $100
>   Credit Chase Checking $100
> 
> 6. People / Parties
> Track who owes me and who I owe.
> 
> Create people table:
> - id
> - display_name
> - type: person, company, vendor, family, employer, platform, agency
> - email
> - phone
> - notes
> - status
> 
> 7. Personal Debts / IOUs
> Create debts table:
> - id
> - title
> - debt_type: owes_me, i_owe, disputed, reimbursement, claim, informal_ledger
> - person_id
> - original_amount
> - current_balance
> - currency
> - start_date
> - due_date
> - status: active, paid, disputed, forgiven, written_off
> - priority
> - notes
> - evidence_url
> 
> Debt requirements:
> - A debt should optionally connect to journal entries.
> - Payments toward a debt should reduce current_balance.
> - Allow a ledger view by person showing all debts, payments, adjustments, and notes.
> - Show “Who owes me” and “Who I owe” reports.
> 
> 8. Bills
> Create bills table:
> - id
> - vendor_id
> - title
> - amount
> - due_date
> - recurring_frequency: none, weekly, biweekly, monthly, yearly
> - status: upcoming, paid, overdue, cancelled
> - account_id
> - category_id
> - notes
> - evidence_url
> 
> Bill features:
> - upcoming bills list
> - overdue bills list
> - mark bill as paid
> - when bill is paid, create the related journal entry
> 
> 9. Assets
> Create assets table:
> - id
> - name
> - asset_type: vehicle, electronics, property, equipment, cash_value, other
> - purchase_date
> - purchase_price
> - estimated_value
> - account_id
> - status
> - notes
> - evidence_url
> 
> Asset features:
> - asset list
> - estimated total asset value
> - optional connection to debts, loans, and evidence
> 
> 10. Reports
> Build these reports:
> - Balance Sheet
> - Income Statement
> - General Ledger
> - Account Register
> - Trial Balance
> - Cash Flow Summary
> - Debts Owed To Me
> - Debts I Owe
> - Bills Due
> - Net Worth
> - Disputed / Reimbursable Items
> - Transactions Missing Evidence
> - Transactions Needing Review
> 
> 11. Import-ready design
> Prepare for future CSV import from banks, but do not build a complex importer yet.
> 
> Create import_batches table:
> - id
> - source_name
> - source_account_id
> - imported_file_name
> - import_date
> - status
> - notes
> 
> Transactions/journal entries should optionally link to import_batch_id.
> 
> 12. Evidence / Receipts
> Allow attaching receipt/evidence URLs to:
> - journal entries
> - debts
> - bills
> - assets
> - people
> 
> Use Supabase Storage or simple URL fields for MVP.
> 
> 13. Security
> The app is private.
> 
> Architecture:
> - Cloudflare Zero Trust protects access to the app.
> - The frontend is deployed on Cloudflare Pages.
> - If Supabase service role access is needed, use a Cloudflare Worker API. Never expose Supabase service role keys in the browser.
> - Browser should only use safe public anon keys if direct Supabase access is used.
> - Prefer RLS policies in Supabase.
> - Create migrations for all tables.
> - Use environment variables for all secrets.
> 
> 14. UI Requirements
> Create clean pages:
> 
> - /dashboard
> - /accounts
> - /transactions
> - /ledger
> - /debts
> - /people
> - /bills
> - /assets
> - /reports
> - /settings
> 
> Design style:
> - simple
> - fast
> - mobile-friendly
> - readable
> - not overdesigned
> - admin-dashboard style
> - clear tables
> - good filters
> - quick add buttons
> 
> 15. Filters/Search
> Add filtering by:
> - date range
> - account
> - person
> - category
> - status
> - disputed
> - reimbursable
> - missing evidence
> - amount range
> 
> 16. Status fields
> Use review workflow statuses where useful:
> - draft
> - unreviewed
> - reviewed
> - confirmed
> - needs_evidence
> - disputed
> - reimbursable
> - ignored
> - posted
> - voided
> 
> 17. Development output
> Please produce:
> 
> - Supabase SQL migrations
> - TypeScript database types
> - React components
> - Routing structure
> - API layer if needed
> - Environment variable example
> - Deployment notes for Cloudflare Pages
> - Notes for setting up Cloudflare Zero Trust Access
> - Seed data for example accounts/categories
> - Clear README
> 
> 18. MVP priority
> Build in this order:
> 
> Phase 1:
> - database schema
> - accounts
> - categories
> - people
> - debts
> - basic transaction entry
> - journal entries and journal lines
> - double-entry validation
> 
> Phase 2:
> - dashboard
> - account register
> - debts owed to me / debts I owe
> - bills
> - assets
> 
> Phase 3:
> - reports
> - evidence uploads
> - import batches
> - better filters
> 
> Do not overcomplicate the first version. But do not fake double-entry accounting. The ledger must balance.
> :::
> 
> ## My correction to your framing
> 
> “Shouldn’t be too hard” is half true.
> 
> The **screens** are easy.
> 
> The **accounting correctness** is the trap. If you build transactions first and try to bolt on double-entry later, you’ll make a mess.
> 
> Use this rule:
> 
> ```text
> Simple transaction form for humans.
> Double-entry journal under the hood.
> ```
> 
> That gives you ease without fake accounting cosplay.
