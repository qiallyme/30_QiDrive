---
layout: adr
title: Decision 0010: Spaces for Scoped Shared Access
slug: decision-0010-spaces-for-scoped-shared-access
status: active
updated_at: "2026-06-29"
tags:
  - qispark
  - decisions
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

# Decision 0010: Spaces for Scoped Shared Access

## Context

QiLife needs to support Mom Care notes without building a separate app or a bloated clinical EMR.

## Decision

Use Spaces to provide scoped shared access. Mom Care will be a space with specific access roles. Everything defaults to Cody Private, and items are explicitly shared.

## Consequences

- Simplifies architecture by using one backend for multiple contexts.
- Avoids overbuilding an EMR. Focuses on lightweight buckets and timeline notes.
- Private notes can safely generate sanitized shared Care Notes.
