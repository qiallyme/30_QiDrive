---
layout: page
title: "Caregiver Portal Zia Prompt"
slug: "caregiver_portal_zia_prompt"
created_at: "2026-01-25 10:01:59"
updated_at: "2026-07-18T11:03:13-04:00"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-003.json"
template_key: master-template
date: 2026-01-25
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69763e65-8180-8331-ab27-d92c51a08a4e"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Caregiver Portal Zia Prompt

## Overview
- **Date**: 2026-01-25 10:01:59
- **Conversation ID**: `69763e65-8180-8331-ab27-d92c51a08a4e`
- **Source**: `Chat-Export-28513-2026/conversations-003.json`

## Chat History

### User
> GIVE ME A ZIA PROMPT TO CREATE A CARE GIVER PORTAL FOR MY MOM THAT WILL HELP US TRACK HER APPOINTMENTS TRACK HER OXYGEN MEDICAL SUPPLIES INVENTORIES AND ORDERING, DOCUMENT HEALTH CONDITION AND CHANGES HER CARE PLAN, OTHER HEALTH TRACKERS SHE CAN INPUT, MEDICINE REMINDERS, CHORES/TASK LISTS, CARE GIVER INFORMATION, PLACE TO STORE IMPORTANT DOCUMENTS, SEND MESSAGES TO CARE GIVERS, AND SHOPPING LISTS.

