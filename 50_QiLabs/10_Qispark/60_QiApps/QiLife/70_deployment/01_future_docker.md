---
layout: page
title: Future Docker Deployment Plan
slug: future-docker-deployment-plan
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
uid: cfb2317bf3494eb6b80b20ba8f0877bc
canonical_ref: ""
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
