---
layout: page
title: "Using Directus 101"
slug: "using_directus_101"
created_at: "2026-06-18 17:29:18"
updated_at: "2026-06-18 17:29:18"
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
uid: "6a347138-e0f4-83ea-99b7-4108a7df1d15"
canonical_ref: ""
---

# Using Directus 101

## Overview
- **Date**: 2026-06-18 17:29:18
- **Conversation ID**: `6a347138-e0f4-83ea-99b7-4108a7df1d15`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> directus is up and running how do i tuse it.

### Assistant
> Directus being “up” is step one. Now we turn it from a shiny admin screen into your actual control panel for the QiLabs source-of-truth stack: schema first, then data, then rules/API.

### Assistant
> Directus is your **front desk/admin cockpit** for Supabase/Postgres.
> 
> **Supabase/Postgres = truth.**  
> **Directus = human-friendly interface + permissions + API layer + automations.**
> 
> Do **not** treat Directus like another random note app. Use it as the structured control panel for data you want AI/apps/scripts to query cleanly.
> 
> ## 1. First mental model
> 
> In Directus:
> 
> | Directus word | Plain English |
> |---|---|
> | **Collection** | Database table |
> | **Field** | Column |
> | **Item** | Row / record |
> | **Relation** | Link between tables |
> | **Data Studio** | Admin UI |
> | **Flow** | Automation |
> | **Role / Policy / Permission** | Who can see or change what |
> | **API Token** | Key for apps/scripts/AI to query data |
> 
> Directus collections are database tables with Directus metadata on top, and Directus-specific system tables use the `directus_` prefix. It can create collections through the UI or sit on top of existing SQL tables. citeturn386344search1
> 
> ## 2. What to do first — in order
> 
> ### Step 1 — Log in and check the admin UI
> 
> Open your Directus URL, probably something like:
> 
> `http://YOUR_SERVER_IP:8055/admin`
> 
> or
> 
> `https://directus.yourdomain.com/admin`
> 
> Log in with the admin email/password from setup.
> 
> Once inside, do not start making 40 random collections. That is how systems become spaghetti with a login screen.
> 
> ---
> 
> ## 3. Create your first real collection: `keybits`
> 
> This should be your first useful table because it matches how you actually think: fast capture, later structured.
> 
> Go to:
> 
> **Settings gear → Data Model → Create Collection**
> 
> Create:
> 
> ### Collection name
> 
> `keybits`
> 
> ### Purpose
> 
> Quick captured thoughts, events, decisions, notes, facts, evidence pointers.
> 
> ### Fields to add
> 
> | Field | Type | Why |
> |---|---|---|
> | `id` | UUID or auto ID | Unique record |
> | `title` | String | Short label |
> | `body` | Text | The actual note |
> | `capture_type` | Dropdown | note, event, task, evidence, decision, idea |
> | `status` | Dropdown | inbox, processed, archived |
> | `source` | String | voice, text, email, screenshot, import |
> | `occurred_at` | DateTime | When it happened |
> | `created_at` | DateTime | When entered |
> | `tags` | JSON or relation later | Search grouping |
> | `priority` | Dropdown | low, normal, high, urgent |
> 
> Then go to:
> 
> **Content → keybits → Create Item**
> 
> Add one test item:
> 
> **Title:** Directus is online  
> **Capture type:** decision  
> **Body:** Directus will be the admin UI for structured QiLabs data, with Supabase/Postgres as the database truth.  
> **Status:** inbox
> 
> That is your first real record.
> 
> ---
> 
> ## 4. Then create the core QiLabs collections
> 
> Do **not** start with every folder in QiLabs. Start with the minimum database spine.
> 
> ### Core collections
> 
> | Collection | What it stores |
> |---|---|
> | `keybits` | raw captures / notes / events |
> | `entities` | people, companies, agencies, systems |
> | `projects` | active workstreams |
> | `matters` | legal/admin/case-like situations |
> | `tasks` | action items |
> | `sources` | files, emails, screenshots, URLs, Drive refs |
> | `events` | dated happenings |
> | `decisions` | locked choices / ADR-style records |
> | `tags` | controlled labels |
> | `relationships` | links between entities/items |
> 
> That is enough. Anything more right now is probably noise wearing a fake mustache.
> 
> ---
> 
> ## 5. Set up relationships
> 
> Directus supports standard database relationships like many-to-one, one-to-many, many-to-many, and many-to-any. citeturn386344search2
> 
> Use these:
> 
> ### `tasks`
> 
> Add:
> 
> | Field | Relation |
> |---|---|
> | `project_id` | many tasks → one project |
> | `matter_id` | many tasks → one matter |
> | `related_entity_id` | many tasks → one entity |
> 
> ### `events`
> 
> Add:
> 
> | Field | Relation |
> |---|---|
> | `matter_id` | many events → one matter |
> | `source_id` | many events → one source |
> | `entity_id` | many events → one entity |
> 
> ### `sources`
> 
> Add:
> 
> | Field | Relation |
> |---|---|
> | `matter_id` | many sources → one matter |
> | `project_id` | many sources → one project |
> 
> This makes Directus queryable instead of just “organized vibes.”
> 
> ---
> 
> ## 6. Set permissions before connecting apps
> 
> By default, do **not** make your data public. Directus authentication can use tokens, cookies, or sessions, and private data requires authentication unless you intentionally configure the Public role. citeturn445064search0
> 
> Go to:
> 
> **Settings → User Directory / Roles & Permissions**
> 
> Create a service user:
> 
> ### User
> 
> `qilabs_service`
> 
> ### Role
> 
> `QiLabs Service`
> 
> Give it access only to the collections your scripts/AI need.
> 
> Suggested permissions:
> 
> | Collection | Create | Read | Update | Delete |
> |---|---:|---:|---:|---:|
> | `keybits` | yes | yes | yes | no |
> | `tasks` | yes | yes | yes | no |
> | `projects` | no | yes | yes | no |
> | `matters` | no | yes | yes | no |
> | `sources` | yes | yes | yes | no |
> | `entities` | yes | yes | yes | no |
> 
> No delete for service accounts. Ever. Delete is how “oops” becomes “where is my life.”
> 
> ---
> 
> ## 7. Create an API token
> 
> For scripts, local AI, or your future QiCapture app:
> 
> Go to your service user → create/copy a **static token**.
> 
> Directus says static tokens do not expire unless regenerated, while standard/session tokens are short-lived and need refreshing. citeturn445064search0
> 
> Store it in your app/server `.env`, not in notes:
> 
> ```env
> DIRECTUS_URL=https://your-directus-url.com
> DIRECTUS_TOKEN=your_token_here
> ```
> 
> Then test the API:
> 
> ```bash
> curl -H "Authorization: Bearer YOUR_TOKEN" \
>   https://your-directus-url.com/items/keybits
> ```
> 
> Directus exposes REST and GraphQL APIs, and the API adapts to your project schema. citeturn445064search2
> 
> ---
> 
> ## 8. Use Directus daily like this
> 
> ### For you manually
> 
> Use Directus to:
> 
> - add/edit records
> - review captured notes
> - clean inbox items
> - connect notes to matters/projects/entities
> - check what data exists
> - fix bad imports
> 
> ### For AI/tools
> 
> Use the API to:
> 
> - insert new captures
> - search records
> - pull context for briefings
> - update statuses
> - attach source references
> - feed embeddings/vector search later
> 
> ### For automation
> 
> Use **Flows** later for:
> 
> - when a `keybit` is created → classify it
> - when a `task` becomes urgent → send notification
> - when a `source` is added → mark related matter updated
> - when a decision is created → lock it into QiDNA/QiSpark
> 
> Directus Flows are event-driven automations made from triggers and operations. citeturn445064search5
> 
> ---
> 
> ## 9. The actual Cody workflow
> 
> Here is the clean operational loop:
> 
> ### Capture
> 
> Fast note goes into `keybits`.
> 
> ### Process
> 
> You or AI assigns:
> 
> - type
> - matter/project
> - entity
> - priority
> - status
> 
> ### Promote
> 
> Important stuff becomes:
> 
> - `event`
> - `task`
> - `decision`
> - `source`
> - `matter`
> 
> ### Query
> 
> Apps/AI can ask:
> 
> - “What happened with Hertz?”
> - “Show open tasks for QiServer.”
> - “What records mention Comfort Keepers?”
> - “What decisions did we lock about Supabase vs Directus?”
> - “What sources support this claim?”
> 
> That is the point. Not decoration. Queryable reality.
> 
> ---
> 
> ## 10. What I would do next
> 
> Create these **three collections only** right now:
> 
> 1. `keybits`
> 2. `projects`
> 3. `matters`
> 
> Then create 5 test records:
> 
> | Collection | Record |
> |---|---|
> | `projects` | QiLabs Source of Truth |
> | `projects` | QiDriveMaid |
> | `matters` | Lyft Hertz Rental Dispute |
> | `matters` | Comfort Keepers Pay Dispute |
> | `keybits` | Directus is online and connected |
> 
> After that, add `tasks`, `sources`, and `entities`.
> 
> Do **not** build the whole empire before proving the loop. Build the spine first. Then we can make it gorgeous.
