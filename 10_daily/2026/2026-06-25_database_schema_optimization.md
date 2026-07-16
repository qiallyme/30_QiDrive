---
layout: page
title: "Database Schema Optimization"
slug: "database_schema_optimization"
created_at: "2026-06-25 22:10:24"
updated_at: "2026-06-25 22:10:24"
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
date: 2026-06-25
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a3ded9a-6c3c-83ea-8866-c6f6b68784aa"
canonical_ref: ""
---

# Database Schema Optimization

## Overview
- **Date**: 2026-06-25 22:10:24
- **Conversation ID**: `6a3ded9a-6c3c-83ea-8866-c6f6b68784aa`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> i think we have too many columns, Name,Chapter,Chapter Code,Decimal ID,Last Updated,Level,Notes,Parent Code,Parent item,Path,QiCode,Related Sections,Section,Section Code,Sort Key,Status,Sub-item,Tags,Title,Title Number,Type,Version
> 1. 🎯 Core Principles,qi_doctrine_principles,,,"June 25, 2026 8:33 PM",,Merged into existing draft chapter without changing chapter name.,,Title 01 — Doctrine & Principles (Title%2001%20%E2%80%94%20Doctrine%20&%20Principles%208480e028937a46569ca6431ffe585bd7.csv),,,,Core Principles,,,draft,,,.legacy,,Section,
> SECTION 1: VISION & ARCHITECTURE,qiapps_projects_integrations,,,"June 25, 2026 8:37 PM",,Merged into existing draft chapter without changing chapter name.,,Title 07 — Security & Access (Title%2007%20%E2%80%94%20Security%20&%20Access%208fbdb5a7433844f48ad0b371ccbee59b.csv),,§ 07.02.001,,Vision & Architecture,,,draft,,,.legacy,,Section,
> SECTION 2: FOUNDATIONS & ENVIRONMENT,qiapps_projects_integrations,,,"June 25, 2026 8:37 PM",,Merged into existing draft chapter without changing chapter name.,,Title 07 — Security & Access (Title%2007%20%E2%80%94%20Security%20&%20Access%208fbdb5a7433844f48ad0b371ccbee59b.csv),,§ 07.02.002,,Foundations & Environment,,,draft,,,.legacy,,Section,
> SECTION 3: CORE MODULES,qiapps_projects_integrations,,,"June 25, 2026 8:37 PM",,Merged into existing draft chapter without changing chapter name.,,Title 07 — Security & Access (Title%2007%20%E2%80%94%20Security%20&%20Access%208fbdb5a7433844f48ad0b371ccbee59b.csv),,§ 07.02.003,,Core Modules,,,draft,,,.legacy,,Section,
> SECTION 4: UI & INTERACTION,qiapps_projects_integrations,,,"June 25, 2026 8:37 PM",,Merged into existing draft chapter without changing chapter name.,,Title 07 — Security & Access (Title%2007%20%E2%80%94%20Security%20&%20Access%208fbdb5a7433844f48ad0b371ccbee59b.csv),,§ 07.02.004,,UI & Interaction,,,draft,,,.legacy,,Section,
> SECTION 5: WORKFLOWS & AUTOMATION,qiapps_projects_integrations,,,"June 25, 2026 8:37 PM",,Merged into existing draft chapter without changing chapter name.,,Title 07 — Security & Access (Title%2007%20%E2%80%94%20Security%20&%20Access%208fbdb5a7433844f48ad0b371ccbee59b.csv),,§ 07.02.005,,Workflows & Automation,,,draft,,,.legacy,,Workflow,
> SECTION 6: EXPANSION & COLLAB,qiapps_projects_integrations,,,"June 25, 2026 8:37 PM",,Merged into existing draft chapter without changing chapter name.,,Title 07 — Security & Access (Title%2007%20%E2%80%94%20Security%20&%20Access%208fbdb5a7433844f48ad0b371ccbee59b.csv),,§ 07.02.006,,Expansion & Collab,,,draft,,,.legacy,,Section,
> SECTION 7: DNA & DOCUMENTATION,qiapps_projects_integrations,,,"June 25, 2026 8:37 PM",,Merged into existing draft chapter without changing chapter name.,,Title 07 — Security & Access (Title%2007%20%E2%80%94%20Security%20&%20Access%208fbdb5a7433844f48ad0b371ccbee59b.csv),,§ 07.02.007,,DNA & Documentation,,,draft,,,.legacy,,Section,
> 📘 QiCodex — Unified Decimal Registry,scope_definitions_numbering,,,"June 25, 2026 8:32 PM",,Merged into existing draft chapter without changing chapter name.,,Title 00 — General Provisions (Title%2000%20%E2%80%94%20General%20Provisions%20fca8e718a53d46afad20fe1b13fb4caf.csv),,§ 00.01.005,,QiCodex Unified Decimal Registry,,,draft,,,.legacy,,Reference,
> 1.21.2_Principle_of_Presence.md,qi_doctrine_principles,,,"June 25, 2026 8:33 PM",,Merged into existing draft chapter without changing chapter name.,,Title 01 — Doctrine & Principles (Title%2001%20%E2%80%94%20Doctrine%20&%20Principles%

### Assistant
> Yes — this is bloated. You’re encoding the same hierarchy four ways, which will make Notion feel “organized” for five minutes and then turn into mud.

### Assistant
> Yes. **This table is overbuilt.** You have at least **6 duplicate naming/hierarchy columns** and **4 duplicate code columns**.
> 
> The real problem: you are trying to store **tree structure, legal numbering, import metadata, and page names** all as separate columns. That is how databases become haunted.
> 
> ## Keep this lean schema
> 
> For the main Notion database, use:
> 
> ```csv
> Name,Type,QiCode,Parent,Sort Key,Status,Tags,Notes,Source,Version
> ```
> 
> That’s it.
> 
> ## What each column means
> 
> | Keep | Purpose |
> |---|---|
> | **Name** | The human-readable title of the item |
> | **Type** | Title, Chapter, Section, Rule, Workflow, Reference, Template, Principle |
> | **QiCode** | The official decimal/legal code, ex: `§ 07.02.001` |
> | **Parent** | The parent item/chapter/section |
> | **Sort Key** | Controls ordering, ex: `07.02.001` |
> | **Status** | draft, active, archived, legacy |
> | **Tags** | Light metadata only |
> | **Notes** | Migration notes, merge notes, context |
> | **Source** | Old file/source path, only if useful |
> | **Version** | Optional, but okay for doctrine/control docs |
> 
> ## Merge/delete map
> 
> | Current Column | Action |
> |---|---|
> | **Name** | Keep as `Name` |
> | **Title** | Merge into `Name`, then delete |
> | **Section** | Merge into `Name`, then delete |
> | **Sub-item** | Merge into `Name`, then delete |
> | **Chapter** | Replace with `Parent`, then delete |
> | **Parent item** | Rename to `Parent` |
> | **Parent Code** | Delete unless you need it temporarily for import matching |
> | **Chapter Code** | Delete |
> | **Section Code** | Delete |
> | **Decimal ID** | Delete or merge into `QiCode` |
> | **QiCode** | Keep |
> | **Title Number** | Delete; it is inside `QiCode` / `Sort Key` |
> | **Level** | Delete; `Type` handles this |
> | **Path** | Delete; path should be generated, not manually stored |
> | **Related Sections** | Delete for now, or make a real relation later |
> | **Last Updated** | Delete; Notion already tracks this automatically |
> | **Status** | Keep |
> | **Tags** | Keep |
> | **Notes** | Keep |
> | **Type** | Keep |
> | **Version** | Optional keep |
> 
> ## The cleaner model
> 
> Use **one database** called something like:
> 
> > **QiCodex Registry**
> 
> Every row is one item:
> 
> - Title
> - Chapter
> - Section
> - Rule
> - Principle
> - Workflow
> - Reference
> - Template
> 
> Hierarchy comes from the **Parent** relation, not from 47 columns.
> 
> Example:
> 
> ```csv
> Name,Type,QiCode,Parent,Sort Key,Status,Tags,Notes,Source,Version
> Title 07 — Security & Access,Title,§ 07,QiCodex,07,draft,,Security/access governance root,,0.1
> Vision & Architecture,Section,§ 07.02.001,Title 07 — Security & Access,07.02.001,draft,legacy,Merged from qiapps_projects_integrations,qiapps_projects_integrations,0.1
> Foundations & Environment,Section,§ 07.02.002,Title 07 — Security & Access,07.02.002,draft,legacy,Merged from qiapps_projects_integrations,qiapps_projects_integrations,0.1
> Core Modules,Section,§ 07.02.003,Title 07 — Security & Access,07.02.003,draft,legacy,Merged from qiapps_projects_integrations,qiapps_projects_integrations,0.1
> ```
> 
> ## One thing I would fix immediately
> 
> This part looks suspicious:
> 
> > `SECTION 1: VISION & ARCHITECTURE`  
> > parented under **Title 07 — Security & Access**
> 
> That may be wrong.
> 
> **Vision & Architecture** sounds more like:
> 
> - **Title 00 — General Provisions**
> - **Title 02 — System Architecture**
> - or **Title 04/05 — QiApps / Projects / Integrations**
> 
> It probably does **not** belong under Security & Access unless that chapter is specifically about access architecture.
> 
> So your cleanup rule should be:
> 
> > **Do not preserve bad parentage just because the import script assigned it.**
> 
> ## Final recommended columns
> 
> Use this exact header:
> 
> ```csv
> Name,Type,QiCode,Parent,Sort Key,Status,Tags,Notes,Source,Version
> ```
> 
> And keep this mental rule:
> 
> > **Name says what it is. Type says what kind of thing it is. Parent says where it lives. QiCode says how it is officially numbered. Everything else better have a damn reason.**
