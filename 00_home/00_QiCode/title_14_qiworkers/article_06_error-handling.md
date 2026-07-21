---
layout: article
title: Article 6. Error Handling
slug: qicode-title-14-article-06-error-handling
summary: ""
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
qicode_title: 14
qicode_article: 6
parent_title: Title 14. QiWorkers
canonical_ref: QiCode T14.A06
source_type: manual
---

## Article 6. Error Handling

Stable ID: `T14.A06`

### Sec. 14.06.010. Error Policy

Stable ID: `T14.A06.S010`

- `Line 1` Workers must be observable: every worker must emit structured logs accessible without SSH. (`Sec. 14.06.010.L001`; stable ID `T14.A06.S010.L001`)
- `Line 2` Workers must be recoverable: failure state must not require manual reconstruction of lost work. (`Sec. 14.06.010.L002`; stable ID `T14.A06.S010.L002`)
- `Line 3` Workers must be documented: the runbook for each worker must exist before it is deployed. (`Sec. 14.06.010.L003`; stable ID `T14.A06.S010.L003`)


