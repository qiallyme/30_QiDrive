---
layout: page
title: "Monorepo Structure Cleanup"
slug: "monorepo_structure_cleanup"
created_at: "2026-03-07 20:41:09"
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
date: 2026-03-07
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69ace1bc-0b70-8333-98c8-58b55b078ddf"
canonical_ref: ""
---

# Monorepo Structure Cleanup

## Overview
- **Date**: 2026-03-07 20:41:09
- **Conversation ID**: `69ace1bc-0b70-8333-98c8-58b55b078ddf`
- **Source**: `Chat-Export-28513-2026/conversations-004.json`

## Chat History

### User
> ok chat i am done dealing with all these side projects i got going on in my mono repo, lets just put in the folder for the only apps i need in my apps in my mono repo. right.

### Assistant
> Yes. Good call. You’re bleeding focus across too many surfaces. Monorepos only work when the **apps layer is brutally small** and everything else is packages or archive.
> 
> Let’s tighten it.
> 
> ## Rule
> `/apps` = **only things that actually run**
> 
> Not experiments  
> Not utilities  
> Not documentation tools  
> Not ingestion scripts
> 
> Just **deployable interfaces**.
> 
> ---
> 
> # Clean Monorepo Structure
> 
> ```
> qi-one/
> │
> ├─ apps/
> │   ├─ portal/          # QiAlly client portal (Astro / React / Supabase)
> │   ├─ archive/         # QiArchive document system UI (Paperless + viewer)
> │   ├─ chronicle/       # QiChronicle timeline / event log
> │   ├─ cockpit/         # Admin dashboard for you (internal ops)
> │
> ├─ packages/
> │   ├─ db/              # Postgres schemas & migrations
> │   ├─ ui/              # shared UI components
> │   ├─ auth/            # auth helpers
> │   ├─ storage/         # drive / s3 / paperless connectors
> │   ├─ ingestion/       # document pipelines
> │   ├─ ai/              # embeddings / agents / GINA logic
> │
> ├─ scripts/
> │   ├─ ingestion/
> │   ├─ maintenance/
> │   ├─ automation/
> │
> ├─ infrastructure/
> │   ├─ railway/
> │   ├─ cloudflare/
> │   ├─ docker/
> │
> ├─ archive/             # retired experiments
> │
> └─ docs/
> ```
> 
> ---
> 
> # The Only Apps You Actually Need
> 
> ### 1️⃣ **portal**
> Client facing.
> 
> Purpose:
> - client dashboards
> - tax clients
> - caregiver portal
> - case portal
> - authentication
> 
> This becomes **QiPortals**.
> 
> ---
> 
> ### 2️⃣ **archive**
> Document intelligence.
> 
> Purpose:
> - Paperless UI wrapper
> - file viewer
> - metadata editing
> - AI tagging
> 
> This becomes **QiArchive**.
> 
> ---
> 
> ### 3️⃣ **chronicle**
> Your life / legal / ops timeline.
> 
> Purpose:
> - event logging
> - legal timeline
> - activity log
> - notes
> 
> This becomes **QiChronicle**.
> 
> ---
> 
> ### 4️⃣ **cockpit**
> Your **control panel**.
> 
> Purpose:
> - system health
> - ingestion monitoring
> - queues
> - AI jobs
> - DB stats
> - admin tools
> 
> This is basically **QiCockpit**.
> 
> ---
> 
> # Everything Else Should NOT Be Apps
> 
> These belong in **packages**:
> 
> | thing | where |
> |---|---|
> AI agents | `packages/ai` |
> Supabase schemas | `packages/db` |
> shared UI | `packages/ui` |
> ingestion pipelines | `packages/ingestion` |
> paperless connector | `packages/storage` |
> automation | `scripts/` |
> 
> ---
> 
> # The Mistake You Were Making
> You were turning **every idea into an app**.
> 
> Instead:
> 
> ```
> Idea
>    ↓
> package
>    ↓
> used by app
> ```
> 
> Apps should be **very few**.
> 
> ---
> 
> # Final Monorepo Reality
> 
> You are really building **one system with four doors**
> 
> ```
> QiOne System
>      │
>      ├ portal
>      ├ archive
>      ├ chronicle
>      └ cockpit
> ```
> 
> Everything else = infrastructure.
> 
> ---
> 
> ## One More Brutal Truth
> 
> You probably only need **two apps right now**.
> 
> ```
> apps/
>    portal
>    archive
> ```
> 
> Chronicle and cockpit can come later.
> 
> Ship the **document brain first**.
> 
> ---
> 
> If you want, next I can also show you the **clean Astro monorepo layout** that will prevent this repo from turning into chaos again. It’ll make your life about **80% easier**.

### User
> look at my tree then tell me again. ```markdown

> . 📂 _QiOne_MonoRepo_v2

> ├── 📄 LICENSE

> ├── 📄 README.md

> ├── 📄 _QiOne_MonoRepo_Astro.code-workspace

> └── 📂 apps/

> │  └── 📂 api-core/

> │    ├── 📄  - Copy.keep

> │  └── 📂 gina-ai-chat/

> │    └── 📂 GINA_launcher/

> │      ├── 📄 index.html

> │      └── 📂 src/

> │        └── 📂 components/

> │          ├── 📄 FileBrowser.jsx

> │          ├── 📄 index.html

> │        ├── 📄 config.js

> │        ├── 📄 index.html

> │    └── 📂 apps/

> │      └── 📂 QiDocs/

> │        ├── 📄 index.html

> │      └── 📂 gina_core/

> │        └── 📂 __pycache__/

> │          ├── 📄 __init__.cpython-314.pyc

> │          ├── 📄 utils.cpython-314.pyc

> │        ├── 📄 db.py

> │        ├── 📄 index.html

> │        ├── 📄 main.py

> │        └── 📂 services/

> │          ├── 📄 capture.py

> │          ├── 📄 index.html

> │        ├── 📄 utils.py

> │      ├── 📄 index.html

> │      └── 📂 launcher/

> │        ├── 📄 index.html

> │        ├── 📄 package-lock.json

> │        ├── 📄 package.json

> │        └── 📂 public/

> │          ├── 📄 index.html

> │        └── 📂 src/

> │          ├── 📄 App.css

> │          ├── 📄 App.jsx

> │          └── 📂 components/

> │            ├── 📄 FileBrowser.css

> │            ├── 📄 Tooltip.css

> │            ├── 📄 Tooltip.jsx

> │            ├── 📄 index.html

> │          ├── 📄 index.css

> │          ├── 📄 index.html

> │          ├── 📄 main.jsx

> │          ├── 📄 theme.js

> │    └── 📂 data/

> │      └── 📂 compiled/

> │        ├── 📄 index.html

> │        ├── 📄 qios_constitution_v1.json

> │      ├── 📄 index.html

> │      └── 📂 migrations/

> │        ├── 📄 001_ingestion_queue.sql

> │        ├── 📄 002_semantic_profile_file_level.sql

> │        ├── 📄 index.html

> │      └── 📂 outputs/

> │        ├── 📄 index.html

> │      ├── 📄 qios_01_tables_and_registries.canvas

> │      ├── 📄 qios_03_directory_tree.canvas

> │      └── 📂 schemas/

> │        ├── 📄 index.html

> │      └── 📂 seeds/

> │        ├── 📄 index.html

> │        ├── 📄 supabase_seed_qid.sql

> │        ├── 📄 supabase_seed_realms.sql

> │        ├── 📄 supabase_seed_rules.sql

> │      └── 📂 sheets/

> │        ├── 📄 front_matter_schema_v1.csv

> │        ├── 📄 fs_ignore_v1.csv

> │        ├── 📄 index.html

> │        ├── 📄 qios_rules_v1_1.csv

> │    └── 📂 docs/

> │      ├── 📄 INTEGRATION_COMPLETE.md

> │      ├── 📄 QiAlly Call Ecosystem & Gina Voice Architecture.md

> │      ├── 📄 gina_n8n_workflows.md

> │      ├── 📄 index.html

> │      ├── 📄 integration_summary.md

> │      ├── 📄 launcher_ui_mindmap.md

> │      ├── 📄 markdownlint_analysis_genesis.md

> │      ├── 📄 markdownlint_analysis_remaining.md

> │      ├── 📄 markdownlint_final_analysis.md

> │      ├── 📄 markdownlint_quick_reference.md

> │      ├── 📄 markdownlint_review_summary.md

> │      ├── 📄 markdownlint_summary.md

> │      └── 📂 notes/

> │        ├── 📄 discussion26-07-01.md

> │        ├── 📄 index.html

> │      └── 📂 prompts/

> │        ├── 📄 cockpit_gui_prompt.md

> │        ├── 📄 index.html

> │      ├── 📄 ui_contracts_v1.md

> │    ├── 📄 env.example

> │    └── 📂 gina_core/

> │      ├── 📄 index.html

> │      ├── 📄 main.py

> │      ├── 📄 requirements.txt

> │    ├── 📄 index.html

> │    ├── 📄 package-lock.json

> │    ├── 📄 package.json

> │    └── 📂 public/

> │      ├── 📄 index.html

> │    ├── 📄 qios_00_genesis.canvas

> │    ├── 📄 qios_runtime_mindmap.canvas

> │    └── 📂 rules/

> │      ├── 📄 _readme.md

> │      ├── 📄 folder_registry.yaml

> │      ├── 📄 index.html

> │      ├── 📄 qios_04_rules_and_readmes.canvas.canvas

> │      ├── 📄 qios_05_Cursor_and_naming.canvas

> │      └── 📂 qios_cursor_prompts/

> │        ├── 📄 index.html

> │        ├── 📄 install_ingestion_worker.md

> │        ├── 📄 project_prompt.md.md

> │        ├── 📄 qicompiler_add_prompt.md

> │        ├── 📄 qicompiler_orchestrator_prompt.md

> │        ├── 📄 qimatrix_csv_prompt.md

> │        ├── 📄 qimatrix_sql_prompt.md

> │        ├── 📄 qimatrix_yaml_prompt.md

> │        ├── 📄 step3_tree_compiler_prompt.md

> │        ├── 📄 user_prompt.md.md

> │      ├── 📄 realms_registry.yaml

> │    └── 📂 src/

> │      ├── 📄 App.css

> │      ├── 📄 App.jsx

> │      └── 📂 components/

> │        ├── 📄 FileBrowser.css

> │        ├── 📄 Tooltip.css

> │        ├── 📄 Tooltip.jsx

> │        ├── 📄 index.html

> │      ├── 📄 index.css

> │      ├── 📄 index.html

> │      ├── 📄 main.jsx

> │      ├── 📄 theme.js

> │    └── 📂 templates/

> │      └── 📂 docs/

> │        ├── 📄 index.html

> │        ├── 📄 readme_template.md.md

> │      ├── 📄 index.html

> │    └── 📂 tests/

> │      ├── 📄 index.html

> │      ├── 📄 verify_parsing.py

> │    └── 📂 tools/

> │      ├── 📄 README_SCANNER.md

> │      ├── 📄 index.html

> │      ├── 📄 run_migrations.py

> │    └── 📂 workers/

> │      ├── 📄 _readme.md

> │      └── 📂 _shared/

> │        ├── 📄 index.html

> │      └── 📂 embedder/

> │        ├── 📄 index.html

> │        ├── 📄 worker_embedder.ts

> │      ├── 📄 index.html

> │      └── 📂 ingestion/

> │        ├── 📄 index.html

> │        ├── 📄 worker_ingestion.ts

> │      └── 📂 linter/

> │        ├── 📄 index.html

> │        ├── 📄 readme_generator.py

> │      └── 📂 metadata_naming/

> │        ├── 📄 index.html

> │      └── 📂 orchestrator/

> │        ├── 📄 OrchestratorState.ts

> │        ├── 📄 index.html

> │        └── 📂 migrations/

> │          ├── 📄 0001_do.mjs

> │          ├── 📄 index.html

> │        ├── 📄 package-lock.json

> │        ├── 📄 package.json

> │        ├── 📄 qios_06_workers_orchestrator.canvas

> │        ├── 📄 worker_orchestrator.ts

> │      └── 📂 self_heal/

> │        ├── 📄 index.html

> │        ├── 📄 worker_self_heal.ts

> │      └── 📂 semantic_router/

> │        ├── 📄 index.html

> │  └── 📂 qially-com/

> │    ├── 📄 404.html

> │    ├── 📄 README (2).md

> │    ├── 📄 README.md

> │    └── 📂 _qsaysit_legacy/

> │    ├── 📄 _redirects

> │    └── 📂 assets/

> │      └── 📂 css/

> │      └── 📂 files/

> │        ├── 📄 balance-sheet-template.xlsx

> │        └── 📂 forms/

> │          └── 📂 uscis/

> │            ├── 📄 Form I-485, Application to Register Permanent Residence or Adjust Status.pdf

> │            ├── 📄 Form I-693, Report of Immigration Medical Examination and Vaccination Record.pdf

> │        ├── 📄 income-statement-template.xlsx

> │        ├── 📄 payroll-calendar-2026.pdf

> │        ├── 📄 tax-prep-checklist.pdf

> │      └── 📂 imgs/

> │        ├── 📄 allegaracasa.jpg

> │        ├── 📄 astrotext.png

> │        └── 📂 business_tools/

> │          ├── 📄 balance_sheet.svg

> │          ├── 📄 calendar.svg

> │          ├── 📄 capital.svg

> │          ├── 📄 checklist.svg

> │          ├── 📄 funding.svg

> │          ├── 📄 income.svg

> │          ├── 📄 inventory.svg

> │          ├── 📄 invoice.svg

> │          ├── 📄 payroll.svg

> │          ├── 📄 sku.svg

> │        ├── 📄 llegaracasa.jpg

> │        ├── 📄 logo.png

> │        ├── 📄 profile.jpg

> │      └── 📂 js/

> │        ├── 📄 i18n.js

> │      └── 📂 vids/

> │    ├── 📄 astro.config.mjs

> │    └── 📂 cody/

> │      ├── 📄 index.html

> │    ├── 📄 contact.json

> │    ├── 📄 footer.html

> │    └── 📂 functions/

> │      ├── 📄 [[path]].js

> │    ├── 📄 header.html

> │    ├── 📄 humans.txt

> │    ├── 📄 index.html

> │    └── 📂 kb/

> │      └── 📂 accounting-cleanup/

> │        ├── 📄 index.html

> │      └── 📂 getting-started/

> │        ├── 📄 index.html

> │      ├── 📄 index.html

> │      └── 📂 irs-notices/

> │        ├── 📄 index.html

> │      └── 📂 tax-resolution/

> │        ├── 📄 index.html

> │    ├── 📄 main.js

> │    ├── 📄 manifest.webmanifest

> │    └── 📂 modules/

> │      └── 📂 hr-ops/

> │        ├── 📄 index.html

> │      ├── 📄 index.html

> │      └── 📂 it-ai/

> │        ├── 📄 index.html

> │      └── 📂 qisuite/

> │        ├── 📄 index.html

> │      └── 📂 taxes/

> │        ├── 📄 index.html

> │        └── 📂 tax-prep-2025/

> │          ├── 📄 FormsQRCode.png

> │          ├── 📄 bookingQRCode.png

> │          └── 📂 email-templates/

> │            ├── 📄 email-01-simple-w2.html

> │            ├── 📄 email-02-self-employed.html

> │            ├── 📄 email-03-complex.html

> │            ├── 📄 email-04-itin.html

> │            ├── 📄 email-05-business.html

> │            ├── 📄 email-06-confirmation-docs.html

> │            ├── 📄 email-generic-next-steps.html

> │            ├── 📄 email-intake-received.html

> │          └── 📂 forms/

> │            ├── 📄 business.html

> │            ├── 📄 complex.html

> │            ├── 📄 head-of-household.html

> │            ├── 📄 itin.html

> │            ├── 📄 self-employed.html

> │            ├── 📄 simple-w2.html

> │          ├── 📄 index.html

> │          └── 📂 next-steps/

> │            ├── 📄 business.html

> │            ├── 📄 complex.html

> │            ├── 📄 head-of-household.html

> │            ├── 📄 index.html

> │            ├── 📄 itin.html

> │            ├── 📄 self-employed.html

> │            ├── 📄 simple-w2.html

> │          ├── 📄 prompts.md

> │          ├── 📄 qr-code.html

> │          ├── 📄 tax-prep-2025-booking.html

> │          ├── 📄 tax-prep-2025-intake.html

> │          ├── 📄 taxprepqially.jpg

> │        └── 📂 year-end-process/

> │          ├── 📄 index.html

> │    ├── 📄 orchestrate_clarity.py

> │    ├── 📄 package.json

> │    └── 📂 pages/

> │      └── 📂 budgets/

> │        ├── 📄 index.html

> │      └── 📂 business_tools/

> │        ├── 📄 index.html

> │      └── 📂 chat/

> │        ├── 📄 index.html

> │        ├── 📄 sales-iq-landing-page-qr-code.png

> │      └── 📂 compliance/

> │        ├── 📄 data-inventory.html

> │        ├── 📄 incident-response.html

> │        ├── 📄 index.html

> │        └── 📂 internal/

> │          └── 📂 provider-agreements/

> │            ├── 📄 index.html

> │          └── 📂 training-logs/

> │            ├── 📄 index.html

> │        ├── 📄 risk-assessment.html

> │        └── 📂 service_animal_gigi/

> │          ├── 📄 Gigi_Certification_Statement.html

> │          ├── 📄 Gigi_Documentation_Pack.md

> │          ├── 📄 Gigi_Documentation_Pack_Print.html

> │          ├── 📄 Gigi_Service_Dog_Training_Manual.md

> │          ├── 📄 Gigi_Services_Dog_Training_Manual_Print.html

> │          ├── 📄 Notice_Service_Animal_Status.html

> │          └── 📂 assets/

> │            ├── 📄 gigi_service_dog_hero.png

> │          ├── 📄 index.html

> │        ├── 📄 wisp-core.html

> │      └── 📂 ecard/

> │        ├── 📄 cody.vcf

> │        ├── 📄 index.html

> │      └── 📂 letters/

> │        └── 📂 client.wiletvaldo_calderon-ramirez/

> │          ├── 📄 index.html

> │          ├── 📄 infographic.png

> │          ├── 📄 review_audio.m4a

> │        └── 📂 engagement/

> │          ├── 📄 SignForm_URL_QR.png

> │          ├── 📄 engagement_standard.html

> │          ├── 📄 index.html

> │        └── 📂 evansville_inn/

> │          ├── 📄 Notice_Room_Conditions.html

> │      └── 📂 msa/

> │        ├── 📄 index.html

> │      └── 📂 portfolio/

> │        ├── 📄 index.html

> │      └── 📂 privacy/

> │        ├── 📄 index.html

> │      └── 📂 referral/

> │        └── 📂 cashapp/

> │          ├── 📄 index.html

> │        ├── 📄 index.html

> │        └── 📂 quickbooks/

> │          ├── 📄 index.html

> │        └── 📂 zoho/

> │          ├── 📄 index.html

> │      └── 📂 resources/

> │        ├── 📄 index.html

> │      └── 📂 review/

> │        ├── 📄 index.html

> │      └── 📂 services/

> │        ├── 📄 index.html

> │      └── 📂 showcases/

> │        └── 📂 20000-swing/

> │          ├── 📄 index.html

> │        ├── 📄 videos.html

> │      └── 📂 terms/

> │        ├── 📄 index.html

> │    └── 📂 public/

> │      ├── 📄 favicon.ico

> │      ├── 📄 favicon.svg

> │    └── 📂 qially-com-v2.0/

> │      └── 📂 QiAlly-com/

> │        ├── 📄 index.html

> │        ├── 📄 package-lock.json

> │        ├── 📄 postcss.config.js

> │        └── 📂 public/

> │        └── 📂 src/

> │      ├── 📄 README.md

> │      └── 📂 accounting/

> │      └── 📂 assets/

> │        └── 📂 css/

> │        └── 📂 js/

> │        └── 📂 public/

> │      └── 📂 blog/

> │      ├── 📄 contact.json

> │      └── 📂 files/

> │        ├── 📄 cody_rice_velasquez-fullstack.pdf

> │        └── 📂 forms/

> │        └── 📂 resume/

> │      ├── 📄 footer.html

> │      └── 📂 forms/

> │      └── 📂 hr-ops/

> │        ├── 📄 index.html

> │      ├── 📄 humans.txt

> │      └── 📂 images/

> │        ├── 📄 cover.jpg

> │        ├── 📄 profile.jpg

> │        ├── 📄 video-logo.mp4

> │      └── 📂 individual/

> │        ├── 📄 index.html

> │      └── 📂 it-ai/

> │      └── 📂 legal/

> │      └── 📂 portfolio/

> │        ├── 📄 q-showcase-light.html

> │      ├── 📄 privacy.html

> │      └── 📂 qisuite/

> │      └── 📂 review/

> │        ├── 📄 qrcode_www.google.com.png

> │      └── 📂 service-agreement/

> │      └── 📂 showcases/

> │        └── 📂 20000-swing/

> │        ├── 📄 videos.html

> │      ├── 📄 sitemap.xml

> │      └── 📂 taxes/

> │        ├── 📄 index.html

> │        └── 📂 itin/

> │    ├── 📄 robots.txt

> │    ├── 📄 service-worker.js

> │    ├── 📄 sitemap.xml

> │    └── 📂 sites_QiAlly.com_cashapp_bonus/

> │      ├── 📄 Cash_App_$15_Bonus_Five_Simple_Steps.m4a

> │      ├── 📄 bonus_cody_en.mp3

> │      ├── 📄 bonus_cody_es.mp3

> │      ├── 📄 bonus_explainer_nlm_en.mp3

> │      ├── 📄 bonus_explainer_nlm_es.mp3

> │      ├── 📄 bonus_steps_es.png

> │      ├── 📄 index.html

> │      ├── 📄 infographic.png

> │      ├── 📄 unnamed.png

> │    └── 📂 sites_QiAlly.com_flows/

> │      ├── 📄 README.md

> │      └── 📂 assets/

> │        ├── 📄 favicon.ico

> │        ├── 📄 logo.svg

> │        ├── 📄 styles.css

> │      ├── 📄 index.html

> │      ├── 📄 privacy.html

> │      ├── 📄 terms.html

> │    └── 📂 sites_QiAlly.com_helpcody/

> │      ├── 📄 README.md

> │      ├── 📄 data.csv

> │      ├── 📄 index.html

> │    └── 📂 sites_QiAlly.com_tax99/

> │      ├── 📄 README.md

> │      ├── 📄 index.html

> │      └── 📂 steps/

> │        ├── 📄 index.html

> │      └── 📂 templates/

> │        ├── 📄 email-template-client.html

> │        ├── 📄 email-template-internal.html

> │        ├── 📄 index.html

> │      ├── 📄 worker.js

> │      ├── 📄 wrangler.toml

> │    └── 📂 sites_Qially.com_kb/

> │    └── 📂 src/

> │      └── 📂 pages/

> │        ├── 📄 index.astro

> │    ├── 📄 tsconfig.json

> │    ├── 📄 vizvibe.mmd

> │  └── 📂 qione-portal/

> │    └── 📂 _dirtfree_legacy/

> │      ├── 📄 ACCOUNT_LINKING.md

> │      ├── 📄 BLUEPRINT.md

> │      ├── 📄 DIRT_FREE_PROMPTS.md

> │      ├── 📄 LAUNCH_CHECKLIST.md

> │      ├── 📄 LICENSE

> │      ├── 📄 QiOS_Local_Only.code-workspace

> │      ├── 📄 README.md

> │      ├── 📄 REALTIME_SYNC.md

> │      ├── 📄 convert_blueprint.py

> │      └── 📂 dirt-free-portal/

> │        ├── 📄 BUNDLE-OPTIMIZATION-SUMMARY.md

> │        ├── 📄 DEPLOYMENT.md

> │        ├── 📄 ERROR-TRACKING.md

> │        ├── 📄 LOGGING.md

> │        ├── 📄 OPTIMIZATION-SUMMARY.md

> │        ├── 📄 PERFORMANCE-MONITORING.md

> │        ├── 📄 PERFORMANCE-OPTIMIZATION.md

> │        ├── 📄 RATE-LIMITING.md

> │        ├── 📄 README.md

> │        ├── 📄 SECURITY-HEADERS.md

> │        └── 📂 __tests__/

> │          ├── 📄 sample.test.tsx

> │        ├── 📄 components.json

> │        └── 📂 docs/

> │          ├── 📄 API.md

> │          ├── 📄 DATABASE_OPTIMIZATION.md

> │          ├── 📄 LAUNCH_PROCEDURES.md

> │          ├── 📄 PERFORMANCE.md

> │          ├── 📄 PRE-LAUNCH-CHECKLIST.md

> │          ├── 📄 USER_GUIDE.md

> │        └── 📂 e2e/

> │          ├── 📄 appointments.spec.ts

> │          └── 📂 fixtures/

> │            ├── 📄 auth.ts

> │          ├── 📄 login.spec.ts

> │        ├── 📄 eslint.config.mjs

> │        ├── 📄 instrumentation.ts

> │        ├── 📄 jest.config.js

> │        ├── 📄 jest.setup.js

> │        ├── 📄 middleware.ts

> │        ├── 📄 next.config.ts

> │        ├── 📄 next.config.ts.bak

> │        ├── 📄 next.config.ts.bak2

> │        ├── 📄 package-lock.json

> │        ├── 📄 package.json

> │        ├── 📄 playwright.config.ts

> │        ├── 📄 postcss.config.mjs

> │        └── 📂 public/

> │        └── 📂 scripts/

> │          ├── 📄 create-test-customer.mjs

> │          ├── 📄 monitor-production.mjs

> │          ├── 📄 performance-audit.mjs

> │          ├── 📄 pre-launch-check.mjs

> │        ├── 📄 sentry.client.config.ts

> │        ├── 📄 sentry.edge.config.ts

> │        ├── 📄 sentry.server.config.ts

> │        └── 📂 src/

> │          └── 📂 __tests__/

> │            └── 📂 api/

> │              └── 📂 payments/

> │                ├── 📄 create-intent.test.ts

> │                ├── 📄 webhooks.test.ts

> │            └── 📂 components/

> │              └── 📂 dashboard/

> │                ├── 📄 sidebar.test.tsx

> │            └── 📂 fixtures/

> │              ├── 📄 invoices.ts

> │              ├── 📄 payments.ts

> │            └── 📂 helpers/

> │              ├── 📄 stripe-mocks.ts

> │              ├── 📄 supabase-mocks.ts

> │            └── 📂 lib/

> │              ├── 📄 utils.test.ts

> │          └── 📂 app/

> │            └── 📂 (auth)/

> │              └── 📂 login/

> │            └── 📂 (dashboard)/

> │              └── 📂 dashboard/

> │                └── 📂 account/

> │                  ├── 📄 page.tsx

> │                  └── 📂 payment-methods/

> │                    ├── 📄 page.tsx

> │                    ├── 📄 page.tsx.bak

> │                └── 📂 appointments/

> │                  └── 📂 [id]/

> │                    ├── 📄 page.tsx.bak2

> │                    └── 📂 reschedule/

> │                      ├── 📄 layout.tsx

> │                      ├── 📄 page.tsx

> │                  └── 📂 new/

> │                    └── 📂 confirm/

> │                      ├── 📄 page.tsx

> │                    └── 📂 datetime/

> │                    ├── 📄 page.tsx

> │                  ├── 📄 page.tsx

> │                └── 📂 documents/

> │                  ├── 📄 page.tsx

> │                  └── 📂 warranties/

> │                └── 📂 help/

> │                  ├── 📄 page.tsx

> │                └── 📂 invoices/

> │                  └── 📂 [id]/

> │                    └── 📂 pay/

> │                      ├── 📄 page.tsx.bak

> │                    └── 📂 success/

> │                      ├── 📄 page.tsx

> │                  ├── 📄 page.tsx

> │                └── 📂 messages/

> │                  └── 📂 [id]/

> │                    ├── 📄 page.tsx.bak

> │                    ├── 📄 page.tsx.bak2

> │                  └── 📂 new/

> │                  ├── 📄 page.tsx

> │                └── 📂 notifications/

> │                  ├── 📄 page.tsx

> │                ├── 📄 page.tsx

> │                └── 📂 rewards/

> │                  └── 📂 history/

> │                  ├── 📄 page.tsx

> │                  └── 📂 referrals/

> │                    ├── 📄 page.tsx

> │              ├── 📄 error.tsx

> │              ├── 📄 layout.tsx

> │            └── 📂 api/

> │              └── 📂 analytics/

> │                └── 📂 portal-stats/

> │                  ├── 📄 route.ts

> │                └── 📂 track-session/

> │                  ├── 📄 route.ts

> │              └── 📂 appointments/

> │                └── 📂 [id]/

> │                  └── 📂 cancel/

> │                    ├── 📄 route.ts

> │              └── 📂 cache/

> │                └── 📂 clear/

> │                  ├── 📄 route.ts

> │                └── 📂 stats/

> │                  ├── 📄 route.ts

> │              └── 📂 health/

> │                ├── 📄 route.ts

> │              └── 📂 invoices/

> │                └── 📂 [id]/

> │                  └── 📂 pdf/

> │                    ├── 📄 route.ts

> │              └── 📂 notifications/

> │                └── 📂 send-email/

> │                  ├── 📄 route.ts

> │                  ├── 📄 route.ts.bak

> │              └── 📂 payments/

> │                └── 📂 confirm/

> │                  ├── 📄 route.ts

> │                  ├── 📄 route.ts.bak

> │                └── 📂 create-intent/

> │                  ├── 📄 route.ts

> │                └── 📂 export/

> │                  ├── 📄 route.ts

> │                └── 📂 methods/

> │                  └── 📂 [id]/

> │                    ├── 📄 route.ts

> │                  ├── 📄 route.ts

> │                └── 📂 setup-intent/

> │                  ├── 📄 route.ts

> │              └── 📂 rewards/

> │                └── 📂 [id]/

> │                  └── 📂 redeem/

> │                    ├── 📄 route.ts

> │              └── 📂 webhooks/

> │                └── 📂 stripe/

> │                  ├── 📄 route.ts

> │            ├── 📄 error.tsx

> │            ├── 📄 global-error.tsx

> │            ├── 📄 globals.css

> │            ├── 📄 layout.tsx

> │            ├── 📄 not-found.tsx

> │          └── 📂 components/

> │            └── 📂 analytics/

> │              ├── 📄 payment-success-tracker.tsx

> │              ├── 📄 performance-monitor.tsx

> │              ├── 📄 session-tracker.tsx

> │            └── 📂 dashboard/

> │              ├── 📄 header.tsx

> │              ├── 📄 mobile-nav.tsx

> │              ├── 📄 quick-actions-card.tsx

> │              ├── 📄 recent-activity-section.tsx

> │              ├── 📄 sidebar.tsx

> │            └── 📂 documents/

> │              ├── 📄 photo-gallery.tsx

> │            ├── 📄 error-boundary.tsx

> │            └── 📂 errors/

> │              ├── 📄 customer-not-found.tsx

> │            └── 📂 help/

> │              ├── 📄 print-button.tsx

> │            └── 📂 invoices/

> │              ├── 📄 DownloadButton.tsx

> │            └── 📂 messages/

> │              ├── 📄 AttachmentCard.tsx

> │              ├── 📄 MessageList.tsx

> │              ├── 📄 MessageThread.tsx

> │              ├── 📄 NewMessageDialog.tsx

> │            └── 📂 notifications/

> │              ├── 📄 NotificationBell.tsx

> │              ├── 📄 NotificationCenter.tsx

> │              ├── 📄 notification-provider.tsx

> │            └── 📂 payments/

> │              ├── 📄 AddCardDialog.tsx

> │              ├── 📄 payment-form.tsx

> │            └── 📂 rewards/

> │              ├── 📄 redeem-button.tsx

> │            └── 📂 ui/

> │              ├── 📄 alert-dialog.tsx

> │              ├── 📄 alert.tsx

> │              ├── 📄 avatar.tsx

> │              ├── 📄 button.tsx

> │              ├── 📄 calendar.tsx

> │              ├── 📄 checkbox.tsx

> │              ├── 📄 dialog.tsx

> │              ├── 📄 dropdown-menu.tsx

> │              ├── 📄 file-upload.tsx

> │              ├── 📄 label.tsx

> │              ├── 📄 optimized-image.tsx

> │              ├── 📄 popover.tsx

> │              ├── 📄 scroll-area.tsx

> │              ├── 📄 select.tsx

> │              ├── 📄 separator.tsx

> │              ├── 📄 sheet.tsx

> │              ├── 📄 skeleton.tsx

> │              ├── 📄 sonner.tsx

> │              ├── 📄 switch.tsx

> │              ├── 📄 tabs.tsx

> │              ├── 📄 tooltip.tsx

> │          └── 📂 hooks/

> │            ├── 📄 useUnreadMessages.ts

> │          └── 📂 lib/

> │            └── 📂 analytics/

> │            ├── 📄 analytics.ts

> │              ├── 📄 session-tracking.ts

> │            ├── 📄 audit.ts

> │            ├── 📄 db-cache.ts

> │            └── 📂 email/

> │              ├── 📄 send.ts

> │              ├── 📄 templates.ts

> │            ├── 📄 env.ts

> │            ├── 📄 logger.ts

> │            ├── 📄 monitoring.ts

> │            ├── 📄 notifications.ts

> │            ├── 📄 pdf-generator-lazy.ts

> │            ├── 📄 pdf-generator.ts

> │            ├── 📄 rate-limit.ts

> │            ├── 📄 sentry-utils.ts

> │            ├── 📄 storage.ts

> │            └── 📂 stripe/

> │              ├── 📄 client.ts

> │              ├── 📄 server.ts

> │            └── 📂 supabase/

> │              ├── 📄 client.ts

> │              ├── 📄 middleware.ts

> │              ├── 📄 realtime-helper.ts

> │              ├── 📄 server.ts

> │          └── 📂 types/

> │        └── 📂 supabase/

> │          ├── 📄 01-create-portal-tables.sql

> │          ├── 📄 02-apply-rls-policies.sql

> │          ├── 📄 03-create-storage-buckets.sql

> │          ├── 📄 03-create-test-customer.sql

> │          ├── 📄 04-add-file-attachments-support.sql

> │          ├── 📄 05-add-missing-message-columns.sql

> │          ├── 📄 06-add-reply-attachments-support.sql

> │          ├── 📄 07-add-attachment-analytics.sql

> │          ├── 📄 08-create-notifications-table.sql

> │          ├── 📄 09-add-portal-analytics.sql

> │          ├── 📄 10-add-performance-indexes.sql

> │          ├── 📄 11-create-audit-logs-table.sql

> │          ├── 📄 README.md

> │          ├── 📄 policies.sql

> │        ├── 📄 tailwind.config.ts

> │        ├── 📄 tsconfig.json

> │        ├── 📄 vercel.json

> │      ├── 📄 middleware.ts

> │      ├── 📄 package-lock.json

> │      ├── 📄 package.json

> │      └── 📂 src/

> │        └── 📂 app/

> │          └── 📂 (auth)/

> │            ├── 📄 layout.tsx

> │            └── 📂 login/

> │              ├── 📄 page.tsx

> │          └── 📂 (dashboard)/

> │            └── 📂 dashboard/

> │              └── 📂 account/

> │                ├── 📄 layout.tsx

> │                ├── 📄 page.tsx

> │                └── 📂 payment-methods/

> │                  ├── 📄 layout.tsx

> │                  ├── 📄 page.tsx

> │              └── 📂 appointments/

> │                └── 📂 [id]/

> │                  ├── 📄 page.tsx

> │                  └── 📂 reschedule/

> │                    ├── 📄 page.tsx

> │                └── 📂 new/

> │                  └── 📂 confirm/

> │                    ├── 📄 page.tsx

> │                  └── 📂 datetime/

> │                    ├── 📄 page.tsx

> │                  ├── 📄 layout.tsx

> │              └── 📂 documents/

> │                ├── 📄 page.tsx

> │                └── 📂 warranties/

> │                  ├── 📄 page.tsx

> │              ├── 📄 example-realtime-usage.tsx

> │              └── 📂 history/

> │                ├── 📄 page.tsx

> │              └── 📂 invoices/

> │                └── 📂 [id]/

> │                  └── 📂 pay/

> │                    ├── 📄 layout.tsx

> │                    ├── 📄 page.tsx

> │                  └── 📂 success/

> │                    ├── 📄 page.tsx

> │                ├── 📄 page.tsx

> │              ├── 📄 loading.tsx

> │              └── 📂 messages/

> │                └── 📂 [id]/

> │                  ├── 📄 page.tsx

> │                └── 📂 new/

> │                  ├── 📄 layout.tsx

> │                  ├── 📄 page.tsx

> │                ├── 📄 page.tsx

> │              ├── 📄 page.tsx

> │              └── 📂 rewards/

> │                └── 📂 history/

> │                  ├── 📄 page.tsx

> │                └── 📂 referrals/

> │                  ├── 📄 layout.tsx

> │            ├── 📄 error.tsx

> │            ├── 📄 layout.tsx

> │          └── 📂 api/

> │            └── 📂 appointments/

> │              └── 📂 [id]/

> │                └── 📂 cancel/

> │                  ├── 📄 route.ts

> │            └── 📂 auth/

> │              └── 📂 link-account/

> │                ├── 📄 route.ts

> │              └── 📂 sso/

> │                ├── 📄 route.ts

> │                └── 📂 verify/

> │                  ├── 📄 route.ts

> │            └── 📂 payments/

> │              └── 📂 confirm/

> │                ├── 📄 route.ts

> │              └── 📂 create-intent/

> │                ├── 📄 route.ts

> │              └── 📂 export/

> │                ├── 📄 route.ts

> │              └── 📂 methods/

> │                └── 📂 [id]/

> │                  ├── 📄 route.ts

> │                ├── 📄 route.ts

> │            └── 📂 rewards/

> │              └── 📂 [id]/

> │                └── 📂 redeem/

> │                  ├── 📄 route.ts

> │            └── 📂 webhooks/

> │              └── 📂 stripe/

> │                ├── 📄 route.ts

> │          ├── 📄 page.tsx

> │        └── 📂 components/

> │          └── 📂 analytics/

> │            ├── 📄 payment-success-tracker.tsx

> │          └── 📂 dashboard/

> │            ├── 📄 AccountLinkingBanner.tsx

> │            ├── 📄 header.tsx

> │            ├── 📄 sidebar.tsx

> │          └── 📂 documents/

> │            ├── 📄 photo-gallery.tsx

> │            ├── 📄 service-timeline.tsx

> │          └── 📂 messages/

> │            ├── 📄 reply-form.tsx

> │          └── 📂 notifications/

> │            ├── 📄 notification-provider.tsx

> │          └── 📂 payments/

> │          └── 📂 realtime/

> │            ├── 📄 ConnectionStatus.tsx

> │          └── 📂 rewards/

> │            ├── 📄 redeem-button.tsx

> │          └── 📂 ui/

> │            ├── 📄 badge.tsx

> │            ├── 📄 card.tsx

> │            ├── 📄 input.tsx

> │            ├── 📄 progress.tsx

> │            ├── 📄 textarea.tsx

> │        └── 📂 hooks/

> │          ├── 📄 useRealtime.ts

> │        └── 📂 lib/

> │          ├── 📄 analytics.ts

> │          └── 📂 auth/

> │            ├── 📄 signup.ts

> │            ├── 📄 sso-token.ts

> │          └── 📂 email/

> │            ├── 📄 send.ts

> │            ├── 📄 templates.ts

> │          ├── 📄 env.ts

> │          ├── 📄 rate-limit.ts

> │          └── 📂 realtime/

> │            ├── 📄 sync.ts

> │          └── 📂 stripe/

> │            ├── 📄 client.ts

> │            ├── 📄 server.ts

> │          └── 📂 supabase/

> │            ├── 📄 client.ts

> │            ├── 📄 middleware.ts

> │            ├── 📄 server.ts

> │          ├── 📄 utils.ts

> │        └── 📂 types/

> │          ├── 📄 database.types.ts

> │          ├── 📄 index.ts

> │      └── 📂 supabase/

> │        ├── 📄 policies.sql

> │      ├── 📄 tailwind.config.ts

> │      ├── 📄 vercel.json

> │    └── 📂 app/

> │      └── 📂 (portal)/

> │        ├── 📄 layout.tsx

> │        └── 📂 objects/

> │          └── 📂 [objectKey]/

> │            └── 📂 contract/

> │              ├── 📄 page.tsx

> │            └── 📂 csv/

> │              └── 📂 [formKey]/

> │                ├── 📄 page.tsx

> │            └── 📂 forms/

> │              └── 📂 [formKey]/

> │                ├── 📄 page.tsx

> │            ├── 📄 page.tsx

> │        ├── 📄 page.tsx

> │        └── 📂 qichronicle/

> │          ├── 📄 page.tsx

> │      └── 📂 api/

> │        └── 📂 qichronicle/

> │          └── 📂 moments/

> │            └── 📂 [id]/

> │              ├── 📄 route.ts

> │            ├── 📄 route.ts

> │      ├── 📄 layout.tsx

> │    ├── 📄 next-env.d.ts

> │    ├── 📄 next.config.mjs

> │    ├── 📄 package.json

> │    └── 📂 src/

> │      └── 📂 qione/

> │        └── 📂 contracts/

> │          ├── 📄 deriveContract.ts

> │        └── 📂 csv/

> │          ├── 📄 csvParse.ts

> │          ├── 📄 csvValidate.ts

> │        └── 📂 objects/

> │          ├── 📄 appointment.ts

> │          ├── 📄 case.ts

> │          ├── 📄 chore.ts

> │          ├── 📄 contact.ts

> │          ├── 📄 expense.ts

> │          ├── 📄 index.ts

> │          ├── 📄 medication.ts

> │          ├── 📄 patient.ts

> │          ├── 📄 types.ts

> │      └── 📂 ui/

> │        └── 📂 components/

> │          ├── 📄 DataTable.tsx

> │          ├── 📄 FieldRenderer.tsx

> │          ├── 📄 FormRenderer.tsx

> │          ├── 📄 Sidebar.tsx

> │          ├── 📄 Topbar.tsx

> │        └── 📂 styles/

> │          ├── 📄 globals.css

> │    ├── 📄 tsc_errors.txt

> │    ├── 📄 tsc_errors_utf8.txt

> │    ├── 📄 tsconfig.json

> │  └── 📂 qivault-web/

> │    ├── 📄 README.md

> │    ├── 📄 contract.md

> │    ├── 📄 package.json

> │    └── 📂 src/

> │      ├── 📄 App.tsx

> │      └── 📂 pages/

> │        ├── 📄 DocumentDetailPage.tsx

> │        ├── 📄 InboxPage.tsx

> │        ├── 📄 SearchPage.tsx

> │        ├── 📄 SettingsPage.tsx

> │        ├── 📄 TagsPage.tsx

> │      └── 📂 services/

> │        ├── 📄 storage.ts

> │      └── 📂 types/

> │        ├── 📄 index.ts

> │    ├── 📄 vite.config.ts

> └── 📂 content/

> │  ├── 📄 README.md

> └── 📂 experiments/

> ├── 📄 package.json

> └── 📂 packages/

> │  └── 📂 assets/

> │    ├── 📄 introvideo.mp4

> │    ├── 📄 package.json

> │    └── 📂 public/

> │      ├── 📄 introvideo.mp4

> │    └── 📂 src/

> │      └── 📂 brand/

> │      └── 📂 icons/

> │        ├── 📄 home-40.svg

> │      ├── 📄 index.ts

> │  └── 📂 auth/

> │    ├── 📄 package.json

> │    └── 📂 src/

> │      ├── 📄 index.ts

> │  └── 📂 config/

> │    ├── 📄 package.json

> │    └── 📂 src/

> │      ├── 📄 index.ts

> │      ├── 📄 repoRules.ts

> │      ├── 📄 rulesRegistry.ts

> │  └── 📂 database/

> │    └── 📂 migrations/

> │    ├── 📄 package.json

> │    └── 📂 src/

> │      ├── 📄 contentFrontMatter.ts

> │      ├── 📄 database.types.ts

> │      ├── 📄 index.ts

> │  └── 📂 email/

> │    └── 📂 partials/

> │      ├── 📄 footer.html

> │      ├── 📄 header.html

> │    ├── 📄 render.ts

> │    └── 📂 supabase-auth/

> │      ├── 📄 README.md

> │      ├── 📄 change_email.html

> │      ├── 📄 confirmation.html

> │      ├── 📄 invite.html

> │      ├── 📄 magic_link.html

> │      ├── 📄 otp.html

> │      ├── 📄 reauthentication.html

> │      ├── 📄 recovery.html

> │    └── 📂 templates/

> │      └── 📂 billing/

> │        ├── 📄 invoice.html

> │      └── 📂 general/

> │        ├── 📄 welcome.html

> │      └── 📂 projects/

> │        ├── 📄 update.html

> │      └── 📂 tax/

> │        ├── 📄 return-accepted.html

> │  └── 📂 obsidian-engine/

> │  └── 📂 schemas/

> │    ├── 📄 package.json

> │    └── 📂 src/

> │      ├── 📄 contentFrontMatter.ts

> │      ├── 📄 database.types.ts

> │      ├── 📄 index.ts

> │  └── 📂 sdk/

> │  └── 📂 supabase/

> │    ├── 📄 bootstrap_tenant.sql

> │    └── 📂 migrations/

> │      ├── 📄 00001_core_saas_setup.sql

> │      ├── 📄 00002_vault_and_queues.sql

> │      ├── 📄 00003_app_schemas.sql

> │      ├── 📄 00004_content_index.sql

> │      ├── 📄 00005_cms_schema.sql

> │      ├── 📄 00006_qivault_docs.sql

> │      ├── 📄 00007_qione_platform.sql

> │      ├── 📄 00008_qihome_app.sql

> │      ├── 📄 00009_qichronicle.sql

> │      ├── 📄 001_init_qione.sql

> │      ├── 📄 002_qihome_mvp.sql

> │      ├── 📄 003_qitax_returns.sql

> │      ├── 📄 003a_qitax_seed.sql

> │    ├── 📄 package.json

> │    └── 📂 src/

> │      ├── 📄 index.ts

> │  └── 📂 ui/

> │    ├── 📄 package.json

> │    └── 📂 src/

> │      ├── 📄 index.ts

> │  └── 📂 utils/

> │    ├── 📄 package.json

> │    └── 📂 src/

> │      ├── 📄 index.ts

> ├── 📄 pnpm-workspace.yaml

> └── 📂 python_core/

> │  └── 📂 agents/

> │  └── 📂 document-processors/

> │    ├── 📄 WEB_INTERFACE.md

> │    ├── 📄 __init__.py

> │    ├── 📄 cli.py

> │    ├── 📄 config.py

> │    ├── 📄 exceptions.py

> │    ├── 📄 extractor.py

> │    ├── 📄 index.html

> │    └── 📂 pipeline/

> │      ├── 📄 __init__.py

> │      ├── 📄 index.html

> │      ├── 📄 layout_detector.py

> │      ├── 📄 model_downloader.py

> │      ├── 📄 nanonets_processor.py

> │      ├── 📄 neural_document_processor.py

> │      ├── 📄 ocr_service.py

> │    └── 📂 processors/

> │      ├── 📄 __init__.py

> │      ├── 📄 base.py

> │      ├── 📄 cloud_processor.py

> │      ├── 📄 docx_processor.py

> │      ├── 📄 excel_processor.py

> │      ├── 📄 gpu_processor.py

> │      ├── 📄 html_processor.py

> │      ├── 📄 image_processor.py

> │      ├── 📄 index.html

> │      ├── 📄 pdf_processor.py

> │      ├── 📄 pptx_processor.py

> │      ├── 📄 txt_processor.py

> │      ├── 📄 url_processor.py

> │    ├── 📄 result.py

> │    └── 📂 services/

> │      ├── 📄 __init__.py

> │      ├── 📄 auth_service.py

> │      ├── 📄 index.html

> │      ├── 📄 ollama_service.py

> │    └── 📂 static/

> │      ├── 📄 index.html

> │      ├── 📄 logo_clean.png

> │      ├── 📄 script.js

> │      ├── 📄 styles.css

> │    └── 📂 templates/

> │      ├── 📄 index.html

> │    └── 📂 utils/

> │      ├── 📄 __init__.py

> │      ├── 📄 gpu_utils.py

> │      ├── 📄 index.html

> │    ├── 📄 web_app.py

> │  └── 📂 gina-ai/

> │    ├── 📄 index.html

> │    ├── 📄 main.py

> │    ├── 📄 requirements.txt

> │  ├── 📄 requirements.txt

> ├── 📄 repo.rules.json

> ├── 📄 requirements.txt

> └── 📂 scripts/

> │  ├── 📄 README.md

> │  ├── 📄 README_add_frontmatter.md

> │  ├── 📄 README_generate_indexes.md

> │  ├── 📄 README_organize_vault.md

> │  ├── 📄 SCANNER_AGENT_README.md

> │  ├── 📄 _tools.md

> │  ├── 📄 copy-assets.mjs

> │  └── 📂 database/

> │  └── 📂 exe/

> │    ├── 📄 dotenv.exe

> │    ├── 📄 f2py.exe

> │    ├── 📄 fastapi.exe

> │    ├── 📄 google-oauthlib-tool.exe

> │    ├── 📄 normalizer.exe

> │    ├── 📄 numpy-config.exe

> │    ├── 📄 pip.exe

> │    ├── 📄 pyrsa-decrypt.exe

> │    ├── 📄 pyrsa-encrypt.exe

> │    ├── 📄 pyrsa-keygen.exe

> │    ├── 📄 pyrsa-priv2pub.exe

> │    ├── 📄 pyrsa-sign.exe

> │    ├── 📄 pyrsa-verify.exe

> │    ├── 📄 uvicorn.exe

> │  └── 📂 git_pusher/

> │    ├── 📄 README.md

> │    ├── 📄 git_manifest.json

> │    ├── 📄 git_pusher.py

> │  └── 📂 hotkeys/

> │    ├── 📄 git-autopush.ahk

> │  └── 📂 inbox/

> │    ├── 📄 audit_inbox.ts

> │    ├── 📄 dedup_detect.ts

> │    ├── 📄 fix_inbox_names.ts

> │    ├── 📄 merge_plan.ts

> │    ├── 📄 normalize_inbox.ts

> │    ├── 📄 run_inbox.ts

> │  └── 📂 local/

> │    └── 📂 file_ops/

> │      └── 📂 unzip_goblin/

> │  └── 📂 modules/

> │    ├── 📄 create_app.py

> │  ├── 📄 navigator-3d.html

> │  └── 📂 node/

> │    ├── 📄 build-timeline-713.js

> │    ├── 📄 build-timeline.js

> │  └── 📂 pdf/

> │    ├── 📄 process_inbox_pdfs.ts

> │    ├── 📄 process_pdf.ts

> │    ├── 📄 validate_pdfs.ts

> │  └── 📂 poppler-25.12.0/

> │    └── 📂 Library/

> │      └── 📂 bin/

> │      └── 📂 include/

> │      └── 📂 lib/

> │      └── 📂 share/

> │    └── 📂 share/

> │      └── 📂 poppler/

> │  └── 📂 python/

> │    ├── 📄 README_DEV_ERROR_MEMORY.md

> │    ├── 📄 _7.10_python.md

> │    └── 📂 agents/

> │      ├── 📄 qios_agent.py

> │    └── 📂 audit/

> │      ├── 📄 check-md.py

> │      ├── 📄 fix-spaces.py

> │      ├── 📄 linter.py

> │      ├── 📄 linterrunner.py

> │    ├── 📄 build_file_registry.py

> │    ├── 📄 clean_qi_prefixes.py

> │    ├── 📄 cleanup_app_roots.py

> │    ├── 📄 cleanup_intake_and_trash.py

> │    ├── 📄 code_extractor.py

> │    └── 📂 compile/

> │      ├── 📄 code-compile-review.py

> │    └── 📂 convert/

> │      ├── 📄 enhance-mkv.PY

> │      ├── 📄 flat-folders.py

> │      ├── 📄 unzip_downloads.py

> │    └── 📂 core/

> │      ├── 📄 add_frontmatter.py

> │      ├── 📄 generate_indexes.py

> │      ├── 📄 organize_vault_structure.py

> │    └── 📂 create/

> │      ├── 📄 attach-mirrors.py

> │      ├── 📄 cloudflare-create-md.py

> │      ├── 📄 create-canvas-directory.py

> │      ├── 📄 create-canvas.py

> │    └── 📂 csv-to-md/

> │      ├── 📄 README.md

> │      ├── 📄 USAGE.md

> │      ├── 📄 _Convert_csv_to_md.md

> │      ├── 📄 _csv-to-md.md

> │      ├── 📄 check-csv-md.py

> │      ├── 📄 csv_to_md.py

> │      └── 📂 data/

> │      ├── 📄 mapping.json

> │      └── 📂 mapping_examples/

> │      └── 📂 output/

> │      └── 📂 tests/

> │    └── 📂 debug/

> │      ├── 📄 debug-maps.py

> │    ├── 📄 detect_stubs.py

> │    └── 📂 directory_tools/

> │      ├── 📄 directory_mapper.py

> │      ├── 📄 flatten_directory.py

> │    ├── 📄 fast_move_notion_md_twins.py

> │    ├── 📄 fast_move_tiny_id_md.py

> │    ├── 📄 final_structure.py

> │    ├── 📄 find_duplicates.py

> │    ├── 📄 fs_scanner.py

> │    ├── 📄 generate_kb_from_json.py

> │    ├── 📄 get_file_error_context.py

> │    └── 📂 housekeeping/

> │      ├── 📄 housekeeper_runner.py

> │      ├── 📄 organize_inbox_complete.py

> │    ├── 📄 immigration_structure_example.py

> │    ├── 📄 log_error_to_supabase.py

> │    ├── 📄 mark_error_resolved.py

> │    ├── 📄 master_experiment_consolidation.py

> │    └── 📂 media_processing/

> │      ├── 📄 merge_mkvs.py

> │    ├── 📄 merge_app_docs.py

> │    ├── 📄 merge_experiment_twins.py

> │    ├── 📄 move_chatgpt_audio_from_registry.py

> │    ├── 📄 move_md_by_body_content.py

> │    ├── 📄 move_notion_md_twins_from_registry.py

> │    ├── 📄 move_notions_export_md_from_registry.py

> │    ├── 📄 move_safetodelete_media_to_assets.py

> │    ├── 📄 move_trash_dupes_from_registry.py

> │    ├── 📄 move_trash_image_name_matches_from_registry.py

> │    ├── 📄 move_trash_junk_from_registry.py

> │    ├── 📄 move_trash_nonimportant_exts_from_registry.py

> │    └── 📂 obsidian_tools/

> │      ├── 📄 generate_obsidian_canvas_interactive.py

> │    └── 📂 other_tools/

> │      ├── 📄 examine_db.py

> │      ├── 📄 merge_media_tree.py

> │    └── 📂 qi_codex_tool/

> │      ├── 📄 README.md

> │      ├── 📄 qi_codex_tool.py

> │      ├── 📄 usage.md

> │    ├── 📄 qicompiler.py

> │    └── 📂 qieos_tools/

> │      ├── 📄 README_migrate_frontmatter.md

> │      ├── 📄 qd_autoname.py

> │      ├── 📄 qi_migrate.py

> │    ├── 📄 qios_dedup_tool.py

> │    ├── 📄 queue_loader.py

> │    └── 📂 review/

> │      ├── 📄 compare-csv-md.py

> │      ├── 📄 compare-drive.py

> │      ├── 📄 search-csv.py

> │      ├── 📄 sort-files.py

> │    ├── 📄 run_system_test.ps1

> │    ├── 📄 safe_collect_intake_and_trash.py

> │    ├── 📄 simple_structure.py

> │    ├── 📄 slugs_mapping.json.py

> │    ├── 📄 slugs_mapping.py

> │    ├── 📄 slugs_mapping.yaml.py

> │    ├── 📄 smart_target_directories.py

> │    ├── 📄 spawn_client_os.py

> │    ├── 📄 spawn_mypunchpro.py

> │    ├── 📄 stub_list.txt

> │    ├── 📄 stub_results.txt

> │    ├── 📄 summarize_qios_files.py

> │    ├── 📄 summarize_trash_from_registry.py

> │    ├── 📄 sync_errors_to_markdown.py

> │    ├── 📄 test_abbreviations.py

> │    ├── 📄 test_gina_chat_simple.ps1

> │    ├── 📄 tree_compiler.py

> │    ├── 📄 ultra_clean_folders.py

> │  ├── 📄 qios_tools.json

> │  └── 📂 qitax-cli/

> │  └── 📂 rules/

> │    ├── 📄 audit_repo_rules.ts

> │    ├── 📄 fix_repo_rules.ts

> │  └── 📂 scripts/

> │    ├── 📄 build-timeline.js

> │    ├── 📄 build.ps1

> │    ├── 📄 convert_to_csv.js

> │    ├── 📄 extract-code-report.js

> │    ├── 📄 timeline-loader.js

> │  └── 📂 shell/

> │    ├── 📄 README.md

> │    ├── 📄 README_LAUNCHERS.md

> │    ├── 📄 RUN_COMPLETE_INBOX_ORGANIZATION.bat

> │    ├── 📄 RUN_OBSIDIAN_ATTACHMENT_MIRRORS.bat

> │    ├── 📄 _7.30_shell.md

> │    ├── 📄 _generate_file_registry.ps1

> │    ├── 📄 _move_duplicate_files.ps1

> │    ├── 📄 _move_issitax_files.ps1

> │    ├── 📄 activate

> │    ├── 📄 activate.bat

> │    ├── 📄 cleanup_analysis.ps1

> │    ├── 📄 comprehensive_cleanup.ps1

> │    ├── 📄 continue_cleanup.ps1

> │    ├── 📄 convert_to_csv.ps1

> │    ├── 📄 deploy-worker.ps1

> │    ├── 📄 deploy_all_workers.ps1

> │    ├── 📄 disable-lfs-hooks.ps1

> │    ├── 📄 enable-lfs-hooks.ps1

> │    ├── 📄 find_duplicates.ps1

> │    ├── 📄 finish_flattening.ps1

> │    ├── 📄 flatten_and_organize.ps1

> │    ├── 📄 flatten_inbox.ps1

> │    ├── 📄 get_worker_urls.ps1

> │    ├── 📄 housekeeping.ps1

> │    ├── 📄 install_scheduler.ps1

> │    ├── 📄 log_build_error.ps1

> │    ├── 📄 merge_media_tree.bat

> │    ├── 📄 move_large_files.ps1

> │    ├── 📄 newnode.bat

> │    ├── 📄 qios_dev_start.ps1

> │    ├── 📄 qios_start_all.ps1

> │    ├── 📄 qios_start_quick.ps1

> │    ├── 📄 run-qiindex.bat

> │    ├── 📄 run_3d_mindmap.bat

> │    ├── 📄 run_3d_real.bat

> │    ├── 📄 run_3d_simple.bat

> │    ├── 📄 run_housekeeper.bat

> │    ├── 📄 run_housekeeper_dry-run.bat

> │    ├── 📄 run_qios.ps1

> │    ├── 📄 scanner_scheduler.ps1

> │    ├── 📄 setup.ps1

> │    ├── 📄 start_gina_and_launcher.ps1

> │    ├── 📄 start_launcher.ps1

> │    ├── 📄 start_qios.ps1

> │    ├── 📄 start_qios_full.ps1

> │    ├── 📄 start_qios_local.ps1

> │    ├── 📄 test_pipeline.ps1

> │    ├── 📄 validate_cloud.ps1

> │    ├── 📄 validate_local.ps1

> │  ├── 📄 storage_bloat_destroyer.py

> │  └── 📂 sync/

> │    ├── 📄 index_content.ts

> │    ├── 📄 sync_dev_gdrive.py

> │  ├── 📄 sync_gdrive.ps1

> │  └── 📂 tools/

> │    ├── 📄 enforce_fm.py

> │    ├── 📄 fm_config.json

> │    ├── 📄 unblock_all.bat

> │  ├── 📄 tools_manifest.json

> │  ├── 📄 windows_task_scheduler.xml

> │  └── 📂 yaml/

> │    ├── 📄 csv_to_md_mappings.yaml

> │    ├── 📄 housekeeping.yaml

> │    ├── 📄 qi_codex.config.yaml

> │    ├── 📄 qi_prefix_map.yaml

> │    ├── 📄 qicompiler_config.yaml

> │    ├── 📄 qione_rag_routes.yaml

> │    ├── 📄 slugs_mapping.yaml

> │    ├── 📄 tree_compiler_config.yaml

> └── 📂 supabase/

> │  ├── 📄 config.toml

> │  └── 📂 functions/

> │    └── 📂 qivault-ingest/

> │      ├── 📄 index.ts

> │  └── 📂 migrations/

> │    ├── 📄 00001_core_saas_setup.sql

> │    ├── 📄 00002_vault_and_queues.sql

> │    ├── 📄 00003_app_schemas.sql

> │    ├── 📄 00004_content_index.sql

> │    ├── 📄 00005_cms_schema.sql

> │    ├── 📄 00006_qivault_docs.sql

> │    ├── 📄 00007_qione_platform.sql

> │    ├── 📄 00008_qihome_app.sql

> │    ├── 📄 00009_qichronicle.sql

> │    ├── 📄 00100_qichronicle_moments.sql

> │    ├── 📄 001_init_qione.sql

> │    ├── 📄 002_qihome_mvp.sql

> │    ├── 📄 003_qitax_returns.sql

> │    ├── 📄 003a_qitax_seed.sql

> │  └── 📂 snippets/

> ├── 📄 target_architecture.txt

> ├── 📄 turbo.json

> ├── 📄 vizvibe.mmd

> └── 📂 workers/

> │  ├── 📄 _readme.md

> │  └── 📂 _shared/

> │    ├── 📄 constitution.ts

> │    ├── 📄 heartbeat.ts

> │    ├── 📄 ignore.ts

> │  └── 📂 cloud/

> │    └── 📂 embedder/

> │      ├── 📄 EMBEDDER_IMPROVEMENTS.md

> │      ├── 📄 EMBEDDER_SIMPLIFICATION.md

> │      ├── 📄 package-lock.json

> │      ├── 📄 package.json

> │      ├── 📄 worker_embedder.ts

> │      ├── 📄 wrangler.toml

> │    └── 📂 ingestion/

> │      ├── 📄 package-lock.json

> │      ├── 📄 package.json

> │      ├── 📄 worker_ingestion.ts

> │      ├── 📄 wrangler.toml

> │    └── 📂 memory/

> │      ├── 📄 README_API.md

> │      ├── 📄 README_DEV.md

> │      ├── 📄 README_SECRETS.md

> │      ├── 📄 VERIFY_SETUP.md

> │      ├── 📄 package.json

> │      └── 📂 src/

> │      ├── 📄 sync-secrets.sh

> │      └── 📂 tests/

> │      ├── 📄 wrangler.toml

> │    └── 📂 metadata_naming/

> │      ├── 📄 package-lock.json

> │      ├── 📄 package.json

> │      ├── 📄 worker_metadata_naming.ts

> │      ├── 📄 wrangler.toml

> │    └── 📂 orchestrator/

> │      ├── 📄 OrchestratorState.ts

> │      └── 📂 migrations/

> │      ├── 📄 package-lock.json

> │      ├── 📄 package.json

> │      ├── 📄 qios_06_workers_orchestrator.canvas

> │      ├── 📄 worker_orchestrator.ts

> │      ├── 📄 wrangler.toml

> │    └── 📂 self_heal/

> │      ├── 📄 package-lock.json

> │      ├── 📄 package.json

> │      ├── 📄 worker_self_heal.ts

> │      ├── 📄 wrangler.toml

> │    └── 📂 semantic_router/

> │      ├── 📄 package-lock.json

> │      ├── 📄 package.json

> │      ├── 📄 worker_semantic_router.ts

> │      ├── 📄 wrangler.toml

> │  └── 📂 data/

> │    └── 📂 vector/

> │      ├── 📄 qios_local.db

> │  ├── 📄 dns_map.yml

> │  └── 📂 embedder/

> │    ├── 📄 EMBEDDER_IMPROVEMENTS.md

> │    ├── 📄 EMBEDDER_SIMPLIFICATION.md

> │    ├── 📄 package-lock.json

> │    ├── 📄 package.json

> │    ├── 📄 worker_embedder.ts

> │    ├── 📄 wrangler.toml

> │  └── 📂 ingestion-queue/

> │    ├── 📄 package-lock.json

> │    ├── 📄 package.json

> │    ├── 📄 worker_ingestion.ts

> │    ├── 📄 wrangler.toml

> │  └── 📂 local_core/

> │    ├── 📄 QUICK_START.md

> │    ├── 📄 README.md

> │    ├── 📄 README_WORKER.md

> │    ├── 📄 SETUP.md

> │    ├── 📄 TESTING_ROADMAP.md

> │    ├── 📄 api_dev_history.py

> │    ├── 📄 api_gina.py

> │    ├── 📄 api_ingest.py

> │    ├── 📄 api_query.py

> │    ├── 📄 check_status.py

> │    ├── 📄 check_workers.py

> │    └── 📂 crawler/

> │      ├── 📄 __init__.py

> │      ├── 📄 vault_crawler.py

> │    ├── 📄 db.py

> │    ├── 📄 dev_error_helpers.py

> │    ├── 📄 frontmatter_utils.py

> │    ├── 📄 fs_scan_config.yaml

> │    ├── 📄 fs_scanner.py

> │    ├── 📄 gina_chat_contract.md

> │    ├── 📄 gina_chat_contract.ts

> │    ├── 📄 gina_personality_prompt.md

> │    ├── 📄 gina_prompt.py

> │    └── 📂 integrations/

> │      ├── 📄 INTEGRATION_LAYER_SUMMARY.md

> │      ├── 📄 README.md

> │      ├── 📄 __init__.py

> │      ├── 📄 base.py

> │      └── 📂 calendar/

> │      └── 📂 email/

> │      └── 📂 tts/

> │      └── 📂 twilio/

> │      └── 📂 zoho/

> │    ├── 📄 job_processor.py

> │    ├── 📄 jobs.py

> │    ├── 📄 memory.py

> │    └── 📂 migrations/

> │      ├── 📄 001_init.sql

> │      ├── 📄 002_conversation_tables.sql

> │      ├── 📄 003_filesystem_index.sql

> │      ├── 📄 004_integration_tokens.sql

> │      ├── 📄 005_worker_status_unique.sql

> │      ├── 📄 006_add_worker_id.sql

> │      ├── 📄 007_file_registry.sql

> │      ├── 📄 008_jobs.sql

> │      ├── 📄 009_notes.sql

> │    ├── 📄 models.py

> │    ├── 📄 qios_local_core.py

> │    ├── 📄 quick_start.ps1

> │    ├── 📄 rag.py

> │    ├── 📄 requirements.txt

> │    └── 📂 scripts/

> │      ├── 📄 README.md

> │      ├── 📄 check-auth.ps1

> │      ├── 📄 check-secrets.ps1

> │      ├── 📄 deploy-all.ps1

> │      ├── 📄 deploy-critical.ps1

> │      ├── 📄 set-critical-secrets.ps1

> │      ├── 📄 set-secrets-from-env.ps1

> │      ├── 📄 sync-secrets.ps1

> │      ├── 📄 test-rag-system.ps1

> │      ├── 📄 test-with-curl.ps1

> │      ├── 📄 verify-and-test.ps1

> │    ├── 📄 start_worker.ps1

> │    ├── 📄 test_debug_ingest.ps1

> │    ├── 📄 test_ingest.py

> │    ├── 📄 test_queue_admin.ps1

> │    └── 📂 tests/

> │      ├── 📄 README.md

> │      ├── 📄 run_tests.sh

> │      ├── 📄 test_db_sanity.sql

> │      ├── 📄 test_manual_failures.md

> │      ├── 📄 test_sanity_checks.py

> │    ├── 📄 text_extractor.py

> │    └── 📂 tools/

> │    ├── 📄 tools.py

> │      ├── 📄 append_to_vault_note.py

> │      ├── 📄 calendar_create_event.py

> │      ├── 📄 calendar_get_upcoming.py

> │      ├── 📄 check_worker_status.py

> │      ├── 📄 create_vault_note.py

> │      ├── 📄 crm_create_contact.py

> │      ├── 📄 crm_create_task.py

> │      ├── 📄 crm_list_recent_contacts.py

> │      ├── 📄 crm_search_person.py

> │      ├── 📄 list_realm_files.py

> │      ├── 📄 mail_get_recent.py

> │      ├── 📄 mail_send.py

> │      ├── 📄 run_agent_command.py

> │      ├── 📄 search_processed_documents.py

> │      ├── 📄 sms_send.py

> │      ├── 📄 start_agent_service.py

> │      ├── 📄 start_worker.py

> │      ├── 📄 web_get.py

> │      ├── 📄 web_search.py

> │    ├── 📄 tools_manifest.yaml

> │    ├── 📄 worker.py

> │  └── 📂 metadata-naming/

> │    ├── 📄 package-lock.json

> │    ├── 📄 package.json

> │    ├── 📄 worker_metadata_naming.ts

> │    ├── 📄 wrangler.toml

> │  ├── 📄 package-lock.json

> │  ├── 📄 package.json

> │  └── 📂 semantic-router/

> │    ├── 📄 package-lock.json

> │    ├── 📄 package.json

> │    ├── 📄 worker_semantic_router.ts

> │    └── 📄 wrangler.toml

> ```

