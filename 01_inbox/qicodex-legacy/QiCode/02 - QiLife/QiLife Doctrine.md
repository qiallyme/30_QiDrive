---
title: "QiLife Doctrine"
aliases:
  - "QiLife Purpose and Doctrine"
system: "QiOS"
document_type: "doctrine"
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
> **Related:** [[QiLife Architecture|Architecture]] · [[QiLife Data Model|Data Model]] · [[QiLife Workflows|Workflows]]

# QiLife Doctrine

> **Title:** 06 — QiLife  
> **Chapter:** 06.01 — Purpose, Boundaries & Scope

This document is the canonical statement of what QiLife is, what it is not, and what belongs in V1.

## § 06.01.001 — Purpose & Operating Doctrine

QiLife is the private life operating application inside **QiApps**.

It exists to capture, organize, relate, retrieve, review, and act on real-life information.

QiLife is not:

- the documentation site;
- the file drive;
- the server or runtime layer;
- a full finance system; or
- a CRM.

QiLife is the structured life-operating layer. It answers:

> What came in? What does it mean? Who or what is connected? What requires action? Where does it belong?

##### Doctrine Rules

- User-created records use **ULIDs**.
- Static lookup tables may use stable text keys.
- Raw capture is preserved.
- AI output is stored separately from approved truth.
- The timeline is a projection, not a separate core table.
- Files live in QiDrive; QiLife stores metadata and links.
- Notes and reflections are QiBit types, not separate tables.
- Finance-specific records remain outside QiLife core unless the need is proven.
- Properties, tags, metadata, and links should be used before creating more tables.

##### Final Operating Rule

QiLife should make life easier to operate.

A table, field, module, or feature does not belong in V1 unless it helps capture, clarify, connect, act, retrieve, review, or preserve truth.

Keep the spine lean:

- Use properties before tables.
- Use links before duplication.
- Use threads before fake modules.
- Use QiDrive for files.
- Use QiSpark for documentation.
- Use QiLife for living operations.
- Use QiFinance when finance earns its own specialized module.

## § 06.01.002 — Core V1 Scope

QiLife V1 starts with capture, buckets, threads, actions, people, events, documents, links, and review.

Do not start with:

- finance;
- advanced AI; or
- perfect UI.
