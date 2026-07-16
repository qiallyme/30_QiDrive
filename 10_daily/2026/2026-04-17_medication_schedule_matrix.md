---
layout: page
title: "Medication Schedule Matrix"
slug: "medication_schedule_matrix"
created_at: "2026-04-17 00:24:22"
updated_at: "2026-04-17 00:24:22"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-005.json"
template_key: master-template
date: 2026-04-17
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69e1c3d1-e61c-83ea-a95f-2214456c6a61"
canonical_ref: ""
---

# Medication Schedule Matrix

## Overview
- **Date**: 2026-04-17 00:24:22
- **Conversation ID**: `69e1c3d1-e61c-83ea-a95f-2214456c6a61`
- **Source**: `Chat-Export-28513-2026/conversations-005.json`

## Chat History

### User
> whats the best way to compile my moms medicine list into a matrices i can print out and all she has to do is check of the medication taken and the time, like x axis is the time of day (hours) y is the medication and dosages. what do you think.

### Assistant
> Yes — a **printable MAR-style sheet** is the right move.
> 
> But do **not** make it just “hours across the top, meds down the side” with nothing else. That gets messy fast, especially if she has:
> - meds with different frequencies
> - as-needed meds
> - inhalers/nebulizers
> - dose changes
> - half tablets or variable instructions
> 
> The best setup is a **2-part system**:
> 
> ## 1) Master medication list
> This is the reference sheet. One line per med.
> 
> Columns:
> - Medication name
> - Strength
> - Actual dose taken
> - What it’s for
> - When to take it
> - Special instructions
> - Prescriber
> - Pharmacy
> - Refill info
> 
> Example:
> - Gabapentin | 300 mg | 1 capsule | nerve pain | 8 AM / 8 PM | may cause drowsiness
> - Albuterol neb | 2.5 mg/3 mL | 1 treatment | breathing | every 4 hrs PRN | record symptoms too
> 
> This page stays mostly static.
> 
> ## 2) Daily checkoff matrix
> This is the tracking page she actually uses.
> 
> ### Best layout
> **Rows**
> - Medication name
> - Dose
> - Optional: route (pill, inhaler, nebulizer)
> 
> **Columns**
> - Scheduled times only, not every single hour unless she truly has hourly meds
> 
> So instead of:
> `6 AM | 7 AM | 8 AM | 9 AM | 10 AM ...`
> 
> Do:
> `6 AM | 8 AM | 12 PM | 4 PM | 8 PM | Bedtime`
> 
> Or even better, only include the times that matter for *her actual regimen*.
> 
> Each cell should have:
> - checkbox
> - tiny space for actual time taken
> - optional initials
> 
> Example row:
> 
> | Med | Dose | 8 AM | 12 PM | 4 PM | 8 PM | Bedtime |
> |---|---|---|---|---|---|---|
> | Gabapentin | 300 mg | ☐ ___ |  |  | ☐ ___ |  |
> | Cyclobenzaprine | 5 mg |  |  | ☐ ___ |  | ☐ ___ |
> 
> That’s cleaner than a full 24-hour grid for most people.
> 
> ## What I’d do for your mom specifically
> Use **three sections on the same daily sheet**:
> 
> ### A. Scheduled meds
> Stuff taken on a regular schedule.
> 
> ### B. PRN / as-needed meds
> Separate this completely from the main grid.
> 
> Columns:
> - Medication
> - Dose
> - Time given
> - Reason
> - Effect after 30–60 min
> 
> This matters because PRNs should not just get a checkbox. You need context.
> 
> ### C. Treatments / monitoring
> For things like:
> - nebulizer
> - oxygen check
> - pulse ox
> - CPAP
> - pain score
> - temp
> 
> That keeps medication tracking from turning into a chaotic mixed log.
> 
> ## What not to do
> Do **not** make one giant mega-grid with:
> - every med
> - every symptom
> - every hour
> - every note
> - every vital sign
> 
> That becomes unreadable and nobody uses it after day two.
> 
> ## Best printable format
> Use **landscape letter size**:
> - 8.5 x 11
> - larger font
> - high contrast
> - enough white space to write real times
> 
> And make it **one page per day** max, plus one master med list page.
> 
> ## My recommendation
> Build:
> - **Page 1:** Master Medication List
> - **Page 2:** Daily Medication & Treatment Checkoff Sheet
> - **Page 3:** PRN / Symptoms / Notes Log
> 
> That gives you structure without making her think too hard.
> 
> ## The real answer
> Your base idea is good.  
> A plain hour-by-hour X/Y matrix is **close**, but not quite enough.
> 
> The smarter version is:
> - **scheduled-time matrix for routine meds**
> - **separate PRN table**
> - **separate monitoring/treatment section**
> 
> That’s the format most likely to actually get used and reduce mistakes.
> 
> I can turn this into a clean printable one-page template for you next.

### User
> ok, here is the spreed sheet i have.

### Assistant
> I’m opening the sheet and checking how it’s structured now, then I’ll turn that into a cleaner printable med matrix instead of guessing.

### Assistant
> I turned your workbook into a cleaner printable tracker.
> 
> Download it here:
> [care-sheets_printable_med_tracker.xlsx](sandbox:/mnt/data/care-sheets_printable_med_tracker.xlsx)
> 
> What’s inside:
> - **Print_Master_Meds** — cleaned reference list from your source tabs
> - **Print_Daily_Checkoff** — daily matrix with checkoff boxes and space to write actual time
> - **Print_PRN_and_Interval** — as-needed meds log + interval med section
> 
> Important:
> - A few entries are flagged for **review** because the source sheet shows an expired/discard date.
> - Some “once daily” meds were placed in **Morning as a placeholder** because the source data didn’t include exact times.
> 
> If you want, next I can do one of two things:
> 1. make this into a **weekly version**, or  
> 2. tighten the schedule into **exact hour columns** once you tell me the real administration times.