### Assistant
> Yeah — and looking at **your actual tree**, my answer changes a bit.
> 
> You do **not** have “a few apps.”  
> You have **4 real app roots, 2 half-apps, and a graveyard of nested pseudo-apps** living inside other apps.
> 
> So the fix is not just “keep fewer apps.”  
> The fix is: **stop calling storage, legacy, nested prototypes, and internal modules “apps.”**
> 
> ## What should stay in `/apps`
> These are the only ones that look like legitimate top-level app candidates:
> 
> ```txt
> apps/
>   qially-com/
>   qione-portal/
>   qivault-web/
>   api-core/   ← maybe, but only if it is truly a deployable runtime
> ```
> 
> That’s the clean version.
> 
> ## What should not be in `/apps`
> These are the ones polluting the layer:
> 
> - `gina-ai-chat/` → not a clean app, it’s a **mixed sandbox / nested repo / launcher bundle**
> - nested `apps/` inside `gina-ai-chat/` → absolutely not
> - `qially-com-v2.0/` inside `qially-com/` → versioned clone, not an app root
> - `sites_QiAlly.com_*` folders inside `qially-com/` → these are **site content / microsites / campaigns**, not monorepo apps
> - `_dirtfree_legacy/` inside `qione-portal/` → archive
> - `_qsaysit_legacy/` inside `qially-com/` → archive
> - random `index.html` placeholders everywhere → noise, not architecture
> 
> ## Brutal truth
> Your main problem is not “too many apps.”
> 
> Your problem is this:
> 
> ### 1. App boundaries are broken
> You’ve got:
> - app inside app
> - legacy inside app
> - prototype inside app
> - data inside app
> - docs inside app
> - workers duplicated inside app and root
> - Python runtime logic inside frontend-ish folders
> 
> That’s why it feels like chaos.
> 
> ### 2. `gina-ai-chat` is a mess
> That folder is doing too much:
> - launcher
> - nested apps
> - docs
> - rules
> - templates
> - workers
> - migrations
> - data
> - src
> - Python core
> - public UI
> 
> That is **not one app**. That is a junk drawer pretending to be a product.
> 
> ### 3. You have duplication all over
> Examples:
> - `workers/` exists at root **and** under `apps/api-core/`
> - `supabase migrations` exist under `packages/supabase` **and** root `supabase/`
> - `gina_core` appears multiple times
> - `qione-portal` has duplicated structures and bak files
> - `qially-com` has multiple generations of the same site in one app folder
> 
> That duplication is what’s draining your brain.
> 
> # What I would keep right now
> 
> ## Keep these app roots
> ```txt
> apps/
>   qially-com/
>   qione-portal/
>   qivault-web/
>   api-core/   # only if this is the actual backend app/API surface
> ```
> 
> ## Everything else: move, merge, or archive
> 
> ---
> 
> # What each app should mean
> 
> ## `apps/qially-com`
> This should be your **public business website** only.
> 
> Keep here:
> - main marketing site
> - service pages
> - portfolio
> - lead capture
> - public forms
> - public KB if you want it public
> 
> Move out:
> - old versions
> - campaign microsites unless intentionally deployed as routes of same site
> - random files/assets that are not directly used
> - duplicated v2 folders
> - legacy folders
> 
> ### inside `qially-com`, kill or move:
> - `_qsaysit_legacy/` → `archive/legacy/qially-com/qsaysit/`
> - `qially-com-v2.0/` → archive or merge
> - `sites_QiAlly.com_cashapp_bonus/` → either:
>   - route under main site, or
>   - move to `content/campaigns/`
> - `sites_QiAlly.com_flows/` → likely content/campaign or archive
> - `sites_QiAlly.com_helpcody/` → separate cause-site or archive
> - `sites_QiAlly.com_tax99/` → probably a campaign route, not separate app
> - excessive PDFs/xlsx/forms in app assets → move to `content/` or object storage manifest source
> 
> ---
> 
> ## `apps/qione-portal`
> This should be your **actual client/internal portal app**.
> 
> Keep here:
> - auth
> - dashboard
> - objects/forms/contracts
> - qichronicle pages if the portal is the shell
> - app API routes if this app owns them
> 
> Move/archive:
> - `_dirtfree_legacy/`
> - `.bak`, `.bak2`
> - duplicated older src structures once you choose the canonical one
> 
> ### Important:
> Right now `qione-portal` looks like **three eras smashed together**:
> 1. dirt-free legacy portal
> 2. newer src/app portal
> 3. object/form engine
> 
> Pick one canonical structure and archive the rest.
> 
> ---
> 
> ## `apps/qivault-web`
> This is clean enough conceptually.
> This should be your **document UI**.
> 
> Keep here:
> - inbox
> - search
> - tags
> - settings
> - document detail
> - storage client logic specific to the UI
> 
> This one is probably one of the least offensive folders in the whole tree.
> 
> ---
> 
> ## `apps/api-core`
> Only keep this if it is truly one thing:
> - FastAPI service
> - backend orchestration API
> - Gina API surface
> - ingestion control plane
> 
> But right now? It looks bloated and confused.
> 
> It contains:
> - frontend src
> - docs
> - rules
> - templates
> - tests
> - tools
> - workers
> - data
> - Python core
> - launcher junk
> - nested apps
> 
> That means **`api-core` is not an app yet.**  
> It is currently a **staging area for your whole nervous system**.
> 
> So here’s the real answer:
> 
> ### Option A — keep `api-core`, but gut it
> If you want one backend app, then `apps/api-core/` should end up like this:
> 
> ```txt
> apps/api-core/
>   src/
>   package.json or pyproject.toml
>   README.md
>   env.example
>   tests/
> ```
> 
> Maybe plus:
> ```txt
>   app/
>   routes/
>   services/
> ```
> 
> That’s it.
> 
> Everything else gets moved out.
> 
> ### Option B — delete `api-core` as an app root
> If the actual backend logic belongs in workers + python_core + packages, then stop pretending `api-core` is its own app and move the runtime elsewhere.
> 
> Honestly? Based on your tree, **this might be the smarter move** unless you truly need one consolidated backend service.
> 
> # My revised recommendation
> 
> ## Final `/apps` target
> This is the lean version I’d push you toward:
> 
> ```txt
> apps/
>   qially-com/      # public site
>   qione-portal/    # portal shell + authenticated app
>   qivault-web/     # document UI
>   api-core/        # only if real and cleaned
> ```
> 
> ## If you want maximum focus right now
> Even tighter:
> 
> ```txt
> apps/
>   qially-com/
>   qione-portal/
>   qivault-web/
> ```
> 
> And then:
> - `api-core` becomes `packages/api` or `python_core/api`
> - root `workers/` remains infra/runtime
> - root `supabase/` remains DB infra
> - `content/` becomes content
> - `archive/` gets all old crap
> 
> # What to move out of apps entirely
> 
> ## Move to `/archive`
> ```txt
> archive/
>   legacy/
>     qially-com/
>     qione-portal/
>     gina-ai-chat/
> ```
> 
> Put in there:
> - `_dirtfree_legacy`
> - `_qsaysit_legacy`
> - `qially-com-v2.0`
> - nested launcher experiments
> - bak files if you truly need them
> 
> ## Move to `/packages`
> Anything reusable:
> - shared auth
> - shared schemas
> - email templates/renderers
> - UI library
> - config
> - db types
> - sdk
> - utils
> 
> You already started this. Good. Keep going.
> 
> ## Move to `/workers`
> All workers live in one place only.
> Not in apps.
> Not duplicated.
> 
> Pick **root `/workers`** as canonical and kill the copies under `api-core`.
> 
> ## Move to `/supabase`
> One canonical migrations location.
> Not two.
> 
> Right now you’ve got migration logic in:
> - `packages/supabase`
> - root `supabase`
> - parts of apps
> 
> That’s sloppy. Pick one:
> - I’d make **root `/supabase`** canonical
> - `packages/supabase` can expose typed helpers, not duplicate migration truth
> 
> ## Move to `/content`
> Stuff like:
> - PDFs
> - public resources
> - campaign assets
> - intake templates
> - KB source docs
> - marketing content
> - docs meant to render into sites
> 
> ## Move to `/python_core`
> Python services that are not frontend apps:
> - gina-ai
> - document processors
> - local agent runtimes
> 
> # The one folder I would kill first
> ## `apps/gina-ai-chat/`
> Not because Gina is bad.  
> Because that folder is lying about what it is.
> 
> It is not a single app. It is:
> - prototype UI
> - launcher
> - nested apps
> - runtime fragments
> - docs
> - migrations
> - workers
> - data
> - templates
> 
> That folder needs to be **exploded and sorted**, not preserved as an app.
> 
> # So, after seeing your real tree, here’s the corrected answer:
> 
> ## Keep in `/apps`
> ```txt
> apps/
>   qially-com
>   qione-portal
>   qivault-web
>   api-core   # only after cleanup, otherwise demote/remove
> ```
> 
> ## Remove from `/apps`
> ```txt
> gina-ai-chat
> nested apps inside gina-ai-chat
> legacy clones
> version clones
> campaign microsites pretending to be apps
> ```
> 
> # My blunt recommendation
> If you want your repo to stop frying your brain, do this:
> 
> ### Phase 1
> Keep only:
> 
> ```txt
> apps/
>   qially-com
>   qione-portal
>   qivault-web
> ```
> 
> ### Phase 2
> Create:
> ```txt
> archive/
>   legacy/
> ```
> 
> ### Phase 3
> Move `gina-ai-chat` out of `apps` completely and split it into:
> - `python_core/gina-ai/`
> - `workers/...`
> - `packages/...`
> - maybe `apps/gina-console/` later if there is a real UI
> 
> That’s the real cleanup.
> 
> ## Bottom line
> Your repo does **not** need more app thinking.  
> It needs **app boundary enforcement**.
> 
> Right now your real app count should be **3, maybe 4**.
> 
> Not 9.  
> Not nested.  
> Not “v2 inside app inside launcher inside Gina.”
> 
> That part is nonsense.
> 
> Paste me just the **`apps/` folder names plus one sentence of what each is supposed to do**, and I’ll give you the exact **keep / merge / archive map** with no fluff.

