---
layout: page
title: "Organizing Financial Data"
slug: "organizing_financial_data"
created_at: "2026-05-29 00:12:20"
updated_at: "2026-05-29 00:12:20"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-008.json"
template_key: master-template
date: 2026-05-29
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a192024-33e0-83ea-9583-86171db3dcc9"
canonical_ref: ""
---

# Organizing Financial Data

## Overview
- **Date**: 2026-05-29 00:12:20
- **Conversation ID**: `6a192024-33e0-83ea-9583-86171db3dcc9`
- **Source**: `Chat-Export-28513-2026/conversations-008.json`

## Chat History

### User
> ok, i need your help i have all this old financial data like balance sheets, profit and loss statement, transaction records, bills, etc from previous years, I may very well need this data but also I dont want it distracting me and im getting frustrated, what should i do

### Assistant
> Yes. You need to **separate “archive value” from “active work.”** Right now old financial data is acting like a haunted junk drawer. It may matter later, but it does **not** deserve front-row attention.
> 
> Here’s the move.
> 
> ## The rule
> 
> Old financial data should be treated as **evidence + reference**, not active operating data.
> 
> Do **not** try to fully clean, categorize, or rebuild all of it right now. That is a trap. That is how you lose three days and come out with twelve “systems” and no current ledger. Absolutely not.
> 
> ## Create three buckets
> 
> ### 1. Active Finance System
> 
> This is only for **current year / current operating reality**.
> 
> Use this for:
> 
> - Current bank accounts
> - Current transactions
> - Current bills
> - Current debts
> - Current income
> - Current cash plan
> - Current budget
> - Current ledger
> 
> This is the system you actually work from.
> 
> Suggested folder:
> 
> `60_finance/10_active/2026_finance_ops/`
> 
> Or in QiNexus style:
> 
> `60_finance/10_active/2026_current_finance/`
> 
> ## 2. Historical Financial Archive
> 
> This is where old stuff goes. It is kept, indexed enough to find, but not cleaned unless needed.
> 
> Use this for:
> 
> - Old balance sheets
> - Old P&L statements
> - Prior-year tax docs
> - Old QuickBooks exports
> - bank statements from prior years
> - old bills
> - old invoices
> - old loan docs
> - prior business records
> 
> Suggested folder:
> 
> `60_finance/80_archive/`
> 
> Inside:
> 
> ```text
> 60_finance/
>   80_archive/
>     2019/
>     2020/
>     2021/
>     2022/
>     2023/
>     2024/
>     2025/
> ```
> 
> If you want it cleaner:
> 
> ```text
> 60_finance/
>   80_archive/
>     2022/
>       statements/
>       tax/
>       reports/
>       transactions/
>       bills/
>       receipts/
>       exports/
>     2023/
>       statements/
>       tax/
>       reports/
>       transactions/
>       bills/
>       receipts/
>       exports/
> ```
> 
> ## 3. Finance Intake / Sorting Pile
> 
> This is for messy unsorted financial documents you are not ready to process.
> 
> Suggested folder:
> 
> `60_finance/00_intake/`
> 
> Inside:
> 
> ```text
> 60_finance/
>   00_intake/
>     unsorted_finance_docs/
>     needs_review/
>     duplicate_check/
>     imported_exports/
> ```
> 
> This keeps the mess contained instead of splashing all over the system.
> 
> ## The practical workflow
> 
> Do this in order:
> 
> ### Step 1: Stop organizing by emotion
> 
> Do not open each file and spiral.
> 
> Make one folder:
> 
> `60_finance/00_intake/old_finance_dump_YYYY-MM-DD/`
> 
> Dump everything old there.
> 
> That alone gives your brain relief.
> 
> ### Step 2: Sort only by year first
> 
> Do not sort by vendor, account, category, tax type, “vibes,” or trauma signature. Year first. Always year first.
> 
> Example:
> 
> ```text
> 80_archive/
>   2021/
>   2022/
>   2023/
>   2024/
>   2025/
> ```
> 
> If you do not know the year, put it here:
> 
> ```text
> 80_archive/_unknown_year/
> ```
> 
> No shame folder. Just containment.
> 
> ### Step 3: Add basic document type folders
> 
> Only after year sorting:
> 
> ```text
> 2024/
>   bank_statements/
>   credit_cards/
>   reports/
>   tax/
>   bills/
>   receipts/
>   payroll_income/
>   exports/
>   legal_financial/
>   misc/
> ```
> 
> Do not overbuild this. These are enough.
> 
> ### Step 4: Make a simple archive index
> 
> You need one simple spreadsheet or NocoDB table called:
> 
> `finance_archive_index`
> 
> Columns:
> 
> | Field | Purpose |
> |---|---|
> | year | 2022, 2023, etc. |
> | source | QuickBooks, Chase, Cash App, IRS, vendor, etc. |
> | document_type | statement, P&L, balance sheet, bill, receipt |
> | account_or_business | which account/entity it belongs to |
> | date_range | Jan-Dec 2023, Q1 2024, etc. |
> | file_path | where it lives |
> | status | archived, needs review, duplicate, tax relevant |
> | notes | optional |
> 
> That’s it. Not a full accounting rebuild. Just a map.
> 
> ## What not to do
> 
> Do **not** rebuild old books unless there is a reason.
> 
> Only process historical data when it supports one of these:
> 
> 1. Tax filing or amendment  
> 2. Legal claim or evidence  
> 3. Debt/account dispute  
> 4. Business reconstruction  
> 5. Pattern analysis  
> 6. Asset/liability verification  
> 7. Audit/support documentation  
> 
> Otherwise, archive it and move on.
> 
> ## Recommended folder structure
> 
> Use this:
> 
> ```text
> 60_finance/
>   00_intake/
>     current_inbox/
>     old_finance_dump_2026-05-29/
>     needs_review/
>     duplicates/
> 
>   10_active/
>     2026_current_finance/
>       ledger/
>       bank_accounts/
>       bills/
>       income/
>       debts/
>       reports/
>       exports/
> 
>   20_statements/
>     bank/
>     credit_cards/
>     payment_apps/
> 
>   30_tax/
>     2022/
>     2023/
>     2024/
>     2025/
>     2026/
> 
>   40_business_finance/
>     qially/
>     ind_loop/
>     other_entities/
> 
>   70_reference/
>     chart_of_accounts/
>     category_map/
>     account_registry/
>     vendor_registry/
> 
>   80_archive/
>     2019/
>     2020/
>     2021/
>     2022/
>     2023/
>     2024/
>     2025/
>     _unknown_year/
> 
>   90_exports/
>     quickbooks/
>     firefly/
>     bank_exports/
>     csv_exports/
> ```
> 
> Clean, boring, stable. Exactly what finance needs.
> 
> ## The decision
> 
> Your old financial data is **not trash**. But it is also **not the mission today**.
> 
> The mission today is:
> 
> 1. Build current-year intake.
> 2. Preserve old data safely.
> 3. Index old data lightly.
> 4. Only deep-process historical records when there is a legal, tax, or accounting reason.
> 
> That keeps you from throwing away evidence, but also stops the archive from hijacking your nervous system.
> 
> ## Immediate next move
> 
> Create this folder right now:
> 
> ```text
> 60_finance/00_intake/old_finance_dump_2026-05-29/
> ```
> 
> Put all old financial files there.
> 
> Then create:
> 
> ```text
> 60_finance/80_archive/
> ```
> 
> Sort only by year.
> 
> Nothing else today unless a document is obviously urgent.

