---
layout: page
title: 02 Cockpit And Agent Flow
slug: 02-cockpit-and-agent-flow
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
uid: ca9272455f10471a8e0d64c11979a511
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Cockpit and Agent Flow
The UI serves as a Cockpit for managing the AI Life Copilot.

## Core Interaction
- “What happened?” / “Talk to QiLife” / “Handle this.”
- The home screen focuses on today's state, pending AI drafts, open loops, and an insight feed.

## Feature Toggles / Adoption Modes
QiLife supports feature toggles through a central feature registry (`frontend/src/config/features.ts`).
Adoption Presets: Simple Mode, Care Mode, Full Mode.
Toggling a feature off hides it from navigation but does not delete data.