### User
> no, i mean looking at my tree and what you know about my goals, what should the final apps actually be, we essentially have aihub (rag, vectors, recal, agents, skills, etc), we have content and storage, we have ingestion and processings, then we hae sties like marketing and other web sites or pwa apps for actually doing stuff, what else, workers, apis, and content creation like journals and stories or note taking.

### Assistant
> Yes. Now we’re talking about the **actual platform map**, not just folder janitoring.
> 
> Looking at your tree and your goals, your final apps should map to **runtime surfaces**, not concepts, not pipelines, not storage layers, and not internal mechanics.
> 
> ## First: what is *not* an app
> 
> These are platform layers, not apps:
> 
> - **RAG / vectors / recall / skills / agents** → platform services
> - **content / storage** → infrastructure + data layer
> - **ingestion / processing** → pipeline/runtime workers
> - **workers** → compute/runtime
> - **APIs** → service interfaces
> - **schemas / migrations / rules / registries** → platform foundation
> 
> If you put all of that in `/apps`, you’ll recreate the same mess.
> 
> ## The right way to think about it
> 
> Your monorepo should end up with roughly this split:
> 
> ### 1. Experience layer = `/apps`
> Things humans open and use
> 
> ### 2. Platform layer = `/packages`, `/workers`, `/supabase`, `/python_core`
> Things that power the experiences
> 
> ### 3. Content layer = `/content`
> Things you write, publish, transform, ingest, or render
> 
> ---
> 
> # The final app families you actually need
> 
> Based on your goals, I’d define **6 real app surfaces** max.
> 
> ## 1) `hub`
> The internal brain dashboard.
> 
> This is your **AIHub / QiHub / Gina control surface**.
> 
> Purpose:
> - search across your knowledge
> - query memory / recall
> - run agents/tools/skills
> - inspect queues/jobs
> - trigger workflows
> - view embeddings / ingestion status / source health
> - operate the system without living in raw infra
> 
> This is the **operator UI** for the intelligence layer.
> 
> ### This is an app
> Because a human opens it and does work there.
> 
> ---
> 
> ## 2) `portal`
> The structured work app.
> 
> This is your **QiOne / QiPortals / client-and-case operating surface**.
> 
> Purpose:
> - client portals
> - forms
> - contracts
> - object records
> - timelines
> - care workflows
> - tax workflows
> - case workflows
> - household/work operational dashboards
> 
> This is where “doing stuff” happens in a structured way.
> 
> ### This is an app
> Because it’s a real interaction surface for repeatable workflows.
> 
> ---
> 
> ## 3) `vault`
> The document and file app.
> 
> This is your **QiVault / QiArchive / document system UI**.
> 
> Purpose:
> - inbox
> - document review
> - metadata editing
> - OCR results review
> - content browsing
> - tags
> - search
> - file lifecycle state
> - canonical document view
> 
> This should be the **human-facing shell** for storage/content retrieval.
> 
> ### This is an app
> Because documents are a user-facing product surface for you.
> 
> ---
> 
> ## 4) `sites`
> Public-facing web presence.
> 
> This is your **marketing / landing / public microsite layer**.
> 
> Depending on how you want to organize, this is either:
> - one multi-route app, or
> - a small set of site apps
> 
> Purpose:
> - qially.com
> - public landing pages
> - public resources
> - offers
> - showcases
> - cause/support pages
> - lead magnets
> - simple public PWAs if they are public-facing
> 
> ### This is an app family
> But ideally **not 17 app roots**.
> 
> You probably want either:
> 
> ### Option A — one app
> ```txt
> apps/sites
> ```
> 
> with domains/routes for:
> - main marketing
> - tax99
> - helpcody
> - flows
> - public knowledge pages
> 
> ### Option B — two apps max
> ```txt
> apps/marketing
> apps/public-tools
> ```
> 
> I would not keep every microsite as its own monorepo app unless it truly deploys separately and earns that complexity.
> 
> ---
> 
> ## 5) `studio`
> Content creation and publishing workspace.
> 
> This is the part you were circling when you said:
> - journals
> - stories
> - note taking
> - content creation
> 
> Now, important truth: this might end up as an app **or** just content + editor integration.
> 
> But if you want an actual writing surface inside your ecosystem, this is the clean app for it.
> 
> Purpose:
> - journal entry capture
> - story drafting
> - structured note creation
> - content staging
> - publishing prep
> - voice-to-note / reflection capture
> - QiNote-style writing workspace
> 
> This is your **authoring layer**.
> 
> ### This is only an app if:
> you want a dedicated UI to write/manage content inside your platform.
> 
> If not, keep it as:
> - `/content`
> - plus ingestion/editor tooling
> 
> But given your goals, I actually think you **do** eventually want this.
> 
> ---
> 
> ## 6) `api`
> A single unified service surface, if needed.
> 
> This is **not every background process**.  
> This is only the app/service if you need a central API gateway or backend runtime.
> 
> Purpose:
> - authenticated app endpoints
> - orchestration endpoints
> - retrieval endpoints
> - webhook receiver surface
> - service composition layer
> 
> ### This is optional as an app root
> If your portal/site/vault apps can own their own route handlers and workers do the rest, then you may not need this as a separate app.
> 
> But if you want:
> - one stable internal API
> - one service gateway
> - one control plane backend
> 
> then yes, keep `api`.
> 
> ---
> 
> # So the final app map is:
> 
> ## Core recommendation
> ```txt
> apps/
>   hub/        # AIHub operator console
>   portal/     # structured workflows / client operations
>   vault/      # documents, storage, archive UI
>   sites/      # public sites and marketing surfaces
>   studio/     # journaling, stories, notes, publishing
>   api/        # optional unified backend service
> ```
> 
> That is the clean future-state map.
> 
> ---
> 
> # What each of your current concepts maps to
> 
> ## “AI hub (RAG, vectors, recall, agents, skills, etc)”
> **App:** `hub`  
> **Backend support:** `workers/`, `python_core/`, `packages/ai`, `supabase/`
> 
> ---
> 
> ## “content and storage”
> **App:** `vault` for human interaction  
> **Backend support:** `content/`, storage buckets, database, file registries
> 
> ---
> 
> ## “ingestion and processing”
> **Not an app**  
> This belongs in:
> ```txt
> workers/
> python_core/
> packages/ingestion/
> ```
> 
> ---
> 
> ## “sites like marketing and other websites or PWA apps for actually doing stuff”
> Split this cleanly:
> 
> - public/external → `sites`
> - authenticated/business/process work → `portal`
> - document work → `vault`
> - intelligence operations → `hub`
> 
> Don’t blur them again.
> 
> ---
> 
> ## “workers”
> **Not an app**  
> Root runtime layer.
> 
> ---
> 
> ## “apis”
> Usually **not** separate apps unless there is a real gateway/service.  
> If needed: `apps/api`
> 
> ---
> 
> ## “content creation like journals and stories or note taking”
> Potentially:
> - `apps/studio` if there is a real writing UI
> - `/content` if it’s file-first
> 
> Given you want modular systems and future publishing, I’d reserve `studio`.
> 
> ---
> 
> # The real architecture underneath
> 
> Your repo should look more like this:
> 
> ```txt
> apps/
>   hub/
>   portal/
>   vault/
>   sites/
>   studio/
>   api/          # optional
> 
> packages/
>   ai/
>   auth/
>   ui/
>   database/
>   schemas/
>   sdk/
>   config/
>   email/
>   utils/
> 
> workers/
>   cloud/
>   local_core/
>   ingestion/
>   embedder/
>   routing/
>   naming/
>   orchestration/
> 
> python_core/
>   agents/
>   document-processors/
>   local-ai/
> 
> content/
>   journals/
>   stories/
>   notes/
>   campaigns/
>   kb/
>   templates/
>   prompts/
> 
> supabase/
>   migrations/
>   functions/
> ```
> 
> That shape matches your actual intent.
> 
> ---
> 
> # What you are missing conceptually
> 
> You asked “what else?”
> 
> Here’s what else matters:
> 
> ## A) `hub` and `portal` are not the same thing
> This distinction matters a lot.
> 
> - **hub** = operator intelligence console
> - **portal** = structured workflow/product app
> 
> If you combine those, you’ll get a bloated admin monster.
> 
> ---
> 
> ## B) `vault` and `studio` are not the same thing
> Also important.
> 
> - **vault** = managed documents/content assets already in system
> - **studio** = creating and shaping new content
> 
> If you combine those, note-taking gets buried under archive logic.
> 
> ---
> 
> ## C) `sites` is a publishing surface, not your operating system
> Your marketing/public sites should not carry the whole universe of your internal logic.
> 
> Keep them thin.
> 
> ---
> 
> ## D) ingestion, workers, memory, vectors, processing are infrastructure
> They should be treated like **engines**, not places you work directly.
> 
> That’s what fried the current tree.
> 
> ---
> 
> # My blunt recommendation for *right now*
> 
> You do **not** need to build all 6 immediately.
> 
> You need to name them now so the repo stops shapeshifting.
> 
> ## Build in this order
> 
> ### Phase 1
> ```txt
> apps/
>   portal/
>   vault/
>   sites/
> ```
> 
> Because those are the clearest human-facing surfaces.
> 
> ### Phase 2
> ```txt
> apps/
>   hub/
> ```
> 
> Once your backend intelligence layer is stable enough to deserve a console.
> 
> ### Phase 3
> ```txt
> apps/
>   studio/
> ```
> 
> Once content authoring needs a dedicated home.
> 
> ### Optional
> ```txt
> apps/
>   api/
> ```
> 
> Only if route ownership gets messy.
> 
> ---
> 
> # My final answer
> 
> ## Final app set
> ```txt
> apps/
>   hub
>   portal
>   vault
>   sites
>   studio
>   api   # optional
> ```
> 
> ## Not apps
> ```txt
> workers
> ingestion
> processing
> vectors
> rag
> memory
> skills
> agents
> storage
> content registries
> schemas
> migrations
> rules
> ```
> 
> Those are platform layers.
> 
> ---
> 
> # Translation into your world
> 
> If I rename them in your language:
> 
> ```txt
> hub     = AIHub / Gina / operator console
> portal  = QiOne / QiPortals / structured workflow surface
> vault   = QiVault / QiArchive / document and storage interface
> sites   = QiAlly public web surfaces / marketing / landing / public tools
> studio  = QiNote / QiChronicle authoring / journals / stories / reflections
> api     = unified backend gateway if needed
> ```
> 
> That’s the map.
> 
> The cleanest version, honestly, is probably:
> 
> ```txt
> apps/
>   qihub
>   qione
>   qivault
>   qially-web
>   qistudio
> ```
> 
> with `api` only if it proves necessary.
> 
> If you want, next I’ll turn this into a **keep / merge / rename map** from your current app names to final target names.

### User
> but wait, isnt most of this just modules in the portal, ? qione

### Assistant
> Yes — **a lot of it can be modules inside `qione`**.
> 
> That’s the key distinction:
> 
> ## `qione` = the operating shell
> If your goal is one authenticated app where **you and maybe clients** do actual work, then `qione` can absolutely contain modules like:
> 
> - AI hub
> - chronicle
> - forms
> - contracts
> - cases
> - tax workflows
> - care workflows
> - notes
> - journals
> - object records
> - dashboards
> 
> So the question is not “is it a module?”  
> The question is:
> 
> ## Does this need to be its **own app surface** or just a **module inside qione**?
> 
> ### Keep it inside `qione` if:
> - it shares auth
> - it shares navigation
> - it shares database context
> - it’s part of the same daily workflow
> - it doesn’t need separate deployment/runtime/security boundaries
> - it’s mainly for you/internal users/clients already in the same system
> 
> That means, yes, these can likely be **modules in qione**:
> - `qichronicle`
> - `qinote` / journals / stories / reflections
> - forms engine
> - contracts
> - object management
> - client operations
> - case ops
> - tax ops
> - maybe even a lightweight AI assistant panel
> 
> ## Make it a separate app only if:
> - it has a very different audience
> - it needs separate deployment
> - it has distinct runtime needs
> - it’s public-facing
> - it’s document-first enough to deserve its own UX
> - it’s heavy enough that forcing it into qione makes qione bloated and confused
> 
> ---
> 
> # So the cleaner final answer is probably this:
> 
> ## Core apps
> ```txt
> apps/
>   qione
>   qivault
>   qially-web
> ```
> 
> ## Optional later
> ```txt
>   qihub   # only if the AI/operator layer outgrows qione
>   api     # only if you truly need a unified service app
> ```
> 
> That’s probably your real end state.
> 
> ---
> 
> # What belongs where
> 
> ## `qione`
> Your main authenticated operating system.
> 
> Modules inside it:
> - dashboard
> - objects
> - forms
> - contracts
> - qichronicle
> - qinote
> - journals
> - stories
> - case management
> - tax workflows
> - care workflows
> - reminders/tasks
> - lightweight AI workspace
> 
> This is the **do-stuff app**.
> 
> ---
> 
> ## `qivault`
> Separate because document management is its own beast.
> 
> Why separate:
> - storage-heavy
> - search-heavy
> - file lifecycle UX is different
> - ingestion/review/archive flows are different
> - can later integrate with Paperless / Drive / OCR / metadata pipelines cleanly
> 
> This one earns separation.
> 
> ---
> 
> ## `qially-web`
> Public site / marketing / public tools / landing pages.
> 
> Definitely separate from `qione`.
> 
> ---
> 
> # What about AIHub?
> This is the part to be careful with.
> 
> ### Early stage:
> AIHub can just be a **module inside `qione`**.
> 
> Example:
> ```txt
> qione/
>   /ai
>   /search
>   /memory
>   /agents
>   /skills
> ```
> 
> That’s fine.
> 
> ### Later:
> If it becomes a true operator console with:
> - queue inspection
> - worker health
> - embeddings status
> - ingestion jobs
> - source sync health
> - prompt testing
> - tool registry
> - model routing
> - admin diagnostics
> 
> Then it deserves its own app:
> ```txt
> apps/qihub
> ```
> 
> But not yet unless you’re really using it that way.
> 
> ---
> 
> # What about note-taking / journals / stories?
> Same answer.
> 
> At first:
> - module inside `qione`
> 
> Later, if you build a real authoring/publishing environment:
> - separate `qistudio`
> 
> Right now, separate app is probably premature.
> 
> ---
> 
> # So the practical architecture is:
> 
> ```txt
> apps/
>   qione
>   qivault
>   qially-web
> ```
> 
> ### Inside `qione` as modules:
> ```txt
> modules/
>   dashboard
>   ai
>   qichronicle
>   qinote
>   forms
>   objects
>   contracts
>   cases
>   tax
>   care
>   tasks
> ```
> 
> ### Separate platform layers:
> ```txt
> workers/
> packages/
> python_core/
> supabase/
> content/
> ```
> 
> ---
> 
> # Blunt answer
> You were right to question it.
> 
> Most of the things you listed are **not separate apps yet**.  
> They’re **capabilities**.
> 
> And capabilities usually belong as **modules in `qione`** until they prove they need their own boundary.
> 
> ## So final recommendation:
> ### Keep these as true apps:
> - `qione`
> - `qivault`
> - `qially-web`
> 
> ### Maybe later:
> - `qihub`
> - `api`
> 
> That’s the tighter, saner map.
> 
> If you want, I’ll turn that into a **final target `/apps` tree** plus which of your current folders merge into each one.

### User
> i want to login to qione and from there do anything else from one app. period, permission will define what others see who login.

### Assistant
> Then yes — **stop splitting the experience layer**.
> 
> Your north star is:
> 
> ## One app: `qione`
> Everything user-facing lives behind that login. Permissions decide what each person sees.
> 
> That means your final app strategy becomes much simpler.
> 
> # Final answer
> 
> ## True app surface
> ```txt
> apps/
>   qione
> ```
> 
> That is the **only primary application**.
> 
> Everything else is either:
> - a module inside `qione`
> - a service powering `qione`
> - a public site outside the authenticated system
> 
> ---
> 
> # What lives inside `qione`
> 
> ## Modules inside the one app
> These are not separate apps anymore:
> 
> - dashboard
> - AI hub
> - qichronicle
> - qinote
> - journals
> - stories
> - forms
> - contracts
> - objects
> - clients
> - cases
> - tax workflows
> - care workflows
> - tasks
> - reminders
> - document search
> - document viewer
> - uploads
> - reports
> - settings
> - admin
> - permissions
> - notifications
> 
> So yes: **Vault, Chronicle, Note, AI workspace, portals, workflows — all of that can be modules in `qione`.**
> 
> ---
> 
> # What still stays separate from `qione`
> 
> ## 1) Public site
> ```txt
> apps/
>   qially-web
> ```
> 
> This is marketing, public landing pages, public intake, showcases, SEO pages, maybe public tools.
> 
> Why separate?
> Because public web and authenticated operating system are different jobs.
> 
> ---
> 
> ## 2) Optional dedicated API app
> Only if needed.
> 
> ```txt
> apps/
>   api
> ```
> 
> But do **not** create this unless you actually need a standalone gateway/control plane.  
> A lot of this can live as route handlers, server actions, workers, or services behind `qione`.
> 
> So for now:
> 
> ```txt
> apps/
>   qione
>   qially-web
> ```
> 
> That’s probably your real answer.
> 
> ---
> 
> # What this means structurally
> 
> ## `qione` is your shell
> Think:
> 
> ```txt
> qione
> ├─ dashboard
> ├─ workspace
> ├─ documents
> ├─ ai
> ├─ chronicle
> ├─ notes
> ├─ objects
> ├─ forms
> ├─ clients
> ├─ cases
> ├─ tax
> ├─ care
> ├─ settings
> └─ admin
> ```
> 
> Permission-based access controls determine:
> - which nav items appear
> - which records can be accessed
> - which modules are enabled
> - which actions are allowed
> 
> Exactly what you said.
> 
> ---
> 
> # So what is `qivault` now?
> Not a separate app.
> 
> It becomes one or both of these:
> 
> ## Option A: a module in `qione`
> ```txt
> qione/modules/documents
> ```
> 
> ## Option B: a product/domain name
> You can still call the document module **QiVault** or **QiArchive** publicly/internal branding-wise.
> 
> But architecturally, it is part of `qione`.
> 
> Same for:
> - QiChronicle
> - QiNote
> - AIHub
> - QiCare
> - QiTax
> 
> These are **modules/products**, not separate app roots.
> 
> That’s cleaner.
> 
> ---
> 
> # What is not an app now
> 
> These are all backend/platform layers:
> 
> - RAG
> - vectors
> - recall
> - memory
> - agents
> - skills
> - ingestion
> - OCR
> - processing
> - workers
> - storage
> - sync
> - queueing
> - orchestration
> - database schemas
> - migrations
> - registries
> - rules
> 
> They support `qione`.  
> They are not things users log into directly.
> 
> ---
> 
> # Your final monorepo shape should probably be this
> 
> ```txt
> apps/
>   qione/
>   qially-web/
> 
> packages/
>   ai/
>   auth/
>   ui/
>   database/
>   schemas/
>   email/
>   config/
>   sdk/
>   utils/
> 
> workers/
>   cloud/
>   local_core/
>   ingestion/
>   embedder/
>   metadata_naming/
>   semantic_router/
>   orchestrator/
>   self_heal/
> 
> python_core/
>   agents/
>   document-processors/
>   local_services/
> 
> content/
>   journals/
>   stories/
>   notes/
>   prompts/
>   templates/
>   kb/
>   campaigns/
> 
> supabase/
>   migrations/
>   functions/
> 
> scripts/
> archive/
> ```
> 
> That’s it. Much tighter.
> 
> ---
> 
> # The internal module map for `qione`
> 
> Here’s the part that matters.
> 
> ## Recommended module groups
> 
> ### 1. Core workspace
> - dashboard
> - inbox
> - search
> - notifications
> - tasks
> - settings
> 
> ### 2. Records + workflows
> - contacts
> - clients
> - cases
> - tax
> - care
> - forms
> - contracts
> - appointments
> - timelines
> 
> ### 3. Knowledge + content
> - documents
> - qichronicle
> - notes
> - journals
> - stories
> - media/assets
> 
> ### 4. Intelligence
> - ai chat
> - memory search
> - agent runner
> - prompt tools
> - automations
> - source connectors
> 
> ### 5. Admin
> - users
> - roles
> - permissions
> - audit
> - queues
> - worker health
> - source sync
> - ingestion status
> 
> That gives you one shell, many capabilities.
> 
> ---
> 
> # The naming truth
> 
> You’ve been thinking in product names, which is fine, but for architecture:
> 
> - **QiOne** = the app shell
> - **QiVault** = documents module
> - **QiChronicle** = timeline module
> - **QiNote** = writing/notes module
> - **AIHub / Gina** = intelligence module
> - **QiTax / QiCare / QiHome** = domain modules
> 
> That is the right hierarchy.
> 
> ## So:
> **QiOne is the house.**
> Everything else is a room unless it absolutely must be a separate building.
> 
> That’s the cleanest version of your vision.
> 
> ---
> 
> # My blunt recommendation
> Do **not** keep separate app roots for:
> - qivault-web
> - qichronicle
> - qinote
> - gina-ai-chat
> 
> Fold them into `qione` unless there is a hard technical reason not to.
> 
> Keep only:
> 
> ```txt
> apps/
>   qione
>   qially-web
> ```
> 
> Maybe later:
> ```txt
>   api
> ```
> 
> But only if forced.
> 
> ---
> 
> # Decision
> If your stated goal is one login, one place, one permission model, one operating surface, then the repo should reflect that.
> 
> Not five sibling apps pretending to be one system.
> 
> It should be one system.
> 
> ## Final target
> ```txt
> apps/
>   qione
>   qially-web
> ```
> 
> And inside `qione`, everything else becomes modules.
> 
> Next move should be to define the **top-level module namespaces inside `qione`** before you touch folders again.

### User
> yes, that is the goal, so what is the folder structure under qioneportal and also so do i even need to worry about turb repos and shared blah blah if its one app?

### Assistant
> Yes — if `qione` is the one real app, then **do not over-engineer this**.
> 
> You probably **do not need a fancy Turborepo strategy right now** just because the repo happens to be called a monorepo.
> 
> If there is **one main app**, then optimize for:
> - clean boundaries
> - predictable folders
> - easy imports
> - future extraction if needed
> 
> Not for theoretical scale.
> 
> ## Blunt answer
> 
> ### Do you need Turborepo?
> **Not urgently.**
> If it’s already there and not causing pain, fine, keep it.
> If it’s adding mental overhead, **ignore most of it for now**.
> 
> ### Do you need shared packages?
> **Only a few.**
> Not because “best practice.”
> Because some things genuinely should not live inside the app.
> 
> For one app, the clean model is:
> 
> ```txt
> apps/
>   qione/
>   qially-web/   # optional public site
> 
> packages/
>   ui/           # only if shared with qially-web
>   database/     # types/helpers if reused
>   config/       # only if actually shared
> ```
> 
> That’s it.  
> You do **not** need 11 abstraction packages just to feel architect-y.
> 
> ---
> 
> # What `apps/qione/` should look like
> 
> This is the structure I’d recommend for your actual goal:
> 
> ```txt
> apps/
>   qione/
>     package.json
>     tsconfig.json
>     next.config.mjs
>     middleware.ts
>     .env.example
>     README.md
> 
>     public/
>       favicon.ico
>       icons/
>       images/
> 
>     src/
>       app/
>         (public)/
>           login/
>             page.tsx
>           invite/
>             page.tsx
>           reset-password/
>             page.tsx
> 
>         (app)/
>           layout.tsx
>           page.tsx                    # dashboard / home
> 
>           ai/
>             page.tsx
>             agents/
>               page.tsx
>             memory/
>               page.tsx
>             prompts/
>               page.tsx
>             automations/
>               page.tsx
> 
>           chronicle/
>             page.tsx
>             [id]/
>               page.tsx
> 
>           notes/
>             page.tsx
>             [id]/
>               page.tsx
>             new/
>               page.tsx
> 
>           documents/
>             page.tsx
>             inbox/
>               page.tsx
>             [id]/
>               page.tsx
>             tags/
>               page.tsx
>             search/
>               page.tsx
> 
>           objects/
>             page.tsx
>             contacts/
>               page.tsx
>               [id]/
>                 page.tsx
>             clients/
>               page.tsx
>               [id]/
>                 page.tsx
>             cases/
>               page.tsx
>               [id]/
>                 page.tsx
>             expenses/
>               page.tsx
>             tasks/
>               page.tsx
>             appointments/
>               page.tsx
> 
>           forms/
>             page.tsx
>             [formKey]/
>               page.tsx
> 
>           contracts/
>             page.tsx
>             [id]/
>               page.tsx
> 
>           tax/
>             page.tsx
>             returns/
>               page.tsx
>             clients/
>               page.tsx
>             organizers/
>               page.tsx
> 
>           care/
>             page.tsx
>             patients/
>               page.tsx
>             meds/
>               page.tsx
>             supplies/
>               page.tsx
> 
>           settings/
>             page.tsx
>             profile/
>               page.tsx
>             notifications/
>               page.tsx
>             connections/
>               page.tsx
> 
>           admin/
>             page.tsx
>             users/
>               page.tsx
>             roles/
>               page.tsx
>             permissions/
>               page.tsx
>             audit/
>               page.tsx
>             system/
>               page.tsx
>             workers/
>               page.tsx
> 
>         api/
>           ai/
>             chat/
>               route.ts
>             memory/
>               route.ts
>           chronicle/
>             route.ts
>             [id]/
>               route.ts
>           documents/
>             upload/
>               route.ts
>             search/
>               route.ts
>           forms/
>             [formKey]/
>               route.ts
>           objects/
>             [objectType]/
>               route.ts
>             [objectType]/
>               [id]/
>                 route.ts
>           admin/
>             worker-health/
>               route.ts
>             queue-status/
>               route.ts
>           webhooks/
>             stripe/
>               route.ts
> 
>       components/
>         layout/
>           AppShell.tsx
>           Sidebar.tsx
>           Topbar.tsx
>           Breadcrumbs.tsx
> 
>         ai/
>         chronicle/
>         notes/
>         documents/
>         objects/
>         forms/
>         contracts/
>         tax/
>         care/
>         admin/
> 
>         ui/
>           button.tsx
>           card.tsx
>           dialog.tsx
>           input.tsx
>           table.tsx
>           tabs.tsx
>           textarea.tsx
> 
>       features/
>         ai/
>           server/
>           client/
>           schemas/
>           utils.ts
> 
>         chronicle/
>           server/
>           client/
>           schemas/
>           utils.ts
> 
>         notes/
>           server/
>           client/
>           schemas/
>           utils.ts
> 
>         documents/
>           server/
>           client/
>           schemas/
>           utils.ts
> 
>         objects/
>           server/
>           client/
>           schemas/
>           registry.ts
>           utils.ts
> 
>         forms/
>           server/
>           client/
>           schemas/
>           registry.ts
>           utils.ts
> 
>         contracts/
>           server/
>           client/
>           schemas/
>           utils.ts
> 
>         tax/
>           server/
>           client/
>           schemas/
>           utils.ts
> 
>         care/
>           server/
>           client/
>           schemas/
>           utils.ts
> 
>         admin/
>           server/
>           client/
>           schemas/
>           utils.ts
> 
>       lib/
>         auth/
>           guards.ts
>           permissions.ts
>           session.ts
> 
>         db/
>           client.ts
>           server.ts
>           queries.ts
> 
>         storage/
>           uploads.ts
>           files.ts
> 
>         ai/
>           embeddings.ts
>           recall.ts
>           tools.ts
> 
>         integrations/
>           email.ts
>           calendar.ts
>           crm.ts
> 
>         utils/
>           dates.ts
>           money.ts
>           strings.ts
>           ids.ts
> 
>         env.ts
>         constants.ts
> 
>       types/
>         auth.ts
>         database.ts
>         permissions.ts
>         common.ts
> 
>       styles/
>         globals.css
> 
>     supabase/
>       migrations/
>       seed/
>       policies.sql
> 
>     content/
>       forms/
>       prompts/
>       templates/
>       kb/
> ```
> 
> ---
> 
> # Why this structure works
> 
> Because it reflects the reality:
> 
> ## `app/`
> Routes and pages only.
> 
> ## `components/`
> Reusable UI pieces.
> 
> ## `features/`
> This is the important part.  
> Each domain gets its own little island.
> 
> That stops the app from turning into soup.
> 
> Example:
> - `features/documents`
> - `features/chronicle`
> - `features/ai`
> - `features/forms`
> 
> Each feature can hold:
> - server logic
> - client hooks
> - validators/schemas
> - helper functions
> 
> That gives you module boundaries **without** pretending each module is its own app.
> 
> ## `lib/`
> True cross-cutting services only:
> - auth
> - db
> - storage
> - integrations
> - shared utilities
> 
> Not random dumping ground trash.
> 
> ---
> 
> # The top-level module names I’d use inside `qione`
> 
> These are the ones that actually match your world:
> 
> ```txt
> ai
> chronicle
> notes
> documents
> objects
> forms
> contracts
> tax
> care
> admin
> settings
> ```
> 
> If you want, `objects` can contain:
> - contacts
> - clients
> - cases
> - tasks
> - expenses
> - appointments
> - assets
> 
> That keeps the nav sane.
> 
> ---
> 
> # What I would NOT do
> 
> ## Don’t do this
> ```txt
> src/
>   components/
>   utils/
>   hooks/
>   services/
>   pages/
>   randomstuff/
>   new/
>   old/
>   beta/
> ```
> 
> That becomes unsearchable garbage fast.
> 
> ## Don’t split into 30 packages
> You do not need:
> - `@qione/forms`
> - `@qione/chronicle`
> - `@qione/notes`
> - `@qione/permissions`
> - `@qione/tax`
> - blah blah blah
> 
> Not yet. Maybe later if forced. Right now that’s just procrastination disguised as architecture.
> 
> ---
> 
> # Do you need Turborepo/shared packages if it’s one app?
> 
> ## Right now: mostly no
> You can absolutely run this as:
> 
> ```txt
> apps/
>   qione/
>   qially-web/
> ```
> 
> And be done.
> 
> ## Shared packages only make sense when:
> - both `qione` and `qially-web` use the same UI or config
> - both need shared DB types/helpers
> - you truly reuse code, not just think you might
> 
> So the sane version is:
> 
> ```txt
> packages/
>   ui         # only if both apps use same components
>   database   # shared types/helpers
>   config     # maybe
> ```
> 
> That’s enough.
> 
> ## Turborepo is useful mainly for:
> - consistent scripts across apps/packages
> - caching builds
> - managing multiple packages/apps cleanly
> 
> But it is **not required** to have good structure.
> 
> If it’s already in place, keep it light.
> If it’s confusing you, don’t build your life around it.
> 
> ---
> 
> # My actual recommendation for you
> 
> ## Keep:
> ```txt
> apps/
>   qione/
>   qially-web/
> ```
> 
> ## Keep a small packages layer:
> ```txt
> packages/
>   ui/         # optional
>   database/   # likely useful
>   config/     # optional
> ```
> 
> ## Everything else:
> ```txt
> workers/
> python_core/
> supabase/
> scripts/
> content/
> archive/
> ```
> 
> ---
> 
> # Even simpler version if you want zero fluff
> 
> If you want to move fast and stop spiraling, here is the stripped-down version:
> 
> ```txt
> apps/
>   qione/
>     src/
>       app/
>       components/
>       features/
>       lib/
>       types/
>       styles/
>     public/
>     supabase/
> 
>   qially-web/
> ```
> 
> That is enough.
> 
> ---
> 
> # My recommendation on naming under qione
> 
> I would use this nav/domain order:
> 
> ```txt
> dashboard
> documents
> ai
> chronicle
> notes
> objects
> forms
> contracts
> tax
> care
> settings
> admin
> ```
> 
> That sequence makes sense operationally:
> - daily work first
> - specialized modules later
> - admin last
> 
> ---
> 
> # Bottom line
> 
> You do **not** need to obsess over monorepo cleverness if the system is really one app.
> 
> You need:
> - one app shell
> - clean feature boundaries
> - a few shared utilities
> - backend/runtime separated from UI
> 
> That’s it.
> 
> The right level of sophistication here is **boring and durable**, not “enterprise cosplay.”
> 
> If you want, next I’ll turn this into an exact **rename/move map from your current `qione-portal` tree to the final `apps/qione` structure**.

### User
> just give me a ide promtp to merge, migrate, update and purge the old.

### Assistant
> ```markdown
> You are helping me refactor and normalize my monorepo into a **single primary app architecture**.
> 
> ## Mission
> Merge, migrate, update, and purge the repo so that the final experience layer is centered on:
> 
> - `apps/qione` = the one authenticated operating app
> - `apps/qially-web` = the public-facing marketing / public web app
> 
> Everything else should be evaluated as:
> - module inside `qione`
> - shared package
> - worker/runtime/service
> - content/data
> - archive/legacy
> - delete/noise
> 
> ---
> 
> ## Core architectural decision
> Treat **QiOne** as the single login shell and primary user-facing app.
> 
> This means the following are **not separate apps anymore** unless there is a hard technical reason:
> - QiVault
> - QiArchive
> - QiChronicle
> - QiNote
> - Gina AI chat
> - AI hub
> - document viewer/search
> - notes/journals/stories
> - forms/contracts/objects/cases/tax/care workflows
> 
> These should become modules/features inside `apps/qione`.
> 
> ---
> 
> ## Final target structure
> Build toward this shape:
> 
> ```txt
> apps/
>   qione/
>     public/
>     src/
>       app/
>       components/
>       features/
>       lib/
>       types/
>       styles/
>     supabase/
>     content/
>     package.json
>     tsconfig.json
>     next.config.mjs
>     middleware.ts
>     README.md
> 
>   qially-web/
>     ...
> 
> packages/
>   ui/           # only if truly shared between qione and qially-web
>   database/     # shared types/helpers if truly reused
>   config/       # only if truly shared
> 
> workers/
> python_core/
> supabase/
> scripts/
> content/
> archive/
> ```
> 
> ---
> 
> ## Required behavior
> Do **all** of the following:
> 
> ### 1. Inventory and classify
> Scan the current repo and classify folders/files into one of these buckets:
> 
> - `KEEP_IN_QIONE`
> - `KEEP_IN_QIALLY_WEB`
> - `MOVE_TO_PACKAGES`
> - `MOVE_TO_WORKERS`
> - `MOVE_TO_PYTHON_CORE`
> - `MOVE_TO_SUPABASE`
> - `MOVE_TO_CONTENT`
> - `MOVE_TO_ARCHIVE`
> - `DELETE`
> 
> Before changing anything, produce a clear migration plan.
> 
> ---
> 
> ### 2. Consolidate app roots
> Refactor the repo so that:
> - `apps/qione-portal` becomes the base of the new `apps/qione`
> - document, chronicle, note, AI, forms, object, and workflow capabilities are merged into `apps/qione` as feature modules
> - `apps/qially-com` becomes `apps/qially-web` if needed, or is normalized in place as the single public web app
> - old nested pseudo-apps, duplicate app roots, and legacy app folders are removed or archived
> 
> ---
> 
> ### 3. Purge fake app boundaries
> Identify folders that are pretending to be standalone apps but are actually:
> - prototypes
> - nested repos
> - old launchers
> - duplicated versions
> - legacy snapshots
> - microsites/campaigns that should be content/routes instead
> - mixed junk drawers containing docs/data/workers/templates/public/src all together
> 
> Examples likely needing demotion, merge, archive, or deletion:
> - `apps/gina-ai-chat`
> - nested `apps/` inside app folders
> - `qially-com-v2.0`
> - `_dirtfree_legacy`
> - `_qsaysit_legacy`
> - `.bak`, `.bak2`, duplicated route files, duplicate structures
> - duplicate workers inside app folders when canonical workers exist at root
> - duplicate supabase migration trees when canonical migrations exist elsewhere
> - stray `index.html` placeholders that serve no real purpose
> 
> Do **not** preserve chaos just because it exists.
> 
> ---
> 
> ### 4. Rebuild `apps/qione` around feature modules
> Restructure `apps/qione` so that it uses a clean feature/domain layout.
> 
> Target module namespaces:
> 
> ```txt
> dashboard
> documents
> ai
> chronicle
> notes
> objects
> forms
> contracts
> tax
> care
> settings
> admin
> ```
> 
> Use this internal pattern where appropriate:
> 
> ```txt
> src/
>   app/
>   components/
>   features/
>     ai/
>     chronicle/
>     notes/
>     documents/
>     objects/
>     forms/
>     contracts/
>     tax/
>     care/
>     admin/
>   lib/
>   types/
>   styles/
> ```
> 
> Rules:
> - route files live in `src/app`
> - reusable UI lives in `src/components`
> - domain logic lives in `src/features/<domain>`
> - true cross-cutting services live in `src/lib`
> - no random dumping grounds
> 
> ---
> 
> ### 5. Preserve what matters
> When merging and migrating:
> - preserve important business logic
> - preserve working route handlers
> - preserve useful UI components
> - preserve database integrations worth keeping
> - preserve reusable types/helpers
> - preserve canonical migrations
> - preserve working authentication and permission logic
> - preserve real workflows
> 
> But:
> - do not preserve duplication
> - do not preserve obsolete experiments by default
> - do not preserve placeholder junk
> - do not preserve multiple competing “final” versions
> 
> ---
> 
> ### 6. Archive aggressively, don’t hoard in-place
> Anything old but maybe worth reference should move to a proper archive area such as:
> 
> ```txt
> archive/
>   legacy/
>     qione/
>     qially-web/
>     gina/
>     experiments/
> ```
> 
> Use archive instead of leaving old junk mixed into live app roots.
> 
> If something is clearly useless, delete it instead of archiving it.
> 
> ---
> 
> ### 7. Normalize naming
> Apply consistent naming:
> - no version suffixes like `-v2`, `v2.0`, `copy`, `final-final`
> - no nested app roots inside app folders
> - no mixed casing chaos
> - no duplicate “launcher” or “core” names unless they refer to real distinct runtime boundaries
> - prefer stable names aligned to final architecture
> 
> Use:
> - `qione`
> - `qially-web`
> - `workers`
> - `python_core`
> - `supabase`
> - `packages`
> - `content`
> - `archive`
> 
> ---
> 
> ### 8. Prefer boring architecture over clever architecture
> Do **not** over-modularize into unnecessary packages.
> Only extract shared packages if the reuse is real.
> 
> For now, assume:
> - one main app = `qione`
> - one public app = `qially-web`
> - small shared package layer at most
> 
> Do not create abstraction just for aesthetics.
> 
> ---
> 
> ## Deliverables
> Work in this order:
> 
> ### Phase A — analysis
> Output:
> 1. current problems found
> 2. proposed target map
> 3. keep / move / archive / delete plan
> 
> ### Phase B — migration execution
> Then perform the reorganization:
> - rename folders
> - move files
> - merge duplicate logic where appropriate
> - update imports/paths/references
> - remove dead files
> - create missing target folders
> - preserve build integrity
> 
> ### Phase C — cleanup
> After migration:
> - remove empty folders
> - remove duplicate package-locks where not needed
> - remove obsolete app-local worker copies if canonical workers exist
> - remove stale `.bak` / `.bak2` files
> - remove unused placeholders
> - update README / workspace references / config paths if needed
> 
> ### Phase D — final report
> At the end, provide:
> 1. final folder tree for `apps/qione`
> 2. final folder tree for `apps/qially-web`
> 3. list of archived folders
> 4. list of deleted folders/files
> 5. any manual follow-up items still required
> 
> ---
> 
> ## Guardrails
> - Do not invent features that are not already implied by the repo
> - Do not blindly delete without classifying first
> - Do not leave multiple competing structures active
> - Do not keep legacy folders in live app roots
> - Do not split major features into separate apps unless absolutely necessary
> - Do not turn infrastructure into app folders
> - Do not create unnecessary packages
> 
> ---
> 
> ## Decision rule
> When uncertain, prefer this hierarchy:
> 
> 1. module inside `apps/qione`
> 2. shared package if genuinely reused
> 3. worker/runtime layer if background processing
> 4. archive if old but maybe useful
> 5. delete if junk
> 
> ---
> 
> ## Success criteria
> The repo should end with:
> - one clear authenticated app: `apps/qione`
> - one clear public app: `apps/qially-web`
> - all major capabilities folded into `qione` as modules/features
> - no fake app boundaries
> - no duplicate legacy clutter in live app roots
> - no unresolved architectural identity crisis
> 
> Start by analyzing the current tree and produce the keep/move/archive/delete plan before executing changes.
> ```

