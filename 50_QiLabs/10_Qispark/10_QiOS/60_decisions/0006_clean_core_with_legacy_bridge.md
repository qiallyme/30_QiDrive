---
layout: page
title: 0006 Clean Core With Legacy Bridge
slug: 0006-clean-core-with-legacy-bridge
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
uid: 2805ac747112497f8b21636e208219b2
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Decision 0006: Clean Core with Legacy Bridge

## Context
QiLife is replacing an older Supabase-backed system that has a messy schema.

## Decision
QiLife will use a clean canonical schema locally in SQLite, avoiding inheritance of the old Supabase schema chaos. A Legacy Data Bridge will be built to map and selectively import useful records as legacy QiBits.

## Consequences
- Supabase is no longer the runtime source of truth.
- We need explicit bridge tables (`legacy_sources`, `legacy_tables`, etc.).
- The core data model remains clean and agent-friendly.
