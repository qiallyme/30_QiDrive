---
layout: page
title: "App Testing Workflow"
slug: "app_testing_workflow"
created_at: "2026-05-17 03:17:34"
updated_at: "2026-07-18T11:03:15-04:00"
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
date: 2026-05-17
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a09798c-db90-83ea-86ac-21faea4ba744"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# App Testing Workflow

## Overview
- **Date**: 2026-05-17 03:17:34
- **Conversation ID**: `6a09798c-db90-83ea-86ac-21faea4ba744`
- **Source**: `Chat-Export-28513-2026/conversations-007.json`

## Chat History

### User
> what is the best way to test my app and make notes of what needs to be corrected for ai input of what to work on.

### Assistant
> Best way: **test like a user, document like a product manager, and feed AI like a developer.**
> 
> Do **not** just say “fix the app.” That gives AI too much room to wander and break things. You want structured issue notes.
> 
> ## The workflow
> 
> ### 1. Create a testing note per session
> 
> Use one file per testing run:
> 
> `2026-05-17_app_testing_notes.md`
> 
> Inside, organize it like this:
> 
> ```md
> # App Testing Notes
> 
> Date: 2026-05-17
> App/Module:
> Environment:
> Tester:
> Version/Branch:
> 
> ## Testing Goal
> 
> What am I trying to verify in this session?
> 
> Example:
> Test the main UI flow for creating, editing, saving, and deleting records.
> 
> ---
> 
> ## Test Path
> 
> 1. Open app
> 2. Navigate to:
> 3. Click:
> 4. Enter:
> 5. Expected:
> 6. Actual:
> 
> ---
> 
> ## Issues Found
> 
> ### ISSUE-001 — Short title
> 
> Priority: High / Medium / Low
> Type: Bug / UI / Performance / Data / Feature / UX / Security
> Location: Page, screen, component, or file if known
> 
> Expected:
> What should have happened.
> 
> Actual:
> What happened instead.
> 
> Steps to reproduce:
> 1.
> 2.
> 3.
> 
> Evidence:
> Screenshot, error message, traceback, console log, bad output, etc.
> 
> Suggested fix:
> Optional. Only if obvious.
> 
> AI instruction:
> What should the AI/code agent do?
> 
> Status:
> Open / Fixed / Retest Needed / Deferred
> 
> ---
> 
> ## Notes / Ideas
> 
> Non-urgent observations, feature ideas, friction points.
> 
> ---
> 
> ## Final AI Work Order
> 
> A clean summary of what needs to be fixed next.
> ```
> 
> That’s your master format.
> 
> ## 2. Use priority buckets
> 
> Don’t treat everything equally. That’s how apps become soup.
> 
> Use this:
> 
> ### P0 — App broken
> 
> Crashes, won’t open, data loss, login blocked, save fails.
> 
> ### P1 — Core workflow broken
> 
> Main feature technically opens but cannot be used correctly.
> 
> ### P2 — UX/UI friction
> 
> Confusing layout, bad labels, annoying flow, ugly but usable.
> 
> ### P3 — Polish / later
> 
> Nice-to-have, spacing, wording, extra features.
> 
> AI should work in this order:
> 
> **P0 → P1 → P2 → P3**
> 
> No exceptions unless you intentionally choose otherwise.
> 
> ## 3. Capture issues in “AI-ready” format
> 
> For every issue, write it like this:
> 
> ```md
> ### ISSUE-001 — App crashes when opening Directory Markmind Mapper
> 
> Priority: P0
> Type: Import / Startup Bug
> Location: tools/system/sys_directory_markmind_mapper
> 
> Expected:
> The toolbox should open normally and load the Directory Markmind Mapper tool.
> 
> Actual:
> The app crashes on startup with ModuleNotFoundError.
> 
> Steps to reproduce:
> 1. Run main_ui.py
> 2. App attempts to import sys_directory_markmind_mapper
> 3. Startup fails
> 
> Evidence:
> ModuleNotFoundError: No module named 'tools.system.sys_directory_markmind_mapper.SysDirectoryMarkmindMapperTool'
> 
> Likely cause:
> The __init__.py file imports a class/module name that does not match the actual filename or class.
> 
> AI instruction:
> Inspect the sys_directory_markmind_mapper package, verify the filename, class name, and __init__.py exports. Fix the import path so main_ui.py can load the tool without crashing. Do not rename unrelated tools. Add a small import smoke test if appropriate.
> 
> Status:
> Open
> ```
> 
> That is the kind of input Codex/Aider/AI can actually use.
> 
> ## 4. Test by user flows, not random clicking
> 
> Use a checklist like this:
> 
> ```md
> ## Core User Flow Test
> 
> ### Flow 1 — App launches
> - [ ] App opens without error
> - [ ] Main screen loads
> - [ ] Tools/modules appear
> - [ ] No console traceback
> 
> ### Flow 2 — Tool opens
> - [ ] Select tool
> - [ ] Tool panel loads
> - [ ] Required fields are visible
> - [ ] Buttons are clear
> 
> ### Flow 3 — Input works
> - [ ] User can choose file/folder
> - [ ] User can enter text/settings
> - [ ] Bad input shows helpful error
> - [ ] Empty input does not crash
> 
> ### Flow 4 — Output works
> - [ ] Output is created
> - [ ] Output saved in correct folder
> - [ ] Filename follows convention
> - [ ] User sees success message
> 
> ### Flow 5 — Error handling
> - [ ] Missing file handled cleanly
> - [ ] Permission issue handled cleanly
> - [ ] Bad path handled cleanly
> - [ ] Error message tells user what to do
> ```
> 
> This keeps you from ADHD-clicking yourself into chaos. Test the road, not every blade of grass.
> 
> ## 5. Give AI a tight work order
> 
> After testing, don’t paste all notes blindly. Give the AI this:
> 
> ```md
> # AI Work Order
> 
> You are working on this app:
> 
> App:
> Repo/path:
> Branch:
> Relevant files:
> 
> ## Goal
> 
> Fix the highest-priority issues found during manual testing without changing unrelated architecture.
> 
> ## Rules
> 
> 1. Fix P0 and P1 issues first.
> 2. Do not refactor unrelated systems.
> 3. Preserve current folder structure unless required.
> 4. Keep naming consistent with existing tool conventions.
> 5. Add or update README/dev notes if the fix changes behavior.
> 6. Add simple smoke tests where useful.
> 7. After changes, summarize:
>    - Files changed
>    - Bugs fixed
>    - How to test
>    - Anything deferred
> 
> ## Issues to fix
> 
> [paste issues here]
> ```
> 
> That keeps the AI from going “I redesigned your entire app because one import was broken.” Absolutely not, little robot.
> 
> ## 6. Best tool setup for you
> 
> For your toolbox/dev work, I’d use this folder pattern:
> 
> ```md
> /docs/dev_history/
>   2026-05-17_app_testing_notes.md
>   2026-05-17_ai_work_order.md
>   2026-05-17_test_results.md
> ```
> 
> And for each standalone tool:
> 
> ```md
> tools/system/sys_directory_markmind_mapper/
>   README.md
>   ai_manifest.md
>   test_notes.md
> ```
> 
> Best practice:
> 
> - **Session notes** go in `docs/dev_history/`
> - **Tool-specific bugs** can also be copied into that tool’s folder
> - **Reusable templates** go in something like:
> 
> ```md
> docs/60_operations/02_templates/
>   app_testing_note_template.md
>   ai_work_order_template.md
>   bug_report_template.md
> ```
> 
> ## My recommended minimum system
> 
> Use only these 3 documents at first:
> 
> 1. **Bug Report Template**
> 2. **App Testing Session Template**
> 3. **AI Work Order Template**
> 
> Don’t overbuild this yet. The danger is creating a testing bureaucracy instead of fixing the damn app.
> 
> Your best move:
> 
> Create one testing session note, test one flow at a time, write issues in AI-ready format, then feed only the top 3–5 issues to Codex/Aider.

