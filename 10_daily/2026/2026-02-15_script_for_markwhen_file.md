---
layout: page
title: "Script for Markwhen File"
slug: "script_for_markwhen_file"
created_at: "2026-02-15 19:27:42"
updated_at: "2026-07-16T06:49:30-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-004.json"
template_key: master-template
date: 2026-02-15
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69927268-4fc4-832e-b307-30ad125be733"
canonical_ref: ""
---

# Script for Markwhen File

## Overview
- **Date**: 2026-02-15 19:27:42
- **Conversation ID**: `69927268-4fc4-832e-b307-30ad125be733`
- **Source**: `Chat-Export-28513-2026/conversations-004.json`

## Chat History

### User
> we need a script that builts the markwhen file from the files of the md files inside the folder, so i guess we need to match the file properties with what it does in the markwhen file?

### Assistant
> Yes. Markwhen is basically just a timeline text file, so your script’s job is:
> 
> 1) **crawl a folder for `.md` files**  
> 2) **extract “event fields” from each file** (date, title, optional tags/links/description)  
> 3) **emit a `.mw` file** in Markwhen syntax
> 
> The “match file properties” part = decide what becomes:
> - the **date** (start/end)
> - the **event title**
> - the **description/body**
> - optional **metadata** (tags, links, groups)
> 
> Below is a solid Python script that supports the two most common ways you’ll have dates:
> - **Filename date prefix** like `2026-02-15_Something.md` (your preferred convention)
> - **YAML front matter** inside the markdown (optional)
> 
> It outputs a single `timeline.mw`.
> 
> ---
> 
> ## Python script: build Markwhen from a folder of Markdown files
> 
> ```python
> #!/usr/bin/env python3
> """
> Build a Markwhen (.mw) timeline from markdown files in a folder.
> 
> Rules (in priority order):
> 1) Date from YAML front matter keys: date, start_date, start (YYYY-MM-DD)
> 2) Else date from filename prefix: YYYY-MM-DD_...
> Title:
> 1) YAML: title
> 2) Else first markdown H1
> 3) Else filename slug
> 
> Description:
> - If YAML has "summary" or "description", use it.
> - Else use the first non-empty paragraph from body (after H1), truncated.
> 
> Output:
> - Sort by date ascending
> - Write Markwhen events like: "2026-02-15: Title"
> """
> 
> from __future__ import annotations
> 
> import re
> import sys
> from dataclasses import dataclass
> from datetime import date
> from pathlib import Path
> from typing import Optional, Tuple, List
> 
> DATE_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})")
> FILENAME_DATE_RE = re.compile(r"^(?P<d>\d{4}-\d{2}-\d{2})[_\-\s].*\.md$", re.IGNORECASE)
> 
> FRONT_MATTER_RE = re.compile(r"^\s*---\s*\n(.*?)\n---\s*\n", re.DOTALL)
> 
> H1_RE = re.compile(r"^\s*#\s+(.+?)\s*$", re.MULTILINE)
> 
> def parse_iso_date(s: str) -> Optional[date]:
>     s = s.strip()
>     m = DATE_RE.match(s)
>     if not m:
>         return None
>     try:
>         return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
>     except ValueError:
>         return None
> 
> def safe_one_line(s: str) -> str:
>     s = re.sub(r"\s+", " ", s).strip()
>     return s
> 
> def extract_front_matter(md_text: str) -> Tuple[dict, str]:
>     """
>     Minimal YAML-frontmatter parser (key: value lines only).
>     Returns (meta, body_without_frontmatter).
>     """
>     meta = {}
>     m = FRONT_MATTER_RE.match(md_text)
>     if not m:
>         return meta, md_text
>     raw = m.group(1)
>     body = md_text[m.end():]
> 
>     # simple "key: value" parsing; ignores nested YAML
>     for line in raw.splitlines():
>         line = line.strip()
>         if not line or line.startswith("#"):
>             continue
>         if ":" not in line:
>             continue
>         k, v = line.split(":", 1)
>         meta[k.strip()] = v.strip().strip('"').strip("'")
>     return meta, body
> 
> def first_paragraph(md_body: str) -> str:
>     """
>     Grab first paragraph-like chunk (non-empty, not a heading/list fence),
>     keep it short.
>     """
>     # remove code fences to avoid grabbing junk
>     body = re.sub(r"```.*?```", "", md_body, flags=re.DOTALL)
>     lines = [ln.rstrip() for ln in body.splitlines()]
> 
>     # drop leading empties
>     i = 0
>     while i < len(lines) and not lines[i].strip():
>         i += 1
> 
>     # if first meaningful line is an H1, skip it
>     if i < len(lines) and lines[i].lstrip().startswith("#"):
>         i += 1
>         while i < len(lines) and not lines[i].strip():
>             i += 1
> 
>     para_lines = []
>     while i < len(lines):
>         ln = lines[i].strip()
>         if not ln:
>             break
>         # stop if another header starts immediately
>         if ln.startswith("#"):
>             break
>         para_lines.append(lines[i])
>         i += 1
> 
>     para = safe_one_line(" ".join(para_lines))
>     if len(para) > 240:
>         para = para[:237].rstrip() + "..."
>     return para
> 
> def extract_title(meta: dict, md_body: str, file_path: Path) -> str:
>     if meta.get("title"):
>         return safe_one_line(meta["title"])
> 
>     h1 = H1_RE.search(md_body)
>     if h1:
>         return safe_one_line(h1.group(1))
> 
>     # fallback: filename without date + extension
>     stem = file_path.stem
>     # strip leading date chunk if present
>     stem = re.sub(r"^\d{4}-\d{2}-\d{2}[_\-\s]+", "", stem)
>     stem = stem.replace("_", " ").strip()
>     return stem or file_path.stem
> 
> def extract_event_date(meta: dict, file_path: Path) -> Optional[date]:
>     for key in ("date", "start_date", "start"):
>         if meta.get(key):
>             d = parse_iso_date(meta[key])
>             if d:
>                 return d
> 
>     m = FILENAME_DATE_RE.match(file_path.name)
>     if m:
>         return parse_iso_date(m.group("d"))
> 
>     return None
> 
> @dataclass
> class Event:
>     d: date
>     title: str
>     desc: str
>     relpath: str
> 
> def build_markwhen_event(e: Event) -> str:
>     # Link back to file for quick jump in your repo/obsidian
>     # Markwhen treats markdown-ish links fine in descriptions.
>     header = f"{e.d.isoformat()}: {e.title}"
>     details_parts = []
>     if e.desc:
>         details_parts.append(e.desc)
>     details_parts.append(f"[source]({e.relpath})")
>     details = "\n  - " + "\n  - ".join(details_parts) if details_parts else ""
>     return header + details
> 
> def main() -> int:
>     if len(sys.argv) < 2:
>         print("Usage: build_markwhen.py /path/to/folder [output.mw]", file=sys.stderr)
>         return 2
> 
>     root = Path(sys.argv[1]).expanduser().resolve()
>     out_path = Path(sys.argv[2]).expanduser().resolve() if len(sys.argv) >= 3 else (root / "timeline.mw")
> 
>     if not root.exists() or not root.is_dir():
>         print(f"Error: folder not found: {root}", file=sys.stderr)
>         return 2
> 
>     md_files = sorted(root.rglob("*.md"))
>     events: List[Event] = []
> 
>     for fp in md_files:
>         try:
>             text = fp.read_text(encoding="utf-8", errors="replace")
>         except Exception as ex:
>             print(f"Skip (read error): {fp} ({ex})", file=sys.stderr)
>             continue
> 
>         meta, body = extract_front_matter(text)
>         d = extract_event_date(meta, fp)
>         if not d:
>             # no date → skip, because Markwhen needs a timeline anchor
>             continue
> 
>         title = extract_title(meta, body, fp)
>         desc = safe_one_line(meta.get("summary") or meta.get("description") or "") or first_paragraph(body)
> 
>         relpath = fp.relative_to(root).as_posix()
>         events.append(Event(d=d, title=title, desc=desc, relpath=relpath))
> 
>     events.sort(key=lambda e: (e.d, e.title.lower()))
> 
>     header = [
>         "# Auto-generated Markwhen timeline",
>         f"# Source folder: {root.as_posix()}",
>         "",
>     ]
>     content = "\n\n".join(build_markwhen_event(e) for e in events)
>     out_path.write_text("\n".join(header) + content + "\n", encoding="utf-8")
> 
>     print(f"Wrote {out_path} ({len(events)} events, scanned {len(md_files)} md files)")
>     return 0
> 
> if __name__ == "__main__":
>     raise SystemExit(main())
> ```
> 
> ---
> 
> ## What “matching file properties” means (practical mapping)
> You need **one** consistent mapping. Here’s the sane default (and what the script uses):
> 
> - **Date**:
>   - `YAML.date` (or `start_date`) if present
>   - else filename prefix `YYYY-MM-DD_`
> - **Title**:
>   - `YAML.title` if present
>   - else first `# H1`
>   - else filename
> - **Description**:
>   - `YAML.summary`/`description` if present
>   - else first paragraph of body
> - **Link back to source**: always include `[source](relative/path.md)`
> 
> ---
> 
> ## Run it
> ```bash
> python build_markwhen.py "C:\path\to\your\folder" "C:\path\to\your\folder\timeline.mw"
> ```
> 
> Or on mac/linux:
> ```bash
> python3 build_markwhen.py ~/vault/03_PHASES ~/vault/03_PHASES/timeline.mw
> ```
> 
> ---
> 
> If you tell me **what folder(s)** you want scanned (e.g., `03_PHASES` only vs whole vault) and whether you want **grouping** (like `## C-01 Service Notice Defects` by folder), I’ll tweak the output format to match how you actually want to read it in Markwhen.

