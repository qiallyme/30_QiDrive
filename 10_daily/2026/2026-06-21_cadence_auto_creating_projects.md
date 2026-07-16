---
layout: page
title: "Cadence auto-creating projects"
slug: "cadence_auto_creating_projects"
created_at: "2026-06-21 16:52:28"
updated_at: "2026-06-21 16:52:28"
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
date: 2026-06-21
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a385d07-93c0-83ea-9dea-e50122827b73"
canonical_ref: ""
---

# Cadence auto-creating projects

## Overview
- **Date**: 2026-06-21 16:52:28
- **Conversation ID**: `6a385d07-93c0-83ea-9dea-e50122827b73`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> for some reason every time i open most notes in obsidian cadence auto creates the same project over and over and over like 15 times.

### Assistant
> That sounds like a plugin state/metadata loop, not you “doing something wrong.” I’ll separate **stop the bleeding now** from **root-cause cleanup** so you don’t end up deleting useful notes while chasing the gremlin.

### Assistant
> Yeah — **Cadence is probably seeing a frontmatter value in your notes and auto-creating a Project entity from it every time the note loads.** Not you. Plugin loop. Annoying as hell.
> 
> Cadence’s own docs say it uses Markdown/frontmatter as the source of truth, creates folders/entities on demand, and has **Background Entity Auto-Creation** when a property suggestion source points to a folder like `Cadence/Contacts` or similar. That is likely the trapdoor here. citeturn882577view1
> 
> ## Stop the bleeding first
> 
> Do this now:
> 
> 1. **Obsidian → Settings → Community plugins**
> 2. **Disable Cadence**
> 3. Do **not** delete the duplicate projects yet.
> 4. Make a quick copy/backup of the vault folder.
> 
> Now Cadence cannot keep spawning more little demon projects while you clean it.
> 
> ## Most likely cause
> 
> One of your note templates or imported notes probably has something like:
> 
> ```yaml
> project: QiSpark
> ```
> 
> or:
> 
> ```yaml
> projects:
>   - QiSpark
> ```
> 
> or maybe:
> 
> ```yaml
> project:
>   - "[[QiSpark]]"
> ```
> 
> And Cadence is interpreting that as:
> 
> > “Oh, this note references a project. I don’t see the project exactly where I expect it. I’ll create it.”
> 
> Then because the existing one doesn’t match cleanly — wrong folder, weird wikilink format, duplicate title, casing, slash in name, sync delay, or metadata refresh — it creates it again. And again. Like a cursed copier.
> 
> ## Fix path
> 
> ### 1. Find the trigger
> 
> In Obsidian search, search the exact repeated project name.
> 
> Example:
> 
> ```text
> "QiSpark"
> ```
> 
> Look especially at the YAML/frontmatter at the top of notes.
> 
> You’re looking for a common repeated field like:
> 
> ```yaml
> project:
> ```
> 
> ```yaml
> projects:
> ```
> 
> ```yaml
> client:
> ```
> 
> ```yaml
> initiative:
> ```
> 
> ```yaml
> workspace:
> ```
> 
> Anything Cadence may have configured as a Project relationship.
> 
> ## 2. Check your templates
> 
> Check these folders if they exist:
> 
> ```text
> Templates/
> 00_Templates/
> Cadence/
> 10_qispark/cadence/
> .obsidian/plugins/
> ```
> 
> The big red flag is a default note template that stamps the same project into every note.
> 
> Bad:
> 
> ```yaml
> project: QiSpark
> ```
> 
> Better:
> 
> ```yaml
> project:
> ```
> 
> or remove the field entirely unless that note truly belongs to the project.
> 
> ## 3. Check Cadence settings
> 
> When you re-enable Cadence, go to:
> 
> **Settings → Cadence → Custom Entity Properties**
> 
> Look for any Project-related property with suggestion source like:
> 
> ```text
> folder:Cadence/Projects
> ```
> 
> or maybe:
> 
> ```text
> folder:10_qispark/cadence/projects
> ```
> 
> Cadence docs specifically say folder-based suggestion sources can auto-create referenced notes in the background. That is likely what is biting you. citeturn882577view1
> 
> For now, turn off or neutralize auto-creation behavior if the setting exists, or change the suggestion source to `none` until the vault is clean.
> 
> ## 4. Clean the duplicates safely
> 
> After Cadence is disabled:
> 
> 1. Open the duplicate project notes.
> 2. Keep the oldest/best/most complete one.
> 3. Move the extras to a quarantine folder, not trash.
> 
> Use something like:
> 
> ```text
> 99_quarantine/cadence_duplicate_projects/
> ```
> 
> Do **not** hard-delete until you confirm nothing useful is inside.
> 
> ## My blunt read
> 
> This is probably caused by **too much automation too early**. Cadence is trying to be CRM + PM + planner + relationship engine, but your QiSpark vault already has structure. Two systems are both trying to “own” project metadata.
> 
> For your setup, I would not let Cadence freely auto-create Projects from random note metadata. That is chaos fuel.
> 
> ## Better rule for your vault
> 
> Use this:
> 
> ```yaml
> cadence_project:
> ```
> 
> only on notes that Cadence should manage.
> 
> Do **not** use generic:
> 
> ```yaml
> project:
> ```
> 
> across the whole vault unless you want every plugin to treat it as a project relationship.
> 
> Generic metadata names are cute until every plugin starts hallucinating jurisdiction. Rename the field and make it explicit.

