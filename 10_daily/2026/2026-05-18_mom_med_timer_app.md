---
layout: page
title: "Mom Med Timer App"
slug: "mom_med_timer_app"
created_at: "2026-05-18 09:48:45"
updated_at: "2026-05-18 09:48:45"
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
date: 2026-05-18
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a0b2586-cf30-83ea-b368-330dab9059c3"
canonical_ref: ""
---

# Mom Med Timer App

## Overview
- **Date**: 2026-05-18 09:48:45
- **Conversation ID**: `6a0b2586-cf30-83ea-b368-330dab9059c3`
- **Source**: `Chat-Export-28513-2026/conversations-007.json`

## Chat History

### User
> ok so i have been thinking im trying to make this care app with all this detail for my moms care, which is important and should definetely be built BUT right now its not helping her at all but there is one thing that she is doing that i think we can definetly build in a split second, and that is a kinda timer app with just what she needs or does now. So my mom does the following, take a breathing treatment she writes down the time and which med, then she estimates when its ok for her to do another one, since they are as needed all she is doing is making sure there is at least 3 hours between treaments and no more than 6 a day, but sometimes the max varies depending on the med but thats about the jist, then she sometimes writes down if she took her am meds and her pm meds, then she writes down the as needed meds as not to exceed the maximun allowed like tylenol to not od and she documents her morphin, so i think a simple list table, the name, type, amount, daily max, interval then we a usage table to enter when she takes them then the formula or function calculates the time to wait befoer next or it gets checked off as done and all my mom sees is like big buttons with the name and icon she clicks it then it will change to green and asay done or a timer stating wait time before another does and for med that have a meximum it will show how many mgs taking in the last 24 hours or a precentage

### Assistant
> You’re absolutely right to pivot. The huge care app matters, but this is the “actually helps Mom today” layer: fewer decisions, safer timing, less paper chaos.

