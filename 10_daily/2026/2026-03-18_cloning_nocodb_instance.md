---
layout: page
title: "Cloning NocoDB Instance"
slug: "cloning_nocodb_instance"
created_at: "2026-03-18 21:38:07"
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
source_file: "Chat-Export-28513-2026/conversations-005.json"
template_key: master-template
date: 2026-03-18
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69bb618e-cc7c-8330-9057-c4ee3e50596c"
canonical_ref: ""
---

# Cloning NocoDB Instance

## Overview
- **Date**: 2026-03-18 21:38:07
- **Conversation ID**: `69bb618e-cc7c-8330-9057-c4ee3e50596c`
- **Source**: `Chat-Export-28513-2026/conversations-005.json`

## Chat History

### User
> ok my nocodb instance on railway is tripping and im not sure how to fix it, but i rather just clone the repo and have my own copy, how do i do that because they got all these install methods i never use.

### Assistant
> I’m checking the current NocoDB install paths so I don’t hand you stale steps, then I’ll give you the fastest route that fits how you actually work.

### Assistant
> Yeah — cloning the repo is **not** the same thing as cloning your actual NocoDB instance.
> 
> What you probably want is one of these:
> 
> 1. **Clone the app source** so you can deploy your own copy of NocoDB
> 2. **Clone your actual instance** so your bases/data come with it too
> 
> Those are different jobs.
> 
> ## The blunt answer
> 
> If your Railway NocoDB is acting stupid and you want control, the clean move is:
> 
> - **do not bother with random install methods**
> - **use Docker Compose**
> - **use Postgres for the database**
> - **back up your current Railway DB first if you care about the data**
> 
> NocoDB’s repo still points people toward Docker-based self-hosting, and their current GitHub releases are active, with `0.301.5` published March 18, 2026. Their repo also points to an install script and other self-host options. citeturn404818view0turn404818view1
> 
> ## What “clone the repo” actually means
> 
> That means getting the NocoDB source code from GitHub:
> 
> ```bash
> git clone https://github.com/nocodb/nocodb.git
> cd nocodb
> ```
> 
> That gives you **their codebase**, not your data. citeturn404818view0
> 
> If your goal is just “I want my own NocoDB running somewhere I control,” you do **not** need to build from source unless you enjoy unnecessary suffering.
> 
> ## Best path for you
> 
> ### Option A — fastest sane option
> Run your own NocoDB with Docker Compose on:
> - a VPS
> - your local machine
> - or even another Railway service if you really want, though I’d rather put it somewhere more predictable
> 
> Use:
> - **NocoDB container**
> - **Postgres container** or external Postgres
> - persistent volume
> 
> ### Option B — keep using Railway, but your own deployment
> Railway has supported NocoDB templates in their documented install flow. citeturn404818view2
> 
> That is fine for quick deployment, but if Railway itself is the thing annoying you, moving to your own Docker/VPS setup is the smarter escape.
> 
> ---
> 
> # What to do right now
> 
> ## 1) Back up your current data first
> If your current instance matters, do this before touching anything.
> 
> If your NocoDB is using Railway Postgres, export it with `pg_dump`.
> 
> Example:
> 
> ```bash
> pg_dump "postgresql://USER:PASSWORD@HOST:PORT/DBNAME" > nocodb_backup.sql
> ```
> 
> If you do **not** know whether your NocoDB data is in SQLite or Postgres, check Railway service variables / mounted storage first.  
> If it’s SQLite, you need the SQLite database file.  
> If it’s Postgres, you need a SQL dump.
> 
> ## 2) Spin up your own copy with Docker Compose
> 
> Here’s the simplest practical starter:
> 
> ```yaml
> services:
>   postgres:
>     image: postgres:16
>     container_name: nocodb-postgres
>     restart: unless-stopped
>     environment:
>       POSTGRES_DB: nocodb
>       POSTGRES_USER: nocodb
>       POSTGRES_PASSWORD: change_this_now
>     volumes:
>       - ./postgres_data:/var/lib/postgresql/data
>     ports:
>       - "5432:5432"
> 
>   nocodb:
>     image: nocodb/nocodb:latest
>     container_name: nocodb
>     restart: unless-stopped
>     depends_on:
>       - postgres
>     environment:
>       NC_DB: "pg://postgres:5432?u=nocodb&p=change_this_now&d=nocodb"
>     ports:
>       - "8080:8080"
>     volumes:
>       - ./nocodb_data:/usr/app/data
> ```
> 
> Then run:
> 
> ```bash
> docker compose up -d
> ```
> 
> Open:
> 
> ```bash
> http://localhost:8080
> ```
> 
> That gets you your own NocoDB without messing with source builds.
> 
> ## 3) Restore your data
> If you exported Postgres:
> 
> ```bash
> psql "postgresql://nocodb:change_this_now@localhost:5432/nocodb" < nocodb_backup.sql
> ```
> 
> Then restart NocoDB:
> 
> ```bash
> docker compose restart nocodb
> ```
> 
> ---
> 
> # If you really want to build from source
> 
> Only do this if you want to modify NocoDB itself.
> 
> ```bash
> git clone https://github.com/nocodb/nocodb.git
> cd nocodb
> ```
> 
> From there you’d follow their dev setup, install dependencies, and run the app in development. But for your use case, that’s extra complexity for no benefit. The repo itself separates “other methods” and treats binaries as quick testing, which is another hint that source/dev setup is not the main self-host path. citeturn404818view0
> 
> So: **don’t build from source unless you plan to hack the product.**
> 
> ---
> 
> # My recommendation for you
> 
> Use this decision tree:
> 
> - **Need it working today, least drama:** Docker Compose
> - **Need it online but still easy:** VPS + Docker Compose
> - **Need temporary convenience:** Railway template
> - **Need custom dev changes:** clone repo + build from source
> 
> ## The real trap
> Do **not** say “I cloned the repo so I have my instance now.”  
> No you don’t. You have the app code. Your actual instance lives in the database and storage.
> 
> So the correct migration mindset is:
> 
> **app + database + storage + env vars = your real instance**
> 
> Not just the repo.
> 
> If you want, I’ll give you the exact:
> - Windows-local setup
> - Railway-to-Docker migration steps
> - or a ready-to-paste `docker-compose.yml` plus `.env` built for your setup.

