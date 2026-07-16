---
layout: page
title: "Tech stack for PDF forms"
slug: "tech_stack_for_pdf_forms"
created_at: "2025-09-20 07:45:33"
updated_at: "2025-09-20 07:45:33"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-000.json"
template_key: master-template
date: 2025-09-20
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "68cea1c5-2bf8-8331-bad7-2e475fbf1c88"
canonical_ref: ""
---

# Tech stack for PDF forms

## Overview
- **Date**: 2025-09-20 07:45:33
- **Conversation ID**: `68cea1c5-2bf8-8331-bad7-2e475fbf1c88`
- **Source**: `Chat-Export-28513-2026/conversations-000.json`

## Chat History

### User
> ok real quick we need to talk about my tech stack , i need a pdf filler form creator and workflow where i can send out a questionnaire that pre fills pdf forms for immigration and such is there open sources or something we can piece together.

### Assistant
> Short answer: yes, we can stitch this together without selling our souls to a pricey SaaS. Longer answer below, with a clean MVP you can ship, and a future-proof path when you want automations and branching logic.
> 
> # Two-tier plan
> 
> ## 1) Bare fix (fastest path that actually works)
> **Stack:**  
> - **Questionnaire UI:** `react-jsonschema-form` (JSON-schema forms, easy validation) citeturn0search3turn0search8  
> - **PDF fill + e-signature:** **DocuSeal** (open source, self-hosted or cloud, API to prefill fields, workflows, signer roles) citeturn0search10turn0search5  
> - **DB:** Supabase (store submissions + person/org)  
> - **Orchestration:** n8n or a tiny Worker to call DocuSeal’s API  
> - **Hosting:** Cloudflare Pages/Workers, because that’s your religion now.
> 
> **Why this works:** many USCIS PDFs are a mess. Some are standard **AcroForms**, others are **XFA** (Adobe’s weird, half-proprietary format). Most FOSS libraries struggle with XFA. DocuSeal sidesteps that by letting you overlay your own fields on top of the PDF and prefill/sign via API, so you don’t care what the original field names were. citeturn0search26turn0search9turn0search4
> 
> **Flow:**
> 1. Build your intake form as JSON Schema.
> 2. Save the response in Supabase.
> 3. Call DocuSeal API with a **template_id** and a **prefill map** derived from the schema output.
> 4. DocuSeal emails the client a secure link, they review, edit any prefilled items, sign, done. citeturn0search5
> 
> **What you avoid:** fighting with XFA field names, PDF quirks, and hand-rolled signature logic.
> 
> ---
> 
> ## 2) Upgrade/future-proof (branching interviews, complex logic, multi-doc bundles)
> **Stack option:** **docassemble**. It’s the open-source standard in legal for guided interviews that assemble PDFs/DOCX, email, multi-language, the works. It’s heavier than the Bare Fix, but perfect when you need branching logic, multiple forms in one flow, conditional exhibits, etc. citeturn0search11turn0search1turn0search6turn0search15
> 
> **Alternate form builder:** **Form.io** if you want a drag-and-drop, self-hosted form builder and API for enterprise-y workflows. It’s open source, Dockerable, and plays fine with your stack. citeturn0search7turn0search12turn0search24
> 
> ---
> 
> # MVP you can stand up today
> 
> ## A. Define the questionnaire
> Use `react-jsonschema-form` so you don’t waste time on React state drama.
> 
> Schema sketch:
> ```json
> {
>   "title": "USCIS Intake",
>   "type": "object",
>   "required": ["fullName", "dob", "aNumber", "address"],
>   "properties": {
>     "fullName": { "type": "string", "title": "Full legal name" },
>     "dob": { "type": "string", "format": "date", "title": "Date of birth" },
>     "aNumber": { "type": "string", "title": "A-Number" },
>     "address": {
>       "type": "object",
>       "required": ["line1","city","state","zip"],
>       "properties": {
>         "line1": { "type": "string", "title": "Street" },
>         "line2": { "type": "string", "title": "Apt/Unit" },
>         "city": { "type": "string" },
>         "state": { "type": "string" },
>         "zip": { "type": "string" }
>       }
>     }
>   }
> }
> ```
> Docs for rjsf: playground and guide. citeturn0search17turn0search8
> 
> ## B. Create a fillable template in DocuSeal
> 1. Upload the official PDF (e.g., I-589).  
> 2. Drag overlays for each field you want, name them with sane keys like `client.full_name`, `client.address.city`.  
> 3. Save as a template and note the `template_id`.  
> DocuSeal on-prem and features: citeturn0search5turn0search10
> 
> ## C. Map questionnaire → DocuSeal prefill
> Create a little mapping JSON so you can reuse it across forms:
> ```json
> {
>   "client.full_name": "fullName",
>   "client.dob": "dob",
>   "client.a_number": "aNumber",
>   "client.address.street": "address.line1",
>   "client.address.city": "address.city",
>   "client.address.state": "address.state",
>   "client.address.zip": "address.zip"
> }
> ```
> 
> ## D. Cloudflare Worker to generate a packet
> Pseudocode outline:
> ```js
> export default {
>   async fetch(req, env) {
>     if (req.method !== "POST") return new Response("Nope.", { status: 405 });
> 
>     const body = await req.json();       // rjsf submission
>     const mapping = env.I589_MAPPING;    // JSON string in KV or env
>     const m = JSON.parse(mapping);
> 
>     // flatten submission and map to DocuSeal fields
>     const flat = flatten(body);          // write a tiny flatten(obj) helper
>     const prefill = Object.fromEntries(
>       Object.entries(m).map(([docusealKey, schemaPath]) => [docusealKey, get(flat, schemaPath)])
>     );
> 
>     const payload = {
>       template_id: env.DOCUSEAL_TEMPLATE_ID,
>       recipients: [{ email: body.contactEmail, role: "Client" }],
>       fields: prefill
>     };
> 
>     const resp = await fetch("https://api.docuseal.com/v1/submissions", {
>       method: "POST",
>       headers: {
>         "Authorization": `Bearer ${env.DOCUSEAL_API_KEY}`,
>         "Content-Type": "application/json"
>       },
>       body: JSON.stringify(payload)
>     });
> 
>     if (!resp.ok) return new Response(await resp.text(), { status: 500 });
>     return new Response(JSON.stringify(await resp.json()), { headers: { "Content-Type": "application/json" }});
>   }
> };
> ```
> DocuSeal’s API supports creating submissions with prefilled fields and auto-emails the signer. citeturn0search5
> 
> ## E. Storage and audit trail
> - Save the rjsf submission and the returned DocuSeal submission ID in Supabase for traceability.
> - Webhook from DocuSeal on “completed” to store the signed PDF and a JSON receipt.
> 
> ---
> 
> # Notes on immigration PDFs, because they’re chaos in a trench coat
> - **Two PDF species exist:** AcroForms (standard) and **XFA** (Adobe’s special). Many immigration forms still use or used XFA. Most open-source PDF libraries don’t fill XFA reliably. That’s why overlay-and-prefill via DocuSeal is the path of least pain. citeturn0search26turn0search9
> - If you insist on code-level filling: `pdf-lib`/PyPDF2 handle **AcroForms** nicely, not XFA. You’ll end up flattening or overlaying anyway. Enjoy your weekend.  
> - If a particular USCIS form is stubborn, upload it to DocuSeal and ignore the native fields; place your own overlays and pass values by API. Done.
> 
> ---
> 
> # When you outgrow the MVP
> - **docassemble**: one-question-at-a-time interviews, logic trees, multiple document outputs, email, multilingual, and can still spit out PDFs from templates. It’s the legal tech workhorse. citeturn0search11turn0search1
> - **Form.io**: drag-and-drop form builder you can self-host; great if non-devs need to author forms and you want a native data API. citeturn0search7turn0search12
> 
> ---
> 
> # Quick pick for you
> You’re Cloudflare-first and need results now. Do this:
> 1. rjsf questionnaire on **Pages**. citeturn0search8  
> 2. Store JSON in Supabase.  
> 3. **DocuSeal** for templating + signatures. Prefill via a **Worker**. citeturn0search5  
> 4. n8n optional for email + file routing.
> 
> That gets you a clean, repeatable pipeline: intake → prefill → sign → archive. Minimal drama, maximum throughput. If you want the branching/interview magic later, bolt in docassemble and migrate form definitions when you’re bored.
> 
> Snap out: you don’t need ten tools and a headache. Ship the MVP above, then we can layer the clever stuff.

