---
layout: page
title: Qi Os Home Blueprint
slug: qi-os-home-blueprint
summary: ""
status: active
created_at: "2026-07-16T06:19:39-04:00"
updated_at: "2026-07-16T06:19:39-04:00"
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: 27ce53ce261541b58e801047a1c5c010
canonical_ref: ""
source_type: manual
template_key: master-template
---

# QiAccess Start Blueprint

**Version:** 1.0 Draft  
**Status:** Active Working Doctrine  
**Owner:** Cody  
**Scope:** Personal, family, care, knowledge, legal, finance, tech, and self-hosted systems  
**Primary Runtime:** qiserver  
**Primary Knowledge Base:** Wiki.js  
**Primary Storage Backbone:** Google Drive / QiNexus  
**Primary App / Front Door:** QiAccess Start  

---

# 00. Purpose

QiAccess Start is Cody’s operational front door and personal start page.

It exists to reduce friction, centralize access, clarify priorities, and make Cody’s real-life systems understandable at a glance.

This blueprint replaces the older business/client-oriented QiOS blueprint as the active doctrine. The older blueprint remains an ancestor document, but the current system is about Cody’s actual life: family, care, legal, finance, knowledge, tech, and daily action.

This is not a generic dashboard.

This is the start page for Cody’s operating system.

---

# 01. Core Doctrine

## 01.01 Operating Statement

QiAccess Start is the operational front door for Cody’s life, systems, care responsibilities, documents, and self-hosted tools.

## 01.02 Primary Goal

The goal is not to build more apps.

The goal is to create one coherent entry point where Cody can:

- see what exists
- know where to go
- launch the right tool
- access protected services
- find documentation
- understand the system structure
- reuse the pattern later for Mom’s Care and other apps

## 01.03 Practical Truth

Current reality matters more than theoretical architecture.

The active system includes:

- access.qially.com
- qiserver
- Portainer
- Cockpit
- Wiki.js
- self-hosted services
- Google Drive / QiNexus
- Mom’s Care app work
- family, legal, and finance workflows

## 01.04 Anti-Chaos Rule

When naming, folder structure, or architecture becomes confusing, return to one question:

**What job does this part do?**

If it has no clear job, it is noise, legacy, or future-state.

---

# 02. System Map

## 02.01 QiAccess Start

QiAccess Start is the operational front door, start page, launcher, and access dashboard.

It answers:

**Where do I go next, and how do I safely get there?**

It shows main sections, current priorities, service shortcuts, quick actions, system status, Wiki.js links, storage links, and protected service entry points.

It launches Mom’s Care, Family OS, QiNexus, Wiki.js, Portainer, Cockpit, Paperless, Open WebUI, Supabase, GitHub, legal tools, finance tools, server tools, and documentation spaces.

QiAccess Start is not three separate products. It is one operational app with start, launcher, access, and server sections.

## 02.02 QiServer

QiServer is the self-hosted machine and service layer.

It represents the stack running on qiserver: Docker services, Portainer, Cockpit, Wiki.js, Paperless, Open WebUI, Ollama, Neo4j, dashboards, routing, backups, and monitoring.

## 02.03 Wiki.js

Wiki.js is the readable knowledge base and manual library running from qiserver.

It should hold Family OS docs, Mom’s Care manuals, QiAccess Start docs, tech runbooks, legal and finance process notes, household checklists, personal guides, and reference pages.

## 02.04 Repo Docs

Repo docs are the engineering and source-of-truth layer for how the app is built.

They hold the blueprint, roadmap, architecture, ADRs, folder structure, developer instructions, app flow, service map, and deployment/runbook notes.

## 02.05 Google Drive / QiNexus

Google Drive is the cloud storage backbone.

QiNexus is Cody’s personal PARA-inspired organization system for files, working docs, assets, data, references, and archives.

---

# 03. Naming Model

- **QiAccess Start** — main operational front door, start page, launcher, and access dashboard
- **Start** — landing/home and launcher experience inside QiAccess Start
- **Access** — protected service/control section inside QiAccess Start
- **QiServer** — machine/service layer running self-hosted tools
- **Wiki.js** — readable knowledge base and manual library
- **QiBlueprint** — guiding doctrine: why the system exists and how it stays coherent
- **QiRoadmap** — execution sequence: what gets built next
- **QiNexus** — Cody’s personal storage/workspace model

---

# 04. Current Operating Model

## 04.01 Deployment Reality

The working front-door URL may remain:

**access.qially.com**

The codebase may still reference QiAccess for now. That is acceptable while the product model is being aligned.

The internal product model should become:

