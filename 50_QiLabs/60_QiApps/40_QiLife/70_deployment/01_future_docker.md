---
layout: page
title: 01 Future Docker
slug: 01-future-docker
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
uid: fcb84e80891346c89f00f54473092716
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
