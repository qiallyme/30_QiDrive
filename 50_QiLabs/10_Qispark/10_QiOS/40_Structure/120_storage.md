---
layout: page
title: Storage
slug: storage
status: publish
updated_at: "2026-07-16T06:49:38-04:00"
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
uid: 190ed61d1ad44c3a8388aaf5cd477b08
canonical_ref: ""
template_key: master-template
---

# Storage

Storage is handled primarily via QiNexus and the local persistence structure.

## Storage Backbone

- Google Drive/QiNexus remains the primary storage backbone.

## Path Doctrine

- /srv/qios/data is for persistent app data.
- /srv/qios/stacks is for Docker Compose runtime stacks.
- /srv/qios/repos is for cloned Git repos and coding work.

## Conditional / Future Elements

*Note: Supabase Postgres and pgvector are not active doctrine unless a future retrieval pipeline explicitly needs them.*
