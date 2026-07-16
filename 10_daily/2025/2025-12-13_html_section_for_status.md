---
layout: page
title: "Html section for status"
slug: "html_section_for_status"
created_at: "2025-12-13 10:31:18"
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
source_file: "Chat-Export-28513-2026/conversations-002.json"
template_key: master-template
date: 2025-12-13
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "693d94b1-6eb0-8329-a3dc-2e847430bff3"
canonical_ref: ""
---

# Html section for status

## Overview
- **Date**: 2025-12-13 10:31:18
- **Conversation ID**: `693d94b1-6eb0-8329-a3dc-2e847430bff3`
- **Source**: `Chat-Export-28513-2026/conversations-002.json`

## Chat History

### User
> Give me an html section to add to my QiAlly.me site at the top for current status

### Assistant
> Below is a **clean, top-of-page HTML section** you can drop directly into **QiAlly.me**.  
> It is neutral, professional, and flexible—no drama, no oversharing, no promises you can’t keep.  
> You can update **one line** to change status without touching structure.
> 
> ---
> 
> ### ✅ **Current Status Banner (Top of Page)**
> 
> ```html
> <section id="current-status" style="
>   width: 100%;
>   padding: 1.25rem 1.5rem;
>   margin-bottom: 2rem;
>   border-radius: 14px;
>   background: rgba(255, 255, 255, 0.08);
>   backdrop-filter: blur(10px);
>   -webkit-backdrop-filter: blur(10px);
>   border: 1px solid rgba(255, 255, 255, 0.15);
> ">
> 
>   <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 1rem;">
>     
>     <div style="
>       font-weight: 600;
>       letter-spacing: 0.08em;
>       font-size: 0.75rem;
>       opacity: 0.75;
>       text-transform: uppercase;
>       white-space: nowrap;
>     ">
>       Current Status
>     </div>
> 
>     <div style="
>       flex: 1;
>       font-size: 0.95rem;
>       line-height: 1.4;
>     ">
>       Actively managing client work and infrastructure updates. Limited availability for new requests.
>     </div>
> 
>   </div>
> </section>
> ```
> 
> ---
> 
> ### 🔧 **How to Use This Efficiently**
> - **Change only this sentence** to update status:
>   ```html
>   Actively managing client work and infrastructure updates. Limited availability for new requests.
>   ```
> - Works **without external CSS**
> - Glassmorphism-safe
> - Mobile-friendly
> - No icons (clean + serious)
> - Doesn’t beg, explain, or over-justify
> 
> ---
> 
> ### Optional Variations (copy/paste replacements)
> 
> **High availability**
> ```text
> Accepting new projects and consultations. Response times are currently normal.
> ```
> 
> **Heads-down / crisis mode**
> ```text
> Focused on critical work. Response times may be delayed.
> ```
> 
> **Paused intake**
> ```text
> Temporarily paused on new engagements while completing existing commitments.
> ```
> 
> ---
> 
> ### Straight talk
> This does what you need:
> - Sets expectations
> - Protects your energy
> - Signals professionalism
> - Avoids personal disclosure
> - Avoids guilt language
> 
> If you want:
> - a **version with timestamps**
> - a **status auto-pulled from a JSON file**
> - or a **client-only expanded status**
> 
> say the word and I’ll tighten it.

### User
> Can y ok put different options and severity level on them and I can just comment out the inactive ones so only the current one shows without me having to think and type the updates

