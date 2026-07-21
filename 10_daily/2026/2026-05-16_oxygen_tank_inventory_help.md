---
layout: page
title: "Oxygen tank inventory help"
slug: "oxygen_tank_inventory_help"
created_at: "2026-05-16 15:56:37"
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
date: 2026-05-16
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a08d9fc-5f9c-83ea-81c4-eaedeecb1254"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Oxygen tank inventory help

## Overview
- **Date**: 2026-05-16 15:56:37
- **Conversation ID**: `6a08d9fc-5f9c-83ea-81c4-eaedeecb1254`
- **Source**: `Chat-Export-28513-2026/conversations-007.json`

## Chat History

### User
> i forgot how to fill this out. id

> uuid

> Default: gen_random_uuid()

> patient_id

> uuid

> c5c16555-10b9-45f3-a5a3-d7528600cd47

> Has a foreign key relation tocare.patients.id

> 

> metadata_json

> jsonb

> Default: '{}'::jsonb

> created_at

> timestamptz

> 

> 05/16/2026 03:56:01 PM

> Default: now()

> 

> Your local timezone will be automatically applied (-0500)

> 

> 

> updated_at

> timestamptz

> 

> 05/16/2026 03:56:04 PM

> Default: now()

> 

> Your local timezone will be automatically applied (-0500)

> 

> 

> Optional Fields

> These are columns that do not need any value

> 

> tank_label

> text

> D

> tank_type

> text

> Default: NULL

> capacity_liters

> numeric

> NULL

> current_status

> text

> Default: NULL

> last_pressure_psi

> numeric

> NULL

> last_checked_at

> timestamptz

> 

> mm/dd/yyyy --:--:-- --

> Your local timezone will be automatically applied (-0500)

> 

> 

> notes

> text

> Default: NULL

### Assistant
> Yep — this looks like an **oxygen tank inventory / status record**. Fill it out like this:
> 
> | Field | What to enter |
> |---|---|
> | `id` | Leave blank. Supabase will generate it. |
> | `patient_id` | Already filled: `c5c16555-10b9-45f3-a5a3-d7528600cd47` |
> | `metadata_json` | Leave as `{}` unless you have extra structured info. |
> | `created_at` | Leave as default unless back-entering an old record. |
> | `updated_at` | Leave as default. |
> | `tank_label` | Your simple label, like `D`, `E`, `Backup D`, `Portable 1`, etc. |
> | `tank_type` | Enter the size/type: likely `D`, `E`, `M6`, `M9`, `H`, concentrator, etc. |
> | `capacity_liters` | Optional. Leave blank unless you know the tank capacity. |
> | `current_status` | Use a clean status like `full`, `in_use`, `low`, `empty`, `backup`, `needs_refill`, `unknown`. |
> | `last_pressure_psi` | Enter gauge pressure if you checked it, like `2000`, `1500`, `500`. |
> | `last_checked_at` | Enter when you checked it, like `05/16/2026 03:56:00 PM`. |
> | `notes` | Human-readable context. Example: `Portable D tank near bed. Gauge not checked yet.` |
> 
> For the one you’re looking at, I’d probably enter:
> 
> ```text
> tank_label: D
> tank_type: D
> capacity_liters: [leave blank]
> current_status: unknown
> last_pressure_psi: [leave blank unless checked]
> last_checked_at: [leave blank unless checked]
> notes: D portable oxygen tank. Status/pressure not verified yet.
> metadata_json: {}
> ```
> 
> Cleaner version if you **did check it just now**:
> 
> ```text
> tank_label: D
> tank_type: D
> capacity_liters: [leave blank]
> current_status: backup
> last_pressure_psi: 2000
> last_checked_at: 05/16/2026 03:56:00 PM
> notes: D portable oxygen tank checked and available as backup.
> metadata_json: {}
> ```
> 
> Truthfully: don’t overfill this. The **only fields that really matter operationally tonight** are:
> 
> ```text
> tank_label
> tank_type
> current_status
> last_pressure_psi
> last_checked_at
> notes
> ```
> 
> Everything else can chill.

