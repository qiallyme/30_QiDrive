---
layout: adr
title: ADR-0002: Single Domain Rule
slug: adr-0002-single-domain-rule
status: active
updated_at: "2026-06-29"
tags:
  - qispark
  - decisions
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

# ADR-0002: Single Domain Rule

**Date**: 2026-03-27
**Status**: Accepted

## Context

Early schema design placed domain logic in the `public` schema and mixed concerns across tables. This created unclear ownership and made RLS enforcement fragile.

## Decision

Every domain in QiOS gets **one canonical Postgres schema**. No domain logic lives in `public`. The mapping is enforced in `registry/domain_registry.yaml`.

Rules:
- One schema per domain (e.g., `qicase`, `qivault`, `qihome`)
- All domain tables must carry `tenant_id` for RLS isolation
- `public` schema is reserved for legacy stubs and global auth-adjacent data only
- Cross-domain access must go through the Platform RBAC layer

## Consequences

- All new tables are created in their domain schema, never in `public`
- Domain registry must be updated when a new schema is created
- Existing `public` tables (`todos`, `nods_page`) are marked legacy and will not be extended
