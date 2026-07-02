---
layout: page
title: 09 Document Vault And Dedupe
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
