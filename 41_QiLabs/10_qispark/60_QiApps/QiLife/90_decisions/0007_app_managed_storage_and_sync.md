---
layout: adr
title: Decision 0007: App-Managed Storage and Sync
slug: decision-0007-app-managed-storage-and-sync
status: active
updated_at: "2026-06-29"
tags:
  - qispark
  - decisions
source_type: manual
summary: ""
created_at: ""
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ""
canonical_ref: ""
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
