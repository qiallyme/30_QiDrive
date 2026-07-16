---
layout: page
title: GINA (Generative Intelligence Neural Archivist)
slug: gina-generative-intelligence-neural-archivist
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
uid: c6a8995ede62493dbce31ca87051e4df
canonical_ref: ""
template_key: master-template
---

# GINA (Generative Intelligence Neural Archivist)

Complete guide to GINA, the neural core of QiOS.

## Overview

GINA is the Generative Intelligence Neural Archivist - the orchestrator and neural core of QiOS. GINA coordinates ingestion, embedding, semantic routing, and provides intelligent chat capabilities with RAG (Retrieval Augmented Generation).

## Architecture

GINA operates at multiple levels:

1. **Local Core** (`workers/local/local_core/`) - Primary GINA implementation
   - FastAPI service on port 7130
   - SQLite database for local-first operation
   - OpenAI and Ollama integration

2. **Cloud Orchestrator** (`workers/cloud/orchestrator/`) - Cloud-based GINA
   - Cloudflare Worker for cloud deployment
   - Supabase integration for multi-device sync
   - RAG context from Memory Worker

## GINA Chat Endpoint

### Local Core: POST /gina/chat

**Request:**
```json
{
  "messages": [
    {
      "role": "user",
      "content": "What is QiOS Genesis-"
    }
  ],
  "realm": "QiVault",
  "enableRag": true
}
```

**Response:**
```json
{
  "answer": "QiOS Genesis is...",
  "matches": [...],
  "meta": {
    "rag_used": true,
    "match_count": 5,
    "chat_model": "gpt-4o-mini"
  }
}
```

### Cloud Orchestrator: POST /api/gina/chat

Similar interface, but uses cloud workers for processing.

## GINA Personality

GINA's system prompt includes:

- "You are Gina, Cody's assistant. Sassy, loyal, smart, direct, witty."
- "direct but warm"
- "sassy but caring"
- "ADHD-friendly"
- "very organized"
- "you keep Cody on track"
- "you remember context"
- "you DO NOT hallucinate tasks he didn't ask for"

## Features

### RAG (Retrieval Augmented Generation)

GINA uses RAG to provide context-aware responses:

1. User asks a question
2. GINA searches semantic_profile for relevant chunks
3. Injects matching context into system prompt
4. Generates response using LLM with context

### Function Calling

GINA supports tool execution:

- Start/stop workers
- Query system status
- Ingest files
- Query semantic memory

### System Telemetry

GINA gathers live system state:

- Worker status from `worker_status` table
- Ingestion queue status
- Semantic profile statistics
- System health metrics

## Integration

### QiNote Integration

QiNote connects to GINA via:
- `POST /gina/chat` for chat interface
- Automatic ingestion after note creation
- RAG search for related notes

### QiLauncher Integration

QiLauncher uses GINA for:
- System navigation and status queries
- File routing recommendations
- Workflow orchestration

## Configuration

### Environment Variables

```env

# OpenAI (primary LLM)

OPENAI_API_KEY=xxx

# Ollama (fallback LLM)

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_LLM_MODEL=llama3.2

# Supabase (for cloud sync)

SUPABASE_URL=https://xxx.supabase.co
SUPABASE_SERVICE_ROLE_KEY=xxx

# Local Core

QIOS_LOCAL_PORT=7130
QIOS_LOCAL_CORE_URL=http://localhost:7130
```

### Model Configuration

- **Primary**: OpenAI GPT-4o-mini (configurable)
- **Fallback**: Ollama llama3.2 (local)
- **Embeddings**: OpenAI text-embedding-3-small or Ollama nomic-embed-text

## API Contract

See `workers/local/local_core/gina_chat_contract.md` for the complete API contract.

Key points:
- Request/response models are strictly typed
- System context is automatically gathered
- RAG context is injected when `enableRag: true`
- Function calling is supported via tools manifest

## Testing

### Test GINA Chat

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

### Test with RAG

```powershell
$body = @{
    messages = @(
        @{
            role = "user"
            content = "What is QiOS Genesis-"
        }
    )
    realm = "QiVault"
    enableRag = $true
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:7130/gina/chat" `
    -Method POST `
    -Body $body `
    -ContentType "application/json"
```

## Troubleshooting

### GINA Doesn't Use RAG

1. Check `enableRag: true` in request
2. Verify embeddings exist in database
3. Check RAG search is working: `POST /query`
4. Review GINA logs for RAG errors

### Generic Responses

1. Verify RAG context is being injected
2. Check `rag_used: true` in response meta
3. Ensure semantic_profile has relevant content
4. Check match_count in response

### Function Calling Not Working

1. Verify tools manifest is loaded
2. Check tool execution permissions
3. Review function calling logs
4. Ensure tool definitions are correct

## Genesis Alignment

GINA aligns with:
- **Layer 6 (Semantic Routing)**: Intelligent file placement and retrieval
- **Layer 7 (Self-Healing)**: System health monitoring and recommendations

GINA is the **intelligence layer** that makes QiOS cognitive, not just a file system.
