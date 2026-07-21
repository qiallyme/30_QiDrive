---
layout: page
title: "WhatsApp business templates"
slug: "whatsapp_business_templates"
created_at: "2025-09-07 23:21:15"
updated_at: "2026-07-18T11:03:12-04:00"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-000.json"
template_key: master-template
date: 2025-09-07
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "68be59a5-6128-8327-9dc4-3ce1815d24bd"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# WhatsApp business templates

## Overview
- **Date**: 2025-09-07 23:21:15
- **Conversation ID**: `68be59a5-6128-8327-9dc4-3ce1815d24bd`
- **Source**: `Chat-Export-28513-2026/conversations-000.json`

## Chat History

### User
> can you provide me with 5 message templates that are whatsapp business meta approved to send to my clients with variable placeholders.

### Assistant
> Got you. WhatsApp Business messages that Meta approves for client outreach must fit into **pre-approved template categories** (like transactional, appointment update, payment reminder, etc.), and they have to be polite, professional, and clearly useful. They can’t be spammy or purely promotional.  
> 
> Here are **five ready-to-use, Meta-compliant templates** with variable placeholders you can adapt:
> 
> ---
> 
> ### 1. Appointment Reminder
> ```
> Hi {{1}}, this is a friendly reminder of your {{2}} appointment scheduled for {{3}} at {{4}}.  
> Please reply "Confirm" to keep your slot or "Reschedule" if you need another time.
> ```
> - {{1}} = Client name  
> - {{2}} = Service type (e.g., consultation, call, meeting)  
> - {{3}} = Date  
> - {{4}} = Time  
> 
> ---
> 
> ### 2. Order/Project Update
> ```
> Hello {{1}}, your {{2}} is now {{3}}.  
> Tracking ID: {{4}}. You can follow progress here: {{5}}.
> ```
> - {{1}} = Client name  
> - {{2}} = Product/Project name  
> - {{3}} = Current status (e.g., shipped, in review, completed)  
> - {{4}} = Reference number  
> - {{5}} = Tracking link or project portal URL  
> 
> ---
> 
> ### 3. Payment Reminder
> ```
> Hi {{1}}, this is a reminder that your payment of {{2}} for {{3}} is due on {{4}}.  
> If you’ve already made the payment, kindly ignore this message. Otherwise, you can pay here: {{5}}.
> ```
> - {{1}} = Client name  
> - {{2}} = Amount  
> - {{3}} = Service or product description  
> - {{4}} = Due date  
> - {{5}} = Payment link  
> 
> ---
> 
> ### 4. Document/Submission Confirmation
> ```
> Hello {{1}}, we’ve received your {{2}} on {{3}}.  
> Our team will review it and update you by {{4}}.  
> For your records, reference number: {{5}}.
> ```
> - {{1}} = Client name  
> - {{2}} = Document/Submission type (e.g., application, form, file)  
> - {{3}} = Date received  
> - {{4}} = Expected update date  
> - {{5}} = Reference number  
> 
> ---
> 
> ### 5. Service Completion & Feedback Request
> ```
> Hi {{1}}, your {{2}} was successfully completed on {{3}}.  
> We’d love to hear your feedback! Please take a minute to share your thoughts here: {{4}}.
> ```
> - {{1}} = Client name  
> - {{2}} = Service or project name  
> - {{3}} = Completion date  
> - {{4}} = Feedback/Survey link  
> 
> ---
> 
> These are **safe, Meta-approved categories** (reminders, updates, confirmations, receipts, feedback). If you need, I can also shape them into a **JSON upload format** for WhatsApp Business Manager so you can register them directly with placeholders.  
> 
> Want me to prep them in that exact JSON structure for one-click upload?

### User
> ok so bigin is limited to things like profiel inforamtion in the variable fields, so they need to be generic and really say things that, theres and update for your project, please view in your protal if you ahve acccess. or soemthign like that.

### Assistant
> Got it — since Zoho Bigin only lets you pass simple variables (like name, email, maybe ID), we’ll keep the templates **generic** and **self-contained**. They won’t rely on detailed variable fields, just the essentials like `{{customer_name}}` or `{{company_name}}`. That way they’ll always pass Meta’s approval but still feel personal and professional.  
> 
> Here are **five trimmed-down, Bigin-friendly WhatsApp templates**:
> 
> ---
> 
> ### 1. Project Update  
> ```
> Hello {{customer_name}}, there’s an update available for your project.  
> Please log in to your client portal to view the latest details.  
> Thank you,  
> {{company_name}}
> ```
> 
> ---
> 
> ### 2. Document Received  
> ```
> Hi {{customer_name}}, we’ve received your submission.  
> Our team will review it and share any updates in your client portal.  
> – {{company_name}}
> ```
> 
> ---
> 
> ### 3. General Notification  
> ```
> Hello {{customer_name}}, this is a notification from {{company_name}}.  
> Please check your portal for new information or actions required.  
> ```
> 
> ---
> 
> ### 4. Appointment/Task Reminder  
> ```
> Hi {{customer_name}}, this is a reminder from {{company_name}}.  
> Please check your client portal for upcoming tasks or scheduled items.  
> ```
> 
> ---
> 
> ### 5. Completion + Next Steps  
> ```
> Hello {{customer_name}}, your recent service request has been completed.  
> For details and next steps, please view your client portal.  
> Thank you,  
> {{company_name}}
> ```
> 
> ---
> 
> These are intentionally **short, compliant, and generic** so Meta won’t flag them. They push the client back to the portal (your control center), while keeping personalization light.  
> 
> Do you want me to also turn these into the **Meta-approved JSON submission format** (with category + sample variables) so you can upload them directly to your WhatsApp Business Manager?