### Assistant
> Yes. Build **this first**.
> 
> The full care app is the long-term system. This is the **daily safety layer**. It should be stupid-simple, big-button, low-friction, and useful immediately.
> 
> ## The app you actually need right now
> 
> Call it something like:
> 
> **Mom Med Timer**  
> or  
> **Today’s Care Buttons**  
> or  
> **Dose Guard**
> 
> Core idea:
> 
> > Mom taps a big button when she takes or does something.  
> > The app records the time, checks timing/max rules, and tells her whether she is safe to do it again.
> 
> That’s it. Do not overbuild this.
> 
> ---
> 
> # Core tables
> 
> ## 1. `care_action_rules`
> 
> This is the master list of things she can take or do.
> 
> Examples:
> 
> - Breathing treatment — Albuterol
> - Breathing treatment — DuoNeb
> - AM meds
> - PM meds
> - Tylenol
> - Morphine
> - Anxiety med
> - Cough medicine
> - Oxygen tank change
> - Nebulizer cleaning
> 
> Suggested fields:
> 
> ```sql
> create table if not exists care.care_action_rules (
>   id uuid primary key default gen_random_uuid(),
> 
>   patient_id uuid not null references care.patients(id),
> 
>   name text not null,
>   category text not null,
>   icon text,
> 
>   dose_amount numeric,
>   dose_unit text,
> 
>   min_interval_minutes integer,
>   max_uses_per_day integer,
>   max_amount_per_24h numeric,
> 
>   requires_confirmation boolean not null default true,
>   is_scheduled boolean not null default false,
> 
>   schedule_period text,
>   -- examples: 'AM', 'PM', 'BEDTIME', null
> 
>   active boolean not null default true,
> 
>   notes text,
>   metadata_json jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now()
> );
> ```
> 
> ---
> 
> ## 2. `care.care_action_logs`
> 
> This records every time she taps a button.
> 
> ```sql
> create table if not exists care.care_action_logs (
>   id uuid primary key default gen_random_uuid(),
> 
>   patient_id uuid not null references care.patients(id),
>   action_rule_id uuid not null references care.care_action_rules(id),
> 
>   taken_at timestamptz not null default now(),
> 
>   dose_amount numeric,
>   dose_unit text,
> 
>   status text not null default 'completed',
>   -- completed, skipped, corrected, voided
> 
>   notes text,
>   metadata_json jsonb not null default '{}'::jsonb,
> 
>   created_by text,
> 
>   created_at timestamptz not null default now()
> );
> ```
> 
> ---
> 
> # The logic
> 
> For each care action, the app calculates:
> 
> ## Next allowed time
> 
> ```text
> last_taken_at + min_interval_minutes
> ```
> 
> Example:
> 
> - Treatment at 9:00 AM
> - Minimum interval: 3 hours
> - Next allowed: 12:00 PM
> 
> Button shows:
> 
> ```text
> Wait 1h 42m
> ```
> 
> or:
> 
> ```text
> Available now
> ```
> 
> ---
> 
> ## Uses in last 24 hours
> 
> Count all logs for that action where:
> 
> ```text
> taken_at >= now() - interval '24 hours'
> ```
> 
> Example:
> 
> ```text
> 4 of 6 used
> ```
> 
> If she hits the max:
> 
> ```text
> Max reached
> ```
> 
> Button should lock or require override.
> 
> ---
> 
> ## Amount in last 24 hours
> 
> For meds like Tylenol:
> 
> ```text
> sum(dose_amount) in last 24 hours
> ```
> 
> Example:
> 
> ```text
> 2,000 / 3,000 mg
> ```
> 
> or:
> 
> ```text
> 67%
> ```
> 
> When near limit:
> 
> ```text
> Caution: 2,500 / 3,000 mg
> ```
> 
> At or over limit:
> 
> ```text
> Do not take more
> ```
> 
> ---
> 
> ## Scheduled checkoffs
> 
> For AM meds and PM meds, you do **not** need interval logic.
> 
> You need daily status:
> 
> ```text
> AM meds: Done today
> PM meds: Not done
> ```
> 
> Rule:
> 
> ```text
> If schedule_period = AM, check whether logged today between start of day and now.
> ```
> 
> Simple version:
> 
> - AM meds resets every day at midnight
> - PM meds resets every day at midnight
> 
> Later you can make “AM window” and “PM window,” but don’t start there.
> 
> ---
> 
> # UI she should see
> 
> Not a table.
> 
> Not admin.
> 
> Not medical chart nonsense.
> 
> She should see **huge cards/buttons**.
> 
> Example:
> 
> ```text
> Breathing Treatment
> Albuterol
> Available now
> [ Take Now ]
> ```
> 
> After she taps:
> 
> ```text
> Breathing Treatment
> Albuterol
> Done at 10:42 AM
> Next allowed at 1:42 PM
> ```
> 
> Another example:
> 
> ```text
> Tylenol
> 500 mg
> 1,500 / 3,000 mg used
> [ Take Now ]
> ```
> 
> Morphine:
> 
> ```text
> Morphine
> 5 mg
> Last taken: 8:15 AM
> Next allowed: 12:15 PM
> 2 of 6 used
> [ Take Now ]
> ```
> 
> AM meds:
> 
> ```text
> AM Meds
> Not done today
> [ Mark Done ]
> ```
> 
> After tapping:
> 
> ```text
> AM Meds
> Done at 9:04 AM
> ```
> 
> ---
> 
> # Status colors
> 
> Keep this painfully obvious:
> 
> | State | Meaning |
> |---|---|
> | Green | Available / done / safe |
> | Yellow | Caution / close to max |
> | Red | Too soon / max reached |
> | Gray | Inactive / not relevant |
> 
> Do not get clever. Color should scream the answer.
> 
> ---
> 
> # Minimum viable version
> 
> Build this in this order:
> 
> ## Phase 1 — Today screen
> 
> One screen:
> 
> ```text
> Today’s Care
> ```
> 
> Shows all active action rules as big cards.
> 
> Each card shows:
> 
> - Name
> - Dose
> - Last taken time
> - Next allowed time
> - Uses today / max
> - Amount last 24h / max
> - Big action button
> 
> ## Phase 2 — Tap to log
> 
> When she taps:
> 
> ```text
> Confirm: Mark Morphine 5mg taken now?
> [Cancel] [Confirm]
> ```
> 
> For low-risk things like AM meds, maybe one tap is fine.
> 
> For morphine/Tylenol/breathing treatments, require confirmation.
> 
> ## Phase 3 — Admin edit screen
> 
> You need a basic admin table where you can edit:
> 
> - Name
> - Category
> - Dose amount
> - Dose unit
> - Minimum interval
> - Max uses per day
> - Max amount per 24 hours
> - Active/inactive
> - Notes
> 
> This is where **you** configure the rules.
> 
> She never sees this unless needed.
> 
> ---
> 
> # Important safety note
> 
> Do **not** hardcode medical assumptions.
> 
> The app should not say:
> 
> ```text
> Safe to take
> ```
> 
> It should say:
> 
> ```text
> Available based on saved timing rules
> ```
> 
> That’s less legally/medically sketchy and more accurate.
> 
> Also, all intervals and max doses should be configurable because her doctor may change them.
> 
> ---
> 
> # Example seed data
> 
> Use your real patient ID.
> 
> ```sql
> insert into care.care_action_rules
> (patient_id, name, category, icon, dose_amount, dose_unit, min_interval_minutes, max_uses_per_day, max_amount_per_24h, is_scheduled, schedule_period, notes)
> values
> (
>   'PATIENT_ID_HERE',
>   'Albuterol Breathing Treatment',
>   'breathing_treatment',
>   'lungs',
>   1,
>   'treatment',
>   180,
>   6,
>   null,
>   false,
>   null,
>   'As-needed breathing treatment. Confirm actual max with care team.'
> ),
> (
>   'PATIENT_ID_HERE',
>   'AM Meds',
>   'scheduled_meds',
>   'sunrise',
>   null,
>   null,
>   null,
>   1,
>   null,
>   true,
>   'AM',
>   'Daily morning medications.'
> ),
> (
>   'PATIENT_ID_HERE',
>   'PM Meds',
>   'scheduled_meds',
>   'moon',
>   null,
>   null,
>   null,
>   1,
>   null,
>   true,
>   'PM',
>   'Daily evening medications.'
> ),
> (
>   'PATIENT_ID_HERE',
>   'Tylenol',
>   'as_needed_med',
>   'pill',
>   500,
>   'mg',
>   null,
>   null,
>   3000,
>   false,
>   null,
>   'Track total acetaminophen in last 24 hours. Verify max dose with care team.'
> ),
> (
>   'PATIENT_ID_HERE',
>   'Morphine',
>   'as_needed_med',
>   'shield-alert',
>   5,
>   'mg',
>   240,
>   6,
>   null,
>   false,
>   null,
>   'PRN medication. Verify interval and daily max with prescription instructions.'
> );
> ```
> 
> ---
> 
> # The view/query you’ll want
> 
> You want the app to calculate status from logs.
> 
> Conceptually:
> 
> ```sql
> select
>   r.id,
>   r.name,
>   r.category,
>   r.icon,
>   r.dose_amount,
>   r.dose_unit,
>   r.min_interval_minutes,
>   r.max_uses_per_day,
>   r.max_amount_per_24h,
> 
>   max(l.taken_at) as last_taken_at,
> 
>   count(l.id) filter (
>     where l.taken_at >= now() - interval '24 hours'
>   ) as uses_last_24h,
> 
>   coalesce(sum(l.dose_amount) filter (
>     where l.taken_at >= now() - interval '24 hours'
>   ), 0) as amount_last_24h
> 
> from care.care_action_rules r
> left join care.care_action_logs l
>   on l.action_rule_id = r.id
>   and l.status = 'completed'
> 
> where r.active = true
> 
> group by r.id
> 
> order by
>   r.category,
>   r.name;
> ```
> 
> Codex can turn that into either:
> 
> - a Supabase query with computed logic in TypeScript, or
> - a SQL view like `care.v_care_action_status`.
> 
> I’d prefer a SQL view plus frontend display logic.
> 
> ---
> 
> # Codex prompt
> 
> Copy/paste this:
> 
> ```text
> We need to add a simple “Today Care Timer” feature to the existing Mom Care App.
> 
> Goal:
> Create a low-friction screen for the patient/caregiver to log PRN meds, breathing treatments, and scheduled AM/PM meds. This is a safety/timing helper, not a full medication administration system.
> 
> Requirements:
> 
> 1. Add or use these Supabase tables in the care schema:
> 
> - care_action_rules
> - care_action_logs
> 
> care_action_rules should store:
> - id uuid primary key default gen_random_uuid()
> - patient_id uuid references care.patients(id)
> - name text
> - category text
> - icon text nullable
> - dose_amount numeric nullable
> - dose_unit text nullable
> - min_interval_minutes integer nullable
> - max_uses_per_day integer nullable
> - max_amount_per_24h numeric nullable
> - requires_confirmation boolean default true
> - is_scheduled boolean default false
> - schedule_period text nullable, examples: AM, PM, BEDTIME
> - active boolean default true
> - notes text nullable
> - metadata_json jsonb default '{}'
> - created_at timestamptz default now()
> - updated_at timestamptz default now()
> 
> care_action_logs should store:
> - id uuid primary key default gen_random_uuid()
> - patient_id uuid references care.patients(id)
> - action_rule_id uuid references care.care_action_rules(id)
> - taken_at timestamptz default now()
> - dose_amount numeric nullable
> - dose_unit text nullable
> - status text default 'completed'
> - notes text nullable
> - metadata_json jsonb default '{}'
> - created_by text nullable
> - created_at timestamptz default now()
> 
> 2. Create a Today Care Timer page.
> 
> Route suggestion:
> /admin/today-care
> or
> /care/today
> 
> This page should show active care_action_rules as large cards/buttons, not a dense table.
> 
> Each card should show:
> - action name
> - category
> - dose amount/unit if present
> - last taken time
> - next allowed time if min_interval_minutes exists
> - countdown/wait time if too soon
> - uses in last 24 hours vs max_uses_per_day if configured
> - amount in last 24 hours vs max_amount_per_24h if configured
> - clear status state:
>   - green/available
>   - yellow/caution
>   - red/too soon or max reached
>   - gray/inactive/not applicable
> 
> 3. Button behavior:
> 
> Each card should have a primary button:
> - “Take Now”
> - “Mark Done”
> - or disabled/warning state when max reached or too soon
> 
> When clicked:
> - If requires_confirmation is true, show confirmation modal:
>   “Confirm: Mark [name] [dose] as taken now?”
> - On confirm, insert a row into care.care_action_logs using the rule’s default dose_amount and dose_unit.
> - Refresh the status immediately.
> 
> 4. Timing logic:
> 
> For each rule:
> - last_taken_at = most recent completed log
> - next_allowed_at = last_taken_at + min_interval_minutes
> - too_soon = now < next_allowed_at
> - uses_last_24h = completed logs where taken_at >= now - 24 hours
> - amount_last_24h = sum(dose_amount) where taken_at >= now - 24 hours
> - max_reached = uses_last_24h >= max_uses_per_day OR amount_last_24h >= max_amount_per_24h
> 
> For scheduled meds:
> - if is_scheduled = true and schedule_period is AM or PM, show whether there is a completed log today.
> - If logged today, show “Done today” and the time.
> - If not logged today, show “Not done today.”
> 
> 5. Admin management:
> 
> Add a simple admin page or section to create/edit care_action_rules.
> It can be a basic table + form.
> Fields:
> - name
> - category
> - icon
> - dose_amount
> - dose_unit
> - min_interval_minutes
> - max_uses_per_day
> - max_amount_per_24h
> - requires_confirmation
> - is_scheduled
> - schedule_period
> - active
> - notes
> 
> This admin screen is for Cody/caregiver setup only. The patient-facing Today Care Timer should remain extremely simple.
> 
> 6. Safety language:
> 
> Do not display “safe to take.”
> Use wording like:
> - “Available based on saved timing rules”
> - “Wait before next dose”
> - “Daily limit reached based on saved rules”
> - “Confirm with prescription/care team for actual limits”
> 
> 7. UX priorities:
> 
> - Big buttons
> - Minimal text
> - Mobile-friendly
> - Clear colors
> - Easy for an older patient to use
> - No dense medical chart layout
> - No complicated event system
> - This should be separate from the larger care plan UI
> 
> 8. Please update TypeScript/Supabase types as needed.
> Use existing project patterns, components, routing, auth, and Supabase client conventions.
> Do not break existing care app tables or event views.
> Add this as a small standalone feature.
> ```
> 
> ---
> 
> # My blunt take
> 
> This is the right move.
> 
> The big care app is your **system of record**.
> 
> This timer is the **system of action**.
> 
> Your mom does not need a beautiful database right now. She needs a button that says:
> 
> ```text
> Morphine
> Last: 8:15 AM
> Wait 1h 20m
> ```
> 
> That’s the win. Build this first, then let the big care app ingest or display the logs later.