### User
> i was thinking more like a spreadsheet, but we also need a checklist.

### Assistant
> Yes — **spreadsheet is better** for tracking app testing. The checklist is the testing script; the spreadsheet is the command center.
> 
> Use both:
> 
> ## Best structure
> 
> ### Sheet 1: `Test Checklist`
> 
> This is the repeatable “what do I test every time?” sheet.
> 
> | Area | Test Item | Steps | Expected Result | Pass/Fail | Notes |
> |---|---|---|---|---|---|
> | Startup | App opens | Run app from main entry | App opens without traceback |  |  |
> | Navigation | Tool list loads | Open main UI | All tools appear correctly |  |  |
> | Tool Launch | Open selected tool | Click tool button | Tool panel loads |  |  |
> | Input | Empty input handling | Submit blank form | User gets helpful message, no crash |  |  |
> | Output | File creation | Run tool with valid input | Output saves correctly |  |  |
> | Error Handling | Bad path | Enter invalid path | Clean error message appears |  |  |
> 
> This is your reusable QA checklist.
> 
> ---
> 
> ### Sheet 2: `Issues`
> 
> This is where bugs/friction go.
> 
> | Issue ID | Priority | Type | Area | Title | Expected | Actual | Steps to Reproduce | Evidence | AI Instruction | Status |
> |---|---|---|---|---|---|---|---|---|---|---|
> | BUG-001 | P0 | Startup Bug | Directory Mapper | App crashes on import | App opens normally | ModuleNotFoundError | Run main_ui.py | Traceback pasted | Fix import path/class mismatch in tool package | Open |
> 
> This is the most important sheet for AI.
> 
> The **AI Instruction** column is the sauce. That column turns messy observations into actionable dev tasks.
> 
> ---
> 
> ### Sheet 3: `AI Work Queue`
> 
> This is the cleaned-up “what should Codex/Aider do next?” sheet.
> 
> | Work ID | Source Issue(s) | Priority | Task | Files/Area | Done Criteria | Assigned Tool | Status |
> |---|---|---|---|---|---|---|---|
> | WORK-001 | BUG-001 | P0 | Fix broken import for Directory Markmind Mapper | tools/system/sys_directory_markmind_mapper | App launches without ModuleNotFoundError | Codex/Aider | Ready |
> 
> This prevents AI from trying to solve every little thing at once.
> 
> ---
> 
> ### Sheet 4: `Retest Log`
> 
> After fixes, log whether the fix actually worked.
> 
> | Date | Issue ID | Fix Tested | Result | Notes | Retest Needed |
> |---|---|---|---|---|---|
> | 2026-05-17 | BUG-001 | Re-ran main_ui.py | Pass/Fail |  | Yes/No |
> 
> This protects you from the classic “AI said fixed but it broke three other things” nonsense.
> 
> ---
> 
> ## Priority system
> 
> Use these exactly:
> 
> | Priority | Meaning |
> |---|---|
> | P0 | App crashes, data loss, tool will not open |
> | P1 | Core workflow broken |
> | P2 | Confusing, ugly, slow, or annoying but usable |
> | P3 | Polish or future idea |
> 
> Rule: **AI only works P0/P1 first unless you deliberately override it.**
> 
> ---
> 
> ## Status options
> 
> For checklist:
> 
> - Not Tested
> - Pass
> - Fail
> - Blocked
> - Needs Retest
> 
> For issues:
> 
> - Open
> - Sent to AI
> - Fixed
> - Retest Needed
> - Closed
> - Deferred
> 
> ---
> 
> ## My recommendation for your actual workbook
> 
> Make one workbook called:
> 
> `2026-05-17_app_testing_tracker.xlsx`
> 
> Tabs:
> 
> 1. `Dashboard`
> 2. `Test Checklist`
> 3. `Issues`
> 4. `AI Work Queue`
> 5. `Retest Log`
> 6. `Ideas Backlog`
> 
> The **Dashboard** should show:
> 
> | Metric | Count |
> |---|---|
> | Total Issues |  |
> | P0 Open |  |
> | P1 Open |  |
> | Ready for AI |  |
> | Retest Needed |  |
> | Closed |  |
> 
> That gives you instant triage instead of spreadsheet soup.
> 
> ## Clean operating flow
> 
> 1. Test from the checklist.
> 2. Every failure becomes an issue.
> 3. Every real issue gets an AI instruction.
> 4. Top issues move to AI Work Queue.
> 5. After AI fixes, retest and close or reopen.
> 
> That’s the system. Clean, boring, effective — which is exactly what testing needs to be.