### User
> btw we were talking about atomic entites for how we would do our logic and did you know i literally was trying to create a node app that used cells as the metaphor and i have installed the atomic database for testing how it looks and then you asked me that today. interesting.

### Assistant
> Yeah… that’s actually **very on-brand for the way your brain works**. You tend to circle a concept from multiple directions until it finally snaps into a clean model. The “cells / atomic entities” thing isn’t random — it’s the natural end state of the systems you’ve been trying to build.
> 
> Let’s unpack the coincidence a little because there’s a real architectural insight hiding in it.
> 
> ---
> 
> # Why the “atomic / cell” metaphor keeps appearing
> 
> Everything you’ve been designing across QiOne already pushes toward the same pattern:
> 
> You want:
> 
> - **entity-first logic**
> - modular systems
> - composable records
> - everything linkable
> - timeline awareness
> - RAG over knowledge objects
> - permissioned access
> - cross-domain reuse
> 
> Those requirements **almost always converge on an atomic data model**.
> 
> Meaning:
> 
> ```
> system = graph of small entities
> ```
> 
> not
> 
> ```
> system = giant rigid tables or documents
> ```
> 
> ---
> 
> # What “atomic entities” actually means in your system
> 
> An **atomic entity** is the smallest meaningful unit of truth.
> 
> Examples in your world:
> 
> | entity | example |
> |------|------|
> | person | client, contact, family member |
> | document | pdf, receipt, contract |
> | event | chronicle moment |
> | task | reminder, todo |
> | object | asset, property |
> | record | tax return |
> | message | communication |
> | note | journal entry |
> | case | legal issue |
> | file | storage object |
> 
> Each one becomes a **cell** in the system.
> 
> ---
> 
> # Why the cell metaphor works
> 
> Think of QiOne like a **living organism**.
> 
> ```
> cells = entities
> tissue = modules
> organs = features
> organism = qione
> ```
> 
> So:
> 
> ```
> Contact
> Case
> Document
> Note
> Task
> ChronicleMoment
> TaxReturn
> Expense
> Asset
> ```
> 
> These are **cells**.
> 
> Modules like:
> 
> ```
> documents
> chronicle
> tax
> care
> ai
> objects
> ```
> 
> are **organs** built from those cells.
> 
> ---
> 
> # This is exactly how modern knowledge systems work
> 
> Systems built like this include:
> 
> - **Notion**
> - **Airtable**
> - **Coda**
> - **Roam / Logseq**
> - **Obsidian graph plugins**
> - **Datomic**
> - **EdgeDB**
> - **SurrealDB**
> - **Neo4j**
> - **Firebase**
> 
> They all eventually converge on:
> 
> ```
> entity + attributes + relationships
> ```
> 
> instead of rigid schemas.
> 
> ---
> 
> # Why this matters for QiOne
> 
> Because your modules will become **views over the same atomic entities**.
> 
> Example:
> 
> ### A document
> 
> ```
> Entity: Document
> id: doc_001
> title: Lease Agreement
> owner: Cody
> tags: legal
> created: 2025-10-04
> ```
> 
> ### Chronicle
> 
> ```
> ChronicleMoment
> linked_entity: doc_001
> event: signed
> date: 2025-10-05
> ```
> 
> ### Case module
> 
> ```
> Case
> documents: [doc_001]
> participants: [contact_002]
> timeline: [...]
> ```
> 
> ### AI module
> 
> ```
> RAG embedding
> source_entity: doc_001
> vector: [...]
> ```
> 
> Same **atomic entity** reused everywhere.
> 
> ---
> 
> # Why your instinct to test an “atomic database” makes sense
> 
> Because systems like **Datomic** and **SurrealDB** already follow this philosophy.
> 
> Atomic / entity databases treat data as:
> 
> ```
> entity
> attribute
> value
> ```
> 
> Example:
> 
> ```
> [doc_001, type, document]
> [doc_001, owner, cody]
> [doc_001, title, "Lease Agreement"]
> [doc_001, created, 2025-10-04]
> ```
> 
> Everything becomes composable.
> 
> ---
> 
> # What your Node “cell system” probably wanted to become
> 
> Something like:
> 
> ```
> Cell {
>   id
>   type
>   attributes {}
>   relations []
> }
> ```
> 
> Example:
> 
> ```
> Cell
>  id: contact_001
>  type: contact
>  attributes:
>    name: "Sara"
>    email: "..."
>  relations:
>    cases: [case_003]
>    documents: [doc_001]
> ```
> 
> That’s a **graph-like atomic model**.
> 
> ---
> 
> # How this fits perfectly with your QiOne architecture
> 
> If you follow the entity model, your modules become **interfaces over entities**.
> 
> Example:
> 
> ```
> features/
>   objects
>   documents
>   chronicle
>   tax
>   care
>   ai
> ```
> 
> Each module just operates on entities.
> 
> ---
> 
> # Example entity registry
> 
> Something like:
> 
> ```
> entity_types
> 
> contact
> client
> case
> document
> note
> chronicle_moment
> task
> expense
> tax_return
> asset
> appointment
> message
> file
> ```
> 
> Then modules reference those.
> 
> ---
> 
> # This is why I keep pushing “entity-first”
> 
> Because once you do this:
> 
> You can easily add new modules without rewriting the system.
> 
> Example:
> 
> You add:
> 
> ```
> feature: immigration
> ```
> 
> You don’t redesign the database.
> 
> You reuse:
> 
> ```
> contacts
> documents
> cases
> timeline
> notes
> tasks
> ```
> 
> ---
> 
> # Funny part about the coincidence
> 
> You said:
> 
> > I literally was trying to create a node app that used cells
> 
> That’s basically the **same mental model** as:
> 
> - entity graph
> - atomic records
> - composable objects
> - knowledge graph
> - RAG entity store
> 
> You were already halfway there.
> 
> ---
> 
> # The real architecture insight
> 
> Your system is probably this:
> 
> ```
> QiOne = entity operating system
> ```
> 
> Modules = tools that manipulate entities.
> 
> AI = assistant that reasons about entities.
> 
> Workers = processes that generate entities.
> 
> ---
> 
> # Example
> 
> You upload a document.
> 
> ```
> worker
> ↓
> create entity: document
> ↓
> extract text
> ↓
> create entity: document_content
> ↓
> create entity: embedding
> ↓
> link chronicle event
> ↓
> AI indexes
> ```
> 
> Everything becomes **cells in the organism**.
> 
> ---
> 
> # Why this matters for you specifically
> 
> Because you hate systems where:
> 
> - data gets trapped in silos
> - modules can’t talk to each other
> - schemas block new ideas
> 
> Atomic/entity systems solve that.
> 
> ---
> 
> # One warning though
> 
> Atomic models are **powerful but dangerous** if you go too abstract too early.
> 
> You still need:
> 
> ```
> domain models
> validation
> permissions
> indexes
> queries
> ```
> 
> Otherwise you build chaos.
> 
> ---
> 
> # The sweet spot
> 
> Use **structured entities**, not pure free-form atomic chaos.
> 
> Example:
> 
> ```
> Document
> Contact
> Case
> ChronicleMoment
> Note
> Task
> Expense
> TaxReturn
> ```
> 
> Each has a defined schema but still links freely.
> 
> ---
> 
> # My guess about what just happened
> 
> You were unconsciously trying to design:
> 
> ```
> QiOne = entity graph OS
> ```
> 
> before we even said it out loud.
> 
> The “cell” metaphor was your brain’s way of expressing the same architecture.
> 
> ---
> 
> If you want, next I can also show you something that would **really lock this system together**:
> 
> The **QiOne Entity Registry + Object Contract model**.
> 
> It’s basically the missing piece that makes atomic/entity architecture sane instead of chaotic.

### User
> you know i just finished cleaning my repo and i was left with 7 repos. lol, the mono repo, qiarchive, qione, qinode that im going to share with you about what we ware talking about, astro modulaur, qially.coma nd qially.com flows which is the n8n api i think.

### Assistant
> That actually tracks. Seven is still a lot, but it’s **way better than the shapeshifting blob** you had before.
> 
> Here’s the honest read:
> 
> ## What you probably have now
> 
> - **monorepo** → should be the main house
> - **qiarchive** → maybe should be folded in unless it has a real separate runtime reason
> - **qione** → maybe this should actually become the monorepo app, depending on what’s inside the mono repo
> - **qinode** → likely your entity/logic playground or engine
> - **astro modular** → sounds like framework scaffolding, not necessarily a forever repo
> - **qially.com** → public site, valid separate repo if you want
> - **qially.com flows** → likely infra/service repo, not really a brand-level product repo
> 
> ## My blunt take
> 
> You probably still have **too many repos**, but now they at least sound classifiable.
> 
> The real question is not “is 7 okay?”
> The real question is:
> 
> ## Which of these are:
> - **core product**
> - **public web**
> - **supporting engine**
> - **temporary scaffold**
> - **infra/service**
> - **redundant**
> 
> Because I strongly suspect some of these should collapse.
> 
> # My first-pass classification
> 
> ## Likely keep
> ### 1. **monorepo**
> This should be the primary repo **if** it truly contains the unified future state.
> 
> ### 2. **qially.com**
> Public site repo. Fine.
> 
> ### 3. **qially.com flows**
> Maybe keep, but rename later. This sounds like integration/automation infra, not a normal public repo.
> 
> ## Probably merge or absorb
> ### 4. **qione**
> If your monorepo is supposed to contain `apps/qione`, then a separate `qione` repo is suspicious.
> You probably want:
> - either `qione` is the monorepo
> - or `qione` becomes an app inside the monorepo
> 
> Not both long-term.
> 
> ### 5. **qiarchive**
> If archive/document intelligence is part of the unified logged-in system, this likely becomes:
> - `apps/qione/src/features/documents`
> - plus workers/services
> 
> A separate repo only makes sense if it is a truly standalone product/runtime.
> 
> ### 6. **astro modular**
> This sounds the most disposable.
> Could be:
> - starter kit
> - component playground
> - migration source
> - design scaffold
> 
> But it does **not** sound like a forever repo unless you’re using it as a true framework base.
> 
> ### 7. **qinode**
> This one could be important, depending on what it is.
> 
> If `qinode` is:
> - your atomic entity engine
> - object contract system
> - graph/cell logic
> - core domain model playground
> 
> then it may deserve life as a **package or engine**, not necessarily a separate repo.
> 
> # My likely end-state recommendation
> 
> Long-term, I’d expect this to compress toward:
> 
> ### Keep as separate repos
> - **QiOne monorepo** or whatever your main repo becomes
> - **qially.com**
> - **flows/infra** repo if truly separate operationally
> 
> ### Fold into the main repo
> - qiarchive
> - qione
> - astro modular
> - maybe qinode
> 
> So maybe:
> ## 7 now → 3 or 4 later
> 
> That’s probably the right direction.
> 
> # The part you need to decide fast
> 
> You need to choose what the **center of gravity** is.
> 
> Right now I’d ask this strategically:
> 
> ## Which repo is the real future home?
> Only one gets to be the center.
> 
> Probably one of these:
> - the monorepo
> - qione
> 
> Not both.
> 
> If the monorepo is the future, then:
> - `qione` becomes app/module content
> - `qiarchive` becomes a module/service set
> - `qinode` becomes a package/engine
> - `astro modular` becomes source material or archive
> 
> If `qione` is the future, then the “monorepo” may just be badly named staging clutter.
> 
> # Naming problem
> Also, tiny but important:
> You’ve got names describing **brand, app, framework, and infra** all at the same level. That creates false equivalence.
> 
> These are not peers:
> 
> - `qially.com` = public web presence
> - `qione` = product/app
> - `qinode` = maybe engine/model
> - `flows` = automation/integration service
> - `astro modular` = framework/starter/migration base
> - `qiarchive` = product/module/domain
> 
> Those belong to different layers.
> 
> # My straight recommendation
> 
> For now, don’t merge anything blindly just because there are seven.
> 
> Do this instead:
> 
> ## Label each repo with one role only
> Use this exact format:
> 
> ```txt
> Repo Name
> Primary role:
> Users:
> Why separate:
> Likely future:
> ```
> 
> Example:
> 
> ```txt
> qially.com
> Primary role: public marketing site
> Users: public visitors
> Why separate: public deploy cycle and SEO
> Likely future: keep separate
> ```
> 
> Do that for all 7 and the dead weight will expose itself fast.
> 
> ## My current suspicion
> Here’s my rough call without seeing internals:
> 
> ```txt
> KEEP
> - monorepo
> - qially.com
> - qially.com flows
> 
> MERGE LATER
> - qione
> - qiarchive
> - qinode
> 
> PROBABLY TEMP / ARCHIVE
> - astro modular
> ```
> 
> That’s my honest guess.
> 
> Send me the one-line purpose of each of the 7 and I’ll tell you which are real, which are duplicate, and which are just emotional support repos.

### User
> heres the readme for the qinode experiement. 🧬 QiNode: Master Specification v1.1

> Powered by the Qiondria Protocol

> The Local-First, Cellular Self-Healing Autonomous Knowledge Organism.

> 

> 🧬 Phase 1: Expansion Status

> The Nucleus (QiNode_Genesis_Root): Your root authority is alive.

> The DNA (data.json): Contains the immutable UUID and lineage.

> The Proteins (index.md): Explains the mission of retention and creation.

> The Stem Cells (src/main.rs): Awaiting the instruction set for the Qiondria Engine.

> 🔬 Dev Note: Genesis Verification

> NOTE: To verify the Visual Membrane, open QiNode_Genesis_Root/bin/logo.svg in a browser. In this phase, we ensure the SVG Morphogenesis is locked. (The bin folder and logo.svg have been successfully synthesized).

> 

> 🛠️ Phase 2: The Tissue (Ingestion Engine)

> We now transition from Creation to Metabolism. Our goal is to build the "Sight" of the organism—teaching it to ingest a PDF and distill it into a new QiNode.

> 

> Step 1: The Genetic Configuration (Cargo.toml)

> We have added the "Proteins" (libraries) to handle high-fidelity extraction and image processing:

> 

> [dependencies]

> # The Sight: For PDF rendering and image compression

> pdfium-render = "0.8" 

> image = { version = "0.24", features = ["webp"] }

> Step 2: The First Metabolic Function (src/main.rs)

> We will start by coding the PDF-to-Image pipeline. This function will take a file, render each page at 150 DPI, and save it as an optimized WebP in a new node's bin/ folder.

> 

> 층 2: The Nervous System (The Local Ledger)

> To manage 100,000+ nodes, the organism requires a high-speed coordination layer that mirrors the state of the drive.

> 

> The Master Ledger (SQLite + FTS5)

> The Map: A local, lightning-fast index that mirrors the DNA of all discovered QiNodes.

> The Observer: A background service (Chokidar/Notify) that watches for "Mutations" (file moves or renames in the OS).

> The Pulse: Real-time updating of the Ledger when a user moves a folder externally.

> 층 3: The Organism (The Desktop Application)

> The QiNode Desktop App is the macro-interface for the human to interact with the colony of nodes.

> 

> Core Systems

> The Lens (UI): A block-based Markdown editor that renders the index.md and "hydrates" the bin/ assets.

> The Immune System (Reconstruction Engine): The "Disaster Recovery" tool. It ignores folder paths, reads internal DNA, and rebuilds the entire KB structure from a "shattered" state.

> The Synapse (Search): Hybrid search combining Keyword (SQLite) and Semantic (Vector) logic.

> The Portal (Light Viewer): A zero-dependency, Wasm-based web tool that can open and search a single QiNode folder anywhere.

> 층 4: The Evolution (History & Lineage)

> QiNode records its own evolution to ensure data is never truly lost.

> 

> Mitosis (Branching): New nodes carry the parent_id of their source, preserving the tree of knowledge.

> The Ledger Log: An append-only record of changes, allowing the "Immune System" to restore the organism to a specific timestamp.

> 🛡 The Developer Manifesto

> Sovereignty: A node must be able to leave the app and remain functional.

> Resilience: The system must be able to rebuild itself from the files alone.

> Purity: No cloud dependencies. No proprietary formats. Local-First forever.

> © 2024 QiNode Project - Powered by Qiondria

### Assistant
> This README is actually **very revealing**, and I’m glad you shared it. I’m going to give you the **straight architectural read**, not the hype read.
> 
> Short version:
> 
> **QiNode is not an app.  
> QiNode is a data model + storage protocol.**
> 
> That’s the key realization.
> 
> ---
> 
> # What QiNode actually is
> 
> Under all the poetic language, QiNode describes a **local-first knowledge object format**.
> 
> Your “cell” idea again.
> 
> A QiNode looks like:
> 
> ```
> node/
>  ├─ data.json     # identity / lineage / metadata (DNA)
>  ├─ index.md      # human-readable content (proteins)
>  ├─ bin/          # assets (images, pdf pages, media)
>  └─ lineage.log   # optional history
> ```
> 
> Each folder is a **portable knowledge object**.
> 
> This is extremely similar to how systems like:
> 
> - Obsidian
> - Logseq
> - Roam export
> - Git-based knowledge bases
> - Datomic-style entity stores
> 
> structure things.
> 
> But your version adds:
> 
> - **UUID identity**
> - **lineage**
> - **self-healing reconstruction**
> - **local ledger indexing**
> 
> That’s actually pretty solid.
> 
> ---
> 
> # The important realization
> 
> QiNode should **not be its own product repo long-term**.
> 
> It should become one of these:
> 
> ### Option A (best): a **core protocol**
> Inside your main system.
> 
> ```
> packages/
>   qinode/
> ```
> 
> or
> 
> ```
> packages/
>   knowledge-node/
> ```
> 
> It defines:
> 
> - node format
> - ingestion rules
> - lineage tracking
> - reconstruction logic
> - indexing model
> 
> ---
> 
> ### Option B: a **filesystem storage layer**
> 
> Your system becomes:
> 
> ```
> QiOne (app)
>     ↓
> QiNode protocol (storage format)
>     ↓
> filesystem
> ```
> 
> Meaning:
> 
> ```
> QiOne = interface
> QiNode = data organism
> ```
> 
> That pairing actually makes sense.
> 
> ---
> 
> # What the README is trying to build
> 
> You outlined 4 layers.
> 
> Let’s translate them into real engineering terms.
> 
> ---
> 
> ## Layer 1 — Node format
> 
> ```
> QiNode folder
> ```
> 
> Portable atomic knowledge unit.
> 
> Contains:
> 
> ```
> data.json
> index.md
> bin/
> ```
> 
> This is basically **a knowledge object container**.
> 
> Good idea.
> 
> ---
> 
> ## Layer 2 — ingestion engine
> 
> This is just a **pipeline**:
> 
> ```
> PDF
>  ↓
> render pages
>  ↓
> compress images
>  ↓
> generate node
> ```
> 
> Technically this belongs in:
> 
> ```
> workers/
>   ingestion
> ```
> 
> not a separate repo.
> 
> ---
> 
> ## Layer 3 — local ledger
> 
> You described:
> 
> ```
> SQLite + FTS
> file watcher
> indexing
> ```
> 
> This is your **metadata index**.
> 
> That belongs either in:
> 
> ```
> packages/qinode-index
> ```
> 
> or
> 
> ```
> workers/indexer
> ```
> 
> ---
> 
> ## Layer 4 — desktop organism
> 
> This is the **UI**.
> 
> But your architecture already decided:
> 
> > QiOne is the UI.
> 
> So this becomes:
> 
> ```
> QiOne
>   documents module
>   knowledge module
> ```
> 
> ---
> 
> # The manifesto is actually good
> 
> These principles are solid:
> 
> ### Sovereignty
> Files survive without app.
> 
> ### Resilience
> System can rebuild from files.
> 
> ### Purity
> Local-first storage.
> 
> That aligns with your goals.
> 
> ---
> 
> # The real architecture that emerges
> 
> You accidentally designed something very coherent.
> 
> ```
> QiOne (main app)
>    ↓
> QiNode protocol (knowledge objects)
>    ↓
> filesystem
> ```
> 
> Supporting layers:
> 
> ```
> workers/
>   ingestion
>   embedding
>   metadata
>   indexer
> 
> supabase/
>   ledger
>   vectors
> 
> packages/
>   qinode
>   ai
>   database
> ```
> 
> ---
> 
> # Why this experiment matters
> 
> QiNode solves a problem most apps ignore:
> 
> **long-term knowledge durability**
> 
> Typical apps trap data in:
> 
> - databases
> - SaaS platforms
> - proprietary formats
> 
> Your approach:
> 
> ```
> knowledge = folders
> ```
> 
> That’s powerful.
> 
> ---
> 
> # What I would change in the README
> 
> The biological metaphor is fun but hides the real architecture.
> 
> Underneath, this is simply:
> 
> ```
> Portable Knowledge Node Specification
> ```
> 
> You could rewrite the concept like this:
> 
> ```
> QiNode = Atomic Knowledge Object
> 
> Structure:
>   node/
>     data.json
>     index.md
>     assets/
> ```
> 
> ---
> 
> # The real place QiNode belongs
> 
> Not as a separate repo.
> 
> I would move it into your main architecture as:
> 
> ```
> packages/
>   qinode/
>       node_schema
>       lineage
>       ingestion
>       reconstruction
> ```
> 
> Then workers use it.
> 
> And QiOne reads it.
> 
> ---
> 
> # The coolest part of your idea
> 
> This line:
> 
> > The Immune System (Reconstruction Engine)
> 
> That’s actually **the killer feature**.
> 
> It means:
> 
> If the directory structure breaks:
> 
> ```
> scan all nodes
> read UUIDs
> read lineage
> rebuild structure
> ```
> 
> That is genuinely clever.
> 
> ---
> 
> # The connection to the “atomic entities” discussion
> 
> QiNode = **filesystem entity**
> 
> QiOne database = **indexed entity**
> 
> Your system becomes:
> 
> ```
> filesystem = truth
> database = index
> ```
> 
> Very robust model.
> 
> ---
> 
> # My recommendation
> 
> Do **not** keep QiNode as a standalone product repo.
> 
> Instead:
> 
> ### move it into the monorepo as
> 
> ```
> packages/qinode
> ```
> 
> Then use it across:
> 
> ```
> workers
> QiOne
> ingestion
> RAG
> search
> ```
> 
> ---
> 
> # Your repo structure then becomes
> 
> ```
> apps/
>   qione
>   qially-web
> 
> packages/
>   qinode
>   ai
>   database
>   ui
> 
> workers/
>   ingestion
>   indexer
>   embedding
>   metadata
> 
> content/
>   nodes
> 
> supabase/
>   migrations
> ```
> 
> ---
> 
> # My honest take
> 
> This experiment is actually **one of the more interesting ideas you’ve had**.
> 
> But the mistake would be treating it as:
> 
> ```
> QiNode = another product
> ```
> 
> It’s not.
> 
> It’s a **knowledge storage protocol** for your system.
> 
> ---
> 
> If you want, I can also show you something important next:
> 
> **How QiNode + QiOne + RAG can form a unified knowledge organism.**
> 
> And that architecture is **much simpler than you probably expect.**

### User
> yes, we move it into the qione app, its like ive been building all the pieces randomly and frustrated nothing works until one day i slam by fist on the desk and all the random project fall to the floor and then i see it how they really all are part of something bigger.

### Assistant
> Exactly. That’s what was happening.
> 
> You were not “failing to finish projects.”  
> You were **discovering system fragments out of order**.
> 
> Annoying? Yes.  
> Inefficient? Also yes.  
> But not meaningless.
> 
> What you’ve really been building is:
> 
> - a **single operating environment**
> - with **multiple domain surfaces**
> - powered by a **shared entity model**
> - backed by **portable knowledge objects**
> - with ingestion, memory, search, and workflows all feeding the same organism
> 
> So the fix is not “try harder on random side projects.”  
> The fix is:
> 
> ## stop treating fragments like separate destinies
> 
> They were prototypes of organs, not standalone creatures.
> 
> ### Translation of your past projects
> - **QiNode** = knowledge object protocol
> - **QiArchive** = document/ingestion domain
> - **QiChronicle** = temporal/event layer
> - **Gina / AI hub** = intelligence interface
> - **forms/contracts/objects** = structured operational layer
> - **qially.com** = public face
> - **workers / pipelines** = metabolism
> - **Supabase / vectors / ledger** = nervous system + memory index
> 
> All of that belongs to the same body.
> 
> # The new rule
> From now on, every idea gets forced through one question:
> 
> ## Is this:
> 1. a **Qione module**
> 2. a **Qione package/service**
> 3. **public web**
> 4. **archive**
> 
> That’s it.
> 
> No fifth category called “new repo because I’m irritated.”
> 
> # What this means in practice
> 
> ## Inside `apps/qione`
> You now have one shell with modules like:
> 
> ```txt
> src/
>   app/
>     dashboard/
>     ai/
>     documents/
>     chronicle/
>     notes/
>     objects/
>     forms/
>     contracts/
>     tax/
>     care/
>     settings/
>     admin/
> ```
> 
> ## Inside `packages/`
> You move the reusable guts:
> 
> ```txt
> packages/
>   qinode/       # node protocol, lineage, reconstruction, parsing
>   database/     # shared db types/helpers
>   ui/           # only if truly shared
>   ai/           # shared AI helpers if needed
> ```
> 
> ## Inside `workers/`
> You move background metabolism:
> 
> ```txt
> workers/
>   ingestion/
>   embedder/
>   metadata_naming/
>   semantic_router/
>   orchestrator/
>   self_heal/
> ```
> 
> ## Inside `content/`
> You keep actual authored material:
> 
> ```txt
> content/
>   journals/
>   stories/
>   notes/
>   prompts/
>   templates/
>   kb/
>   nodes/
> ```
> 
> # The most important mental shift
> 
> You do **not** need every subsystem to have its own full-blown identity anymore.
> 
> You can still keep the names as **internal product/module names**:
> 
> - QiNode
> - QiArchive
> - QiChronicle
> - QiNote
> 
> But architecturally they become:
> 
> - `documents` module
> - `chronicle` module
> - `notes` module
> - `packages/qinode`
> 
> That’s cleaner and way less cognitively expensive.
> 
> # The truth underneath your frustration
> You were trying to force coherence at the **repo level** before you had coherence at the **system level**.
> 
> Now you do.
> 
> So don’t go back.
> 
> # The decision you just made
> This is the right one:
> 
> ## QiNode does not become another app.
> It becomes part of Qione.
> 
> More specifically:
> 
> ```txt
> apps/qione
>   uses packages/qinode
> ```
> 
> or, if you want to move even faster short-term:
> 
> ```txt
> apps/qione/src/features/documents/qinode/
> ```
> 
> Then later extract it to `packages/qinode` if needed.
> 
> # Best practical move
> Given your tendency to over-fragment when stressed, I’d do this in two stages:
> 
> ## Stage 1: keep it inside Qione
> Fastest path.
> 
> ```txt
> apps/qione/src/features/documents/qinode/
> ```
> 
> Put there:
> - node schema
> - DNA/data.json logic
> - lineage logic
> - reconstruction logic
> - parser/serializer
> - local node helpers
> 
> ## Stage 2: extract later if reuse becomes real
> Move to:
> 
> ```txt
> packages/qinode/
> ```
> 
> Only after it proves itself.
> 
> That keeps you from doing enterprise cosplay before the system breathes.
> 
> # Your new lens
> When random ideas show up, don’t ask:
> 
> “Should this be its own thing?”
> 
> Ask:
> 
> ## “Which part of the organism is this?”
> 
> Because that’s the real pattern you finally saw.
> 
> You weren’t building random trash.  
> You were building dismembered anatomy.
> 
> Now put the body together.
> 
> If you want, next I’ll give you the exact **Qione module map with where QiNode, QiArchive, Chronicle, AI, and forms fit physically in folders**.

### User
> so now we should be able to lock in the repo tree, i think we lock in the root and one level down and hard code it or something to keep me form messing it up again.

### Assistant
> Yes. Do that.
> 
> You are past the “keep it fluid” stage. What you need now is **structural governance**. Lock the root and first level down, then make it annoying to violate.
> 
> ## The move
> Treat the repo tree like a **constitution**, not a suggestion.
> 
> You want two things:
> 
> 1. **Canonical root structure**
> 2. **Automated enforcement**
> 
> Not just a README nobody reads.
> 
> # Lock this in
> 
> ## Root
> ```txt
> /
> ├─ apps/
> ├─ packages/
> ├─ workers/
> ├─ python_core/
> ├─ supabase/
> ├─ content/
> ├─ scripts/
> ├─ archive/
> ├─ docs/
> ├─ .github/
> ```
> 
> If you want it even tighter, `docs/` is optional, but the rest is clean.
> 
> ## One level down
> 
> ### `apps/`
> ```txt
> apps/
> ├─ qione/
> └─ qially-web/
> ```
> 
> ### `packages/`
> Only create if real.
> ```txt
> packages/
> ├─ database/
> ├─ ui/
> ├─ ai/
> └─ qinode/
> ```
> 
> You do **not** need all 4 on day one. But these are the only names allowed unless deliberately added.
> 
> ### `workers/`
> ```txt
> workers/
> ├─ ingestion/
> ├─ embedder/
> ├─ metadata_naming/
> ├─ semantic_router/
> ├─ orchestrator/
> └─ self_heal/
> ```
> 
> ### `python_core/`
> ```txt
> python_core/
> ├─ agents/
> ├─ document_processors/
> └─ local_services/
> ```
> 
> ### `supabase/`
> ```txt
> supabase/
> ├─ migrations/
> ├─ functions/
> ├─ seed/
> └─ snippets/
> ```
> 
> ### `content/`
> ```txt
> content/
> ├─ journals/
> ├─ stories/
> ├─ notes/
> ├─ prompts/
> ├─ templates/
> ├─ kb/
> └─ nodes/
> ```
> 
> ### `scripts/`
> ```txt
> scripts/
> ├─ repo/
> ├─ ingestion/
> ├─ database/
> ├─ sync/
> ├─ dev/
> └─ maintenance/
> ```
> 
> ### `archive/`
> ```txt
> archive/
> ├─ legacy/
> ├─ experiments/
> └─ snapshots/
> ```
> 
> ### `docs/`
> ```txt
> docs/
> ├─ architecture/
> ├─ decisions/
> ├─ guides/
> └─ references/
> ```
> 
> # For `apps/qione`, lock one more level too
> This is worth enforcing because this is where the chaos will come back first.
> 
> ```txt
> apps/qione/
> ├─ public/
> ├─ src/
> ├─ supabase/
> ├─ content/
> ├─ tests/
> └─ docs/
> ```
> 
> And inside `src/`:
> 
> ```txt
> src/
> ├─ app/
> ├─ components/
> ├─ features/
> ├─ lib/
> ├─ types/
> └─ styles/
> ```
> 
> That should be hard-coded too.
> 
> # Yes, hard-code it
> Not emotionally. Literally.
> 
> ## Use 4 layers of enforcement
> 
> ### 1. `target_architecture.txt`
> Create one canonical tree file at root.
> 
> Example:
> ```txt
> ROOT
> - apps
>   - qione
>   - qially-web
> - packages
>   - database
>   - ui
>   - ai
>   - qinode
> - workers
>   - ingestion
>   - embedder
>   - metadata_naming
>   - semantic_router
>   - orchestrator
>   - self_heal
> - python_core
>   - agents
>   - document_processors
>   - local_services
> - supabase
>   - migrations
>   - functions
>   - seed
>   - snippets
> - content
>   - journals
>   - stories
>   - notes
>   - prompts
>   - templates
>   - kb
>   - nodes
> - scripts
>   - repo
>   - ingestion
>   - database
>   - sync
>   - dev
>   - maintenance
> - archive
>   - legacy
>   - experiments
>   - snapshots
> - docs
>   - architecture
>   - decisions
>   - guides
>   - references
> ```
> 
> ### 2. `repo.rules.json`
> Make a machine-readable rules file.
> 
> Example:
> ```json
> {
>   "locked_root_dirs": [
>     "apps",
>     "packages",
>     "workers",
>     "python_core",
>     "supabase",
>     "content",
>     "scripts",
>     "archive",
>     "docs",
>     ".github"
>   ],
>   "locked_first_level": {
>     "apps": ["qione", "qially-web"],
>     "packages": ["database", "ui", "ai", "qinode"],
>     "workers": ["ingestion", "embedder", "metadata_naming", "semantic_router", "orchestrator", "self_heal"],
>     "python_core": ["agents", "document_processors", "local_services"],
>     "supabase": ["migrations", "functions", "seed", "snippets"],
>     "content": ["journals", "stories", "notes", "prompts", "templates", "kb", "nodes"],
>     "scripts": ["repo", "ingestion", "database", "sync", "dev", "maintenance"],
>     "archive": ["legacy", "experiments", "snapshots"],
>     "docs": ["architecture", "decisions", "guides", "references"]
>   }
> }
> ```
> 
> ### 3. validation script
> Have a script that:
> - checks root dirs
> - checks first-level dirs
> - flags unauthorized additions
> - flags misplaced folders
> - optionally auto-suggests destination
> 
> Example script names:
> ```txt
> scripts/repo/validate_tree.py
> scripts/repo/fix_tree.py
> scripts/repo/print_tree_diff.py
> ```
> 
> ### 4. pre-commit or pre-push check
> Run the validator before commits or pushes so you can’t casually mutate structure when annoyed.
> 
> # Real rule set
> These need to be explicit:
> 
> ## Allowed
> - new files inside approved folders
> - new feature folders inside `apps/qione/src/features`
> - new routes inside `apps/qione/src/app`
> - new scripts inside approved script buckets
> 
> ## Not allowed without deliberate update
> - new root folders
> - new first-level folders under locked dirs
> - nested apps
> - versioned clones like `v2`, `copy`, `final-final`
> - duplicate migration trees
> - worker copies inside app folders
> - random docs/data/templates mixed into app root
> 
> # Best practice for your brain
> Because you’re prone to building sideways when the system feels fuzzy, add this rule:
> 
> ## Any new top-level or first-level folder must be created only by generator
> Meaning one script like:
> 
> ```txt
> python scripts/repo/create_structure_item.py --parent apps --name qione
> ```
> 
> or
> 
> ```txt
> python scripts/repo/create_feature.py --name documents
> ```
> 
> No freestyle creation for governed layers.
> 
> # Hard truth
> If you do not lock the tree now, you will absolutely drift it again. Not because you’re sloppy. Because your brain explores by spawning structure. That works for ideation, but it wrecks long-term maintainability.
> 
> So yes, **externalize discipline into the repo**.
> 
> # My recommendation
> Lock these levels:
> 
> ## Locked
> - root
> - first level under root
> - `apps/qione/src`
> - maybe `apps/qially-web/src`
> 
> ## Flexible
> - feature internals
> - route internals
> - component internals
> - content internals
> 
> That gives you structure without suffocation.
> 
> # Clean governance principle
> Think of it like this:
> 
> - **root and level 1** = constitutional law
> - **app src level** = city zoning
> - **feature internals** = furniture arrangement
> 
> You keep moving furniture.  
> You do **not** keep rebuilding the city.
> 
> # The exact next move
> Create these three files first:
> 
> ```txt
> target_architecture.txt
> repo.rules.json
> scripts/repo/validate_tree.py
> ```
> 
> And make `validate_tree.py` fail loudly when the structure drifts.
> 
> If you want, I’ll write all three for you in copy-paste form.

### User
> {'asset_pointer': 'sediment://file_00000000a270722f855c5b0c1e26d5da', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 2048, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 415615, 'width': 1492}wait what do i do with all the module pieces.

