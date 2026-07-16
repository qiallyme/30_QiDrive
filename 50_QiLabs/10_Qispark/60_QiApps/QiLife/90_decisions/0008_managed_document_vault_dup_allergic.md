---
layout: adr
title: Decision 0008: Managed Document Vault (Dup-Allergic)
slug: decision-0008-managed-document-vault-dup-allergic
status: publish
updated_at: "2026-07-16T06:49:40-04:00"
tags: []
  - qispark
  - decisions
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
uid: c64d6e6c2d1641009e3136de0d48314a
canonical_ref: ""
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
