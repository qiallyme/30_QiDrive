---
layout: page
title: "Directory tree structure"
slug: "directory_tree_structure"
created_at: "2025-12-11 13:13:56"
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
source_file: "Chat-Export-28513-2026/conversations-002.json"
template_key: master-template
date: 2025-12-11
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "693b17f3-6360-8332-9b72-ad4d84675059"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Directory tree structure

## Overview
- **Date**: 2025-12-11 13:13:56
- **Conversation ID**: `693b17f3-6360-8332-9b72-ad4d84675059`
- **Source**: `Chat-Export-28513-2026/conversations-002.json`

## Chat History

### User
> Uh, ma'am, can we work on, uh, putting together this project, real quick, of Soho Projects? With the different, uh, I guess phases would be the different filings, like the different, like, uh, strategic plans or whatever. You might want to just start off by giving me, like, what a directory tree would look like for this project.

### Assistant
> Yep, let’s spin this up.
> 
> I’m going to treat **Soho Projects** as the master folder for everything around FCFCU / sheriff / housing, and then break it into **phases = filings / strategies** with a **reusable template** for each phase.
> 
> Here’s a clean starting tree:
> 
> ```text
> Soho_Projects/
> ├── 00_SYSTEM/
> │   ├── 00_README_Soho_Projects.md
> │   ├── 01_Master_Timeline.xlsx
> │   ├── 02_Contact_List.md
> │   ├── 03_Glossary_and_Codes.md
> │   └── 04_Templates/
> │       ├── Phase_Folder_Template.txt
> │       ├── Pleading_Template.docx
> │       ├── Evidence_Affidavit_Template.docx
> │       └── Email_Letter_Template.docx
> │
> ├── 01_Facts_and_Records/
> │   ├── 01_Property_and_Mortgage/
> │   ├── 02_Sheriff_Service_Records/
> │   ├── 03_Sheriff_Sale_and_Writ/
> │   ├── 04_Case_Docket_and_Orders/
> │   └── 05_Personal_Statements_and_Affidavits/
> │
> ├── 02_Research_and_Strategy/
> │   ├── 01_Legal_Research_TR60_and_Service/
> │   ├── 02_ADA_TitleII_and_Access/
> │   ├── 03_Tort_and_Damages_Theory/
> │   └── 99_Notes_Scratchpad/
> │
> ├── 10_Phase_01_Void_Judgment_TR60B/
> │   ├── 00_PLAN/
> │   │   ├── 01_Objectives.md
> │   │   └── 02_Issues_Checklist.md
> │   ├── 10_Drafts/
> │   │   └── 2025-12-10_Motion_to_Vacate_Void_Judgment_draft.docx
> │   ├── 20_Filed/
> │   │   └── 2025-12-10_01_motion_vacate_filed.pdf
> │   ├── 30_Exhibits/
> │   │   ├── EX_A_Sheriff_Return_2025-03-05.pdf
> │   │   ├── EX_B_Sheriff_Return_2025-04-15.pdf
> │   │   ├── EX_C_Summons_Blank_Return.pdf
> │   │   ├── EX_D_Plaintiff_Motion_for_Default_Judgment.pdf
> │   │   └── EX_F_Cody_Affidavit_No_Service.pdf
> │   ├── 40_Orders_and_Hearings/
> │   └── 90_Archive/
> │
> ├── 20_Phase_02_Stay_or_Quash_Writ_and_Protect_Property/
> │   ├── 00_PLAN/
> │   ├── 10_Drafts/
> │   │   └── Emergency_Motion_Stay_Writ_and_Protect_Property_draft.docx
> │   ├── 20_Filed/
> │   │   └── 2025-12-10_02_emergency_motion_stay_writ_filed.pdf
> │   ├── 30_Exhibits/
> │   │   ├── EX_E_Petition_for_Writ_of_Assistance.pdf
> │   │   ├── EX_F_Cody_Affidavit_Displacement_and_Harm.pdf
> │   │   └── Photos_Video_Removal_Event/
> │   ├── 40_Orders_and_Hearings/
> │   └── 90_Archive/
> │
> ├── 30_Phase_03_ADA_and_Access_Accommodations/
> │   ├── 00_PLAN/
> │   ├── 10_Drafts/
> │   │   ├── ADA_Notice_TitleII_draft.docx
> │   │   └── Accommodation_Requests_to_Court_Sheriff_Bank.docx
> │   ├── 20_Filed_or_Sent/
> │   │   ├── ADA_TitleII_Notice_filed_or_served.pdf
> │   │   └── AES_ADA_Documentation_Packet.pdf
> │   ├── 30_Exhibits/
> │   │   └── Medical_and_Disability_Docs/
> │   ├── 40_Responses_and_Orders/
> │   └── 90_Archive/
> │
> ├── 40_Phase_04_Damages_and_Follow_on_Claims/
> │   ├── 00_PLAN/
> │   ├── 10_Drafts/
> │   │   ├── Draft_Complaint_Damages_vs_FCFCU_and_Others.docx
> │   │   └── Demand_Letters_to_Insurers_and_Agencies.docx
> │   ├── 20_Filed/
> │   ├── 30_Exhibits/
> │   ├── 40_Settlement_and_Offers/
> │   └── 90_Archive/
> │
> ├── 50_Provider_and_E-Filing_Operations/
> │   ├── 01_EFiling_Providers_and_Logins/
> │   │   ├── EFSP_Comparison_Chart.pdf
> │   │   └── Provider_Notes.md
> │   ├── 02_EFiling_Receipts_and_Envelopes/
> │   │   └── 2025-12-10_Envelope_37268798_Receipt.pdf
> │   └── 03_Checklists_for_Efile_and_Service.md
> │
> ├── 60_Communications_and_Correspondence/
> │   ├── 01_To_Court_Clerk_and_Staff/
> │   ├── 02_To_Sheriff_and_Civil_Process/
> │   ├── 03_To_FCFCU_and_Counsel/
> │   │   ├── 2025-12-09_Request_to_Schedule_Retrieval_of_Personal_Belongings_email.pdf
> │   └── 04_To_Third_Parties_(AES, agencies, etc.)/
> │
> └── 90_ARCHIVE_and_Exports/
>     ├── 01_Zip_Backups/
>     └── 02_Obsidian_Exports/
> ```
> 
> How this maps to what you already have
> 
> - **Phase 1 – Void Judgment (TR 60(B))** → where your *Motion to Vacate Void Judgment* and proposed order live, plus the exhibit list and combined exhibits. fileciteturn0file3  
> - **Phase 2 – Stay/Quash Writ + Protect Property** → your *Emergency Motion to Stay/Quash Writ* and proposed order(s) go here, with all evidence of removal, freezing temps, dog, and risk to belongings. fileciteturn0file3  
> - **Phase 3 – ADA / Access** → your ADA Title II notice and AES disability packet slot straight into this phase. fileciteturn0file3  
> - **Phase 4 – Damages** → future claims once you’ve stabilized and the court has dealt with the void judgment / writ.
> 
> - The **E-filing ops** folder hangs all the EFSP comparison stuff and envelope receipts in one place so you’re not hunting for “that random PDF with the provider chart” every time you need to file. fileciteturn0file1  
> - The **Comms** folder is where your email to FCFCU about retrieving belongings lives (that’s part of the story and also evidence of how they handled your stuff). fileciteturn0file0  
> 
> If you want, next step I can:
> 
> - Turn this into a **copy-pasteable scaffold script** (bash / PowerShell) so you can generate this tree in one shot, and  
> - Fill in a **Phase_Folder_Template.md** so every new filing/phase you spin up has the same internal structure automatically.

### User
> we need a real name for this projet for the filings and such with AES and FCFCU and anyone else that trys to take my rights from me. what do we call this project.

### Assistant
> Alright, Cody — pause. You need a **clean, serious, umbrella project name** that sounds like a legal program, not a revenge tour. It has to work on:  
> - court filings  
> - ADA notices  
> - correspondence  
> - future civil claims  
> - your internal binder structure  
> - and not make you look unhinged to a judge or attorney.
> 
> **Constraints:**  
> - Neutral, professional, not emotional  
> - Broad enough to cover FCFCU, Sheriff, AES, *and any future entity*  
> - Signals “systemic rights violations + procedural failures”  
> - Works as a *case project*, not a brand
> 
> I’ll give you **six strong contenders** and tell you which one is the best.
> 
> ---
> 
> # 🔥 Top Picks (with meaning)
> 
> ## **1. “Project Due Process”**  
> **Cleanest, safest, most judge-friendly.**  
> Covers everything: improper service, wrongful eviction, ADA violations, utilities issues — all flow from **lack of due process + failure to provide legally required notice and accommodations.**  
> You can use this in filings without raising eyebrows.
> 
> → *This is my #1 recommendation.*
> 
> ---
> 
> ## **2. “Civil Rights Continuity Project”**  
> Signals: my civil rights were interrupted, violated, or ignored.  
> Covers housing, utilities, disability access, service of process, etc.
> 
> ---
> 
> ## **3. “Access & Accountability Initiative”**  
> This is ADA-compatible and broad enough for procedural failures.  
> Sounds like a policy reform project, not a personal meltdown. Good for credibility.
> 
> ---
> 
> ## **4. “Project Safeguard”**  
> More protective in tone: “I’m documenting every breach of my legal safeguards.”
> 
> ---
> 
> ## **5. “The Rights Restoration Project”**  
> For when you’re overturning void judgments, restoring access, correcting false records, stabilizing utilities, and reclaiming property.
> 
> ---
> 
> ## **6. “Continuum Case Integrity Project”**  
> This is the high-end, consultant-grade version.  
> Focuses on:  
> - integrity of the record  
> - continuity of service  
> - failures across agencies  
> Fits your vibe *and* looks great in an evidence binder.
> 
> ---
> 
> # If you want the **leanest**, most litigation-ready name:
> ### ⭐ **Project Due Process**
> 
> # If you want the **most Cody / strategic systems** name:
> ### ⭐ **Continuum Case Integrity Project (CCIP)**  
> — This one also aligns with QiAlly’s systems architecture vibe.
> 
> ---
> 
> # My blunt recommendation  
> Pick one of these three depending on tone:
> 
> | Tone You Want | Best Name |
> |---------------|-----------|
> | Professional, legal, judge-safe | **Project Due Process** |
> | Systems + accountability | **Continuum Case Integrity Project (CCIP)** |
> | Civil rights focus | **Rights Restoration Project** |
> 
> ---
> 
> Tell me which tone you want, and I’ll finalize the name *and rebuild your directory tree under it.*

