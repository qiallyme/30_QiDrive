---
layout: page
title: "QiFinance"
slug: "qifinance"
created_at: "2026-04-01 15:14:55"
updated_at: "2026-04-01 15:14:55"
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
date: 2026-04-01
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69cd7ca8-274c-832d-b89c-8ce67e3067e1"
canonical_ref: ""
---

# QiFinance

## Overview
- **Date**: 2026-04-01 15:14:55
- **Conversation ID**: `69cd7ca8-274c-832d-b89c-8ce67e3067e1`
- **Source**: `Chat-Export-28513-2026/conversations-005.json`

## Chat History

### User
> WHAT DID I DECIDE ON TRACKING MY PERSONAL FINANCES. I DONT THINK I DID. WAS IT ZOHO FOR PERSONAL BUT WE SWITCHED THE BUSINESS TO SQUARE TO USE IN ZOHO SO DID I STILL NEED A PERSONAL SOLUTION SINCE QBO DRIVES ME NUTES.

### Assistant
> I’m pulling your prior finance-stack decisions together so I don’t guess and accidentally invent a “decision” you never actually made.

### Assistant
> You **did not actually lock in a personal finance system**.
> 
> What you **did** decide:
> 
> ## Business
> You moved toward this stack:
> 
> - **Square** for client invoicing / payment collection
> - **Zoho Finance Suite** as the clean business back end
> - **QuickBooks** only for **client books**, not your own business books
> 
> So yes: **QBO was effectively demoted out of your own business ops** because it was annoying, bloated, and creating integration mess.
> 
> ## Personal
> I do **not** see a final decision that says:
> 
> - “Use Zoho for personal finances”
> - “Keep QBO for personal only”
> - “Use Splitwise / Notion / spreadsheet / app X for personal”
> 
> That part looks **unresolved**.
> 
> ## One important distinction
> You **did** discuss a **household/shared bills system** for Home Hub:
> 
> - Bills DB
> - Payments DB
> - possible Splitwise-style reconciliation
> - shared expense tracking for the house
> 
> But that is **not the same thing** as your full personal finance system.
> 
> ## So the clean answer
> Your current state looks like this:
> 
> - **Business accounting decision:** mostly made
> - **Personal finance tracking decision:** **not actually made**
> - **Household expense tracking concept:** partially designed, not the same as personal bookkeeping
> 
> ## My blunt read
> You were probably mentally blending **three separate lanes**:
> 
> 1. **Business accounting**
> 2. **Household/shared expense management**
> 3. **Your own personal money tracking**
> 
> And only lane **1** got a real decision.
> 
> ## Best next move
> Do **not** use QBO for personal just because it exists. That is how you end up with more rage and zero clarity.
> 
> You need to choose one of these on purpose:
> 
> - **Simple personal tracking:** spreadsheet or lightweight app
> - **Shared household tracking:** Home Hub / bills DB / Splitwise-style logic
> - **Full personal bookkeeping:** Zoho Books only if you want a real ledger and will actually maintain it
> 
> My recommendation for you is:
> **personal = simple**
> **household = structured**
> **business = Zoho/Square**
> 
> That is the least stupid split.
> 
> I can narrow this to a **1-system recommendation** for your personal finances right now and give you the exact setup.

### User
> OK BUT FOR ME PERSONALLY I NEED SOMETHING I DONT WANT TO PAY LOL OF COURSE BUT IT WOULD BE NICE TO JUST CONNECT MY ACCOUNTS, CASHAPP IF POSSIBLE SET SOME RULES AND IM DONE.

### Assistant
> I’m checking what still exists, what’s actually free, and whether Cash App plays nice with account sync right now.

### Assistant
> Yeah — for **you personally**, I would **not** use QBO. That would be self-inflicted annoyance.
> 
> ## Best fit: **Empower Personal Dashboard**
> This is the closest match to your actual ask: **free, connect accounts, categorize transactions, set rules, and mostly leave it alone**. Empower’s dashboard is free and includes **Budgeting & Cash Flow, Net Worth, Transactions, Savings Planner, Debt Paydown, and Portfolio Analysis**. Its support docs also show transaction editing that can be applied to future transactions as rules, plus export options if you ever want your data out. citeturn346215search2turn346215search6turn934406search0turn934406search4
> 
> ## Second-best: **NerdWallet**
> NerdWallet is a solid lighter-weight option if you want something more mobile/simple. Their free app supports linked accounts, **cash flow tracking, net worth, spending by category, recurring bills/subscriptions**, and manual transaction entry. They also say linked account data is typically updated automatically about every 24 hours. citeturn917519search1turn346215search1turn346215search3turn346215search5turn487667search2
> 
> ## What I would *not* pick first: **Rocket Money**
> Rocket Money’s free version is real, and the free mobile app includes **account linking, balance alerts, subscription management, and spend tracking**. But some stuff people actually want long-term is gated or nudged toward Premium; for example, their help docs say **manual transaction entry** and some **net worth controls** are Premium-only. So it’s good, but it’s more **freemium pressure** than “set it and forget it for free.” citeturn872828search1turn872828search4turn872828search13turn487667search7turn487667search10
> 
> ## Cash App: the annoying part
> This is the weak link. Cash App officially supports linking an external bank account and exposes account details for things like direct deposit, and both NerdWallet and Rocket Money say they connect accounts through Plaid or another secure linking provider. Rocket Money also explicitly says some institutions simply won’t be supported. I could not verify an official support page from these budgeting apps that clearly promises **Cash App itself** will sync cleanly as a transaction source, so the safe assumption is: **do not build your finance system around Cash App compatibility**. Build it around your actual bank/credit accounts, and treat Cash App as a pass-through layer. That’s an inference from the connector setup and support limitations. citeturn511445search0turn511445search8turn917519search9turn487667search4turn487667search8
> 
> ## My recommendation
> Use this stack:
> 
> - **Personal finance hub:** **Empower**
> - **Primary synced accounts:** checking, savings, credit cards, loans, investment accounts
> - **Cash App strategy:** do **not** rely on it as the source of truth; sweep money to your bank regularly and let the bank feed the dashboard
> - **Avoid:** QBO for personal, unless you randomly decide you want full accountant-core suffering as a hobby
> 
> ## Clean decision
> If you want the least stupid option:
> 
> **Pick Empower for personal finances.**
> 
> Why:
> - actually free
> - broad dashboard
> - rules/categories
> - exports
> - less “paywall tease” than Rocket Money
> - more complete than trying to brute-force a spreadsheet from day one citeturn346215search2turn346215search6turn934406search0turn934406search4
> 
> ## One warning
> If a big chunk of your real spending lives only inside **Cash App balance** and never touches your bank or cards, **no app is going to magically fix that cleanly**. The better system move is behavioral: route more personal spending through accounts that sync reliably, and use Cash App as a transfer tool, not your ledger.
> 
> If you want, I’ll narrow this into a **10-minute setup plan for Empower** with the exact account order, category logic, and rule structure so you don’t overbuild it.

