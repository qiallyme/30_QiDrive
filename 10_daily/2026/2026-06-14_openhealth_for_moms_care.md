---
layout: page
title: "OpenHealth for Mom's Care"
slug: "openhealth_for_moms_care"
created_at: "2026-06-14 21:42:43"
updated_at: "2026-06-14 21:42:43"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-009.json"
template_key: master-template
date: 2026-06-14
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a2f669c-27d0-83ea-a288-25fe6468bc51"
canonical_ref: ""
---

# OpenHealth for Mom's Care

## Overview
- **Date**: 2026-06-14 21:42:43
- **Conversation ID**: `6a2f669c-27d0-83ea-a288-25fe6468bc51`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> what do you think about this for my moms care. https://github.com/OpenHealthForAll

### Assistant
> I’ll sanity-check the repo, not just vibe-check the name. The real question is: **does it reduce your care chaos now**, or does it become another shiny unfinished system.

### Assistant
> ## My take: **promising, but do not make it Mom’s live care system yet.**
> 
> OpenHealth is interesting because it’s basically trying to be a **local AI health-data assistant**: centralize health data, parse it, structure it, and use it for AI context. That lines up with what you need: records, meds, symptoms, questions, care history, and less chaos. Its README says it supports health records, blood tests, prescriptions/imaging, Apple/Google health data, wearables, symptoms, and local LLMs like LLaMA/Ollama. citeturn319012view0
> 
> But here’s the blunt truth: **for your mom’s care, this is a “research / prototype / helper layer,” not the operational source of truth.**
> 
> ### Why I like it
> 
> It has the right conceptual shape:
> 
> | Need for Mom | OpenHealth fit |
> |---|---|
> | Central medical record bucket | Yes |
> | Parse PDFs / records | Yes-ish; uses Docling/local parsing |
> | AI chat over health context | Yes |
> | Local-first privacy potential | Yes |
> | Docker deployable on qiserver | Yes |
> | Works with Ollama/local LLM idea | Yes |
> 
> The repo also has decent public traction: the main repo shows about **3.9k stars**, **419 forks**, and an AGPL-3.0 license. citeturn148797view0
> 
> ### Why I would **not** trust it as the main care system yet
> 
> It is still young. Latest release listed is **v0.2.0 from February 21, 2025**, and current open issues include install/build problems and a recent RFC for a “Validated Health Data Engine,” which tells me the validation layer is still being thought through, not finished. citeturn932513view0turn932513view1
> 
> Also, the data model is pretty generic. The Prisma schema has a `HealthData` table with fields like `type`, `data Json`, `metadata`, `filePath`, `fileType`, and `status`, plus chat rooms, assistant modes, LLM providers, and messages. That is useful for ingestion and AI context, but it is **not a full care-coordination database** for meds, oxygen logs, falls, transfers, appointments, escalation rules, home-health notes, Humana notes, caregiver tasks, and Family OS decisions. citeturn843880view1
> 
> And security-wise: the Docker compose exposes Postgres on `5432` and the app on `3000`; fine for local testing, not fine to casually expose to the internet with Mom’s PHI sitting inside. citeturn843880view0
> 
> ## My recommendation
> 
> Use OpenHealth as a **sidecar**, not the cockpit.
> 
> Your actual system should still be:
> 
> **QiLife / MomCare OS = source of truth**  
> **Paperless / Obsidian / Supabase = records + structured logs**  
> **OpenHealth = optional medical-record parser + AI exploration sandbox**
> 
> Basically:
> 
> ```text
> Mom documents / notes / PDFs
>         ↓
> Paperless / QiNexus archive
>         ↓
> QiLife MomCare structured tables
>         ↓
> OpenHealth sidecar for AI medical-context review
> ```
> 
> Do **not** let OpenHealth become another whole universe you have to maintain. That’s how we get “seven systems and no system.” We are not doing that circus.
> 
> ## Hard boundaries for Mom’s safety
> 
> Do **not** use it to decide:
> 
> - oxygen changes
> - morphine / hydroxyzine / prednisone / antibiotic decisions
> - medication timing changes
> - whether symptoms are anxiety vs COPD flare
> - whether to avoid ER / 911
> 
> Use it for:
> 
> - summarizing visit notes
> - extracting medication mentions
> - building doctor questions
> - organizing timelines
> - comparing discharge instructions
> - finding conflicts across records
> - generating “verify this with pharmacist/doctor” lists
> 
> The OpenHealth Clinic page itself says AI can make mistakes and emergencies require local emergency services. That’s the right warning. citeturn972777view1
> 
> ## Privacy reality check
> 
> Mom’s medical data is sensitive as hell. HHS defines individually identifiable health information broadly: physical/mental condition, care provided, payment info, and identifiers like name, birth date, address, etc. citeturn778879view0
> 
> So:
> 
> - **Local-only testing:** acceptable.
> - **Cloud OpenHealth account with Mom’s real data:** no, not until privacy, retention, deletion, and compliance are verified.
> - **Public tunnel / Cloudflare exposure:** only behind strong auth, no public route, no casual sharing.
> - **Use fake/de-identified test records first.**
> 
> ## Best next move
> 
> I’d give it a **2-hour controlled test**, max. No rabbit hole.
> 
> ### Test goal
> 
> See whether OpenHealth can help with **medical record parsing + AI review** better than your current flow.
> 
> ### Test with fake or redacted data first
> 
> Use one sanitized PDF or copy of a visit summary with:
> 
> - name removed
> - DOB removed
> - address removed
> - account numbers removed
> - MRN removed
> - phone numbers removed
> 
> ### Success criteria
> 
> Keep it only if it can reliably produce:
> 
> 1. medication mentions  
> 2. diagnosis/problem list  
> 3. appointment/follow-up items  
> 4. red-alert symptoms  
> 5. “questions for doctor/pharmacist”  
> 6. clean structured output you can move into QiLife/Supabase
> 
> If it cannot do that cleanly, it’s a cool GitHub project, not your MomCare engine.
> 
> ## Verdict
> 
> **Worth testing. Not worth migrating to.**
> 
> For your mom, the winning architecture is **your own structured care OS**, with OpenHealth used as a **local AI medical document assistant** if it proves useful. Don’t hand the keys to a young health-AI repo when the actual job is caregiver coordination, safety logging, medication verification, and family accountability.
