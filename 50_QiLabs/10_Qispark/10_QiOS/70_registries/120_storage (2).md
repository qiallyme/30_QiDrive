---
layout: page
title: 120 Storage
slug: 120-storage
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
uid: a83a30c20ffe44ce9a97ade5d391544f
canonical_ref: ""
source_type: manual
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