### User
> ok, actual budget, ezbookkeeping, firefly or another suggestion?

### Assistant
> I’m verifying what each one actually does before I rank them. “EZBookkeeping” is the fuzzy one, so I’m checking that first instead of pretending I know which product you meant.

### Assistant
> I’ve got the ranking. The annoying truth is that “free + account sync + rules” is where these tools separate hard.

### Assistant
> Pick **Actual Budget**.
> 
> That’s the cleanest answer **for you**, not in theory. It gives you real budgeting, rules, schedules, imports, transfer handling, and optional bank sync. Actual’s docs also show built-in support for bank syncing through providers including **SimpleFIN for US/Canada**, plus imports for CSV, OFX, QFX, QIF, and CAMT.053. citeturn771141view0turn771141view1turn198174search2turn198174search26
> 
> ## My ranking
> 
> ### 1) Actual Budget — best fit
> Why it wins:
> - It is the only one of the three that really lines up with your stated goal: **connect accounts, set rules, move on**.
> - It has a real rules engine, envelope-style budgeting, schedules, reports, and decent import support. citeturn273901search13turn771141view0turn198174search2turn198174search26
> 
> The catch:
> - In the US/Canada, the bank connection story usually means **SimpleFIN**, which is **$15/year**. Actual itself is free/open source, but the sync bridge is not. Also, Actual’s bank retrieval is not background-magic; their docs say you fetch transactions with the **Bank Sync** action. Its old mobile apps are deprecated, though the web UI is responsive. citeturn771141view1turn819329view2turn931902search0
> 
> ### 2) Firefly III — powerful, but more work than you need
> Firefly III is legit, but it is more “finance sysadmin hobby” than “set it and forget it.” Its docs show a **separate Data Importer** for importing data, third-party provider support through that importer, a rules engine, and multi-user support. That is solid, but it is more moving pieces than Actual. citeturn381590search2turn198174search19turn381590search0turn198174search1turn198174search7
> 
> My blunt read: unless you specifically want a more elaborate self-hosted finance stack, **Firefly is overkill for your use case**. citeturn381590search2turn198174search19turn381590search0
> 
> ### 3) ezBookkeeping — nicest lightweight tracker, wrong tool if budgeting/sync matter
> ezBookkeeping looks good as a lightweight self-hosted app. Its official site says it is free/open source, browser-based with PWA behavior, supports mobile/desktop, 2FA/OIDC, and a long list of import formats. citeturn819329view3turn819329view4
> 
> But here’s the problem: on **its own comparison page**, ezBookkeeping says it does **not** support budgeting, does **not** support direct bank connections, and does **not** automatically update transactions by rules. So if your actual goal is “link accounts, define rules, done,” ezBookkeeping is the wrong horse. citeturn771141view3
> 
> ## Another suggestion
> If you want the least setup and do **not** care about self-hosting, **Empower Personal Dashboard** is the easier answer than all three. Empower markets the dashboard as free and built around having your financial accounts in one place, with budgeting/cash-flow tooling and a mobile app. citeturn198174search6turn198174search0turn198174search9
> 
> ## The real decision
> For **self-hosted**:
> - **Actual Budget** if you want the best overall fit.
> - **Firefly III** only if you want a more complex finance platform and don’t mind extra setup.
> - **ezBookkeeping** only if you want a lightweight manual tracker and can live without real budgeting + account sync. citeturn771141view0turn381590search2turn819329view3turn771141view3
> 
> For **lowest friction overall**:
> - **Empower** beats all of them on convenience.
> - **Actual** beats them on control. citeturn198174search6turn771141view0
> 
> ## My recommendation for you
> **Actual Budget + SimpleFIN**  
> That is the best compromise between:
> - low cost
> - rules
> - account linking
> - sane UI
> - not becoming your new side job citeturn771141view1turn931902search0turn273901search13turn198174search2
> 
> If you want **strictly free**, then the honest answer is:
> **Actual without sync** or **ezBookkeeping with imports**.  
> Because the moment you want reliable US bank syncing, “free” usually stops being true. citeturn771141view1turn931902search0turn771141view3
> 
> I can map this into a dead-simple setup path: **Actual vs Empower**, with the exact rule structure and account layout.

### User
> Okay, well, who pays for this? Nothing's ever free, so they're obviously, they have the free dashboards so people can put in their transactions and they can aggregate the data and use the rule of large numbers and target certain people and get them to sign up for other products. I get it. It's advertising. And that's fair. I'm giving you a free tool, quote-unquote free tool, in exchange for your, some of your information. I accept that. But who? Or is it multiple companies?

### Assistant
> I’m checking the actual money trail instead of giving you the fake “it’s free because magic” answer.

