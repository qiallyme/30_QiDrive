---
layout: page
title: 01 Product Doctrine
slug: 01-product-doctrine
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
uid: 3ed66c9645fd4877b87344c144b1e9f3
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Product Doctrine

## Non-Negotiables

1. **QiBit-first capture**
   Every important item starts as a QiBit or links back to one for provenance.
2. **Timeline-first retrieval**
   Chronology is the primary retrieval spine across modules.
3. **Bucket-aligned hierarchy**
   Buckets mirror the QiNexus/QiAccess structure and remain stable.
4. **Personal LifeDesk metaphor**
   QiLife behaves like a single-agent private helpdesk for life, not a generic todo app or CRM.
5. **Context Dock over separate wiki**
   Knowledge appears beside the active object; it is not split into a separate Wiki.js-style product.
6. **Repo docs are canonical during build**
   Repository docs are the system source of truth and are indexed into the app later as read-only imported knowledge.
7. **Raw evidence stays separate from interpretation**
   `qibits.raw_capture`, file metadata, and append-only history are preserved apart from summaries, AI output, and reflections.
8. **Human review for AI**
   AI suggests and stages outputs; Cody approves before structured records are committed.
9. **SQLite first, Postgres later**
   V1 is local-first SQLite. Migration to Postgres happens only after the model proves stable and multi-device pressure justifies it.

## Vocabulary

Use these terms consistently:

- **QiLife**: the product
- **Personal LifeDesk**: the operating metaphor
- **QiBit**: atomic captured life item
- **Bucket**: top-level structural domain
- **Thread**: case, project, storyline, or ongoing situation
- **Action**: task or work order
- **Step**: subtask within an action
- **Context Dock**: embedded side panel for relevant knowledge/context
- **Ask QiLife**: AI query layer

Avoid introducing parallel vocabulary such as `ticket`, `queue`, `note table`, `reflection table`, or `timeline entry table` as canonical database concepts for v1.
