---
layout: page
title: "Supabase table list query"
slug: "supabase_table_list_query"
created_at: "2026-05-14 20:16:12"
updated_at: "2026-05-14 20:16:12"
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
date: 2026-05-14
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a0673cc-8340-83ea-aef1-2412788615f6"
canonical_ref: ""
---

# Supabase table list query

## Overview
- **Date**: 2026-05-14 20:16:12
- **Conversation ID**: `6a0673cc-8340-83ea-aef1-2412788615f6`
- **Source**: `Chat-Export-28513-2026/conversations-007.json`

## Chat History

### User
> what is the command or code to get a full list of the tables and fields for moms care app in supabase

### Assistant
> Use this in the **Supabase SQL Editor** to get a clean list of every table and field in the `public` schema:
> 
> ```sql
> SELECT
>   table_schema,
>   table_name,
>   ordinal_position,
>   column_name,
>   data_type,
>   is_nullable,
>   column_default
> FROM information_schema.columns
> WHERE table_schema = 'public'
> ORDER BY table_name, ordinal_position;
> ```
> 
> Better version, because it also shows primary keys:
> 
> ```sql
> SELECT
>   c.table_schema,
>   c.table_name,
>   c.ordinal_position,
>   c.column_name,
>   c.data_type,
>   c.is_nullable,
>   c.column_default,
>   CASE
>     WHEN pk.column_name IS NOT NULL THEN 'YES'
>     ELSE 'NO'
>   END AS is_primary_key
> FROM information_schema.columns c
> LEFT JOIN (
>   SELECT
>     kcu.table_schema,
>     kcu.table_name,
>     kcu.column_name
>   FROM information_schema.table_constraints tc
>   JOIN information_schema.key_column_usage kcu
>     ON tc.constraint_name = kcu.constraint_name
>    AND tc.table_schema = kcu.table_schema
>    AND tc.table_name = kcu.table_name
>   WHERE tc.constraint_type = 'PRIMARY KEY'
> ) pk
>   ON c.table_schema = pk.table_schema
>  AND c.table_name = pk.table_name
>  AND c.column_name = pk.column_name
> WHERE c.table_schema = 'public'
> ORDER BY c.table_name, c.ordinal_position;
> ```
> 
> If you want it as a **copy/paste export for Codex**, use this version:
> 
> ```sql
> SELECT
>   table_name || '.' || column_name AS field,
>   data_type,
>   is_nullable,
>   column_default
> FROM information_schema.columns
> WHERE table_schema = 'public'
> ORDER BY table_name, ordinal_position;
> ```
> 
> If you’re using the **Supabase CLI / psql**, run:
> 
> ```bash
> supabase db dump --schema public --schema-only > supabase_schema.sql
> ```
> 
> That gives you the full table definitions, relationships, constraints, indexes, etc. That’s the better artifact for Codex.
> 
> For a quick human-readable table list only:
> 
> ```sql
> SELECT table_name
> FROM information_schema.tables
> WHERE table_schema = 'public'
>   AND table_type = 'BASE TABLE'
> ORDER BY table_name;
> ```
> 
> Best move for Mom’s Care App: run the **primary-key version** first, then run the CLI schema dump if you want Codex to safely compare your Google Sheets / care sheets against the actual Supabase structure.

