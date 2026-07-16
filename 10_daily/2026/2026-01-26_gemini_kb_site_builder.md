---
layout: page
title: "Gemini KB Site Builder"
slug: "gemini_kb_site_builder"
created_at: "2026-01-26 23:09:50"
updated_at: "2026-07-16T06:49:29-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-003.json"
template_key: master-template
date: 2026-01-26
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69784860-e03c-832e-9a92-2370c8c57c1b"
canonical_ref: ""
---

# Gemini KB Site Builder

## Overview
- **Date**: 2026-01-26 23:09:50
- **Conversation ID**: `69784860-e03c-832e-9a92-2370c8c57c1b`
- **Source**: `Chat-Export-28513-2026/conversations-003.json`

## Chat History

### User
> i need a quick kb site builder give me gemini prompt this will the teh qially kb at kb.qially.com for all internal kb and qially.com/help/* is where teh external public kb goes just fyi.

### Assistant
> Got it. You don’t need a debate or options paralysis — you need **one clean Gemini prompt** that spits out a **working KB site builder** you can deploy fast.
> 
> Below is a **copy-paste-ready Gemini prompt**. It is opinionated, minimal, and aligned with how you actually work.
> 
> ---
> 
> ## 🔧 GEMINI PROMPT — QiAlly Knowledge Base Site Builder
> 
> ```text
> You are a senior web engineer and technical writer.
> 
> Build a FAST, STATIC, HTML-FIRST Knowledge Base site generator for the QiAlly ecosystem.
> 
> CONTEXT (DO NOT IGNORE):
> - Internal Knowledge Base (private):
>   → Domain: https://kb.qially.com
>   → Audience: internal use only (me + collaborators)
> - Public Knowledge Base (external):
>   → Path: https://qially.com/help/*
>   → Audience: clients and public users
> - SAME CODEBASE, different build targets
> 
> PRIMARY GOALS:
> - Zero JS frameworks (NO React, NO Next, NO Vite)
> - Static HTML output
> - Markdown as source of truth
> - Clean URLs
> - Fast build, easy deploy
> - Human-readable, printable pages
> - Works with Cloudflare Pages
> 
> TECH STACK (MANDATORY):
> - Pure HTML + CSS
> - Optional vanilla JS only if truly necessary
> - Markdown → HTML conversion
> - Directory-based routing
> - No database
> - No server runtime
> 
> DIRECTORY STRUCTURE (REQUIRED):
> /kb-builder
>   /content
>     /internal
>       /guides
>       /systems
>       /decisions
>     /public
>       /getting-started
>       /faq
>       /how-to
>   /templates
>     base.html
>     kb_index.html
>     kb_article.html
>   /assets
>     /css
>       kb.css
>     /icons
>   build.py
>   config.yaml
>   README.md
> 
> ROUTING RULES:
> - Markdown file → HTML page
> - Folder → index.html
> - Internal build outputs to:
>   → /dist/kb/  → deploy to kb.qially.com
> - Public build outputs to:
>   → /dist/help/ → deploy to qially.com/help/
> 
> FEATURES TO IMPLEMENT:
> 1. Left sidebar navigation (folder-based)
> 2. Page title + breadcrumb
> 3. Last updated date (from file metadata)
> 4. Table of contents auto-generated from headings
> 5. Search (simple client-side, optional but preferred)
> 6. Print-friendly CSS
> 7. Dark mode via CSS variables
> 8. Internal KB clearly labeled "INTERNAL"
> 
> CONFIGURATION:
> - config.yaml controls:
>   - site title
>   - base path
>   - internal vs public mode
>   - branding (QiAlly)
> - One command builds both internal and public KBs
> 
> BUILD SCRIPT:
> - Python-based (preferred)
> - Reads markdown files
> - Applies templates
> - Writes static HTML
> - Deterministic output (no randomness)
> 
> OUTPUT REQUIREMENTS:
> - Provide:
>   1. build.py (complete, runnable)
>   2. Example templates (base + article)
>   3. Example CSS (clean, modern, readable)
>   4. Sample markdown files
>   5. README with build + deploy steps for Cloudflare Pages
> 
> STYLE:
> - Clean
> - Professional
> - Not “bloggy”
> - Think “Stripe docs” meets “Obsidian clarity”
> 
> IMPORTANT:
> Do NOT over-engineer.
> Do NOT introduce frameworks.
> Do NOT hand-wave implementation.
> Return FULL FILE CONTENTS.
> 
> Begin immediately.
> ```
> 
> ---
> 
> ## 🧠 Strategic Reality Check (truth mode)
> 
> - This is **the right call**.  
> - React/Next would slow you down and add cognitive debt you don’t need.
> - Static + Markdown matches how you already think and organize.
> - Cloudflare Pages loves this setup.
> - This will scale quietly without becoming another “system to maintain.”
> 
> If Gemini tries to sneak in:
> - Next.js
> - Astro
> - MDX
> - Tailwind build steps
> - Node tooling
> 
> 👉 **Reject it and rerun the prompt.**
> 
> ---
> 
> ## 🔜 Next (when ready)
> If you want, I can:
> - Tighten this into a **QiOS-canonical KB standard**
> - Add **Zero Trust gating** for `kb.qially.com`
> - Generate a **search index script**
> - Align this with your **QiNote / Drive mirror**
> 
> Say the word.
