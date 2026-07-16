---
layout: page
title: 0001 Personal Lifedesk Model
slug: 0001-personal-lifedesk-model
summary: ""
status: active
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
uid: a48ae40b612842f483aa4b823bd5a784
canonical_ref: ""
source_type: manual
template_key: master-template
---

# ADR 0001: Personal LifeDesk Model

## Status
Accepted

---

## Context
Cody's daily life operations (LifeOps) involve tasks, legal issues, financial obligations, documentation, and relationships. Managing these using generic tools (Trello, standard todo apps, spreadsheets) creates fragmentation and cognitive overload. There is no unified metaphor that brings these elements together in a way that respects their interconnected nature (e.g., how a financial loan relates to a specific person and a legal dispute).

---

## Decision
We will standardize the entire application architecture on the **Personal LifeDesk** model. Under this model:
*   The application behaves like an IT/customer helpdesk console.
*   **Cody** is the sole "agent" (the one resolving items) and the primary "customer" (the one whose life is being managed).
*   All other individuals, agencies, and vendors are treated as external requesters/contacts.
*   The data model maps exactly to helpdesk concepts:
    *   Ticket = **QiBit**
    *   Queue/Department = **Bucket**
    *   Case/Project = **Thread**
    *   Work Order = **Action**
    *   Subtask = **Step**
    *   Sidebar widget = **Context Dock**

---

## Consequences
*   **Simplicity**: The backend database and routing are simplified. There is no need for complex multi-tenant row-level security or multi-user permission roles in V1.
*   **Strict Vocabulary**: Developers and AI agents must strictly use the terms: QiLife, QiBit, Personal LifeDesk, Timeline, Bucket, Thread, Action, Step, Context Dock, and Ask QiLife.
*   **Narrow Scope**: We will not build complex Customer Relationship Management (CRM) sales pipelines or client portals.
