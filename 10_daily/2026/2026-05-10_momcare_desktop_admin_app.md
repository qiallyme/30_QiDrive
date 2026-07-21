---
layout: page
title: "MomCare Desktop Admin App"
slug: "momcare_desktop_admin_app"
created_at: "2026-05-10 03:52:48"
updated_at: "2026-07-18T11:03:15-04:00"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-007.json"
template_key: master-template
date: 2026-05-10
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a0046f0-43dc-83ea-a00a-093fb6755696"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# MomCare Desktop Admin App

## Overview
- **Date**: 2026-05-10 03:52:48
- **Conversation ID**: `6a0046f0-43dc-83ea-a00a-093fb6755696`
- **Source**: `Chat-Export-28513-2026/conversations-007.json`

## Chat History

### User
> ok number one i need a desktop app version of momscare for my to use on my pc, and allowing me to update entries and stuff, and add new ones to, right now, the app is choking on the sher volume of things, one, i need to be able to go into the backend and very simply, realtime and fluidly, add med, inventory, take inventory count, bklklklklklklklklklklklklklklklklklklklklklklklklklklklklklklklklklklkl

### Assistant
> Yes. What you’re asking for is **not “more app features.”** It’s a **desktop operations console** for MomCare so you can manage the backend without the web app choking.
> 
> Here’s the clean direction:
> 
> ## What you actually need
> 
> ### 1. MomCare Desktop Admin App
> 
> A PC app for you only, focused on fast data entry and backend management.
> 
> Not pretty. Not public. Not patient-facing. Just **fluid control panel mode**.
> 
> Core modules:
> 
> - **Meds**
>   - Add medication
>   - Mark active/inactive
>   - Update dose/frequency
>   - Add location: pill basket, bottle, nebulizer box, fridge, etc.
>   - Add verification status: confirmed / needs verification / inactive
> 
> - **Inventory**
>   - Add item
>   - Count stock
>   - Update quantity fast
>   - Mark low supply
>   - Add location
>   - Add reorder threshold
> 
> - **Care Logs**
>   - Add breathing/O2 note
>   - Add pain note
>   - Add bathroom/diaper note
>   - Add transfer/fall-risk note
>   - Add general caregiver shift note
> 
> - **Quick Actions**
>   - “Med taken”
>   - “Inventory counted”
>   - “Need refill”
>   - “Need doctor/pharmacy verification”
>   - “Print current med list”
>   - “Print nurse handoff”
> 
> ## Best technical path
> 
> Use **Tauri + React + Supabase**.
> 
> Why?
> 
> - Runs as a real desktop app on Windows
> - Much lighter than Electron
> - Can reuse your current React/Supabase logic
> - Fast enough for admin tables
> - Can talk directly to Supabase
> - Can be packaged as a `.exe`
> - Keeps your existing web app alive but stops forcing it to do heavy admin work
> 
> Electron works too, but Tauri is cleaner and less bloated. Electron is the “big purse with bricks in it” option.
> 
> ## Immediate architecture
> 
> Keep the current MomCare app as:
> 
> > **MomCare Web App = daily caregiving UI**
> 
> Create a separate:
> 
> > **MomCare Desktop Admin = backend control console**
> 
> Do **not** cram this into the current choking app. That is how we make the spaghetti monster angrier.
> 
> ## Tables the desktop app should manage first
> 
> Minimum useful scope:
> 
> 1. `medications`
> 2. `medication_schedule`
> 3. `medication_administrations`
> 4. `inventory_items`
> 5. `inventory_counts`
> 6. `caregiver_notes`
> 7. `care_events`
> 8. `contacts_or_providers`
> 
> ## Inventory fields you need
> 
> For inventory, this is the shape:
> 
> | Field | Purpose |
> |---|---|
> | item_name | “Wipes”, “Dupixent”, “Nebulizer cups” |
> | category | meds, hygiene, oxygen, bedding, food, paperwork |
> | current_quantity | What you counted |
> | unit | tablets, boxes, bottles, packs, each |
> | reorder_threshold | When it becomes low |
> | location | bedside, bathroom, med basket, fridge |
> | status | okay, low, out, ordered |
> | last_counted_at | When you checked |
> | notes | Anything weird |
> 
> ## Medication fields you need
> 
> | Field | Purpose |
> |---|---|
> | name | Medication name |
> | strength | 20mg, 400mg, etc. |
> | form | tablet, inhaler, neb solution, injection |
> | route | oral, inhaled, topical, injection |
> | frequency | daily, BID, PRN, every 14 days |
> | active_status | active, inactive, needs verification |
> | location | bottle, pill organizer, fridge, nebulizer bin |
> | purpose | pain, breathing, BP, etc. |
> | risk_notes | sedation, breathing risk, dizziness, etc. |
> | verified_source | bottle, pharmacy list, discharge paper, doctor |
> | last_verified_at | Date confirmed |
> 
> ## What to tell Codex
> 
> Send Codex this:
> 
> ```text
> Build a separate Windows desktop admin app for the MomCare system using Tauri + React + TypeScript + Supabase.
> 
> Purpose:
> This is not the patient-facing daily care app. This is a private desktop backend operations console for Cody to quickly manage MomCare data when the main app is too slow or overloaded.
> 
> Core requirements:
> 1. Connect to the existing Supabase project using the existing environment variables.
> 2. Create a fast admin dashboard with sections:
>    - Medications
>    - Medication Schedule
>    - Medication Administrations
>    - Inventory Items
>    - Inventory Counts
>    - Caregiver Notes
>    - Care Events
> 3. Use table/grid views with:
>    - search
>    - filters
>    - inline edit where practical
>    - add new record
>    - edit existing record
>    - mark inactive/status changes
> 4. Prioritize speed and reliability over visual polish.
> 5. Use optimistic UI only where safe.
> 6. Add loading states, error states, and save confirmation.
> 7. Do not delete records by default. Use status/inactive fields unless a table already supports soft delete.
> 8. Add print/export buttons later, but scaffold the UI routes now.
> 
> Initial inventory fields needed:
> - id
> - item_name
> - category
> - current_quantity
> - unit
> - reorder_threshold
> - location
> - status
> - last_counted_at
> - notes
> - created_at
> - updated_at
> 
> Initial medication fields needed:
> - id
> - name
> - strength
> - form
> - route
> - frequency
> - active_status
> - location
> - purpose
> - risk_notes
> - verified_source
> - last_verified_at
> - notes
> - created_at
> - updated_at
> 
> Important:
> Do not break the current web app. This should be a separate desktop admin app folder/package, preferably apps/momcare-desktop-admin or similar.
> 
> Before writing migration SQL, inspect the existing Supabase schema and report what tables already exist, what columns are missing, and what migrations are needed.
> ```
> 
> ## What to do first
> 
> Do **not** start with a huge desktop app.
> 
> Start with this order:
> 
> 1. **Inventory admin**
> 2. **Medication admin**
> 3. **Caregiver notes**
> 4. **Print/export views**
> 5. **Trend reporting later**
> 
> The choking problem is probably from too much UI/state/data being loaded at once. So the desktop app should use **paged tables**, not “load the whole universe and pray.”
> 
> ## Clean requirement statement
> 
> Here’s the real spec:
> 
> > I need a local Windows desktop backend console for MomCare so I can quickly add, edit, count, verify, and organize medication, inventory, and care records without relying on the overloaded web app UI.
> 
> That’s the sentence. That’s the product. That’s the lane.

