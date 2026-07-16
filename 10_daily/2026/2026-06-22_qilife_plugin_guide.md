---
layout: page
title: "QiLife Plugin Guide"
slug: "qilife_plugin_guide"
created_at: "2026-06-22 23:30:24"
updated_at: "2026-06-22 23:30:24"
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
date: 2026-06-22
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a3a0b9f-3ab0-83ea-aff6-e807b7280234"
canonical_ref: ""
---

# QiLife Plugin Guide

## Overview
- **Date**: 2026-06-22 23:30:24
- **Conversation ID**: `6a3a0b9f-3ab0-83ea-aff6-e807b7280234`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> how do we take this plugin as a guide in building my life management app qilife i like the layout and how the plugin works and i think we can use this as a guide and i mean its only four files this must be easier than what we are making it.

### Assistant
> I’m going to treat this plugin as a **working prototype pattern**, not something to blindly copy. The useful question is: what parts make QiLife simpler, and what parts would become a trap if we copy them too literally?

### Assistant
> Yes. **This plugin is a very good guide for QiLife.** But here’s the truth: it is not “easy” because it is four files. It is “easy” because the **pattern is simple**.
> 
> The plugin is basically:
> 
> | File | Job |
> |---|---|
> | `manifest.json` | declares the app/plugin identity |
> | `data.json` | stores settings, modules, layouts, custom entities, reminders |
> | `main.js` | app logic, navigation, entity registry, rendering, CRUD-ish behavior |
> | `styles.css` | visual system and layout |
> 
> That is the lesson.
> 
> Not “copy four files and we’re done.”  
> The lesson is: **QiLife needs a small shell + config-driven modules + generic entity screens.**
> 
> ## The big useful idea
> 
> Cadence works because it has a **single app shell** with internal navigation, not 50 scattered apps. Its own comment says it is a “single unified view with internal tab nav” and treats Markdown files as the source of truth. fileciteturn0file1
> 
> That maps beautifully to QiLife:
> 
> > **QiLife should be one life-command interface with modules inside it.**
> 
> Not separate random apps for care, finance, tasks, documents, people, projects, etc.
> 
> ## What we steal from Cadence
> 
> ### 1. The sidebar module model
> 
> Cadence has grouped navigation:
> 
> - Home
> - Planner
> - Projects
> - CRM
> - PRM
> - Workflow
> - Reports
> - Settings
> 
> For QiLife, we translate that into life domains:
> 
> ```txt
> Home
> Capture
> Today
> Life
> People
> Care
> Finance
> Legal
> Home / House
> Projects
> Documents
> Reports
> Settings
> ```
> 
> The QiAccess blueprint already says the goal is not to build more apps, but to create one coherent entry point where you can see what exists, know where to go, launch tools, access docs, and understand the system. fileciteturn2file0
> 
> That is the exact same pattern.
> 
> ### 2. The entity registry
> 
> This is the real gold.
> 
> Cadence defines entities like:
> 
> - contact
> - company
> - project
> - deal
> - activity
> - partner
> - transaction
> 
> Each entity has:
> 
> - folder
> - label
> - fields
> - columns
> - types
> - enum options
> - suggestion sources
> 
> Your `data.json` already shows this config-driven model with custom entities, module toggles, layouts, reminders, dashboards, and fields. fileciteturn0file0
> 
> For QiLife, we do the same thing:
> 
> ```ts
> entities = {
>   person,
>   task,
>   event,
>   care_note,
>   medication,
>   appointment,
>   document,
>   expense,
>   legal_matter,
>   home_item,
>   vehicle,
>   pet,
>   project
> }
> ```
> 
> Then we build **one generic table/card/detail renderer** that can display any entity.
> 
> That means we do **not** hand-build every screen from scratch. Thank God.
> 
> ### 3. Source-of-truth clarity
> 
> Cadence’s manifest literally describes it as a workspace with planner, reminders, projects, reports, CSV import, and “Markdown source-of-truth, no server required.” fileciteturn0file2
> 
> For QiLife, we adjust that:
> 
> ```txt
> QiLife source of truth:
> Supabase = structured truth
> QiNexus / Drive = file/blob truth
> Markdown/Wiki = readable operating manuals
> QiLife UI = command surface
> ```
> 
> So no, we should **not** make Markdown the main truth for everything if Supabase is already the long-term structured truth. But we can absolutely copy the **source-of-truth discipline**.
> 
> Cadence says: “I know where my data lives.”  
> QiLife must say the same.
> 
> ### 4. Config-driven pages
> 
> Cadence lets custom pages point to an entity key and default layout. Your `data.json` has a custom Transactions page using `entityKey: "reports_transaction"` and `defaultLayout: "table"`. fileciteturn0file0
> 
> That means QiLife can have pages like:
> 
> ```ts
> customPages = [
>   {
>     id: "finance.transactions",
>     label: "Transactions",
>     entityKey: "transaction",
>     defaultLayout: "table",
>     sectionId: "finance"
>   },
>   {
>     id: "care.medications",
>     label: "Medications",
>     entityKey: "medication",
>     defaultLayout: "table",
>     sectionId: "care"
>   },
>   {
>     id: "legal.matters",
>     label: "Legal Matters",
>     entityKey: "legal_matter",
>     defaultLayout: "cards",
>     sectionId: "legal"
>   }
> ]
> ```
> 
> That is how we stop overbuilding.
> 
> ## What we do **not** copy
> 
> Here is where I’m going to be blunt.
> 
> ### Do not build QiLife as a giant single `main.js`
> 
> Cadence can get away with that because it is an Obsidian plugin. But for your app, a massive single file will become chaos with a cute outfit on.
> 
> QiLife should copy the **pattern**, not the file structure.
> 
> The QiAccess blueprint already gives the better structure:
> 
> ```txt
> Route → Page → Feature → Component → Data
> ```
> 
> Routes open pages, pages compose screens, features contain behavior, components render pieces, and data files hold static config until a database is needed. fileciteturn2file0
> 
> That is the keeper.
> 
> ### Do not make every life thing a full app
> 
> Your ADHD trap here is wanting the perfect system before the first useful surface works.
> 
> Nope.
> 
> QiLife v1 should be:
> 
> ```txt
> One shell.
> One sidebar.
> One dashboard.
> One entity registry.
> One generic entity list.
> One generic detail page.
> One quick capture.
> ```
> 
> Then we add modules.
> 
> ## The QiLife version of the Cadence pattern
> 
> ### QiLife app shell
> 
> ```txt
> QiLife
> ├── Topbar
> │   ├── Current mode
> │   ├── Quick capture
> │   ├── Search
> │   └── Sync/status
> ├── Sidebar
> │   ├── Home
> │   ├── Capture
> │   ├── Today
> │   ├── Life
> │   ├── People
> │   ├── Care
> │   ├── Finance
> │   ├── Legal
> │   ├── Home
> │   ├── Projects
> │   ├── Documents
> │   ├── Reports
> │   └── Settings
> └── Content Surface
>     ├── Dashboard
>     ├── Entity table
>     ├── Entity cards
>     ├── Kanban
>     ├── Detail view
>     └── Reports
> ```
> 
> ### QiLife core entities
> 
> Start with this. Not 80 tables. Not a cathedral.
> 
> ```txt
> person
> task
> event
> note
> project
> document
> expense
> account
> care_note
> medication
> appointment
> legal_matter
> home_item
> asset
> reminder
> ```
> 
> Later:
> 
> ```txt
> vehicle
> pet
> provider
> case_event
> evidence_item
> income_source
> subscription
> routine
> meal
> inventory_item
> ```
> 
> But later. Do not let “later” bully v1.
> 
> ## Best architecture for QiLife
> 
> Cadence is local-first Markdown. QiLife should be **database-backed with a config-driven UI**.
> 
> ```txt
> QiLife UI
>   ↓
> Entity registry config
>   ↓
> Generic screens
>   ↓
> Supabase tables/views
>   ↓
> QiNexus files / Google Drive blobs
>   ↓
> Wiki.js readable docs
> ```
> 
> Your own blueprint already says canonical truth can live in app source code, repo docs, database records when used, Google Drive source files, and designated Wiki.js operating pages. fileciteturn2file0
> 
> That means the split should be:
> 
> | Layer | Truth type |
> |---|---|
> | Supabase | structured records |
> | QiNexus / Drive | files, receipts, documents, photos |
> | Wiki.js / QiSpark | manuals, explanations, doctrine |
> | QiLife app | operational UI |
> | AI/vector/graph | derived intelligence, not truth |
> 
> ## MVP build plan
> 
> ### Phase 1 — Clone the shell concept
> 
> Build:
> 
> ```txt
> QiLifeShell
> SidebarNav
> Topbar
> PageHeader
> DashboardCards
> EntityList
> EntityDetail
> QuickCaptureModal
> SettingsPage
> ```
> 
> No fancy AI yet. No Neo4j yet. No overcooked nonsense.
> 
> ### Phase 2 — Define the entity registry
> 
> Make one file:
> 
> ```txt
> src/features/qilife/data/entityRegistry.ts
> ```
> 
> Example:
> 
> ```ts
> export const entityRegistry = {
>   person: {
>     label: "Person",
>     plural: "People",
>     table: "qilife.people",
>     primaryField: "name",
>     defaultLayout: "table",
>     fields: [
>       { key: "name", label: "Name", type: "text", primary: true },
>       { key: "role", label: "Role", type: "text" },
>       { key: "phone", label: "Phone", type: "text" },
>       { key: "email", label: "Email", type: "text" },
>       { key: "tags", label: "Tags", type: "tags" }
>     ],
>     columns: ["name", "role", "phone", "email"]
>   }
> }
> ```
> 
> This is the Cadence entity model, but upgraded for Supabase.
> 
> ### Phase 3 — Build generic entity pages
> 
> Instead of hardcoding a People page, Finance page, Care page, etc., build:
> 
> ```txt
> /entities/:entityKey
> /entities/:entityKey/:id
> ```
> 
> Then the registry tells the UI what to render.
> 
> That is the leverage.
> 
> ### Phase 4 — Add domain dashboards
> 
> Once generic CRUD works, add smarter dashboards:
> 
> ```txt
> Home dashboard
> Care dashboard
> Finance dashboard
> Legal dashboard
> House dashboard
> Projects dashboard
> ```
> 
> These are **views over entities**, not separate systems.
> 
> ### Phase 5 — Add AI later
> 
> AI should not be the foundation. AI should sit on top:
> 
> ```txt
> summarize my week
> show overdue care issues
> find contradictions
> draft a message
> classify this receipt
> connect this document to a legal matter
> ```
> 
> If we add AI before the data shape is stable, we get a haunted Roomba with a login screen.
> 
> ## The decision
> 
> Use Cadence as the **UI and product architecture guide**.
> 
> Do **not** use it as the exact technical foundation.
> 
> The correct move:
> 
> ```txt
> Cadence pattern:
> single shell + sidebar + registry + generic views + quick capture
> 
> QiLife implementation:
> React/Next/Vite UI + Supabase structured truth + QiNexus file links + Wiki.js docs
> ```
> 
> ## The clean QiLife v1 target
> 
> ```txt
> QiLife v1 = personal command center
> 
> Must have:
> - Home dashboard
> - Today view
> - Quick capture
> - People
> - Tasks
> - Projects
> - Care notes
> - Appointments
> - Expenses
> - Documents
> - Legal matters
> - Settings
> - Generic table/card/detail layouts
> 
> Must not have yet:
> - giant graph brain
> - perfect automation
> - every possible life category
> - ten database abstractions
> - multi-user enterprise nonsense
> ```
> 
> The plugin proves the app does **not** need to be conceptually huge.
> 
> It needs a clean shell, a registry, and disciplined data. That’s the move.

### User
> ok, i gave the ide this now what should the code be

### Assistant
> We don’t need to jump to a full monster app. The next code should be a **thin QiLife shell** with a registry-driven entity system. That gives you the Cadence feel without recreating Cadence’s giant single-file situation.