### User
> at 11607 (/usr/src/app/docker/index.js:1:16196460)

>     at _0x5acfbe (/usr/src/app/docker/index.js:1:25792506)

>     at 49614 (/usr/src/app/docker/index.js:1:12108432)

>     at _0x5acfbe (/usr/src/app/docker/index.js:1:25792506)

>     at 68538 (/usr/src/app/docker/index.js:1:9668603) {

>   code: 'ERR_INVALID_URL',

>   input: 'nocodb.qially.com'

> }

> Node.js v22.12.0

> Mounting volume on: /var/lib/containers/railwayapp/bind-mounts/7baa66d6-8294-4fcb-83c3-3171e12df581/vol_59vf9c5wvoehgmiy

> Skip sourcing /mnt/efs/master_config.env as file does not exists

> Skip sourcing /mnt/efs//cluster.env as file does not exists

> splitting NC_PROPERTIES_JSON into env variables

> completed configure

> node:internal/url:818

>       href = bindingUrl.parse(input, base, true);

>                         ^

> TypeError: Invalid URL

>     at new URL (node:internal/url:818:25)

>     at 41721 (/usr/src/app/docker/index.js:1:13313714)

>     at _0x5acfbe (/usr/src/app/docker/index.js:1:25792506)

>     at 85698 (/usr/src/app/docker/index.js:1:21307455)

>     at _0x5acfbe (/usr/src/app/docker/index.js:1:25792506)

>     at 11607 (/usr/src/app/docker/index.js:1:16196460)

>     at _0x5acfbe (/usr/src/app/docker/index.js:1:25792506)

>     at 49614 (/usr/src/app/docker/index.js:1:12108432)

>     at _0x5acfbe (/usr/src/app/docker/index.js:1:25792506)

>     at 68538 (/usr/src/app/docker/index.js:1:9668603) {

>   code: 'ERR_INVALID_URL',

>   input: 'nocodb.qially.com'

> }

> Node.js v22.12.0

> Skip sourcing /mnt/efs/master_config.env as file does not exists

> Skip sourcing /mnt/efs//cluster.env as file does not exists

> splitting NC_PROPERTIES_JSON into env variables

> completed configure