### Assistant
> Below is a **copy-paste ready Zia (Zoho Creator + Zia AI) master prompt**.  
> This is written to force **structure, not fluff**, and to produce a **usable caregiver portal**, not a demo toy.
> 
> ---
> 
> ## ZIA MASTER PROMPT — CAREGIVER PORTAL (MOTHER CARE)
> 
> ```
> You are Zia, acting as a senior Zoho Creator solution architect and healthcare workflow designer.
> 
> GOAL:
> Create a secure, role-based Caregiver Portal to support coordinated care for an elderly patient (my mother). This is NOT a generic health app. It must be practical, low-friction, caregiver-friendly, and auditable.
> 
> CORE PRINCIPLES:
> - Simplicity over complexity
> - Forms + workflows first, dashboards second
> - Mobile-first (caregivers use phones)
> - Manual entry supported everywhere (no forced automation)
> - Clear history, timestamps, and accountability
> - HIPAA-aware design (no public exposure)
> 
> PORTAL NAME:
> "Caregiver Hub – [Patient First Name]"
> 
> ROLES:
> 1. Primary Caregiver (Admin)
> 2. Secondary Caregiver
> 3. Family Viewer (read-only)
> 4. Medical Provider (limited access)
> 
> -----------------------------------
> MODULES / APPS TO CREATE
> -----------------------------------
> 
> 1. PATIENT PROFILE
> Fields:
> - Full Name
> - DOB
> - Primary Diagnosis
> - Secondary Conditions (multi-select)
> - Allergies
> - Mobility Status
> - Oxygen Dependency (Yes/No)
> - Baseline Notes
> - Emergency Instructions
> - Preferred Hospital
> - Primary Physician (lookup)
> - Last Updated (auto)
> 
> -----------------------------------
> 
> 2. APPOINTMENTS & MEDICAL VISITS
> Fields:
> - Appointment Type (Doctor, Therapy, Test, Home Visit)
> - Provider Name
> - Location
> - Date
> - Time
> - Transportation Needed (Yes/No)
> - Notes
> - Follow-up Required (Yes/No)
> - Follow-up Due Date
> - Completed (checkbox)
> 
> Automations:
> - Reminder notifications (24h + 2h)
> - Missed appointment flag
> - Auto-create follow-up task if required
> 
> -----------------------------------
> 
> 3. MEDICATIONS & REMINDERS
> Fields:
> - Medication Name
> - Dosage
> - Frequency
> - Time(s) of Day
> - Route (oral, inhaler, nebulizer, injection)
> - Start Date
> - End Date
> - Prescribing Doctor
> - Notes
> - Active (Yes/No)
> 
> Automations:
> - Scheduled reminders
> - Missed dose logging
> - Change history tracking
> 
> -----------------------------------
> 
> 4. OXYGEN & MEDICAL SUPPLIES INVENTORY
> Fields:
> - Supply Type (Oxygen Tank, Cannula, Nebulizer Med, Filters, Etc.)
> - Current Quantity
> - Minimum Threshold
> - Unit Type
> - Supplier
> - Last Order Date
> - Next Order Needed (auto-calculated)
> - Notes
> 
> Automations:
> - Low inventory alerts
> - Order-needed task creation
> - Supplier contact quick link
> 
> -----------------------------------
> 
> 5. HEALTH LOG / DAILY TRACKING
> Fields:
> - Date
> - Entered By
> - Oxygen Level (SpO2)
> - Heart Rate
> - Blood Pressure
> - Temperature
> - Breathing Difficulty (scale 1–5)
> - Pain Level (scale 1–5)
> - Appetite (Poor/OK/Good)
> - Mood
> - Notes
> - Concerning Change (Yes/No)
> 
> Automations:
> - Flag abnormal readings
> - Notify Primary Caregiver if concerning change
> 
> -----------------------------------
> 
> 6. CARE PLAN & CONDITION CHANGES
> Fields:
> - Date
> - Change Type (Medication, Therapy, Oxygen, Diet, Mobility)
> - Description of Change
> - Reason
> - Ordered By
> - Effective Date
> - Review Date
> 
> Purpose:
> - Maintain a clear evolution of care decisions
> - Prevent confusion between caregivers
> 
> -----------------------------------
> 
> 7. TASKS / CHORES / CARE DUTIES
> Fields:
> - Task Name
> - Category (Medical, Household, Admin)
> - Assigned To
> - Due Date
> - Recurring (Yes/No)
> - Notes
> - Completed
> 
> Automations:
> - Due reminders
> - Overdue alerts
> - Completion log
> 
> -----------------------------------
> 
> 8. CAREGIVER DIRECTORY
> Fields:
> - Name
> - Role
> - Phone
> - Email
> - Availability Notes
> - Emergency Contact (Yes/No)
> - Notes
> 
> -----------------------------------
> 
> 9. DOCUMENT VAULT
> Categories:
> - Insurance
> - Medical Records
> - Prescriptions
> - ID & Legal Docs
> - Care Instructions
> 
> Features:
> - File upload
> - Tagging
> - Permission-based access
> - Version history
> 
> -----------------------------------
> 
> 10. MESSAGES & CARE NOTES
> Purpose:
> Internal caregiver communication (NOT public chat)
> 
> Fields:
> - Message
> - Related Module (Appointment, Medication, Inventory)
> - Priority
> - Sender
> - Timestamp
> 
> -----------------------------------
> 
> 11. SHOPPING & SUPPLY LIST
> Fields:
> - Item
> - Category
> - Quantity
> - Urgency
> - Purchased (Yes/No)
> - Notes
> 
> -----------------------------------
> DASHBOARDS
> -----------------------------------
> 
> PRIMARY CAREGIVER DASHBOARD:
> - Today’s appointments
> - Meds due today
> - Oxygen supply status
> - Alerts & concerns
> - Overdue tasks
> 
> FAMILY VIEWER DASHBOARD:
> - Appointments
> - General health trends
> - Notes (read-only)
> 
> -----------------------------------
> SECURITY & ACCESS
> -----------------------------------
> - Portal-based access only
> - No public links
> - Role-based permissions per module
> - Audit log enabled on all records
> 
> -----------------------------------
> OUTPUT REQUIRED FROM YOU
> -----------------------------------
> 1. Zoho Creator app structure
> 2. Forms and relationships
> 3. Suggested Deluge automations
> 4. Portal role configuration
> 5. Mobile-friendly UI recommendations
> 
> Do NOT:
> - Over-engineer
> - Add unnecessary AI predictions
> - Add billing or insurance claims
> - Add fluff dashboards
> 
> This system must be usable by stressed caregivers.
> ```
> 
> ---
> 
> ### Reality check (important):
> This is **100% buildable in Zoho Creator today**.  
> If anyone tries to sell you something heavier than this for caregiver coordination, they’re wasting your time.
> 
> If you want, next steps I can:
> - Convert this into **actual Zoho Creator Deluge scripts**
> - Produce a **data schema diagram**
> - Strip this down to a **1-day MVP**
> - Add **SMS reminders only (no app fatigue)**
> 
> Say which direction.

