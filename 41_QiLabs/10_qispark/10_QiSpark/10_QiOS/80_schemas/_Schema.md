---
layout: page
title: Schema
slug: schema
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

# Schema

## Overview

`Schema/` describes QiOS domains, entities, relationships, flows, and boundaries while distinguishing intent from verified implementation.

## Responsibilities

- Define shared system concepts.
- Link detailed schemas from their owning domain.
- Mark proposed structures as proposed.
- Avoid duplicating migrations or runtime configuration.

## Current Model

```text
QiAccess -> QiLife -> (QiSystem + QiNexus + QiCapture + QiConnect)
                         |
                      QiServer
```