### User
> the tanks are 2000 psi and she uses about 2liters per minute

### Assistant
> Perfect. Fill it like this:
> 
> ```text
> tank_label: D
> tank_type: D
> capacity_liters: [leave blank unless the tank label lists water capacity]
> current_status: full
> last_pressure_psi: 2000
> last_checked_at: 05/16/2026 03:56:00 PM
> notes: D portable oxygen tank. Gauge reads 2000 PSI. Patient uses oxygen at approximately 2 L/min.
> metadata_json: {}
> ```
> 
> Better `metadata_json` version, if you want the app to use it later:
> 
> ```json
> {
>   "flow_rate_lpm": 2,
>   "pressure_unit": "psi",
>   "use_case": "portable oxygen",
>   "estimated_status": "full"
> }
> ```
> 
> So the full clean entry is:
> 
> ```text
> tank_label: D
> tank_type: D
> current_status: full
> last_pressure_psi: 2000
> last_checked_at: 05/16/2026 03:56:00 PM
> notes: Gauge reads 2000 PSI. Oxygen flow rate is approximately 2 L/min.
> metadata_json: {"flow_rate_lpm":2,"pressure_unit":"psi","use_case":"portable oxygen","estimated_status":"full"}
> ```
> 
> One important correction: **don’t put `2` in `capacity_liters`**. That field is tank capacity, not her oxygen flow rate. Her usage belongs in `notes` or `metadata_json`.

### User
> so what is the capacity

### Assistant
> For a **D oxygen cylinder**, the usable gas capacity is usually about **425 liters** when full around **2,000 PSI**.
> 
> So enter:
> 
> ```text
> capacity_liters: 425
> last_pressure_psi: 2000
> ```
> 
> At **2 L/min**, rough runtime is:
> 
> ```text
> 425 liters ÷ 2 L/min = 212.5 minutes
> ```
> 
> That is about:
> 
> ```text
> 3.5 hours
> ```
> 
> Practical chart:
> 
> ```text
> Full D tank at 2000 PSI
> Flow rate: 2 L/min
> Estimated runtime: about 3 to 3.5 hours
> ```
> 
> For notes, I’d put:
> 
> ```text
> D portable oxygen tank. Full at approximately 2000 PSI. Estimated capacity about 425 L. Patient uses approximately 2 L/min; estimated runtime around 3.5 hours when full.
> ```
> 
> Tiny but important: if the tank is actually an **E tank**, capacity is closer to **680 liters**, so runtime would be about **5.5 hours** at 2 L/min. So check the shoulder/label: **D = ~425 L**, **E = ~680 L**.

### User
> shoulnt there be a tank type sheet where we can put in the standard info for each tank type so when we add a tank it prefils with capacity, anme, psi ect.

