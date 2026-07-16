---
layout: page
title: "AI Ingestion Pipeline Setup"
slug: "ai_ingestion_pipeline_setup"
created_at: "2026-05-18 11:37:37"
updated_at: "2026-07-16T06:49:32-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-007.json"
template_key: master-template
date: 2026-05-18
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a0b4033-5454-83ea-bb9a-5bfd306f2478"
canonical_ref: ""
---

# AI Ingestion Pipeline Setup

## Overview
- **Date**: 2026-05-18 11:37:37
- **Conversation ID**: `6a0b4033-5454-83ea-bb9a-5bfd306f2478`
- **Source**: `Chat-Export-28513-2026/conversations-007.json`

## Chat History

### User
> We need to get this AI ingestion pipeline, memory rag graph database up and running already, codex can build it what do i tell it to do.

### Assistant
> Yeah. This is the right thread to pull now: stop debating architecture and have Codex build the first boring-but-working ingestion spine. I’m going to give you a Codex-ready build brief that starts local-first, respects QiAccess doctrine, and avoids the “cathedral before plumbing” trap.

### Assistant
> Yes. Tell Codex to build **the ingestion spine**, not the whole AI brain. First win is: **Paperless/Drive/docs → normalized text chunks → embeddings in Qdrant → document/entity graph in Neo4j → searchable API → simple admin UI/logs.**
> 
> The doctrine fit: QiAccess says derived systems like vectors, graphs, summaries, and dashboards are **not canonical truth**; they are helpers built from repo docs, database records, Google Drive files, and Wiki.js/Paperless source pages. So the pipeline should preserve source references and never pretend generated summaries are truth. fileciteturn0file0
> 
> Here’s the Codex prompt.
> 
> ```text
> You are working inside the QiAccess Start / QiServer ecosystem.
> 
> Build the first working version of Cody’s local-first AI ingestion, memory, RAG, and graph pipeline.
> 
> DO NOT overbuild. DO NOT invent a giant platform. Build the boring spine that works.
> 
> Goal:
> Create a local-first ingestion service that can pull documents from known sources, normalize them, chunk them, embed them with Ollama, store vectors in Qdrant, store document/entity relationships in Neo4j, and expose search/query endpoints for QiAccess Start, Wiki.js, and future agents.
> 
> Current stack assumptions:
> - Runtime: qiserver
> - Containers already exist or may exist: Paperless-ngx, Qdrant, Neo4j, Ollama, Open WebUI, Wiki.js, Portainer
> - Preferred language: Python for ingestion/backend
> - API: FastAPI
> - Storage: local SQLite or Postgres for ingestion ledger, depending on current repo patterns
> - Vector DB: Qdrant
> - Graph DB: Neo4j
> - Embeddings: Ollama local embedding endpoint
> - Canonical truth remains source files/docs/databases. Vector/graph/search outputs are derived indexes only.
> 
> Important doctrine:
> - Do not treat AI summaries as canonical truth.
> - Every chunk, vector, and graph node must point back to a source document.
> - Every ingestion run must be logged.
> - Every document must have a stable source_id.
> - Every chunk must have a stable chunk_id.
> - Use simple, readable code.
> - Prefer working pipeline over clever abstractions.
> - Keep secrets in .env, never hardcode.
> - Admin/control services must remain local/private unless explicitly configured otherwise.
> 
> Build this as a new backend module/service unless an existing backend clearly exists.
> 
> Suggested folder:
> services/ai_ingestion/
> 
> Inside it create:
> - README.md
> - .env.example
> - requirements.txt or pyproject.toml
> - app/main.py
> - app/config.py
> - app/models.py
> - app/ingest/
>   - sources/
>     - paperless.py
>     - local_folder.py
>     - markdown_repo.py
>   - normalize.py
>   - chunk.py
>   - embed.py
>   - qdrant_store.py
>   - graph_store.py
>   - ledger.py
>   - pipeline.py
> - app/api/
>   - routes_health.py
>   - routes_ingest.py
>   - routes_search.py
>   - routes_graph.py
> - app/cli.py
> - scripts/
>   - run_ingest_once.py
>   - test_connections.py
> - docker-compose.ai-ingestion.yml
> - docs/
>   - AI_Ingestion_Pipeline.md
>   - Graph_Schema.md
>   - RAG_Query_Model.md
> 
> Phase 1: Connection tests
> Build a script:
> scripts/test_connections.py
> 
> It should test:
> - Ollama endpoint
> - Qdrant endpoint
> - Neo4j endpoint
> - Paperless endpoint if credentials are present
> - local folder path if configured
> 
> Output clear PASS/FAIL messages.
> 
> Environment variables:
> OLLAMA_BASE_URL=http://127.0.0.1:11434
> OLLAMA_EMBED_MODEL=nomic-embed-text
> QDRANT_URL=http://127.0.0.1:6333
> QDRANT_COLLECTION=qi_memory_chunks
> NEO4J_URI=bolt://127.0.0.1:7687
> NEO4J_USER=neo4j
> NEO4J_PASSWORD=
> PAPERLESS_BASE_URL=http://127.0.0.1:8010
> PAPERLESS_TOKEN=
> LOCAL_INGEST_PATH=
> INGEST_LEDGER_DB=./data/ingestion_ledger.sqlite
> 
> Phase 2: Ingestion ledger
> Create a local ingestion ledger that tracks:
> - source_id
> - source_type
> - source_uri
> - title
> - checksum/hash
> - modified_at/source_modified_at
> - ingested_at
> - ingestion_status
> - error_message
> - chunk_count
> - embedding_model
> - graph_status
> 
> Use SQLite for v1 unless the repo already has a better DB convention.
> 
> The ledger prevents reprocessing unchanged documents.
> 
> Phase 3: Source connectors
> Implement three source connectors:
> 
> 1. Paperless connector
> - Pull document metadata and text/content from Paperless API.
> - Support pagination.
> - Do not delete or modify Paperless documents.
> - Source type: paperless
> - source_id format: paperless:{document_id}
> 
> 2. Local folder connector
> - Walk a configured folder.
> - Include .md, .txt, .pdf text if extraction is already available/simple.
> - Skip binary/build junk:
>   node_modules, dist, build, .next, .git, __pycache__, .venv, vendor
> - Source type: local_file
> - source_id format: local_file:{sha256_of_absolute_path}
> 
> 3. Markdown repo connector
> - Walk repo docs and markdown files.
> - Prioritize docs/, README.md, architecture/runbook files.
> - Source type: repo_doc
> - source_id format: repo_doc:{relative_path_hash}
> 
> Phase 4: Normalization
> Normalize documents into:
> {
>   source_id,
>   source_type,
>   source_uri,
>   title,
>   body_text,
>   metadata
> }
> 
> Keep source metadata:
> - path or Paperless document ID
> - created/modified dates if available
> - tags/correspondent/document_type if Paperless provides them
> - filename
> - extension
> - repo path when applicable
> 
> Phase 5: Chunking
> Create deterministic chunks:
> - Target chunk size: 800-1200 tokens or roughly 3500-5000 characters
> - Overlap: 100-200 tokens or roughly 500 characters
> - Preserve headings when possible for markdown
> - Each chunk must have:
>   chunk_id = sha256(source_id + chunk_index + chunk_text_hash)
>   source_id
>   chunk_index
>   text
>   metadata
> 
> Phase 6: Embeddings with Ollama
> Use Ollama /api/embed for embeddings.
> Batch where reasonable.
> Store embedding_model in metadata.
> If embedding fails, log and continue gracefully.
> 
> Phase 7: Qdrant storage
> Create collection if missing.
> Upsert chunk vectors into Qdrant.
> Payload must include:
> - chunk_id
> - source_id
> - source_type
> - source_uri
> - title
> - chunk_index
> - text preview or full text depending on size
> - tags/categories if available
> - ingested_at
> - embedding_model
> 
> Qdrant should be used for semantic search over chunks.
> 
> Phase 8: Neo4j graph storage
> Create a simple graph schema:
> 
> Nodes:
> - Document
> - Chunk
> - Source
> - Tag
> - Entity
> - IngestionRun
> 
> Relationships:
> - (Source)-[:PROVIDES]->(Document)
> - (Document)-[:HAS_CHUNK]->(Chunk)
> - (Document)-[:TAGGED_AS]->(Tag)
> - (Chunk)-[:MENTIONS]->(Entity)
> - (IngestionRun)-[:PROCESSED]->(Document)
> 
> For v1, entity extraction can be simple:
> - detect emails
> - dates
> - money amounts
> - likely people/org names with simple heuristics
> - hashtags/tags
> Do not rely on an LLM for entity extraction in v1 unless optional.
> 
> Use MERGE so re-ingestion is idempotent.
> 
> Phase 9: FastAPI endpoints
> Create endpoints:
> 
> GET /health
> Returns status for API.
> 
> GET /health/dependencies
> Checks Ollama, Qdrant, Neo4j, Paperless if configured.
> 
> POST /ingest/run
> Runs ingestion manually.
> Body:
> {
>   "sources": ["paperless", "local_folder", "markdown_repo"],
>   "limit": 50,
>   "force": false
> }
> 
> GET /ingest/runs
> Returns recent ingestion runs.
> 
> GET /search
> Query params:
> q
> limit
> source_type optional
> 
> Search Qdrant and return:
> - score
> - title
> - source_uri
> - source_type
> - chunk text
> - metadata
> 
> GET /graph/document/{source_id}
> Returns graph neighbors for a document.
> 
> GET /graph/entity/{name}
> Returns documents/chunks connected to an entity.
> 
> Phase 10: CLI
> Add CLI commands:
> python -m app.cli test
> python -m app.cli ingest --source paperless --limit 25
> python -m app.cli ingest --source markdown_repo
> python -m app.cli search "query text"
> 
> Phase 11: Docker/dev setup
> Provide docker-compose.ai-ingestion.yml for the FastAPI ingestion service only.
> Do not redefine Qdrant/Neo4j/Ollama unless absolutely necessary.
> Assume they are already hosted on qiserver or localhost.
> 
> Expose API locally only by default:
> 127.0.0.1:8095:8095
> 
> Phase 12: Documentation
> Create docs/AI_Ingestion_Pipeline.md explaining:
> - What the pipeline does
> - What it does not do
> - Source of truth rule
> - How to test connections
> - How to run ingestion once
> - How to search
> - How to troubleshoot
> 
> Create docs/Graph_Schema.md explaining node labels, relationships, properties, and examples.
> 
> Create docs/RAG_Query_Model.md explaining:
> - semantic search via Qdrant
> - relationship/context lookup via Neo4j
> - future API for agents
> - why the graph/vector DB are derived indexes, not truth
> 
> Acceptance criteria:
> 1. I can run connection tests and see clear PASS/FAIL.
> 2. I can ingest at least local markdown files.
> 3. I can ingest Paperless documents if credentials are configured.
> 4. Chunks are stored in Qdrant.
> 5. Document/chunk/source relationships are stored in Neo4j.
> 6. I can search with a text query and get relevant chunks back.
> 7. Re-running ingestion does not duplicate unchanged documents.
> 8. Every result includes source reference information.
> 9. README explains exact setup and commands.
> 10. The code is simple enough for another AI agent to maintain.
> 
> Do not build:
> - full chat UI
> - agent swarm
> - autonomous background planner
> - complicated auth
> - Supabase integration
> - fancy frontend
> - multi-tenant platform
> - production Cloudflare exposure
> 
> After implementing, produce:
> - concise summary of files changed
> - exact commands to run
> - exact .env variables needed
> - known limitations
> - next recommended phase
> ```
> 
> Use that as-is.
> 
> One thing I’d tighten: **make Codex start with local markdown ingestion first**, then Paperless. Paperless has a documented REST API and browsable schema, so it is a good connector, but don’t let API wiring block the pipeline skeleton. citeturn631174search3
> 
> The technical spine is sound: Qdrant supports batch point uploads/upserts for vector storage, Neo4j has an actively maintained Python driver for graph writes, and Ollama exposes a local embeddings API suitable for RAG pipelines. citeturn631174search0turn631174search6turn631174search1turn631174search13
> 
> The uncomfortable truth: don’t ask Codex to build “memory” yet. Ask it to build **ingestion ledger + vectors + graph + search API**. “Memory” is just the UX/personality layer on top of a trustworthy indexed substrate. Build the substrate first, then we let Gina get spooky.
