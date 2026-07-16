---
layout: page
title: "Track narcissist behavior"
slug: "track_narcissist_behavior"
created_at: "2025-09-24 17:55:12"
updated_at: "2026-07-16T06:49:28-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-000.json"
template_key: master-template
date: 2025-09-24
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "68d476ba-7874-832c-a196-ae2103957a9f"
canonical_ref: ""
---

# Track narcissist behavior

## Overview
- **Date**: 2025-09-24 17:55:12
- **Conversation ID**: `68d476ba-7874-832c-a196-ae2103957a9f`
- **Source**: `Chat-Export-28513-2026/conversations-000.json`

## Chat History

### User
> if i was to put different acrtivities to track my narcisists friend behavior and track how much time i deal with him what activities should i have.

### Assistant
> Track these activities and fields. Use a simple CSV/Notion record per interaction.  
> 
> ### Activities to track (bare minimum)
> - Contact type (call / text / DM / in-person / voicemail)  
> - Start timestamp / End timestamp → compute duration (minutes)  
> - Initiator (them / you / 3rd party)  
> - Topic (money / logistics / drama / favor / apology / boundary)  
> - Trigger (ask, insult, guilt, emergency, gaslight, joke)  
> - Boundary enforced? (yes/no) + which boundary  
> - Outcome (resolved / escalated / hung up / ignored / postponed)  
> - Emotional cost (0–10)  
> - Productivity impact (minutes lost from work)  
> - Follow-up required? (yes/no) + due date  
> - Action taken (responded / delayed / didn’t respond / blocked / set limit)  
> - Evidence attached (screenshot/link)  
> - Pattern flag (repeated ask / boundary test / love-bomb / bait)  
> - Notes (short factual summary)
> 
> ### Metrics to compute (daily / weekly)
> - Total interactions  
> - Total time dealing (sum duration)  
> - % initiated by them  
> - Avg emotional cost  
> - Minutes lost to work  
> - # boundary breaches  
> - # times you enforced boundary vs ignored  
> - Top 3 topics by frequency  
> - Escalation events count
> 
> ### Quick CSV header (copy/paste)
> `date,start,end,duration_min,contact_type,initiator,topic,trigger,boundary_enforced,outcome,emotional_cost,productivity_loss_min,follow_up,follow_up_date,action_taken,evidence,pattern_flag,notes`
> 
> ### Example row
> `2025-09-24,13:05,13:22,17,text,them,money,pressure,yes,postponed,6,30,yes,2025-09-25,delayed_response,ss1.png,repeated ask,"asked for invoice twice; demanded immediate help"`
> 
> ### Notion/Obsidian fields
> - properties: Date, Duration (number), Contact Type (select), Initiator (select), Topic (multi-select), Boundary Enforced (checkbox), Emotional Cost (number), Productivity Loss (number), Action Taken (select), Evidence (files), Tags (multi), Follow-up (date), Notes (text).
> 
> ### Two-tier solution
> 1) Bare fix: start recording using the CSV header above. Log every interaction for 2 weeks. Review weekly totals.  
> 2) Upgrade / future-proof: build a Notion database or simple Airtable with those fields. Add automation: when Emotional Cost ≥8 or Boundary Breach ≥2 in 7 days, auto-create a “Boundary Review” task and set a hard action (mute/block threshold). Add a weekly dashboard showing trends and a rolling 4-week heatmap.
> 
> ### Short rules for logging
> - Record within 24 hours.  
> - Keep notes factual. No editorializing.  
> - Attach screenshots when possible.  
> - Use timing to justify boundary enforcement to yourself and others.
> 
> Want a Notion template or a CSV file I can generate now?

### User
> no i mean like, Sleeping, Intimate, Argument, Using gaslighting and parvo like behaviors and lashin out or physical.