### User
> i hate docker it never works for me. can i still use docassemble?

### Assistant
> Yes, but you’re going to need to get a little crafty because docassemble is married to Docker by default. It’s a Python monster under the hood (Flask + Celery + PostgreSQL), so Docker is just the “please don’t scream at me while I install 50 dependencies” wrapper. If Docker makes you want to set fire to your laptop, you’ve got a few options:
> 
> ---
> 
> ## 1) Bare-metal or VM install (no Docker)
> You can run docassemble directly on:
> - **Ubuntu/Debian** with `apt install` + `pip install` (they actually have a no-Docker guide).
> - PostgreSQL + Redis manually installed.
> - `pip install docassemble` and configure `config.yml` yourself.
> - You’ll need to run Gunicorn or uWSGI + Nginx, and set up background workers for interviews and email.
> 
> This gives you full control and zero Docker layers, but you are now your own sysadmin. It’s doable if you like tinkering.
> 
> ---
> 
> ## 2) Lightweight VPS + Prebuilt Image
> Instead of Docker, spin up a cheap VM (DigitalOcean, Linode, whatever), install the packages above, and keep it isolated. This way, if it melts down, you just snapshot/restore the VM and move on.
> 
> ---
> 
> ## 3) Don’t self-host — Use their free or paid hosted version
> Docassemble has a community demo server and multiple hosted offerings (like Community.Lawyer and CourtFormsOnline clones). You get all the docassemble logic, none of the sysadmin pain. If uptime and backups matter more than root access, just pay the $20–50/month.
> 
> ---
> 
> ## 4) If you just want the “guided interview → PDF” part
> Skip docassemble entirely and:
> - Use `react-jsonschema-form` for the questionnaire.
> - Save the responses to Supabase.
> - Merge into a PDF template with `pdf-lib` or `pdfrw` (or even DocuSeal’s prefill API like we just discussed).
> - Serve via Cloudflare Worker.  
> This is less magic but less overhead — no Docker, no Celery, no maintenance.
> 
> ---
> 
> ## My honest take for you
> You’re already Cloudflare + Supabase — skip Docker and full docassemble unless you need:
> - branching logic interviews  
> - multi-doc bundles  
> - automated emailing  
> - courtroom-grade audit trails  
> 
> If you just need to prefill USCIS forms and send them out, DocuSeal + your existing stack will do it with 10% of the overhead. If you later decide you need docassemble-style logic, we can spin up a tiny Ubuntu VM and install it bare-metal — it’s not pretty, but it works.
> 
> Would you like me to write you a **bare-metal install checklist** for docassemble so you can skip Docker entirely and not get lost in dependency hell?

