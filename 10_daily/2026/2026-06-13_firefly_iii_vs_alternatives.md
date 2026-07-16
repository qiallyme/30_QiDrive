---
layout: page
title: "Firefly III vs Alternatives"
slug: "firefly_iii_vs_alternatives"
created_at: "2026-06-13 16:07:22"
updated_at: "2026-06-13 16:07:22"
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
date: 2026-06-13
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a2dc67c-6530-83ea-b8f8-28bb692e2cf0"
canonical_ref: ""
---

# Firefly III vs Alternatives

## Overview
- **Date**: 2026-06-13 16:07:22
- **Conversation ID**: `6a2dc67c-6530-83ea-b8f8-28bb692e2cf0`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> what do you thhink about receipt wrangler, and what about ezbookkeeping or moneymatter and if we stay with firefly, read teh reddit they have some tips. https://www.reddit.com/r/selfhosted/comments/11w5068/firefly_iii_vs/

### Assistant
> I’ll sanity-check the actual projects plus that Reddit thread, then give you the practical stack call: what belongs in QiOS now, what’s a distraction, and what to test without overbuilding.

### Assistant
> Early read: Receipt Wrangler looks like **evidence capture**, not the finance brain. ezBookkeeping looks more serious than I expected. MoneyMatter looks shiny but still young, so I’m not trusting it as your main ledger yet.

