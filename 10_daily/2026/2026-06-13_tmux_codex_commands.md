---
layout: page
title: "Tmux Codex Commands"
slug: "tmux_codex_commands"
created_at: "2026-06-13 10:12:43"
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
uid: "6a2d7345-b3a4-83ea-9cd0-786d1174d4ca"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Tmux Codex Commands

## Overview
- **Date**: 2026-06-13 10:12:43
- **Conversation ID**: `6a2d7345-b3a4-83ea-9cd0-786d1174d4ca`
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
