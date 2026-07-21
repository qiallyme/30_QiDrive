---
layout: article
title: Article 8. Path Doctrine
slug: qicode-title-13-article-08-path-doctrine
summary: ""
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
qicode_title: 13
qicode_article: 8
parent_title: Title 13. QiServer
canonical_ref: QiCode T13.A08
source_type: manual
---

## Article 8. Path Doctrine

Stable ID: `T13.A08`

### Sec. 13.08.010. Server Path Standards

Stable ID: `T13.A08.S010`

- `Line 1` QiServer runtime root is `/srv/qios`; repos live in `/srv/qios/repos`, Docker Compose stacks in `/srv/qios/stacks`, persistent app data in `/srv/qios/data`. (`Sec. 13.08.010.L001`; stable ID `T13.A08.S010.L001`)
- `Line 2` Do not create nested Git repos inside `/srv/qios/stacks`; repo source lives in `/srv/qios/repos` only. (`Sec. 13.08.010.L002`; stable ID `T13.A08.S010.L002`)
- `Line 3` Tailnet address is `qiserver-1.cerberus-sirius.ts.net` and Tailscale IPv4 is `100.121.111.106`; these are the private access coordinates. (`Sec. 13.08.010.L003`; stable ID `T13.A08.S010.L003`)