### User
> actually here is is i think. -- WARNING: This schema is for context only and is not meant to be run.
> -- Table order and constraints may not be valid for execution.
> 
> CREATE TABLE care.attachments (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   encounter_id uuid,
>   file_name text,
>   file_type text,
>   storage_path text,
>   attachment_kind text,
>   notes text,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   uploaded_at timestamp with time zone NOT NULL DEFAULT now(),
>   discharge_document_id uuid,
>   care_plan_id uuid,
>   CONSTRAINT attachments_pkey PRIMARY KEY (id),
>   CONSTRAINT attachments_discharge_document_id_fkey FOREIGN KEY (discharge_document_id) REFERENCES care.discharge_documents(id),
>   CONSTRAINT attachments_care_plan_id_fkey FOREIGN KEY (care_plan_id) REFERENCES care.care_plans(id),
>   CONSTRAINT attachments_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id),
>   CONSTRAINT attachments_encounter_id_fkey FOREIGN KEY (encounter_id) REFERENCES care.encounters(id)
> );
> CREATE TABLE care.care_daily_notes (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   household_id uuid,
>   caregiver_id uuid,
>   note_date date NOT NULL,
>   caregiver_name text,
>   sleep_last_night text CHECK (sleep_last_night = ANY (ARRAY['good'::text, 'fair'::text, 'poor'::text])),
>   overall_day text CHECK (overall_day = ANY (ARRAY['better'::text, 'same'::text, 'worse'::text])),
>   o2_range text,
>   heart_rate text,
>   blood_pressure text,
>   temperature text,
>   breathing_quality text CHECK (breathing_quality = ANY (ARRAY['easy'::text, 'moderate'::text, 'hard'::text])),
>   symptoms ARRAY NOT NULL DEFAULT '{}'::text[],
>   last_morphine_time text,
>   last_norco_time text,
>   nebulizers_completed boolean,
>   prednisone_taken boolean,
>   blood_sugar_checked boolean,
>   medication_notes text,
>   transfer_status text CHECK (transfer_status = ANY (ARRAY['easy'::text, 'moderate'::text, 'difficult'::text])),
>   bathroom_status text CHECK (bathroom_status = ANY (ARRAY['normal'::text, 'trouble'::text, 'assistance_needed'::text])),
>   walking_standing text CHECK (walking_standing = ANY (ARRAY['better'::text, 'same'::text, 'worse'::text])),
>   mental_state ARRAY NOT NULL DEFAULT '{}'::text[],
>   key_notes_events text,
>   red_flags ARRAY NOT NULL DEFAULT '{}'::text[],
>   urgent_followup boolean NOT NULL DEFAULT false,
>   is_printed boolean NOT NULL DEFAULT false,
>   printed_at timestamp with time zone,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
>   deleted_at timestamp with time zone,
>   CONSTRAINT care_daily_notes_pkey PRIMARY KEY (id),
>   CONSTRAINT care_daily_notes_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id)
> );
> CREATE TABLE care.care_plan_items (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   care_plan_id uuid NOT NULL,
>   patient_id uuid NOT NULL,
>   category text,
>   item_text text NOT NULL,
>   frequency text,
>   status text,
>   target_metric text,
>   target_value numeric,
>   notes text,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
>   CONSTRAINT care_plan_items_pkey PRIMARY KEY (id),
>   CONSTRAINT care_plan_items_care_plan_id_fkey FOREIGN KEY (care_plan_id) REFERENCES care.care_plans(id),
>   CONSTRAINT care_plan_items_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id)
> );
> CREATE TABLE care.care_plans (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   title text NOT NULL,
>   status text,
>   start_date date,
>   end_date date,
>   created_by text,
>   source_type text,
>   summary text,
>   precautions text,
>   escalation_rules text,
>   notes text,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
>   CONSTRAINT care_plans_pkey PRIMARY KEY (id),
>   CONSTRAINT care_plans_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id)
> );
> CREATE TABLE care.conditions (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   category text,
>   summary text,
>   risks text,
>   actions text,
>   status text,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
>   condition_name text,
>   medical_code text,
>   code_system text,
>   watch_fors text,
>   interaction_summary text,
>   compounding_risks text,
>   CONSTRAINT conditions_pkey PRIMARY KEY (id),
>   CONSTRAINT conditions_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id)
> );
> CREATE TABLE care.device_profiles (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   device_type text NOT NULL,
>   manufacturer text,
>   model text,
>   serial_number text,
>   active boolean NOT NULL DEFAULT true,
>   notes text,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
>   CONSTRAINT device_profiles_pkey PRIMARY KEY (id),
>   CONSTRAINT device_profiles_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id)
> );
> CREATE TABLE care.device_readings (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   device_profile_id uuid NOT NULL,
>   reading_type text,
>   reading_name text NOT NULL,
>   reading_value numeric,
>   reading_unit text,
>   recorded_at timestamp with time zone NOT NULL DEFAULT now(),
>   notes text,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   CONSTRAINT device_readings_pkey PRIMARY KEY (id),
>   CONSTRAINT device_readings_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id),
>   CONSTRAINT device_readings_device_profile_id_fkey FOREIGN KEY (device_profile_id) REFERENCES care.device_profiles(id)
> );
> CREATE TABLE care.discharge_actions (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   discharge_document_id uuid NOT NULL,
>   action_type text,
>   action_text text NOT NULL,
>   due_date date,
>   status text,
>   completed_at timestamp with time zone,
>   notes text,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
>   CONSTRAINT discharge_actions_pkey PRIMARY KEY (id),
>   CONSTRAINT discharge_actions_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id),
>   CONSTRAINT discharge_actions_discharge_document_id_fkey FOREIGN KEY (discharge_document_id) REFERENCES care.discharge_documents(id)
> );
> CREATE TABLE care.discharge_documents (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   encounter_id uuid,
>   document_title text,
>   discharge_date date,
>   facility text,
>   provider_name text,
>   summary text,
>   medication_changes_text text,
>   follow_up_text text,
>   warning_signs_text text,
>   raw_text text,
>   status text,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
>   CONSTRAINT discharge_documents_pkey PRIMARY KEY (id),
>   CONSTRAINT discharge_documents_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id),
>   CONSTRAINT discharge_documents_encounter_id_fkey FOREIGN KEY (encounter_id) REFERENCES care.encounters(id)
> );
> CREATE TABLE care.encounters (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   encounter_type text,
>   provider_name text,
>   facility text,
>   status text,
>   occurred_at timestamp with time zone,
>   summary text,
>   med_changes text,
>   follow_up_needed text,
>   notes text,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
>   CONSTRAINT encounters_pkey PRIMARY KEY (id),
>   CONSTRAINT encounters_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id)
> );
> CREATE TABLE care.interactions (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   med1 text,
>   med2 text,
>   severity text,
>   description text,
>   recommendation text,
>   source_notes text,
>   metadata_json jsonb DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone DEFAULT now(),
>   CONSTRAINT interactions_pkey PRIMARY KEY (id)
> );
> CREATE TABLE care.kb_sections (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   title text NOT NULL,
>   category text,
>   section_key text,
>   summary text,
>   content text NOT NULL,
>   content_format text NOT NULL DEFAULT 'markdown'::text,
>   source_type text,
>   source_path text,
>   source_title text,
>   tags ARRAY NOT NULL DEFAULT '{}'::text[],
>   ai_retrievable boolean NOT NULL DEFAULT true,
>   review_status text NOT NULL DEFAULT 'active'::text,
>   sort_order integer NOT NULL DEFAULT 0,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
>   CONSTRAINT kb_sections_pkey PRIMARY KEY (id),
>   CONSTRAINT kb_sections_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id)
> );
> CREATE TABLE care.medication_events (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   medication_id uuid,
>   encounter_id uuid,
>   action text NOT NULL,
>   dose_taken text,
>   quantity_change numeric,
>   reason text,
>   notes text,
>   source_type text,
>   occurred_at timestamp with time zone NOT NULL DEFAULT now(),
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   discharge_document_id uuid,
>   CONSTRAINT medication_events_pkey PRIMARY KEY (id),
>   CONSTRAINT medication_events_discharge_document_id_fkey FOREIGN KEY (discharge_document_id) REFERENCES care.discharge_documents(id),
>   CONSTRAINT medication_events_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id),
>   CONSTRAINT medication_events_medication_id_fkey FOREIGN KEY (medication_id) REFERENCES care.medications(id),
>   CONSTRAINT medication_events_encounter_id_fkey FOREIGN KEY (encounter_id) REFERENCES care.encounters(id)
> );
> CREATE TABLE care.medications (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   medication_name text NOT NULL,
>   strength text,
>   form text,
>   prescriber text,
>   dosage_instructions text,
>   frequency text,
>   quantity_prescribed numeric,
>   quantity_remaining numeric,
>   active boolean NOT NULL DEFAULT true,
>   notes text,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
>   expiration_date date,
>   refills_allowed integer,
>   prescribed_date date,
>   prescription_notes text,
>   medication_image_url text,
>   barcode text,
>   strength_value numeric,
>   strength_unit text,
>   route text,
>   unit_type text,
>   low_supply_threshold numeric,
>   pharmacy_source text,
>   cost numeric,
>   medication_status text NOT NULL DEFAULT 'active'::text CHECK (medication_status = ANY (ARRAY['active'::text, 'on_hold'::text, 'inactive'::text])),
>   hold_reason text,
>   hold_started_at timestamp with time zone,
>   hold_requested_by text,
>   hold_notes text,
>   clinician_review_needed boolean NOT NULL DEFAULT false,
>   review_reason text,
>   CONSTRAINT medications_pkey PRIMARY KEY (id),
>   CONSTRAINT medications_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id)
> );
> CREATE TABLE care.milestones (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   name text NOT NULL,
>   metric text,
>   value numeric,
>   baseline_value numeric,
>   target_value numeric,
>   unit text,
>   notes text,
>   recorded_at timestamp with time zone NOT NULL DEFAULT now(),
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   care_plan_id uuid,
>   CONSTRAINT milestones_pkey PRIMARY KEY (id),
>   CONSTRAINT milestones_care_plan_id_fkey FOREIGN KEY (care_plan_id) REFERENCES care.care_plans(id),
>   CONSTRAINT milestones_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id)
> );
> CREATE TABLE care.observations (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   encounter_id uuid,
>   category text,
>   subtype text,
>   severity integer,
>   body_area text,
>   notes text,
>   recorded_at timestamp with time zone NOT NULL DEFAULT now(),
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   care_plan_id uuid,
>   CONSTRAINT observations_pkey PRIMARY KEY (id),
>   CONSTRAINT observations_care_plan_id_fkey FOREIGN KEY (care_plan_id) REFERENCES care.care_plans(id),
>   CONSTRAINT observations_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id),
>   CONSTRAINT observations_encounter_id_fkey FOREIGN KEY (encounter_id) REFERENCES care.encounters(id)
> );
> CREATE TABLE care.oxygen_tanks (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   tank_label text,
>   tank_type text,
>   capacity_liters numeric,
>   current_status text,
>   last_pressure_psi numeric,
>   last_checked_at timestamp with time zone,
>   notes text,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
>   CONSTRAINT oxygen_tanks_pkey PRIMARY KEY (id),
>   CONSTRAINT oxygen_tanks_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id)
> );
> CREATE TABLE care.oxygen_usage_sessions (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   oxygen_tank_id uuid NOT NULL,
>   started_at timestamp with time zone,
>   ended_at timestamp with time zone,
>   flow_rate_lpm numeric,
>   starting_pressure_psi numeric,
>   ending_pressure_psi numeric,
>   estimated_empty_at timestamp with time zone,
>   notes text,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
>   CONSTRAINT oxygen_usage_sessions_pkey PRIMARY KEY (id),
>   CONSTRAINT oxygen_usage_sessions_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id),
>   CONSTRAINT oxygen_usage_sessions_oxygen_tank_id_fkey FOREIGN KEY (oxygen_tank_id) REFERENCES care.oxygen_tanks(id)
> );
> CREATE TABLE care.patients (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   full_name text,
>   dob date,
>   baseline_notes text,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
>   CONSTRAINT patients_pkey PRIMARY KEY (id)
> );
> CREATE TABLE care.regimen_events (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   regimen_id uuid NOT NULL,
>   status text NOT NULL,
>   performed_at timestamp with time zone NOT NULL DEFAULT now(),
>   notes text,
>   source_type text,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   CONSTRAINT regimen_events_pkey PRIMARY KEY (id),
>   CONSTRAINT regimen_events_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id),
>   CONSTRAINT regimen_events_regimen_id_fkey FOREIGN KEY (regimen_id) REFERENCES care.regimens(id)
> );
> CREATE TABLE care.regimens (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   regimen_type text NOT NULL,
>   title text NOT NULL,
>   linked_medication_id uuid,
>   instructions text,
>   with_food boolean,
>   food_instruction_text text,
>   is_prn boolean NOT NULL DEFAULT false,
>   min_interval_minutes integer,
>   schedule_type text NOT NULL,
>   schedule_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   active boolean NOT NULL DEFAULT true,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
>   CONSTRAINT regimens_pkey PRIMARY KEY (id),
>   CONSTRAINT regimens_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id),
>   CONSTRAINT regimens_linked_medication_id_fkey FOREIGN KEY (linked_medication_id) REFERENCES care.medications(id)
> );
> CREATE TABLE care.supply_events (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   supply_item_id uuid NOT NULL,
>   event_type text NOT NULL,
>   quantity_change numeric NOT NULL,
>   occurred_at timestamp with time zone NOT NULL DEFAULT now(),
>   notes text,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   CONSTRAINT supply_events_pkey PRIMARY KEY (id),
>   CONSTRAINT supply_events_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id),
>   CONSTRAINT supply_events_supply_item_id_fkey FOREIGN KEY (supply_item_id) REFERENCES care.supply_items(id)
> );
> CREATE TABLE care.supply_inventory (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   supply_item_id uuid NOT NULL,
>   quantity_on_hand numeric NOT NULL DEFAULT 0,
>   quantity_reserved numeric NOT NULL DEFAULT 0,
>   last_counted_at timestamp with time zone,
>   notes text,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
>   CONSTRAINT supply_inventory_pkey PRIMARY KEY (id),
>   CONSTRAINT supply_inventory_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id),
>   CONSTRAINT supply_inventory_supply_item_id_fkey FOREIGN KEY (supply_item_id) REFERENCES care.supply_items(id)
> );
> CREATE TABLE care.supply_items (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   name text NOT NULL,
>   category text,
>   unit text,
>   reorder_threshold numeric,
>   target_stock_level numeric,
>   notes text,
>   active boolean NOT NULL DEFAULT true,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
>   location text,
>   status text,
>   cost numeric,
>   CONSTRAINT supply_items_pkey PRIMARY KEY (id),
>   CONSTRAINT supply_items_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id)
> );
> CREATE TABLE care.supply_order_items (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   order_id uuid NOT NULL,
>   supply_item_id uuid NOT NULL,
>   quantity_ordered numeric NOT NULL DEFAULT 0,
>   quantity_received numeric NOT NULL DEFAULT 0,
>   notes text,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
>   CONSTRAINT supply_order_items_pkey PRIMARY KEY (id),
>   CONSTRAINT supply_order_items_order_id_fkey FOREIGN KEY (order_id) REFERENCES care.supply_orders(id),
>   CONSTRAINT supply_order_items_supply_item_id_fkey FOREIGN KEY (supply_item_id) REFERENCES care.supply_items(id)
> );
> CREATE TABLE care.supply_orders (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   vendor_contact_id uuid,
>   status text,
>   ordered_at timestamp with time zone,
>   expected_at timestamp with time zone,
>   received_at timestamp with time zone,
>   notes text,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
>   CONSTRAINT supply_orders_pkey PRIMARY KEY (id),
>   CONSTRAINT supply_orders_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id)
> );
> CREATE TABLE care.vitals (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   encounter_id uuid,
>   systolic integer,
>   diastolic integer,
>   pulse integer,
>   oxygen integer,
>   temp numeric,
>   context text,
>   notes text,
>   recorded_at timestamp with time zone NOT NULL DEFAULT now(),
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   glucose numeric,
>   ketones numeric,
>   weight numeric,
>   respiratory_rate integer,
>   CONSTRAINT vitals_pkey PRIMARY KEY (id),
>   CONSTRAINT vitals_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id),
>   CONSTRAINT vitals_encounter_id_fkey FOREIGN KEY (encounter_id) REFERENCES care.encounters(id)
> );