### User
> lean and aligns with QiAlly. QiMotions Case Q, or something.

### Assistant
> Alright — you want **lean, system-coded, QiAlly-aligned**, and something that still looks legit in a court filing without looking like you're running a Marvel franchise.
> 
> Here’s the clean truth:  
> **“QiMotions Case Q” is *close*, but it reads a little too cute for legal use.**  
> We need something that threads the needle:
> 
> - **QiAlly internal structure** ✔  
> - **Neutral to outsiders** ✔  
> - **Looks like a legitimate legal operations codename** ✔  
> - **Scalable across FCFCU, AES, Sheriff, future defendants** ✔  
> - **Short enough to slap on folders/docs** ✔  
> 
> So here are the *tightest*, most legally-palatable options that stay on-brand:
> 
> ---
> 
> # 🔥 **TOP 3 (Lean, QiAlly-style, Court-Safe)**
> 
> ## ⭐ **1. QiCase-Q**  
> **This is the cleanest.**  
> Elegant, neutral, system-coded, instantly readable.
> 
> - “QiCase” = your standardized QiAlly litigation framework  
> - “Q” = your identifier (matches your personal brand)  
> - Judge-safe: doesn’t look dramatic, emotional, or informal  
> 
> **Formats nicely:**  
> - `QiCase-Q/01_Facts`  
> - `QiCase-Q/10_Motions`  
> - `QiCase-Q/ADA/Notice_TitleII.pdf`
> 
> ---
> 
> ## ⭐ **2. QiDocket-Q**  
> Slightly more judicial-flavored.  
> Gives the sense of: “This is my internal record integrity and filings workflow.”
> 
> Good if you want something closer to “official court vibe.”
> 
> ---
> 
> ## ⭐ **3. QiMotions-Q**  
> This is closest to what *you* proposed — but tightened.  
> It implies: “This is my internal system for motions and responses.”
> 
> Cleaner and more professional than “QiMotions Case Q.”
> 
> ---
> 
> # 🧠 Why these work
> They mirror how professional litigation support systems name internal projects:  
> **short prefix + case ID.**  
> It makes everything modular and machine-sortable, which fits your QiAlly architecture.
> 
> And — important —  
> **none of these will look weird if an attorney, judge, or agency sees them on a file header.**
> 
> ---
> 
> # 🎯 My recommendation (if you want the exact right balance)  
> ## ➤ **QiCase-Q**  
> Leanest. Strongest. Most scalable.  
> Zero cringe factor.  
> Fully compatible with future sub-cases (Eviction, Bankruptcy, Utilities, ADA).
> 
> ---
> 
> # If you pick one, I’ll immediately regenerate your full directory tree under that name.
> 
> So:  
> **QiCase-Q, QiDocket-Q, or QiMotions-Q?**

### User
> actually before we shoot me in the foot I have project for AES already, since these are similar but different entities, should we just keep fcfcu in its own projec.t

### Assistant
> Yes. **Keep FCFCU in its own project.**  
> Do *not* merge AES + FCFCU into one mega-case archive. That will shoot you in BOTH feet.
> 
> Here’s the hard truth:
> 
> - **AES = utilities, billing, energy assistance, ADA access failures, meter issues, wrongful disconnections.**  
> - **FCFCU = foreclosure, service errors, sheriff conduct, property loss, due process violations.**  
> 
> Different facts.  
> Different laws.  
> Different defendants.  
> Different courts.  
> Different remedies.
> 
> If you merge them, your binder turns into a swamp, and no attorney will touch it.
> 
> ### BUT — your master system can still use a common naming structure:
> - **QiCase-AES**  
> - **QiCase-FCFCU**  
> - **QiCase-SHERIFF** (if needed)  
> - **QiCase-STATE** (if you ever pursue ADA Title II state-level action)
> 
> This keeps everything aligned with QiAlly and still court-clean.
> 
> ---
> 
> # Why this separation is critical  
> ### 1. **Judges hate when unrelated issues are mixed.**  
> If you present AES disputes inside FCFCU filings, your credibility tanks.
> 
> ### 2. **It preserves clarity of harm.**  
> - FCFCU violated your **property rights + due process**.  
> - AES violated your **access accommodations + essential services**.
> 
> They’re related emotionally, not legally.
> 
> ### 3. **You are building future claims.**  
> Each defendant needs its own documentary trail.
> 
> ### 4. **You can still reference cross-impact**  
> You can say:  
> > “Due to the unlawful eviction, I lost access to utilities and essential documentation needed for AES casework.”  
> …but only as context — not part of the case itself.
> 
> ---
> 
> # Clean hierarchy going forward
> 
> ```
> QiCase-FCFCU/
>    00_SYSTEM/
>    01_Facts/
>    10_Phase_01_Void_Judgment/
>    20_Phase_02_Stay_Writ/
>    ...
> 
> QiCase-AES/
>    00_SYSTEM/
>    01_Facts/
>    10_Phase_01_Account_Dispute/
>    20_Phase_02_ADA_Accommodations/
>    ...
> 
> QiCase-SHERIFF/         (optional but smart)
>    00_SYSTEM/
>    01_Facts/
>    10_Phase_01_Unlawful_Entry/
>    20_Phase_02_Damages/
>    ...
> 
> QiCase-STATE/           (only if needed)
> ```
> 
> ---
> 
> # Now the real question for you:
> ### ➤ Do you want **FCFCU** to be called:  
> - **QiCase-FCFCU**,  
> - **QiCase-Q**, or  
> - something slightly stylized like **QiCase-MortgageQ**?
> 
> I can spin the directory tree instantly once you pick.

### User
> ok give me the project description what tabs to include, and the directory and phases, tasklists and tasks, now we already have a somewhay system going try not to end up making my ADHD ass have to rename and renumver everything.

### Assistant
> Got you. I’m NOT blowing up your system or forcing renames.  
> I’m locking this into what you’ve *already* been building, just tightening it so you can run without re-numbering your whole damn life again.
> 
> This is for **QiCase-FCFCU** only.  
> (We keep AES as **QiCase-AES**, untouched.)
> 
> ---
> 
> # ✅ **PROJECT DESCRIPTION — QiCase-FCFCU**
> **QiCase-FCFCU** is your structured litigation-ops project for everything involving:
> 
> - FCFCU’s foreclosure procedural failures  
> - Lack of service → void judgment  
> - Sheriff’s unlawful/defective execution of writ  
> - Property loss, harm, ADA access failures  
> - Emergency filings needed to stabilize the situation  
> 
> This project tracks **facts, filings, evidence, correspondence, ADA accommodations, hearings, and damages** in a structured, numbered, ADHD-proof system.
> 
> **Goal:**  
> Restore due process, vacate void judgment, stay/undo writ actions, reclaim rights/property, and build a clean documentary foundation for damages.
> 
> ---
> 
> # ✅ **CORE TABS (You’ll use these repeatedly)**  
> (These reflect how your brain already organizes info.)
> 
> ### **1. Facts & Evidence**
> - Timeline  
> - Exhibits  
> - Photos/videos  
> - Affidavits  
> - Sheriff actions  
> - Bank communications  
> - Debit card renewal evidence  
> - “No notice ever received” proof  
> - ADA context (optional cross-reference only)
> 
> ### **2. Filings (Motions, Proposed Orders, Drafts)**
> Each filing = its own small “phase” folder (you already know this rhythm).
> 
> ### **3. Service & E-Filing Ops**
> - EFSP receipts  
> - File-stamped PDFs  
> - What was served + when  
> - Who received it
> 
> ### **4. Research & Strategy**
> - TR60(B) (void judgment)  
> - Stay / quash writ  
> - Service rules  
> - Damages theories  
> - ADA Title II intersections (context only)
> 
> ### **5. Communications**
> - To clerk  
> - To sheriff  
> - To FCFCU  
> - To attorneys  
> - To agencies  
> - Phone scripts + email drafts
> 
> ### **6. Orders & Hearings**
> - Scheduled dates  
> - Notes  
> - Required follow-ups  
> - What to file before/after a hearing
> 
> ### **7. Taskboard (ADHD-safe)**
> - Today  
> - Urgent  
> - Next filings  
> - Evidence to pull  
> - People to call  
> - Items to print  
> - To archive later
> 
> ---
> 
> # ✅ **DIRECTORY: CLEAN + MINIMAL CHANGES TO WHAT YOU HAVE**
> I’m keeping the logic identical so you’re not renaming your life.
> 
> ```text
> QiCase-FCFCU/
> ├── 00_SYSTEM/
> │   ├── README_QiCase_FCFCU.md
> │   ├── Master_Timeline.xlsx
> │   ├── Contacts.md
> │   ├── Glossary.md
> │   └── Templates/
> │       ├── Motion_Template.docx
> │       ├── Proposed_Order_Template.docx
> │       ├── Affidavit_Template.docx
> │       └── Evidence_Index_Template.md
> │
> ├── 01_Facts_and_Evidence/
> │   ├── Timeline/
> │   ├── Exhibits/
> │   ├── Affidavits/
> │   ├── Photos_Video/
> │   └── Communications_Proof/
> │
> ├── 02_Research_and_Strategy/
> │   ├── TR60B_Void_Judgment/
> │   ├── Service_of_Process/
> │   ├── Stay_and_Writ_Law/
> │   ├── Damages_Research/
> │   └── Notes_Scratchpad/
> │
> ├── 10_Phase_01_Void_Judgment/
> │   ├── 00_PLAN/
> │   ├── 10_Drafts/
> │   ├── 20_Filed/
> │   ├── 30_Exhibits/
> │   ├── 40_Orders/
> │   └── 90_Archive/
> │
> ├── 20_Phase_02_Stay_or_Quash_Writ/
> │   ├── 00_PLAN/
> │   ├── 10_Drafts/
> │   ├── 20_Filed/
> │   ├── 30_Exhibits/
> │   ├── 40_Orders/
> │   └── 90_Archive/
> │
> ├── 30_Phase_03_Retrieval_of_Property/
> │   ├── 00_PLAN/
> │   ├── 10_Drafts/
> │   ├── 20_Filed_or_Sent/
> │   ├── 30_Damage_Inventory/
> │   ├── 40_Orders_or_Responses/
> │   └── 90_Archive/
> │
> ├── 40_Phase_04_Damages_and_FollowOn_Claims/
> │   ├── 00_PLAN/
> │   ├── 10_Drafts/
> │   ├── 20_Filed/
> │   ├── 30_Evidence/
> │   ├── 40_Offers_and_Responses/
> │   └── 90_Archive/
> │
> ├── 50_EFiling_and_Service/
> │   ├── EFSP_Comparison.pdf
> │   ├── Envelopes/
> │   ├── Service_Proof/
> │   └── Checklists.md
> │
> ├── 60_Communications/
> │   ├── Court_Clerk/
> │   ├── Sheriff/
> │   ├── FCFCU/
> │   ├── Attorneys/
> │   └── Third_Parties/
> │
> └── 90_ARCHIVE/
>     └── _Backups/
> ```
> 
> This requires **zero renumbering** of any system you built earlier.
> 
> ---
> 
> # ✅ **PHASES (DON’T REORDER — THIS MATCHES WHAT WE ALREADY BUILT)**
> ### **Phase 01 — Void Judgment (TR60(B))**  
> The foundation. Everything else hangs from this.
> 
> ### **Phase 02 — Emergency Stay / Quash Writ**  
> Stops sheriff actions, stabilizes situation.
> 
> ### **Phase 03 — Retrieval of Property / ADA Access Failures**  
> Document losses, mishandling, inability to access belongings, etc.
> 
> ### **Phase 04 — Damages & Follow-on Claims**  
> Only after the case stabilizes.
> 
> ---
> 
> # ✅ **ADHD-SAFE TASK CATEGORIES**
> Use this format so you don’t feel scattered:
> 
> ### ⭐ **1. Critical (Today / ASAP)**
> - Call clerk  
> - Confirm hearing dates  
> - Track filings  
> - Retrieve file-stamped versions  
> - Prep next motion (if any)
> 
> ### ⭐ **2. Evidence Tasks**
> - Pull debit card replacement letter  
> - Pull credit report timeline  
> - Pull eviction-day audio/video recollections  
> - Document personal property losses  
> - Document notice failures  
> - Document sheriff conduct
> 
> ### ⭐ **3. Filing Tasks**
> - Draft supplemental affidavit  
> - Draft proposed order revisions  
> - Prepare exhibit labels  
> - Update evidence index
> 
> ### ⭐ **4. Communications Tasks**
> - Sheriff request for inventory access  
> - FCFCU legal contact outreach  
> - Clerk verification emails  
> - ADA notice (optional)
> 
> ### ⭐ **5. Organizational Tasks**
> - File PDFs into the correct phase  
> - Update timeline  
> - Add tasks to QiOS/QiSuite view  
> 
> ---
> 
> # ⭐ **HERE’S YOUR OFFICIAL PROJECT NAME + STRUCTURE**
> 
> ## **Project Name:**  
> # **QiCase-FCFCU**
> 
> ## **Short Description:**  
> “A structured due-process case management system for FCFCU foreclosure errors, improper service, sheriff misconduct, ADA access issues, and resulting damages.”
> 
> ## **Status:**  
> Active — Phase 01 + Phase 02 underway.
> 
> ---
> 
> If you want, I’ll now:
> 
> - generate your **README_QiCase_FCFCU.md**  
> - generate your **taskboard** as a markdown checklist  
> - generate your **Phase templates**  
> - or generate **your binder cover + spine labels**  
> 
> Tell me which one you want next.

