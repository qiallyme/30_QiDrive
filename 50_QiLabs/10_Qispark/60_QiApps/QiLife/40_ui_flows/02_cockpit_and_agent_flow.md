---
layout: page
title: Cockpit and Agent Flow
slug: cockpit-and-agent-flow
status: publish
updated_at: "2026-07-16T06:49:40-04:00"
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
uid: 0788b8beaf894bfb9e74e69e82e389bd
canonical_ref: ""
template_key: master-template
---

# Cockpit and Agent Flow
The UI serves as a Cockpit for managing the AI Life Copilot.

## Core Interaction

- “What happened-” / “Talk to QiLife” / “Handle this.”
- The home screen focuses on today's state, pending AI drafts, open loops, and an insight feed.

## Feature Toggles / Adoption Modes

QiLife supports feature toggles through a central feature registry (`frontend/src/config/features.ts`).
Adoption Presets: Simple Mode, Care Mode, Full Mode.
Toggling a feature off hides it from navigation but does not delete data.
