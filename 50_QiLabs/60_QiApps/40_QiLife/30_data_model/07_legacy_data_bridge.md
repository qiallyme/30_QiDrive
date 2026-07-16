---
layout: page
title: 07 Legacy Data Bridge
slug: 07-legacy-data-bridge
summary: ""
status: publish
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
uid: 6311bc2aa31e42f1baf6b3ceb26c611e
canonical_ref: ""
source_type: manual
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
