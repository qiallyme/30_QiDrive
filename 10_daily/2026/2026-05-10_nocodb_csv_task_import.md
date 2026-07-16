---
layout: page
title: "NocoDB CSV Task Import"
slug: "nocodb_csv_task_import"
created_at: "2026-05-10 08:13:42"
updated_at: "2026-05-10 08:13:42"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-007.json"
template_key: master-template
date: 2026-05-10
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a008473-f224-83ea-b5b8-9f8c40ab7465"
canonical_ref: ""
---

# NocoDB CSV Task Import

## Overview
- **Date**: 2026-05-10 08:13:42
- **Conversation ID**: `6a008473-f224-83ea-b5b8-9f8c40ab7465`
- **Source**: `Chat-Export-28513-2026/conversations-007.json`

## Chat History

### User
> ok so what is the current plan and open tasks can you give me this ina csv for import into noco database.

### Assistant
> I’ll turn the messy care-plan threads into a clean Noco-ready CSV: one row per task/plan item, with status, priority, owner, category, due/repeat, and notes. I’m going to pull from the uploaded handoff/current notes first so we don’t lose the real source of truth.

### Assistant
> I’ve got the spine now: safety setup, med reconciliation, breathing/O2 tracking, transfer protocol, bills/telecom cleanup, grocery/supply controls, and the MomCare/Noco app build tasks. I’m packaging it as one import table instead of scattered lists — because scattered lists are how chaos sneaks back in wearing a fake mustache.

### Assistant
> Done — I made the NocoDB-ready CSV with **57 rows** covering:
> 
> - Current operating plan
> - Open care/safety tasks
> - Medication verification tasks
> - Breathing/O2 tracking
> - Transfer/commode safety
> - Daily recurring checklists
> - Bills/telecom cleanup
> - MomCare desktop/Noco app build tasks
> - Open medical/household questions
> 
> Download it here:
> 
> [2026-05-10_momcare_current_plan_open_tasks_nocodb_import.csv](sandbox:/mnt/data/2026-05-10_momcare_current_plan_open_tasks_nocodb_import.csv)
> 
> I based it on the household meeting summary, the MOM_CARE handoff, and the COPD care guide. The key source documents identify the immediate “Do First / Do Next / Do Later” tasks, the need for one shared task ledger, medication reconciliation, transfer safety, O2/breathing tracking, and daily care rhythms. fileciteturn1file0 fileciteturn1file1 fileciteturn1file2

### User
> ok, how should i give this to gamma or gemini to create a presentaiton or should i just give it to notebook lm, pull the video and put on youtube?