> Mounting volume on: /var/lib/containers/railwayapp/bind-mounts/7baa66d6-8294-4fcb-83c3-3171e12df581/vol_59vf9c5wvoehgmiy

>     at 49614 (/usr/src/app/docker/index.js:1:12108432)

>     at _0x5acfbe (/usr/src/app/docker/index.js:1:25792506)

>     at 68538 (/usr/src/app/docker/index.js:1:9668603) {

>   code: 'ERR_INVALID_URL',

>   input: 'nocodb.qially.com'

> }

> Node.js v22.12.0

> node:internal/url:818

>       href = bindingUrl.parse(input, base, true);

>                         ^

> TypeError: Invalid URL

>     at new URL (node:internal/url:818:25)

>     at 41721 (/usr/src/app/docker/index.js:1:13313714)

>     at _0x5acfbe (/usr/src/app/docker/index.js:1:25792506)

>     at 85698 (/usr/src/app/docker/index.js:1:21307455)

>     at _0x5acfbe (/usr/src/app/docker/index.js:1:25792506)

>     at 11607 (/usr/src/app/docker/index.js:1:16196460)

>     at _0x5acfbe (/usr/src/app/docker/index.js:1:25792506)

> Skip sourcing /mnt/efs/master_config.env as file does not exists

> Skip sourcing /mnt/efs//cluster.env as file does not exists

> splitting NC_PROPERTIES_JSON into env variables

> completed configure

> Mounting volume on: /var/lib/containers/railwayapp/bind-mounts/7baa66d6-8294-4fcb-83c3-3171e12df581/vol_59vf9c5wvoehgmiy

> node:internal/url:818

>       href = bindingUrl.parse(input, base, true);

>                         ^

> TypeError: Invalid URL

>     at new URL (node:internal/url:818:25)

>     at 41721 (/usr/src/app/docker/index.js:1:13313714)

>     at _0x5acfbe (/usr/src/app/docker/index.js:1:25792506)

>     at 85698 (/usr/src/app/docker/index.js:1:21307455)

>     at _0x5acfbe (/usr/src/app/docker/index.js:1:25792506)

>     at 11607 (/usr/src/app/docker/index.js:1:16196460)

>     at _0x5acfbe (/usr/src/app/docker/index.js:1:25792506)

>     at 49614 (/usr/src/app/docker/index.js:1:12108432)

>     at _0x5acfbe (/usr/src/app/docker/index.js:1:25792506)

>     at 68538 (/usr/src/app/docker/index.js:1:9668603) {

>   code: 'ERR_INVALID_URL',

>   input: 'nocodb.qially.com'

> }

> Node.js v22.12.0

> Skip sourcing /mnt/efs/master_config.env as file does not exists

> Skip sourcing /mnt/efs//cluster.env as file does not exists

> splitting NC_PROPERTIES_JSON into env variables

> completed configure

> Mounting volume on: /var/lib/containers/railwayapp/bind-mounts/7baa66d6-8294-4fcb-83c3-3171e12df581/vol_59vf9c5wvoehgmiy

>     at 68538 (/usr/src/app/docker/index.js:1:9668603) {

>   code: 'ERR_INVALID_URL',

>   input: 'nocodb.qially.com'

> }

> Node.js v22.12.0

> node:internal/url:818

>       href = bindingUrl.parse(input, base, true);

>                         ^

> TypeError: Invalid URL

>     at new URL (node:internal/url:818:25)

>     at 41721 (/usr/src/app/docker/index.js:1:13313714)

>     at _0x5acfbe (/usr/src/app/docker/index.js:1:25792506)

>     at 85698 (/usr/src/app/docker/index.js:1:21307455)

>     at _0x5acfbe (/usr/src/app/docker/index.js:1:25792506)

>     at 11607 (/usr/src/app/docker/index.js:1:16196460)

>     at _0x5acfbe (/usr/src/app/docker/index.js:1:25792506)

>     at 49614 (/usr/src/app/docker/index.js:1:12108432)

>     at _0x5acfbe (/usr/src/app/docker/index.js:1:25792506)

> Skip sourcing /mnt/efs/master_config.env as file does not exists

> Skip sourcing /mnt/efs//cluster.env as file does not exists

> splitting NC_PROPERTIES_JSON into env variables