### Assistant
> Yes. The next code should be the **QiLife Cadence-style shell**.
> 
> Do **not** tell the IDE to build the whole app. Tell it to build the **first working slice**:
> 
> > sidebar → home dashboard → generic entity registry → generic table/cards/detail → quick capture → Supabase-backed records
> 
> Cadence works because it has a unified app shell, internal nav, entity registry, settings/config, and generic renderers. fileciteturn0file1 Your QiAccess blueprint already says the goal is one coherent entry point, not more random apps. fileciteturn2file0
> 
> Paste this into the IDE.
> 
> ---
> 
> ## IDE prompt
> 
> ```txt
> Build the first QiLife app slice using the Cadence plugin pattern as inspiration, but do not copy Cadence directly.
> 
> Goal:
> Create a clean QiLife shell with sidebar navigation, topbar, home dashboard, quick capture, and a generic entity system powered by an entity registry.
> 
> Architecture:
> - React + TypeScript
> - Keep it modular, not one huge file.
> - Use a generic qiliife.records Supabase table for MVP.
> - Entity definitions live in a registry file.
> - Generic entity pages render from the registry.
> - The app must work for People, Tasks, Projects, Care Notes, Appointments, Expenses, Documents, Legal Matters, Home Items, and Reminders.
> - Do not overbuild AI, graph, automations, or advanced permissions yet.
> 
> Create or update these files:
> 
> src/features/qilife/types.ts
> src/features/qilife/data/entityRegistry.ts
> src/features/qilife/data/navRegistry.ts
> src/features/qilife/services/qilifeStore.ts
> src/features/qilife/components/QiLifeShell.tsx
> src/features/qilife/components/SidebarNav.tsx
> src/features/qilife/components/Topbar.tsx
> src/features/qilife/components/HomeDashboard.tsx
> src/features/qilife/components/EntityPage.tsx
> src/features/qilife/components/EntityTable.tsx
> src/features/qilife/components/EntityCards.tsx
> src/features/qilife/components/QuickCaptureModal.tsx
> src/features/qilife/styles/qilife.css
> src/lib/supabaseClient.ts
> 
> Also add this SQL migration:
> 
> supabase/migrations/0001_qilife_records.sql
> 
> Do not build fake business CRM features.
> This is for Cody’s life operating system: daily action, people, care, finance, legal, home, documents, projects, and reminders.
> ```
> 
> ---
> 
> # 1. Supabase migration
> 
> ```sql
> -- supabase/migrations/0001_qilife_records.sql
> 
> create schema if not exists qilife;
> 
> create extension if not exists pgcrypto;
> 
> create table if not exists qilife.records (
>   id uuid primary key default gen_random_uuid(),
> 
>   entity_key text not null,
>   title text not null,
> 
>   status text,
>   priority text,
>   due_date date,
> 
>   data jsonb not null default '{}'::jsonb,
> 
>   source text not null default 'qilife',
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now(),
>   archived_at timestamptz
> );
> 
> create index if not exists idx_qilife_records_entity_key
>   on qilife.records (entity_key);
> 
> create index if not exists idx_qilife_records_status
>   on qilife.records (status);
> 
> create index if not exists idx_qilife_records_due_date
>   on qilife.records (due_date);
> 
> create index if not exists idx_qilife_records_data_gin
>   on qilife.records using gin (data);
> 
> create or replace function qilife.set_updated_at()
> returns trigger as $$
> begin
>   new.updated_at = now();
>   return new;
> end;
> $$ language plpgsql;
> 
> drop trigger if exists trg_qilife_records_updated_at on qilife.records;
> 
> create trigger trg_qilife_records_updated_at
> before update on qilife.records
> for each row
> execute function qilife.set_updated_at();
> ```
> 
> ---
> 
> # 2. Types
> 
> ```ts
> // src/features/qilife/types.ts
> 
> export type QiFieldType =
>   | "text"
>   | "textarea"
>   | "number"
>   | "currency"
>   | "date"
>   | "datetime"
>   | "enum"
>   | "tags"
>   | "relation"
>   | "checkbox";
> 
> export type QiLayout = "table" | "cards" | "kanban";
> 
> export interface QiField {
>   key: string;
>   label: string;
>   type: QiFieldType;
>   primary?: boolean;
>   required?: boolean;
>   options?: string[];
>   relationEntity?: string;
>   locked?: boolean;
> }
> 
> export interface QiEntityDefinition {
>   key: string;
>   label: string;
>   plural: string;
>   icon?: string;
>   section: string;
>   defaultLayout: QiLayout;
>   titleField: string;
>   statusField?: string;
>   fields: QiField[];
>   columns: string[];
> }
> 
> export interface QiRecord {
>   id: string;
>   entity_key: string;
>   title: string;
>   status?: string | null;
>   priority?: string | null;
>   due_date?: string | null;
>   data: Record<string, unknown>;
>   source?: string;
>   created_at?: string;
>   updated_at?: string;
>   archived_at?: string | null;
> }
> 
> export interface QiCreateRecordInput {
>   entity_key: string;
>   title: string;
>   status?: string | null;
>   priority?: string | null;
>   due_date?: string | null;
>   data?: Record<string, unknown>;
> }
> ```
> 
> ---
> 
> # 3. Entity registry
> 
> ```ts
> // src/features/qilife/data/entityRegistry.ts
> 
> import type { QiEntityDefinition } from "../types";
> 
> export const entityRegistry: Record<string, QiEntityDefinition> = {
>   person: {
>     key: "person",
>     label: "Person",
>     plural: "People",
>     icon: "users",
>     section: "people",
>     defaultLayout: "table",
>     titleField: "name",
>     fields: [
>       { key: "name", label: "Name", type: "text", primary: true, required: true },
>       { key: "role", label: "Role", type: "text" },
>       { key: "phone", label: "Phone", type: "text" },
>       { key: "email", label: "Email", type: "text" },
>       { key: "relationship", label: "Relationship", type: "text" },
>       { key: "tags", label: "Tags", type: "tags" },
>       { key: "notes", label: "Notes", type: "textarea" }
>     ],
>     columns: ["name", "role", "phone", "email", "relationship"]
>   },
> 
>   task: {
>     key: "task",
>     label: "Task",
>     plural: "Tasks",
>     icon: "check-square",
>     section: "today",
>     defaultLayout: "table",
>     titleField: "title",
>     statusField: "status",
>     fields: [
>       { key: "title", label: "Title", type: "text", primary: true, required: true },
>       {
>         key: "status",
>         label: "Status",
>         type: "enum",
>         options: ["inbox", "next", "waiting", "done", "cancelled"]
>       },
>       {
>         key: "priority",
>         label: "Priority",
>         type: "enum",
>         options: ["low", "medium", "high", "urgent"]
>       },
>       { key: "due_date", label: "Due", type: "date" },
>       { key: "project", label: "Project", type: "relation", relationEntity: "project" },
>       { key: "notes", label: "Notes", type: "textarea" }
>     ],
>     columns: ["title", "status", "priority", "due_date", "project"]
>   },
> 
>   project: {
>     key: "project",
>     label: "Project",
>     plural: "Projects",
>     icon: "folder-kanban",
>     section: "projects",
>     defaultLayout: "cards",
>     titleField: "name",
>     statusField: "status",
>     fields: [
>       { key: "name", label: "Name", type: "text", primary: true, required: true },
>       {
>         key: "status",
>         label: "Status",
>         type: "enum",
>         options: ["active", "on_hold", "backlog", "done", "cancelled"]
>       },
>       {
>         key: "priority",
>         label: "Priority",
>         type: "enum",
>         options: ["low", "medium", "high"]
>       },
>       { key: "owner", label: "Owner", type: "relation", relationEntity: "person" },
>       { key: "due_date", label: "Due", type: "date" },
>       { key: "tags", label: "Tags", type: "tags" },
>       { key: "brief", label: "Brief", type: "textarea" }
>     ],
>     columns: ["name", "status", "priority", "owner", "due_date"]
>   },
> 
>   care_note: {
>     key: "care_note",
>     label: "Care Note",
>     plural: "Care Notes",
>     icon: "heart-pulse",
>     section: "care",
>     defaultLayout: "table",
>     titleField: "subject",
>     fields: [
>       { key: "subject", label: "Subject", type: "text", primary: true, required: true },
>       { key: "person", label: "Person", type: "relation", relationEntity: "person" },
>       {
>         key: "category",
>         label: "Category",
>         type: "enum",
>         options: ["symptom", "medication", "appointment", "incident", "supply", "general"]
>       },
>       { key: "when", label: "When", type: "datetime" },
>       { key: "notes", label: "Notes", type: "textarea" }
>     ],
>     columns: ["subject", "person", "category", "when"]
>   },
> 
>   appointment: {
>     key: "appointment",
>     label: "Appointment",
>     plural: "Appointments",
>     icon: "calendar",
>     section: "care",
>     defaultLayout: "table",
>     titleField: "title",
>     fields: [
>       { key: "title", label: "Title", type: "text", primary: true, required: true },
>       { key: "person", label: "Person", type: "relation", relationEntity: "person" },
>       { key: "provider", label: "Provider", type: "text" },
>       { key: "when", label: "When", type: "datetime" },
>       {
>         key: "status",
>         label: "Status",
>         type: "enum",
>         options: ["scheduled", "completed", "cancelled", "reschedule"]
>       },
>       { key: "notes", label: "Notes", type: "textarea" }
>     ],
>     columns: ["title", "person", "provider", "when", "status"]
>   },
> 
>   expense: {
>     key: "expense",
>     label: "Expense",
>     plural: "Expenses",
>     icon: "receipt",
>     section: "finance",
>     defaultLayout: "table",
>     titleField: "description",
>     fields: [
>       { key: "description", label: "Description", type: "text", primary: true, required: true },
>       { key: "amount", label: "Amount", type: "currency" },
>       { key: "account", label: "Account", type: "text" },
>       { key: "category", label: "Category", type: "text" },
>       { key: "date", label: "Date", type: "date" },
>       { key: "receipt_url", label: "Receipt", type: "text" },
>       { key: "notes", label: "Notes", type: "textarea" }
>     ],
>     columns: ["description", "amount", "account", "category", "date"]
>   },
> 
>   document: {
>     key: "document",
>     label: "Document",
>     plural: "Documents",
>     icon: "file-text",
>     section: "documents",
>     defaultLayout: "table",
>     titleField: "title",
>     fields: [
>       { key: "title", label: "Title", type: "text", primary: true, required: true },
>       {
>         key: "domain",
>         label: "Domain",
>         type: "enum",
>         options: ["life", "care", "finance", "legal", "home", "tech", "identity"]
>       },
>       { key: "file_url", label: "File URL", type: "text" },
>       { key: "related_person", label: "Related Person", type: "relation", relationEntity: "person" },
>       { key: "tags", label: "Tags", type: "tags" },
>       { key: "notes", label: "Notes", type: "textarea" }
>     ],
>     columns: ["title", "domain", "related_person", "file_url"]
>   },
> 
>   legal_matter: {
>     key: "legal_matter",
>     label: "Legal Matter",
>     plural: "Legal Matters",
>     icon: "scale",
>     section: "legal",
>     defaultLayout: "cards",
>     titleField: "title",
>     statusField: "status",
>     fields: [
>       { key: "title", label: "Title", type: "text", primary: true, required: true },
>       {
>         key: "status",
>         label: "Status",
>         type: "enum",
>         options: ["active", "waiting", "filed", "resolved", "closed"]
>       },
>       { key: "jurisdiction", label: "Jurisdiction", type: "text" },
>       { key: "deadline", label: "Deadline", type: "date" },
>       { key: "notes", label: "Notes", type: "textarea" }
>     ],
>     columns: ["title", "status", "jurisdiction", "deadline"]
>   },
> 
>   home_item: {
>     key: "home_item",
>     label: "Home Item",
>     plural: "Home Items",
>     icon: "home",
>     section: "home",
>     defaultLayout: "table",
>     titleField: "name",
>     fields: [
>       { key: "name", label: "Name", type: "text", primary: true, required: true },
>       {
>         key: "category",
>         label: "Category",
>         type: "enum",
>         options: ["safety", "repair", "supply", "furniture", "utility", "cleaning", "other"]
>       },
>       {
>         key: "status",
>         label: "Status",
>         type: "enum",
>         options: ["needed", "bought", "installed", "returned", "done"]
>       },
>       { key: "cost", label: "Cost", type: "currency" },
>       { key: "location", label: "Location", type: "text" },
>       { key: "notes", label: "Notes", type: "textarea" }
>     ],
>     columns: ["name", "category", "status", "cost", "location"]
>   },
> 
>   reminder: {
>     key: "reminder",
>     label: "Reminder",
>     plural: "Reminders",
>     icon: "bell",
>     section: "today",
>     defaultLayout: "table",
>     titleField: "text",
>     statusField: "status",
>     fields: [
>       { key: "text", label: "Text", type: "text", primary: true, required: true },
>       { key: "when", label: "When", type: "datetime" },
>       {
>         key: "status",
>         label: "Status",
>         type: "enum",
>         options: ["open", "done", "cancelled"]
>       },
>       { key: "notes", label: "Notes", type: "textarea" }
>     ],
>     columns: ["text", "when", "status"]
>   }
> };
> ```
> 
> ---
> 
> # 4. Navigation registry
> 
> ```ts
> // src/features/qilife/data/navRegistry.ts
> 
> export const navGroups = [
>   {
>     id: "home",
>     label: "",
>     items: [{ id: "home", label: "Home", entityKey: null }]
>   },
>   {
>     id: "today",
>     label: "Today",
>     items: [
>       { id: "task", label: "Tasks", entityKey: "task" },
>       { id: "reminder", label: "Reminders", entityKey: "reminder" }
>     ]
>   },
>   {
>     id: "life",
>     label: "Life",
>     items: [
>       { id: "person", label: "People", entityKey: "person" },
>       { id: "project", label: "Projects", entityKey: "project" },
>       { id: "document", label: "Documents", entityKey: "document" }
>     ]
>   },
>   {
>     id: "care",
>     label: "Care",
>     items: [
>       { id: "care_note", label: "Care Notes", entityKey: "care_note" },
>       { id: "appointment", label: "Appointments", entityKey: "appointment" }
>     ]
>   },
>   {
>     id: "operations",
>     label: "Operations",
>     items: [
>       { id: "expense", label: "Expenses", entityKey: "expense" },
>       { id: "legal_matter", label: "Legal Matters", entityKey: "legal_matter" },
>       { id: "home_item", label: "Home Items", entityKey: "home_item" }
>     ]
>   }
> ];
> ```
> 
> ---
> 
> # 5. Supabase client
> 
> ```ts
> // src/lib/supabaseClient.ts
> 
> import { createClient } from "@supabase/supabase-js";
> 
> const supabaseUrl = import.meta.env.VITE_SUPABASE_URL as string | undefined;
> const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY as string | undefined;
> 
> if (!supabaseUrl || !supabaseAnonKey) {
>   console.warn("Missing VITE_SUPABASE_URL or VITE_SUPABASE_ANON_KEY.");
> }
> 
> export const supabase = createClient(
>   supabaseUrl || "",
>   supabaseAnonKey || ""
> );
> ```
> 
> ---
> 
> # 6. QiLife store
> 
> ```ts
> // src/features/qilife/services/qilifeStore.ts
> 
> import { supabase } from "../../../lib/supabaseClient";
> import type { QiCreateRecordInput, QiRecord } from "../types";
> 
> export async function listRecords(entityKey: string): Promise<QiRecord[]> {
>   const { data, error } = await supabase
>     .schema("qilife")
>     .from("records")
>     .select("*")
>     .eq("entity_key", entityKey)
>     .is("archived_at", null)
>     .order("updated_at", { ascending: false });
> 
>   if (error) throw error;
>   return data || [];
> }
> 
> export async function createRecord(input: QiCreateRecordInput): Promise<QiRecord> {
>   const { data, error } = await supabase
>     .schema("qilife")
>     .from("records")
>     .insert({
>       entity_key: input.entity_key,
>       title: input.title,
>       status: input.status ?? null,
>       priority: input.priority ?? null,
>       due_date: input.due_date ?? null,
>       data: input.data ?? {}
>     })
>     .select("*")
>     .single();
> 
>   if (error) throw error;
>   return data;
> }
> 
> export async function updateRecord(
>   id: string,
>   patch: Partial<QiRecord>
> ): Promise<QiRecord> {
>   const { data, error } = await supabase
>     .schema("qilife")
>     .from("records")
>     .update(patch)
>     .eq("id", id)
>     .select("*")
>     .single();
> 
>   if (error) throw error;
>   return data;
> }
> 
> export async function archiveRecord(id: string): Promise<void> {
>   const { error } = await supabase
>     .schema("qilife")
>     .from("records")
>     .update({ archived_at: new Date().toISOString() })
>     .eq("id", id);
> 
>   if (error) throw error;
> }
> ```
> 
> ---
> 
> # 7. Shell
> 
> ```tsx
> // src/features/qilife/components/QiLifeShell.tsx
> 
> import { useState } from "react";
> import { entityRegistry } from "../data/entityRegistry";
> import { SidebarNav } from "./SidebarNav";
> import { Topbar } from "./Topbar";
> import { HomeDashboard } from "./HomeDashboard";
> import { EntityPage } from "./EntityPage";
> import { QuickCaptureModal } from "./QuickCaptureModal";
> import "../styles/qilife.css";
> 
> export function QiLifeShell() {
>   const [activeEntityKey, setActiveEntityKey] = useState<string | null>(null);
>   const [captureOpen, setCaptureOpen] = useState(false);
> 
>   const activeEntity = activeEntityKey ? entityRegistry[activeEntityKey] : null;
> 
>   return (
>     <div className="qilife-app">
>       <Topbar
>         activeLabel={activeEntity?.plural || "Home"}
>         onQuickCapture={() => setCaptureOpen(true)}
>       />
> 
>       <div className="qilife-body">
>         <SidebarNav
>           activeEntityKey={activeEntityKey}
>           onSelectEntity={setActiveEntityKey}
>           onHome={() => setActiveEntityKey(null)}
>         />
> 
>         <main className="qilife-content">
>           {activeEntity ? (
>             <EntityPage entity={activeEntity} />
>           ) : (
>             <HomeDashboard onOpenEntity={setActiveEntityKey} />
>           )}
>         </main>
>       </div>
> 
>       {captureOpen && (
>         <QuickCaptureModal onClose={() => setCaptureOpen(false)} />
>       )}
>     </div>
>   );
> }
> ```
> 
> ---
> 
> # 8. Sidebar
> 
> ```tsx
> // src/features/qilife/components/SidebarNav.tsx
> 
> import { navGroups } from "../data/navRegistry";
> 
> interface SidebarNavProps {
>   activeEntityKey: string | null;
>   onSelectEntity: (entityKey: string) => void;
>   onHome: () => void;
> }
> 
> export function SidebarNav({
>   activeEntityKey,
>   onSelectEntity,
>   onHome
> }: SidebarNavProps) {
>   return (
>     <aside className="qilife-sidebar">
>       <div className="qilife-brand" onClick={onHome}>
>         <div className="qilife-brand-mark">◐</div>
>         <div>
>           <div className="qilife-brand-title">QiLife</div>
>           <div className="qilife-brand-subtitle">Life Command</div>
>         </div>
>       </div>
> 
>       <nav className="qilife-nav">
>         {navGroups.map((group) => (
>           <section key={group.id} className="qilife-nav-group">
>             {group.label && (
>               <div className="qilife-nav-group-label">{group.label}</div>
>             )}
> 
>             {group.items.map((item) => {
>               const active =
>                 item.entityKey === activeEntityKey ||
>                 (!item.entityKey && !activeEntityKey);
> 
>               return (
>                 <button
>                   key={item.id}
>                   className={`qilife-nav-item ${active ? "active" : ""}`}
>                   onClick={() =>
>                     item.entityKey ? onSelectEntity(item.entityKey) : onHome()
>                   }
>                 >
>                   {item.label}
>                 </button>
>               );
>             })}
>           </section>
>         ))}
>       </nav>
>     </aside>
>   );
> }
> ```
> 
> ---
> 
> # 9. Topbar
> 
> ```tsx
> // src/features/qilife/components/Topbar.tsx
> 
> interface TopbarProps {
>   activeLabel: string;
>   onQuickCapture: () => void;
> }
> 
> export function Topbar({ activeLabel, onQuickCapture }: TopbarProps) {
>   return (
>     <header className="qilife-topbar">
>       <div>
>         <div className="qilife-eyebrow">QILIFE</div>
>         <h1>{activeLabel}</h1>
>       </div>
> 
>       <div className="qilife-topbar-actions">
>         <button className="qilife-btn" type="button">
>           Search
>         </button>
> 
>         <button
>           className="qilife-btn primary"
>           type="button"
>           onClick={onQuickCapture}
>         >
>           + Capture
>         </button>
>       </div>
>     </header>
>   );
> }
> ```
> 
> ---
> 
> # 10. Home dashboard
> 
> ```tsx
> // src/features/qilife/components/HomeDashboard.tsx
> 
> import { entityRegistry } from "../data/entityRegistry";
> 
> interface HomeDashboardProps {
>   onOpenEntity: (entityKey: string) => void;
> }
> 
> const dashboardCards = [
>   {
>     title: "Today",
>     description: "Tasks, reminders, and appointments that need attention.",
>     entityKey: "task"
>   },
>   {
>     title: "Care",
>     description: "Care notes, appointments, symptoms, supplies, and follow-up.",
>     entityKey: "care_note"
>   },
>   {
>     title: "Finance",
>     description: "Expenses, receipts, household costs, and money tracking.",
>     entityKey: "expense"
>   },
>   {
>     title: "Legal",
>     description: "Matters, deadlines, evidence, filings, and event trails.",
>     entityKey: "legal_matter"
>   },
>   {
>     title: "Documents",
>     description: "Drive/QiNexus linked documents and source files.",
>     entityKey: "document"
>   },
>   {
>     title: "Projects",
>     description: "Active builds, repairs, systems, and major life containers.",
>     entityKey: "project"
>   }
> ];
> 
> export function HomeDashboard({ onOpenEntity }: HomeDashboardProps) {
>   return (
>     <div className="qilife-page">
>       <section className="qilife-hero">
>         <div className="qilife-eyebrow">COMMAND CENTER</div>
>         <h2>What needs your attention?</h2>
>         <p>
>           This is the front door for daily action, care, finance, legal, files,
>           home, and projects.
>         </p>
>       </section>
> 
>       <section className="qilife-card-grid">
>         {dashboardCards.map((card) => {
>           const entity = entityRegistry[card.entityKey];
> 
>           return (
>             <button
>               key={card.entityKey}
>               className="qilife-card"
>               type="button"
>               onClick={() => onOpenEntity(card.entityKey)}
>             >
>               <div className="qilife-card-title">{card.title}</div>
>               <div className="qilife-card-desc">{card.description}</div>
>               <div className="qilife-card-meta">{entity?.plural}</div>
>             </button>
>           );
>         })}
>       </section>
>     </div>
>   );
> }
> ```
> 
> ---
> 
> # 11. Entity page
> 
> ```tsx
> // src/features/qilife/components/EntityPage.tsx
> 
> import { useEffect, useState } from "react";
> import type { QiEntityDefinition, QiRecord } from "../types";
> import { createRecord, listRecords } from "../services/qilifeStore";
> import { EntityTable } from "./EntityTable";
> import { EntityCards } from "./EntityCards";
> 
> interface EntityPageProps {
>   entity: QiEntityDefinition;
> }
> 
> export function EntityPage({ entity }: EntityPageProps) {
>   const [records, setRecords] = useState<QiRecord[]>([]);
>   const [layout, setLayout] = useState(entity.defaultLayout);
>   const [loading, setLoading] = useState(true);
>   const [error, setError] = useState<string | null>(null);
> 
>   async function load() {
>     try {
>       setLoading(true);
>       setError(null);
>       const rows = await listRecords(entity.key);
>       setRecords(rows);
>     } catch (err) {
>       setError(err instanceof Error ? err.message : "Failed to load records.");
>     } finally {
>       setLoading(false);
>     }
>   }
> 
>   async function handleCreate() {
>     const title = window.prompt(`New ${entity.label}`);
>     if (!title?.trim()) return;
> 
>     await createRecord({
>       entity_key: entity.key,
>       title: title.trim(),
>       status: entity.fields.find((f) => f.key === "status")?.options?.[0] ?? null,
>       data: {
>         [entity.titleField]: title.trim()
>       }
>     });
> 
>     await load();
>   }
> 
>   useEffect(() => {
>     load();
>   }, [entity.key]);
> 
>   return (
>     <div className="qilife-page">
>       <div className="qilife-page-header">
>         <div>
>           <div className="qilife-eyebrow">{entity.section}</div>
>           <h2>{entity.plural}</h2>
>           <p>{records.length} records</p>
>         </div>
> 
>         <div className="qilife-actions">
>           <button
>             className="qilife-btn"
>             type="button"
>             onClick={() => setLayout(layout === "table" ? "cards" : "table")}
>           >
>             {layout === "table" ? "Cards" : "Table"}
>           </button>
> 
>           <button
>             className="qilife-btn primary"
>             type="button"
>             onClick={handleCreate}
>           >
>             + New {entity.label}
>           </button>
>         </div>
>       </div>
> 
>       {loading && <div className="qilife-empty">Loading...</div>}
>       {error && <div className="qilife-error">{error}</div>}
> 
>       {!loading && !error && records.length === 0 && (
>         <div className="qilife-empty">
>           No {entity.plural.toLowerCase()} yet. Create the first one.
>         </div>
>       )}
> 
>       {!loading && !error && records.length > 0 && layout === "table" && (
>         <EntityTable entity={entity} records={records} onChanged={load} />
>       )}
> 
>       {!loading && !error && records.length > 0 && layout !== "table" && (
>         <EntityCards entity={entity} records={records} onChanged={load} />
>       )}
>     </div>
>   );
> }
> ```
> 
> ---
> 
> # 12. Entity table
> 
> ```tsx
> // src/features/qilife/components/EntityTable.tsx
> 
> import type { QiEntityDefinition, QiRecord } from "../types";
> import { archiveRecord } from "../services/qilifeStore";
> 
> interface EntityTableProps {
>   entity: QiEntityDefinition;
>   records: QiRecord[];
>   onChanged: () => void;
> }
> 
> function getValue(record: QiRecord, key: string): string {
>   if (key === "title") return record.title;
>   if (key === "status") return record.status || "";
>   if (key === "priority") return record.priority || "";
>   if (key === "due_date") return record.due_date || "";
> 
>   const value = record.data?.[key];
> 
>   if (Array.isArray(value)) return value.join(", ");
>   if (value === null || value === undefined) return "";
> 
>   return String(value);
> }
> 
> export function EntityTable({ entity, records, onChanged }: EntityTableProps) {
>   async function handleArchive(id: string) {
>     const ok = window.confirm("Archive this record?");
>     if (!ok) return;
> 
>     await archiveRecord(id);
>     onChanged();
>   }
> 
>   return (
>     <div className="qilife-table-wrap">
>       <table className="qilife-table">
>         <thead>
>           <tr>
>             {entity.columns.map((column) => (
>               <th key={column}>
>                 {entity.fields.find((field) => field.key === column)?.label ||
>                   column}
>               </th>
>             ))}
>             <th />
>           </tr>
>         </thead>
> 
>         <tbody>
>           {records.map((record) => (
>             <tr key={record.id}>
>               {entity.columns.map((column) => (
>                 <td key={column}>{getValue(record, column)}</td>
>               ))}
> 
>               <td className="qilife-row-actions">
>                 <button
>                   className="qilife-mini-btn"
>                   type="button"
>                   onClick={() => handleArchive(record.id)}
>                 >
>                   Archive
>                 </button>
>               </td>
>             </tr>
>           ))}
>         </tbody>
>       </table>
>     </div>
>   );
> }
> ```
> 
> ---
> 
> # 13. Entity cards
> 
> ```tsx
> // src/features/qilife/components/EntityCards.tsx
> 
> import type { QiEntityDefinition, QiRecord } from "../types";
> 
> interface EntityCardsProps {
>   entity: QiEntityDefinition;
>   records: QiRecord[];
>   onChanged: () => void;
> }
> 
> function getSubtitle(record: QiRecord, entity: QiEntityDefinition): string {
>   const parts = entity.columns
>     .filter((column) => column !== entity.titleField)
>     .slice(0, 3)
>     .map((column) => {
>       if (column === "status") return record.status;
>       if (column === "priority") return record.priority;
>       if (column === "due_date") return record.due_date;
>       return record.data?.[column];
>     })
>     .filter(Boolean)
>     .map(String);
> 
>   return parts.join(" · ");
> }
> 
> export function EntityCards({ entity, records }: EntityCardsProps) {
>   return (
>     <div className="qilife-card-grid">
>       {records.map((record) => (
>         <article key={record.id} className="qilife-card">
>           <div className="qilife-card-title">{record.title}</div>
>           <div className="qilife-card-desc">{getSubtitle(record, entity)}</div>
>           <div className="qilife-card-meta">{entity.label}</div>
>         </article>
>       ))}
>     </div>
>   );
> }
> ```
> 
> ---
> 
> # 14. Quick capture
> 
> ```tsx
> // src/features/qilife/components/QuickCaptureModal.tsx
> 
> import { useState } from "react";
> import { entityRegistry } from "../data/entityRegistry";
> import { createRecord } from "../services/qilifeStore";
> 
> interface QuickCaptureModalProps {
>   onClose: () => void;
> }
> 
> export function QuickCaptureModal({ onClose }: QuickCaptureModalProps) {
>   const [entityKey, setEntityKey] = useState("task");
>   const [text, setText] = useState("");
>   const [saving, setSaving] = useState(false);
> 
>   async function handleSave() {
>     const clean = text.trim();
>     if (!clean) return;
> 
>     const entity = entityRegistry[entityKey];
> 
>     setSaving(true);
> 
>     await createRecord({
>       entity_key: entityKey,
>       title: clean,
>       status: entity.fields.find((f) => f.key === "status")?.options?.[0] ?? null,
>       data: {
>         [entity.titleField]: clean,
>         captured_at: new Date().toISOString()
>       }
>     });
> 
>     setSaving(false);
>     onClose();
>   }
> 
>   return (
>     <div className="qilife-modal-backdrop">
>       <div className="qilife-modal">
>         <div className="qilife-modal-header">
>           <h2>Quick Capture</h2>
>           <button className="qilife-mini-btn" type="button" onClick={onClose}>
>             Close
>           </button>
>         </div>
> 
>         <label className="qilife-label">
>           Capture as
>           <select
>             value={entityKey}
>             onChange={(event) => setEntityKey(event.target.value)}
>           >
>             {Object.values(entityRegistry).map((entity) => (
>               <option key={entity.key} value={entity.key}>
>                 {entity.label}
>               </option>
>             ))}
>           </select>
>         </label>
> 
>         <label className="qilife-label">
>           What is it?
>           <textarea
>             value={text}
>             onChange={(event) => setText(event.target.value)}
>             placeholder="Dump the thought here. We will organize it later."
>             rows={5}
>           />
>         </label>
> 
>         <div className="qilife-actions end">
>           <button className="qilife-btn" type="button" onClick={onClose}>
>             Cancel
>           </button>
> 
>           <button
>             className="qilife-btn primary"
>             type="button"
>             onClick={handleSave}
>             disabled={saving}
>           >
>             {saving ? "Saving..." : "Capture"}
>           </button>
>         </div>
>       </div>
>     </div>
>   );
> }
> ```
> 
> ---
> 
> # 15. CSS
> 
> ```css
> /* src/features/qilife/styles/qilife.css */
> 
> .qilife-app {
>   height: 100vh;
>   display: flex;
>   flex-direction: column;
>   background: #101312;
>   color: #f1f5f2;
>   font-family:
>     Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI",
>     sans-serif;
> }
> 
> .qilife-topbar {
>   height: 72px;
>   border-bottom: 1px solid rgba(255, 255, 255, 0.08);
>   display: flex;
>   align-items: center;
>   justify-content: space-between;
>   padding: 0 24px;
>   background: #0b0e0d;
> }
> 
> .qilife-topbar h1,
> .qilife-page h2 {
>   margin: 0;
>   font-size: 24px;
>   letter-spacing: -0.04em;
> }
> 
> .qilife-eyebrow {
>   font-size: 11px;
>   text-transform: uppercase;
>   letter-spacing: 0.14em;
>   color: #89b99b;
>   font-weight: 700;
> }
> 
> .qilife-body {
>   flex: 1;
>   min-height: 0;
>   display: flex;
> }
> 
> .qilife-sidebar {
>   width: 240px;
>   flex-shrink: 0;
>   background: #0b0e0d;
>   border-right: 1px solid rgba(255, 255, 255, 0.08);
>   padding: 16px 12px;
>   overflow-y: auto;
> }
> 
> .qilife-brand {
>   display: flex;
>   align-items: center;
>   gap: 10px;
>   padding: 10px;
>   margin-bottom: 16px;
>   cursor: pointer;
> }
> 
> .qilife-brand-mark {
>   width: 34px;
>   height: 34px;
>   border-radius: 10px;
>   background: #1f3a2c;
>   color: #b4e6c5;
>   display: grid;
>   place-items: center;
> }
> 
> .qilife-brand-title {
>   font-size: 15px;
>   font-weight: 800;
> }
> 
> .qilife-brand-subtitle {
>   font-size: 11px;
>   color: #7d8a82;
> }
> 
> .qilife-nav-group {
>   margin-bottom: 18px;
> }
> 
> .qilife-nav-group-label {
>   padding: 8px 10px;
>   font-size: 10px;
>   font-weight: 800;
>   color: #68736c;
>   letter-spacing: 0.14em;
>   text-transform: uppercase;
> }
> 
> .qilife-nav-item {
>   width: 100%;
>   border: 0;
>   background: transparent;
>   color: #cbd5ce;
>   text-align: left;
>   padding: 9px 12px;
>   border-radius: 8px;
>   cursor: pointer;
>   font-size: 14px;
> }
> 
> .qilife-nav-item:hover {
>   background: rgba(255, 255, 255, 0.06);
> }
> 
> .qilife-nav-item.active {
>   background: #1f3a2c;
>   color: #b4e6c5;
> }
> 
> .qilife-content {
>   flex: 1;
>   min-width: 0;
>   overflow-y: auto;
> }
> 
> .qilife-page {
>   padding: 24px;
> }
> 
> .qilife-hero {
>   border: 1px solid rgba(255, 255, 255, 0.08);
>   background: linear-gradient(135deg, #142019, #0f1311);
>   border-radius: 18px;
>   padding: 28px;
>   margin-bottom: 20px;
> }
> 
> .qilife-hero p,
> .qilife-page-header p {
>   color: #96a39b;
>   margin: 6px 0 0;
> }
> 
> .qilife-page-header {
>   display: flex;
>   align-items: flex-end;
>   justify-content: space-between;
>   margin-bottom: 20px;
> }
> 
> .qilife-actions,
> .qilife-topbar-actions {
>   display: flex;
>   align-items: center;
>   gap: 8px;
> }
> 
> .qilife-actions.end {
>   justify-content: flex-end;
> }
> 
> .qilife-btn,
> .qilife-mini-btn {
>   border: 1px solid rgba(255, 255, 255, 0.12);
>   background: #171d1a;
>   color: #f1f5f2;
>   border-radius: 9px;
>   padding: 9px 14px;
>   cursor: pointer;
>   font-weight: 650;
> }
> 
> .qilife-mini-btn {
>   padding: 6px 10px;
>   font-size: 12px;
> }
> 
> .qilife-btn.primary {
>   background: #b4e6c5;
>   color: #07100b;
>   border-color: #b4e6c5;
> }
> 
> .qilife-btn:disabled {
>   opacity: 0.6;
>   cursor: not-allowed;
> }
> 
> .qilife-card-grid {
>   display: grid;
>   grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
>   gap: 14px;
> }
> 
> .qilife-card {
>   text-align: left;
>   border: 1px solid rgba(255, 255, 255, 0.09);
>   background: #151a18;
>   color: inherit;
>   border-radius: 16px;
>   padding: 18px;
>   cursor: pointer;
> }
> 
> .qilife-card:hover {
>   border-color: #89b99b;
> }
> 
> .qilife-card-title {
>   font-size: 16px;
>   font-weight: 800;
>   margin-bottom: 6px;
> }
> 
> .qilife-card-desc {
>   font-size: 13px;
>   color: #a7b4ac;
>   line-height: 1.45;
> }
> 
> .qilife-card-meta {
>   margin-top: 14px;
>   font-size: 11px;
>   color: #89b99b;
>   text-transform: uppercase;
>   letter-spacing: 0.1em;
>   font-weight: 800;
> }
> 
> .qilife-table-wrap {
>   border: 1px solid rgba(255, 255, 255, 0.09);
>   border-radius: 14px;
>   overflow: hidden;
>   background: #151a18;
> }
> 
> .qilife-table {
>   width: 100%;
>   border-collapse: collapse;
> }
> 
> .qilife-table th {
>   text-align: left;
>   font-size: 11px;
>   text-transform: uppercase;
>   letter-spacing: 0.12em;
>   color: #7d8a82;
>   padding: 12px;
>   background: #0f1311;
> }
> 
> .qilife-table td {
>   padding: 12px;
>   border-top: 1px solid rgba(255, 255, 255, 0.07);
>   color: #e4ebe6;
> }
> 
> .qilife-row-actions {
>   text-align: right;
> }
> 
> .qilife-empty,
> .qilife-error {
>   padding: 28px;
>   border: 1px dashed rgba(255, 255, 255, 0.14);
>   border-radius: 14px;
>   color: #a7b4ac;
> }
> 
> .qilife-error {
>   color: #ffb4a8;
>   border-color: rgba(255, 180, 168, 0.3);
> }
> 
> .qilife-modal-backdrop {
>   position: fixed;
>   inset: 0;
>   background: rgba(0, 0, 0, 0.64);
>   display: grid;
>   place-items: center;
>   padding: 20px;
> }
> 
> .qilife-modal {
>   width: min(560px, 100%);
>   background: #111613;
>   border: 1px solid rgba(255, 255, 255, 0.12);
>   border-radius: 18px;
>   padding: 20px;
>   box-shadow: 0 30px 80px rgba(0, 0, 0, 0.4);
> }
> 
> .qilife-modal-header {
>   display: flex;
>   justify-content: space-between;
>   align-items: center;
>   margin-bottom: 16px;
> }
> 
> .qilife-modal-header h2 {
>   margin: 0;
> }
> 
> .qilife-label {
>   display: flex;
>   flex-direction: column;
>   gap: 8px;
>   margin-bottom: 14px;
>   font-size: 13px;
>   color: #a7b4ac;
>   font-weight: 700;
> }
> 
> .qilife-label input,
> .qilife-label textarea,
> .qilife-label select {
>   width: 100%;
>   border-radius: 10px;
>   border: 1px solid rgba(255, 255, 255, 0.12);
>   background: #0b0e0d;
>   color: #f1f5f2;
>   padding: 10px;
>   font: inherit;
> }
> ```
> 
> ---
> 
> # 16. Wire it into the app
> 
> Wherever your main app renders, mount:
> 
> ```tsx
> import { QiLifeShell } from "./features/qilife/components/QiLifeShell";
> 
> export default function App() {
>   return <QiLifeShell />;
> }
> ```
> 
> ---
> 
> ## Important: do this in order
> 
> 1. Add the SQL migration.
> 2. Run the migration.
> 3. Add the React files.
> 4. Add `.env` values:
> 
> ```env
> VITE_SUPABASE_URL=your_supabase_project_url
> VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
> ```
> 
> 5. Start the app.
> 6. Test quick capture.
> 7. Test creating a Person, Task, Expense, and Care Note.
> 
> This is the right first version. Not glamorous, not bloated, not fake-smart. It gives you the exact leverage you liked in Cadence: **one shell, many life surfaces, one registry, one generic record engine.**

