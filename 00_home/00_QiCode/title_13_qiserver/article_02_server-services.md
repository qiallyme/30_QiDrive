---
layout: article
title: Article 2. Server Services
slug: qicode-title-13-article-02-server-services
summary: ""
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
qicode_title: 13
qicode_article: 2
parent_title: Title 13. QiServer
canonical_ref: QiCode T13.A02
source_type: manual
---

## Article 2. Server Services

Stable ID: `T13.A02`

### Sec. 13.02.010. Service Catalog

Stable ID: `T13.A02.S010`

- `Line 1` Verified active services on QiServer include: Cockpit, Portainer, GetHomepage, Tailscale, Cloudflared, Uptime Kuma, Open WebUI, Ollama, Neo4j, Qdrant, n8n, SolidTime, Firefly III, Wiki.js, Paperless-ngx, BookStack, DailyWave, QiTTS, and QiTranscribe. (`Sec. 13.02.010.L001`; stable ID `T13.A02.S010.L001`)
- `Line 2` Each service must have a corresponding runbook or documentation file in `20_QiServer`; the canonical service map is `20_QiServer/Service_Map.md`. (`Sec. 13.02.010.L002`; stable ID `T13.A02.S010.L002`)
- `Line 3` Services with public exposure must be documented in a security review before activation; the public restricted entry point is `https://access.qially.com` via Cloudflared tunnel. (`Sec. 13.02.010.L003`; stable ID `T13.A02.S010.L003`)