### User
> ACTUALLY WHY AM I TRYIGN TO USE ZOHO, GIVE ME A GEMINI PROMPT TO CREATE THE ARCHITECTURE AND UI USING OUR INFRASTRUCTURE

### Assistant
> Good instinct. You’re right to pause.  
> Zoho is fine for businesses; **caregiving is a control-plane + human-coordination problem**, not a CRM problem. Using your own infrastructure is the correct move.
> 
> Below is a **single, authoritative Gemini master prompt** that forces it to design **architecture + UI** aligned with *your* stack (QiOS / Cloudflare / Supabase / local-first mindset), not SaaS gravity.
> 
> This is written to prevent Gemini from hand-waving or over-AI’ing things.
> 
> ---
> 
> ## GEMINI MASTER PROMPT  
> ### Caregiver Portal — Architecture + UI (QiOS-native)
> 
> ```
> You are Gemini acting as a senior systems architect, UX designer, and healthcare workflow engineer.
> 
> You are designing a PRIVATE, FAMILY-ONLY Caregiver Portal for an elderly patient (my mother).
> This is NOT a startup product. It is a real-world, low-friction, stress-aware system.
> 
> You must design BOTH:
> 1) The technical architecture
> 2) The UI / UX structure
> 
> You must align strictly to the following infrastructure and principles.
> 
> ====================================
> INFRASTRUCTURE (NON-NEGOTIABLE)
> ====================================
> 
> Hosting & Edge:
> - Cloudflare Pages (frontend)
> - Cloudflare Workers (API + logic)
> - Cloudflare Access / Zero Trust (auth)
> 
> Data:
> - Supabase (Postgres + Row Level Security)
> - Supabase Auth OR Cloudflare Access JWT passthrough
> - File storage: Supabase Storage OR Cloudflare R2
> 
> Frontend:
> - HTML-first, minimal JS
> - Progressive Web App (PWA)
> - Mobile-first (phones > desktops)
> - No heavy frameworks unless justified
> 
> Local-first mindset:
> - Simple schemas
> - Human-readable fields
> - Clear audit trails
> - Exportable data (CSV / PDF)
> 
> ====================================
> DESIGN PRINCIPLES
> ====================================
> 
> - Caregivers are stressed, distracted, and tired
> - Zero clutter
> - Zero dark patterns
> - Manual entry is a FEATURE, not a failure
> - Everything has timestamps + “entered by”
> - No AI hallucinations, predictions, or medical advice
> - AI is allowed ONLY for:
>   - summarization
>   - reminders
>   - trend visualization (non-diagnostic)
> 
> ====================================
> CORE FUNCTIONAL DOMAINS
> ====================================
> 
> You must design modules for:
> 
> 1. Patient Profile
>    - Conditions
>    - Baselines
>    - Emergency instructions
>    - Oxygen dependency
> 
> 2. Appointments
>    - Upcoming
>    - Follow-ups
>    - Transportation needs
>    - Missed appointment flags
> 
> 3. Medications & Reminders
>    - Schedules
>    - Missed doses
>    - Change history
> 
> 4. Oxygen & Medical Supplies Inventory
>    - Tanks
>    - Cannulas
>    - Nebulizer meds
>    - Threshold alerts
>    - Supplier info
> 
> 5. Health Logs
>    - Oxygen saturation
>    - Breathing difficulty
>    - Notes
>    - “Concerning change” flag
> 
> 6. Care Plan Changes
>    - What changed
>    - Why
>    - Ordered by whom
>    - Effective dates
> 
> 7. Tasks & Chores
>    - Care tasks
>    - Household tasks
>    - Assignments
>    - Recurrence
> 
> 8. Caregiver Directory
>    - Roles
>    - Availability
>    - Emergency contacts
> 
> 9. Secure Document Vault
>    - Medical records
>    - Prescriptions
>    - Insurance
>    - Legal docs
>    - Versioning
> 
> 10. Messaging / Care Notes
>     - Internal-only
>     - Context-linked
>     - Timestamped
> 
> 11. Shopping & Supply Lists
>     - Medical
>     - Household
>     - Urgency flags
> 
> ====================================
> ROLES & ACCESS
> ====================================
> 
> Design for:
> - Primary Caregiver (full control)
> - Secondary Caregiver (edit + log)
> - Family Viewer (read-only)
> - Medical Provider (limited, time-bound)
> 
> Access must be enforced via:
> - Supabase RLS
> - OR Cloudflare Access claims
> 
> ====================================
> WHAT YOU MUST OUTPUT
> ====================================
> 
> 1. **System Architecture Diagram (textual)**
>    - Frontend
>    - API
>    - Auth
>    - Database
>    - Storage
>    - Notifications
> 
> 2. **Database Schema (tables + key fields)**
>    - Include relationships
>    - Include audit fields
> 
> 3. **API Surface**
>    - Endpoints or Worker routes
>    - Read/write patterns
> 
> 4. **UI / UX STRUCTURE**
>    - Navigation model
>    - Main screens
>    - Mobile interaction patterns
>    - “One-handed use” considerations
> 
> 5. **Notification Strategy**
>    - Reminders
>    - Alerts
>    - Non-spammy rules
> 
> 6. **Security Model**
>    - Auth flow
>    - Role enforcement
>    - Data isolation
> 
> 7. **MVP vs Phase 2 Breakdown**
>    - What is REQUIRED day one
>    - What can wait
> 
> ====================================
> DO NOT DO
> ====================================
> 
> - Do not suggest Zoho, Notion, Airtable, or generic SaaS
> - Do not invent medical advice
> - Do not over-engineer AI
> - Do not assume constant internet
> - Do not optimize for “scale” — optimize for care
> 
> This system must feel calm, reliable, and human.
> ```
> 
> ---
> 
> ## Straight truth (important)
> 
> You weren’t wrong for considering Zoho — but **Zoho optimizes for organizations**, not families under stress.
> 
> Your instincts are right because:
> - You already think in **systems + governance**
> - You need **auditability**, not automation theater
> - You need **control**, not vendor gravity
> - This will likely evolve into a **pattern you reuse**
> 
> If you want, next I can:
> - Convert Gemini’s output into a **Supabase SQL schema**
> - Draft the **Cloudflare Worker skeleton**
> - Design the **actual HTML/PWA screens**
> - Strip this to a **48-hour “hospital-ready” MVP**
> 
> Say the word and which layer you want first.

