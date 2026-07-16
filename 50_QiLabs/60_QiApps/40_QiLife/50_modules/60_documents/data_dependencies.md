---
layout: page
title: Data Dependencies
slug: data-dependencies
summary: ""
status: publish
created_at: "2026-07-16T06:19:39-04:00"
updated_at: "2026-07-16T06:19:39-04:00"
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: 8fbd37516096410ab3772f142cf7f879
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Documents: Data Dependencies
*   **Reads/Writes**: Database records written to the `documents` table.
*   **Links**: Heavily dependent on the `links` table to establish relationships with `qibits`, `transactions`, `obligations`, and `people`.
