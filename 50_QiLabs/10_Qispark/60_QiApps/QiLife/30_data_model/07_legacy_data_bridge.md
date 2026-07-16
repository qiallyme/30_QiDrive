---
layout: page
title: Legacy Data Bridge
slug: legacy-data-bridge
status: publish
updated_at: "2026-06-29"
tags:
  - qispark
source_type: manual
summary: ""
created_at: ""
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ""
canonical_ref: ""
template_key: master-template
---

# Legacy Data Bridge
QiLife should not inherit old Supabase schema chaos.

## Doctrine

- QiLife uses a clean canonical schema.
- Existing Supabase tables are legacy sources.
- Preserve/export Supabase data.
- Inventory tables, stage legacy rows.
- Selectively migrate useful records.
- Import messy useful rows as legacy QiBits.
- Supabase is not the runtime source of truth.

## Planned Legacy Bridge Tables

- `legacy_sources`
- `legacy_tables`
- `legacy_records`
- `legacy_mappings`
- `legacy_import_runs`