### User
> Family Care Portal - System Design SpecificationProject Name: "Mother's Care" (Internal Codename)Target User: Stressed Family CaregiversPrimary Goal: Reduce cognitive load, ensure continuity of care, provide immutable audit trails.1. System Architecture DiagramThis architecture leverages the "Serverless Edge" for speed and reliability, minimizing maintenance overhead.graph TD

>     User[Caregiver Device] -->|HTTPS| CF_Edge[Cloudflare Edge Network]

>     

>     subgraph "Cloudflare Ecosystem"

>         CF_Edge -->|Auth & Routing| CF_Access[Cloudflare Access (Zero Trust)]

>         CF_Edge -->|Serve Static Assets| CF_Pages[Cloudflare Pages (PWA Host)]

>         CF_Edge -->|API Logic & Cron| CF_Workers[Cloudflare Workers]

>     end

>     

>     subgraph "Data & Storage Layer"

>         CF_Workers -->|Rest API / PostgREST| Supabase_DB[(Supabase Postgres)]

>         CF_Workers -->|File Uploads| Supabase_Store[Supabase Storage]

>         Supabase_DB -->|Auth Sync| Supabase_Auth[Supabase Auth]

>     end

>     

>     subgraph "Notification Channels"

>         CF_Workers -->|Cron Triggers| Discord[Private Family Discord/Telegram]