### User
> i need full on interviews and logics that spit out the final pdfs ready to go at teh end and maybe pipe into opensource type e sign too.

### Assistant
> If you want real interviews with branching logic that spit out final PDFs and then kick to an open-source e-sign tool, that’s literally docassemble’s home turf. Docker isn’t required; it’s just the training wheels they push so fewer people rage-quit mid-install. You can run it on a plain Ubuntu VM and glue in an open-source signer like DocuSeal. Yes, it’s work. No, it’s not black magic.
> 
> # Stack that fits your ask
> - **Interviews & logic:** **docassemble** (one-question-at-a-time flows, variables, conditions, multilingual, file bundles) citeturn0search1turn0search17  
> - **PDF generation:** docassemble templates (PDF overlay or DOCX → PDF), with tools for overflow text and multi-doc bundles via AssemblyLine add-ons citeturn0search6turn0search12  
> - **E-sign (open source):**  
>   - **DocuSeal** (modern, active, API for prefill + signer roles) citeturn0search2turn0search13turn0search18  
>   - Alternates: **Open eSignForms** (older but OSS) or **OpenSign** or **LibreSign** (Nextcloud app) if you already run Nextcloud. DocuSeal is the least headache. citeturn0search3turn0search19turn0search10turn0search15
> 
> # Deploy without Docker, fine
> Docassemble’s own docs admit you can install sans Docker; you’ll manage Python deps, Postgres, Redis, Gunicorn/uWSGI, and workers. If you’d rather not become a part-time SRE, use a small VM and snapshot it. citeturn0search0turn0search5
> 
> # Minimal working architecture
> 1) **VM**: Ubuntu 22.04, Nginx, Postgres, Redis.  
> 2) **docassemble**: bare-metal install; store your interviews and templates. citeturn0search5  
> 3) **Document assembly**: use DOCX templates for sane text handling, or PDF overlays when you need exact USCIS layouts; AssemblyLine helpers for multi-doc sets and overflow handling. citeturn0search6turn0search12  
> 4) **Signing**: when the interview completes, call DocuSeal’s API to create a submission, prefill fields, and email the signer. Save the submission ID and final signed PDF back to your storage. citeturn0search13
> 
> # Example: docassemble interview → PDF → DocuSeal
> Here’s the shape, not the full novel.
> 
> **1) Simple interview block (YAML)**
> ```yaml
> ---
> question: Your full legal name
> fields:
>   - Full name: user_name
>     datatype: text
> ---
> question: Date of birth
> fields:
>   - DOB: user_dob
>     datatype: date
> ---
> question: A-Number
> fields:
>   - A-Number: a_number
>     datatype: text
> ---
> mandatory: True
> code: |
>   # decide which documents to assemble and then trigger signing
>   final_doc = docx_template("i589_cover.docx")
>   # If you must match an exact USCIS PDF, use a PDF template and field mapping
>   # pdf_template_file = pdf_template("I-589.pdf")
> ```
> 
> **2) Template binding**
> - DOCX route gives you robust text handling; docassemble injects variables directly. PDF overlays require explicit field maps; AssemblyLine adds utilities for overflow and multi-document bundles. citeturn0search6turn0search12
> 
> **3) Hand-off to DocuSeal (Python block inside the interview)**
> ```yaml
> ---
> code: |
>   import requests, json
>   payload = {
>     "template_id": int(os.getenv("DOCUSEAL_TEMPLATE_ID")),
>     "recipients": [{"email": user_email, "role": "Client"}],
>     "fields": {
>       "client.full_name": user_name,
>       "client.dob": str(user_dob),
>       "client.a_number": a_number
>     }
>   }
>   r = requests.post(
>     "https://api.docuseal.com/submissions",
>     headers={"Authorization": f"Bearer {os.getenv('DOCUSEAL_API_KEY')}",
>              "Content-Type": "application/json"},
>     data=json.dumps(payload),
>     timeout=30
>   )
>   r.raise_for_status()
>   signing_info = r.json()
> ```
> DocuSeal’s API expects a template, recipients, and a prefill map; it emails the signer and tracks completion. You get webhooks for status and a final signed PDF. citeturn0search13
> 
> # Bare-metal install checklist (no Docker)
> - Create VM, add swap, system updates.  
> - Install Nginx, Certbot, Postgres, Redis.  
> - Install Python 3.10+, pipx/virtualenv, LibreOffice + unoconv (for DOCX→PDF), pandoc if needed.  
> - `pip install docassemble` and configure `config.yml` to point at Postgres/Redis, email settings, and file storage.  
> - Run Gunicorn/uWSGI for the web app, Supervisor/systemd for background workers.  
> - Backups: nightly Postgres dump + rsync the files directory.  
> Docassemble’s docs cover non-Docker guidance, even if they keep nagging you to use Docker. citeturn0search5
> 
> # Why this beats hand-rolled PDFs
> - You get proper branching logic, validation, multi-document bundles, and “download/email the whole packet” screens out of the box. AssemblyLine’s helpers solve dumb PDF quirks like text overflow. citeturn0search12  
> - Then you punt signatures to a purpose-built, open source signer instead of reinventing that wheel with duct tape. DocuSeal is actively maintained and has a clean API. citeturn0search2turn0search18
> 
> # If you refuse DocuSeal
> You can try **Open eSignForms** or **OpenSign**. They’re viable, just rougher around the edges. **LibreSign** works if you already run Nextcloud and want signatures inside that ecosystem. Translation: DocuSeal is the least drama. citeturn0search3turn0search19turn0search10
> 
> # Quick start order (aka “do this and stop overthinking it”)
> 1. Stand up docassemble on a fresh Ubuntu VM; confirm you can run a hello-world interview. citeturn0search5  
> 2. Build one clean I-589 intake interview that outputs: cover letter DOCX and a PDF overlay for the official form. citeturn0search6  
> 3. In DocuSeal, upload the I-589 PDF, overlay fields with sane keys, and note the `template_id`. citeturn0search18  
> 4. From docassemble’s final screen, POST to DocuSeal with your variable map; store the submission ID; listen for completion webhook and archive the signed PDF. citeturn0search13  
> 5. Repeat for your other immigration packets. Use AssemblyLine to bundle multi-form outputs and manage overflow text elegantly. citeturn0search12
> 
> You get guided interviews, deterministic PDFs, and open-source e-sign, all without Docker tantrums. Ship the first flow, then we can layer on client portals and automated evidence checklists.

