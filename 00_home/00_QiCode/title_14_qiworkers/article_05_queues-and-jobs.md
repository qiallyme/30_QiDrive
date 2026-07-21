---
layout: article
title: Article 5. Queues and Jobs
slug: qicode-title-14-article-05-queues-and-jobs
summary: ""
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
qicode_title: 14
qicode_article: 5
parent_title: Title 14. QiWorkers
canonical_ref: QiCode T14.A05
source_type: manual
---

## Article 5. Queues and Jobs

Stable ID: `T14.A05`

### Sec. 14.05.010. Job Queue Policy

Stable ID: `T14.A05.S010`

- `Line 1` Long-running or deferred operations must use a queue; fire-and-forget is not acceptable for critical workflows. (`Sec. 14.05.010.L001`; stable ID `T14.A05.L010.L001`)
- `Line 2` Queue failures must be logged, alerted, and recoverable without manual data reconstruction. (`Sec. 14.05.010.L002`; stable ID `T14.A05.S010.L002`)
- `Line 3` Job retention and dead-letter policy must be documented for each queue. (`Sec. 14.05.010.L003`; stable ID `T14.A05.S010.L003`)


