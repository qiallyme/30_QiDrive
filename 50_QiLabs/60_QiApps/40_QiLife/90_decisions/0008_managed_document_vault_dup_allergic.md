---
layout: page
title: 0008 Managed Document Vault Dup Allergic
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

# Decision 0008: Managed Document Vault (Dup-Allergic)

## Context
Ingesting the same documents multiple times creates noise and fragments context.

## Decision
QiLife will implement a managed document vault that hashes every incoming file. The system will be dup-allergic, preventing duplicate blobs and flagging near-duplicates.

## Consequences
- Meaningful documents are separated from raw file objects.
- Requires building hashing, duplicate candidate review, and versioning flows.
- Allows safe, restorable deletion before purging.
