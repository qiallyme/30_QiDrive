---
layout: page
title: "HTML Glance Sheet Review"
slug: "html_glance_sheet_review"
created_at: "2026-01-23 09:23:19"
updated_at: "2026-01-23 09:23:19"
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
date: 2026-01-23
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69739267-5fec-832b-858e-e4d0fc88bb2c"
canonical_ref: ""
---

# HTML Glance Sheet Review

## Overview
- **Date**: 2026-01-23 09:23:19
- **Conversation ID**: `69739267-5fec-832b-858e-e4d0fc88bb2c`
- **Source**: `Chat-Export-28513-2026/conversations-003.json`

## Chat History

### User
> <!DOCTYPE html>
> <html lang="en">
> <head>
>   <meta charset="UTF-8" />
>   <meta name="viewport" content="width=device-width,initial-scale=1" />
>   <title>Daily $100 Glance Sheet</title>
>   <style>
>     :root {
>       --bg: #ffffff; --card: #f8f9fa; --ink: #1a1a1a; --muted: #5f6368;
>       --border: #dadce0; --blue: #1a73e8; --green: #1e8e3e; --gold: #f9ab00; --red: #d93025;
>     }
>     body {
>       margin: 0; font-family: -apple-system, system-ui, sans-serif;
>       background: var(--bg); color: var(--ink); line-height: 1.4;
>     }
>     .container { max-width: 500px; margin: 0 auto; padding: 15px; }
>     .header { text-align: center; border-bottom: 2px solid var(--ink); margin-bottom: 20px; padding-bottom: 10px; }
>     h1 { margin: 0; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; }
>     
>     .checkpoint-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 20px; }
>     .tile { border: 2px solid var(--border); padding: 12px; border-radius: 12px; text-align: center; }
>     .tile b { display: block; font-size: 12px; color: var(--muted); }
>     .tile span { font-size: 22px; font-weight: 800; display: block; margin: 4px 0; }
>     
>     .bucket-box { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 15px; margin-bottom: 15px; }
>     .bucket-item { display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid var(--border); }
>     .bucket-item:last-child { border: 0; }
>     
>     .rule-tag { display: inline-block; background: #eee; padding: 4px 10px; border-radius: 5px; font-size: 12px; font-weight: bold; margin-bottom: 5px; }
>     .decision { border-left: 5px solid var(--ink); padding-left: 15px; font-style: italic; margin: 20px 0; }
>     
>     @media print {
>       .container { width: 100%; max-width: 100%; }
>       body { -webkit-print-color-adjust: exact; }
>     }
>   </style>
> </head>
> <body>
>   <div class="container">
>     <div class="header">
>       <h1>Daily $100 Glance</h1>
>       <p style="font-size: 13px; margin: 5px 0;">Fri/Sat Target: <b>$125</b></p>
>     </div>
> 
>     <div class="checkpoint-grid">
>       <div class="tile" style="border-color: var(--blue)"><b>6:00 AM</b><span>$25</span><small>25%</small></div>
>       <div class="tile" style="border-color: var(--green)"><b>12:00 PM</b><span>$50</span><small>50%</small></div>
>       <div class="tile" style="border-color: var(--gold)"><b>6:00 PM</b><span>$75</span><small>75%</small></div>
>       <div class="tile" style="border-color: var(--red)"><b>Midnight</b><span>$100</span><small>Done</small></div>
>     </div>
> 
>     <div class="bucket-box">
>       <div class="rule-tag">DAILY DEPOSITS</div>
>       <div class="bucket-item"><span>🏠 Rent</span><b>$43</b></div>
>       <div class="bucket-item"><span>🏡 Home</span><b>$33</b></div>
>       <div class="bucket-item"><span>🍽️ Plates</span><b>$23</b></div>
>       <p style="font-size: 11px; color: var(--muted); margin-top: 10px;">Extra cash goes to <b>Emergency Savings</b>.</p>
>     </div>
> 
>     <div class="decision">
>       <b>The Clock Rule:</b> If behind checkpoint, keep working. If ahead, you may rest.
>     </div>
> 
>     <div style="font-size: 13px;">
>       <b>Big Targets:</b>
>       <ul style="padding-left: 20px;">
>         <li>Plates: $700 (~30 days)</li>
>         <li>Home: $2,600 (~80 days)</li>
>       </ul>
>     </div>
>   </div>
> </body>
> </html>

### Assistant
> I’m going to be direct: this is **clean, usable, and not broken**. You’re not missing anything critical. What you *are* missing are a few high-leverage refinements that will make this more resilient, clearer under stress, and better for print and reuse.
> 
> Below is a tight review + concrete improvements. No fluff.
> 
> ---
> 
> ## What’s already solid
> - **Visual hierarchy works**: checkpoints → buckets → rule → targets.
> - **Cognitive load is low**: numbers are glanceable; nothing noisy.
> - **Print-safe**: you already handled `@media print` correctly.
> - **Constraint framing** (“Clock Rule”) is excellent for ADHD.
> 
> You did not screw this up.
> 
> ---
> 
> ## Gaps / risks (fix these)
> ### 1. Emojis may fail in print or some browsers
> If this is for **printing or courts / forms / PDFs**, emojis are unreliable.
> 
> **Fix**: add a text fallback or switch to icons via CSS.
> 
> Example:
> ```html
> <span class="label"><span aria-hidden="true">🏠</span> Rent</span>
> ```
> 
> And add:
> ```css
> @media print {
>   .label span[aria-hidden="true"] { display: none; }
> }
> ```
> 
> ---
> 
> ### 2. No way to mark *actual progress*
> Right now this is **static**. Under pressure, your brain will want:
> - “Where am I *now*?”
> - “Am I behind or ahead?”
> 
> **Minimal fix (no JS):** add a manual “Today’s Actual” row.
> 
> ```html
> <div class="bucket-item">
>   <span><b>Actual Today</b></span>
>   <b>______</b>
> </div>
> ```
> 
> This matters more than you think.
> 
> ---
> 
> ### 3. Color meaning is implicit, not explicit
> You know what blue/green/gold/red mean. Someone else won’t.  
> Future-you at 2am might not either.
> 
> **Fix**: add a micro-legend.
> 
> ```html
> <p style="font-size:11px;color:var(--muted);margin-top:8px;">
>   Blue = Start • Green = On Track • Gold = Push • Red = Finish
> </p>
> ```
> 
> Tiny change. Big clarity.
> 
> ---
> 
> ### 4. Hardcoded dates will age badly
> “Fri/Sat Target: $125” will betray you in a week.
> 
> **Fix**: label it structurally, not temporally.
> 
> Change:
> ```html
> Fri/Sat Target: <b>$125</b>
> ```
> 
> To:
> ```html
> High-Demand Day Target: <b>$125</b>
> ```
> 
> Or:
> ```html
> Peak-Day Target: <b>$125</b>
> ```
> 
> ---
> 
> ## Optional upgrades (only if you want)
> ### A. Make checkpoints reusable
> If you ever reuse this, abstract the times.
> 
> ```html
> <b>Checkpoint 1</b>
> <span>$25</span>
> <small>Morning</small>
> ```
> 
> This lets you adapt for night shifts or court days.
> 
> ---
> 
> ### B. Add a “Stop Condition” (very ADHD-safe)
> You already have a work rule. Add a **stop rule**.
> 
> ```html
> <div class="decision">
>   <b>Stop Rule:</b> When target is met, stop working. No “one more run.”
> </div>
> ```
> 
> This prevents burnout spirals.
> 
> ---
> 
> ## Verdict
> - This is **good enough to use today**.
> - With the 4 fixes above, it becomes **durable**, not just pretty.
> - Do **not** over-engineer this with JS unless you’re automating deposits.
> 
> If you want, next step I can:
> - Convert this into a **fillable PDF**
> - Add a **print-optimized black-and-white mode**
> - Or refactor it into a **Quartz / Obsidian daily sheet**
> 
> Tell me which direction—or say “lock it, ship it.”

### User
> Turn into a fillable pdf full color so it doubles as a cheat sheet and daily traveler and can you put tool tips in Pashto for zai.

### Assistant
> Done. This is now a **full-color, fillable PDF** that works as both a **daily traveler + cheat sheet**, with **Pashto tooltips for Zai** embedded in the fillable fields.
> 
> **What I delivered**
> - Fillable **“Actual”** fields for each checkpoint
> - Full color preserved (print-safe)
> - Clean layout for daily carry or reuse
> - **Pashto tooltips** on each entry field explaining what it’s for (hover/tap)
> 
> **Download it here:**
> [Download the fillable Daily $100 Glance PDF](sandbox:/mnt/data/Daily_100_Glance_Fillable.pdf)
> 
> **Important, straight talk**
> - Pashto uses Arabic script. Most modern PDF viewers (Adobe Reader, macOS Preview) will display the tooltips fine.
> - Some lightweight mobile viewers may show the Pashto text without proper letter shaping. That’s a PDF limitation, not your design.
> - Functionally, this is still 100% usable for Zai.
> 
> **If you want next-level**
> I can:
> 1. Add **fillable bucket totals** with tooltips  
> 2. Add a **“Day Complete” checkbox** (very grounding for ADHD)  
> 3. Produce a **black-and-white court-safe version**  
> 4. Add **English + Pashto dual tooltips**  
> 5. Lock layout but keep fields editable (traveler-proof)
> 
> Tell me what to add or say **“lock it”** and I won’t touch it further.

### User
> girl i need this in a great looking easy to understand with color html document that i qwill print out not this boring boxes on a white page.

### Assistant
> Yep — that PDF I gave you is functional, but visually it’s “DMV chic.” If you’re printing a **cheat sheet + daily traveler**, you want something that *looks* like a dashboard, not a tax form.
> 
> Here’s a **single-file, full-color, print-optimized HTML** version that’s easy to understand, with **fillable fields** and **Pashto tooltips for Zai** (hover on desktop; long-press sometimes works on mobile depending on browser).
> 
> Copy-paste into `daily_100_glance.html`, open in Chrome, and print.
> 
> ```html
> <!DOCTYPE html>
> <html lang="en">
> <head>
>   <meta charset="UTF-8" />
>   <meta name="viewport" content="width=device-width,initial-scale=1" />
>   <title>Daily $100 Glance Sheet</title>
>   <style>
>     :root{
>       --bg1:#0b1220;
>       --bg2:#0f1a30;
>       --card: rgba(255,255,255,.08);
>       --card2: rgba(255,255,255,.10);
>       --ink:#f5f7ff;
>       --muted: rgba(245,247,255,.72);
>       --border: rgba(255,255,255,.18);
> 
>       --blue:#4ea1ff;
>       --green:#3ee07d;
>       --gold:#ffd36a;
>       --red:#ff5b6e;
> 
>       --shadow: 0 18px 55px rgba(0,0,0,.35);
>       --radius: 18px;
>     }
> 
>     * { box-sizing: border-box; }
>     body{
>       margin:0;
>       font-family: -apple-system, system-ui, Segoe UI, Roboto, Arial, sans-serif;
>       color:var(--ink);
>       background: radial-gradient(1200px 900px at 20% 10%, #1b2c55 0%, rgba(27,44,85,0) 60%),
>                   radial-gradient(1000px 800px at 80% 30%, #2a1f5c 0%, rgba(42,31,92,0) 55%),
>                   linear-gradient(160deg, var(--bg1), var(--bg2));
>       min-height:100vh;
>       padding: 18px;
>     }
> 
>     .wrap{
>       max-width: 760px;
>       margin: 0 auto;
>     }
> 
>     .topbar{
>       display:flex;
>       gap:14px;
>       align-items: stretch;
>       justify-content: space-between;
>       margin-bottom: 14px;
>     }
> 
>     .hero{
>       flex: 1;
>       border: 1px solid var(--border);
>       background: linear-gradient(180deg, rgba(255,255,255,.11), rgba(255,255,255,.06));
>       border-radius: var(--radius);
>       padding: 16px 18px;
>       box-shadow: var(--shadow);
>       position: relative;
>       overflow:hidden;
>     }
>     .hero:before{
>       content:"";
>       position:absolute;
>       inset:-2px;
>       background: radial-gradient(900px 160px at 20% 0%, rgba(78,161,255,.22), rgba(0,0,0,0) 60%),
>                   radial-gradient(700px 160px at 80% 0%, rgba(62,224,125,.18), rgba(0,0,0,0) 55%);
>       pointer-events:none;
>       opacity:.9;
>     }
>     .hero h1{
>       margin:0;
>       font-size: 22px;
>       letter-spacing: .6px;
>       text-transform: uppercase;
>       position: relative;
>       z-index: 1;
>     }
>     .hero p{
>       margin: 6px 0 0 0;
>       color: var(--muted);
>       font-size: 13px;
>       position: relative;
>       z-index: 1;
>     }
> 
>     .target{
>       width: 230px;
>       border: 1px solid var(--border);
>       background: linear-gradient(180deg, rgba(255,255,255,.12), rgba(255,255,255,.07));
>       border-radius: var(--radius);
>       padding: 14px 14px 12px 14px;
>       box-shadow: var(--shadow);
>     }
>     .pill{
>       display:inline-flex;
>       gap:8px;
>       align-items:center;
>       padding: 6px 10px;
>       border-radius: 999px;
>       border: 1px solid var(--border);
>       background: rgba(255,255,255,.08);
>       color: var(--muted);
>       font-size: 12px;
>       font-weight: 700;
>     }
>     .big{
>       margin-top: 10px;
>       display:flex;
>       align-items: baseline;
>       justify-content: space-between;
>       gap:10px;
>     }
>     .big .amt{
>       font-size: 30px;
>       font-weight: 900;
>       letter-spacing: .3px;
>     }
>     .big .note{
>       color: var(--muted);
>       font-size: 12px;
>       line-height: 1.2;
>       text-align:right;
>     }
> 
>     .section{
>       margin-top: 14px;
>       display:grid;
>       grid-template-columns: 1.2fr .8fr;
>       gap: 14px;
>     }
> 
>     .card{
>       border: 1px solid var(--border);
>       background: linear-gradient(180deg, rgba(255,255,255,.11), rgba(255,255,255,.06));
>       border-radius: var(--radius);
>       padding: 14px;
>       box-shadow: var(--shadow);
>     }
> 
>     .card h2{
>       margin:0 0 10px 0;
>       font-size: 13px;
>       letter-spacing: .6px;
>       text-transform: uppercase;
>       color: var(--muted);
>     }
> 
>     /* Checkpoints */
>     .grid{
>       display:grid;
>       grid-template-columns: 1fr 1fr;
>       gap: 12px;
>     }
> 
>     .checkpoint{
>       border-radius: 16px;
>       border: 1px solid var(--border);
>       background: rgba(0,0,0,.18);
>       padding: 12px;
>       position: relative;
>       overflow:hidden;
>     }
>     .checkpoint:before{
>       content:"";
>       position:absolute;
>       inset:0;
>       opacity:.40;
>       pointer-events:none;
>     }
>     .cp-blue:before{ background: radial-gradient(320px 160px at 20% 0%, rgba(78,161,255,.85), rgba(0,0,0,0) 60%); }
>     .cp-green:before{ background: radial-gradient(320px 160px at 20% 0%, rgba(62,224,125,.85), rgba(0,0,0,0) 60%); }
>     .cp-gold:before{ background: radial-gradient(320px 160px at 20% 0%, rgba(255,211,106,.9), rgba(0,0,0,0) 60%); }
>     .cp-red:before{ background: radial-gradient(320px 160px at 20% 0%, rgba(255,91,110,.9), rgba(0,0,0,0) 60%); }
> 
>     .checkpoint .row{
>       display:flex;
>       justify-content: space-between;
>       align-items:center;
>       position: relative;
>       z-index: 1;
>       gap:10px;
>     }
>     .tlabel{
>       font-weight: 800;
>       font-size: 13px;
>       letter-spacing: .2px;
>     }
>     .kpi{
>       font-size: 22px;
>       font-weight: 900;
>     }
>     .sub{
>       color: var(--muted);
>       font-size: 12px;
>       margin-top: 6px;
>       position: relative;
>       z-index: 1;
>       display:flex;
>       justify-content: space-between;
>       align-items:center;
>       gap:10px;
>     }
> 
>     .input{
>       width: 120px;
>       padding: 9px 10px;
>       border-radius: 12px;
>       border: 1px solid rgba(255,255,255,.25);
>       background: rgba(255,255,255,.10);
>       color: var(--ink);
>       font-weight: 800;
>       outline: none;
>     }
>     .input::placeholder{ color: rgba(245,247,255,.55); font-weight: 700; }
>     .input:focus{
>       border-color: rgba(255,255,255,.45);
>       background: rgba(255,255,255,.14);
>     }
> 
>     /* Deposits */
>     .bucket{
>       display:flex;
>       align-items:center;
>       justify-content: space-between;
>       padding: 10px 10px;
>       border-radius: 14px;
>       border: 1px solid rgba(255,255,255,.18);
>       background: rgba(0,0,0,.16);
>       margin-bottom: 10px;
>       gap:10px;
>     }
>     .bucket .left{
>       display:flex;
>       align-items:center;
>       gap:10px;
>       font-weight: 800;
>     }
>     .tag{
>       font-size: 11px;
>       letter-spacing: .5px;
>       text-transform: uppercase;
>       padding: 5px 9px;
>       border-radius: 999px;
>       border: 1px solid rgba(255,255,255,.20);
>       background: rgba(255,255,255,.08);
>       color: var(--muted);
>     }
>     .bucket b{
>       font-size: 18px;
>       font-weight: 900;
>     }
> 
>     .micro{
>       color: var(--muted);
>       font-size: 12px;
>       margin: 8px 0 0 0;
>       line-height: 1.35;
>     }
> 
>     /* Rules */
>     .rule{
>       border-left: 6px solid rgba(255,255,255,.35);
>       padding: 10px 12px;
>       border-radius: 14px;
>       background: rgba(0,0,0,.18);
>       border: 1px solid rgba(255,255,255,.18);
>       margin-top: 12px;
>     }
>     .rule b{ color: var(--ink); }
>     .rule span{ color: var(--muted); }
> 
>     /* Big Targets */
>     .targets{
>       display:grid;
>       gap:10px;
>     }
>     .targetRow{
>       padding: 10px 10px;
>       border-radius: 14px;
>       border: 1px solid rgba(255,255,255,.18);
>       background: rgba(0,0,0,.16);
>       display:flex;
>       justify-content: space-between;
>       align-items: center;
>       gap:12px;
>     }
>     .targetRow .name{ font-weight: 900; }
>     .targetRow .meta{ color: var(--muted); font-size: 12px; text-align:right; }
> 
>     /* Footer quick notes */
>     .notes{
>       margin-top: 14px;
>       display:flex;
>       gap: 12px;
>       flex-wrap: wrap;
>     }
>     .noteCard{
>       flex: 1;
>       min-width: 240px;
>       border: 1px dashed rgba(255,255,255,.25);
>       border-radius: 16px;
>       padding: 10px 12px;
>       background: rgba(255,255,255,.06);
>       color: var(--muted);
>       font-size: 12px;
>       line-height: 1.35;
>     }
>     .noteCard b{ color: var(--ink); }
> 
>     /* Print */
>     @media print{
>       body{
>         padding: 0;
>         background: #0b1220 !important;
>         -webkit-print-color-adjust: exact;
>         print-color-adjust: exact;
>       }
>       .wrap{
>         max-width: 100%;
>         margin: 0;
>       }
>       .card, .hero, .target{
>         box-shadow: none;
>       }
>       /* Make inputs look like part of the design on paper */
>       .input{
>         background: rgba(255,255,255,.12) !important;
>         border-color: rgba(255,255,255,.35) !important;
>       }
>     }
>   </style>
> </head>
> <body>
>   <div class="wrap">
>     <div class="topbar">
>       <div class="hero">
>         <h1>Daily $100 Glance</h1>
>         <p>Cheat sheet + daily traveler. Fill in “Actual” as you go. Print with background graphics enabled.</p>
>       </div>
> 
>       <div class="target">
>         <div class="pill">Peak-Day Target</div>
>         <div class="big">
>           <div class="amt">$125</div>
>           <div class="note">Use on Fri/Sat or any “we need extra” day.</div>
>         </div>
>       </div>
>     </div>
> 
>     <div class="section">
>       <!-- Left column: checkpoints -->
>       <div class="card">
>         <h2>Checkpoints</h2>
>         <div class="grid">
>           <div class="checkpoint cp-blue">
>             <div class="row">
>               <div class="tlabel">6:00 AM</div>
>               <div class="kpi">$25</div>
>             </div>
>             <div class="sub">
>               <div>25% • Start strong</div>
>               <input
>                 class="input"
>                 type="text"
>                 inputmode="decimal"
>                 placeholder="Actual $"
>                 title="زای: دا د سهار پرمختګ دی (Actual پیسې دلته ولیکه)"
>               />
>             </div>
>           </div>
> 
>           <div class="checkpoint cp-green">
>             <div class="row">
>               <div class="tlabel">12:00 PM</div>
>               <div class="kpi">$50</div>
>             </div>
>             <div class="sub">
>               <div>50% • On track</div>
>               <input
>                 class="input"
>                 type="text"
>                 inputmode="decimal"
>                 placeholder="Actual $"
>                 title="زای: دا د غرمی پرمختګ دی (Actual پیسې دلته ولیکه)"
>               />
>             </div>
>           </div>
> 
>           <div class="checkpoint cp-gold">
>             <div class="row">
>               <div class="tlabel">6:00 PM</div>
>               <div class="kpi">$75</div>
>             </div>
>             <div class="sub">
>               <div>75% • Push hour</div>
>               <input
>                 class="input"
>                 type="text"
>                 inputmode="decimal"
>                 placeholder="Actual $"
>                 title="زای: دا د ماښام پرمختګ دی (Actual پیسې دلته ولیکه)"
>               />
>             </div>
>           </div>
> 
>           <div class="checkpoint cp-red">
>             <div class="row">
>               <div class="tlabel">Midnight</div>
>               <div class="kpi">$100</div>
>             </div>
>             <div class="sub">
>               <div>Done • Shut it down</div>
>               <input
>                 class="input"
>                 type="text"
>                 inputmode="decimal"
>                 placeholder="Actual $"
>                 title="زای: دا د ورځې وروستۍ نتیجه ده (Final Actual دلته ولیکه)"
>               />
>             </div>
>           </div>
>         </div>
> 
>         <div class="rule">
>           <b>The Clock Rule:</b> <span>If behind checkpoint, keep working. If ahead, you may rest.</span>
>         </div>
>         <div class="rule" style="margin-top:10px;">
>           <b>Stop Rule:</b> <span>When target is met, stop working. No “one more run.”</span>
>         </div>
> 
>         <p class="micro" style="margin-top:10px;">
>           Legend: <b style="color:var(--blue)">Blue</b>=Start • <b style="color:var(--green)">Green</b>=On Track •
>           <b style="color:var(--gold)">Gold</b>=Push • <b style="color:var(--red)">Red</b>=Finish
>         </p>
>       </div>
> 
>       <!-- Right column: deposits + targets -->
>       <div class="card">
>         <h2>Daily Deposits</h2>
> 
>         <div class="bucket">
>           <div class="left">
>             <span class="tag">Rent</span>
>             <span>🏠 Rent</span>
>           </div>
>           <b>$43</b>
>         </div>
> 
>         <div class="bucket">
>           <div class="left">
>             <span class="tag">Home</span>
>             <span>🏡 Home</span>
>           </div>
>           <b>$33</b>
>         </div>
> 
>         <div class="bucket">
>           <div class="left">
>             <span class="tag">Plates</span>
>             <span>🍽️ Plates</span>
>           </div>
>           <b>$23</b>
>         </div>
> 
>         <div class="bucket" style="opacity:.95;">
>           <div class="left">
>             <span class="tag">Extra</span>
>             <span>🧯 Emergency</span>
>           </div>
>           <input
>             class="input"
>             style="width: 110px;"
>             type="text"
>             inputmode="decimal"
>             placeholder="Extra $"
>             title="زای: که اضافي پیسې وي، دلته ولیکه (Emergency Savings)"
>           />
>         </div>
> 
>         <p class="micro">
>           Extra cash goes to <b>Emergency Savings</b>. Don’t negotiate with this. It’s what keeps you from spiraling.
>         </p>
> 
>         <h2 style="margin-top:14px;">Big Targets</h2>
>         <div class="targets">
>           <div class="targetRow">
>             <div class="name">🍽️ Plates</div>
>             <div class="meta">$700 • ~30 days</div>
>           </div>
>           <div class="targetRow">
>             <div class="name">🏡 Home</div>
>             <div class="meta">$2,600 • ~80 days</div>
>           </div>
>         </div>
> 
>         <div class="rule" style="margin-top:12px;">
>           <b>One-liner:</b> <span>Make the money, split the buckets, stop when done.</span>
>         </div>
>       </div>
>     </div>
> 
>     <div class="notes">
>       <div class="noteCard">
>         <b>Print tip:</b> In Chrome print dialog, turn on <b>“Background graphics”</b> so the colors don’t disappear.
>       </div>
>       <div class="noteCard">
>         <b>Carry version:</b> Print at 90–95% scale. It stays legible but fits better in a folder/binder.
>       </div>
>     </div>
>   </div>
> </body>
> </html>
> ```
> 
> If you want it to be even more “traveler”:
> - I can add a **checkbox row** (Worked / Rested / Deposit done)
> - Add a **tiny “today’s date” fill field**
> - Add a **QR code** that opens your dashboard/notes (optional)
> 
> Say the word and tell me if you want **letter** or **half-sheet** print layout.

### User
> how can i track it and have something push a reminder to me to enter how much i have so far at each point ect.

### Assistant
> You track it by separating **(A) reminders** from **(B) a single place to log the number**. Don’t try to do both inside your brain.
> 
> ### What I can do right now (already set up)
> I set you up with **daily reminders** to log your earnings at:
> - **6:00 AM** (target $25)
> - **12:00 PM** (target $50)
> - **6:00 PM** (target $75)
> - **12:00 AM** (target $100)
> 
> So you’ll get a prompt from me at each checkpoint.
> 
> ### Where to *log* the number (pick ONE)
> You’ve got three good options. Anything else is overkill.
> 
> #### Option 1 (fastest): Notes app (1 running note)
> - Create one Apple Note titled: **“Daily $100 Glance — Log”**
> - Each reminder: add a line like  
>   `Jan 23 — 6am: $18 | 12pm: $61 | 6pm: $74 | 12am: $112`
> - This is the lowest-friction, highest compliance path.
> 
> #### Option 2 (best long-term): Google Sheet (4 fields)
> - Sheet columns: Date, 6am, 12pm, 6pm, midnight
> - You can later graph it, total it, and audit it.
> 
> #### Option 3 (cleanest UX): iPhone Shortcut “Log Checkpoint”
> - One button that asks: “Which checkpoint?” + “How much so far?”  
> - Then it appends to your Note or Google Sheet.
> 
> If you tell me **Notes or Google Sheet**, I’ll give you the exact iOS Shortcut setup in 6–10 steps (no code, no nonsense).
> 
> ### One critical print setting (so your HTML stays pretty)
> If you print the cheat sheet from Chrome/Safari: enable **Background Graphics** or your colors will wash out.
> 
> If you want this to be *automatic*, the best combo is:
> **ChatGPT reminders + iOS Shortcut that opens the log form immediately.**

### User
> what if i just want to do this in a spreadsheet or something like notion, but screw that i just need a slick cheat sheet to put into my window or visort

### Assistant
> Good — that tells me exactly what to do.
> 
> You **do NOT** need Notion, spreadsheets, automations, or dashboards for this phase. That’s procrastination dressed as “systems.” You need **one glanceable, idiot-proof visual** that lives in your line of sight and tells you **what time it is, what number you should see, and whether to stop or keep going**.
> 
> So here’s the correct move.
> 
> ---
> 
> ## The Right Answer (no overengineering)
> 
> ### You want a **VISOR / WINDOW CHEAT SHEET**
> Not interactive.  
> Not track-everything.  
> Not “loggable.”  
> 
> **A laminated, color, high-contrast target card.**
> 
> You track progress **mentally + by your app** (Lyft/Uber/etc).  
> The sheet exists to answer ONE question:
> 
> > “Am I on pace or not?”
> 
> That’s it.
> 
> ---
> 
> ## Final Design Recommendation (what to print)
> 
> ### 1. Two versions. Period.
> - **Front:** Pace checkpoints (the money clock)
> - **Back:** Deposit buckets + rules
> 
> No scrolling. No writing. No thinking.
> 
> ---
> 
> ### FRONT — “THE MONEY CLOCK”
> Big, stupid-clear, readable from 2–3 feet away.
> 
> ```
> DAILY $100 TARGET
> 
> 6:00 AM    $25   (START)
> 12:00 PM   $50   (ON TRACK)
> 6:00 PM    $75   (PUSH)
> MIDNIGHT   $100  (STOP)
> ```
> 
> Color code only:
> - Blue → Green → Gold → Red
> 
> Under it, one line only:
> > IF BEHIND → KEEP WORKING  
> > IF AHEAD → YOU MAY REST
> 
> That’s the whole front.
> 
> ---
> 
> ### BACK — “AUTO-SPLIT RULE”
> No math. No debate.
> 
> ```
> EVERY $100 DAY
> 
> 🏠 RENT     $43
> 🏡 HOME     $33
> 🍽️ PLATES  $23
> 
> EXTRA → EMERGENCY
> ```
> 
> Bottom line:
> > DO NOT NEGOTIATE THESE NUMBERS
> 
> ---
> 
> ## How to physically deploy it (this matters)
> 
> ### Best placement (in order)
> 1. **Driver-side visor** (ideal)
> 2. **Dashboard corner**
> 3. **Passenger window (low)**
> 
> Rules:
> - Matte paper (no glare)
> - Dark background, light text
> - 90–95% print scale
> - Laminate if possible
> 
> This becomes a **behavioral anchor**, not a record.
> 
> ---
> 
> ## Why you *don’t* want a spreadsheet or Notion here
> Truth mode:
> 
> - You won’t open it while driving.
> - It adds cognitive friction.
> - It shifts you from **action → analysis**.
> - You already have numbers in your driving app.
> 
> This is **pace control**, not accounting.
> 
> Accounting happens later.
> 
> ---
> 
> ## What I can do next (pick one)
> 1. Generate a **print-perfect visor version** (letter + half-sheet)
> 2. Make a **black-background, ultra-high-contrast** version for night driving
> 3. Add **Pashto micro-text** under each rule for Zai
> 4. Create a **2-page front/back PDF** ready for laminate
> 
> Say the number.  
> We lock it and stop touching it.

### User
> in html long landscapt like a strip

### Assistant
> Here. This is a **long landscape “strip” HTML** designed to print as a **banner** you can cut and stick in the window/visor. It’s full-color, high-contrast, and built to be readable from arm’s length.
> 
> Copy into `daily_strip.html`, open in Chrome, Print → **More settings → Background graphics ON**.
> 
> ```html
> <!DOCTYPE html>
> <html lang="en">
> <head>
>   <meta charset="UTF-8" />
>   <meta name="viewport" content="width=device-width,initial-scale=1" />
>   <title>Daily $100 Glance — Strip</title>
>   <style>
>     :root{
>       --bg:#0b1220;
>       --panel: rgba(255,255,255,.10);
>       --panel2: rgba(255,255,255,.06);
>       --ink:#f5f7ff;
>       --muted: rgba(245,247,255,.72);
>       --border: rgba(255,255,255,.18);
> 
>       --blue:#4ea1ff;
>       --green:#3ee07d;
>       --gold:#ffd36a;
>       --red:#ff5b6e;
>     }
> 
>     *{ box-sizing:border-box; }
>     body{
>       margin:0;
>       background: radial-gradient(1100px 380px at 15% 20%, rgba(78,161,255,.22), rgba(0,0,0,0) 60%),
>                   radial-gradient(900px 340px at 80% 30%, rgba(62,224,125,.18), rgba(0,0,0,0) 55%),
>                   linear-gradient(160deg, #070c16, var(--bg));
>       color:var(--ink);
>       font-family: -apple-system, system-ui, Segoe UI, Roboto, Arial, sans-serif;
>       -webkit-print-color-adjust: exact;
>       print-color-adjust: exact;
>       padding: 16px;
>     }
> 
>     /* ===== STRIP SIZE CONTROL =====
>        Pick ONE size. Default below is 11" x 3" (perfect “strip”).
>        If you want longer, change width/height in @page and .strip.
>     */
>     @page{
>       size: 11in 3in;
>       margin: 0.15in;
>     }
> 
>     .strip{
>       width: 11in;
>       height: 3in;
>       border: 1px solid var(--border);
>       border-radius: 18px;
>       background: linear-gradient(180deg, rgba(255,255,255,.10), rgba(255,255,255,.05));
>       overflow:hidden;
>       display:flex;
>       flex-direction: column;
>       justify-content: space-between;
>       padding: 14px 14px 12px 14px;
>     }
> 
>     .top{
>       display:flex;
>       justify-content: space-between;
>       align-items:flex-start;
>       gap: 14px;
>     }
> 
>     .title{
>       display:flex;
>       flex-direction: column;
>       gap: 4px;
>       min-width: 220px;
>     }
>     .title h1{
>       margin:0;
>       font-size: 18px;
>       letter-spacing: .8px;
>       text-transform: uppercase;
>       line-height: 1.05;
>     }
>     .title .sub{
>       font-size: 12px;
>       color: var(--muted);
>       line-height: 1.2;
>     }
> 
>     .targetBox{
>       display:flex;
>       gap: 10px;
>       align-items: center;
>       border: 1px solid var(--border);
>       background: rgba(255,255,255,.07);
>       padding: 10px 12px;
>       border-radius: 16px;
>       min-width: 250px;
>       justify-content: space-between;
>     }
>     .pill{
>       font-size: 11px;
>       letter-spacing: .6px;
>       text-transform: uppercase;
>       color: var(--muted);
>       border: 1px solid var(--border);
>       background: rgba(255,255,255,.06);
>       padding: 4px 8px;
>       border-radius: 999px;
>       font-weight: 800;
>       white-space: nowrap;
>     }
>     .targetAmt{
>       font-size: 24px;
>       font-weight: 950;
>       letter-spacing: .3px;
>       white-space: nowrap;
>     }
>     .targetNote{
>       font-size: 11px;
>       color: var(--muted);
>       text-align: right;
>       line-height: 1.2;
>       max-width: 130px;
>     }
> 
>     .mid{
>       display:grid;
>       grid-template-columns: 1.35fr .65fr;
>       gap: 12px;
>       align-items: stretch;
>     }
> 
>     .clock{
>       display:grid;
>       grid-template-columns: repeat(4, 1fr);
>       gap: 10px;
>     }
> 
>     .cp{
>       border: 1px solid var(--border);
>       border-radius: 16px;
>       background: rgba(0,0,0,.18);
>       padding: 10px 10px 8px 10px;
>       position: relative;
>       overflow:hidden;
>       display:flex;
>       flex-direction: column;
>       justify-content: space-between;
>       min-height: 92px;
>     }
>     .cp:before{
>       content:"";
>       position:absolute; inset:0;
>       opacity:.45;
>       pointer-events:none;
>     }
>     .cp.blue:before{ background: radial-gradient(300px 140px at 20% 0%, rgba(78,161,255,.9), rgba(0,0,0,0) 60%); }
>     .cp.green:before{ background: radial-gradient(300px 140px at 20% 0%, rgba(62,224,125,.9), rgba(0,0,0,0) 60%); }
>     .cp.gold:before{ background: radial-gradient(300px 140px at 20% 0%, rgba(255,211,106,.95), rgba(0,0,0,0) 60%); }
>     .cp.red:before{ background: radial-gradient(300px 140px at 20% 0%, rgba(255,91,110,.95), rgba(0,0,0,0) 60%); }
> 
>     .cp .row{
>       display:flex;
>       justify-content: space-between;
>       align-items: baseline;
>       gap:10px;
>       position: relative;
>       z-index: 1;
>     }
>     .time{
>       font-size: 12px;
>       font-weight: 900;
>       letter-spacing: .4px;
>       text-transform: uppercase;
>       color: rgba(245,247,255,.92);
>       white-space: nowrap;
>     }
>     .goal{
>       font-size: 20px;
>       font-weight: 950;
>       white-space: nowrap;
>     }
>     .hint{
>       position: relative;
>       z-index: 1;
>       margin-top: 6px;
>       display:flex;
>       justify-content: space-between;
>       align-items: center;
>       gap:10px;
>       color: var(--muted);
>       font-size: 11px;
>       line-height: 1.15;
>     }
> 
>     .buckets{
>       border: 1px solid var(--border);
>       border-radius: 16px;
>       background: rgba(0,0,0,.18);
>       padding: 10px;
>       display:flex;
>       flex-direction: column;
>       justify-content: space-between;
>       gap: 8px;
>       min-height: 92px;
>     }
>     .bTop{
>       display:flex;
>       justify-content: space-between;
>       align-items:center;
>       gap:10px;
>     }
>     .bTop .label{
>       font-size: 11px;
>       letter-spacing: .6px;
>       text-transform: uppercase;
>       color: var(--muted);
>       font-weight: 900;
>     }
>     .bucketRow{
>       display:flex;
>       justify-content: space-between;
>       align-items:center;
>       gap:10px;
>       padding: 7px 8px;
>       border-radius: 12px;
>       border: 1px solid rgba(255,255,255,.16);
>       background: rgba(255,255,255,.05);
>       font-weight: 850;
>     }
>     .bucketRow b{
>       font-size: 14px;
>       font-weight: 950;
>       white-space: nowrap;
>     }
> 
>     .bottom{
>       display:flex;
>       justify-content: space-between;
>       align-items: center;
>       gap: 10px;
>       border-top: 1px solid rgba(255,255,255,.14);
>       padding-top: 10px;
>     }
>     .rule{
>       flex: 1;
>       border-left: 6px solid rgba(255,255,255,.30);
>       padding: 6px 10px;
>       border-radius: 12px;
>       background: rgba(0,0,0,.16);
>       border: 1px solid rgba(255,255,255,.14);
>       font-size: 12px;
>       line-height: 1.2;
>     }
>     .rule b{ font-weight: 950; }
>     .rule span{ color: var(--muted); }
> 
>     .legend{
>       display:flex;
>       gap: 10px;
>       align-items:center;
>       color: var(--muted);
>       font-size: 11px;
>       white-space: nowrap;
>     }
>     .dot{
>       width: 10px; height: 10px; border-radius: 999px; display:inline-block;
>       border: 1px solid rgba(255,255,255,.25);
>       vertical-align: middle;
>       margin-right: 5px;
>     }
> 
>     @media print{
>       body{ padding:0; background: var(--bg) !important; }
>       .strip{ box-shadow:none; }
>     }
>   </style>
> </head>
> <body>
>   <div class="strip" role="document" aria-label="Daily $100 Glance Strip">
> 
>     <div class="top">
>       <div class="title">
>         <h1>Daily $100 Glance</h1>
>         <div class="sub">Window/visor strip • Use it to check pace, not to “track everything.”</div>
>       </div>
> 
>       <div class="targetBox">
>         <div>
>           <div class="pill">Peak-Day Target</div>
>           <div class="targetAmt">$125</div>
>         </div>
>         <div class="targetNote">Use Fri/Sat or “we need extra” days.</div>
>       </div>
>     </div>
> 
>     <div class="mid">
>       <div class="clock">
>         <div class="cp blue">
>           <div class="row">
>             <div class="time">6:00 AM</div>
>             <div class="goal" style="color:var(--blue)">$25</div>
>           </div>
>           <div class="hint">
>             <div>25% • Start strong</div>
>             <div title="زای: که شاته یې، کار ته دوام ورکړه. که مخکې یې، لږ استراحت وکړه.">PACE</div>
>           </div>
>         </div>
> 
>         <div class="cp green">
>           <div class="row">
>             <div class="time">12:00 PM</div>
>             <div class="goal" style="color:var(--green)">$50</div>
>           </div>
>           <div class="hint">
>             <div>50% • On track</div>
>             <div title="زای: دا د غرمی هدف دی — تر دې وخته باید لږ تر لږه $50 وي.">CHECK</div>
>           </div>
>         </div>
> 
>         <div class="cp gold">
>           <div class="row">
>             <div class="time">6:00 PM</div>
>             <div class="goal" style="color:var(--gold)">$75</div>
>           </div>
>           <div class="hint">
>             <div>75% • Push hour</div>
>             <div title="زای: دا د ماښام هدف دی — که کم وي، فشار/زیات کار.">PUSH</div>
>           </div>
>         </div>
> 
>         <div class="cp red">
>           <div class="row">
>             <div class="time">MIDNIGHT</div>
>             <div class="goal" style="color:var(--red)">$100</div>
>           </div>
>           <div class="hint">
>             <div>Done • Stop</div>
>             <div title="زای: که هدف پوره شو، نور مه کوه. بس!">STOP</div>
>           </div>
>         </div>
>       </div>
> 
>       <div class="buckets">
>         <div class="bTop">
>           <div class="label">Daily Deposits</div>
>           <div class="pill" title="زای: دا درې برخې ثابتې دي — بحث پکې نشته.">NO NEGOTIATION</div>
>         </div>
> 
>         <div class="bucketRow"><span>🏠 Rent</span><b>$43</b></div>
>         <div class="bucketRow"><span>🏡 Home</span><b>$33</b></div>
>         <div class="bucketRow"><span>🍽️ Plates</span><b>$23</b></div>
> 
>         <div style="font-size:11px;color:var(--muted);padding:0 4px;">
>           Extra → <b style="color:var(--ink);">Emergency</b>
>           <span title="زای: هر اضافي پیسې بیړني سپما ته ځي.">(Pashto tip)</span>
>         </div>
>       </div>
>     </div>
> 
>     <div class="bottom">
>       <div class="rule">
>         <b>Clock Rule:</b> <span>If behind checkpoint → keep working. If ahead → you may rest.</span>
>       </div>
>       <div class="rule">
>         <b>Stop Rule:</b> <span>When target is met → stop. No “one more run.”</span>
>       </div>
> 
>       <div class="legend">
>         <span><i class="dot" style="background:var(--blue)"></i>Start</span>
>         <span><i class="dot" style="background:var(--green)"></i>Track</span>
>         <span><i class="dot" style="background:var(--gold)"></i>Push</span>
>         <span><i class="dot" style="background:var(--red)"></i>Finish</span>
>       </div>
>     </div>
> 
>   </div>
> </body>
> </html>
> ```
> 
> ### Print settings (so it actually looks good)
> - Chrome → Print
> - **More settings → Background graphics: ON**
> - Scale: **100%** (or 95% if your printer clips edges)
> - Paper: **Letter** (it will print as an 11" x 3" strip on the page; you cut it)
> 
> ### Want it longer than 11 inches?
> Tell me the exact dimensions you want (e.g., **“14in x 3in”** or **“10in x 2.5in”**) and I’ll adjust the `@page` + `.strip` so it prints perfectly.

### Assistant
> 12:00 PM checkpoint: enter your current total earned so far. Target by now is **$50**.

### Assistant
> 6:00 PM checkpoint: enter your current total earned so far. Target by now is **$75**.

### Assistant
> Midnight checkpoint: enter your final total earned so far. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working until you do.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target by now is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target by now is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target by now is **$75**.

### Assistant
> Midnight checkpoint: enter your final total earned so far. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working until you do.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target by now is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target by now is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target by now is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target by now is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’re at or above it, stop. If you’re under, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for the Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight check-in: log your final Daily $100 Glance total. Goal is **$100**. If you’re at or above it, shut it down. If not, keep pushing.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight check-in: log your final Daily $100 Glance total. Goal is **$100**. If you’ve hit it, stop. If you’re short, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight check-in: log your final Daily $100 Glance total. Goal is **$100**. If you’ve hit it, stop. If you’re short, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight check-in: enter your final total for Daily $100 Glance. Goal is **$100**. If you’ve hit it, stop. If you’re short, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight check-in: enter your final total for Daily $100 Glance. Goal is **$100**. If you’ve hit it, stop. If you’re short, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight check-in: enter your final total for Daily $100 Glance. Goal is **$100**. If you’ve hit it, stop. If you’re short, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6 PM check-in: log your current total. You’re aiming for $75.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is $100. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6 PM check-in: log your current total. You’re aiming for $75.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is $100. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12 PM check-in: log your current earnings. Goal right now is **$50**.

### Assistant
> 6:00 PM checkpoint: log your current total. Goal is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> There was a problem with your scheduled task.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.

### Assistant
> 6:00 PM checkpoint: enter how much you’ve made so far. Target is **$75**.

### Assistant
> Midnight checkpoint: enter your final total for Daily $100 Glance. Target is **$100**. If you’ve hit it, stop. If you’re behind, keep working.

### Assistant
> 6:00 AM checkpoint: enter how much you’ve made so far. Target is **$25**.

### Assistant
> 12:00 PM checkpoint: enter how much you’ve made so far. Target is **$50**.