### User
> tabs are task, reports, documents, Google drive, pages (wiki), reports. finance, expense, timelogs. so I need the Google drive directory tree which you gave me but the pages is the wiki the Case history, case facts, overviews, summaries strategies, and archival filings documents like a true wiki. or we use the wiki as hour semi permanent structure with versioning built in like  hybrid approach what do you think.

### Assistant
> Alright Cody, listen — you’re actually on the right instinct, but let me cut through the fog so you don’t build a monstrosity that collapses under its own ADHD chaos.
> 
> **You need TWO layers:**
> 1. **Google Drive = the hard evidence + filings + PDFs + exhibits + receipts.**  
> 2. **Wiki (Pages) = the brain → narrative, summaries, strategy, history, timelines, interpretation.**
> 
> Never mix them.  
> Never overload Drive with “thinking.”  
> Never overload the wiki with “documents.”
> 
> This hybrid is actually how professional litigation teams run cases.
> 
> Let me break it down clean and smart.
> 
> ---
> 
> # ✅ **THE RIGHT APPROACH (hybrid):**
> ### **Google Drive = SYSTEM OF RECORD**  
> Always the truth.  
> No versions except actual file history.  
> All court filings, all evidence, all exhibits, all receipts, all media, all affidavits.
> 
> ### **Wiki (Pages) = SYSTEM OF MEANING**  
> Your interpretations.  
> Your summaries.  
> Your taskboard.  
> Your case history.  
> Your strategy snapshots.  
> Your timelines.
> 
> And Pages/Wiki *naturally* provides versioning, which protects your ADHD from overwriting history or losing track of changes.
> 
> ---
> 
> # 🔥 So yes — **use the Wiki as the semi-permanent structure**  
> with versioning,  
> and use Drive as the cold storage evidence vault.
> 
> ---
> 
> # 🧩 **Let me give you both trees side-by-side now.**
> 
> ---
> 
> # ===========================
> # ✅ **1. GOOGLE DRIVE DIRECTORY TREE (QiCase-FCFCU)**
> # ===========================
> **This is the authoritative evidence vault.**  
> You already like the numbering system. I’m not changing it.
> 
> ```text
> QiCase-FCFCU/
> ├── 00_SYSTEM/
> │   ├── README_QiCase_FCFCU.md
> │   ├── Master_Timeline.xlsx
> │   ├── Contacts.md
> │   ├── Glossary.md
> │   └── Templates/
> │       ├── Motion_Template.docx
> │       ├── Proposed_Order_Template.docx
> │       ├── Evidence_Affidavit_Template.docx
> │       └── Evidence_Index_Template.md
> │
> ├── 01_Facts_and_Evidence/
> │   ├── Timeline/
> │   ├── Exhibits/
> │   ├── Affidavits/
> │   ├── Photos_and_Video/
> │   └── Communications_Proof/
> │
> ├── 02_Research_and_Strategy/
> │   ├── TR60B_Void_Judgment/
> │   ├── Service_of_Process/
> │   ├── Stay_and_Writ_Law/
> │   ├── Damages_Research/
> │   └── Notes/
> │
> ├── 10_Phase_01_Void_Judgment/
> │   ├── 00_PLAN/
> │   ├── 10_Drafts/
> │   ├── 20_Filed/
> │   ├── 30_Exhibits/
> │   ├── 40_Orders/
> │   └── 90_Archive/
> │
> ├── 20_Phase_02_Stay_or_Quash_Writ/
> │   ├── 00_PLAN/
> │   ├── 10_Drafts/
> │   ├── 20_Filed/
> │   ├── 30_Exhibits/
> │   ├── 40_Orders/
> │   └── 90_Archive/
> │
> ├── 30_Phase_03_Retrieval_of_Property/
> │   ├── 00_PLAN/
> │   ├── 10_Drafts/
> │   ├── 20_Filed_or_Sent/
> │   ├── 30_Damage_Inventory/
> │   ├── 40_Responses/
> │   └── 90_Archive/
> │
> ├── 40_Phase_04_Damages_and_FollowOn_Claims/
> │   ├── 00_PLAN/
> │   ├── 10_Drafts/
> │   ├── 20_Filed/
> │   ├── 30_Evidence/
> │   ├── 40_Offers_and_Responses/
> │   └── 90_Archive/
> │
> ├── 50_EFiling_and_Service/
> │   ├── EFSP_Comparison.pdf
> │   ├── Envelopes/
> │   ├── Service_Proof/
> │   └── Checklists/
> │
> ├── 60_Communications/
> │   ├── Court_Clerk/
> │   ├── Sheriff/
> │   ├── FCFCU/
> │   ├── Attorneys/
> │   └── Third_Parties/
> │
> └── 90_ARCHIVE/
>     ├── Backups/
>     └── Old_Structures/
> ```
> 
> ---
> 
> # ===========================
> # ✅ **2. WIKI / PAGES (QiCase-FCFCU)**  
> # ===========================
> **This is where your brain goes.**  
> Think of it like a casebook or litigation wiki.
> 
> Here’s the structure that works with your tabs:
> 
> ```text
> Wiki/
> ├── Case_History/
> │   ├── Overview.md
> │   ├── Chronology.md
> │   ├── Key_Issues.md
> │   ├── Parties_and_Roles.md
> │   ├── Case_Positioning.md
> │   └── Status_Updates.md
> │
> ├── Case_Facts/
> │   ├── Service_Failure.md
> │   ├── Sheriff_Conduct.md
> │   ├── Property_Removal_Event.md
> │   ├── Debit_Card_Proof.md
> │   ├── Credit_Report_Sequence.md
> │   └── ADA_Context.md
> │
> ├── Strategy/
> │   ├── Master_Strategy.md
> │   ├── TR60B_Strategy.md
> │   ├── StayOrQuash_Strategy.md
> │   ├── Retrieval_Strategy.md
> │   ├── Damages_Strategy.md
> │   └── Risk_Assessment.md
> │
> ├── Filings_And_Responses/
> │   ├── Filing_Summaries.md
> │   ├── Proposed_Motions.md
> │   ├── Orders_and_Hearings.md
> │   └── Attorney_Notes.md
> │
> ├── Reports/
> │   ├── Daily_Report_Log.md
> │   ├── Weekly_Review.md
> │   ├── Evidence_Audit.md
> │   ├── Witness_Notes.md
> │   └── Expense_to_Financial_Harm_Report.md
> │
> ├── Tasks/
> │   ├── Taskboard.md
> │   ├── Today.md
> │   ├── Filing_Queue.md
> │   ├── Evidence_To_Pull.md
> │   └── Communications_To_Send.md
> │
> ├── Finance/
> │   ├── Expenses.md
> │   ├── Mileage.md
> │   ├── Lost_Property_Valuation.md
> │   ├── Housing_Loss_Costs.md
> │   └── Damages_Model.md
> │
> └── Timelogs/
>     ├── 2025-Dec.md
>     ├── 2026-Jan.md
>     └── Master_Log.md
> ```
> 
> ---
> 
> # 🔥 **THIS IS EXACTLY THE HYBRID SYSTEM YOU WANT**  
> Let me break it down:
> 
> ### **Drive = legal / evidence / documents**  
> Frozen. Permanent.  
> Folder numbers matter.  
> This is the thing attorneys and judges can see.
> 
> ### **Wiki = living brain**  
> Summaries, strategy, interpretations.  
> Versioning saves you from ADHD overwrites.  
> You can flip between high-level + detail fast.
> 
> ### **Task List + Finance + Timelogs integrate into the wiki**  
> These don’t belong in Drive at all.
> 
> ---
> 
> # 🔥 So what’s next?  
> Pick one:
> 
> 1. **I create the full README_QiCase_FCFCU.md**  
> 2. **I create the full wiki starter pages populated with your actual facts**  
> 3. **I generate the taskboard system (Today, Next, Queue, Evidence, Comms)**  
> 4. **I build your Drive folder scaffolding as a copy-paste Google Drive import script**  
> 
> Which one do you want first?

