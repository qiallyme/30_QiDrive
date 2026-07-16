---
layout: page
title: "Gemini UI and Backend Prompts"
slug: "gemini_ui_and_backend_prompts"
created_at: "2026-06-14 21:59:38"
updated_at: "2026-07-16T06:49:33-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-009.json"
template_key: master-template
date: 2026-06-14
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a2f6a76-27f8-83ea-90c2-a5a8be41088c"
canonical_ref: ""
---

# Gemini UI and Backend Prompts

## Overview
- **Date**: 2026-06-14 21:59:38
- **Conversation ID**: `6a2f6a76-27f8-83ea-90c2-a5a8be41088c`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> hey what if we gave gemini new stitcher for the ui and gemini coder to do the app code backend stuff and try to see how close gemeni can get to what i want. what would the prompts be

### Assistant
> Yes. This is actually a smart split: let Gemini/Stitch chase **visual structure**, and let Gemini Coder build the **boring reliable app skeleton**. Don’t let either one “invent the product,” though. The product doctrine is already locked enough.

### Assistant
> Yes. Use Gemini like this:
> 
> - **Stitch / UI tool** = “make the interface feel right”
> - **Gemini Coder** = “turn the interface into clean React/app structure”
> - **Backend work** = only for **QiLife / Mom’s Care / QiBit capture**, not QiAccess Start v1 unless there is a real reason
> 
> Important: **do not let Gemini decide the architecture.** QiAccess Start already has doctrine: it is the operational front door, launcher, access dashboard, system map, and control panel for Cody’s life systems, not a generic SaaS dashboard. fileciteturn2file0
> 
> ## Prompt 1 — Gemini Stitch / UI Designer
> 
> Paste this into Gemini Stitch/UI:
> 
> ```text
> Design a modern, mobile-first UI for “QiAccess Start.”
> 
> Product purpose:
> QiAccess Start is Cody’s operational front door: a personal start page, launcher, access dashboard, and system map. It helps Cody know what exists, where to go next, what needs attention, and how to safely access services.
> 
> This is NOT a generic SaaS dashboard.
> This is a personal operating system front door for:
> - daily priorities
> - Mom’s Care
> - Family OS
> - legal
> - finance
> - Google Drive / QiNexus storage
> - Wiki.js knowledge base
> - qiserver/self-hosted tools
> - protected admin services
> - project/workbench links
> 
> Design tone:
> Clean, sharp, operational, calm, slightly futuristic, not corporate.
> Should feel like a command center for real life, not a startup analytics dashboard.
> Readable on Android phone first, then desktop.
> 
> Primary screens/routes:
> 1. Home Dashboard `/`
>    - “Where do I go next?”
>    - today’s focus
>    - current priorities
>    - urgent care/legal/finance/system alerts
>    - quick launch cards
>    - recently used tools
>    - system status summary
> 
> 2. Start / Launcher `/start`
>    - app tiles
>    - service tiles
>    - categories
>    - favorites
>    - badges: public, protected, private, local, external
>    - search/filter
> 
> 3. Access `/access`
>    - protected/admin service entry
>    - clear warning labels
>    - private/public separation
>    - Tailscale / Cloudflare Access notes
>    - Portainer, Cockpit, Paperless, Open WebUI, Wiki.js, Supabase, GitHub, etc.
> 
> 4. QiServer `/server`
>    - self-hosted service map
>    - service cards
>    - internal URLs
>    - health/status indicators
>    - Docker/server tools
> 
> 5. Knowledge Base `/knowledge`
>    - Wiki.js entry points
>    - Family OS
>    - Mom’s Care
>    - Legal
>    - Finance
>    - Tech
>    - Runbooks
>    - Reference
> 
> 6. Storage / QiNexus `/storage`
>    - root bucket cards:
>      00_inbox, 01_workbench, 02_timeline, 03_life, 04_people,
>      05_business, 06_finance, 07_legal, 08_tech, 09_assets,
>      10_data, 11_reference, 12_archive, 13_system
>    - simple “where should this file go?” helper area
> 
> 7. Roadmap `/roadmap`
>    - phases
>    - current build state
>    - next actions
>    - done / active / blocked statuses
> 
> 8. Blueprint `/blueprint`
>    - readable summary of the operating doctrine
>    - system map
>    - route → page → feature → component → data model
> 
> Navigation:
> Use a strong left nav on desktop.
> Use bottom nav or compact drawer on mobile.
> The UI must support ADHD-friendly scanning:
> - clear hierarchy
> - low clutter
> - obvious next action
> - short labels
> - visual grouping
> - strong status badges
> - no giant walls of text
> 
> Output needed:
> - high-fidelity screen designs
> - reusable component ideas
> - color/token suggestions
> - spacing and typography guidance
> - mobile and desktop layouts
> - example cards/tables/badges
> - do not invent new product names
> - do not turn this into a CRM, client portal, or generic business dashboard
> ```
> 
> ## Prompt 2 — Gemini Coder / Frontend Implementation
> 
> Use this after Stitch gives you a design:
> 
> ```text
> You are working inside the QiAccess Start app repository.
> 
> Goal:
> Implement the QiAccess Start frontend structure using the provided UI design as visual guidance, but preserve the existing product doctrine and architecture.
> 
> Product doctrine:
> QiAccess Start is the operational front door, start page, launcher, access dashboard, and system map for Cody’s life systems.
> 
> Do not turn it into a generic SaaS dashboard.
> Do not turn it into a CRM.
> Do not create client/tenant architecture.
> Do not add Supabase unless explicitly required.
> Do not rebuild auth.
> Do not break existing routes, links, deployment, or working app behavior.
> 
> Current intended routes:
> - `/` = QiAccess Start home
> - `/start` = launcher/start page
> - `/access` = protected service/control section
> - `/server` = QiServer
> - `/apps` = app directory
> - `/storage` = Google Drive / QiNexus
> - `/roadmap` = QiRoadmap
> - `/blueprint` = QiBlueprint summary
> - `/system` = system status/settings
> 
> Use this app structure:
> - `src/app`
> - `src/layouts`
> - `src/pages`
> - `src/components/ui`
> - `src/lib`
> - `src/styles`
> 
> Use these numbered feature modules:
> - `src/features/00_dashboard`
> - `src/features/01_start`
> - `src/features/02_access`
> - `src/features/03_qiserver`
> - `src/features/04_knowledge_base`
> - `src/features/05_storage`
> - `src/features/06_roadmap`
> - `src/features/07_blueprint`
> 
> Each feature module should include:
> - `components/`
> - `data/`
> - `README.md`
> 
> Use this mental model:
> Route → Page → Feature → Component → Data
> 
> Create static config/data files first:
> - `launcherApps.ts`
> - `accessLinks.ts`
> - `serverServices.ts`
> - `storageBuckets.ts`
> - `roadmapPhases.ts`
> - `blueprintSections.ts`
> 
> Implementation rules:
> 1. Inspect the repo first.
> 2. Do not delete files.
> 3. Do not rename working routes unless required and reported.
> 4. Preserve existing deployment assumptions.
> 5. Use TypeScript if the repo already uses it.
> 6. Keep components simple and readable.
> 7. Prefer static data over backend persistence for v1.
> 8. Add TODO comments only where useful.
> 9. Update or create README files explaining each feature.
> 10. After changes, provide:
>    - files changed
>    - routes added/updated
>    - known gaps
>    - commands to run locally
>    - any risks
> 
> First task:
> Create or refactor the frontend skeleton so the app has the route/page/feature/data structure above, with placeholder data and clean reusable UI components.
> ```
> 
> ## Prompt 3 — Gemini Coder / Backend, but for QiLife or Mom’s Care
> 
> For QiAccess Start, backend is mostly premature. The blueprint specifically says static config is enough for v1 and warns not to add Supabase without a specific reason. fileciteturn2file0
> 
> So use this backend prompt only for **QiLife**, **Mom’s Care**, or **QiBit capture**:
> 
> ```text
> You are working on the QiLife backend foundation, not the QiAccess Start static launcher.
> 
> Goal:
> Create a safe backend foundation for capturing and organizing life data as QiBits.
> 
> Core concept:
> A QiBit is one captured unit of life data. It may represent a care note, finance note, legal event, document reference, task, system log, medication note, symptom note, appointment note, or general life capture.
> 
> Backend goals:
> - receive captures
> - normalize metadata
> - support review workflow
> - support timeline/event history
> - prepare for Supabase persistence
> - keep personal/care/legal/finance data separated by domain
> - avoid overengineering
> 
> Do not build a giant platform.
> Do not create multi-tenant SaaS architecture.
> Do not add fake business/client portal logic.
> Do not store real secrets.
> Do not include private production keys.
> Do not run destructive migrations.
> 
> Suggested backend modules:
> - capture
> - review
> - timeline
> - people
> - care
> - finance
> - legal
> - documents
> - system
> 
> Core tables or models to prepare:
> - `qibits`
> - `qibit_sources`
> - `qibit_tags`
> - `qibit_categories`
> - `people`
> - `care_events`
> - `finance_events`
> - `legal_events`
> - `document_refs`
> - `review_queue`
> - `system_events`
> 
> Every record should support:
> - id
> - created_at
> - updated_at
> - source
> - domain
> - title
> - body/notes
> - status
> - tags
> - related_person_id where relevant
> - related_document_id where relevant
> - confidence/review status where relevant
> 
> Implementation rules:
> 1. Inspect existing repo first.
> 2. Do not overwrite existing migrations.
> 3. Create safe starter files only.
> 4. Use placeholder env values.
> 5. Keep local/dev friendly.
> 6. Add README documentation.
> 7. Separate backend code from frontend launcher code.
> 8. Make clear what is implemented now vs future.
> 9. Do not invent sensitive medical/legal conclusions.
> 10. Produce a final report.
> 
> First task:
> Create the backend foundation, schema draft, example seed data using fake data only, and documentation explaining how QiBits move from capture → review → timeline/domain tables.
> ```
> 
> ## Prompt 4 — Gemini Coder / “Audit What Stitch Made”
> 
> Use this after it generates stuff, because Gemini will absolutely get cute and drift if you let it:
> 
> ```text
> Audit the current QiAccess Start implementation against the product doctrine.
> 
> Check for:
> - generic SaaS dashboard drift
> - CRM/client/tenant concepts that do not belong
> - unnecessary backend/database usage
> - broken route naming
> - missing feature folders
> - missing README files
> - unclear Start vs Access boundary
> - unsafe public exposure of admin services
> - too much visual clutter
> - mobile usability problems
> - hardcoded secrets or sensitive URLs
> - files that should be static config instead of logic
> 
> Expected doctrine:
> QiAccess Start is one operational app with start, launcher, access, server, knowledge, storage, roadmap, and blueprint sections.
> 
> Start opens tools.
> Access manages protected/admin service entry.
> Repo docs define how the system is built.
> Wiki.js explains how the system is used.
> Static data is enough for v1 unless there is a specific reason for persistence.
> 
> Output:
> 1. What is aligned
> 2. What is wrong
> 3. What should be removed
> 4. What should be renamed
> 5. What should be simplified
> 6. Exact file-level recommendations
> 7. Priority order for fixes
> ```
> 
> ## The smart workflow
> 
> Do it in this order:
> 
> 1. **Stitch:** generate UI concept.
> 2. **You pick one design direction.**
> 3. **Gemini Coder:** implement frontend skeleton only.
> 4. **Gemini Coder audit:** catch drift.
> 5. **Only then:** backend prompt for QiLife/QiBit/Mom’s Care.
> 
> The trap is trying to make Gemini build the whole empire in one shot. Don’t. Make it do **one slice at a time** or it’ll hallucinate a cathedral, and we already said no cathedrals.