### Assistant
> You **sort the module pieces by responsibility**, not by where they came from.
> 
> Right now you likely have fragments of each module scattered across old apps, scripts, workers, docs, and experiments. Don’t move whole folders blindly. **Disassemble first, then re-home the parts.**
> 
> ## The rule
> 
> Each module gets split into **5 buckets**:
> 
> 1. **routes/pages**
> 2. **UI/components**
> 3. **feature logic**
> 4. **background/runtime**
> 5. **content/docs/schema**
> 
> So for every module like `documents`, `chronicle`, `notes`, `ai`, `forms`, etc., you do this.
> 
> ---
> 
> # Where the pieces go
> 
> ## 1) User-facing route pieces
> Anything that renders a page, layout, or route goes in:
> 
> ```txt
> apps/qione/src/app/<module>/
> ```
> 
> Examples:
> - `page.tsx`
> - `layout.tsx`
> - route folders like `[id]/page.tsx`
> - module dashboard pages
> - create/edit/view screens
> 
> ### Example
> ```txt
> apps/qione/src/app/documents/
> apps/qione/src/app/chronicle/
> apps/qione/src/app/notes/
> ```
> 
> ---
> 
> ## 2) Reusable UI pieces
> Anything visual and reusable goes in:
> 
> ```txt
> apps/qione/src/components/<module>/
> ```
> 
> Examples:
> - tables
> - cards
> - editors
> - upload widgets
> - viewers
> - filters
> - side panels
> 
> ### Example
> ```txt
> apps/qione/src/components/documents/DocumentCard.tsx
> apps/qione/src/components/chronicle/TimelineView.tsx
> apps/qione/src/components/notes/NoteEditor.tsx
> ```
> 
> If a component is ultra-local to one feature and won’t be reused, it can live inside that feature instead.
> 
> ---
> 
> ## 3) Domain logic
> This is the big one.  
> Anything that is the **brain of the module** goes in:
> 
> ```txt
> apps/qione/src/features/<module>/
> ```
> 
> Examples:
> - validators
> - schemas
> - data mappers
> - registries
> - business rules
> - hooks specific to module
> - server-side feature logic
> - parsing helpers
> - local utility functions only relevant to that module
> 
> ### Example
> ```txt
> apps/qione/src/features/documents/
>   server/
>   client/
>   schemas/
>   utils.ts
>   registry.ts
> ```
> 
> This is where most of your “module pieces” actually belong.
> 
> ---
> 
> ## 4) Background/process pieces
> If it runs without the user staring at it, it is **not a module page piece**.
> 
> Move those to:
> 
> ### Workers
> ```txt
> workers/<worker-name>/
> ```
> 
> Examples:
> - ingestion jobs
> - embedding jobs
> - metadata naming
> - routing
> - self-heal
> - orchestration
> 
> ### Python core
> ```txt
> python_core/<service-name>/
> ```
> 
> Examples:
> - document processors
> - local agent services
> - extraction services
> - OCR logic
> - experimental local AI services that aren’t page code
> 
> So if you find:
> - file watchers
> - queue runners
> - PDF processors
> - rebuild engines
> - background sync logic
> 
> those do **not** stay inside the module route folders.
> 
> ---
> 
> ## 5) Content/config/docs/schema pieces
> These go in one of these:
> 
> ### If app-specific and used by qione:
> ```txt
> apps/qione/content/
> apps/qione/docs/
> apps/qione/supabase/
> ```
> 
> ### If global/canonical:
> ```txt
> content/
> docs/
> supabase/
> ```
> 
> Examples:
> - prompts
> - templates
> - KB source docs
> - migration SQL
> - seed files
> - architecture notes
> - reference markdown
> 
> ---
> 
> # The simplest way to process the mess
> 
> For each module, create a **staging checklist** like this:
> 
> ## Module: documents
> Put found files into:
> 
> ```txt
> documents/
>   routes
>   components
>   feature_logic
>   background
>   content_docs
>   delete_or_archive
> ```
> 
> Then sort each file.
> 
> After that, move them to final homes:
> 
> - `routes` → `apps/qione/src/app/documents`
> - `components` → `apps/qione/src/components/documents`
> - `feature_logic` → `apps/qione/src/features/documents`
> - `background` → `workers/` or `python_core/`
> - `content_docs` → `content/`, `docs/`, or `supabase/`
> - `delete_or_archive` → `archive/` or trash
> 
> That’s the process.
> 
> ---
> 
> # Example: what to do with QiNode pieces
> 
> Since we just talked about QiNode:
> 
> ## QiNode is not one folder dump
> Split it like this:
> 
> ### Goes into `apps/qione/src/features/documents/qinode/`
> - node schema
> - parser
> - serializer
> - lineage helpers
> - reconstruction rules
> - node registry helpers
> 
> ### Goes into `workers/ingestion/`
> - PDF-to-node creation pipeline
> - automatic node generation jobs
> 
> ### Goes into `workers/self_heal/`
> - rebuild/reconstruction jobs
> 
> ### Goes into `python_core/document_processors/`
> - heavy extraction or OCR logic
> 
> ### Goes into `content/nodes/`
> - actual node content/examples/templates
> 
> ### Goes into `docs/architecture/`
> - QiNode spec docs
> 
> That’s how you avoid another junk drawer.
> 
> ---
> 
> # Example: what to do with `chronicle` pieces
> 
> ### `apps/qione/src/app/chronicle/`
> - timeline pages
> - detail pages
> - create/edit routes
> 
> ### `apps/qione/src/components/chronicle/`
> - timeline renderer
> - filters
> - event cards
> 
> ### `apps/qione/src/features/chronicle/`
> - moment schema
> - timeline logic
> - event linking
> - query helpers
> 
> ### `supabase/migrations/`
> - chronicle tables
> 
> ### `content/`
> - seed prompts/templates if needed
> 
> ---
> 
> # Example: what to do with `ai` pieces
> 
> ### `apps/qione/src/app/ai/`
> - AI dashboard
> - chat UI
> - memory search page
> - agents page
> 
> ### `apps/qione/src/components/ai/`
> - chat panel
> - memory result card
> - prompt editor
> - tool runner UI
> 
> ### `apps/qione/src/features/ai/`
> - AI request orchestration
> - prompt schemas
> - result adapters
> - feature-specific hooks
> 
> ### `packages/ai/` or `apps/qione/src/lib/ai/`
> - shared AI helpers only if truly cross-cutting
> 
> ### `workers/`
> - embeddings
> - routing
> - orchestration
> 
> ### `python_core/agents/`
> - local agents or processing services
> 
> ---
> 
> # Don’t organize by old project name
> This is where you’ll screw it up again if you’re not careful.
> 
> Do **not** say:
> - “this came from qiarchive”
> - “this came from qinode”
> - “this came from gina-ai-chat”
> 
> That history is useful for migration, but **irrelevant for final placement**.
> 
> Final placement is based on:
> 
> - what it does
> - where it runs
> - who uses it
> - whether it is UI, feature logic, infra, or content
> 
> ---
> 
> # Practical cheat sheet
> 
> ## If it renders a screen
> `apps/qione/src/app/...`
> 
> ## If it renders reusable UI
> `apps/qione/src/components/...`
> 
> ## If it contains module/domain logic
> `apps/qione/src/features/...`
> 
> ## If it is shared cross-cutting app service
> `apps/qione/src/lib/...`
> 
> ## If it runs in background
> `workers/...` or `python_core/...`
> 
> ## If it is SQL/schema/seed
> `supabase/...`
> 
> ## If it is authored material/template/prompt
> `content/...`
> 
> ## If it is explanation/reference
> `docs/...`
> 
> ## If it is old but maybe useful
> `archive/...`
> 
> ---
> 
> # What you do next
> Do **not** move everything at once.
> 
> Do it module by module in this order:
> 
> 1. `documents`
> 2. `ai`
> 3. `chronicle`
> 4. `notes`
> 5. `objects`
> 6. `forms`
> 7. `contracts`
> 8. `tax`
> 9. `care`
> 10. `admin`
> 
> Start with `documents` because it has the most tentacles and will force the architecture to prove itself.
> 
> If you want, I’ll turn this into a **copy-paste IDE prompt specifically for sorting module pieces into final destinations**.

### User
> yes, i want the full tree honey, no guess room for me, it can go into csv if it must. but is must show relationships so any ai can spin up the image or mind map for me.

### Assistant
> Yes. Lock it all the way down.
> 
> Below is the **canonical QiOne repo tree** plus a **relationship CSV edge list** so you or any AI can turn it into a mind map, graph, or diagram without improvising.
> 
> ## Canonical repo tree
> 
> ```txt
> QiOne_Organism/
> ├─ .github/
> │  ├─ workflows/
> │  └─ ISSUE_TEMPLATE/
> │
> ├─ apps/
> │  ├─ qione/
> │  │  ├─ public/
> │  │  │  ├─ favicon.ico
> │  │  │  ├─ icons/
> │  │  │  └─ images/
> │  │  │
> │  │  ├─ src/
> │  │  │  ├─ app/
> │  │  │  │  ├─ (public)/
> │  │  │  │  │  ├─ login/
> │  │  │  │  │  ├─ invite/
> │  │  │  │  │  └─ reset-password/
> │  │  │  │  │
> │  │  │  │  ├─ (app)/
> │  │  │  │  │  ├─ layout.tsx
> │  │  │  │  │  ├─ page.tsx
> │  │  │  │  │  │
> │  │  │  │  │  ├─ dashboard/
> │  │  │  │  │  ├─ ai/
> │  │  │  │  │  ├─ documents/
> │  │  │  │  │  ├─ chronicle/
> │  │  │  │  │  ├─ notes/
> │  │  │  │  │  ├─ objects/
> │  │  │  │  │  ├─ forms/
> │  │  │  │  │  ├─ contracts/
> │  │  │  │  │  ├─ tax/
> │  │  │  │  │  ├─ care/
> │  │  │  │  │  ├─ settings/
> │  │  │  │  │  └─ admin/
> │  │  │  │  │
> │  │  │  │  └─ api/
> │  │  │  │     ├─ ai/
> │  │  │  │     ├─ documents/
> │  │  │  │     ├─ chronicle/
> │  │  │  │     ├─ notes/
> │  │  │  │     ├─ objects/
> │  │  │  │     ├─ forms/
> │  │  │  │     ├─ contracts/
> │  │  │  │     ├─ tax/
> │  │  │  │     ├─ care/
> │  │  │  │     ├─ admin/
> │  │  │  │     └─ webhooks/
> │  │  │  │
> │  │  │  ├─ components/
> │  │  │  │  ├─ layout/
> │  │  │  │  ├─ ui/
> │  │  │  │  ├─ ai/
> │  │  │  │  ├─ documents/
> │  │  │  │  ├─ chronicle/
> │  │  │  │  ├─ notes/
> │  │  │  │  ├─ objects/
> │  │  │  │  ├─ forms/
> │  │  │  │  ├─ contracts/
> │  │  │  │  ├─ tax/
> │  │  │  │  ├─ care/
> │  │  │  │  ├─ settings/
> │  │  │  │  └─ admin/
> │  │  │  │
> │  │  │  ├─ features/
> │  │  │  │  ├─ dashboard/
> │  │  │  │  │  ├─ client/
> │  │  │  │  │  ├─ server/
> │  │  │  │  │  ├─ schemas/
> │  │  │  │  │  └─ utils.ts
> │  │  │  │  │
> │  │  │  │  ├─ ai/
> │  │  │  │  │  ├─ client/
> │  │  │  │  │  ├─ server/
> │  │  │  │  │  ├─ schemas/
> │  │  │  │  │  ├─ prompts/
> │  │  │  │  │  ├─ tools/
> │  │  │  │  │  └─ utils.ts
> │  │  │  │  │
> │  │  │  │  ├─ documents/
> │  │  │  │  │  ├─ client/
> │  │  │  │  │  ├─ server/
> │  │  │  │  │  ├─ schemas/
> │  │  │  │  │  ├─ qinode/
> │  │  │  │  │  │  ├─ dna/
> │  │  │  │  │  │  ├─ lineage/
> │  │  │  │  │  │  ├─ parser/
> │  │  │  │  │  │  ├─ serializer/
> │  │  │  │  │  │  ├─ reconstruction/
> │  │  │  │  │  │  └─ registry/
> │  │  │  │  │  └─ utils.ts
> │  │  │  │  │
> │  │  │  │  ├─ chronicle/
> │  │  │  │  │  ├─ client/
> │  │  │  │  │  ├─ server/
> │  │  │  │  │  ├─ schemas/
> │  │  │  │  │  ├─ timeline/
> │  │  │  │  │  └─ utils.ts
> │  │  │  │  │
> │  │  │  │  ├─ notes/
> │  │  │  │  │  ├─ client/
> │  │  │  │  │  ├─ server/
> │  │  │  │  │  ├─ schemas/
> │  │  │  │  │  ├─ journal/
> │  │  │  │  │  ├─ stories/
> │  │  │  │  │  └─ utils.ts
> │  │  │  │  │
> │  │  │  │  ├─ objects/
> │  │  │  │  │  ├─ client/
> │  │  │  │  │  ├─ server/
> │  │  │  │  │  ├─ schemas/
> │  │  │  │  │  ├─ registry/
> │  │  │  │  │  └─ utils.ts
> │  │  │  │  │
> │  │  │  │  ├─ forms/
> │  │  │  │  │  ├─ client/
> │  │  │  │  │  ├─ server/
> │  │  │  │  │  ├─ schemas/
> │  │  │  │  │  ├─ registry/
> │  │  │  │  │  └─ utils.ts
> │  │  │  │  │
> │  │  │  │  ├─ contracts/
> │  │  │  │  │  ├─ client/
> │  │  │  │  │  ├─ server/
> │  │  │  │  │  ├─ schemas/
> │  │  │  │  │  └─ utils.ts
> │  │  │  │  │
> │  │  │  │  ├─ tax/
> │  │  │  │  │  ├─ client/
> │  │  │  │  │  ├─ server/
> │  │  │  │  │  ├─ schemas/
> │  │  │  │  │  ├─ returns/
> │  │  │  │  │  ├─ organizers/
> │  │  │  │  │  └─ utils.ts
> │  │  │  │  │
> │  │  │  │  ├─ care/
> │  │  │  │  │  ├─ client/
> │  │  │  │  │  ├─ server/
> │  │  │  │  │  ├─ schemas/
> │  │  │  │  │  ├─ meds/
> │  │  │  │  │  ├─ supplies/
> │  │  │  │  │  └─ utils.ts
> │  │  │  │  │
> │  │  │  │  ├─ settings/
> │  │  │  │  │  ├─ client/
> │  │  │  │  │  ├─ server/
> │  │  │  │  │  ├─ schemas/
> │  │  │  │  │  └─ utils.ts
> │  │  │  │  │
> │  │  │  │  └─ admin/
> │  │  │  │     ├─ client/
> │  │  │  │     ├─ server/
> │  │  │  │     ├─ schemas/
> │  │  │  │     ├─ permissions/
> │  │  │  │     ├─ workers/
> │  │  │  │     └─ utils.ts
> │  │  │  │
> │  │  │  ├─ lib/
> │  │  │  │  ├─ auth/
> │  │  │  │  ├─ db/
> │  │  │  │  ├─ storage/
> │  │  │  │  ├─ ai/
> │  │  │  │  ├─ integrations/
> │  │  │  │  ├─ permissions/
> │  │  │  │  ├─ utils/
> │  │  │  │  ├─ constants.ts
> │  │  │  │  └─ env.ts
> │  │  │  │
> │  │  │  ├─ types/
> │  │  │  │  ├─ auth.ts
> │  │  │  │  ├─ database.ts
> │  │  │  │  ├─ permissions.ts
> │  │  │  │  └─ common.ts
> │  │  │  │
> │  │  │  └─ styles/
> │  │  │     └─ globals.css
> │  │  │
> │  │  ├─ supabase/
> │  │  │  ├─ module_sql/
> │  │  │  └─ seeds/
> │  │  │
> │  │  ├─ content/
> │  │  │  ├─ prompts/
> │  │  │  ├─ templates/
> │  │  │  ├─ forms/
> │  │  │  └─ kb/
> │  │  │
> │  │  ├─ tests/
> │  │  │  ├─ unit/
> │  │  │  ├─ integration/
> │  │  │  └─ e2e/
> │  │  │
> │  │  ├─ docs/
> │  │  │  ├─ module_maps/
> │  │  │  ├─ route_maps/
> │  │  │  └─ permissions/
> │  │  │
> │  │  ├─ package.json
> │  │  ├─ tsconfig.json
> │  │  ├─ next.config.mjs
> │  │  ├─ middleware.ts
> │  │  ├─ README.md
> │  │  └─ .env.example
> │  │
> │  └─ qially-web/
> │     ├─ public/
> │     ├─ src/
> │     │  ├─ app/
> │     │  ├─ components/
> │     │  ├─ content/
> │     │  ├─ lib/
> │     │  ├─ styles/
> │     │  └─ types/
> │     ├─ package.json
> │     ├─ tsconfig.json
> │     ├─ README.md
> │     └─ .env.example
> │
> ├─ packages/
> │  ├─ qinode/
> │  │  ├─ src/
> │  │  │  ├─ dna/
> │  │  │  ├─ lineage/
> │  │  │  ├─ parser/
> │  │  │  ├─ serializer/
> │  │  │  ├─ reconstruction/
> │  │  │  ├─ registry/
> │  │  │  └─ index.ts
> │  │  ├─ package.json
> │  │  └─ README.md
> │  │
> │  ├─ database/
> │  │  ├─ src/
> │  │  │  ├─ types/
> │  │  │  ├─ queries/
> │  │  │  ├─ adapters/
> │  │  │  └─ index.ts
> │  │  ├─ package.json
> │  │  └─ README.md
> │  │
> │  ├─ ui/
> │  │  ├─ src/
> │  │  │  ├─ components/
> │  │  │  ├─ tokens/
> │  │  │  └─ index.ts
> │  │  ├─ package.json
> │  │  └─ README.md
> │  │
> │  └─ ai/
> │     ├─ src/
> │     │  ├─ prompts/
> │     │  ├─ tools/
> │     │  ├─ adapters/
> │     │  └─ index.ts
> │     ├─ package.json
> │     └─ README.md
> │
> ├─ workers/
> │  ├─ ingestion/
> │  ├─ embedder/
> │  ├─ metadata_naming/
> │  ├─ semantic_router/
> │  ├─ orchestrator/
> │  └─ self_heal/
> │
> ├─ python_core/
> │  ├─ agents/
> │  ├─ document_processors/
> │  └─ local_services/
> │
> ├─ supabase/
> │  ├─ migrations/
> │  ├─ functions/
> │  ├─ seed/
> │  └─ snippets/
> │
> ├─ content/
> │  ├─ journals/
> │  ├─ stories/
> │  ├─ notes/
> │  ├─ prompts/
> │  ├─ templates/
> │  ├─ kb/
> │  └─ nodes/
> │
> ├─ scripts/
> │  ├─ repo/
> │  ├─ ingestion/
> │  ├─ database/
> │  ├─ sync/
> │  ├─ dev/
> │  └─ maintenance/
> │
> ├─ archive/
> │  ├─ legacy/
> │  ├─ experiments/
> │  └─ snapshots/
> │
> └─ docs/
>    ├─ architecture/
>    ├─ decisions/
>    ├─ guides/
>    └─ references/
> ```
> 
> ## Relationship rules
> 
> Use these as **hard placement rules**.
> 
> ### Module placement
> - `apps/qione/src/app/<module>` = routes and screens
> - `apps/qione/src/components/<module>` = reusable UI
> - `apps/qione/src/features/<module>` = module/domain logic
> - `apps/qione/src/lib/*` = cross-cutting services only
> - `apps/qione/content/*` = app-local prompts/templates/forms/KB assets
> - `apps/qione/docs/*` = app-local documentation
> - `apps/qione/supabase/*` = app-local SQL helpers only, not canonical migrations
> 
> ### Global placement
> - `packages/*` = only truly shared code
> - `workers/*` = background runtime jobs
> - `python_core/*` = heavy/local Python services
> - `supabase/*` = canonical DB truth
> - `content/*` = canonical authored content
> - `archive/*` = old but maybe useful
> - `docs/*` = system-level documentation
> 
> ---
> 
> # Mind-map / graph CSV
> 
> Use this as an **edge list**.  
> Columns: `parent,child,relationship,layer,notes`
> 
> ```csv
> parent,child,relationship,layer,notes
> QiOne_Organism,.github,contains,root,repo automation and templates
> QiOne_Organism,apps,contains,root,experience layer
> QiOne_Organism,packages,contains,root,shared code layer
> QiOne_Organism,workers,contains,root,background runtime layer
> QiOne_Organism,python_core,contains,root,python processing layer
> QiOne_Organism,supabase,contains,root,canonical database layer
> QiOne_Organism,content,contains,root,canonical content layer
> QiOne_Organism,scripts,contains,root,developer operations layer
> QiOne_Organism,archive,contains,root,retired assets and experiments
> QiOne_Organism,docs,contains,root,system documentation
> 
> apps,qione,contains,app,primary authenticated operating app
> apps,qially-web,contains,app,public marketing and public web app
> 
> qione,public,contains,app_static,public assets for qione
> qione,src,contains,app_source,source code for qione
> qione,supabase,contains,app_support,app-local sql helpers and seeds
> qione,content,contains,app_support,app-local prompts templates forms kb
> qione,tests,contains,app_support,test suite
> qione,docs,contains,app_support,app-local docs
> 
> src,app,contains,routing,all routes and pages
> src,components,contains,ui,reusable UI components
> src,features,contains,domain,module logic by responsibility
> src,lib,contains,shared,cross-cutting app services
> src,types,contains,types,app-wide types
> src,styles,contains,styles,global styles
> 
> app,(public),contains,routing,unauthenticated routes
> app,(app),contains,routing,authenticated routes
> app,api,contains,routing,route handlers and app APIs
> 
> (app),dashboard,contains,module,main overview and home
> (app),ai,contains,module,ai surfaces inside qione
> (app),documents,contains,module,document and qinode-facing UX
> (app),chronicle,contains,module,timeline and event UX
> (app),notes,contains,module,notes journals stories UX
> (app),objects,contains,module,atomic entity records UX
> (app),forms,contains,module,form rendering and submissions UX
> (app),contracts,contains,module,contract workflows UX
> (app),tax,contains,module,tax workflows UX
> (app),care,contains,module,caregiver and health workflows UX
> (app),settings,contains,module,user-level settings UX
> (app),admin,contains,module,system administration UX
> 
> components,layout,contains,ui,app shell components
> components,ui,contains,ui,primitive shared UI components
> components,ai,contains,ui,module-specific UI
> components,documents,contains,ui,module-specific UI
> components,chronicle,contains,ui,module-specific UI
> components,notes,contains,ui,module-specific UI
> components,objects,contains,ui,module-specific UI
> components,forms,contains,ui,module-specific UI
> components,contracts,contains,ui,module-specific UI
> components,tax,contains,ui,module-specific UI
> components,care,contains,ui,module-specific UI
> components,settings,contains,ui,module-specific UI
> components,admin,contains,ui,module-specific UI
> 
> features,dashboard,contains,feature,module logic
> features,ai,contains,feature,module logic
> features,documents,contains,feature,module logic
> features,chronicle,contains,feature,module logic
> features,notes,contains,feature,module logic
> features,objects,contains,feature,module logic
> features,forms,contains,feature,module logic
> features,contracts,contains,feature,module logic
> features,tax,contains,feature,module logic
> features,care,contains,feature,module logic
> features,settings,contains,feature,module logic
> features,admin,contains,feature,module logic
> 
> features/documents,qinode,contains,protocol,local qinode implementation until extracted
> qinode,dna,contains,protocol,node identity logic
> qinode,lineage,contains,protocol,parent-child history logic
> qinode,parser,contains,protocol,node reader logic
> qinode,serializer,contains,protocol,node writer logic
> qinode,reconstruction,contains,protocol,self-heal rebuild logic
> qinode,registry,contains,protocol,node indexing helpers
> 
> lib,auth,contains,shared,auth guards and session helpers
> lib,db,contains,shared,database clients and queries
> lib,storage,contains,shared,file and blob access helpers
> lib,ai,contains,shared,ai helpers used across modules
> lib,integrations,contains,shared,email calendar crm etc
> lib,permissions,contains,shared,role and access control helpers
> lib,utils,contains,shared,generic helper functions
> 
> packages,qinode,contains,package,extract only when reuse is real
> packages,database,contains,package,shared db helpers and types
> packages,ui,contains,package,shared UI only if truly reused
> packages,ai,contains,package,shared AI helpers only if truly reused
> 
> workers,ingestion,contains,worker,document intake and pipeline jobs
> workers,embedder,contains,worker,vector embedding jobs
> workers,metadata_naming,contains,worker,naming and metadata normalization
> workers,semantic_router,contains,worker,classification and routing jobs
> workers,orchestrator,contains,worker,queue and workflow orchestration
> workers,self_heal,contains,worker,rebuild and repair jobs
> 
> python_core,agents,contains,service,python agent services
> python_core,document_processors,contains,service,ocr extraction heavy parsing
> python_core,local_services,contains,service,local APIs and utilities
> 
> supabase,migrations,contains,data,canonical database schema history
> supabase,functions,contains,data,serverless database-side functions
> supabase,seed,contains,data,seed data
> supabase,snippets,contains,data,sql reference snippets
> 
> content,journals,contains,content,canonical journal content
> content,stories,contains,content,canonical story content
> content,notes,contains,content,canonical note content
> content,prompts,contains,content,canonical prompts
> content,templates,contains,content,canonical reusable templates
> content,kb,contains,content,knowledge base source
> content,nodes,contains,content,qinode-style knowledge objects
> 
> scripts,repo,contains,ops,repo governance and validation
> scripts,ingestion,contains,ops,ingestion developer scripts
> scripts,database,contains,ops,database developer scripts
> scripts,sync,contains,ops,sync and mirror scripts
> scripts,dev,contains,ops,developer startup and helpers
> scripts,maintenance,contains,ops,cleanup and maintenance scripts
> 
> archive,legacy,contains,archive,old live systems retired from active use
> archive,experiments,contains,archive,prototype work not in active architecture
> archive,snapshots,contains,archive,point-in-time captures
> 
> docs,architecture,contains,docs,system maps and architecture docs
> docs,decisions,contains,docs,ADR-style decisions
> docs,guides,contains,docs,how-to and operational guides
> docs,references,contains,docs,reference material
> 
> documents,workers/ingestion,depends_on,flow,documents rely on ingestion jobs
> documents,workers/embedder,depends_on,flow,documents rely on vector indexing
> documents,workers/metadata_naming,depends_on,flow,documents rely on metadata naming
> documents,workers/self_heal,depends_on,flow,documents rely on reconstruction and repair
> documents,python_core/document_processors,depends_on,flow,documents rely on heavy extraction
> documents,supabase/migrations,depends_on,data,documents require canonical schema
> documents,content/nodes,depends_on,content,documents can emit qinode objects
> 
> ai,workers/embedder,depends_on,flow,ai uses embeddings
> ai,workers/semantic_router,depends_on,flow,ai uses routing and classification
> ai,workers/orchestrator,depends_on,flow,ai uses workflow orchestration
> ai,python_core/agents,depends_on,flow,ai may use python agents
> ai,packages/ai,depends_on,package,ai may share common adapters
> 
> chronicle,supabase/migrations,depends_on,data,chronicle needs canonical schema
> chronicle,objects,depends_on,domain,chronicle links to atomic entities
> notes,content/notes,depends_on,content,notes may persist to canonical note content
> notes,content/journals,depends_on,content,journals are a notes subdomain
> notes,content/stories,depends_on,content,stories are a notes subdomain
> 
> forms,objects,depends_on,domain,forms create or update atomic entities
> contracts,objects,depends_on,domain,contracts attach to entities
> tax,documents,depends_on,domain,tax consumes documents
> tax,forms,depends_on,domain,tax uses organizers and intake forms
> care,objects,depends_on,domain,care depends on patients meds supplies as entities
> admin,lib/permissions,depends_on,shared,admin controls authorization surfaces
> admin,workers/orchestrator,depends_on,flow,admin monitors workflows
> admin,workers/self_heal,depends_on,flow,admin monitors repair jobs
> 
> qione,qially-web,separate_from,boundary,public web must remain separate from authenticated app
> qione,packages,uses,boundary,qione may use shared packages but should not depend on unnecessary ones
> qione,workers,uses,boundary,qione triggers and monitors workers
> qione,python_core,uses,boundary,qione may call python services
> qione,supabase,uses,boundary,qione uses canonical db layer
> qione,content,uses,boundary,qione reads and writes canonical content
> ```
> 
> ## Hard anti-chaos rules
> 
> ```txt
> 1. No new root folders without updating the architecture map.
> 2. No new first-level folders under locked roots without deliberate approval.
> 3. No nested apps inside apps.
> 4. No duplicate migrations outside canonical supabase/ unless explicitly app-local helpers.
> 5. No workers inside app folders.
> 6. No versioned clones like v2, copy, final-final, backup-app.
> 7. No module logic dumped into random utils/services folders.
> 8. No keeping old folders in place “just for now”; archive them.
> ```
> 
> ## The actual answer to your question about module pieces
> 
> Every module gets split across these exact homes:
> 
> ```txt
> module routes       -> apps/qione/src/app/<module>/
> module UI           -> apps/qione/src/components/<module>/
> module logic        -> apps/qione/src/features/<module>/
> cross-cutting code  -> apps/qione/src/lib/
> background jobs     -> workers/ or python_core/
> db truth            -> supabase/
> content/templates   -> content/ or apps/qione/content/
> old leftovers       -> archive/
> ```
> 
> That’s the whole thing. No guess room.
> 
> If you want, next I’ll turn this into a **second CSV with columns `current_path,target_path,action,module,reason`** so you can mass-migrate the existing repo without thinking.

### User
> no need just give me the complete csv including files i mean i want no guessing.