### Assistant
> ## My call
> 
> **Stay with Firefly III as the finance ledger for now. Add Receipt Wrangler only if you need receipt capture/proof. Do not migrate to ezBookkeeping or MoneyMatter yet.**
> 
> Not because they’re bad. Because switching ledgers right now is a shiny-object trap.
> 
> Your actual problem is not “which finance app is prettiest?” Your problem is:
> 
> **capture → categorize → reconcile → attach proof → export/migrate later.**
> 
> Firefly already gives you the ledger/API/rules/import ecosystem. You need to make it usable, not restart the entire stack.
> 
> ---
> 
> ## The app-by-app verdict
> 
> | Tool | My verdict | Why |
> |---|---:|---|
> | **Firefly III** | **Keep as main ledger** | Powerful, self-hosted, API-driven, supports budgets/categories/tags, rules, reports, recurring transactions, Docker, multi-currency, and external import tools. It is heavier, but it fits your “system of record” brain better. citeturn265491view4 |
> | **Receipt Wrangler** | **Good add-on, not replacement** | It is for receipt capture: OCR/AI scanning, smart categorization, multi-user/collaborative tracking, email upload, bulk upload, dashboards, and “who owes who.” Great for evidence/proof. Not your accounting brain. citeturn265491view0turn265491view1 |
> | **ezBookkeeping** | **Best challenger** | Legit project. Lightweight, mobile/PWA-friendly, Docker, SQLite/MySQL/PostgreSQL, receipt recognition, MCP/AI integrations, strong import/export list including Firefly III. But switching now would cost focus. citeturn265491view2turn212929view2 |
> | **MoneyMatter** | **Watchlist, not core** | Looks modern and AI-forward, but it is early-access, its own site says bank connections currently support Monobank with more integrations coming, and the GitHub repo is young: 31 stars, 9 forks, latest release Jun. 12, 2026. Cool, not “trust my money system” mature yet. citeturn265491view3turn212929view1turn212929view3 |
> | **Maybe Finance** | **No-go for core** | Different from MoneyMatter. The Maybe repo says it is “no longer actively maintained.” Do not anchor QiOS finance on an abandoned upstream unless you deliberately choose a maintained fork. citeturn497523search0 |
> 
> ---
> 
> ## What the Reddit thread actually says
> 
> The Reddit signal is basically: **Firefly is powerful but fussy; Actual is easier; rules/import are the make-or-break layer.**
> 
> genui{"reddit":{"quotes":[{"refid":"turn623258view0","quote":"Firefly 3 had for me a little steep learning curve but it's quite powerful."},{"refid":"turn740147view0","quote":"I found Firefly a bit overcomplicated. The difference between budget and piggy banks wasn't clear to me and the number of steps to update a transaction was high."},{"refid":"turn740147view3","quote":"Unfortunately I switched over to Actual Budget. It was far far easier to spin up in Docker and has all the features I need for my personal use"}]}}
> 
> That lines up with what I’d expect. Firefly is not the “I just want cute budgeting” app. Firefly is the “I want a serious self-hosted money database with rules and imports” app. Annoying, but useful.
> 
> ---
> 
> ## The Firefly setup tips I’d actually use
> 
> ### 1. Do **not** manually enter every transaction
> 
> Use Firefly’s **Data Importer**. Official docs say importing requires the separate Firefly III Data Importer app, which connects to the Firefly API. citeturn476505search0
> 
> Your flow should be:
> 
> **Bank CSV / Cash App CSV / receipts → staging folder → importer/API → Firefly → rules → review queue**
> 
> Not “Cody becomes a human QuickBooks goblin at 2 a.m.”
> 
> ### 2. Use broad rules, not one rule per merchant
> 
> Reddit complaints were about needing too many rules. The fix is broad categories:
> 
> | Rule | Match examples |
> |---|---|
> | `Food - Fast Food` | McDonald’s, Wendy’s, Taco Bell, DoorDash |
> | `Gig Work - Fuel` | Shell, BP, Circle K, Marathon |
> | `Mom Care - Supplies` | Walgreens, CVS, Walmart pharmacy |
> | `Vehicle - Rental/Lyft/Hertz` | Hertz, Lyft Express, rental fees |
> 
> Firefly has a rule engine that automatically updates transactions when transactions are created or changed. citeturn476505search1
> 
> ### 3. Keep “tags” different from “categories”
> 
> Use **categories** for accounting buckets.
> 
> Use **tags** for cases/projects/evidence.
> 
> Example:
> 
> | Field | Example |
> |---|---|
> | Category | `Vehicle Rental` |
> | Tag | `Hertz Dispute` |
> | Tag | `Indy Stranded June 2026` |
> | Tag | `Lyft Express` |
> 
> This matters because categories answer: **where did the money go?**  
> Tags answer: **what story/case/project does this belong to?**
> 
> ### 4. Handle transfers carefully
> 
> One Reddit user complained about auto-imported transfers not matching correctly when the two bank descriptions differed. Firefly’s docs have a specific import-transfers page, so treat transfers as their own cleanup category, not as normal income/expense. citeturn740147view0turn476505search27
> 
> Your transfer categories should be boring:
> 
> - `Transfer - Internal`
> - `Transfer - Cash App`
> - `Transfer - Savings`
> - `Transfer - Reimbursement Pending`
> 
> ### 5. Don’t expect Firefly to be your forecasting engine
> 
> One Reddit comment says Firefly feels opinionated toward past-data tracking rather than future analysis. That is consistent with Firefly’s stated framing: knowing where money is going, tracking expenses/income, budgeting, reports, and control. citeturn740147view0turn265491view4
> 
> So: **Firefly = ledger/reconciliation.**  
> **QiLife/Supabase = forecasting, strategy, dispute math, “what happens next.”**
> 
> ---
> 
> ## The architecture I’d use for QiOS
> 
> ### Keep this clean:
> 
> ```text
> Receipt Wrangler / Paperless
>         ↓
> Evidence + receipt archive
>         ↓
> Firefly III
>         ↓
> Working ledger / categories / tags / rules
>         ↓
> Supabase later
>         ↓
> Canonical QiFinance database + dashboards + disputes + reports
> ```
> 
> ### Roles:
> 
> | Layer | Tool |
> |---|---|
> | Receipt/evidence capture | Paperless-ngx + maybe Receipt Wrangler |
> | Daily finance ledger | Firefly III |
> | Rule-based categorization | Firefly rules |
> | Import staging | CSV folder / scripts / Firefly Data Importer |
> | Long-term canonical database | Supabase |
> | Strategic dashboard | QiLife |
> 
> ---
> 
> ## My recommendation
> 
> ### Do this now
> 
> **Keep Firefly. Add a disciplined Firefly structure before adding more apps.**
> 
> Set up:
> 
> 1. **Accounts**
>    - Cash App
>    - Main Bank
>    - Credit Cards
>    - Cash
>    - Zai Ledger
>    - Mom Shared Expenses
>    - Gig Income
> 
> 2. **Categories**
>    - Income
>    - Gig Work
>    - Vehicle
>    - Housing
>    - Mom Care
>    - Medical
>    - Food
>    - Debt / Loans
>    - Legal / Dispute
>    - Transfer
> 
> 3. **Tags**
>    - `Hertz Dispute`
>    - `Lyft Express`
>    - `Mom Care`
>    - `Comfort Keepers`
>    - `Court Surplus`
>    - `Zai Ledger`
>    - `Shared Home`
>    - `Tax Evidence`
> 
> 4. **Receipt Wrangler**
>    - Only install if you want fast receipt capture and “who owes who.”
>    - Do **not** make it the ledger.
> 
> ### Do not do this yet
> 
> Do not move to MoneyMatter. Too young.
> 
> Do not move to ezBookkeeping unless Firefly becomes emotionally or operationally unworkable after a real 7-day test.
> 
> Do not run Firefly, ezBookkeeping, MoneyMatter, Actual, and Receipt Wrangler all at once. That is not a finance system. That is a Docker-powered anxiety terrarium.
> 
> ---
> 
> ## Final answer
> 
> **Firefly III stays. Receipt Wrangler can be the receipt/proof module. ezBookkeeping gets a parking-lot test later. MoneyMatter is watchlist only.**
> 
> The move is not “pick the prettiest app.”  
> The move is:
> 
> **Make Firefly boring, rule-based, importable, tagged, and export-ready.**