### Assistant
> Yes. **Usually it’s multiple companies**, and the payer depends on the model.
> 
> ## The actual money trail
> 
> ### 1) “Free dashboard” companies
> These are usually funded by **other revenue lines**, not charity.
> 
> - **Empower** keeps the dashboard free, but it also has **paid advisory services**, and it runs **affiliate/lead programs** tied to users who connect and track significant assets. Empower’s own site says the dashboard remains free, its advisory clients pay fees, and its affiliate program pays for “qualified leads” once a visitor tracks $100K in assets. Empower’s privacy policy also says it does **not sell customers’ personal information**. citeturn181478search2turn397470search8turn304804search3
> - **NerdWallet** is basically a **recommendation/referral machine**. Their official help page says they receive compensation tied to referred investment accounts and a share of free-cash interest in certain arrangements. Their main site is also obviously built around matching people to financial products. citeturn397470search1turn181478search3
> - **Rocket Money** uses a **freemium** model. Its help docs say it has a free plan plus Premium, and it also charges **success fees** on bill negotiations if it saves you money. citeturn462301search0turn462301search1turn462301search3turn462301search9
> 
> So for those apps, the answer is basically:
> 
> **the company pays for the free tier up front, and gets paid back by advisory fees, subscriptions, referrals, lead-gen, or service fees.** citeturn181478search2turn397470search1turn462301search0
> 
> ## 2) The account-connection middleman
> There is often a **second company** in the chain whose entire job is account linking.
> 
> - **Plaid** says it powers account connections and that **the app or service pays Plaid**, not you, when you connect your bank account. Plaid also says you can manage app connections through Plaid Portal. citeturn304804search18turn304804search21
> - For **Actual Budget** in the US/Canada, the sync path is often **SimpleFIN Bridge**, and **you** pay that bridge directly if you want bank sync: currently **$1.50/month or $15/year**. Actual’s docs confirm SimpleFIN support, and Actual’s bank sync is manual fetch, not always-on magic. citeturn181478search0turn181478search1turn181478search5turn181478search9
> 
> So yes, there can easily be **two businesses** touching the same workflow:
> - the budgeting app
> - the bank-data connector citeturn304804search18turn181478search0
> 
> ## 3) Open-source/self-hosted tools
> These are a different animal.
> 
> - **Actual Budget** is open source and funded through **Open Collective / GitHub Sponsors**. Their funding docs say project funds cover operational costs like hosting and code-signing, and GitHub shows sponsor support. citeturn726546search1turn397470search3turn397470search7
> - **Firefly III** is also open source and supported through **donations/sponsorships**. Its docs and GitHub pages point to donations, Patreon/GitHub Sponsors, and sponsor support. citeturn726546search2turn726546search3turn726546search7turn726546search11
> - **ezBookkeeping** is basically the opposite of a monetized funnel: its FAQ says it has **no official hosted service**, accepts **no donations or sponsorships**, and offers **no paid features**. That means **you pay indirectly** with your own hosting, machine, time, and setup burden. citeturn304804search1
> 
> ## So, bluntly: who pays?
> 
> Depends on which path you choose.
> 
> ### If you use Empower / NerdWallet / Rocket Money
> You are **not the only product**, but you are also not necessarily “the product” in the lazy meme sense.
> 
> The paying parties are usually some mix of:
> - **premium subscribers**
> - **advisory clients**
> - **partner banks / lenders / financial product companies**
> - **bill-negotiation fees**
> - **lead-gen / referral compensation** citeturn181478search2turn397470search1turn462301search0turn462301search1
> 
> ### If you use Actual / Firefly / ezBookkeeping
> Then the paying party is mostly:
> - **you** through hosting/time/setup
> - **donors/sponsors** supporting the open-source project
> - and for Actual with sync, **you also pay SimpleFIN** if you want the connection layer citeturn726546search1turn726546search2turn304804search1turn181478search0
> 
> ## The practical takeaway for you
> 
> If your concern is **“who is monetizing my behavior?”**, the order is basically:
> 
> **Most monetized funnel:** Empower / NerdWallet / Rocket Money  
> **Less monetized, more DIY:** Actual / Firefly  
> **Least monetized, most manual:** ezBookkeeping citeturn181478search2turn397470search1turn462301search0turn726546search1turn726546search2turn304804search1
> 
> ## My clean read for you
> 
> You already understand the trade:
> - **Convenience** = somebody somewhere is making money off the ecosystem.
> - **Control/privacy** = you do more setup work.
> 
> So your real choice is not “free or not free.”
> It is:
> 
> **Do you want to pay with money, attention, data-sharing permissions, or admin effort?**
> 
> For you, that means:
> - **Empower** if you want easiest
> - **Actual + SimpleFIN** if you want best control-to-effort ratio
> - **ezBookkeeping** only if you are okay giving up sync and doing more manual work citeturn181478search10turn181478search0turn304804search1
> 
> I can give you a **trust-cost map** next: a dead-simple breakdown of **what each option “costs” in money, privacy exposure, and maintenance**.

### User
> empower is already irritating me i think actual budget might be the way to go, also since its on github cant we customize it a little use supabase possibly and eventually pipe in GINA but for now, hosting it how, and is running a server on my pc (keeping it on) a way to host these non-critical apps and avoiding the high costs with blue ocean and them.

### Assistant
> I’m checking Actual’s current self-hosting and sync architecture so I can tell you what’s realistic versus what sounds cute and becomes a maintenance trap.

### Assistant
> I’ve confirmed the core architecture: Actual is very hackable, but it is **not** a natural “swap in Supabase as the database” app. That distinction matters because it changes whether you’re customizing versus forking the damn thing.

