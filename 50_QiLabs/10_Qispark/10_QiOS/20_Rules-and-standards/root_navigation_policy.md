---
layout: page
title: Root Navigation Policy
slug: ""
summary: ""
status: publish
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

# Root Navigation Policy

- The active repository uses a numbered root structure (`00_QiEOS`, `10_QiOS_Start`, `20_QiSystem`, `30_QiServer`, `40_QiCapture`, `50_QiNexus`, `60_QiApps`, `70_QiConnect`, `packages`, `scripts`, `toolbox`, `_QUARANTINE_`).
- New user-facing concerns belong inside an existing root unless a blueprint change explicitly approves a new root.
- System subroutes remain nested under `System`.
