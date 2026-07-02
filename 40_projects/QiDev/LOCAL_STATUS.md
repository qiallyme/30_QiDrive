---
layout: page
title: Local Status & Control API
slug: local-status-control-api
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

# Local Status & Control API

The FastAPI server (`qi_rag_api_supabase.py`) exposes endpoints to monitor and control the ingestion system.

## Endpoints

### GET `/status`

Returns comprehensive status including:
- **KB Status**: From Supabase `get_kb_status()` RPC
  - `embeddings_rows`: Total embeddings in database
  - `files_indexed`: Number of files tracked
  - `bytes_indexed`: Total bytes indexed
  - `running`: Number of active ingest runs
  - `last_finished`: Timestamp of last completed run
  - `recent_errors_24h`: Error count in last 24 hours
- **Watcher Status**: Local watcher state
  - `running`: Whether watcher process is active
  - `queue_len`: Number of pending files in work queue
- **Roots**: Configured root directories from `config.yaml`
- **Last Run**: Most recent `kb_runs` record with status, counts, etc.

**Example:**
```bash
curl http://127.0.0.1:8010/status
```

**Response:**
```json
{
  "kb": {
    "embeddings_rows": 12345,
    "files_indexed": 234,
    "bytes_indexed": 56789012,
    "running": 0,
    "last_finished": "2025-01-15T10:30:00Z",
    "recent_errors_24h": 2
  },
  "watcher": {
    "running": true,
    "queue_len": 5
  },
  "roots": [
    "C:\\Users\\codyr\\My Drive\\QiOne",
    "C:\\Users\\codyr\\iCloudDrive\\QiOne"
  ],
  "last_run": {
    "id": 42,
    "started_at": "2025-01-15T10:00:00Z",
    "ended_at": "2025-01-15T10:30:00Z",
    "status": "success",
    "files_scanned": 234,
    "chunks_embedded": 1234,
    "chunks_upserted": 1234
  }
}
```

### POST `/control`

Control the watcher and ingestion process.

**Actions:**
- `"stop"`: Create `local/meta/STOP` file to pause watcher
- `"start"`: Remove STOP file to resume watcher
- `"reindex"`: Trigger full reindex (forces re-embedding of all files)

**Example:**
```bash

# Stop watcher

curl -X POST http://127.0.0.1:8010/control \
  -H "Content-Type: application/json" \
  -d '{"action": "stop"}'

# Start watcher

curl -X POST http://127.0.0.1:8010/control \
  -H "Content-Type: application/json" \
  -d '{"action": "start"}'

# Trigger reindex

curl -X POST http://127.0.0.1:8010/control \
  -H "Content-Type: application/json" \
  -d '{"action": "reindex"}'
```

**Response:**
```json
{
  "status": "stopped",
  "message": "Watcher will pause when it checks STOP file"
}
```

### GET `/logs`

Get last N lines from the ingest log file.

**Query Parameters:**
- `tail` (default: 200, max: 10000): Number of lines to return

**Example:**
```bash

# Get last 200 lines (default)

curl http://127.0.0.1:8010/logs

# Get last 500 lines

curl "http://127.0.0.1:8010/logs-tail=500"
```

**Response:**
```json
{
  "lines": [
    "2025-01-15 10:00:00 - INFO - Starting Supabase Ingestion",
    "2025-01-15 10:00:01 - INFO - Found 234 files to scan",
    "..."
  ]
}
```

## Incremental Ingestion Behavior

### How It Works

The ingestion system uses **SHA-256 file hashing** and **mtime (modification time)** to determine if files need re-processing:

1. **File State Tracking**: Each file's state is stored in:
   - **Local SQLite** (`local/meta/ingest.db`): Fast local checks
   - **Supabase** (`kb_files` table): Persistent across machines

2. **Change Detection**: A file is processed if:
   - File size changed
   - Modification time changed
   - Content SHA-256 hash changed
   - File not found in either state database

3. **Chunk-Level Deduplication**: Even if a file changed, only new or modified chunks are embedded and upserted (via `chunk_hash` unique constraint).

### When Files Are Skipped

Files are **automatically skipped** if:
- Size, mtime, and SHA256 match previous ingestion
- File was successfully ingested recently

### Force Reindex

To force re-processing of all files (ignoring state checks):

1. **Via API:**
   ```bash
   curl -X POST http://127.0.0.1:8010/control \
     -H "Content-Type: application/json" \
     -d '{"action": "reindex"}'
   ```

2. **Via Command Line:**
   ```powershell
   python local/5_rag/ingest/ingest_supabase.py --reindex
   ```

This will:
- Re-compute all file hashes
- Re-embed all chunks
- Update all state records
- Useful after schema changes or embedding model updates

## Watcher Control

### STOP/RESUME Files

The watcher respects control files in `local/meta/`:

- **`STOP`**: If this file exists, watcher pauses (doesn't queue new files)
- **`RESUME`**: If this file exists, watcher removes STOP and resumes

**Manual Control:**
```powershell

# Stop watcher

New-Item -ItemType File -Path "local\meta\STOP" -Force

# Resume watcher

Remove-Item -Path "local\meta\STOP" -ErrorAction SilentlyContinue
```

### Work Queue

Changed files are queued in SQLite `work_queue` table:
- Files are queued with `op='changed'` and `status='pending'`
- Queue can be processed by background worker (future enhancement)
- Current implementation processes queue during full ingest runs

## PowerShell Helpers

### `local/run_watch.ps1`

Start the file watcher:
```powershell
.\local\run_watch.ps1
```

### `local/run_ingest.ps1`

Run full ingestion pass:
```powershell
.\local\run_ingest.ps1
```

### `local/tail_logs.ps1`

Tail the ingest log file:
```powershell
.\local\tail_logs.ps1
```

## Configuration

All paths and settings are in `local/5_rag/config.yaml`:

```yaml
roots:
  - "C:\\Users\\codyr\\My Drive\\QiOne"
  - "C:\\Users\\codyr\\iCloudDrive\\QiOne"
include_ext: [".md", ".txt", ".csv", ".pdf"]
chunk_chars: 800
batch_max_items: 64
batch_max_chars: 250000
log_file: "local/meta/ingest.log"
state_db: "local/meta/ingest.db"
```

Update these paths to match your system.

## Troubleshooting

### Status Shows 0 Files

- Check that roots in `config.yaml` exist and are accessible
- Verify file extensions match `include_ext` list
- Run ingest with `--reindex` to force full scan

### Watcher Not Running

- Check if `local/meta/STOP` file exists and remove it
- Verify watcher process is running: `Get-Process python`
- Check logs: `.\local\tail_logs.ps1`

### Errors in Status

- Check `/logs` endpoint for detailed error messages
- Review Supabase `kb_errors` table via SQL Editor
- Verify Supabase credentials in `.env`
