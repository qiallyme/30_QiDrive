---
layout: page
title: "Branch · Tmux Codex Commands"
slug: "branch_tmux_codex_commands"
created_at: "2026-06-13 11:24:17"
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
uid: "6a2d842c-5b80-83ea-8ce4-78242848d0b4"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Branch · Tmux Codex Commands

## Overview
- **Date**: 2026-06-13 11:24:17
- **Conversation ID**: `6a2d842c-5b80-83ea-8ce4-78242848d0b4`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> ok so i am at my server terminal and i want to pull up the tmux running with codex, but i dont knwo the commands, question one, what is the command and questions two, how do i save these commands somewhere easy to use and access for the future.

### Assistant
> ## 1) Pull up the running tmux session
> 
> At your server terminal, run:
> 
> ```bash
> tmux ls
> ```
> 
> That lists active sessions.
> 
> Then attach to the one running Codex:
> 
> ```bash
> tmux attach -t SESSION_NAME
> ```
> 
> Example:
> 
> ```bash
> tmux attach -t codex
> ```
> 
> If there is only one tmux session, this usually works:
> 
> ```bash
> tmux attach
> ```
> 
> ### Useful tmux exits
> 
> Detach without killing Codex:
> 
> ```text
> Ctrl+b, then d
> ```
> 
> Kill the session only if you mean it:
> 
> ```bash
> tmux kill-session -t SESSION_NAME
> ```
> 
> Do **not** casually kill it. That ends the running Codex session. Tiny chaos button. Avoid.
> 
> ---
> 
> ## 2) Save these commands somewhere easy
> 
> Best answer: make yourself a tiny command cheat sheet **and** a shortcut script.
> 
> ### Option A — create a terminal cheat sheet
> 
> Run:
> 
> ```bash
> mkdir -p ~/notes
> nano ~/notes/tmux-codex.md
> ```
> 
> Paste this:
> 
> ```md
> # tmux / Codex commands
> 
> List sessions:
> tmux ls
> 
> Attach to session:
> tmux attach -t SESSION_NAME
> 
> Attach if only one session:
> tmux attach
> 
> Detach safely:
> Ctrl+b, then d
> 
> Kill session:
> tmux kill-session -t SESSION_NAME
> ```
> 
> Save in nano:
> 
> ```text
> Ctrl+O
> Enter
> Ctrl+X
> ```
> 
> Then anytime:
> 
> ```bash
> cat ~/notes/tmux-codex.md
> ```
> 
> ---
> 
> ### Option B — make a shortcut command
> 
> This is cleaner.
> 
> Run:
> 
> ```bash
> nano ~/.bashrc
> ```
> 
> Add this at the bottom:
> 
> ```bash
> alias tls='tmux ls'
> alias ta='tmux attach -t'
> alias codex-tmux='tmux attach -t codex'
> alias tmux-help='cat ~/notes/tmux-codex.md'
> ```
> 
> Save:
> 
> ```text
> Ctrl+O
> Enter
> Ctrl+X
> ```
> 
> Reload:
> 
> ```bash
> source ~/.bashrc
> ```
> 
> Now you can use:
> 
> ```bash
> tls
> ```
> 
> to list sessions,
> 
> ```bash
> ta codex
> ```
> 
> to attach to Codex,
> 
> or:
> 
> ```bash
> codex-tmux
> ```
> 
> if the session is named `codex`.
> 
> ---
> 
> ## What I’d do right now
> 
> Run this first:
> 
> ```bash
> tmux ls
> ```
> 
> Then whatever session name shows up, attach like:
> 
> ```bash
> tmux attach -t whatever-name-shows-here
> ```
> 
> After that, create the cheat sheet and aliases. That way future-you doesn’t have to rediscover basic tmux commands while already annoyed.

### User
> ok, i will work on this later for now, where should i store the csv files i exported from notion and zoho to later be converted migrated to our database we are working on w.

### Assistant
> Store them in **QiNexus intake**, not randomly in Downloads.
> 
> Use this structure:
> 
> ```text
> C:\QiLabs\50_QiNexus\My Drive\00_Intake\20_Data_Migration\
> ```
> 
> Then split by source:
> 
> ```text
> C:\QiLabs\50_QiNexus\My Drive\00_Intake\20_Data_Migration\Notion\
> C:\QiLabs\50_QiNexus\My Drive\00_Intake\20_Data_Migration\Zoho\
> ```
> 
> Inside each one:
> 
> ```text
> 00_raw_exports\
> 10_cleaned_exports\
> 20_mapping_notes\
> 30_ready_for_import\
> 90_archive\
> ```
> 
> So the real destination is:
> 
> ```text
> C:\QiLabs\50_QiNexus\My Drive\00_Intake\20_Data_Migration\Notion\00_raw_exports\
> C:\QiLabs\50_QiNexus\My Drive\00_Intake\20_Data_Migration\Zoho\00_raw_exports\
> ```
> 
> ## File naming
> 
> Use boring names. Boring wins.
> 
> ```text
> YYYY-MM-DD_source_exportname_raw.csv
> ```
> 
> Examples:
> 
> ```text
> 2026-06-13_notion_tasks_raw.csv
> 2026-06-13_notion_clients_raw.csv
> 2026-06-13_zoho_contacts_raw.csv
> 2026-06-13_zoho_invoices_raw.csv
> ```
> 
> ## Rule
> 
> **Do not edit the raw CSVs.**  
> Raw exports are evidence/source-of-truth snapshots.
> 
> When we clean or transform them, copy them into:
> 
> ```text
> 10_cleaned_exports
> ```
> 
> When they are mapped and ready for Supabase/database import:
> 
> ```text
> 30_ready_for_import
> ```
> 
> ## Tiny note file to add
> 
> In each source folder, create:
> 
> ```text
> README.md
> ```
> 
> Put:
> 
> ```text
> Source:
> Export date:
> Exported from:
> Purpose:
> Notes:
> ```
> 
> This keeps future-you from opening 40 mystery CSVs and cussing at past-you.