### User
> go ahead and build the app for me to download please.

### Assistant
> I’ll package this as a runnable **Vite + React + TypeScript QiLife MVP**, not just loose snippets. I’m also going to make it usable even before Supabase is configured by adding a localStorage fallback—otherwise you’d download a pretty brick.

### Assistant
> I’ve got the project scaffolded with the Supabase migration and a fallback store. Next I’m wiring the actual UI components: shell, navigation, dashboard, generic entity pages, create/edit modal, and styling.

### Assistant
> Done. I built the downloadable QiLife MVP app package.
> 
> **Download:** [qilife-app.zip](sandbox:/mnt/data/qilife-app.zip)
> 
> Included:
> 
> - Vite + React + TypeScript app
> - QiLife shell/sidebar/topbar
> - Home dashboard
> - Quick Capture modal
> - Generic registry-driven entities
> - People, Tasks, Projects, Care Notes, Appointments, Expenses, Documents, Legal Matters, Home Items, Reminders
> - Create/edit/archive records
> - Supabase migration: `qilife.records`
> - localStorage fallback so it runs immediately without Supabase
> - README + architecture note
> - Production `dist/` build included
> 
> I also ran the build successfully. No TypeScript/build errors.

### User
> whay do we need a workers for the app to talk to the database?

### Assistant
> You **do not need a Worker** just for the QiLife app to talk to Supabase.
> 
> For the MVP I built, the clean path is:
> 
> ```txt
> QiLife React app
>   ↓ supabase-js with anon key
> Supabase API
>   ↓ Row Level Security
> qilife.records table
> ```
> 
> That is enough.
> 
> ## When you **do not** need a Worker
> 
> You do **not** need a Cloudflare Worker / backend API if:
> 
> - the app uses Supabase
> - you only use the public `anon` key
> - your tables have proper Row Level Security
> - the user is logged in through Supabase Auth, or you are still in local/dev mode
> - the app is doing normal CRUD: create, read, update, archive records
> 
> For QiLife v1, this is fine.
> 
> ## When you **do** need a Worker/backend
> 
> You need a Worker or backend when something requires **secrets, privilege, or protected server-side logic**.
> 
> Examples:
> 
> | Need | Worker/backend? | Why |
> |---|---:|---|
> | Reading/writing normal QiLife records through Supabase | No | Supabase client handles this |
> | Using `service_role` key | Yes | Never expose that in the browser |
> | Direct PostgreSQL connection | Yes | Browsers should not connect directly to Postgres |
> | Calling OpenAI/Gemini APIs | Yes | API keys must stay private |
> | Google Drive/Gmail/Calendar sync | Usually yes | OAuth tokens and refresh logic need protection |
> | File ingestion/classification jobs | Yes | Long-running/background work |
> | Webhooks | Yes | External services need an endpoint |
> | Admin actions bypassing RLS | Yes | Browser should not have god powers |
> | Scheduled automations | Yes | Browser is not always open |
> 
> ## The blunt answer
> 
> If the IDE is trying to add a Worker **just to talk to Supabase**, it is overengineering.
> 
> For this stage:
> 
> ```txt
> No Worker.
> No backend.
> No Cloudflare functions.
> No fake architecture flex.
> ```
> 
> Use:
> 
> ```txt
> React app → Supabase client → RLS-protected tables
> ```
> 
> Later, add Workers only for:
> 
> ```txt
> AI actions
> Google integrations
> file ingestion
> secure admin operations
> scheduled jobs
> webhooks
> private service calls
> ```
> 
> ## Correct QiLife architecture for now
> 
> ```txt
> QiLife UI
>   ↓
> Supabase anon client
>   ↓
> Supabase RLS
>   ↓
> qilife.records
> ```
> 
> Future:
> 
> ```txt
> QiLife UI
>   ↓
> Supabase
>   ↓
> Worker/API layer for privileged operations only
>   ↓
> AI / Google / Drive / background sync / admin tasks
> ```
> 
> So no, you’re not crazy. The Worker is not required for basic app/database communication. It becomes useful later when QiLife needs to act like an actual assistant, not just a CRUD dashboard.

