---
layout: page
title: Migrations
slug: migrations
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
uid: f640434239f247999d8ef11893766329
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Migrations

## Rule

All schema changes must be captured in migrations.

## Migration Naming

```text
YYYYMMDDHHMM_description.sql
```

## Development Practice

- Never manually patch production without recording the migration.
- Keep destructive migrations explicit.
- Seed demo data separately from schema.