### Assistant
> Yes. **100%.** You just caught the missing normalization layer.
> 
> Right now your tank record is mixing two different things:
> 
> 1. **Tank instance** — “this physical tank labeled D near Mom’s bed”
> 2. **Tank type/spec** — “a D cylinder usually has ~425 L capacity at ~2000 PSI”
> 
> Those should not live in the same table as repeated manually typed values. That’s how garbage data sneaks in wearing a fake mustache.
> 
> You want:
> 
> ## 1. `oxygen_tank_types`
> 
> This is the reference/spec table.
> 
> ```sql
> create table if not exists care.oxygen_tank_types (
>   id uuid primary key default gen_random_uuid(),
> 
>   type_code text not null unique,
>   display_name text not null,
> 
>   standard_capacity_liters numeric,
>   standard_full_pressure_psi numeric,
>   reserve_pressure_psi numeric,
> 
>   notes text,
>   metadata_json jsonb not null default '{}'::jsonb,
> 
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now()
> );
> ```
> 
> Example rows:
> 
> ```sql
> insert into care.oxygen_tank_types (
>   type_code,
>   display_name,
>   standard_capacity_liters,
>   standard_full_pressure_psi,
>   reserve_pressure_psi,
>   notes,
>   metadata_json
> )
> values
>   (
>     'D',
>     'D portable oxygen cylinder',
>     425,
>     2000,
>     500,
>     'Common portable oxygen tank size. Approximate usable gas capacity varies by supplier/tank.',
>     '{"typical_use":"portable_backup"}'
>   ),
>   (
>     'E',
>     'E portable oxygen cylinder',
>     680,
>     2000,
>     500,
>     'Larger portable oxygen tank. Approximate usable gas capacity varies by supplier/tank.',
>     '{"typical_use":"portable_extended"}'
>   )
> on conflict (type_code) do update set
>   display_name = excluded.display_name,
>   standard_capacity_liters = excluded.standard_capacity_liters,
>   standard_full_pressure_psi = excluded.standard_full_pressure_psi,
>   reserve_pressure_psi = excluded.reserve_pressure_psi,
>   notes = excluded.notes,
>   metadata_json = excluded.metadata_json,
>   updated_at = now();
> ```
> 
> ## 2. Update your existing tank inventory table
> 
> Whatever this table is called — probably something like `care.oxygen_tanks` or `care.oxygen_inventory` — it should reference the tank type.
> 
> Add:
> 
> ```sql
> alter table care.oxygen_tanks
> add column if not exists tank_type_id uuid references care.oxygen_tank_types(id);
> ```
> 
> Then you still keep fields like:
> 
> ```text
> tank_label
> current_status
> last_pressure_psi
> last_checked_at
> location
> notes
> ```
> 
> But **capacity should come from the type table**, not be typed fresh every time.
> 
> ## 3. The clean model
> 
> ### `oxygen_tank_types`
> 
> ```text
> D = 425 L, full at 2000 PSI
> E = 680 L, full at 2000 PSI
> M6 = whatever standard value you confirm
> M9 = whatever standard value you confirm
> H = large home cylinder
> ```
> 
> ### `oxygen_tanks`
> 
> ```text
> Tank Label: D
> Tank Type: D portable oxygen cylinder
> Current PSI: 2000
> Status: full
> Location: bedroom / bedside / wheelchair bag / backup area
> ```
> 
> ## 4. Runtime should be calculated, not manually typed
> 
> Formula:
> 
> ```text
> estimated_runtime_minutes = capacity_liters * (last_pressure_psi / full_pressure_psi) / flow_rate_lpm
> ```
> 
> For Mom:
> 
> ```text
> 425 * (2000 / 2000) / 2 = 212.5 minutes
> ```
> 
> So about **3.5 hours**.
> 
> For a half-full D tank at 1000 PSI:
> 
> ```text
> 425 * (1000 / 2000) / 2 = 106.25 minutes
> ```
> 
> So about **1.75 hours**.
> 
> ## 5. Better Codex prompt
> 
> Give Codex this:
> 
> ```text
> Add a normalized oxygen tank type reference system.
> 
> Goal:
> Create a tank type/spec table so oxygen tank inventory records do not manually duplicate standard capacity, full PSI, reserve PSI, display name, or default metadata.
> 
> Create table:
> care.oxygen_tank_types
> 
> Fields:
> - id uuid primary key default gen_random_uuid()
> - type_code text not null unique
> - display_name text not null
> - standard_capacity_liters numeric
> - standard_full_pressure_psi numeric
> - reserve_pressure_psi numeric
> - notes text
> - metadata_json jsonb not null default '{}'::jsonb
> - created_at timestamptz not null default now()
> - updated_at timestamptz not null default now()
> 
> Seed at minimum:
> - D portable oxygen cylinder, approx 425 L, full PSI 2000, reserve PSI 500
> - E portable oxygen cylinder, approx 680 L, full PSI 2000, reserve PSI 500
> 
> Then update the existing oxygen tank inventory table to reference this table with:
> - tank_type_id uuid references care.oxygen_tank_types(id)
> 
> Do not remove existing fields yet.
> Do not break current UI.
> Do not drop data.
> Keep existing tank_type text field for now as a legacy/display fallback.
> 
> Add calculated helper logic, view, or frontend utility for estimated runtime:
> runtime_minutes = standard_capacity_liters * (last_pressure_psi / standard_full_pressure_psi) / flow_rate_lpm
> 
> Use Mom’s default oxygen flow rate as 2 L/min where no event-specific flow rate is provided, but make flow rate overrideable.
> 
> Also add admin UI behavior:
> When adding a tank and selecting tank type, prefill or display:
> - display name
> - standard capacity liters
> - standard full PSI
> - reserve PSI
> - estimated runtime based on current PSI and flow rate
> 
> Keep this additive and non-breaking.
> ```
> 
> And yes, in Google Sheets you should mirror this as a separate tab:
> 
> ```text
> oxygen_tank_types
> ```
> 
> With columns:
> 
> ```csv
> type_code,display_name,standard_capacity_liters,standard_full_pressure_psi,reserve_pressure_psi,notes
> D,D portable oxygen cylinder,425,2000,500,Common portable backup tank
> E,E portable oxygen cylinder,680,2000,500,Larger portable oxygen tank
> ```
> 
> This is exactly the kind of table that prevents “wait, what do I put here again?” every single time.