### User
> ok so do i need to add auth or is cloudflare zero trust enough?

### Assistant
> This is one of those places where the wrong choice creates a security mess later. I’m checking the current Supabase/Cloudflare model, then I’ll give you the practical answer—not the enterprise cosplay answer.

### Assistant
> ## Blunt answer
> 
> **Cloudflare Zero Trust is enough to protect the app URL.**  
> It is **not enough to safely protect the Supabase database** if the browser talks directly to Supabase.
> 
> So for QiLife:
> 
> ```txt
> Use BOTH:
> Cloudflare Zero Trust = front-door gate
> Supabase Auth + RLS = database security
> ```
> 
> That is the sane setup.
> 
> ## Why Cloudflare alone is not enough
> 
> Cloudflare Access sits in front of your web app and checks whether someone is allowed to reach the app. Cloudflare describes it as an identity-aware proxy that checks requests against Access policies before allowing them through. citeturn781745search13
> 
> But your React app, once loaded, talks to Supabase directly:
> 
> ```txt
> Browser
>   → Supabase API
>   → qilife.records
> ```
> 
> Cloudflare is **not automatically protecting the Supabase API**. Supabase is its own public API endpoint. Supabase says frontend apps can access data safely from the browser only when Row Level Security is enabled and properly configured. citeturn781745search15
> 
> That means if you expose the Supabase anon/publishable key in the app and your RLS policy is loose, someone could hit Supabase directly even if they cannot open `access.qially.com`.
> 
> ## The correct mental model
> 
> | Layer | What it protects | Enough by itself? |
> |---|---|---:|
> | Cloudflare Zero Trust | The web app doorway | No |
> | Supabase Auth | Who the database thinks you are | No |
> | Supabase RLS | What records that user can access | No |
> | All together | App + data + future sharing | Yes |
> 
> ## Best move for QiLife
> 
> ### For v1 personal use
> 
> Use:
> 
> ```txt
> Cloudflare Zero Trust
> + Supabase Auth
> + RLS policies
> ```
> 
> Keep Supabase Auth simple:
> 
> ```txt
> Google login or magic link
> ```
> 
> No custom auth system. No Worker. No nonsense.
> 
> Supabase Auth issues JWTs, and Supabase uses JWTs for authentication/authorization. citeturn781745search3 Then RLS can enforce “Cody can only access Cody’s records.”
> 
> ## What I would change in the database
> 
> Your current MVP table should get an `owner_id`.
> 
> ```sql
> alter table qilife.records
> add column if not exists owner_id uuid references auth.users(id);
> 
> alter table qilife.records enable row level security;
> 
> drop policy if exists "Users can read own qilife records" on qilife.records;
> drop policy if exists "Users can insert own qilife records" on qilife.records;
> drop policy if exists "Users can update own qilife records" on qilife.records;
> drop policy if exists "Users can delete own qilife records" on qilife.records;
> 
> create policy "Users can read own qilife records"
> on qilife.records
> for select
> to authenticated
> using (owner_id = auth.uid());
> 
> create policy "Users can insert own qilife records"
> on qilife.records
> for insert
> to authenticated
> with check (owner_id = auth.uid());
> 
> create policy "Users can update own qilife records"
> on qilife.records
> for update
> to authenticated
> using (owner_id = auth.uid())
> with check (owner_id = auth.uid());
> 
> create policy "Users can delete own qilife records"
> on qilife.records
> for delete
> to authenticated
> using (owner_id = auth.uid());
> ```
> 
> Then the app inserts records like:
> 
> ```ts
> {
>   owner_id: user.id,
>   entity_key: "task",
>   title: "Call pharmacy",
>   data: {}
> }
> ```
> 
> ## When Cloudflare alone *would* be enough
> 
> Cloudflare Zero Trust alone is enough only if:
> 
> ```txt
> Browser → Your protected backend/API → Supabase
> ```
> 
> Meaning the browser never talks directly to Supabase, and your backend/Worker verifies the Cloudflare identity before touching the database.
> 
> But you just asked whether you need a Worker, and for this MVP we already said no. So if there is **no Worker/backend**, then yes: **add Supabase Auth.**
> 
> ## Decision
> 
> For QiLife:
> 
> ```txt
> Cloudflare Zero Trust = keep strangers away from the app.
> Supabase Auth = identify Cody inside the app.
> Supabase RLS = protect Cody’s records.
> ```
> 
> That is the clean answer.
> 
> Do not rely on Cloudflare alone unless you move all database writes behind a backend. That would be more complex than adding Supabase Auth, so don’t do that yet.

### User
> what do i tell the ide or should we have codex finish u p the app?

