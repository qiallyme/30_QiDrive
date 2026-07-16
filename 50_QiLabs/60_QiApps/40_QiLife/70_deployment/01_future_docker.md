---
layout: page
title: 01 Future Docker
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

# Future Docker Deployment Plan

## Services

1. Frontend
2. Backend
3. SQLite-backed data volume for v1

## Canonical Database Path

Use `sqlite:////app/data/db/qilife.sqlite` inside the backend container.

## Compose Direction

- Mount `/app/data` as a persistent volume.
- Keep the repo docs mounted or baked into the image so the importer can read `docs/`.
- Preserve the same database path convention used in local development.

Postgres remains a later migration target, not a v1 dependency.
