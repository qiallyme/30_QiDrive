---
layout: article
title: Article 6. Security and Access
slug: qicode-title-13-article-06-security-and-access
summary: ""
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
qicode_title: 13
qicode_article: 6
parent_title: Title 13. QiServer
canonical_ref: QiCode T13.A06
source_type: manual
---

## Article 6. Security and Access

Stable ID: `T13.A06`

### Sec. 13.06.010. Access Control

Stable ID: `T13.A06.S010`

- `Line 1` Tailscale governs remote access to QiServer; no other VPN or direct exposure is permitted without documentation. (`Sec. 13.06.010.L001`; stable ID `T13.A06.S010.L001`)
- `Line 2` Cloudflare is the public edge; it proxies and protects any public-facing QiServer endpoints. (`Sec. 13.06.010.L002`; stable ID `T13.A06.S010.L002`)
- `Line 3` All public interfaces must be documented in a `public_interfaces.md` file in `20_QiServer`. (`Sec. 13.06.010.L003`; stable ID `T13.A06.S010.L003`)


