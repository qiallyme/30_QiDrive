---
layout: section
title: Title 13. QiServer
slug: qicode-title-13-qiserver
summary: QiServer governs 20_QiServer — the runtime, infrastructure, services, and operations layer of QiLabs.
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
  - qilabs
source_type: manual
---

# Title 13. QiServer

## Citation

- Legal citation: `QiCode Title 13`
- Article citation: `QiCode Title 13, Article #`
- Section citation: `QiCode Sec. 13.##.###`
- Stable ID alias: `QiCode T13.A##.S###.L###`

## Rule of Construction

- `Rule 13.001.L001` This title governs `20_QiServer` — the runtime and infrastructure layer on the physical server `qiserver` (Tailscale: `qiserver-1`). (stable ID `T13.R001.L001`)
- `Rule 13.001.L002` A section states a governing principle; a line states a citeable rule or application. (stable ID `T13.R001.L002`)
- `Rule 13.001.L003` Verified runtime facts win over repo planning notes when they conflict. (stable ID `T13.R001.L003`)

## Article 1. Runtime Authority

Stable ID: `T13.A01`

### Sec. 13.01.010. Primary Function

Stable ID: `T13.A01.S010`

- `Line 1` QiServer is the runtime and infrastructure layer: it hosts services, databases, containers, and local AI. (`Sec. 13.01.010.L001`; stable ID `T13.A01.S010.L001`)
- `Line 2` QiServer must not be used as a docs site, vault, or life app layer. (`Sec. 13.01.010.L002`; stable ID `T13.A01.S010.L002`)
- `Line 3` If use is ambiguous, the placement rule for the nearest parent title controls. (`Sec. 13.01.010.L003`; stable ID `T13.A01.S010.L003`)

## Article 2. Server Services

Stable ID: `T13.A02`

### Sec. 13.02.010. Service Catalog

Stable ID: `T13.A02.S010`

- `Line 1` Verified active services on QiServer include: Cockpit, Portainer, GetHomepage, Tailscale, Cloudflared, Uptime Kuma, Open WebUI, Ollama, Neo4j, Qdrant, n8n, SolidTime, Firefly III, Wiki.js, Paperless-ngx, BookStack, DailyWave, QiTTS, and QiTranscribe. (`Sec. 13.02.010.L001`; stable ID `T13.A02.S010.L001`)
- `Line 2` Each service must have a corresponding runbook or documentation file in `20_QiServer`; the canonical service map is `20_QiServer/Service_Map.md`. (`Sec. 13.02.010.L002`; stable ID `T13.A02.S010.L002`)
- `Line 3` Services with public exposure must be documented in a security review before activation; the public restricted entry point is `https://access.qially.com` via Cloudflared tunnel. (`Sec. 13.02.010.L003`; stable ID `T13.A02.S010.L003`)

## Article 3. Docker and Containers

Stable ID: `T13.A03`

### Sec. 13.03.010. Container Governance

Stable ID: `T13.A03.S010`

- `Line 1` All containerized services must be defined in version-controlled Docker Compose files. (`Sec. 13.03.010.L001`; stable ID `T13.A03.S010.L001`)
- `Line 2` Container configurations must not include secrets inline; use environment files or secrets managers. (`Sec. 13.03.010.L002`; stable ID `T13.A03.S010.L002`)
- `Line 3` Portainer manages container state; Portainer itself is governed by QiServer. (`Sec. 13.03.010.L003`; stable ID `T13.A03.S010.L003`)

## Article 4. Databases

Stable ID: `T13.A04`

### Sec. 13.04.010. Database Authority

Stable ID: `T13.A04.S010`

- `Line 1` Local databases hosted on QiServer (Neo4j, Qdrant, Firefly III DB, BookStack DB, SolidTime DB) are governed by QiServer doctrine for access, backups, and migrations. (`Sec. 13.04.010.L001`; stable ID `T13.A04.S010.L001`)
- `Line 2` Supabase is a cloud-hosted SaaS database and is the canonical data authority for QiLife and connected apps; it is NOT hosted on QiServer — QiServer connects to it remotely (ADR-0018). (`Sec. 13.04.010.L002`; stable ID `T13.A04.S010.L002`)
- `Line 3` Directus is the admin UI and API layer for Supabase/Postgres per ADR-0019; NocoDB is deprecated and scheduled for decommissioning. Schema changes must be versioned migration scripts, not Directus-panel edits. (`Sec. 13.04.010.L003`; stable ID `T13.A04.S010.L003`)