### Assistant
> Yes. Here’s a **drop-in “status banner” section** with **severity levels** and **pre-written options**. You’ll just **uncomment ONE block** and comment the others. No typing, no thinking.
> 
> ```html
> <!-- =========================
>      QiAlly | Current Status
>      Usage: Leave ONLY ONE status <div class="status-card ..."> uncommented.
>      ========================= -->
> 
> <section id="current-status" style="
>   width: 100%;
>   padding: 1.25rem 1.5rem;
>   margin-bottom: 2rem;
>   border-radius: 14px;
>   background: rgba(255, 255, 255, 0.08);
>   backdrop-filter: blur(10px);
>   -webkit-backdrop-filter: blur(10px);
>   border: 1px solid rgba(255, 255, 255, 0.15);
> ">
> 
>   <div style="
>     display: flex;
>     flex-wrap: wrap;
>     align-items: center;
>     gap: 1rem;
>   ">
>     <div style="
>       font-weight: 600;
>       letter-spacing: 0.08em;
>       font-size: 0.75rem;
>       opacity: 0.75;
>       text-transform: uppercase;
>       white-space: nowrap;
>     ">
>       Current Status
>     </div>
> 
>     <!-- Base styles applied per status below -->
>   </div>
> 
>   <!-- ============
>        STATUS OPTIONS
>        Comment out all but ONE.
>        ============ -->
> 
>   <!-- SEVERITY 0 — NORMAL (Green-ish) -->
>   <!--
>   <div class="status-card" style="
>     margin-top: 0.9rem;
>     padding: 0.9rem 1rem;
>     border-radius: 12px;
>     border: 1px solid rgba(70, 255, 120, 0.25);
>     background: rgba(70, 255, 120, 0.08);
>   ">
>     <div style="font-weight: 600; font-size: 0.95rem;">Normal Operations</div>
>     <div style="opacity: 0.9; margin-top: 0.25rem;">
>       Accepting new work. Standard response times.
>     </div>
>   </div>
>   -->
> 
>   <!-- SEVERITY 1 — LIMITED (Blue) -->
>   <!--
>   <div class="status-card" style="
>     margin-top: 0.9rem;
>     padding: 0.9rem 1rem;
>     border-radius: 12px;
>     border: 1px solid rgba(90, 180, 255, 0.28);
>     background: rgba(90, 180, 255, 0.10);
>   ">
>     <div style="font-weight: 600; font-size: 0.95rem;">Limited Availability</div>
>     <div style="opacity: 0.9; margin-top: 0.25rem;">
>       Active client delivery + infrastructure work. New requests may be scheduled.
>     </div>
>   </div>
>   -->
> 
>   <!-- SEVERITY 2 — DELAYED (Amber) -->
>   <!--
>   <div class="status-card" style="
>     margin-top: 0.9rem;
>     padding: 0.9rem 1rem;
>     border-radius: 12px;
>     border: 1px solid rgba(255, 190, 80, 0.30);
>     background: rgba(255, 190, 80, 0.10);
>   ">
>     <div style="font-weight: 600; font-size: 0.95rem;">Delayed Responses</div>
>     <div style="opacity: 0.9; margin-top: 0.25rem;">
>       Heads-down on deadlines. Replies may take longer than usual.
>     </div>
>   </div>
>   -->
> 
>   <!-- SEVERITY 3 — PAUSED INTAKE (Orange/Red) -->
>   <!--
>   <div class="status-card" style="
>     margin-top: 0.9rem;
>     padding: 0.9rem 1rem;
>     border-radius: 12px;
>     border: 1px solid rgba(255, 120, 80, 0.30);
>     background: rgba(255, 120, 80, 0.10);
>   ">
>     <div style="font-weight: 600; font-size: 0.95rem;">Paused New Intake</div>
>     <div style="opacity: 0.9; margin-top: 0.25rem;">
>       Temporarily not taking new work while completing current commitments.
>     </div>
>   </div>
>   -->
> 
>   <!-- SEVERITY 4 — CRITICAL / OUT (Red) -->
>   <!--
>   <div class="status-card" style="
>     margin-top: 0.9rem;
>     padding: 0.9rem 1rem;
>     border-radius: 12px;
>     border: 1px solid rgba(255, 80, 80, 0.32);
>     background: rgba(255, 80, 80, 0.10);
>   ">
>     <div style="font-weight: 600; font-size: 0.95rem;">Out of Office / Emergency Mode</div>
>     <div style="opacity: 0.9; margin-top: 0.25rem;">
>       Minimal connectivity. Only urgent items will be handled until further notice.
>     </div>
>   </div>
>   -->
> 
> </section>
> ```
> 
> If you tell me where this lives (Astro component, React component, plain HTML page), I can convert this into a **single reusable component** with a one-line switch like `data-status="2"` so you never have to comment/uncomment again.