### Assistant
> Yes — **have Codex finish the app**.
> 
> The IDE chat is fine for ideas, but this is now repo-level work: migrations, auth, RLS, wiring, testing, build errors. Codex is better for that.
> 
> Give Codex this:
> 
> ```txt id="codex-qilife-auth-finish"
> You are finishing the QiLife MVP app.
> 
> Context:
> QiLife is a React + TypeScript + Vite personal life-management app inspired by the Cadence Obsidian plugin pattern: one app shell, sidebar navigation, quick capture, and registry-driven generic entity pages.
> 
> Current app includes:
> - QiLifeShell
> - SidebarNav
> - Topbar
> - HomeDashboard
> - EntityPage
> - EntityTable
> - EntityCards
> - QuickCaptureModal
> - entityRegistry
> - navRegistry
> - qilifeStore
> - Supabase migration for qilife.records
> - localStorage fallback
> 
> Important architecture decision:
> Do NOT add Cloudflare Workers.
> Do NOT add a backend API.
> Do NOT use the Supabase service_role key.
> The browser app should talk directly to Supabase using the anon/publishable key.
> Security should be:
> Cloudflare Zero Trust protects the app URL.
> Supabase Auth identifies the user inside the app.
> Supabase Row Level Security protects the data.
> 
> Your job:
> Finish the app so it is usable and safe for a personal MVP.
> 
> Tasks:
> 
> 1. Add Supabase Auth support.
>    - Create src/features/qilife/auth/AuthProvider.tsx
>    - Create src/features/qilife/auth/LoginPage.tsx
>    - Create src/features/qilife/auth/useAuth.ts
>    - Support email magic link login at minimum.
>    - If Google OAuth is easy and already supported by env/config, add it as optional.
>    - Add sign out in the topbar.
> 
> 2. Protect QiLifeShell.
>    - If Supabase env vars are present, require login before showing the app.
>    - If Supabase env vars are missing, allow localStorage fallback mode and clearly show "Local Mode" in the UI.
>    - Do not break local development.
> 
> 3. Update Supabase migration.
>    - Add owner_id uuid references auth.users(id)
>    - Enable RLS on qilife.records
>    - Add policies:
>      - authenticated users can select their own records
>      - authenticated users can insert their own records
>      - authenticated users can update their own records
>      - authenticated users can archive/delete their own records
>    - Ensure owner_id = auth.uid()
> 
> 4. Update qilifeStore.
>    - When Supabase is configured and user is logged in, include owner_id on insert.
>    - All list/create/update/archive operations should work with authenticated Supabase.
>    - Keep localStorage fallback working.
>    - Do not store records globally in localStorage if possible; namespace by local mode.
> 
> 5. Improve record creation.
>    - Replace window.prompt with a proper modal form.
>    - Reuse entityRegistry fields to render inputs.
>    - Required primary field must be enforced.
>    - Save normal fields inside data jsonb.
>    - Map common top-level fields:
>      - status to records.status
>      - priority to records.priority
>      - due_date to records.due_date
> 
> 6. Add basic edit support.
>    - Clicking a table row or card should open an edit modal.
>    - User can edit fields and save.
>    - User can archive from edit modal.
> 
> 7. Improve UX.
>    - Show active mode clearly.
>    - Show loading and error states.
>    - Show empty states.
>    - Add a small status pill:
>      - "Supabase Connected"
>      - "Local Mode"
>      - "Signed in as {email}"
> 
> 8. Keep code clean.
>    - No giant single-file app.
>    - Keep files modular.
>    - Use TypeScript types.
>    - Avoid overengineering.
>    - Do not add graph, AI, automations, file ingestion, or Workers yet.
> 
> 9. Test.
>    - Run npm install if needed.
>    - Run npm run build.
>    - Fix all TypeScript/build errors.
>    - Report exactly what changed and any remaining setup steps.
> 
> Expected result:
> A working QiLife MVP where Cody can:
> - log in through Supabase Auth
> - create/edit/archive records
> - use local fallback if Supabase is not configured
> - safely store personal records with owner-scoped RLS
> - navigate People, Tasks, Projects, Care Notes, Appointments, Expenses, Documents, Legal Matters, Home Items, and Reminders
> ```
> 
> ## My call
> 
> Use **Codex** for this part.
> 
> The IDE can design. Codex should finish the wiring because it can actually chase the errors across files.
> 
> ## Don’t let it wander
> 
> Tell Codex this too if it starts getting cute:
> 
> ```txt id="codex-boundary"
> Stop. Do not add new architecture. Finish the MVP only:
> Auth, RLS, owner_id, CRUD modals, build pass.
> No Workers. No AI. No graph. No multi-user sharing. No dashboard analytics yet.
> ```
> 
> ## After Codex finishes, your checklist is simple
> 
> ```txt id="finish-checklist"
> 1. Supabase migration runs.
> 2. App builds.
> 3. App opens in local mode without env vars.
> 4. App requires login when Supabase env vars exist.
> 5. Create a task.
> 6. Refresh page.
> 7. Task persists.
> 8. Sign out.
> 9. Data is not visible when signed out.
> 10. RLS policies exist in Supabase.
> ```
> 
> That’s the move. Codex finishes this slice. Then we package it again and deploy it behind Cloudflare Zero Trust.

### User
> do we need to update this?

### Assistant
> Yes. **Update it.** The old prompt is good, but now it needs one important correction:
> 
> > **Do not edit the original migration if it may already have run. Create a new `0002` auth/RLS migration instead.**
> 
> Otherwise Codex might rewrite history and make your database migration chain messy. Tiny thing, big consequences. Classic little gremlin.
> 
> Use this updated version:
> 
> :::writing{variant="standard" id="73842"}
> You are finishing the existing QiLife MVP app.
> 
> Important:
> Do NOT create a new app from scratch.
> Modify the existing repo/app files only.
> Keep the current Cadence-inspired architecture: one shell, sidebar navigation, quick capture, and registry-driven generic entity pages.
> 
> Current architecture:
> - React + TypeScript + Vite
> - Supabase optional
> - localStorage fallback mode
> - Generic qilife.records table
> - Entity registry for People, Tasks, Projects, Care Notes, Appointments, Expenses, Documents, Legal Matters, Home Items, and Reminders
> 
> Security decision:
> Do NOT add Cloudflare Workers.
> Do NOT add a backend API.
> Do NOT use or expose the Supabase service_role key.
> The browser app should talk directly to Supabase using the anon/publishable key.
> 
> Security model:
> - Cloudflare Zero Trust protects the app URL.
> - Supabase Auth identifies the user inside the app.
> - Supabase Row Level Security protects database records.
> - RLS is required for Supabase mode.
> 
> Tasks:
> 
> 1. Add Supabase Auth support.
>    - Add AuthProvider, LoginPage, and useAuth hook.
>    - Support email magic link login.
>    - Add optional Google OAuth only if easy and clean.
>    - Add sign out button/status in the topbar.
>    - Show signed-in email when available.
> 
> 2. Protect the app.
>    - If Supabase env vars are present, require login before showing QiLife.
>    - If Supabase env vars are missing, allow localStorage fallback mode.
>    - In fallback mode, clearly show a "Local Mode" status pill.
>    - Do not break local development.
> 
> 3. Add a new migration.
>    - Do not rewrite an already-run migration unless it has definitely not been applied.
>    - Prefer creating:
>      supabase/migrations/0002_qilife_auth_rls.sql
> 
>    Migration must:
>    - Add owner_id uuid references auth.users(id) to qilife.records if missing.
>    - Enable row level security on qilife.records.
>    - Add RLS policies so authenticated users can select, insert, update, and archive/delete only their own records.
>    - Ensure owner_id equals auth.uid().
>    - If possible, make owner_id default to auth.uid() for inserts.
> 
> 4. Update qilifeStore.
>    - In Supabase mode, require an authenticated user.
>    - Insert records with owner_id set to the authenticated user id.
>    - List/update/archive only records owned by the signed-in user.
>    - Keep localStorage fallback working.
>    - Namespace localStorage records clearly, for example: qilife.local.records.v1.
> 
> 5. Replace window.prompt creation.
>    - Add a proper reusable EntityFormModal.
>    - Render fields from entityRegistry.
>    - Enforce required primary fields.
>    - Store normal fields in data jsonb.
>    - Map common top-level fields:
>      - status → records.status
>      - priority → records.priority
>      - due_date → records.due_date
> 
> 6. Add edit support.
>    - Clicking a table row or card opens the edit modal.
>    - User can edit fields and save.
>    - User can archive from edit modal.
>    - Archive should set archived_at rather than hard delete.
> 
> 7. Improve UX.
>    - Show loading states.
>    - Show error states.
>    - Show empty states.
>    - Show status pills:
>      - Supabase Connected
>      - Local Mode
>      - Signed in as {email}
>    - Keep the UI simple and clean.
> 
> 8. Do not overbuild.
>    - No Workers.
>    - No backend API.
>    - No AI.
>    - No graph.
>    - No file ingestion.
>    - No multi-user sharing.
>    - No complex dashboard analytics yet.
>    - No giant single-file rewrite.
> 
> 9. Test.
>    - Run npm install if needed.
>    - Run npm run build.
>    - Fix all TypeScript/build errors.
>    - Report exactly what changed.
>    - Report any remaining setup steps.
> 
> Expected result:
> A working QiLife MVP where Cody can:
> - run locally without Supabase using localStorage fallback
> - connect Supabase through env vars
> - log in with Supabase Auth
> - create/edit/archive records
> - keep records owner-scoped with RLS
> - navigate all registry-driven life domains
> - build successfully with no TypeScript errors
> :::
> 
> ## The migration should look roughly like this
> 
> Give Codex this too if it needs the SQL:
> 
> ```sql
> -- supabase/migrations/0002_qilife_auth_rls.sql
> 
> alter table qilife.records
> add column if not exists owner_id uuid references auth.users(id);
> 
> alter table qilife.records
> alter column owner_id set default auth.uid();
> 
> alter table qilife.records enable row level security;
> 
> drop policy if exists "Users can read own qilife records" on qilife.records;
> drop policy if exists "Users can insert own qilife records" on qilife.records;
> drop policy if exists "Users can update own qilife records" on qilife.records;
> drop policy if exists "Users can delete own qilife records" on qilife.records;
> 
> create policy "Users can read own qilife records"
> on qilife.records
> for select
> to authenticated
> using (owner_id = auth.uid());
> 
> create policy "Users can insert own qilife records"
> on qilife.records
> for insert
> to authenticated
> with check (owner_id = auth.uid());
> 
> create policy "Users can update own qilife records"
> on qilife.records
> for update
> to authenticated
> using (owner_id = auth.uid())
> with check (owner_id = auth.uid());
> 
> create policy "Users can delete own qilife records"
> on qilife.records
> for delete
> to authenticated
> using (owner_id = auth.uid());
> ```
> 
> ## One correction
> 
> For archive actions, the app does **update**, not delete:
> 
> ```txt
> archive = update archived_at
> ```
> 
> So the delete policy is optional for now. The important one is **update own records**.

### User
> what database driver do i need in vs code for supabase.

### Assistant
> For VS Code, don’t overthink this: Supabase is PostgreSQL. I’m verifying the current connection guidance so I don’t give you stale port/connection-string nonsense.

### Assistant
> Use a **PostgreSQL driver**. Supabase is Postgres.
> 
> Best VS Code setup:
> 
> ```txt
> SQLTools
> + SQLTools PostgreSQL/Cockroach Driver
> ```
> 
> Supabase’s own docs describe connecting to the database as connecting to a Postgres instance, with direct connections or pooler connections depending on your network/setup. citeturn390534search0 SQLTools’ Postgres driver supports normal PostgreSQL connection strings. citeturn390534search1
> 
> ## What to install in VS Code
> 
> Install these extensions:
> 
> ```txt
> SQLTools
> SQLTools PostgreSQL/Cockroach Driver
> Supabase
> ```
> 
> The **Supabase extension** is useful for project integration, but for plain SQL browsing/querying, the thing you need is still the **PostgreSQL driver**. citeturn390534search15
> 
> ## Which connection string to use
> 
> In Supabase:
> 
> ```txt
> Project Dashboard
> → Connect
> → Database connection string
> ```
> 
> Use **Session pooler** if your internet/network is IPv4-only. Supabase says direct connections are IPv6 unless you have the IPv4 add-on; if you’re IPv4-only, use the pooler session mode. citeturn390534search0
> 
> So your simple choice is:
> 
> ```txt
> For VS Code SQLTools: use Session Pooler connection string
> Driver: PostgreSQL
> ```
> 
> ## Do not use this in the app
> 
> This is only for VS Code / admin querying:
> 
> ```txt
> postgresql://...
> ```
> 
> Your React app does **not** use the database driver. It uses:
> 
> ```txt
> VITE_SUPABASE_URL
> VITE_SUPABASE_ANON_KEY
> ```
> 
> through `supabase-js`.
> 
> ## Clean answer
> 
> Use:
> 
> ```txt
> Driver: PostgreSQL
> Extension: SQLTools PostgreSQL/Cockroach Driver
> Connection: Supabase Session Pooler connection string
> ```
> 
> That’s it. Don’t install a random “Supabase database driver.” It’s Postgres wearing a Supabase hoodie.

### User
> Request URL
> https://emnskvvajdlqixwzjfsm.supabase.co/rest/v1/records?select=*
> Request Method
> POST
> Status Code
> 403 Forbidden (from service worker)
> Referrer Policy
> strict-origin-when-cross-origin
> access-control-allow-origin
> https://qilife.qially.com
> access-control-expose-headers
> Content-Encoding, Content-Location, Content-Range, Content-Type, Date, Location, Server, Transfer-Encoding, Range-Unit
> alt-svc
> h3=":443"; ma=86400
> cf-cache-status
> DYNAMIC
> cf-ray
> a10159ee48161fa5-ORD
> content-encoding
> br
> content-type
> application/json; charset=utf-8
> date
> Tue, 23 Jun 2026 06:14:13 GMT
> priority
> u=1,i
> proxy-status
> PostgREST; error=42501
> sb-gateway-version
> 1
> sb-project-ref
> emnskvvajdlqixwzjfsm
> sb-request-id
> 019ef31d-70ee-71a4-bda1-f1c66b7d9bba
> server
> cloudflare
> server-timing
> cfExtPri
> strict-transport-security
> max-age=31536000; includeSubDomains; preload
> x-content-type-options
> nosniff
> x-envoy-attempt-count
> 1
> x-envoy-upstream-service-time
> 130
> accept
> application/vnd.pgrst.object+json
> apikey
> eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVtbnNrdnZhamRscWl4d3pqZnNtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODEzNjEyMTAsImV4cCI6MjA5NjkzNzIxMH0.7v_iGqu1BtAWYnwzk0x_tjcd4q3-yNxoHfrJW1bW2Sc
> authorization
> Bearer eyJhbGciOiJFUzI1NiIsImtpZCI6IjQ3ZTE5ZDRkLWM4MGItNGIzNC1hMDIyLWNiODI2ODFlYTIxZSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2VtbnNrdnZhamRscWl4d3pqZnNtLnN1cGFiYXNlLmNvL2F1dGgvdjEiLCJzdWIiOiJlZGQzZWZjZS1lMTk5LTRlOTktODRjYi05YjJlNGQyY2ZjZDUiLCJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzgyMTk4Nzk3LCJpYXQiOjE3ODIxOTUxOTcsImVtYWlsIjoiY3JpY2U0NDg1QGdtYWlsLmNvbSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZW1haWwiLCJwcm92aWRlcnMiOlsiZW1haWwiXX0sInVzZXJfbWV0YWRhdGEiOnsiZW1haWwiOiJjcmljZTQ0ODVAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBob25lX3ZlcmlmaWVkIjpmYWxzZSwic3ViIjoiZWRkM2VmY2UtZTE5OS00ZTk5LTg0Y2ItOWIyZTRkMmNmY2Q1In0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoib3RwIiwidGltZXN0YW1wIjoxNzgyMTk1MTk3fV0sInNlc3Npb25faWQiOiJiYWQ5MmJjMS01NmFhLTQ2ZjktYWQ2Mi04ZDRkMzZmNGJlZDQiLCJpc19hbm9ueW1vdXMiOmZhbHNlfQ.dvcnUnYnImOAn2j2XpCpzvS82ZgWfAdZakYlC2bX_auNCyoFvsuTLWmbD4taUkl2r3qIa5FKbutKo5dVwio44g
> content-profile
> qilife
> content-type
> application/json
> dnt
> 1
> prefer
> return=representation
> referer
> https://qilife.qially.com/
> sec-ch-ua
> "Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"
> sec-ch-ua-mobile
> ?0
> sec-ch-ua-platform
> "Windows"
> user-agent
> Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36
> x-client-info
> supabase-js/2.108.2; runtime=web

### Assistant
> The good news: your app is actually logged in. The `Authorization: Bearer ...` token has `role: authenticated`, so auth is not the broken piece. The broken piece is **Postgres permissions/RLS**.

