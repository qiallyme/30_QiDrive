---
layout: page
title: "Lyft Daily Log Setup"
slug: "lyft_daily_log_setup"
created_at: "2026-03-06 22:56:47"
updated_at: "2026-03-06 22:56:47"
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
date: 2026-03-06
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69abaff5-041c-8325-bc6d-161dde7615eb"
canonical_ref: ""
---

# Lyft Daily Log Setup

## Overview
- **Date**: 2026-03-06 22:56:47
- **Conversation ID**: `69abaff5-041c-8325-bc6d-161dde7615eb`
- **Source**: `Chat-Export-28513-2026/conversations-004.json`

## Chat History

### User
> i need a daily tab on my lyft work, like starting odometer ending or manual mileage entry expenses, file upload for reaceipts, total expense and income for hte day and such

### Assistant
> You basically want a **daily driver log** — but built like a **tiny ops dashboard**, not a boring spreadsheet. Think: *one tab per day → log everything → auto totals → attach receipts*. This also aligns nicely with the systems you’ve been building (Qi-style logging).
> 
> Here’s the **clean structure** I’d use.
> 
> ---
> 
> # Lyft Daily Log — Structure
> 
> ## 1️⃣ Daily Summary (top of the tab)
> This gives you a **quick operational snapshot**.
> 
> **Fields**
> 
> | Field | Type |
> |---|---|
> | Date | Auto |
> | Start Time | Time |
> | End Time | Time |
> | Starting Odometer | Number |
> | Ending Odometer | Number |
> | Manual Mileage (optional override) | Number |
> | Total Miles Driven | Auto calc |
> | Gross Earnings | Currency |
> | Cash Tips | Currency |
> | Other Income | Currency |
> | Total Income | Auto calc |
> | Total Expenses | Auto calc |
> | Net Income | Auto calc |
> 
> **Formula logic**
> 
> ```
> Total Miles = Ending Odometer - Starting Odometer
> ```
> 
> or
> 
> ```
> If Manual Mileage entered → use Manual
> ```
> 
> ```
> Total Income = Gross Earnings + Cash Tips + Other Income
> ```
> 
> ```
> Net Income = Total Income - Total Expenses
> ```
> 
> ---
> 
> # 2️⃣ Expense Tracker (sub-table)
> Every expense logged separately.
> 
> | Field | Type |
> |---|---|
> | Expense Type | Dropdown |
> | Amount | Currency |
> | Notes | Text |
> | Receipt Upload | File |
> 
> **Expense Types**
> 
> - Gas
> - Car Wash
> - Parking
> - Toll
> - Food (driver meal)
> - Phone
> - Maintenance
> - Misc
> 
> Auto-sum:
> 
> ```
> Total Expenses = SUM(Expense Amount)
> ```
> 
> ---
> 
> # 3️⃣ Trip Metrics (optional but powerful)
> 
> | Field | Type |
> |---|---|
> | Rides Completed | Number |
> | Online Time | Hours |
> | Ride Time | Hours |
> | Average Ride Earnings | Auto |
> | Earnings per Hour | Auto |
> | Earnings per Mile | Auto |
> 
> Formulas:
> 
> ```
> Avg Ride = Gross Earnings / Rides
> ```
> 
> ```
> $ per Hour = Gross / Online Time
> ```
> 
> ```
> $ per Mile = Gross / Miles
> ```
> 
> This shows you **if the day was actually worth it**.
> 
> ---
> 
> # 4️⃣ Receipt Upload Section
> 
> Just a file upload area.
> 
> Fields:
> 
> | Field | Type |
> |---|---|
> | File | Upload |
> | Expense Link | Relation to expense |
> 
> This keeps **audit proof for taxes**.
> 
> ---
> 
> # 5️⃣ End-of-Day Quick Reflection (optional but useful)
> 
> | Field | Type |
> |---|---|
> | Area Driven | Text |
> | Peak Hours Worked | Text |
> | Strategy Notes | Text |
> | Rating Issues | Text |
> 
> Example:
> 
> > Downtown surge after 10pm was worth it  
> > Avoid east side — low ride density
> 
> This builds your **driver intelligence over time**.
> 
> ---
> 
> # 6️⃣ Monthly Rollup (automatic)
> 
> Across all daily tabs:
> 
> | Metric | Formula |
> |---|---|
> | Total Miles | SUM |
> | Total Income | SUM |
> | Total Expenses | SUM |
> | Net Profit | SUM |
> 
> This becomes **tax ready**.
> 
> ---
> 
> # The Best Tool for This (honestly)
> 
> You have 3 good options:
> 
> ### Option A — **Notion database**
> Best for:
> 
> - mobile entry
> - file uploads
> - daily template
> 
> ### Option B — **Airtable**
> Best for:
> 
> - calculations
> - cleaner interface
> - receipt attachments
> 
> ### Option C — **your own PWA**
> Best for:
> 
> - full control
> - connects to Qi systems
> - Supabase backend
> 
> ---
> 
> # If you want the slickest workflow
> 
> Daily flow would be:
> 
> 1️⃣ Open phone  
> 2️⃣ Tap **“Start Shift”**  
> 3️⃣ Enter odometer  
> 4️⃣ During day → add expenses  
> 5️⃣ Upload receipts  
> 6️⃣ End shift → enter final odometer + earnings  
> 7️⃣ Dashboard shows profit instantly
> 
> ---
> 
> # If you want, I can also build you
> 
> - a **clean Airtable template**
> - a **Notion template**
> - OR a **simple HTML PWA driver log** you can install on your phone
> 
> The **PWA route would actually be very on-brand with your Qi stack** and takes about **15 minutes to scaffold**.
> 
> If you want that, say the word and I’ll drop the **full UI + database schema + installable PWA**.