### Assistant
> Yep. Here’s the **locked target architecture as CSV**.
> 
> This is a **canonical target-state CSV**, not a forensic dump of every old file currently floating around your repo. That would be fake precision. This gives you the **exact approved structure to build toward**, including folders and baseline files, so there’s no freestyle nonsense.
> 
> ## Columns
> - `path`
> - `type`
> - `parent`
> - `layer`
> - `module`
> - `required`
> - `purpose`
> 
> ```csv
> path,type,parent,layer,module,required,purpose
> QiOne_Organism,directory,,root,root,yes,canonical repository root
> 
> .github,directory,QiOne_Organism,root,repo,yes,github metadata and automation
> .github/workflows,directory,.github,root,repo,yes,ci and automation workflows
> .github/ISSUE_TEMPLATE,directory,.github,root,repo,no,issue templates
> 
> apps,directory,QiOne_Organism,experience,root,yes,application layer
> apps/qione,directory,apps,experience,qione,yes,primary authenticated operating app
> apps/qione/package.json,file,apps/qione,experience,qione,yes,app package manifest
> apps/qione/tsconfig.json,file,apps/qione,experience,qione,yes,typescript config
> apps/qione/next.config.mjs,file,apps/qione,experience,qione,yes,next config
> apps/qione/middleware.ts,file,apps/qione,experience,qione,yes,auth and request middleware
> apps/qione/README.md,file,apps/qione,experience,qione,yes,app readme
> apps/qione/.env.example,file,apps/qione,experience,qione,yes,environment variable template
> 
> apps/qione/public,directory,apps/qione,experience,qione,yes,public static assets
> apps/qione/public/favicon.ico,file,apps/qione/public,experience,qione,yes,favicon
> apps/qione/public/icons,directory,apps/qione/public,experience,qione,yes,icon assets
> apps/qione/public/images,directory,apps/qione/public,experience,qione,yes,image assets
> 
> apps/qione/src,directory,apps/qione,experience,qione,yes,source root
> apps/qione/src/app,directory,apps/qione/src,experience,qione,yes,route layer
> apps/qione/src/components,directory,apps/qione/src,experience,qione,yes,reusable ui layer
> apps/qione/src/features,directory,apps/qione/src,experience,qione,yes,module logic layer
> apps/qione/src/lib,directory,apps/qione/src,experience,qione,yes,cross-cutting services
> apps/qione/src/types,directory,apps/qione/src,experience,qione,yes,shared types
> apps/qione/src/styles,directory,apps/qione/src,experience,qione,yes,styles
> apps/qione/src/styles/globals.css,file,apps/qione/src/styles,experience,qione,yes,global stylesheet
> 
> apps/qione/src/app/(public),directory,apps/qione/src/app,experience,public,yes,unauthenticated routes
> apps/qione/src/app/(public)/login,directory,apps/qione/src/app/(public),experience,public,yes,login route
> apps/qione/src/app/(public)/login/page.tsx,file,apps/qione/src/app/(public)/login,experience,public,yes,login page
> apps/qione/src/app/(public)/invite,directory,apps/qione/src/app/(public),experience,public,no,invite route
> apps/qione/src/app/(public)/invite/page.tsx,file,apps/qione/src/app/(public)/invite,experience,public,no,invite page
> apps/qione/src/app/(public)/reset-password,directory,apps/qione/src/app/(public),experience,public,no,password reset route
> apps/qione/src/app/(public)/reset-password/page.tsx,file,apps/qione/src/app/(public)/reset-password,experience,public,no,password reset page
> 
> apps/qione/src/app/(app),directory,apps/qione/src/app,experience,qione,yes,authenticated route group
> apps/qione/src/app/(app)/layout.tsx,file,apps/qione/src/app/(app),experience,qione,yes,authenticated app shell layout
> apps/qione/src/app/(app)/page.tsx,file,apps/qione/src/app/(app),experience,dashboard,yes,authenticated home dashboard
> 
> apps/qione/src/app/(app)/dashboard,directory,apps/qione/src/app/(app),experience,dashboard,yes,dashboard routes
> apps/qione/src/app/(app)/dashboard/page.tsx,file,apps/qione/src/app/(app)/dashboard,experience,dashboard,yes,dashboard landing page
> 
> apps/qione/src/app/(app)/ai,directory,apps/qione/src/app/(app),experience,ai,yes,ai routes
> apps/qione/src/app/(app)/ai/page.tsx,file,apps/qione/src/app/(app)/ai,experience,ai,yes,ai home
> apps/qione/src/app/(app)/ai/agents,directory,apps/qione/src/app/(app)/ai,experience,ai,no,agent runner routes
> apps/qione/src/app/(app)/ai/agents/page.tsx,file,apps/qione/src/app/(app)/ai/agents,experience,ai,no,agents page
> apps/qione/src/app/(app)/ai/memory,directory,apps/qione/src/app/(app)/ai,experience,ai,no,memory search routes
> apps/qione/src/app/(app)/ai/memory/page.tsx,file,apps/qione/src/app/(app)/ai/memory,experience,ai,no,memory page
> apps/qione/src/app/(app)/ai/prompts,directory,apps/qione/src/app/(app)/ai,experience,ai,no,prompt management routes
> apps/qione/src/app/(app)/ai/prompts/page.tsx,file,apps/qione/src/app/(app)/ai/prompts,experience,ai,no,prompts page
> apps/qione/src/app/(app)/ai/automations,directory,apps/qione/src/app/(app)/ai,experience,ai,no,automation routes
> apps/qione/src/app/(app)/ai/automations/page.tsx,file,apps/qione/src/app/(app)/ai/automations,experience,ai,no,automations page
> 
> apps/qione/src/app/(app)/documents,directory,apps/qione/src/app/(app),experience,documents,yes,document routes
> apps/qione/src/app/(app)/documents/page.tsx,file,apps/qione/src/app/(app)/documents,experience,documents,yes,documents landing page
> apps/qione/src/app/(app)/documents/inbox,directory,apps/qione/src/app/(app)/documents,experience,documents,no,document inbox route
> apps/qione/src/app/(app)/documents/inbox/page.tsx,file,apps/qione/src/app/(app)/documents/inbox,experience,documents,no,document inbox page
> apps/qione/src/app/(app)/documents/search,directory,apps/qione/src/app/(app)/documents,experience,documents,no,document search route
> apps/qione/src/app/(app)/documents/search/page.tsx,file,apps/qione/src/app/(app)/documents/search,experience,documents,no,document search page
> apps/qione/src/app/(app)/documents/tags,directory,apps/qione/src/app/(app)/documents,experience,documents,no,document tags route
> apps/qione/src/app/(app)/documents/tags/page.tsx,file,apps/qione/src/app/(app)/documents/tags,experience,documents,no,document tags page
> apps/qione/src/app/(app)/documents/[id],directory,apps/qione/src/app/(app)/documents,experience,documents,no,document detail route
> apps/qione/src/app/(app)/documents/[id]/page.tsx,file,apps/qione/src/app/(app)/documents/[id],experience,documents,no,document detail page
> 
> apps/qione/src/app/(app)/chronicle,directory,apps/qione/src/app/(app),experience,chronicle,yes,chronicle routes
> apps/qione/src/app/(app)/chronicle/page.tsx,file,apps/qione/src/app/(app)/chronicle,experience,chronicle,yes,chronicle landing page
> apps/qione/src/app/(app)/chronicle/[id],directory,apps/qione/src/app/(app)/chronicle,experience,chronicle,no,chronicle detail route
> apps/qione/src/app/(app)/chronicle/[id]/page.tsx,file,apps/qione/src/app/(app)/chronicle/[id],experience,chronicle,no,chronicle detail page
> 
> apps/qione/src/app/(app)/notes,directory,apps/qione/src/app/(app),experience,notes,yes,notes routes
> apps/qione/src/app/(app)/notes/page.tsx,file,apps/qione/src/app/(app)/notes,experience,notes,yes,notes landing page
> apps/qione/src/app/(app)/notes/new,directory,apps/qione/src/app/(app)/notes,experience,notes,no,new note route
> apps/qione/src/app/(app)/notes/new/page.tsx,file,apps/qione/src/app/(app)/notes/new,experience,notes,no,new note page
> apps/qione/src/app/(app)/notes/[id],directory,apps/qione/src/app/(app)/notes,experience,notes,no,note detail route
> apps/qione/src/app/(app)/notes/[id]/page.tsx,file,apps/qione/src/app/(app)/notes/[id],experience,notes,no,note detail page
> 
> apps/qione/src/app/(app)/objects,directory,apps/qione/src/app/(app),experience,objects,yes,objects routes
> apps/qione/src/app/(app)/objects/page.tsx,file,apps/qione/src/app/(app)/objects,experience,objects,yes,objects landing page
> apps/qione/src/app/(app)/objects/contacts,directory,apps/qione/src/app/(app)/objects,experience,objects,no,contacts routes
> apps/qione/src/app/(app)/objects/contacts/page.tsx,file,apps/qione/src/app/(app)/objects/contacts,experience,objects,no,contacts list page
> apps/qione/src/app/(app)/objects/contacts/[id],directory,apps/qione/src/app/(app)/objects/contacts,experience,objects,no,contact detail route
> apps/qione/src/app/(app)/objects/contacts/[id]/page.tsx,file,apps/qione/src/app/(app)/objects/contacts/[id],experience,objects,no,contact detail page
> apps/qione/src/app/(app)/objects/clients,directory,apps/qione/src/app/(app)/objects,experience,objects,no,clients routes
> apps/qione/src/app/(app)/objects/clients/page.tsx,file,apps/qione/src/app/(app)/objects/clients,experience,objects,no,clients list page
> apps/qione/src/app/(app)/objects/clients/[id],directory,apps/qione/src/app/(app)/objects/clients,experience,objects,no,client detail route
> apps/qione/src/app/(app)/objects/clients/[id]/page.tsx,file,apps/qione/src/app/(app)/objects/clients/[id],experience,objects,no,client detail page
> apps/qione/src/app/(app)/objects/cases,directory,apps/qione/src/app/(app)/objects,experience,objects,no,cases routes
> apps/qione/src/app/(app)/objects/cases/page.tsx,file,apps/qione/src/app/(app)/objects/cases,experience,objects,no,cases list page
> apps/qione/src/app/(app)/objects/cases/[id],directory,apps/qione/src/app/(app)/objects/cases,experience,objects,no,case detail route
> apps/qione/src/app/(app)/objects/cases/[id]/page.tsx,file,apps/qione/src/app/(app)/objects/cases/[id],experience,objects,no,case detail page
> apps/qione/src/app/(app)/objects/tasks,directory,apps/qione/src/app/(app)/objects,experience,objects,no,tasks routes
> apps/qione/src/app/(app)/objects/tasks/page.tsx,file,apps/qione/src/app/(app)/objects/tasks,experience,objects,no,tasks list page
> apps/qione/src/app/(app)/objects/expenses,directory,apps/qione/src/app/(app)/objects,experience,objects,no,expenses routes
> apps/qione/src/app/(app)/objects/expenses/page.tsx,file,apps/qione/src/app/(app)/objects/expenses,experience,objects,no,expenses list page
> apps/qione/src/app/(app)/objects/appointments,directory,apps/qione/src/app/(app)/objects,experience,objects,no,appointments routes
> apps/qione/src/app/(app)/objects/appointments/page.tsx,file,apps/qione/src/app/(app)/objects/appointments,experience,objects,no,appointments list page
> 
> apps/qione/src/app/(app)/forms,directory,apps/qione/src/app/(app),experience,forms,yes,forms routes
> apps/qione/src/app/(app)/forms/page.tsx,file,apps/qione/src/app/(app)/forms,experience,forms,yes,forms landing page
> apps/qione/src/app/(app)/forms/[formKey],directory,apps/qione/src/app/(app)/forms,experience,forms,no,form renderer route
> apps/qione/src/app/(app)/forms/[formKey]/page.tsx,file,apps/qione/src/app/(app)/forms/[formKey],experience,forms,no,form renderer page
> 
> apps/qione/src/app/(app)/contracts,directory,apps/qione/src/app/(app),experience,contracts,yes,contracts routes
> apps/qione/src/app/(app)/contracts/page.tsx,file,apps/qione/src/app/(app)/contracts,experience,contracts,yes,contracts landing page
> apps/qione/src/app/(app)/contracts/[id],directory,apps/qione/src/app/(app)/contracts,experience,contracts,no,contract detail route
> apps/qione/src/app/(app)/contracts/[id]/page.tsx,file,apps/qione/src/app/(app)/contracts/[id],experience,contracts,no,contract detail page
> 
> apps/qione/src/app/(app)/tax,directory,apps/qione/src/app/(app),experience,tax,yes,tax routes
> apps/qione/src/app/(app)/tax/page.tsx,file,apps/qione/src/app/(app)/tax,experience,tax,yes,tax landing page
> apps/qione/src/app/(app)/tax/returns,directory,apps/qione/src/app/(app)/tax,experience,tax,no,tax returns routes
> apps/qione/src/app/(app)/tax/returns/page.tsx,file,apps/qione/src/app/(app)/tax/returns,experience,tax,no,tax returns page
> apps/qione/src/app/(app)/tax/organizers,directory,apps/qione/src/app/(app)/tax,experience,tax,no,tax organizers routes
> apps/qione/src/app/(app)/tax/organizers/page.tsx,file,apps/qione/src/app/(app)/tax/organizers,experience,tax,no,tax organizers page
> apps/qione/src/app/(app)/tax/clients,directory,apps/qione/src/app/(app)/tax,experience,tax,no,tax clients routes
> apps/qione/src/app/(app)/tax/clients/page.tsx,file,apps/qione/src/app/(app)/tax/clients,experience,tax,no,tax clients page
> 
> apps/qione/src/app/(app)/care,directory,apps/qione/src/app/(app),experience,care,yes,care routes
> apps/qione/src/app/(app)/care/page.tsx,file,apps/qione/src/app/(app)/care,experience,care,yes,care landing page
> apps/qione/src/app/(app)/care/patients,directory,apps/qione/src/app/(app)/care,experience,care,no,patients routes
> apps/qione/src/app/(app)/care/patients/page.tsx,file,apps/qione/src/app/(app)/care/patients,experience,care,no,patients page
> apps/qione/src/app/(app)/care/meds,directory,apps/qione/src/app/(app)/care,experience,care,no,meds routes
> apps/qione/src/app/(app)/care/meds/page.tsx,file,apps/qione/src/app/(app)/care/meds,experience,care,no,meds page
> apps/qione/src/app/(app)/care/supplies,directory,apps/qione/src/app/(app)/care,experience,care,no,supplies routes
> apps/qione/src/app/(app)/care/supplies/page.tsx,file,apps/qione/src/app/(app)/care/supplies,experience,care,no,supplies page
> 
> apps/qione/src/app/(app)/settings,directory,apps/qione/src/app/(app),experience,settings,yes,settings routes
> apps/qione/src/app/(app)/settings/page.tsx,file,apps/qione/src/app/(app)/settings,experience,settings,yes,settings landing page
> apps/qione/src/app/(app)/settings/profile,directory,apps/qione/src/app/(app)/settings,experience,settings,no,profile settings route
> apps/qione/src/app/(app)/settings/profile/page.tsx,file,apps/qione/src/app/(app)/settings/profile,experience,settings,no,profile settings page
> apps/qione/src/app/(app)/settings/notifications,directory,apps/qione/src/app/(app)/settings,experience,settings,no,notification settings route
> apps/qione/src/app/(app)/settings/notifications/page.tsx,file,apps/qione/src/app/(app)/settings/notifications,experience,settings,no,notification settings page
> apps/qione/src/app/(app)/settings/connections,directory,apps/qione/src/app/(app)/settings,experience,settings,no,connection settings route
> apps/qione/src/app/(app)/settings/connections/page.tsx,file,apps/qione/src/app/(app)/settings/connections,experience,settings,no,connection settings page
> 
> apps/qione/src/app/(app)/admin,directory,apps/qione/src/app/(app),experience,admin,yes,admin routes
> apps/qione/src/app/(app)/admin/page.tsx,file,apps/qione/src/app/(app)/admin,experience,admin,yes,admin landing page
> apps/qione/src/app/(app)/admin/users,directory,apps/qione/src/app/(app)/admin,experience,admin,no,user admin route
> apps/qione/src/app/(app)/admin/users/page.tsx,file,apps/qione/src/app/(app)/admin/users,experience,admin,no,user admin page
> apps/qione/src/app/(app)/admin/roles,directory,apps/qione/src/app/(app)/admin,experience,admin,no,role admin route
> apps/qione/src/app/(app)/admin/roles/page.tsx,file,apps/qione/src/app/(app)/admin/roles,experience,admin,no,role admin page
> apps/qione/src/app/(app)/admin/permissions,directory,apps/qione/src/app/(app)/admin,experience,admin,no,permissions admin route
> apps/qione/src/app/(app)/admin/permissions/page.tsx,file,apps/qione/src/app/(app)/admin/permissions,experience,admin,no,permissions admin page
> apps/qione/src/app/(app)/admin/audit,directory,apps/qione/src/app/(app)/admin,experience,admin,no,audit route
> apps/qione/src/app/(app)/admin/audit/page.tsx,file,apps/qione/src/app/(app)/admin/audit,experience,admin,no,audit page
> apps/qione/src/app/(app)/admin/system,directory,apps/qione/src/app/(app)/admin,experience,admin,no,system route
> apps/qione/src/app/(app)/admin/system/page.tsx,file,apps/qione/src/app/(app)/admin/system,experience,admin,no,system page
> apps/qione/src/app/(app)/admin/workers,directory,apps/qione/src/app/(app)/admin,experience,admin,no,worker status route
> apps/qione/src/app/(app)/admin/workers/page.tsx,file,apps/qione/src/app/(app)/admin/workers,experience,admin,no,worker status page
> 
> apps/qione/src/app/api,directory,apps/qione/src/app,experience,api,yes,route handlers
> apps/qione/src/app/api/ai,directory,apps/qione/src/app/api,experience,ai,yes,ai route handlers
> apps/qione/src/app/api/ai/chat,directory,apps/qione/src/app/api/ai,experience,ai,no,chat api
> apps/qione/src/app/api/ai/chat/route.ts,file,apps/qione/src/app/api/ai/chat,experience,ai,no,chat route handler
> apps/qione/src/app/api/ai/memory,directory,apps/qione/src/app/api/ai,experience,ai,no,memory api
> apps/qione/src/app/api/ai/memory/route.ts,file,apps/qione/src/app/api/ai/memory,experience,ai,no,memory route handler
> 
> apps/qione/src/app/api/documents,directory,apps/qione/src/app/api,experience,documents,yes,document route handlers
> apps/qione/src/app/api/documents/search,directory,apps/qione/src/app/api/documents,experience,documents,no,document search api
> apps/qione/src/app/api/documents/search/route.ts,file,apps/qione/src/app/api/documents/search,experience,documents,no,document search route
> apps/qione/src/app/api/documents/upload,directory,apps/qione/src/app/api/documents,experience,documents,no,document upload api
> apps/qione/src/app/api/documents/upload/route.ts,file,apps/qione/src/app/api/documents/upload,experience,documents,no,document upload route
> 
> apps/qione/src/app/api/chronicle,directory,apps/qione/src/app/api,experience,chronicle,yes,chronicle route handlers
> apps/qione/src/app/api/chronicle/route.ts,file,apps/qione/src/app/api/chronicle,experience,chronicle,no,chronicle collection route
> apps/qione/src/app/api/chronicle/[id],directory,apps/qione/src/app/api/chronicle,experience,chronicle,no,chronicle item api
> apps/qione/src/app/api/chronicle/[id]/route.ts,file,apps/qione/src/app/api/chronicle/[id],experience,chronicle,no,chronicle item route
> 
> apps/qione/src/app/api/notes,directory,apps/qione/src/app/api,experience,notes,yes,notes route handlers
> apps/qione/src/app/api/notes/route.ts,file,apps/qione/src/app/api/notes,experience,notes,no,notes collection route
> apps/qione/src/app/api/notes/[id],directory,apps/qione/src/app/api/notes,experience,notes,no,note item api
> apps/qione/src/app/api/notes/[id]/route.ts,file,apps/qione/src/app/api/notes/[id],experience,notes,no,note item route
> 
> apps/qione/src/app/api/objects,directory,apps/qione/src/app/api,experience,objects,yes,object route handlers
> apps/qione/src/app/api/objects/[objectType],directory,apps/qione/src/app/api/objects,experience,objects,no,object collection api
> apps/qione/src/app/api/objects/[objectType]/route.ts,file,apps/qione/src/app/api/objects/[objectType],experience,objects,no,object collection route
> apps/qione/src/app/api/objects/[objectType]/[id],directory,apps/qione/src/app/api/objects/[objectType],experience,objects,no,object item api
> apps/qione/src/app/api/objects/[objectType]/[id]/route.ts,file,apps/qione/src/app/api/objects/[objectType]/[id],experience,objects,no,object item route
> 
> apps/qione/src/app/api/forms,directory,apps/qione/src/app/api,experience,forms,yes,forms route handlers
> apps/qione/src/app/api/forms/[formKey],directory,apps/qione/src/app/api/forms,experience,forms,no,form route
> apps/qione/src/app/api/forms/[formKey]/route.ts,file,apps/qione/src/app/api/forms/[formKey],experience,forms,no,form route handler
> 
> apps/qione/src/app/api/contracts,directory,apps/qione/src/app/api,experience,contracts,yes,contracts route handlers
> apps/qione/src/app/api/contracts/route.ts,file,apps/qione/src/app/api/contracts,experience,contracts,no,contracts collection route
> 
> apps/qione/src/app/api/tax,directory,apps/qione/src/app/api,experience,tax,yes,tax route handlers
> apps/qione/src/app/api/tax/route.ts,file,apps/qione/src/app/api/tax,experience,tax,no,tax collection route
> 
> apps/qione/src/app/api/care,directory,apps/qione/src/app/api,experience,care,yes,care route handlers
> apps/qione/src/app/api/care/route.ts,file,apps/qione/src/app/api/care,experience,care,no,care collection route
> 
> apps/qione/src/app/api/admin,directory,apps/qione/src/app/api,experience,admin,yes,admin route handlers
> apps/qione/src/app/api/admin/worker-health,directory,apps/qione/src/app/api/admin,experience,admin,no,worker health api
> apps/qione/src/app/api/admin/worker-health/route.ts,file,apps/qione/src/app/api/admin/worker-health,experience,admin,no,worker health route
> apps/qione/src/app/api/admin/queue-status,directory,apps/qione/src/app/api/admin,experience,admin,no,queue status api
> apps/qione/src/app/api/admin/queue-status/route.ts,file,apps/qione/src/app/api/admin/queue-status,experience,admin,no,queue status route
> 
> apps/qione/src/app/api/webhooks,directory,apps/qione/src/app/api,experience,webhooks,yes,external webhooks
> apps/qione/src/app/api/webhooks/stripe,directory,apps/qione/src/app/api/webhooks,experience,webhooks,no,stripe webhook
> apps/qione/src/app/api/webhooks/stripe/route.ts,file,apps/qione/src/app/api/webhooks/stripe,experience,webhooks,no,stripe webhook route
> 
> apps/qione/src/components/layout,directory,apps/qione/src/components,experience,layout,yes,application shell components
> apps/qione/src/components/layout/AppShell.tsx,file,apps/qione/src/components/layout,experience,layout,yes,app shell wrapper
> apps/qione/src/components/layout/Sidebar.tsx,file,apps/qione/src/components/layout,experience,layout,yes,main sidebar
> apps/qione/src/components/layout/Topbar.tsx,file,apps/qione/src/components/layout,experience,layout,yes,top navigation
> apps/qione/src/components/layout/Breadcrumbs.tsx,file,apps/qione/src/components/layout,experience,layout,no,breadcrumb navigation
> 
> apps/qione/src/components/ui,directory,apps/qione/src/components,experience,ui,yes,primitive ui components
> apps/qione/src/components/ui/button.tsx,file,apps/qione/src/components/ui,experience,ui,yes,button primitive
> apps/qione/src/components/ui/card.tsx,file,apps/qione/src/components/ui,experience,ui,yes,card primitive
> apps/qione/src/components/ui/dialog.tsx,file,apps/qione/src/components/ui,experience,ui,yes,dialog primitive
> apps/qione/src/components/ui/input.tsx,file,apps/qione/src/components/ui,experience,ui,yes,input primitive
> apps/qione/src/components/ui/table.tsx,file,apps/qione/src/components/ui,experience,ui,no,table primitive
> apps/qione/src/components/ui/tabs.tsx,file,apps/qione/src/components/ui,experience,ui,no,tabs primitive
> apps/qione/src/components/ui/textarea.tsx,file,apps/qione/src/components/ui,experience,ui,no,textarea primitive
> 
> apps/qione/src/components/ai,directory,apps/qione/src/components,experience,ai,yes,ai ui components
> apps/qione/src/components/ai/ChatPanel.tsx,file,apps/qione/src/components/ai,experience,ai,no,chat interface
> apps/qione/src/components/ai/PromptEditor.tsx,file,apps/qione/src/components/ai,experience,ai,no,prompt editor
> apps/qione/src/components/ai/MemoryResultCard.tsx,file,apps/qione/src/components/ai,experience,ai,no,memory search result card
> 
> apps/qione/src/components/documents,directory,apps/qione/src/components,experience,documents,yes,document ui components
> apps/qione/src/components/documents/DocumentCard.tsx,file,apps/qione/src/components/documents,experience,documents,no,document summary card
> apps/qione/src/components/documents/DocumentViewer.tsx,file,apps/qione/src/components/documents,experience,documents,no,document viewer
> apps/qione/src/components/documents/UploadPanel.tsx,file,apps/qione/src/components/documents,experience,documents,no,upload interface
> 
> apps/qione/src/components/chronicle,directory,apps/qione/src/components,experience,chronicle,yes,chronicle ui components
> apps/qione/src/components/chronicle/TimelineView.tsx,file,apps/qione/src/components/chronicle,experience,chronicle,no,timeline visualization
> apps/qione/src/components/chronicle/EventCard.tsx,file,apps/qione/src/components/chronicle,experience,chronicle,no,event card
> 
> apps/qione/src/components/notes,directory,apps/qione/src/components,experience,notes,yes,notes ui components
> apps/qione/src/components/notes/NoteEditor.tsx,file,apps/qione/src/components/notes,experience,notes,no,note editor
> apps/qione/src/components/notes/NoteCard.tsx,file,apps/qione/src/components/notes,experience,notes,no,note card
> 
> apps/qione/src/components/objects,directory,apps/qione/src/components,experience,objects,yes,objects ui components
> apps/qione/src/components/objects/ObjectTable.tsx,file,apps/qione/src/components/objects,experience,objects,no,object table
> apps/qione/src/components/objects/ObjectDetail.tsx,file,apps/qione/src/components/objects,experience,objects,no,object detail panel
> 
> apps/qione/src/components/forms,directory,apps/qione/src/components,experience,forms,yes,forms ui components
> apps/qione/src/components/forms/FormRenderer.tsx,file,apps/qione/src/components/forms,experience,forms,no,form renderer
> apps/qione/src/components/forms/FieldRenderer.tsx,file,apps/qione/src/components/forms,experience,forms,no,field renderer
> 
> apps/qione/src/components/contracts,directory,apps/qione/src/components,experience,contracts,yes,contracts ui components
> apps/qione/src/components/contracts/ContractViewer.tsx,file,apps/qione/src/components/contracts,experience,contracts,no,contract viewer
> 
> apps/qione/src/components/tax,directory,apps/qione/src/components,experience,tax,yes,tax ui components
> apps/qione/src/components/tax/ReturnCard.tsx,file,apps/qione/src/components/tax,experience,tax,no,tax return card
> 
> apps/qione/src/components/care,directory,apps/qione/src/components,experience,care,yes,care ui components
> apps/qione/src/components/care/MedicationCard.tsx,file,apps/qione/src/components/care,experience,care,no,medication card
> apps/qione/src/components/care/SupplyTable.tsx,file,apps/qione/src/components/care,experience,care,no,supply table
> 
> apps/qione/src/components/settings,directory,apps/qione/src/components,experience,settings,yes,settings ui components
> apps/qione/src/components/settings/ConnectionCard.tsx,file,apps/qione/src/components/settings,experience,settings,no,connection card
> 
> apps/qione/src/components/admin,directory,apps/qione/src/components,experience,admin,yes,admin ui components
> apps/qione/src/components/admin/PermissionMatrix.tsx,file,apps/qione/src/components/admin,experience,admin,no,permissions matrix
> apps/qione/src/components/admin/WorkerStatusTable.tsx,file,apps/qione/src/components/admin,experience,admin,no,worker status table
> 
> apps/qione/src/features/dashboard,directory,apps/qione/src/features,domain,dashboard,yes,dashboard feature
> apps/qione/src/features/dashboard/client,directory,apps/qione/src/features/dashboard,domain,dashboard,yes,client-side logic
> apps/qione/src/features/dashboard/server,directory,apps/qione/src/features/dashboard,domain,dashboard,yes,server-side logic
> apps/qione/src/features/dashboard/schemas,directory,apps/qione/src/features/dashboard,domain,dashboard,yes,validation schemas
> apps/qione/src/features/dashboard/utils.ts,file,apps/qione/src/features/dashboard,domain,dashboard,no,dashboard helpers
> 
> apps/qione/src/features/ai,directory,apps/qione/src/features,domain,ai,yes,ai feature
> apps/qione/src/features/ai/client,directory,apps/qione/src/features/ai,domain,ai,yes,client-side ai logic
> apps/qione/src/features/ai/server,directory,apps/qione/src/features/ai,domain,ai,yes,server-side ai logic
> apps/qione/src/features/ai/schemas,directory,apps/qione/src/features/ai,domain,ai,yes,ai schemas
> apps/qione/src/features/ai/prompts,directory,apps/qione/src/features/ai,domain,ai,no,ai prompt assets
> apps/qione/src/features/ai/tools,directory,apps/qione/src/features/ai,domain,ai,no,ai tool adapters
> apps/qione/src/features/ai/utils.ts,file,apps/qione/src/features/ai,domain,ai,no,ai helpers
> 
> apps/qione/src/features/documents,directory,apps/qione/src/features,domain,documents,yes,documents feature
> apps/qione/src/features/documents/client,directory,apps/qione/src/features/documents,domain,documents,yes,client-side document logic
> apps/qione/src/features/documents/server,directory,apps/qione/src/features/documents,domain,documents,yes,server-side document logic
> apps/qione/src/features/documents/schemas,directory,apps/qione/src/features/documents,domain,documents,yes,document schemas
> apps/qione/src/features/documents/qinode,directory,apps/qione/src/features/documents,domain,documents,yes,qinode protocol implementation
> apps/qione/src/features/documents/qinode/dna,directory,apps/qione/src/features/documents/qinode,domain,documents,yes,node identity logic
> apps/qione/src/features/documents/qinode/lineage,directory,apps/qione/src/features/documents/qinode,domain,documents,yes,node lineage logic
> apps/qione/src/features/documents/qinode/parser,directory,apps/qione/src/features/documents/qinode,domain,documents,yes,node parsing logic
> apps/qione/src/features/documents/qinode/serializer,directory,apps/qione/src/features/documents/qinode,domain,documents,yes,node writing logic
> apps/qione/src/features/documents/qinode/reconstruction,directory,apps/qione/src/features/documents/qinode,domain,documents,yes,node rebuild logic
> apps/qione/src/features/documents/qinode/registry,directory,apps/qione/src/features/documents/qinode,domain,documents,yes,node registry helpers
> apps/qione/src/features/documents/utils.ts,file,apps/qione/src/features/documents,domain,documents,no,document helpers
> 
> apps/qione/src/features/chronicle,directory,apps/qione/src/features,domain,chronicle,yes,chronicle feature
> apps/qione/src/features/chronicle/client,directory,apps/qione/src/features/chronicle,domain,chronicle,yes,client-side chronicle logic
> apps/qione/src/features/chronicle/server,directory,apps/qione/src/features/chronicle,domain,chronicle,yes,server-side chronicle logic
> apps/qione/src/features/chronicle/schemas,directory,apps/qione/src/features/chronicle,domain,chronicle,yes,chronicle schemas
> apps/qione/src/features/chronicle/timeline,directory,apps/qione/src/features/chronicle,domain,chronicle,no,timeline helpers
> apps/qione/src/features/chronicle/utils.ts,file,apps/qione/src/features/chronicle,domain,chronicle,no,chronicle helpers
> 
> apps/qione/src/features/notes,directory,apps/qione/src/features,domain,notes,yes,notes feature
> apps/qione/src/features/notes/client,directory,apps/qione/src/features/notes,domain,notes,yes,client-side notes logic
> apps/qione/src/features/notes/server,directory,apps/qione/src/features/notes,domain,notes,yes,server-side notes logic
> apps/qione/src/features/notes/schemas,directory,apps/qione/src/features/notes,domain,notes,yes,notes schemas
> apps/qione/src/features/notes/journal,directory,apps/qione/src/features/notes,domain,notes,no,journal subdomain logic
> apps/qione/src/features/notes/stories,directory,apps/qione/src/features/notes,domain,notes,no,stories subdomain logic
> apps/qione/src/features/notes/utils.ts,file,apps/qione/src/features/notes,domain,notes,no,notes helpers
> 
> apps/qione/src/features/objects,directory,apps/qione/src/features,domain,objects,yes,objects feature
> apps/qione/src/features/objects/client,directory,apps/qione/src/features/objects,domain,objects,yes,client-side objects logic
> apps/qione/src/features/objects/server,directory,apps/qione/src/features/objects,domain,objects,yes,server-side objects logic
> apps/qione/src/features/objects/schemas,directory,apps/qione/src/features/objects,domain,objects,yes,object schemas
> apps/qione/src/features/objects/registry,directory,apps/qione/src/features/objects,domain,objects,no,entity registry logic
> apps/qione/src/features/objects/utils.ts,file,apps/qione/src/features/objects,domain,objects,no,object helpers
> 
> apps/qione/src/features/forms,directory,apps/qione/src/features,domain,forms,yes,forms feature
> apps/qione/src/features/forms/client,directory,apps/qione/src/features/forms,domain,forms,yes,client-side forms logic
> apps/qione/src/features/forms/server,directory,apps/qione/src/features/forms,domain,forms,yes,server-side forms logic
> apps/qione/src/features/forms/schemas,directory,apps/qione/src/features/forms,domain,forms,yes,form schemas
> apps/qione/src/features/forms/registry,directory,apps/qione/src/features/forms,domain,forms,no,form registry logic
> apps/qione/src/features/forms/utils.ts,file,apps/qione/src/features/forms,domain,forms,no,form helpers
> 
> apps/qione/src/features/contracts,directory,apps/qione/src/features,domain,contracts,yes,contracts feature
> apps/qione/src/features/contracts/client,directory,apps/qione/src/features/contracts,domain,contracts,yes,client-side contract logic
> apps/qione/src/features/contracts/server,directory,apps/qione/src/features/contracts,domain,contracts,yes,server-side contract logic
> apps/qione/src/features/contracts/schemas,directory,apps/qione/src/features/contracts,domain,contracts,yes,contract schemas
> apps/qione/src/features/contracts/utils.ts,file,apps/qione/src/features/contracts,domain,contracts,no,contract helpers
> 
> apps/qione/src/features/tax,directory,apps/qione/src/features,domain,tax,yes,tax feature
> apps/qione/src/features/tax/client,directory,apps/qione/src/features/tax,domain,tax,yes,client-side tax logic
> apps/qione/src/features/tax/server,directory,apps/qione/src/features/tax,domain,tax,yes,server-side tax logic
> apps/qione/src/features/tax/schemas,directory,apps/qione/src/features/tax,domain,tax,yes,tax schemas
> apps/qione/src/features/tax/returns,directory,apps/qione/src/features/tax,domain,tax,no,returns subdomain logic
> apps/qione/src/features/tax/organizers,directory,apps/qione/src/features/tax,domain,tax,no,organizers subdomain logic
> apps/qione/src/features/tax/utils.ts,file,apps/qione/src/features/tax,domain,tax,no,tax helpers
> 
> apps/qione/src/features/care,directory,apps/qione/src/features,domain,care,yes,care feature
> apps/qione/src/features/care/client,directory,apps/qione/src/features/care,domain,care,yes,client-side care logic
> apps/qione/src/features/care/server,directory,apps/qione/src/features/care,domain,care,yes,server-side care logic
> apps/qione/src/features/care/schemas,directory,apps/qione/src/features/care,domain,care,yes,care schemas
> apps/qione/src/features/care/meds,directory,apps/qione/src/features/care,domain,care,no,medication subdomain logic
> apps/qione/src/features/care/supplies,directory,apps/qione/src/features/care,domain,care,no,supplies subdomain logic
> apps/qione/src/features/care/utils.ts,file,apps/qione/src/features/care,domain,care,no,care helpers
> 
> apps/qione/src/features/settings,directory,apps/qione/src/features,domain,settings,yes,settings feature
> apps/qione/src/features/settings/client,directory,apps/qione/src/features/settings,domain,settings,yes,client-side settings logic
> apps/qione/src/features/settings/server,directory,apps/qione/src/features/settings,domain,settings,yes,server-side settings logic
> apps/qione/src/features/settings/schemas,directory,apps/qione/src/features/settings,domain,settings,yes,settings schemas
> apps/qione/src/features/settings/utils.ts,file,apps/qione/src/features/settings,domain,settings,no,settings helpers
> 
> apps/qione/src/features/admin,directory,apps/qione/src/features,domain,admin,yes,admin feature
> apps/qione/src/features/admin/client,directory,apps/qione/src/features/admin,domain,admin,yes,client-side admin logic
> apps/qione/src/features/admin/server,directory,apps/qione/src/features/admin,domain,admin,yes,server-side admin logic
> apps/qione/src/features/admin/schemas,directory,apps/qione/src/features/admin,domain,admin,yes,admin schemas
> apps/qione/src/features/admin/permissions,directory,apps/qione/src/features/admin,domain,admin,no,permissions subdomain logic
> apps/qione/src/features/admin/workers,directory,apps/qione/src/features/admin,domain,admin,no,worker monitoring logic
> apps/qione/src/features/admin/utils.ts,file,apps/qione/src/features/admin,domain,admin,no,admin helpers
> 
> apps/qione/src/lib/auth,directory,apps/qione/src/lib,shared,qione,yes,auth helpers
> apps/qione/src/lib/auth/guards.ts,file,apps/qione/src/lib/auth,shared,qione,no,route and action guards
> apps/qione/src/lib/auth/session.ts,file,apps/qione/src/lib/auth,shared,qione,no,session helpers
> 
> apps/qione/src/lib/db,directory,apps/qione/src/lib,shared,qione,yes,database helpers
> apps/qione/src/lib/db/client.ts,file,apps/qione/src/lib/db,shared,qione,no,db client
> apps/qione/src/lib/db/server.ts,file,apps/qione/src/lib/db,shared,qione,no,server db client
> apps/qione/src/lib/db/queries.ts,file,apps/qione/src/lib/db,shared,qione,no,shared db queries
> 
> apps/qione/src/lib/storage,directory,apps/qione/src/lib,shared,qione,yes,storage helpers
> apps/qione/src/lib/storage/files.ts,file,apps/qione/src/lib/storage,shared,qione,no,file helpers
> apps/qione/src/lib/storage/uploads.ts,file,apps/qione/src/lib/storage,shared,qione,no,upload helpers
> 
> apps/qione/src/lib/ai,directory,apps/qione/src/lib,shared,qione,yes,shared ai helpers
> apps/qione/src/lib/ai/embeddings.ts,file,apps/qione/src/lib/ai,shared,qione,no,embedding helpers
> apps/qione/src/lib/ai/recall.ts,file,apps/qione/src/lib/ai,shared,qione,no,recall helpers
> apps/qione/src/lib/ai/tools.ts,file,apps/qione/src/lib/ai,shared,qione,no,tool helpers
> 
> apps/qione/src/lib/integrations,directory,apps/qione/src/lib,shared,qione,yes,integration helpers
> apps/qione/src/lib/integrations/email.ts,file,apps/qione/src/lib/integrations,shared,qione,no,email integration
> apps/qione/src/lib/integrations/calendar.ts,file,apps/qione/src/lib/integrations,shared,qione,no,calendar integration
> apps/qione/src/lib/integrations/crm.ts,file,apps/qione/src/lib/integrations,shared,qione,no,crm integration
> 
> apps/qione/src/lib/permissions,directory,apps/qione/src/lib,shared,qione,yes,permissions helpers
> apps/qione/src/lib/permissions/roles.ts,file,apps/qione/src/lib/permissions,shared,qione,no,role definitions
> apps/qione/src/lib/permissions/access.ts,file,apps/qione/src/lib/permissions,shared,qione,no,access helpers
> 
> apps/qione/src/lib/utils,directory,apps/qione/src/lib,shared,qione,yes,generic utility helpers
> apps/qione/src/lib/utils/dates.ts,file,apps/qione/src/lib/utils,shared,qione,no,date utilities
> apps/qione/src/lib/utils/money.ts,file,apps/qione/src/lib/utils,shared,qione,no,money utilities
> apps/qione/src/lib/utils/strings.ts,file,apps/qione/src/lib/utils,shared,qione,no,string utilities
> apps/qione/src/lib/utils/ids.ts,file,apps/qione/src/lib/utils,shared,qione,no,id utilities
> apps/qione/src/lib/constants.ts,file,apps/qione/src/lib,shared,qione,no,shared constants
> apps/qione/src/lib/env.ts,file,apps/qione/src/lib,shared,qione,no,environment parsing
> 
> apps/qione/src/types/auth.ts,file,apps/qione/src/types,shared,qione,no,auth types
> apps/qione/src/types/database.ts,file,apps/qione/src/types,shared,qione,no,database types
> apps/qione/src/types/permissions.ts,file,apps/qione/src/types,shared,qione,no,permissions types
> apps/qione/src/types/common.ts,file,apps/qione/src/types,shared,qione,no,common types
> 
> apps/qione/supabase,directory,apps/qione,app_support,qione,yes,app-local sql and seed support
> apps/qione/supabase/module_sql,directory,apps/qione/supabase,app_support,qione,yes,module-level sql helpers
> apps/qione/supabase/seeds,directory,apps/qione/supabase,app_support,qione,yes,app-local seed files
> 
> apps/qione/content,directory,apps/qione,app_support,qione,yes,app-local content
> apps/qione/content/prompts,directory,apps/qione/content,app_support,qione,yes,local prompts
> apps/qione/content/templates,directory,apps/qione/content,app_support,qione,yes,local templates
> apps/qione/content/forms,directory,apps/qione/content,app_support,qione,yes,local form definitions
> apps/qione/content/kb,directory,apps/qione/content,app_support,qione,no,local knowledge fragments
> 
> apps/qione/tests,directory,apps/qione,app_support,qione,yes,tests
> apps/qione/tests/unit,directory,apps/qione/tests,app_support,qione,yes,unit tests
> apps/qione/tests/integration,directory,apps/qione/tests,app_support,qione,yes,integration tests
> apps/qione/tests/e2e,directory,apps/qione/tests,app_support,qione,yes,end-to-end tests
> 
> apps/qione/docs,directory,apps/qione,app_support,qione,yes,app-local docs
> apps/qione/docs/module_maps,directory,apps/qione/docs,app_support,qione,yes,module maps
> apps/qione/docs/route_maps,directory,apps/qione/docs,app_support,qione,yes,route maps
> apps/qione/docs/permissions,directory,apps/qione/docs,app_support,qione,yes,permission docs
> 
> apps/qially-web,directory,apps,experience,qially-web,yes,public web app
> apps/qially-web/package.json,file,apps/qially-web,experience,qially-web,yes,public app package manifest
> apps/qially-web/tsconfig.json,file,apps/qially-web,experience,qially-web,yes,typescript config
> apps/qially-web/README.md,file,apps/qially-web,experience,qially-web,yes,public app readme
> apps/qially-web/.env.example,file,apps/qially-web,experience,qially-web,yes,environment variable template
> apps/qially-web/public,directory,apps/qially-web,experience,qially-web,yes,public assets
> apps/qially-web/src,directory,apps/qially-web,experience,qially-web,yes,source root
> apps/qially-web/src/app,directory,apps/qially-web/src,experience,qially-web,yes,routes
> apps/qially-web/src/components,directory,apps/qially-web/src,experience,qially-web,yes,components
> apps/qially-web/src/content,directory,apps/qially-web/src,experience,qially-web,no,site content
> apps/qially-web/src/lib,directory,apps/qially-web/src,experience,qially-web,yes,helpers
> apps/qially-web/src/styles,directory,apps/qially-web/src,experience,qially-web,yes,styles
> apps/qially-web/src/types,directory,apps/qially-web/src,experience,qially-web,no,types
> 
> packages,directory,QiOne_Organism,shared,root,yes,shared package layer
> packages/qinode,directory,packages,shared,qinode,no,shared qinode package when extraction is real
> packages/qinode/package.json,file,packages/qinode,shared,qinode,no,package manifest
> packages/qinode/README.md,file,packages/qinode,shared,qinode,no,package readme
> packages/qinode/src,directory,packages/qinode,shared,qinode,no,source root
> packages/qinode/src/dna,directory,packages/qinode/src,shared,qinode,no,node identity logic
> packages/qinode/src/lineage,directory,packages/qinode/src,shared,qinode,no,node lineage logic
> packages/qinode/src/parser,directory,packages/qinode/src,shared,qinode,no,node parser logic
> packages/qinode/src/serializer,directory,packages/qinode/src,shared,qinode,no,node serializer logic
> packages/qinode/src/reconstruction,directory,packages/qinode/src,shared,qinode,no,node rebuild logic
> packages/qinode/src/registry,directory,packages/qinode/src,shared,qinode,no,node registry logic
> packages/qinode/src/index.ts,file,packages/qinode/src,shared,qinode,no,package export surface
> 
> packages/database,directory,packages,shared,database,no,shared database helpers
> packages/database/package.json,file,packages/database,shared,database,no,package manifest
> packages/database/README.md,file,packages/database,shared,database,no,package readme
> packages/database/src,directory,packages/database,shared,database,no,source root
> packages/database/src/types,directory,packages/database/src,shared,database,no,shared db types
> packages/database/src/queries,directory,packages/database/src,shared,database,no,shared query helpers
> packages/database/src/adapters,directory,packages/database/src,shared,database,no,adapters
> packages/database/src/index.ts,file,packages/database/src,shared,database,no,package export surface
> 
> packages/ui,directory,packages,shared,ui,no,shared ui package
> packages/ui/package.json,file,packages/ui,shared,ui,no,package manifest
> packages/ui/README.md,file,packages/ui,shared,ui,no,package readme
> packages/ui/src,directory,packages/ui,shared,ui,no,source root
> packages/ui/src/components,directory,packages/ui/src,shared,ui,no,shared ui components
> packages/ui/src/tokens,directory,packages/ui/src,shared,ui,no,design tokens
> packages/ui/src/index.ts,file,packages/ui/src,shared,ui,no,package export surface
> 
> packages/ai,directory,packages,shared,ai,no,shared ai package
> packages/ai/package.json,file,packages/ai,shared,ai,no,package manifest
> packages/ai/README.md,file,packages/ai,shared,ai,no,package readme
> packages/ai/src,directory,packages/ai,shared,ai,no,source root
> packages/ai/src/prompts,directory,packages/ai/src,shared,ai,no,prompt assets
> packages/ai/src/tools,directory,packages/ai/src,shared,ai,no,tool helpers
> packages/ai/src/adapters,directory,packages/ai/src,shared,ai,no,provider adapters
> packages/ai/src/index.ts,file,packages/ai/src,shared,ai,no,package export surface
> 
> workers,directory,QiOne_Organism,runtime,root,yes,background workers
> workers/ingestion,directory,workers,runtime,documents,yes,document ingestion worker
> workers/embedder,directory,workers,runtime,ai,yes,embedding worker
> workers/metadata_naming,directory,workers,runtime,documents,yes,metadata naming worker
> workers/semantic_router,directory,workers,runtime,ai,yes,semantic routing worker
> workers/orchestrator,directory,workers,runtime,system,yes,workflow orchestration worker
> workers/self_heal,directory,workers,runtime,documents,yes,rebuild and repair worker
> 
> python_core,directory,QiOne_Organism,runtime,root,yes,python services
> python_core/agents,directory,python_core,runtime,ai,yes,python agent services
> python_core/document_processors,directory,python_core,runtime,documents,yes,heavy parsing and ocr services
> python_core/local_services,directory,python_core,runtime,system,yes,local python service utilities
> 
> supabase,directory,QiOne_Organism,data,root,yes,canonical database layer
> supabase/migrations,directory,supabase,data,root,yes,canonical schema migrations
> supabase/functions,directory,supabase,data,root,yes,database functions
> supabase/seed,directory,supabase,data,root,yes,seed data
> supabase/snippets,directory,supabase,data,root,no,sql snippets
> 
> content,directory,QiOne_Organism,content,root,yes,canonical authored content
> content/journals,directory,content,content,notes,yes,journal content
> content/stories,directory,content,content,notes,yes,story content
> content/notes,directory,content,content,notes,yes,note content
> content/prompts,directory,content,content,ai,yes,prompt content
> content/templates,directory,content,content,system,yes,reusable templates
> content/kb,directory,content,content,knowledge,yes,knowledge base content
> content/nodes,directory,content,content,documents,yes,qinode knowledge objects
> 
> scripts,directory,QiOne_Organism,ops,root,yes,developer scripts
> scripts/repo,directory,scripts,ops,repo,yes,repo governance scripts
> scripts/ingestion,directory,scripts,ops,documents,yes,ingestion scripts
> scripts/database,directory,scripts,ops,database,yes,database scripts
> scripts/sync,directory,scripts,ops,system,yes,sync scripts
> scripts/dev,directory,scripts,ops,system,yes,developer scripts
> scripts/maintenance,directory,scripts,ops,system,yes,cleanup and maintenance scripts
> 
> archive,directory,QiOne_Organism,archive,root,yes,retired material
> archive/legacy,directory,archive,archive,root,yes,retired live systems
> archive/experiments,directory,archive,archive,root,yes,prototype work
> archive/snapshots,directory,archive,archive,root,yes,point-in-time snapshots
> 
> docs,directory,QiOne_Organism,docs,root,yes,system documentation
> docs/architecture,directory,docs,docs,root,yes,architecture docs
> docs/decisions,directory,docs,docs,root,yes,decision records
> docs/guides,directory,docs,docs,root,yes,operational guides
> docs/references,directory,docs,docs,root,yes,reference docs
> ```
> 
> ## Non-negotiable placement rules
> 
> ```csv
> rule_id,scope,rule
> R001,root,no new root folders without updating the architecture CSV
> R002,apps,no nested apps inside app folders
> R003,workers,no workers inside apps/qione or apps/qially-web
> R004,supabase,no canonical migrations outside root supabase/migrations
> R005,archive,no old live folders left inside active app roots
> R006,versioning,no v2 copy final-final backup-app folder names
> R007,features,module logic goes in apps/qione/src/features/<module>
> R008,components,reusable ui goes in apps/qione/src/components/<module>
> R009,routes,routes go in apps/qione/src/app/(app|public|api)
> R010,content,canonical authored content goes in root content
> ```
> 
> That’s the hard tree.
> 
> If you want this as an actual `.csv` file artifact instead of chat paste, say `make the csv file` and I’ll generate it.