### Assistant
> Yep — this is the schema. The important correction: your app is using the **`care` schema**, not `public`.
> 
> So the command I gave earlier should be adjusted from:
> 
> ```sql
> WHERE table_schema = 'public'
> ```
> 
> to:
> 
> ```sql
> WHERE table_schema = 'care'
> ```
> 
> ## Clean command for Mom’s Care App schema
> 
> Run this in Supabase SQL Editor:
> 
> ```sql
> SELECT
>   c.table_schema,
>   c.table_name,
>   c.ordinal_position,
>   c.column_name,
>   c.data_type,
>   c.udt_name,
>   c.is_nullable,
>   c.column_default,
>   CASE
>     WHEN pk.column_name IS NOT NULL THEN 'YES'
>     ELSE 'NO'
>   END AS is_primary_key
> FROM information_schema.columns c
> LEFT JOIN (
>   SELECT
>     kcu.table_schema,
>     kcu.table_name,
>     kcu.column_name
>   FROM information_schema.table_constraints tc
>   JOIN information_schema.key_column_usage kcu
>     ON tc.constraint_name = kcu.constraint_name
>    AND tc.table_schema = kcu.table_schema
>    AND tc.table_name = kcu.table_name
>   WHERE tc.constraint_type = 'PRIMARY KEY'
>     AND tc.table_schema = 'care'
> ) pk
>   ON c.table_schema = pk.table_schema
>  AND c.table_name = pk.table_name
>  AND c.column_name = pk.column_name
> WHERE c.table_schema = 'care'
> ORDER BY c.table_name, c.ordinal_position;
> ```
> 
> ## Simpler export for Codex
> 
> ```sql
> SELECT
>   table_name,
>   column_name,
>   data_type,
>   udt_name,
>   is_nullable,
>   column_default
> FROM information_schema.columns
> WHERE table_schema = 'care'
> ORDER BY table_name, ordinal_position;
> ```
> 
> ## Full table list
> 
> ```sql
> SELECT table_name
> FROM information_schema.tables
> WHERE table_schema = 'care'
>   AND table_type = 'BASE TABLE'
> ORDER BY table_name;
> ```
> 
> ## Foreign key map
> 
> This one is useful for Codex because it shows how tables connect:
> 
> ```sql
> SELECT
>   tc.table_schema,
>   tc.table_name,
>   kcu.column_name,
>   ccu.table_schema AS foreign_table_schema,
>   ccu.table_name AS foreign_table_name,
>   ccu.column_name AS foreign_column_name,
>   tc.constraint_name
> FROM information_schema.table_constraints AS tc
> JOIN information_schema.key_column_usage AS kcu
>   ON tc.constraint_name = kcu.constraint_name
>  AND tc.table_schema = kcu.table_schema
> JOIN information_schema.constraint_column_usage AS ccu
>   ON ccu.constraint_name = tc.constraint_name
>  AND ccu.table_schema = tc.table_schema
> WHERE tc.constraint_type = 'FOREIGN KEY'
>   AND tc.table_schema = 'care'
> ORDER BY tc.table_name, kcu.column_name;
> ```
> 
> ## What you currently have
> 
> You have a pretty solid care-system spine already:
> 
> ```text
> care.patients
> care.medications
> care.medication_events
> care.regimens
> care.regimen_events
> care.vitals
> care.conditions
> care.observations
> care.encounters
> care.discharge_documents
> care.discharge_actions
> care.care_plans
> care.care_plan_items
> care.care_daily_notes
> care.device_profiles
> care.device_readings
> care.oxygen_tanks
> care.oxygen_usage_sessions
> care.supply_items
> care.supply_inventory
> care.supply_events
> care.supply_orders
> care.supply_order_items
> care.attachments
> care.kb_sections
> care.milestones
> care.interactions
> ```
> 
> ## The thing you were right about: you are missing a proper “stations / locations” layer
> 
> You have `care.supply_items.location`, but that is too flat. That works for “gloves are in bathroom,” but not for restaurant-style station documentation like:
> 
> ```text
> Bathroom Station
> Bedside Station
> Medication Station
> Oxygen Station
> Cleaning Station
> Emergency Go-Bag
> Wound Care / Skin Care Bin
> Transfer / Mobility Area
> ```
> 
> Better structure would be:
> 
> ```sql
> CREATE TABLE care.care_locations (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   name text NOT NULL,
>   location_type text,
>   parent_location_id uuid,
>   notes text,
>   active boolean NOT NULL DEFAULT true,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
>   CONSTRAINT care_locations_pkey PRIMARY KEY (id),
>   CONSTRAINT care_locations_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id),
>   CONSTRAINT care_locations_parent_location_id_fkey FOREIGN KEY (parent_location_id) REFERENCES care.care_locations(id)
> );
> ```
> 
> Then add a station requirements table:
> 
> ```sql
> CREATE TABLE care.station_requirements (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   location_id uuid NOT NULL,
>   supply_item_id uuid NOT NULL,
>   par_level numeric,
>   minimum_level numeric,
>   required boolean NOT NULL DEFAULT true,
>   notes text,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
>   CONSTRAINT station_requirements_pkey PRIMARY KEY (id),
>   CONSTRAINT station_requirements_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id),
>   CONSTRAINT station_requirements_location_id_fkey FOREIGN KEY (location_id) REFERENCES care.care_locations(id),
>   CONSTRAINT station_requirements_supply_item_id_fkey FOREIGN KEY (supply_item_id) REFERENCES care.supply_items(id)
> );
> ```
> 
> That gives you the restaurant-style logic:
> 
> ```text
> This station should always have:
> - 2 packs gloves
> - 1 wipes pack
> - 1 trash bag roll
> - 1 barrier cream
> - 1 bed pad stack
> ```
> 
> ## Also: your “events log” already partially exists
> 
> You have several event tables:
> 
> ```text
> care.medication_events
> care.regimen_events
> care.supply_events
> care.oxygen_usage_sessions
> care.device_readings
> care.vitals
> care.observations
> care.encounters
> care.care_daily_notes
> ```
> 
> But you do **not** have one unified general event log.
> 
> I would add this:
> 
> ```sql
> CREATE TABLE care.care_events (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   event_type text NOT NULL,
>   event_category text,
>   title text NOT NULL,
>   description text,
>   severity text,
>   occurred_at timestamp with time zone NOT NULL DEFAULT now(),
>   related_table text,
>   related_id uuid,
>   caregiver_name text,
>   followup_needed boolean NOT NULL DEFAULT false,
>   followup_status text,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
>   CONSTRAINT care_events_pkey PRIMARY KEY (id),
>   CONSTRAINT care_events_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES care.patients(id)
> );
> ```
> 
> That becomes your master timeline:
> 
> ```text
> Medication change
> Fall risk event
> Breathing episode
> Bathroom issue
> Caregiver shift note
> Supply shortage
> Doctor call
> Family conflict affecting care
> Improvement milestone
> Emergency warning sign
> ```
> 
> Best next move: give Codex this instruction:
> 
> ```text
> Review the current Supabase schema under the care schema. Add a generalized care_events table for unified timeline logging and add care_locations + station_requirements tables to support restaurant-style care stations/inventory placement. Do not remove the existing specialized event tables. The new care_events table should act as a human-readable master timeline and may reference specialized records through related_table and related_id.
> ```

