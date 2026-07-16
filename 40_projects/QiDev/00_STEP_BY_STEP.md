---
layout: page
title: QiOne RAG — One Zip Setup (Step-by-Step)
slug: qione-rag-one-zip-setup-step-by-step
status: publish
updated_at: "2026-06-29"
tags:
  - projects
source_type: manual
summary: ""
created_at: ""
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ""
canonical_ref: ""
template_key: master-template
---

# QiOne RAG — One Zip Setup (Step-by-Step)

This guide assumes you know nothing. Follow in order. Total time: ~20–30 min.

---

## 0) Requirements

- Windows 10/11
- **Python 3.10+** (https://www.python.org/downloads/) – check `python --version`
- **Docker Desktop** (https://www.docker.com/products/docker-desktop/) – start it once
- **Google Drive for desktop** and **iCloud Drive** already installed and signed in
- Your content exists **once** inside both:
  - `C:\Users\YOURNAME\My Drive\QiOne`
  - `C:\Users\YOURNAME\iCloudDrive\QiOne`

> We will NOT copy your notes again. The app will read both folders directly.

---

## 1) Unzip this bundle

Extract this zip to a workspace folder. Example:
```
C:\Users\YOURNAME\QiOneApp
```
Open **PowerShell** in that folder (Shift + Right-Click → “Open PowerShell window here”).

---

## 2) One-time bootstrap (installs Python packages + starts Qdrant)

Run this in PowerShell:
```powershell
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
pip install -r local\requirements.txt
pip install -r local\requirements-drive.txt   # adds Google Drive API libs (optional but recommended)
docker compose -f local\3_infra\docker-compose.yml up -d
Copy-Item local\.env.example local\.env -Force
```

---

## 3) Configure your paths and keys

Open `local/.env` and set:
```

# Models (OpenAI or compatible)

OPENAI_API_KEY=sk-...

# Your two *existing* mirrored folders:

VAULT_GDRIVE=C:\Users\YOURNAME\My Drive\QiOne
VAULT_ICLOUD=C:\Users\YOURNAME\iCloudDrive\QiOne

# Vector DB (local Qdrant or your Qdrant Cloud URL)

QDRANT_URL=http://localhost:6333
QDRANT_COLLECTION=qinote_global

# (optional) Supabase if you want cloud vectors too

SUPABASE_URL=
SUPABASE_ANON_KEY=

# Canon index file

QIINDEX_PATH=meta/QiIndex.csv
```

---

## 4) First ingest (multi-root + dedupe)

This reads BOTH folders directly and avoids duplicates by hashing chunk content.
```powershell
. .\.venv\Scripts\Activate.ps1
python local\5_rag\ingest\ingest_fs.py --roots "$env:VAULT_GDRIVE" "$env:VAULT_ICLOUD"
```

**What happens:**
- Finds `.md/.txt/.csv/.pdf`
- Extracts text, **chunks**, **embeds** (SBERT offline; uses OpenAI only if you switch later)
- Stores vectors in **Qdrant** at `QDRANT_URL`
- **Dedupes** identical chunks across Drive/iCloud (no bloat)

---

## 5) Start your local chat API + UI

```powershell
uvicorn local\5_rag\qi_rag_api:app --reload --host 0.0.0.0 --port 8010
```
Open `local\1_apps\chat.html` in your browser and ask questions.

---

## 6) Auto-update while you work

Watches BOTH folders. On change, it re-ingests only what's changed.
```powershell
python local\5_rag\watch\watch.py --roots "$env:VAULT_GDRIVE" "$env:VAULT_ICLOUD"
```

---

## 7) (Optional) Push embeddings to Supabase pgvector (cloud portability)

If you want to keep a **cloud copy** of vectors so a new PC can be turned on instantly:

1. Create a Supabase project → SQL editor → run the files in `cloud\supabase\sql\`.
2. Put your `SUPABASE_URL` and `SUPABASE_ANON_KEY` into `local/.env`.
3. Run:
```powershell
python local\5_rag\ingest\push_to_supabase.py --collection qinote_global
```
This reads what’s in Qdrant and upserts rows to Supabase (`kb_embeddings`).

> You can re-run this after big ingests, or schedule it to keep cloud vectors current.

---

## 8) (Optional) Cloud Mode (any browser, even if PC dies)

Use the files under `cloud/` to deploy:
- Supabase **Edge Function** that ingests from **Google Drive folder ID** (no PC needed).
- Cloudflare **Worker** that exposes `/query` via Supabase RPC.
- Cloudflare **Pages** hosting the chat UI.

Follow `cloud/README_CLOUD.md`.

---

## 9) Disaster recovery (your “spin up anywhere” plan)

On a new PC:
1. Install Google Drive + iCloud Drive and sign in.
2. Wait for **QiOne** folders to sync.
3. Copy this app folder, activate venv, `docker compose up -d` for Qdrant **or** set Qdrant Cloud URL.
4. Set `.env` with the same `VAULT_*` + your Supabase/Qdrant creds.
5. Run ingest (or skip if Supabase already has vectors), start API, open chat.

---

## 10) Daily usage

- Create/edit notes in **either** QiOne folder → watcher picks it up → vectors update.
- Ask via local chat or cloud Pages.
- Keep `QiIndex.csv` as your canon (optional) and use `qd_autoname.py` for Gi-EOS IDs.

You're done. Enjoy your second brain.