### Assistant
> Got it. Here’s a compact list of **activity types** you can track plus the exact CSV fields to log them. Use factual, short entries.
> 
> ### Activity types (pick one per interaction)
> - **Sleeping / Present** — they’re physically there but passive.  
> - **Intimate / Sexual** — consensual intimacy. Track consent and safety.  
> - **Argument / Verbal Fight** — heated words, shouting.  
> - **Gaslighting / Manipulation** — denying facts, twisting truth.  
> - **Passive-Aggressive** — sarcasm, silent snub, undermining.  
> - **Love-bombing / Charm** — flattery, excessive gifts, sudden affection.  
> - **Boundary-test** — asks past agreed limits.  
> - **Financial Pressure** — demands money, guilt trips for cash.  
> - **Threats / Intimidation** — explicit threats or coercion.  
> - **Lashing Out / Angry Physical Gestures** — throwing, slamming, pushing (non-injurious).  
> - **Physical Assault** — hitting, restraining, injuring. (Flag as safety).  
> - **Stalking / Monitoring** — excessive checking, showing up uninvited.  
> - **Silent Treatment / Withholding** — refusal to respond as control.  
> - **Apology / Repair Attempt** — genuine repair, make amends.  
> - **Substance-influenced** — under alcohol/drugs.  
> - **Other / Misc.**
> 
> ### Severity scale (use number)
> 1 = Low annoyance  
> 2 = Noticeable disruption  
> 3 = High emotional cost  
> 4 = Safety risk (non-injury)  
> 5 = Immediate danger / assault
> 
> ### Immediate flags (checkbox-style)
> - SafetyConcern (yes/no)  
> - PoliceNeeded (yes/no)  
> - MedicalNeeded (yes/no)  
> - Blocked (yes/no)  
> - EvidenceAttached (yes/no)
> 
> ### CSV header (copy/paste)
> `date,start_time,end_time,duration_min,activity_type,subtype,initiator,location,severity,SafetyConcern,PoliceNeeded,MedicalNeeded,consent_status,emotional_cost,productivity_loss_min,follow_up_needed,follow_up_date,action_taken,evidence,notes`
> 
> ### Field notes (short)
> - **subtype**: short phrase (e.g., “gaslight—deny text”, “intimate—consensual”).  
> - **consent_status**: for Intimate — `consensual / coerced / unclear`.  
> - **initiator**: `them / you / third`  
> - **evidence**: filename or screenshot short tag.  
> - **notes**: one factual sentence only.
> 
> ### Example rows
> `2025-09-24,22:10,22:40,30,Intimate,consensual,them,home,1,no,no,no,consensual,2,0,no,,left early to avoid argument,photo1.jpg`  
> `2025-09-25,14:05,14:22,17,Gaslighting,deny earlier promise,them,cafe,3,yes,no,no,,6,45,yes,2025-09-26,delayed response,ss2.png,"said I agreed when I did not"`
> 
> ### Quick rules
> - Log within 24 hours.  
> - Keep entries factual. No labels like “crazy” or “psycho.”  
> - If **severity ≥4**, mark SafetyConcern=yes and follow your safety plan.  
> - Use the data to set thresholds. e.g., 3 incidents ≥ severity 3 in 7 days → escalate (mute/block/safety check).
> 
> Want a ready CSV file I can paste here now?

### User
> can we make this like 5

### Assistant
> If you only want 5 activity categories to keep it simple, here’s a clean framework:
> 
> ### Core 5 to Track
> 1. **Peaceful / Neutral**  
>    - Sleeping, chilling, present without conflict.  
> 2. **Intimate / Affectionate**  
>    - Sexual, cuddling, physical closeness. Log consent clearly.  
> 3. **Argument / Verbal Conflict**  
>    - Disagreement, shouting, circular fights.  
> 4. **Manipulation / Narc Tactics**  
>    - Gaslighting, guilt-trips, passive-aggressive, love-bombing.  
> 5. **Aggression / Physical Risk**  
>    - Lashing out, throwing things, hitting, unsafe behavior.
> 
> ### Optional fields
> - **Duration (minutes)**  
> - **Initiator (them/you)**  
> - **Severity (1–5)**  
> - **Consent (for Intimate)**  
> - **Safety flag (yes/no)**  
> - **Notes (one factual line)**  
> 
> ### Example CSV header
> `date,start_time,end_time,duration_min,activity_type,initiator,severity,consent_status,safety_flag,notes`
> 
> This way you can log everything into just 5 buckets but still capture intensity and safety flags.  
> 
> Want me to spin you up a **ready-to-use CSV template** with those 5 columns plus severity/notes pre-set?

### User
> what do you call when they just wotn go away, like they just wont leave your side for days at a time

### Assistant
> That pattern is usually called **clinginess** or **enmeshment** in general terms.  
> In narcissistic or toxic dynamics, it is often described as:  
> 
> - **Hovering** — they stick around to keep control or attention.  
> - **Engulfment** — they won’t allow space, take over your time.  
> - **Smothering** — constant presence, no room to breathe.  
> - **Invasion of boundaries** — refusing to respect limits on time/space.  
> 
> For your 5-category tracker, that behavior fits best under **Manipulation / Narc Tactics**, with a subtype note like *hovering/clingy*.  
> 
> Do you want me to add **“Clingy / Hovering”** as its own sixth activity type, or fold it into Manipulation with a subtype field?
