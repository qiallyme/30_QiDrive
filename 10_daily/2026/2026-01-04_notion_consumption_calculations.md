---
layout: page
title: "Notion Consumption Calculations"
slug: "notion_consumption_calculations"
created_at: "2026-01-04 07:33:03"
updated_at: "2026-01-04 07:33:03"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-003.json"
template_key: master-template
date: 2026-01-04
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "695a6bde-2610-832c-a255-779a97d69364"
canonical_ref: ""
---

# Notion Consumption Calculations

## Overview
- **Date**: 2026-01-04 07:33:03
- **Conversation ID**: `695a6bde-2610-832c-a255-779a97d69364`
- **Source**: `Chat-Export-28513-2026/conversations-003.json`

## Chat History

### User
> i need help figuring out the calculations and roll ups in notion for this table, that has dates when a product was received the number of units and i want to find out how many units per 30 days consumed month over month to get a anverage of daily consumptions how should i do that.

### Assistant
> You’re not crazy—this is a **classic Notion problem**, and the clean solution requires **two tables and deliberate rollups**. Trying to do this in one table will get brittle fast. I’ll give you the **correct, scalable approach**, then the exact formulas.
> 
> ---
> 
> ## What you are trying to calculate (clarified)
> 
> From **receipts over time** (date + units received), you want:
> 
> 1. **Units consumed per 30-day period**
> 2. **Month-over-month consumption**
> 3. **Average daily consumption** (rolling or monthly)
> 
> This is a **rate problem**, not a raw sum problem. That’s the key mental shift.
> 
> ---
> 
> ## Correct Architecture (don’t skip this)
> 
> ### Table 1 — **Inventory Events (Receipts)**
> Each row = a receipt or inventory adjustment.
> 
> Properties:
> - `Date Received` (Date)
> - `Units` (Number) → positive for received, negative if you track removals
> - `Product` (Relation → Products table)
> 
> You likely already have this.
> 
> ---
> 
> ### Table 2 — **Time Buckets (Months or Rolling 30-Day Periods)**
> 
> Each row = **one period** you want analytics for.
> 
> Choose ONE:
> - **Calendar Months** (recommended for MoM)
> - **Rolling 30-Day windows** (recommended for ops forecasting)
> 
> You can do both, but start with months.
> 
> Properties:
> - `Period Start` (Date)
> - `Period End` (Date)
> - `Product` (Relation → Products)
> - `Receipts (rollup)` → Units
> - `Total Units Received`
> - `Units Consumed`
> - `Avg Daily Consumption`
> 
> ---
> 
> ## Step 1: Define the Time Window
> 
> In **Time Buckets table**:
> 
> ### Period Start
> - Manual or formula (e.g. `2025-01-01`)
> 
> ### Period End (formula)
> ```notion
> dateAdd(prop("Period Start"), 1, "months")
> ```
> 
> (Use 30 days instead if you want rolling windows.)
> 
> ---
> 
> ## Step 2: Link Receipts to Time Buckets (Critical)
> 
> In **Inventory Events**, add:
> 
> ### `In Period?` (Formula)
> ```notion
> and(
>   prop("Date Received") >= prop("Period").prop("Period Start"),
>   prop("Date Received") < prop("Period").prop("Period End")
> )
> ```
> 
> ⚠️ This requires:
> - Inventory Events ↔ Time Buckets relation
> - One receipt can relate to multiple periods, but only **counts when In Period = true**
> 
> ---
> 
> ## Step 3: Roll Up Units Per Period
> 
> In **Time Buckets**:
> 
> ### `Total Units Received` (Rollup)
> - Relation: Inventory Events
> - Property: `Units`
> - Filter: `In Period` = true
> - Aggregation: **Sum**
> 
> Now you have **units per month / 30-day window**.
> 
> ---
> 
> ## Step 4: Convert Received → Consumed (Reality Check)
> 
> If you **only track receipts**, consumption must be inferred.
> 
> ### Option A — You track stock on hand (BEST)
> Then:
> ```text
> Consumed = Previous Period Ending Stock − Current Ending Stock
> ```
> 
> ### Option B — No stock tracking (most common)
> Then:
> ```text
> Consumption ≈ Units Received − Net Inventory Change
> ```
> 
> If inventory change is unknown, **assume steady draw**:
> ```text
> Consumption = Total Units Received
> ```
> 
> Be honest here—this is an estimate, not gospel.
> 
> ---
> 
> ## Step 5: Average Daily Consumption (Formula)
> 
> ### `Days in Period` (Formula)
> ```notion
> dateBetween(prop("Period End"), prop("Period Start"), "days")
> ```
> 
> ### `Avg Daily Consumption`
> ```notion
> prop("Total Units Received") / prop("Days in Period")
> ```
> 
> Now you have:
> - Monthly consumption
> - Daily burn rate
> - Comparable MoM metrics
> 
> ---
> 
> ## Optional (but powerful): Rolling 30-Day Average
> 
> Duplicate the Time Buckets table and instead of months:
> 
> ```notion
> dateAdd(prop("Period Start"), 30, "days")
> ```
> 
> This smooths spikes and is **far better for forecasting**.
> 
> ---
> 
> ## What NOT to Do (hard truth)
> 
> - ❌ Do not try to calculate this **inside the receipt table**
> - ❌ Do not rely on calendar grouping alone
> - ❌ Do not mix receipts and consumption logic in one property
> - ❌ Do not expect Notion to “just know” consumption without time buckets
> 
> ---
> 
> ## If you want, next we can:
> - Build **exact formulas tailored to your current schema**
> - Decide whether **monthly vs rolling is smarter** for your use case
> - Add **forecasting (days until depletion)**
> - Normalize for **multiple products**
> 
> If you want precision, paste:
> 1. Your current property names
> 2. Whether you track stock on hand
> 3. Monthly vs rolling preference
> 
> I’ll wire it cleanly.

### User
> put together the readme for this.

### Assistant
> README is drafted and structured for direct drop-in use.  
> 
> If you want, next steps I can do quickly and cleanly:
> - Tailor this README to **your exact property names**
> - Add a **worked example** (sample rows + numbers)
> - Append a **forecasting section** (days until depletion, reorder trigger)
> - Create a **one-page “How to Use”** for non-technical users
> 
> Tell me how production-grade you want this to be.