### User
> ok, so can you give me in quick copy the sql to get the details you need, and the ones to make the additions or changes you mentioned, without altering what is currently there just adding to or creating so nothing breaks, well i guess do the creating first then the commands to get the full list with fields and how they connect at the end.

### Assistant
> Absolutely. Copy/paste this whole thing into Supabase SQL Editor.
> 
> ```sql
> -- ============================================================
> -- MOM'S CARE APP — SAFE ADDITIONS ONLY
> -- Creates:
> -- 1. care.care_locations
> -- 2. care.station_requirements
> -- 3. care.care_events
> --
> -- This does NOT alter existing tables.
> -- It only creates new tables if they do not already exist.
> -- ============================================================
> 
> 
> -- ============================================================
> -- 1. CARE LOCATIONS / STATIONS
> -- Examples:
> -- Bathroom Station, Bedside Station, Medication Station,
> -- Oxygen Station, Cleaning Station, Emergency Go-Bag
> -- ============================================================
> 
> CREATE TABLE IF NOT EXISTS care.care_locations (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   name text NOT NULL,
>   location_type text,
>   parent_location_id uuid,
>   notes text,
>   active boolean NOT NULL DEFAULT true,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
> 
>   CONSTRAINT care_locations_pkey PRIMARY KEY (id),
> 
>   CONSTRAINT care_locations_patient_id_fkey
>     FOREIGN KEY (patient_id)
>     REFERENCES care.patients(id),
> 
>   CONSTRAINT care_locations_parent_location_id_fkey
>     FOREIGN KEY (parent_location_id)
>     REFERENCES care.care_locations(id)
> );
> 
> 
> -- ============================================================
> -- 2. STATION REQUIREMENTS
> -- Defines what each station/location should always contain.
> -- Example:
> -- Bathroom Station should always have gloves, wipes, trash bags,
> -- barrier cream, pads, etc.
> -- ============================================================
> 
> CREATE TABLE IF NOT EXISTS care.station_requirements (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
>   location_id uuid NOT NULL,
>   supply_item_id uuid NOT NULL,
>   par_level numeric,
>   minimum_level numeric,
>   required boolean NOT NULL DEFAULT true,
>   notes text,
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
> 
>   CONSTRAINT station_requirements_pkey PRIMARY KEY (id),
> 
>   CONSTRAINT station_requirements_patient_id_fkey
>     FOREIGN KEY (patient_id)
>     REFERENCES care.patients(id),
> 
>   CONSTRAINT station_requirements_location_id_fkey
>     FOREIGN KEY (location_id)
>     REFERENCES care.care_locations(id),
> 
>   CONSTRAINT station_requirements_supply_item_id_fkey
>     FOREIGN KEY (supply_item_id)
>     REFERENCES care.supply_items(id)
> );
> 
> 
> -- ============================================================
> -- 3. GENERAL CARE EVENTS LOG
> -- Human-readable master timeline.
> --
> -- This does not replace specialized tables like:
> -- care.medication_events
> -- care.supply_events
> -- care.vitals
> -- care.observations
> -- care.encounters
> --
> -- It lets you log meaningful events in one place and optionally
> -- point back to a specialized record using related_table + related_id.
> -- ============================================================
> 
> CREATE TABLE IF NOT EXISTS care.care_events (
>   id uuid NOT NULL DEFAULT gen_random_uuid(),
>   patient_id uuid NOT NULL,
> 
>   event_type text NOT NULL,
>   event_category text,
>   title text NOT NULL,
>   description text,
> 
>   severity text,
>   occurred_at timestamp with time zone NOT NULL DEFAULT now(),
> 
>   related_table text,
>   related_id uuid,
> 
>   caregiver_name text,
> 
>   followup_needed boolean NOT NULL DEFAULT false,
>   followup_status text,
> 
>   metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
>   created_at timestamp with time zone NOT NULL DEFAULT now(),
>   updated_at timestamp with time zone NOT NULL DEFAULT now(),
> 
>   CONSTRAINT care_events_pkey PRIMARY KEY (id),
> 
>   CONSTRAINT care_events_patient_id_fkey
>     FOREIGN KEY (patient_id)
>     REFERENCES care.patients(id)
> );
> 
> 
> -- ============================================================
> -- OPTIONAL BUT SAFE INDEXES
> -- These help app performance later.
> -- They do not change table behavior.
> -- ============================================================
> 
> CREATE INDEX IF NOT EXISTS idx_care_locations_patient_id
>   ON care.care_locations(patient_id);
> 
> CREATE INDEX IF NOT EXISTS idx_care_locations_parent_location_id
>   ON care.care_locations(parent_location_id);
> 
> CREATE INDEX IF NOT EXISTS idx_station_requirements_patient_id
>   ON care.station_requirements(patient_id);
> 
> CREATE INDEX IF NOT EXISTS idx_station_requirements_location_id
>   ON care.station_requirements(location_id);
> 
> CREATE INDEX IF NOT EXISTS idx_station_requirements_supply_item_id
>   ON care.station_requirements(supply_item_id);
> 
> CREATE INDEX IF NOT EXISTS idx_care_events_patient_id
>   ON care.care_events(patient_id);
> 
> CREATE INDEX IF NOT EXISTS idx_care_events_occurred_at
>   ON care.care_events(occurred_at);
> 
> CREATE INDEX IF NOT EXISTS idx_care_events_event_type
>   ON care.care_events(event_type);
> 
> CREATE INDEX IF NOT EXISTS idx_care_events_related
>   ON care.care_events(related_table, related_id);
> 
> 
> -- ============================================================
> -- AFTER CREATING TABLES:
> -- RUN THESE QUERIES TO EXPORT SCHEMA DETAILS FOR CODEX / REVIEW
> -- ============================================================
> 
> 
> -- ============================================================
> -- A. FULL TABLE + FIELD LIST
> -- ============================================================
> 
> SELECT
>   c.table_schema,
>   c.table_name,
>   c.ordinal_position,
>   c.column_name,
>   c.data_type,
>   c.udt_name,
>   c.is_nullable,
>   c.column_default,
>   CASE
>     WHEN pk.column_name IS NOT NULL THEN 'YES'
>     ELSE 'NO'
>   END AS is_primary_key
> FROM information_schema.columns c
> LEFT JOIN (
>   SELECT
>     kcu.table_schema,
>     kcu.table_name,
>     kcu.column_name
>   FROM information_schema.table_constraints tc
>   JOIN information_schema.key_column_usage kcu
>     ON tc.constraint_name = kcu.constraint_name
>    AND tc.table_schema = kcu.table_schema
>    AND tc.table_name = kcu.table_name
>   WHERE tc.constraint_type = 'PRIMARY KEY'
>     AND tc.table_schema = 'care'
> ) pk
>   ON c.table_schema = pk.table_schema
>  AND c.table_name = pk.table_name
>  AND c.column_name = pk.column_name
> WHERE c.table_schema = 'care'
> ORDER BY c.table_name, c.ordinal_position;
> 
> 
> -- ============================================================
> -- B. FOREIGN KEY MAP
> -- Shows how tables connect.
> -- ============================================================
> 
> SELECT
>   tc.table_schema,
>   tc.table_name,
>   kcu.column_name,
>   ccu.table_schema AS foreign_table_schema,
>   ccu.table_name AS foreign_table_name,
>   ccu.column_name AS foreign_column_name,
>   tc.constraint_name
> FROM information_schema.table_constraints AS tc
> JOIN information_schema.key_column_usage AS kcu
>   ON tc.constraint_name = kcu.constraint_name
>  AND tc.table_schema = kcu.table_schema
> JOIN information_schema.constraint_column_usage AS ccu
>   ON ccu.constraint_name = tc.constraint_name
>  AND ccu.table_schema = tc.table_schema
> WHERE tc.constraint_type = 'FOREIGN KEY'
>   AND tc.table_schema = 'care'
> ORDER BY tc.table_name, kcu.column_name;
> 
> 
> -- ============================================================
> -- C. TABLE LIST ONLY
> -- ============================================================
> 
> SELECT
>   table_schema,
>   table_name,
>   table_type
> FROM information_schema.tables
> WHERE table_schema = 'care'
> ORDER BY table_name;
> 
> 
> -- ============================================================
> -- D. INDEX LIST
> -- Useful to confirm indexes were created.
> -- ============================================================
> 
> SELECT
>   schemaname,
>   tablename,
>   indexname,
>   indexdef
> FROM pg_indexes
> WHERE schemaname = 'care'
> ORDER BY tablename, indexname;
> 
> 
> -- ============================================================
> -- E. CHECK CONSTRAINTS
> -- Useful for fields with allowed values.
> -- ============================================================
> 
> SELECT
>   tc.table_schema,
>   tc.table_name,
>   tc.constraint_name,
>   cc.check_clause
> FROM information_schema.table_constraints tc
> JOIN information_schema.check_constraints cc
>   ON tc.constraint_name = cc.constraint_name
> WHERE tc.table_schema = 'care'
>   AND tc.constraint_type = 'CHECK'
> ORDER BY tc.table_name, tc.constraint_name;
> ```
> 
> One note: because Supabase usually runs one result grid per query, you may need to highlight and run the creation section first, then run sections **A–E** one at a time. Supabase SQL Editor can be annoying like that because, naturally, the useful thing must be slightly inconvenient.

