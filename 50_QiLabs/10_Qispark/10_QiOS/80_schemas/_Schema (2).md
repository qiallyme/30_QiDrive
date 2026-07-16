---
layout: page
title: Schema
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