### User
> now this is the update the timeline here is what the current markwhen looks like. 
> # ==============================================================================
> # COLOR DEFINITIONS
> # ==============================================================================
> #Violation_Group: #b00020
> #Standard_Step: #475569
> #Filing_Plaintiff: #1e3a8a
> #Filing_Defendant: #0ea5e9
> #Order_Neutral: #6b21a8
> #Order_Adverse: #7c2d12
> #Service_Defect: #ef4444
> #Critical_Defect: #b91c1c
> #Acceleration_Point: #c2410c
> #ADA_Violation: #be185d
> #Physical_Dispossession: #9a3412
> #Housing_Harm: #78350f
> #Property_Damage: #9a3412
> #Credit_Harm: #451a03
> #Recovery_Action: #15803d
> #Regulatory_Filing: #059669
> #Evidence_Hold: #0e7490
> #Planned: #4b5563
> #Strategic_Goal: #0891b2
> 
> # ==============================================================================
> group [1] STANDARD LEGAL TIMELINE (The "Wait" Path) #Standard_Step
> # ==============================================================================
> 
> 2025-01-16: Complaint Filed & Summons Issued #Standard_Step
> 2025-01-30: Personal Service or Service by Mail Attempted #Standard_Step
> 2025-02-15: IF Copy Service used, mandatory first-class mailing must follow (TR 4.1.B). #Standard_Step
> 2025-03-15: Minimum 20-30 day window for Defendant to respond after VALID service. #Standard_Step
> 2025-06-01: Mediation/Discovery Phase (Standard for FHA/ADA protected households). #Standard_Step
> 2026-01-01: Judgment entered ONLY after jurisdiction is verified. #Standard_Step
> 2026-07-01: Sheriff Sale (Standard 180+ day redemption window). #Standard_Step
> 2026-12-07: Mandatory 48-Hour Safety/Notice period for removal. #Standard_Step
> 2027-01-01: Orderly physical transition of property. #Standard_Step
> 
> endgroup
> 
> # ==============================================================================
> group [2] ACTUAL DEFECTIVE TIMELINE (The "Shortcut" Path)
> # ==============================================================================
> 
> 2025-01-16: Complaint Filed (Omissions of known ADA status) #Filing_Plaintiff #Critical_Defect #ADA_Violation
>   ## Significance
>   This marks the initiation of the foreclosure case. All subsequent proceedings depend on valid service of these initial documents.
> 
> ---
> 
> 2025-03-05: Copy Service Attempted (No mailing sent, no jurisdiction) #Filing_Plaintiff #Service_Defect #Critical_Defect
> 
> ---
> 
> 2025-05-13: Motion for Default Filed despite service failure. #Filing_Plaintiff #Critical_Defect
> 
> ---
> 
> 2025-05-28: Default Judgment Entered WITHOUT jurisdiction #Order_Adverse #Acceleration_Point #Critical_Defect
>   ## Significance
>   This judgment is the foundation for all downstream proceedings. If vacated as void, all subsequent actions are invalid.
> 
> ---
> 
> 2025-08-15: Sheriff Sale (Accelerated by approx 1 year due to bypassed wait periods) #Order_Adverse #Acceleration_Point
>   ## Significance
>   The sale transferred ownership. If the underlying judgment is void, the sale and subsequent writ are also invalid.
> 
> ---
> 
> 2025-09-15: [MISSING] Notice of New Owner / Demand for Possession #Service_Defect #Critical_Defect
>   - Statutory requirement for new owner to identify themselves and demand possession was SKIPPED.
> 
> ---
> 
> 2025-10-15: [MISSING] Notice to Quit (Prerequisite for Eviction) #Service_Defect #Critical_Defect
>   - Standard eviction due process requires notice to vacate prior to writ application. This step was SKIPPED.
> 
> ---
> 
> 2025-12-09: FORCED REMOVAL with ZERO Advance Notice #Physical_Dispossession #Acceleration_Point #Critical_Defect #ADA_Violation
>   ## FACTS
>   - FCFCU obtained removal order same-day.
>   - Zero advance notice; zero service of writ.
>   - Forced to leave without essentials in freezing weather.
>   
>   ## LEGAL OBSERVATIONS
>   - Bypassed standard 48-hour safety/notice protocols.
>   - ADA accommodations requested but ignored by FCFCU.
>   - Inconsistent application of occupant protections.
> 
> endgroup
> 
> # ==============================================================================
> group [3] MASTER INTERNAL LOG (Comprehensive History)
> # ==============================================================================
> 
> # SECTION 1: THE FILING & MISREPRESENTATION PHASE (2025)
> # ------------------------------------------------------------------------------
> # Focus: Defective service and lack of personal jurisdiction.
> 
> 2025-01-16: Foreclosure Filing Initiated (Cause No. 49D04-2501-MF-002559) #Filing_Plaintiff #Service_Defect #ADA_Violation
>   ## Significance
>   This marks the initiation of the foreclosure case. All subsequent proceedings depend on valid service of these initial documents.
>   - Material omissions of ADA accommodation requests and documented cure efforts.
>   - Failure to disclose hardship context.
> 
> ---
> 
> 2025-03-05: Service Attempt #1 (Copy Service) #Filing_Plaintiff #Service_Defect
>   - Copy left at property, but NO secondary mailing (Trial Rule 4.1 failure).
> 
> ---
> 
> 2025-04-15: Service Attempt #2 (Copy Service) #Filing_Plaintiff #Service_Defect
>   - Second attempt, still NO secondary mailing. Personal jurisdiction fails to attach.
> 
> ---
> 
> 2025-05-13: Motion for Default Judgment Filed #Filing_Plaintiff
>   - FCFCU moves for judgment despite defective service.
> 
> ---
> 
> 2025-05-21: Order Denying Motion for Default Judgment #Order_Neutral
>   ## Legal Significance
>   ### Service Requirements
>   - Court denied motion due to missing service returns for co-defendants.
>   - This highlights the importance of proper service on all parties.
>   - Defendant's position: service on primary defendant was also defective.
> 
> ---
> 
> 2025-05-23: Amended Motion for Default Judgment Filed #Filing_Plaintiff
>   ## Legal Significance
>   ### Service Issues Addressed
>   - Amended motion likely addressed the missing service returns for co-defendants.
>   - However, the underlying service dispute regarding the primary defendant remains.
>   - Defendant maintains service was defective per TR 4.1(B).
> 
> ---
> 
> 2025-05-28: Default Judgment Entered #Order_Adverse #Service_Defect
>   ## Significance
>   This judgment is the foundation for all downstream proceedings (sheriff sale, writ, removal). If vacated as void, all subsequent actions are invalid.
>   - Judgment entered based on voidable service. Jurisdiction is flawed.
> 
> ---
> 
> 2025-05-30: Praecipe for Sheriff's Sale Filed #Filing_Plaintiff
>   ## Legal Significance
>   ### Post-Judgment Process
>   - Praecipe initiates the sheriff sale process.
>   - Sale scheduled for 2025-08-15.
>   - If judgment is void, the sale is also invalid.
> 
> ---
> 
> # SECTION 2: THE TRANSFER & DISPLACEMENT PHASE (2025)
> # ------------------------------------------------------------------------------
> # Focus: Acceleration of sale and physical dispossession without due process.
> 
> 2025-07-09: Sheriff Sale Notice Posted #Filing_Plaintiff
>   ## Legal Significance
>   ### Notice Requirements
>   - Notice posted at property address.
>   - Sale scheduled for approximately 5 weeks later.
>   - If judgment is void, the sale notice and sale are invalid.
> 
> ---
> 
> 2025-08-15: Sheriff Sale Conducted & Ownership Transfer #Order_Adverse #Physical_Dispossession
>   ## Significance
>   The sale transferred ownership of the property. If the underlying judgment is void, the sale and subsequent writ are also invalid.
>   - **Sale Number:** 032
>   - **Total Paid:** $240,464.20
> 
> ---
> 
> 2025-09-15: [MISSING] Notice of New Owner & Demand for Possession #Service_Defect #Procedural_Defect
>   ## Significance
>   - **Procedural Failure:** FCFCU (as new owner) failed to provide statutory notice of ownership transfer.
>   - **Impact:** Occupant was not informed of the new ownership status or given a formal demand for possession, preventing any opportunity for voluntary compliance or negotiation.
> 
> ---
> 
> 2025-10-15: [MISSING] Prerequisite Eviction Notice (Notice to Quit) #Service_Defect #Due_Process_Violation
>   ## Significance
>   - **Procedural Failure:** No "Notice to Quit" or formal eviction notice was served prior to seeking the Writ.
>   - **Legal Context:** In a standard workflow, a Writ of Assistance should only be requested *after* the occupant refuses a formal notice to vacate. Skipping this step denied the occupant due process and notice.
> 
> ---
> 
> 2025-10-29: Petition for Writ of Assistance Filed #Filing_Plaintiff
> 2025-11-06: Writ of Assistance Issued #Order_Adverse
>   - Court directs Sheriff to dispossess occupants.
> 
> ---
> 
> 2025-12-09: WRIT EXECUTED - FORCED PHYSICAL REMOVAL #Physical_Dispossession #Housing_Harm #ADA_Violation
>   ## SUMMARY
>   Forced removal executed by Sheriff without standard 48-hour ADA safety notice. Armed escalation (guns drawn) despite full compliance.
>   
>   ## FACTS
>   - FCFCU obtained an order/writ authorizing same-day sheriff removal.
>   - No advance notice of a vacate date or removal date was provided.
>   - No notice was posted on the door or mailbox; no mail/email notice.
>   - Treated as a potential threat despite no criminal behavior or resistance.
>   - Forced to leave without essentials (toiletries, grooming supplies).
>   
>   ## LEGAL / PROCEDURAL OBSERVATIONS
>   - Inconsistency: Law enforcement requires civil eviction for guests (Luis) but executed immediate writ for FCFCU.
>   - Same-day enforcement without service or notice is a due process violation.
>   
>   ## DISABILITY CHALLENGES
>   - ADA communication requests (email vs phone) systematically ignored by FCFCU.
>   - Neurodivergent stress responses misinterpreted as evasiveness by authorities.
>   
>   ## EMOTIONAL IMPACT
>   - Humiliation, fear, and grief. Stripped of dignity and humanity.
> 
> ---
> 
> 2025-12-10: Emergency Motions Filed - Vacate and Stay #Filing_Defendant #Recovery_Action
>   - Motion to Vacate Void Judgment (TR 60(B))
>   - Emergency Motion to Stay Writ and Protect Property
> 
> ---
> 
> 2025-12-11: Court Orders & Hearing Scheduled #Order_Neutral
>   ## Legal Significance
>   - Court denied emergency stay (as writ was already executed).
>   - Hearing on Motion to Vacate set for **January 9, 2026**.
> 
> ---
> 
> 2025-12-12: Supplemental Emergency Motion Filed #Filing_Defendant
>   - Seeking temporary access for essential belongings (ADA necessity).
> 
> ---
> 
> 2025-12-15: Case DNA & Strategic Planning Session #Internal
>   ## SUMMARY
>   Consolidation of case narrative: shift from survival into long-term offensive strategy.
>   - Decision to use public-opinion pressure via standalone donation page.
>   - Identified "payout" strategy and multi-phase regulatory pressure.
>   - Insight: FCFCU's prior professional knowledge of Cody's capacity suggests predatory targeting.
> 
> ---
> 
> 2025-12-16: Post-Removal Access Denial #Housing_Harm #ADA_Violation
>   ## FACTS
>   - Susan Abbett (FCFCU) admits no one available to provide access.
>   - Defendant unhoused in freezing conditions without essentials.
> 
> ---
> 
> 2025-12-21: Displacement Harm: Service Animal Escape & Property Damage #Housing_Harm #ADA_Violation #Property_Damage
>   ## SUMMARY
>   Acute crisis event: Service animal (Gigi) escaped vehicle during repacking in roach-infested hotel transition.
>   
>   ## POST-REMOVAL DAMAGE DISCOVERED
>   - Pipes in laundry room burst due to freezing; water damage and mold.
>   - Mini-fridge unplugged/destroyed (sentimental loss).
>   - Systematic interference: electronics (cameras, routers) deliberately unplugged.
>   - Utilities remain in Cody's name despite dispossession.
> 
> ---
> 
> # SECTION 3: THE ENFORCEMENT & RECOVERY PHASE (2026)
> # ------------------------------------------------------------------------------
> # Focus: Turning the tide through regulatory and credit recovery actions.
> 
> 2026-01-09: Summary Hearing / Appearance by Plaintiff #Filing_Plaintiff #Order_Neutral
>   - Plaintiff's counsel appears in response to emergency motions.
> 
> ---
> 
> 2026-01-18: Cascade of Harm: Zai Asylum & Secondary Displacement #Housing_Harm #ADA_Violation
>   ## ZAI ASYLUM IMPACT
>   - Displacement contributes to the loss of legal status protection for household member.
>   
>   ## SECONDARY DISPLACEMENT (OTIS)
>   - Forced to vacate unsafe "Otis" room rental (bugs, smoke, harassment).
>   - Otis intensified financial extortion (drug-related) and squatting behavior.
>   - Cody/Zai forced to move out immediately; searching for stable suites.
> 
> ---
> 
> 2026-01-18: Forced Relocation to Evansville, IN #Housing_Harm #Physical_Dispossession
>   ## Impact
>   - Professional harm: Loss of local client base.
>   - Technical bottlenecks: Slow internet preventing efficient litigation workflow.
>   - Psychological harm: Secondary displacement trauma.
> 
> ---
> 
> 2026-01-27: Phase 01.5 - Evidence Preservation Packet Dispatched #Evidence_Hold
>   - Formal notice to FCFCU, Counsel, and Sheriff.
>   - Duty to preserve data back to 01/16/2024.
> 
> ---
> 
> 2026-01-27: Phase 02 - Emergency Credit Recovery Initiated #Recovery_Action #Credit_Harm
>   - Direct Disputes to FCFCU (Demand suppression).
>   - Bureau Disputes (Experian, Equifax, TransUnion).
>   - CFPB Complaint Filed (Housing Harm Narrative).
> 
> ---
> 
> 2026-01-27: Phase 03 - Regulator Filings Launch #Regulatory_Filing #Strategic_Goal
>   - Regulator Filings (HUD, NCUA, DOJ).
>   - Broad-spectrum regulatory pressure launch.
> 
> ---
> 
> 2026-01-27: Phase 04 - The Hotel Enforcement (Evansville) #Housing_Harm #Planned
>   - Active enforcement of habitability and service animal rights at current residence.
> 
> ---
> 
> # SECTION 4: FUTURE TARGETS & DEADLINES
> # ------------------------------------------------------------------------------
> # Focus: Maintaining momentum and escalating to federal court.
> 
> 2026-02-10: Deadline for Evidence Preservation Confirmation (48hr + Mail) #Planned
> 2026-02-15: Trigger Phase 04 - Federal Court Escalation (if no cure) #Planned #Filing_Defendant
> 2026-02-27: FCRA Reinvestigation Deadline (30-day clock) #Planned #Recovery_Action
> 2026-03-15: Follow-up on HUD/DOJ Civil Rights Complaints #Planned #ADA_Violation
> 2026-04-01: Valuation Assessment for Settlement / Trial Prep #Planned
> 
> endgroup
> 
> ---
> ### THE "ACCELERATION" ANALYSIS
> By bypassing the mailing requirement of Trial Rule 4.1(B), the Plaintiff "jumped" directly to a Default Judgment 10 months earlier than a standard contested case would have allowed. This shortcut effectively "blinded" the court to the existence of the Defendant, resulting in a void judgment and the subsequent displacement crisis.
> <div class="ob-timelines"
> 	data-title=""
> 	data-description=""
> 	data-start-date=""
> 	data-end-date=""
> 	data-classes=""
> 	data-color=""
> 	data-era=""
> 	data-group=""
> 	data-path=""
> 	data-points-to=""
> 	data-type=""
> 	data-tags="">
> 	New Event
> </div>
> 
> # ==============================================================================
> 
> # ==============================================================================
> group [4] VIOLATIONS & DAMAGES LOG (The "Harm" Path) #Violation_Group
> # ==============================================================================
> 
> 2025-05-28: Service of process was not completed in accordance with Indiana Trial Rule 4.1(B); The Court therefore did not acquire personal jurisdiction over Defendant; A judgment entered without personal jurisdiction is VOID ab initio and must be vacated. #Procedural
> 2025-12-09: Cody was removed from the residence at 4817 Shadow Pointe Dr. on December 9, 2025, through enforcement of a Writ of Assistance whose validity is currently under challenge. #Procedural
> 2025-12-09: No advance notice of a vacate date or removal date was provided to me. No notice was posted on the door or mailbox... I was not served with the writ prior to enforcement. #Procedural
> 2025-12-09: Sheriff executed a forcible removal WITHOUT an eviction case. No summons, no hearing, no eviction order. Sheriff posted no 48-hour notice before removal. #Procedural
> 2025-12-10: Every federal court that has addressed the issue has held that Rule 13(a)... bars a defendant who defaults... from later filing a transactionally related claim in a subsequent suit. This Article argues that the federal courts’ interpretation of Rule 13(a) is fundamentally wrong. #Procedural
> 2025-12-21: I discovered that all interior security cameras had been unplugged and rendered nonfunctional... The unplugging of security cameras constitutes interference with potential evidence and spoliation. #Statutory
> 2026-01-02: Exhibit X — Inventory of Jurisdictional, Execution, and Civil Rights Violations #Statutory
> 
> endgroup

