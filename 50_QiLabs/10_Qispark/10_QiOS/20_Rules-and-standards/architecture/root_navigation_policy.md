---
layout: page
title: Root Navigation Policy
slug: root-navigation-policy
status: publish
updated_at: "2026-07-16T06:49:38-04:00"
tags: []
  - qispark
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
uid: e87da070f0704a29b2a28e2d5dba284d
canonical_ref: ""
template_key: master-template
---

# Root Navigation Policy

- The active repository uses a numbered root structure (`00_QiEOS`, `10_QiOS_Start`, `20_QiSystem`, `30_QiServer`, `40_QiCapture`, `50_QiNexus`, `60_QiApps`, `70_QiConnect`, `packages`, `scripts`, `toolbox`, `_QUARANTINE_`).
- New user-facing concerns belong inside an existing root unless a blueprint change explicitly approves a new root.
- System subroutes remain nested under `System`.