- `/` = QiAccess Start home
- `/start` = launcher/start page
- `/access` = protected service/control section
- `/server` = QiServer
- `/apps` = app directory
- `/storage` = Google Drive / QiNexus
- `/roadmap` = QiRoadmap
- `/blueprint` = QiBlueprint summary
- `/system` = system status/settings

## 04.02 No DNS Fight Rule

Do not waste time renaming domains before the app model is clear.

Keep the working URL. Refactor the mental model and app structure first.

---

# 05. Source of Truth Model

## 05.01 Repo Docs vs Wiki.js

**Repo docs define how the system is built.**

They hold app structure, architecture, folder doctrine, developer instructions, ADRs, runtime rules, blueprint, and roadmap.

**Wiki.js explains how the system is used.**

It holds readable manuals, workflows, household procedures, care processes, runbooks, and plain-English explanations.

## 05.02 Derived Systems Are Not Truth

AI summaries, vector search, graphs, exports, dashboards, and reports are helpful, but they are not canonical truth.

Canonical truth lives in app source code, repo docs, database records when used, Google Drive source files, and designated Wiki.js operating pages.

---

# 06. QiNexus / Google Drive Storage Model

## 06.01 Storage Doctrine

Google Drive is the storage backbone.

QiNexus is Cody’s adapted PARA model layered on top of it.

Projects and tasks are not separate root folders. Projects are major task containers; tasks are execution units inside them.

## 06.02 Canonical Root Order

1. `00_inbox`
2. `01_workbench`
3. `02_timeline`
4. `03_life`
5. `04_people`
6. `05_business`
7. `06_finance`
8. `07_legal`
9. `08_tech`
10. `09_assets`
11. `10_data`
12. `11_reference`
13. `12_archive`
14. `13_system`

## 06.03 Bucket Definitions

- **00_inbox** — temporary landing zone; nothing lives here permanently
- **01_workbench** — active work, projects, tasks, builds, drafts, and current documents
- **02_timeline** — journals, logs, event trails, daily/weekly notes, and chronology
- **03_life** — routines, home needs, planning, wellness structures, and personal operations
- **04_people** — family, support network, caregiving coordination, and relationship/context notes
- **05_business** — brand, revenue, client, and business materials; no longer the main driver
- **06_finance** — budgets, bills, reports, reconciliations, account notes, and planning
- **07_legal** — matters, filings, court records, evidence, timelines, and legal research
- **08_tech** — servers, apps, code notes, scripts, architecture, and deployments
- **09_assets** — reusable images, videos, audio, templates, branding, design, and media
- **10_data** — CSVs, sheets, exports, datasets, logs, and structured source material
- **11_reference** — articles, laws, examples, guides, research, citations, and external docs
- **12_archive** — inactive, historical, deprecated, completed, or frozen material
- **13_system** — rules, manifests, indexes, schemas, automation records, and structure docs

## 06.04 Storage Rules

Use shallow folders. Avoid overlapping siblings. Organize by function, not mood.

Keep active work in `01_workbench`, reusable assets in `09_assets`, structured exports in `10_data`, and completed work in `12_archive`.

Do not create new root folders casually.

---

# 07. App Folder Doctrine

## 07.01 Learning-Friendly Structure

Use a hybrid structure:

- standard React infrastructure folders stay unnumbered
- system feature modules are numbered for learning and navigation

## 07.02 Standard App Folders

- `src/app`
- `src/layouts`
- `src/pages`
- `src/components/ui`
- `src/lib`
- `src/styles`

Do not number these. They are technical infrastructure folders.

## 07.03 Numbered Feature Modules

- `src/features/00_dashboard`
- `src/features/01_start`
- `src/features/02_access`
- `src/features/03_qiserver`
- `src/features/04_knowledge_base`
- `src/features/05_storage`
- `src/features/06_roadmap`
- `src/features/07_blueprint`

## 07.04 Feature Meanings

- **00_dashboard** — home status, quick actions, priorities, and entry cards
- **01_start** — app tiles, service tiles, categories, favorites, and workflow entries
- **02_access** — protected links, exposure notes, admin warnings, and secure access
- **03_qiserver** — server tools, Docker services, status, internal URLs, and qiserver notes
- **04_knowledge_base** — Wiki.js links, documentation sections, and manual entry points
- **05_storage** — Google Drive / QiNexus buckets, rules, naming, and quick links
- **06_roadmap** — build phases, milestones, next actions, and status
- **07_blueprint** — app-readable summary of this blueprint and link to the full repo doc

## 07.05 Feature Folder Pattern

Each feature module should include:

- `components/`
- `data/`
- `README.md`

Each README explains what the module does, what page uses it, what data powers it, where to edit items, and how it connects to QiAccess Start.

## 07.06 Mental Model