### Assistant
> Yes — **Actual is probably your lane**.
> 
> And yes, **running non-critical apps on your own PC is a completely valid hosting strategy** **if** you treat it like what it is: a cheap personal utility host, **not** “production.” Actual officially supports running on your own machine via Docker, the Server CLI, the desktop app, or from source, and they explicitly position a personal server as the standard long-term setup. citeturn720373search0turn243258view1
> 
> ## The clean read
> 
> ### 1) Can you customize Actual?
> **Yes.**
> Actual is open source, the API is official, and the docs explicitly say you can use the Node client to import from custom sources, export elsewhere, or “write anything you want on top of Actual.” citeturn243258view2
> 
> ### 2) Should you replace its storage with Supabase?
> **Not as the core database.**
> That’s the wrong move unless you want to fork the app and own the consequences.
> 
> Why:
> - Actual’s core data model is **SQLite**, not Postgres/Supabase. citeturn243258view4turn680840search10
> - The server stores budget files as blobs plus its own `account.sqlite` metadata/auth file. citeturn243258view5
> - Their API is **not** a normal REST backend; the official model is a Node client working against Actual’s data model/headless logic. citeturn243258view2
> 
> So the smart architecture is:
> 
> **Actual = source-of-truth budgeting app**  
> **Supabase = sidecar/integration layer later**
> 
> That means:
> - keep Actual intact
> - use `@actual-app/api`
> - mirror selected data into Supabase for dashboards, automations, or future GINA hooks
> 
> That is customization.  
> Trying to make Supabase the native backend is a fork-shaped headache.
> 
> ## 3) Can GINA plug into it later?
> Yes, but **through the API layer**, not by trying to turn Actual into your finance microservice platform. The official API supports programmatic access, including importing/exporting and running bank sync operations through code. citeturn243258view2turn680840search16turn615282search8
> 
> So later you could do things like:
> - nightly export of balances / categories / transactions
> - anomaly checks
> - spend summaries
> - rule suggestions
> - sync selected metrics into Supabase
> 
> That’s sane.
> 
> ## 4) Hosting: your PC vs cloud
> For **right now**, your PC is fine.
> 
> ### Your PC is a good fit if:
> - this is **non-critical**
> - you are okay with it being unavailable when the machine is asleep, rebooting, updating, or your internet flakes
> - you want **near-zero monthly cost**
> - you mostly use it yourself
> 
> ### Your PC is a bad fit if:
> - you want 24/7 reliable remote access
> - you are going to expose it publicly without thinking through security
> - you want “works like SaaS” uptime
> - you don’t want to think about backups
> 
> That’s the real trade.
> 
> ## Best hosting path for you
> 
> ### Right now
> Run Actual **locally on your PC**.
> 
> You have three realistic options:
> 
> #### Option A — easiest dev/control path
> **Docker on your PC**
> 
> Why:
> - easiest to keep isolated
> - easy volume mounts for backups
> - easiest future move to a mini PC / NAS / VPS
> - matches their reverse-proxy examples directly citeturn243258view0
> 
> #### Option B — easiest no-Docker path
> **Server CLI on your PC**
> Actual provides an official sync-server NPM package, requires Node.js v22+, and runs from a folder you choose. citeturn243258view1
> 
> #### Option C — lowest-friction personal start
> **Desktop app with built-in sync server**
> Since release 25.6.0, the desktop app can run the sync server, specifically to simplify things like bank sync. citeturn243258view3
> 
> For you, I’d rank them:
> 1. **Docker**
> 2. **Desktop app sync server**
> 3. **Server CLI**
> 
> ## My actual recommendation
> ### Phase 1
> **Run Actual on your PC, but keep it private.**  
> Do **not** expose it to the public internet yet.
> 
> Use it from:
> - that PC
> - maybe other devices only through a private network path
> 
> Why I’m saying that:
> If you expose Actual publicly, their docs explicitly recommend putting it behind a **reverse proxy with SSL**, and they note extra security hardening is still your job. citeturn243258view0
> 
> So your safest cheap move is:
> - local host now
> - backup the data folder
> - no public exposure yet
> 
> ### Phase 2
> Once you actually like the workflow:
> - move it to a dedicated always-on box, mini PC, or cheap host
> - then add reverse proxy + SSL if remote web access matters citeturn243258view0
> 
> ### Phase 3
> Then add:
> - API scripts
> - Supabase sidecar
> - GINA integration
> 
> ## What I would **not** do
> Do **not** do all this at once:
> - Actual
> - custom fork
> - Supabase backend replacement
> - Gina integration
> - public hosting
> - auth experiments
> 
> That’s how a budgeting app becomes a six-week infrastructure side quest.
> 
> ## Practical warning
> Actual had important security fixes in early 2026, including fixes affecting sync-server users and certain bank-sync/multi-user scenarios, so if you self-host, you need to **stay updated**. citeturn555302view1
> 
> ## Clean decision
> Your best move is:
> 
> **Use Actual as-is. Host it on your PC first. Keep it private. Customize around it, not through it. Use Supabase later as an integration/analytics layer, not the primary store.**
> 
> That’s the lowest-cost, lowest-stupidity path.
> 
> ## If you want the sharp version
> Do this:
> 
> - **Install Actual locally on your PC**
> - **Use Docker if possible**
> - **Do not expose it publicly yet**
> - **Back up the data folder**
> - **Use the official API later for GINA**
> - **Mirror into Supabase later only if you actually need cross-app analytics or automations**
> 
> And yes — using your own PC to host non-critical personal tools is absolutely a legit cost-avoidance strategy. It’s just **home-lab hosting**, not magic.
> 
> I can map the exact **“Cody-safe” setup path** next: local Docker + folder layout + backup plan + future Supabase hook points.

