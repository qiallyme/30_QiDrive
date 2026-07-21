---
layout: page
title: Public Interfaces
slug: public-interfaces
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
uid: a8aaf9e90fe44977b66f7f43a1b5c24d
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Interfaces

> Quarantine notice: this page contains useful interface rules, but parts of its setup and tenant language belong to the older platform model. Treat it as reference-only until revalidated. See `08_appendices/20_legacy/qiaccess_start_legacy_quarantine.md`.

Interfaces are specialized views and interaction surfaces within the QiOS ecosystem.

## Interface Types

| Interface | Purpose | Source Schema |
|---|---|---|
| **Search UI** | Find archive records by metadata or semantic query | `qiarchive` + pgvector |
| **Review UI** | Human review of pipeline-routed documents | `qiarchive.ingest_jobs` |
| **Archive UI** | Browse and inspect registered files | `qiarchive.archive_files` |
| **Chatbot UI** | AI-powered retrieval with provenance-aware answers | `qially` + pgvector + Neo4j |
| **Setup / Onboarding UI** | Tenant and module configuration | `qione` |

## Interface Law

* Every interface must authenticate before accessing tenant data
* Chatbot UI must display source references (archive_id / chunk_id) — it may not answer without provenance
* Review UI decisions must update pipeline state in `qiarchive.ingest_jobs`, not create shadow records
* Search results must link back to canonical archive records, not to derived copies