### User
> codex is not on supabase yet, so i added the table and made the change, how do we add the forumulas and such

### Assistant
> You’re at the right next layer: don’t cram formulas into the raw table unless they’re truly stable. Use a view for calculated values, then the app/admin page can read that cleanly.

### Assistant
> Yes. Add the “formulas” as a **SQL view**, not as normal fields.
> 
> Reason: runtime depends on data from **two tables**:
> 
> ```text
> oxygen_tanks.last_pressure_psi
> oxygen_tank_types.standard_capacity_liters
> oxygen_tank_types.standard_full_pressure_psi
> flow_rate_lpm
> ```
> 
> Postgres generated columns are useful, but they can only reference the current row and must use immutable expressions, so they are not ideal for calculations that need a joined tank-type table. Supabase itself points to Postgres generated columns as the preferred computed-field method only when those restrictions fit. citeturn982891search0turn982891search3
> 
> Use this.
> 
> ```sql
> create or replace view care.oxygen_tanks_with_runtime as
> select
>   t.id,
>   t.patient_id,
>   t.tank_label,
>   t.tank_type,
>   t.tank_type_id,
> 
>   tt.type_code,
>   tt.display_name as tank_type_name,
>   tt.standard_capacity_liters,
>   tt.standard_full_pressure_psi,
>   tt.reserve_pressure_psi,
> 
>   t.current_status,
>   t.last_pressure_psi,
>   t.last_checked_at,
> 
>   -- Default to Mom's 2 L/min unless overridden in metadata_json
>   coalesce(
>     nullif(t.metadata_json->>'flow_rate_lpm', '')::numeric,
>     2
>   ) as flow_rate_lpm,
> 
>   -- Estimated usable liters remaining
>   case
>     when t.last_pressure_psi is null
>       or tt.standard_full_pressure_psi is null
>       or tt.standard_full_pressure_psi = 0
>       or tt.standard_capacity_liters is null
>     then null
>     else round(
>       tt.standard_capacity_liters
>       * (t.last_pressure_psi / tt.standard_full_pressure_psi),
>       1
>     )
>   end as estimated_liters_remaining,
> 
>   -- Estimated runtime in minutes
>   case
>     when t.last_pressure_psi is null
>       or tt.standard_full_pressure_psi is null
>       or tt.standard_full_pressure_psi = 0
>       or tt.standard_capacity_liters is null
>       or coalesce(nullif(t.metadata_json->>'flow_rate_lpm', '')::numeric, 2) = 0
>     then null
>     else round(
>       (
>         tt.standard_capacity_liters
>         * (t.last_pressure_psi / tt.standard_full_pressure_psi)
>       )
>       / coalesce(nullif(t.metadata_json->>'flow_rate_lpm', '')::numeric, 2),
>       1
>     )
>   end as estimated_runtime_minutes,
> 
>   -- Estimated runtime in hours
>   case
>     when t.last_pressure_psi is null
>       or tt.standard_full_pressure_psi is null
>       or tt.standard_full_pressure_psi = 0
>       or tt.standard_capacity_liters is null
>       or coalesce(nullif(t.metadata_json->>'flow_rate_lpm', '')::numeric, 2) = 0
>     then null
>     else round(
>       (
>         (
>           tt.standard_capacity_liters
>           * (t.last_pressure_psi / tt.standard_full_pressure_psi)
>         )
>         / coalesce(nullif(t.metadata_json->>'flow_rate_lpm', '')::numeric, 2)
>       ) / 60,
>       2
>     )
>   end as estimated_runtime_hours,
> 
>   -- Human-useful status flag
>   case
>     when t.last_pressure_psi is null then 'unknown'
>     when tt.reserve_pressure_psi is not null
>       and t.last_pressure_psi <= tt.reserve_pressure_psi
>     then 'low_or_reserve'
>     when tt.standard_full_pressure_psi is not null
>       and t.last_pressure_psi >= tt.standard_full_pressure_psi * 0.9
>     then 'full_or_near_full'
>     else 'partial'
>   end as calculated_pressure_status,
> 
>   t.notes,
>   t.metadata_json,
>   t.created_at,
>   t.updated_at
> 
> from care.oxygen_tanks t
> left join care.oxygen_tank_types tt
>   on tt.id = t.tank_type_id;
> ```
> 
> Then test it:
> 
> ```sql
> select
>   tank_label,
>   type_code,
>   tank_type_name,
>   last_pressure_psi,
>   standard_capacity_liters,
>   flow_rate_lpm,
>   estimated_liters_remaining,
>   estimated_runtime_minutes,
>   estimated_runtime_hours,
>   calculated_pressure_status
> from care.oxygen_tanks_with_runtime
> where patient_id = 'c5c16555-10b9-45f3-a5a3-d7528600cd47'
> order by tank_label;
> ```
> 
> For the current D tank, assuming:
> 
> ```text
> D tank capacity: 425 L
> Full pressure: 2000 PSI
> Current pressure: 2000 PSI
> Flow rate: 2 L/min
> ```
> 
> The view should calculate:
> 
> ```text
> estimated_liters_remaining: 425
> estimated_runtime_minutes: 212.5
> estimated_runtime_hours: 3.54
> calculated_pressure_status: full_or_near_full
> ```
> 
> To store Mom’s flow rate on the tank record, update the tank metadata like this:
> 
> ```sql
> update care.oxygen_tanks
> set metadata_json = metadata_json || '{"flow_rate_lpm": 2}'::jsonb,
>     updated_at = now()
> where patient_id = 'c5c16555-10b9-45f3-a5a3-d7528600cd47'
>   and tank_label = 'D';
> ```
> 
> If your actual inventory table is **not** named `care.oxygen_tanks`, replace `care.oxygen_tanks` in the SQL with the real table name. Don’t over-engineer this with triggers yet. Views are cleaner, safer, and additive — exactly what you want right now.

