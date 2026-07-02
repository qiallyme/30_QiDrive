---
layout: page
title: Gethomepage
slug: ""
summary: ""
status: active
created_at: ""
updated_at: ""
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ""
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Private Server Launcher (gethomepage)

## Purpose
A local-only server dashboard and utility for quick access to qiserver services via the tailnet.

## Current Status
Active

## URLs
- Local: `http://127.0.0.1:3001`
- Tailnet: `https://qiserver-1.cerberus-sirius.ts.net` (via Tailscale Serve)

## Paths
- Stack: `/srv/qios/stacks/_qiaccess_start`
- Config: `/srv/qios/stacks/_qiaccess_start/config/services.yaml`

## Access Class
Private / Tailnet Only

## Notes / TODOs
- **CRITICAL:** This is separate from the public `access.qially.com` portal. 
- Editing `services.yaml` only affects this local view.
- Public portal links are managed in the portal's own source data files.