### User
> ok, this is settled now give me the complete entry or entries into my master blueprint for this addtiont o my stack, also the blueprint is getting big we need to start a another level down (subfolders), ```markdown
> . 📂 _qios_master_blueprint
> └── 📂 00_genesis/
> └── 📂 01_governance/
> │  ├── 📄 agent_rules.md
> │  ├── 📄 decisions.md
> │  ├── 📄 index.md
> │  ├── 📄 policies.md
> │  ├── 📄 principles.md
> │  ├── 📄 registry.md
> │  ├── 📄 standards.md
> └── 📂 02_architecture/
> │  ├── 📄 component_map.md
> │  ├── 📄 data_flow.md
> │  ├── 📄 device_model.md
> │  ├── 📄 identity.md
> │  ├── 📄 index.md
> │  ├── 📄 runtime_zones.md
> │  ├── 📄 service_boundaries.md
> │  ├── 📄 system_model.md
> └── 📂 03_structure/
> │  ├── 📄 bands.md
> │  ├── 📄 directory_tree.md
> │  ├── 📄 domains.md
> │  ├── 📄 index.md
> │  ├── 📄 namespace_registry.md
> │  ├── 📄 object_model.md
> │  ├── 📄 placement_rules.md
> │  ├── 📄 subdomains.md
> └── 📂 04_data/
> │  ├── 📄 exports.md
> │  ├── 📄 index.md
> │  ├── 📄 metadata.md
> │  ├── 📄 objects.md
> │  ├── 📄 qievidence.md
> │  ├── 📄 schema.md
> │  ├── 📄 storage.md
> └── 📂 05_compute/
> │  ├── 📄 apis.md
> │  ├── 📄 index.md
> │  ├── 📄 integrations.md
> │  ├── 📄 pipelines.md
> │  ├── 📄 runtime.md
> │  ├── 📄 tech_stack.md
> │  ├── 📄 workers.md
> └── 📂 06_applications/
> │  ├── 📄 admin.md
> │  ├── 📄 index.md
> │  ├── 📄 interfaces.md
> │  ├── 📄 portal.md
> │  ├── 📄 tools.md
> │  ├── 📄 web.md
> └── 📂 07_operations/
> │  ├── 📄 cases.md
> │  ├── 📄 clients.md
> │  ├── 📄 finance.md
> │  ├── 📄 index.md
> │  ├── 📄 products.md
> │  ├── 📄 templates.md
> └── 📂 adr/
> │  ├── 📄 ADR-0000_template.md
> │  ├── 📄 ADR-0001-blueprint-scope.md
> │  ├── 📄 ADR-0001_blueprint_scope.md
> │  ├── 📄 ADR-0002-single-domain-rule.md
> │  ├── 📄 ADR-0002_single_domain_rule.md
> │  ├── 📄 ADR-0003-band-model.md
> │  ├── 📄 ADR-0003_band_model.md
> │  ├── 📄 ADR-0004-qilabs-root.md
> │  ├── 📄 ADR-0004_qilabs_root.md
> │  ├── 📄 ADR-0005-hosted-fleet-orchestration.md
> │  ├── 📄 ADR-0005_fleet_orchestration.md
> │  ├── 📄 ADR-0006_narrative_and_knowledge_consolidation.md
> │  ├── 📄 update-adr.md
> └── 📂 appendices/
> │  ├── 📄 changelog.md
> │  ├── 📄 glossary.md
> │  ├── 📄 legacy_csv_inventory.json
> │  ├── 📄 legacy_csv_migration_plan.md
> │  ├── 📄 legacy_salvage.md
> │  ├── 📄 migration_notes.md
> └── 📂 assets/
> │  ├── 📄 _QiOS_Master_Document.jpg
> │  └── 📂 diagrams/
> │  └── 📂 tables/
> ├── 📄 index.md
> ├── 📄 main.py
> ├── 📄 markmind.html
> ├── 📄 mkdocs.yml
> └── 📂 overrides/
> │  ├── 📄 home.html
> └── 📂 registry/
> │  ├── 📄 band_registry.yaml
> │  ├── 📄 deprecation_registry.yaml
> │  ├── 📄 domain_registry.yaml
> │  ├── 📄 folder_registry.yaml
> │  ├── 📄 qios_04_rules_and_readmes.canvas.canvas
> │  ├── 📄 qios_05_Cursor_and_naming.canvas
> │  ├── 📄 realms_registry.yaml
> │  ├── 📄 sensitivity_classification.yaml
> │  ├── 📄 subdomain_registry.yaml
> │  ├── 📄 workspace_realms.yaml
> └── 📂 schemas/
> │  ├── 📄 band_registry.schema.json
> │  ├── 📄 qievidence.sql
> └── 📂 scripts/
> │  ├── 📄 enforce_structure.py
> └── 📂 standards/
> │  ├── 📄 content_metadata_profile.yaml
> │  ├── 📄 metadata_rules.yaml
> │  ├── 📄 naming_rules.yaml
> │  ├── 📄 pdf_standards.yaml
> │  ├── 📄 repo_rules.yaml
> │  ├── 📄 strict-compliance.md
> └── 📂 stylesheets/
> │  ├── 📄 extra.css
> └── 📂 templates/
> │  ├── 📄 README.md
> │  ├── 📄 artifact_template.md
> │  └── 📄 note_template.md
> ```

### Assistant
> I’m not going to just stuff one more flat file into that tree. The blueprint is past the point where “more markdown at root of each domain” is a sane pattern.