### User
> dont we need to tell codex to use teh same types so there ae not any database issues, also my mom needs to track her bow movements, urinations and we need a way to update her care schedule and care plan, so that way we can set repeating reminders and schedules, for her care with checklists for bed time, morning start, midday, meds review on sundays, etc.

### Assistant
> Yes. **Absolutely.** That is the missing piece. Codex needs to be told:
> 
> > Do not invent types. Do not hand-roll database shapes. Use the same Supabase-generated TypeScript types as the existing MomCare app.
> 
> Otherwise you get the classic dumb mess: one app thinks the column is `active_status`, another thinks it is `status`, another thinks it is `is_active`, and then everybody’s yelling at Postgres like it started the fight.
> 
> Here’s the upgraded Codex instruction.
> 
> ---
> 
> ## Updated Codex Prompt: MomCare Desktop Admin + Shared Types + Care Schedule
> 
> Tell Codex this:
> 
> ```text
> Build a separate Windows desktop admin app for the MomCare system using Tauri + React + TypeScript + Supabase.
> 
> This desktop app must use the SAME Supabase database, SAME schema, and SAME generated TypeScript database types as the existing MomCare web app.
> 
> Critical type requirement:
> 1. Do not hand-write table types.
> 2. Do not invent duplicate interfaces for Supabase rows.
> 3. Use the existing generated Supabase Database type if it already exists.
> 4. If no shared generated type exists, create one canonical generated type file from Supabase and import it in both apps.
> 5. Preferred location:
>    - packages/database/src/types/supabase.ts
>    - or src/lib/supabase/database.types.ts if this is not a monorepo yet.
> 6. All Supabase queries must be typed using the generated Database type.
> 7. Before adding migrations, inspect the current schema and report:
>    - existing tables
>    - existing columns
>    - missing columns
>    - duplicate/conflicting fields
>    - risky naming inconsistencies
> 8. Do not break the current web app.
> 
> Architecture:
> - Keep the current MomCare web app as the caregiver-facing daily app.
> - Create a separate private desktop admin console for Cody.
> - Suggested folder:
>   - apps/momcare-desktop-admin
> - The desktop app should connect to Supabase using existing environment variables.
> - It should share Supabase client setup/types where practical.
> 
> Desktop app modules:
> 1. Medications Admin
> 2. Inventory Admin
> 3. Bowel / Urination Tracking
> 4. Care Schedule / Repeating Reminders
> 5. Care Plan Management
> 6. Checklist Templates
> 7. Caregiver Notes
> 8. Printable / Exportable Views later
> 
> Primary goal:
> Give Cody a fast backend operations console to add, edit, verify, count, schedule, and document MomCare records without the main web app choking on heavy data volume.
> 
> Performance requirements:
> - Use paginated table views.
> - Do not load entire tables into memory.
> - Use search, filters, and status tabs.
> - Use optimistic UI only where safe.
> - Add loading, error, save-success, and unsaved-change states.
> - Prefer soft delete/status changes over destructive delete.
> ```
> 
> ---
> 
> ## Add Bathroom Tracking
> 
> This needs its own module. Do **not** bury it inside random notes.
> 
> Call it:
> 
> > **Elimination Log**
> 
> Professional enough for nurses. Clear enough for home care.
> 
> ### Tables / fields to support
> 
> ```text
> Elimination Log fields:
> - id
> - patient_id
> - event_type: bowel_movement | urination | both | attempted
> - occurred_at
> - amount: none | small | medium | large
> - bowel_consistency: hard | formed | soft | loose | diarrhea | unknown
> - urine_color: clear | pale | yellow | dark | cloudy | blood_seen | unknown
> - pain_or_burning: yes | no | unknown
> - accident_or_incontinence: yes | no
> - assistance_needed: none | setup | standby | hands_on | full_assist
> - location: toilet | bedside_commode | brief | bed | other
> - notes
> - created_by
> - created_at
> - updated_at
> ```
> 
> This matters because bowel/urination changes can signal dehydration, constipation, infection, medication side effects, mobility decline, or breathing strain from transfers. Not drama — actual care signal.
> 
> ---
> 
> ## Add Care Schedule / Repeating Reminders
> 
> This should be separate from one-time logs.
> 
> You need two layers:
> 
> ### 1. Care Schedule Templates
> 
> Examples:
> 
> - Morning Start
> - Midday Reset
> - Evening Reset
> - Bedtime Prep
> - Sunday Med Review
> - Linen Change
> - Inventory Count
> - Breathing Equipment Check
> - Dupixent Every 14 Days
> - Nurse Visit Prep
> - PT Prep
> 
> ### 2. Scheduled Care Tasks
> 
> Actual recurring instances generated from the template.
> 
> Fields:
> 
> ```text
> Care Schedule Template fields:
> - id
> - title
> - category: meds | hygiene | mobility | breathing | meals | inventory | admin | appointment_prep | bedtime | morning | other
> - description
> - default_time
> - recurrence_rule
> - priority: low | normal | high | critical
> - is_active
> - checklist_template_id
> - notes
> - created_at
> - updated_at
> ```
> 
> ```text
> Scheduled Care Task fields:
> - id
> - template_id
> - title
> - scheduled_for
> - due_window_start
> - due_window_end
> - status: pending | in_progress | completed | skipped | missed | rescheduled
> - completed_at
> - completed_by
> - skip_reason
> - notes
> - created_at
> - updated_at
> ```
> 
> Use `recurrence_rule` so it can handle daily, weekly, every 14 days, etc. Codex should not hard-code “every Sunday” logic everywhere like a menace.
> 
> ---
> 
> ## Add Checklist Templates
> 
> This is where bedtime/morning/midday lives.
> 
> ```text
> Checklist Template fields:
> - id
> - title
> - category
> - is_active
> - version
> - notes
> - created_at
> - updated_at
> ```
> 
> ```text
> Checklist Item fields:
> - id
> - checklist_template_id
> - label
> - description
> - sort_order
> - is_required
> - default_status
> - created_at
> - updated_at
> ```
> 
> ```text
> Checklist Completion fields:
> - id
> - scheduled_task_id
> - checklist_template_id
> - completed_by
> - completed_at
> - overall_status: complete | partial | skipped
> - notes
> - created_at
> ```
> 
> ```text
> Checklist Item Completion fields:
> - id
> - checklist_completion_id
> - checklist_item_id
> - status: done | skipped | not_needed | issue
> - notes
> - created_at
> ```
> 
> This gives you reusable checklists without rewriting the bedtime list 500 times.
> 
> ---
> 
> ## Care Plan Management
> 
> This is bigger than schedule. The care plan is the current operating doctrine.
> 
> You need a versioned care plan.
> 
> ```text
> Care Plan fields:
> - id
> - title
> - status: draft | active | archived
> - version
> - effective_date
> - summary
> - mobility_notes
> - breathing_notes
> - medication_notes
> - pain_notes
> - diet_hydration_notes
> - fall_risk_notes
> - cognitive_behavior_notes
> - caregiver_instructions
> - escalation_instructions
> - created_at
> - updated_at
> ```
> 
> Important rule:
> 
> > Only one care plan should be active at a time.
> 
> Codex should enforce that either in app logic or with a database constraint/function.
> 
> ---
> 
> ## Add This Safety Rule
> 
> Tell Codex:
> 
> ```text
> Medical safety rule:
> The app is for documentation, scheduling, and care coordination only. It must not recommend medication changes, dosing changes, or clinical decisions. Medication records should support verification status and notes, not automatic medical advice.
> ```
> 
> Very important. We are building a care ops system, not a rogue doctor in a trench coat.
> 
> ---
> 
> ## Better Build Order
> 
> Do it in this sequence:
> 
> 1. **Shared Supabase types**
> 2. **Schema inspection report**
> 3. **Inventory admin**
> 4. **Medication admin**
> 5. **Elimination log**
> 6. **Checklist templates**
> 7. **Care schedule templates**
> 8. **Scheduled care tasks / reminders**
> 9. **Care plan editor**
> 10. **Print/export**
> 
> Do **not** let Codex start with reminders first. That gets messy fast if the data model is not clean.
> 
> ---
> 
> ## Short version to paste at the top
> 
> Use this as the command header:
> 
> ```text
> Important: before building UI, first stabilize the database contract.
> 
> The desktop admin app must share the exact same Supabase-generated TypeScript Database types as the existing web app. Do not hand-write types or invent duplicate row interfaces. Inspect the current schema first, identify missing tables/columns, then propose migrations. After the database contract is clean, build the Tauri desktop admin console modules for medications, inventory, elimination logs, care schedule templates, repeating reminders, checklist templates, and care plan management.
> ```
> 
> That’s the move. You are not wrong — **shared types are non-negotiable** here. Otherwise we’re just building a second app to disagree with the first app faster.