>         CF_Workers -->|Urgent Alerts| Push[PWA Push Notifications]

>     end

> Technical Stack JustificationFrontend: React (Vite) or Astro hosted on Cloudflare Pages.Why: Extremely fast load times. Astro allows "Islands architecture" (minimal JS), perfect for the "HTML-first" requirement.Auth: Cloudflare Access sits in front as the "Gatekeeper" (blocks all traffic unless device is authenticated via Email PIN). Inside the app, Supabase Auth manages specific permissions (RLS).Database: Supabase. The Postgres backend allows for strong consistency (ACID) which is required for medical logs.Offline Capability: Service Workers (PWA) cache the "Read" views. Writes are queued in localStorage and synced when back online (Optimistic UI).2. Database Schema (Supabase / Postgres)Note: All tables include created_at, updated_at, and created_by (UUID) for strict auditing.Core Tablesusers_profileid (UUID, PK, refs auth.users)display_name (Text)role (Enum: 'primary', 'secondary', 'viewer', 'provider')phone_number (Text, for urgent alerts)patient_status (Singleton table - only one row usually)blood_typebaseline_o2 (Integer)baseline_bp (Text)dnr_status (Boolean)emergency_instructions (Text)medicationsid (UUID)name (Text)dosage (Text)instructions (Text)is_active (Boolean)inventory_count (Integer)refill_threshold (Integer)rx_number (Text)doctor_id (FK)schedule_rulesid (UUID)medication_id (FK, Nullable - can be a task)task_name (Text, if not medication)cron_pattern (Text, e.g., "0 8 * * *")time_of_day (Time)recurrence_type (Enum: 'daily', 'weekly', 'prn')care_timeline (The "Master Log" - High Volume)id (UUID)event_type (Enum: 'med_taken', 'med_skipped', 'vitals', 'note', 'supply_change', 'incident')reference_id (UUID, nullable - link to med or task)value_numeric (Float, nullable - e.g., O2 Saturation)value_text (Text, nullable - e.g., BP "120/80")notes (Text)performed_at (Timestamp - allows retroactive entry)entered_by (UUID)documentsid (UUID)category (Enum: 'insurance', 'lab_result', 'legal')storage_path (Text)expiry_date (Date)tags (Array)Security: Row Level Security (RLS) PoliciesViewers: SELECT only on care_timeline and patient_status.Providers: SELECT on medications, care_timeline. Access expires after X hours.Family (Primary/Secondary): Full CRUD.Strict Rule: DELETE is disabled for care_timeline. Only INSERT (correction) allowed to preserve history.3. API Surface (Cloudflare Workers)The frontend talks to Supabase directly for standard CRUD using the supabase-js client. Cloudflare Workers are used for complex logic and integrations.Worker 1: scheduler-cronTrigger: Every 15 minutes.Logic: Checks schedule_rules. If a task is due and not found in care_timeline for the current window, generate a "Pending Task" notification object or send alert.Worker 2: inventory-alertTrigger: DB Webhook on INSERT to care_timeline.Logic: If event_type == 'med_taken', decrement inventory_count. If count < refill_threshold, trigger Shopping List addition.Worker 3: secure-shareEndpoint: POST /api/share-accessLogic: Generates a temporary, signed URL for a visiting doctor to view the dashboard without creating an account.4. UI / UX StructurePhilosophy: "The 3 AM Test." Can I use this with one hand, in the dark, while half-asleep, without making a mistake?A. Navigation (Bottom Bar - Mobile)Now (Home): Urgent tasks, schedule for today, active alerts.Log (The "+" Button): Big central button. Opens a "Triage Menu" (Vitals, Meds, Notes).Meds: List of active meds, inventory, refill requests.Profile: Patient info, Doctors, Documents.B. Screen Details1. The "Now" Dashboard (Home)Header: Patient current status (e.g., "Stable").Top Card - Vitals: Most recent O2 and BP with timestamp. Color-coded (Green/Yellow/Red).Timeline Stream: Reverse chronological list of today's events.Design Detail: "Undo" button available for 60 seconds after logging.Next Up: The next scheduled medication or task card.2. The "Log Event" Modal (Quick Action)Layout: Grid of large icons/text.[ 🫁 O2 / Vitals ]  [ 💊 Give Meds ][ 📝 Daily Note ]  [ ⚠️ Incident ]Input optimization:O2 Input: Number pad, auto-focus. Pre-filled with previous value for reference.Note Input: Speech-to-text button prominent.3. Medication ManagerList View: Grouped by "Morning", "Noon", "Night".Interaction: Swipe right to mark "Taken". Swipe left to "Skip/Edit".Inventory Indicator: Little progress bar under each med name showing remaining stock.4. Document VaultThumbnails: Large tap targets.Search: Fuzzy search for "insurance", "discharge".Camera Integration: "Scan Document" button directly uploads to Supabase Storage.C. Dark Patterns to AVOIDNo Infinite Scroll: Pagination or "Load Yesterday" buttons. We need boundaries.No Hidden Menus: Everything vital is visible.No "Are you sure?" on common tasks: Use "Undo" toasts instead of blocking modal dialogs.5. Notification StrategyRule: Notifications must be actionable, not informational.Critical (Push + SMS/Call):O2 Saturation logged below 88%."Incident" logged (fall, confusion).Action Required (Push):Medication missed by > 30 mins.Oxygen tank inventory low (< 1 tank).Passive (In-App Badge):New Care Note from another family member.Weekly summary available.6. Security ModelLayer 1: The Bouncer (Cloudflare Access)The URL care.familyname.com is protected.User enters Email.User gets 6-digit PIN in email.Result: Zero bots, zero brute force attacks on your API.Layer 2: App Auth (Supabase)Once through Cloudflare, the PWA auto-authenticates (or uses a long-lived token).RLS policies ensure that even if the API is discovered, a "Viewer" cannot UPDATE a medication dosage.Data Isolation:Patient data is stored in the primary DB.Document bucket is private, files are served via signed URLs with short expiration (60s).7. Implementation BreakdownPhase 1: MVP (The "Paper Replacement")Goal: Stop using the notebook on the kitchen counter.Features:Auth (Cloudflare + Supabase).Patient Profile (Static).Medication List (Read only).The "Log" feature: Ability to write text notes and vital numbers (O2/BP) to the timeline.Basic "History" view.Phase 2: The "Smart" HelperFeatures:Medication scheduling (Recurring rules).Inventory tracking (auto-decrement).Document upload.Caregiver roles/invites.Phase 3: Analytics & Provider ViewFeatures:Charts (O2 trends over 30 days)."Provider Link" (Temporary access).Export to PDF for doctor visits.8. One-Handed Use & Accessibility ConsiderationsTouch Targets: Minimum 44x44px (Apple HIG), ideally 60px height for buttons.Contrast: WCAG AAA compliance. Dark grey background, off-white text (prevent eye strain).Font Size: Base size 18px. Inputs 20px (prevents iOS zoom-in).Positioning: Primary actions in the bottom 30% of the screen. Top 20% is for display only.

