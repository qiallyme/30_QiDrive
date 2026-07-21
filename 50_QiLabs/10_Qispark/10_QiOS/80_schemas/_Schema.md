---
layout: page
title: Schema
slug: schema
status: publish
updated_at: "2026-07-16T06:49:38-04:00"
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
uid: 2a9be7237b61485e87bdb84bd47d4d48
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
