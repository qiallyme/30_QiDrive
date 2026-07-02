---
layout: page
title: 02 Future Qiserver
slug: ""
summary: ""
status: active
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

# QiServer Deployment (Future)

This document is a post-v1 deployment target. It should not alter the local-first v1 doctrine.

## Canonical Production Data Path

- DB path: `/var/lib/qilife/data/db/qilife.sqlite`
- backups path: `/mnt/backups/qilife`

## Backup Rule

Use SQLite's online backup API against the canonical path:

```bash
sqlite3 /var/lib/qilife/data/db/qilife.sqlite ".backup '/mnt/backups/qilife/qilife_YYYYMMDD_HHMM.sqlite'"
```

## Repo Docs Doctrine

- Repo `docs/` remain the canonical authoring source for system knowledge.
- The app imports those docs into `knowledge_items` as read-only records.
- Reverse sync from in-app edited knowledge to an external markdown vault is out of scope for v1.