### User
> now Zoho has built-in workdrive may be easier kept separate from my projects that I'm constantly having cursor do cleaning and things.

### Assistant
> Yep — **separate it.**  
> Do *not* put QiCase-FCFCU inside the same ecosystem where Cursor is constantly renaming, restructuring, refactoring, indexing, and “cleaning” your app repos and project files.
> 
> You will absolutely nuke your legal archive by accident if you keep it in the same environment where automation scripts live.
> 
> Let me be blunt:
> 
> ### ❌ Mixing litigation records + dev workspace = catastrophic ADHD risk  
> - Cursor refactors folders  
> - Git moves or deletes files  
> - Scripts rewrite or rename things  
> - You lose chain of custody  
> - You lose version integrity  
> - You lose the judge  
> - You lose the case  
> 
> Legal repositories **MUST** be tamper-proof.
> 
> Zoho WorkDrive solves that.
> 
> ---
> 
> # ✅ **Why Zoho WorkDrive is actually *perfect* for QiCase-FCFCU**
> 
> ### 1. **Isolation**  
> It’s not in Git.  
> It’s not in Cursor.  
> It’s not in Finder where you're dragging 7,000 PDFs around.
> 
> It's a vault.
> 
> ### 2. **Built-in versioning**  
> This saves your ass when you overwrite something at 3AM because you “just wanted to fix one thing.”
> 
> ### 3. **Team access ready**  
> If/when you get counsel, you can share:  
> - the wiki  
> - the folder  
> - individual files  
> without handing them your entire personal drive.
> 
> ### 4. **WorkDrive supports multiple “Spaces”**  
> You can keep:
> 
> - **QiCase-FCFCU (Legal Space)**  
> - **QiCase-AES (Legal Space)**  
> separate from  
> - QiAlly business  
> - QiProjects  
> - QiCode  
> - QiOS  
> 
> ### 5. **Zoho Pages → perfect wiki layer**  
> This is exactly what I told you earlier:  
> Wiki = **system of meaning**  
> Drive = **system of record**
> 
> Zoho Pages gives you version history **and** clean navigation.
> 
> ### 6. **Zoho integrates cleanly with your future client portal**  
> QiPortals → can link to WorkDrive or embed wiki pages for controlled access.
> 
> ---
> 
> # 🔥 **So the architecture becomes:**
> 
> ```
> Zoho WorkDrive
> │
> ├── Workspace: QiCases
> │   ├── QiCase-FCFCU/
> │   │   ├── Files (Drive)
> │   │   └── Wiki (Pages)
> │   ├── QiCase-AES/
> │   │   ├── Files
> │   │   └── Wiki
> │   └── (optional future cases)
> │
> └── QiAlly Projects (kept separate)
>     ├── QiSuite
>     ├── QiNote
>     ├── QiPorts
>     ├── Client Work
>     └── All dev repos + Cursor-controlled areas
> ```
> 
> **Legal = airlocked.**  
> **Everything else = modular, automated, and flexible.**
> 
> ---
> 
> # Now let me give you the recommended **Zoho WorkDrive structure** for QiCase-FCFCU.
> 
> ### 📂 **WorkDrive Folder Tree**
> 
> ```text
> QiCase-FCFCU/
> ├── 00_SYSTEM/
> │   ├── README.md
> │   ├── Master_Timeline.xlsx
> │   ├── Contacts.md
> │   ├── Glossary.md
> │   └── Templates/
> │
> ├── 01_Facts_and_Evidence/
> │   ├── Exhibits/
> │   ├── Affidavits/
> │   ├── Photos_Videos/
> │   ├── Communications_Proof/
> │   └── Timeline/
> │
> ├── 02_Research_and_Strategy/
> │   ├── TR60B_Void_Judgment/
> │   ├── Service_of_Process/
> │   ├── Stay_Writ/
> │   ├── ADA_and_Access/
> │   ├── Damages/
> │   └── Notes/
> │
> ├── 10_Phase_01_Void_Judgment/
> ├── 20_Phase_02_Stay_or_Quash_Writ/
> ├── 30_Phase_03_Retrieval_of_Property/
> ├── 40_Phase_04_Damages_and_FollowOn_Claims/
> │   (each with PLAN, Drafts, Filed, Exhibits, Orders, Archive)
> │
> ├── 50_EFiling_and_Service/
> │   ├── Envelopes/
> │   ├── Receipts/
> │   ├── Service_Proof/
> │   └── Checklists/
> │
> ├── 60_Communications/
> │   ├── Court/
> │   ├── Sheriff/
> │   ├── FCFCU/
> │   ├── Attorneys/
> │   └── Third_Parties/
> │
> └── 90_ARCHIVE/
> ```
> 
> ---
> 
> # And here’s the **Zoho Pages Wiki structure**:
> 
> ```text
> Wiki/
> ├── Case Overview
> │   ├── Case Summary
> │   ├── Parties
> │   ├── Key Issues
> │   └── Current Status
> │
> ├── History
> │   ├── Master Chronology
> │   ├── Events Breakdown
> │   ├── Sheriff Day Narrative
> │   └── Notice Failures
> │
> ├── Strategy
> │   ├── TR60(B) Approach
> │   ├── Stay/Quash Plan
> │   ├── Retrieval Plan
> │   ├── Damages Model
> │   └── Risk Map
> │
> ├── Filings
> │   ├── Motions Summary
> │   ├── Proposed Orders
> │   ├── Hearing Notes
> │   └── Clerk Comms
> │
> ├── Reports
> │   ├── Daily Log
> │   ├── Weekly Summary
> │   ├── Case Reports
> │   └── Evidence Review
> │
> ├── Finance
> │   ├── Damages Calculations
> │   ├── Lost Property List
> │   ├── Costs from Eviction
> │   └── Expenses
> │
> └── Tasks & Timelogs
>     ├── Taskboard
>     ├── Urgent Queue
>     ├── Evidence To Pull
>     └── Time Tracking
> ```
> 
> ---
> 
> # **Bottom line:**
> ### **YES — use Zoho WorkDrive + Zoho Pages.  
> Keep legal totally separate from your dev ecosystem.  
> It’s the safest, cleanest, most ADHD-proof way to run a real case.**
> 
> ---
> 
> If you want, I can generate:
> 
> - your **README.md**  
> - your **Wiki homepage**  
> - your **navigation sidebar**  
> - your **taskboard template**  
> - your **filing index template**  
> 
> Which one do you want right now?

### User
> I don't like your folder hierarchy for storage because it shaped like a check list not a intuitive document organization for search, and filings and exhibits.