Route → Page → Feature → Component → Data

Routes open pages. Pages compose screens. Features contain behavior. Components render pieces. Data files hold static config until a database is needed.

---

# 08. Repository Documentation Model

## 08.01 One Main Blueprint First

Keep the active doctrine in one practical main document:

`docs/00_blueprint/QiAccess_Start_Blueprint.md`

This keeps it easy to review, edit, and visualize with Markmap.

## 08.02 Supporting Docs Later

Split supporting docs only after the main blueprint stabilizes.

Recommended future docs:

- `docs/01_roadmap/QiRoadmap.md`
- `docs/02_architecture/System_Map.md`
- `docs/02_architecture/App_Flow.md`
- `docs/02_architecture/Service_Map.md`
- `docs/02_architecture/Runtime_Zones.md`
- `docs/03_storage/Google_Drive_Buckets.md`
- `docs/03_storage/QiNexus_Model.md`
- `docs/04_decisions/ADR-0001_QiAccess_Start_As_Operational_Front_Door.md`
- `docs/04_decisions/ADR-0002_Start_Access_Boundary.md`
- `docs/04_decisions/ADR-0003_WikiJS_As_Knowledge_Base.md`
- `docs/04_decisions/ADR-0004_Google_Drive_As_Storage_Backbone.md`
- `docs/04_decisions/ADR-0005_QiNexus_As_Personal_PARA_Model.md`
- `docs/05_operations/Qiserver_Runbook.md`
- `docs/05_operations/Access_And_Exposure_Rules.md`
- `docs/06_learning_notes/React_App_Flow.md`

## 08.03 Markmap Rule

Maintain clean heading hierarchy. Use headings for structure. Avoid bloated paragraphs under deep headings.

---

# 09. Runtime and Access Rules

## 09.01 qiserver Role

qiserver is the primary self-hosted runtime for Cody’s personal operating system.

It may host Wiki.js, dashboards, Portainer, Cockpit, Paperless, Open WebUI, Ollama, Neo4j, internal tools, and future app services.

## 09.02 Access Boundary

Admin services must not be casually exposed to the public internet.

Admin surfaces include SSH, Portainer, Cockpit, database tools, Docker socket access, system dashboards, and local AI runtimes.

## 09.03 Exposure Classes

- **Private Only** — Tailscale, LAN, or private network only; examples: SSH, Cockpit, Portainer, raw databases, and Ollama endpoints
- **Public Restricted** — internet reachable but protected by Cloudflare Access, app auth, or login; examples: access.qially.com and selected dashboards
- **Public Safe** — intentionally public and non-sensitive; examples: landing pages and published information pages

## 09.04 Safety Rule

If a service can control the server, access files, manage containers, expose secrets, or change infrastructure, it belongs behind private/protected access.

No exception without a decision record.

---

# 10. Wiki.js Knowledge Base Model

## 10.01 Decision

Wiki.js is the primary self-hosted readable knowledge base for Cody’s operating system.

It runs from qiserver.

## 10.02 Primary Sections

Recommended top-level sections:

- QiAccess Start
- Start
- Access
- QiServer
- Family OS
- Mom’s Care
- QiNexus
- Legal
- Finance
- Tech
- Personal Workflows
- Reference
- Runbooks

## 10.03 Repo-to-Wiki Rule

The repo stores engineering source. Wiki.js stores readable operating manuals.

A Wiki.js page should not silently override the repo blueprint. If a Wiki.js page changes doctrine, update the repo blueprint or create a decision record.

---

# 11. Roadmap

## Phase 0 — Stabilize Current Reality

Keep access.qially.com working, inventory links, document qiserver services, confirm Portainer/Cockpit/Wiki.js access, update the README, and add this blueprint.

## Phase 1 — Refactor Folder Structure

Create standard app folders, numbered feature modules, data files, module READMEs, and preserve working links.

## Phase 2 — Build QiAccess Start Home

Build the home dashboard, major system cards, quick actions, current workbench area, and links to Start, Access, QiServer, Wiki.js, and QiNexus.

## Phase 3 — Build Start

Build the launcher grid, categories, favorites, service metadata, internal/external badges, and app tile data.

## Phase 4 — Build Access

Build secure service cards, access badges, Tailscale/Cloudflare notes, private/public separation, and admin warnings.

## Phase 5 — Connect Wiki.js

Add Wiki.js to Start and the QiAccess Start home page, create a knowledge base section map, add a knowledge base page, and link repo docs where useful.

## Phase 6 — Add Storage / QiNexus Page

Show the root folder order, explain buckets, link Drive folders where possible, and add file placement rules.

## Phase 7 — Reuse Pattern for Mom’s Care

