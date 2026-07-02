---
layout: page
title: QiOne — Supabase-Only (No Docker) Setup
slug: qione-supabase-only-no-docker-setup
status: active
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

# QiOne — Supabase-Only (No Docker) Setup

This guide assumes you know nothing. Follow in order. Total time: ~20–30 min.

---

## 0) Requirements

- Windows 10/11
- **Python 3.10+** (https://www.python.org/downloads/) – check `python --version`
- **Google Drive for desktop** and **iCloud Drive** already installed and signed in
- Your content exists **once** inside both:
  - `C:\Users\YOURNAME\My Drive\QiOne`
  - `C:\Users\YOURNAME\iCloudDrive\QiOne`

> We will NOT copy your notes again. The app will read both folders directly.

---

## 1) Extract and setup

Extract this bundle to a workspace folder. Example:
```
C:\Users\YOURNAME\QiOneApp
```
Open **PowerShell** in that folder (Shift + Right-Click → "Open PowerShell window here").

---

## 2) One-time bootstrap (installs Python packages)

Run this in PowerShell:
```powershell
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
pip install -r local\requirements.txt
```

---

## 3) Configure your paths and keys

Copy the example env file:
```powershell
Copy-Item local\.env.example local\.env
```

Open `local/.env` and set:
```env

# OpenAI API (required for embeddings)

OPENAI_API_KEY=sk-...

# Your two *existing* mirrored folders:

VAULT_GDRIVE=C:\Users\YOURNAME\My Drive\QiOne
VAULT_ICLOUD=C:\Users\YOURNAME\iCloudDrive\QiOne

# Supabase (required)

SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_ROLE=your-service-role-key-here   # For writes (ingest scripts)
SUPABASE_ANON_KEY=your-anon-key-here                # For reads (API/Worker)

# Optional: Chat model

CHAT_MODEL=gpt-4o-mini
```

---

## 4) Set up Supabase

1. Create a new Supabase project at https://supabase.com
2. In the SQL Editor, run `cloud/supabase/sql/01_init.sql` to create:
   - pgvector extension
   - `kb_embeddings` table with `chunk_hash` unique constraint
   - IVFFlat index for vector search
   - `match_kb` RPC function
3. Run `cloud/supabase/sql/02_policies.sql` to set up RLS policies
4. Run `cloud/supabase/sql/03_status.sql` to create status/telemetry tables:
   - `kb_files` - file tracking with metadata
   - `kb_runs` - ingest run history
   - `kb_errors` - error log
   - RPCs: `upsert_file_state`, `get_kb_status`, `list_recent_errors`
5. Get your keys from Settings → API:
   - **Service Role Key** (secret) → Use for `SUPABASE_SERVICE_ROLE` (ingest scripts write to DB)
   - **Anon Key** (public) → Use for `SUPABASE_ANON_KEY` (API/Worker reads from DB)

> **Note:** Writers (ingest scripts) should use the service-role key when calling `upsert_file_state` and writing to status tables. This bypasses RLS and ensures writes succeed.

---

## 5) First ingest → Supabase (no duplicates)

This reads BOTH folders directly and avoids duplicates by hashing chunk content.

```powershell
. .\.venv\Scripts\Activate.ps1
python local\5_rag\ingest\ingest_supabase.py --roots "$env:VAULT_GDRIVE" "$env:VAULT_ICLOUD"
```

**What happens:**
- Finds `.md/.txt/.csv/.pdf` files in both folders
- Extracts text, **chunks** (800 chars), **embeds** with OpenAI (1536-dim)
- Stores vectors in **Supabase** `kb_embeddings` table
- **Dedupes** identical chunks across Drive/iCloud (SHA-256 hash → unique constraint)

---

## 6) Start your local API (queries Supabase)

```powershell
. .\.venv\Scripts\Activate.ps1
uvicorn local.5_rag.qi_rag_api_supabase:app --reload --port 8010
```

Open `local\1_apps\chat.html` in your browser and ask questions.

---

## 7) Keep it synced while you work (optional)

Watches BOTH folders. On change, it re-ingests (safe because upsert + unique hash prevents duplicates).

```powershell
. .\.venv\Scripts\Activate.ps1
python local\5_rag\watch\watch_supabase.py --roots "$env:VAULT_GDRIVE" "$env:VAULT_ICLOUD"
```

Leave this running in a separate terminal.

---

## 8) (Optional) Cloud Mode (any browser, even if PC dies)

Use the files under `cloud/` to deploy:
- Cloudflare **Worker** that exposes `/query` via Supabase RPC
- Cloudflare **Pages** hosting the chat UI

Follow `cloud/README_CLOUD.md`.

---

## 9) Disaster recovery (your "spin up anywhere" plan)

On a new PC:
1. Install Google Drive + iCloud Drive and sign in.
2. Wait for **QiOne** folders to sync.
3. Copy this app folder, activate venv, install requirements.
4. Set `.env` with the same `VAULT_*` + your Supabase creds.
5. Skip ingestion (Supabase already has vectors) or run ingest if needed.
6. Start API, open chat.

---

## 10) Daily usage

- Create/edit notes in **either** QiOne folder → watcher picks it up → vectors update.
- Ask via local chat or cloud Pages.
- Keep `QiIndex.csv` as your canon (optional) and use `qd_autoname.py` for Gi-EOS IDs.

---

## What's inside

- `docs/STEP_BY_STEP_SUPABASE.md` — this file
- `local/.env.example` — fill in keys + your two folder paths
- `local/requirements.txt` — no Docker deps
- `local/5_rag/ingest/ingest_supabase.py` — walks both folders, chunks (800 chars), dedupes by chunk hash, embeds with OpenAI, upserts to Supabase
- `local/5_rag/qi_rag_api_supabase.py` — FastAPI that embeds the query and calls Supabase RPC `match_kb`
- `local/5_rag/watch/watch_supabase.py` — simple watcher that re-ingests on changes (safe because upsert+unique hash)
- `cloud/supabase/sql/01_init.sql` — schema with `chunk_hash` unique, vector(1536), IVFFlat index, `match_kb` RPC
- `cloud/supabase/sql/02_policies.sql` — permissive anon read (tighten later)
- `cloud/worker + cloud/pages` — optional Cloudflare Worker `/query` + Pages chat for browser-anywhere access

---

## Notes you'll care about

- **No duplication.** We read your existing GDrive/iCloud QiOne folders directly.
- **Dedup:** same chunk in both mirrors → one vector (SHA-256 content hash).
- **Portable:** everything lives in Supabase, so on a new box just install Drive/iCloud + this folder, set .env, done.
- **Private:** the included policy is permissive for testing; flip to service-role + RLS when you want to lock it down.

---

## Troubleshooting

### Embeddings Failing

If you see errors during the embedding phase:

1. **Check API key validity:**
   - Verify `OPENAI_API_KEY` is set correctly in `.env`
   - Test with: `curl https://api.openai.com/v1/models -H "Authorization: Bearer $OPENAI_API_KEY"`

2. **Model name exact:**
   - Must be exactly `text-embedding-3-large` (case-sensitive)

3. **Input length issues:**
   - The script automatically splits batches if they exceed 250k chars (~62.5k tokens)
   - If you see 400 errors, check the log for the first bad chunk length and sample text
   - Single chunks over 8192 tokens will fail - consider chunking at a smaller size (e.g., 400 chars)

4. **Rate limits (429 errors):**
   - OpenAI has rate limits on embeddings API
   - Wait a few minutes and retry
   - Consider reducing batch size with `--batch-size 25`

5. **Network errors:**
   - Check internet connection
   - Verify OpenAI API is accessible from your network
   - Check firewall/proxy settings

### No Matches Found

If queries return no results:

1. **Verify SQL was applied:**
   - Check Supabase SQL Editor → run `SELECT COUNT(*) FROM kb_embeddings;`
   - Should show > 0 rows after ingestion

2. **Check RPC function exists:**
   - In Supabase SQL Editor, run: `SELECT routine_name FROM information_schema.routines WHERE routine_name = 'match_kb';`
   - If empty, re-run `cloud/supabase/sql/01_init.sql`

3. **Test RPC manually:**
   ```sql
   -- Get a sample embedding first
   SELECT embedding FROM kb_embeddings LIMIT 1;
   -- Then test the RPC (replace with actual embedding vector)
   SELECT * FROM match_kb(
     (SELECT embedding FROM kb_embeddings LIMIT 1),
     6
   );
   ```

4. **Verify embedding dimensions:**
   - Should be 1536 dimensions for `text-embedding-3-large`
   - Check: `SELECT array_length(embedding, 1) FROM kb_embeddings LIMIT 1;`

### Worker 500 Errors

If the Cloudflare Worker returns 500 errors:

1. **Check Worker logs:**
   ```bash
   cd cloud/worker
   wrangler tail
   ```
   Look for error messages indicating which step failed (embeddings, supabase_rpc, chat_completion)

2. **Verify secrets are set:**
   ```bash
   wrangler secret list
   ```
   Should show: `OPENAI_API_KEY`, `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `CHAT_MODEL`

3. **Test RPC manually:**
   - Use curl to test the Supabase RPC directly:
   ```bash
   curl -X POST "https://YOUR_PROJECT.supabase.co/rest/v1/rpc/match_kb" \
     -H "apikey: YOUR_ANON_KEY" \
     -H "Authorization: Bearer YOUR_ANON_KEY" \
     -H "Content-Type: application/json" \
     -d '{"query_embedding": [0.1, 0.2, ...], "match_count": 6}'
   ```

4. **Check environment variables:**
   - Worker code checks for missing env vars and returns clear error messages
   - Look for `{ error: "Missing environment variables", missing: [...] }` in response

### Test Small Ingest

To test with 1-2 files and inspect logs:

```powershell

# Create a test folder with 1-2 markdown files

mkdir test_ingest

# Copy 1-2 small .md files there

# Run ingest on just that folder

python local\5_rag\ingest\ingest_supabase.py --roots test_ingest

# Check the logs

cat ingest.log
```

Look for:
- ✅ Start/end messages with file count and chunk count
- 📊 Token estimates (chars / 4)
- 📦 Batch progress
- ✅ Success messages or ❌ errors with details

You're done. Enjoy your second brain.