### User
> i really dont want to restrict it at all i want to see what it comes up with if we just give it the goal of what the app should do.

### Assistant
> I get it. You don’t want “obedient implementation.” You want **creative divergence** — let Gemini show you what *it thinks the product wants to become*. That’s valid. Just separate “exploration prompt” from “production prompt,” or it’ll pollute your repo with alien architecture.

### Assistant
> Yes — that’s the better experiment.
> 
> What you want is **not** “Gemini, follow my architecture.”  
> You want: **“Gemini, here is the problem. Show me what you think the app should become.”**
> 
> That’s useful because it can surface ideas we would not reach while staying inside the current folder doctrine. The only thing I would still protect is **repo safety**: no secrets, no destructive edits, no deleting. Everything else can be wide open.
> 
> Your core goal is enough: QiAccess Start exists to reduce friction, centralize access, clarify priorities, and make Cody’s real-life systems understandable at a glance; it should help you see what exists, know where to go, launch tools, access protected services, find docs, and understand the system. fileciteturn4file0
> 
> ## Prompt 1 — Gemini Stitch, “Unrestricted Product Vision”
> 
> ```text
> Design the best possible UI/UX for an app called QiAccess Start.
> 
> Do not simply make a generic dashboard.
> 
> Goal:
> QiAccess Start is the front door for a real personal operating system. It should help one person manage and access their life systems from one place.
> 
> The app should help with:
> - knowing what needs attention now
> - launching the right tool or system
> - accessing self-hosted services
> - navigating personal documents and storage
> - opening knowledge base / Wiki.js docs
> - tracking care, family, legal, finance, tech, and daily priorities
> - making a complex life system understandable at a glance
> - reducing friction and decision fatigue
> - making the next action obvious
> 
> Context:
> The user has a self-hosted server, apps, documents, care workflows, finance/legal workflows, family systems, and knowledge base docs. The app should feel like a personal command center, not a corporate SaaS product.
> 
> Creative freedom:
> You may invent the layout, navigation, screen structure, component model, hierarchy, visual language, and interaction patterns.
> You may propose features I did not list.
> You may rethink the information architecture.
> You may suggest screens, widgets, modes, automations, AI helpers, search, timeline views, launchers, alerts, and system maps.
> 
> Design priorities:
> - mobile-first
> - ADHD-friendly
> - fast scanning
> - low clutter
> - clear next actions
> - emotionally calm but operationally powerful
> - personal, not corporate
> - practical, not decorative
> - suitable for daily use
> 
> Output:
> Create a high-quality UI concept for this app.
> Include:
> 1. main app layout
> 2. homepage/dashboard
> 3. launcher/tool access screen
> 4. system/service map
> 5. knowledge/docs area
> 6. storage/files area
> 7. care/family/legal/finance areas if useful
> 8. mobile navigation
> 9. desktop navigation
> 10. reusable components
> 11. visual style direction
> 12. anything else you think this app needs
> 
> Do not ask me to confirm every detail. Make strong product decisions.
> ```
> 
> ## Prompt 2 — Gemini Coder, “Build What You Think It Should Be”
> 
> Use this in a **branch or experimental copy**, not your main app. We are letting it cook, not handing it the deed to the house.
> 
> ```text
> You are building an experimental full-stack prototype for QiAccess Start.
> 
> Goal:
> Create the best working prototype you can for an app that serves as the front door to a personal operating system.
> 
> QiAccess Start should help the user:
> - see what needs attention
> - launch tools
> - access self-hosted services
> - navigate documents and storage
> - open knowledge base/docs
> - understand their system
> - manage life domains like care, family, legal, finance, tech, projects, and daily action
> - reduce decision fatigue
> - know the next best action
> 
> You have creative freedom.
> 
> You may decide:
> - app architecture
> - routes
> - layout
> - components
> - data model
> - backend shape
> - database schema draft
> - API routes
> - UI patterns
> - dashboard widgets
> - search behavior
> - launcher model
> - timeline/capture model
> - status/alert model
> - domain organization
> - navigation structure
> 
> Build an actual usable prototype, not just a design.
> 
> Suggested product feel:
> A personal command center for real life.
> Not a generic SaaS dashboard.
> Not a CRM.
> Not a toy landing page.
> It should feel operational, calm, smart, and useful.
> 
> Hard safety rules:
> - do not use real secrets
> - do not include API keys
> - do not delete existing files
> - do not run destructive commands
> - do not expose private admin services publicly
> - use fake/example data only
> - clearly label assumptions
> 
> Preferred output:
> 1. implement the prototype
> 2. create or update frontend screens
> 3. create backend/API stubs if useful
> 4. create fake seed/config data
> 5. document how the app works
> 6. document what you invented
> 7. document what should be reviewed before merging
> 8. provide commands to run locally
> 9. provide a summary of files changed
> 
> Important:
> Do not over-ask questions.
> Make strong assumptions and proceed.
> The goal is to see how close you can get to the desired product from the goal alone.
> ```
> 
> ## Prompt 3 — Gemini Coder, “Full Product Architect Mode”
> 
> This one is even less restricted. Use it when you want Gemini to think like a founder/product architect.
> 
> ```text
> Act as a product architect, UX designer, and full-stack engineer.
> 
> I want you to design and prototype an app called QiAccess Start.
> 
> The only real goal:
> Create the best possible personal operating system front door for someone managing a complex life system.
> 
> The app should help the user:
> - know what matters today
> - launch tools and services
> - access documents and knowledge
> - manage personal/family/care/legal/finance/tech workflows
> - understand system structure
> - capture information quickly
> - find things later
> - avoid chaos
> - make better next decisions
> 
> You are not required to follow any existing architecture.
> You may propose a better one.
> You may create new routes, components, models, APIs, database tables, workflows, or concepts.
> You may invent features if they genuinely serve the goal.
> 
> Think deeply about:
> - what the homepage should show
> - what daily use looks like
> - how the app should reduce cognitive load
> - how capture/review/timeline should work
> - how docs/files/services should connect
> - how alerts and priorities should work
> - how protected tools should be represented safely
> - how a non-technical user could understand the system
> - how a power user could move fast
> 
> Build a working prototype with fake data.
> 
> Safety:
> - no real secrets
> - no destructive actions
> - no private data
> - no exposing admin tools publicly
> - clearly mark assumptions
> 
> Deliver:
> 1. product concept
> 2. implemented prototype
> 3. app structure
> 4. data model
> 5. backend/API plan or starter
> 6. UI screens
> 7. fake data
> 8. run instructions
> 9. what you believe the app should become next
> ```
> 
> ## Prompt 4 — After It Builds: “Tell Me What You Were Thinking”
> 
> This is the money prompt. Use it after Gemini generates the thing:
> 
> ```text
> Explain the product decisions you made.
> 
> I want to understand:
> 1. what you think QiAccess Start is
> 2. what problem you optimized for
> 3. what you intentionally included
> 4. what you intentionally left out
> 5. what assumptions you made
> 6. what you think the homepage should accomplish
> 7. what the core daily workflow is
> 8. what backend/data model you chose and why
> 9. what parts are experimental
> 10. what should be kept, changed, or thrown away
> 
> Be direct. Do not flatter the project.
> Tell me where the concept is strong and where it is weak.
> ```
> 
> ## My take
> 
> Do the unrestricted version. Absolutely.
> 
> But don’t run it straight on your canonical repo like a maniac. Put it in:
> 
> ```text
> experiments/gemini_qiaccess_unrestricted/
> ```
> 
> or a branch like:
> 
> ```text
> experiment/gemini-unrestricted-qistart
> ```
> 
> Then we compare:
> 
> | Version | Purpose |
> |---|---|
> | **Doctrine version** | safe, aligned, buildable |
> | **Gemini wild version** | idea discovery |
> | **Final version** | steal the best ideas, reject the nonsense |
> 
> That’s the clean move: **let Gemini hallucinate strategically, then we harvest.**