### User
> ok lets put this together and see how we tie it into qiEos for admin electron creation and push to clients portals as tasks.

### Assistant
> Fine. We’re building the “Interview → PDFs → e-sign → task to client → tracked in QiEOS” conveyor belt. No Docker tantrums, Cloudflare-first, Supabase brain, Electron for admin. Here’s the clean MVP and the upgrade path.
> 
> # Two-tier plan
> 
> ## 1) Bare fix (ship today)
> Pipeline: **docassemble VM** → **Cloudflare Worker API** → **Supabase** → **Client Portal task** → **DocuSeal e-sign** → **webhooks back to Supabase** → **notify admin in QiEOS**.
> 
> ## 2) Upgrade (bundles, branching, SLAs)
> Same spine, plus AssemblyLine bundles, multi-form packets, retry queues, and role-based workflows across orgs.
> 
> ---
> 
> # Architecture (MVP)
> 
> ```
> [Admin Electron (QiEOS)]
>       ↓ create task/interview
> [Cloudflare Worker: /admin/create_interview]
>       ↓ writes
> [Supabase: tasks, interviews, packets]
>       ↓ returns launch_url
> [Client Portal (React/Vite)]
>       ↓ user clicks "Start"
> [docassemble (Ubuntu VM, no Docker)]
>       ↓ completes interview → builds PDFs
> [Cloudflare Worker: /handoff/sign]
>       ↓ calls
> [DocuSeal: submission + signer email]
>       ↓ webhook
> [Cloudflare Worker: /webhooks/docuseal]
>       ↓ updates
> [Supabase: task status = signed, files saved]
>       ↓
> [Admin Electron sees status, downloads packet]
> ```
> 
> ---
> 
> # Supabase schema (SQL)
> 
> ```sql
> -- Tenants and users you likely already have
> create table orgs (
>   id uuid primary key default gen_random_uuid(),
>   name text not null,
>   slug text unique not null
> );
> 
> create table portal_users (
>   id uuid primary key default gen_random_uuid(),
>   org_id uuid references orgs(id),
>   email text unique not null,
>   role text check (role in ('admin','member','client')) default 'client'
> );
> 
> -- Interview templates (per USCIS form/packet)
> create table interview_templates (
>   id uuid primary key default gen_random_uuid(),
>   code text not null,              -- e.g., 'i-589-initial'
>   title text not null,
>   docassemble_path text not null,  -- e.g., /interview?i=package:i589.yml
>   docuseal_template_id text,       -- optional, for e-sign handoff
>   active boolean default true
> );
> 
> -- A task assigned to a user
> create table tasks (
>   id uuid primary key default gen_random_uuid(),
>   org_id uuid references orgs(id),
>   assignee_id uuid references portal_users(id),
>   template_id uuid references interview_templates(id),
>   status text check (status in ('queued','in_progress','awaiting_signature','signed','failed','archived'))
>      default 'queued',
>   title text not null,
>   due_at timestamptz,
>   created_by uuid references portal_users(id),
>   launch_url text,                 -- preauth link to docassemble
>   signing_url text,                -- optional if you surface it
>   packet_url text,                 -- final bundle PDF in R2 or Supabase storage
>   meta jsonb default '{}'::jsonb
> );
> 
> -- Each interview run
> create table interview_runs (
>   id uuid primary key default gen_random_uuid(),
>   task_id uuid references tasks(id),
>   org_id uuid references orgs(id),
>   user_id uuid references portal_users(id),
>   docassemble_session_id text,
>   started_at timestamptz default now(),
>   completed_at timestamptz,
>   output_json jsonb,
>   output_files jsonb               -- array of file keys in storage
> );
> 
> -- E-sign tracking
> create table signatures (
>   id uuid primary key default gen_random_uuid(),
>   task_id uuid references tasks(id),
>   vendor text check (vendor in ('docuseal')),
>   submission_id text,
>   status text check (status in ('created','sent','completed','declined','error')) default 'created',
>   signed_pdf_url text,
>   payload jsonb
> );
> ```
> 
> ### Storage
> - Use **Supabase Storage** or **Cloudflare R2** bucket `packets/ORG_SLUG/TASK_ID/*.pdf`.
> - Save raw outputs plus a merged bundle `packet.pdf`.
> 
> ### RLS quick locks
> Lock rows to org and role. You know the drill.
> 
> ```sql
> alter table tasks enable row level security;
> create policy org_read on tasks for select using (
>   exists(select 1 from portal_users u where u.id = auth.uid() and u.org_id = tasks.org_id)
> );
> create policy org_write on tasks for update using (
>   exists(select 1 from portal_users u where u.id = auth.uid() and u.org_id = tasks.org_id and u.role in ('admin'))
> );
> ```
> 
> ---
> 
> # Cloudflare Workers
> 
> ## 1) Create interview task
> `POST /admin/create_interview`
> 
> - Input: `{ org_slug, assignee_email, template_code, due_at, prefill }`
> - Steps: look up org, user, template. Generate a signed **docassemble preauth link** with query params. Insert `tasks` row with `status='queued'`, store `launch_url`. Return `launch_url`.
> 
> Skeleton:
> 
> ```js
> export default {
>   async fetch(req, env) {
>     if (req.method !== "POST") return new Response("no", { status: 405 });
>     const { org_slug, assignee_email, template_code, due_at, prefill={} } = await req.json();
> 
>     // 1) lookups via Supabase REST or PostgREST
>     // 2) generate launch_url for docassemble
>     const params = new URLSearchParams({
>       org: org_slug,
>       email: assignee_email,
>       prefill: btoa(JSON.stringify(prefill))
>     });
>     const launch_url = `${env.DA_BASE_URL}/interview?i=${encodeURIComponent(env.DA_PATHS[template_code])}&${params.toString()}`;
> 
>     // 3) insert task
>     // ... call Supabase REST to insert row, return task + launch_url
>     return Response.json({ launch_url });
>   }
> }
> ```
> 
> ## 2) Handoff to e-sign
> `POST /handoff/sign`
> 
> - Input: `{ task_id }`
> - Pull interview outputs from `interview_runs`. Map to DocuSeal fields. Create submission.
> 
> ```js
> const payload = {
>   template_id: env.DOCUSEAL_TEMPLATE_ID,  // from interview_templates
>   recipients: [{ email: assignee_email, role: "Client" }],
>   fields: mapToDocuSeal(interview_output_json)
> };
> const r = await fetch("https://api.docuseal.com/v1/submissions", {
>   method: "POST",
>   headers: { "Authorization": `Bearer ${env.DOCUSEAL_API_KEY}`, "Content-Type": "application/json" },
>   body: JSON.stringify(payload)
> });
> const info = await r.json();
> // upsert signatures, update tasks.status='awaiting_signature'
> ```
> 
> ## 3) DocuSeal webhook
> `POST /webhooks/docuseal`
> 
> - Validate signature header. On `completed`, fetch signed PDF, store in R2/Storage, update `signatures` and `tasks.status='signed'`, `tasks.packet_url`.
> 
> ---
> 
> # docassemble wiring (no Docker)
> 
> - Ubuntu VM with Nginx, Postgres, Redis, Python, LibreOffice.
> - In interview YAML:
>   1) read `org`, `email`, `prefill` from request args
>   2) guide user through branching interview
>   3) generate PDFs (DOCX → PDF or PDF overlays)
>   4) POST results to `CF Worker /handoff/sign` or stash to Supabase first, then redirect the user back to the portal
> 
> Example end-screen code block:
> 
> ```yaml
> ---
> event: finalize
> code: |
>   # save output JSON and file keys to Supabase
>   save_to_supabase(task_id, {
>     "output_json": interview_dict(),
>     "output_files": assembled_file_keys
>   })
> 
>   # call handoff to sign
>   http_post(env("WORKER_SIGN_URL"), {"task_id": task_id})
> 
>   next_screen = "done"
> ---
> question: All set
> subquestion: >
>   We generated your packet and sent it for signature. You’ll also see this task update inside your client portal.
> buttons:
>   - Exit: exit
> ```
> 
> ---
> 
> # Client Portal UI (React/Vite)
> 
> - **Route:** `/tasks` shows cards: title, due date, status chip.
> - **Task detail:** shows steps: “Fill interview,” “Review PDF,” “Sign.”  
>   - If `status='queued'`, show “Start interview” with `launch_url`.
>   - If `awaiting_signature'`, show link to manual signing if you want to expose it, else leave it email-only.
>   - When webhook marks it `signed`, show “Download packet” button bound to `packet_url`.
> 
> Minimal component shape:
> 
> ```tsx
> function TaskCard({ task }) {
>   return (
>     <Card>
>       <h3>{task.title}</h3>
>       <p>Status: {task.status}</p>
>       {task.status === 'queued' && <a href={task.launch_url}>Start interview</a>}
>       {task.status === 'signed' && <a href={task.packet_url}>Download packet</a>}
>     </Card>
>   );
> }
> ```
> 
> ---
> 
> # Admin Electron (QiEOS)
> 
> Wire IPC to hit Worker endpoints with the admin’s Supabase JWT.
> 
> - **Create task** flow:
>   - Select org → user → template → due date → optional prefill JSON.
>   - Call `/admin/create_interview` and display the `launch_url`.
>   - Option to “Send invite” email through your existing mailer.
> 
> - **Monitor**:
>   - Poll `tasks` where `org_id in my_orgs`. Color rows by status.
>   - Open signed `packet_url` or export to client folder.
> 
> Electron IPC sketch:
> 
> ```ts
> ipcMain.handle('tasks:create', async (_, payload) => {
>   const res = await fetch(WORKER_URL + '/admin/create_interview', {
>     method: 'POST',
>     headers: { 'Authorization': 'Bearer ' + supabaseAdminJWT, 'Content-Type':'application/json' },
>     body: JSON.stringify(payload)
>   });
>   return await res.json();
> });
> 
> ipcMain.handle('tasks:list', async (_, { org_id }) => {
>   const res = await fetch(SUPABASE_REST + '/tasks?org_id=eq.'+org_id, {
>     headers: { 'apikey': SUPABASE_KEY, 'Authorization': 'Bearer ' + supabaseServiceJWT }
>   });
>   return await res.json();
> });
> ```
> 
> ---
> 
> # Config you’ll need
> 
> - `DOCUSEAL_API_KEY`
> - `DOCUSEAL_TEMPLATE_ID` per form or per packet
> - `DA_BASE_URL` and `DA_PATHS[template_code]`
> - Supabase keys for server side workers
> - R2 or Supabase Storage credentials for packet upload
> 
> ---
> 
> # Cursor prompts you can paste
> 
> **1) Worker endpoint: create_interview**
> ```
> You are building a Cloudflare Worker endpoint POST /admin/create_interview.
> Inputs: org_slug, assignee_email, template_code, due_at, prefill.
> Tasks:
> - Fetch org, user, template via Supabase REST.
> - Build docassemble launch_url with query params for org/email/prefill.
> - Insert a row into tasks with status='queued' and return {task_id, launch_url}.
> Return full TypeScript worker code with Env bindings for SUPABASE_URL, SUPABASE_SERVICE_KEY, DA_BASE_URL, DA_PATHS (JSON), and a helper supa() for REST calls. Include minimal error handling.
> ```
> 
> **2) Worker endpoint: handoff/sign**
> ```
> Build a Cloudflare Worker POST /handoff/sign.
> Input: task_id.
> Steps:
> - Load task, latest interview_run with output_json.
> - Map fields to DocuSeal fields using a mapping table keyed by template_code from interview_templates.
> - Create a DocuSeal submission and upsert signatures row.
> - Update task.status='awaiting_signature'.
> Return JSON {submission_id}.
> ```
> 
> **3) Worker endpoint: docuseal webhook**
> ```
> Implement POST /webhooks/docuseal for status updates.
> On 'completed':
> - Download signed PDF file.
> - Upload to R2 (bucket 'packets') path packets/{org_slug}/{task_id}/signed.pdf.
> - Update signatures.status='completed', signatures.signed_pdf_url with public URL.
> - Update tasks.status='signed', tasks.packet_url to the signed file.
> Return 200 fast. Include basic HMAC validation on a DOCUSEAL_WEBHOOK_SECRET header.
> ```
> 
> **4) docassemble interview skeleton**
> ```
> Create a docassemble YAML interview that:
> - Reads org/email/prefill from URL args.
> - Displays 5 questions (name, DOB, A-Number, address, immigration category).
> - Generates a DOCX cover letter and overlays data onto an I-589 PDF template.
> - On finalize, POSTs {task_id, output_json, file_keys[]} to WORKER_SAVE_URL, then POST to WORKER_SIGN_URL to trigger e-sign.
> Use Python blocks sparingly and show the post() helper.
> ```
> 
> **5) React Task list**
> ```
> Create a React component <TaskList /> that reads tasks from Supabase for the current user and renders status chips and action buttons: Start Interview, Resume, Download Packet. Include optimistic UI for status changes.
> ```
> 
> ---
> 
> # Field mapping pattern
> 
> Keep your mappings reusable per template:
> 
> ```json
> {
>   "i-589-initial": {
>     "docuseal_template_id": "1234",
>     "map": {
>       "client.full_name": "answers.name_full",
>       "client.dob": "answers.dob",
>       "client.a_number": "answers.a_number",
>       "client.address.street": "answers.address.street",
>       "client.address.city": "answers.address.city",
>       "client.address.state": "answers.address.state",
>       "client.address.zip": "answers.address.zip"
>     }
>   }
> }
> ```
> 
> Store that JSON in Supabase table `template_mappings` or as a KV in Workers.
> 
> ---
> 
> # Status lifecycle
> 
> - `queued` created by admin
> - `in_progress` when docassemble session starts
> - `awaiting_signature` when DocuSeal submission is created
> - `signed` when webhook closes it
> - `failed` on any hard error
> - `archived` when the admin closes it out
> 
> ---
> 
> # Upgrade levers
> 
> - Add **AssemblyLine** helpers for overflow and multi-doc bundles.  
> - Add **org-scoped SLA rules**: overdue highlighting, automatic reminders.  
> - Add **retry queues** in Workers for flaky webhook fetches.  
> - Add **audit log** table for compliance: who created, who edited, IPs, timestamps.
> 
> ---
> 
> # Reality check
> 
> - This keeps your sacred Cloudflare-first rule.  
> - No Docker, because you said so. docassemble sits in its own VM and pretends to be normal software.  
> - Signatures handled by DocuSeal so you don’t build crypto-stamped nonsense from scratch.  
> - Admin and client experiences are dead simple: task card in, signed packet out.
> 
> Finish: this is the spine. If you want, I’ll spit the Worker code and a minimal docassemble YAML next.