### User
> can you giveme the atommic entities we disucused in csv adn their schemas

### Assistant
> Yes. Best way to do this is as **two CSVs**:
> 
> 1. `atomic_entities.csv` = the entity registry  
> 2. `atomic_entity_fields.csv` = the field/schema definitions
> 
> That keeps it normalized and machine-friendly.
> 
> ## `atomic_entities.csv`
> 
> ```csv
> entity_key,entity_name,category,description,primary_module,canonical_table,extends_entity,is_core,is_content,is_temporal,is_document,is_system
> user,User,identity,Authenticated system user,admin,users,,true,false,false,false,true
> role,Role,identity,Permission role for access control,admin,roles,,true,false,false,false,true
> permission,Permission,identity,Granular action or scope permission,admin,permissions,,true,false,false,false,true
> contact,Contact,party,Any person or organization record,objects,contacts,,true,false,false,false,false
> client,Client,party,A contact that receives services or belongs to a business relationship,objects,clients,contact,true,false,false,false,false
> household,Household,party,A household or grouped living unit,objects,households,,false,false,false,false,false
> case,Case,work,A legal business or operational matter,objects,cases,,true,false,true,false,false
> project,Project,work,A bounded effort with tasks documents and timeline,objects,projects,,false,false,true,false,false
> task,Task,work,Action item assigned to a person or workflow,objects,tasks,,true,false,true,false,false
> appointment,Appointment,work,Scheduled event with participants,objects,appointments,,false,false,true,false,false
> message,Message,communication,A communication item in a thread or channel,objects,messages,,false,false,true,false,false
> thread,Thread,communication,A grouping container for messages,objects,threads,,false,false,true,false,false
> note,Note,knowledge,General knowledge note or reference,notes,notes,,true,true,true,false,false
> journal_entry,Journal Entry,knowledge,Personal or reflective dated note,notes,journal_entries,note,false,true,true,false,false
> story,Story,knowledge,Narrative or authored longform content,notes,stories,note,false,true,true,false,false
> chronicle_moment,Chronicle Moment,timeline,An event or moment on a timeline,chronicle,chronicle_moments,,true,false,true,false,false
> timeline,Timeline,timeline,A logical grouping of chronicle moments,chronicle,timelines,,false,false,true,false,false
> document,Document,document,A managed document record,documents,documents,,true,true,true,true,false
> file_asset,File Asset,document,Underlying stored file or binary asset,documents,file_assets,,true,false,false,true,false
> document_version,Document Version,document,Version snapshot of a document,documents,document_versions,document,false,false,true,true,false
> document_chunk,Document Chunk,document,Extracted text chunk for indexing and retrieval,documents,document_chunks,,false,false,false,true,false
> tag,Tag,classification,Reusable label for classification,documents,tags,,true,false,false,false,false
> collection,Collection,classification,Named grouping of entities or assets,documents,collections,,false,false,false,false,false
> form_definition,Form Definition,workflow,Renderable schema-driven form definition,forms,form_definitions,,true,true,false,false,false
> form_submission,Form Submission,workflow,Submitted form instance with answers,forms,form_submissions,,true,false,true,false,false
> contract,Contract,workflow,Agreement record with parties and status,contracts,contracts,,true,true,true,true,false
> signature,Signature,workflow,Signature or signing event tied to a contract or form,contracts,signatures,,false,false,true,false,false
> tax_return,Tax Return,tax,Tax return record for a filing year, tax,tax_returns,,true,false,true,false,false
> tax_organizer,Tax Organizer,tax,Tax intake or organizer record,tax,tax_organizers,,false,false,true,false,false
> expense,Expense,finance,Expense or outgoing financial item,objects,expenses,,true,false,true,false,false
> income,Income,finance,Income or incoming financial item,objects,income,,false,false,true,false,false
> account,Account,finance,Financial or logical account container,objects,accounts,,false,false,false,false,false
> asset,Asset,finance,Owned resource tangible or intangible,objects,assets,,true,false,false,false,false
> liability,Liability,finance,Debt or obligation record,objects,liabilities,,false,false,false,false,false
> patient,Patient,care,Care recipient or monitored person,care,patients,contact,true,false,false,false,false
> medication,Medication,care,Medication record tied to a patient,care,medications,,false,false,true,false,false
> supply,Supply,care,Consumable or care supply record,care,supplies,,false,false,false,false,false
> care_log,Care Log,care,Logged care action or observation,care,care_logs,,false,false,true,false,false
> prompt_asset,Prompt Asset,ai,Reusable prompt resource,ai,prompt_assets,,false,true,false,false,false
> agent_run,Agent Run,ai,Execution record of an AI or automation run,ai,agent_runs,,true,false,true,false,true
> embedding,Embedding,ai,Vector representation of an entity or chunk,ai,embeddings,,true,false,false,false,true
> automation,Automation,system,Recurring or triggered workflow definition,admin,automations,,false,false,true,false,true
> integration_connection,Integration Connection,system,Connected external service credential or link,settings,integration_connections,,false,false,false,false,true
> audit_event,Audit Event,system,Immutable system audit trail event,admin,audit_events,,true,false,true,false,true
> workflow_run,Workflow Run,system,Execution record for a workflow or orchestrated process,admin,workflow_runs,,false,false,true,false,true
> queue_job,Queue Job,system,Background job tracked through processing stages,admin,queue_jobs,,false,false,true,false,true
> ```
> 
> ## `atomic_entity_fields.csv`
> 
> ```csv
> entity_key,field_name,data_type,required,is_primary_key,is_foreign_key,foreign_entity,is_array,is_nullable,default_value,enum_values,description
> *,id,uuid,true,true,false,,false,false,,,"Global unique identifier"
> *,entity_type,text,true,false,false,,false,false,,,"Canonical entity discriminator"
> *,tenant_id,uuid,false,false,false,,false,true,,,"Tenant or workspace scope"
> *,realm_key,text,false,false,false,,false,true,,,"Logical realm or domain scope"
> *,title,text,false,false,false,,false,true,,,"Human-readable title"
> *,slug,text,false,false,false,,false,true,,,"Stable URL or lookup slug"
> *,status,text,false,false,false,,false,true,draft,"draft|active|archived|deleted|pending|completed","Lifecycle status"
> *,visibility,text,false,false,false,,false,true,private,"private|internal|shared|public","Visibility/access scope"
> *,created_at,timestamptz,true,false,false,,false,false,now(),,"Creation timestamp"
> *,updated_at,timestamptz,true,false,false,,false,false,now(),,"Last update timestamp"
> *,created_by,uuid,false,false,true,user,false,true,,,"Creating user"
> *,updated_by,uuid,false,false,true,user,false,true,,,"Last modifying user"
> *,owned_by,uuid,false,false,true,user,false,true,,,"Owning user"
> *,notes,text,false,false,false,,false,true,,,"Freeform notes"
> *,summary,text,false,false,false,,false,true,,,"Short summary"
> *,description,text,false,false,false,,false,true,,,"Long description"
> *,tags,jsonb,false,false,false,tag,true,true,[],, "Array of tag ids or tag objects"
> *,metadata,jsonb,false,false,false,,false,true,{},, "Flexible extra metadata"
> *,attributes,jsonb,false,false,false,,false,true,{},, "Extended entity-specific attributes"
> *,source_system,text,false,false,false,,false,true,,,"Source system name"
> *,source_id,text,false,false,false,,false,true,,,"External system identifier"
> *,canonical_path,text,false,false,false,,false,true,,,"Canonical file or logical path"
> *,sort_order,integer,false,false,false,,false,true,0,, "Ordering value"
> *,is_active,boolean,false,false,false,,false,false,true,, "Active flag"
> *,archived_at,timestamptz,false,false,false,,false,true,,,"Archive timestamp"
> *,deleted_at,timestamptz,false,false,false,,false,true,,,"Soft delete timestamp"
> 
> user,email,text,true,false,false,,false,false,,,"Login email"
> user,display_name,text,false,false,false,,false,true,,,"Display name"
> user,first_name,text,false,false,false,,false,true,,,"First name"
> user,last_name,text,false,false,false,,false,true,,,"Last name"
> user,phone,text,false,false,false,,false,true,,,"Phone number"
> user,last_login_at,timestamptz,false,false,false,,false,true,,,"Last login time"
> 
> role,name,text,true,false,false,,false,false,,,"Role name"
> role,role_key,text,true,false,false,,false,false,,,"Stable role key"
> role,description,text,false,false,false,,false,true,,,"Role description"
> 
> permission,permission_key,text,true,false,false,,false,false,,,"Stable permission key"
> permission,resource_type,text,true,false,false,,false,false,,,"Protected resource type"
> permission,action,text,true,false,false,,false,false,,,"Allowed action"
> permission,description,text,false,false,false,,false,true,,,"Permission description"
> 
> contact,contact_type,text,false,false,false,,false,true,person,"person|organization","Contact type"
> contact,full_name,text,false,false,false,,false,true,,,"Full name"
> contact,company_name,text,false,false,false,,false,true,,,"Organization name"
> contact,email,text,false,false,false,,false,true,,,"Primary email"
> contact,phone,text,false,false,false,,false,true,,,"Primary phone"
> contact,address_json,jsonb,false,false,false,,false,true,{},, "Structured address"
> contact,preferred_language,text,false,false,false,,false,true,,,"Preferred language"
> 
> client,contact_id,uuid,true,false,true,contact,false,false,,,"Linked contact"
> client,client_code,text,false,false,false,,false,true,,,"Business/client code"
> client,client_status,text,false,false,false,,false,true,active,"lead|active|inactive|closed","Client state"
> client,onboarded_at,timestamptz,false,false,false,,false,true,,,"Onboarding date"
> 
> household,name,text,true,false,false,,false,false,,,"Household name"
> household,primary_contact_id,uuid,false,false,true,contact,false,true,,,"Primary contact"
> 
> case,case_key,text,true,false,false,,false,false,,,"Stable case key"
> case,case_type,text,false,false,false,,false,true,,,"Case type"
> case,opened_at,timestamptz,false,false,false,,false,true,,,"Open date"
> case,closed_at,timestamptz,false,false,false,,false,true,,,"Close date"
> case,priority,text,false,false,false,,false,true,normal,"low|normal|high|urgent","Priority level"
> 
> project,project_key,text,true,false,false,,false,false,,,"Stable project key"
> project,start_date,date,false,false,false,,false,true,,,"Project start date"
> project,end_date,date,false,false,false,,false,true,,,"Project end date"
> 
> task,parent_entity_type,text,false,false,false,,false,true,,,"Linked entity type"
> task,parent_entity_id,uuid,false,false,false,,false,true,,,"Linked entity id"
> task,assigned_to,uuid,false,false,true,user,false,true,,,"Assigned user"
> task,due_at,timestamptz,false,false,false,,false,true,,,"Due time"
> task,completed_at,timestamptz,false,false,false,,false,true,,,"Completion time"
> task,priority,text,false,false,false,,false,true,normal,"low|normal|high|urgent","Task priority"
> 
> appointment,start_at,timestamptz,true,false,false,,false,false,,,"Scheduled start"
> appointment,end_at,timestamptz,false,false,false,,false,true,,,"Scheduled end"
> appointment,location_text,text,false,false,false,,false,true,,,"Location label"
> appointment,participants,jsonb,false,false,false,,true,true,[],, "Participant ids"
> 
> thread,thread_key,text,true,false,false,,false,false,,,"Thread key"
> thread,channel_type,text,false,false,false,,false,true,,,"Email sms internal etc"
> 
> message,thread_id,uuid,true,false,true,thread,false,false,,,"Parent thread"
> message,sender_id,uuid,false,false,true,contact,false,true,,,"Sender"
> message,body,text,false,false,false,,false,true,,,"Message body"
> message,sent_at,timestamptz,false,false,false,,false,true,,,"Sent timestamp"
> 
> note,body_md,text,false,false,false,,false,true,,,"Markdown body"
> note,note_type,text,false,false,false,,false,true,general,"general|reference|scratch|idea","Note type"
> 
> journal_entry,entry_date,date,true,false,false,,false,false,,,"Journal date"
> journal_entry,mood,text,false,false,false,,false,true,,,"Mood label"
> 
> story,story_type,text,false,false,false,,false,true,,,"Story subtype"
> story,body_md,text,false,false,false,,false,true,,,"Story markdown"
> 
> chronicle_moment,moment_at,timestamptz,true,false,false,,false,false,,,"Event timestamp"
> chronicle_moment,parent_entity_type,text,false,false,false,,false,true,,,"Linked entity type"
> chronicle_moment,parent_entity_id,uuid,false,false,false,,false,true,,,"Linked entity id"
> chronicle_moment,event_type,text,true,false,false,,false,false,,,"Event kind"
> chronicle_moment,importance,integer,false,false,false,,false,true,0,, "Importance score"
> 
> timeline,timeline_key,text,true,false,false,,false,false,,,"Timeline key"
> timeline,timeline_type,text,false,false,false,,false,true,,,"Timeline type"
> 
> document,file_asset_id,uuid,false,false,true,file_asset,false,true,,,"Current primary file"
> document,document_type,text,false,false,false,,false,true,,,"Document type"
> document,mime_type,text,false,false,false,,false,true,,,"Mime type"
> document,text_content,text,false,false,false,,false,true,,,"Extracted full text"
> document,page_count,integer,false,false,false,,false,true,,,"Number of pages"
> document,document_date,date,false,false,false,,false,true,,,"Document date"
> document,ocr_status,text,false,false,false,,false,true,pending,"pending|complete|failed","OCR state"
> document,index_status,text,false,false,false,,false,true,pending,"pending|indexed|failed","Index state"
> 
> file_asset,storage_provider,text,false,false,false,,false,true,local,"local|supabase|s3|drive","Storage backend"
> file_asset,storage_bucket,text,false,false,false,,false,true,,,"Bucket or drive name"
> file_asset,storage_key,text,false,false,false,,false,true,,,"Storage object key"
> file_asset,file_name,text,false,false,false,,false,true,,,"Stored file name"
> file_asset,file_ext,text,false,false,false,,false,true,,,"File extension"
> file_asset,file_size_bytes,bigint,false,false,false,,false,true,,,"File size"
> file_asset,sha256,text,false,false,false,,false,true,,,"Content hash"
> 
> document_version,document_id,uuid,true,false,true,document,false,false,,,"Parent document"
> document_version,version_no,integer,true,false,false,,false,false,,,"Version number"
> document_version,change_summary,text,false,false,false,,false,true,,,"Change summary"
> 
> document_chunk,document_id,uuid,true,false,true,document,false,false,,,"Parent document"
> document_chunk,chunk_index,integer,true,false,false,,false,false,,,"Chunk order"
> document_chunk,chunk_text,text,true,false,false,,false,false,,,"Chunk text"
> document_chunk,token_count,integer,false,false,false,,false,true,,,"Token count"
> document_chunk,embedding_id,uuid,false,false,true,embedding,false,true,,,"Optional vector link"
> 
> tag,tag_key,text,true,false,false,,false,false,,,"Stable tag key"
> tag,color,text,false,false,false,,false,true,,,"Display color"
> 
> collection,collection_key,text,true,false,false,,false,false,,,"Stable collection key"
> collection,collection_type,text,false,false,false,,false,true,,,"Collection type"
> 
> form_definition,form_key,text,true,false,false,,false,false,,,"Stable form key"
> form_definition,version_no,integer,true,false,false,,false,false,1,, "Definition version"
> form_definition,schema_json,jsonb,true,false,false,,false,false,{},, "Renderable form schema"
> 
> form_submission,form_definition_id,uuid,true,false,true,form_definition,false,false,,,"Source definition"
> form_submission,submitted_by,uuid,false,false,true,user,false,true,,,"Submitting user"
> form_submission,submitted_at,timestamptz,false,false,false,,false,true,now(),,"Submission timestamp"
> form_submission,answers_json,jsonb,true,false,false,,false,false,{},, "Submitted answers"
> 
> contract,contract_key,text,true,false,false,,false,false,,,"Stable contract key"
> contract,contract_type,text,false,false,false,,false,true,,,"Contract type"
> contract,effective_date,date,false,false,false,,false,true,,,"Effective date"
> contract,expiration_date,date,false,false,false,,false,true,,,"Expiration date"
> contract,contract_status,text,false,false,false,,false,true,draft,"draft|sent|signed|void|expired","Contract status"
> contract,body_md,text,false,false,false,,false,true,,,"Contract body markdown"
> 
> signature,parent_entity_type,text,true,false,false,,false,false,,,"Signed entity type"
> signature,parent_entity_id,uuid,true,false,false,,false,false,,,"Signed entity id"
> signature,signed_by_contact_id,uuid,false,false,true,contact,false,true,,,"Signer"
> signature,signed_at,timestamptz,false,false,false,,false,true,,,"Signature time"
> signature,signature_status,text,false,false,false,,false,true,pending,"pending|signed|declined","Signature state"
> 
> tax_return,client_id,uuid,false,false,true,client,false,true,,,"Related client"
> tax_return,tax_year,integer,true,false,false,,false,false,,,"Tax year"
> tax_return,filing_status,text,false,false,false,,false,true,,,"Filing status"
> tax_return,return_status,text,false,false,false,,false,true,draft,"draft|in_progress|filed|accepted|rejected","Return state"
> 
> tax_organizer,client_id,uuid,false,false,true,client,false,true,,,"Related client"
> tax_organizer,tax_year,integer,true,false,false,,false,false,,,"Organizer year"
> tax_organizer,organizer_status,text,false,false,false,,false,true,draft,"draft|sent|received|reviewed","Organizer state"
> 
> expense,account_id,uuid,false,false,true,account,false,true,,,"Related account"
> expense,amount,numeric,true,false,false,,false,false,,,"Amount"
> expense,currency,text,false,false,false,,false,true,USD,, "Currency"
> expense,expense_date,date,false,false,false,,false,true,,,"Expense date"
> expense,payee_contact_id,uuid,false,false,true,contact,false,true,,,"Payee"
> expense,receipt_document_id,uuid,false,false,true,document,false,true,,,"Receipt doc"
> 
> income,account_id,uuid,false,false,true,account,false,true,,,"Related account"
> income,amount,numeric,true,false,false,,false,false,,,"Amount"
> income,currency,text,false,false,false,,false,true,USD,, "Currency"
> income,received_date,date,false,false,false,,false,true,,,"Received date"
> income,payer_contact_id,uuid,false,false,true,contact,false,true,,,"Payer"
> 
> account,account_key,text,true,false,false,,false,false,,,"Stable account key"
> account,account_type,text,false,false,false,,false,true,,,"Account type"
> account,institution_name,text,false,false,false,,false,true,,,"Institution"
> 
> asset,asset_type,text,false,false,false,,false,true,,,"Asset type"
> asset,estimated_value,numeric,false,false,false,,false,true,,,"Estimated value"
> asset,acquired_at,date,false,false,false,,false,true,,,"Acquisition date"
> 
> liability,liability_type,text,false,false,false,,false,true,,,"Liability type"
> liability,balance,numeric,false,false,false,,false,true,,,"Outstanding balance"
> liability,due_date,date,false,false,false,,false,true,,,"Due date"
> 
> patient,contact_id,uuid,true,false,true,contact,false,false,,,"Underlying contact"
> patient,date_of_birth,date,false,false,false,,false,true,,,"DOB"
> patient,care_status,text,false,false,false,,false,true,active,"active|paused|closed","Care status"
> 
> medication,patient_id,uuid,true,false,true,patient,false,false,,,"Related patient"
> medication,dosage_text,text,false,false,false,,false,true,,,"Dosage"
> medication,frequency_text,text,false,false,false,,false,true,,,"Frequency"
> medication,start_date,date,false,false,false,,false,true,,,"Start date"
> medication,end_date,date,false,false,false,,false,true,,,"End date"
> 
> supply,patient_id,uuid,false,false,true,patient,false,true,,,"Related patient"
> supply,quantity,numeric,false,false,false,,false,true,,,"Quantity on hand"
> supply,unit,text,false,false,false,,false,true,,,"Unit"
> 
> care_log,patient_id,uuid,true,false,true,patient,false,false,,,"Related patient"
> care_log,logged_at,timestamptz,true,false,false,,false,false,now(),,"Log timestamp"
> care_log,log_type,text,true,false,false,,false,false,,,"Observation|medication|task|incident"
> care_log,details_json,jsonb,false,false,false,,false,true,{},, "Structured details"
> 
> prompt_asset,prompt_key,text,true,false,false,,false,false,,,"Stable prompt key"
> prompt_asset,prompt_text,text,true,false,false,,false,false,,,"Prompt body"
> prompt_asset,prompt_role,text,false,false,false,,false,true,system,"system|user|assistant","Prompt role"
> 
> agent_run,agent_key,text,true,false,false,,false,false,,,"Agent identifier"
> agent_run,parent_entity_type,text,false,false,false,,false,true,,,"Linked entity type"
> agent_run,parent_entity_id,uuid,false,false,false,,false,true,,,"Linked entity id"
> agent_run,started_at,timestamptz,false,false,false,,false,true,now(),,"Start time"
> agent_run,finished_at,timestamptz,false,false,false,,false,true,,,"Finish time"
> agent_run,run_status,text,false,false,false,,false,true,running,"running|success|failed|canceled","Run state"
> agent_run,input_json,jsonb,false,false,false,,false,true,{},, "Run input"
> agent_run,output_json,jsonb,false,false,false,,false,true,{},, "Run output"
> 
> embedding,parent_entity_type,text,true,false,false,,false,false,,,"Embedded entity type"
> embedding,parent_entity_id,uuid,true,false,false,,false,false,,,"Embedded entity id"
> embedding,vector_model,text,false,false,false,,false,true,,,"Embedding model"
> embedding,dimensions,integer,false,false,false,,false,true,,,"Vector dimensions"
> 
> automation,automation_key,text,true,false,false,,false,false,,,"Stable automation key"
> automation,trigger_type,text,false,false,false,,false,true,,,"manual|schedule|event"
> automation,schedule_text,text,false,false,false,,false,true,,,"Cron or schedule"
> automation,automation_status,text,false,false,false,,false,true,active,"active|paused|disabled","Automation state"
> 
> integration_connection,provider_key,text,true,false,false,,false,false,,,"Service provider key"
> integration_connection,connection_status,text,false,false,false,,false,true,connected,"connected|expired|revoked|error","Connection state"
> integration_connection,last_sync_at,timestamptz,false,false,false,,false,true,,,"Last sync"
> 
> audit_event,event_key,text,true,false,false,,false,false,,,"Stable audit key"
> audit_event,actor_user_id,uuid,false,false,true,user,false,true,,,"Actor user"
> audit_event,target_entity_type,text,false,false,false,,false,true,,,"Target type"
> audit_event,target_entity_id,uuid,false,false,false,,false,true,,,"Target id"
> audit_event,event_at,timestamptz,true,false,false,,false,false,now(),,"Event time"
> audit_event,event_payload,jsonb,false,false,false,,false,true,{},, "Audit payload"
> 
> workflow_run,workflow_key,text,true,false,false,,false,false,,,"Workflow key"
> workflow_run,started_at,timestamptz,false,false,false,,false,true,now(),,"Start time"
> workflow_run,finished_at,timestamptz,false,false,false,,false,true,,,"Finish time"
> workflow_run,run_status,text,false,false,false,,false,true,running,"running|success|failed|canceled","Workflow state"
> 
> queue_job,job_key,text,true,false,false,,false,false,,,"Job key"
> queue_job,queue_name,text,true,false,false,,false,false,,,"Queue name"
> queue_job,parent_entity_type,text,false,false,false,,false,true,,,"Linked entity type"
> queue_job,parent_entity_id,uuid,false,false,false,,false,true,,,"Linked entity id"
> queue_job,scheduled_at,timestamptz,false,false,false,,false,true,,,"Scheduled time"
> queue_job,started_at,timestamptz,false,false,false,,false,true,,,"Start time"
> queue_job,finished_at,timestamptz,false,false,false,,false,true,,,"Finish time"
> queue_job,job_status,text,false,false,false,,false,true,queued,"queued|running|success|failed|dead","Job state"
> queue_job,payload_json,jsonb,false,false,false,,false,true,{},, "Job payload"
> ```
> 
> ## Schema rules you should keep hard-coded
> 
> ```csv
> rule_key,rule_description
> BASE01,Every entity must inherit the common base fields marked with entity_key = *
> BASE02,Every entity must have id entity_type created_at updated_at status visibility metadata attributes
> BASE03,Use uuid for all primary ids and foreign ids
> BASE04,Use jsonb only for flexible payloads not as a substitute for core modeled fields
> BASE05,Use parent_entity_type plus parent_entity_id when linking across many entity types
> BASE06,Use canonical tables for durable entities and keep transient UI state out of the entity model
> BASE07,Chronicle moments audit events queue jobs and agent runs are append-friendly temporal entities
> BASE08,Documents file assets document chunks and embeddings are separate entities and should not be collapsed into one table
> BASE09,QiNode maps best to document plus file_asset plus document_chunk plus lineage metadata
> BASE10,Clients and patients extend contact conceptually even if implemented as separate tables
> ```
> 
> ## Practical read
> 
> If you want the **minimum viable atomic core**, start with these first:
> 
> ```csv
> entity_key
> contact
> client
> case
> task
> note
> chronicle_moment
> document
> file_asset
> form_definition
> form_submission
> contract
> tax_return
> expense
> patient
> medication
> tag
> embedding
> audit_event
> queue_job
> ```
> 
> That’s enough to make QiOne breathe without turning it into abstract soup.
> 
> If you want, next I can turn this into:
> - **actual SQL table starter schemas**
> - **a Supabase/Postgres migration**
> - or **downloadable CSV files**.

### User
> give me the system or dev docs for this conversation

### Assistant
> Below is the **developer/system documentation artifact** for this session.  
> It captures the architecture decisions, entity model, and repo structure we just locked down.
> 
> You can drop this directly into:
> 
> ```
> docs/decisions/ADR-0007-qione-architecture-lock.md
> ```
> 
> ---
> 
> :::writing{variant="standard" id="48162"}
> # ADR-0007 — QiOne Architecture Lock
> Date: 2026-03-10  
> Status: Accepted  
> Author: Cody Rice-Velasquez  
> System: QiOne Monorepo  
> 
> ---
> 
> # 1. Executive Summary
> 
> QiOne is the **single authenticated operating environment** for the Qi ecosystem.
> 
> Previous development fragmented across multiple experimental repos (QiNode, QiArchive, AIHub, etc.).  
> These projects represented **partial system organs**, not independent systems.
> 
> This decision consolidates them into a **single organism architecture**.
> 
> All user functionality must now occur **inside the QiOne application**.
> 
> Permissions determine visibility.
> 
> No separate apps for individual modules.
> 
> ---
> 
> # 2. Architectural Principles
> 
> ### 2.1 Single Entry System
> 
> All authenticated interaction begins at:
> 
> ```
> apps/qione
> ```
> 
> After login, users navigate modules within the same application.
> 
> Examples:
> 
> ```
> /dashboard
> /documents
> /chronicle
> /forms
> /contracts
> /tax
> /care
> /admin
> ```
> 
> ---
> 
> ### 2.2 Module-Based Architecture
> 
> Each domain exists as a **module**, not a separate app.
> 
> Modules consist of:
> 
> ```
> route layer
> UI layer
> feature logic
> database schema
> worker integrations
> ```
> 
> Modules currently defined:
> 
> | Module | Purpose |
> |------|------|
> | dashboard | system overview |
> | ai | assistant / RAG interface |
> | documents | document ingestion + QiNode |
> | chronicle | timeline events |
> | notes | journals stories notes |
> | objects | atomic entity records |
> | forms | dynamic forms |
> | contracts | agreement workflows |
> | tax | tax preparation |
> | care | healthcare / caregiver |
> | settings | user configuration |
> | admin | system operations |
> 
> ---
> 
> # 3. Repository Topology
> 
> The QiOne monorepo root is locked to the following structure.
> 
> ```
> QiOne/
> ```
> 
> ```
> apps/
> packages/
> workers/
> python_core/
> supabase/
> content/
> scripts/
> archive/
> docs/
> .github/
> ```
> 
> These directories are **architecture-locked**.
> 
> No new root folders may be added without an architecture decision record.
> 
> ---
> 
> # 4. Application Layer
> 
> Primary application:
> 
> ```
> apps/qione
> ```
> 
> Structure:
> 
> ```
> apps/qione
>  ├ public
>  ├ src
>  │  ├ app
>  │  ├ components
>  │  ├ features
>  │  ├ lib
>  │  ├ types
>  │  └ styles
>  ├ supabase
>  ├ content
>  ├ tests
>  └ docs
> ```
> 
> ### Layer Responsibilities
> 
> | Layer | Responsibility |
> |-----|-----|
> | app | routing and screens |
> | components | UI building blocks |
> | features | module logic |
> | lib | shared services |
> | types | global type definitions |
> | styles | global CSS |
> 
> ---
> 
> # 5. Module Implementation Pattern
> 
> Each module follows the same pattern.
> 
> Example:
> 
> ```
> documents module
> ```
> 
> ```
> src/app/documents
> src/components/documents
> src/features/documents
> ```
> 
> Within the feature layer:
> 
> ```
> features/documents
>  ├ client
>  ├ server
>  ├ schemas
>  ├ qinode
>  └ utils
> ```
> 
> ---
> 
> # 6. QiNode Integration
> 
> QiNode is **not a separate app**.
> 
> It becomes a **document protocol implementation**.
> 
> Location:
> 
> ```
> features/documents/qinode
> ```
> 
> Responsibilities:
> 
> | Subsystem | Function |
> |--------|--------|
> | dna | node identity |
> | lineage | parent child graph |
> | parser | node reader |
> | serializer | node writer |
> | reconstruction | disaster recovery |
> | registry | node discovery |
> 
> QiNode folders remain portable and self-describing.
> 
> ---
> 
> # 7. Worker Layer
> 
> Background jobs run outside the application.
> 
> Location:
> 
> ```
> workers/
> ```
> 
> Current workers:
> 
> ```
> ingestion
> embedder
> metadata_naming
> semantic_router
> orchestrator
> self_heal
> ```
> 
> Responsibilities:
> 
> | Worker | Purpose |
> |------|------|
> | ingestion | document intake |
> | embedder | vector generation |
> | metadata_naming | canonical naming |
> | semantic_router | classification |
> | orchestrator | workflow coordination |
> | self_heal | node rebuild |
> 
> ---
> 
> # 8. Python Processing Layer
> 
> Heavy processing services run under:
> 
> ```
> python_core/
> ```
> 
> Structure:
> 
> ```
> agents
> document_processors
> local_services
> ```
> 
> Use cases:
> 
> * OCR
> * AI agents
> * document extraction
> * large compute tasks
> 
> ---
> 
> # 9. Database Layer
> 
> Canonical schema lives in:
> 
> ```
> supabase/
> ```
> 
> Structure:
> 
> ```
> migrations
> functions
> seed
> snippets
> ```
> 
> Rules:
> 
> * All schema changes must go through migrations
> * modules may include SQL helpers inside app directories
> * canonical schema remains centralized
> 
> ---
> 
> # 10. Content Layer
> 
> Human-authored assets live in:
> 
> ```
> content/
> ```
> 
> Structure:
> 
> ```
> journals
> stories
> notes
> prompts
> templates
> kb
> nodes
> ```
> 
> This allows:
> 
> * AI training
> * personal writing
> * knowledge base storage
> * QiNode data
> 
> ---
> 
> # 11. Atomic Entity Model
> 
> The system uses **atomic entities** instead of application-specific records.
> 
> Every record inherits the base entity fields.
> 
> ### Base Entity Fields
> 
> ```
> id
> entity_type
> tenant_id
> realm_key
> status
> visibility
> created_at
> updated_at
> created_by
> updated_by
> metadata
> attributes
> ```
> 
> ---
> 
> ### Core Entity Domains
> 
> | Domain | Examples |
> |------|------|
> | identity | user role permission |
> | party | contact client household |
> | work | case task project |
> | knowledge | note journal story |
> | timeline | chronicle_moment |
> | document | document file_asset chunk |
> | workflow | form contract signature |
> | tax | tax_return organizer |
> | finance | account expense income |
> | care | patient medication care_log |
> | ai | embedding agent_run prompt |
> | system | audit_event queue_job workflow_run |
> 
> ---
> 
> # 12. Chronicle Event Model
> 
> The chronicle module records **temporal events**.
> 
> Example event:
> 
> ```
> chronicle_moment
> ```
> 
> Fields:
> 
> ```
> moment_at
> parent_entity_type
> parent_entity_id
> event_type
> importance
> ```
> 
> This produces the **system timeline**.
> 
> ---
> 
> # 13. Document System
> 
> Documents are normalized across four entities.
> 
> ```
> document
> file_asset
> document_version
> document_chunk
> ```
> 
> Purpose:
> 
> | Entity | Responsibility |
> |------|------|
> | document | logical record |
> | file_asset | binary storage |
> | version | revision history |
> | chunk | embedding index |
> 
> ---
> 
> # 14. AI Integration
> 
> AI functionality integrates through three layers.
> 
> ```
> packages/ai
> workers/embedder
> features/ai
> ```
> 
> Capabilities include:
> 
> * RAG retrieval
> * prompt execution
> * agent workflows
> * vector search
> 
> ---
> 
> # 15. Anti-Entropy Rules
> 
> These rules exist to prevent architectural drift.
> 
> 1. No new root folders without ADR.
> 2. No new applications unless absolutely required.
> 3. No duplicate migrations.
> 4. Workers must remain outside apps.
> 5. Modules cannot become independent repos.
> 6. Archive old work instead of leaving it in place.
> 7. Avoid dumping logic into generic utils.
> 
> ---
> 
> # 16. Migration Strategy
> 
> Existing experiments move into:
> 
> ```
> archive/experiments
> ```
> 
> Production components move into their respective layers.
> 
> Examples:
> 
> | Project | New Location |
> |------|------|
> | QiNode | features/documents/qinode |
> | QiArchive | documents module |
> | AIHub | ai module |
> | ingestion scripts | workers/ingestion |
> 
> ---
> 
> # 17. Long Term Goal
> 
> QiOne becomes:
> 
> > a **local-first cognitive operating system**
> 
> Capabilities:
> 
> * knowledge graph
> * document archive
> * AI assistant
> * workflow automation
> * personal and business OS
> 
> All through **one login interface**.
> 
> ---
> 
> # 18. Final Statement
> 
> QiOne is no longer a collection of projects.
> 
> It is a **single organism**.
> 
> Modules represent organs.
> 
> Workers represent metabolism.
> 
> The database represents memory.
> 
> And the interface represents consciousness.
> 
> ---
> :::
> 
> ---
> 
> If you want, I can also generate the **three docs that usually come next for systems like this**:
> 
> 1. **QiOne Module Dependency Map**
> 2. **QiOne Database ERD**
> 3. **QiOne Worker Pipeline Diagram**
> 
> Those will make your repo **AI-navigable automatically** (Cursor / GPT / Claude / Gemini).

