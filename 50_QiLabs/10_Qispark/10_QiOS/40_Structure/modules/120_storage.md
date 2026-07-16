---
layout: page
title: 120 Storage
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
