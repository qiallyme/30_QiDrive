---
layout: article
title: Article 7. Deployment Rules
slug: qicode-title-14-article-07-deployment-rules
summary: ""
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
qicode_title: 14
qicode_article: 7
parent_title: Title 14. QiWorkers
canonical_ref: QiCode T14.A07
source_type: manual
---

## Article 7. Deployment Rules

Stable ID: `T14.A07`

### Sec. 14.07.010. Deployment Governance

Stable ID: `T14.A07.S010`

- `Line 1` Workers are deployed to QiServer (Docker), Cloudflare Workers, or an equivalent governed runtime. (`Sec. 14.07.010.L001`; stable ID `T14.A07.S010.L001`)
- `Line 2` Deployment configuration must be version-controlled in `25_QiWorkers`. (`Sec. 14.07.010.L002`; stable ID `T14.A07.S010.L002`)
- `Line 3` Environment secrets must not be committed to source control; use `.env.example` and a secrets manager. (`Sec. 14.07.010.L003`; stable ID `T14.A07.S010.L003`)