### User
> ok now give me the prompt for codex to udpate the app or types or whatever so this is workign right.

### Assistant
> Here’s the Codex prompt — clean, direct, non-breaking:
> 
> ```text
> Update the app so the oxygen tank inventory system uses the new normalized tank type table and runtime view.
> 
> Context:
> Codex does not need to create the Supabase table manually. The database changes were already made in Supabase.
> 
> New database objects now available:
> 
> 1. care.oxygen_tank_types
> Purpose: reference/spec table for standard oxygen cylinder types.
> 
> Expected fields:
> - id uuid
> - type_code text
> - display_name text
> - standard_capacity_liters numeric
> - standard_full_pressure_psi numeric
> - reserve_pressure_psi numeric
> - notes text
> - metadata_json jsonb
> - created_at timestamptz
> - updated_at timestamptz
> 
> Seeded examples:
> - D portable oxygen cylinder, approx 425 L, full PSI 2000, reserve PSI 500
> - E portable oxygen cylinder, approx 680 L, full PSI 2000, reserve PSI 500
> 
> 2. Existing oxygen tank inventory table now has:
> - tank_type_id uuid references care.oxygen_tank_types(id)
> 
> Keep existing fields.
> Do not remove legacy tank_type text yet.
> Do not break existing pages.
> 
> 3. New view:
> care.oxygen_tanks_with_runtime
> 
> Purpose:
> Read-friendly oxygen tank inventory view that joins each tank to its tank type/spec and calculates estimated remaining oxygen and runtime.
> 
> Expected calculated fields include:
> - type_code
> - tank_type_name
> - standard_capacity_liters
> - standard_full_pressure_psi
> - reserve_pressure_psi
> - flow_rate_lpm
> - estimated_liters_remaining
> - estimated_runtime_minutes
> - estimated_runtime_hours
> - calculated_pressure_status
> 
> Goal:
> Update frontend/admin UI/types so oxygen tank inventory works cleanly with this normalized structure.
> 
> Tasks:
> 
> 1. Update Supabase/database TypeScript types
> - Regenerate or manually update DB types so the app recognizes:
>   - care.oxygen_tank_types
>   - tank_type_id on the existing oxygen tank inventory table
>   - care.oxygen_tanks_with_runtime view
> - If using generated Supabase types, run the appropriate generation command.
> - If generated types are not available, add safe local interface/types without breaking existing generated types.
> 
> 2. Add TypeScript domain types/helpers
> Create or update oxygen inventory domain types for:
> - OxygenTankType
> - OxygenTankInventoryRecord
> - OxygenTankWithRuntime
> 
> Include these fields:
> OxygenTankType:
> - id
> - type_code
> - display_name
> - standard_capacity_liters
> - standard_full_pressure_psi
> - reserve_pressure_psi
> - notes
> - metadata_json
> 
> OxygenTankWithRuntime:
> - id
> - patient_id
> - tank_label
> - tank_type
> - tank_type_id
> - type_code
> - tank_type_name
> - standard_capacity_liters
> - standard_full_pressure_psi
> - reserve_pressure_psi
> - current_status
> - last_pressure_psi
> - last_checked_at
> - flow_rate_lpm
> - estimated_liters_remaining
> - estimated_runtime_minutes
> - estimated_runtime_hours
> - calculated_pressure_status
> - notes
> - metadata_json
> - created_at
> - updated_at
> 
> 3. Update data fetching
> - Fetch tank type options from care.oxygen_tank_types.
> - Fetch display/runtime inventory from care.oxygen_tanks_with_runtime instead of manually calculating runtime in the main UI.
> - Keep fallback support for existing inventory rows that only have legacy tank_type text and no tank_type_id.
> - Make sure patient_id filtering still works.
> 
> 4. Update oxygen tank add/edit form
> When adding or editing an oxygen tank:
> - Add/select tank type from oxygen_tank_types.
> - Store selected type in tank_type_id.
> - Optionally keep tank_type text populated with the selected type_code/display fallback for now.
> - Keep tank_label editable.
> - Keep current_status editable.
> - Keep last_pressure_psi editable.
> - Keep last_checked_at editable.
> - Keep notes editable.
> - Support flow_rate_lpm through metadata_json.
> 
> Default behavior:
> - Default flow_rate_lpm to 2 if blank.
> - When a user selects a tank type, display the standard specs:
>   - display_name
>   - standard_capacity_liters
>   - standard_full_pressure_psi
>   - reserve_pressure_psi
> - Do not manually write standard_capacity_liters to the tank instance record unless the current schema still requires it.
> - Capacity should come from oxygen_tank_types / runtime view.
> 
> 5. Runtime display
> In the admin/inventory view, show:
> - Tank label
> - Tank type
> - Location if the existing schema has location
> - Current status
> - Last pressure PSI
> - Flow rate L/min
> - Estimated liters remaining
> - Estimated runtime minutes/hours
> - Calculated pressure status
> - Last checked time
> - Notes
> 
> Formatting:
> - If estimated_runtime_hours exists, show it as something like “3.5 hrs”.
> - If estimated_runtime_minutes exists and hours is null or under 1, show minutes.
> - If values are null, show “Unknown” instead of crashing.
> - Highlight or clearly mark calculated_pressure_status:
>   - full_or_near_full
>   - partial
>   - low_or_reserve
>   - unknown
> 
> 6. Runtime logic
> Prefer using the database view values:
> - estimated_liters_remaining
> - estimated_runtime_minutes
> - estimated_runtime_hours
> - calculated_pressure_status
> 
> Only add frontend fallback calculation if the view is unavailable or values are null and all required values are present.
> 
> Formula:
> estimated_runtime_minutes =
> standard_capacity_liters * (last_pressure_psi / standard_full_pressure_psi) / flow_rate_lpm
> 
> Guard against:
> - null pressure
> - null capacity
> - null full PSI
> - zero full PSI
> - zero flow rate
> 
> 7. Metadata handling
> For flow_rate_lpm:
> - Store in metadata_json.flow_rate_lpm
> - Preserve existing metadata_json values when updating
> - Do not overwrite the entire metadata_json object unless intentionally merging
> - Default to 2 L/min in UI when no value exists
> 
> Example metadata_json:
> {
>   "flow_rate_lpm": 2,
>   "pressure_unit": "psi",
>   "use_case": "portable oxygen"
> }
> 
> 8. Non-breaking requirements
> - Do not drop columns.
> - Do not delete existing data.
> - Keep legacy tank_type text field for now.
> - Keep old oxygen tank pages working while adding the normalized tank type behavior.
> - Use additive migrations only if adding missing objects/types is necessary.
> - Do not assume all existing tank rows have tank_type_id populated.
> - Handle nulls gracefully.
> 
> 9. Suggested UI behavior
> Admin oxygen tank form:
> - Tank Label: text input
> - Tank Type: select dropdown from oxygen_tank_types
> - Current PSI: number input
> - Flow Rate L/min: number input, default 2
> - Status: select/text input
> - Last Checked At: datetime input
> - Notes: textarea
> 
> Below the form or inside a preview card, display:
> - Standard capacity
> - Full PSI
> - Reserve PSI
> - Estimated runtime
> - Calculated status
> 
> 10. Add a small sanity check/test
> Add a lightweight test, dev assertion, or local helper validation confirming:
> D tank:
> - standard_capacity_liters = 425
> - standard_full_pressure_psi = 2000
> - last_pressure_psi = 2000
> - flow_rate_lpm = 2
> 
> Expected:
> - estimated_runtime_minutes ≈ 212.5
> - estimated_runtime_hours ≈ 3.54
> 
> Do not overbuild this.
> The priority is making the admin entry page practical, accurate, and hard to mess up.
> ```
> 
> And here’s the **super-short version** in case Codex behaves better with less:
> 
> ```text
> Update the oxygen tank inventory UI/types to use the new normalized Supabase table care.oxygen_tank_types and the new view care.oxygen_tanks_with_runtime.
> 
> The database is already updated.
> 
> Add/read:
> - care.oxygen_tank_types for tank type dropdown/specs
> - tank_type_id on oxygen tank inventory records
> - care.oxygen_tanks_with_runtime for display/runtime calculations
> 
> In the add/edit tank form:
> - user selects tank type from oxygen_tank_types
> - save tank_type_id
> - keep legacy tank_type text as fallback
> - current PSI stays on the tank record
> - flow_rate_lpm should be stored in metadata_json.flow_rate_lpm, default 2
> - preserve existing metadata_json when updating
> 
> In the inventory display:
> Use care.oxygen_tanks_with_runtime and show:
> - tank_label
> - tank_type_name / type_code
> - last_pressure_psi
> - flow_rate_lpm
> - estimated_liters_remaining
> - estimated_runtime_minutes
> - estimated_runtime_hours
> - calculated_pressure_status
> - last_checked_at
> - notes
> 
> Handle nulls gracefully.
> Do not drop columns.
> Do not delete data.
> Do not break existing pages.
> Keep this additive and practical.
> ```