### Assistant
> Yep — this is **not a Cloudflare problem** and not really a service worker problem.
> 
> Your request proves:
> 
> ```txt
> Auth works ✅
> Supabase project URL works ✅
> Custom schema is being targeted ✅
> Database permission/RLS is blocking the insert ❌
> ```
> 
> The key clue:
> 
> ```txt
> Status Code: 403
> proxy-status: PostgREST; error=42501
> content-profile: qilife
> authorization: Bearer ... role authenticated
> ```
> 
> Supabase’s Data API uses **both Postgres grants and RLS policies**. Grants decide whether `authenticated` can touch the table at all; RLS decides which rows they can touch. citeturn491928search5 For custom schemas, Supabase also requires the schema to be exposed and granted to API roles. citeturn491928search1
> 
> ## Most likely cause
> 
> One of these is missing:
> 
> 1. `GRANT USAGE ON SCHEMA qilife TO authenticated`
> 2. `GRANT INSERT/SELECT/UPDATE ON qilife.records TO authenticated`
> 3. RLS insert policy
> 4. `owner_id` default/check is wrong
> 5. The app is not sending `owner_id`, and the DB has no `default auth.uid()`
> 
> Run this in Supabase SQL Editor:
> 
> ```sql
> -- 1. Make sure schema can be used by the API roles
> grant usage on schema qilife to anon, authenticated, service_role;
> 
> -- 2. Make sure authenticated users can reach the table.
> -- RLS will still restrict rows.
> grant select, insert, update, delete on table qilife.records to authenticated;
> 
> -- Optional: local/dev reads for anon should usually stay off for private app.
> -- Do NOT grant table access to anon unless you intentionally want logged-out access.
> 
> -- 3. Ensure owner_id exists.
> alter table qilife.records
> add column if not exists owner_id uuid references auth.users(id);
> 
> -- 4. Make owner_id auto-fill from the logged-in user.
> alter table qilife.records
> alter column owner_id set default auth.uid();
> 
> -- 5. Enable RLS.
> alter table qilife.records enable row level security;
> 
> -- 6. Replace policies cleanly.
> drop policy if exists "Users can read own qilife records" on qilife.records;
> drop policy if exists "Users can insert own qilife records" on qilife.records;
> drop policy if exists "Users can update own qilife records" on qilife.records;
> drop policy if exists "Users can delete own qilife records" on qilife.records;
> 
> create policy "Users can read own qilife records"
> on qilife.records
> for select
> to authenticated
> using (owner_id = auth.uid());
> 
> create policy "Users can insert own qilife records"
> on qilife.records
> for insert
> to authenticated
> with check (owner_id = auth.uid());
> 
> create policy "Users can update own qilife records"
> on qilife.records
> for update
> to authenticated
> using (owner_id = auth.uid())
> with check (owner_id = auth.uid());
> 
> create policy "Users can delete own qilife records"
> on qilife.records
> for delete
> to authenticated
> using (owner_id = auth.uid());
> ```
> 
> Then refresh the app and try creating a record again.
> 
> ## If it still fails
> 
> Check what the app is inserting. The payload should either include:
> 
> ```json
> {
>   "owner_id": "edd3efce-e199-4e99-84cb-9b2e4d2cfcd5"
> }
> ```
> 
> or the DB default should fill it automatically with:
> 
> ```sql
> default auth.uid()
> ```
> 
> For safety, I’d do **both**:
> 
> ```ts
> owner_id: user.id
> ```
> 
> in the app insert **and** keep the DB default. Belt and suspenders. Less drama.
> 
> ## Also check this setting
> 
> In Supabase:
> 
> ```txt
> Project Settings
> → Data API
> → Exposed schemas
> ```
> 
> Make sure this includes:
> 
> ```txt
> qilife
> ```
> 
> Your request has `content-profile: qilife`, so it probably is exposed already, but verify it anyway. If a custom schema is not exposed/granted correctly, Supabase can throw `42501` permission errors. citeturn491928search19
> 
> ## Tell Codex/IDE this
> 
> ```txt
> The app is authenticated, but Supabase POST to qilife.records returns 403 / PostgREST 42501.
> 
> Fix the Supabase permissions/RLS setup.
> 
> Ensure:
> - qilife schema is exposed in Supabase Data API.
> - authenticated has USAGE on schema qilife.
> - authenticated has select, insert, update, delete grants on qilife.records.
> - qilife.records has owner_id uuid references auth.users(id).
> - owner_id defaults to auth.uid().
> - RLS is enabled.
> - select/insert/update/delete policies restrict owner_id = auth.uid().
> - App inserts owner_id: user.id when in Supabase mode.
> 
> Do not add Workers.
> Do not use service_role in the browser.
> Do not disable RLS.
> Do not grant public anon access to private life records.
> ```
> 
> One more thing: don’t paste full auth bearer tokens publicly. The anon key is meant to be public-ish, but the logged-in `Authorization` token is session-sensitive. It expires, but still — don’t feed the gremlins.

### User
> {'asset_pointer': 'sediment://file_00000000c9ec720cb0f4d32ed3353378', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 897, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 224874, 'width': 1897}take a look at cadence, you see how the sidebar is first the planner with inbox, today, celadnar, then of course the we need to change this from a work app to a life app, to crm should just be ERM i forget what the RM stands for so instad of crm it PRM p for people here we have people, vendors, government. then in planner we add activitys there too and then what else should be in planner, PRM, then instead of PRM we maybe have workbench here we can put like the projects, creative stuff, my journal maybe.

### Assistant
> Yes — this is the right read.
> 
> Cadence’s sidebar works because it separates **time**, **relationships**, **work objects**, and **reports**. In the plugin code, that structure is literally defined as grouped nav: Planner, Projects, CRM, PRM, Workflow, Reports, etc. fileciteturn0file1 The settings/data file also shows the same module idea: planner, CRM, PRM, projects, custom pages, layouts, and custom entities. fileciteturn0file0
> 
> But for **QiLife**, we need to stop letting business-app language sneak in wearing a fake mustache.
> 
> ## First correction: don’t call it CRM/PRM
> 
> CRM = **Customer Relationship Management**.  
> PRM = **Partner Relationship Management**.  
> ERM could mean **Entity Relationship Management**, but that sounds database-y and weird for a life app.
> 
> For QiLife, call it plainly:
> 
> ```txt
> Relationships
> ```
> 
> Or, if you want the acronym:
> 
> ```txt
> RM = Relationship Management
> ```
> 
> But the sidebar label should probably just say:
> 
> ```txt
> PEOPLE
> ```
> 
> Cleaner. Less corporate. More you.
> 
> ---
> 
> # Better QiLife sidebar structure
> 
> Here is the structure I’d use:
> 
> ```txt
> Home
> 
> Planner
>   Inbox
>   Today
>   Calendar
>   Activities
>   Reminders
>   Routines
> 
> People
>   People
>   Family
>   Vendors
>   Government
>   Providers
>   Organizations
>   Interactions
> 
> Care
>   Care Dashboard
>   Care Notes
>   Appointments
>   Medications
>   Symptoms
>   Supplies
>   Incidents
> 
> Workbench
>   Projects
>   Creative
>   Journal
>   Tasks
>   Ideas
>   Decisions
> 
> Operations
>   Finance
>   Legal
>   Home
>   Vehicles
>   Pets
>   Inventory
> 
> Vault
>   Documents
>   Evidence
>   Receipts
>   Assets
>   References
> 
> Reports
>   Timeline
>   Money
>   Care
>   Legal
>   Productivity
>   Graph
> 
> System
>   Templates
>   Settings
>   Import
> ```
> 
> That is the life-app translation of Cadence.
> 
> ---
> 
> # What belongs where
> 
> ## Planner = time and execution
> 
> This is where your day gets controlled.
> 
> ```txt
> Planner
>   Inbox
>   Today
>   Calendar
>   Activities
>   Reminders
>   Routines
> ```
> 
> ### Why Activities belongs here
> 
> An **activity** is not really a person. It is a time/event/action object.
> 
> Examples:
> 
> ```txt
> Called pharmacy
> Paid rent
> Mom had appointment
> Sent legal email
> Installed smoke detector
> Went to DMV
> ```
> 
> So yes, put **Activities** under Planner.
> 
> But activities should also link to people, projects, care, legal, finance, etc.
> 
> ---
> 
> ## People = relationship management
> 
> This replaces CRM/PRM.
> 
> ```txt
> People
>   People
>   Family
>   Vendors
>   Government
>   Providers
>   Organizations
>   Interactions
> ```
> 
> ### Suggested entity split
> 
> | Entity | Meaning |
> |---|---|
> | People | actual humans |
> | Family | people with family role/filter |
> | Vendors | companies/services you pay |
> | Government | agencies, courts, benefits offices |
> | Providers | doctors, lawyers, caseworkers, contractors |
> | Organizations | companies, hospitals, agencies, nonprofits |
> | Interactions | calls, texts, meetings, emails |
> 
> Honestly, **Family, Vendors, Government, Providers** can be filtered views of People/Organizations at first. Do not over-table this yet.
> 
> Use:
> 
> ```txt
> person
> organization
> interaction
> ```
> 
> Then add categories:
> 
> ```txt
> person.category = family | provider | vendor_contact | government_contact | friend | support
> organization.category = vendor | government | medical | legal | finance | utility | nonprofit
> ```
> 
> That keeps it flexible.
> 
> ---
> 
> ## Care = caregiving domain
> 
> This gets its own section because it is operationally heavy.
> 
> ```txt
> Care
>   Care Dashboard
>   Care Notes
>   Appointments
>   Medications
>   Symptoms
>   Supplies
>   Incidents
> ```
> 
> This is where Mom’s Care lives later, but don’t make Mom’s Care the whole app.
> 
> ---
> 
> ## Workbench = active creation and build zone
> 
> This is the replacement for Cadence’s Projects/Workflow area.
> 
> ```txt
> Workbench
>   Projects
>   Creative
>   Journal
>   Tasks
>   Ideas
>   Decisions
> ```
> 
> This is where your “I am building my life and systems” work lives.
> 
> ### Journal placement
> 
> Yes, journal can go here, **but** there are two kinds:
> 
> | Journal type | Goes where |
> |---|---|
> | Daily operational journal | Planner / Today |
> | Longform reflection / creative / processing | Workbench / Journal |
> 
> So in the UI:
> 
> ```txt
> Planner → Today = daily note/action log
> Workbench → Journal = deeper entries
> ```
> 
> ---
> 
> ## Operations = adulting hellscape containment unit
> 
> This is finance/legal/home/etc.
> 
> ```txt
> Operations
>   Finance
>   Legal
>   Home
>   Vehicles
>   Pets
>   Inventory
> ```
> 
> This keeps “life admin” from polluting Planner and People.
> 
> ---
> 
> ## Vault = source files
> 
> QiLife should not pretend files are the same thing as tasks. The Vault is for artifacts.
> 
> ```txt
> Vault
>   Documents
>   Evidence
>   Receipts
>   Assets
>   References
> ```
> 
> This mirrors your QiNexus idea: files and source material live in storage; QiLife tracks and links them.
> 
> ---
> 
> # Clean MVP version
> 
> Do **not** build the full version yet. For the app right now, use this:
> 
> ```txt
> Home
> 
> Planner
>   Inbox
>   Today
>   Calendar
>   Activities
>   Reminders
> 
> People
>   People
>   Organizations
>   Interactions
> 
> Care
>   Care Notes
>   Appointments
>   Medications
>   Supplies
> 
> Workbench
>   Projects
>   Journal
>   Ideas
>   Decisions
> 
> Operations
>   Finance
>   Legal
>   Home Items
> 
> Vault
>   Documents
>   Receipts
>   Evidence
> 
> Reports
>   Timeline
>   Money
>   Care
>   Legal
> 
> System
>   Templates
>   Settings
> ```
> 
> That is enough. Anything more right now is glitter on a moving truck.
> 
> ---
> 
> # Entity registry changes
> 
> Your core entities should become:
> 
> ```txt
> planner:
>   inbox_item
>   task
>   activity
>   reminder
>   routine
> 
> people:
>   person
>   organization
>   interaction
> 
> care:
>   care_note
>   appointment
>   medication
>   symptom
>   supply
> 
> workbench:
>   project
>   journal_entry
>   idea
>   decision
> 
> operations:
>   expense
>   legal_matter
>   home_item
>   vehicle
>   pet
>   inventory_item
> 
> vault:
>   document
>   receipt
>   evidence_item
>   asset
>   reference
> ```
> 
> For MVP, only actually build these first:
> 
> ```txt
> task
> activity
> reminder
> person
> organization
> interaction
> care_note
> appointment
> medication
> project
> journal_entry
> idea
> decision
> expense
> legal_matter
> home_item
> document
> receipt
> evidence_item
> ```
> 
> ---
> 
> # What to tell Codex
> 
> Paste this:
> 
> ```txt
> Update QiLife navigation to follow the Cadence sidebar pattern, but translate it from a work app into a life management app.
> 
> Do not use CRM or PRM labels.
> Replace them with life-oriented groups.
> 
> New sidebar groups:
> 
> Home
> 
> Planner
> - Inbox
> - Today
> - Calendar
> - Activities
> - Reminders
> 
> People
> - People
> - Organizations
> - Interactions
> 
> Care
> - Care Notes
> - Appointments
> - Medications
> - Supplies
> 
> Workbench
> - Projects
> - Journal
> - Ideas
> - Decisions
> 
> Operations
> - Finance
> - Legal Matters
> - Home Items
> 
> Vault
> - Documents
> - Receipts
> - Evidence
> 
> Reports
> - Timeline
> - Money
> - Care
> - Legal
> 
> System
> - Templates
> - Settings
> 
> Update navRegistry.ts to reflect this structure.
> 
> Update entityRegistry.ts to include these entity keys:
> - task
> - activity
> - reminder
> - person
> - organization
> - interaction
> - care_note
> - appointment
> - medication
> - supply
> - project
> - journal_entry
> - idea
> - decision
> - expense
> - legal_matter
> - home_item
> - document
> - receipt
> - evidence_item
> 
> Keep this registry-driven.
> Do not hardcode separate pages for each entity.
> Each nav item should point to an entityKey unless it is Home, Today, Calendar, Reports, Templates, or Settings.
> 
> Use the same generic EntityPage, EntityTable, EntityCards, and EntityFormModal.
> 
> Do not add AI, graph, Workers, or advanced dashboards yet.
> Do not rename database tables.
> Everything still stores in qilife.records using entity_key.
> ```
> 
> ---
> 
> # My recommendation
> 
> Use this label set:
> 
> ```txt
> Planner
> People
> Care
> Workbench
> Operations
> Vault
> Reports
> System
> ```
> 
> That is the clean QiLife spine.
> 
> Not CRM. Not PRM. Not ERM. Not business cosplay. This is your life OS, not Salesforce in a trench coat.

### User
> are we making it more specific unnessarily, i like to keep it lean and properties give the items more specific meaning or something, we want to keep tables low, remember our guiding principals.