### User
> I mean situational status like hotel stay secured paid shelter good until 10am, food source unknown state of mind poor but functioning. Or something like a few or 10 related options as thing change I just comment out the rest showing the one I want shown

### Assistant
> Got it. You want a **personal ops status** block: concrete, situational, and pre-written so you can **flip one on** by uncommenting it. Here’s a clean version that still looks professional on QiAlly.me (and doesn’t read like a diary unless someone goes looking).
> 
> Paste this at the top of the site; **uncomment ONE “STATUS CARD”** at a time.
> 
> ```html
> <!-- =========================
>      QiAlly | Situational Status (Ops Snapshot)
>      Use: UNCOMMENT ONE status-card block. Leave the rest commented out.
>      ========================= -->
> 
> <section id="ops-status" style="
>   width: 100%;
>   padding: 1.25rem 1.5rem;
>   margin-bottom: 2rem;
>   border-radius: 14px;
>   background: rgba(255, 255, 255, 0.08);
>   backdrop-filter: blur(10px);
>   -webkit-backdrop-filter: blur(10px);
>   border: 1px solid rgba(255, 255, 255, 0.15);
> ">
> 
>   <div style="display:flex; flex-wrap:wrap; align-items:center; gap:0.75rem;">
>     <div style="
>       font-weight: 700;
>       letter-spacing: 0.08em;
>       font-size: 0.75rem;
>       opacity: 0.75;
>       text-transform: uppercase;
>       white-space: nowrap;">
>       Ops Status
>     </div>
> 
>     <div style="opacity:0.75; font-size:0.85rem;">
>       Real-time snapshot. Updated as needed.
>     </div>
>   </div>
> 
>   <!-- =========================
>        STATUS CARDS (Pick ONE)
>        ========================= -->
> 
>   <!-- STATUS 01 — STABLE WINDOW (Hotel secured until morning) -->
>   <!--
>   <div class="status-card" style="
>     margin-top: 0.9rem;
>     padding: 1rem;
>     border-radius: 12px;
>     border: 1px solid rgba(90, 180, 255, 0.28);
>     background: rgba(90, 180, 255, 0.10);
>   ">
>     <div style="font-weight:700; font-size:1rem;">Stable Window</div>
>     <div style="margin-top:0.5rem; display:grid; gap:0.35rem; font-size:0.92rem; opacity:0.92;">
>       <div><strong>Shelter:</strong> Hotel secured / paid — good until 10:00 AM</div>
>       <div><strong>Food:</strong> Unknown / in progress</div>
>       <div><strong>Operating state:</strong> Poor but functioning</div>
>       <div><strong>Priority:</strong> Secure next 24 hours + stabilize cash flow</div>
>     </div>
>   </div>
>   -->
> 
>   <!-- STATUS 02 — SHELTER UNSECURED (Time-sensitive) -->
>   <!--
>   <div class="status-card" style="
>     margin-top: 0.9rem;
>     padding: 1rem;
>     border-radius: 12px;
>     border: 1px solid rgba(255, 190, 80, 0.30);
>     background: rgba(255, 190, 80, 0.10);
>   ">
>     <div style="font-weight:700; font-size:1rem;">Shelter Unsecured</div>
>     <div style="margin-top:0.5rem; display:grid; gap:0.35rem; font-size:0.92rem; opacity:0.92;">
>       <div><strong>Shelter:</strong> Not confirmed for tonight</div>
>       <div><strong>Food:</strong> Limited / unknown</div>
>       <div><strong>Operating state:</strong> Functional, under strain</div>
>       <div><strong>Priority:</strong> Lock shelter plan + recharge + rest</div>
>     </div>
>   </div>
>   -->
> 
>   <!-- STATUS 03 — SHELTER SECURED (Non-hotel / couch / safe place) -->
>   <!--
>   <div class="status-card" style="
>     margin-top: 0.9rem;
>     padding: 1rem;
>     border-radius: 12px;
>     border: 1px solid rgba(70, 255, 120, 0.25);
>     background: rgba(70, 255, 120, 0.08);
>   ">
>     <div style="font-weight:700; font-size:1rem;">Shelter Secured</div>
>     <div style="margin-top:0.5rem; display:grid; gap:0.35rem; font-size:0.92rem; opacity:0.92;">
>       <div><strong>Shelter:</strong> Safe place confirmed (not hotel)</div>
>       <div><strong>Food:</strong> Basic coverage</div>
>       <div><strong>Operating state:</strong> Recovering</div>
>       <div><strong>Priority:</strong> Sleep + execute next steps calmly</div>
>     </div>
>   </div>
>   -->
> 
>   <!-- STATUS 04 — RECOVERY MODE (Rest + low comms) -->
>   <!--
>   <div class="status-card" style="
>     margin-top: 0.9rem;
>     padding: 1rem;
>     border-radius: 12px;
>     border: 1px solid rgba(160, 160, 255, 0.22);
>     background: rgba(160, 160, 255, 0.08);
>   ">
>     <div style="font-weight:700; font-size:1rem;">Recovery Mode</div>
>     <div style="margin-top:0.5rem; display:grid; gap:0.35rem; font-size:0.92rem; opacity:0.92;">
>       <div><strong>Shelter:</strong> Stable</div>
>       <div><strong>Food:</strong> Stable</div>
>       <div><strong>Operating state:</strong> Low battery — resting</div>
>       <div><strong>Comms:</strong> Minimal / delayed responses</div>
>     </div>
>   </div>
>   -->
> 
>   <!-- STATUS 05 — FOCUS BLOCK (Working window; interruptions costly) -->
>   <!--
>   <div class="status-card" style="
>     margin-top: 0.9rem;
>     padding: 1rem;
>     border-radius: 12px;
>     border: 1px solid rgba(90, 180, 255, 0.28);
>     background: rgba(90, 180, 255, 0.10);
>   ">
>     <div style="font-weight:700; font-size:1rem;">Focus Block</div>
>     <div style="margin-top:0.5rem; display:grid; gap:0.35rem; font-size:0.92rem; opacity:0.92;">
>       <div><strong>Status:</strong> Heads-down execution window</div>
>       <div><strong>Comms:</strong> Delayed unless urgent</div>
>       <div><strong>Priority:</strong> Deliverables + income tasks only</div>
>     </div>
>   </div>
>   -->
> 
>   <!-- STATUS 06 — CASH CRITICAL (Immediate funding gap) -->
>   <!--
>   <div class="status-card" style="
>     margin-top: 0.9rem;
>     padding: 1rem;
>     border-radius: 12px;
>     border: 1px solid rgba(255, 120, 80, 0.30);
>     background: rgba(255, 120, 80, 0.10);
>   ">
>     <div style="font-weight:700; font-size:1rem;">Cash Critical</div>
>     <div style="margin-top:0.5rem; display:grid; gap:0.35rem; font-size:0.92rem; opacity:0.92;">
>       <div><strong>Runway:</strong> &lt; 24 hours</div>
>       <div><strong>Shelter:</strong> Unclear</div>
>       <div><strong>Operating state:</strong> Functional but pressured</div>
>       <div><strong>Priority:</strong> Bridge funds + stabilize essentials</div>
>     </div>
>   </div>
>   -->
> 
>   <!-- STATUS 07 — FOOD GAP (Fuel needed) -->
>   <!--
>   <div class="status-card" style="
>     margin-top: 0.9rem;
>     padding: 1rem;
>     border-radius: 12px;
>     border: 1px solid rgba(255, 190, 80, 0.30);
>     background: rgba(255, 190, 80, 0.10);
>   ">
>     <div style="font-weight:700; font-size:1rem;">Food Gap</div>
>     <div style="margin-top:0.5rem; display:grid; gap:0.35rem; font-size:0.92rem; opacity:0.92;">
>       <div><strong>Food:</strong> Not secured</div>
>       <div><strong>Operating state:</strong> Slipping due to low fuel</div>
>       <div><strong>Priority:</strong> Secure a meal + basics to regain function</div>
>     </div>
>   </div>
>   -->
> 
>   <!-- STATUS 08 — TRANSPORT / POWER CONSTRAINT (Charging / car logistics) -->
>   <!--
>   <div class="status-card" style="
>     margin-top: 0.9rem;
>     padding: 1rem;
>     border-radius: 12px;
>     border: 1px solid rgba(90, 180, 255, 0.28);
>     background: rgba(90, 180, 255, 0.10);
>   ">
>     <div style="font-weight:700; font-size:1rem;">Transport / Power Constraint</div>
>     <div style="margin-top:0.5rem; display:grid; gap:0.35rem; font-size:0.92rem; opacity:0.92;">
>       <div><strong>Vehicle:</strong> Managing charge / logistics</div>
>       <div><strong>Comms:</strong> Limited while in transit</div>
>       <div><strong>Priority:</strong> Charge + safe parking + next move</div>
>     </div>
>   </div>
>   -->
> 
>   <!-- STATUS 09 — MENTAL LOAD HIGH (Do not add tasks) -->
>   <!--
>   <div class="status-card" style="
>     margin-top: 0.9rem;
>     padding: 1rem;
>     border-radius: 12px;
>     border: 1px solid rgba(255, 80, 80, 0.32);
>     background: rgba(255, 80, 80, 0.10);
>   ">
>     <div style="font-weight:700; font-size:1rem;">Mental Load High</div>
>     <div style="margin-top:0.5rem; display:grid; gap:0.35rem; font-size:0.92rem; opacity:0.92;">
>       <div><strong>Operating state:</strong> Overloaded</div>
>       <div><strong>Comms:</strong> Minimal</div>
>       <div><strong>Request:</strong> Keep messages short + actionable only</div>
>     </div>
>   </div>
>   -->
> 
>   <!-- STATUS 10 — BACK ONLINE (Stabilized enough for normal comms) -->
>   <!--
>   <div class="status-card" style="
>     margin-top: 0.9rem;
>     padding: 1rem;
>     border-radius: 12px;
>     border: 1px solid rgba(70, 255, 120, 0.25);
>     background: rgba(70, 255, 120, 0.08);
>   ">
>     <div style="font-weight:700; font-size:1rem;">Back Online</div>
>     <div style="margin-top:0.5rem; display:grid; gap:0.35rem; font-size:0.92rem; opacity:0.92;">
>       <div><strong>Shelter:</strong> Stable</div>
>       <div><strong>Food:</strong> Stable</div>
>       <div><strong>Operating state:</strong> Good enough to engage</div>
>       <div><strong>Comms:</strong> Normal response cadence</div>
>     </div>
>   </div>
>   -->
> 
> </section>
> ```
> 
> Two fast warnings (because you’re putting this on a public site):
> 1) This is **highly identifying** (tells people when you’re vulnerable). If QiAlly.me is public, this can be risky.  
> 2) Better: make this section **only visible behind Zero Trust** or on your private “Home Center” page.
> 
> If you want, I’ll give you a **“public-safe”** version (no shelter/food details) and a **“private ops”** version (exact details) using the same comment-toggle pattern.

