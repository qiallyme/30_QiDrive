---
layout: page
title: Local Development Guide
slug: local-development-guide
status: publish
updated_at: "2026-07-16T06:49:37-04:00"
tags: []
  - projects
source_type: manual
summary: ""
created_at: "2026-07-01T23:17:15-05:00"
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: fa2f6d4a95b940fab71a4197baf7f5c4
canonical_ref: ""
template_key: master-template
---

# Local Development Guide

Complete guide for developing and running QiOS locally.

## Overview

QiOS Local Core is the **local-first brain** that runs on your machine. It provides ingestion, embeddings, semantic search, and GINA orchestrator functionality without requiring cloud services.

## Architecture

- **Database**: SQLite (`data/vector/qios_local.db`)
- **Runtime**: Python FastAPI service
- **Port**: 7130 (configurable via `QIOS_LOCAL_PORT`)
- **Location**: `workers/local/local_core/`

## Quick Start

### Automated Startup

```powershell
cd C:\QiOS_v1
.\start_qios_local.ps1
```

This script will:
- Check if Ollama is running and start it if needed
- Start Local Core service in a new window
- Optionally start the ingestion worker
- Run a status check

### Manual Setup

#### 1. Install Dependencies

```bash
cd workers/local/local_core
pip install -r requirements.txt
```

#### 2. Configure Environment

Create/update `.env` file in project root:

```env

# Supabase (for cloud sync, optional)

SUPABASE_URL=https://xxx.supabase.co
SUPABASE_ANON_KEY=xxx
SUPABASE_SERVICE_ROLE_KEY=xxx

# Ollama (for local LLM)

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_EMBEDDING_MODEL=nomic-embed-text
OLLAMA_LLM_MODEL=llama3.2

# Local Core

QIOS_LOCAL_PORT=7130
QIOS_LOCAL_CORE_URL=http://localhost:7130

# OpenAI (optional, for cloud embeddings)

OPENAI_API_KEY=xxx
```

#### 3. Start Services

**Start Ollama:**
```powershell
ollama serve
```

In another terminal, pull required models:
```powershell
ollama pull nomic-embed-text
ollama pull llama3.2
```

**Start Local Core:**
```powershell
cd workers/local/local_core
python qios_local_core.py
```

**Start Ingestion Worker (optional):**
```powershell
cd workers/local/local_core
python worker.py
```

## API Endpoints

### Health & Status

**GET /health**
```json
{
  "status": "ok",
  "db_path": "/path/to/data/vector/qios_local.db"
}
```

**GET /queue**
```json
{
  "total": 123,
  "by_status": {
    "pending": 100,
    "extracted": 20,
    "embedded": 3
  }
}
```

### Ingestion

**POST /ingest**
- Enqueue files/notes for processing
- Returns ingestion ID

**GET /ingest/{id}**
- Check ingestion status

### Query & RAG

**POST /query**
- Semantic search over local embeddings
- Returns matching chunks with similarity scores

**POST /gina/chat**
- GINA chat endpoint with RAG context
- Supports function calling and tool execution

## Database

SQLite database lives at `data/vector/qios_local.db`.

Migrations are in `workers/local/local_core/migrations/` and run automatically on startup.

## Worker Process

The ingestion worker (`worker.py`) continuously processes items:

1. Polls `ingestion_queue` for pending items
2. Extracts text from files
3. Generates embeddings (OpenAI or Ollama)
4. Writes to `semantic_profile` table
5. Updates queue status

**Environment variables:**
- `OPENAI_API_KEY` - Required for OpenAI embeddings
- `WORKER_NAME` - Default: `local-worker-01`
- `WORKER_BATCH_SIZE` - Default: 5
- `WORKER_SLEEP_MS` - Default: 300ms

## Testing

### Status Check

```powershell
cd workers/local/local_core
python check_status.py
```

### Run Tests

```powershell
cd workers/local/local_core
python tests/test_sanity_checks.py
```

### Manual API Test

```powershell
$body = @{
    messages = @(
        @{
            role = "user"
            content = "Who are you-"
        }
    )
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:7130/gina/chat" `
    -Method POST `
    -Body $body `
    -ContentType "application/json"
```

## Troubleshooting

### Ollama Not Running

- Check: `curl http://localhost:11434/api/tags`
- Start: `ollama serve`
- Pull models: `ollama pull nomic-embed-text` and `ollama pull llama3.2`

### Local Core Service Not Starting

- Check port 7130 is not in use: `netstat -an | findstr 7130`
- Check `.env` file exists and has correct variables
- Check Python dependencies: `pip install -r requirements.txt`

### RAG Not Working

- Check embeddings exist in SQLite database
- Verify Ollama embedding model is correct (nomic-embed-text, 768 dimensions)
- Check worker is processing ingestion queue

## Genesis Alignment

- **Layer 0 (Root Integrity)**: Lives under `workers/` as QiWorker
- **Layer 1 (Dark Matter)**: Protects system substrate
- **Layer 6 (Semantic Routing)**: Handles ingestion and routing
- **Layer 7 (Self-Healing)**: Tracks file history and events

This is the **local nervous system** before cloud sync.
