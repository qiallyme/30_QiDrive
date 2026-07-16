---
layout: page
title: Security and Data Access Policy
slug: security-and-data-access-policy
status: publish
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

# Security and Data Access Policy

- **Anon Zero-Write Law**: Public unauthenticated access is read-only by default and must not write to canonical records directly.
- **System Role Isolation**: Elevated service credentials belong only to trusted backend, worker, or controlled automation paths.
- **Protected Surface Rule**: Private infrastructure such as server admin, storage internals, diagnostics, and raw runtime control stays behind explicit protection boundaries.
- **Derived Truth Rule**: Search, AI, graph, and export layers may assist but may not silently replace canonical sources.