### Assistant
> I’ll treat these as the outputs from Supabase and sanity-check whether the new tables landed cleanly, then I’ll tell you what’s missing or what Codex should do next.

### Assistant
> Yep — the additions **worked**.
> 
> The file named **Care Stations, Requirements, and Event Timeline** confirms these new tables exist:
> 
> ```text
> care.care_locations
> care.station_requirements
> care.care_events
> ```
> 
> But your **List Columns with Primary Key Flag** export is incomplete. It only has **100 rows** and stops around:
> 
> ```text
> care.device_profiles
> ```
> 
> That means Supabase probably only exported the first page of results. Annoying, but normal Supabase nonsense.
> 
> Use this better query instead. It compresses each table into one row, so you can export the whole schema without hitting the 100-row grid issue.
> 
> ```sql
> -- ============================================================
> -- MOM'S CARE APP — FULL SCHEMA SUMMARY, ONE ROW PER TABLE
> -- Better for Supabase export / Codex review
> -- ============================================================
> 
> SELECT
>   c.table_schema,
>   c.table_name,
>   jsonb_agg(
>     jsonb_build_object(
>       'position', c.ordinal_position,
>       'column_name', c.column_name,
>       'data_type', c.data_type,
>       'udt_name', c.udt_name,
>       'is_nullable', c.is_nullable,
>       'column_default', c.column_default,
>       'is_primary_key',
>         CASE
>           WHEN pk.column_name IS NOT NULL THEN true
>           ELSE false
>         END
>     )
>     ORDER BY c.ordinal_position
>   ) AS columns
> FROM information_schema.columns c
> LEFT JOIN (
>   SELECT
>     kcu.table_schema,
>     kcu.table_name,
>     kcu.column_name
>   FROM information_schema.table_constraints tc
>   JOIN information_schema.key_column_usage kcu
>     ON tc.constraint_name = kcu.constraint_name
>    AND tc.table_schema = kcu.table_schema
>    AND tc.table_name = kcu.table_name
>   WHERE tc.constraint_type = 'PRIMARY KEY'
>     AND tc.table_schema = 'care'
> ) pk
>   ON c.table_schema = pk.table_schema
>  AND c.table_name = pk.table_name
>  AND c.column_name = pk.column_name
> WHERE c.table_schema = 'care'
> GROUP BY c.table_schema, c.table_name
> ORDER BY c.table_name;
> ```
> 
> Then run this for the relationship map:
> 
> ```sql
> -- ============================================================
> -- MOM'S CARE APP — FOREIGN KEY MAP
> -- Shows how tables connect
> -- ============================================================
> 
> SELECT
>   tc.table_schema,
>   tc.table_name,
>   kcu.column_name,
>   ccu.table_schema AS foreign_table_schema,
>   ccu.table_name AS foreign_table_name,
>   ccu.column_name AS foreign_column_name,
>   tc.constraint_name
> FROM information_schema.table_constraints AS tc
> JOIN information_schema.key_column_usage AS kcu
>   ON tc.constraint_name = kcu.constraint_name
>  AND tc.table_schema = kcu.table_schema
> JOIN information_schema.constraint_column_usage AS ccu
>   ON ccu.constraint_name = tc.constraint_name
>  AND ccu.table_schema = tc.table_schema
> WHERE tc.constraint_type = 'FOREIGN KEY'
>   AND tc.table_schema = 'care'
> ORDER BY tc.table_name, kcu.column_name;
> ```
> 
> And this one specifically verifies the three new tables:
> 
> ```sql
> -- ============================================================
> -- VERIFY NEW TABLES
> -- ============================================================
> 
> SELECT
>   table_schema,
>   table_name,
>   column_name,
>   data_type,
>   udt_name,
>   is_nullable,
>   column_default
> FROM information_schema.columns
> WHERE table_schema = 'care'
>   AND table_name IN (
>     'care_locations',
>     'station_requirements',
>     'care_events'
>   )
> ORDER BY table_name, ordinal_position;
> ```
> 
> Current read:
> 
> ```text
> Status: good.
> New tables: created.
> Existing schema: not broken.
> Problem: column export was truncated at 100 rows.
> Next move: run the compressed full-schema query above and export that.
> ```
> 
> Tiny win, not glamorous, but this is the right database spine. Now the care app can track **where things belong**, **what each station requires**, and **what actually happened over time** without mangling the existing medication/vitals/supply tables.

