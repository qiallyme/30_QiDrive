---
layout: page
title: Database Stability Strategy
slug: database-stability-strategy
status: publish
updated_at: "2026-07-16T06:49:40-04:00"
tags: []
  - qispark
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
uid: 9252e5e0115d49b29efd4f883a5739b2
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