### User
> is qi server with everything that should be in that module {

>   "name": "30_QiServer",

>   "path": "c:\\QiLabs\\30_QiServer",

>   "type": "directory",

>   "children": [

>     {

>       "name": "backups",

>       "type": "folder"

>     },

>     {

>       "name": "cloudflare",

>       "type": "folder"

>     },

>     {

>       "name": "data",

>       "type": "folder",

>       "children": [

>         {

>           "name": "MMEX",

>           "type": "folder",

>           "children": [

>             {

>               "name": "moneydb.mmb",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "csv",

>           "type": "folder",

>           "children": [

>             {

>               "name": "20251116_biz_ai_kb_full.csv",

>               "type": "file"

>             },

>             {

>               "name": "20251116_biz_blueprints_workflows_list.csv",

>               "type": "file"

>             },

>             {

>               "name": "20251116_biz_drive_health_tracker_full.csv",

>               "type": "file"

>             },

>             {

>               "name": "20251116_biz_it_tools_inventory_full.csv",

>               "type": "file"

>             },

>             {

>               "name": "20251116_biz_mandated_training_full.csv",

>               "type": "file"

>             },

>             {

>               "name": "20251116_biz_pricing_category_feature.csv",

>               "type": "file"

>             },

>             {

>               "name": "20251116_biz_unified_data_sheet.csv",

>               "type": "file"

>             },

>             {

>               "name": "AES_Usage_Timeline.csv",

>               "type": "file"

>             },

>             {

>               "name": "API Recovery Keys & Related.csv",

>               "type": "file"

>             },

>             {

>               "name": "Blueprints and Workflows Lists 1b8f84a0440281bf8a61e310341c1f4e_all.csv",

>               "type": "file"

>             },

>             {

>               "name": "Chrome Passwords.csv",

>               "type": "file"

>             },

>             {

>               "name": "Company_Details_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "Core Registry 277f84a044028064be05eb377973ee4e_all.csv",

>               "type": "file"

>             },

>             {

>               "name": "Core Registry.csv",

>               "type": "file"

>             },

>             {

>               "name": "Currency_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "DNS Settings 1ccf84a044028062b0d0f53e3ac73bc3_all.csv",

>               "type": "file"

>             },

>             {

>               "name": "Domains 1caf84a0440281329311ff8f52bcb6d6_all.csv",

>               "type": "file"

>             },

>             {

>               "name": "Domains.csv",

>               "type": "file"

>             },

>             {

>               "name": "Drive Health Tracker.csv",

>               "type": "file"

>             },

>             {

>               "name": "Emails_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "FieldDependencyRelation_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "Fields_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "Flow Docs_C_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "IT Tools Systems Software Inventory.csv",

>               "type": "file"

>             },

>             {

>               "name": "Internal COA (OS).csv",

>               "type": "file"

>             },

>             {

>               "name": "Invitees_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "Invoices_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "LayoutFieldProperties_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "Layout_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "Meetings_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "Modules_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "Notes_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "Notes_Contacts_2025_08_31.csv",

>               "type": "file"

>             },

>             {

>               "name": "Notifications 20df84a04402800588c0ede6eaabefb3_all.csv",

>               "type": "file"

>             },

>             {

>               "name": "Notifications.csv",

>               "type": "file"

>             },

>             {

>               "name": "Ordered Items_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "PickListFieldProperties_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "Posts 139f84a044028193a945f14394f08053_all.csv",

>               "type": "file"

>             },

>             {

>               "name": "Products_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "Profiles_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "Programming Languages 5e783f64b8db430d87f79656eafb588e_all.csv",

>               "type": "file"

>             },

>             {

>               "name": "QiCode_Chart_of_Accounts_Mapping.csv",

>               "type": "file"

>             },

>             {

>               "name": "Quoted Items_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "Roles_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "SOFI-Checking-7940-2025-10-31T12_45_50.csv",

>               "type": "file"

>             },

>             {

>               "name": "Sales Orders_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "Social Channels.csv",

>               "type": "file"

>             },

>             {

>               "name": "Solutions_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "StickyNotes_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "Translation_Codes_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "Translation_Language_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "Triggers Detail 1e1f84a0440281ed9e4fdac4463a497c_all.csv",

>               "type": "file"

>             },

>             {

>               "name": "Triggers Detail.csv",

>               "type": "file"

>             },

>             {

>               "name": "Untitled_1.csv",

>               "type": "file"

>             },

>             {

>               "name": "Vendors_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "businesses_2025-11-09_6.csv",

>               "type": "file"

>             },

>             {

>               "name": "card_list_combined.csv",

>               "type": "file"

>             },

>             {

>               "name": "contact_merged.csv",

>               "type": "file"

>             },

>             {

>               "name": "contacts_cleaned.csv",

>               "type": "file"

>             },

>             {

>               "name": "conversations.csv",

>               "type": "file"

>             },

>             {

>               "name": "db_Coins Database 169f84a0440280a790b0e7e2a0db38a9_all.csv",

>               "type": "file"

>             },

>             {

>               "name": "db_RawEmails_KB 23550d1b26bb4b28a71867c584e55805_all.csv",

>               "type": "file"

>             },

>             {

>               "name": "db_RawEmails_KB.csv",

>               "type": "file"

>             },

>             {

>               "name": "docket.csv",

>               "type": "file"

>             },

>             {

>               "name": "file_system_nodes.csv",

>               "type": "file"

>             },

>             {

>               "name": "fs_ignore_v1.csv",

>               "type": "file"

>             },

>             {

>               "name": "gina_memory_rows.csv",

>               "type": "file"

>             },

>             {

>               "name": "ignore_list_v1.csv",

>               "type": "file"

>             },

>             {

>               "name": "internal_coa_os__all.csv",

>               "type": "file"

>             },

>             {

>               "name": "master_services_catalog__all.csv",

>               "type": "file"

>             },

>             {

>               "name": "qimessages_C_001.csv",

>               "type": "file"

>             },

>             {

>               "name": "qios_matrix.csv",

>               "type": "file"

>             },

>             {

>               "name": "raw_emails_combined.csv",

>               "type": "file"

>             },

>             {

>               "name": "reading_journal__all.csv",

>               "type": "file"

>             },

>             {

>               "name": "realms_registry.csv",

>               "type": "file"

>             },

>             {

>               "name": "sensitivity_classification_matrix_v1.csv",

>               "type": "file"

>             },

>             {

>               "name": "sensitivity_classification_registry.csv",

>               "type": "file"

>             },

>             {

>               "name": "service_matrix.csv",

>               "type": "file"

>             },

>             {

>               "name": "untitled.csv",

>               "type": "file"

>             },

>             {

>               "name": "vendors_merged.csv",

>               "type": "file"

>             },

>             {

>               "name": "zai-vitals.csv",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "devices",

>           "type": "folder",

>           "children": [

>             {

>               "name": "this-device",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": "capabilities.json",

>                   "type": "file"

>                 },

>                 {

>                   "name": "device.json",

>                   "type": "file"

>                 },

>                 {

>                   "name": "last_heartbeat.json",

>                   "type": "file"

>                 },

>                 {

>                   "name": "watcher_assignments.json",

>                   "type": "file"

>                 }

>               ]

>             }

>           ]

>         },

>         {

>           "name": "docs",

>           "type": "folder",

>           "children": [

>             {

>               "name": "notes",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": "discussion26-07-01.md",

>                   "type": "file"

>                 }

>               ]

>             },

>             {

>               "name": "prompts",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": "cockpit_gui_prompt.md",

>                   "type": "file"

>                 }

>               ]

>             },

>             {

>               "name": "INTEGRATION_COMPLETE.md",

>               "type": "file"

>             },

>             {

>               "name": "PART_X_Resource_Opportunity_Graph.md",

>               "type": "file"

>             },

>             {

>               "name": "QiAlly Call Ecosystem & Gina Voice Architecture.md",

>               "type": "file"

>             },

>             {

>               "name": "gina_n8n_workflows.md",

>               "type": "file"

>             },

>             {

>               "name": "index.html",

>               "type": "file"

>             },

>             {

>               "name": "integration_summary.md",

>               "type": "file"

>             },

>             {

>               "name": "launcher_ui_mindmap.md",

>               "type": "file"

>             },

>             {

>               "name": "markdownlint_analysis_genesis.md",

>               "type": "file"

>             },

>             {

>               "name": "markdownlint_analysis_remaining.md",

>               "type": "file"

>             },

>             {

>               "name": "markdownlint_final_analysis.md",

>               "type": "file"

>             },

>             {

>               "name": "markdownlint_quick_reference.md",

>               "type": "file"

>             },

>             {

>               "name": "markdownlint_review_summary.md",

>               "type": "file"

>             },

>             {

>               "name": "markdownlint_summary.md",

>               "type": "file"

>             },

>             {

>               "name": "ui_contracts_v1.md",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "dropzones",

>           "type": "folder",

>           "children": [

>             {

>               "name": "default",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": ".gitkeep",

>                   "type": "file"

>                 }

>               ]

>             },

>             {

>               "name": "imports",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": ".gitkeep",

>                   "type": "file"

>                 }

>               ]

>             },

>             {

>               "name": "mobile",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": ".gitkeep",

>                   "type": "file"

>                 }

>               ]

>             },

>             {

>               "name": "scans",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": "scan-snap",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "2026-04-01.pdf",

>                       "type": "file"

>                     },

>                     {

>                       "name": "2026-04-01_A. Allegation of _Unauthorized Pel.pdf",

>                       "type": "file"

>                     },

>                     {

>                       "name": "2026-04-01_Department of Treasury Internal Revenue Service IRS Tax Professional PTIN Processing Center PO Box 380638 San Antonio, TX 78268.pdf",

>                       "type": "file"

>                     },

>                     {

>                       "name": "2026-04-01_Department of Treasury Internal Revenue Service IRS Tax Professional PTIN Processing Center PO Box 380638 San Antonio, TX 78268_001.pdf",

>                       "type": "file"

>                     },

>                     {

>                       "name": "2026-04-01_FCFCU-card received during case.pdf",

>                       "type": "file"

>                     },

>                     {

>                       "name": "2026-04-01_INVOICE.pdf",

>                       "type": "file"

>                     },

>                     {

>                       "name": "2026-04-01_INVOICE_001.pdf",

>                       "type": "file"

>                     },

>                     {

>                       "name": "2026-04-01_If you do not attend the hearing in this case, the  j.pdf",

>                       "type": "file"

>                     },

>                     {

>                       "name": "2026-04-01_PTIN.pdf",

>                       "type": "file"

>                     },

>                     {

>                       "name": "2026-04-01_UMTim.pdf",

>                       "type": "file"

>                     },

>                     {

>                       "name": "2026-04-01_Wrect.pdf",

>                       "type": "file"

>                     },

>                     {

>                       "name": "2026-04-01_Your subscription payment is due..pdf",

>                       "type": "file"

>                     },

>                     {

>                       "name": "2026-04-01_n_‘-‘ Person IWant to Make Care Decisio-.pdf",

>                       "type": "file"

>                     },

>                     {

>                       "name": "2026-04-01_paysign.pdf",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": ".gitkeep",

>                   "type": "file"

>                 }

>               ]

>             },

>             {

>               "name": "README.md",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "embeddings_cache",

>           "type": "folder",

>           "children": [

>             {

>               "name": ".gitkeep",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "extracted_text",

>           "type": "folder",

>           "children": [

>             {

>               "name": ".gitkeep",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "failed",

>           "type": "folder",

>           "children": [

>             {

>               "name": ".gitkeep",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "inbox",

>           "type": "folder",

>           "children": [

>             {

>               "name": ".gitkeep",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "json",

>           "type": "folder",

>           "children": [

>             {

>               "name": "QiRealms_seed.json",

>               "type": "file"

>             },

>             {

>               "name": "QiTagClasses_schema.json",

>               "type": "file"

>             },

>             {

>               "name": "QiTags_seed.json",

>               "type": "file"

>             },

>             {

>               "name": "bio_contact_info.json",

>               "type": "file"

>             },

>             {

>               "name": "client_memberships_rows.json",

>               "type": "file"

>             },

>             {

>               "name": "eos_frontmatter.schema.json",

>               "type": "file"

>             },

>             {

>               "name": "frontmatter.schema.json",

>               "type": "file"

>             },

>             {

>               "name": "intake_form_schema.json",

>               "type": "file"

>             },

>             {

>               "name": "kb_spaces_rows.json",

>               "type": "file"

>             },

>             {

>               "name": "message_feedback.json",

>               "type": "file"

>             },

>             {

>               "name": "portfolio-content.json",

>               "type": "file"

>             },

>             {

>               "name": "portfolio-projects.json",

>               "type": "file"

>             },

>             {

>               "name": "qios_constitution_schema_v1.json",

>               "type": "file"

>             },

>             {

>               "name": "qios_constitution_v1.json",

>               "type": "file"

>             },

>             {

>               "name": "slugs_mapping.json",

>               "type": "file"

>             },

>             {

>               "name": "systemInfoCMD.json",

>               "type": "file"

>             },

>             {

>               "name": "user.json",

>               "type": "file"

>             },

>             {

>               "name": "voice_mapper_rules.json",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "legacy",

>           "type": "folder",

>           "children": [

>             {

>               "name": "QiCodex.csv",

>               "type": "file"

>             },

>             {

>               "name": "manifest.txt",

>               "type": "file"

>             },

>             {

>               "name": "opensourcetools.txt",

>               "type": "file"

>             },

>             {

>               "name": "qios_00_genesis.canvas",

>               "type": "file"

>             },

>             {

>               "name": "qios_runtime_mindmap.canvas",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "logs",

>           "type": "folder",

>           "children": [

>             {

>               "name": "ingest",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": ".gitkeep",

>                   "type": "file"

>                 }

>               ]

>             },

>             {

>               "name": "local-agent",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": ".gitkeep",

>                   "type": "file"

>                 }

>               ]

>             },

>             {

>               "name": "runtime",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": ".gitkeep",

>                   "type": "file"

>                 }

>               ]

>             },

>             {

>               "name": "sync",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": ".gitkeep",

>                   "type": "file"

>                 }

>               ]

>             }

>           ]

>         },

>         {

>           "name": "lumara",

>           "type": "folder",

>           "children": [

>             {

>               "name": "assets",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": "imgs",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "cover.jpeg",

>                       "type": "file"

>                     },

>                     {

>                       "name": "icon.jpeg",

>                       "type": "file"

>                     },

>                     {

>                       "name": "icon.png",

>                       "type": "file"

>                     },

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     },

>                     {

>                       "name": "logo.jpeg",

>                       "type": "file"

>                     },

>                     {

>                       "name": "square.jpeg",

>                       "type": "file"

>                     }

>                   ]

>                 }

>               ]

>             },

>             {

>               "name": "db",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": "index.html",

>                   "type": "file"

>                 },

>                 {

>                   "name": "lumara_schema_resource_graph.sql",

>                   "type": "file"

>                 }

>               ]

