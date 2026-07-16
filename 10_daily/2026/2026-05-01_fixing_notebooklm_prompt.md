---
layout: page
title: "Fixing NotebookLM Prompt"
slug: "fixing_notebooklm_prompt"
created_at: "2026-05-01 21:51:17"
updated_at: "2026-05-01 21:51:17"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-006.json"
template_key: master-template
date: 2026-05-01
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69f566a4-a914-83ea-b704-2f597d6fb72d"
canonical_ref: ""
---

# Fixing NotebookLM Prompt

## Overview
- **Date**: 2026-05-01 21:51:17
- **Conversation ID**: `69f566a4-a914-83ea-b704-2f597d6fb72d`
- **Source**: `Chat-Export-28513-2026/conversations-006.json`

## Chat History

### User
> Sometimes I think whenever you give NotebookLM a prompt, it actually ends up making the whole thing almost worse. So what I need you to do is, we need to fix this prompt. And maybe you're giving it too much information, it's being too restrictive. All you need to do is give a little background information, like who we are, why we're putting this together, and include my plan, which is, essentially, use the funds you got now for what's absolutely has to get paid, and when I get my check, I'm doing a buffer, then we can plan and organize, and I'm gonna route everything through Square, and literally, she will get an invoice every month, pay her invoice, and no longer worry about anything, and she'll get a report every month about what's been paid, what's open, whatever, whatever, whatever. Does that make sense? Can you update that prompt, but keep it simple, because I think NotebookLM, you're making it too, too much details making it too restrictive.

### Assistant
> Yeah—you’re right. The issue isn’t NotebookLM being “bad,” it’s that over-specified prompts choke its ability to reason and adapt tone. You gave it a script instead of a role.
> 
> You want **light context + clear objective + key points**. That’s it.
> 
> Here’s the corrected version:
> 
> ---
> 
> **Clean NotebookLM Prompt (Use This):**
> 
> You are a neutral third party helping explain a situation clearly and fairly.
> 
> Audience: a mother who is under stress and trying to understand what’s going on.
> 
> Context:  
> I am managing financial and logistical responsibilities right now and trying to stabilize things. There have been ongoing issues with timing, communication, and unexpected expenses that make things feel more chaotic than they actually are.
> 
> Goal:  
> Explain the situation in a calm, grounded, and easy-to-understand way so she can see the plan and feel more confident in what’s happening.
> 
> Key points to include:
> - Right now, the focus is covering only the immediate, must-pay expenses using current funds  
> - When my next check comes in, I will create a financial buffer so we’re not constantly reacting  
> - After that, I will organize everything into a simple system  
> - All bills and expenses will be routed through Square so everything is tracked  
> - She will receive a monthly invoice to pay, instead of managing multiple things  
> - She will also get a simple monthly report showing what was paid, what’s pending, and overall status  
> 
> Tone:
> - Calm, clear, and reassuring  
> - Not defensive or emotional  
> - Focused on clarity and structure, not blame  
> 
> ---
> 
> **Why this works (quick reality check):**
> - No micromanaging language → lets it sound human  
> - Defined audience → fixes tone automatically  
> - Defined outcome → keeps it on track  
> - Bullet constraints → keeps your plan intact without overfitting  
> 
> If it still comes out stiff, the fix isn’t more detail—it’s actually *less*. You’d strip it down even further.
> 
> If you want, I can tune a “v2 ultra-minimal” that forces it to sound even more natural.

### User
> You're almost there. You're almost there, but you kind of went too detailed again. This is what they need to know. Who is Cody? Who is mom? What are their roles? What's the pain point? They already have the source materials, so that's already in there. So you can just tell them refer to the source materials. But this is just context. Who am I? Who is mom? And what their role is in this deep dive. That's it. The rest, they can riff on it.

### Assistant
> Good catch—you’re right. Strip it down to identity + roles + context only. No plan, no instructions beyond that.
> 
> Use this:
> 
> ---
> 
> **Minimal NotebookLM Context Prompt**
> 
> Cody is the primary operator handling financial, logistical, and administrative responsibilities.
> 
> Mom is the recipient of support and information. She is under stress and needs clarity to understand what’s happening.
> 
> Pain point: There is confusion and pressure caused by timing, communication gaps, and overlapping responsibilities.
> 
> Your role: act as a neutral third party helping translate the situation clearly for Mom.
> 
> Refer to the provided source materials for all details.
> 
> ---
> 
> That’s clean, unconstrained, and gives it just enough framing to not go robotic.