### User
> she is also tracking when she poops or pees and how many prenizone she is taking, and lets track her powerade intake she loves that stuff, then an super easy way to enter a quicknote to the usage or events table. now i think we basically have all these tables already but I almost rather make this the carelite schema on its own just to keep it clean.

### Assistant
> Yep — make this its own `carelite` layer. Don’t pollute the bigger care schema while you’re still discovering the real daily workflow. This is exactly where a clean “operational capture” schema shines.

### Assistant
> Yes. I’d split it.
> 
> Your existing `care` schema is becoming the **clinical/care-record system**.
> 
> This new thing should be:
> 
> > **`carelite` = fast daily tracking, big buttons, timers, intake/output, quick notes.**
> 
> It can later sync, map, or roll up into the main `care` schema, but right now the priority is speed, clarity, and zero schema anxiety.
> 
> ---
> 
> # What CareLite should track
> 
> You now have these daily capture categories:
> 
> | Thing | Type | Needs timer/max? |
> |---|---|---|
> | Breathing treatments | Medication/action | Yes: interval + max/day |
> | PRN meds | Medication/action | Yes: interval, max/day, max amount |
> | Morphine | Medication/action | Yes, extra important |
> | Tylenol | Medication/action | Yes, amount max |
> | Prednisone | Medication/scheduled variable dose | Track quantity/dose |
> | AM meds | Daily checklist | Once/day |
> | PM meds | Daily checklist | Once/day |
> | Pee | Body event | Count/time/note |
> | Poop | Body event | Count/time/quality/note |
> | Powerade | Intake | Amount/time |
> | Quick note | General event | Note only |
> 
> That’s a very coherent mini-app.
> 
> ---
> 
> # Better schema name
> 
> Use:
> 
> ```sql
> carelite
> ```
> 
> Clean, obvious, and separate.
> 
> ---
> 
> # CareLite core design
> 
> You only need three main tables:
> 
> ## 1. `carelite.items`
> 
> This defines the buttons/options.
> 
> Examples:
> 
> - Albuterol treatment
> - Morphine
> - Tylenol
> - Prednisone
> - AM meds
> - PM meds
> - Pee
> - Poop
> - Powerade
> - Quick Note
> 
> ## 2. `carelite.entries`
> 
> This records every tap/log.
> 
> Examples:
> 
> - Mom took morphine at 8:15 AM
> - Mom peed at 10:02 AM
> - Mom drank 12 oz Powerade
> - Mom took 3 prednisone tablets
> - Mom wrote a note
> 
> ## 3. `carelite.daily_summary_view`
> 
> This calculates what happened today / last 24 hours.
> 
> That’s enough.
> 
> Don’t make 14 tables. That’s how this gets stupid again.
> 
> ---
> 
> # Suggested SQL
> 
> ## Create schema
> 
> ```sql
> create schema if not exists carelite;
> ```
> 
> ---
> 
> ## `carelite.items`
> 
> ```sql
> create table if not exists carelite.items (
>   id uuid primary key default gen_random_uuid(),
> 
>   patient_id uuid not null references care.patients(id),
> 
>   name text not null,
>   item_type text not null,
>   -- examples:
>   -- med
>   -- treatment
>   -- scheduled_check
>   -- body_event
>   -- intake
>   -- note
> 
>   category text,
>   -- examples:
>   -- breathing
>   -- pain
>   -- steroid
>   -- bathroom
>   -- hydration
>   -- general
> 
>   icon text,
>   color text,
> 
>   default_amount numeric,
>   default_unit text,
>   -- examples:
>   -- 5 mg
>   -- 500 mg
>   -- 1 treatment
>   -- 12 oz
>   -- 1 tablet
> 
>   min_interval_minutes integer,
>   max_uses_per_24h integer,
>   max_amount_per_24h numeric,
> 
>   is_scheduled boolean not null default false,
>   schedule_period text,
>   -- AM, PM, BEDTIME, DAILY
> 
>   requires_confirmation boolean not null default false,
>   allow_note boolean not null default true,
>   active boolean not null default true,
> 
>   sort_order integer not null default 100,
> 
>   notes text,
>   metadata_json jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now()
> );
> ```
> 
> ---
> 
> ## `carelite.entries`
> 
> ```sql
> create table if not exists carelite.entries (
>   id uuid primary key default gen_random_uuid(),
> 
>   patient_id uuid not null references care.patients(id),
>   item_id uuid references carelite.items(id),
> 
>   entry_type text not null,
>   -- should usually copy item_type:
>   -- med
>   -- treatment
>   -- scheduled_check
>   -- body_event
>   -- intake
>   -- note
> 
>   occurred_at timestamptz not null default now(),
> 
>   amount numeric,
>   unit text,
> 
>   status text not null default 'completed',
>   -- completed
>   -- skipped
>   -- corrected
>   -- voided
> 
>   note text,
> 
>   metadata_json jsonb not null default '{}'::jsonb,
> 
>   created_by text,
>   created_at timestamptz not null default now()
> );
> ```
> 
> ---
> 
> # Why this works
> 
> For meds/treatments:
> 
> ```text
> item = Morphine
> entry = took 5 mg at 8:15 AM
> ```
> 
> For pee:
> 
> ```text
> item = Pee
> entry = peed at 10:04 AM
> ```
> 
> For poop:
> 
> ```text
> item = Poop
> entry = pooped at 11:20 AM, note: loose
> ```
> 
> For Powerade:
> 
> ```text
> item = Powerade
> entry = drank 12 oz at 2:15 PM
> ```
> 
> For prednisone:
> 
> ```text
> item = Prednisone
> entry = took 3 tablets at 9:00 AM
> ```
> 
> For quick note:
> 
> ```text
> item = Quick Note
> entry = note at 4:30 PM: coughing more after walking
> ```
> 
> Simple. Flexible. Not fragile.
> 
> ---
> 
> # Add useful indexes
> 
> ```sql
> create index if not exists idx_carelite_items_patient_active
> on carelite.items(patient_id, active);
> 
> create index if not exists idx_carelite_entries_patient_occurred
> on carelite.entries(patient_id, occurred_at desc);
> 
> create index if not exists idx_carelite_entries_item_occurred
> on carelite.entries(item_id, occurred_at desc);
> 
> create index if not exists idx_carelite_entries_type_occurred
> on carelite.entries(entry_type, occurred_at desc);
> ```
> 
> ---
> 
> # Status view
> 
> This gives the app everything it needs for the big-button screen.
> 
> ```sql
> create or replace view carelite.v_item_status as
> select
>   i.id,
>   i.patient_id,
>   i.name,
>   i.item_type,
>   i.category,
>   i.icon,
>   i.color,
>   i.default_amount,
>   i.default_unit,
>   i.min_interval_minutes,
>   i.max_uses_per_24h,
>   i.max_amount_per_24h,
>   i.is_scheduled,
>   i.schedule_period,
>   i.requires_confirmation,
>   i.allow_note,
>   i.sort_order,
>   i.active,
> 
>   max(e.occurred_at) filter (
>     where e.status = 'completed'
>   ) as last_occurred_at,
> 
>   count(e.id) filter (
>     where e.status = 'completed'
>       and e.occurred_at >= now() - interval '24 hours'
>   ) as uses_last_24h,
> 
>   coalesce(sum(e.amount) filter (
>     where e.status = 'completed'
>       and e.occurred_at >= now() - interval '24 hours'
>   ), 0) as amount_last_24h,
> 
>   count(e.id) filter (
>     where e.status = 'completed'
>       and e.occurred_at >= date_trunc('day', now())
>   ) as uses_today,
> 
>   coalesce(sum(e.amount) filter (
>     where e.status = 'completed'
>       and e.occurred_at >= date_trunc('day', now())
>   ), 0) as amount_today
> 
> from carelite.items i
> left join carelite.entries e
>   on e.item_id = i.id
> where i.active = true
> group by i.id;
> ```
> 
> ---
> 
> # Seed items
> 
> Replace `PATIENT_ID_HERE`.
> 
> ```sql
> insert into carelite.items
> (patient_id, name, item_type, category, icon, default_amount, default_unit, min_interval_minutes, max_uses_per_24h, max_amount_per_24h, is_scheduled, schedule_period, requires_confirmation, sort_order, notes)
> values
> 
> (
>   'PATIENT_ID_HERE',
>   'Breathing Treatment',
>   'treatment',
>   'breathing',
>   'lungs',
>   1,
>   'treatment',
>   180,
>   6,
>   null,
>   false,
>   null,
>   true,
>   10,
>   'PRN breathing treatment. Confirm med-specific rules with prescription/care team.'
> ),
> 
> (
>   'PATIENT_ID_HERE',
>   'AM Meds',
>   'scheduled_check',
>   'daily_meds',
>   'sunrise',
>   1,
>   'set',
>   null,
>   1,
>   null,
>   true,
>   'AM',
>   false,
>   20,
>   'Daily morning medication checkoff.'
> ),
> 
> (
>   'PATIENT_ID_HERE',
>   'PM Meds',
>   'scheduled_check',
>   'daily_meds',
>   'moon',
>   1,
>   'set',
>   null,
>   1,
>   null,
>   true,
>   'PM',
>   false,
>   30,
>   'Daily evening medication checkoff.'
> ),
> 
> (
>   'PATIENT_ID_HERE',
>   'Prednisone',
>   'med',
>   'steroid',
>   'pill',
>   1,
>   'tablet',
>   null,
>   null,
>   null,
>   false,
>   null,
>   true,
>   40,
>   'Track number of prednisone tablets taken.'
> ),
> 
> (
>   'PATIENT_ID_HERE',
>   'Tylenol',
>   'med',
>   'pain',
>   'pill',
>   500,
>   'mg',
>   null,
>   null,
>   3000,
>   false,
>   null,
>   true,
>   50,
>   'Track acetaminophen amount in rolling 24 hours. Confirm max with care team.'
> ),
> 
> (
>   'PATIENT_ID_HERE',
>   'Morphine',
>   'med',
>   'pain',
>   'shield-alert',
>   5,
>   'mg',
>   240,
>   6,
>   null,
>   false,
>   null,
>   true,
>   60,
>   'PRN morphine. Confirm interval and max with prescription/care team.'
> ),
> 
> (
>   'PATIENT_ID_HERE',
>   'Pee',
>   'body_event',
>   'bathroom',
>   'droplets',
>   1,
>   'time',
>   null,
>   null,
>   null,
>   false,
>   null,
>   false,
>   70,
>   'Track urination events.'
> ),
> 
> (
>   'PATIENT_ID_HERE',
>   'Poop',
>   'body_event',
>   'bathroom',
>   'toilet',
>   1,
>   'time',
>   null,
>   null,
>   null,
>   false,
>   null,
>   false,
>   80,
>   'Track bowel movements. Use notes for loose, hard, normal, constipation, etc.'
> ),
> 
> (
>   'PATIENT_ID_HERE',
>   'Powerade',
>   'intake',
>   'hydration',
>   'cup-soda',
>   12,
>   'oz',
>   null,
>   null,
>   null,
>   false,
>   null,
>   false,
>   90,
>   'Track Powerade intake.'
> ),
> 
> (
>   'PATIENT_ID_HERE',
>   'Quick Note',
>   'note',
>   'general',
>   'sticky-note',
>   null,
>   null,
>   null,
>   null,
>   null,
>   false,
>   null,
>   false,
>   100,
>   'Fast note capture.'
> );
> ```
> 
> ---
> 
> # UI layout
> 
> The main screen should have sections:
> 
> ```text
> Today
> ```
> 
> ## Top row: urgent/action meds
> 
> - Breathing Treatment
> - Morphine
> - Tylenol
> - Prednisone
> 
> ## Daily checkoffs
> 
> - AM Meds
> - PM Meds
> 
> ## Bathroom
> 
> - Pee
> - Poop
> 
> ## Intake
> 
> - Powerade
> 
> ## Notes
> 
> - Quick Note
> 
> Each one is a big button/card.
> 
> ---
> 
> # What each button does
> 
> ## Breathing treatment
> 
> Tap → confirm → logs:
> 
> ```text
> 1 treatment now
> ```
> 
> Shows:
> 
> ```text
> Last: 10:42 AM
> Next: 1:42 PM
> Used: 2 / 6
> ```
> 
> ---
> 
> ## Prednisone
> 
> This one needs a tiny amount selector.
> 
> Tap Prednisone → modal:
> 
> ```text
> How many tablets?
> [-] 1 [+]
> [Save]
> ```
> 
> Because prednisone tapers change. Hardcoding one dose is how you end up with bad data.
> 
> ---
> 
> ## Powerade
> 
> Same idea:
> 
> ```text
> How much?
> [8 oz] [12 oz] [16 oz] [20 oz]
> [Custom]
> ```
> 
> Default to 12 oz because that’s probably close enough.
> 
> ---
> 
> ## Poop
> 
> Tap → quick options:
> 
> ```text
> Poop
> [Normal] [Loose] [Hard] [Tiny] [Constipated]
> Optional note
> [Save]
> ```
> 
> Store the selected option in `metadata_json`, like:
> 
> ```json
> {
>   "stool_type": "loose"
> }
> ```
> 
> Do not overbuild Bristol stool chart right now unless you want to scare everyone with poop science.
> 
> ---
> 
> ## Pee
> 
> Tap → log immediately.
> 
> Optional modal only if you want:
> 
> ```text
> Pee
> [Normal] [Dark] [Low amount] [Burning]
> ```
> 
> But for MVP, just log the time.
> 
> ---
> 
> ## Quick Note
> 
> Tap → text box:
> 
> ```text
> What happened?
> ```
> 
> Save to `carelite.entries.note`.
> 
> This becomes your universal “oh shit, remember this” button.
> 
> ---
> 
> # Strong recommendation
> 
> Do **not** make separate tables for pee, poop, Powerade, prednisone, notes, etc.
> 
> That feels cleaner at first, but it is worse for the app.
> 
> You want one universal log table because the UI is one universal behavior:
> 
> > Something happened at this time, with optional amount and note.
> 
> That’s the model.
> 
> ---
> 
> # Codex prompt
> 
> Copy this:
> 
> ```text
> Add a new lightweight daily tracking feature called CareLite.
> 
> Goal:
> Create a separate carelite schema and a simple UI for fast daily tracking for Mom. This should not disturb the existing care schema or existing care app features. CareLite is a low-friction operational capture layer: big buttons, quick logs, timers, daily checkoffs, bathroom tracking, intake tracking, and notes.
> 
> Database requirements:
> 
> 1. Create schema:
> carelite
> 
> 2. Create table carelite.items:
> - id uuid primary key default gen_random_uuid()
> - patient_id uuid not null references care.patients(id)
> - name text not null
> - item_type text not null
>   examples: med, treatment, scheduled_check, body_event, intake, note
> - category text nullable
>   examples: breathing, pain, steroid, bathroom, hydration, general, daily_meds
> - icon text nullable
> - color text nullable
> - default_amount numeric nullable
> - default_unit text nullable
> - min_interval_minutes integer nullable
> - max_uses_per_24h integer nullable
> - max_amount_per_24h numeric nullable
> - is_scheduled boolean not null default false
> - schedule_period text nullable
>   examples: AM, PM, BEDTIME, DAILY
> - requires_confirmation boolean not null default false
> - allow_note boolean not null default true
> - active boolean not null default true
> - sort_order integer not null default 100
> - notes text nullable
> - metadata_json jsonb not null default '{}'
> - created_at timestamptz not null default now()
> - updated_at timestamptz not null default now()
> 
> 3. Create table carelite.entries:
> - id uuid primary key default gen_random_uuid()
> - patient_id uuid not null references care.patients(id)
> - item_id uuid references carelite.items(id)
> - entry_type text not null
>   examples: med, treatment, scheduled_check, body_event, intake, note
> - occurred_at timestamptz not null default now()
> - amount numeric nullable
> - unit text nullable
> - status text not null default 'completed'
>   examples: completed, skipped, corrected, voided
> - note text nullable
> - metadata_json jsonb not null default '{}'
> - created_by text nullable
> - created_at timestamptz not null default now()
> 
> 4. Add indexes:
> - carelite.items(patient_id, active)
> - carelite.entries(patient_id, occurred_at desc)
> - carelite.entries(item_id, occurred_at desc)
> - carelite.entries(entry_type, occurred_at desc)
> 
> 5. Create a view carelite.v_item_status that returns one row per active item with:
> - item fields
> - last_occurred_at
> - uses_last_24h
> - amount_last_24h
> - uses_today
> - amount_today
> 
> Use completed entries only for the calculations.
> 
> 6. Create seed items for the current patient:
> - Breathing Treatment
>   type: treatment
>   category: breathing
>   default amount: 1 treatment
>   min interval: 180 minutes
>   max uses per 24h: 6
>   requires confirmation: true
> 
> - AM Meds
>   type: scheduled_check
>   category: daily_meds
>   default amount: 1 set
>   is_scheduled: true
>   schedule_period: AM
>   max uses per 24h: 1
>   requires confirmation: false
> 
> - PM Meds
>   type: scheduled_check
>   category: daily_meds
>   default amount: 1 set
>   is_scheduled: true
>   schedule_period: PM
>   max uses per 24h: 1
>   requires confirmation: false
> 
> - Prednisone
>   type: med
>   category: steroid
>   default amount: 1 tablet
>   requires confirmation: true
>   notes: Track number of prednisone tablets taken.
> 
> - Tylenol
>   type: med
>   category: pain
>   default amount: 500 mg
>   max_amount_per_24h: 3000
>   requires confirmation: true
>   notes: Track acetaminophen amount in rolling 24 hours. Confirm actual max with care team.
> 
> - Morphine
>   type: med
>   category: pain
>   default amount: 5 mg
>   min_interval_minutes: 240
>   max_uses_per_24h: 6
>   requires confirmation: true
>   notes: PRN medication. Confirm interval/max with prescription instructions.
> 
> - Pee
>   type: body_event
>   category: bathroom
>   default amount: 1 time
>   requires confirmation: false
> 
> - Poop
>   type: body_event
>   category: bathroom
>   default amount: 1 time
>   requires confirmation: false
>   allow note: true
> 
> - Powerade
>   type: intake
>   category: hydration
>   default amount: 12 oz
>   requires confirmation: false
> 
> - Quick Note
>   type: note
>   category: general
>   allow note: true
>   requires confirmation: false
> 
> Frontend requirements:
> 
> 1. Add a CareLite page.
> Suggested route:
> /carelite
> or
> /admin/carelite
> 
> 2. Main UI:
> A mobile-friendly page with large button cards grouped into:
> - Priority Meds / Treatments
> - Daily Meds
> - Bathroom
> - Intake
> - Notes
> 
> 3. Each card should show:
> - name
> - amount/unit if relevant
> - last logged time
> - next allowed time if min_interval_minutes exists
> - wait countdown if too soon
> - uses_last_24h / max_uses_per_24h if max exists
> - amount_last_24h / max_amount_per_24h if max exists
> - uses_today for body events/intake
> - clear status color:
>   green = available/done/okay based on saved rule
>   yellow = caution/near limit
>   red = too soon or limit reached
>   gray = inactive/not applicable
> 
> 4. Logging behavior:
> When a user taps a card:
> - For normal quick items like Pee, log immediately.
> - For requires_confirmation items, show confirm modal.
> - For Prednisone, show a simple quantity selector for number of tablets before saving.
> - For Powerade, show quick amount buttons: 8 oz, 12 oz, 16 oz, 20 oz, Custom.
> - For Poop, show quick options: Normal, Loose, Hard, Tiny, Constipated, plus optional note.
> - For Quick Note, open a text box and save note to carelite.entries.note.
> 
> 5. Insert logs into carelite.entries:
> - patient_id
> - item_id
> - entry_type copied from item_type
> - occurred_at default now
> - amount from selected/default amount
> - unit from selected/default unit
> - status completed
> - note if provided
> - metadata_json for extra selections, such as stool_type
> 
> 6. Add a simple recent activity feed below the buttons:
> Show today’s entries newest first:
> - time
> - item name
> - amount/unit
> - note if any
> 
> 7. Add a simple admin management section:
> Create/edit carelite.items.
> Fields:
> - name
> - item_type
> - category
> - icon
> - color
> - default_amount
> - default_unit
> - min_interval_minutes
> - max_uses_per_24h
> - max_amount_per_24h
> - is_scheduled
> - schedule_period
> - requires_confirmation
> - allow_note
> - active
> - sort_order
> - notes
> 
> 8. Safety wording:
> Do not say “safe to take.”
> Use:
> - “Available based on saved timing rules”
> - “Wait before next dose”
> - “Limit reached based on saved rules”
> - “Confirm actual medical limits with prescription/care team”
> 
> 9. Use existing project conventions:
> - existing Supabase client
> - existing auth
> - existing patient context if available
> - existing components/styles where appropriate
> - do not break existing care schema features
> 
> Build this as a small standalone feature first. Keep it simple, fast, and usable.
> ```
> 
> ---
> 
> # The decision
> 
> Do `carelite`.
> 
> This should be the app your mom can actually use while half-tired, short of breath, annoyed, and holding a Powerade.
> 
> That’s the design test.