### Assistant
> Use **NotebookLM first**, then **Gamma/Gemini second**. Don’t start with Gamma. Gamma will make it pretty, but it may flatten the logic and turn the care system into generic “wellness plan” fluff. We do not need Canva-with-a-stethoscope nonsense.
> 
> Best workflow:
> 
> 1. **Give NotebookLM the CSV + the handoff/current-state docs**
> 2. Ask NotebookLM to create:
>    - executive summary
>    - caregiver briefing
>    - family-facing explanation
>    - video/audio overview
> 3. Use that output as the **narrative source**
> 4. Then give Gamma/Gemini the cleaned narrative and say: “Turn this into a presentation.”
> 
> That way NotebookLM does the “understand the source” work, and Gamma/Gemini does the “make it presentable” work.
> 
> ## What I’d make
> 
> For YouTube, I would not make it a public “here’s my mom’s care plan” video unless you scrub identifying details. Better options:
> 
> **Private/unlisted YouTube video** for family/caregivers: yes.
> 
> **Public YouTube video** only if reframed as:
> “How to Build a Home Care Operating System for a Medically Complex Parent”
> 
> That version should remove names, addresses, medication specifics, account/bill details, and anything that could embarrass your mom. Truth mode: public posting the raw family version is a privacy landmine. Unlisted is fine. Public needs anonymizing.
> 
> ## Prompt for NotebookLM
> 
> Use this first:
> 
> ```text
> You are reviewing source materials for a family home-care operating system.
> 
> The purpose is to create a clear, objective briefing that explains:
> 1. The current care situation
> 2. The operating plan
> 3. The safety priorities
> 4. The open tasks
> 5. The roles and responsibilities
> 6. The documentation system
> 7. Why this structure is necessary going forward
> 
> Audience:
> This is for family members and caregivers who need to understand the plan without blame, shame, or emotional escalation.
> 
> Important framing:
> This is not about criticizing anyone. This is about keeping a medically complex parent safer at home, reducing missed details, preventing avoidable crises, and making sure care, bills, supplies, medications, appointments, and household responsibilities are documented in one system.
> 
> Use the uploaded CSV as the task/action database.
> Use the handoff/current-state documents as the background context.
> 
> Create the following outputs:
> 
> 1. Executive Summary
> A short plain-language summary of what is happening and why the system is needed.
> 
> 2. Current Plan
> Explain the operating plan in practical terms.
> 
> 3. Top Safety Priorities
> Focus on breathing/O2, medication verification, transfer/fall risk, hygiene/continence, food/hydration, and caregiver capacity.
> 
> 4. Open Task Breakdown
> Group the open tasks by category:
> - Immediate safety
> - Medication verification
> - Breathing/O2
> - Daily care schedule
> - Supplies/groceries
> - Bills/telecom
> - App/database/system build
> - External communication
> 
> 5. Family Roles
> Explain Cody’s role as care coordinator/systems organizer, Mom’s role as decision-maker whose safety and dignity are centered, and support contributors’ role in helping execute tasks.
> 
> 6. Why Verbal Requests Are Not Enough
> Explain why care-related requests must be written down and tracked.
> 
> 7. Video Script
> Create a calm, family-facing video script that can be used for a private or unlisted YouTube explainer.
> 
> 8. Presentation Outline
> Create a 10-slide presentation outline suitable for Gamma or Gemini.
> ```
> 
> ## Prompt for Gamma / Gemini Presentation
> 
> After NotebookLM gives you the summary, give Gamma/Gemini this:
> 
> ```text
> Create a clean, family-facing presentation based on the attached care operating plan and task summary.
> 
> Goal:
> Explain the current home-care plan clearly so family members and caregivers understand what matters, what is being tracked, what needs action, and why the system exists.
> 
> Tone:
> Clear, calm, practical, respectful, and organized. Do not make it overly clinical or dramatic.
> 
> Audience:
> Family members, household support people, and caregivers.
> 
> Presentation length:
> 10–12 slides.
> 
> Structure:
> 1. Title: Home Care Operating Plan
> 2. Why This System Exists
> 3. Current Care Situation
> 4. Top Safety Priorities
> 5. Daily Care Rhythm
> 6. Medication Verification & Safety
> 7. Breathing/Oxygen & Symptom Tracking
> 8. Transfers, Commode, Fall Prevention
> 9. Supplies, Groceries, and Household Support
> 10. Bills, Transportation, and Admin Tasks
> 11. Roles and Responsibilities
> 12. What Happens Next
> 
> Design style:
> Use a clean dashboard-like design.
> Use simple icons.
> Use large readable text.
> Avoid clutter.
> Use checklists and category cards.
> Do not include private financial details, full medication specifics, addresses, or sensitive identifiers unless they are explicitly included in the source and marked safe to display.
> 
> Output:
> Create a presentation suitable for family review and private sharing.
> ```
> 
> ## For YouTube
> 
> Use this title if private/unlisted:
> 
> **Home Care Operating Plan — Family Briefing**
> 
> Use this title if public/anonymized:
> 
> **How to Build a Home Care Operating System for a Medically Complex Parent**
> 
> Description for private/unlisted:
> 
> ```text
> This video summarizes the current home-care operating plan, safety priorities, open tasks, and family support structure. It is intended to help everyone stay aligned, reduce confusion, and keep care-related responsibilities documented in one place.
> ```
> 
> My call: **NotebookLM first. Pull the video. Then use Gamma/Gemini only if you want a cleaner slide deck.** NotebookLM is better for turning the sources into a coherent explanation. Gamma is better for the pretty wrapper.

### User
> ok, im supposed to have a daily checklist when i go back in there, morning checks and prep, cleanings transfers to chair, clean up, afternoon prep, medicine, errands, then theres the wash everything, prep dinner, prep for overnight, then go back and do all the admin work.