### User
> ok, got gemini working on that can you still give me a checklist in markdown for the momscare app specifically.

### Assistant
> Absolutely. Here’s a **MomCare app-specific QA checklist** you can paste into your notes, GitHub issue, Gemini, Codex, or your testing spreadsheet.
> 
> # MomCare App Testing Checklist
> 
> Date Tested:  
> Tester: Cody  
> App Version / Branch:  
> Device:  
> Browser / OS:  
> Environment: Local / Dev / Production  
> 
> ---
> 
> ## 1. App Startup & Access
> 
> - [ ] App opens without crashing.
> - [ ] No console errors appear on initial load.
> - [ ] App loads within a reasonable time.
> - [ ] User can access the main dashboard/home screen.
> - [ ] App works on desktop.
> - [ ] App works on mobile.
> - [ ] Layout does not break on small screens.
> - [ ] Navigation/menu is visible and usable.
> - [ ] Page refresh does not break the app.
> - [ ] Direct URL navigation works if applicable.
> 
> Notes:
> 
> ---
> 
> ## 2. Main Dashboard
> 
> - [ ] Dashboard clearly shows today’s care status.
> - [ ] Dashboard shows the current date.
> - [ ] Dashboard shows the caregiver name or active user if applicable.
> - [ ] Dashboard shows urgent/open care items.
> - [ ] Dashboard shows recent logs or last update.
> - [ ] Dashboard shows upcoming appointments or reminders.
> - [ ] Dashboard separates “urgent” from “routine.”
> - [ ] Dashboard is readable at a glance.
> - [ ] Dashboard does not feel cluttered.
> - [ ] Dashboard has clear buttons for adding new entries.
> 
> Notes:
> 
> ---
> 
> ## 3. Daily Care Log
> 
> - [ ] User can create a new daily care log.
> - [ ] Date defaults to today.
> - [ ] User can edit the date if needed.
> - [ ] User can add morning notes.
> - [ ] User can add afternoon notes.
> - [ ] User can add evening notes.
> - [ ] User can save partial entries.
> - [ ] User can edit saved entries.
> - [ ] User can delete or archive incorrect entries.
> - [ ] App confirms when an entry is saved.
> - [ ] App warns before deleting.
> - [ ] Saved logs appear in the correct order.
> - [ ] Logs do not duplicate after saving.
> - [ ] Required fields are clear.
> - [ ] Optional fields are clearly optional.
> 
> Notes:
> 
> ---
> 
> ## 4. Vitals Tracking
> 
> - [ ] User can enter blood pressure.
> - [ ] Blood pressure format is easy to understand.
> - [ ] User can enter heart rate.
> - [ ] User can enter oxygen saturation.
> - [ ] User can enter temperature.
> - [ ] User can enter glucose.
> - [ ] User can enter pain level.
> - [ ] User can mark whether vitals were taken before or after eating.
> - [ ] User can add notes about symptoms or context.
> - [ ] App handles missing vitals without crashing.
> - [ ] App flags unusual values visually, if that feature exists.
> - [ ] App does not provide unsafe medical advice.
> - [ ] Vitals save correctly.
> - [ ] Vitals display correctly in history.
> - [ ] Vitals can be edited if entered wrong.
> - [ ] Units are clear: °F, bpm, %, mg/dL, etc.
> 
> Notes:
> 
> ---
> 
> ## 5. Oxygen / Breathing Equipment Tracking
> 
> - [ ] User can record oxygen tubing check.
> - [ ] User can record whether tubing has kinks.
> - [ ] User can record oxygen tank count.
> - [ ] User can record full tanks.
> - [ ] User can record empty tanks.
> - [ ] User can record concentrator status if applicable.
> - [ ] User can record charger/battery status.
> - [ ] User can mark “needs reorder.”
> - [ ] App clearly shows low oxygen supply alerts if applicable.
> - [ ] App allows caregiver notes for breathing treatments.
> - [ ] App handles “not checked” without treating it as failure.
> 
> Notes:
> 
> ---
> 
> ## 6. Meals / Food / Intake
> 
> - [ ] User can log breakfast.
> - [ ] User can log lunch.
> - [ ] User can log dinner.
> - [ ] User can log snacks.
> - [ ] User can log drinks.
> - [ ] User can mark appetite: good / okay / poor.
> - [ ] User can note food reactions or stomach issues.
> - [ ] User can mark “after eating” when logging glucose.
> - [ ] Food entries save correctly.
> - [ ] Food history is easy to review.
> - [ ] App does not make the meal log too complicated.
> 
> Notes:
> 
> ---
> 
> ## 7. Hygiene / Bathroom / Personal Care
> 
> - [ ] User can log bathroom assistance.
> - [ ] User can log hygiene assistance.
> - [ ] User can use respectful wording, not demeaning labels.
> - [ ] User can log wipes/cleaning.
> - [ ] User can log clothing or bedding change if applicable.
> - [ ] User can mark “not needed.”
> - [ ] User can add private caregiver notes.
> - [ ] Entries are easy to complete quickly.
> - [ ] App avoids making routine care feel overly clinical.
> 
> Notes:
> 
> ---
> 
> ## 8. Safety Scan
> 
> - [ ] User can complete a daily safety scan.
> - [ ] Checklist includes kitchen.
> - [ ] Checklist includes living room.
> - [ ] Checklist includes bathroom path.
> - [ ] Checklist includes bedroom path.
> - [ ] Checklist includes oxygen tubing.
> - [ ] Checklist includes fall hazards.
> - [ ] Checklist includes clutter/laundry.
> - [ ] Checklist includes floor hazards.
> - [ ] User can mark each area as clear / needs attention / not checked.
> - [ ] User can add notes.
> - [ ] User can create follow-up tasks from safety issues.
> - [ ] Safety scan saves to the daily log.
> 
> Notes:
> 
> ---
> 
> ## 9. Tasks & Follow-Ups
> 
> - [ ] User can create a task.
> - [ ] User can assign a task category.
> - [ ] User can set priority.
> - [ ] User can set due date.
> - [ ] User can mark task as done.
> - [ ] User can edit task.
> - [ ] User can delete/archive task.
> - [ ] Tasks can be linked to appointments, care logs, or provider instructions.
> - [ ] Open tasks are visible on dashboard.
> - [ ] Completed tasks are still accessible in history.
> - [ ] App separates care tasks from admin tasks.
> - [ ] App separates urgent tasks from routine follow-ups.
> 
> Notes:
> 
> ---
> 
> ## 10. Appointments
> 
> - [ ] User can add an appointment.
> - [ ] User can enter appointment type.
> - [ ] User can enter provider/location.
> - [ ] User can enter date and time.
> - [ ] User can add prep notes.
> - [ ] User can add transportation notes.
> - [ ] User can add follow-up notes after appointment.
> - [ ] Appointment appears on dashboard or calendar view.
> - [ ] Appointment can be edited.
> - [ ] Appointment can be canceled/archived.
> - [ ] Appointment does not disappear after the date passes.
> - [ ] Past appointments are easy to review.
> 
> Notes:
> 
> ---
> 
> ## 11. Provider / MyChart Task Capture
> 
> - [ ] User can enter provider task manually.
> - [ ] User can paste copied MyChart/task text.
> - [ ] User can upload or attach screenshot/photo if supported.
> - [ ] User can categorize provider tasks.
> - [ ] User can mark task source: MyChart / provider / phone call / discharge papers / other.
> - [ ] User can mark urgency.
> - [ ] User can link provider task to Mom’s care record.
> - [ ] User can mark provider task as scheduled.
> - [ ] User can mark provider task as completed.
> - [ ] App preserves original text/source notes.
> 
> Notes:
> 
> ---
> 
> ## 12. Voice / Quick Capture
> 
> - [ ] User can quickly add a note without filling out a huge form.
> - [ ] User can capture messy real-life notes and clean them later.
> - [ ] User can add “quick note” from dashboard.
> - [ ] Quick notes are timestamped.
> - [ ] Quick notes can be converted into tasks.
> - [ ] Quick notes can be converted into care log entries.
> - [ ] Quick notes can be edited after capture.
> - [ ] App does not force perfection during capture.
> 
> Notes:
> 
> ---
> 
> ## 13. Search & History
> 
> - [ ] User can search care logs.
> - [ ] User can search tasks.
> - [ ] User can search appointments.
> - [ ] User can filter by date.
> - [ ] User can filter by category.
> - [ ] User can filter by status.
> - [ ] User can find a previous day’s log quickly.
> - [ ] User can review trends without hunting.
> - [ ] Search results are clear and readable.
> 
> Notes:
> 
> ---
> 
> ## 14. Reports / Export
> 
> - [ ] User can generate a daily summary.
> - [ ] User can generate a weekly summary.
> - [ ] User can generate an appointment prep summary.
> - [ ] User can export to Markdown.
> - [ ] User can export to PDF if supported.
> - [ ] Export includes date range.
> - [ ] Export includes vitals.
> - [ ] Export includes tasks.
> - [ ] Export includes appointments.
> - [ ] Export includes caregiver notes.
> - [ ] Export avoids clutter.
> - [ ] Export is readable by a provider/family member.
> - [ ] Export does not expose unnecessary private notes unless selected.
> 
> Notes:
> 
> ---
> 
> ## 15. Data Integrity
> 
> - [ ] Saved data persists after refresh.
> - [ ] Saved data persists after closing/reopening app.
> - [ ] Editing one entry does not change unrelated entries.
> - [ ] Deleting one entry does not delete unrelated data.
> - [ ] Duplicate records are not created accidentally.
> - [ ] Dates are stored correctly.
> - [ ] Times are stored correctly.
> - [ ] Empty fields do not break the app.
> - [ ] Special characters do not break saving.
> - [ ] Long notes do not break layout or database save.
> - [ ] App handles connection/database errors gracefully.
> 
> Notes:
> 
> ---
> 
> ## 16. Error Handling
> 
> - [ ] App shows useful error messages.
> - [ ] Error messages explain what went wrong.
> - [ ] Error messages tell user what to do next.
> - [ ] App does not expose raw technical errors to normal users unless in dev mode.
> - [ ] Failed saves are clearly shown.
> - [ ] User does not think something saved when it failed.
> - [ ] App protects against accidental duplicate submissions.
> - [ ] App handles invalid input without crashing.
> 
> Notes:
> 
> ---
> 
> ## 17. UI / UX Sanity Check
> 
> - [ ] Buttons are clearly labeled.
> - [ ] Forms are not too long.
> - [ ] Most common actions are easy to reach.
> - [ ] Text is readable.
> - [ ] Spacing is clean.
> - [ ] Important information is visually prioritized.
> - [ ] Urgent items stand out.
> - [ ] Routine items do not scream for attention.
> - [ ] Mobile layout is usable one-handed.
> - [ ] The app feels calm, not chaotic.
> - [ ] The app supports caregiver reality, not fantasy-office workflow.
> 
> Notes:
> 
> ---
> 
> ## 18. Accessibility & Low-Energy Use
> 
> - [ ] App can be used when caregiver is tired.
> - [ ] App can be used quickly during interruptions.
> - [ ] Labels are plain language.
> - [ ] Click/tap targets are large enough.
> - [ ] Color is not the only way status is shown.
> - [ ] Important items have text labels.
> - [ ] Forms can be completed in under 1–2 minutes where possible.
> - [ ] App does not require perfect typing.
> - [ ] App supports “capture now, organize later.”
> 
> Notes:
> 
> ---
> 
> ## 19. Privacy / Permissions
> 
> - [ ] Sensitive notes are not exposed on public screens.
> - [ ] Export does not include private notes by default.
> - [ ] User roles/permissions work if applicable.
> - [ ] Family-facing view is separate from caregiver/admin view if applicable.
> - [ ] App does not leak private data in console logs.
> - [ ] App does not store unnecessary sensitive data.
> - [ ] Backups/export files are named clearly.
> 
> Notes:
> 
> ---
> 
> ## 20. Final Retest Checklist
> 
> Use this after Gemini/Codex/Aider makes changes.
> 
> - [ ] App still starts.
> - [ ] Dashboard still loads.
> - [ ] Daily log still saves.
> - [ ] Vitals still save.
> - [ ] Tasks still save.
> - [ ] Appointments still save.
> - [ ] Search/history still works.
> - [ ] No new console errors.
> - [ ] Previous bug is fixed.
> - [ ] No obvious new bug was introduced.
> - [ ] Updated behavior matches the requested fix.
> - [ ] Documentation/notes were updated if behavior changed.
> 
> Notes:
> 
> ---
> 
> # Issue Capture Template
> 
> Use this every time something fails.
> 
> ## ISSUE-___ — Short title
> 
> Priority: P0 / P1 / P2 / P3  
> Type: Bug / UI / UX / Data / Performance / Feature / Safety / Export  
> Area: Dashboard / Daily Log / Vitals / Tasks / Appointments / Reports / Other  
> Status: Open / Sent to AI / Fixed / Retest Needed / Closed / Deferred  
> 
> ### Expected
> 
> What should have happened?
> 
> ### Actual
> 
> What happened instead?
> 
> ### Steps to Reproduce
> 
> 1.  
> 2.  
> 3.  
> 
> ### Evidence
> 
> Screenshot, traceback, console error, wrong output, broken layout, etc.
> 
> ### Impact
> 
> Why does this matter?
> 
> ### AI Instruction
> 
> Tell the AI exactly what to fix.
> 
> Example:
> 
> Fix the daily care log save behavior so entries persist after refresh. Do not change unrelated dashboard layout. Add a simple test or manual verification note showing that saved logs remain visible after reload.
> 
> ---
> 
> # AI Work Order Template
> 
> ## MomCare App Work Order
> 
> Goal:  
> Fix the highest-priority testing issues without redesigning unrelated parts of the app.
> 
> ## Rules
> 
> - Fix P0 and P1 issues first.
> - Do not refactor unrelated architecture.
> - Do not rename fields unless required.
> - Preserve existing data structure unless a migration is necessary.
> - Keep forms fast and caregiver-friendly.
> - Update documentation if behavior changes.
> - Summarize files changed, fixes made, and how to retest.
> 
> ## Issues to Fix
> 
> 1.  
> 2.  
> 3.  
> 
> ## Done Criteria
> 
> - App launches.
> - Core care log flow works.
> - Vitals/tasks/appointments save correctly.
> - No new obvious console errors.
> - Retest checklist passes.