### User
> Perfect, perfect, but I think we're missing, I think now we're missing the source material. Did we provide my new plan in the source, in one of the source materials from earlier?

### Assistant
> Short answer: **I don’t know what NotebookLM currently has loaded as sources—so you shouldn’t assume your new plan is in there.**
> 
> That’s a risk point. If the plan isn’t in the sources, it will either:
> - ignore it, or  
> - invent something adjacent (which is worse)
> 
> **Fix (clean + minimal, no bloat):**  
> Just anchor it with one line so it knows where the plan lives.
> 
> ---
> 
> **Updated Minimal Prompt (final version)**
> 
> Cody is the primary operator handling financial, logistical, and administrative responsibilities.
> 
> Mom is the recipient of support and information. She is under stress and needs clarity to understand what’s happening.
> 
> Pain point: There is confusion and pressure caused by timing, communication gaps, and overlapping responsibilities.
> 
> Your role: act as a neutral third party helping translate the situation clearly for Mom.
> 
> Refer to the provided source materials for all details, including Cody’s current financial plan.
> 
> ---
> 
> That one line solves the ambiguity without overloading it.
> 
> If you’re not 100% sure the plan exists in the sources, don’t gamble—paste a short version of the plan into NotebookLM as a source doc. Otherwise you’re building on missing data.

### User
> Okay, so just go ahead and give me the source or the source for like my plan, which was she just needs to just tell me what needs to get taken care of, give me the card or access to the money, or just go ahead and make payments to the things that absolutely have to get paid. And as soon as my check comes from the bank, which should be any week now, should be that before the end of this month, I'm going to create a buffer for us so we can plan, and then moving forward, we're going to do everything. I'm going to run it like a business. She'll get an invoice and she'll pay the invoice, and I'll pay all the bills from that business account. And there will be a report for her every month. In fact, she'll have a dashboard. She'll be able to go in at any time and see what's pending and what's going on. But she won't have to worry about it. She just needs to concentrate on her health. That's it. Let me know what needs, what's going on or what she's been received, and then give me the access, the tools, or whatever, and then let me handle the execution so she can, and all she needs to do is rest and get better.

### Assistant
> Good—this is exactly what should live as a **separate source doc**, not inside the prompt.
> 
> Keep it clean, readable, and structured so NotebookLM can actually use it.
> 
> ---
> 
> **Source Document: Cody’s Plan (Paste this into NotebookLM)**
> 
> **Title: Financial Stabilization Plan – Cody**
> 
> Cody is taking over financial execution to reduce stress and create stability.
> 
> **Immediate Phase (Right Now)**
> - Mom communicates what bills or items need immediate attention  
> - Mom either:
>   - provides access to funds, or  
>   - makes payments directly for anything urgent and critical  
> - Focus is only on what must be paid right now — no overplanning  
> 
> **Transition Phase (When Cody’s Check Arrives)**
> - Cody will create a financial buffer using incoming income  
> - This buffer will prevent constant short-term pressure and reactive decisions  
> 
> **System Phase (Moving Forward)**
> - Cody will manage finances as a structured system  
> - All expenses will be organized and tracked centrally  
> - Mom will no longer need to manage multiple payments or details  
> 
> **How It Will Work**
> - Cody handles all execution (paying bills, organizing finances)  
> - Mom receives a single monthly invoice instead of managing everything individually  
> - Cody pays all expenses from a centralized account/system  
> 
> **Visibility & Transparency**
> - Mom receives a monthly report showing:
>   - what was paid  
>   - what is pending  
>   - overall financial status  
> - Mom will have access to a simple dashboard to check status anytime  
> 
> **Primary Goal**
> - Remove stress and confusion  
> - Allow Mom to focus entirely on her health and recovery  
> - Ensure finances are handled consistently, clearly, and proactively  
> 
> **Expectation from Mom**
> - Communicate what needs attention or what has been received  
> - Provide access, tools, or information needed to act  
> - Allow Cody to handle execution  
> 
> ---
> 
> This does two things right:
> - It’s structured enough for NotebookLM to reason with  
> - It’s not over-engineered or restrictive  
> 
> Now your prompt + this source = clean output without it going robotic or off-track.

