---
layout: page
title: "Money Manager EX Plan"
slug: "money_manager_ex_plan"
created_at: "2026-04-29 01:28:37"
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
source_file: "Chat-Export-28513-2026/conversations-006.json"
template_key: master-template
date: 2026-04-29
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69f1a4f3-9fc4-83ea-a939-d950485b985b"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Money Manager EX Plan

## Overview
- **Date**: 2026-04-29 01:28:37
- **Conversation ID**: `69f1a4f3-9fc4-83ea-a939-d950485b985b`
- **Source**: `Chat-Export-28513-2026/conversations-006.json`

## Chat History

### User
> ok so im going to use money manager ex with its own database to track the home finances, because i need somwhere to do it and to track monies zai owes me because i cant get quicken and my mom does everythign in her head and spereadhseets aint cutting it. whats the plan.

### Assistant
> We’re making this operational, not cute. The goal is: one shared household finance ledger, clean categories, clear “who owes who,” and no spreadsheet chaos.

### Assistant
> Yes. **Money Manager EX is the right “good enough” tool here** because you need a practical ledger, not a whole finance empire.
> 
> The plan is to treat it like a **household operating ledger** with three jobs:
> 
> 1. Track household bills and spending.
> 2. Track reimbursements / money Zai owes you / money you owe anyone.
> 3. Give you a clean monthly truth report without relying on Mom’s memory or spreadsheet spaghetti.
> 
> ## Core Setup
> 
> Create **one MMEX database** called something like:
> 
> `Cody_Home_Finances.mmb`
> 
> Store it somewhere backed up, ideally:
> 
> `Google Drive / QiHome / Finance / MoneyManagerEX / Cody_Home_Finances.mmb`
> 
> But do **not** open the same database from multiple devices at the same time. That can corrupt it. One active user/device at a time.
> 
> ## Account Structure
> 
> Set up accounts based on how money actually moves.
> 
> ### Main Accounts
> 
> Create these:
> 
> | Account | Type | Purpose |
> |---|---:|---|
> | Cody Cash | Cash | Physical cash Cody handles |
> | Cody Checking | Checking | Your bank/debit spending |
> | Mom Cash | Cash | Cash Mom contributes/spends |
> | Mom Checking | Checking | Optional if you track her payments |
> | Zai Cash | Cash | Cash Zai gives/spends |
> | Zai Ledger | Asset or Cash | Tracks what Zai owes / pays |
> | Household Holding | Cash | Temporary shared money pool |
> | Reimbursements Receivable | Asset | Money owed back to you |
> | Bills Paid by Cody | Cash/Tracking | Optional staging account |
> 
> Keep it simple at first. Minimum viable version:
> 
> - Cody Checking
> - Cody Cash
> - Household Holding
> - Zai Ledger
> - Reimbursements Receivable
> 
> ## Categories
> 
> Do **not** overbuild categories. Start with practical categories you’ll actually use.
> 
> ### Income
> 
> - Income: Cody
> - Income: Mom Contribution
> - Income: Zai Contribution
> - Income: Reimbursement Received
> - Income: Surplus / Legal Funds
> - Income: Other
> 
> ### Housing
> 
> - Housing: Rent
> - Housing: Utilities - Electric
> - Housing: Utilities - Water
> - Housing: Internet
> - Housing: Phone
> - Housing: Insurance
> - Housing: Repairs
> - Housing: Household Supplies
> 
> ### Food / Household
> 
> - Food: Groceries
> - Food: Fast Food
> - Food: Household Shared
> - Household: Cleaning Supplies
> - Household: Furniture
> - Household: Laundry
> - Household: Pet Supplies
> 
> ### Transportation
> 
> - Transportation: Gas
> - Transportation: Jeep
> - Transportation: Plates / Registration
> - Transportation: Repairs
> - Transportation: Rideshare Work Expense
> 
> ### Gigi / Pets
> 
> - Pets: Food
> - Pets: Treats
> - Pets: Vet
> - Pets: Supplies
> - Pets: Grooming
> 
> ### Debt / Reimbursement
> 
> This is the important part.
> 
> - Reimbursement: Zai Owes Cody
> - Reimbursement: Mom Owes Cody
> - Reimbursement: Cody Owes Mom
> - Reimbursement: Cody Owes Zai
> - Reimbursement: Paid Back
> - Reimbursement: Forgiven / Adjusted
> 
> ### Legal / Admin
> 
> - Legal: Court Filing
> - Legal: Printing / Mailing
> - Legal: Transportation
> - Admin: Documents
> - Admin: Subscriptions
> - Admin: Miscellaneous
> 
> ## How to Track “Zai Owes Me”
> 
> This is the key workflow.
> 
> When you pay for something Zai is supposed to repay:
> 
> **Example:** You pay $95 for Jeep plates that Zai owes back.
> 
> Enter transaction from **Cody Checking**:
> 
> - Payee: BMV / Plates
> - Category: `Reimbursement: Zai Owes Cody`
> - Amount: `$95`
> - Notes: `Jeep plates - Zai to repay Cody`
> 
> Then also record it in **Zai Ledger** as a debt marker.
> 
> Simpler method:
> 
> Use **one category report** to track all `Reimbursement: Zai Owes Cody`.
> 
> Better method:
> 
> Create a separate **Zai Ledger account** and enter:
> 
> - Deposit into Zai Ledger: `$95`
> - Category: `Reimbursement: Zai Owes Cody`
> - Notes: `Owes Cody for Jeep plates`
> 
> When Zai pays you back:
> 
> In Cody Checking/Cash:
> 
> - Payee: Zai
> - Category: `Reimbursement: Paid Back`
> - Amount: `$95`
> - Notes: `Repayment for Jeep plates`
> 
> Then in Zai Ledger:
> 
> - Withdrawal: `$95`
> - Notes: `Paid back`
> 
> The balance of **Zai Ledger** becomes the running amount he owes you.
> 
> That’s the cleanest way.
> 
> ## Monthly Household Bill Setup
> 
> Use recurring transactions for predictable bills.
> 
> Based on what we discussed before, start with:
> 
> | Bill | Estimated Amount | Responsible Lane |
> |---|---:|---|
> | Rent | $1,250 | Household |
> | Electric | $300 | Mom / Household |
> | Water | $120 | Household |
> | Internet | $55 | Cody/Admin |
> | Insurance | $20 | Household |
> | Household Supplies | $150 | Shared |
> | Phone | Add actual amount | Whoever pays |
> | Pet/Gigi Care | Add actual amount | Household/Pet lane |
> 
> Create these as recurring monthly transactions even if the amount changes. You can edit the exact amount when paid.
> 
> ## Household Split Method
> 
> Do **not** try to make MMEX do emotional math. Decide the rule first.
> 
> Use one of these:
> 
> ### Option A — Equal Split
> 
> Everyone shares household bills evenly.
> 
> Good for fairness. Bad if incomes are uneven.
> 
> ### Option B — Assigned Lanes
> 
> Each person owns certain categories.
> 
> This fits your house better.
> 
> Example:
> 
> | Person | Lane |
> |---|---|
> | Cody | IT/admin/legal, tracking, internet, documents |
> | Mom | Main monthly bills/groceries |
> | Zai | Cars, maintenance, pet support, errands |
> 
> ### Option C — Hybrid
> 
> Best option.
> 
> Shared bills are split, but certain people own specific lanes.
> 
> Use this:
> 
> - Rent/utilities = shared household
> - Car/Jeep = Zai lane unless otherwise agreed
> - Legal/admin = Cody lane unless household-related
> - Groceries = shared unless personal
> - Gigi = shared or assigned depending on actual agreement
> 
> ## Weekly Workflow
> 
> Do this once per week, not daily unless something major happens.
> 
> ### Sunday or Monday Finance Reset
> 
> Open MMEX and enter:
> 
> 1. Bills paid.
> 2. Cash spent.
> 3. Money borrowed/lent.
> 4. Receipts that matter.
> 5. What Zai owes.
> 6. What Mom paid from memory.
> 
> Then generate/check:
> 
> - Spending by category
> - Upcoming bills
> - Zai Ledger balance
> - Household Holding balance
> - Reimbursement Receivable balance
> 
> ## Naming Rules for Payees
> 
> Keep payees consistent or reports turn into garbage.
> 
> Use clean payee names:
> 
> - Walmart
> - Dollar General
> - BMV
> - CenterPoint
> - Evansville Water
> - Spectrum / Internet Provider
> - Landlord
> - Zai
> - Mom
> - Cody
> - Cash Withdrawal
> - Household Transfer
> 
> Do **not** use messy payees like:
> 
> - “walmart again”
> - “zai thing”
> - “mom paid me”
> - “that bill”
> 
> That’s how databases become haunted.
> 
> ## Transaction Notes Format
> 
> Use this simple note format:
> 
> `Who / What / Why / Repay?`
> 
> Examples:
> 
> `Zai / Jeep plates / needed to avoid tow / repay by June`
> 
> `Mom / groceries / shared household / no repayment`
> 
> `Cody / filing fee / foreclosure case / legal expense`
> 
> ## Monthly Report
> 
> At the end of each month, export or screenshot:
> 
> 1. Total household spending.
> 2. Bills paid.
> 3. Bills still due.
> 4. Zai balance owed.
> 5. Mom balance owed, if any.
> 6. Cody out-of-pocket household support.
> 7. Cash on hand / upcoming pressure points.
> 
> Call it:
> 
> `2026-04_Household_Finance_Report`
> 
> Save it in:
> 
> `QiHome / Finance / Monthly Reports /`
> 
> ## Immediate Setup Checklist
> 
> Do this in order:
> 
> ### Step 1 — Create the database
> 
> Name:
> 
> `Cody_Home_Finances.mmb`
> 
> ### Step 2 — Create accounts
> 
> Minimum:
> 
> - Cody Checking
> - Cody Cash
> - Household Holding
> - Zai Ledger
> - Reimbursements Receivable
> 
> ### Step 3 — Create categories
> 
> Start with:
> 
> - Housing
> - Utilities
> - Food
> - Household
> - Transportation
> - Pets
> - Legal
> - Admin
> - Reimbursement
> 
> ### Step 4 — Enter current known balances
> 
> Do not overthink historical cleanup.
> 
> Start with today’s truth.
> 
> - Current cash
> - Current checking
> - Current amount Zai owes
> - Current bills due
> - Current rent/utilities situation
> 
> ### Step 5 — Enter known debts
> 
> Add every current “Zai owes me” item as its own transaction.
> 
> Example:
> 
> | Item | Amount | Category |
> |---|---:|---|
> | Jeep plates | $95 | Reimbursement: Zai Owes Cody |
> | Food/water loan | whatever amount | Reimbursement: Zai Owes Cody |
> | Phone/internet help | amount | Reimbursement: Zai Owes Cody |
> 
> ### Step 6 — Set recurring bills
> 
> Add rent, utilities, internet, phone, insurance, pet needs, and major household expenses.
> 
> ### Step 7 — Start fresh from now
> 
> Do **not** try to perfectly reconstruct the past unless needed.
> 
> That’s the trap. We only backfill what affects current balances.
> 
> ## The Rule
> 
> MMEX is now the **truth ledger**.
> 
> Mom can still think in her head. Zai can still “remember different.” Cute. Doesn’t matter.
> 
> If it is not in the ledger, it is not settled.
> 
> Your operating sentence:
> 
> > “I’m not arguing memory anymore. I’m tracking the household ledger so we can all stay clear.”
> 
> ## Best Starting Structure
> 
> Use this setup:
> 
> ```text
> MoneyManagerEX
> └── Cody_Home_Finances.mmb
>     ├── Accounts
>     │   ├── Cody Checking
>     │   ├── Cody Cash
>     │   ├── Household Holding
>     │   ├── Zai Ledger
>     │   └── Reimbursements Receivable
>     │
>     ├── Categories
>     │   ├── Housing
>     │   ├── Utilities
>     │   ├── Food
>     │   ├── Household
>     │   ├── Transportation
>     │   ├── Pets
>     │   ├── Legal
>     │   ├── Admin
>     │   └── Reimbursement
>     │
>     └── Monthly Reports
>         ├── Bills Paid
>         ├── Bills Due
>         ├── Shared Expenses
>         └── Zai Balance Owed
> ```
> 
> ## Bottom Line
> 
> This is the right move.
> 
> Do not make it perfect. Make it **usable**.
> 
> Your first mission is only this:
> 
> **By tonight, MMEX should answer one question: “What does Zai currently owe Cody?”**
> 
> Everything else can mature after that.