### User
> Or what if we just do like 5 colums each column is a need, shelter, food, mental state, money/resources, social. Like the hierarchy of needs and there is like a section in the html where I just update the number of each one and depending on that the triangle update the blocks color and the colors mean something like red means, insecure high risk urgent emergency or something red orange yellow green blue blue being the perfect ideal state red being the emergency state. That way I update a few numbers in the code and the triangle of needs reflects my reality and that selects and explanation based on the combination of values predefined like all 5s the note says I’m at the optimal state I can be considering and actively improving or if score is super low meaning all reds it would say Cody is in survival mode no room for error potential risk of life no bandwidth for social rules etc need immediate monitory or resource donations you get what I mean?

### Assistant
> Yes. This is the smarter, lower-friction model: you update **5 numbers**, the UI updates automatically, and the page prints a **prewritten interpretation** based on the combination.
> 
> Below is a single **drop-in HTML block** (inline CSS + tiny JS) that creates **5 “needs meters”** (columns), colors them on a **red → orange → yellow → green → blue** scale, and generates a **status readout**.
> 
> You only edit this line:
> 
> ```js
> const levels = { shelter: 2, food: 3, mental: 2, money: 1, social: 2 };
> ```
> 
> ---
> 
> ```html
> <section id="needs-status" style="
>   width: 100%;
>   padding: 1.25rem 1.5rem;
>   margin-bottom: 2rem;
>   border-radius: 14px;
>   background: rgba(255, 255, 255, 0.08);
>   backdrop-filter: blur(10px);
>   -webkit-backdrop-filter: blur(10px);
>   border: 1px solid rgba(255, 255, 255, 0.15);
> ">
> 
>   <div style="display:flex; flex-wrap:wrap; align-items:center; gap:0.75rem;">
>     <div style="
>       font-weight:700;
>       letter-spacing:0.08em;
>       font-size:0.75rem;
>       opacity:0.75;
>       text-transform:uppercase;
>       white-space:nowrap;
>     ">Needs Snapshot</div>
> 
>     <div style="opacity:0.7; font-size:0.85rem;">
>       Quick reality check across the basics. (Scale: 1 = emergency, 5 = ideal)
>     </div>
>   </div>
> 
>   <div id="needs-grid" style="
>     margin-top: 1rem;
>     display: grid;
>     grid-template-columns: repeat(5, minmax(110px, 1fr));
>     gap: 0.9rem;
>   "></div>
> 
>   <div id="needs-summary" style="
>     margin-top: 1rem;
>     padding: 0.9rem 1rem;
>     border-radius: 12px;
>     border: 1px solid rgba(255,255,255,0.14);
>     background: rgba(255,255,255,0.06);
>   ">
>     <div id="needs-title" style="font-weight:700; font-size:1rem;">Status</div>
>     <div id="needs-message" style="margin-top:0.4rem; opacity:0.92; line-height:1.4;"></div>
>   </div>
> 
>   <script>
>     // =========================
>     // EDIT ONLY THIS OBJECT
>     // Scale per category: 1 (Red) .. 5 (Blue)
>     // =========================
>     const levels = {
>       shelter: 2,
>       food: 3,
>       mental: 2,
>       money: 1,
>       social: 2
>     };
> 
>     // Labels and order
>     const categories = [
>       { key: "shelter", label: "Shelter" },
>       { key: "food",    label: "Food" },
>       { key: "mental",  label: "Mental" },
>       { key: "money",   label: "Money" },
>       { key: "social",  label: "Social" }
>     ];
> 
>     // Color mapping by level (1..5)
>     const levelStyle = {
>       1: { name: "Emergency", border: "rgba(255,80,80,0.32)",  fill: "rgba(255,80,80,0.12)"  }, // red
>       2: { name: "High Risk", border: "rgba(255,120,80,0.30)", fill: "rgba(255,120,80,0.12)" }, // orange/red
>       3: { name: "Unstable",  border: "rgba(255,190,80,0.30)", fill: "rgba(255,190,80,0.12)" }, // amber/yellow
>       4: { name: "Stable",    border: "rgba(70,255,120,0.25)", fill: "rgba(70,255,120,0.10)"  }, // green
>       5: { name: "Ideal",     border: "rgba(90,180,255,0.28)", fill: "rgba(90,180,255,0.12)"  }  // blue
>     };
> 
>     // Render columns with 5 stacked blocks (a “pyramid” vibe in columns form)
>     function render() {
>       const grid = document.getElementById("needs-grid");
>       grid.innerHTML = "";
> 
>       categories.forEach(({ key, label }) => {
>         const value = clamp(levels[key], 1, 5);
> 
>         const card = document.createElement("div");
>         card.style.cssText = `
>           padding: 0.85rem 0.9rem;
>           border-radius: 12px;
>           border: 1px solid rgba(255,255,255,0.14);
>           background: rgba(255,255,255,0.04);
>         `;
> 
>         const head = document.createElement("div");
>         head.style.cssText = "display:flex; align-items:baseline; justify-content:space-between; gap:0.5rem;";
>         head.innerHTML = `
>           <div style="font-weight:700;">${label}</div>
>           <div style="opacity:0.75; font-size:0.85rem;">${value}/5</div>
>         `;
> 
>         const meter = document.createElement("div");
>         meter.style.cssText = `
>           margin-top: 0.65rem;
>           display: grid;
>           grid-template-rows: repeat(5, 12px);
>           gap: 6px;
>         `;
> 
>         // Build 5 blocks bottom-up; fill up to value
>         for (let i = 5; i >= 1; i--) {
>           const block = document.createElement("div");
>           const active = i <= value;
>           const style = levelStyle[i];
> 
>           block.style.cssText = `
>             border-radius: 999px;
>             border: 1px solid ${active ? style.border : "rgba(255,255,255,0.12)"};
>             background: ${active ? style.fill : "rgba(255,255,255,0.03)"};
>           `;
>           meter.appendChild(block);
>         }
> 
>         const foot = document.createElement("div");
>         foot.style.cssText = "margin-top:0.65rem; opacity:0.75; font-size:0.8rem;";
>         foot.textContent = levelStyle[value].name;
> 
>         card.appendChild(head);
>         card.appendChild(meter);
>         card.appendChild(foot);
>         grid.appendChild(card);
>       });
> 
>       summarize();
>     }
> 
>     // Generate a predefined explanation based on combination
>     function summarize() {
>       const v = Object.values(levels).map(n => clamp(n, 1, 5));
>       const avg = v.reduce((a,b) => a+b, 0) / v.length;
>       const min = Math.min(...v);
> 
>       const shelter = clamp(levels.shelter, 1, 5);
>       const food    = clamp(levels.food, 1, 5);
>       const mental  = clamp(levels.mental, 1, 5);
>       const money   = clamp(levels.money, 1, 5);
>       const social  = clamp(levels.social, 1, 5);
> 
>       let title = "Status: Monitoring";
>       let msg = "Staying functional. Focus on stabilizing the lowest category first.";
> 
>       // Rule set (prioritize safety + survival constraints)
>       if (min === 1 && avg <= 2.2) {
>         title = "Status: Survival Mode";
>         msg = "Cody is in survival mode. No room for extra demands. Priorities are immediate safety, shelter, food, and cash stability. Communication may be brief and transactional.";
>       } else if (shelter <= 2 || money <= 2) {
>         title = "Status: High Risk / Time-Sensitive";
>         msg = "High risk window. Shelter and/or money stability is low. Primary objective is extending runway (safe place + funds). Everything else is secondary until those rise.";
>       } else if (mental <= 2 && (shelter >= 3 && food >= 3)) {
>         title = "Status: Strained but Functional";
>         msg = "Basics are somewhat covered, but mental load is high. Reduce inputs, avoid conflict, and prioritize rest + simple execution tasks only.";
>       } else if (avg >= 4.6 && min >= 4) {
>         title = "Status: Optimal Operating State";
>         msg = "Cody is in a strong, stable state: essentials covered, bandwidth available, and actively improving forward momentum.";
>       } else if (avg >= 3.6 && min >= 3) {
>         title = "Status: Stable / Building";
>         msg = "Core needs are stable. This is a good window to execute, rebuild runway, and increase buffers (money + contingency plans).";
>       } else if (social <= 2 && avg >= 3) {
>         title = "Status: Protected Comms";
>         msg = "Maintaining stability with low social bandwidth. Keep interactions minimal, structured, and supportive—no high-emotion negotiations.";
>       }
> 
>       // Style the summary card based on overall severity (min drives risk)
>       const summary = document.getElementById("needs-summary");
>       const severityLevel = (min <= 2) ? min : Math.round(avg); // bias toward risk
> 
>       summary.style.border = `1px solid ${levelStyle[severityLevel].border}`;
>       summary.style.background = levelStyle[severityLevel].fill;
> 
>       document.getElementById("needs-title").textContent = title;
>       document.getElementById("needs-message").textContent = msg;
>     }
> 
>     function clamp(n, a, b) { return Math.max(a, Math.min(b, Number(n) || a)); }
> 
>     render();
>   </script>
> </section>
> ```
> 
> Two blunt notes (because this matters):
> - If this is on **public QiAlly.me**, you are broadcasting when you’re vulnerable. That’s operationally risky.
> - Best practice: keep this exact block on a **Zero Trust / private page**, and put a **public-safe version** on the homepage (e.g., “Availability: Limited / Normal / Delayed”).
> 
> If you want, I’ll generate the **public-safe mirror** that uses the *same 5 numbers* but outputs sanitized language.