### Assistant
> Got it. You don’t want a fresh “timeline.mw” anymore — you want an **updater** that:
> 
> - **preserves your existing header + color definitions + hand-written narrative**
> - **rebuilds specific groups (or specific sections inside a group)** from `.md` files
> - keeps your **tagging style** (`#Filing_Plaintiff #Critical_Defect …`)
> - outputs Markwhen that matches your current formatting
> 
> Also: your current file has a **random Obsidian HTML `<div class="ob-timelines">…</div>`** wedged into the Markwhen. That should be removed automatically because it will break/dirty the timeline.
> 
> Below is a script that does exactly that.
> 
> ---
> 
> ## What this script updates (safe + controlled)
> 
> ### ✅ It preserves everything except blocks you explicitly “own” with markers
> You’ll add (or keep) markers in the `.mw` file like:
> 
> ```mw
> # >>> AUTOGEN:GROUP3:START
> ... replaced ...
> # >>> AUTOGEN:GROUP3:END
> ```
> 
> Same idea for the Violations group:
> 
> ```mw
> # >>> AUTOGEN:GROUP4:START
> ... replaced ...
> # >>> AUTOGEN:GROUP4:END
> ```
> 
> Everything outside those markers stays untouched.
> 
> ### ✅ It generates Markwhen events from your `.md` files
> It reads each `.md` and extracts:
> - **date**: YAML `date:` or filename prefix `YYYY-MM-DD_`
> - **title**: YAML `title:` or first `# H1` or filename
> - **tags**: YAML `tags:` (comma or bracket list) OR inferred from folders if you want
> - **body**: optional `summary:` / `description:` or first paragraph
> 
> It then formats the event like your existing style:
> 
> ```mw
> 2025-12-09: WRIT EXECUTED - FORCED PHYSICAL REMOVAL #Physical_Dispossession #Housing_Harm #ADA_Violation
>   ## SUMMARY
>   ...
> ---
> ```
> 
> ---
> 
> ## Required YAML convention (minimal)
> For best results, stick this at the top of your event `.md` files:
> 
> ```yaml
> ---
> date: 2025-12-09
> title: WRIT EXECUTED - FORCED PHYSICAL REMOVAL
> tags: Physical_Dispossession, Housing_Harm, ADA_Violation
> group: 3
> ---
> ```
> 
> Optional:
> - `summary:` or `description:` (used for the first bullet/paragraph)
> - `section:` (if you want sub-ordering inside a group)
> 
> If you don’t include YAML, it will still work from filename + H1.
> 
> ---
> 
> ## Python: `update_markwhen.py`
> 
> ```python
> #!/usr/bin/env python3
> """
> Update an existing Markwhen file by replacing AUTOGEN blocks with events generated from Markdown files.
> 
> - Preserves everything outside AUTOGEN markers.
> - Removes Obsidian HTML artifacts like <div class="ob-timelines">...</div>.
> - Generates Markwhen events in your house style (date: title #tags + optional body).
> """
> 
> from __future__ import annotations
> 
> import re
> import sys
> from dataclasses import dataclass
> from datetime import date
> from pathlib import Path
> from typing import Dict, List, Optional, Tuple
> 
> # -----------------------------
> # Parsing helpers
> # -----------------------------
> 
> DATE_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")
> FILENAME_DATE_RE = re.compile(r"^(?P<d>\d{4}-\d{2}-\d{2})[_\-\s].*\.md$", re.IGNORECASE)
> FRONT_MATTER_RE = re.compile(r"^\s*---\s*\n(.*?)\n---\s*\n", re.DOTALL)
> H1_RE = re.compile(r"^\s*#\s+(.+?)\s*$", re.MULTILINE)
> 
> # Remove Obsidian timeline HTML blocks
> OB_TIMELINES_DIV_RE = re.compile(r"<div\s+class=[\"']ob-timelines[\"'].*?</div>", re.DOTALL | re.IGNORECASE)
> 
> 
> def parse_iso_date(s: str) -> Optional[date]:
>     s = s.strip()
>     m = DATE_RE.match(s)
>     if not m:
>         return None
>     try:
>         return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
>     except ValueError:
>         return None
> 
> 
> def one_line(s: str) -> str:
>     return re.sub(r"\s+", " ", s).strip()
> 
> 
> def extract_front_matter(md_text: str) -> Tuple[Dict[str, str], str]:
>     """
>     Minimal YAML front matter parser:
>     - supports key: value
>     - supports tags: [a, b] or tags: a, b
>     - does NOT support nested yaml (by design)
>     """
>     meta: Dict[str, str] = {}
>     m = FRONT_MATTER_RE.match(md_text)
>     if not m:
>         return meta, md_text
> 
>     raw = m.group(1)
>     body = md_text[m.end():]
> 
>     for line in raw.splitlines():
>         line = line.strip()
>         if not line or line.startswith("#") or ":" not in line:
>             continue
>         k, v = line.split(":", 1)
>         meta[k.strip()] = v.strip().strip('"').strip("'")
> 
>     return meta, body
> 
> 
> def parse_tags(meta: Dict[str, str]) -> List[str]:
>     raw = meta.get("tags", "") or ""
>     raw = raw.strip()
>     if not raw:
>         return []
>     # tags: [A, B]
>     if raw.startswith("[") and raw.endswith("]"):
>         raw = raw[1:-1].strip()
>     # split by comma
>     parts = [p.strip() for p in raw.split(",")]
>     return [p for p in parts if p]
> 
> 
> def extract_title(meta: Dict[str, str], body: str, fp: Path) -> str:
>     if meta.get("title"):
>         return one_line(meta["title"])
>     h1 = H1_RE.search(body)
>     if h1:
>         return one_line(h1.group(1))
>     stem = fp.stem
>     stem = re.sub(r"^\d{4}-\d{2}-\d{2}[_\-\s]+", "", stem)
>     return stem.replace("_", " ").strip() or fp.stem
> 
> 
> def extract_date(meta: Dict[str, str], fp: Path) -> Optional[date]:
>     for key in ("date", "start_date", "start"):
>         if meta.get(key):
>             d = parse_iso_date(meta[key])
>             if d:
>                 return d
>     m = FILENAME_DATE_RE.match(fp.name)
>     if m:
>         return parse_iso_date(m.group("d"))
>     return None
> 
> 
> def first_paragraph(body: str) -> str:
>     # strip code fences
>     body2 = re.sub(r"```.*?```", "", body, flags=re.DOTALL)
>     lines = [ln.rstrip() for ln in body2.splitlines()]
> 
>     # skip empties
>     i = 0
>     while i < len(lines) and not lines[i].strip():
>         i += 1
> 
>     # skip first H1 if present
>     if i < len(lines) and lines[i].lstrip().startswith("#"):
>         i += 1
>         while i < len(lines) and not lines[i].strip():
>             i += 1
> 
>     para = []
>     while i < len(lines):
>         ln = lines[i].strip()
>         if not ln:
>             break
>         if ln.startswith("#"):
>             break
>         # stop before hr
>         if ln.strip() == "---":
>             break
>         para.append(lines[i])
>         i += 1
> 
>     text = one_line(" ".join(para))
>     if len(text) > 260:
>         text = text[:257].rstrip() + "..."
>     return text
> 
> 
> # -----------------------------
> # Markwhen generation
> # -----------------------------
> 
> @dataclass
> class Event:
>     d: date
>     title: str
>     tags: List[str]
>     body: str  # markdown-ish text
>     source_rel: str  # link back to md
> 
> 
> def format_event(e: Event) -> str:
>     tags_str = (" " + " ".join(f"#{t}" for t in e.tags)) if e.tags else ""
>     out = [f"{e.d.isoformat()}: {e.title}{tags_str}"]
>     if e.body:
>         # indent body by two spaces to match your style
>         for line in e.body.splitlines():
>             out.append(f"  {line}".rstrip())
>     out.append("")
>     out.append("---")
>     out.append("")
>     return "\n".join(out)
> 
> 
> def md_to_event(fp: Path, root: Path) -> Optional[Event]:
>     text = fp.read_text(encoding="utf-8", errors="replace")
>     text = OB_TIMELINES_DIV_RE.sub("", text)  # scrub embedded ob-timelines html if any
>     meta, body = extract_front_matter(text)
> 
>     d = extract_date(meta, fp)
>     if not d:
>         return None
> 
>     title = extract_title(meta, body, fp)
>     tags = parse_tags(meta)
> 
>     desc = meta.get("summary") or meta.get("description") or ""
>     desc = desc.strip()
> 
>     if desc:
>         # Keep it as a simple paragraph; you can put your own "## Significance" blocks in the md body.
>         first = one_line(desc)
>         body_out = f"- {first}\n- [source]({fp.relative_to(root).as_posix()})"
>     else:
>         para = first_paragraph(body)
>         # If the md already contains structured sections, keep the body as-is (minus front matter).
>         # Heuristic: if it has "## " headings, preserve it.
>         if "## " in body:
>             body_clean = OB_TIMELINES_DIV_RE.sub("", body).strip()
>             body_out = body_clean + f"\n\n- [source]({fp.relative_to(root).as_posix()})"
>         else:
>             bits = []
>             if para:
>                 bits.append(f"- {para}")
>             bits.append(f"- [source]({fp.relative_to(root).as_posix()})")
>             body_out = "\n".join(bits)
> 
>     return Event(
>         d=d,
>         title=title,
>         tags=tags,
>         body=body_out.strip(),
>         source_rel=fp.relative_to(root).as_posix(),
>     )
> 
> 
> def collect_events(md_root: Path, group_filter: Optional[str] = None) -> List[Event]:
>     """
>     If group_filter is provided, only include md files whose YAML has group: <filter>.
>     """
>     events: List[Event] = []
>     files = sorted(md_root.rglob("*.md"))
>     for fp in files:
>         try:
>             text = fp.read_text(encoding="utf-8", errors="replace")
>         except Exception:
>             continue
>         meta, _ = extract_front_matter(text)
>         if group_filter is not None:
>             g = (meta.get("group") or "").strip()
>             if g != str(group_filter):
>                 continue
> 
>         e = md_to_event(fp, md_root)
>         if e:
>             events.append(e)
> 
>     events.sort(key=lambda x: (x.d, x.title.lower()))
>     return events
> 
> 
> # -----------------------------
> # AUTOGEN block replacement
> # -----------------------------
> 
> def replace_block(mw_text: str, block_name: str, replacement: str) -> str:
>     """
>     Replace content between:
>       # >>> AUTOGEN:<block_name>:START
>       ...
>       # >>> AUTOGEN:<block_name>:END
>     """
>     start = f"# >>> AUTOGEN:{block_name}:START"
>     end = f"# >>> AUTOGEN:{block_name}:END"
> 
>     if start not in mw_text or end not in mw_text:
>         raise RuntimeError(
>             f"Missing AUTOGEN markers for block '{block_name}'. "
>             f"Add:\n{start}\n...\n{end}\n"
>         )
> 
>     before, rest = mw_text.split(start, 1)
>     _, after = rest.split(end, 1)
> 
>     # Keep markers, replace interior
>     return before + start + "\n" + replacement.rstrip() + "\n" + end + after
> 
> 
> def scrub_ob_html(mw_text: str) -> str:
>     return OB_TIMELINES_DIV_RE.sub("", mw_text)
> 
> 
> def main() -> int:
>     if len(sys.argv) < 4:
>         print(
>             "Usage:\n"
>             "  python update_markwhen.py <markwhen_file.mw> <md_folder_root> <block_name> [<group_filter>]\n\n"
>             "Examples:\n"
>             "  python update_markwhen.py timeline.mw 03_PHASES GROUP3 3\n"
>             "  python update_markwhen.py timeline.mw 03_PHASES GROUP4 4\n",
>             file=sys.stderr,
>         )
>         return 2
> 
>     mw_path = Path(sys.argv[1]).expanduser().resolve()
>     md_root = Path(sys.argv[2]).expanduser().resolve()
>     block_name = sys.argv[3].strip()
>     group_filter = sys.argv[4].strip() if len(sys.argv) >= 5 else None
> 
>     if not mw_path.exists():
>         print(f"Markwhen file not found: {mw_path}", file=sys.stderr)
>         return 2
>     if not md_root.exists() or not md_root.is_dir():
>         print(f"MD folder not found: {md_root}", file=sys.stderr)
>         return 2
> 
>     mw_text = mw_path.read_text(encoding="utf-8", errors="replace")
>     mw_text = scrub_ob_html(mw_text)
> 
>     events = collect_events(md_root, group_filter=group_filter)
>     replacement = "\n".join(format_event(e) for e in events).rstrip()
> 
>     updated = replace_block(mw_text, block_name, replacement)
>     mw_path.write_text(updated, encoding="utf-8")
> 
>     print(f"Updated {mw_path.name} block {block_name} with {len(events)} events from {md_root}")
>     return 0
> 
> 
> if __name__ == "__main__":
>     raise SystemExit(main())
> ```
> 
> ---
> 
> ## How to wire this into your current `.mw` file
> 
> ### Step 1) Add AUTOGEN markers inside Group 3 and Group 4
> 
> Example placement for **Group 3** (inside your existing group [3] … endgroup):
> 
> ```mw
> group [3] MASTER INTERNAL LOG (Comprehensive History)
> # ==============================================================================
> 
> # >>> AUTOGEN:GROUP3:START
> # (this section will be replaced by script)
> # >>> AUTOGEN:GROUP3:END
> 
> endgroup
> ```
> 
> For **Group 4**:
> 
> ```mw
> group [4] VIOLATIONS & DAMAGES LOG (The "Harm" Path) #Violation_Group
> # ==============================================================================
> 
> # >>> AUTOGEN:GROUP4:START
> # (this section will be replaced by script)
> # >>> AUTOGEN:GROUP4:END
> 
> endgroup
> ```
> 
> ### Step 2) Run updates
> 
> Rebuild Group 3 from `.md` files with `group: 3`:
> 
> ```bash
> python update_markwhen.py "timeline.mw" "C:\path\to\md_root" GROUP3 3
> ```
> 
> Rebuild Group 4 from `.md` files with `group: 4`:
> 
> ```bash
> python update_markwhen.py "timeline.mw" "C:\path\to\md_root" GROUP4 4
> ```
> 
> ---
> 
> ## Two blunt fixes you should make right now
> 
> 1) **Stop using `#Procedural_Defect`, `#Due_Process_Violation`, etc. if you haven’t defined them** in your “COLOR DEFINITIONS”, *unless you don’t care about color consistency*. Right now you have tags in the file that don’t exist in your definitions.
> 
> 2) **Kill the `#Procedural` trailing tags in Group 4** or formalize them. You’re mixing two tagging systems:
> - the color-coded taxonomy tags (`#ADA_Violation`, `#Critical_Defect`)
> - generic category labels (`#Procedural`, `#Statutory`)
> 
> Either is fine, but mixing will make your timeline visually inconsistent unless you define and color them too.
> 
> ---
> 
> If you tell me where the `.md` files live (one folder vs many) and whether you want **folder → tag mapping** (ex: `C-01_Service_Notice_Defects/` automatically adds `#Service_Defect`), I’ll extend the script to infer tags from your vault structure automatically.