### User
> how about we do just clearing accounts, cody clearing, mom clearing, zai clearning, home clearning or something like that,

### Assistant
> Yes — **that’s actually cleaner for your brain**.
> 
> Use **clearing accounts** as “buckets of responsibility,” not fake bank accounts. This lets you track who fronted what, who owes what, and what belongs to the house without needing Quicken-level nonsense.
> 
> ## Recommended MMEX Account Setup
> 
> Create these accounts:
> 
> | Account | Purpose |
> |---|---|
> | **Cody Clearing** | Anything Cody pays, fronts, receives, or is owed |
> | **Mom Clearing** | Anything Mom pays, fronts, receives, or is owed |
> | **Zai Clearing** | Anything Zai pays, fronts, receives, or owes |
> | **Home Clearing** | Shared household bills, groceries, rent, utilities, supplies |
> | **Cash on Hand** | Optional, only if you care about physical cash |
> | **Bank / Card Actual** | Optional, only if you want real account balances too |
> 
> Honestly? Start with just:
> 
> ```text
> Cody Clearing
> Mom Clearing
> Zai Clearing
> Home Clearing
> ```
> 
> That’s enough.
> 
> ## The Logic
> 
> Think of it like this:
> 
> - **Home Clearing** = the household itself
> - **Cody Clearing** = Cody’s side of the ledger
> - **Mom Clearing** = Mom’s side
> - **Zai Clearing** = Zai’s side
> 
> When someone pays for a shared thing, you record:
> 
> > Person paid → Home benefited
> 
> When someone owes someone else, you record:
> 
> > Person’s clearing balance shows the obligation
> 
> ## Best Way to Use It
> 
> ### Example 1: Cody pays rent for the house
> 
> Transaction:
> 
> | Field | Entry |
> |---|---|
> | From | Cody Clearing |
> | To / Category | Home Clearing or Housing: Rent |
> | Amount | $1,250 |
> | Note | Cody paid rent for household |
> 
> This shows Cody carried that cost.
> 
> ### Example 2: Zai owes Cody $80
> 
> Record it in **Zai Clearing**:
> 
> | Field | Entry |
> |---|---|
> | Account | Zai Clearing |
> | Payee | Cody |
> | Category | Owes Cody |
> | Amount | $80 |
> | Note | Zai owes Cody for [reason] |
> 
> Or, cleaner:
> 
> Transfer:
> 
> ```text
> Zai Clearing → Cody Clearing
> $80
> Note: Zai owes Cody for [item]
> ```
> 
> This makes Cody’s side increase and Zai’s side decrease.
> 
> ### Example 3: Zai pays Cody back $40
> 
> Transfer:
> 
> ```text
> Cody Clearing → Zai Clearing
> $40
> Note: Partial repayment from Zai
> ```
> 
> Depending on how MMEX displays signs, you may need to flip direction after testing once.
> 
> The core truth: **one direction means debt created, opposite direction means repayment.**
> 
> ## Use Home Clearing for Shared Stuff
> 
> ### Cody buys groceries for everyone
> 
> ```text
> Cody Clearing → Home Clearing
> $65
> Category: Food: Groceries
> Note: Shared groceries
> ```
> 
> ### Mom pays electric
> 
> ```text
> Mom Clearing → Home Clearing
> $280
> Category: Utilities: Electric
> Note: April electric paid by Mom
> ```
> 
> ### Zai buys dog food
> 
> ```text
> Zai Clearing → Home Clearing
> $45
> Category: Pets: Gigi Food
> Note: Shared pet expense
> ```
> 
> Now you can see who is actually carrying the home.
> 
> ## Categories Still Matter
> 
> Accounts answer:
> 
> > **Who touched the money?**
> 
> Categories answer:
> 
> > **What was the money for?**
> 
> So keep categories simple:
> 
> ```text
> Housing
>   Rent
>   Repairs
> 
> Utilities
>   Electric
>   Water
>   Internet
>   Phone
> 
> Food
>   Groceries
>   Fast Food
>   Household Shared
> 
> Transportation
>   Gas
>   Jeep
>   Repairs
>   Registration
> 
> Pets
>   Gigi Food
>   Gigi Treats
>   Vet
>   Supplies
> 
> Reimbursement
>   Zai Owes Cody
>   Mom Owes Cody
>   Cody Owes Mom
>   Paid Back
> 
> Admin
>   Printing
>   Documents
>   Subscriptions
> 
> Legal
>   Filing Fees
>   Mailing
>   Copies
> ```
> 
> ## The One Rule That Keeps This Clean
> 
> Do **not** mix real bank accuracy with household fairness at first.
> 
> This setup is not trying to reconcile Chase/Cash App down to the penny.
> 
> It is trying to answer:
> 
> ```text
> Who paid?
> For what?
> Was it shared?
> Does anyone owe anyone?
> What is still unpaid?
> ```
> 
> That is the mission.
> 
> ## My Preferred Setup for You
> 
> Use this:
> 
> ```text
> ACCOUNTS
> 
> Cody Clearing
> Mom Clearing
> Zai Clearing
> Home Clearing
> Cash Drawer
> ```
> 
> Optional later:
> 
> ```text
> Cody Checking
> Cash App
> Mom Checking
> Zai Cash
> ```
> 
> But not yet. Don’t let the database become a tiny government.
> 
> ## How to Interpret Balances
> 
> This part matters.
> 
> You need to decide what positive/negative means.
> 
> I’d use:
> 
> ```text
> Positive balance = person has contributed / is owed credit
> Negative balance = person owes / has been covered by others
> ```
> 
> So if Cody fronts $100 for Zai:
> 
> ```text
> Zai Clearing = -100
> Cody Clearing = +100
> ```
> 
> Nice and obvious.
> 
> ## Naming Convention
> 
> Use consistent account names:
> 
> ```text
> CLEARING - Cody
> CLEARING - Mom
> CLEARING - Zai
> CLEARING - Home
> ```
> 
> That will keep them grouped together.
> 
> Better than:
> 
> ```text
> Cody clearing
> mom clear
> zai clearning
> home account thing
> ```
> 
> No haunted database. We are adults today, unfortunately.
> 
> ## Starting Move
> 
> Create only these four:
> 
> ```text
> CLEARING - Cody
> CLEARING - Mom
> CLEARING - Zai
> CLEARING - Home
> ```
> 
> Then enter opening balances:
> 
> ```text
> CLEARING - Cody: 0
> CLEARING - Mom: 0
> CLEARING - Zai: amount he currently owes as negative
> CLEARING - Home: 0
> ```
> 
> Example:
> 
> If Zai owes you $220 right now:
> 
> ```text
> CLEARING - Cody: +220
> CLEARING - Zai: -220
> ```
> 
> Or enter one transfer/debt transaction:
> 
> ```text
> Transfer: CLEARING - Zai → CLEARING - Cody
> Amount: 220
> Note: Opening balance - Zai owes Cody as of 2026-04-29
> ```
> 
> ## Final Answer
> 
> Yes. Use clearing accounts.
> 
> This is the clean version:
> 
> ```text
> CLEARING - Cody
> CLEARING - Mom
> CLEARING - Zai
> CLEARING - Home
> ```
> 
> Then every transaction gets two labels:
> 
> ```text
> Account = who is financially affected
> Category = what the money was for
> Note = why it matters
> ```
> 
> Your first database goal stays the same:
> 
> **Make MMEX show what Zai owes Cody without a debate, memory fog, or “I thought you meant…” theater.**