### Assistant
> Yes. **You caught it.** I was drifting too specific.
> 
> We should **not** create a separate entity for every life noun. That is how we accidentally rebuild a giant Notion database swamp with better CSS. Bad trade.
> 
> The better rule:
> 
> ```txt
> Few entity types.
> Rich properties.
> Filtered views.
> ```
> 
> ## Correct QiLife principle
> 
> Instead of:
> 
> ```txt
> medication
> supply
> receipt
> evidence_item
> journal_entry
> idea
> decision
> interaction
> activity
> appointment
> home_item
> inventory_item
> vehicle
> pet
> ```
> 
> Use fewer core record types:
> 
> ```txt
> task
> event
> note
> person
> organization
> project
> document
> transaction
> asset
> matter
> ```
> 
> Then properties give meaning.
> 
> Example:
> 
> ```txt
> record_type: note
> domain: workbench
> category: journal | idea | decision | care_note | legal_note
> ```
> 
> Or:
> 
> ```txt
> record_type: document
> domain: legal
> category: evidence | receipt | form | letter | medical_record
> ```
> 
> That is much leaner.
> 
> ---
> 
> # The real model
> 
> ## Keep the database low
> 
> Your database should stay boring:
> 
> ```txt
> qilife.records
> qilife.record_links
> qilife.files maybe later
> ```
> 
> Not 40 tables.
> 
> ## Keep entity types low
> 
> Use these core entity types:
> 
> ```txt
> task
> event
> note
> person
> organization
> project
> document
> transaction
> asset
> matter
> ```
> 
> That is probably enough for 80% of QiLife.
> 
> ## Use properties for specificity
> 
> Every record can have:
> 
> ```txt
> domain
> category
> status
> priority
> date
> due_date
> person_id
> project_id
> matter_id
> tags
> data
> ```
> 
> So a “medication” does not need to be a whole entity/table at first. It can be:
> 
> ```txt
> record_type: asset
> domain: care
> category: medication
> title: Doxycycline
> ```
> 
> A “doctor appointment” can be:
> 
> ```txt
> record_type: event
> domain: care
> category: appointment
> ```
> 
> A “receipt” can be:
> 
> ```txt
> record_type: document
> domain: finance
> category: receipt
> ```
> 
> A “government agency” can be:
> 
> ```txt
> record_type: organization
> domain: legal
> category: government
> ```
> 
> That is the way.
> 
> ---
> 
> # Revised sidebar: lean version
> 
> Use sections as **views**, not separate databases.
> 
> ```txt
> Home
> 
> Planner
>   Inbox
>   Today
>   Calendar
>   Tasks
>   Events
>   Notes
> 
> People
>   People
>   Organizations
>   Relationships
> 
> Workbench
>   Projects
>   Notes
>   Decisions
>   Ideas
> 
> Operations
>   Finance
>   Legal
>   Care
>   Home
> 
> Vault
>   Documents
>   Assets
>   Receipts
>   Evidence
> 
> Reports
>   Timeline
>   Money
>   Care
>   Legal
> 
> System
>   Templates
>   Settings
> ```
> 
> The sidebar can feel specific, but under the hood it should mostly be filtered views.
> 
> Example:
> 
> ```txt
> Vault → Receipts
> = record_type document
> + category receipt
> ```
> 
> Not a new table. Not even necessarily a new entity.
> 
> ---
> 
> # Better core registry
> 
> Tell Codex to use this:
> 
> ```txt
> Core entity keys only:
> 
> task
> event
> note
> person
> organization
> relationship
> project
> document
> transaction
> asset
> matter
> ```
> 
> Then add these shared fields:
> 
> ```txt
> domain:
>   planner
>   people
>   workbench
>   care
>   finance
>   legal
>   home
>   vault
>   system
> 
> category:
>   flexible per domain
> 
> status:
>   inbox
>   active
>   waiting
>   done
>   archived
> 
> priority:
>   low
>   medium
>   high
>   urgent
> 
> tags:
>   freeform
> ```
> 
> ---
> 
> # What this means practically
> 
> ## “Care Notes” is not an entity
> 
> It is a filtered view:
> 
> ```txt
> note where domain = care
> ```
> 
> ## “Appointments” is not an entity
> 
> It is a filtered view:
> 
> ```txt
> event where category = appointment
> ```
> 
> ## “Receipts” is not an entity
> 
> It is a filtered view:
> 
> ```txt
> document where category = receipt
> ```
> 
> ## “Evidence” is not an entity
> 
> It is a filtered view:
> 
> ```txt
> document where category = evidence
> ```
> 
> ## “Ideas” and “Decisions” are not entities
> 
> They are filtered notes:
> 
> ```txt
> note where category = idea
> note where category = decision
> ```
> 
> ## “Legal Matters” probably **is** an entity
> 
> But call it:
> 
> ```txt
> matter
> ```
> 
> Then:
> 
> ```txt
> matter.domain = legal
> matter.category = dispute | filing | benefits | immigration | housing | vehicle | employment
> ```
> 
> ---
> 
> # The better instruction for Codex
> 
> Use this instead of the previous bloated one:
> 
> ```txt
> Update QiLife to stay lean and property-driven.
> 
> Do not create a separate entity for every life category.
> Use a small set of core entity types and filtered views.
> 
> Core entity keys:
> - task
> - event
> - note
> - person
> - organization
> - relationship
> - project
> - document
> - transaction
> - asset
> - matter
> 
> Do not add separate entities for:
> - care_note
> - appointment
> - medication
> - supply
> - journal_entry
> - idea
> - decision
> - receipt
> - evidence_item
> - home_item
> 
> Represent those as core entity records with domain/category properties.
> 
> Examples:
> - Care Note = note with domain "care"
> - Appointment = event with category "appointment"
> - Medication = asset with domain "care" and category "medication"
> - Receipt = document with category "receipt"
> - Evidence = document with category "evidence"
> - Journal = note with category "journal"
> - Idea = note with category "idea"
> - Decision = note with category "decision"
> - Home Item = asset with domain "home"
> 
> Keep one generic qilife.records table.
> Keep entityRegistry small.
> Add navRegistry items as filtered views over core entities.
> Do not create new database tables.
> Do not overbuild.
> ```
> 
> ---
> 
> # The final spine
> 
> This is the correct QiLife model:
> 
> ```txt
> One records table.
> About 10 core record types.
> Domain + category gives meaning.
> Sidebar pages are filtered views.
> AI can interpret and enrich later.
> ```
> 
> That is aligned with your principles.
> 
> You were right to push back. My previous list was useful for brainstorming, but too specific for the actual build.

### User
> ok, for now dont worry about finance items because those have to be the full system and we are using an app for finances right now, lets first define the core tables for qilife.

### Assistant
> Yes. **Finance stays out for now.** Good call.
> 
> For QiLife core, we keep the database lean:
> 
> ```txt
> One main record table.
> One link table.
> One attachment table.
> One log/timeline table.
> Optional settings/views table later.
> ```
> 
> That matches the anti-chaos rule: every part needs a clear job, or it is noise. fileciteturn3file1 It also matches the source-of-truth split: database records can be truth, Drive/QiNexus files are storage truth, and AI/graphs/reports are derived, not canonical. fileciteturn3file2
> 
> # QiLife Core Tables v1
> 
> ## Keep these tables
> 
> | Table | Job |
> |---|---|
> | `qilife.records` | Main universal life item table |
> | `qilife.record_links` | Relationships between records |
> | `qilife.attachments` | Links to Drive/QiNexus/files |
> | `qilife.activity_log` | Timeline/audit trail of what happened |
> | `qilife.saved_views` | Optional UI/sidebar filtered views |
> 
> ## Do **not** create these yet
> 
> ```txt
> people
> organizations
> tasks
> events
> notes
> projects
> documents
> assets
> matters
> care_notes
> appointments
> medications
> receipts
> evidence
> transactions
> ```
> 
> Those become **record types/categories**, not tables.
> 
> ---
> 
> # Core record types
> 
> Inside `qilife.records`, use:
> 
> ```txt
> task
> event
> note
> person
> organization
> project
> document
> asset
> matter
> ```
> 
> No finance records yet except maybe generic `document` for receipts if needed. But no transaction/ledger/account system inside QiLife right now.
> 
> ---
> 
> # Core fields
> 
> Every QiLife record gets:
> 
> ```txt
> record_type   = what kind of object this is
> domain        = where it belongs
> category      = more specific meaning
> title         = human-readable name
> status        = lifecycle
> priority      = urgency/importance
> starts_at     = for events/routines/time blocks
> due_at        = for tasks/deadlines
> happened_at   = for timeline notes/events
> data          = flexible JSON properties
> tags          = simple text array
> ```
> 
> Examples:
> 
> ```txt
> Care note:
> record_type = note
> domain = care
> category = care_note
> 
> Appointment:
> record_type = event
> domain = care
> category = appointment
> 
> Medication:
> record_type = asset
> domain = care
> category = medication
> 
> Journal entry:
> record_type = note
> domain = workbench
> category = journal
> 
> Decision:
> record_type = note
> domain = workbench
> category = decision
> 
> Government agency:
> record_type = organization
> domain = legal
> category = government
> 
> Legal matter:
> record_type = matter
> domain = legal
> category = housing / vehicle / benefits / family / etc.
> ```
> 
> That keeps tables low and meaning rich. Exactly the right direction.
> 
> ---
> 
> # SQL: QiLife core schema v1
> 
> Give Codex this as the next migration. If `qilife.records` already exists, this should be a new migration, not a rewrite.
> 
> ```sql
> -- supabase/migrations/0003_qilife_core_spine.sql
> 
> create schema if not exists qilife;
> 
> create extension if not exists pgcrypto;
> 
> -- ============================================================
> -- 1. Core universal record table
> -- ============================================================
> 
> create table if not exists qilife.records (
>   id uuid primary key default gen_random_uuid(),
> 
>   owner_id uuid not null references auth.users(id) default auth.uid(),
> 
>   record_type text not null,
>   domain text,
>   category text,
> 
>   title text not null,
>   summary text,
> 
>   status text not null default 'active',
>   priority text,
> 
>   starts_at timestamptz,
>   due_at timestamptz,
>   happened_at timestamptz,
> 
>   tags text[] not null default '{}',
>   data jsonb not null default '{}'::jsonb,
> 
>   source text not null default 'qilife',
>   source_id text,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now(),
>   archived_at timestamptz
> );
> 
> create index if not exists idx_qilife_records_owner
>   on qilife.records(owner_id);
> 
> create index if not exists idx_qilife_records_type
>   on qilife.records(record_type);
> 
> create index if not exists idx_qilife_records_domain_category
>   on qilife.records(domain, category);
> 
> create index if not exists idx_qilife_records_status
>   on qilife.records(status);
> 
> create index if not exists idx_qilife_records_due_at
>   on qilife.records(due_at);
> 
> create index if not exists idx_qilife_records_happened_at
>   on qilife.records(happened_at);
> 
> create index if not exists idx_qilife_records_tags
>   on qilife.records using gin(tags);
> 
> create index if not exists idx_qilife_records_data
>   on qilife.records using gin(data);
> 
> -- ============================================================
> -- 2. Generic record-to-record links
> -- ============================================================
> 
> create table if not exists qilife.record_links (
>   id uuid primary key default gen_random_uuid(),
> 
>   owner_id uuid not null references auth.users(id) default auth.uid(),
> 
>   from_record_id uuid not null references qilife.records(id) on delete cascade,
>   to_record_id uuid not null references qilife.records(id) on delete cascade,
> 
>   link_type text not null,
>   direction text not null default 'outgoing',
> 
>   note text,
>   data jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
> 
>   constraint record_links_no_self_link
>     check (from_record_id <> to_record_id)
> );
> 
> create index if not exists idx_qilife_record_links_owner
>   on qilife.record_links(owner_id);
> 
> create index if not exists idx_qilife_record_links_from
>   on qilife.record_links(from_record_id);
> 
> create index if not exists idx_qilife_record_links_to
>   on qilife.record_links(to_record_id);
> 
> create index if not exists idx_qilife_record_links_type
>   on qilife.record_links(link_type);
> 
> create unique index if not exists uq_qilife_record_links_unique
>   on qilife.record_links(from_record_id, to_record_id, link_type);
> 
> -- ============================================================
> -- 3. Attachments / external file references
> -- Drive, QiNexus, local paths, URLs, future storage providers
> -- ============================================================
> 
> create table if not exists qilife.attachments (
>   id uuid primary key default gen_random_uuid(),
> 
>   owner_id uuid not null references auth.users(id) default auth.uid(),
> 
>   record_id uuid references qilife.records(id) on delete cascade,
> 
>   title text,
>   attachment_type text,
> 
>   storage_provider text not null default 'url',
>   storage_key text,
>   url text,
> 
>   mime_type text,
>   file_name text,
>   file_size bigint,
> 
>   data jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
>   archived_at timestamptz
> );
> 
> create index if not exists idx_qilife_attachments_owner
>   on qilife.attachments(owner_id);
> 
> create index if not exists idx_qilife_attachments_record
>   on qilife.attachments(record_id);
> 
> create index if not exists idx_qilife_attachments_type
>   on qilife.attachments(attachment_type);
> 
> -- ============================================================
> -- 4. Activity log / timeline
> -- This tracks important changes and real-world events.
> -- ============================================================
> 
> create table if not exists qilife.activity_log (
>   id uuid primary key default gen_random_uuid(),
> 
>   owner_id uuid not null references auth.users(id) default auth.uid(),
> 
>   record_id uuid references qilife.records(id) on delete set null,
> 
>   action text not null,
>   message text,
> 
>   happened_at timestamptz not null default now(),
> 
>   actor_type text not null default 'user',
>   actor_id uuid,
> 
>   data jsonb not null default '{}'::jsonb
> );
> 
> create index if not exists idx_qilife_activity_log_owner
>   on qilife.activity_log(owner_id);
> 
> create index if not exists idx_qilife_activity_log_record
>   on qilife.activity_log(record_id);
> 
> create index if not exists idx_qilife_activity_log_action
>   on qilife.activity_log(action);
> 
> create index if not exists idx_qilife_activity_log_happened_at
>   on qilife.activity_log(happened_at);
> 
> -- ============================================================
> -- 5. Saved views
> -- Optional, but useful for sidebar filters without hardcoding forever.
> -- ============================================================
> 
> create table if not exists qilife.saved_views (
>   id uuid primary key default gen_random_uuid(),
> 
>   owner_id uuid not null references auth.users(id) default auth.uid(),
> 
>   key text not null,
>   label text not null,
>   section text not null,
> 
>   record_type text,
>   domain text,
>   category text,
> 
>   filters jsonb not null default '{}'::jsonb,
>   layout text not null default 'table',
>   sort jsonb not null default '{}'::jsonb,
> 
>   position integer not null default 0,
>   is_system boolean not null default false,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now(),
> 
>   unique(owner_id, key)
> );
> 
> create index if not exists idx_qilife_saved_views_owner
>   on qilife.saved_views(owner_id);
> 
> create index if not exists idx_qilife_saved_views_section
>   on qilife.saved_views(section);
> 
> -- ============================================================
> -- Updated-at helper
> -- ============================================================
> 
> create or replace function qilife.set_updated_at()
> returns trigger as $$
> begin
>   new.updated_at = now();
>   return new;
> end;
> $$ language plpgsql;
> 
> drop trigger if exists trg_qilife_records_updated_at on qilife.records;
> create trigger trg_qilife_records_updated_at
> before update on qilife.records
> for each row
> execute function qilife.set_updated_at();
> 
> drop trigger if exists trg_qilife_saved_views_updated_at on qilife.saved_views;
> create trigger trg_qilife_saved_views_updated_at
> before update on qilife.saved_views
> for each row
> execute function qilife.set_updated_at();
> 
> -- ============================================================
> -- Grants
> -- ============================================================
> 
> grant usage on schema qilife to authenticated;
> 
> grant select, insert, update, delete on table qilife.records to authenticated;
> grant select, insert, update, delete on table qilife.record_links to authenticated;
> grant select, insert, update, delete on table qilife.attachments to authenticated;
> grant select, insert, update, delete on table qilife.activity_log to authenticated;
> grant select, insert, update, delete on table qilife.saved_views to authenticated;
> 
> -- ============================================================
> -- RLS
> -- ============================================================
> 
> alter table qilife.records enable row level security;
> alter table qilife.record_links enable row level security;
> alter table qilife.attachments enable row level security;
> alter table qilife.activity_log enable row level security;
> alter table qilife.saved_views enable row level security;
> 
> -- records
> drop policy if exists "Users can read own records" on qilife.records;
> drop policy if exists "Users can insert own records" on qilife.records;
> drop policy if exists "Users can update own records" on qilife.records;
> drop policy if exists "Users can delete own records" on qilife.records;
> 
> create policy "Users can read own records"
> on qilife.records
> for select
> to authenticated
> using (owner_id = auth.uid());
> 
> create policy "Users can insert own records"
> on qilife.records
> for insert
> to authenticated
> with check (owner_id = auth.uid());
> 
> create policy "Users can update own records"
> on qilife.records
> for update
> to authenticated
> using (owner_id = auth.uid())
> with check (owner_id = auth.uid());
> 
> create policy "Users can delete own records"
> on qilife.records
> for delete
> to authenticated
> using (owner_id = auth.uid());
> 
> -- record_links
> drop policy if exists "Users can read own record links" on qilife.record_links;
> drop policy if exists "Users can insert own record links" on qilife.record_links;
> drop policy if exists "Users can update own record links" on qilife.record_links;
> drop policy if exists "Users can delete own record links" on qilife.record_links;
> 
> create policy "Users can read own record links"
> on qilife.record_links
> for select
> to authenticated
> using (owner_id = auth.uid());
> 
> create policy "Users can insert own record links"
> on qilife.record_links
> for insert
> to authenticated
> with check (owner_id = auth.uid());
> 
> create policy "Users can update own record links"
> on qilife.record_links
> for update
> to authenticated
> using (owner_id = auth.uid())
> with check (owner_id = auth.uid());
> 
> create policy "Users can delete own record links"
> on qilife.record_links
> for delete
> to authenticated
> using (owner_id = auth.uid());
> 
> -- attachments
> drop policy if exists "Users can read own attachments" on qilife.attachments;
> drop policy if exists "Users can insert own attachments" on qilife.attachments;
> drop policy if exists "Users can update own attachments" on qilife.attachments;
> drop policy if exists "Users can delete own attachments" on qilife.attachments;
> 
> create policy "Users can read own attachments"
> on qilife.attachments
> for select
> to authenticated
> using (owner_id = auth.uid());
> 
> create policy "Users can insert own attachments"
> on qilife.attachments
> for insert
> to authenticated
> with check (owner_id = auth.uid());
> 
> create policy "Users can update own attachments"
> on qilife.attachments
> for update
> to authenticated
> using (owner_id = auth.uid())
> with check (owner_id = auth.uid());
> 
> create policy "Users can delete own attachments"
> on qilife.attachments
> for delete
> to authenticated
> using (owner_id = auth.uid());
> 
> -- activity_log
> drop policy if exists "Users can read own activity log" on qilife.activity_log;
> drop policy if exists "Users can insert own activity log" on qilife.activity_log;
> drop policy if exists "Users can update own activity log" on qilife.activity_log;
> drop policy if exists "Users can delete own activity log" on qilife.activity_log;
> 
> create policy "Users can read own activity log"
> on qilife.activity_log
> for select
> to authenticated
> using (owner_id = auth.uid());
> 
> create policy "Users can insert own activity log"
> on qilife.activity_log
> for insert
> to authenticated
> with check (owner_id = auth.uid());
> 
> create policy "Users can update own activity log"
> on qilife.activity_log
> for update
> to authenticated
> using (owner_id = auth.uid())
> with check (owner_id = auth.uid());
> 
> create policy "Users can delete own activity log"
> on qilife.activity_log
> for delete
> to authenticated
> using (owner_id = auth.uid());
> 
> -- saved_views
> drop policy if exists "Users can read own saved views" on qilife.saved_views;
> drop policy if exists "Users can insert own saved views" on qilife.saved_views;
> drop policy if exists "Users can update own saved views" on qilife.saved_views;
> drop policy if exists "Users can delete own saved views" on qilife.saved_views;
> 
> create policy "Users can read own saved views"
> on qilife.saved_views
> for select
> to authenticated
> using (owner_id = auth.uid());
> 
> create policy "Users can insert own saved views"
> on qilife.saved_views
> for insert
> to authenticated
> with check (owner_id = auth.uid());
> 
> create policy "Users can update own saved views"
> on qilife.saved_views
> for update
> to authenticated
> using (owner_id = auth.uid())
> with check (owner_id = auth.uid());
> 
> create policy "Users can delete own saved views"
> on qilife.saved_views
> for delete
> to authenticated
> using (owner_id = auth.uid());
> ```
> 
> ---
> 
> # Sidebar/views should be filters, not tables
> 
> For now, the app sidebar should map to filtered views like this:
> 
> ```txt
> Planner
>   Inbox       = records where status = inbox
>   Today       = tasks/events/notes due or happening today
>   Calendar    = records where record_type = event
>   Tasks       = records where record_type = task
>   Notes       = records where record_type = note
> 
> People
>   People      = record_type person
>   Orgs        = record_type organization
>   Government  = organization + category government
>   Providers   = organization/person + category provider
> 
> Workbench
>   Projects    = record_type project
>   Journal     = note + category journal
>   Ideas       = note + category idea
>   Decisions   = note + category decision
> 
> Operations
>   Care        = domain care
>   Legal       = domain legal OR record_type matter
>   Home        = domain home
> 
> Vault
>   Documents   = record_type document
>   Evidence    = document + category evidence
>   Assets      = record_type asset
> ```
> 
> Again: **views, not tables.**
> 
> ---
> 
> # Tell Codex this
> 
> ```txt
> Define QiLife core tables using a lean property-driven model.
> 
> Do not create finance tables yet.
> Do not create separate tables for people, tasks, events, notes, projects, documents, care notes, appointments, receipts, or evidence.
> 
> Use these core tables only:
> - qilife.records
> - qilife.record_links
> - qilife.attachments
> - qilife.activity_log
> - qilife.saved_views
> 
> Everything user-facing should be represented as records with:
> - record_type
> - domain
> - category
> - title
> - status
> - priority
> - starts_at
> - due_at
> - happened_at
> - tags
> - data jsonb
> 
> Core record_type values:
> - task
> - event
> - note
> - person
> - organization
> - project
> - document
> - asset
> - matter
> 
> Use filtered views for sidebar pages.
> Examples:
> - Care Note = note with domain care and category care_note
> - Appointment = event with domain care and category appointment
> - Medication = asset with domain care and category medication
> - Receipt = document with category receipt, but do not build finance system yet
> - Evidence = document with category evidence
> - Journal = note with category journal
> - Decision = note with category decision
> 
> Add or update Supabase SQL migrations safely.
> Do not rewrite already-applied migrations unless they have not been run.
> Add owner_id, grants, and RLS policies for authenticated users.
> No Workers.
> No service_role in browser.
> No finance/ledger/accounting module yet.
> ```
> 
> ## My call
> 
> The actual QiLife core is:
> 
> ```txt
> records
> record_links
> attachments
> activity_log
> saved_views
> ```
> 
> That’s it. Everything else earns its own table later only if it proves the generic model cannot handle it. This keeps the system lean instead of turning into a database junk drawer with a login screen.

