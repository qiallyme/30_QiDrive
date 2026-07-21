---
layout: article
title: Article 4. Sync and Automation
slug: qicode-title-14-article-04-sync-and-automation
summary: ""
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
qicode_title: 14
qicode_article: 4
parent_title: Title 14. QiWorkers
canonical_ref: QiCode T14.A04
source_type: manual
---

## Article 4. Sync and Automation

Stable ID: `T14.A04`

### Sec. 14.04.010. Sync Governance

Stable ID: `T14.A04.S010`

- `Line 1` Sync workers reconcile state between QiLabs systems; they must be idempotent and recoverable. (`Sec. 14.04.010.L001`; stable ID `T14.A04.S010.L001`)
- `Line 2` Automation workflows (n8n or equivalent) that cross domain boundaries must be documented in QiWorkers. (`Sec. 14.04.010.L002`; stable ID `T14.A04.S010.L002`)
- `Line 3` Sync operations must not silently overwrite canonical records without a conflict resolution policy. (`Sec. 14.04.010.L003`; stable ID `T14.A04.S010.L003`)