### User
> ok lets start with may monthlys lets get those entered first. also is there a way to run this app on the web? 

> Money Manager Ex

> • Version: 1.9.2 64-bit

> • Built on: Jan 20 2026 16:00:01

> • Database version: 21 (aes256cbc-hmac-sha512)

> • Git commit: 96c3984 (2026-01-20)

> MMEX is using the following support products:

> • wxWidgets 3.3.1 (wxMSW 10.0)

> • wxSQLite3 4.9.1 (SQLite 3.40.0)

> • RapidJSON 1.1.0

> • Lua 5.3.5

> • libcurl/8.5.0-DEV Schannel

> • gettext 0.22.5

> • apexcharts.js

> Built with:

> • CMake 4.1.0

> • MSBuild 17.14.23.42201

> • Microsoft Visual Studio 17.0

> • Microsoft Visual C++ 19.44.35219.0

> • Windows SDK 10.0.26100.0

> Running on:

> • Windows 11 (build 29570), 64-bit edition

> • System Locale: 

> • User Interface Language: en_US.windows-1252

> • 1920x1080 32-bit 96x96ppi

### Assistant
> Good. We’ll build May as the baseline month first, not reconstruct all history. I’ll also check the web-app question against the current MMEX project info so we don’t invent features.

### Assistant
> Yes — start with **May Monthlies** first. That becomes the operating baseline.
> 
> ## First: Web version answer
> 
> **Kind of, but not the way you probably mean.**
> 
> MMEX has a separate **Money Manager EX WebApp**, but it is **not a full web version of the desktop app**. It mainly lets you enter “transaction reminders” from a browser, then the desktop app later downloads/reviews them. The official GitHub description says the WebApp lets you insert new transactions from any device/browser, but those entries are reviewed later in the desktop version. citeturn887608search4
> 
> So the real answer:
> 
> | Option | Verdict |
> |---|---|
> | Full MMEX in browser | **No, not really** |
> | Enter quick transactions from browser | **Yes, with WebApp** |
> | Use Android/iOS app | **Yes** |
> | Sync database through Google Drive/OneDrive/Dropbox/Nextcloud | **Yes, carefully** |
> | Multiple people editing same database at same time | **Hell no** |
> 
> MMEX supports “bring your own cloud” storage through providers like Google Drive, OneDrive, Dropbox, Nextcloud, Synology, or Syncthing, but the database is still a file-based SQLite database, so conflicts are the danger. citeturn887608search10 MMEX’s own sync guidance says Android/iOS/desktop sync workflows rely on local copies/cloud sync and conflicts have to be handled carefully. citeturn887608search1
> 
> **Recommendation for you:** do **not** self-host the WebApp yet. Use desktop MMEX as the source of truth. Add mobile/web later only for quick entry.
> 
> ---
> 
> # May Monthlies Setup
> 
> Create the month as:
> 
> ```text
> MAY 2026 HOUSEHOLD BASELINE
> Period: 2026-05-01 through 2026-05-31
> ```
> 
> ## Accounts
> 
> Use your clearing-account plan:
> 
> ```text
> CLEARING - Cody
> CLEARING - Mom
> CLEARING - Zai
> CLEARING - Home
> ```
> 
> Optional but useful:
> 
> ```text
> CASH - On Hand
> BANK - Cody Checking
> ```
> 
> But for now, the clean ADHD-friendly version is just the four clearing accounts.
> 
> ---
> 
> # May Monthly Bills to Enter
> 
> Enter these as **recurring monthly transactions** or scheduled transactions.
> 
> Use the due dates you know. If you do not know the exact due date yet, use a placeholder and fix it later.
> 
> ## Core May Bills
> 
> | Due Date | Bill | Amount | Account | Category | Notes |
> |---:|---|---:|---|---|---|
> | May 1 | Rent | $1,250 | CLEARING - Home | Housing: Rent | May household rent |
> | May ? | Electric | $300 estimate | CLEARING - Home | Utilities: Electric | May electric estimate |
> | May ? | Water | $120 estimate | CLEARING - Home | Utilities: Water | May water estimate |
> | May ? | Internet | $55 | CLEARING - Home | Utilities: Internet | May internet |
> | May ? | Insurance | $20 | CLEARING - Home | Housing: Insurance | May household insurance |
> | May ? | Household Supplies | $150 budget | CLEARING - Home | Household: Supplies | Cleaning, paper goods, basics |
> | May ? | Groceries | Set budget | CLEARING - Home | Food: Groceries | Shared groceries |
> | May ? | Phone | Actual amount needed | CLEARING - Home or Cody | Utilities: Phone | Add real amount |
> | May ? | Gigi / Pets | Set budget | CLEARING - Home | Pets: Food/Supplies | Gigi/pet baseline |
> 
> ## Suggested Starting May Budget
> 
> Based on what we already had:
> 
> ```text
> Rent:                  $1,250
> Electric:              $300
> Water:                 $120
> Internet:              $55
> Insurance:             $20
> Household Supplies:    $150
> Groceries:             $400 placeholder
> Pets/Gigi:             $75 placeholder
> Phone:                 TBD
> Transportation/Car:    TBD
> ```
> 
> Known subtotal without phone/car:
> 
> ```text
> $2,370
> ```
> 
> That gives you a working household baseline.
> 
> ---
> 
> # How to Enter Them in MMEX
> 
> For each bill, use:
> 
> ```text
> Account: CLEARING - Home
> Type: Withdrawal
> Payee: Landlord / Utility / Vendor
> Category: Correct category
> Date: May due date
> Amount: Bill amount
> Status: Not reconciled / Follow up
> Notes: May 2026 monthly bill
> ```
> 
> Example:
> 
> ```text
> Date: 2026-05-01
> Account: CLEARING - Home
> Type: Withdrawal
> Payee: Landlord
> Category: Housing: Rent
> Amount: 1250.00
> Notes: May 2026 household rent
> ```
> 
> For estimates, mark the note:
> 
> ```text
> ESTIMATE - replace with actual when bill arrives
> ```
> 
> Example:
> 
> ```text
> Date: 2026-05-10
> Account: CLEARING - Home
> Type: Withdrawal
> Payee: CenterPoint
> Category: Utilities: Electric
> Amount: 300.00
> Notes: ESTIMATE - May electric, replace with actual
> ```
> 
> ---
> 
> # Categories to Create Before Entering May
> 
> Create these first so entries stay clean:
> 
> ```text
> Housing
>   Rent
>   Insurance
>   Repairs
> 
> Utilities
>   Electric
>   Water
>   Internet
>   Phone
> 
> Food
>   Groceries
>   Takeout
>   Shared Meals
> 
> Household
>   Supplies
>   Furniture
>   Laundry
>   Maintenance
> 
> Pets
>   Food
>   Treats
>   Supplies
>   Vet
> 
> Transportation
>   Gas
>   Registration
>   Repairs
>   Rideshare
> 
> Reimbursement
>   Zai Owes Cody
>   Mom Owes Cody
>   Cody Owes Mom
>   Paid Back
> 
> Admin
>   Printing
>   Documents
>   Subscriptions
> 
> Legal
>   Filing Fees
>   Copies
>   Mailing
> ```
> 
> ---
> 
> # Responsibility Tracking
> 
> Here is the key: **Home Clearing tracks the bill. Person Clearing tracks who paid or owes.**
> 
> ## When Cody pays a Home bill
> 
> Example: Cody pays internet.
> 
> ```text
> Withdrawal:
> Account: CLEARING - Home
> Payee: Internet Provider
> Category: Utilities: Internet
> Amount: 55.00
> Notes: May internet paid by Cody
> ```
> 
> Then add a transfer:
> 
> ```text
> Transfer:
> From: CLEARING - Home
> To: CLEARING - Cody
> Amount: 55.00
> Notes: Cody covered May internet
> ```
> 
> This shows Cody gets credit for carrying that household cost.
> 
> ## When Mom pays electric
> 
> ```text
> Withdrawal:
> Account: CLEARING - Home
> Payee: Electric Company
> Category: Utilities: Electric
> Amount: 300.00
> Notes: May electric paid by Mom
> ```
> 
> Then:
> 
> ```text
> Transfer:
> From: CLEARING - Home
> To: CLEARING - Mom
> Amount: 300.00
> Notes: Mom covered May electric
> ```
> 
> ## When Zai owes Cody directly
> 
> Do **not** put that through Home unless it was a household expense.
> 
> Use:
> 
> ```text
> Transfer:
> From: CLEARING - Zai
> To: CLEARING - Cody
> Amount: [amount]
> Notes: Zai owes Cody for [reason]
> ```
> 
> When he pays:
> 
> ```text
> Transfer:
> From: CLEARING - Cody
> To: CLEARING - Zai
> Amount: [amount paid]
> Notes: Zai repayment for [reason]
> ```
> 
> You may need to flip directions after one test depending on how MMEX displays balances. The principle stays the same:
> 
> ```text
> Cody positive = Cody is owed / has covered more
> Zai negative = Zai owes / has been covered
> ```
> 
> ---
> 
> # May Entry Order
> 
> Do it in this order:
> 
> ## 1. Create accounts
> 
> ```text
> CLEARING - Cody
> CLEARING - Mom
> CLEARING - Zai
> CLEARING - Home
> ```
> 
> ## 2. Create categories
> 
> Use the category tree above.
> 
> ## 3. Enter May expected bills
> 
> Put everything under `CLEARING - Home`.
> 
> ## 4. Mark unknowns as estimates
> 
> Use notes like:
> 
> ```text
> ESTIMATE - update when bill arrives
> ```
> 
> ## 5. Enter known payer credits
> 
> Only once someone actually pays.
> 
> ## 6. Enter Zai debts separately
> 
> Do not bury Zai debts inside groceries or car expenses. Use direct reimbursement tracking.
> 
> ---
> 
> # May Monthly Template
> 
> Copy this into your notes while entering:
> 
> ```text
> MAY 2026 MONTHLIES
> 
> [ ] Rent - $1,250 - Due May 1 - Housing: Rent
> [ ] Electric - $300 est. - Utilities: Electric
> [ ] Water - $120 est. - Utilities: Water
> [ ] Internet - $55 - Utilities: Internet
> [ ] Insurance - $20 - Housing: Insurance
> [ ] Household Supplies - $150 budget - Household: Supplies
> [ ] Groceries - $400 budget - Food: Groceries
> [ ] Pets/Gigi - $75 budget - Pets: Food/Supplies
> [ ] Phone - TBD - Utilities: Phone
> [ ] Transportation/Car - TBD - Transportation
> [ ] Zai Current Balance Owed - TBD - Reimbursement: Zai Owes Cody
> ```
> 
> ## Decision
> 
> Do **desktop MMEX only for now**.
> 
> No web app yet. No self-hosting yet. No extra tech goblin doorways. We are entering May bills and making the household ledger tell the truth first.

