---
layout: page
title: "HTML Template Repo Structure"
slug: "html_template_repo_structure"
created_at: "2026-03-04 11:15:05"
updated_at: "2026-03-04 11:15:05"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-004.json"
template_key: master-template
date: 2026-03-04
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69a86887-8090-832e-8d1a-081f29b048fa"
canonical_ref: ""
---

# HTML Template Repo Structure

## Overview
- **Date**: 2026-03-04 11:15:05
- **Conversation ID**: `69a86887-8090-832e-8d1a-081f29b048fa`
- **Source**: `Chat-Export-28513-2026/conversations-004.json`

## Chat History

### User
> where woul you put html email templates or html docs in the current repo structure.

### Assistant
> Ohhh good question. This is where repo entropy either starts… or gets eliminated. Let’s not create future-you cleanup work.
> 
> Given how you think (modular, consistent, no duplicate logic, no “random dump folders”), here’s the clean way to do it.
> 
> ---
> 
> # First: Decide the Role of the HTML
> 
> You’ve got two very different beasts:
> 
> 1. **Transactional HTML emails** (password reset, invoice sent, reminder, etc.)
> 2. **Standalone HTML documents** (cheat sheets, printable PDFs, landing pages, client exports, etc.)
> 
> They should NOT live in the same place unless you want chaos later.
> 
> ---
> 
> # ✅ Option A — If This Is a Monorepo (QiOne style)
> 
> ### 🔹 For Email Templates
> 
> Put them in a shared package.
> 
> ```
> /packages
>   /email
>     /templates
>       invoice_sent.html
>       password_reset.html
>       daily_reminder.html
>     /partials
>       header.html
>       footer.html
>     render.ts
> ```
> 
> Why?
> 
> - Emails are cross-app infrastructure.
> - They’re not tied to frontend UI.
> - They’re system-level utilities.
> - You’ll likely render them server-side (Worker, API, n8n, etc.).
> 
> This keeps them reusable across:
> - Portal
> - Internal tools
> - QiTax
> - Care Portal
> - Future SaaS tenants
> 
> Infrastructure belongs in `/packages`.
> 
> ---
> 
> ### 🔹 For Standalone HTML Docs (Printable, Static, Cheat Sheets)
> 
> These belong closer to the app that uses them.
> 
> If it's portal-facing:
> 
> ```
> /apps
>   /portal
>     /public
>       /docs
>         daily_glance_sheet.html
>         travel_strip.html
> ```
> 
> If they are generated artifacts:
> 
> ```
> /apps
>   /portal
>     /artifacts
> ```
> 
> If they’re part of QiVault knowledge content:
> 
> ```
> /vault
>   /exports
>     daily_glance_sheet.html
> ```
> 
> Don’t bury user-facing docs inside packages unless they’re true system templates.
> 
> ---
> 
> # ⚠️ What NOT To Do
> 
> Do NOT:
> - Throw them into `/public` at root.
> - Mix email + printable docs.
> - Scatter them across random app folders.
> - Duplicate the same template in 3 apps.
> 
> That’s how repo drift starts.
> 
> ---
> 
> # 🔥 My Recommendation For *Your* System
> 
> Knowing how you build:
> 
> ### Create:
> 
> ```
> /packages/ui-docs
> /packages/email
> ```
> 
> Separation of concerns:
> - `email` = transactional system comms
> - `ui-docs` = printable / embeddable HTML documents
> - `apps/*` = actual apps
> - `vault/*` = content
> 
> You are building a cognitive OS. Treat documents like modules.
> 
> ---
> 
> # If You Want It Ultra-Clean
> 
> You could even version them like this:
> 
> ```
> /packages/email/templates/v1/
> /packages/email/templates/v2/
> ```
> 
> Because email rendering bugs are real and versioning prevents accidental breaking.
> 
> ---
> 
> # Quick Decision Rule
> 
> Ask:
> 
> > Is this sent by the system automatically?
> → `/packages/email`
> 
> > Is this something a human prints, views, or downloads?
> → `/packages/ui-docs` OR app-level `/public/docs`
> 
> ---
> 
> If you show me your current top-level folder tree, I’ll tell you exactly where I’d anchor it so it fits your QiDecimal logic and doesn’t create future friction.