## Article 5. Local AI

Stable ID: `T13.A05`

### Sec. 13.05.010. AI Compute Governance

Stable ID: `T13.A05.S010`

- `Line 1` Local AI services (Ollama, Open WebUI, Qdrant, Neo4j) are hosted and governed under QiServer; the active chat model is `llama3.2` and the embedding model is `embeddinggemma`. (`Sec. 13.05.010.L001`; stable ID `T13.A05.S010.L001`)
- `Line 2` AI models and vector indexes must be versioned and documented in `20_QiServer/10_ai_compute`; graph and vector outputs are derived — they are not canonical sources of truth. (`Sec. 13.05.010.L002`; stable ID `T13.A05.S010.L002`)
- `Line 3` Local AI services must not process protected legal or evidence records without explicit governance review; QiTTS and QiTranscribe are local AI services subject to this rule. (`Sec. 13.05.010.L003`; stable ID `T13.A05.S010.L003`)

## Article 6. Security and Access

Stable ID: `T13.A06`

### Sec. 13.06.010. Access Control

Stable ID: `T13.A06.S010`

- `Line 1` Tailscale governs remote access to QiServer; no other VPN or direct exposure is permitted without documentation. (`Sec. 13.06.010.L001`; stable ID `T13.A06.S010.L001`)
- `Line 2` Cloudflare is the public edge; it proxies and protects any public-facing QiServer endpoints. (`Sec. 13.06.010.L002`; stable ID `T13.A06.S010.L002`)
- `Line 3` All public interfaces must be documented in a `public_interfaces.md` file in `20_QiServer`. (`Sec. 13.06.010.L003`; stable ID `T13.A06.S010.L003`)

## Article 7. Backups and Recovery

Stable ID: `T13.A07`

### Sec. 13.07.010. Backup Policy

Stable ID: `T13.A07.S010`

- `Line 1` All QiServer databases and critical service configurations must have a documented backup schedule. (`Sec. 13.07.010.L001`; stable ID `T13.A07.S010.L001`)
- `Line 2` Recovery procedures must be documented and tested before the system is considered production-ready; re-entry starts with `/srv/qios/docs/000_RUN_ME_FIRST.md`. (`Sec. 13.07.010.L002`; stable ID `T13.A07.S010.L002`)
- `Line 3` Backup storage must not rely solely on the same physical server being backed up. (`Sec. 13.07.010.L003`; stable ID `T13.A07.S010.L003`)

## Article 8. Path Doctrine

Stable ID: `T13.A08`

### Sec. 13.08.010. Server Path Standards

Stable ID: `T13.A08.S010`

- `Line 1` QiServer runtime root is `/srv/qios`; repos live in `/srv/qios/repos`, Docker Compose stacks in `/srv/qios/stacks`, persistent app data in `/srv/qios/data`. (`Sec. 13.08.010.L001`; stable ID `T13.A08.S010.L001`)
- `Line 2` Do not create nested Git repos inside `/srv/qios/stacks`; repo source lives in `/srv/qios/repos` only. (`Sec. 13.08.010.L002`; stable ID `T13.A08.S010.L002`)
- `Line 3` Tailnet address is `qiserver-1.cerberus-sirius.ts.net` and Tailscale IPv4 is `100.121.111.106`; these are the private access coordinates. (`Sec. 13.08.010.L003`; stable ID `T13.A08.S010.L003`)

## Cross References

- [QiCode Index](../_index.md)
- [Title 10 — QiLabs](../title_10_qilabs/title_10_qilabs.md)
- [Migration Map](../reference/qilabs_title_migration_map.md)
- [Legacy Service Map](../../../../50_QiLabs/20_QiServer/Service_Map.md)