### User
> how do i make them be checkmarks in obsidian

### Assistant
> In Obsidian, checkboxes are just Markdown task list items.
> 
> Use this format:
> 
> ```md
> - [ ] App opens without crashing.
> - [ ] Dashboard loads.
> - [ ] Daily care log saves.
> - [ ] Vitals save correctly.
> ```
> 
> After Obsidian renders it, those become clickable checkboxes.
> 
> When checked, Obsidian changes them to:
> 
> ```md
> - [x] App opens without crashing.
> ```
> 
> ## Important spacing
> 
> This works:
> 
> ```md
> - [ ] Task here
> ```
> 
> This may not work right:
> 
> ```md
> -[ ] Task here
> - [] Task here
> - [ ]Task here
> ```
> 
> The exact pattern is:
> 
> `dash space left-bracket space right-bracket space text`
> 
> ## For your MomCare checklist
> 
> Use:
> 
> ```md
> ## App Startup & Access
> 
> - [ ] App opens without crashing.
> - [ ] No console errors appear on initial load.
> - [ ] App loads within a reasonable time.
> - [ ] User can access the main dashboard/home screen.
> - [ ] App works on desktop.
> - [ ] App works on mobile.
> ```
> 
> Tiny but useful: in Obsidian, you can also toggle a line into a checkbox with the command palette: **Ctrl+P → Toggle checkbox status**.