### Assistant
> Yes. You need a **Daily Care Run Sheet** — not a vague checklist. This should follow the actual flow of the day so your brain is not rebuilding the plan every time you walk in.
> 
> Here’s the clean version.
> 
> # Mom Daily Care Checklist
> 
> ## 1. Arrival / Safety Scan
> 
> **Before asking Mom to move:**
> 
> - Check breathing/O2 status
> - Check if oxygen is on and tubing is safe
> - Clear floor path
> - Check commode position
> - Check bed/chair/wheelchair brakes
> - Check if she seems confused, dizzy, overly sleepy, panicked, or in pain
> - Ask: “Do you need bathroom, pain help, breathing treatment, food, or drink first?”
> 
> **Stop and reassess if:**
> - She is dizzy
> - O2 seems low
> - She is too sleepy
> - Breathing looks worse
> - She is rushing or panicking
> 
> ---
> 
> ## 2. Morning Check + Prep
> 
> - Check overnight condition:
>   - bed wet/soiled?
>   - diaper/underwear issue?
>   - bowel movement?
>   - urination?
>   - pain level?
>   - breathing overnight?
> - Give Powerade/drink within reach
> - Prep breakfast or small food
> - Check morning meds against verified med list
> - Log meds actually taken
> - Check O2/pulse if needed
> - Check nebulizer/breathing treatment schedule
> - Make sure phone, charger, remote, wipes, tissues, trash bag are reachable
> 
> **Morning log:**
> - O2/pulse
> - pain level
> - food/drink
> - bathroom/bowel/urine
> - meds taken
> - mood/cognition
> - any dizziness
> 
> ---
> 
> ## 3. Cleaning / Body Care / Bed Reset
> 
> When she is safely out of bed or positioned:
> 
> - Remove trash, cups, wrappers, tissues
> - Change pads/linens if wet or dirty
> - Wipe down bed area
> - Replace wipes, diapers/underwear, gloves, trash bags
> - Check skin comfort if there was wetness/soiling
> - Clean commode/urine container if used
> - Put dirty laundry in one designated bin/bag
> - Reset bed for next rest period
> 
> This is not “cleaning.” This is **infection control and fall prevention**. Tiny distinction, big deal.
> 
> ---
> 
> ## 4. Transfer to Chair / Commode / Wheelchair
> 
> Before transfer:
> 
> - Oxygen tubing clear
> - Brakes locked
> - Feet positioned
> - Chair/commode close
> - She sits upright first
> - Wait for dizziness to pass
> - No rushing
> 
> During transfer:
> 
> - One move at a time
> - Keep instructions short
> - Do not argue mid-transfer
> - If she gets weak/dizzy: stop, sit, stabilize
> 
> After transfer:
> 
> - Check breathing
> - Check comfort
> - Put drink/phone/remote nearby
> - Log dizziness or difficulty
> 
> ---
> 
> ## 5. Midday / Afternoon Prep
> 
> - Refill drink / Powerade
> - Offer food/snack/protein
> - Check pain level
> - Check breathing/O2
> - Check if nebulizer or inhaler is due/needed per instructions
> - Check bathroom need before urgency hits
> - Reset room again lightly
> - Confirm what errands actually matter today
> 
> Sort errands into:
> 
> **Must do today**
> - Meds
> - Oxygen/breathing supplies
> - Food basics
> - Bills that create shutoff/late risk
> - Medical appointments/calls
> 
> **Can wait**
> - Comfort extras
> - Non-urgent shopping
> - Cosmetic cleaning
> - Random requests
> - Anything that came from panic, not priority
> 
> ---
> 
> ## 6. Medicine Check
> 
> Do this as its own block, not while juggling chaos.
> 
> - Compare against verified med list
> - Confirm time window
> - Confirm food requirement
> - Log actual time taken
> - Note missed/refused/held meds
> - Track PRNs separately
> - Track opioid timing separately
> - Check for sedation/dizziness after pain meds
> - Check refill levels
> 
> **Do not rely on memory. Memory is fired from this job.**
> 
> ---
> 
> ## 7. Errands / Outside Tasks
> 
> Before leaving:
> 
> - Mom has drink
> - Food/snack reachable
> - Phone/charger reachable
> - Commode/urine setup safe
> - Oxygen setup safe
> - Meds not scattered
> - Trash/dirty items contained
> - Zai or backup knows what to watch if present
> 
> Errand list should be batched:
> 
> - Pharmacy
> - Groceries
> - Supplies
> - Bills/payment
> - Vehicle/work tasks
> - Household repair items
> 
> ---
> 
> ## 8. Wash Everything / Laundry Reset
> 
> Daily or as needed:
> 
> - Soiled clothes
> - Bed pads
> - Blankets/sheets
> - Towels/washcloths
> - Reusable pads/protectors
> - Mom clothing
> - Cleaning cloths
> 
> Keep separate:
> 
> - Soiled medical/hygiene laundry
> - Normal household laundry
> - Cody/Zai laundry
> - Bedding
> 
> This prevents the whole house from turning into one giant “what is this smell” mystery box.
> 
> ---
> 
> ## 9. Dinner Prep
> 
> - Prep real food or easy meal
> - Make sure she eats enough before evening meds
> - Refill Powerade/drinks
> - Set aside snacks for night
> - Set aside morning food if useful
> - Check trash/commode before night setup
> - Ask if she needs pain/breathing/bathroom help before settling
> 
> ---
> 
> ## 10. Overnight Prep
> 
> This is the big safety closeout.
> 
> - Dinner/snacks done
> - Morning snack/food nearby if needed
> - Powerade/drink + ice ready
> - Night meds taken/logged
> - Oxygen tanks/concentrator ready
> - Oxygen tubing safe
> - Nebulizer machine reachable
> - Nebulizer meds in stock
> - Pill basket reachable but not chaotic
> - Wipes reachable
> - Diapers/underwear ready
> - Bed pad/blankets/pillows good
> - Commode positioned
> - Trash bag nearby
> - Phone plugged in and reachable
> - Remote reachable
> - Night light on
> - TV functioning
> - Path clear
> 
> Final question:
> 
> “Are you comfortable, breathing okay, and do you need bathroom before I settle everything?”
> 
> ---
> 
> ## 11. Admin Work After Care
> 
> Only after the physical care loop is stable.
> 
> Update:
> 
> - Med log
> - Pain log
> - O2/breathing log
> - Bowel/urination log
> - Transfer/fall-risk notes
> - Food/hydration notes
> - Supplies used
> - Groceries needed
> - Bills/tasks
> - Calls/messages from doctors/pharmacy/home health
> - Anything Mom requested
> - Anything Cody needs help with
> 
> Then sort tasks:
> 
> | Bucket | Meaning |
> |---|---|
> | Urgent safety | Do now |
> | Care task | Schedule today |
> | Admin task | Log and batch |
> | Money task | Add to budget/bill tracker |
> | Emotional noise | Do not chase |
> | Can wait | Park it |
> 
> ## The Daily Flow
> 
> Use this as the master order:
> 
> 1. **Safety scan**
> 2. **Morning meds/food/breathing**
> 3. **Bathroom/transfer**
> 4. **Clean/reset**
> 5. **Afternoon care check**
> 6. **Errands/pharmacy/groceries**
> 7. **Laundry/wash everything**
> 8. **Dinner**
> 9. **Overnight prep**
> 10. **Admin/documentation**
> 
> That’s the system. Not perfect. Just repeatable. Repeatable beats heroic every single time.