### User
> oh and this has to have the o2 tanks estimated deplition, she just clicks the tank button that starts a tank at 2 liters per minute i think it is, it holds 2000 psi, when she takes it off she clicks again this will pause the timer, when she clicks again it starts the timer, when the timer is close to done it give a notice or warning to prepare next tank, once it hits zerio she clicks it and will ask, is this ia new tank yes no, if yes, start over, if no, it justs stays pausese and that flow repeats until there is a new tank yes clicked

### Assistant
> Good catch. O2 tanks are not just “inventory”; they’re an active runtime resource. The app needs a tank session state machine: start, pause, resume, replace.

### Assistant
> Yes. Add O2 tank runtime tracking to **CareLite**.
> 
> But important correction:
> 
> > **2000 PSI alone is not enough to know tank duration.**
> 
> You also need the **tank size/type** or usable oxygen capacity.
> 
> Example: an **E tank** at 2000 PSI usually has roughly **~625 liters** of oxygen.  
> At **2 L/min**, that’s about:
> 
> ```text
> 625 liters / 2 LPM = 312.5 minutes
> ≈ 5.2 hours
> ```
> 
> But don’t hardcode that blindly. Put the capacity in the database so you can adjust it.
> 
> ---
> 
> # CareLite oxygen model
> 
> You need two new concepts:
> 
> ## 1. Tank profile
> 
> This defines the type of tank.
> 
> Examples:
> 
> - E tank
> - D tank
> - M6 tank
> - Portable concentrator battery, maybe later
> 
> ## 2. Tank session
> 
> This tracks the active tank being used.
> 
> States:
> 
> ```text
> running
> paused
> depleted
> replaced
> ```
> 
> Her UI flow:
> 
> ```text
> Tank button clicked
> → start tank
> 
> Tank button clicked again
> → pause tank
> 
> Tank button clicked again
> → resume tank
> 
> Timer reaches near-empty
> → warning: prepare next tank
> 
> Timer reaches zero
> → show: Is this a new tank?
>    Yes → start fresh tank
>    No → remain paused/depleted
> ```
> 
> That’s the right behavior.
> 
> ---
> 
> # Add table: `carelite.oxygen_tank_profiles`
> 
> ```sql
> create table if not exists carelite.oxygen_tank_profiles (
>   id uuid primary key default gen_random_uuid(),
> 
>   patient_id uuid not null references care.patients(id),
> 
>   name text not null,
>   -- example: E Tank
> 
>   tank_type text,
>   -- example: E, D, M6
> 
>   starting_pressure_psi numeric not null default 2000,
> 
>   usable_liters numeric not null,
>   -- example: 625 for an E tank at 2000 PSI
> 
>   default_flow_lpm numeric not null default 2,
> 
>   warning_minutes_remaining integer not null default 30,
> 
>   active boolean not null default true,
> 
>   notes text,
>   metadata_json jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now()
> );
> ```
> 
> ---
> 
> # Add table: `carelite.oxygen_tank_sessions`
> 
> ```sql
> create table if not exists carelite.oxygen_tank_sessions (
>   id uuid primary key default gen_random_uuid(),
> 
>   patient_id uuid not null references care.patients(id),
>   tank_profile_id uuid not null references carelite.oxygen_tank_profiles(id),
> 
>   status text not null default 'running',
>   -- running, paused, depleted, replaced, voided
> 
>   started_at timestamptz not null default now(),
>   ended_at timestamptz,
> 
>   flow_lpm numeric not null default 2,
> 
>   starting_pressure_psi numeric not null default 2000,
>   usable_liters numeric not null,
> 
>   total_runtime_seconds integer not null default 0,
> 
>   last_started_at timestamptz,
>   last_paused_at timestamptz,
> 
>   depleted_at timestamptz,
>   replaced_at timestamptz,
> 
>   note text,
>   metadata_json jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now()
> );
> ```
> 
> ---
> 
> # How the timer math works
> 
> ## Estimated total runtime
> 
> ```text
> usable_liters / flow_lpm
> ```
> 
> Example:
> 
> ```text
> 625 liters / 2 LPM = 312.5 minutes
> ```
> 
> In seconds:
> 
> ```text
> (usable_liters / flow_lpm) * 60
> ```
> 
> ---
> 
> ## Runtime used
> 
> When running:
> 
> ```text
> total_runtime_seconds + seconds since last_started_at
> ```
> 
> When paused:
> 
> ```text
> total_runtime_seconds
> ```
> 
> ---
> 
> ## Remaining time
> 
> ```text
> estimated_total_seconds - runtime_used_seconds
> ```
> 
> If remaining time is less than warning threshold:
> 
> ```text
> Prepare next tank
> ```
> 
> If remaining time is zero or below:
> 
> ```text
> Tank estimated empty
> ```
> 
> ---
> 
> # Important design choice
> 
> Do **not** write database updates every second.
> 
> That’s how you make a dumb little timer expensive and annoying.
> 
> Instead:
> 
> - Save `last_started_at`
> - Save `total_runtime_seconds` only when paused/replaced/depleted
> - Let the frontend calculate the live countdown visually
> 
> The database only needs to know:
> 
> ```text
> When did this tank start?
> How much runtime had already been used?
> Is it running or paused?
> ```
> 
> Clean. Efficient. Correct enough.
> 
> ---
> 
> # Oxygen UI card
> 
> Add a big button/card:
> 
> ```text
> O2 Tank
> Running
> 4h 12m left
> Flow: 2 L/min
> [ Pause Tank ]
> ```
> 
> Paused:
> 
> ```text
> O2 Tank
> Paused
> 3h 48m left
> [ Resume Tank ]
> ```
> 
> Warning:
> 
> ```text
> O2 Tank
> Low Soon
> 24m left
> Prepare next tank
> [ Pause Tank ]
> ```
> 
> Empty:
> 
> ```text
> O2 Tank
> Estimated Empty
> Is this a new tank?
> [ No ] [ Yes, New Tank ]
> ```
> 
> When she clicks **Yes, New Tank**:
> 
> 1. Mark current session as `replaced`
> 2. Set `ended_at`
> 3. Set `replaced_at`
> 4. Create a new session
> 5. Start timer again
> 
> When she clicks **No**:
> 
> 1. Keep current tank paused/depleted
> 2. Do not reset timer
> 3. Show the same prompt when resumed/checked again
> 
> ---
> 
> # Add a CareLite item too
> 
> Even though tank sessions get their own table, I’d still add an item in `carelite.items` so it appears in the same button system.
> 
> ```sql
> insert into carelite.items
> (patient_id, name, item_type, category, icon, default_amount, default_unit, requires_confirmation, sort_order, notes)
> values
> (
>   'PATIENT_ID_HERE',
>   'O2 Tank',
>   'oxygen_tank',
>   'oxygen',
>   'gauge',
>   2,
>   'L/min',
>   false,
>   15,
>   'Tracks estimated oxygen tank depletion using flow rate and tank profile.'
> );
> ```
> 
> But don’t force oxygen tank runtime into the generic `entries` table only. It needs its own session state.
> 
> ---
> 
> # Seed tank profile
> 
> Assuming E tank, but verify the actual tank label.
> 
> ```sql
> insert into carelite.oxygen_tank_profiles
> (patient_id, name, tank_type, starting_pressure_psi, usable_liters, default_flow_lpm, warning_minutes_remaining, notes)
> values
> (
>   'PATIENT_ID_HERE',
>   'Standard O2 Tank',
>   'VERIFY',
>   2000,
>   625,
>   2,
>   30,
>   'Placeholder estimate. Verify actual tank type/capacity with supplier label.'
> );
> ```
> 
> Bluntly: name it `VERIFY` until you confirm the tank type. PSI is pressure, not total oxygen capacity by itself.
> 
> ---
> 
> # Optional log entries
> 
> When tank events happen, also write to `carelite.entries` for the daily feed.
> 
> Examples:
> 
> ```text
> 10:00 AM — O2 Tank started
> 12:15 PM — O2 Tank paused, 2h 45m estimated left
> 12:45 PM — O2 Tank resumed
> 3:30 PM — O2 Tank estimated depleted
> 3:35 PM — New O2 Tank started
> ```
> 
> That gives you history without forcing the generic entries table to manage the timer.
> 
> ---
> 
> # Add this to the Codex prompt
> 
> Paste this as an addendum to the previous CareLite prompt:
> 
> ```text
> Add oxygen tank depletion tracking to CareLite.
> 
> Important:
> O2 tank depletion is a runtime/session feature, not just a generic log entry. It should appear as a big CareLite card/button, but the active timer state should be stored in dedicated oxygen tank tables.
> 
> Database additions:
> 
> 1. Create carelite.oxygen_tank_profiles:
> - id uuid primary key default gen_random_uuid()
> - patient_id uuid not null references care.patients(id)
> - name text not null
> - tank_type text nullable
> - starting_pressure_psi numeric not null default 2000
> - usable_liters numeric not null
> - default_flow_lpm numeric not null default 2
> - warning_minutes_remaining integer not null default 30
> - active boolean not null default true
> - notes text nullable
> - metadata_json jsonb not null default '{}'
> - created_at timestamptz not null default now()
> - updated_at timestamptz not null default now()
> 
> 2. Create carelite.oxygen_tank_sessions:
> - id uuid primary key default gen_random_uuid()
> - patient_id uuid not null references care.patients(id)
> - tank_profile_id uuid not null references carelite.oxygen_tank_profiles(id)
> - status text not null default 'running'
>   allowed values conceptually: running, paused, depleted, replaced, voided
> - started_at timestamptz not null default now()
> - ended_at timestamptz nullable
> - flow_lpm numeric not null default 2
> - starting_pressure_psi numeric not null default 2000
> - usable_liters numeric not null
> - total_runtime_seconds integer not null default 0
> - last_started_at timestamptz nullable
> - last_paused_at timestamptz nullable
> - depleted_at timestamptz nullable
> - replaced_at timestamptz nullable
> - note text nullable
> - metadata_json jsonb not null default '{}'
> - created_at timestamptz not null default now()
> - updated_at timestamptz not null default now()
> 
> 3. Add indexes:
> - carelite.oxygen_tank_profiles(patient_id, active)
> - carelite.oxygen_tank_sessions(patient_id, status)
> - carelite.oxygen_tank_sessions(patient_id, started_at desc)
> 
> 4. Add a CareLite item:
> - name: O2 Tank
> - item_type: oxygen_tank
> - category: oxygen
> - icon: gauge
> - default_amount: 2
> - default_unit: L/min
> - requires_confirmation: false
> - sort_order: 15
> 
> 5. Oxygen tank timer behavior:
> 
> The O2 Tank card should use the active oxygen_tank_session.
> 
> If no active session exists:
> - Show “No tank running”
> - Button: “Start Tank”
> - On click, create a new oxygen_tank_session from the active tank profile:
>   - status = running
>   - started_at = now()
>   - last_started_at = now()
>   - flow_lpm = profile.default_flow_lpm
>   - starting_pressure_psi = profile.starting_pressure_psi
>   - usable_liters = profile.usable_liters
>   - total_runtime_seconds = 0
> 
> If session status is running:
> - Frontend calculates live runtime:
>   total_runtime_seconds + seconds since last_started_at
> - Estimated total seconds:
>   (usable_liters / flow_lpm) * 60
> - Remaining seconds:
>   estimated_total_seconds - runtime_used_seconds
> - Button: “Pause Tank”
> - On click:
>   - calculate seconds since last_started_at
>   - add that to total_runtime_seconds
>   - set last_paused_at = now()
>   - set status = paused
>   - clear or preserve last_started_at as appropriate
> 
> If session status is paused:
> - Show remaining time based on total_runtime_seconds
> - Button: “Resume Tank”
> - On click:
>   - set status = running
>   - set last_started_at = now()
> 
> If remaining seconds <= warning_minutes_remaining * 60:
> - Show warning state:
>   “Prepare next tank”
>   “Estimated [Xm] left”
> 
> If remaining seconds <= 0:
> - Show red/depleted state:
>   “Tank estimated empty”
>   Prompt:
>   “Is this a new tank?”
>   Buttons:
>   - “No”
>   - “Yes, New Tank”
> 
> If user clicks “Yes, New Tank”:
> - Mark current session:
>   - status = replaced
>   - ended_at = now()
>   - replaced_at = now()
> - Create a new session from the active tank profile:
>   - status = running
>   - started_at = now()
>   - last_started_at = now()
>   - total_runtime_seconds = 0
> - Refresh card
> 
> If user clicks “No”:
> - Keep current session paused/depleted.
> - Do not reset total_runtime_seconds.
> - Keep showing depleted/paused state until a new tank is started.
> 
> 6. Do not update the database every second.
> The frontend should calculate the live countdown. The database should only update on:
> - start tank
> - pause tank
> - resume tank
> - mark depleted
> - replace tank
> - void/correct session
> 
> 7. Optional but preferred:
> Write carelite.entries records for major oxygen events:
> - O2 tank started
> - O2 tank paused
> - O2 tank resumed
> - O2 tank estimated depleted
> - O2 tank replaced
> 
> These should appear in the recent activity feed.
> 
> 8. UI requirements:
> The O2 Tank card should be large and obvious.
> 
> States:
> - No active tank: gray/neutral, “Start Tank”
> - Running: green, countdown shown
> - Warning: yellow, “Prepare next tank”
> - Depleted: red, “Is this a new tank?”
> - Paused: blue/gray, “Resume Tank”
> 
> Display:
> - status
> - flow rate, usually 2 L/min
> - estimated time remaining
> - last started/resumed time
> - warning when close to empty
> 
> Safety wording:
> Use “estimated” everywhere. Do not imply the app knows the exact tank contents.
> Examples:
> - “Estimated tank time left”
> - “Prepare next tank”
> - “Estimated empty”
> - “Verify tank pressure and capacity manually when unsure.”
> 
> Important:
> Do not assume 2000 PSI alone determines duration. Store usable_liters on the tank profile. Seed a placeholder profile with 625 usable liters only if needed, and label it as needing verification.
> ```
> 
> ---
> 
> # Final design call
> 
> CareLite now has four modules:
> 
> ```text
> 1. Meds / treatments
> 2. Daily checkoffs
> 3. Body + intake tracking
> 4. O2 tank runtime
> ```
> 
> That’s still clean.
> 
> Do **not** merge this back into the big care app yet. CareLite is your daily cockpit. The big app is the archive/control center.