### Assistant
> I found the likely failure already: something is trying to parse `nocodb.qially.com` as a full URL, and that is **not** a valid URL by itself. It needs `https://nocodb.qially.com` or the offending env var needs to be removed.

### Assistant
> Yep. This is not a repo problem yet. Your NocoDB is choking on a **bad URL env var**.
> 
> ## What the log is saying
> 
> This line is the giveaway:
> 
> `input: 'nocodb.qially.com'`
> 
> Node is trying to do `new URL(...)`, and `nocodb.qially.com` by itself is **not** a valid absolute URL. It needs a scheme like:
> 
> - `https://nocodb.qially.com`
> - or `http://nocodb.qially.com`
> 
> NocoDB’s current self-host env docs say `NC_PUBLIC_URL` is the base URL for the public-facing app, and `NUXT_PUBLIC_NC_BACKEND_URL` is also a URL field. Those must be real URLs, not bare domains. citeturn244047view0
> 
> ## Most likely cause
> 
> One of these Railway env vars is set wrong:
> 
> - `NC_PUBLIC_URL`
> - `NC_APP_URL`
> - `NUXT_PUBLIC_NC_BACKEND_URL`
> - something inside `NC_PROPERTIES_JSON`
> 
> Your log literally says:
> 
> - “splitting `NC_PROPERTIES_JSON` into env variables”
> - then it crashes on invalid URL
> 
> So the strongest guess is: **you have a URL-like property in `NC_PROPERTIES_JSON` or normal env vars set to `nocodb.qially.com` instead of `https://nocodb.qially.com`.** NocoDB has had startup failures from invalid URL env config before, during early config loading. citeturn244047view1turn244047view0
> 
> ## Fix this first
> 
> In Railway, open the NocoDB service and search your variables for:
> 
> - `NC_PUBLIC_URL`
> - `NC_APP_URL`
> - `NUXT_PUBLIC_NC_BACKEND_URL`
> - `NC_PROPERTIES_JSON`
> 
> Then fix any value that looks like this:
> 
> ```text
> nocodb.qially.com
> ```
> 
> Change it to:
> 
> ```text
> https://nocodb.qially.com
> ```
> 
> ## What I would do, in order
> 
> ### 1. Remove junk URL vars
> If you are not explicitly using them, temporarily delete these:
> 
> - `NC_APP_URL`
> - `NUXT_PUBLIC_NC_BACKEND_URL`
> 
> Keep only:
> 
> ```text
> NC_PUBLIC_URL=https://nocodb.qially.com
> ```
> 
> That is the cleanest test, because NocoDB can infer some URLs if you do not override them. `NC_PUBLIC_URL` is the documented public-facing base URL. citeturn244047view0
> 
> ### 2. Check `NC_PROPERTIES_JSON`
> Because your logs mention it directly, inspect it. If you see any field with:
> 
> ```json
> "something":"nocodb.qially.com"
> ```
> 
> change it to:
> 
> ```json
> "something":"https://nocodb.qially.com"
> ```
> 
> or remove that property entirely for the test.
> 
> ### 3. Redeploy
> After fixing/removing the bad env var, redeploy the service.
> 
> ---
> 
> ## Minimal safe Railway env set
> 
> For a basic test, I would reduce it to something like:
> 
> ```env
> NC_PUBLIC_URL=https://nocodb.qially.com
> PORT=8080
> ```
> 
> And your database env, depending on how you connected it.
> 
> If you are using Postgres, the exact DB env matters too, but this particular crash is **not** a DB auth error. It is a URL parsing error before normal startup.
> 
> ---
> 
> ## Important detail
> 
> A lot of apps accept bare domains casually. Node’s URL parser does not.  
> This fails:
> 
> ```text
> nocodb.qially.com
> ```
> 
> This works:
> 
> ```text
> https://nocodb.qially.com
> ```
> 
> That is why it’s blowing up.
> 
> ## Do not do this yet
> Do **not** jump straight into cloning/building from source just because Railway is acting stupid. Right now the failure looks like **config**, not some deep broken install.
> 
> ## Your fastest path
> 
> Do this exact triage:
> 
> 1. Search all Railway variables for `qially.com`
> 2. Any value that is just `nocodb.qially.com` gets changed to `https://nocodb.qially.com`
> 3. Temporarily remove `NC_APP_URL` and `NUXT_PUBLIC_NC_BACKEND_URL`
> 4. Inspect `NC_PROPERTIES_JSON` for the same mistake
> 5. Redeploy
> 
> If it still crashes after that, paste your env var names and values with secrets redacted, like this:
> 
> ```text
> NC_PUBLIC_URL=https://nocodb.qially.com
> NC_APP_URL=...
> NUXT_PUBLIC_NC_BACKEND_URL=...
> NC_PROPERTIES_JSON=...
> ```
> 
> and I’ll tell you exactly which one is the offender.