>             },

>             {

>               "name": "js",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": "lina-api-client.js",

>                   "type": "file"

>                 },

>                 {

>                   "name": "lina-widget-drop.js",

>                   "type": "file"

>                 },

>                 {

>                   "name": "lina-widget.js",

>                   "type": "file"

>                 }

>               ]

>             },

>             {

>               "name": "QiMobileResourcetolumar.md",

>               "type": "file"

>             },

>             {

>               "name": "lumara_resource_graph_investor_section.md",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "manifests",

>           "type": "folder",

>           "children": [

>             {

>               "name": ".gitkeep",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "migrations",

>           "type": "folder",

>           "children": [

>             {

>               "name": "index.html",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "model_cache",

>           "type": "folder",

>           "children": [

>             {

>               "name": ".gitkeep",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "normalized",

>           "type": "folder",

>           "children": [

>             {

>               "name": ".gitkeep",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "outputs",

>           "type": "folder",

>           "children": [

>             {

>               "name": "index.html",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "posts",

>           "type": "folder",

>           "children": [

>             {

>               "name": "2026",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": "2026-02-19_post-title",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "assets",

>                       "type": "folder",

>                       "children": [

>                         {

>                           "name": "brief.m4a",

>                           "type": "file"

>                         },

>                         {

>                           "name": "critique.m4a",

>                           "type": "file"

>                         },

>                         {

>                           "name": "debate.m4a",

>                           "type": "file"

>                         },

>                         {

>                           "name": "deepdive.m4a",

>                           "type": "file"

>                         },

>                         {

>                           "name": "explainer.mp4",

>                           "type": "file"

>                         },

>                         {

>                           "name": "hero.jpg",

>                           "type": "file"

>                         },

>                         {

>                           "name": "infographic.jpg",

>                           "type": "file"

>                         }

>                       ]

>                     },

>                     {

>                       "name": "index.md",

>                       "type": "file"

>                     }

>                   ]

>                 }

>               ]

>             },

>             {

>               "name": "index.md",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "previews",

>           "type": "folder",

>           "children": [

>             {

>               "name": ".gitkeep",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "processing",

>           "type": "folder",

>           "children": [

>             {

>               "name": ".gitkeep",

>               "type": "file"

>             },

>             {

>               "name": "README_Q6CFA05.md",

>               "type": "file"

>             },

>             {

>               "name": "README_Q9F2A58.md",

>               "type": "file"

>             },

>             {

>               "name": "test_tmp1pzzpqaq_Q7579B5.txt",

>               "type": "file"

>             },

>             {

>               "name": "test_tmp24462bb9_QA3EB4F.txt",

>               "type": "file"

>             },

>             {

>               "name": "test_tmpq7_y0ey4_Q1FC037.txt",

>               "type": "file"

>             },

>             {

>               "name": "tmp2peyi7y3_Q890C10.txt",

>               "type": "file"

>             },

>             {

>               "name": "tmpp8arr_kv_Q637D6F.txt",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "qios_cursor_prompts",

>           "type": "folder",

>           "children": [

>             {

>               "name": "index.html",

>               "type": "file"

>             },

>             {

>               "name": "install_ingestion_worker.md",

>               "type": "file"

>             },

>             {

>               "name": "project_prompt.md.md",

>               "type": "file"

>             },

>             {

>               "name": "qicompiler_add_prompt.md",

>               "type": "file"

>             },

>             {

>               "name": "qicompiler_orchestrator_prompt.md",

>               "type": "file"

>             },

>             {

>               "name": "qimatrix_csv_prompt.md",

>               "type": "file"

>             },

>             {

>               "name": "qimatrix_sql_prompt.md",

>               "type": "file"

>             },

>             {

>               "name": "qimatrix_yaml_prompt.md",

>               "type": "file"

>             },

>             {

>               "name": "step3_tree_compiler_prompt.md",

>               "type": "file"

>             },

>             {

>               "name": "user_prompt.md.md",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "quarantine",

>           "type": "folder",

>           "children": [

>             {

>               "name": ".gitkeep",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "reviewed",

>           "type": "folder",

>           "children": [

>             {

>               "name": ".gitkeep",

>               "type": "file"

>             },

>             {

>               "name": "README_Q6CFA05.md",

>               "type": "file"

>             },

>             {

>               "name": "README_Q9F2A58.md",

>               "type": "file"

>             },

>             {

>               "name": "tmpp8arr_kv_Q637D6F.txt",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "schemas",

>           "type": "folder",

>           "children": [

>             {

>               "name": "index.html",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "seeds",

>           "type": "folder",

>           "children": [

>             {

>               "name": "seeds",

>               "type": "folder"

>             },

>             {

>               "name": "index.html",

>               "type": "file"

>             },

>             {

>               "name": "supabase_seed_qid.sql",

>               "type": "file"

>             },

>             {

>               "name": "supabase_seed_realms.sql",

>               "type": "file"

>             },

>             {

>               "name": "supabase_seed_rules.sql",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "sheets",

>           "type": "folder",

>           "children": [

>             {

>               "name": "front_matter_schema_v1.csv",

>               "type": "file"

>             },

>             {

>               "name": "fs_ignore_v1.csv",

>               "type": "file"

>             },

>             {

>               "name": "index.html",

>               "type": "file"

>             },

>             {

>               "name": "qios_rules_v1_1.csv",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "sites_QiAlly.com",

>           "type": "folder",

>           "children": [

>             {

>               "name": "assets",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": "css",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "styles.css",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "files",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "index.md",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "js",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "main.js",

>                       "type": "file"

>                     }

>                   ]

>                 }

>               ]

>             },

>             {

>               "name": "cody",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": "index.html",

>                   "type": "file"

>                 }

>               ]

>             },

>             {

>               "name": "functions",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": "[[path]].js",

>                   "type": "file"

>                 }

>               ]

>             },

>             {

>               "name": "kb",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": "accounting-cleanup",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "getting-started",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "irs-notices",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "tax-resolution",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "index.html",

>                   "type": "file"

>                 }

>               ]

>             },

>             {

>               "name": "modules",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": "hr-ops",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "it-ai",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "qisuite",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "taxes",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "tax-prep-2025",

>                       "type": "folder",

>                       "children": [

>                         {

>                           "name": "next-steps",

>                           "type": "folder",

>                           "children": [

>                             {

>                               "name": "index.html",

>                               "type": "file"

>                             }

>                           ]

>                         },

>                         {

>                           "name": "FormsQRCode.png",

>                           "type": "file"

>                         },

>                         {

>                           "name": "bookingQRCode.png",

>                           "type": "file"

>                         },

>                         {

>                           "name": "index.html",

>                           "type": "file"

>                         },

>                         {

>                           "name": "prompts.md",

>                           "type": "file"

>                         },

>                         {

>                           "name": "tax-prep-2025-intake.html",

>                           "type": "file"

>                         },

>                         {

>                           "name": "taxprepqially.jpg",

>                           "type": "file"

>                         }

>                       ]

>                     },

>                     {

>                       "name": "year-end-process",

>                       "type": "folder",

>                       "children": [

>                         {

>                           "name": "index.html",

>                           "type": "file"

>                         }

>                       ]

>                     },

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "index.html",

>                   "type": "file"

>                 }

>               ]

>             },

>             {

>               "name": "pages",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": "budgets",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "business_tools",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "chat",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     },

>                     {

>                       "name": "sales-iq-landing-page-qr-code.png",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "compliance",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "internal",

>                       "type": "folder",

>                       "children": [

>                         {

>                           "name": "provider-agreements",

>                           "type": "folder",

>                           "children": [

>                             {

>                               "name": "index.html",

>                               "type": "file"

>                             }

>                           ]

>                         },

>                         {

>                           "name": "training-logs",

>                           "type": "folder",

>                           "children": [

>                             {

>                               "name": "index.html",

>                               "type": "file"

>                             }

>                           ]

>                         }

>                       ]

>                     },

>                     {

>                       "name": "service_animal_gigi",

>                       "type": "folder",

>                       "children": [

>                         {

>                           "name": "assets",

>                           "type": "folder",

>                           "children": [

>                             {

>                               "name": "gigi_service_dog_hero.png",

>                               "type": "file"

>                             }

>                           ]

>                         },

>                         {

>                           "name": "Gigi_Certification_Statement.html",

>                           "type": "file"

>                         },

>                         {

>                           "name": "Gigi_Documentation_Pack.md",

>                           "type": "file"

>                         },

>                         {

>                           "name": "Gigi_Documentation_Pack_Print.html",

>                           "type": "file"

>                         },

>                         {

>                           "name": "Gigi_Service_Dog_Training_Manual.md",

>                           "type": "file"

>                         },

>                         {

>                           "name": "Gigi_Services_Dog_Training_Manual_Print.html",

>                           "type": "file"

>                         },

>                         {

>                           "name": "Notice_Service_Animal_Status.html",

>                           "type": "file"

>                         },

>                         {

>                           "name": "index.html",

>                           "type": "file"

>                         }

>                       ]

>                     },

>                     {

>                       "name": "data-inventory.html",

>                       "type": "file"

>                     },

>                     {

>                       "name": "incident-response.html",

>                       "type": "file"

>                     },

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     },

>                     {

>                       "name": "risk-assessment.html",

>                       "type": "file"

>                     },

>                     {

>                       "name": "wisp-core.html",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "ecard",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "cody.vcf",

>                       "type": "file"

>                     },

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "estate-planning",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "letters",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "client.wiletvaldo_calderon-ramirez",

>                       "type": "folder",

>                       "children": [

>                         {

>                           "name": "index.html",

>                           "type": "file"

>                         },

>                         {

>                           "name": "infographic.png",

>                           "type": "file"

>                         },

>                         {

>                           "name": "review_audio.m4a",

>                           "type": "file"

>                         }

>                       ]

>                     },

>                     {

>                       "name": "engagement",

>                       "type": "folder",

>                       "children": [

>                         {

>                           "name": "SignForm_URL_QR.png",

>                           "type": "file"

>                         },

>                         {

>                           "name": "engagement_standard.html",

>                           "type": "file"

>                         },

>                         {

>                           "name": "index.html",

>                           "type": "file"

>                         }

>                       ]

>                     },

>                     {

>                       "name": "evansville_inn",

>                       "type": "folder",

>                       "children": [

>                         {

>                           "name": "Notice_Room_Conditions.html",

>                           "type": "file"

>                         }

>                       ]

>                     }

>                   ]

>                 },

>                 {

>                   "name": "msa",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "portfolio",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "privacy",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "referral",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "cashapp",

>                       "type": "folder",

>                       "children": [

>                         {

>                           "name": "index.html",

>                           "type": "file"

>                         }

>                       ]

>                     },

>                     {

>                       "name": "quickbooks",

>                       "type": "folder",

>                       "children": [

>                         {

>                           "name": "index.html",

>                           "type": "file"

>                         }

>                       ]

>                     },

>                     {

>                       "name": "zoho",

>                       "type": "folder",

>                       "children": [

>                         {

>                           "name": "index.html",

>                           "type": "file"

>                         }

>                       ]

>                     },

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "resources",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "review",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     },

>                     {

>                       "name": "qrcode_www.google.com.png",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "services",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "showcases",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "20000-swing",

>                       "type": "folder",

>                       "children": [

>                         {

>                           "name": "index.html",

>                           "type": "file"

>                         }

>                       ]

>                     },

>                     {

>                       "name": "videos.html",

>                       "type": "file"

>                     }

>                   ]

>                 },

>                 {

>                   "name": "terms",

>                   "type": "folder",

>                   "children": [

>                     {

>                       "name": "index.html",

>                       "type": "file"

>                     }

>                   ]

>                 }

>               ]

>             },

>             {

>               "name": "contact.json",

>               "type": "file"

>             },

>             {

>               "name": "index.html",

>               "type": "file"

>             },

>             {

>               "name": "main.js",

>               "type": "file"

>             },

>             {

>               "name": "orchestrate_clarity.py",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "sql",

>           "type": "folder",

>           "children": [

>             {

>               "name": "01_init.sql",

>               "type": "file"

>             },

>             {

>               "name": "02_policies.sql",

>               "type": "file"

>             },

>             {

>               "name": "03_add_chunk_hash.sql",

>               "type": "file"

>             },

>             {

>               "name": "get-workspace-id.sql",

>               "type": "file"

>             },

>             {

>               "name": "schema.sql",

>               "type": "file"

>             },

>             {

>               "name": "tax_returns_schema.sql",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "state",

>           "type": "folder",

>           "children": [

>             {

>               "name": "local-agent",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": "cursor.json",

>                   "type": "file"

>                 },

>                 {

>                   "name": "locks.json",

>                   "type": "file"

>                 },

>                 {

>                   "name": "queue.json",

>                   "type": "file"

>                 }

>               ]

>             },

>             {

>               "name": "runtime",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": "embeddings_state.json",

>                   "type": "file"

>                 },

>                 {

>                   "name": "pipeline_state.json",

>                   "type": "file"

>                 },

>                 {

>                   "name": "repair_state.json",

>                   "type": "file"

>                 }

>               ]

>             },

>             {

>               "name": "sync",

>               "type": "folder",

>               "children": [

>                 {

>                   "name": "conflict_log.json",

>                   "type": "file"

>                 },

>                 {

>                   "name": "sync_cursor.json",

>                   "type": "file"

>                 }

>               ]

>             }

>           ]

>         },

>         {

>           "name": "vector",

>           "type": "folder",

>           "children": [

>             {

>               "name": "qios_local.db",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "yaml",

>           "type": "folder",

>           "children": [

>             {

>               "name": "fs_ignore.yaml",

>               "type": "file"

>             },

>             {

>               "name": "qios_matrix.yaml",

>               "type": "file"

>             },

>             {

>               "name": "qios_rules_v1.yaml",

>               "type": "file"

>             },

>             {

>               "name": "registry_folders.yaml",

>               "type": "file"

>             },

>             {

>               "name": "registry_realms.yaml",

>               "type": "file"

>             }

>           ]

>         },

>         {

>           "name": "README.md",

>           "type": "file"

>         },

>         {

>           "name": "index.html",

>           "type": "file"

>         }

>       ]

>     },

>     {

>       "name": "deploy",

>       "type": "folder"

>     },

>     {

>       "name": "docker",

>       "type": "folder"

>     },

>     {

>       "name": "monitoring",

>       "type": "folder"

>     },

>     {

>       "name": "opeartions",

>       "type": "folder"

>     },

>     {

>       "name": "tailscale",

>       "type": "folder"

>     },

>     {

>       "name": "README.md",

>       "type": "file"

>     },

>     {

>       "name": "qiserver_runbook.md",

>       "type": "file"

>     }

>   ],

>   "metadata": {

>     "generated": "2026-06-13T16:18:06.244Z",

>     "generator": "FileTree Pro Extension",

>     "version": "0.2.0",

>     "showIcons": false,

>     "maxDepth": 10

>   }

> }

### Assistant
> I’m going to treat **30_QiServer** as the runtime/infrastructure module, not the junk drawer. The key question is: “Does this file help operate the server, deploy services, monitor infrastructure, or support local ingestion?”

### Assistant
> No. **30_QiServer has the right skeleton, but it is currently polluted.**  
> It contains several things that belong in **QiNexus**, **QiEOS/DNA**, **QiLife/app modules**, or **client/business content** — not the server module.
> 
> ## What `30_QiServer` should be
> 
> `30_QiServer` should be the **infrastructure/runtime module**.
> 
> It should contain:
> 
> ```text
> 30_QiServer/
>   backups/
>   cloudflare/
>   deploy/
>   docker/
>   monitoring/
>   operations/
>   tailscale/
>   data/
>     logs/
>     state/
>     vector/
>     embeddings_cache/
>     model_cache/
>     dropzones/
>     processing/
>     failed/
>     normalized/
>     outputs/
>   README.md
>   qiserver_runbook.md
> ```
> 
> That part is mostly right.
> 
> But right now `data/` has become a **warehouse of app data, exports, docs, website content, migration files, schemas, seeds, and random legacy material**. That is where the mess is.
> 
> Also: rename this typo immediately:
> 
> ```text
> opeartions → operations
> ```
> 
> Tiny typo, big future pain.
> 
> ---
> 
> # Verdict by section
> 
> ## Keep in `30_QiServer`
> 
> These belong here:
> 
> ```text
> backups/
> cloudflare/
> deploy/
> docker/
> monitoring/
> tailscale/
> qiserver_runbook.md
> ```
> 
> Inside `data/`, these also make sense **if they are server runtime data**:
> 
> ```text
> data/devices/
> data/dropzones/
> data/embeddings_cache/
> data/extracted_text/
> data/failed/
> data/inbox/
> data/logs/
> data/manifests/
> data/model_cache/
> data/normalized/
> data/outputs/
> data/processing/
> data/quarantine/
> data/reviewed/
> data/state/
> data/vector/
> ```
> 
> These are operational pipeline/runtime folders. Fine.
> 
> ---
> 
> # Things that should probably move out
> 
> ## 1) CSV exports do **not** belong loose in `30_QiServer/data/csv`
> 
> This folder is the biggest offender.
> 
> You have Notion exports, Zoho exports, finance exports, domain records, email exports, schema-ish CSVs, system inventories, business data, raw email data, and personal/legal/medical-ish data all mixed together.
> 
> That is not a server module. That is a **migration intake pile**.
> 
> Move:
> 
> ```text
> 30_QiServer/data/csv/
> ```
> 
> to something like:
> 
> ```text
> 50_QiNexus/My Drive/00_Intake/20_Data_Migration/
> ```
> 
> Suggested split:
> 
> ```text
> 50_QiNexus/My Drive/00_Intake/20_Data_Migration/
>   00_raw_exports/
>     Notion/
>     Zoho/
>     Finance/
>     Legal/
>     Contacts/
>     System_Inventory/
>     Unknown/
>   10_cleaned_exports/
>   20_mapping_notes/
>   30_ready_for_import/
>   90_archive/
> ```
> 
> Server can later **consume** from QiNexus intake, but the raw CSV library should not live inside QiServer.
> 
> Especially move these out:
> 
> ```text
> Chrome Passwords.csv
> API Recovery Keys & Related.csv
> SOFI-Checking-7940-2025-10-31T12_45_50.csv
> docket.csv
> zai-vitals.csv
> raw_emails_combined.csv
> db_RawEmails_KB.csv
> contact_merged.csv
> contacts_cleaned.csv
> vendors_merged.csv
> ```
> 
> Also, **Chrome Passwords.csv and API Recovery Keys & Related.csv should be treated as sensitive/secrets**. They should not sit in a random CSV folder. Put them in a locked/secrets quarantine, not normal migration intake.
> 
> Better:
> 
> ```text
> 50_QiNexus/My Drive/90_Sensitive/Secrets_Quarantine/
> ```
> 
> or if you have a secrets module:
> 
> ```text
> 40_QiVault/Secrets_Quarantine/
> ```
> 
> Do not let Codex casually ingest those. That is how future-you leaks keys into logs. Very dumb. Very avoidable.
> 
> ---
> 
> ## 2) Website content should not live in QiServer data
> 
> This does not belong here:
> 
> ```text
> data/sites_QiAlly.com/
> ```
> 
> That is not server infrastructure. That is a website/app/content module.
> 
> Move to something like:
> 
> ```text
> 20_QiApps/sites/QiAlly.com/
> ```
> 
> or:
> 
> ```text
> 40_QiWeb/sites/QiAlly.com/
> ```
> 
> depending on your module naming.
> 
> Same with:
> 
> ```text
> data/posts/
> ```
> 
> That is content publishing, not server runtime.
> 
> Move:
> 
> ```text
> data/posts/
> ```
> 
> to:
> 
> ```text
> 50_QiNexus/My Drive/Content/Posts/
> ```
> 
> or under the relevant web/content module.
> 
> ---
> 
> ## 3) Lumara should be its own app/product module
> 
> This should not be buried inside server data:
> 
> ```text
> data/lumara/
> ```
> 
> It has assets, JS, DB schema, investor/resource graph docs. That is an app/product package.
> 
> Move to something like:
> 
> ```text
> 20_QiApps/Lumara/
> ```
> 
> or:
> 
> ```text
> 40_Products/Lumara/
> ```
> 
> QiServer may host/deploy Lumara, but it should not **own** Lumara’s source material.
> 
> ---
> 
> ## 4) QiOS doctrine / registry / rules files probably belong in DNA, not QiServer
> 
> These smell like canonical system governance:
> 
> ```text
> data/yaml/qios_matrix.yaml
> data/yaml/qios_rules_v1.yaml
> data/yaml/registry_folders.yaml
> data/yaml/registry_realms.yaml
> data/json/qios_constitution_schema_v1.json
> data/json/qios_constitution_v1.json
> data/sheets/qios_rules_v1_1.csv
> data/sheets/front_matter_schema_v1.csv
> ```
> 
> Move canonical versions to:
> 
> ```text
> 00_QiEOS/
> ```
> 
> or wherever your DNA/doctrine repo lives.
> 
> QiServer can keep **generated runtime copies** if needed, but source-of-truth governance belongs in DNA, not server runtime.
> 
> The clean rule:
> 
> ```text
> QiEOS/DNA owns doctrine.
> QiServer consumes doctrine.
> QiServer does not define doctrine.
> ```
> 
> ---
> 
> ## 5) SQL / schemas / seeds need a clearer home
> 
> These may be okay in QiServer **only if they are server deployment artifacts**:
> 
> ```text
> data/sql/
> data/schemas/
> data/seeds/
> data/migrations/
> ```
> 
> But if they define the actual app database, they probably belong with the app/domain they serve.
> 
> Better split:
> 
> ```text
> 30_QiServer/deploy/db/
>   migrations/
>   seeds/
>   schemas/
> ```
> 
> for deployment infrastructure.
> 
> But app-owned schema should live closer to the app:
> 
> ```text
> 20_QiApps/QiLife/db/
>   migrations/
>   seeds/
>   schemas/
> ```
> 
> or:
> 
> ```text
> 00_QiEOS/implementation_blueprint/database/
> ```
> 
> for canonical design.
> 
> Current state is ambiguous. That ambiguity will bite you later.
> 
> ---
> 
> ## 6) Docs folder is mixed
> 
> This folder:
> 
> ```text
> data/docs/
> ```
> 
> contains things like:
> 
> ```text
> INTEGRATION_COMPLETE.md
> QiAlly Call Ecosystem & Gina Voice Architecture.md
> gina_n8n_workflows.md
> ui_contracts_v1.md
> launcher_ui_mindmap.md
> ```
> 
> Some of that may belong in QiServer, but most of it sounds like architecture/product documentation.
> 
> Split it:
> 
> ### Keep in QiServer docs only if server-specific:
> 
> ```text
> 30_QiServer/docs/
>   cloudflare.md
>   tailscale.md
>   docker.md
>   backup_policy.md
>   monitoring.md
>   runbook.md
>   incident_response.md
> ```
> 
> ### Move app/product/architecture docs to DNA or app module:
> 
> ```text
> 00_QiEOS/architecture/
> 20_QiApps/Gina/
> 20_QiApps/QiLife/
> 20_QiApps/QiAccess/
> ```
> 
> Do not store conceptual architecture inside `data/docs`. `data/` should be machine/runtime data, not human doctrine.
> 
> ---
> 
> # Recommended target structure
> 
> I would refactor `30_QiServer` to this:
> 
> ```text
> 30_QiServer/
>   README.md
>   qiserver_runbook.md
> 
>   cloudflare/
>   tailscale/
>   docker/
>   deploy/
>     compose/
>     scripts/
>     db/
>       migrations/
>       seeds/
>       schemas/
> 
>   monitoring/
>     dashboards/
>     alerts/
>     healthchecks/
> 
>   operations/
>     runbooks/
>     checklists/
>     maintenance/
> 
>   backups/
>     configs/
>     manifests/
>     restore-tests/
> 
>   data/
>     dropzones/
>       default/
>       imports/
>       mobile/
>       scans/
>     inbox/
>     processing/
>     reviewed/
>     quarantine/
>     failed/
>     normalized/
>     extracted_text/
>     outputs/
>     logs/
>       ingest/
>       runtime/
>       sync/
>       local-agent/
>     state/
>       runtime/
>       sync/
>       local-agent/
>     vector/
>     embeddings_cache/
>     model_cache/
>     devices/
>     manifests/
> ```
> 
> That is clean. Server owns runtime, deployment, operations, logs, queues, cache, state, local vector DB, and dropzones.
> 
> It does **not** own every piece of data the server might someday touch.
> 
> ---
> 
> # Specific move map
> 
> ## Move to QiNexus migration intake
> 
> ```text
> 30_QiServer/data/csv/
> ```
> 
> to:
> 
> ```text
> 50_QiNexus/My Drive/00_Intake/20_Data_Migration/00_raw_exports/
> ```
> 
> ## Move sensitive CSVs to locked quarantine
> 
> ```text
> Chrome Passwords.csv
> API Recovery Keys & Related.csv
> ```
> 
> to:
> 
> ```text
> 50_QiNexus/My Drive/90_Sensitive/Secrets_Quarantine/
> ```
> 
> ## Move website
> 
> ```text
> 30_QiServer/data/sites_QiAlly.com/
> ```
> 
> to:
> 
> ```text
> 20_QiApps/sites/QiAlly.com/
> ```
> 
> or:
> 
> ```text
> 40_QiWeb/sites/QiAlly.com/
> ```
> 
> ## Move Lumara
> 
> ```text
> 30_QiServer/data/lumara/
> ```
> 
> to:
> 
> ```text
> 20_QiApps/Lumara/
> ```
> 
> ## Move posts/content
> 
> ```text
> 30_QiServer/data/posts/
> ```
> 
> to:
> 
> ```text
> 50_QiNexus/My Drive/Content/Posts/
> ```
> 
> ## Move canonical QiOS doctrine/schema
> 
> ```text
> data/yaml/qios_*
> data/json/qios_*
> data/sheets/qios_rules*
> data/sheets/front_matter_schema*
> ```
> 
> to:
> 
> ```text
> 00_QiEOS/
> ```
> 
> or:
> 
> ```text
> 00_QiEOS/20_registries/
> 00_QiEOS/30_schemas/
> 00_QiEOS/40_rules/
> ```
> 
> ## Move prompts
> 
> ```text
> data/qios_cursor_prompts/
> ```
> 
> probably to:
> 
> ```text
> 00_QiEOS/60_prompts/
> ```
> 
> or:
> 
> ```text
> 20_QiApps/Codex/prompts/
> ```
> 
> depending on whether they are canonical governance prompts or tool-specific working prompts.
> 
> ---
> 
> # What should stay in `30_QiServer/data/csv`?
> 
> Honestly? Almost nothing.
> 
> Maybe only generated operational reports like:
> 
> ```text
> service_health_export.csv
> docker_container_inventory.csv
> backup_manifest.csv
> sync_error_report.csv
> ```
> 
> But source exports from Notion, Zoho, banks, contacts, email, domains, etc.? No. Those are **QiNexus intake** or **domain module source data**.
> 
> ---
> 
> # The clean principle
> 
> Use this rule:
> 
> ## `30_QiServer` owns the machine.
> 
> That means:
> 
> - deployment
> - containers
> - tunnels
> - ports
> - logs
> - state
> - local queues
> - backups
> - monitoring
> - runtime cache
> - ingestion mechanics
> - server runbooks
> 
> ## `50_QiNexus` owns raw source material.
> 
> That means:
> 
> - CSV exports
> - PDFs
> - scans
> - documents
> - evidence
> - attachments
> - personal/business records
> - raw migration files
> 
> ## `00_QiEOS` owns doctrine and canonical definitions.
> 
> That means:
> 
> - schemas
> - rules
> - registries
> - naming standards
> - canonical field definitions
> - relationship models
> - architecture decisions
> 
> ## `20_QiApps` owns app/product source.
> 
> That means:
> 
> - Lumara
> - QiLife
> - QiAccess
> - QiAlly site
> - app-specific migrations
> - app UI contracts
> - app JS/assets
> 
> ---
> 
> # My blunt answer
> 
> **QiServer is structurally correct but content-wise messy.**
> 
> The biggest cleanup is:
> 
> 1. Rename `opeartions` → `operations`.
> 2. Move `data/csv` out to QiNexus migration intake.
> 3. Move secrets/password CSVs into sensitive quarantine.
> 4. Move `sites_QiAlly.com`, `lumara`, and `posts` out of QiServer.
> 5. Move QiOS canonical rules/schemas/registries back to QiEOS/DNA.
> 6. Keep only runtime/server operational data under `30_QiServer/data`.
> 
> Right now, `30_QiServer` is trying to be **server + archive + migration warehouse + website repo + doctrine repo + app repo**.
> 
> That is too many jobs. Split it before Codex builds on top of the mess.

### User
> question to stay consistent should our schemas in the database we choose literally be the main folder they are from, like qiaccess, qisystem, etc.

### Assistant
> Yes — **mostly**. For consistency, your database schemas should map to your **major system domains/modules**, not every folder.
> 
> The clean rule:
> 
> > **Top-level product/system modules can become database schemas. Lower folders usually become tables, views, or namespaces inside that schema.**
> 
> ## Recommended schema pattern
> 
> Use schemas like:
> 
> ```text
> qiaccess
> qilife
> qiserver
> qisystem
> qieos
> qinexus
> qiconnect
> qivault
> ```
> 
> But do **not** blindly turn every folder into a schema. That creates schema confetti.
> 
> ## Better mapping
> 
> | Folder / Module | DB Schema? | Why |
> |---|---:|---|
> | `QiAccess` | Yes | front door, identity-ish, capture entry points |
> | `QiLife` | Yes | personal cockpit, events, care, tasks, timeline |
> | `QiServer` | Maybe | only for runtime/service inventory/log metadata |
> | `QiSystem` | Yes | system-wide registry, configs, module catalog |
> | `QiEOS` | Yes | doctrine, canonical rules, field registry, governance |
> | `QiNexus` | Yes | storage index, source files, document metadata |
> | `QiConnect` | Yes | integrations, APIs, sync jobs, external accounts |
> | `QiVault` | Yes | secrets metadata, sensitive record registry — not raw secrets |
> | `Lumara` | Maybe | yes if it is a real product/app, no if just content right now |
> | `QiAlly.com` | No/Maybe | better as `qially` only if app-like; otherwise content tables under `content` |
> 
> ## The real distinction
> 
> ### Folder = where files live
> 
> Example:
> 
> ```text
> 30_QiServer/docker/
> 30_QiServer/cloudflare/
> 30_QiServer/tailscale/
> ```
> 
> Those should **not** become schemas.
> 
> ### Schema = ownership boundary in the database
> 
> Example:
> 
> ```sql
> qiserver.services
> qiserver.deployments
> qiserver.health_checks
> qiserver.backup_runs
> ```
> 
> That makes sense.
> 
> ## My recommended core DB schemas
> 
> Start with these:
> 
> ```text
> core
> qieos
> qisystem
> qinexus
> qiaccess
> qilife
> qiconnect
> qiserver
> qivault
> ```
> 
> Optional later:
> 
> ```text
> qially
> lumara
> finance
> legal
> care
> content
> ```
> 
> But do not add optional schemas until there is enough gravity.
> 
> ## What each should own
> 
> ### `core`
> 
> Global primitives used everywhere.
> 
> ```text
> core.entities
> core.people
> core.organizations
> core.locations
> core.identifiers
> core.relationships
> core.tags
> core.notes
> core.attachments
> ```
> 
> This is your boring foundation. Boring is correct.
> 
> ---
> 
> ### `qieos`
> 
> Doctrine/canonical governance.
> 
> ```text
> qieos.modules
> qieos.fields
> qieos.field_usages
> qieos.statuses
> qieos.rules
> qieos.relationship_types
> qieos.naming_standards
> qieos.adr_records
> ```
> 
> This is where your “master fields table” idea belongs.
> 
> ---
> 
> ### `qisystem`
> 
> Operational model of the whole Qi ecosystem.
> 
> ```text
> qisystem.apps
> qisystem.modules
> qisystem.environments
> qisystem.routes
> qisystem.features
> qisystem.permissions
> qisystem.capabilities
> ```
> 
> Think “map of the system.”
> 
> ---
> 
> ### `qinexus`
> 
> Storage, files, source records, ingestion.
> 
> ```text
> qinexus.sources
> qinexus.files
> qinexus.file_versions
> qinexus.import_batches
> qinexus.ingestion_jobs
> qinexus.extracted_text
> qinexus.document_links
> ```
> 
> Raw CSVs and PDFs are not “in the database” at first. The database tracks them.
> 
> ---
> 
> ### `qiaccess`
> 
> Front door/capture/access layer.
> 
> ```text
> qiaccess.capture_events
> qiaccess.quick_entries
> qiaccess.intake_sessions
> qiaccess.entry_routes
> qiaccess.user_surfaces
> ```
> 
> This schema should be lean. Do not shove all life data here just because it entered through QiAccess.
> 
> ---
> 
> ### `qilife`
> 
> Personal cockpit / lived operations.
> 
> ```text
> qilife.events
> qilife.tasks
> qilife.timeline_items
> qilife.care_logs
> qilife.medications
> qilife.appointments
> qilife.financial_events
> qilife.projects
> ```
> 
> This is where actual daily operating data lands after capture/classification.
> 
> ---
> 
> ### `qiconnect`
> 
> External systems and sync.
> 
> ```text
> qiconnect.accounts
> qiconnect.providers
> qiconnect.sync_jobs
> qiconnect.webhooks
> qiconnect.api_tokens_metadata
> qiconnect.external_ids
> ```
> 
> Do not store actual secrets here. Store references/metadata.
> 
> ---
> 
> ### `qiserver`
> 
> Infrastructure/runtime metadata.
> 
> ```text
> qiserver.hosts
> qiserver.services
> qiserver.containers
> qiserver.ports
> qiserver.tunnels
> qiserver.backup_runs
> qiserver.health_checks
> qiserver.incidents
> ```
> 
> This schema should not contain Notion exports, Zoho exports, client data, or life records.
> 
> ---
> 
> ### `qivault`
> 
> Sensitive data registry.
> 
> ```text
> qivault.secret_refs
> qivault.sensitive_records
> qivault.access_events
> qivault.encryption_keys_metadata
> qivault.redaction_rules
> ```
> 
> Again: **metadata and references**, not plaintext passwords sitting in tables like a cursed piñata.
> 
> ---
> 
> # The naming standard I’d use
> 
> Use lowercase schemas:
> 
> ```text
> qiaccess
> qilife
> qiserver
> qisystem
> qieos
> qinexus
> qiconnect
> qivault
> ```
> 
> Use snake_case tables:
> 
> ```text
> qieos.field_registry
> qinexus.import_batches
> qiserver.health_checks
> qilife.timeline_items
> ```
> 
> Use singular or plural consistently. I recommend **plural tables**:
> 
> ```text
> people
> organizations
> events
> tasks
> files
> fields
> modules
> services
> ```
> 
> ## Example
> 
> Instead of:
> 
> ```text
> QiServer → Data → CSV → Fields_001.csv
> ```
> 
> Database target should be:
> 
> ```text
> qieos.fields
> qieos.field_usages
> qinexus.import_batches
> qinexus.source_files
> ```
> 
> Not:
> 
> ```text
> qiserver.csv_fields
> ```
> 
> Because the CSV happened to sit in QiServer, but the **meaning** belongs to QiEOS/QiNexus.
> 
> That distinction matters.
> 
> # The actual answer
> 
> Yes, schemas should generally align to your **main canonical modules**, like:
> 
> ```text
> qiaccess
> qisystem
> qilife
> qieos
> qinexus
> qiserver
> ```
> 
> But they should align to **ownership**, not physical folder accidents.
> 
> The folder tree tells you where something currently lives.  
> The schema tells you who owns its meaning.
> 
> That is the principle.

### User
> ok, you want to put together the master schema document or something you would know better what that actually looks like.

### Assistant
> I’m going to make this as a **canonical planning document**, not SQL yet. SQL comes after we lock ownership boundaries, otherwise Codex will happily build a very organized dumpster fire.

### Assistant
> Yes. What you need is a **Master Schema Governance Document** — not just “a list of database schemas.”
> 
> This should live in QiEOS/DNA because it defines the rules for the database across the whole system.
> 
> Suggested file path:
> 
> ```text
> C:\QiLabs\00_QiEOS\30_standards\database\master_schema_governance.md
> ```
> 
> Here’s the first clean version.
> 
> :::writing{variant="document" id="48291"}
> # QiOS Master Schema Governance
> 
> ## 1. Purpose
> 
> This document defines the canonical database schema strategy for the QiOS ecosystem.
> 
> The goal is to prevent database sprawl, duplicate tables, unclear ownership, and accidental coupling between modules.
> 
> The database should reflect **domain ownership**, not temporary folder placement.
> 
> A file’s current folder tells us where it lives.
> 
> A database schema tells us who owns its meaning.
> 
> ---
> 
> # 2. Core Principle
> 
> ## Schemas map to major system domains, not every folder.
> 
> Top-level Qi modules may become database schemas when they represent a real ownership boundary.
> 
> Subfolders should usually become:
> 
> - tables
> - views
> - enum groups
> - metadata records
> - file paths
> - ingestion categories
> - documentation sections
> 
> They should not automatically become schemas.
> 
> ---
> 
> # 3. Canonical Schema Naming Rules
> 
> ## 3.1 Schema names
> 
> All database schemas use:
> 
> - lowercase
> - no spaces
> - no hyphens
> - `qi` prefix where the schema represents a canonical Qi module
> 
> Examples:
> 
> ```text
> qieos
> qisystem
> qinexus
> qiaccess
> qilife
> qiconnect
> qiserver
> qivault
> ```
> 
> ## 3.2 Table names
> 
> Tables use:
> 
> - lowercase
> - snake_case
> - plural nouns unless there is a strong reason otherwise
> 
> Examples:
> 
> ```text
> qieos.fields
> qieos.field_usages
> qinexus.files
> qinexus.import_batches
> qiserver.services
> qilife.timeline_items
> ```
> 
> ## 3.3 Column names
> 
> Columns use:
> 
> - lowercase
> - snake_case
> - clear semantic naming
> - no ambiguous abbreviations unless standardized
> 
> Examples:
> 
> ```text
> created_at
> updated_at
> source_system
> external_id
> canonical_status
> sensitivity_level
> ```
> 
> ---
> 
> # 4. Required Core Schemas
> 
> ## 4.1 `core`
> 
> The `core` schema contains global primitives used across the whole ecosystem.
> 
> It should stay boring, stable, and reusable.
> 
> ### Owns
> 
> - people
> - organizations
> - locations
> - entities
> - identifiers
> - relationships
> - tags
> - notes
> - attachments
> - audit metadata
> 
> ### Example tables
> 
> ```text
> core.entities
> core.people
> core.organizations
> core.locations
> core.identifiers
> core.relationships
> core.tags
> core.entity_tags
> core.notes
> core.attachments
> core.audit_events
> ```
> 
> ### Rule
> 
> If a concept is used everywhere and does not belong to one app, it probably belongs in `core`.
> 
> ---
> 
> ## 4.2 `qieos`
> 
> The `qieos` schema contains doctrine, standards, governance, canonical definitions, field registries, and system rules.
> 
> This is the database home for the “master fields table” concept.
> 
> ### Owns
> 
> - canonical modules
> - field registry
> - field usages
> - schema registry
> - table registry
> - status registry
> - relationship type registry
> - naming standards
> - architectural decisions
> - governance rules
> 
> ### Example tables
> 
> ```text
> qieos.modules
> qieos.schemas
> qieos.tables
> qieos.fields
> qieos.field_usages
> qieos.field_dependencies
> qieos.statuses
> qieos.relationship_types
> qieos.naming_standards
> qieos.rules
> qieos.adr_records
> ```
> 
> ### Rule
> 
> QiEOS defines what things mean.
> 
> It does not store operational runtime data unless that data is governance metadata.
> 
> ---
> 
> ## 4.3 `qisystem`
> 
> The `qisystem` schema contains the map of the operating system itself.
> 
> It describes the applications, modules, capabilities, surfaces, routes, and system boundaries.
> 
> ### Owns
> 
> - app registry
> - module registry
> - feature registry
> - route registry
> - permission model
> - capability model
> - environment model
> - system configuration metadata
> 
> ### Example tables
> 
> ```text
> qisystem.apps
> qisystem.modules
> qisystem.features
> qisystem.routes
> qisystem.capabilities
> qisystem.permissions
> qisystem.environments
> qisystem.config_items
> ```
> 
> ### Rule
> 
> QiSystem maps the system.
> 
> QiEOS defines the doctrine.
> 
> QiServer runs the machine.
> 
> Do not merge those three.
> 
> ---
> 
> ## 4.4 `qinexus`
> 
> The `qinexus` schema contains file, source, archive, document, and ingestion metadata.
> 
> QiNexus owns the index of source material.
> 
> It does not necessarily store every raw file directly inside the database.
> 
> ### Owns
> 
> - source systems
> - files
> - file versions
> - import batches
> - ingestion jobs
> - extracted text references
> - document metadata
> - source-to-entity links
> - migration intake tracking
> 
> ### Example tables
> 
> ```text
> qinexus.sources
> qinexus.files
> qinexus.file_versions
> qinexus.import_batches
> qinexus.import_files
> qinexus.ingestion_jobs
> qinexus.extracted_text
> qinexus.document_links
> qinexus.source_entity_links
> ```
> 
> ### Rule
> 
> Raw CSVs, PDFs, scans, exports, and evidence belong under QiNexus ownership.
> 
> The database tracks them, classifies them, and links them.
> 
> The database should not casually absorb raw messy exports as final tables.
> 
> ---
> 
> ## 4.5 `qiaccess`
> 
> The `qiaccess` schema contains front-door capture, intake, and access-layer events.
> 
> QiAccess is where information enters the system.
> 
> It does not own all data that passes through it.
> 
> ### Owns
> 
> - capture events
> - quick entries
> - intake sessions
> - user surfaces
> - entry routes
> - temporary intake payloads
> - classification handoff records
> 
> ### Example tables
> 
> ```text
> qiaccess.capture_events
> qiaccess.quick_entries
> qiaccess.intake_sessions
> qiaccess.entry_routes
> qiaccess.user_surfaces
> qiaccess.classification_queue
> qiaccess.handoff_events
> ```
> 
> ### Rule
> 
> QiAccess captures.
> 
> Other schemas own the final meaning.
> 
> A medical note captured through QiAccess does not become `qiaccess.medical_notes`.
> 
> It should become a care, life, document, or entity record depending on meaning.
> 
> ---
> 
> ## 4.6 `qilife`
> 
> The `qilife` schema contains personal operating data, daily life events, care logs, tasks, timelines, and lived records.
> 
> ### Owns
> 
> - timeline items
> - tasks
> - appointments
> - care logs
> - medications
> - symptoms
> - financial life events
> - projects
> - routines
> - personal events
> 
> ### Example tables
> 
> ```text
> qilife.timeline_items
> qilife.tasks
> qilife.appointments
> qilife.care_logs
> qilife.medications
> qilife.symptoms
> qilife.financial_events
> qilife.projects
> qilife.routines
> ```
> 
> ### Rule
> 
> QiLife owns lived operational data.
> 
> It should not own server infrastructure, doctrine, raw document storage, or external sync mechanics.
> 
> ---
> 
> ## 4.7 `qiconnect`
> 
> The `qiconnect` schema contains integrations, external accounts, provider connections, sync jobs, webhooks, and external IDs.
> 
> ### Owns
> 
> - providers
> - connected accounts
> - sync jobs
> - webhook events
> - external IDs
> - API connection metadata
> - integration health
> 
> ### Example tables
> 
> ```text
> qiconnect.providers
> qiconnect.connected_accounts
> qiconnect.sync_jobs
> qiconnect.webhook_events
> qiconnect.external_ids
> qiconnect.integration_health
> qiconnect.api_token_refs
> ```
> 
> ### Rule
> 
> QiConnect stores connection metadata and external system mapping.
> 
> It should not store plaintext secrets.
> 
> Secrets belong in secure storage, with references tracked by `qivault`.
> 
> ---
> 
> ## 4.8 `qiserver`
> 
> The `qiserver` schema contains infrastructure and runtime metadata.
> 
> It represents the server, services, containers, tunnels, ports, backup runs, and health checks.
> 
> ### Owns
> 
> - hosts
> - services
> - containers
> - ports
> - tunnels
> - backup runs
> - health checks
> - incidents
> - runtime jobs
> - deployment metadata
> 
> ### Example tables
> 
> ```text
> qiserver.hosts
> qiserver.services
> qiserver.containers
> qiserver.ports
> qiserver.tunnels
> qiserver.backup_runs
> qiserver.health_checks
> qiserver.incidents
> qiserver.runtime_jobs
> qiserver.deployments
> ```
> 
> ### Rule
> 
> QiServer owns the machine and runtime.
> 
> It does not own random CSV exports, client data, website content, app source code, or doctrine.
> 
> ---
> 
> ## 4.9 `qivault`
> 
> The `qivault` schema contains sensitive-data metadata, secret references, access logs, redaction rules, and security classifications.
> 
> It should not become a plaintext password database.
> 
> ### Owns
> 
> - secret references
> - sensitive record metadata
> - access events
> - encryption key metadata
> - redaction rules
> - sensitivity classifications
> 
> ### Example tables
> 
> ```text
> qivault.secret_refs
> qivault.sensitive_records
> qivault.access_events
> qivault.encryption_key_metadata
> qivault.redaction_rules
> qivault.sensitivity_levels
> ```
> 
> ### Rule
> 
> QiVault tracks sensitive data safely.
> 
> Actual secrets should live in a proper secret manager or encrypted storage.
> 
> The database may store references, hashes, labels, and access metadata.
> 
> ---
> 
> # 5. Optional Future Schemas
> 
> Optional schemas should only be created when the domain has enough gravity to justify its own boundary.
> 
> Do not create optional schemas just because a folder exists.
> 
> ## 5.1 Possible future schemas
> 
> ```text
> finance
> legal
> care
> content
> qially
> lumara
> clients
> ```
> 
> ## 5.2 Creation test
> 
> A new schema is allowed only if at least three of the following are true:
> 
> - It has its own lifecycle.
> - It has its own permissions model.
> - It has many tables.
> - It has independent business logic.
> - It integrates with external systems.
> - It has sensitive boundaries.
> - It has a separate product/app identity.
> - It would become messy if forced into another schema.
> 
> ---
> 
> # 6. Folder-to-Schema Interpretation Rules
> 
> ## 6.1 Physical folder does not equal database schema
> 
> Example:
> 
> ```text
> 30_QiServer/data/csv/Fields_001.csv
> ```
> 
> This file physically sits under QiServer, but its meaning may belong to:
> 
> ```text
> qieos.fields
> qieos.field_usages
> qinexus.import_batches
> qinexus.files
> ```
> 
> It should not become:
> 
> ```text
> qiserver.csv_fields
> ```
> 
> unless the CSV specifically describes server infrastructure fields.
> 
> ## 6.2 Ownership beats location
> 
> When deciding schema placement, ask:
> 
> 1. What does this record mean?
> 2. Which module owns that meaning?
> 3. Which module governs its lifecycle?
> 4. Which module would be damaged if this data were wrong?
> 5. Which module needs permission/control over this data?
> 
> The answer determines the schema.
> 
> ---
> 
> # 7. Master Registry Tables
> 
> QiOS should maintain registry tables to prevent duplicate definitions.
> 
> ## 7.1 Field registry
> 
> Canonical home:
> 
> ```text
> qieos.fields
> ```
> 
> Purpose:
> 
> Track every canonical field used across the system.
> 
> Example fields:
> 
> ```text
> id
> field_key
> display_name
> description
> data_type
> canonical_format
> sensitivity_level
> allowed_values
> created_at
> updated_at
> deprecated_at
> ```
> 
> ## 7.2 Field usage registry
> 
> Canonical home:
> 
> ```text
> qieos.field_usages
> ```
> 
> Purpose:
> 
> Track where each field appears.
> 
> Example fields:
> 
> ```text
> id
> field_id
> schema_name
> table_name
> column_name
> required
> unique
> indexed
> default_value
> usage_notes
> ```
> 
> ## 7.3 Schema registry
> 
> Canonical home:
> 
> ```text
> qieos.schemas
> ```
> 
> Purpose:
> 
> Track approved schemas and ownership.
> 
> Example fields:
> 
> ```text
> id
> schema_name
> owning_module
> purpose
> status
> created_at
> updated_at
> deprecated_at
> ```
> 
> ## 7.4 Table registry
> 
> Canonical home:
> 
> ```text
> qieos.tables
> ```
> 
> Purpose:
> 
> Track approved tables and their meaning.
> 
> Example fields:
> 
> ```text
> id
> schema_id
> table_name
> purpose
> owner
> status
> sensitivity_level
> source_of_truth_policy
> created_at
> updated_at
> deprecated_at
> ```
> 
> ---
> 
> # 8. Source-of-Truth Rules
> 
> Every table should declare its source-of-truth policy.
> 
> Allowed values:
> 
> ```text
> canonical
> derived
> imported
> cached
> runtime
> staging
> archived
> external_reference
> ```
> 
> ## Definitions
> 
> ### `canonical`
> 
> The table is the official source of truth inside QiOS.
> 
> ### `derived`
> 
> The table is generated from other canonical data.
> 
> ### `imported`
> 
> The table stores imported data from an external source.
> 
> ### `cached`
> 
> The table stores replaceable cache data.
> 
> ### `runtime`
> 
> The table stores operational runtime state.
> 
> ### `staging`
> 
> The table stores temporary pre-review data.
> 
> ### `archived`
> 
> The table stores historical or inactive data.
> 
> ### `external_reference`
> 
> The table points to an external source but does not own the full record.
> 
> ---
> 
> # 9. Sensitivity Rules
> 
> Every schema and table should support sensitivity classification.
> 
> Suggested levels:
> 
> ```text
> public
> internal
> private
> sensitive
> restricted
> secret
> ```
> 
> ## Default sensitivity by schema
> 
> ```text
> core: private
> qieos: internal
> qisystem: internal
> qinexus: private
> qiaccess: private
> qilife: sensitive
> qiconnect: sensitive
> qiserver: internal
> qivault: restricted
> ```
> 
> ## Rule
> 
> No table should silently accept sensitive data without classification.
> 
> If a table can contain medical, legal, financial, identity, passwords, API keys, or private relationship data, it must be classified.
> 
> ---
> 
> # 10. Ingestion Flow
> 
> Raw data should move through a controlled pipeline.
> 
> ## Standard flow
> 
> ```text
> Raw file
> → qinexus.files
> → qinexus.import_batches
> → staging table or extracted payload
> → review/classification
> → canonical target schema
> → source link retained
> ```
> 
> ## Example
> 
> A Zoho contacts CSV should flow as:
> 
> ```text
> CSV file in QiNexus
> → qinexus.files
> → qinexus.import_batches
> → staging.zoho_contacts
> → review/dedupe
> → core.people / core.organizations
> → qiconnect.external_ids
> ```
> 
> It should not be directly dumped into final production tables.
> 
> ---
> 
> # 11. Staging Strategy
> 
> A dedicated staging schema may be used during migration.
> 
> Recommended staging schema:
> 
> ```text
> staging
> ```
> 
> ### Example tables
> 
> ```text
> staging.notion_tasks_raw
> staging.zoho_contacts_raw
> staging.zoho_invoices_raw
> staging.mmex_transactions_raw
> staging.chrome_passwords_quarantine
> ```
> 
> ## Rule
> 
> Staging tables are temporary.
> 
> They are not canonical.
> 
> Every staging table must have:
> 
> ```text
> import_batch_id
> source_file_id
> row_number
> raw_payload
> review_status
> created_at
> ```
> 
> ---
> 
> # 12. Relationship Strategy
> 
> Relationships should be explicit.
> 
> Do not rely only on scattered foreign keys when the system needs flexible graph behavior.
> 
> ## Recommended approach
> 
> Use normal foreign keys for strong structural relationships.
> 
> Use `core.relationships` for flexible cross-domain relationships.
> 
> ### Example
> 
> A person can be related to:
> 
> - an organization
> - a document
> - a task
> - a care event
> - a legal matter
> - a project
> - an external account
> 
> Canonical flexible relationship table:
> 
> ```text
> core.relationships
> ```
> 
> Suggested fields:
> 
> ```text
> id
> source_entity_id
> target_entity_id
> relationship_type
> relationship_strength
> start_date
> end_date
> status
> notes
> created_at
> updated_at
> ```
> 
> ---
> 
> # 13. Required Metadata Columns
> 
> Most canonical tables should include:
> 
> ```text
> id
> created_at
> updated_at
> created_by
> updated_by
> status
> source_system
> source_file_id
> import_batch_id
> sensitivity_level
> notes
> ```
> 
> Not every table needs every column, but missing metadata should be intentional.
> 
> ---
> 
> # 14. Anti-Patterns
> 
> Avoid these.
> 
> ## 14.1 Schema confetti
> 
> Do not make every folder a database schema.
> 
> Bad:
> 
> ```text
> docker
> cloudflare
> csv
> docs
> posts
> json
> yaml
> sheets
> ```
> 
> Better:
> 
> ```text
> qiserver.services
> qiserver.tunnels
> qinexus.files
> qieos.rules
> content.posts
> ```
> 
> ## 14.2 Location-based ownership
> 
> Bad:
> 
> ```text
> qiserver.csv_contacts
> ```
> 
> Better:
> 
> ```text
> qinexus.files
> staging.zoho_contacts_raw
> core.people
> core.organizations
> qiconnect.external_ids
> ```
> 
> ## 14.3 Plaintext secrets in normal tables
> 
> Bad:
> 
> ```text
> qiconnect.api_keys
> ```
> 
> Better:
> 
> ```text
> qivault.secret_refs
> qiconnect.api_token_refs
> ```
> 
> ## 14.4 Duplicate fields everywhere
> 
> Bad:
> 
> ```text
> client_email
> contact_email
> person_email
> primary_email_address
> email_1
> ```
> 
> Better:
> 
> ```text
> qieos.fields
> qieos.field_usages
> core.identifiers
> ```
> 
> ## 14.5 Raw imports pretending to be final data
> 
> Bad:
> 
> ```text
> core.zoho_contacts_import
> ```
> 
> Better:
> 
> ```text
> staging.zoho_contacts_raw
> core.people
> core.organizations
> qiconnect.external_ids
> ```
> 
> ---
> 
> # 15. First Approved Schema Set
> 
> The initial database should begin with:
> 
> ```text
> core
> qieos
> qisystem
> qinexus
> qiaccess
> qilife
> qiconnect
> qiserver
> qivault
> staging
> ```
> 
> Optional schemas may be added later only after the creation test is passed.
> 
> ---
> 
> # 16. Immediate Build Order
> 
> ## Phase 1: Governance foundation
> 
> Create:
> 
> ```text
> qieos.schemas
> qieos.tables
> qieos.fields
> qieos.field_usages
> qieos.relationship_types
> qieos.statuses
> ```
> 
> ## Phase 2: Core primitives
> 
> Create:
> 
> ```text
> core.entities
> core.people
> core.organizations
> core.identifiers
> core.relationships
> core.tags
> ```
> 
> ## Phase 3: Source tracking
> 
> Create:
> 
> ```text
> qinexus.sources
> qinexus.files
> qinexus.import_batches
> qinexus.import_files
> ```
> 
> ## Phase 4: Intake and staging
> 
> Create:
> 
> ```text
> qiaccess.capture_events
> staging.import_rows
> ```
> 
> ## Phase 5: Runtime/system metadata
> 
> Create:
> 
> ```text
> qisystem.modules
> qisystem.apps
> qiserver.hosts
> qiserver.services
> qiserver.health_checks
> ```
> 
> ---
> 
> # 17. Final Rule
> 
> The database should make QiOS easier to reason about.
> 
> If a schema, table, or field makes ownership less clear, it is probably wrong.
> 
> When in doubt:
> 
> ```text
> QiEOS defines.
> QiSystem maps.
> QiNexus stores/indexes.
> QiAccess captures.
> QiLife operates.
> QiConnect syncs.
> QiServer runs.
> QiVault protects.
> Core connects.
> Staging cleans.
> ```
> :::
> 
> ## My recommendation
> 
> This should be your **first canonical database doctrine file**. Then the next document should be:
> 
> ```text
> master_table_catalog.md
> ```
> 
> That one lists the actual first-pass tables, fields, and relationships. This doc is the constitution; the table catalog is the blueprint.

### User
> where should it be stored inside qidna

### Assistant
> Store it in **QiDNA / QiEOS standards**, because it is a cross-system doctrine file.
> 
> Best path:
> 
> ```text
> C:\QiLabs\_QiOS_DNA\00_QiEOS\30_standards\database\master_schema_governance.md
> ```
> 
> If that `database` folder does not exist, create it.
> 
> ## Why there?
> 
> Because this document is not app-specific. It governs:
> 
> ```text
> core
> qieos
> qisystem
> qinexus
> qiaccess
> qilife
> qiconnect
> qiserver
> qivault
> staging
> ```
> 
> So it belongs in **QiEOS standards**, not inside QiServer, QiLife, or QiAccess.
> 
> ## Recommended QiDNA placement
> 
> ```text
> _QiOS_DNA/
>   00_QiEOS/
>     30_standards/
>       database/
>         master_schema_governance.md
>         master_table_catalog.md
>         naming_conventions.md
>         source_of_truth_rules.md
>         sensitivity_classification.md
> ```
> 
> ## If you want the cleaner numbered structure
> 
> Use this:
> 
> ```text
> _QiOS_DNA/
>   00_QiEOS/
>     30_standards/
>       40_database/
>         00_master_schema_governance.md
>         10_master_table_catalog.md
>         20_field_registry_standard.md
>         30_source_of_truth_rules.md
>         40_sensitivity_classification.md
> ```
> 
> That’s the one I’d pick.
> 
> ## Final answer
> 
> Put it here:
> 
> ```text
> C:\QiLabs\_QiOS_DNA\00_QiEOS\30_standards\40_database\00_master_schema_governance.md
> ```
> 
> That keeps it canonical, findable, and not buried in runtime sludge.

### User
> you want to go ahead and give me the master table catalog too, or better yet give me everything ready for download so i can just drop it in dont forget to check the qidna docs for overlap missing items, etc.

### Assistant
> I’ll make this as a drop-in **QiDNA database standards pack**: markdown files, clean folder layout, and a manifest. I’ll also check the live QiDNA docs/site for naming or section overlap before I package it.

### Assistant
> I’m building the pack around the QiDNA path we already settled: `00_QiEOS/30_standards/40_database/`. I could not reliably read the live `dna.qially.com` page through the browser, so I’m cross-checking against the folder tree and known QiEOS/DNA structure instead.

### Assistant
> Done. I made a drop-in QiDNA database standards pack.
> 
> Download it here:
> 
> [Download `qidna_database_standards_pack.zip`](sandbox:/mnt/data/qidna_database_standards_pack.zip)
> 
> ## What’s inside
> 
> It drops into:
> 
> ```text
> C:\QiLabs\_QiOS_DNA\00_QiEOS\30_standards\40_database\
> ```
> 
> Included files:
> 
> ```text
> 00_INDEX.md
> 00_master_schema_governance.md
> 10_master_table_catalog.md
> 20_field_registry_standard.md
> 30_source_of_truth_rules.md
> 40_sensitivity_classification.md
> 50_ingestion_staging_standard.md
> 60_database_naming_conventions.md
> 70_schema_decision_matrix.md
> 80_codex_implementation_prompt.md
> _support/
>   overlap_review_notes.md
>   qidna_database_pack_manifest.json
> ```
> 
> I also included:
> 
> ```text
> README_DROP_THIS_IN.md
> install_qidna_database_pack.ps1
> ```
> 
> ## Important note
> 
> I could not fully crawl the live `dna.qially.com` page through the browser because the tool blocked direct access to that URL. So I cross-checked against the QiDNA/QiServer structure you provided and included an explicit `overlap_review_notes.md` file documenting likely overlaps and missing items. citeturn490088view0
> 
> ## My read
> 
> This is the right next layer:
> 
> ```text
> schema governance = constitution
> master table catalog = blueprint
> SQL migrations = next
> ```
> 
> Do **not** let Codex jump straight to SQL until this pack is dropped in. That’s how we avoid encoding the current folder chaos into the database like a haunted filing cabinet.

### User
> says fatal could no resolve head

### Assistant
> That error usually means: **Git repo exists, but there is no first commit yet.**  
> So `HEAD` has nothing to point to. Git is basically saying, “girl, there is no history.”
> 
> ## Fix it
> 
> Go to the repo folder first:
> 
> ```bash
> cd /srv/qios
> ```
> 
> or if you’re on Windows:
> 
> ```powershell
> cd C:\QiLabs\_QiOS_DNA
> ```
> 
> Then run:
> 
> ```bash
> git status
> git add .
> git commit -m "Initial commit"
> ```
> 
> After that, `HEAD` exists and the error should stop.
> 
> ---
> 
> ## If Git complains about name/email
> 
> Run:
> 
> ```bash
> git config user.name "qiallyme"
> git config user.email "crice4485@gmail.com"
> ```
