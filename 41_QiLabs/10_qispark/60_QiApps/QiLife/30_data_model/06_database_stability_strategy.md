---
layout: page
title: Database Stability Strategy
slug: database-stability-strategy
status: active
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

# Database Stability Strategy
Use SQLite for local-first development now, but design for future Postgres on QiServer.

## Strategy

- Use stable IDs (ULID preferred).
- Migrations from day one.
- Raw vs interpreted data separation.
- `activity_log` as append-only history.
- `daily_summaries` for generated/reflected daily summaries.
- `links` table for relationships.
- `ai_outputs`, `ai_drafts`, `review_events`, `trust_rules`.
- Soft delete/archive fields.
- `amount_cents` for money.
- File metadata in DB, blobs on disk.

## Service Boundaries

Do not add Qdrant, Redis, Neo4j, Supabase, R2, or MinIO in first code pass. Design boundaries for them:
- Postgres = future structured source of truth
- Qdrant = future semantic memory
- Redis = future background jobs
- Neo4j = optional future graph mirror
- R2/MinIO = future blob provider