### User
> give me the csvs to import. i got to go.

### Assistant
> Yep. Don’t overcomplicate it.
> 
> Use **3 CSVs** so you don’t trap yourself in one ugly flat file:
> 
> 1. **daily_shifts.csv** → one row per workday  
> 2. **daily_expenses.csv** → multiple expenses per day  
> 3. **daily_receipts.csv** → file tracking / attachment reference  
> 
> If your system only wants one file, import **daily_shifts.csv** first and add the others after.
> 
> ## 1) `daily_shifts.csv`
> 
> ```csv
> shift_id,shift_date,platform,start_time,end_time,starting_odometer,ending_odometer,manual_mileage,total_miles,gross_earnings,cash_tips,other_income,total_income,total_expenses,net_income,rides_completed,online_hours,ride_hours,earnings_per_hour,earnings_per_mile,area_driven,notes,status
> SHIFT-2026-03-06-001,2026-03-06,Lyft,08:00 PM,11:30 PM,125000,125086,,86,142.50,12.00,0.00,154.50,28.75,125.75,11,3.50,2.80,44.14,1.80,Evansville West Side,"Solid evening shift",Closed
> SHIFT-2026-03-07-001,2026-03-07,Lyft,09:00 AM,01:15 PM,125086,125154,,68,96.00,5.00,0.00,101.00,18.40,82.60,8,4.25,3.10,23.76,1.49,Evansville East Side,"Slow lunch traffic",Closed
> SHIFT-2026-03-08-001,2026-03-08,Lyft,05:30 PM,10:45 PM,125154,125269,,115,188.25,18.00,0.00,206.25,41.20,165.05,15,5.25,4.30,39.29,1.79,Downtown + East,"Weekend surge helped",Closed
> ```
> 
> ## 2) `daily_expenses.csv`
> 
> ```csv
> expense_id,shift_id,expense_date,expense_type,vendor,amount,payment_method,is_business_only,receipt_ref,notes
> EXP-2026-03-06-001,SHIFT-2026-03-06-001,2026-03-06,Gas,Thorntons,22.50,Debit,Yes,RCPT-2026-03-06-001,"Fuel before shift"
> EXP-2026-03-06-002,SHIFT-2026-03-06-001,2026-03-06,Food,Taco Bell,6.25,Debit,No,RCPT-2026-03-06-002,"Driver meal"
> EXP-2026-03-07-001,SHIFT-2026-03-07-001,2026-03-07,Parking,Downtown Meter,3.00,Card,Yes,RCPT-2026-03-07-001,"Short downtown stop"
> EXP-2026-03-07-002,SHIFT-2026-03-07-001,2026-03-07,Car Wash,Mike's Car Wash,15.40,Debit,Yes,RCPT-2026-03-07-002,"Quick wash"
> EXP-2026-03-08-001,SHIFT-2026-03-08-001,2026-03-08,Gas,Shell,34.20,Credit,Yes,RCPT-2026-03-08-001,"Weekend fill-up"
> EXP-2026-03-08-002,SHIFT-2026-03-08-001,2026-03-08,Toll,Indiana Toll,7.00,Card,Yes,RCPT-2026-03-08-002,"Bridge toll"
> ```
> 
> ## 3) `daily_receipts.csv`
> 
> ```csv
> receipt_ref,shift_id,expense_id,receipt_date,file_name,file_url,file_path,upload_status,notes
> RCPT-2026-03-06-001,SHIFT-2026-03-06-001,EXP-2026-03-06-001,2026-03-06,2026-03-06_thorntons_gas.jpg,,/receipts/2026/03/2026-03-06_thorntons_gas.jpg,Pending,"Attach gas receipt image"
> RCPT-2026-03-06-002,SHIFT-2026-03-06-001,EXP-2026-03-06-002,2026-03-06,2026-03-06_tacobell_meal.jpg,,/receipts/2026/03/2026-03-06_tacobell_meal.jpg,Pending,"Attach food receipt image"
> RCPT-2026-03-07-001,SHIFT-2026-03-07-001,EXP-2026-03-07-001,2026-03-07,2026-03-07_parking_meter.jpg,,/receipts/2026/03/2026-03-07_parking_meter.jpg,Pending,"Attach parking receipt"
> RCPT-2026-03-07-002,SHIFT-2026-03-07-001,EXP-2026-03-07-002,2026-03-07,2026-03-07_car_wash.jpg,,/receipts/2026/03/2026-03-07_car_wash.jpg,Pending,"Attach wash receipt"
> RCPT-2026-03-08-001,SHIFT-2026-03-08-001,EXP-2026-03-08-001,2026-03-08,2026-03-08_shell_gas.jpg,,/receipts/2026/03/2026-03-08_shell_gas.jpg,Pending,"Attach fuel receipt"
> RCPT-2026-03-08-002,SHIFT-2026-03-08-001,EXP-2026-03-08-002,2026-03-08,2026-03-08_bridge_toll.jpg,,/receipts/2026/03/2026-03-08_bridge_toll.jpg,Pending,"Attach toll receipt"
> ```
> 
> ## If you want a barebones version instead
> 
> Use this single CSV:
> 
> ```csv
> shift_id,shift_date,start_time,end_time,starting_odometer,ending_odometer,manual_mileage,gross_earnings,cash_tips,other_income,total_expenses,rides_completed,area_driven,notes
> SHIFT-2026-03-06-001,2026-03-06,08:00 PM,11:30 PM,125000,125086,,142.50,12.00,0.00,28.75,11,Evansville West Side,"Solid evening shift"
> SHIFT-2026-03-07-001,2026-03-07,09:00 AM,01:15 PM,125086,125154,,96.00,5.00,0.00,18.40,8,Evansville East Side,"Slow lunch traffic"
> SHIFT-2026-03-08-001,2026-03-08,05:30 PM,10:45 PM,125154,125269,,188.25,18.00,0.00,41.20,15,Downtown + East,"Weekend surge helped"
> ```
> 
> ## Quick field rule so you don’t get jammed up
> - **shift_id** = unique row ID
> - **manual_mileage** = use only if odometer is missing
> - **total_miles / total_income / net_income** = let the app calculate if possible
> - **receipt_ref** links expenses to uploaded files
> 
> Best move: import **daily_shifts** and **daily_expenses** first, then wire receipts after.