### User
> what about form brikcks

### Assistant
> You mean **Formbricks**. Yes, it’s legit, open source, and actually pleasant. It’s a survey/form engine with solid **conditional logic**, **APIs**, **webhooks**, and self-hosting. It is not a PDF engine or e-signer, so it lives at the **intake/interview** layer, then we hand off to docassemble for assembly and DocuSeal for signatures. You keep your Cloudflare/Supabase spine, no drama.
> 
> # Where Formbricks fits
> - **Strong at:** embeddable questionnaires, branching logic, file uploads, webhooks, REST APIs, and easy theming. citeturn0search1turn0search3turn0search5turn0search7  
> - **Not meant for:** generating USCIS PDFs or doing signatures. That’s docassemble + DocuSeal’s job.  
> - **Self-hosting:** officially via Docker or a quick one-click script that installs Docker. If Docker is a red flag, you can still run it from source on a VM, but you’ll be swimming upstream vs their supported path. citeturn0search2turn0search10  
> - **Privacy/compliance story:** good. On-prem is first-class and S3-compatible storage for uploads is supported. citeturn0search8turn0search11
> 
> # Clean integration pattern (QiEOS + Client Portal)
> **Formbricks → Workers → Supabase → docassemble → DocuSeal → webhooks → tasks update**
> 
> 1) **Client portal shows a task** with a “Start intake” button that links to a Formbricks survey URL scoped to org/user.  
> 2) **Formbricks on submit** fires a **webhook** to your Cloudflare Worker with the full response payload. citeturn0search5  
> 3) **Worker maps answers** to your docassemble interview variables and either:  
>    - calls the **docassemble API** to create a session and render PDFs immediately, or  
>    - stores the payload in Supabase, then hits a docassemble endpoint to fetch and assemble. citeturn0search12  
> 4) **Worker sends outputs** to **DocuSeal** to create a submission for e-sign, prefilled with the mapped fields. Task status flips to “Awaiting signature,” and the client gets the email.  
> 5) **DocuSeal webhook** posts back on completion; Worker uploads the signed PDF to R2/Supabase Storage and marks the task “Signed,” exposing a **Download packet** link.  
> 6) **QiEOS (Electron)** polls tasks and shows real-time status.
> 
> # Why use Formbricks at all?
> - You want a **fast, pretty interviewer** with less YAML than docassemble, embeddable in your portal, with **conditional logic** and **APIs** your Workers can boss around. citeturn0search1turn0search3  
> - You still keep **docassemble** where it excels: rule-heavy branching, multi-doc bundles, exact USCIS layouts. This avoids forcing every intake to be a docassemble screen. Balance, like a grown-up system.
> 
> # Minimal wiring you need
> - **Formbricks project + survey** for “I-589 Intake.”  
> - **Webhook** pointing to `/intakes/formbricks` on your Worker. Payload includes respondent answers and metadata. citeturn0search5  
> - **Mapping table** per template (kept in Supabase or KV):
>   ```json
>   {
>     "i-589-initial": {
>       "docassemble_interview": "package:i589.yml",
>       "docuseal_template_id": "1234",
>       "map": {
>         "answers.full_name": "user_name",
>         "answers.dob": "user_dob",
>         "answers.a_number": "a_number",
>         "answers.address.street": "address_street"
>       }
>     }
>   }
>   ```
> - **Worker flow:** validate webhook → upsert `interview_runs` → call docassemble API → generate PDFs → call DocuSeal API → update `tasks`.  
> - **Storage:** S3-compatible for Formbricks file uploads, R2/Supabase for packets. citeturn0search11
> 
> # Reality and tradeoffs
> - If you can tolerate Docker for **Formbricks only**, use their one-click script and be done in an hour. If not, you can build from source, but their docs and scripts center on Docker. Don’t pretend otherwise. citeturn0search10  
> - Formbricks logic is solid, but **docassemble still wins** for gnarly legal decision trees. Use Formbricks for UX speed and funnel control, then punt the heavy lifting to docassemble.
> 
> # TL;DR fit check
> - Want slick intake forms embedded in the portal with logic, uploads, APIs, webhooks? **Formbricks** fits. citeturn0search6  
> - Need final immigration PDFs and signatures? **docassemble + DocuSeal** still handle that part.  
> - Glue it with **Cloudflare Workers + Supabase** like we planned. Minimal churn.
> 
> If you want, I’ll nail the Worker webhook handler and a Formbricks survey JSON next so you can paste and ship. Try not to install five more libraries out of boredom.