### User
> ok, I dont want it archived in the normal sense just i guess by year it good.

### Assistant
> Exactly. Don’t call it “archive” then. That word makes it feel buried/dead, and this data may still be useful.
> 
> Use **by-year historical finance library** instead.
> 
> ## Better structure
> 
> ```text
> 60_finance/
>   00_inbox/
>     unsorted_finance/
> 
>   10_current_year/
>     2026/
> 
>   20_financial_years/
>     2019/
>     2020/
>     2021/
>     2022/
>     2023/
>     2024/
>     2025/
>     2026/
> 
>   90_reference/
>     account_registry/
>     vendor_registry/
>     category_map/
> ```
> 
> ## Inside each year
> 
> Keep it simple:
> 
> ```text
> 2024/
>   01_statements/
>   02_transactions/
>   03_reports/
>   04_bills_invoices/
>   05_receipts/
>   06_tax_docs/
>   07_exports/
>   99_misc/
> ```
> 
> That gives you access without making it scream “old junk.”
> 
> ## Naming rule
> 
> Use this pattern when renaming matters:
> 
> ```text
> yyyy-mm-dd_source_documenttype_account_detail.ext
> ```
> 
> Examples:
> 
> ```text
> 2024-12-31_chase_statement_checking.pdf
> 2024-01-01_2024-12-31_quickbooks_profit-loss_qially.pdf
> 2023-04-15_verizon_bill_business-lines.pdf
> ```
> 
> ## The actual doctrine
> 
> Call the folder:
> 
> ```text
> 20_financial_years
> ```
> 
> Not archive.
> 
> Because the point is:
> 
> **“This is historical operating data, organized by year, available when needed, but not part of today’s active dashboard.”**
> 
> That’s the sweet spot. It gets out of your face without being shoved into a digital basement.

