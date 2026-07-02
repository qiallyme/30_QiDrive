---
layout: page
title: Runtime & Local Setup
slug: runtime-local-setup
status: active
updated_at: "2026-06-29"
tags:
  - qispark
source_type: manual
summary: ""
created_at: ""
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ""
canonical_ref: ""
template_key: master-template
---

# Runtime & Local Setup

The active runtime is qiserver.

## Current Local Services

- **Paperless-ngx**: Locally at 127.0.0.1:8010.
- **NocoDB**: Locally at 127.0.0.1:8088.
- **Open WebUI**: Locally at 127.0.0.1:3000.
- **Wiki.js**: Locally at 127.0.0.1:3002. Verified internal/admin route via Tailscale Serve: `https://qiserver-1.cerberus-sirius.ts.net:9448`. Public Cloudflare route `https://wiki.qially.com` is currently degraded and needs tunnel repair.
- **Homepage/QiAccess**: Locally at 127.0.0.1:3001.
- **Portainer**: Locally at 127.0.0.1:9443 (admin service).
- **Ollama**: Locked to 127.0.0.1:11434 on qiserver.
- **Aider**: Installed under /srv/qios/tools/aider.

## Legacy Local Setup

*Note: Supabase environments, PNPM commands, and Next.js start scripts are legacy. MkDocs is legacy and should not be restored.*