Apply Route → Page → Feature → Component → Data to Mom’s Care. Separate meds, supplies, vitals, care notes, reports, and schedules into feature folders.

Do not use Mom’s Care as the first learning/refactor target.

---

# 12. Legacy Blueprint Reconciliation

## 12.01 What the Old Blueprint Was

The older QiOS Master Blueprint was business/client/platform oriented.

It focused on clients, tenants, portals, CRM-like domains, business delivery, governed platform architecture, strict schema/domain separation, and future automation at scale.

That work is not useless. It is simply not the active center anymore.

## 12.02 What Gets Preserved

Preserve:

- one clear home per concern
- metadata before automation
- local-first where appropriate
- cloud-backed where useful
- human-readable naming with machine-stable identity
- derived systems are not truth
- repo docs as source of truth
- infrastructure exposure boundaries
- Markmap / visual structure thinking
- shallow folder design
- ADRs where needed

## 12.03 What Gets Demoted

Demote tenants, client portals, CRM-first architecture, multi-tenant RBAC, business delivery as the primary purpose, QiSuite/QiPortals as the core model, and strict platform governance beyond current need.

## 12.04 New Priority Order

1. Cody
2. Cody’s household/family
3. Mom’s care
4. legal and finance operations
5. knowledge base and files
6. tech/server systems
7. business only where it supports the above

---

# 13. Build Constraints

## 13.01 Keep It Static First

Do not add a database just because one could exist.

Static config files are enough for v1:

- `launcherApps.ts`
- `accessLinks.ts`
- `serverServices.ts`
- `storageBuckets.ts`
- `roadmapPhases.ts`
- `blueprintSections.ts`

## 13.02 No Auth Rebuild Yet

Use the existing access/protection path first. Revisit auth after structure is stable.

## 13.03 No Supabase Yet

Do not add Supabase to QiAccess Start v1 unless there is a specific reason.

The immediate job is clarity, not persistence.

## 13.04 Preserve Working Links

Do not break qiserver, Portainer, Cockpit, Wiki.js, existing services, or the current deployment path.

## 13.05 Clarity Over Cleverness

Prefer obvious names, readable components, simple data structures, and fewer abstractions.

---

# 14. Decision Records

## ADR-0001 — QiAccess Start as Operational Front Door

QiAccess Start is the main operational front door for Cody’s life and systems.

The app prioritizes start-page clarity, tool launching, protected access, family, care, legal, finance, storage, and server operations.

## ADR-0002 — Start / Access Boundary

Start opens tools.

Access manages protected/admin service entry.

They are sections of the same QiAccess Start app, not separate products.

## ADR-0003 — Wiki.js as Knowledge Base

Wiki.js is the primary readable knowledge base.

Repo docs remain engineering truth. Wiki.js becomes the operating library.

## ADR-0004 — Google Drive as Storage Backbone

Google Drive remains the cloud storage backbone because it is practical, accessible, and already useful.

QiNexus defines the organization model layered onto Drive.

## ADR-0005 — QiNexus as Personal PARA Model

QiNexus uses Cody’s adapted PARA model, not pure PARA.

Projects and tasks live under `01_workbench` instead of separate root folders.

---

# 15. Markmap View

## QiAccess Start Blueprint

### Purpose

- operational front door
- personal start page
- reduce friction
- centralize access
- clarify systems
- support family, care, finance, legal, tech, and knowledge work

### Core System

- QiAccess Start
- Start
- Access
- QiServer
- Wiki.js
- Repo Docs
- Google Drive
- QiNexus

### Runtime

- qiserver
- access.qially.com
- Portainer
- Cockpit
- Wiki.js
- Docker services
- local/private tools

### Storage

- inbox
- workbench
- timeline
- life
- people
- business
- finance
- legal
- tech
- assets
- data
- reference
- archive
- system

### App Structure

- app
- layouts
- pages
- components/ui
- lib
- styles
- numbered features

### Feature Modules

- 00_dashboard
- 01_start
- 02_access
- 03_qiserver
- 04_knowledge_base
- 05_storage
- 06_roadmap
- 07_blueprint

### Roadmap

- stabilize current reality
- refactor folder structure
- build QiAccess Start home
- build Start
- build Access
- connect Wiki.js
- add Storage / QiNexus page
- reuse pattern for Mom’s Care

### Legacy Shift

- old business blueprint becomes ancestor
- clients, tenants, and CRM are demoted
- family, personal operations, and care become the active center

---

# 16. Final Operating Rule

Do not build a cathedral for imaginary future clients while the real system needs a front door, a launcher, a library, a map, and a control panel.

QiAccess Start begins with Cody’s actual life.

Everything else earns its place after that.

