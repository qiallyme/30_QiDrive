---
layout: adr
title: ADR-0019: Directus as Supabase Admin and API Layer; NocoDB Deprecated
slug: adr-0019-directus-as-supabase-admin-and-api-layer-nocodb-deprecated
status: publish
updated_at: "2026-07-16T06:49:38-04:00"
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
uid: ff30339235124a4ab68f1c9127af8234
canonical_ref: ""
template_key: master-template
---

# ADR-0019: Directus as Supabase Admin and API Layer; NocoDB Deprecated

## Status

Accepted on 2026-06-15.

## Context

QiSystem requires a flexible, high-productivity administration dashboard, visual CRUD editor, and REST/GraphQL API layer for managing system records, libraries, staging tables, and care logs.

NocoDB was previously introduced as the alpha visual data interface. While NocoDB served its purpose during initial schema exploration, it has limitations in API flexibility, system metadata structure, role-based access control (RBAC), and enterprise robustness. Directus provides a more mature, schema-first, non-intrusive data administration UI and instant API gateway that runs natively on top of existing PostgreSQL databases.

## Decision

- **Directus is designated as the canonical admin UI, management interface, and visual API layer** connected directly to the Supabase/Postgres database.
- **NocoDB is deprecated** as the alpha data UI. Existing NocoDB setups are scheduled for decommissioning upon validation of the Directus instance.
- **Supabase/Postgres remains the absolute database engine and source of truth**. All tables, relationships, and custom database types reside natively in PostgreSQL.
- **Directus is an administration layer, not a schema authority**. Directus must not be used to blindly or implicitly create or update canonical database schemas.
- **Schema changes must be driven by versioned code**. Any changes to database layouts (adding columns, tables, rules, triggers) must be coded as migration scripts in `sql/` and promoted as timestamped SQL migrations under `migrations/`.
- **System Isolation**: Directus system and metadata tables (prefixed with `directus_`) will reside in the database to store layouts, permissions, and settings. These tables must be isolated from QiSystem domain schemas (such as `qisystem`, `qifinance`, and `qicare`).
- **Configuration Tracking**: Directus collection layouts, visual formatting settings, and relations should be documented, backed up, or snapshotted using Directus Schema API tools (`npx directus schema apply/snapshot`) where applicable.

## Consequences & Safety Warning

- **Do Not Manage Blindly**: Changes made through the Directus admin panel that implicitly alter database columns must be immediately backported into versioned migration SQL code.
- **Data Dictionary Mapping**: The Directus configuration must align with the canonical data models defined in `schemas/data_dictionary.md` and `schemas/qisystem.md`.

## Supersedes

- Prior workspace choices designating NocoDB as the primary database admin UI.
- Direct-to-client exposures that bypass Supabase RLS (Row Level Security) boundaries without explicit policy declarations.
