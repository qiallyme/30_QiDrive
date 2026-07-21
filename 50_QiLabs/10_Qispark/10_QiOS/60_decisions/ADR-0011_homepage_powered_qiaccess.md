---
layout: adr
title: ADR-0011: Homepage-Powered QiAccess
slug: adr-0011-homepage-powered-qiaccess
status: publish
updated_at: "2026-07-16T06:49:38-04:00"
tags: []
  - qispark
  - decisions
source_type: manual
summary: ""
created_at: "2026-07-16T06:19:39-04:00"
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: 632eed70c5ae41ac9ce7ef83097da1f6
canonical_ref: ""
template_key: master-template
---

# ADR-0011: Homepage-Powered QiAccess

## Status

Accepted locally on 2026-05-24.

## Context

QiAccess had drifted into multiple overlapping implementations, including a custom React portal, a legacy Homepage-style local launcher, static site material, and generated documentation artifacts. The active direction is now a branded Homepage dashboard hosted on QiServer.

## Decision

- QiAccess is no longer the custom React portal.
- Homepage is the canonical dashboard runtime for QiAccess.
- The cloned Homepage source tree remains intact at the repo root.
- Active deployment config lives under `qiaccess/`.
- Legacy material remains under `.legacy/` for reference only.
- Cloudflare owns `access.qially.com` routing and should present a static offline/recovery page when QiServer is unavailable.

## Consequences

- Dashboard changes should prefer YAML configuration and light `custom.css` polish over source-code edits.
- Terminal, Cockpit, and Portainer remain the real control surfaces for server actions.
- Legacy material may be salvaged selectively, but it is not part of the active runtime without an explicit documented decision.
