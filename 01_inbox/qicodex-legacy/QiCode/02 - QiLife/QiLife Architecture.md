---
title: "QiLife Architecture"
aliases:
  - "QiLife Placement and Architecture"
system: "QiOS"
document_type: "architecture"
status: "active-doctrine"
version: "1.0"
canonical: true
updated: "2026-07-18"
source:
  - "QiCode Documentation database"
  - "QiLife Data Model Spine"
tags:
  - "qicode"
  - "qios"
  - "qilife"
---
> **Parent:** [[00 - QiCode Home|QiCode Home]]
> **Related:** [[QiLife Doctrine|Doctrine]] · [[QiLife Data Model|Data Model]] · [[QiLife Workflows|Workflows]]

# QiLife Architecture

> **Title:** 06 — QiLife  
> **Chapter:** 06.02 — Architecture & Placement

This document defines QiLife’s position within QiOS, its canonical homes, and its database portability boundary.

## § 06.02.001 — Position in QiOS

```text
QiOS
├── QiSpark
│   └── homepage, docs, doctrine, maps, guides, bookmarks
├── QiApps
│   └── QiLife, MomCare, utilities, dashboards, experiments
├── QiDrive
│   └── files, evidence, documents, assets, exports, archives
├── QiServer
│   └── runtime, cockpit, containers, databases, services, local AI
├── QiConnect
│   └── Google, GitHub, Supabase, imports, exports, sync jobs
└── QiArchive
    └── old systems, deprecated builds, frozen exports
```

QiLife lives in **QiApps**.

- QiSpark documents it.
- QiDrive stores its related files.
- QiServer may run it.
- QiConnect may synchronize data into or out of it.
- QiArchive preserves inactive versions.

## § 06.02.002 — Canonical Placement

- **Application home:** `QiApps/QiLife`
- **Documentation home:** `QiSpark/docs`
- **File backbone:** `QiDrive`

QiLife remains in the application layer. Doctrine and published documentation belong in QiSpark; files belong in QiDrive; runtime services belong in QiServer; synchronization pathways belong in QiConnect; inactive versions belong in QiArchive.

## § 06.02.003 — Database Portability

QiLife’s data model must remain database-portable.

It may begin locally with SQLite for speed, but the schema must be able to move to PostgreSQL or Supabase without conceptual redesign.