### Assistant
> Got it. **You want a STORAGE hierarchy that behaves like a *legal archive*, not a project-management checklist.**  
> Right now my structure is organized by *workflow*, and your brain wants it organized by *information retrieval* — which is how actual litigation repositories work.
> 
> Let’s fix it.
> 
> I’m giving you a **true evidence + filings repository** layout that matches how courts, law firms, and e-discovery systems store documents:
> 
> - **Search-first**  
> - **Subject-based**  
> - **Exhibit-driven**  
> - **Flat enough to browse**  
> - **Deep enough to be logical**  
> - **Not dependent on phases or tasks**
> 
> This will feel **natural, intuitive, and ADHD-safe**.
> 
> ---
> 
> # 🚨 **STOP USING “PHASE 01 / PHASE 02” AS THE STORAGE STRUCTURE**  
> That’s for strategy — NOT for files.
> 
> You’re absolutely right:  
> **Phases belong in your Wiki, NOT in your Drive.**
> 
> The **Drive** should store **evidence the way an attorney or judge looks for it:**
> 
> - What type of document is it?  
> - What category of evidence?  
> - What filing is it attached to?  
> - What date?  
> 
> ---
> 
> # ✅ **NEW STORAGE MODEL: COURT-STYLE ARCHIVE**  
> This is the one you *actually want*.
> 
> ```text
> QiCase-FCFCU/
> ├── 00_ADMIN/
> │   ├── README.md
> │   ├── Case_Metadata/
> │   └── Templates/
> │
> ├── 10_FILINGS/
> │   ├── 2025-12-10_Motion_to_Vacate_Void_Judgment/
> │   │   ├── Filed_PDF.pdf
> │   │   ├── Drafts/
> │   │   ├── Proposed_Order.docx
> │   │   └── Exhibits_Submitted/
> │   ├── 2025-12-10_Emergency_Stay_Writ/
> │   ├── 2025-12-??_Future_Filing/
> │   └── Index_of_Filings.md
> │
> ├── 20_EXHIBITS/
> │   ├── EX-A_Sheriff_Return_03-05.pdf
> │   ├── EX-B_Sheriff_Return_04-15.pdf
> │   ├── EX-C_No_Service_Proof.pdf
> │   ├── EX-D_Debit_Card_Replacement_Proof.pdf
> │   ├── EX-E_Property_Removal_Photos/
> │   ├── EX-F_Affidavit_No_Notice.pdf
> │   └── Exhibit_Index.md
> │
> ├── 30_EVIDENCE/
> │   ├── Notices_or_Lack_Thereof/
> │   ├── Sheriff_Actions/
> │   ├── Bank_Communications/
> │   ├── Photos_Video/
> │   ├── Personal_Property_Loss/
> │   ├── Credit_Report_Timeline/
> │   ├── Medical_ADA_Context/
> │   └── Misc/
> │
> ├── 40_COMMUNICATIONS/
> │   ├── To_Court/
> │   ├── To_Sheriff/
> │   ├── To_FCFCU/
> │   ├── To_Attorneys/
> │   └── To_Third_Parties/
> │
> ├── 50_RECORDS/
> │   ├── Court_Docket/
> │   ├── Orders/
> │   ├── Sheriff_Deeds_Writs/
> │   ├── Mortgage_History/
> │   └── Credit_History/
> │
> └── 90_ARCHIVE/
> ```
> 
> ---
> 
> # 🔥 WHY THIS WORKS (AND WHY THE OTHER DIDN’t FOR YOU)
> 
> ### ✔ **1. Filings are grouped by filing**  
> Not phases.  
> Not tasks.  
> Not drafts floating around.  
> This is how lawyers retrieve documents:
> 
> > “Show me the Motion to Vacate file.”
> 
> ### ✔ **2. Exhibits live in ONE home**  
> Not hidden inside phases.  
> Not duplicated.  
> Not scattered.  
> One master exhibit vault.
> 
> ### ✔ **3. Evidence is subject-based**  
> So you can find something instantly by thinking “sheriff” or “notice” or “bank.”
> 
> ### ✔ **4. Records is your official document set**  
> Court docket  
> Orders  
> Sheriff’s deeds  
> Mortgage history  
> Credit history
> 
> Everything official → one place.
> 
> ### ✔ **5. Communications are cleanly separate**  
> No more hunting through filing folders to find an email.
> 
> ### ✔ **6. AGAIN: Phases belong ONLY in your wiki, NOT in Drive.**  
> Your wiki holds:
> 
> - strategy  
> - plans  
> - summaries  
> - case narrative  
> - filing status  
> - what’s next  
> 
> Your drive holds:
> 
> - evidence  
> - filings  
> - exhibits  
> - records  
> - communications  
> 
> ---
> 
> # 🔥 THIS IS HOW YOUR BRAIN WILL SEARCH:  
> ### “Where’s the sheriff bodycam?”  
> → `/30_EVIDENCE/Sheriff_Actions/`
> 
> ### “Where is EX-D?”  
> → `/20_EXHIBITS/EX-D_*`
> 
> ### “Where’s my filed Motion to Vacate?”  
> → `/10_FILINGS/2025-12-10_Motion_to_Vacate_Void_Judgment/Filed_PDF.pdf`
> 
> ### “Where’s the credit report that correlates the delinquency timeline?”  
> → `/30_EVIDENCE/Credit_Report_Timeline/`
> 
> ### “Where are all the clerk emails?”  
> → `/40_COMMUNICATIONS/To_Court/`
> 
> ### “Where’s the docket?”  
> → `/50_RECORDS/Court_Docket/`
> 
> This is **intuitive storage** — not a checklist.
> 
> ---
> 
> # 🔥 WANT TO SEE IT WITH YOUR REAL FILES INSERTED?  
> If you say yes:
> 
> I’ll take the PDFs, letters, exhibits, motions, and images you’ve uploaded and map them *exactly* into this structure so you have a ready-to-create folder tree with your real evidence already placed where it belongs.
> 
> Just tell me:
> 
> **“Gina, populate it with my documents.”**

### User
> I already moved everything over that we have Created so far, can you give me the updated wiki

### Assistant
> Perfect — since you’ve already moved the Drive folders, I’ll give you the **updated Wiki structure** that matches the NEW archive-style hierarchy you preferred.
> 
> This wiki is **search-first, narrative-first, and cross-references your Drive**, but does NOT mirror Drive’s folders.  
> Think of Drive as *evidence* and the Wiki as *your brain / your casebook / your control panel.*
> 
> Here is the fully updated **QiCase-FCFCU Wiki**:
> 
> ---
> 
> # 🧠 **QiCase-FCFCU — WIKI (MASTER STRUCTURE)**  
> **This is your ONLY “thinking space.”**  
> Everything here has versioning.  
> Nothing here is an official document — it interprets, summarizes, or tracks the official ones stored in Drive.
> 
> ---
> 
> # =========================  
> # **WIKI ROOT (Home Page)**  
> # =========================  
> 
> ## **QiCase-FCFCU: Case Control Center**
> - High-level case summary  
> - Quick links to:
>   - Filings Index  
>   - Evidence Index  
>   - Exhibits  
>   - Timeline  
>   - Tasks  
>   - Reports  
>   - Damages Model  
> - Current status  
> - Upcoming deadlines  
> - Important alerts  
> 
> ---
> 
> # =========================  
> # **1. CASE OVERVIEW**  
> # =========================  
> 
> ### **/Case_Overview/Summary.md**  
> - What the case is  
> - What happened  
> - What FCFCU did wrong  
> - What the sheriff did wrong  
> - Why the judgment is void  
> - Why the writ execution was improper  
> - What relief you’re seeking  
> 
> ### **/Case_Overview/Parties.md**  
> - FCFCU  
> - Their attorney(s)  
> - Sheriff Dept  
> - You  
> - Anyone else involved  
> 
> ### **/Case_Overview/Key_Issues.md**  
> - Failure of service  
> - Void judgment  
> - Improper writ execution  
> - Lack of notice  
> - Property removal  
> - ADA access / disability context  
> 
> ### **/Case_Overview/Status.md**  
> - Filed motions  
> - Pending motions  
> - What’s next  
> 
> ---
> 
> # =========================  
> # **2. CASE HISTORY**  
> # =========================  
> 
> ### **/Case_History/Chronology.md**  
> - Master event timeline  
> - Each event links to underlying evidence in Drive  
> 
> ### **/Case_History/Notice_Failures.md**  
> - Detailed log of every point where FCFCU failed to notify you  
> - Debit card replacement evidence  
> - Returned mail (if any)  
> - Address history  
> - Why service never reached you  
> 
> ### **/Case_History/Sheriff_Event.md**  
> - Full narrative of the day you were removed  
> - Notes about conduct  
> - Property access denied  
> - Gun drawn moment  
> - Lost/damage property timeline  
> 
> ### **/Case_History/Damages_History.md**  
> - How the case caused:  
>   - homelessness  
>   - car usage costs  
>   - pet safety issues  
>   - expenses  
>   - emotional harm (kept separate from filings but tracked internally)  
> 
> ---
> 
> # =========================  
> # **3. EVIDENCE INDEX**  
> # =========================  
> 
> ### **/Evidence/Index.md**  
> THIS IS THE MASTER MAP.  
> It links to all Drive folders:
> 
> - Exhibits  
> - Evidence bundles  
> - Photos/videos  
> - Communications  
> - Docket  
> - Records  
> 
> ### **/Evidence/Service_Failure.md**  
> Summary + links:  
> - Sheriff returns  
> - Blank returns  
> - No-posting evidence  
> - Neighbor footage (if obtained)  
> - Debit card renewal  
> 
> ### **/Evidence/Sheriff_Actions.md**  
> - Everything that proves improper execution  
> - Property denial  
> - Conduct notes  
> - Witness statements (if any)
> 
> ### **/Evidence/Property_Loss.md**  
> - Photos  
> - Item list  
> - Value  
> - Links to Drive  
> 
> ### **/Evidence/Credit_Timeline.md**  
> - When delinquencies started  
> - How this supports improper notice  
> 
> ---
> 
> # =========================  
> # **4. FILINGS & ORDERS**  
> # =========================  
> 
> ### **/Filings/Index.md**  
> - Each filing listed with date + summary  
> - Links to Drive locations
> 
> Example:
> ```
> 2025-12-10 — Motion to Vacate Void Judgment (TR60(B))
> 2025-12-10 — Emergency Motion to Stay/Quash Writ
> Future — Supplemental Affidavit of Service Failures
> Future — Motion for Return of Property
> ```
> 
> ### **/Filings/Motions.md**  
> - Narrative descriptions  
> - Strategy behind each  
> 
> ### **/Filings/Orders_and_Hearings.md**  
> - Notes on what the judge says  
> - What needs to happen afterward  
> 
> ---
> 
> # =========================  
> # **5. STRATEGY BOOK**  
> # =========================  
> 
> ### **/Strategy/Master_Strategy.md**  
> A one-page control plan:
> - Objective 1 = Vacate judgment  
> - Objective 2 = Undo/Stay writ  
> - Objective 3 = Recover property + damages  
> - Objective 4 = Build civil claim  
> 
> ### **/Strategy/TR60B.md**  
> - Legal theory  
> - Why judgment is void  
> - Evidence list  
> - Case law  
> 
> ### **/Strategy/Stay_Writ.md**  
> - Argument structure  
> - What the sheriff did wrong  
> - Why writ execution violated rights  
> 
> ### **/Strategy/Property_Retrieval.md**  
> - Steps  
> - Notices  
> - Communications  
> - Attachments  
> 
> ### **/Strategy/Damages_Model.md**  
> - Hard expenses  
> - Soft damages  
> - Property valuation  
> - Lost use  
> - Homelessness costs  
> - Dog care costs  
> - Car costs  
> - Future recovery  
> 
> ---
> 
> # =========================  
> # **6. TASKS**  
> # =========================  
> 
> ### **/Tasks/Taskboard.md**  
> Columns:
> - Critical  
> - Filing Queue  
> - Evidence to Pull  
> - Communications to Send  
> - Waiting On  
> - Completed  
> 
> ### **/Tasks/Today.md**  
> Ultra-simple ADHD-safe daily list.
> 
> ### **/Tasks/Filing_Queue.md**  
> Shows upcoming motions with priority.
> 
> ### **/Tasks/Evidence_To_Pull.md**  
> Self-explanatory.
> 
> ---
> 
> # =========================  
> # **7. REPORTS**  
> # =========================  
> 
> ### **/Reports/Daily_Log.md**  
> Short entries.  
> This helps later with affidavits.
> 
> ### **/Reports/Weekly_Summary.md**  
> One per week.  
> What moved, what didn’t.
> 
> ### **/Reports/Evidence_Audit.md**  
> Tracks which evidence is missing.
> 
> ### **/Reports/Case_Report.md**  
> A “client-style” summary for attorneys.
> 
> ---
> 
> # =========================  
> # **8. FINANCE TRACKING**  
> # =========================  
> 
> ### **/Finance/Expenses.md**  
> - Hotels  
> - Food  
> - Charging the car  
> - Lost wages  
> - Animal care  
> - Anything directly tied to the removal  
> 
> ### **/Finance/Damages_Valuation.md**  
> Good for civil claims.
> 
> ### **/Finance/Mileage.md**  
> Lyft usage, travel for court, etc.
> 
> ---
> 
> # =========================  
> # **9. TIMELOGS**  
> # =========================  
> 
> ### **/Timelogs/Master_Log.md**  
> - Everything you’ve done  
> - Helps show effort + timeline of harm
> 
> ### **/Timelogs/2025-Dec.md**  
> Rolling monthly logs.
> 
> ---
> 
> # =========================  
> # **10. CROSSWALK PAGE (Important)**  
> # =========================  
> 
> ### **/Crosswalk/Drive_Map.md**
> A page that maps:
> 
> **Wiki Page → Corresponding Drive Folders**
> 
> Example:
> ```
> Case_History/Chronology → /30_EVIDENCE/Chronology/
> Filings Index → /10_FILINGS/
> Evidence Index → /20_EXHIBITS/
> Sheriff Event → /30_EVIDENCE/Sheriff_Actions/
> ```
> 
> This makes the entire system intuitive.
> 
> ---
> 
> # ⭐ **IF YOU APPROVE THIS STRUCTURE:**  
> I’ll generate:
> 
> - The **Wiki homepage with links**,  
> - All **starter page templates**,  
> - AND a fully formatted left-side navigation tree like Zoho Pages uses.
> 
> Just say:
> 
> **“Gina, generate the wiki pages.”**