### User
> and we are back. i think, hold on lol

### Assistant
> Good. That means the app itself probably wasn’t broken — your config was. Classic.
> 
> Check three things before you celebrate:
> 
> 1. Can you load the login page normally at `https://nocodb.qially.com`
> 2. Can you sign in and open a base without errors
> 3. Do the logs stop looping and stay clean after startup
> 
> If that all works, lock in the fix by keeping only the URL vars you actually need. Bare domains in env vars are cute until Node decides to throw a fit.

### User
> Task: Transform our recent discussion into a structured, fluff-free Summary and Action List for Notion.
> 
> Formatting Constraints:
> 
> Use Markdown (H2 for headers, - [ ] for checkboxes).
> 
> No conversational intro or outro (start directly with the content).
> 
> Use Bold for client names and Code blocks for exact message scripts.
> 
> Structure:
> 
> Executive Summary: A 2-sentence overview of today's focus (e.g., "Shift from lead follow-up to active preparation for Damyelo; priority on pending deposits").
> 
> Immediate Action Pipeline: A checklist of clients ordered by "Money First" then "Admin."
> 
> Communication Scripts: A table or list with:
> 
> Client Name
> 
> Status (e.g., Waiting on Deposit, Ready to Start)
> 
> The Script (Ready-to-copy WhatsApp/Text message)
> 
> The "Don't Forget" List: 3–5 bullet points of technical details (e.g., Variable spacing rules, specific tax form nuances)

### Assistant
> ## Executive Summary
> Resolved NocoDB crash caused by invalid URL environment variables (missing protocol), restoring service stability. Priority now is to verify full functionality, clean environment configuration, and secure a portable self-hosted fallback.
> 
> ## Immediate Action Pipeline
> 
> ### 💰 Money First
> - [ ] Confirm NocoDB instance is fully operational (login + base access)
> - [ ] Validate database connection (no silent failures or missing data)
> - [ ] Ensure public URL is correctly set (`https://nocodb.qially.com`)
> 
> ### 🛠️ Admin / Stability
> - [ ] Audit all environment variables for invalid URLs (no bare domains)
> - [ ] Remove unnecessary vars:
>   - [ ] `NC_APP_URL`
>   - [ ] `NUXT_PUBLIC_NC_BACKEND_URL`
> - [ ] Inspect and clean `NC_PROPERTIES_JSON`
> - [ ] Restart + monitor logs for stability (no loop crashes)
> - [ ] Create database backup (pg_dump or SQLite file)
> - [ ] Set up Docker Compose version locally as fallback
> - [ ] Document final working env config for reuse
> 
> ## Communication Scripts
> 
> ### **Self / System Check**
> **Status:** Verification
> 
> ```text
> Confirm system stability:
> - Login works
> - Bases load correctly
> - No repeated errors in logs
> If all pass → lock config and proceed to backup + local deployment.
> ```
> 
> ### **Future You (Deployment Reminder)**
> **Status:** Prevent regression
> 
> ```text
> Do NOT use bare domains in env variables.
> Always use full URLs:
> https://your-domain.com
> 
> Critical vars:
> - NC_PUBLIC_URL must be valid URL
> - Remove unused URL vars unless required
> 
> System = App + DB + Storage + ENV
> Not just code.
> ```
> 
> ## Don't Forget
> 
> - Node.js URL parser **requires protocol** (`https://`) — bare domains will crash startup
> - `NC_PROPERTIES_JSON` can silently inject bad config → always inspect it
> - Railway logs looping = config failure, not app failure
> - Backups before changes (Postgres: `pg_dump`, SQLite: file copy)
> - Docker Compose = fastest escape hatch if platform instability returns
