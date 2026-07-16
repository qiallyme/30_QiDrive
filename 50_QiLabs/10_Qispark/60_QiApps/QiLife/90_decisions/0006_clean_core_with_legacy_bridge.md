---
layout: adr
title: Decision 0006: Clean Core with Legacy Bridge
slug: decision-0006-clean-core-with-legacy-bridge
status: publish
updated_at: "2026-07-16T06:49:40-04:00"
tags: []
  - qispark
  - decisions
source_type: manual
summary: ""
created_at: "2026-07-16T06:19:39-04:00"
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: 4d81c6d6d66d446592f6caaca6d2a334
canonical_ref: ""
template_key: master-template
---

# Decision 0006: Clean Core with Legacy Bridge

> **Superseded by ADR-0018 on 2026-06-14.** Retained as historical decision evidence. Supabase is now canonical; SQLite is transitional only.

## Context

QiLife is replacing an older Supabase-backed system that has a messy schema.

## Decision

QiLife will use a clean canonical schema locally in SQLite, avoiding inheritance of the old Supabase schema chaos. A Legacy Data Bridge will be built to map and selectively import useful records as legacy QiBits.

## Consequences

- Supabase is no longer the runtime source of truth.
- We need explicit bridge tables (`legacy_sources`, `legacy_tables`, etc.).
- The core data model remains clean and agent-friendly.