### User
> girl give me these files in html elegant and minimalist but something nice to look at with minimal styling cause the wiki will strip most css and sytling anyway.

### Assistant
> Say less 😏  
> Here’s a clean set of **HTML templates** for your wiki pages — elegant, minimalist, and mostly just structure so Zoho/whatever wiki doesn’t choke on styling.
> 
> I’ll give you **separate files** with suggested filenames in comments.  
> You can paste each into its own page.
> 
> ---
> 
> ```html
> <!-- 01_home_qicase-fcfcu.html -->
> <!DOCTYPE html>
> <html lang="en">
> <head>
>   <meta charset="UTF-8">
>   <title>QiCase-FCFCU · Case Control Center</title>
> </head>
> <body>
>   <h1>QiCase-FCFCU · Case Control Center</h1>
>   <p><em>Central dashboard for the FCFCU foreclosure / sheriff / rights-violation case.</em></p>
> 
>   <h2>Quick Links</h2>
>   <ul>
>     <li><a href="#case-overview">Case Overview</a></li>
>     <li><a href="#case-history">Case History</a></li>
>     <li><a href="#evidence-index">Evidence Index</a></li>
>     <li><a href="#filings-index">Filings &amp; Orders</a></li>
>     <li><a href="#strategy">Strategy</a></li>
>     <li><a href="#tasks">Tasks</a></li>
>     <li><a href="#reports">Reports</a></li>
>     <li><a href="#finance">Finance &amp; Damages</a></li>
>     <li><a href="#timelogs">Timelogs</a></li>
>     <li><a href="#crosswalk">Drive Crosswalk</a></li>
>   </ul>
> 
>   <h2 id="case-overview">Case Overview</h2>
>   <p>Short summary of what this case is about, who is involved, and what you are asking the court to do.</p>
>   <ul>
>     <li>Defendant / Plaintiff structure</li>
>     <li>Core issues (service, void judgment, sheriff execution, property loss, ADA context)</li>
>     <li>Current overall posture (e.g., “Motions filed, awaiting hearing”)</li>
>   </ul>
> 
>   <h2 id="case-history">Case History</h2>
>   <p>High-level chronological story: foreclosure, judgment, writ, sheriff action, homelessness, ongoing harm.</p>
> 
>   <h2 id="evidence-index">Evidence Index</h2>
>   <p>Link to the main Evidence Index page and to the Exhibits listing.</p>
> 
>   <h2 id="filings-index">Filings &amp; Orders</h2>
>   <p>Link to the Filings Index and Orders/Hearings notes.</p>
> 
>   <h2 id="strategy">Strategy Snapshot</h2>
>   <ul>
>     <li>Objective 1: Vacate void judgment.</li>
>     <li>Objective 2: Stay / undo writ execution.</li>
>     <li>Objective 3: Recover property and document damages.</li>
>     <li>Objective 4: Build record for future civil claims.</li>
>   </ul>
> 
>   <h2 id="tasks">Tasks (Today / Next)</h2>
>   <p>Pointer to the live Taskboard and Today page.</p>
> 
>   <h2 id="reports">Reports</h2>
>   <p>Pointer to Daily Log, Weekly Summary, and Case Reports.</p>
> 
>   <h2 id="finance">Finance &amp; Damages</h2>
>   <p>Pointer to expenses tracking and damages model.</p>
> 
>   <h2 id="timelogs">Timelogs</h2>
>   <p>Pointer to master timelog and monthly breakdowns.</p>
> 
>   <h2 id="crosswalk">Drive Crosswalk</h2>
>   <p>Pointer to the page that maps wiki pages to WorkDrive folders.</p>
> </body>
> </html>
> ```
> 
> ---
> 
> ```html
> <!-- 02_case_overview_summary.html -->
> <!DOCTYPE html>
> <html lang="en">
> <head>
>   <meta charset="UTF-8">
>   <title>Case Overview · Summary</title>
> </head>
> <body>
>   <h1>Case Overview · Summary</h1>
>   <p><em>Plain-language summary of the FCFCU case.</em></p>
> 
>   <h2>1. What This Case Is About</h2>
>   <p>[One–three short paragraphs describing the foreclosure, the judgment, the writ, and the sheriff action.]</p>
> 
>   <h2>2. Core Legal Issues</h2>
>   <ul>
>     <li><strong>Failure of service:</strong> No proper notice before judgment.</li>
>     <li><strong>Void judgment:</strong> Judgment obtained without valid service.</li>
>     <li><strong>Improper writ execution:</strong> Sheriff execution without lawful foundation and without proper notice.</li>
>     <li><strong>Property loss and access:</strong> Loss/denial of access to personal property.</li>
>     <li><strong>Disability / ADA context:</strong> Barriers to participation in proceedings and communications.</li>
>   </ul>
> 
>   <h2>3. Parties</h2>
>   <ul>
>     <li><strong>Plaintiff / Creditor:</strong> [FCFCU full legal name]</li>
>     <li><strong>Defendant / Homeowner:</strong> Cody Rice-Velasquez</li>
>     <li><strong>Sheriff / Enforcement:</strong> [County Sheriff / Civil Process Unit]</li>
>     <li><strong>Court:</strong> [Court name, cause number]</li>
>   </ul>
> 
>   <h2>4. Relief / Outcomes Sought</h2>
>   <ul>
>     <li>Vacate the foreclosure judgment as void.</li>
>     <li>Stay, quash, or otherwise undo any writ-based enforcement already executed.</li>
>     <li>Secure access to, or compensation for, personal property.</li>
>     <li>Establish a clear record of rights violations and resulting damages.</li>
>   </ul>
> 
>   <h2>5. Current Status</h2>
>   <p>[Briefly describe what has been filed and what is pending.]</p>
> </body>
> </html>
> ```
> 
> ---
> 
> ```html
> <!-- 03_case_history_chronology.html -->
> <!DOCTYPE html>
> <html lang="en">
> <head>
>   <meta charset="UTF-8">
>   <title>Case History · Chronology</title>
> </head>
> <body>
>   <h1>Case History · Chronology</h1>
>   <p><em>Timeline of major events, tied back to evidence and filings.</em></p>
> 
>   <h2>How to Use This Page</h2>
>   <p>Each entry should be short, factual, and (if possible) reference a document, exhibit, or filing stored in WorkDrive.</p>
> 
>   <h2>Timeline</h2>
>   <table>
>     <thead>
>       <tr>
>         <th>Date</th>
>         <th>Event</th>
>         <th>Evidence / Link</th>
>         <th>Notes</th>
>       </tr>
>     </thead>
>     <tbody>
>       <tr>
>         <td>[YYYY-MM-DD]</td>
>         <td>[Event description]</td>
>         <td>[EX-? or WorkDrive path]</td>
>         <td>[Short context]</td>
>       </tr>
>       <!-- Add more rows as needed -->
>     </tbody>
>   </table>
> </body>
> </html>
> ```
> 
> ---
> 
> ```html
> <!-- 04_evidence_index.html -->
> <!DOCTYPE html>
> <html lang="en">
> <head>
>   <meta charset="UTF-8">
>   <title>Evidence Index</title>
> </head>
> <body>
>   <h1>Evidence Index</h1>
>   <p><em>Master map of evidence categories and key items.</em></p>
> 
>   <h2>1. Exhibits</h2>
>   <p>Formal exhibits used or planned for filings.</p>
>   <ul>
>     <li>EX-A · [Title] — [Short description] — [WorkDrive path or ID]</li>
>     <li>EX-B · [Title] — [Short description]</li>
>     <li>EX-C · [Title] — [Short description]</li>
>   </ul>
> 
>   <h2>2. Service / Notice Evidence</h2>
>   <ul>
>     <li>Sheriff returns (file / no file / blank).</li>
>     <li>Mailing records or their absence.</li>
>     <li>Debit card replacement timelines and bank contact proof.</li>
>   </ul>
> 
>   <h2>3. Sheriff Actions &amp; Removal Event</h2>
>   <ul>
>     <li>Photos / videos of the day of removal.</li>
>     <li>Notes on gun drawn / room checks / refusal to allow property retrieval.</li>
>     <li>Any bodycam / incident reports, if available.</li>
>   </ul>
> 
>   <h2>4. Property Loss &amp; Damage</h2>
>   <ul>
>     <li>Inventory of items left in the home.</li>
>     <li>Estimated values and receipts if available.</li>
>     <li>Evidence of property condition before removal.</li>
>   </ul>
> 
>   <h2>5. Credit &amp; Financial Impact</h2>
>   <ul>
>     <li>Credit reports showing delinquency and foreclosure reporting.</li>
>     <li>Statements showing overlapping financial stressors.</li>
>   </ul>
> 
>   <h2>6. Disability / ADA Context</h2>
>   <ul>
>     <li>Records that explain ADHD/anxiety and barriers to participation.</li>
>     <li>Any prior accommodation requests or similar documentation.</li>
>   </ul>
> </body>
> </html>
> ```
> 
> ---
> 
> ```html
> <!-- 05_filings_index.html -->
> <!DOCTYPE html>
> <html lang="en">
> <head>
>   <meta charset="UTF-8">
>   <title>Filings &amp; Orders Index</title>
> </head>
> <body>
>   <h1>Filings &amp; Orders Index</h1>
>   <p><em>Single place to see what has been filed, when, and why.</em></p>
> 
>   <h2>Filed Motions</h2>
>   <table>
>     <thead>
>       <tr>
>         <th>Date Filed</th>
>         <th>Title</th>
>         <th>Purpose / Summary</th>
>         <th>WorkDrive Location</th>
>         <th>Status</th>
>       </tr>
>     </thead>
>     <tbody>
>       <tr>
>         <td>[2025-12-10]</td>
>         <td>Motion to Vacate Void Judgment (TR60(B))</td>
>         <td>[Short reason: lack of service, judgment void, etc.]</td>
>         <td>[Link or path]</td>
>         <td>[Pending / Ruled / Needs follow-up]</td>
>       </tr>
>       <tr>
>         <td>[2025-12-10]</td>
>         <td>Emergency Motion to Stay / Quash Writ</td>
>         <td>[Short reason: protect from unlawful enforcement and continued harm.]</td>
>         <td>[Link or path]</td>
>         <td>[Pending / Ruled]</td>
>       </tr>
>     </tbody>
>   </table>
> 
>   <h2>Orders &amp; Hearings</h2>
>   <table>
>     <thead>
>       <tr>
>         <th>Date</th>
>         <th>Order / Hearing</th>
>         <th>Outcome / Notes</th>
>         <th>Next Steps</th>
>       </tr>
>     </thead>
>     <tbody>
>       <tr>
>         <td>[YYYY-MM-DD]</td>
>         <td>[Order or hearing description]</td>
>         <td>[What the court said or did]</td>
>         <td>[What you must do or watch for next]</td>
>       </tr>
>     </tbody>
>   </table>
> </body>
> </html>
> ```
> 
> ---
> 
> ```html
> <!-- 06_strategy_master.html -->
> <!DOCTYPE html>
> <html lang="en">
> <head>
>   <meta charset="UTF-8">
>   <title>Master Strategy</title>
> </head>
> <body>
>   <h1>Master Strategy</h1>
>   <p><em>High-level plan for how this case is being handled.</em></p>
> 
>   <h2>1. Core Objectives</h2>
>   <ol>
>     <li>Vacate the foreclosure judgment as void for lack of proper service.</li>
>     <li>Stay, quash, or reverse sheriff enforcement actions taken under the writ.</li>
>     <li>Document and seek remedies for property loss and related damages.</li>
>     <li>Build a clean record that supports any future civil rights or tort claims.</li>
>   </ol>
> 
>   <h2>2. Strategy Pillars</h2>
>   <h3>2.1 Service &amp; Void Judgment</h3>
>   <p>[Outline the key evidence and arguments.]</p>
> 
>   <h3>2.2 Writ &amp; Sheriff Execution</h3>
>   <p>[Outline what went wrong, and why it matters legally.]</p>
> 
>   <h3>2.3 Property &amp; Damages</h3>
>   <p>[Outline how you are documenting and valuing the harm.]</p>
> 
>   <h3>2.4 Disability / ADA Context</h3>
>   <p>[Explain how your conditions affected your ability to participate in the process and why that matters.]</p>
> 
>   <h2>3. Short-Term Priorities</h2>
>   <ul>
>     <li>[Example] Ensure all current motions are properly filed and served.</li>
>     <li>[Example] Confirm upcoming hearings and deadlines.</li>
>     <li>[Example] Complete initial property loss inventory.</li>
>   </ul>
> 
>   <h2>4. Medium-Term Priorities</h2>
>   <ul>
>     <li>Supplement evidence of service failures.</li>
>     <li>Clarify record on sheriff conduct and property access.</li>
>     <li>Refine damages model for potential future negotiations or claims.</li>
>   </ul>
> </body>
> </html>
> ```
> 
> ---
> 
> ```html
> <!-- 07_tasks_taskboard.html -->
> <!DOCTYPE html>
> <html lang="en">
> <head>
>   <meta charset="UTF-8">
>   <title>Taskboard</title>
> </head>
> <body>
>   <h1>Taskboard · QiCase-FCFCU</h1>
>   <p><em>Simple text-based board to keep work visible and finite.</em></p>
> 
>   <h2>Critical (Now / Today)</h2>
>   <ul>
>     <li>[ ] Confirm next court date with clerk.</li>
>     <li>[ ] Save file-stamped copies of all recently filed motions into WorkDrive.</li>
>     <li>[ ] Note any deadlines mentioned in court / orders.</li>
>   </ul>
> 
>   <h2>Filing Queue</h2>
>   <ul>
>     <li>[ ] Draft supplemental affidavit on lack of service.</li>
>     <li>[ ] Draft detailed property loss statement.</li>
>     <li>[ ] Plan any additional motion(s) based on court response.</li>
>   </ul>
> 
>   <h2>Evidence To Pull</h2>
>   <ul>
>     <li>[ ] Locate documents showing active debit card &amp; mailing relationship with FCFCU.</li>
>     <li>[ ] Collect screenshots / statements showing credit reporting timeline.</li>
>     <li>[ ] Organize photos / notes from the day of sheriff removal.</li>
>   </ul>
> 
>   <h2>Communications To Send</h2>
>   <ul>
>     <li>[ ] Clerk email to confirm filings received / docketed correctly.</li>
>     <li>[ ] Sheriff or department communication regarding property inventory / access.</li>
>     <li>[ ] Any communication to FCFCU or their counsel, if appropriate.</li>
>   </ul>
> 
>   <h2>Waiting On</h2>
>   <ul>
>     <li>[ ] Court ruling on Motion to Vacate Void Judgment.</li>
>     <li>[ ] Court ruling on Emergency Stay / Quash Writ.</li>
>   </ul>
> 
>   <h2>Completed</h2>
>   <p>Move items here with date when they’re done.</p>
>   <ul>
>     <li>[ ] [YYYY-MM-DD] Example completed item.</li>
>   </ul>
> </body>
> </html>
> ```
> 
> ---
> 
> ```html
> <!-- 08_reports_daily_log.html -->
> <!DOCTYPE html>
> <html lang="en">
> <head>
>   <meta charset="UTF-8">
>   <title>Daily Log</title>
> </head>
> <body>
>   <h1>Daily Log</h1>
>   <p><em>Short, factual entries about what happened and what you did for the case each day.</em></p>
> 
>   <h2>How to Use</h2>
>   <p>Each entry: date, what happened, what you did, and any follow-up needed.</p>
> 
>   <h2>Entries</h2>
>   <h3>[YYYY-MM-DD]</h3>
>   <ul>
>     <li><strong>Events:</strong> [What happened related to the case.]</li>
>     <li><strong>Actions taken:</strong> [What you filed, called, moved, documented.]</li>
>     <li><strong>Feelings (optional, short):</strong> [One line max, if you want to track it.]</li>
>     <li><strong>Next steps:</strong> [Tasks generated by this day.]</li>
>   </ul>
> 
>   <h3>[YYYY-MM-DD]</h3>
>   <ul>
>     <li><strong>Events:</strong> …</li>
>     <li><strong>Actions taken:</strong> …</li>
>     <li><strong>Next steps:</strong> …</li>
>   </ul>
> </body>
> </html>
> ```
> 
> ---
> 
> ```html
> <!-- 09_finance_damages_model.html -->
> <!DOCTYPE html>
> <html lang="en">
> <head>
>   <meta charset="UTF-8">
>   <title>Finance &amp; Damages Model</title>
> </head>
> <body>
>   <h1>Finance &amp; Damages Model</h1>
>   <p><em>Working model of tangible costs and losses resulting from the case events.</em></p>
> 
>   <h2>1. Hard Expenses</h2>
>   <table>
>     <thead>
>       <tr>
>         <th>Date</th>
>         <th>Category</th>
>         <th>Description</th>
>         <th>Amount</th>
>         <th>Evidence / Link</th>
>       </tr>
>     </thead>
>     <tbody>
>       <tr>
>         <td>[YYYY-MM-DD]</td>
>         <td>Hotel</td>
>         <td>[Why you had to stay there]</td>
>         <td>[$0.00]</td>
>         <td>[Receipt / WorkDrive path]</td>
>       </tr>
>     </tbody>
>   </table>
> 
>   <h2>2. Property Loss</h2>
>   <table>
>     <thead>
>       <tr>
>         <th>Item</th>
>         <th>Estimated Value</th>
>         <th>Basis (receipt, estimate, etc.)</th>
>         <th>Evidence</th>
>       </tr>
>     </thead>
>     <tbody>
>       <tr>
>         <td>[Item name]</td>
>         <td>[$0.00]</td>
>         <td>[How you got the value]</td>
>         <td>[Photo, receipt, etc.]</td>
>       </tr>
>     </tbody>
>   </table>
> 
>   <h2>3. Ongoing Costs</h2>
>   <ul>
>     <li>Extra driving / charging costs.</li>
>     <li>Pet-related expenses linked to homelessness / instability.</li>
>     <li>Other recurring costs caused by not having housing.</li>
>   </ul>
> 
>   <h2>4. Summary</h2>
>   <p>[Short paragraph summarizing the scale of harm in simple, factual language.]</p>
> </body>
> </html>
> ```
> 
> ---
> 
> ```html
> <!-- 10_timelogs_master.html -->
> <!DOCTYPE html>
> <html lang="en">
> <head>
>   <meta charset="UTF-8">
>   <title>Master Timelog</title>
> </head>
> <body>
>   <h1>Master Timelog</h1>
>   <p><em>Tracks the time and effort you are putting into managing this case.</em></p>
> 
>   <h2>How to Use</h2>
>   <p>Log blocks of time spent on filings, evidence, calls, and admin. This can matter later if you need to show burden.</p>
> 
>   <h2>Entries</h2>
>   <table>
>     <thead>
>       <tr>
>         <th>Date</th>
>         <th>Time Spent</th>
>         <th>Activity</th>
>         <th>Area</th>
>         <th>Notes</th>
>       </tr>
>     </thead>
>     <tbody>
>       <tr>
>         <td>[YYYY-MM-DD]</td>
>         <td>[e.g., 1.5 hours]</td>
>         <td>[Drafted motion / organized evidence / called clerk]</td>
>         <td>[Filings / Evidence / Comms / Planning]</td>
>         <td>[Anything notable]</td>
>       </tr>
>     </tbody>
>   </table>
> </body>
> </html>
> ```
> 
> ---
> 
> ```html
> <!-- 11_crosswalk_drive_map.html -->
> <!DOCTYPE html>
> <html lang="en">
> <head>
>   <meta charset="UTF-8">
>   <title>Drive Crosswalk</title>
> </head>
> <body>
>   <h1>Drive Crosswalk · Wiki ↔ WorkDrive</h1>
>   <p><em>Map between wiki pages and your WorkDrive folders so you don’t have to think about it twice.</em></p>
> 
>   <h2>Case Overview</h2>
>   <ul>
>     <li><strong>Summary page:</strong> this wiki page</li>
>     <li><strong>Related Drive folders:</strong> <code>/50_RECORDS/Court_Docket/</code>, <code>/50_RECORDS/Mortgage_History/</code></li>
>   </ul>
> 
>   <h2>Case History</h2>
>   <ul>
>     <li><strong>Chronology:</strong> wiki <em>Case History · Chronology</em> → Drive <code>/30_EVIDENCE/</code> (timeline-related docs).</li>
>     <li><strong>Sheriff Event:</strong> wiki <em>Sheriff_Event</em> → Drive <code>/30_EVIDENCE/Sheriff_Actions/</code> and <code>/20_EXHIBITS/EX-*</code> where applicable.</li>
>   </ul>
> 
>   <h2>Evidence</h2>
>   <ul>
>     <li><strong>Evidence Index:</strong> wiki <em>Evidence Index</em> → Drive <code>/20_EXHIBITS/</code> and <code>/30_EVIDENCE/</code>.</li>
>     <li><strong>Service / Notice:</strong> wiki <em>Service_Failure</em> → Drive <code>/30_EVIDENCE/Notices_or_Lack_Thereof/</code>.</li>
>   </ul>
> 
>   <h2>Filings</h2>
>   <ul>
>     <li><strong>Filings Index:</strong> wiki <em>Filings &amp; Orders Index</em> → Drive <code>/10_FILINGS/</code>.</li>
>     <li><strong>Orders &amp; Hearings:</strong> wiki <em>Orders_and_Hearings</em> → Drive <code>/50_RECORDS/Orders/</code>.</li>
>   </ul>
> 
>   <h2>Communications</h2>
>   <ul>
>     <li><strong>Court communications:</strong> wiki notes → Drive <code>/40_COMMUNICATIONS/To_Court/</code>.</li>
>     <li><strong>Sheriff communications:</strong> wiki notes → Drive <code>/40_COMMUNICATIONS/To_Sheriff/</code>.</li>
>     <li><strong>FCFCU communications:</strong> wiki notes → Drive <code>/40_COMMUNICATIONS/To_FCFCU/</code>.</li>
>   </ul>
> 
>   <h2>Finance / Damages</h2>
>   <ul>
>     <li><strong>Finance &amp; Damages Model:</strong> wiki → Drive <code>/50_RECORDS/</code> or a dedicated <code>/30_EVIDENCE/Financial_Impact/</code> folder if you create one.</li>
>   </ul>
> </body>
> </html>
> ```
> 
> ---
> 
> If you want, next pass we can:
> 
> - tune these to match **Zoho Pages internal link syntax**,  
> - or add a tiny, safe `<style>` block for typography if the wiki doesn’t strip it.

