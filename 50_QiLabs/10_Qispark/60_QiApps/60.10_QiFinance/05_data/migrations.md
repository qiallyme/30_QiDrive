---
layout: page
title: Migrations
slug: ""
summary: ""
status: publish
created_at: ""
updated_at: ""
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ""
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
