---
layout: page
title: 30 Component Map
slug: 30-component-map
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
uid: 3a4e7043d6e1487fa54959e30179fa12
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Component Map

> Quarantine notice: this diagram reflects the older QiOS and QiOne layer model. It is retained for salvage, not as the active QiAccess Start component map. See `08_appendices/20_legacy/qiaccess_start_legacy_quarantine.md`.

## System Components

```
┌─────────────────────────────────────────────┐
│              DELIVERY LAYER                  │
│  QiPortals · Web · Admin · Search · Setup    │
└────────────────────┬────────────────────────┘
                     │
┌────────────────────▼────────────────────────┐
│             APPLICATION LAYER                │
│     QiOne Portal · Tools · Interfaces        │
└────────────────────┬────────────────────────┘
                     │
┌────────────────────▼────────────────────────┐
│              PLATFORM LAYER                  │
│       qione: tenants · members · RBAC        │
│         Supabase Auth: identity              │
└────────────────────┬────────────────────────┘
                     │
┌────────────────────▼────────────────────────┐
│               DOMAIN LAYER                   │
│  qicase · qihome · qitax · qivault          │
│  qichronicle · qicms · qiknowledge          │
└────────────────────┬────────────────────────┘
                     │
┌────────────────────▼────────────────────────┐
│                CORE LAYER                    │
│  qiarchive: registration + identity spine    │
│  qigraph: derived graph (Neo4j projection)   │
│  qially: AI sessions + memory embeddings     │
│  qisys: jobs + workers + system events       │
└─────────────────────────────────────────────┘
```

## Local ↔ Cloud Component Boundary

```
LOCAL MACHINE                    CLOUD (Supabase)
─────────────────                ────────────────
File watcher          →          qiarchive.archive_files
Ingest pipeline       →          qiarchive.ingest_jobs
OCR + Extractor       →          qiarchive.archive_chunks
Embedding engine      →          pgvector (archive_chunks.embedding)
Local API             ↔          App APIs
```

## Key Component Relationships

| From | To | Relationship |
|---|---|---|
| `qiarchive` | All domain schemas | Provides `archive_id` FK anchor |
| `qione.tenants` | All domain schemas | Provides `tenant_id` FK for RLS |
| `auth.users` | `qione.tenant_members` | Identity mapping |
| `qiarchive.archive_chunks` | `qilly.memory_embeddings` | Embedding lineage |
| `qigraph.master_index` | All schemas | Cross-domain object index |