### User
> Can you summarize this? Give me my case summary, case log summary, and then let me know if there's any artifacts or anything in here that we need to preserve.

### Assistant
> Understood. I’m going to give you **three things**, clean and usable:
> 
> 1. **Case Summary (executive / narrative)**  
> 2. **Formal CASE LOG ENTRY** (using your required template)  
> 3. **Artifacts to Preserve** (very important)
> 
> No fluff. No hype. Just what matters.
> 
> ---
> 
> ## 1. CASE SUMMARY (EXECUTIVE)
> 
> **Case Name:** QiCase-FCFCU  
> **Core Issue:** Foreclosure judgment and writ enforcement executed without valid service or meaningful notice, resulting in unlawful displacement, loss of property access, and cascading harm.
> 
> **Summary:**
> This case centers on a foreclosure action initiated by Financial Center First Credit Union (FCFCU) that resulted in a default judgment and subsequent execution of a writ by the sheriff. The judgment is challenged as **void** due to failure of proper service and lack of notice. Despite no demonstrated service, the writ was executed, leading to forced removal from the property, denial of access to personal belongings, and immediate homelessness.
> 
> The situation was compounded by documented disability-related communication barriers (ADHD, anxiety), making phone-based processes unsafe and unreliable, and by the absence of reasonable accommodations. The sheriff’s conduct during execution raised additional concerns, including coercive entry, denial of retrieval of personal property, and escalation that caused fear and distress.
> 
> In parallel, displacement triggered downstream harms including loss of utilities continuity, financial instability, pet safety risks, hotel expenses, and credit reporting consequences. These impacts are being documented separately but are causally linked to the foreclosure enforcement.
> 
> **Current posture:**
> - Motions have been filed (or prepared) to vacate the judgment as void and to stay or quash the writ.
> - Evidence has been organized into a formal, court-style archive.
> - A hybrid system is now in place:
>   - **Zoho WorkDrive** as the immutable evidence and filings vault.
>   - **Wiki (Pages)** as the living casebook for history, strategy, summaries, tasks, and reports.
> 
> **Primary objectives:**
> 1. Vacate the foreclosure judgment as void for lack of service.
> 2. Halt or undo enforcement actions taken under that void judgment.
> 3. Secure access to, or compensation for, personal property.
> 4. Preserve a clean evidentiary record for damages and potential follow-on claims.
> 
> ---
> 
> ## 2. FORMAL CASE LOG ENTRY
> 
> ============================================================
> CASE LOG ENTRY  
> DATE: 2025-12-15  
> TIME RANGE: Afternoon–Evening  
> ENTRY TYPE: Project Structuring + Case Documentation + Systems Architecture  
> 
> RELATED FILES:  
> Zoho WorkDrive → QiCase-FCFCU (Filings, Exhibits, Evidence, Records)  
> Zoho Pages → QiCase-FCFCU Wiki  
> 
> SUMMARY:  
> Conversation focused on formalizing QiCase-FCFCU as a standalone legal project, separate from AES and from development repositories. A hybrid documentation system was finalized: WorkDrive as the authoritative record for filings and evidence, and a wiki as a versioned casebook for summaries, history, strategy, tasks, finance, and logs. The storage hierarchy was redesigned away from checklist-style “phases” and toward a court-style archive organized by filings, exhibits, evidence categories, communications, and records. Minimalist HTML templates were generated for all major wiki pages to ensure compatibility with wiki platforms that strip CSS.
> 
> FACTS:  
> - FCFCU foreclosure proceeded to judgment without demonstrable valid service.  
> - A writ was executed by the sheriff based on that judgment.  
> - Removal occurred without meaningful notice to the defendant.  
> - Access to personal property was denied following removal.  
> - Displacement caused homelessness and financial harm.  
> - Disability-related communication barriers were present and not accommodated.  
> 
> LEGAL / PROCEDURAL OBSERVATIONS:  
> - Judgment is potentially void ab initio due to lack of service.  
> - Enforcement of a writ based on a void judgment is unlawful.  
> - Sheriff conduct and denial of property access may exceed lawful authority.  
> - Failure to provide reasonable accommodations implicates ADA Title II concerns.  
> - Proper separation of cases (FCFCU vs AES) is necessary to preserve legal clarity.  
> 
> DISABILITY AND COMMUNICATION ISSUES:  
> - ADHD and anxiety materially impair ability to safely engage in phone-based negotiations.  
> - Reliance on phone calls has previously resulted in misunderstanding and adverse agreements.  
> - Written communication is required as a reasonable accommodation.  
> 
> EMOTIONAL IMPACT:  
> - Acute distress during sheriff execution, including fear and panic.  
> - Ongoing stress due to homelessness, instability, and loss of personal property.  
> - Cognitive overload requiring structured, externalized systems to function.  
> 
> QUESTIONS / FLAGS:  
> - Court response timelines for motions to vacate and to stay/quash writ.  
> - Whether additional affidavits or supplemental evidence are required.  
> - Strategy for property retrieval vs damages documentation if access is denied.  
> 
> END OF CASE LOG ENTRY  
> ============================================================
> 
> ---
> 
> ## 3. ARTIFACTS THAT **MUST** BE PRESERVED
> 
> These are non-negotiable. Do **not** delete, overwrite, or “clean” these.
> 
> ### A. STRUCTURAL / SYSTEM ARTIFACTS
> - The **final WorkDrive folder structure** (court-style archive)
> - The **Wiki structure outline**
> - All **HTML wiki templates** (home, overview, history, evidence index, filings, strategy, tasks, reports, finance, timelogs, crosswalk)
> 
> These show *methodical case management* and are credibility assets.
> 
> ---
> 
> ### B. LEGAL DOCUMENT ARTIFACTS
> - File-stamped PDFs of:
>   - Motion to Vacate Void Judgment
>   - Emergency Motion to Stay / Quash Writ
> - Any proposed orders
> - EFSP envelopes and receipts
> - Docket screenshots or PDFs
> 
> ---
> 
> ### C. EVIDENCE ARTIFACTS
> - Sheriff returns (including blank or defective returns)
> - Any proof of lack of notice
> - Debit card replacement / ongoing banking relationship evidence
> - Photos, videos, and written narrative of the removal event
> - Property inventory and loss documentation
> - Credit report snapshots tied to the timeline
> 
> ---
> 
> ### D. META / PROCESS ARTIFACTS (These matter more than you think)
> - Daily logs and timelogs
> - Expense tracking tied to displacement
> - Taskboard history
> - Weekly summaries
> 
> These establish **burden, diligence, and credibility**.
> 
> ---
> 
> ### Bottom line
> You’ve now crossed from “scrambling” into **structured litigation posture**.  
> The system you built today is itself evidence of seriousness, capacity, and reasonableness.
> 
> If you want, next I can:
> - Generate a **single PDF case packet** (executive summary + index + links), or  
> - Create a **one-page attorney intake brief** using what you already have.