### User
> ok i need to probably just take advantage of the scan snap receipt scanner and have some system or flow to match receipt the the transaction in firefly or for cash transactions enter them in firefly.

### Assistant
> Yes. This is the right move: **use ScanSnap as the capture mouth**, Firefly as the ledger, and one small review queue to match receipts to transactions. I’ll give you a workflow that avoids double-entry hell.

### Assistant
> Yes. **This is exactly the right workflow.** ScanSnap should become your **receipt intake machine**, not another finance app rabbit hole.
> 
> ## The clean setup
> 
> Use this structure:
> 
> ```text
> ScanSnap
>   ↓
> Receipt Inbox
>   ↓
> Review / Match Queue
>   ↓
> Firefly III transaction
>   ↓
> Receipt archived as evidence
> ```
> 
> The rule is simple:
> 
> > **Every receipt either matches an existing Firefly transaction or creates a new cash/manual transaction.**
> 
> No receipt should just float around like financial confetti.
> 
> ---
> 
> # 1. Use ScanSnap for capture
> 
> ScanSnap Home can export receipt information as **CSV**, and its docs say the exported receipt data can be linked with other applications. Important catch: the receipt-info CSV does **not** export the receipt image itself, so you still need to save the actual scanned image/PDF separately. citeturn614408view2
> 
> Also, ScanSnap’s searchable PDF feature exists, but the ScanSnap FAQ says searchable PDF creation requires the document type to be set as **Documents**, not necessarily Receipts. So do not assume one magical receipt profile will do everything perfectly. Test it once and then lock the workflow. citeturn614408view3
> 
> ## Make two ScanSnap profiles
> 
> ### Profile A: `Receipts - Archive PDF`
> 
> Use this for the actual proof.
> 
> Save to:
> 
> ```text
> C:\QiLabs\50_QiNexus\My Drive\30_Finance\10_Receipts\00_Inbox
> ```
> 
> ### Profile B: `Receipts - CSV Export`
> 
> Use this when you want extracted receipt fields like merchant/date/amount.
> 
> Save CSV to:
> 
> ```text
> C:\QiLabs\50_QiNexus\My Drive\30_Finance\10_Receipts\05_ScanSnap_CSV
> ```
> 
> Do **not** get cute yet. One inbox. One CSV folder. Done.
> 
> ---
> 
> # 2. Use this file naming pattern
> 
> When scanned, rename receipts like this:
> 
> ```text
> YYYY-MM-DD_vendor_amount_payment-method_project-status.pdf
> ```
> 
> Examples:
> 
> ```text
> 2026-06-13_mcdonalds_12.47_cash_gig-work_needs-entry.pdf
> 2026-06-13_hertz_89.32_card-1234_lyft-express_needs-match.pdf
> 2026-06-12_walgreens_24.80_card-5678_mom-care_needs-match.pdf
> ```
> 
> Status suffixes:
> 
> | Status | Meaning |
> |---|---|
> | `needs-match` | Card/bank transaction should already exist in Firefly |
> | `needs-entry` | Cash transaction needs to be created manually |
> | `matched` | Receipt has been matched to Firefly |
> | `duplicate` | Keep or delete later |
> | `dispute` | Keep as evidence for Hertz/mom/legal/tax issue |
> 
> ---
> 
> # 3. Firefly matching rules
> 
> Firefly’s Data Importer can import CSV/CAMT files, run regularly, and supports automation through command line/API workflows. So bank/card transactions should mostly come in through import, not manual entry. citeturn932243view1
> 
> ## For card/bank transactions
> 
> Do this:
> 
> 1. Scan receipt.
> 2. Rename it.
> 3. Wait for bank/card transaction to appear in Firefly.
> 4. Match by:
>    - date
>    - amount
>    - merchant
>    - payment account
> 5. Add Firefly:
>    - category
>    - tags
>    - note with receipt path
>    - attachment, if practical
> 
> Example Firefly note:
> 
> ```text
> Receipt: 30_Finance/10_Receipts/20_Matched/2026/06/2026-06-13_hertz_89.32_card-1234_lyft-express_matched.pdf
> ```
> 
> Use Firefly’s attachment/search capability only if it stays smooth. Firefly search docs include attachment-related search like `has_attachments:true`, but I would still keep the canonical receipt copy in QiNexus/Paperless because app attachments can become annoying during migrations. citeturn368578search23
> 
> **Translation:** attach in Firefly when useful, but don’t make Firefly the only place the proof lives.
> 
> ---
> 
> # 4. For cash transactions
> 
> Cash is different. If there is no bank transaction, the receipt **creates** the Firefly transaction.
> 
> ## Cash receipt flow
> 
> 1. Scan receipt.
> 2. Rename with `_cash_`.
> 3. Create manual Firefly withdrawal from `Cash Wallet`.
> 4. Add:
>    - date
>    - merchant
>    - amount
>    - category
>    - tags
>    - receipt path in notes
> 5. Move receipt to matched folder.
> 
> Example:
> 
> ```text
> Cash Wallet → McDonald’s
> Amount: $12.47
> Category: Food / Meals
> Tags: Gig Work, Indy Trip, Tax Review
> Notes: Receipt: 30_Finance/10_Receipts/20_Matched/2026/06/...
> ```
> 
> ---
> 
> # 5. Folder structure I’d use
> 
> Keep it front-end friendly:
> 
> ```text
> 30_Finance
>   10_Receipts
>     00_Inbox
>     05_ScanSnap_CSV
>     10_Needs_Match
>     15_Needs_Cash_Entry
>     20_Matched
>       2026
>         06_June
>     30_Dispute_Evidence
>       Hertz
>       Mom_Care
>       Comfort_Keepers
>       Court_Surplus
>     90_Duplicates_Trash_Later
> ```
> 
> This gives you a simple daily ritual:
> 
> ```text
> Inbox → Needs Match / Needs Cash Entry → Matched / Dispute
> ```
> 
> That’s it. No labyrinth.
> 
> ---
> 
> # 6. Firefly categories vs tags
> 
> Do **not** blur these.
> 
> ## Categories = accounting bucket
> 
> Examples:
> 
> ```text
> Vehicle Rental
> Fuel
> Food
> Mom Care Supplies
> Medical
> Legal / Court
> Shared Home
> Debt Payment
> Gig Work Expense
> ```
> 
> ## Tags = story/project/evidence trail
> 
> Examples:
> 
> ```text
> Hertz Dispute
> Lyft Express
> Indy Stranded June 2026
> Mom Care
> Comfort Keepers
> Court Surplus
> Tax Evidence
> Zai Ledger
> Shared Home
> ```
> 
> So a Hertz receipt might look like:
> 
> | Firefly field | Value |
> |---|---|
> | Category | Vehicle Rental |
> | Tags | Hertz Dispute, Lyft Express, Indy Stranded June 2026 |
> | Notes | Receipt path |
> | Attachment | Optional PDF |
> 
> ---
> 
> # 7. The minimum viable daily workflow
> 
> Do this once a day or every few days:
> 
> ## Receipt review pass
> 
> | Question | Action |
> |---|---|
> | Was this paid by card/bank? | Move to `10_Needs_Match` |
> | Was this paid by cash? | Move to `15_Needs_Cash_Entry` |
> | Is this Hertz/mom/legal/tax proof? | Also copy/move to `30_Dispute_Evidence` |
> | Is it unreadable/duplicate? | Move to `90_Duplicates_Trash_Later` |
> 
> ## Firefly pass
> 
> 1. Open Firefly.
> 2. Search by amount/date.
> 3. Match receipt.
> 4. Add category/tags.
> 5. Paste receipt path into notes.
> 6. Move file to `20_Matched`.
> 
> ---
> 
> # 8. The “don’t waste your life” version
> 
> For now, do **manual matching**. Don’t build automation yet.
> 
> Automation comes later after you have maybe **50–100 receipts** and know the real patterns.
> 
> The first system should be boring:
> 
> ```text
> Scan → Rename → Match → Tag → Archive
> ```
> 
> Then later we can script:
> 
> ```text
> ScanSnap CSV + bank CSV → fuzzy match by date/amount/vendor → Firefly API update → move receipt
> ```
> 
> Firefly’s API is REST/JSON and intended to interact with most of Firefly’s data, so automation is possible later. citeturn368578search2
> 
> ---
> 
> # My recommendation
> 
> Set up the folder structure and use ScanSnap immediately.
> 
> **Do not install Receipt Wrangler yet.** Not until you prove ScanSnap + Firefly is missing something.
> 
> Your current best stack:
> 
> ```text
> ScanSnap = capture
> QiNexus/Paperless = evidence archive
> Firefly III = finance ledger
> Supabase later = canonical database/dashboard
> ```
> 
> The core rule:
> 
> > **If paid by card: match receipt to imported Firefly transaction.  
> > If paid by cash: receipt creates the Firefly transaction.**
> 
> That’s the whole system. Keep it that clean.
