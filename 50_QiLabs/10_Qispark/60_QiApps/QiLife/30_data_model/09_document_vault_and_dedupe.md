---
layout: page
title: Managed Document Vault and Dedupe
slug: managed-document-vault-and-dedupe
status: publish
updated_at: "2026-07-16T06:49:40-04:00"
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
uid: b9834c2c32724e318f5c8513d5d68593
canonical_ref: ""
template_key: master-template
---

# Managed Document Vault and Dedupe
QiLife eventually replaces Paperless-style intake.

## Doctrine

- QiLife is dup-allergic. Every incoming file must be hashed.
- Exact duplicates should not create duplicate blobs. Near duplicates should be flagged for review.
- Files should be stored as managed file objects.
- Documents are meaning/context records linked to file objects.
- Support document versions.
- File deletion should be safe, logged, and restorable before purge.

## Planned Tables

- `file_objects`
- `documents`
- `document_versions`
- `duplicate_candidates`
- `file_events`
- `text_extractions`