### User
> ok, so daily flow, can you turn dialy flow into a prompt for me to give to gemini and then create a caregiver daily checklist and vitals and notes document.

### Assistant
> Absolutely. Here’s the **Gemini prompt** first, then the actual **caregiver daily checklist + vitals/notes document** you can paste into Gemini, Docs, NotebookLM, or turn into a PDF.
> 
> ## Prompt for Gemini
> 
> Use this:
> 
> ```text
> Create a clean, printable caregiver daily checklist and vitals/notes document based on the daily care flow below.
> 
> Purpose:
> This document is for a family caregiver caring for a medically complex parent at home. It should help the caregiver move through the day without forgetting safety checks, medications, breathing/O2 monitoring, transfers, hygiene, food, errands, laundry, overnight prep, and admin documentation.
> 
> Design requirements:
> - Make it simple, readable, and not overwhelming.
> - Use large headings and checkbox sections.
> - Make it printable.
> - Keep it practical and caregiver-friendly.
> - Include sections for vitals, pain, breathing/O2, bowel movements, urination, food/drink, medication notes, transfer notes, supplies needed, errands, and end-of-day admin.
> - Add a clear “Stop / Escalate” safety box.
> - Include enough blank space for handwritten notes.
> - Do not diagnose or give medical advice.
> - Medication sections should say “verify against current med list / doctor / pharmacist instructions.”
> 
> Daily Flow:
> 1. Safety scan
> 2. Morning meds / food / breathing
> 3. Bathroom / transfer
> 4. Clean / reset
> 5. Afternoon care check
> 6. Errands / pharmacy / groceries
> 7. Laundry / wash everything
> 8. Dinner
> 9. Overnight prep
> 10. Admin / documentation
> 
> Important safety themes:
> - Breathing/O2 status
> - Oxygen tubing and concentrator/tank setup
> - Fall/transfer risk
> - Dizziness before movement
> - Medication timing and verification
> - Opioid/sedation monitoring if applicable
> - Food and hydration
> - Bowel/urination tracking
> - Clean bed and commode setup
> - Caregiver burnout and admin follow-through
> 
> Create:
> 1. A one-page daily caregiver checklist
> 2. A second-page vitals and care notes log
> 3. A third-page admin follow-up log
> ```
> 
> ---
> 
> # Caregiver Daily Checklist
> 
> **Date:** ____________  
> **Caregiver:** ____________  
> **Mom’s starting condition:** ☐ Good ☐ Tired ☐ Pain ☐ Breathing concern ☐ Confused/anxious ☐ Other: ____________
> 
> ---
> 
> ## 1. Arrival Safety Scan
> 
> Before movement, check:
> 
> ☐ Breathing looks stable  
> ☐ Oxygen is on / available as ordered  
> ☐ Tubing path is clear  
> ☐ Floor path is clear  
> ☐ Commode is close enough  
> ☐ Chair/wheelchair/bed brakes checked  
> ☐ Mom is alert enough to move safely  
> ☐ Ask: bathroom, pain, breathing, food, or drink first?
> 
> **Do not rush transfers. Stabilize first.**
> 
> ---
> 
> ## 2. Morning Check + Prep
> 
> ☐ Check overnight bed/diaper/underwear condition  
> ☐ Ask about pain level  
> ☐ Ask about breathing overnight  
> ☐ Check bowel movement / urination  
> ☐ Offer Powerade / drink  
> ☐ Prep breakfast or small food  
> ☐ Check morning meds against verified med list  
> ☐ Log meds actually taken  
> ☐ Check O2 / pulse if needed  
> ☐ Confirm nebulizer / breathing treatment schedule  
> ☐ Phone, charger, remote, wipes, trash bag within reach  
> 
> ---
> 
> ## 3. Bathroom / Transfer
> 
> Before transfer:
> 
> ☐ Sit upright first  
> ☐ Wait for dizziness to pass  
> ☐ Feet positioned  
> ☐ Brakes locked  
> ☐ Oxygen tubing clear  
> ☐ Chair/commode close  
> ☐ One move at a time  
> 
> After transfer:
> 
> ☐ Breathing checked  
> ☐ Comfort checked  
> ☐ Drink/phone/remote nearby  
> ☐ Any dizziness logged  
> 
> ---
> 
> ## 4. Clean / Reset
> 
> ☐ Remove trash, cups, wrappers, tissues  
> ☐ Change wet/dirty pads or linens  
> ☐ Wipe bed area  
> ☐ Replace wipes / diapers / gloves / trash bags  
> ☐ Clean commode or urine container  
> ☐ Put dirty laundry in designated bag/bin  
> ☐ Reset bed for next rest period  
> ☐ Check supplies running low  
> 
> ---
> 
> ## 5. Afternoon Care Check
> 
> ☐ Refill Powerade / drink  
> ☐ Offer snack/protein  
> ☐ Check pain level  
> ☐ Check breathing/O2  
> ☐ Bathroom check before urgency  
> ☐ Check meds due later  
> ☐ Light room reset  
> ☐ Identify must-do errands only  
> 
> **Today’s must-do errands:**  
> 1. __________________________  
> 2. __________________________  
> 3. __________________________  
> 
> ---
> 
> ## 6. Errands / Pharmacy / Groceries
> 
> Before leaving:
> 
> ☐ Mom has drink  
> ☐ Food/snack reachable  
> ☐ Phone/charger reachable  
> ☐ Commode setup safe  
> ☐ Oxygen setup safe  
> ☐ Meds not scattered  
> ☐ Trash/dirty items contained  
> ☐ Backup person knows what to watch, if applicable  
> 
> Errands:
> 
> ☐ Pharmacy  
> ☐ Groceries  
> ☐ Care supplies  
> ☐ Bills/payment  
> ☐ Vehicle/work tasks  
> ☐ Other: ____________________
> 
> ---
> 
> ## 7. Laundry / Wash Everything
> 
> ☐ Soiled clothes  
> ☐ Bed pads  
> ☐ Blankets/sheets  
> ☐ Towels/washcloths  
> ☐ Reusable pads/protectors  
> ☐ Mom clothing  
> ☐ Cleaning cloths  
> 
> Keep separate:
> 
> ☐ Medical/hygiene laundry  
> ☐ Regular household laundry  
> ☐ Bedding  
> ☐ Cody/Zai laundry  
> 
> ---
> 
> ## 8. Dinner Prep
> 
> ☐ Prep dinner or easy meal  
> ☐ Make sure food is available before evening meds  
> ☐ Refill drink / Powerade  
> ☐ Set aside nighttime snacks  
> ☐ Set aside morning food if helpful  
> ☐ Check trash / commode  
> ☐ Ask about pain, breathing, bathroom before settling  
> 
> ---
> 
> ## 9. Overnight Prep
> 
> ☐ Dinner/snacks done  
> ☐ Morning snack/food nearby if needed  
> ☐ Powerade/drink + ice ready  
> ☐ Night meds taken and logged  
> ☐ Oxygen tanks/concentrator ready  
> ☐ Oxygen tubing safe  
> ☐ Nebulizer machine reachable  
> ☐ Nebulizer meds in stock  
> ☐ Pill basket reachable but not chaotic  
> ☐ Wipes reachable  
> ☐ Diapers/underwear ready  
> ☐ Bed pad/blankets/pillows good  
> ☐ Commode positioned  
> ☐ Trash bag nearby  
> ☐ Phone plugged in and reachable  
> ☐ Remote reachable  
> ☐ Night light on  
> ☐ TV functioning  
> ☐ Path clear  
> 
> Final check:
> 
> ☐ Comfortable  
> ☐ Breathing okay  
> ☐ Bathroom need handled  
> ☐ No urgent concerns before leaving/settling  
> 
> ---
> 
> # Vitals + Care Notes Log
> 
> **Date:** ____________
> 
> ## Vitals / Breathing
> 
> | Time | O2 % | Pulse | Oxygen Used? | Breathing Notes |
> |---|---:|---:|---|---|
> | Morning | | | ☐ Yes ☐ No | |
> | Afternoon | | | ☐ Yes ☐ No | |
> | Evening | | | ☐ Yes ☐ No | |
> | Symptom Check | | | ☐ Yes ☐ No | |
> 
> ---
> 
> ## Pain / Comfort
> 
> | Time | Pain Level 0–10 | Location | Med/Comfort Action | Helped? |
> |---|---:|---|---|---|
> | Morning | | | | ☐ Yes ☐ No |
> | Afternoon | | | | ☐ Yes ☐ No |
> | Evening | | | | ☐ Yes ☐ No |
> 
> ---
> 
> ## Food / Drink
> 
> ☐ Breakfast / morning food  
> Notes: ______________________________________
> 
> ☐ Lunch / snack  
> Notes: ______________________________________
> 
> ☐ Dinner  
> Notes: ______________________________________
> 
> ☐ Powerade / drinks available  
> Notes: ______________________________________
> 
> ---
> 
> ## Bathroom / Bowel / Urination
> 
> ### Bowel Movement
> 
> ☐ None today  
> ☐ Yes — time: ____________  
> Amount: ☐ Small ☐ Medium ☐ Large  
> Consistency: ☐ Hard ☐ Normal ☐ Loose ☐ Diarrhea  
> Accident/mess? ☐ No ☐ Yes  
> Notes: ______________________________________
> 
> ### Urination
> 
> ☐ Commode  
> ☐ Diaper/underwear  
> ☐ Bed accident  
> ☐ Urgency issue  
> ☐ Pain/burning/blood concern  
> 
> Notes: ______________________________________
> 
> ---
> 
> ## Medication Notes
> 
> **Verify against current medication list / doctor / pharmacist instructions.**
> 
> | Time | Medication / Category | Taken? | Notes |
> |---|---|---|---|
> | Morning | | ☐ Yes ☐ No ☐ Held | |
> | Midday | | ☐ Yes ☐ No ☐ Held | |
> | Evening | | ☐ Yes ☐ No ☐ Held | |
> | PRN / As-needed | | ☐ Yes ☐ No | |
> 
> Special notes:
> 
> ☐ Opioid/pain med timing logged if used  
> ☐ Sedation/dizziness checked  
> ☐ Breathing concerns after meds? ☐ No ☐ Yes  
> ☐ Refill needed? ☐ No ☐ Yes: ____________________
> 
> ---
> 
> ## Transfer / Mobility Notes
> 
> ☐ Transfer to commode  
> ☐ Transfer to chair  
> ☐ Transfer to wheelchair  
> ☐ Stayed in bed most of day  
> ☐ Dizziness during movement  
> ☐ Weakness during movement  
> ☐ Fall or near-fall concern  
> 
> Notes: ______________________________________
> 
> ---
> 
> # Stop / Escalate Box
> 
> Call for medical help, nurse line, doctor, pharmacy, urgent care, or 911 depending severity if there is:
> 
> ☐ Severe breathing trouble  
> ☐ O2 much lower than usual or not improving  
> ☐ Chest pain  
> ☐ Severe confusion or sudden behavior change  
> ☐ Fall or head injury  
> ☐ New weakness  
> ☐ Severe uncontrolled pain  
> ☐ Possible medication double-dose / overdose  
> ☐ Extreme sleepiness after sedating meds  
> ☐ Blood in stool/urine or black stool  
> ☐ Fever with decline  
> ☐ Signs of dehydration  
> ☐ Allergic reaction or swelling  
> 
> ---
> 
> # Admin Follow-Up Log
> 
> ## Must Handle Today
> 
> 1. ______________________________________  
> 2. ______________________________________  
> 3. ______________________________________  
> 
> ---
> 
> ## Calls / Messages Needed
> 
> ☐ Doctor  
> ☐ Pharmacy  
> ☐ Home health  
> ☐ Caseworker / Humana  
> ☐ Family member  
> ☐ Bill/company  
> ☐ Other: ____________________
> 
> Notes: ______________________________________
> 
> ---
> 
> ## Supplies Needed
> 
> ☐ Wipes  
> ☐ Diapers/underwear  
> ☐ Bed pads  
> ☐ Gloves  
> ☐ Trash bags  
> ☐ Nebulizer meds/supplies  
> ☐ Oxygen tubing/cannula  
> ☐ Cleaning supplies  
> ☐ Powerade/drinks  
> ☐ Easy food/protein  
> ☐ Other: ____________________
> 
> ---
> 
> ## Groceries Needed
> 
> 1. ______________________________________  
> 2. ______________________________________  
> 3. ______________________________________  
> 4. ______________________________________  
> 5. ______________________________________  
> 
> ---
> 
> ## Bills / Money Notes
> 
> ☐ Bill due  
> ☐ Payment made  
> ☐ Login/account needed  
> ☐ Receipt needed  
> ☐ Add to tracker  
> ☐ Reconcile later  
> 
> Notes: ______________________________________
> 
> ---
> 
> ## End-of-Day Documentation
> 
> Update:
> 
> ☐ Med log  
> ☐ Pain log  
> ☐ O2/breathing log  
> ☐ Bowel/urination log  
> ☐ Food/hydration notes  
> ☐ Transfer notes  
> ☐ Supply inventory  
> ☐ Grocery list  
> ☐ Bill tracker  
> ☐ Open requests/tasks  
> 
> ---
> 
> ## Tomorrow’s Top 3
> 
> 1. ______________________________________  
> 2. ______________________________________  
> 3. ______________________________________  
> 
> ---
> 
> The better move: have Gemini make this pretty, but **do not let it rewrite the logic too much**. Tell it to preserve the structure and only improve layout.