### Assistant
> Yes. This is a good point to stop pretending the flat-file layout still scales.
> 
> ## Decision locked
> 
> For **personal finance**, your stack decision is:
> 
> - **Primary app:** Actual Budget
> - **Primary hosting:** self-hosted on your own PC for now
> - **Exposure model:** private/local first, not public internet
> - **Database stance:** **do not** replace Actual’s core storage with Supabase
> - **Supabase role:** optional sidecar later for analytics, automation, cross-app data, GINA hooks
> - **GINA role:** deferred integration through API/export layer, not direct core dependency
> - **Business finance remains separate:** Square + Zoho path
> - **Household/shared finance remains separate:** Home Hub / household ops layer, not Actual core
> 
> ---
> 
> # What to change in the blueprint structure
> 
> Do **not** keep stuffing more into single `finance.md`, `integrations.md`, and `runtime.md` files.
> 
> Start subfolders **only where pressure already exists**.
> 
> ## Recommended structural refactor now
> 
> ```markdown
> 📂 _qios_master_blueprint
> └── 📂 05_compute/
> │   ├── 📄 apis.md
> │   ├── 📄 index.md
> │   ├── 📂 integrations/
> │   │   ├── 📄 index.md
> │   │   ├── 📂 finance/
> │   │   │   └── 📄 actual_budget.md
> │   │   └── 📂 ai/
> │   │       └── 📄 gina_hooks.md
> │   ├── 📄 pipelines.md
> │   ├── 📂 runtime/
> │   │   ├── 📄 index.md
> │   │   └── 📂 hosts/
> │   │       └── 📄 personal_pc_hosting.md
> │   ├── 📄 tech_stack.md
> │   ├── 📄 workers.md
> │
> └── 📂 07_operations/
> │   ├── 📄 cases.md
> │   ├── 📄 clients.md
> │   ├── 📂 finance/
> │   │   ├── 📄 index.md
> │   │   ├── 📄 business_finance.md
> │   │   ├── 📄 household_finance.md
> │   │   └── 📄 personal_finance.md
> │   ├── 📄 index.md
> │   ├── 📄 products.md
> │   ├── 📄 templates.md
> │
> └── 📂 adr/
> │   ├── 📄 ADR-0007_personal_finance_stack_actual_budget.md
> ```
> 
> ## Minimal rule for when a file becomes a folder
> 
> Use this everywhere going forward:
> 
> - If a document is likely to exceed **~250–400 lines**
> - or represents **3+ subtopics**
> - or has both **policy + architecture + operational procedures**
> - it stops being a single file and becomes an `index.md` + child documents
> 
> That keeps the blueprint sane.
> 
> ---
> 
> # Add these entries
> 
> ## 1) ADR entry
> 
> **Path**
> ```markdown
> adr/ADR-0007_personal_finance_stack_actual_budget.md
> ```
> 
> **Content**
> ```markdown
> # ADR-0007 — Personal Finance Stack: Actual Budget + Local Self-Hosting
> 
> - **Status:** Accepted
> - **Date:** 2026-04-01
> - **Owner:** Cody
> - **Domain:** Personal Finance / Compute / Runtime
> - **Supersedes:** None
> 
> ## Context
> 
> A dedicated personal finance system is required that is:
> 
> - low-cost or near-zero-cost to operate
> - under direct control
> - simple enough to maintain consistently
> - separable from business finance
> - extensible later for analytics and AI integration
> 
> QuickBooks Online is rejected for personal finance use due to workflow friction, cognitive overhead, and poor fit for lightweight personal budgeting.
> 
> Hosted “free” dashboards were evaluated, but the preferred direction is to reduce vendor dependence, reduce funnel pressure, and preserve future architecture flexibility.
> 
> Actual Budget was selected because it provides a strong budgeting model, supports self-hosting, and can later be extended through its API/export layer without forcing a rewrite of the finance stack.
> 
> ## Decision
> 
> The personal finance stack shall use **Actual Budget** as the primary personal budgeting and transaction-management system.
> 
> ### Core decisions
> 
> 1. **Actual Budget is the personal finance system of record**
>    - Personal budgeting, transaction review, and personal account tracking will live in Actual.
>    - Actual will not be used as the primary system for business accounting.
> 
> 2. **Initial hosting will be local/self-hosted**
>    - Actual will first be hosted on Cody’s own PC.
>    - This host is treated as a non-critical personal utility host, not production infrastructure.
> 
> 3. **Exposure model is private-first**
>    - Initial deployment is local/private only.
>    - Public internet exposure is deferred unless proper reverse proxy, SSL, authentication review, and backup/restore controls are in place.
> 
> 4. **Supabase is not the primary backend for Actual**
>    - Actual’s internal storage model remains intact.
>    - Supabase may later be used as a sidecar integration layer for:
>      - derived analytics
>      - automation events
>      - cross-system reporting
>      - GINA-facing data products
> 
> 5. **GINA integration is deferred**
>    - GINA will not be a launch dependency.
>    - Future GINA integration must occur through sanctioned APIs, exports, mirrored data, or controlled adapters.
>    - GINA must not directly mutate Actual core storage outside approved workflows.
> 
> 6. **Business finance remains separate**
>    - Business accounting remains on the separate finance stack already selected for business operations.
>    - Personal and business finance must remain logically separated.
> 
> 7. **Household finance remains separate**
>    - Household/shared expense coordination belongs to household operations tooling, not to the core personal finance budget model unless intentionally mirrored.
> 
> ## Rationale
> 
> This decision optimizes for:
> 
> - low operating cost
> - high control
> - low monthly software burden
> - future extensibility
> - clean separation of domains
> 
> It avoids:
> 
> - using QBO for a job it is poorly suited for
> - overengineering the initial deployment
> - turning a budgeting tool into a premature platform rewrite
> - mixing business, household, and personal financial logic into one unstable system
> 
> ## Consequences
> 
> ### Positive
> 
> - Lower cost than commercial finance stacks
> - High control over deployment and retention
> - Easier future integration into QiOS ecosystem
> - Can remain private and lightweight
> - Creates a stable base for later automation
> 
> ### Negative
> 
> - Local-hosted availability depends on Cody’s machine uptime
> - Remote access is limited until hardened hosting is introduced
> - Setup/maintenance burden shifts to owner
> - Some bank sync flows may require optional third-party bridge tooling
> 
> ## Non-Goals
> 
> The following are explicitly out of scope for phase 1:
> 
> - replacing Actual’s core database with Supabase
> - multi-user finance portalization
> - public SaaS-style deployment
> - deep AI automation at initial launch
> - blending business and personal accounting into one ledger
> 
> ## Revisit Triggers
> 
> Revisit this ADR if any of the following become true:
> 
> - remote 24/7 access becomes necessary
> - multi-device or multi-user access becomes a priority
> - local PC hosting becomes unreliable
> - GINA requires structured finance analytics beyond Actual-native workflows
> - a dedicated low-cost always-on host is introduced
> 
> ## Related Documents
> 
> - `05_compute/integrations/finance/actual_budget.md`
> - `05_compute/runtime/hosts/personal_pc_hosting.md`
> - `07_operations/finance/personal_finance.md`
> ```
> 
> ---
> 
> ## 2) Compute integration entry
> 
> **Path**
> ```markdown
> 05_compute/integrations/finance/actual_budget.md
> ```
> 
> **Content**
> ```markdown
> # Actual Budget Integration
> 
> ## Purpose
> 
> This document defines how Actual Budget fits into the QiOS stack as the selected personal finance application.
> 
> It covers:
> 
> - system role
> - hosting posture
> - data boundaries
> - integration constraints
> - future extension points
> 
> ## Role in Stack
> 
> Actual Budget serves as the **personal finance application layer** for:
> 
> - personal budget categories
> - personal transaction review
> - personal account tracking
> - rule-based categorization
> - personal reconciliation workflows
> 
> Actual is **not** the primary business accounting platform.
> 
> ## Boundary Model
> 
> ### In-Scope
> 
> - personal checking, savings, cards, and personal liabilities
> - budget categories
> - rule-based transaction handling
> - manual transaction review and cleanup
> - controlled exports and mirrored downstream data
> 
> ### Out-of-Scope
> 
> - business accounting ledger
> - household master split accounting
> - public-facing finance interfaces
> - direct GINA dependency at launch
> - core database replacement with Supabase
> 
> ## Architecture Position
> 
> Actual occupies the following role:
> 
> - **Application:** personal finance budgeting layer
> - **Runtime:** self-hosted local/private service
> - **Storage:** Actual-native internal storage
> - **Integration Layer:** optional sidecar scripts and mirrored derived data
> - **AI Layer:** deferred, adapter-based
> 
> ## Approved Integration Pattern
> 
> ### Phase 1 — Local Standalone Use
> 
> - Actual runs locally on Cody’s personal machine
> - Local/private access only
> - Data remains in Actual-native storage
> - Manual export or light scripting allowed
> 
> ### Phase 2 — Controlled Automation
> 
> - use Actual API/export layer for:
>   - budget snapshots
>   - transaction extracts
>   - category summaries
>   - reconciliation support
> - optional mirror into Supabase for derived analytics
> - no direct mutation of Actual internals outside approved app/API workflows
> 
> ### Phase 3 — GINA Sidecar
> 
> - GINA consumes mirrored or exported finance data
> - GINA may:
>   - summarize spending
>   - detect patterns
>   - generate reminders
>   - identify anomalies
> - GINA may not silently rewrite Actual core data
> 
> ## Supabase Position
> 
> Supabase is permitted only as a **secondary layer** for:
> 
> - analytics tables
> - automation events
> - rollups
> - cross-domain dashboards
> - AI-ready derived datasets
> 
> Supabase is not approved as a replacement backend for Actual core storage.
> 
> ## Hosting Modes
> 
> ### Approved Initial Mode
> 
> - self-hosted on Cody’s own PC
> - private/local use
> - low-cost non-critical deployment
> 
> ### Future Approved Mode
> 
> - dedicated always-on host
> - reverse proxy + SSL
> - controlled remote access
> - documented backup/restore flow
> 
> ### Disallowed Launch Mode
> 
> - public internet exposure without hardening
> - experimental backend rewrites
> - dependency-heavy overengineering before stable use
> 
> ## Data Flow Summary
> 
> 1. Financial institutions or imports provide transactions
> 2. Actual stores and categorizes personal finance activity
> 3. User reviews, approves, and corrects rules/categories
> 4. Optional export/API scripts produce derived outputs
> 5. Optional mirrored outputs flow into Supabase
> 6. Future GINA layer consumes mirrored/derived data only
> 
> ## Operational Guardrails
> 
> - Actual remains the system of record for personal budgeting
> - Business finance must remain separate
> - Household/shared expense logic must remain separate unless explicitly mirrored
> - No undocumented schema hacks
> - No silent cross-app mutation
> - All automation must be reversible or auditable
> 
> ## Future Extension Points
> 
> - budget health dashboard
> - monthly personal cashflow summary
> - anomaly detection worker
> - recurring transaction review assistant
> - tax-adjacent personal classification support
> - cross-surface dashboard inside QiOS admin layer
> 
> ## Related Documents
> 
> - `adr/ADR-0007_personal_finance_stack_actual_budget.md`
> - `05_compute/runtime/hosts/personal_pc_hosting.md`
> - `07_operations/finance/personal_finance.md`
> ```
> 
> ---
> 
> ## 3) Runtime hosting entry
> 
> **Path**
> ```markdown
> 05_compute/runtime/hosts/personal_pc_hosting.md
> ```
> 
> **Content**
> ```markdown
> # Personal PC Hosting
> 
> ## Purpose
> 
> This document defines the approved use of Cody’s own PC as a low-cost runtime host for non-critical personal applications.
> 
> ## Approved Use Case
> 
> Personal PC hosting is approved for:
> 
> - non-critical tools
> - personal/internal services
> - low-cost experimentation
> - private dashboards
> - self-hosted applications that do not require guaranteed uptime
> 
> This includes the initial deployment of Actual Budget.
> 
> ## Host Classification
> 
> - **Host Type:** Personal Utility Host
> - **Criticality:** Low
> - **Availability Requirement:** Best effort
> - **Security Posture:** Private-first
> - **Exposure:** Local/private only unless explicitly hardened
> 
> ## Suitable Workloads
> 
> - Actual Budget
> - lightweight internal dashboards
> - personal utilities
> - low-risk services with local-first value
> 
> ## Unsuitable Workloads
> 
> - public production portals
> - client-facing critical systems
> - systems requiring guaranteed uptime
> - services without backup/restore discipline
> - anything that creates legal, security, or financial exposure if it goes down
> 
> ## Advantages
> 
> - near-zero monthly cost
> - full control
> - quick deployment
> - ideal for proving utility before paying for infrastructure
> 
> ## Limitations
> 
> - unavailable when PC is off, asleep, rebooting, or unstable
> - subject to local network constraints
> - higher owner-maintenance burden
> - weak fit for public or multi-user reliability expectations
> 
> ## Rules
> 
> 1. Private-first deployment
> 2. No public exposure without reverse proxy, SSL, and documented access controls
> 3. Persistent data must be stored in known, backed-up directories
> 4. Every hosted service must have a documented restore path
> 5. Every hosted service must have a named owner and data location
> 
> ## Actual Budget Hosting Standard
> 
> Actual Budget shall initially be hosted on the personal PC under these conditions:
> 
> - private/local access only
> - backed-up data directory
> - no dependency on public uptime
> - no premature hardening work unless remote access becomes necessary
> 
> ## Upgrade Triggers
> 
> Move a personal-PC-hosted app to a more stable runtime when:
> 
> - uptime matters
> - remote access becomes frequent
> - multiple users depend on it
> - backup/restore becomes too manual
> - security requirements increase
> 
> ## Future Paths
> 
> Approved future upgrade paths include:
> 
> - dedicated mini PC
> - always-on local device
> - private server/VPS
> - managed low-cost host with reverse proxy and SSL
> 
> ## Related Documents
> 
> - `adr/ADR-0007_personal_finance_stack_actual_budget.md`
> - `05_compute/integrations/finance/actual_budget.md`
> ```
> 
> ---
> 
> ## 4) Operations finance entry
> 
> **Path**
> ```markdown
> 07_operations/finance/personal_finance.md
> ```
> 
> **Content**
> ```markdown
> # Personal Finance Operations
> 
> ## Purpose
> 
> This document defines how personal finance is operated within the QiOS ecosystem.
> 
> It is operational, not architectural.
> 
> ## System of Record
> 
> Actual Budget is the approved system of record for personal budgeting and personal transaction operations.
> 
> ## Scope
> 
> ### In-Scope
> 
> - personal accounts
> - personal budgeting
> - personal spending review
> - personal category rules
> - personal recurring transaction tracking
> - personal cashflow review
> 
> ### Out-of-Scope
> 
> - business accounting
> - business invoicing
> - shared household settlement logic
> - tax firm bookkeeping workflows
> - client finance workflows
> 
> ## Separation Rules
> 
> ### Business vs Personal
> 
> Business finance must remain separate from personal finance.
> 
> Business transactions should not live in the personal budget except in explicitly documented reimbursement or owner-draw contexts.
> 
> ### Household vs Personal
> 
> Household/shared expenses may be referenced, but household financial coordination belongs to the household operations stack, not the personal budget system by default.
> 
> ## Operating Rules
> 
> 1. Actual Budget is the personal budget source of truth
> 2. Personal finance rules should reduce manual review, not create more admin
> 3. Cash App should not be treated as the long-term source of truth if underlying accounts are available elsewhere
> 4. Personal finance review should remain lightweight and sustainable
> 5. Personal finance tooling must not become a hidden business accounting system
> 
> ## Review Cadence
> 
> ### Weekly
> 
> - review uncategorized transactions
> - approve or adjust rules
> - check pending/duplicate items
> - confirm balances at a high level
> 
> ### Monthly
> 
> - review category drift
> - review recurring charges/subscriptions
> - export or snapshot if needed
> - verify backup presence
> 
> ### Quarterly
> 
> - clean stale categories
> - review rule bloat
> - review whether local hosting still fits
> - evaluate whether mirrored analytics are needed
> 
> ## Data Handling
> 
> ### Approved
> 
> - direct use inside Actual
> - controlled exports
> - mirrored derived data for analytics
> - documented automation outputs
> 
> ### Not Approved
> 
> - undocumented spreadsheet drift as parallel source of truth
> - hidden business commingling
> - untracked manual rewrites outside the approved application workflow
> 
> ## Cash App Policy
> 
> Cash App may be used operationally, but it should not define the personal finance architecture.
> 
> Preferred handling:
> 
> - use synced bank/card accounts as the durable source of truth
> - treat Cash App as an edge/payment rail where possible
> - minimize dependence on isolated balance-only workflows
> 
> ## Future Enhancements
> 
> Potential later additions:
> 
> - personal finance dashboard rollups
> - anomaly summaries
> - GINA-generated monthly summaries
> - mirrored analytics in Supabase
> - budget-health alerts
> 
> ## Related Documents
> 
> - `adr/ADR-0007_personal_finance_stack_actual_budget.md`
> - `05_compute/integrations/finance/actual_budget.md`
> - `05_compute/runtime/hosts/personal_pc_hosting.md`
> ```
> 
> ---
> 
> # New index files you should add
> 
> ## `05_compute/integrations/index.md`
> 
> ```markdown
> # Integrations
> 
> ## Purpose
> 
> This section defines approved external and cross-system integrations used by QiOS compute services.
> 
> ## Subsections
> 
> - `finance/actual_budget.md` — Personal finance application integration
> - `ai/gina_hooks.md` — Future AI adapter and hook definitions
> 
> ## Rules
> 
> - Integrations must respect system-of-record boundaries
> - No integration may silently replace a core storage model without an ADR
> - All automation must be auditable and reversible where practical
> ```
> 
> ## `05_compute/runtime/index.md`
> 
> ```markdown
> # Runtime
> 
> ## Purpose
> 
> This section defines where and how compute workloads run.
> 
> ## Subsections
> 
> - `hosts/personal_pc_hosting.md` — Approved use of Cody’s personal PC as a runtime host
> 
> ## Rules
> 
> - Runtime classification must match service criticality
> - Low-cost local hosting is acceptable for non-critical private services
> - Public exposure requires explicit hardening and documentation
> ```
> 
> ## `07_operations/finance/index.md`
> 
> ```markdown
> # Finance Operations
> 
> ## Purpose
> 
> This section separates financial operations by domain.
> 
> ## Subsections
> 
> - `business_finance.md` — Business accounting and business finance tooling
> - `household_finance.md` — Household/shared expense operations
> - `personal_finance.md` — Personal budgeting and personal finance operations
> 
> ## Rules
> 
> - Personal, business, and household finance are distinct operational domains
> - Shared terms do not justify shared ledgers
> - Each finance domain must have an explicit system of record
> ```
> 
> ---
> 
> # Existing files that need a small update
> 
> ## `01_governance/decisions.md`
> Add an entry like this:
> 
> ```markdown
> - **ADR-0007 — Personal Finance Stack: Actual Budget + Local Self-Hosting**
>   - Actual Budget selected as the personal finance system of record
>   - initial runtime is Cody’s personal PC
>   - Supabase deferred to sidecar/analytics role only
>   - GINA integration deferred to API/export layer
> ```
> 
> ## `05_compute/tech_stack.md`
> Add this entry:
> 
> ```markdown
> ### Personal Finance Stack
> 
> - **Application:** Actual Budget
> - **Role:** personal budgeting and personal transaction management
> - **Hosting:** self-hosted on personal PC initially
> - **Remote Exposure:** deferred/private-first
> - **Secondary Data Layer:** Supabase (future sidecar only; not core backend)
> - **AI Integration:** GINA via API/export/mirrored-data adapters in later phase
> ```
> 
> ## `03_structure/directory_tree.md`
> Add a note like this:
> 
> ```markdown
> ### Folderization Rule
> 
> When a blueprint topic grows beyond a single-document scope, convert the topic from a leaf markdown file into:
> 
> - `topic/index.md`
> - `topic/<child_documents>.md`
> 
> Initial pressure zones now using this pattern:
> 
> - `05_compute/integrations/`
> - `05_compute/runtime/`
> - `07_operations/finance/`
> ```
> 
> ---
> 
> # My blunt recommendation on the refactor
> 
> Do **not** refactor the whole blueprint today. That is how you burn hours renaming files instead of making the system better.
> 
> Do this instead:
> 
> ## Phase 1
> Create only these new folders:
> 
> - `05_compute/integrations/`
> - `05_compute/runtime/`
> - `07_operations/finance/`
> 
> ## Phase 2
> Move only the new Actual/personal-finance material into the new structure.
> 
> ## Phase 3
> Later, convert other bloated files only when they hit the threshold.
> 
> That keeps the blueprint clean **without** kicking off a fake “taxonomy improvement project” that eats the week.
> 
> If you want, next I’ll give you the **exact revised tree block** for your whole blueprint in your preferred style so you can paste it directly into `directory_tree.md`.