### User
> yes, and i need to make sure my google sheets tables match this schema its how i audit what isreal vs what the app has or can do correctly.

### Assistant
> You’re exactly right: Google Sheets is your audit layer, but Supabase is the source of truth. I’m going to turn the schema exports you uploaded into a clean audit workbook/template so you can paste Sheet headers and instantly see mismatches.

### Assistant
> Exactly. That is the correct audit pattern:
> 
> ```text
> Google Sheets = human audit / operational checklist
> Supabase = app truth / relational database
> Audit goal = prove what exists in Sheets vs what the app can actually store/use
> ```
> 
> I made you a workbook for that:
> 
> [Download the Mom’s Care Supabase ↔ Google Sheets Audit Workbook](sandbox:/mnt/data/moms_care_supabase_google_sheets_audit.xlsx)
> 
> It includes:
> 
> ```text
> README
> Supabase_Schema
> Foreign_Keys
> New_Tables_Verified
> Table_Summary
> Google_Sheets_Headers
> Audit
> Google_Extras_Check
> Suggested_Sheets
> ```
> 
> How to use it:
> 
> 1. Open the workbook.
> 2. Go to **Google_Sheets_Headers**.
> 3. Paste your Google Sheet tab names and column/header names.
> 4. Go to **Audit** to see what Supabase expects but Google Sheets is missing.
> 5. Go to **Google_Extras_Check** to see what Google Sheets has that Supabase does not model yet.
> 
> The real audit logic is:
> 
> ```text
> Missing in Google Sheets = app can store it, but your sheet is not tracking it.
> Extra in Google Sheets = your sheet tracks it, but the app/database may not support it yet.
> Matched = aligned.
> ```
> 
> Important callout: do **not** blindly force Google Sheets to include every technical Supabase field like:
> 
> ```text
> id
> patient_id
> created_at
> updated_at
> metadata_json
> ```
> 
> Those are database plumbing. For Sheets, you mainly care about the human-operational fields: meds, vitals, events, supplies, station requirements, care notes, oxygen, encounters, and follow-ups.
> 
> The best next move is to paste/export your actual Google Sheets headers into the **Google_Sheets_Headers** tab, then the workbook will tell us where reality and the app schema are out of sync.