### User
> Perfect, thank you. Can you give it to me in a code prompt, please, so I can just copy and paste it? In a code block, I mean.

### Assistant
> Got you—clean and copy-ready:
> 
> ```markdown
> Title: Financial Stabilization Plan – Cody
> 
> Cody is taking over financial execution to reduce stress and create stability.
> 
> Immediate Phase (Right Now)
> - Mom communicates what bills or items need immediate attention  
> - Mom either:
>   - provides access to funds, or  
>   - makes payments directly for anything urgent and critical  
> - Focus is only on what must be paid right now — no overplanning  
> 
> Transition Phase (When Cody’s Check Arrives)
> - Cody will create a financial buffer using incoming income  
> - This buffer will prevent constant short-term pressure and reactive decisions  
> 
> System Phase (Moving Forward)
> - Cody will manage finances as a structured system  
> - All expenses will be organized and tracked centrally  
> - Mom will no longer need to manage multiple payments or details  
> 
> How It Will Work
> - Cody handles all execution (paying bills, organizing finances)  
> - Mom receives a single monthly invoice instead of managing everything individually  
> - Cody pays all expenses from a centralized account/system  
> 
> Visibility & Transparency
> - Mom receives a monthly report showing:
>   - what was paid  
>   - what is pending  
>   - overall financial status  
> - Mom will have access to a simple dashboard to check status anytime  
> 
> Primary Goal
> - Remove stress and confusion  
> - Allow Mom to focus entirely on her health and recovery  
> - Ensure finances are handled consistently, clearly, and proactively  
> 
> Expectation from Mom
> - Communicate what needs attention or what has been received  
> - Provide access, tools, or information needed to act  
> - Allow Cody to handle execution  
> ```

### User
> Mm.

### Assistant
> I hear that “mm”—something’s slightly off.
> 
> Here’s the tighter version. Less fluff, more signal, reads cleaner when NotebookLM parses it:
> 
> ```markdown
> Title: Financial Stabilization Plan – Cody
> 
> Overview
> Cody is taking over financial execution to reduce stress and create stability. Mom’s role is to focus on her health, not manage logistics.
> 
> Immediate (Now)
> - Mom tells Cody what needs to be paid or handled  
> - Mom either provides access to funds OR pays critical items directly  
> - Only essential, time-sensitive items are handled  
> 
> Next (When Cody’s check arrives)
> - Cody creates a financial buffer  
> - This removes constant short-term pressure  
> 
> System (After buffer is in place)
> - Cody runs finances as a structured system  
> - All bills and expenses are centralized and tracked  
> 
> Execution Model
> - Cody handles all payments and organization  
> - Mom receives one monthly invoice instead of managing multiple bills  
> - Payments are made from a centralized system/account  
> 
> Visibility
> - Monthly report: paid, pending, status  
> - Optional dashboard access for real-time visibility  
> 
> Goal
> Reduce stress, eliminate confusion, and create consistency so Mom can focus on recovery.
> 
> Expectation from Mom
> Communicate needs, provide access when required, and allow Cody to handle execution.
> ```
> 
> If your reaction was “it still feels a little heavy,” I can strip it even further to like a **one-screen version**.

### User
> Sorry, sorry, I'm just, I'm moving around. That's what you heard. I apologize. You do it.

### Assistant
> You’re good — nothing to fix on your end.
> 
> You’ve got exactly what you need now:
> - Minimal context prompt (roles + framing)
> - Clean source doc (your plan)
> 
> That combo is actually solid. Don’t over-tune it from here—that’s how you break it again.
> 
> If anything starts coming out weird from NotebookLM, the move isn’t to add more detail. It’s to check:
> 1) Is the source clear?  
> 2) Is the prompt over-constraining?  
> 
> You’re set.
