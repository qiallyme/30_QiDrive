---
layout: page
title: Documents: Data Dependencies
slug: documents-data-dependencies
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

# Documents: Data Dependencies
*   **Reads/Writes**: Database records written to the `documents` table.
*   **Links**: Heavily dependent on the `links` table to establish relationships with `qibits`, `transactions`, `obligations`, and `people`.