### User
> i needed this in obsidian markdown.

### Assistant
> Yep — my bad. Here’s the **Obsidian-ready Markdown checklist** version. Paste this directly into Obsidian and the checkboxes will render.
> 
> # MomCare App QA Checklist
> 
> **Date Tested:**  
> **Tester:** Cody  
> **App Version / Branch:**  
> **Device:**  
> **Browser / OS:**  
> **Environment:** Local / Dev / Production  
> 
> ---
> 
> ## 1. App Startup & Access
> 
> - [ ] App opens without crashing.
> - [ ] No console errors appear on initial load.
> - [ ] App loads within a reasonable time.
> - [ ] User can access the main dashboard/home screen.
> - [ ] App works on desktop.
> - [ ] App works on mobile.
> - [ ] Layout does not break on small screens.
> - [ ] Navigation/menu is visible and usable.
> - [ ] Page refresh does not break the app.
> - [ ] Direct URL navigation works if applicable.
> 
> ### Notes
> 
> ---
> 
> ## 2. Main Dashboard
> 
> - [ ] Dashboard clearly shows today’s care status.
> - [ ] Dashboard shows the current date.
> - [ ] Dashboard shows the caregiver name or active user if applicable.
> - [ ] Dashboard shows urgent/open care items.
> - [ ] Dashboard shows recent logs or last update.
> - [ ] Dashboard shows upcoming appointments or reminders.
> - [ ] Dashboard separates urgent from routine.
> - [ ] Dashboard is readable at a glance.
> - [ ] Dashboard does not feel cluttered.
> - [ ] Dashboard has clear buttons for adding new entries.
> 
> ### Notes
> 
> ---
> 
> ## 3. Daily Care Log
> 
> - [ ] User can create a new daily care log.
> - [ ] Date defaults to today.
> - [ ] User can edit the date if needed.
> - [ ] User can add morning notes.
> - [ ] User can add afternoon notes.
> - [ ] User can add evening notes.
> - [ ] User can save partial entries.
> - [ ] User can edit saved entries.
> - [ ] User can delete or archive incorrect entries.
> - [ ] App confirms when an entry is saved.
> - [ ] App warns before deleting.
> - [ ] Saved logs appear in the correct order.
> - [ ] Logs do not duplicate after saving.
> - [ ] Required fields are clear.
> - [ ] Optional fields are clearly optional.
> 
> ### Notes
> 
> ---
> 
> ## 4. Vitals Tracking
> 
> - [ ] User can enter blood pressure.
> - [ ] Blood pressure format is easy to understand.
> - [ ] User can enter heart rate.
> - [ ] User can enter oxygen saturation.
> - [ ] User can enter temperature.
> - [ ] User can enter glucose.
> - [ ] User can enter pain level.
> - [ ] User can mark whether vitals were taken before or after eating.
> - [ ] User can add notes about symptoms or context.
> - [ ] App handles missing vitals without crashing.
> - [ ] App flags unusual values visually, if that feature exists.
> - [ ] App does not provide unsafe medical advice.
> - [ ] Vitals save correctly.
> - [ ] Vitals display correctly in history.
> - [ ] Vitals can be edited if entered wrong.
> - [ ] Units are clear: °F, bpm, %, mg/dL, etc.
> 
> ### Notes
> 
> ---
> 
> ## 5. Oxygen / Breathing Equipment Tracking
> 
> - [ ] User can record oxygen tubing check.
> - [ ] User can record whether tubing has kinks.
> - [ ] User can record oxygen tank count.
> - [ ] User can record full tanks.
> - [ ] User can record empty tanks.
> - [ ] User can record concentrator status if applicable.
> - [ ] User can record charger/battery status.
> - [ ] User can mark needs reorder.
> - [ ] App clearly shows low oxygen supply alerts if applicable.
> - [ ] App allows caregiver notes for breathing treatments.
> - [ ] App handles not checked without treating it as failure.
> 
> ### Notes
> 
> ---
> 
> ## 6. Meals / Food / Intake
> 
> - [ ] User can log breakfast.
> - [ ] User can log lunch.
> - [ ] User can log dinner.
> - [ ] User can log snacks.
> - [ ] User can log drinks.
> - [ ] User can mark appetite: good / okay / poor.
> - [ ] User can note food reactions or stomach issues.
> - [ ] User can mark after eating when logging glucose.
> - [ ] Food entries save correctly.
> - [ ] Food history is easy to review.
> - [ ] App does not make the meal log too complicated.
> 
> ### Notes
> 
> ---
> 
> ## 7. Hygiene / Bathroom / Personal Care
> 
> - [ ] User can log bathroom assistance.
> - [ ] User can log hygiene assistance.
> - [ ] User can use respectful wording, not demeaning labels.
> - [ ] User can log wipes/cleaning.
> - [ ] User can log clothing or bedding change if applicable.
> - [ ] User can mark not needed.
> - [ ] User can add private caregiver notes.
> - [ ] Entries are easy to complete quickly.
> - [ ] App avoids making routine care feel overly clinical.
> 
> ### Notes
> 
> ---
> 
> ## 8. Safety Scan
> 
> - [ ] User can complete a daily safety scan.
> - [ ] Checklist includes kitchen.
> - [ ] Checklist includes living room.
> - [ ] Checklist includes bathroom path.
> - [ ] Checklist includes bedroom path.
> - [ ] Checklist includes oxygen tubing.
> - [ ] Checklist includes fall hazards.
> - [ ] Checklist includes clutter/laundry.
> - [ ] Checklist includes floor hazards.
> - [ ] User can mark each area as clear / needs attention / not checked.
> - [ ] User can add notes.
> - [ ] User can create follow-up tasks from safety issues.
> - [ ] Safety scan saves to the daily log.
> 
> ### Notes
> 
> ---
> 
> ## 9. Tasks & Follow-Ups
> 
> - [ ] User can create a task.
> - [ ] User can assign a task category.
> - [ ] User can set priority.
> - [ ] User can set due date.
> - [ ] User can mark task as done.
> - [ ] User can edit task.
> - [ ] User can delete/archive task.
> - [ ] Tasks can be linked to appointments, care logs, or provider instructions.
> - [ ] Open tasks are visible on dashboard.
> - [ ] Completed tasks are still accessible in history.
> - [ ] App separates care tasks from admin tasks.
> - [ ] App separates urgent tasks from routine follow-ups.
> 
> ### Notes
> 
> ---
> 
> ## 10. Appointments
> 
> - [ ] User can add an appointment.
> - [ ] User can enter appointment type.
> - [ ] User can enter provider/location.
> - [ ] User can enter date and time.
> - [ ] User can add prep notes.
> - [ ] User can add transportation notes.
> - [ ] User can add follow-up notes after appointment.
> - [ ] Appointment appears on dashboard or calendar view.
> - [ ] Appointment can be edited.
> - [ ] Appointment can be canceled/archived.
> - [ ] Appointment does not disappear after the date passes.
> - [ ] Past appointments are easy to review.
> 
> ### Notes
> 
> ---
> 
> ## 11. Provider / MyChart Task Capture
> 
> - [ ] User can enter provider task manually.
> - [ ] User can paste copied MyChart/task text.
> - [ ] User can upload or attach screenshot/photo if supported.
> - [ ] User can categorize provider tasks.
> - [ ] User can mark task source: MyChart / provider / phone call / discharge papers / other.
> - [ ] User can mark urgency.
> - [ ] User can link provider task to Mom’s care record.
> - [ ] User can mark provider task as scheduled.
> - [ ] User can mark provider task as completed.
> - [ ] App preserves original text/source notes.
> 
> ### Notes
> 
> ---
> 
> ## 12. Voice / Quick Capture
> 
> - [ ] User can quickly add a note without filling out a huge form.
> - [ ] User can capture messy real-life notes and clean them later.
> - [ ] User can add quick note from dashboard.
> - [ ] Quick notes are timestamped.
> - [ ] Quick notes can be converted into tasks.
> - [ ] Quick notes can be converted into care log entries.
> - [ ] Quick notes can be edited after capture.
> - [ ] App does not force perfection during capture.
> 
> ### Notes
> 
> ---
> 
> ## 13. Search & History
> 
> - [ ] User can search care logs.
> - [ ] User can search tasks.
> - [ ] User can search appointments.
> - [ ] User can filter by date.
> - [ ] User can filter by category.
> - [ ] User can filter by status.
> - [ ] User can find a previous day’s log quickly.
> - [ ] User can review trends without hunting.
> - [ ] Search results are clear and readable.
> 
> ### Notes
> 
> ---
> 
> ## 14. Reports / Export
> 
> - [ ] User can generate a daily summary.
> - [ ] User can generate a weekly summary.
> - [ ] User can generate an appointment prep summary.
> - [ ] User can export to Markdown.
> - [ ] User can export to PDF if supported.
> - [ ] Export includes date range.
> - [ ] Export includes vitals.
> - [ ] Export includes tasks.
> - [ ] Export includes appointments.
> - [ ] Export includes caregiver notes.
> - [ ] Export avoids clutter.
> - [ ] Export is readable by a provider/family member.
> - [ ] Export does not expose unnecessary private notes unless selected.
> 
> ### Notes
> 
> ---
> 
> ## 15. Data Integrity
> 
> - [ ] Saved data persists after refresh.
> - [ ] Saved data persists after closing/reopening app.
> - [ ] Editing one entry does not change unrelated entries.
> - [ ] Deleting one entry does not delete unrelated data.
> - [ ] Duplicate records are not created accidentally.
> - [ ] Dates are stored correctly.
> - [ ] Times are stored correctly.
> - [ ] Empty fields do not break the app.
> - [ ] Special characters do not break saving.
> - [ ] Long notes do not break layout or database save.
> - [ ] App handles connection/database errors gracefully.
> 
> ### Notes
> 
> ---
> 
> ## 16. Error Handling
> 
> - [ ] App shows useful error messages.
> - [ ] Error messages explain what went wrong.
> - [ ] Error messages tell user what to do next.
> - [ ] App does not expose raw technical errors to normal users unless in dev mode.
> - [ ] Failed saves are clearly shown.
> - [ ] User does not think something saved when it failed.
> - [ ] App protects against accidental duplicate submissions.
> - [ ] App handles invalid input without crashing.
> 
> ### Notes
> 
> ---
> 
> ## 17. UI / UX Sanity Check
> 
> - [ ] Buttons are clearly labeled.
> - [ ] Forms are not too long.
> - [ ] Most common actions are easy to reach.
> - [ ] Text is readable.
> - [ ] Spacing is clean.
> - [ ] Important information is visually prioritized.
> - [ ] Urgent items stand out.
> - [ ] Routine items do not scream for attention.
> - [ ] Mobile layout is usable one-handed.
> - [ ] The app feels calm, not chaotic.
> - [ ] The app supports caregiver reality, not fantasy-office workflow.
> 
> ### Notes
> 
> ---
> 
> ## 18. Accessibility & Low-Energy Use
> 
> - [ ] App can be used when caregiver is tired.
> - [ ] App can be used quickly during interruptions.
> - [ ] Labels are plain language.
> - [ ] Click/tap targets are large enough.
> - [ ] Color is not the only way status is shown.
> - [ ] Important items have text labels.
> - [ ] Forms can be completed in under 1–2 minutes where possible.
> - [ ] App does not require perfect typing.
> - [ ] App supports capture now, organize later.
> 
> ### Notes
> 
> ---
> 
> ## 19. Privacy / Permissions
> 
> - [ ] Sensitive notes are not exposed on public screens.
> - [ ] Export does not include private notes by default.
> - [ ] User roles/permissions work if applicable.
> - [ ] Family-facing view is separate from caregiver/admin view if applicable.
> - [ ] App does not leak private data in console logs.
> - [ ] App does not store unnecessary sensitive data.
> - [ ] Backups/export files are named clearly.
> 
> ### Notes
> 
> ---
> 
> ## 20. Final Retest Checklist
> 
> - [ ] App still starts.
> - [ ] Dashboard still loads.
> - [ ] Daily log still saves.
> - [ ] Vitals still save.
> - [ ] Tasks still save.
> - [ ] Appointments still save.
> - [ ] Search/history still works.
> - [ ] No new console errors.
> - [ ] Previous bug is fixed.
> - [ ] No obvious new bug was introduced.
> - [ ] Updated behavior matches the requested fix.
> - [ ] Documentation/notes were updated if behavior changed.
> 
> ### Notes
> 
> ---
> 
> # Issue Capture Template
> 
> ## ISSUE-000 — Short Title
> 
> **Priority:** P0 / P1 / P2 / P3  
> **Type:** Bug / UI / UX / Data / Performance / Feature / Safety / Export  
> **Area:** Dashboard / Daily Log / Vitals / Tasks / Appointments / Reports / Other  
> **Status:** Open / Sent to AI / Fixed / Retest Needed / Closed / Deferred  
> 
> ### Expected
> 
> What should have happened?
> 
> ### Actual
> 
> What happened instead?
> 
> ### Steps to Reproduce
> 
> - [ ] Step 1
> - [ ] Step 2
> - [ ] Step 3
> 
> ### Evidence
> 
> Screenshot, traceback, console error, wrong output, broken layout, etc.
> 
> ### Impact
> 
> Why does this matter?
> 
> ### AI Instruction
> 
> Tell the AI exactly what to fix.
> 
> Example:
> 
> Fix the daily care log save behavior so entries persist after refresh. Do not change unrelated dashboard layout. Add a simple test or manual verification note showing that saved logs remain visible after reload.
> 
> ---
> 
> # AI Work Order Template
> 
> ## MomCare App Work Order
> 
> **Goal:**  
> Fix the highest-priority testing issues without redesigning unrelated parts of the app.
> 
> ## Rules
> 
> - [ ] Fix P0 and P1 issues first.
> - [ ] Do not refactor unrelated architecture.
> - [ ] Do not rename fields unless required.
> - [ ] Preserve existing data structure unless a migration is necessary.
> - [ ] Keep forms fast and caregiver-friendly.
> - [ ] Update documentation if behavior changes.
> - [ ] Summarize files changed, fixes made, and how to retest.
> 
> ## Issues to Fix
> 
> - [ ] ISSUE-001:
> - [ ] ISSUE-002:
> - [ ] ISSUE-003:
> 
> ## Done Criteria
> 
> - [ ] App launches.
> - [ ] Core care log flow works.
> - [ ] Vitals/tasks/appointments save correctly.
> - [ ] No new obvious console errors.
> - [ ] Retest checklist passes.

### User
> this looks the same just make the file for me to download.

### Assistant
> Got you — I’ll make the actual `.md` file so you can drop it straight into Obsidian instead of fighting the formatting in chat.

### Assistant
> Done — here’s the Obsidian-ready Markdown file:
> 
> [Download the MomCare App QA Checklist](sandbox:/mnt/data/2026-05-17_momcare_app_qa_checklist.md)

### User
> what about one for qiaccess start.

### Assistant
> Absolutely — QiAccess Start needs its own checklist because it is not just an app; it’s the front door/control panel for your whole local system. I’ll make this as an Obsidian-ready `.md` file with checkboxes, issue capture, and AI work-order sections.

### Assistant
> Done — here’s the Obsidian-ready QA checklist for QiAccess Start:
> 
> [Download the QiAccess Start QA Checklist](sandbox:/mnt/data/2026-05-17_qiaccess_start_qa_checklist.md)
