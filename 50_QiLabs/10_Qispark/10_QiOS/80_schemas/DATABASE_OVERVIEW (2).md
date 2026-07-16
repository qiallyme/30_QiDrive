---
layout: page
title: Database Overview
slug: database-overview
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
uid: 5cde7454f8b74433bf22886a91ef8b33
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Database Overview

## Authority

Supabase Postgres is the canonical structured-data store for QiLife under ADR-0018. SQLite is deprecated and may support legacy, local, or transitional operation only.

## Why Supabase

- Centralized relational data.
- Cross-device and API access.
- Normalized CSV import targets.
- Database-enforced relationships and constraints.
- Controlled migration history.

## Schema Per Module

Postgres schemas make ownership and security boundaries explicit without inventing separate databases:

- `qi_entities` owns persistent who/what records.
- `qi_events` owns QiBits.

A new schema requires a proven ownership need and accepted reconciliation decision.

## API Exposure

The custom schemas are private by default. RLS is enabled, but Data API exposure, grants, and policies are deferred until user identity and authorization rules are approved.

## Files

QiNexus remains authoritative for files, exports, references, archives, and backups. Paperless is a document-processing and application surface. Supabase stores references and structured metadata, not duplicate file authority.

## Transition

The existing SQLite database and SQLModel models are migration evidence. This baseline does not deploy, copy, transform, or delete SQLite data. A later cutover plan must define mapping, validation, backup, rollback, and application integration.