### User
> This internet is way to slow. Ok so I was thinking about just using QuickBooks since technically I get it for free since I’m an accountant but then the internet is too slow. Money EX doesn’t have bills but I can enter scheduled transactions is that the same thing?

### Assistant
> Yes. In MMEX, **scheduled transactions are your “bills” system**.
> 
> It is not as polished as QuickBooks Bills / Vendors / A/P, but for home finance it’s enough and honestly less annoying.
> 
> ## The translation
> 
> | QuickBooks concept | MMEX equivalent |
> |---|---|
> | Bill | Scheduled transaction |
> | Recurring bill | Repeating scheduled transaction |
> | Vendor | Payee |
> | Expense account/category | Category |
> | Due date | Scheduled date |
> | Paid/unpaid | Entered vs. pending / status / notes |
> | A/P aging | Not really built in |
> | Bill reminder | Scheduled transaction reminder |
> 
> So yes: **enter May monthlies as scheduled transactions.**
> 
> ## How to use MMEX Scheduled Transactions
> 
> For each monthly bill:
> 
> ```text
> Type: Withdrawal
> Account: CLEARING - Home
> Payee: Landlord / Utility / Provider
> Category: Housing: Rent / Utilities: Electric / etc.
> Amount: Estimated or actual
> Date: Due date
> Repeat: Monthly
> Status: None or Follow Up
> Notes: May 2026 monthly bill
> ```
> 
> When it is actually paid, you “enter” or confirm the scheduled transaction into the register.
> 
> ## Example: rent
> 
> ```text
> Account: CLEARING - Home
> Type: Withdrawal
> Payee: Landlord
> Category: Housing: Rent
> Amount: 1250.00
> Date: 2026-05-01
> Repeat: Monthly
> Notes: Monthly rent
> ```
> 
> ## Example: electric estimate
> 
> ```text
> Account: CLEARING - Home
> Type: Withdrawal
> Payee: Electric Company
> Category: Utilities: Electric
> Amount: 300.00
> Date: 2026-05-10
> Repeat: Monthly
> Notes: ESTIMATE - replace with actual bill amount before entering
> ```
> 
> ## The one weakness
> 
> MMEX scheduled transactions are **not true Accounts Payable**.
> 
> Meaning: it does not really create a payable liability the same way QuickBooks does. It is more like:
> 
> > “Here is a recurring transaction waiting to be entered.”
> 
> That is fine for your use case.
> 
> You do **not** need QuickBooks for household tracking. QuickBooks would be overkill, and with slow internet it will irritate you into quitting. Not the move.
> 
> ## Best setup for May
> 
> Use scheduled transactions for:
> 
> ```text
> Rent
> Electric
> Water
> Internet
> Insurance
> Phone
> Groceries Budget
> Household Supplies Budget
> Gigi/Pets Budget
> Car/Transportation Budget
> ```
> 
> For variable stuff like groceries, do **not** pretend it is an exact bill. Make it a monthly budget placeholder:
> 
> ```text
> Payee: Household Grocery Budget
> Category: Food: Groceries
> Amount: 400.00
> Repeat: Monthly
> Notes: Budget placeholder, actual grocery entries posted separately
> ```
> 
> ## My recommendation
> 
> Use MMEX like this:
> 
> ```text
> Scheduled Transactions = expected bills and monthly budget anchors
> Regular Transactions = actual spending
> Transfers = who paid / who owes / reimbursement tracking
> Notes = context and receipts
> ```
> 
> That gives you 80% of QuickBooks usefulness with 20% of the headache.
> 
> ## For your clearing accounts
> 
> Enter the bill itself against:
> 
> ```text
> CLEARING - Home
> ```
> 
> Then when someone pays it, enter a credit/transfer to the person:
> 
> ```text
> CLEARING - Cody
> CLEARING - Mom
> CLEARING - Zai
> ```
> 
> Example:
> 
> Rent due:
> 
> ```text
> Scheduled Transaction:
> CLEARING - Home
> Withdrawal
> Landlord
> Housing: Rent
> $1,250
> Monthly
> ```
> 
> Cody pays it:
> 
> ```text
> Transfer:
> CLEARING - Home → CLEARING - Cody
> $1,250
> Note: Cody covered May rent
> ```
> 
> That makes the home ledger show the bill and Cody’s ledger show the contribution.
> 
> ## Bottom line
> 
> Use MMEX.
> 
> Use **Scheduled Transactions as Bills**.
> 
> Do not use QuickBooks for this unless you need formal accounting, invoices, A/P, classes, 1099s, or business reporting. For home finances and “who owes who,” QuickBooks is a chainsaw for slicing bread.

### User
> can we export this into markdown for my knowledge base.

### Assistant
> Absolutely. I’ll package the MMEX household-finance setup into a clean QiNote-style Markdown file so it can drop straight into your knowledge base.

### Assistant
> Done — clean Markdown export for your knowledge base:
> 
> [Download the MMEX Household Finance Setup Markdown](sandbox:/mnt/data/2026-05-03_mmex_household_finance_setup.md)