### User
> this was rejected: Template Preview

> Information

> Template Name

> Project Update

> Language

> English

> Category

> Utility

> Status

>  Rejected

> Preview

> Hello ${Contacts.First Name}, there’s an update available for your project.

> Please log in to your client portal to view the latest details.

> Thank you,

> ${Organization.Organization Name}

> 🌐 ${Organization.Website} --- > 
> 
> 
> and of course meta doesnt ever tell you why.

### Assistant
> Yeah, Meta is notorious for their black-box approvals — no feedback, just vibes. But after watching how templates get rejected, a few patterns emerge:  
> 
> 1. **Too promotional** → Anything that smells like marketing, links that aren’t clearly necessary, or wording like “log in to your portal” sometimes gets flagged. They want “utility” messages to be strictly informational.  
> 2. **Variable formatting** → They’re picky. `${Contacts.First Name}` might not pass — they expect `{{1}}`, `{{2}}`, etc. for placeholders.  
> 3. **Emoji or extra decoration** → Emojis in utility templates can cause rejection. That 🌐 probably tripped it.  
> 4. **Ambiguity** → “Update available for your project” without context could be misread as promotional. They prefer neutral wording like “Your project status has been updated.”  
> 
> Here’s a cleaned-up version of yours, in **Meta-friendly phrasing**:  
> 
> ---
> 
> ### Project Update (Utility) – Safer Version
> ```
> Hello {{1}}, your project status has been updated.  
> Please check your client portal for the latest information.  
> Thank you,  
> {{2}}
> ```
> 
> - {{1}} = First Name  
> - {{2}} = Company Name  
> 
> ---
> 
> ### Why this one is safer:
> - Removed emojis and URLs.  
> - Neutral language (“status has been updated” instead of “there’s an update available”).  
> - No promotional tone.  
> - Uses numbered placeholders instead of custom variable strings.  
> 
> ---
> 
> If you want the link included, Meta usually prefers something like:  
> ```
> You can view details here: {{3}}
> ```
> …but it’s best to submit the “no-link” version first, get it approved, and then clone it and add the URL as a variable.  
> 
> Do you want me to rewrite **all five templates** in this safer Meta-style so you can resubmit without more rejections?

### User
> you think this one will work. Hello ${Contacts.First Name}, your work project status has been updated and is available by accessing the QiAlly QiSuite Portal. Your Username: ${Contacts.Email}

> Portal Enabled?: ${Contacts.Portal Enabled}

> Please check your client portal for the latest information.

> Thank you,

> ${Organization.Organization Name}

### Assistant
> That version is *closer*, but it still has a couple of red flags that could get Meta’s robot bouncer shaking its head:  
> 
> - **Custom variable formatting** (`${Contacts.First Name}` etc.) → Meta wants `{{1}}`, `{{2}}`, not CRM-style placeholders. You can *map* those later in Bigin when you connect the template. If you submit with `${...}`, it’ll almost always bounce.  
> - **“Portal Enabled?: …”** → That line looks like internal system language, not client-facing. Meta might reject it as unclear or confusing.  
> - **Brand mentions** → “QiAlly QiSuite Portal” is fine if it’s your brand, but keep it short and factual (too many capitalized words sometimes looks promotional).  
> 
> Here’s a cleaned-up, more **Meta-compliant** version of what you’re aiming for:  
> 
> ---
> 
> ### Safer Submission Version
> ```
> Hello {{1}}, your project status has been updated.  
> You can access the client portal for details.  
> Username: {{2}}  
> Thank you,  
> {{3}}
> ```
> 
> - {{1}} = Contact First Name  
> - {{2}} = Contact Email (their username)  
> - {{3}} = Organization Name  
> 
> ---
> 
> **Why this should pass:**  
> - Neutral tone (“status has been updated”)  
> - Keeps username info, but avoids “Portal Enabled?” system text  
> - Uses Meta’s `{{}}` placeholder format  
> - No emoji, no unnecessary capitalization  
> 
> Once it’s approved, you can still map those variables in Bigin (`{{1}} = Contacts.First Name`, etc.).  
> 
> Would you like me to rewrite the other four templates you need into this **approval-safe style**, so you’ve got a whole compliant set ready?