### User
> ok how can i quickly build those folders in the root i pick and also i need to merge COAs with firefly coas.

### Assistant
> Yes — this is two moves: build the year folders with one script, then merge your existing COA into Firefly as a mapping layer instead of brute-forcing everything manually.

### Assistant
> Yes. Do this fast and boring. Two separate tools:
> 
> 1. **Folder builder** = creates the year structure wherever you point it.
> 2. **COA merger** = creates a clean mapping between your old COA and Firefly categories/accounts.
> 
> Your uploaded COA already has useful account numbers and hierarchy, but it also has cleanup issues like duplicate account numbers and weird replacement text like `ServEntertainment-Gifts/Fee Income`, so we should **not blindly import it raw**. Use it as source material and merge carefully. fileciteturn0file0
> 
> ---
> 
> # 1. Quick folder builder
> 
> Use this PowerShell script on your PC.
> 
> Save as:
> 
> `build_finance_year_folders.ps1`
> 
> ```powershell
> # build_finance_year_folders.ps1
> # Purpose: Create finance year folders under a root folder the user selects.
> 
> param(
>     [Parameter(Mandatory=$true)]
>     [string]$RootPath,
> 
>     [int]$StartYear = 2019,
>     [int]$EndYear = 2026
> )
> 
> $foldersPerYear = @(
>     "01_statements",
>     "02_transactions",
>     "03_reports",
>     "04_bills_invoices",
>     "05_receipts",
>     "06_tax_docs",
>     "07_exports",
>     "08_supporting_docs",
>     "99_misc"
> )
> 
> $rootFolders = @(
>     "00_inbox\unsorted_finance",
>     "10_current_year",
>     "20_financial_years",
>     "90_reference\account_registry",
>     "90_reference\vendor_registry",
>     "90_reference\category_map"
> )
> 
> foreach ($folder in $rootFolders) {
>     $path = Join-Path $RootPath $folder
>     New-Item -ItemType Directory -Path $path -Force | Out-Null
> }
> 
> for ($year = $StartYear; $year -le $EndYear; $year++) {
>     $yearPath = Join-Path $RootPath "20_financial_years\$year"
>     New-Item -ItemType Directory -Path $yearPath -Force | Out-Null
> 
>     foreach ($subfolder in $foldersPerYear) {
>         New-Item -ItemType Directory -Path (Join-Path $yearPath $subfolder) -Force | Out-Null
>     }
> }
> 
> $currentYearPath = Join-Path $RootPath "10_current_year\$EndYear"
> New-Item -ItemType Directory -Path $currentYearPath -Force | Out-Null
> 
> Write-Host "Finance folder structure created at: $RootPath"
> ```
> 
> Run it like this:
> 
> ```powershell
> .\build_finance_year_folders.ps1 -RootPath "C:\QiNexus\60_finance" -StartYear 2019 -EndYear 2026
> ```
> 
> Change the root path to whatever folder you pick.
> 
> ---
> 
> # 2. Better folder structure
> 
> This is what it creates:
> 
> ```text
> 60_finance/
>   00_inbox/
>     unsorted_finance/
> 
>   10_current_year/
>     2026/
> 
>   20_financial_years/
>     2019/
>       01_statements/
>       02_transactions/
>       03_reports/
>       04_bills_invoices/
>       05_receipts/
>       06_tax_docs/
>       07_exports/
>       08_supporting_docs/
>       99_misc/
>     2020/
>     2021/
>     2022/
>     2023/
>     2024/
>     2025/
>     2026/
> 
>   90_reference/
>     account_registry/
>     vendor_registry/
>     category_map/
> ```
> 
> This avoids the “archive graveyard” feeling. It is just a **financial years library**.
> 
> ---
> 
> # 3. COA merge doctrine
> 
> Do **not** try to make Firefly perfectly mimic QuickBooks/QBO.
> 
> Firefly III is best for cashflow, budgeting, accounts, categories, tags, and reporting. Your old COA is more accounting/tax/bookkeeping oriented.
> 
> So the merge should be:
> 
> | Old COA Field | Firefly Equivalent |
> |---|---|
> | Assets | Asset accounts |
> | Liabilities | Liability accounts / debts |
> | Income accounts | Revenue categories |
> | Expense accounts | Expense categories |
> | Parent accounts | Category groups or naming prefixes |
> | Account number | External reference / sort code |
> | Tax category | Tag or metadata |
> | Personal vs Business | Tag, group, or separate category prefix |
> 
> The clean move is to create a **COA crosswalk**, not force one system into the other.
> 
> ---
> 
> # 4. COA crosswalk table
> 
> Create a CSV called:
> 
> `finance_coa_crosswalk.csv`
> 
> Columns:
> 
> ```text
> old_account_number
> old_full_name
> old_parent
> old_type
> old_detail_type
> firefly_object_type
> firefly_name
> firefly_group
> scope
> tax_line
> status
> notes
> ```
> 
> Example rows:
> 
> ```text
> B511,SchC:Auto:Fuel,SchC:Auto,Expenses,Other Expenses,category,Auto - Fuel,Business Auto,business,Schedule C,active,
> B512,SchC:Auto:Insurance,SchC:Auto,Expenses,Other Expenses,category,Auto - Insurance,Business Auto,business,Schedule C,active,
> P522,Pers:FoodGroceries,Pers:Food,Expenses,Other Expenses,category,Groceries,Personal Food,personal,,active,
> P571,Pers:UtilitiesInternet,Pers:Utilities,Expenses,Other Expenses,category,Internet,Personal Utilities,personal,,active,
> ```
> 
> This becomes your translation layer.
> 
> ---
> 
> # 5. Important cleanup before merging
> 
> Your COA needs a scrub pass before import.
> 
> Issues I can already see:
> 
> | Issue | Example | What to do |
> |---|---|---|
> | Broken text replacement | `ServEntertainment-Gifts/Fee Income` | Normalize to `Service/Fee Income` or similar |
> | Duplicate account number | `P110` appears for Retained Earnings and Pers:AssetsHome | Fix before import |
> | Weird typos | `Utilties`, `LEntertainment-Giftsnses` | Correct spelling |
> | Placeholder liabilities | `Personal Liability 1`, `Business Liability 1` | Keep as placeholders or replace with real creditor names |
> | Mixed personal/business | `SchC` and `Pers` in same COA | Keep scope field: business/personal |
> 
> Do **not** import the mess directly. It will poison the clean system. We use it as a controlled source.
> 
> ---
> 
> # 6. Merge strategy with Firefly
> 
> ## Firefly asset accounts
> 
> Create/import these as Firefly accounts:
> 
> - Checking accounts
> - Savings accounts
> - Cash App
> - PayPal
> - Credit cards
> - Loans
> - Cash accounts
> - Business bank accounts
> - Personal bank accounts
> 
> These are **real-world containers of money/debt**.
> 
> ## Firefly categories
> 
> Create/import these from your COA:
> 
> - Income categories
> - Expense categories
> - Tax deduction categories
> - Personal spending categories
> - Business spending categories
> 
> These are **what the money was for**.
> 
> ## Firefly tags
> 
> Use tags for things that cross categories:
> 
> - `business`
> - `personal`
> - `tax_relevant`
> - `schedule_c`
> - `legal`
> - `caregiving`
> - `joel_case`
> - `mom_care`
> - `qially`
> - `lyft`
> - `onlyfans`
> - `cash_advance`
> - `debt`
> 
> Tags are not redundant when used this way. Categories answer **what**. Tags answer **why / context / project / tax / legal relevance**.
> 
> ---
> 
> # 7. Fast merge workflow
> 
> Do this in this order:
> 
> ## Step 1
> 
> Export current Firefly categories/accounts.
> 
> Keep them as:
> 
> ```text
> firefly_categories_export.csv
> firefly_accounts_export.csv
> ```
> 
> ## Step 2
> 
> Clean your old COA into:
> 
> ```text
> old_coa_cleaned.csv
> ```
> 
> ## Step 3
> 
> Create:
> 
> ```text
> finance_coa_crosswalk.csv
> ```
> 
> This maps old names to Firefly names.
> 
> ## Step 4
> 
> Only import missing Firefly categories/accounts.
> 
> Do **not** duplicate things Firefly already has.
> 
> ## Step 5
> 
> Use crosswalk during transaction import.
> 
> That means when old bank data says:
> 
> `SchC:Auto:Fuel`
> 
> it maps to Firefly:
> 
> `Auto - Fuel`
> 
> with tags:
> 
> `business`, `schedule_c`, `vehicle`
> 
> ---
> 
> # 8. The shortcut version
> 
> For now, build Firefly categories around this simplified structure:
> 
> ## Business income
> 
> ```text
> Business Income
> Business Income - Tax
> Business Income - Accounting
> Business Income - General
> Business Income - IT
> Business Income - Other
> Tips Income
> Late Fee Income
> Refunds / Discounts
> ```
> 
> ## Business expenses
> 
> ```text
> Advertising
> Auto - Fuel
> Auto - Insurance
> Auto - Lease Payments
> Auto - Maintenance
> Auto - Registration
> Auto - Repairs
> Commissions
> Contract Labor
> Depreciation
> Insurance
> Legal & Professional
> Meals
> Office Expense
> Bank Fees
> Business Gifts
> Dues & Memberships
> Education
> Postage
> Software
> Subscriptions
> Interest
> Rent
> Repairs & Maintenance
> Supplies
> Taxes & Licenses
> Travel
> Travel - Lodging
> Travel - Meals
> Travel - Parking & Tolls
> Utilities
> Wages
> Uncategorized Business Expense
> ```
> 
> ## Personal income
> 
> ```text
> Personal Income - Wages
> Personal Income - Interest
> Personal Income - Dividends
> Personal Income - Other
> ```
> 
> ## Personal expenses
> 
> ```text
> Food - Groceries
> Food - Dining Out
> Health - Insurance
> Health - Medical
> Home - Insurance
> Home - Mortgage Interest
> Home - Repairs
> Home - Taxes
> Utilities - Electric
> Utilities - Water
> Utilities - Internet
> Utilities - Phone
> Transportation
> Subscriptions
> Self Care
> Gifts
> Entertainment
> Uncategorized Personal Expense
> ```
> 
> That is enough. Don’t overcook it.
> 
> ---
> 
> # 9. Recommended move
> 
> ## Risk Level
> 
> **Medium.**
> 
> The risk is not losing data. The risk is creating a tangled fake-accounting system that becomes impossible to trust.
> 
> ## Priority Order
> 
> 1. Build year folders.
> 2. Dump old data by year.
> 3. Export Firefly current accounts/categories.
> 4. Clean old COA.
> 5. Create COA crosswalk.
> 6. Import only missing Firefly categories/accounts.
> 7. Use crosswalk for old transaction imports.
> 
> ## Next 3 Actions
> 
> 1. Run the PowerShell folder builder on your chosen finance root.
> 2. Export Firefly categories/accounts.
> 3. Put your uploaded COA into `90_reference/category_map/old_coa_raw.csv`, then create a cleaned version beside it.
> 
> The smart move is: **folder structure first, COA crosswalk second, import third.** Otherwise Firefly becomes a junk drawer with a login screen.