### Assistant
> I opened the tree you uploaded. Good news: **your repo is already very close to the architecture we discussed.** You mostly need **re-grouping and a few naming corrections**, not a rebuild.
> 
> Below is the **cleaned and finalized structure based on your actual tree**, with the relationships made explicit so AI tools can parse it.
> 
> ---
> 
> # Final QiOne Repository Structure (Locked)
> 
> ```text
> QiOne/
> │
> ├─ apps/
> │   ├─ qione/                 # Main system application (ALL functionality)
> │   │
> │   │   ├─ public/
> │   │   │   ├─ images/
> │   │   │   └─ icons/
> │   │   │
> │   │   ├─ src/
> │   │   │   │
> │   │   │   ├─ app/           # Routes (Next/Astro)
> │   │   │   │
> │   │   │   │   ├─ dashboard/
> │   │   │   │   ├─ ai/
> │   │   │   │   ├─ documents/
> │   │   │   │   ├─ chronicle/
> │   │   │   │   ├─ notes/
> │   │   │   │   ├─ objects/
> │   │   │   │   ├─ forms/
> │   │   │   │   ├─ contracts/
> │   │   │   │   ├─ tax/
> │   │   │   │   ├─ care/
> │   │   │   │   ├─ settings/
> │   │   │   │   └─ admin/
> │   │   │   │
> │   │   │   ├─ components/    # UI components
> │   │   │   │   ├─ layout/
> │   │   │   │   ├─ ui/
> │   │   │   │   ├─ documents/
> │   │   │   │   ├─ chronicle/
> │   │   │   │   ├─ forms/
> │   │   │   │   ├─ notes/
> │   │   │   │   └─ ai/
> │   │   │   │
> │   │   │   ├─ features/      # Domain logic modules
> │   │   │   │   ├─ ai/
> │   │   │   │   ├─ documents/
> │   │   │   │   │   └─ qinode/
> │   │   │   │   ├─ chronicle/
> │   │   │   │   ├─ notes/
> │   │   │   │   ├─ objects/
> │   │   │   │   ├─ forms/
> │   │   │   │   ├─ contracts/
> │   │   │   │   ├─ tax/
> │   │   │   │   ├─ care/
> │   │   │   │   └─ admin/
> │   │   │   │
> │   │   │   ├─ lib/           # shared services
> │   │   │   │   ├─ db/
> │   │   │   │   ├─ auth/
> │   │   │   │   ├─ ai/
> │   │   │   │   ├─ storage/
> │   │   │   │   └─ utils/
> │   │   │   │
> │   │   │   ├─ types/
> │   │   │   └─ styles/
> │   │   │
> │   │   ├─ supabase/         # app-level sql helpers
> │   │   ├─ content/
> │   │   ├─ tests/
> │   │   └─ docs/
> │   │
> │   └─ qially-web/            # public marketing website
> │
> ├─ packages/                  # reusable libraries
> │   ├─ database/
> │   ├─ ui/
> │   ├─ ai/
> │   └─ qinode/
> │
> ├─ workers/                   # background services
> │   ├─ ingestion/
> │   ├─ embedder/
> │   ├─ metadata_naming/
> │   ├─ semantic_router/
> │   ├─ orchestrator/
> │   └─ self_heal/
> │
> ├─ python_core/               # heavy compute services
> │   ├─ agents/
> │   ├─ document_processors/
> │   └─ local_services/
> │
> ├─ supabase/
> │   ├─ migrations/
> │   ├─ functions/
> │   ├─ seed/
> │   └─ snippets/
> │
> ├─ content/
> │   ├─ journals/
> │   ├─ stories/
> │   ├─ notes/
> │   ├─ prompts/
> │   ├─ templates/
> │   ├─ kb/
> │   └─ nodes/
> │
> ├─ scripts/
> │   ├─ repo/
> │   ├─ ingestion/
> │   ├─ database/
> │   ├─ sync/
> │   ├─ dev/
> │   └─ maintenance/
> │
> ├─ archive/
> │   ├─ legacy/
> │   ├─ experiments/
> │   └─ snapshots/
> │
> ├─ docs/
> │   ├─ architecture/
> │   ├─ decisions/
> │   ├─ guides/
> │   └─ references/
> │
> └─ .github/
> ```
> 
> ---
> 
> # Relationship Model (How Everything Connects)
> 
> ### 1️⃣ User Flow
> 
> ```
> User
>    ↓
> Login
>    ↓
> apps/qione
>    ↓
> Modules
> ```
> 
> Modules:
> 
> ```
> dashboard
> ai
> documents
> chronicle
> notes
> objects
> forms
> contracts
> tax
> care
> settings
> admin
> ```
> 
> ---
> 
> ### 2️⃣ Module Dependencies
> 
> ```
> modules
>    ↓
> features
>    ↓
> lib services
>    ↓
> database
>    ↓
> workers
> ```
> 
> Example:
> 
> ```
> documents module
>    ↓
> features/documents
>    ↓
> lib/storage
>    ↓
> workers/ingestion
>    ↓
> supabase tables
> ```
> 
> ---
> 
> ### 3️⃣ Document Pipeline
> 
> ```
> Upload
>    ↓
> workers/ingestion
>    ↓
> document_processors
>    ↓
> document entity
>    ↓
> document_chunk
>    ↓
> workers/embedder
>    ↓
> vector index
> ```
> 
> ---
> 
> ### 4️⃣ QiNode Placement
> 
> QiNode belongs to **three layers**
> 
> ```
> features/documents/qinode
> packages/qinode
> workers/self_heal
> ```
> 
> Responsibilities:
> 
> | Layer | Responsibility |
> |------|------|
> app feature | node parsing |
> package | protocol library |
> worker | reconstruction |
> 
> ---
> 
> ### 5️⃣ AI Architecture
> 
> ```
> features/ai
>    ↓
> lib/ai
>    ↓
> workers/embedder
>    ↓
> vector database
> ```
> 
> Capabilities:
> 
> ```
> RAG
> agents
> skills
> search
> automation
> ```
> 
> ---
> 
> ### 6️⃣ Chronicle Event Graph
> 
> ```
> chronicle_moment
>    ↓
> linked to
>    ↓
> ANY entity
> ```
> 
> Example:
> 
> ```
> chronicle_moment
>     parent_entity_type = document
>     parent_entity_id = doc_id
> ```
> 
> Chronicle becomes the **system timeline**.
> 
> ---
> 
> # Why This Structure Works
> 
> It separates **five types of code** clearly:
> 
> | Layer | Responsibility |
> |------|------|
> apps | UI and routes |
> features | business logic |
> packages | reusable libraries |
> workers | async processing |
> python_core | heavy compute |
> 
> This prevents the repo from turning into chaos again.
> 
> ---
> 
> # One Critical Rule
> 
> Never create another app unless it is:
> 
> ```
> public website
> or
> external API service
> ```
> 
> Everything else lives in **qione modules**.
> 
> ---
> 
> # What I Recommend Next
> 
> Your repo is now ready for the **three diagrams that make AI tools insanely powerful with it**:
> 
> 1️⃣ **QiOne System Architecture Map**  
> 2️⃣ **Entity Relationship Diagram (ERD)**  
> 3️⃣ **Worker Processing Pipeline**
> 
> Those three allow Cursor / GPT / Claude to understand the entire repo instantly.
> 
> If you want, I can also generate a **machine-readable architecture file** like:
> 
> ```
> qione_architecture.json
> ```
> 
> which AI agents can parse automatically to navigate the repo.

### User
> lets cleaan up this workers folder first ```markdown

> . 📂 workers

> └── 📂 Tools_Launcher/

> │  └── 📂 api/

> │    ├── 📄 index.html

> │  └── 📂 components/

> │    └── 📂 chat/

> │      ├── 📄 index.html

> │    ├── 📄 index.html

> │    └── 📂 views/

> │      ├── 📄 index.html

> │  ├── 📄 index.html

> │  └── 📂 tools/

> │    ├── 📄 index.html

> ├── 📄 _readme.md

> └── 📂 _shared/

> │  ├── 📄 constitution.ts

> │  ├── 📄 heartbeat.ts

> │  ├── 📄 ignore.ts

> │  ├── 📄 index.html

> └── 📂 ai/

> │  ├── 📄 resourceGraphWorker.ts

> └── 📂 cases/

> │  └── 📂 src/

> │    ├── 📄 index.ts

> │  ├── 📄 wrangler.toml

> └── 📂 cloud/

> │  └── 📂 embedder/

> │    ├── 📄 EMBEDDER_IMPROVEMENTS.md

> │    ├── 📄 EMBEDDER_SIMPLIFICATION.md

> │    ├── 📄 package.json

> │    ├── 📄 worker_embedder.ts

> │    ├── 📄 wrangler.toml

> │  └── 📂 ingestion/

> │    ├── 📄 package.json

> │    ├── 📄 worker_ingestion.ts

> │    ├── 📄 wrangler.toml

> │  └── 📂 memory/

> │    ├── 📄 README_API.md

> │    ├── 📄 README_DEV.md

> │    ├── 📄 README_SECRETS.md

> │    ├── 📄 VERIFY_SETUP.md

> │    ├── 📄 package.json

> │    ├── 📄 sync-secrets.sh

> │    ├── 📄 wrangler.toml

> │  └── 📂 metadata_naming/

> │    ├── 📄 package.json

> │    ├── 📄 worker_metadata_naming.ts

> │    ├── 📄 wrangler.toml

> │  └── 📂 orchestrator/

> │    ├── 📄 OrchestratorState.ts

> │    ├── 📄 package.json

> │    ├── 📄 qios_06_workers_orchestrator.canvas

> │    ├── 📄 worker_orchestrator.ts

> │    ├── 📄 wrangler.toml

> │  └── 📂 self_heal/

> │    ├── 📄 package.json

> │    ├── 📄 worker_self_heal.ts

> │    ├── 📄 wrangler.toml

> │  └── 📂 semantic_router/

> │    ├── 📄 package.json

> │    ├── 📄 worker_semantic_router.ts

> │    ├── 📄 wrangler.toml

> └── 📂 data/

> │  └── 📂 vector/

> │    ├── 📄 qios_local.db

> ├── 📄 dns_map.yml

> └── 📂 embedder/

> │  ├── 📄 EMBEDDER_IMPROVEMENTS.md

> │  ├── 📄 EMBEDDER_SIMPLIFICATION.md

> │  ├── 📄 index.html

> │  ├── 📄 package.json

> │  ├── 📄 worker_embedder.ts

> │  ├── 📄 wrangler.toml

> └── 📂 gina/

> │  ├── 📄 _readme.md

> │  └── 📂 _shared/

> │    ├── 📄 index.html

> │  └── 📂 embedder/

> │    ├── 📄 index.html

> │    ├── 📄 worker_embedder.ts

> │  └── 📂 gina_processor/

> │    ├── 📄 _readme.md

> │    └── 📂 _shared/

> │      ├── 📄 index.html

> │    └── 📂 embedder/

> │      ├── 📄 index.html

> │      ├── 📄 worker_embedder.ts

> │    ├── 📄 index.html

> │    └── 📂 ingestion/

> │      ├── 📄 index.html

> │      ├── 📄 worker_ingestion.ts

> │    └── 📂 linter/

> │      ├── 📄 index.html

> │      ├── 📄 readme_generator.py

> │    └── 📂 metadata_naming/

> │      ├── 📄 index.html

> │    └── 📂 orchestrator/

> │      ├── 📄 OrchestratorState.ts

> │      ├── 📄 index.html

> │      ├── 📄 package.json

> │      ├── 📄 qios_06_workers_orchestrator.canvas

> │      ├── 📄 worker_orchestrator.ts

> │    └── 📂 self_heal/

> │      ├── 📄 index.html

> │      ├── 📄 worker_self_heal.ts

> │    └── 📂 semantic_router/

> │      ├── 📄 index.html

> │  ├── 📄 index.html

> │  └── 📂 ingestion/

> │    ├── 📄 index.html

> │    ├── 📄 worker_ingestion.ts

> │  └── 📂 linter/

> │    ├── 📄 index.html

> │    ├── 📄 readme_generator.py

> │  └── 📂 metadata_naming/

> │    ├── 📄 index.html

> │  └── 📂 orchestrator/

> │    ├── 📄 OrchestratorState.ts

> │    ├── 📄 index.html

> │    ├── 📄 package.json

> │    ├── 📄 qios_06_workers_orchestrator.canvas

> │    ├── 📄 worker_orchestrator.ts

> │  └── 📂 self_heal/

> │    ├── 📄 index.html

> │    ├── 📄 worker_self_heal.ts

> │  └── 📂 semantic_router/

> │    ├── 📄 index.html

> ├── 📄 index.html

> └── 📂 ingestion/

> │  ├── 📄 index.html

> │  ├── 📄 package.json

> │  ├── 📄 worker_ingestion.ts

> │  ├── 📄 wrangler.toml

> └── 📂 lina/

> │  ├── 📄 index.html

> │  ├── 📄 resourceGraphWorker.ts

> └── 📂 local_core/

> │  ├── 📄 QUICK_START.md

> │  ├── 📄 README.md

> │  ├── 📄 README_WORKER.md

> │  ├── 📄 SETUP.md

> │  ├── 📄 TESTING_ROADMAP.md

> │  ├── 📄 api_dev_history.py

> │  ├── 📄 api_gina.py

> │  ├── 📄 api_ingest.py

> │  ├── 📄 api_query.py

> │  ├── 📄 check_status.py

> │  ├── 📄 check_workers.py

> │  └── 📂 crawler/

> │    ├── 📄 __init__.py

> │    ├── 📄 vault_crawler.py

> │  ├── 📄 db.py

> │  ├── 📄 dev_error_helpers.py

> │  ├── 📄 frontmatter_utils.py

> │  ├── 📄 fs_scan_config.yaml

> │  ├── 📄 fs_scanner.py

> │  ├── 📄 gina_chat_contract.md

> │  ├── 📄 gina_chat_contract.ts

> │  ├── 📄 gina_personality_prompt.md

> │  ├── 📄 gina_prompt.py

> │  └── 📂 integrations/

> │    ├── 📄 INTEGRATION_LAYER_SUMMARY.md

> │    ├── 📄 README.md

> │    ├── 📄 __init__.py

> │    ├── 📄 base.py

> │  ├── 📄 job_processor.py

> │  ├── 📄 jobs.py

> │  ├── 📄 memory.py

> │  └── 📂 migrations/

> │    ├── 📄 001_init.sql

> │    ├── 📄 002_conversation_tables.sql

> │    ├── 📄 003_filesystem_index.sql

> │    ├── 📄 004_integration_tokens.sql

> │    ├── 📄 005_worker_status_unique.sql

> │    ├── 📄 006_add_worker_id.sql

> │    ├── 📄 007_file_registry.sql

> │    ├── 📄 008_jobs.sql

> │    ├── 📄 009_notes.sql

> │  ├── 📄 models.py

> │  ├── 📄 qios_local_core.py

> │  ├── 📄 quick_start.ps1

> │  ├── 📄 rag.py

> │  ├── 📄 requirements.txt

> │  └── 📂 scripts/

> │    ├── 📄 README.md

> │    ├── 📄 check-auth.ps1

> │    ├── 📄 check-secrets.ps1

> │    ├── 📄 deploy-all.ps1

> │    ├── 📄 deploy-critical.ps1

> │    ├── 📄 set-critical-secrets.ps1

> │    ├── 📄 set-secrets-from-env.ps1

> │    ├── 📄 sync-secrets.ps1

> │    ├── 📄 test-rag-system.ps1

> │    ├── 📄 test-with-curl.ps1

> │    ├── 📄 verify-and-test.ps1

> │  ├── 📄 start_worker.ps1

> │  ├── 📄 test_debug_ingest.ps1

> │  ├── 📄 test_ingest.py

> │  ├── 📄 test_queue_admin.ps1

> │  └── 📂 tests/

> │    ├── 📄 README.md

> │    ├── 📄 run_tests.sh

> │    ├── 📄 test_db_sanity.sql

> │    ├── 📄 test_manual_failures.md

> │    ├── 📄 test_sanity_checks.py

> │  ├── 📄 text_extractor.py

> │  └── 📂 tools/

> │  ├── 📄 tools.py

> │    ├── 📄 append_to_vault_note.py

> │    ├── 📄 calendar_create_event.py

> │    ├── 📄 calendar_get_upcoming.py

> │    ├── 📄 check_worker_status.py

> │    ├── 📄 create_vault_note.py

> │    ├── 📄 crm_create_contact.py

> │    ├── 📄 crm_create_task.py

> │    ├── 📄 crm_list_recent_contacts.py

> │    ├── 📄 crm_search_person.py

> │    ├── 📄 list_realm_files.py

> │    ├── 📄 mail_get_recent.py

> │    ├── 📄 mail_send.py

> │    ├── 📄 run_agent_command.py

> │    ├── 📄 search_processed_documents.py

> │    ├── 📄 sms_send.py

> │    ├── 📄 start_agent_service.py

> │    ├── 📄 start_worker.py

> │    ├── 📄 web_get.py

> │    ├── 📄 web_search.py

> │  ├── 📄 tools_manifest.yaml

> │  ├── 📄 worker.py

> └── 📂 metadata_naming/

> │  ├── 📄 index.html

> │  └── 📂 metadata-naming/

> │    ├── 📄 package.json

> │    ├── 📄 worker_metadata_naming.ts

> │    ├── 📄 wrangler.toml

> └── 📂 orchestrator/

> │  ├── 📄 index.html

> ├── 📄 package (2).json

> ├── 📄 package.json

> └── 📂 self_heal/

> │  ├── 📄 index.html

> └── 📂 semantic-router/

> │  ├── 📄 package.json

> │  ├── 📄 worker_semantic_router.ts

> │  └── 📄 wrangler.toml

> ```

### Assistant
> Yes. This workers folder is still a junk drawer. The fix is to make `workers/` hold only **real runtime workers**, one level clean, and push everything else out.
> 
> ## Final `workers/` tree
> 
> ```txt
> workers/
> ├─ _shared/
> │  ├─ constitution.ts
> │  ├─ heartbeat.ts
> │  └─ ignore.ts
> │
> ├─ ingestion/
> │  ├─ package.json
> │  ├─ wrangler.toml
> │  └─ src/
> │     └─ worker.ts
> │
> ├─ embedder/
> │  ├─ package.json
> │  ├─ wrangler.toml
> │  ├─ README.md
> │  └─ src/
> │     └─ worker.ts
> │
> ├─ metadata_naming/
> │  ├─ package.json
> │  ├─ wrangler.toml
> │  └─ src/
> │     └─ worker.ts
> │
> ├─ semantic_router/
> │  ├─ package.json
> │  ├─ wrangler.toml
> │  └─ src/
> │     └─ worker.ts
> │
> ├─ orchestrator/
> │  ├─ package.json
> │  ├─ wrangler.toml
> │  └─ src/
> │     ├─ worker.ts
> │     └─ OrchestratorState.ts
> │
> ├─ self_heal/
> │  ├─ package.json
> │  ├─ wrangler.toml
> │  └─ src/
> │     └─ worker.ts
> │
> ├─ resource_graph/
> │  ├─ package.json
> │  ├─ wrangler.toml
> │  └─ src/
> │     └─ worker.ts
> │
> └─ README.md
> ```
> 
> That is the clean target. Nothing else belongs live in here.
> 
> ---
> 
> # What to do with each current folder
> 
> ## Keep and normalize
> These stay, but get flattened and renamed into the structure above.
> 
> ### Keep
> - `_shared/`
> - `ingestion/`
> - `embedder/`
> - `metadata_naming/`
> - `semantic-router/` → rename to `semantic_router/`
> - `orchestrator/`
> - `self_heal/`
> - `ai/resourceGraphWorker.ts` + `lina/resourceGraphWorker.ts` → merge into `resource_graph/`
> 
> ## Delete or archive duplicates
> These are duplicate/confused copies and should not stay live in `workers/`.
> 
> ### Archive
> - `cloud/`
> - `gina/`
> - `gina/gina_processor/`
> 
> Reason: they duplicate the same worker concepts you already have at root.
> 
> ### Delete
> - `index.html` files everywhere in workers
> - `package (2).json`
> - duplicate placeholder folders with no real code
> - `metadata_naming/index.html`
> - `orchestrator/index.html`
> - `self_heal/index.html`
> 
> ## Move out of `workers/`
> These do not belong in the worker runtime layer.
> 
> ### Move to `python_core/`
> - `local_core/` → `python_core/local_services/` or split between:
>   - `python_core/agents/`
>   - `python_core/local_services/`
>   - maybe `python_core/document_processors/`
> 
> ### Move to `archive/experiments/`
> - `Tools_Launcher/`
> 
> ### Move to `apps/qione/src/features/admin/` or `docs/`
> - `cases/` if this is app/domain logic, not a worker
> - worker canvases and architecture notes that are documentation, not runtime
> 
> ### Move to `docs/architecture/`
> - `EMBEDDER_IMPROVEMENTS.md`
> - `EMBEDDER_SIMPLIFICATION.md`
> - `qios_06_workers_orchestrator.canvas`
> 
> ### Move to `content/` or root `data/` if you truly need it
> - `data/vector/qios_local.db` does **not** belong in `workers/`
> 
> ### Move to repo root config/docs if useful
> - `dns_map.yml`
> 
> ---
> 
> # Exact rename map
> 
> ```txt
> workers/semantic-router                  -> workers/semantic_router
> workers/ingestion/worker_ingestion.ts    -> workers/ingestion/src/worker.ts
> workers/embedder/worker_embedder.ts      -> workers/embedder/src/worker.ts
> workers/metadata-naming/...              -> workers/metadata_naming/src/worker.ts
> workers/semantic-router/worker_*.ts      -> workers/semantic_router/src/worker.ts
> workers/orchestrator/worker_*.ts         -> workers/orchestrator/src/worker.ts
> workers/self_heal/worker_*.ts            -> workers/self_heal/src/worker.ts
> workers/ai/resourceGraphWorker.ts        -> workers/resource_graph/src/worker.ts
> workers/lina/resourceGraphWorker.ts      -> merge into workers/resource_graph/src/worker.ts
> ```
> 
> ---
> 
> # Brutal truth on the current mess
> 
> You currently have:
> 
> - root workers
> - `cloud/` workers
> - `gina/` workers
> - `gina_processor/` workers
> - inconsistent hyphen vs underscore naming
> - HTML junk mixed in runtime folders
> - Python local service code pretending to be worker code
> 
> That is nonsense. Pick one runtime surface. The winner is the clean root worker set above.
> 
> ---
> 
> # Clean classification
> 
> ## Live runtime only
> ```txt
> _shared
> ingestion
> embedder
> metadata_naming
> semantic_router
> orchestrator
> self_heal
> resource_graph
> ```
> 
> ## Not runtime
> ```txt
> Tools_Launcher
> local_core
> cloud
> gina
> gina_processor
> data
> dns_map.yml
> html placeholders
> ```
> 
> ---
> 
> # Recommended move order
> 
> Do it in this order so you don’t fry your brain:
> 
> ### 1
> Delete garbage:
> - all `index.html`
> - `package (2).json`
> 
> ### 2
> Rename and normalize:
> - `semantic-router` → `semantic_router`
> - `metadata-naming` nesting nonsense → flatten to `metadata_naming`
> 
> ### 3
> Promote canonical workers:
> - root `ingestion`
> - root `embedder`
> - root `orchestrator`
> - root `self_heal`
> - root `semantic_router`
> - root `metadata_naming`
> 
> ### 4
> Merge resource graph:
> - `ai/resourceGraphWorker.ts`
> - `lina/resourceGraphWorker.ts`
> 
> ### 5
> Archive:
> - `cloud/`
> - `gina/`
> - `gina_processor/`
> - `Tools_Launcher/`
> 
> ### 6
> Move out:
> - `local_core/` → `python_core/local_services/`
> 
> ---
> 
> # The final rule for workers
> 
> A folder may stay in `workers/` only if it satisfies **all** of these:
> 
> - runs background logic
> - has its own runtime/deploy config
> - is not just docs
> - is not just experiments
> - is not app UI
> - is not Python local service tooling unless that is your canonical worker runtime
> 
> If it fails any of those, it moves out.
> 
> ---
> 
> # IDE prompt
> 
> ```markdown
> Clean and normalize the `workers/` directory into a single canonical runtime layer.
> 
> ## Target structure
> 
> workers/
>   _shared/
>     constitution.ts
>     heartbeat.ts
>     ignore.ts
> 
>   ingestion/
>     package.json
>     wrangler.toml
>     src/worker.ts
> 
>   embedder/
>     package.json
>     wrangler.toml
>     README.md
>     src/worker.ts
> 
>   metadata_naming/
>     package.json
>     wrangler.toml
>     src/worker.ts
> 
>   semantic_router/
>     package.json
>     wrangler.toml
>     src/worker.ts
> 
>   orchestrator/
>     package.json
>     wrangler.toml
>     src/worker.ts
>     src/OrchestratorState.ts
> 
>   self_heal/
>     package.json
>     wrangler.toml
>     src/worker.ts
> 
>   resource_graph/
>     package.json
>     wrangler.toml
>     src/worker.ts
> 
>   README.md
> 
> ## Required actions
> 
> 1. Delete junk files:
> - all `index.html` files inside `workers`
> - `package (2).json`
> 
> 2. Rename:
> - `semantic-router` -> `semantic_router`
> 
> 3. Flatten nested duplicates:
> - normalize `metadata_naming`
> - normalize `orchestrator`
> - normalize `self_heal`
> 
> 4. Merge duplicate worker implementations:
> - merge `ai/resourceGraphWorker.ts` and `lina/resourceGraphWorker.ts` into `workers/resource_graph/src/worker.ts`
> - prefer the stronger implementation and archive the weaker one if needed
> 
> 5. Archive duplicate legacy worker trees:
> - `workers/cloud/`
> - `workers/gina/`
> - `workers/gina/gina_processor/`
> - `workers/Tools_Launcher/`
> 
> Move them to:
> - `archive/legacy/workers/` for old worker trees
> - `archive/experiments/workers/` for launcher junk
> 
> 6. Move non-worker runtime code out of `workers`:
> - move `workers/local_core/` to `python_core/local_services/`
> 
> 7. Move documentation artifacts out of worker runtime folders:
> - move `EMBEDDER_IMPROVEMENTS.md`
> - move `EMBEDDER_SIMPLIFICATION.md`
> - move `qios_06_workers_orchestrator.canvas`
> to `docs/architecture/workers/`
> 
> 8. Move stray data/config out:
> - move `workers/data/vector/qios_local.db` out of `workers`
> - move `workers/dns_map.yml` to a more appropriate root docs/config area
> 
> 9. Create a clean `workers/README.md` explaining the purpose of each canonical worker.
> 
> 10. Remove empty folders after migration.
> 
> ## Guardrails
> - do not preserve duplicate worker trees live
> - do not keep html placeholder junk
> - do not keep experiments in the runtime layer
> - do not move app code into workers
> - do not leave multiple versions of the same worker concept
> 
> ## Output
> At the end, provide:
> 1. final cleaned `workers/` tree
> 2. list of archived folders
> 3. list of deleted files
> 4. list of moved files/folders
> ```
> 
> If you want, I’ll do the same cleanup pass next for `python_core/`.

### User
> d2026-03-10T23:02:18.126573Z	Cloning repository...

> 2026-03-10T23:02:28.281724Z	From https://github.com/qiallyme/_QiOne_MonoRepo_v2

> 2026-03-10T23:02:28.282382Z	 * branch            fce4b590fab5d1315dd94914940188d6e48c0ec3 -> FETCH_HEAD

> 2026-03-10T23:02:28.282462Z	

> 2026-03-10T23:02:31.114418Z	HEAD is now at fce4b59 merge repos

> 2026-03-10T23:02:31.114855Z	

> 2026-03-10T23:02:31.160999Z	

> 2026-03-10T23:02:31.161563Z	Using v2 root directory strategy

> 2026-03-10T23:02:31.175599Z	Success: Finished cloning repository files

> 2026-03-10T23:02:33.25189Z	Checking for configuration in a Wrangler configuration file (BETA)

> 2026-03-10T23:02:33.252342Z	

> 2026-03-10T23:02:34.347549Z	No Wrangler configuration file found. Continuing.

> 2026-03-10T23:02:34.562998Z	Detected the following tools from environment: npm@10.9.2, nodejs@22.16.0

> 2026-03-10T23:02:34.563342Z	Installing project dependencies: npm install --progress=false

> 2026-03-10T23:02:58.990714Z	

> 2026-03-10T23:02:58.991083Z	added 350 packages, and audited 351 packages in 24s

> 2026-03-10T23:02:58.991247Z	

> 2026-03-10T23:02:58.991381Z	143 packages are looking for funding

> 2026-03-10T23:02:58.991453Z	  run `npm fund` for details

> 2026-03-10T23:02:58.991778Z	

> 2026-03-10T23:02:58.99224Z	found 0 vulnerabilities

> 2026-03-10T23:02:59.073957Z	Executing user command: npm run build

> 2026-03-10T23:02:59.908111Z	

> 2026-03-10T23:02:59.908406Z	> qione@1.0.0 build

> 2026-03-10T23:02:59.908487Z	> next build

> 2026-03-10T23:02:59.908537Z	

> 2026-03-10T23:03:00.616884Z	⚠ No build cache found. Please configure build caching for faster rebuilds. Read more: https://nextjs.org/docs/messages/no-cache

> 2026-03-10T23:03:00.622449Z	Attention: Next.js now collects completely anonymous telemetry regarding usage.

> 2026-03-10T23:03:00.622622Z	This information is used to shape Next.js' roadmap and prioritize features.

> 2026-03-10T23:03:00.622717Z	You can learn more, including how to opt-out if you'd not like to participate in this anonymous program, by visiting the following URL:

> 2026-03-10T23:03:00.622779Z	https://nextjs.org/telemetry

> 2026-03-10T23:03:00.622846Z	

> 2026-03-10T23:03:00.63915Z	▲ Next.js 16.1.6 (Turbopack)

> 2026-03-10T23:03:00.639493Z	

> 2026-03-10T23:03:00.752934Z	  Creating an optimized production build ...

> 2026-03-10T23:03:06.877871Z	

> 2026-03-10T23:03:06.878196Z	> Build error occurred

> 2026-03-10T23:03:06.880696Z	Error: Turbopack build failed with 4 errors:

> 2026-03-10T23:03:06.881179Z	./src/app/(portal)

> 2026-03-10T23:03:06.881382Z	You cannot have two parallel pages that resolve to the same path. Please check /(app) and /(portal).

> 2026-03-10T23:03:06.88148Z	

> 2026-03-10T23:03:06.881594Z	./src/ui/styles/globals.css

> 2026-03-10T23:03:06.881684Z	Error evaluating Node.js code

> 2026-03-10T23:03:06.881733Z	Error: Cannot find module '@tailwindcss/postcss'

> 2026-03-10T23:03:06.882094Z	Require stack:

> 2026-03-10T23:03:06.882173Z	- /opt/buildhome/repo/apps/qione/.next/build/chunks/[root-of-the-server]__51225daf._.js

> 2026-03-10T23:03:06.882247Z	- /opt/buildhome/repo/apps/qione/.next/build/chunks/[turbopack]_runtime.js

> 2026-03-10T23:03:06.882326Z	- /opt/buildhome/repo/apps/qione/.next/build/postcss.js

> 2026-03-10T23:03:06.882542Z	    [at Function._resolveFilename (node:internal/modules/cjs/loader:1401:15)]

> 2026-03-10T23:03:06.882616Z	    [at defaultResolveImpl (node:internal/modules/cjs/loader:1057:19)]

> 2026-03-10T23:03:06.882664Z	    [at resolveForCJSWithHooks (node:internal/modules/cjs/loader:1062:22)]

> 2026-03-10T23:03:06.882701Z	    [at Function._load (node:internal/modules/cjs/loader:1211:37)]

> 2026-03-10T23:03:06.882786Z	    [at TracingChannel.traceSync (node:diagnostics_channel:322:14)]

> 2026-03-10T23:03:06.882892Z	    [at wrapModuleLoad (node:internal/modules/cjs/loader:235:24)]

> 2026-03-10T23:03:06.882926Z	    [at Module.require (node:internal/modules/cjs/loader:1487:12)]

> 2026-03-10T23:03:06.882957Z	    [at require (node:internal/modules/helpers:135:16)]

> 2026-03-10T23:03:06.883001Z	    at turbopack:///[turbopack-node]/transforms/postcss.ts:49:25 [/opt/buildhome/repo/apps/qione/.next/build/chunks/[root-of-the-server]__51225daf._.js:133:33]

> 2026-03-10T23:03:06.883061Z	    [at <anonymous>]

> 2026-03-10T23:03:06.883125Z	

> 2026-03-10T23:03:06.883519Z	Import trace:

> 2026-03-10T23:03:06.883607Z	  Client Component Browser:

> 2026-03-10T23:03:06.883649Z	    ./src/ui/styles/globals.css [Client Component Browser]

> 2026-03-10T23:03:06.883695Z	    ./src/app/layout.tsx [Server Component]

> 2026-03-10T23:03:06.883724Z	

> 2026-03-10T23:03:06.88375Z	

> 2026-03-10T23:03:06.883808Z	./src/app/api/qichronicle/moments/[id]/route.ts:1:1

> 2026-03-10T23:03:06.883844Z	Module not found: Can't resolve '@supabase/auth-helpers-nextjs'

> 2026-03-10T23:03:06.883882Z	[0m[31m[1m>[22m[39m[90m 1 |[39m [36mimport[39m { createRouteHandlerClient } [36mfrom[39m [32m'@supabase/auth-helpers-nextjs'[39m[33m;[39m

> 2026-03-10T23:03:06.884162Z	 [90m   |[39m [31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m

> 2026-03-10T23:03:06.884271Z	 [90m 2 |[39m [36mimport[39m { cookies } [36mfrom[39m [32m'next/headers'[39m[33m;[39m

> 2026-03-10T23:03:06.884334Z	 [90m 3 |[39m [36mimport[39m { [33mNextResponse[39m } [36mfrom[39m [32m'next/server'[39m[33m;[39m

> 2026-03-10T23:03:06.884388Z	 [90m 4 |[39m[0m

> 2026-03-10T23:03:06.884436Z	

> 2026-03-10T23:03:06.884491Z	

> 2026-03-10T23:03:06.884557Z	

> 2026-03-10T23:03:06.88462Z	https://nextjs.org/docs/messages/module-not-found

> 2026-03-10T23:03:06.884714Z	

> 2026-03-10T23:03:06.884753Z	

> 2026-03-10T23:03:06.884788Z	./src/app/api/qichronicle/moments/route.ts:1:1

> 2026-03-10T23:03:06.884822Z	Module not found: Can't resolve '@supabase/auth-helpers-nextjs'

> 2026-03-10T23:03:06.884851Z	[0m[31m[1m>[22m[39m[90m 1 |[39m [36mimport[39m { createRouteHandlerClient } [36mfrom[39m [32m'@supabase/auth-helpers-nextjs'[39m[33m;[39m

> 2026-03-10T23:03:06.884882Z	 [90m   |[39m [31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m[31m[1m^[22m[39m

> 2026-03-10T23:03:06.884946Z	 [90m 2 |[39m [36mimport[39m { cookies } [36mfrom[39m [32m'next/headers'[39m[33m;[39m

> 2026-03-10T23:03:06.884985Z	 [90m 3 |[39m [36mimport[39m { [33mNextResponse[39m } [36mfrom[39m [32m'next/server'[39m[33m;[39m

> 2026-03-10T23:03:06.885016Z	 [90m 4 |[39m[0m

> 2026-03-10T23:03:06.885096Z	

> 2026-03-10T23:03:06.885161Z	

> 2026-03-10T23:03:06.885198Z	

> 2026-03-10T23:03:06.885243Z	https://nextjs.org/docs/messages/module-not-found

> 2026-03-10T23:03:06.885277Z	

> 2026-03-10T23:03:06.885306Z	

> 2026-03-10T23:03:06.885334Z	    at <unknown> (./src/app/api/qichronicle/moments/[id]/route.ts:1:1)

> 2026-03-10T23:03:06.885367Z	    at <unknown> (https://nextjs.org/docs/messages/module-not-found)

> 2026-03-10T23:03:06.885418Z	    at <unknown> (./src/app/api/qichronicle/moments/route.ts:1:1)

> 2026-03-10T23:03:06.885452Z	    at <unknown> (https://nextjs.org/docs/messages/module-not-found)

> 2026-03-10T23:03:07.026802Z	Failed: Error while executing user command. Exited with error code: 1

> 2026-03-10T23:03:07.034289Z	Failed: build command exited with code: 1

> 2026-03-10T23:03:08.133282Z	Failed: error occurred while running build command

### Assistant
> You’ve got **three separate failures**, and they’re all real.
> 
> ## What broke
> 
> ### 1. Route collision
> You have both `src/app/(app)` and `src/app/(portal)` active in the same Next app, so Next sees two parallel route groups resolving to overlapping paths. Your tree shows both groups live under `apps/qione/src/app` fileciteturn2file0
> 
> **Fix:** kill or archive `(portal)` now.  
> Keep `(app)`, `(public)`, `api`, and maybe `(auth)` if you actually need it.
> 
> ### 2. Missing PostCSS package
> Your build is trying to load `@tailwindcss/postcss` from `./src/ui/styles/globals.css`, but that package is not installed.
> 
> **Fix options:**
> - install the package:
> ```bash
> npm i -D @tailwindcss/postcss
> ```
> - or remove the config/import path that expects it
> - also decide whether `src/ui/styles/globals.css` is even canonical, because your current tree also has `src/styles/globals.css` live, which smells like duplicate style roots fileciteturn2file0
> 
> ### 3. Missing Supabase auth package
> These routes are importing `@supabase/auth-helpers-nextjs`:
> - `src/app/api/qichronicle/moments/route.ts`
> - `src/app/api/qichronicle/moments/[id]/route.ts`
> 
> Your tree confirms `api/qichronicle` still exists alongside the newer `api/chronicle` structure fileciteturn2file0
> 
> **Fix:** either:
> - install it:
> ```bash
> npm i @supabase/auth-helpers-nextjs
> ```
> - or, better, migrate those old routes to your current Supabase client pattern and delete `api/qichronicle`
> 
> ---
> 
> # The real cleanup order
> 
> Do this in order:
> 
> ## First
> Archive/delete the old route group:
> ```txt
> src/app/(portal)
> ```
> 
> ## Second
> Archive/delete old chronicle API:
> ```txt
> src/app/api/qichronicle
> ```
> 
> You already have:
> ```txt
> src/app/(app)/chronicle
> src/app/api/chronicle
> ```
> So `qichronicle` is legacy duplication.
> 
> ## Third
> Pick **one** global CSS location:
> - keep `src/styles/globals.css`
> - remove `src/ui/styles/globals.css` imports
> 
> ## Fourth
> Install missing dependency only if you still need it:
> ```bash
> npm i -D @tailwindcss/postcss
> ```
> 
> ## Fifth
> If any old code still depends on it, either install:
> ```bash
> npm i @supabase/auth-helpers-nextjs
> ```
> or finish removing the legacy routes that require it.
> 
> ---
> 
> # Blunt diagnosis
> 
> Your build is failing because the repo is **half-migrated**:
> - new structure is present
> - old structure is still live
> - old deps are still referenced
> - duplicate route trees are still active
> 
> That’s normal for this stage, but it means you do **not** need to “debug Cloudflare.”  
> You need to finish the repo cleanup.
> 
> ---
> 
> # Minimal fix set to get a build fastest
> 
> ```bash
> # 1. remove/archive old route group
> src/app/(portal)
> 
> # 2. remove/archive old api routes
> src/app/api/qichronicle
> 
> # 3. install missing style dependency
> npm i -D @tailwindcss/postcss
> 
> # 4. if any route still imports it, install supabase helper
> npm i @supabase/auth-helpers-nextjs
> ```
> 
> ---
> 
> # What I would do
> I would **not** keep `(portal)` or `api/qichronicle`. They are old ghosts. Your uploaded tree already shows the newer `(app)` and `api/chronicle` structure, so keeping both is pointless fileciteturn2file0
> 
> Paste me your `apps/qione/package.json` and `apps/qione/src/app/layout.tsx`, and I’ll tell you the exact smallest edits to make this deploy cleanly.
