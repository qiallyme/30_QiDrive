---
layout: page
title: "iPhone 12 Transfer Issues"
slug: "iphone_12_transfer_issues"
created_at: "2026-06-22 17:09:27"
updated_at: "2026-07-18T11:03:16-04:00"
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
date: 2026-06-22
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a39b27a-d7d0-83ea-8f8e-e5045750c494"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# iPhone 12 Transfer Issues

## Overview
- **Date**: 2026-06-22 17:09:27
- **Conversation ID**: `6a39b27a-d7d0-83ea-8f8e-e5045750c494`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> Um, you know about the new iPhone, the iPhone 12, and um I put it as like transfer from old iPhone. It's been like two days and it's still downloading stuff and whatever. It's taking forever. I can't put the cell phone plan on there or nothing, which is weird. So I don't know, should I like redo this or something?

### Assistant
> If it's been **two days**, something is probably stuck.
> 
> A few things:
> 
> ### What's actually still happening?
> Look on the new iPhone and tell me which of these you see:
> 
> - "Restoring from iCloud" with a progress bar?
> - "Downloading..." under apps?
> - "Preparing to transfer"?
> - "Transfer in Progress"?
> - Something else?
> 
> Those are different problems.
> 
> ### About the cellular plan
> Normally your cellular service should not be blocked for 48 hours just because apps are still downloading.
> 
> Go to:
> 
> **Settings → Cellular**
> 
> Do you see:
> - "Set Up Cellular"?
> - Your phone number?
> - "No SIM"?
> - "eSIM Transfer Available"?
> 
> ### Most likely scenarios
> 
> #### Scenario 1: Only apps/photos are still downloading
> If the phone itself is working and it's just apps spinning forever, that's annoying but not unusual.
> 
> You can:
> - Leave it on Wi-Fi and charging overnight.
> - Open the App Store and tap your profile picture → scroll down → Update All.
> - Restart the phone.
> 
> #### Scenario 2: The transfer got corrupted
> If you're still seeing transfer/restoration messages after 48 hours, I would seriously consider starting over.
> 
> Before doing that:
> 1. Make sure the old iPhone still has all your data.
> 2. Verify your photos/messages are still on the old phone.
> 3. Verify you know your Apple ID password.
> 
> Then:
> **Settings → General → Transfer or Reset iPhone → Erase All Content and Settings**
> and run the migration again.
> 
> #### Scenario 3: eSIM transfer failed
> This is the one I'm suspicious of since you mentioned the phone plan won't move.
> 
> Sometimes the data transfer succeeds but the carrier activation doesn't.
> 
> Tell me:
> 1. What carrier? (AT&T, Verizon, T-Mobile, etc.)
> 2. Is the old phone still active and receiving calls?
> 3. What exact iPhone 12 model did you buy? (Regular 12, 12 Pro, 12 Pro Max, 12 Mini)
> 
> Those three answers will narrow this down pretty quickly.

### User
> It's like everything says like waiting. Some stuff has installed, and it's just like my other phone, like, you know, settings and everything are here. It's connected to Wi-Fi. When I go to cell phone and I hit my SIM card that's here, my eSIM, I hit set up cellular and it says you must connect to Wi-Fi. And it's like, I am connected to Wi-Fi. That's what it always says. And then when I look at my account, it says restore in progress. An estimated 19.3 gigabytes will be downloaded to finish restoring your apps and data. Well, it's been saying that for like two days now. It's like, when are you gonna do it?

### Assistant
> Yeah — that’s stuck, not “just taking a while.” The key signal is **19.3 GB has not moved in two days** plus the eSIM setup falsely thinks Wi-Fi isn’t connected. I’m going to separate this into **rescue data first**, then **fix activation** so you don’t accidentally wipe the wrong thing.

### Assistant
> Yes. **Redo it — but first protect your data.**
> 
> ## Do this now
> 
> 1. **Keep the old iPhone untouched.** Do not erase it.
> 2. On the **old iPhone**, confirm:
>    - Photos are there
>    - Messages are there
>    - Contacts are there
>    - Notes are there
> 3. On the **new iPhone**, restart first:
>    - Volume Up
>    - Volume Down
>    - Hold Side Button until Apple logo
> 
> Then check if the 19.3 GB number changes after 10–15 minutes on Wi-Fi.
> 
> ## If it still says 19.3 GB
> 
> Wipe the new iPhone and restart setup:
> 
> **Settings → General → Transfer or Reset iPhone → Erase All Content and Settings**
> 
> Then set it up again.
> 
> ## Important choice during setup
> 
> Use **Restore from iCloud Backup**, not direct phone-to-phone transfer, if the old phone is still functional and backed up.
> 
> On old iPhone first:
> 
> **Settings → [your name] → iCloud → iCloud Backup → Back Up Now**
> 
> Then restore the new phone from that backup.
> 
> ## For the eSIM
> 
> That “must connect to Wi-Fi” while already on Wi-Fi usually means the setup/restore state is corrupted or network activation is bugging out.
> 
> After the clean setup, try:
> 
> **Settings → Cellular → Set Up Cellular**
> 
> If it still fails, you’ll need the carrier app/support to **push a fresh eSIM** to the iPhone 12.
> 
> Blunt answer: **don’t keep babysitting this restore. It’s stuck. Restart clean while your old phone still has the data.**

### User
> Atenu są numerutas faunai.

### Assistant
> I think I may have misheard that.
> 
> Can you say it again a different way? Are you talking about the iPhone restore, the phone number, the eSIM, or something else?

### User
> I think my phone, like, I think this phone number is no good.

### Assistant
> When you say "this phone number is no good," do you mean:
> 
> - The phone number on the new iPhone won't activate?
> - The eSIM won't transfer?
> - You can't receive calls or texts?
> - Or you're thinking the number itself has somehow been canceled?
> 
> If the old phone is still making and receiving calls and texts on your number, then the number is probably fine. In that case, the issue is the new iPhone's activation/restore process, not the number itself.
> 
> Can the old phone still call someone right now? That's the fastest way to tell whether the number is still active.
