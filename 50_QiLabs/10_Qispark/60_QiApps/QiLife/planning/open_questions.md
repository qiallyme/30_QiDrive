---
layout: page
title: QiLife Open Questions
slug: qilife-open-questions
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
uid: 560d1298c07c49909bd57cfc4ad955f6
canonical_ref: ""
template_key: master-template
---

# QiLife Open Questions

This document tracks unresolved technical decisions and product details that require clarification before transitioning to the v1 Spine build phase.

---

## 1. AI Integration Strategy

*   **Question**: Which LLM provider should be the primary target for Phase 5 integration-
    *   *Option A (Local-First)*: Connect to a local Ollama server running on QiServer (e.g. `llama3:8b`). This guarantees privacy and zero operating cost, but requires higher computing overhead on Cody's server.
    *   *Option B (Cloud Hybrid)*: Use the Gemini API or OpenAI API via API key configuration. This offers higher quality triage/reasoning but introduces monthly token costs and external data dependency.
    *   *Recommendation*: Build an adapter interface enabling either provider, default to Mock for Spine build.

---

## 2. Multi-Device Operations

*   **Question**: How will Cody access the UI on a mobile device-
    *   *Details*: SQLite databases lock under concurrent writes. If Cody accesses QiLife from both his desktop computer and phone (via local LAN routing to QiServer), the FastAPI server must handle session transactions carefully.
    *   *Recommendation*: Configure SQLite to operate in **WAL (Write-Ahead Logging) mode** and enforce tight transaction limits in SQLAlchemy/SQLModel.

---

## 3. Repo Document Syncer Directionality

*   **Question**: When editing a knowledge item in the QiLife browser UI that originated as a repository markdown file, how does the change propagate-
    *   *Option A (One-Way Import)*: Markdown files in the repo are static source-of-truth. Editing in the app is disabled for these files; edits must be done via code editor and synced.
    *   *Option B (Bi-directional Sync)*: Editing in the app updates the database, and an automated background runner overwrites the local markdown files on QiServer.
    *   *Recommendation*: Option A for V1 to keep implementation simple and prevent accidental file overrides.

---

## 4. Calendar Sync Boundary

*   **Question**: Are external calendar events (Google Calendar / Apple Calendar) rendered in the QiLife calendar dashboard-
    *   *Details*: Master spec calls for "no calendar sync" in V1 to avoid over-engineering. However, a read-only ICS feed import might be highly useful without the complexity of bi-directional write syncing.
    *   *Recommendation*: Enforce strict local-only events for V1. Re-evaluate ICS feed parsing in V2.
