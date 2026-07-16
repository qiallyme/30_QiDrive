---
layout: page
title: "QiAccess Restart Solution"
slug: "qiaccess_restart_solution"
created_at: "2026-05-18 11:41:01"
updated_at: "2026-05-18 11:41:01"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-007.json"
template_key: master-template
date: 2026-05-18
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a0b4107-0da4-83ea-80c6-f94f5b47566d"
canonical_ref: ""
---

# QiAccess Restart Solution

## Overview
- **Date**: 2026-05-18 11:41:01
- **Conversation ID**: `6a0b4107-0da4-83ea-80c6-f94f5b47566d`
- **Source**: `Chat-Export-28513-2026/conversations-007.json`

## Chat History

### User
> ok, so my wiki.js is not running we need to have a way from my fornt door to restart servers or have them set to restart

### Assistant
> Yes. This is exactly what **QiAccess Start / Access** should do: front door = launcher + control panel, not just pretty tiles. Wiki.js being down is the proof.
> 
> The right answer has **two layers**:
> 
> 1. **Auto-restart at Docker/system level** so services heal themselves.
> 2. **QiAccess Start control actions** so you can restart/check services from the front door without SSH’ing every time.
> 
> This aligns with the blueprint: QiAccess Start is your operational front door, while QiServer is the service layer running Wiki.js, Portainer, Cockpit, Paperless, Open WebUI, etc. fileciteturn0file0
> 
> ---
> 
> ## Immediate fix: set Wiki.js to restart automatically
> 
> On qiserver:
> 
> ```bash
> cd /srv/qios/stacks/wikijs
> sudo docker compose ps
> sudo docker compose up -d
> sudo docker update --restart unless-stopped wikijs
> sudo docker update --restart unless-stopped wikijs-db
> ```
> 
> Then check logs:
> 
> ```bash
> sudo docker logs --tail=80 wikijs
> ```
> 
> If the container names are different, get them with:
> 
> ```bash
> sudo docker ps -a --format "table {{.Names}}\t{{.Image}}\t{{.Status}}"
> ```
> 
> Then apply restart policy to the right names.
> 
> ---
> 
> ## Better permanent fix: add restart policy in docker-compose.yml
> 
> In the Wiki.js compose file, each service should have:
> 
> ```yaml
> restart: unless-stopped
> ```
> 
> Example shape:
> 
> ```yaml
> services:
>   wikijs:
>     image: requarks/wiki:2
>     restart: unless-stopped
>     depends_on:
>       - wikijs-db
>     ports:
>       - "127.0.0.1:3002:3000"
> 
>   wikijs-db:
>     image: postgres:16
>     restart: unless-stopped
> ```
> 
> Then run:
> 
> ```bash
> cd /srv/qios/stacks/wikijs
> sudo docker compose up -d
> ```
> 
> That handles normal crashes and reboot recovery.
> 
> ---
> 
> ## What QiAccess Start should add
> 
> Add a **QiServer Control Panel** inside `/server` or `/access`.
> 
> Minimum buttons:
> 
> | Action | Purpose |
> |---|---|
> | Check status | Shows whether services are up/down |
> | Restart Wiki.js | Restarts only Wiki.js |
> | Restart Paperless | Restarts Paperless stack |
> | Restart Open WebUI | Restarts Open WebUI |
> | Restart all safe services | Restarts approved non-dangerous services |
> | Open Portainer | Manual fallback |
> | Open Cockpit | Server fallback |
> 
> Do **not** expose raw Docker controls publicly. That is admin power. It belongs behind Cloudflare Access/Tailscale/app auth, because the blueprint already classifies server-control surfaces as protected/private admin services. fileciteturn0file0
> 
> ---
> 
> ## Best architecture
> 
> Do not let the React front end directly run shell commands. That is asking for chaos with glitter on it.
> 
> Use this pattern:
> 
> **QiAccess Start UI → local protected API → allowlisted service commands → Docker**
> 
> Example:
> 
> ```text
> QiAccess Start
>   /server
>     Restart Wiki.js button
>         ↓
> QiServer Control API
>   POST /api/services/wikijs/restart
>         ↓
> Allowlist check
>         ↓
> docker compose restart wikijs
> ```
> 
> Only allow specific service names. No arbitrary command input. No “run shell command” box. Absolutely not.
> 
> ---
> 
> ## Codex prompt
> 
> Give Codex this:
> 
> ```text
> We need to add a protected QiServer control layer to QiAccess Start.
> 
> Context:
> QiAccess Start is the operational front door for Cody’s self-hosted system. The front door should not only link to services; it should show health/status and allow safe restart actions for approved services like Wiki.js. Admin controls must not expose arbitrary shell access.
> 
> Goal:
> Add a QiServer Control Panel with service status and safe restart buttons.
> 
> Requirements:
> 1. Add or update the `/server` page in QiAccess Start.
> 2. Create a service registry data file, likely `src/features/03_qiserver/data/serverServices.ts`.
> 3. Each service record should include:
>    - id
>    - displayName
>    - description
>    - category
>    - publicUrl or internalUrl
>    - stackPath
>    - composeServiceNames
>    - healthCheckUrl if available
>    - isAdmin
>    - exposureClass: private_only | public_restricted | public_safe
>    - restartAllowed: boolean
> 4. Add UI cards showing:
>    - service name
>    - status: online / offline / unknown
>    - exposure badge
>    - open link
>    - restart button only when restartAllowed is true
> 5. Add backend API endpoints for:
>    - GET `/api/server/services/status`
>    - POST `/api/server/services/:id/restart`
> 6. The restart endpoint must:
>    - only accept service IDs from the allowlisted registry
>    - reject unknown services
>    - reject services where restartAllowed is false
>    - never accept raw shell commands from the client
>    - run `docker compose restart` only from the registered stack path
> 7. Add Wiki.js as the first controlled service.
> 8. Add clear error messages in the UI when restart fails.
> 9. Add a README under `src/features/03_qiserver/README.md` explaining:
>    - what this module does
>    - how to add a new service
>    - safety rules
>    - why arbitrary shell commands are forbidden
> 10. Keep the UI simple:
>    - left-side navigation
>    - main content area
>    - no duplicate card grids
>    - no nested card chaos
>    - elegant, plain, useful
> 
> Initial service:
> id: wikijs
> displayName: Wiki.js
> description: Primary readable knowledge base/manual library.
> stackPath: /srv/qios/stacks/wikijs
> composeServiceNames: ["wikijs"]
> healthCheckUrl: http://127.0.0.1:3002
> exposureClass: public_restricted
> restartAllowed: true
> 
> Also add a deployment/runbook note explaining that the Wiki.js docker-compose.yml should include:
> restart: unless-stopped
> 
> Security rule:
> QiAccess Start may trigger safe allowlisted service actions only. It must not become a browser-based root shell.
> ```
> 
> ---
> 
> ## Also tell Codex to fix Docker restart policies
> 
> Separate prompt for the server repo/docs side:
> 
> ```text
> Audit the qiserver Docker stack compose files and add restart policies.
> 
> Goal:
> All long-running self-hosted services should automatically recover after crashes or server reboot.
> 
> Scope:
> Review compose files under `/srv/qios/stacks`.
> 
> For each stable service, add:
> restart: unless-stopped
> 
> Prioritize:
> - Wiki.js
> - Paperless
> - Portainer
> - Open WebUI
> - Qdrant
> - Neo4j
> - NocoDB
> - Uptime Kuma
> - SolidTime
> - cloudflared
> 
> Do not change ports, volumes, env vars, networks, or image versions unless required.
> 
> After edits, run:
> sudo docker compose config
> sudo docker compose up -d
> 
> Then produce a report listing:
> - stack name
> - services updated
> - restart policy applied
> - services currently healthy/running
> - any failures and logs needed
> ```
> 
> ---
> 
> ## The strategic answer
> 
> You do **not** need another dashboard app. You need QiAccess Start to grow teeth.
> 
> Minimum viable version:
> 
> 1. **Docker restart policies**: `restart: unless-stopped`
> 2. **Status page**: shows online/offline
> 3. **Safe restart buttons**: allowlisted only
> 4. **Fallback links**: Portainer + Cockpit
> 5. **Runbook link**: “Wiki.js down? Click here.”
> 
> That’s the clean move. Not overbuilt. Not fragile. Useful immediately.
