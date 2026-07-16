---
layout: page
title: 0010 Spaces For Scoped Shared Access
slug: 0010-spaces-for-scoped-shared-access
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
uid: be8d82f60af6457c830bd7a0bf868caa
canonical_ref: ""
source_type: manual
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