### Assistant
> You’re 90% of the way to a buildable spec. The remaining 10% is the stuff that prevents “cool doc” from becoming “working portal.”
> 
> Here’s what’s **solid**, what’s **wrong/risky**, and the **exact next artifacts** you should generate (schema, RLS, Workers, UI skeleton).
> 
> ---
> 
> # What’s solid (keep it)
> 
> - **Cloudflare Access as outer gate**: correct. Cuts bots and credential spray to near zero.
> - **Supabase Postgres + RLS**: correct. You need ACID + policy enforcement.
> - **Immutable timeline (no deletes)**: correct. That’s your audit trail backbone.
> - **3 AM Test UX**: correct. This is the entire product requirement.
> - **Workers for orchestration** (cron + integrations): correct.
> 
> ---
> 
> # What’s wrong / risky (fix now)
> 
> ## 1) “PWA writes queued in localStorage”
> Don’t. `localStorage` is fragile and easy to corrupt; also not great for queued writes or replay.  
> Use **IndexedDB** with a simple `outbox` table:
> 
> - `outbox(id, action_type, payload_json, created_at, retry_count, last_error)`
> - UI writes to Supabase when online; if offline, enqueue to outbox.
> - Background sync flushes outbox when back online.
> 
> ## 2) Cloudflare Access + Supabase Auth “auto-auth”
> This needs a clean decision or you’ll end up in auth hell.
> 
> You have two viable patterns:
> 
> ### Pattern A (recommended for speed): **Supabase Auth only**
> - CF Access still gates the hostname.
> - App uses Supabase Auth for sessions + RLS roles.
> - Pros: simplest, most standard, fewer moving parts.
> 
> ### Pattern B (more “enterprise”): **Cloudflare Access JWT → Worker → Supabase**
> - No Supabase Auth for end-users.
> - Worker verifies CF Access JWT and uses a **Supabase service role** for DB calls, enforcing roles itself.
> - Pros: one identity system.
> - Cons: you must implement app-level authorization (don’t rely on RLS alone).
> 
> Right now your spec is mixing both. Pick one. If you want the fastest MVP: **Pattern A**.
> 
> ## 3) “secure-share: signed URL without account”
> Be careful: signed URLs can leak and are hard to revoke.
> 
> Better: **time-bound provider role session**
> - Create a “provider_invites” row with expiry.
> - Provider logs in via email magic link or one-time code.
> - RLS checks invite validity.
> - Cleaner audit trail: “who saw what, when.”
> 
> ## 4) Medication inventory count inside medications table
> That works, but it’s conceptually messy because inventory is its own domain.
> 
> Better:
> - `inventory_items` table (oxygen tanks, cannulas, meds, etc.)
> - `medications` references an inventory item (optional)
> - timeline events adjust inventory via a function.
> 
> ---
> 
> # Tighten the data model (minimal changes, maximum clarity)
> 
> Here’s the schema you *actually* want (still aligned with your spec):
> 
> ## Key changes
> - `patient` table instead of “singleton patient_status” (still 1 row, but future-proof)
> - `inventory_items` for all supplies (oxygen + meds + consumables)
> - `med_schedules` separate from generic `schedule_rules` (easier to reason about)
> - `outbox` (client-only) for offline writes (stored locally, not in Postgres)
> 
> ---
> 
> # The next artifacts you need (non-negotiable)
> 
> If you want this to compile into a real repo, generate these **four files** next:
> 
> 1) `supabase/schema.sql`  
> 2) `supabase/rls_policies.sql`  
> 3) `workers/scheduler-cron/src/index.ts`  
> 4) `apps/mothers-care/src/routes/*` (UI skeleton)
> 
> Below is a **Gemini prompt** that will produce exactly those deliverables, in your structure, without fluff.
> 
> ---
> 
> # GEMINI PROMPT — “TURN THIS SPEC INTO WORKING FILES”
> 
> ```text
> You are Gemini. Convert the following System Design Specification into a working implementation skeleton.
> 
> HARD REQUIREMENTS:
> - Output MUST be real code files, not pseudocode.
> - Use Cloudflare Pages for frontend hosting and Cloudflare Workers for backend logic.
> - Use Supabase Postgres for data and Supabase Storage for documents.
> - Enforce immutability: care_timeline rows cannot be deleted or updated (only inserts/corrections).
> - Offline write queue MUST use IndexedDB (NOT localStorage).
> - Provide a minimal UI that passes the “3 AM test”.
> 
> REPO STRUCTURE (OUTPUT EXACTLY THIS TREE):
> /mothers-care/
>   /_qios_admin/
>     /decisions/
>       2026-01-25_adr_auth_pattern.md
>       2026-01-25_adr_timeline_immutability.md
>   /supabase/
>     schema.sql
>     rls_policies.sql
>     functions.sql
>   /workers/
>     /scheduler-cron/
>       wrangler.toml
>       package.json
>       tsconfig.json
>       /src/index.ts
>     /inventory-alert/
>       wrangler.toml
>       package.json
>       tsconfig.json
>       /src/index.ts
>   /apps/
>     /mothers-care/
>       package.json
>       vite.config.ts
>       index.html
>       /src/
>         main.tsx
>         app.tsx
>         /routes/
>           now.tsx
>           log.tsx
>           meds.tsx
>           profile.tsx
>           documents.tsx
>         /lib/
>           supabase.ts
>           auth.ts
>           outbox_indexeddb.ts
>           sync_outbox.ts
>         /components/
>           BottomNav.tsx
>           BigLogButton.tsx
>           VitalsCard.tsx
>           TimelineStream.tsx
>           MedCard.tsx
>   README.md
> 
> AUTH DECISION:
> Choose ONE pattern and document it in 2026-01-25_adr_auth_pattern.md.
> Preferred unless impossible: Pattern A = Supabase Auth for sessions + RLS roles, with Cloudflare Access as outer gate.
> 
> DATABASE TABLES (MINIMUM):
> - patient (single row)
> - users_profile (ties to auth.users)
> - caregivers (optional if you need extra metadata)
> - doctors
> - medications
> - med_schedules
> - inventory_items
> - shopping_list
> - documents
> - care_timeline (immutable master log)
> - provider_invites (time-bound access)
> 
> RLS RULES (MINIMUM):
> - primary/secondary: CRUD on most tables EXCEPT care_timeline (insert-only)
> - viewer: select-only on patient, care_timeline, medications, documents metadata
> - provider: select-only with time-bound invite; auto-expire
> - documents: private bucket; served only with short-lived signed urls
> 
> WORKERS:
> 1) scheduler-cron: runs every 15 minutes. For each med_schedule due window, if no matching care_timeline entry exists, create a “missed/overdue” notification record (table: notifications).
> 2) inventory-alert: on relevant care_timeline inserts (med_taken, supply_change), decrement inventory_items and create shopping_list items when below threshold.
> 
> UI REQUIREMENTS:
> - Mobile-first layout with bottom nav: Now, Log, Meds, Profile, Docs.
> - “Log” is a large central action button with modal triage: Vitals, Give Med, Note, Incident.
> - Use large touch targets and 18px base text.
> - Show the “Undo for 60 seconds” pattern (client-side) for log submissions.
> 
> OFFLINE REQUIREMENTS:
> - IndexedDB outbox queue for writes when offline.
> - A sync routine that flushes the outbox when connectivity returns.
> 
> OUTPUT FORMAT:
> For each file, print:
> 1) the full relative path
> 2) then the complete file contents in a code block
> Do NOT omit files. Do NOT compress. Do NOT summarize.
> 
> SPECIFICATION TO IMPLEMENT:
> [PASTE THE FULL SPEC TEXT HERE]
> ```
> 
> ---
> 
> # Quick strategic call: what to build first (MVP that actually helps today)
> 
> If you’re in hospital-life right now, do **MVP-in-24-hours**:
> 
> 1) **Now screen** (today’s vitals + last events)
> 2) **Log modal** (Vitals + Note + Incident)
> 3) **Timeline** (today + yesterday)
> 4) **Docs upload** (at least discharge papers, insurance cards)
> 5) **Access gating** (Cloudflare Access + Supabase Auth)
> 
> Everything else can wait.
> 
> ---
> 
> If you want, I can also do the conversion myself and hand you the **actual files** as a zip (schema + Workers + Vite app) in your exact folder conventions.