### User
> {'asset_pointer': 'sediment://file_00000000257c71f5bbae112378891e9c', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 842, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 84361, 'width': 1588}{'asset_pointer': 'sediment://file_00000000c128722fa64bfe8d1c631409', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 842, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 62189, 'width': 1588}{'asset_pointer': 'sediment://file_00000000228071f59233eb62bfffdf1e', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 842, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 95234, 'width': 1588}{'asset_pointer': 'sediment://file_00000000752871f5b89312b2ee4e342d', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 842, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 46833, 'width': 1588}{'asset_pointer': 'sediment://file_0000000090cc71f59028a43fc498867f', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 842, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 110786, 'width': 1588}fyi this is what you ahve to work with in supabase as of now.

### Assistant
> Good. This changes the move.
> 
> You already have **most of the generic spine** sitting there. So no, we should **not** blindly create a fresh parallel QiLife schema and duplicate the same concepts. That would be database clutter with a fancy hat.
> 
> From the screenshots, I can see you already have tables like:
> 
> ```txt
> records
> folders
> tags
> record_tags
> attachments
> events
> links
> flow_rules
> ```
> 
> And then separate existing systems:
> 
> ```txt
> storage.*
> vault.secrets
> realtime.*
> finance-ish tables: banks, accounts, journal_lines, import_profiles, financial_institutions, etc.
> ```
> 
> So the correct move is **not** “make new tables.” The correct move is:
> 
> ```txt
> Audit existing spine
> → decide whether it becomes QiLife core
> → add missing columns/properties
> → point the app at the correct schema/table
> → do not touch finance yet
> ```
> 
> ## The important thing I notice
> 
> Your existing `records` table already has:
> 
> ```txt
> id
> library_id
> title
> module
> record_type
> data
> created_at
> updated_at
> ```
> 
> That is basically the lean QiLife model already.
> 
> So instead of adding:
> 
> ```txt
> qilife.records
> ```
> 
> we need to decide:
> 
> ### Option A — reuse existing `records`
> 
> Probably best if this table is already your generic OS spine.
> 
> Add missing columns:
> 
> ```txt
> owner_id
> domain
> category
> status
> priority
> starts_at
> due_at
> happened_at
> archived_at
> tags maybe optional because record_tags already exists
> ```
> 
> ### Option B — keep existing `records` for QiNexus / old system and create `qilife.records`
> 
> Only do this if the current `records` table belongs to another module and you want QiLife isolated.
> 
> But based on your “keep it lean” principle, **Option A is probably right**.
> 
> ## Do not duplicate these
> 
> Since they already exist:
> 
> ```txt
> attachments
> tags
> record_tags
> events
> links
> folders
> ```
> 
> Do **not** create new versions unless the current ones are broken or belong to a different schema.
> 
> So instead of:
> 
> ```txt
> qilife.attachments
> qilife.activity_log
> qilife.record_links
> ```
> 
> we likely adapt/use:
> 
> ```txt
> attachments
> events
> links
> record_tags
> tags
> folders
> ```
> 
> ## The likely reason your app failed earlier
> 
> Your app request was hitting:
> 
> ```txt
> content-profile: qilife
> /rest/v1/records
> ```
> 
> That means the frontend is asking for:
> 
> ```txt
> qilife.records
> ```
> 
> But your visible `records` table may be in another schema, likely `public` or an existing app schema.
> 
> So the app may be pointing to the wrong schema.
> 
> That means we need to answer one thing before changing code:
> 
> ```txt
> Where is the current records table?
> public.records?
> qilife.records?
> another schema?
> ```
> 
> If the existing table is `public.records`, then either:
> 
> ```txt
> 1. Change app to use public.records
> ```
> 
> or:
> 
> ```txt
> 2. Move/adapt the table into qilife.records
> ```
> 
> I would **not** move yet. I’d first get it working.
> 
> ---
> 
> # Recommended decision
> 
> For now:
> 
> ```txt
> Use existing records spine.
> Do not create new core tables.
> Do not touch finance.
> Add QiLife-specific columns to existing records table.
> Update app to use that schema/table.
> ```
> 
> ## Core QiLife tables from what already exists
> 
> Use these:
> 
> | Current table | QiLife role |
> |---|---|
> | `records` | universal item table |
> | `folders` | libraries/buckets/views/collections |
> | `tags` | reusable tag dictionary |
> | `record_tags` | record/tag join table |
> | `attachments` | files, Drive links, evidence, documents |
> | `events` | timeline/system/life events |
> | `links` | relationship/event links |
> | `flow_rules` | later automation/classification rules |
> 
> That is enough. Honestly, that’s a solid spine.
> 
> ## What to add to `records`
> 
> Add these columns only if missing:
> 
> ```sql
> alter table records
> add column if not exists owner_id uuid references auth.users(id) default auth.uid();
> 
> alter table records
> add column if not exists domain text;
> 
> alter table records
> add column if not exists category text;
> 
> alter table records
> add column if not exists status text default 'active';
> 
> alter table records
> add column if not exists priority text;
> 
> alter table records
> add column if not exists starts_at timestamptz;
> 
> alter table records
> add column if not exists due_at timestamptz;
> 
> alter table records
> add column if not exists happened_at timestamptz;
> 
> alter table records
> add column if not exists archived_at timestamptz;
> ```
> 
> But careful: if the table is not in `public`, prefix the schema:
> 
> ```sql
> alter table your_schema.records ...
> ```
> 
> ## Better field mapping
> 
> You already have `module`.
> 
> So we can map:
> 
> ```txt
> module = domain
> record_type = type
> data = flexible details
> library_id = folder/library/container
> ```
> 
> Meaning maybe we do **not** even need `domain` if `module` already serves that role.
> 
> But I’d probably standardize to this:
> 
> ```txt
> module = high-level system/module: qilife, qinexus, qifinance, qilegal
> domain = life domain: care, legal, home, workbench, people, planner
> category = specific subtype: appointment, care_note, evidence, journal, decision
> record_type = core shape: task, event, note, person, organization, project, document, asset, matter
> ```
> 
> That gives you flexibility without multiplying tables.
> 
> ---
> 
> # What to tell Codex now
> 
> Use this, not the older migration prompt:
> 
> ```txt
> Stop before creating new QiLife core tables.
> 
> The Supabase project already has an existing generic spine:
> - records
> - folders
> - tags
> - record_tags
> - attachments
> - events
> - links
> - flow_rules
> 
> Do not duplicate these with new qilife.records / qilife.attachments tables unless they do not exist in the target schema.
> 
> First inspect the actual schema location of these tables:
> - public.records or other_schema.records?
> - public.attachments or other_schema.attachments?
> - public.events?
> - public.tags?
> - public.record_tags?
> - public.links?
> 
> Then update the app/store to point at the existing records table/schema.
> 
> QiLife should reuse the existing generic records spine and remain property-driven.
> 
> Do not create finance tables.
> Do not touch existing finance/accounting tables.
> Do not create separate tables for tasks, people, notes, appointments, medications, evidence, receipts, or documents.
> 
> Use records with:
> - module
> - record_type
> - domain
> - category
> - title
> - status
> - priority
> - starts_at
> - due_at
> - happened_at
> - data jsonb
> 
> If missing, add these columns to the existing records table:
> - owner_id uuid references auth.users(id) default auth.uid()
> - domain text
> - category text
> - status text default 'active'
> - priority text
> - starts_at timestamptz
> - due_at timestamptz
> - happened_at timestamptz
> - archived_at timestamptz
> 
> Keep existing:
> - library_id
> - module
> - record_type
> - data
> - created_at
> - updated_at
> 
> Add grants/RLS to the actual table schema:
> - grant usage on schema <schema_name> to authenticated
> - grant select, insert, update, delete on <schema_name>.records to authenticated
> - enable RLS
> - policies owner_id = auth.uid()
> 
> Update the frontend Supabase client calls:
> - If using public schema, remove .schema("qilife")
> - If using a custom schema, make sure the schema exists, is exposed in Supabase Data API, and has proper grants.
> 
> Do not add Workers.
> Do not use service_role in browser.
> Do not disable RLS.
> ```
> 
> ## My current read
> 
> You already built the generic core once.
> 
> QiLife should become a **view/app layer over that spine**, not another schema island unless we have a very specific reason.
> 
> The immediate fix is probably:
> 
> ```txt
> Frontend is querying qilife.records
> but your real records table is elsewhere.
> ```
> 
> So align the app to the actual existing `records` table before adding more tables. That’s the clean move.