### User
> this one triggered something

### Assistant
> Yep. This file is suspicious. The trigger is probably **invalid-ish YAML values caused by the `... ...` placeholders**.
> 
> Your frontmatter has fields like:
> 
> ```yaml
> layout: page ... ...
> status: proposed ... ...
> sensitivity: internal ... ...
> classification: business_internal ... ...
> source_type: manual ... ...
> ```
> 
> That is not clean metadata. It looks like a templating/export artifact. Obsidian/Cadence may parse those as strange scalar values, then Cadence tries to resolve or create entities based on them. The file also has a generic `template_key` and many empty relationship-looking fields like `owner`, `realm_label`, `context`, `target_system`, `target_scope`, `registry_key`, and `standard_key`, which can confuse an entity-driven plugin if Cadence is watching those property names. fileciteturn0file0
> 
> ## The immediate fix
> 
> Change this:
> 
> ```yaml
> layout: page ... ...
> status: proposed ... ...
> sensitivity: internal ... ...
> classification: business_internal ... ...
> source_type: manual ... ...
> ```
> 
> To this:
> 
> ```yaml
> layout: page
> status: proposed
> sensitivity: internal
> classification: business_internal
> source_type: manual
> ```
> 
> And I’d also change this:
> 
> ```yaml
> title: "Procedure: "
> ```
> 
> To either:
> 
> ```yaml
> title: ""
> ```
> 
> or:
> 
> ```yaml
> title: "Procedure"
> ```
> 
> That trailing colon inside the title is legal because it is quoted, but it is still dumb bait for tools that do sloppy parsing. Don’t feed the gremlin.
> 
> ## Safer cleaned version
> 
> Use this instead:
> 
> ```yaml
> ---
> layout: page
> title: ""
> slug: ""
> summary: ""
> status: proposed
> created_at: ""
> updated_at: ""
> author: ""
> owner: ""
> sensitivity: internal
> classification: business_internal
> realm_label: ""
> context: ""
> aliases: []
> tags: []
> keywords: []
> references: []
> target_system: ""
> target_scope: ""
> canonical_ref: ""
> uid: ""
> template_key:
>   - operational-template
> source_type: manual
> adr_id: ""
> supersedes: ""
> artifact_kind: ""
> registry_key: ""
> standard_key: ""
> ---
> 
> # {{title}}
> 
> ## Objective
> 
> ## Prerequisites
> 
> ## Steps
> 
> ## Verification
> ```
> 
> ## My stronger recommendation
> 
> For Cadence specifically, I would **strip this template down** until the plugin stops multiplying projects.
> 
> Use a minimal test version:
> 
> ```yaml
> ---
> title: ""
> status: proposed
> tags: []
> template_key:
>   - operational-template
> ---
> 
> # {{title}}
> 
> ## Objective
> 
> ## Prerequisites
> 
> ## Steps
> 
> ## Verification
> ```
> 
> Then re-enable Cadence and open the note.
> 
> If the duplicate project creation stops, the issue is in one of the extra metadata fields. Then add fields back in batches.
> 
> ## Most likely problem fields
> 
> These are the ones I’d side-eye first:
> 
> ```yaml
> owner: ""
> realm_label: ""
> context: ""
> target_system: ""
> target_scope: ""
> registry_key: ""
> standard_key: ""
> ```
> 
> They sound like entity references. Cadence may be treating one of them as something it needs to create in its project/entity system.
> 
> ## Bottom line
> 
> This template is not safe as-is. The `... ...` placeholders are the obvious bug. Clean those first, then test with Cadence disabled/enabled.
