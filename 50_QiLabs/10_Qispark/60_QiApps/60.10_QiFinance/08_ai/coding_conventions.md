---
layout: page
title: Coding Conventions
slug: coding-conventions
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
uid: aaf97f8261e44fc7a87032c0d26d1e56
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Coding Conventions

## Naming

Use clear domain names:

- account
- transaction
- split
- workspace
- payee
- rule

## Avoid

- Ambiguous names like item, record, thing, entry unless domain-specific
- Cody-only constants except in demo seed config

## Validation

Ledger validation belongs in shared logic, not scattered UI checks.