### User
> ok i need the full dev documentation for this complete with the goals, mvp list, estetic, codex commands, ide, gemini commands and the workflow to utilize these tools, etc.

### Assistant
> I’m going to turn this into a proper dev handoff doc, not just another chat blob. I’ll include the architecture, MVP boundaries, schema, UI rules, and tool workflow so Codex/Gemini don’t go wandering into the weeds.

### Assistant
> I verified the CLI basics so the handoff doesn’t rot immediately: Codex installs with `npm install -g @openai/codex` or Homebrew, and Gemini CLI supports `npx`, global npm, Homebrew, interactive, and non-interactive prompt modes.

### Assistant
> Done — I put the full **CareLite Dev Documentation** into canvas.
> 
> I included:
> 
> - Product goals
> - MVP scope
> - Non-goals
> - UX/aesthetic direction
> - `carelite` schema design
> - SQL tables/views/indexes
> - O2 tank session model
> - Seed data
> - Frontend component plan
> - Build order
> - Codex phase prompts
> - Gemini review prompts
> - IDE workflow
> - Git workflow
> - QA checklist
> - Risk register
> - Definition of done
> 
> Two verified tool notes so we don’t build on stale assumptions:
> 
> - Codex CLI currently installs via `npm install -g @openai/codex` or `brew install --cask codex`, then runs with `codex`. citeturn138065view0
> - Gemini CLI supports `npx @google/gemini-cli`, `npm install -g @google/gemini-cli`, `brew install gemini-cli`, interactive `gemini`, and non-interactive `gemini -p "..."`. citeturn754856view0turn754856view1
> 
> Blunt call: this doc is now strong enough to hand to Codex in phases. Do **not** give it the whole thing and say “build this.” Use the phase prompts. That keeps the gremlin contained.
