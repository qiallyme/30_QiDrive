---
layout: page
title: 0007 App Managed Storage And Sync
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

# Decision 0007: App-Managed Storage and Sync

## Context
Managing files and syncing manually across folders is brittle and error-prone.

## Decision
QiLife will act as a control center managing its own storage footprint (DB, file vault, exports). Folders will be projections of metadata rather than the source of truth.

## Consequences
- Eliminates manual folder management.
- Requires building storage management and health check features.
- Clear separation between repo (code), private data (DB/files), and exports (Drive/QiNexus).
