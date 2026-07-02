---
layout: page
title: Coding Conventions
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
