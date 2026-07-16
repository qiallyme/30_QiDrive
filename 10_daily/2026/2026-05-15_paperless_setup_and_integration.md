---
layout: page
title: "Paperless Setup and Integration"
slug: "paperless_setup_and_integration"
created_at: "2026-05-15 07:19:31"
updated_at: "2026-05-15 07:19:31"
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
date: 2026-05-15
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a070f2f-fcb4-83ea-b85c-4daf2575cee2"
canonical_ref: ""
---

# Paperless Setup and Integration

## Overview
- **Date**: 2026-05-15 07:19:31
- **Conversation ID**: `6a070f2f-fcb4-83ea-b85c-4daf2575cee2`
- **Source**: `Chat-Export-28513-2026/conversations-007.json`

## Chat History

### User
> we need to work on finishing setting up paperless right away and prepare for the next step to take what paperless does and pipe into our tables/vector graph storage.

### Assistant
> Yes. We’re at the “make Paperless useful, not just installed” stage: intake → OCR/classify → export metadata/text → push into SQL/vector/graph. I’ll give you the right next sequence and the cold-start doc shape so Codex/server work doesn’t drift.

### Assistant
> Yes — Paperless needs to become the **document intake/OCR layer**, not the final brain. The final brain is:
> 
> **Paperless → canonical tables → chunks → vectors → graph → Wiki/QiAccess views**
> 
> That matches the QiAccess doctrine: Paperless belongs on **qiserver** as part of the self-hosted runtime, while vector search/graphs/reports are useful derived systems, not canonical truth. fileciteturn0file0
> 
> ## Immediate mission
> 
> ### Phase 1 — Finish Paperless correctly
> 
> Do **not** rebuild unless the current container is broken. First inspect what exists.
> 
> Run on `qiserver`:
> 
> ```bash
> sudo docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}"
> 
> sudo docker inspect paperless --format '{{json .Mounts}}' | jq
> 
> sudo docker logs --tail=100 paperless
> ```
> 
> Then verify the web UI:
> 
> ```bash
> curl -I http://localhost:8000 || curl -I http://localhost:8010 || curl -I http://localhost:8080
> ```
> 
> If Paperless is running healthy, the next job is not “install.” It is:
> 
> 1. confirm login works  
> 2. confirm consume folder works  
> 3. confirm OCR works  
> 4. create document types/tags/correspondents  
> 5. create API token  
> 6. add export/backup path  
> 7. add post-consumption hook or sync worker  
> 
> Paperless officially supports Docker Compose installs, watched consume folders, REST API access, and post-consumption scripts, so we should use those instead of inventing nonsense. citeturn551446search3turn551446search1turn551446search6
> 
> ---
> 
> ## Paperless folder standard for qiserver
> 
> Target structure:
> 
> ```bash
> /srv/qios/stacks/paperless/
> /srv/qios/data/paperless/consume
> /srv/qios/data/paperless/export
> /srv/qios/data/paperless/media
> /srv/qios/data/paperless/data
> /srv/qios/data/paperless/scripts
> /srv/qios/data/paperless/sync
> ```
> 
> But do **not** blindly move existing volumes yet. First inspect current mounts. Paperless docs note that Docker volume storage may live under Docker-managed volumes unless bind-mounted, so we need to know the current reality before moving anything. citeturn551446search10
> 
> Run:
> 
> ```bash
> sudo mkdir -p /srv/qios/data/paperless/{consume,export,media,data,scripts,sync}
> sudo chown -R qiadmin:qiadmin /srv/qios/data/paperless
> sudo chmod -R 775 /srv/qios/data/paperless
> ```
> 
> Then test the consume folder once we confirm its actual mounted path.
> 
> ---
> 
> ## Paperless setup checklist
> 
> Inside Paperless UI:
> 
> ### 1. Create base document types
> 
> Use practical categories first:
> 
> - Medical Record
> - Legal Filing
> - Court Notice
> - Financial Statement
> - Bill
> - Receipt
> - Tax Document
> - Insurance
> - Care Document
> - Identity / Vital Record
> - Tech / Server Doc
> - Reference
> 
> ### 2. Create starter tags
> 
> Use cross-cutting tags, not folders pretending to be tags:
> 
> - mom-care
> - legal
> - finance
> - medical
> - taxes
> - qiserver
> - qiaccess
> - urgent
> - review-needed
> - source-record
> - exported
> - synced
> 
> ### 3. Create correspondents
> 
> Examples:
> 
> - Ascension / Hospital
> - MyChart
> - Court / Clerk
> - FCFCU
> - Chase
> - IRS
> - SSA
> - Medicaid / Medicare
> - Utility Provider
> - Unknown Sender
> 
> ### 4. Set storage paths later
> 
> Do not over-design this yet. Paperless is not QiNexus. Paperless is the intake machine.
> 
> The clean rule:
> 
> **Paperless organizes scanned/OCR documents. QiNexus organizes canonical life/work files.**
> 
> ---
> 
> ## The pipeline we want
> 
> ### Layer 1 — Paperless
> 
> Paperless owns:
> 
> - original uploaded file
> - archive PDF
> - OCR text
> - title
> - correspondent
> - document type
> - tags
> - created date
> - added date
> - archive serial number
> - custom fields if needed
> 
> ### Layer 2 — Canonical SQL tables
> 
> This is where we normalize Paperless output.
> 
> Proposed tables:
> 
> #### `source_documents`
> 
> One row per Paperless document.
> 
> Fields:
> 
> - `id`
> - `paperless_id`
> - `title`
> - `document_type`
> - `correspondent`
> - `created_date`
> - `added_date`
> - `original_filename`
> - `archive_filename`
> - `content_hash`
> - `paperless_url`
> - `source_system`
> - `sync_status`
> - `last_synced_at`
> 
> #### `document_text`
> 
> One row per document text body.
> 
> Fields:
> 
> - `id`
> - `document_id`
> - `raw_text`
> - `clean_text`
> - `language`
> - `ocr_confidence`
> - `created_at`
> 
> #### `document_chunks`
> 
> One row per searchable chunk.
> 
> Fields:
> 
> - `id`
> - `document_id`
> - `chunk_index`
> - `chunk_text`
> - `token_count`
> - `section_hint`
> - `page_hint`
> - `embedding_id`
> - `created_at`
> 
> #### `document_entities`
> 
> Extracted names, dates, accounts, providers, court case numbers, etc.
> 
> Fields:
> 
> - `id`
> - `document_id`
> - `entity_type`
> - `entity_value`
> - `normalized_value`
> - `confidence`
> - `source_chunk_id`
> 
> #### `ingestion_jobs`
> 
> Audit trail so we know what happened.
> 
> Fields:
> 
> - `id`
> - `source_system`
> - `source_id`
> - `job_type`
> - `status`
> - `started_at`
> - `finished_at`
> - `error_message`
> 
> ---
> 
> ## Vector + graph split
> 
> Do not smash everything into one magic “AI database.” That gets ugly fast.
> 
> Use this:
> 
> ### SQL / Postgres
> 
> Canonical structured records.
> 
> Use for:
> 
> - document registry
> - sync status
> - document metadata
> - tags
> - entities
> - reports
> - dedupe
> - audits
> 
> ### Qdrant
> 
> Vector search.
> 
> Use for:
> 
> - semantic search
> - “find docs like this”
> - question answering over chunks
> - similarity lookup
> 
> ### Neo4j
> 
> Graph relationships.
> 
> Use for:
> 
> - person ↔ document
> - provider ↔ diagnosis/document
> - case ↔ filing ↔ exhibit
> - account ↔ statement ↔ transaction
> - event ↔ document ↔ timeline
> 
> Clean model:
> 
> **SQL tells us what exists. Qdrant finds meaning. Neo4j shows relationships.**
> 
> That’s the sauce. Not optional.
> 
> ---
> 
> ## Best integration method
> 
> There are two good options.
> 
> ### Option A — Scheduled sync worker
> 
> Simple and safer.
> 
> Every 5–15 minutes:
> 
> 1. call Paperless API
> 2. fetch changed documents
> 3. save/update metadata in Postgres
> 4. pull OCR text
> 5. chunk text
> 6. embed chunks into Qdrant
> 7. extract entities
> 8. upsert graph relationships into Neo4j
> 
> This is my preferred v1.
> 
> ### Option B — Paperless post-consumption script
> 
> Fast trigger after each new document.
> 
> Paperless supports post-consumption scripts in Docker by mounting a script directory and setting `PAPERLESS_POST_CONSUME_SCRIPT`. citeturn551446search6
> 
> But for us, the script should only enqueue a sync job. It should not do heavy AI work inside the Paperless container.
> 
> Correct pattern:
> 
> **Paperless consumes → post-consume script calls webhook → worker processes document**
> 
> Not:
> 
> **Paperless consumes → Paperless container runs all AI/vector/graph logic**
> 
> That second one is cursed. We do not put the whole kitchen inside the toaster.
> 
> ---
> 
> ## Immediate next commands for Codex/server
> 
> Create the future sync area:
> 
> ```bash
> sudo mkdir -p /srv/qios/apps/paperless-sync
> sudo mkdir -p /srv/qios/data/paperless/sync/{logs,tmp,state}
> sudo chown -R qiadmin:qiadmin /srv/qios/apps/paperless-sync /srv/qios/data/paperless/sync
> ```
> 
> Create environment placeholder:
> 
> ```bash
> cat > /srv/qios/apps/paperless-sync/.env.example <<'EOF'
> PAPERLESS_BASE_URL=http://paperless:8000
> PAPERLESS_API_TOKEN=change_me
> 
> POSTGRES_URL=postgresql://user:password@host:5432/qios
> QDRANT_URL=http://qdrant:6333
> NEO4J_URI=bolt://neo4j:7687
> NEO4J_USER=neo4j
> NEO4J_PASSWORD=change_me
> 
> SYNC_STATE_PATH=/data/state/paperless-sync-state.json
> LOG_LEVEL=info
> EOF
> ```
> 
> Create the first README:
> 
> ```bash
> cat > /srv/qios/apps/paperless-sync/README.md <<'EOF'
> # Paperless Sync Worker
> 
> ## Purpose
> 
> This worker moves Paperless-ngx document metadata and OCR text into Cody's structured knowledge pipeline.
> 
> Paperless is the intake and OCR layer.
> 
> The sync worker pushes normalized document records into SQL, chunk embeddings into Qdrant, and document relationships into Neo4j.
> 
> ## Source
> 
> - Paperless-ngx REST API
> - Paperless document metadata
> - Paperless OCR text
> - Paperless tags, correspondents, document types, and custom fields
> 
> ## Targets
> 
> - Postgres canonical document tables
> - Qdrant vector collections
> - Neo4j graph relationships
> 
> ## Rule
> 
> Paperless remains the document intake system.
> SQL remains the canonical structured registry.
> Qdrant and Neo4j are derived search/relationship systems.
> EOF
> ```
> 
> ---
> 
> ## Codex build instruction
> 
> Give Codex this:
> 
> Build `/srv/qios/apps/paperless-sync` as a standalone Python sync worker.
> 
> Requirements:
> 
> 1. Read config from `.env`.
> 2. Connect to Paperless-ngx REST API.
> 3. Fetch documents changed since last sync.
> 4. Store sync cursor in `/data/state/paperless-sync-state.json`.
> 5. Upsert document metadata into Postgres.
> 6. Fetch OCR/content text for each document.
> 7. Normalize and chunk text.
> 8. Generate embeddings later through a pluggable embedding provider.
> 9. Upsert vector chunks into Qdrant.
> 10. Upsert document/entity relationships into Neo4j.
> 11. Log every sync job.
> 12. Never delete records automatically.
> 13. Mark missing/deleted Paperless docs as inactive instead of removing them.
> 14. Include a README, `.env.example`, and `docker-compose.yml`.
> 15. Keep the worker independent from Paperless so Paperless upgrades do not break the knowledge pipeline.
> 
> ---
> 
> ## My recommended next step
> 
> Do this in order:
> 
> 1. Run the inspect/log commands.
> 2. Confirm the Paperless URL/port.
> 3. Drop one test PDF into the consume folder.
> 4. Verify OCR text appears in Paperless.
> 5. Create the API token.
> 6. Build `paperless-sync` as a separate worker.
> 
> The biggest mistake would be trying to build the vector/graph layer before verifying Paperless OCR + metadata are stable. That’s how you get a fancy broken pipeline. Paperless first, pipe second.

### User
> QISERVER → Runbook: /srv/qios/docs/000_RUN_ME_FIRST.md
> QISERVER → Status: qs
> QISERVER → UI: https://qiserver-1.cerberus-sirius.ts.net
> 
> qiadmin@qiserver:~$ sudo mkdir -p /srv/qios/data/paperless/{consume,export,media,data,scripts,sync}
> [sudo] password for qiadmin: 
> Sorry, try again.
> [sudo] password for qiadmin: 
> qiadmin@qiserver:~$ sudo mkdir -p /srv/qios/data/paperless/{consume,export,media,data,scripts,sync}
> qiadmin@qiserver:~$ sudo chown -R qiadmin:qiadmin /srv/qios/data/paperless
> qiadmin@qiserver:~$ sudo chmod -R 775 /srv/qios/data/paperless
> qiadmin@qiserver:~$ sudo docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}"
> 
> 
> 
> sudo docker inspect paperless --format '{{json .Mounts}}' | jq
> 
> 
> 
> sudo docker logs --tail=100 paperlessNAMES                        IMAGE                                        STATUS                          PORTS
> paperless                    ghcr.io/paperless-ngx/paperless-ngx:latest   Up 2 days (healthy)             127.0.0.1:8010->8000/tcp
> qitranscribe-whisper-webui   jhj0517/whisper-webui:latest                 Restarting (1) 19 seconds ago   
> solidtime                    solidtime/solidtime:latest                   Up 3 days (healthy)             80/tcp, 443/tcp, 2019/tcp, 443/udp, 127.0.0.1:8095->8000/tcp
> solidtime-db                 postgres:16                                  Up 3 days (healthy)             5432/tcp
> qdrant                       qdrant/qdrant:latest                         Up 3 days                       127.0.0.1:6333-6334->6333-6334/tcp
> uptime-kuma                  louislam/uptime-kuma:2                       Up 3 days (healthy)             127.0.0.1:3005->3001/tcp
> n8n                          docker.n8n.io/n8nio/n8n:latest               Up 3 days                       127.0.0.1:5678->5678/tcp
> portainer                    portainer/portainer-ce:sts                   Up 4 days                       8000/tcp, 9000/tcp, 127.0.0.1:9443->9443/tcp
> wikijs                       requarks/wiki:2                              Up 4 days                       3443/tcp, 127.0.0.1:3002->3000/tcp
> wikijs-db                    postgres:15-alpine                           Up 4 days                       5432/tcp
> homepage                     ghcr.io/gethomepage/homepage:latest          Up 3 days (healthy)             127.0.0.1:3001->3000/tcp
> paperless-postgres           postgres:16                                  Up 4 days                       5432/tcp
> paperless-redis              redis:7                                      Up 4 days                       6379/tcp
> nocodb                       nocodb/nocodb:latest                         Up 5 days                       127.0.0.1:8088->8080/tcp
> nocodb-db                    postgres:16                                  Up 5 days (healthy)             5432/tcp
> nocodb-redis                 redis:7-alpine                               Up 5 days                       6379/tcp
> cloudflared                  cloudflare/cloudflared:latest                Up 5 days                       
> open-webui                   ghcr.io/open-webui/open-webui:main           Up 5 days (healthy)             127.0.0.1:3000->8080/tcp
> neo4j                        neo4j:latest                                 Up 5 days                       127.0.0.1:7474->7474/tcp, 7473/tcp, 127.0.0.1:7687->7687/tcp
> qiadmin@qiserver:~$

### Assistant
> Good. Paperless is already healthy. So we do **not** reinstall. We proceed like sane people for once. Tiny miracle.
> 
> Current facts:
> 
> - Paperless UI is on: `127.0.0.1:8010 -> 8000`
> - Container name: `paperless`
> - DB: `paperless-postgres`
> - Redis: `paperless-redis`
> - Qdrant is already live on `127.0.0.1:6333`
> - Neo4j is already live on `127.0.0.1:7474` and `7687`
> - NocoDB is available on `127.0.0.1:8088`
> 
> That means the stack is basically ready for the intake pipeline. Now we need to verify mounts and Paperless paths.
> 
> ## Run this next
> 
> Your paste bundled several commands, but only `docker ps` clearly returned. Run these separately:
> 
> ```bash
> sudo docker inspect paperless --format '{{json .Mounts}}' | jq
> ```
> 
> Then:
> 
> ```bash
> sudo docker logs --tail=100 paperless
> ```
> 
> Then test the local Paperless UI:
> 
> ```bash
> curl -I http://127.0.0.1:8010
> ```
> 
> Then check whether Paperless sees a consume directory internally:
> 
> ```bash
> sudo docker exec -it paperless bash -lc 'ls -lah /usr/src/paperless/consume || ls -lah /consume || find / -maxdepth 3 -type d -name consume 2>/dev/null | head'
> ```
> 
> ## What we’re checking
> 
> We need to know whether the folder you just created:
> 
> ```bash
> /srv/qios/data/paperless/consume
> ```
> 
> is actually mounted into the Paperless container.
> 
> Creating the folder on the server is good, but it does **nothing** unless Docker Compose maps it into Paperless. That’s the next key truth.
> 
> ## Likely next fix
> 
> If the inspect output does **not** show `/srv/qios/data/paperless/consume`, we need to edit the Paperless compose file and add bind mounts.
> 
> Find the compose file:
> 
> ```bash
> sudo find /srv/qios -iname '*paperless*' -o -name 'docker-compose.yml' | sort
> ```
> 
> Better targeted:
> 
> ```bash
> sudo find /srv/qios/stacks -maxdepth 4 -type f \( -name 'docker-compose.yml' -o -name 'compose.yml' \) -print
> ```
> 
> Then inspect the Paperless stack folder:
> 
> ```bash
> ls -lah /srv/qios/stacks
> ```
> 
> If there is a paperless folder:
> 
> ```bash
> ls -lah /srv/qios/stacks/paperless
> cat /srv/qios/stacks/paperless/docker-compose.yml
> ```
> 
> ## After mounts are confirmed
> 
> We test ingestion:
> 
> ```bash
> echo "QiAccess Paperless OCR pipeline test $(date)" > /tmp/paperless_test.txt
> cp /tmp/paperless_test.txt /srv/qios/data/paperless/consume/
> ls -lah /srv/qios/data/paperless/consume/
> ```
> 
> Then watch logs:
> 
> ```bash
> sudo docker logs -f paperless
> ```
> 
> If Paperless consumes it, the file should disappear from `consume` and show up in the UI.
> 
> ## Strategic call
> 
> Do **not** touch vector/graph sync yet. We need this order:
> 
> 1. Confirm compose/mounts.
> 2. Confirm consume folder works.
> 3. Confirm OCR/import works.
> 4. Create Paperless API token.
> 5. Build `paperless-sync`.
> 6. Push to NocoDB/Postgres first.
> 7. Then Qdrant.
> 8. Then Neo4j.
> 
> Right now your next move is the `docker inspect` mount output. That tells us whether we’re wired or just making pretty folders in the void.

### User
> qiadmin@qiserver:~$ sudo docker inspect paperless --format '{{json .Mounts}}' | jq
> [
>   {
>     "Type": "bind",
>     "Source": "/srv/qios/data/paperless/consume",
>     "Destination": "/usr/src/paperless/consume",
>     "Mode": "rw",
>     "RW": true,
>     "Propagation": "rprivate"
>   },
>   {
>     "Type": "bind",
>     "Source": "/srv/qios/data/paperless/data",
>     "Destination": "/usr/src/paperless/data",
>     "Mode": "rw",
>     "RW": true,
>     "Propagation": "rprivate"
>   },
>   {
>     "Type": "bind",
>     "Source": "/srv/qios/data/paperless/export",
>     "Destination": "/usr/src/paperless/export",
>     "Mode": "rw",
>     "RW": true,
>     "Propagation": "rprivate"
>   },
>   {
>     "Type": "bind",
>     "Source": "/srv/qios/data/paperless/media",
>     "Destination": "/usr/src/paperless/media",
>     "Mode": "rw",
>     "RW": true,
>     "Propagation": "rprivate"
>   }
> ]
> qiadmin@qiserver:~$ ?
> ]
> qiadmin@qiserver:~$ sudo docker logs --tail=100 paperless
>     raise last_ex.with_traceback(None)
> psycopg.OperationalError: connection failed: connection to server at "172.23.0.2", port 5432 failed: FATAL:  could not open file "base/16384/2601": Permission denied
> 
> The above exception was the direct cause of the following exception:
> 
> Traceback (most recent call last):
>   File "/usr/local/lib/python3.12/site-packages/asgiref/sync.py", line 489, in thread_handler
>     raise exc_info[1]
>   File "/usr/local/lib/python3.12/site-packages/django/core/handlers/exception.py", line 42, in inner
>     response = await get_response(request)
>                ^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/asgiref/sync.py", line 489, in thread_handler
>     raise exc_info[1]
>   File "/usr/local/lib/python3.12/site-packages/django/core/handlers/base.py", line 284, in _get_response_async
>     response = await sync_to_async(
>                ^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/asgiref/sync.py", line 439, in __call__
>     ret = await asyncio.shield(exec_coro)
>           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/asgiref/current_thread_executor.py", line 40, in run
>     result = self.fn(*self.args, **self.kwargs)
>              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/asgiref/sync.py", line 493, in thread_handler
>     return func(*args, **kwargs)
>            ^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/template/response.py", line 114, in render
>     self.content = self.rendered_content
>                    ^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/template/response.py", line 92, in rendered_content
>     return template.render(context, self._request)
>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/template/backends/django.py", line 107, in render
>     return self.template.render(context)
>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/template/base.py", line 169, in render
>     with context.bind_template(self):
>          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/contextlib.py", line 137, in __enter__
>     return next(self.gen)
>            ^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/template/context.py", line 259, in bind_template
>     context = processor(self.request)
>               ^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/src/paperless/src/documents/context_processors.py", line 9, in settings
>     general_config = GeneralConfig()
>                      ^^^^^^^^^^^^^^^
>   File "<string>", line 3, in __init__
>   File "/usr/src/paperless/src/paperless/config.py", line 168, in __post_init__
>     app_config = self._get_config_instance()
>                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/src/paperless/src/paperless/config.py", line 17, in _get_config_instance
>     app_config = ApplicationConfiguration.objects.all().first()
>                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/models/query.py", line 1104, in first
>     for obj in queryset[:1]:
>                ~~~~~~~~^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/models/query.py", line 384, in __iter__
>     self._fetch_all()
>   File "/usr/local/lib/python3.12/site-packages/django/db/models/query.py", line 1949, in _fetch_all
>     self._result_cache = list(self._iterable_class(self))
>                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/models/query.py", line 91, in __iter__
>     results = compiler.execute_sql(
>               ^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/models/sql/compiler.py", line 1621, in execute_sql
>     cursor = self.connection.cursor()
>              ^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/utils/asyncio.py", line 26, in inner
>     return func(*args, **kwargs)
>            ^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 320, in cursor
>     return self._cursor()
>            ^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 296, in _cursor
>     self.ensure_connection()
>   File "/usr/local/lib/python3.12/site-packages/django/utils/asyncio.py", line 26, in inner
>     return func(*args, **kwargs)
>            ^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 278, in ensure_connection
>     with self.wrap_database_errors:
>          ^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/utils.py", line 91, in __exit__
>     raise dj_exc_value.with_traceback(traceback) from exc_value
>   File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 279, in ensure_connection
>     self.connect()
>   File "/usr/local/lib/python3.12/site-packages/django/utils/asyncio.py", line 26, in inner
>     return func(*args, **kwargs)
>            ^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 256, in connect
>     self.connection = self.get_new_connection(conn_params)
>                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/utils/asyncio.py", line 26, in inner
>     return func(*args, **kwargs)
>            ^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/backends/postgresql/base.py", line 332, in get_new_connection
>     connection = self.Database.connect(**conn_params)
>                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/psycopg/connection.py", line 120, in connect
>     raise last_ex.with_traceback(None)
> django.db.utils.OperationalError: connection failed: connection to server at "172.23.0.2", port 5432 failed: FATAL:  could not open file "base/16384/2601": Permission denied
> qiadmin@qiserver:~$

### Assistant
> Good catch: mounts are correct. The actual failure is not Paperless intake — it’s the Paperless Postgres data directory permissions. Different layer, same stack. We fix DB storage ownership before doing anything fancy.

### Assistant
> The Paperless bind mounts are **correct**:
> 
> - `/srv/qios/data/paperless/consume` → `/usr/src/paperless/consume`
> - `/data`
> - `/export`
> - `/media`
> 
> So the consume pipeline wiring is fine.
> 
> The failure is here:
> 
> ```text
> FATAL: could not open file "base/16384/2601": Permission denied
> ```
> 
> That is **Postgres**, not Paperless. Paperless is healthy as a container, but its database cannot read one of its own data files. Translation: the DB data directory ownership/permissions got messed up.
> 
> ## Do this next
> 
> ### 1. Inspect the Paperless Postgres mounts
> 
> ```bash
> sudo docker inspect paperless-postgres --format '{{json .Mounts}}' | jq
> ```
> 
> Also check what user Postgres runs as:
> 
> ```bash
> sudo docker exec paperless-postgres id
> ```
> 
> Most official Postgres containers use UID/GID `999:999`, but verify first because we are not guessing with database files. Cute how Linux loves to humble us.
> 
> ---
> 
> ## Likely fix
> 
> After you inspect, if the Postgres data source is something like:
> 
> ```text
> /srv/qios/data/paperless/postgres
> ```
> 
> or a Docker volume path, then stop only the Paperless stack services:
> 
> ```bash
> sudo docker stop paperless
> sudo docker stop paperless-postgres
> sudo docker stop paperless-redis
> ```
> 
> Then fix ownership.
> 
> ### If it is a bind mount under `/srv/qios/...`
> 
> Use the actual source path from inspect:
> 
> ```bash
> sudo chown -R 999:999 /srv/qios/data/paperless/postgres
> sudo find /srv/qios/data/paperless/postgres -type d -exec chmod 700 {} \;
> sudo find /srv/qios/data/paperless/postgres -type f -exec chmod 600 {} \;
> ```
> 
> Then restart:
> 
> ```bash
> sudo docker start paperless-redis
> sudo docker start paperless-postgres
> sleep 5
> sudo docker start paperless
> ```
> 
> Then check:
> 
> ```bash
> sudo docker logs --tail=80 paperless-postgres
> sudo docker logs --tail=80 paperless
> curl -I http://127.0.0.1:8010
> ```
> 
> ---
> 
> ## If Postgres uses a Docker volume instead
> 
> If inspect shows something like:
> 
> ```text
> /var/lib/docker/volumes/...
> ```
> 
> then do **not** hand-edit blindly yet. Run:
> 
> ```bash
> sudo docker inspect paperless-postgres --format '{{range .Mounts}}{{println .Source "->" .Destination}}{{end}}'
> ```
> 
> Then check ownership:
> 
> ```bash
> sudo ls -lah /var/lib/docker/volumes/
> ```
> 
> And for the exact volume source:
> 
> ```bash
> sudo ls -lah EXACT_SOURCE_FROM_INSPECT
> sudo ls -lah EXACT_SOURCE_FROM_INSPECT/_data | head
> ```
> 
> If `_data` exists, the safe ownership fix is usually:
> 
> ```bash
> sudo chown -R 999:999 EXACT_SOURCE_FROM_INSPECT/_data
> ```
> 
> Then restart the three Paperless containers.
> 
> ---
> 
> ## Why this happened
> 
> You ran:
> 
> ```bash
> sudo chown -R qiadmin:qiadmin /srv/qios/data/paperless
> ```
> 
> That was fine for Paperless document folders, but if the Postgres database directory lives somewhere inside `/srv/qios/data/paperless`, that command probably changed DB files away from the `postgres` container user.
> 
> So the fix is not “make everything qiadmin.”
> 
> Correct ownership split:
> 
> ```text
> /srv/qios/data/paperless/consume  → qiadmin:qiadmin okay
> /srv/qios/data/paperless/export   → qiadmin:qiadmin okay
> /srv/qios/data/paperless/media    → paperless container writable
> /srv/qios/data/paperless/data     → paperless container writable
> Postgres data directory           → postgres UID/GID, usually 999:999
> ```
> 
> ## After DB is fixed
> 
> Then we test consume:
> 
> ```bash
> echo "QiAccess Paperless OCR pipeline test $(date)" > /tmp/paperless_test.txt
> cp /tmp/paperless_test.txt /srv/qios/data/paperless/consume/
> sudo docker logs -f paperless
> ```
> 
> But don’t test ingestion until Postgres is clean. Right now the database is the blocker.
> 
> Paperless still fits exactly where we mapped it in QiAccess Start: part of the qiserver self-hosted service layer, feeding the broader knowledge/data system without becoming the whole system of record. fileciteturn0file0

### User
> qiadmin@qiserver:~$ sudo docker inspect paperless-postgres --format '{{json .Mounts}}' | jq
> [
>   {
>     "Type": "bind",
>     "Source": "/srv/qios/data/paperless/postgres",
>     "Destination": "/var/lib/postgresql/data",
>     "Mode": "rw",
>     "RW": true,
>     "Propagation": "rprivate"
>   }
> ]
> qiadmin@qiserver:~$ qiadmin@qiserver:~$ sudo docker exec paperless-postgres id
> uid=0(root) gid=0(root) groups=0(root)
> qiadmin@qiserver:~$

### Assistant
> Yep. Found it.
> 
> Your Paperless Postgres data lives here:
> 
> ```bash
> /srv/qios/data/paperless/postgres
> ```
> 
> And we accidentally made too much of `/srv/qios/data/paperless` owned by `qiadmin`. Postgres is choking because its internal files need Postgres-safe ownership/permissions.
> 
> One weird detail: `docker exec paperless-postgres id` returned `root`, but the actual postgres process usually still drops to the `postgres` user internally. So we’ll inspect the real running process before fixing.
> 
> ## Run this
> 
> ```bash
> sudo docker exec paperless-postgres bash -lc 'ps aux | head -20'
> ```
> 
> Then run:
> 
> ```bash
> sudo docker exec paperless-postgres bash -lc 'id postgres || true'
> ```
> 
> Now fix the DB directory:
> 
> ```bash
> sudo docker stop paperless
> sudo docker stop paperless-postgres
> sudo docker stop paperless-redis
> 
> sudo chown -R 999:999 /srv/qios/data/paperless/postgres
> sudo find /srv/qios/data/paperless/postgres -type d -exec chmod 700 {} \;
> sudo find /srv/qios/data/paperless/postgres -type f -exec chmod 600 {} \;
> 
> sudo docker start paperless-redis
> sudo docker start paperless-postgres
> sleep 5
> sudo docker start paperless
> ```
> 
> Then verify:
> 
> ```bash
> sudo docker logs --tail=80 paperless-postgres
> sudo docker logs --tail=80 paperless
> curl -I http://127.0.0.1:8010
> ```
> 
> ## Why this is safe
> 
> Postgres official containers normally use UID/GID `999:999` for the internal postgres user. Your bind mount is the database storage itself, so it must not be owned by `qiadmin`.
> 
> Going forward:
> 
> ```text
> /srv/qios/data/paperless/consume   = qiadmin writable
> /srv/qios/data/paperless/export    = qiadmin writable
> /srv/qios/data/paperless/media     = Paperless writable
> /srv/qios/data/paperless/data      = Paperless writable
> /srv/qios/data/paperless/postgres  = Postgres only, usually 999:999
> ```
> 
> ## After it comes back clean
> 
> Then test ingestion:
> 
> ```bash
> echo "QiAccess Paperless OCR pipeline test $(date)" > /tmp/paperless_test.txt
> cp /tmp/paperless_test.txt /srv/qios/data/paperless/consume/
> sudo docker logs -f paperless
> ```
> 
> If the file disappears from `consume` and shows up in Paperless, we’re back on track.

### User
> ok you are giving me command to fix stuff before i give you the output of the commands for verifying. ]
> qiadmin@qiserver:~$ sudo docker exec paperless-postgres id
> uid=0(root) gid=0(root) groups=0(root)
> qiadmin@qiserver:~$ sudo docker exec paperless-postgres bash -lc 'ps aux | head -20'
> USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
> postgres       1  0.0  0.3 216740 28048 ?        Ss   12:23   0:00 postgres
> postgres      28  0.0  0.1 216872  8428 ?        Ss   12:23   0:00 postgres: checkpointer 
> postgres      29  0.0  0.0 216896  7056 ?        Ss   12:23   0:00 postgres: background writer 
> postgres      31  0.0  0.1 216740  9964 ?        Ss   12:23   0:00 postgres: walwriter 
> postgres      32  0.0  0.1 218336  8756 ?        Ss   12:23   0:00 postgres: autovacuum launcher 
> postgres      33  0.0  0.1 218324  7916 ?        Ss   12:23   0:00 postgres: logical replication launcher 
> root          47 50.0  0.0   7084  3628 ?        Ss   12:26   0:00 bash -lc ps aux | head -20
> root          55  0.0  0.0   9392  4220 ?        R    12:26   0:00 ps aux
> root          56  0.0  0.0   5588  2044 ?        S    12:26   0:00 head -20
> qiadmin@qiserver:~$ sudo docker exec paperless-postgres bash -lc 'id postgres || true'
> uid=999(postgres) gid=999(postgres) groups=999(postgres),101(ssl-cert)
> qiadmin@qiserver:~$

### Assistant
> You’re right. I jumped one step too far. Good correction.
> 
> Now we **do** have the verification:
> 
> - Container exec default user = `root`
> - Actual Postgres process = `postgres`
> - Internal Postgres UID/GID = `999:999`
> - DB bind mount = `/srv/qios/data/paperless/postgres`
> - Error = Postgres process cannot read DB file because host permissions are wrong
> 
> So now the fix is justified.
> 
> ## Run this exact repair
> 
> ```bash
> sudo docker stop paperless
> sudo docker stop paperless-postgres
> sudo docker stop paperless-redis
> 
> sudo chown -R 999:999 /srv/qios/data/paperless/postgres
> sudo find /srv/qios/data/paperless/postgres -type d -exec chmod 700 {} \;
> sudo find /srv/qios/data/paperless/postgres -type f -exec chmod 600 {} \;
> 
> sudo docker start paperless-redis
> sudo docker start paperless-postgres
> sleep 5
> sudo docker start paperless
> ```
> 
> ## Then verify, in this order
> 
> ```bash
> sudo docker logs --tail=80 paperless-postgres
> ```
> 
> ```bash
> sudo docker logs --tail=80 paperless
> ```
> 
> ```bash
> curl -I http://127.0.0.1:8010
> ```
> 
> ## What we want to see
> 
> For `paperless-postgres`, we want something like:
> 
> ```text
> database system is ready to accept connections
> ```
> 
> For `paperless`, we want **no new**:
> 
> ```text
> Permission denied
> could not open file
> django.db.utils.OperationalError
> ```
> 
> For curl, we want:
> 
> ```text
> HTTP/1.1 200
> ```
> 
> or possibly:
> 
> ```text
> HTTP/1.1 302
> ```
> 
> Either is fine. A 500 is not.
> 
> After that, we test document intake.

### Assistant
> You’re right again — and now the output tells us the actual state.
> 
> ## What happened
> 
> Postgres recovered successfully:
> 
> ```text
> database system is ready to accept connections
> ```
> 
> But Paperless is now **stopped**:
> 
> ```text
> [INFO] Shutting down granian
> worker: Warm shutdown
> ```
> 
> And curl confirms nothing is listening:
> 
> ```text
> curl: (7) Failed to connect to 127.0.0.1 port 8010
> ```
> 
> So we are past the DB permission error, but the Paperless app container did not stay running after restart. The old Paperless log still shows the prior DB error, but the important current issue is: **Paperless is not up.** fileciteturn1file0
> 
> ## Next: inspect current container state
> 
> Run this first:
> 
> ```bash
> sudo docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" | grep -E 'paperless|NAMES'
> ```
> 
> Then:
> 
> ```bash
> sudo docker start paperless
> sleep 5
> sudo docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" | grep -E 'paperless|NAMES'
> sudo docker logs --tail=120 paperless
> ```
> 
> ## If Paperless exits again
> 
> Run:
> 
> ```bash
> sudo docker inspect paperless --format 'ExitCode={{.State.ExitCode}} Error={{.State.Error}} FinishedAt={{.State.FinishedAt}}'
> ```
> 
> And:
> 
> ```bash
> sudo docker inspect paperless --format '{{json .Config.Env}}' | jq
> ```
> 
> ## Why I’m not giving the next repair yet
> 
> Because now the blocker changed. Before, the DB could not read files. Now Postgres looks alive, but the Paperless container isn’t serving on `8010`.
> 
> The next fact we need is whether Paperless:
> 
> 1. is exited,
> 2. is restarting,
> 3. started without the port binding,
> 4. crashed due to stale DB connection,
> 5. crashed due to another permission issue in `/data` or `/media`.
> 
> Run the `ps -a`, `start`, and fresh `logs` commands. That tells us which branch we’re on.

### User
> [INFO] Shutting down granian
> 
> worker: Warm shutdown (MainProcess)
> qiadmin@qiserver:~$ curl -I http://127.0.0.1:8010
> curl: (7) Failed to connect to 127.0.0.1 port 8010 after 0 ms: Couldn't connect to server
> qiadmin@qiserver:~$ sudo docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" | grep -E 'paperless|NAMES'
> NAMES                        STATUS                          PORTS
> paperless                    Exited (0) About a minute ago   
> paperless-postgres           Up 4 minutes                    5432/tcp
> paperless-redis              Up 4 days                       6379/tcp
> qiadmin@qiserver:~$

### Assistant
> Perfect. That tells us a lot.
> 
> Paperless did **not crash**. It exited cleanly:
> 
> ```text id="6s6lox"
> paperless Exited (0)
> ```
> 
> That means this is probably **not** a new fatal error. It likely shut down because of either:
> 
> 1. the container command/entrypoint is wrong,
> 2. the compose service is configured oddly,
> 3. it was started outside compose and exited after running a one-shot command,
> 4. or the app shut down cleanly after failing its dependency check.
> 
> Now we inspect before touching anything else. No more swinging the hammer blind.
> 
> ## Run these
> 
> ```bash id="3aijqe"
> sudo docker inspect paperless --format 'Image={{.Config.Image}}'
> sudo docker inspect paperless --format 'Entrypoint={{json .Config.Entrypoint}}'
> sudo docker inspect paperless --format 'Cmd={{json .Config.Cmd}}'
> sudo docker inspect paperless --format 'RestartPolicy={{json .HostConfig.RestartPolicy}}'
> ```
> 
> Then get the fresh start behavior:
> 
> ```bash id="x55tb7"
> sudo docker start paperless
> sleep 8
> sudo docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" | grep -E 'paperless|NAMES'
> sudo docker logs --tail=160 paperless
> ```
> 
> ## Also find the compose file
> 
> ```bash id="w8hg22"
> sudo find /srv/qios/stacks -maxdepth 5 -type f \( -name 'docker-compose.yml' -o -name 'compose.yml' \) -print | sort
> ```
> 
> If you see a Paperless folder, run:
> 
> ```bash id="hbd0y2"
> sudo cat /srv/qios/stacks/paperless/docker-compose.yml
> ```
> 
> or if it uses `compose.yml`:
> 
> ```bash id="xlc9cf"
> sudo cat /srv/qios/stacks/paperless/compose.yml
> ```
> 
> ## What I’m looking for
> 
> The key thing is this:
> 
> ```text id="rdp0ij"
> Cmd=[...]
> Entrypoint=[...]
> RestartPolicy={...}
> ```
> 
> If `Cmd` is something weird like a management command, migration, or consumer-only command, that explains the clean exit.
> 
> If the compose file has `command:` set incorrectly, we fix that.
> 
> If the compose file is fine, we start it through compose instead of raw `docker start`.
> 
> Right now, the database appears recovered, but the Paperless app is simply not staying alive. The clean exit is the clue. The prior logs show the database permission issue and then a warm shutdown, while curl shows the web server is no longer listening. fileciteturn1file0

### User
> qiadmin@qiserver:~$ curl -I http://127.0.0.1:8010
> curl: (7) Failed to connect to 127.0.0.1 port 8010 after 0 ms: Couldn't connect to server
> qiadmin@qiserver:~$ sudo docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" | grep -E 'paperless|NAMES'
> NAMES                        STATUS                          PORTS
> paperless                    Exited (0) About a minute ago   
> paperless-postgres           Up 4 minutes                    5432/tcp
> paperless-redis              Up 4 days                       6379/tcp
> qiadmin@qiserver:~$ sudo docker inspect paperless --format 'Image={{.Config.Image}}'
> 
> sudo docker inspect paperless --format 'Entrypoint={{json .Config.Entrypoint}}'
> 
> sudo docker inspect paperless --format 'Cmd={{json .Config.Cmd}}'
> 
> sudo docker inspect paperless --format 'RestartPolicy={{json .HostConfig.RestartPolicy}}'Image=ghcr.io/paperless-ngx/paperless-ngx:latest
> qiadmin@qiserver:~$ 
> qiadmin@qiserver:~$ sudo docker start paperless
> 
> sleep 8
> 
> sudo docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" | grep -E 'paperless|NAMES'
> 
> sudo docker logs --tail=160 paperlesspaperless
> qiadmin@qiserver:~$

### Assistant
> Good — but your terminal only returned the **first inspect line**:
> 
> ```text
> Image=ghcr.io/paperless-ngx/paperless-ngx:latest
> ```
> 
> It did **not** show:
> 
> - Entrypoint
> - Cmd
> - RestartPolicy
> - fresh `docker ps`
> - fresh logs
> 
> So either the paste got interrupted, or the terminal ate the batch. Annoying, but not fatal.
> 
> Run these **one at a time** so we don’t get half-output chaos.
> 
> ## 1. Check whether Paperless stayed running after start
> 
> ```bash
> sudo docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" | grep -E 'paperless|NAMES'
> ```
> 
> If it says `Up`, test:
> 
> ```bash
> curl -I http://127.0.0.1:8010
> ```
> 
> If it says `Exited`, continue.
> 
> ## 2. Get the missing inspect fields
> 
> ```bash
> sudo docker inspect paperless --format 'Entrypoint={{json .Config.Entrypoint}}'
> ```
> 
> ```bash
> sudo docker inspect paperless --format 'Cmd={{json .Config.Cmd}}'
> ```
> 
> ```bash
> sudo docker inspect paperless --format 'RestartPolicy={{json .HostConfig.RestartPolicy}}'
> ```
> 
> ## 3. Get fresh logs
> 
> ```bash
> sudo docker logs --tail=200 paperless
> ```
> 
> ## 4. Find the compose file
> 
> ```bash
> sudo find /srv/qios/stacks -maxdepth 5 -type f \( -name 'docker-compose.yml' -o -name 'compose.yml' \) -print | sort
> ```
> 
> If there is a Paperless stack folder, run:
> 
> ```bash
> ls -lah /srv/qios/stacks/paperless
> ```
> 
> Then whichever exists:
> 
> ```bash
> sudo cat /srv/qios/stacks/paperless/docker-compose.yml
> ```
> 
> or:
> 
> ```bash
> sudo cat /srv/qios/stacks/paperless/compose.yml
> ```
> 
> ## What I think is happening
> 
> The database permission problem was real and appears fixed because Postgres reached:
> 
> ```text
> database system is ready to accept connections
> ```
> 
> But the Paperless app is still not serving, and earlier it exited cleanly with `Exited (0)`, plus `curl` could not connect to port `8010`. That means we’re now debugging the app container’s launch behavior, not the DB permissions anymore. fileciteturn1file0
> 
> The next most useful thing is `Cmd=` and the fresh `docker logs --tail=200 paperless`. That will tell us whether it’s a command/compose issue or a second permission issue.

### User
> qiadmin@qiserver:~$ sudo docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" | grep -E 'paperless|NAMES'
> NAMES                        STATUS                          PORTS
> paperless                    Up About a minute (healthy)     127.0.0.1:8010->8000/tcp
> paperless-postgres           Up 12 minutes                   5432/tcp
> paperless-redis              Up 4 days                       6379/tcp
> qiadmin@qiserver:~$ curl -I http://127.0.0.1:8010
> HTTP/1.1 302 Found
> content-type: text/html; charset=utf-8
> location: /accounts/login/?next=/
> x-frame-options: SAMEORIGIN
> content-length: 0
> vary: Accept-Language, origin, Cookie
> content-language: en-us
> x-content-type-options: nosniff
> referrer-policy: same-origin
> cross-origin-opener-policy: same-origin
> server: granian
> date: Fri, 15 May 2026 12:36:27 GMT
> 
> qiadmin@qiserver:~$ sudo docker inspect paperless --format 'Entrypoint={{json .Config.Entrypoint}}'
> Entrypoint=["/init"]
> qiadmin@qiserver:~$ sudo docker inspect paperless --format 'Cmd={{json .Config.Cmd}}'
> Cmd=null
> qiadmin@qiserver:~$ sudo docker inspect paperless --format 'RestartPolicy={{json .HostConfig.RestartPolicy}}'
> RestartPolicy={"Name":"unless-stopped","MaximumRetryCount":0}
> qiadmin@qiserver:~$ sudo docker logs --tail=200 paperless
>     return func(*args, **kwargs)
>            ^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 256, in connect
>     self.connection = self.get_new_connection(conn_params)
>                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/utils/asyncio.py", line 26, in inner
>     return func(*args, **kwargs)
>            ^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/backends/postgresql/base.py", line 332, in get_new_connection
>     connection = self.Database.connect(**conn_params)
>                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/psycopg/connection.py", line 120, in connect
>     raise last_ex.with_traceback(None)
> psycopg.OperationalError: connection failed: connection to server at "172.23.0.2", port 5432 failed: FATAL:  could not open file "base/16384/2601": Permission denied
> 
> The above exception was the direct cause of the following exception:
> 
> Traceback (most recent call last):
>   File "/usr/local/lib/python3.12/site-packages/asgiref/sync.py", line 489, in thread_handler
>     raise exc_info[1]
>   File "/usr/local/lib/python3.12/site-packages/django/core/handlers/exception.py", line 42, in inner
>     response = await get_response(request)
>                ^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/asgiref/sync.py", line 489, in thread_handler
>     raise exc_info[1]
>   File "/usr/local/lib/python3.12/site-packages/django/core/handlers/base.py", line 284, in _get_response_async
>     response = await sync_to_async(
>                ^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/asgiref/sync.py", line 439, in __call__
>     ret = await asyncio.shield(exec_coro)
>           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/asgiref/current_thread_executor.py", line 40, in run
>     result = self.fn(*self.args, **self.kwargs)
>              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/asgiref/sync.py", line 493, in thread_handler
>     return func(*args, **kwargs)
>            ^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/template/response.py", line 114, in render
>     self.content = self.rendered_content
>                    ^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/template/response.py", line 92, in rendered_content
>     return template.render(context, self._request)
>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/template/backends/django.py", line 107, in render
>     return self.template.render(context)
>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/template/base.py", line 169, in render
>     with context.bind_template(self):
>          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/contextlib.py", line 137, in __enter__
>     return next(self.gen)
>            ^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/template/context.py", line 259, in bind_template
>     context = processor(self.request)
>               ^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/src/paperless/src/documents/context_processors.py", line 9, in settings
>     general_config = GeneralConfig()
>                      ^^^^^^^^^^^^^^^
>   File "<string>", line 3, in __init__
>   File "/usr/src/paperless/src/paperless/config.py", line 168, in __post_init__
>     app_config = self._get_config_instance()
>                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/src/paperless/src/paperless/config.py", line 17, in _get_config_instance
>     app_config = ApplicationConfiguration.objects.all().first()
>                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/models/query.py", line 1104, in first
>     for obj in queryset[:1]:
>                ~~~~~~~~^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/models/query.py", line 384, in __iter__
>     self._fetch_all()
>   File "/usr/local/lib/python3.12/site-packages/django/db/models/query.py", line 1949, in _fetch_all
>     self._result_cache = list(self._iterable_class(self))
>                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/models/query.py", line 91, in __iter__
>     results = compiler.execute_sql(
>               ^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/models/sql/compiler.py", line 1621, in execute_sql
>     cursor = self.connection.cursor()
>              ^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/utils/asyncio.py", line 26, in inner
>     return func(*args, **kwargs)
>            ^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 320, in cursor
>     return self._cursor()
>            ^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 296, in _cursor
>     self.ensure_connection()
>   File "/usr/local/lib/python3.12/site-packages/django/utils/asyncio.py", line 26, in inner
>     return func(*args, **kwargs)
>            ^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 278, in ensure_connection
>     with self.wrap_database_errors:
>          ^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/utils.py", line 91, in __exit__
>     raise dj_exc_value.with_traceback(traceback) from exc_value
>   File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 279, in ensure_connection
>     self.connect()
>   File "/usr/local/lib/python3.12/site-packages/django/utils/asyncio.py", line 26, in inner
>     return func(*args, **kwargs)
>            ^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 256, in connect
>     self.connection = self.get_new_connection(conn_params)
>                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/utils/asyncio.py", line 26, in inner
>     return func(*args, **kwargs)
>            ^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/django/db/backends/postgresql/base.py", line 332, in get_new_connection
>     connection = self.Database.connect(**conn_params)
>                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/usr/local/lib/python3.12/site-packages/psycopg/connection.py", line 120, in connect
>     raise last_ex.with_traceback(None)
> django.db.utils.OperationalError: connection failed: connection to server at "172.23.0.2", port 5432 failed: FATAL:  could not open file "base/16384/2601": Permission denied
> [INFO] Shutting down granian
> 
> worker: Warm shutdown (MainProcess)
> [init-start] paperless-ngx docker container starting...
> [init-start] paperless-ngx docker container starting init as root
> [env-init] Checking for environment from files
> [env-init] No *_FILE environment found
> [init-redis-wait] Waiting for Redis to report ready
> [init-db-wait] Waiting for PostgreSQL to start...
> [init-tesseract-langs] Checking if additional teseract languages needed
> [init-tesseract-langs] No additional installs requested
> [init-user] No UID changes for paperless
> [init-user] No GID changes for paperless
> [init-folders] Running with root privileges, adjusting directories and permissions
> paperless-db:5432 - accepting connections
> [init-db-wait] Connected to PostgreSQL
> [init-db-wait] Database is ready
> [init-migrations] Apply database migrations...
> Waiting for Redis...
> Connected to Redis broker.
> [init-redis-wait] Redis ready
> Operations to perform:
>   Apply all migrations: account, admin, auditlog, auth, authtoken, contenttypes, django_celery_results, documents, guardian, mfa, paperless, paperless_mail, sessions, socialaccount
> Running migrations:
>   No migrations to apply.
> [init-superuser] Creating superuser...
> Did not create superuser, a user cody already exists
> [init-superuser] Superuser creation done
> [init-checks] Running Django checks
> System check identified no issues (0 silenced).
> [custom-init] /custom-cont-init.d doesn't exist, nothing to do
> [init-complete] paperless-ngx docker container init completed in 12 seconds
> [init-complete] Starting services
> [svc-flower] Checking if we should start flower...
> [svc-flower] Not starting flower
> [INFO] Starting granian (main PID: 177)
> [INFO] Listening at: http://:::8000
> [INFO] Spawning worker-1 with PID: 197
> celery beat v5.5.3 (immunity) is starting.
> [2026-05-15 07:35:17,391] [INFO] [paperless.management.consumer] Polling directory for changes: /usr/src/paperless/consume
> [2026-05-15 07:35:17,674] [INFO] [paperless.asgi] [init] Paperless-ngx version: v2.20.15
> __    -    ... __   -        _
> LocalTime -> 2026-05-15 07:35:18
> Configuration ->
>     . broker -> redis://paperless-broker:6379//
>     . loader -> celery.loaders.app.AppLoader
>     . scheduler -> celery.beat.PersistentScheduler
>     . db -> /usr/src/paperless/data/celerybeat-schedule.db
>     . logfile -> [stderr]@%INFO
>     . maxinterval -> 5.00 minutes (300s)
> [2026-05-15 07:35:18,067] [INFO] [celery.beat] beat: Starting...
> [2026-05-15 07:35:18,098] [INFO] [celery.beat] Scheduler: Sending due task Check all e-mail accounts (paperless_mail.tasks.process_mail_accounts)
>  
>  -------------- celery@7c43be1853d3 v5.5.3 (immunity)
> --- ***** ----- 
> -- ******* ---- Linux-6.17.0-23-generic-x86_64-with-glibc2.41 2026-05-15 07:35:18
> - *** --- * --- 
> - ** ---------- [config]
> - ** ---------- .> app:         paperless:0x787aa3bb1e20
> - ** ---------- .> transport:   redis://paperless-broker:6379//
> - ** ---------- .> results:     
> - *** --- * --- .> concurrency: 1 (prefork)
> -- ******* ---- .> task events: ON
> --- ***** ----- 
>  -------------- [queues]
>                 .> celery           exchange=celery(direct) key=celery
>                 
> 
> [tasks]
>   . documents.bulk_edit.delete
>   . documents.signals.handlers.process_cf_select_update
>   . documents.tasks.bulk_update_documents
>   . documents.tasks.check_scheduled_workflows
>   . documents.tasks.consume_file
>   . documents.tasks.empty_trash
>   . documents.tasks.index_optimize
>   . documents.tasks.sanity_check
>   . documents.tasks.train_classifier
>   . documents.tasks.update_document_content_maybe_archive_file
>   . documents.workflows.webhooks.send_webhook
>   . paperless_mail.mail.apply_mail_action
>   . paperless_mail.mail.error_callback
>   . paperless_mail.tasks.process_mail_accounts
> 
> [2026-05-15 07:35:18,235] [INFO] [celery.worker.consumer.connection] Connected to redis://paperless-broker:6379//
> [2026-05-15 07:35:18,247] [INFO] [celery.apps.worker] celery@7c43be1853d3 ready.
> [2026-05-15 07:35:18,250] [INFO] [celery.worker.strategy] Task paperless_mail.tasks.process_mail_accounts[8c73acb3-ffc2-44d3-82ca-3c7c02458142] received
> [2026-05-15 07:35:18,391] [INFO] [celery.app.trace] Task paperless_mail.tasks.process_mail_accounts[8c73acb3-ffc2-44d3-82ca-3c7c02458142] succeeded in 0.039368095982354134s: 'No new documents were added.'
> qiadmin@qiserver:~$ sudo find /srv/qios/stacks -maxdepth 5 -type f \( -name 'docker-compose.yml' -o -name 'compose.yml' \) -print | sort
> /srv/qios/stacks/cloudflared/docker-compose.yml
> /srv/qios/stacks/n8n/docker-compose.yml
> /srv/qios/stacks/nocodb/docker-compose.yml
> /srv/qios/stacks/paperless/docker-compose.yml
> /srv/qios/stacks/portainer/docker-compose.yml
> /srv/qios/stacks/qdrant/docker-compose.yml
> /srv/qios/stacks/_qiaccess_start/docker-compose.yml
> /srv/qios/stacks/qitranscribe/docker-compose.yml
> /srv/qios/stacks/solidtime/docker-compose.yml
> /srv/qios/stacks/uptime-kuma/docker-compose.yml
> /srv/qios/stacks/wikijs/docker-compose.yml
> qiadmin@qiserver:~$

### Assistant
> Nice. We’re back up. Paperless is **healthy**, the web app is serving, and the consume watcher is active.
> 
> ## Current status
> 
> Paperless is running:
> 
> ```text
> paperless Up About a minute (healthy) 127.0.0.1:8010->8000/tcp
> ```
> 
> Paperless UI responds correctly:
> 
> ```text
> HTTP/1.1 302 Found
> location: /accounts/login/?next=/
> ```
> 
> That `302` is good. It means the web app is alive and redirecting unauthenticated users to login.
> 
> The fresh logs show the actual recovery path:
> 
> ```text
> Database is ready
> No migrations to apply.
> Did not create superuser, a user cody already exists
> Starting services
> Listening at: http://:::8000
> Polling directory for changes: /usr/src/paperless/consume
> Paperless-ngx version: v2.20.15
> celery ready
> ```
> 
> So the DB permission issue is fixed. The scary stack trace above it is old log history, not the current state.
> 
> ## Next move: test intake
> 
> Run this:
> 
> ```bash
> echo "QiAccess Paperless OCR pipeline test $(date)" > /tmp/paperless_test.txt
> cp /tmp/paperless_test.txt /srv/qios/data/paperless/consume/
> ls -lah /srv/qios/data/paperless/consume/
> ```
> 
> Then watch logs:
> 
> ```bash
> sudo docker logs -f paperless
> ```
> 
> What we want:
> 
> ```text
> Consuming paperless_test.txt
> Document ... consumption finished
> ```
> 
> or similar.
> 
> If it complains about unsupported file type, no panic. Then we’ll test with a PDF instead. Paperless is mainly built for PDFs/images/emails, so `.txt` may or may not be accepted depending on config. The cleaner test is a small PDF.
> 
> ## Better PDF test
> 
> Run this if `enscript`/`pandoc` isn’t needed — we’ll use Python to generate a tiny PDF if ReportLab exists:
> 
> ```bash
> python3 - <<'PY'
> from pathlib import Path
> 
> out = Path("/tmp/paperless_test.pdf")
> try:
>     from reportlab.pdfgen import canvas
>     c = canvas.Canvas(str(out))
>     c.drawString(72, 720, "QiAccess Paperless OCR pipeline test")
>     c.drawString(72, 700, "This confirms consume folder, Paperless import, and OCR pipeline.")
>     c.save()
>     print(out)
> except Exception as e:
>     print("ReportLab not available:", e)
> PY
> ```
> 
> If it creates the file:
> 
> ```bash
> cp /tmp/paperless_test.pdf /srv/qios/data/paperless/consume/
> sudo docker logs -f paperless
> ```
> 
> ## Then confirm API access
> 
> Since the superuser already exists as `cody`, log into Paperless at:
> 
> ```text
> https://qiserver-1.cerberus-sirius.ts.net
> ```
> 
> But careful: that URL may be your general qiserver UI/front door, not directly Paperless. Locally Paperless is:
> 
> ```text
> http://127.0.0.1:8010
> ```
> 
> If your homepage has a Paperless tile, use that.
> 
> Once logged into Paperless:
> 
> Go to:
> 
> ```text
> Administration / User / Auth Tokens
> ```
> 
> or user settings/API token depending on the UI version.
> 
> We need a token for the sync worker.
> 
> ## After intake works
> 
> Then we create:
> 
> ```text
> /srv/qios/apps/paperless-sync
> ```
> 
> And make the worker pipeline:
> 
> ```text
> Paperless API
> → Postgres/NocoDB tables
> → document chunks
> → Qdrant vectors
> → Neo4j graph relationships
> ```
> 
> But don’t build that until one test PDF successfully lands in Paperless. The active QiAccess blueprint already places Paperless as part of qiserver’s self-hosted service layer and treats vectors/graphs as derived systems, not canonical truth. That means Paperless intake first, then structured pipeline second. fileciteturn0file0

### User
> lets first make sure that paperless setting are all correct and tagging correctly

### Assistant
> Exactly. Settings and taxonomy first. If we let Paperless auto-learn from messy tags, it’ll faithfully learn chaos wearing a little OCR hat. We’ll lock the intake rules before feeding it real documents.

### Assistant
> Yes. We should treat this like **calibrating the document brain** before dumping your whole life into it.
> 
> Paperless is currently alive, so now we audit:
> 
> 1. environment/config
> 2. OCR/import behavior
> 3. users/security
> 4. document types
> 5. correspondents
> 6. tags
> 7. storage paths
> 8. workflows / auto-matching
> 9. API readiness for the next pipeline
> 
> Paperless assigns tags, correspondents, document types, and storage paths automatically through match rules and matching algorithms, so we want clean rules before real ingestion. citeturn637081search0
> 
> ## Step 1 — Dump current Paperless config safely
> 
> Run this first:
> 
> ```bash
> sudo docker inspect paperless --format '{{range .Config.Env}}{{println .}}{{end}}' | sort
> ```
> 
> Also grab the compose file:
> 
> ```bash
> sudo cat /srv/qios/stacks/paperless/docker-compose.yml
> ```
> 
> Send me the output, but redact anything obviously secret like passwords, tokens, secret keys, SMTP passwords, etc.
> 
> ## Step 2 — Check current Paperless objects
> 
> Run these from the server:
> 
> ```bash
> sudo docker exec -it paperless bash -lc 'python manage.py shell -c "
> from documents.models import Tag, Correspondent, DocumentType, StoragePath, Document
> print(\"Documents:\", Document.objects.count())
> print(\"Tags:\", Tag.objects.count())
> print(\"Correspondents:\", Correspondent.objects.count())
> print(\"DocumentTypes:\", DocumentType.objects.count())
> print(\"StoragePaths:\", StoragePath.objects.count())
> print(\"\\nTAGS:\")
> [print(f\"- {x.name} | match={x.match} | algo={x.matching_algorithm}\") for x in Tag.objects.all().order_by(\"name\")]
> print(\"\\nCORRESPONDENTS:\")
> [print(f\"- {x.name} | match={x.match} | algo={x.matching_algorithm}\") for x in Correspondent.objects.all().order_by(\"name\")]
> print(\"\\nDOCUMENT TYPES:\")
> [print(f\"- {x.name} | match={x.match} | algo={x.matching_algorithm}\") for x in DocumentType.objects.all().order_by(\"name\")]
> print(\"\\nSTORAGE PATHS:\")
> [print(f\"- {x.name} | path={x.path} | match={x.match} | algo={x.matching_algorithm}\") for x in StoragePath.objects.all().order_by(\"name\")]
> "'
> ```
> 
> That tells us if Paperless already has messy labels or if we’re starting clean.
> 
> ## The taxonomy I recommend
> 
> Do **not** make tags do everything. That’s how Paperless turns into a junk drawer with a search bar.
> 
> Use this split:
> 
> ```text
> Document Type = what the file is
> Correspondent = who it came from / who it concerns institutionally
> Tags = why it matters / what domain it belongs to
> Storage Path = where Paperless stores it internally
> Custom Fields = structured metadata we need later
> ```
> 
> ## Starter Document Types
> 
> Use these first:
> 
> ```text
> Bill
> Receipt
> Statement
> Tax Document
> Legal Filing
> Court Notice
> Contract / Agreement
> Medical Record
> Care Document
> Insurance Document
> Identity / Vital Record
> Letter / Notice
> Report
> Technical Document
> Reference Material
> Unknown / Needs Review
> ```
> 
> Keep this list tight. Too many document types creates fake precision.
> 
> ## Starter Tags
> 
> Use domain tags first:
> 
> ```text
> domain:care
> domain:legal
> domain:finance
> domain:tax
> domain:medical
> domain:tech
> domain:household
> domain:identity
> domain:business
> domain:reference
> ```
> 
> Then workflow/status tags:
> 
> ```text
> status:review-needed
> status:processed
> status:exported
> status:synced
> status:duplicate-check
> status:urgent
> ```
> 
> Then special-purpose tags:
> 
> ```text
> source:scan
> source:email
> source:download
> source:drive
> pipeline:qdrant
> pipeline:neo4j
> pipeline:nocodb
> ```
> 
> I’d avoid cute tags like `important`, `random`, `misc`, `mom`, `bank stuff`, etc. Those are vibes, not metadata. Vibes are where retrieval goes to die.
> 
> ## Starter Correspondents
> 
> Only create ones you know you’ll reuse:
> 
> ```text
> Unknown / Needs Review
> Court / Clerk
> FCFCU
> Chase
> IRS
> SSA
> Medicaid / Medicare
> Insurance Provider
> Utility Provider
> Medical Provider
> Paperless Test
> QiAccess / QiServer
> ```
> 
> Later we add exact names like banks, hospitals, courts, attorneys, agencies, vendors.
> 
> ## Storage Paths
> 
> For v1, do **not** over-folder this.
> 
> Use broad paths:
> 
> ```text
> {{ created_year }}/{{ document_type }}/{{ correspondent }}/{{ title }}
> ```
> 
> Or safer:
> 
> ```text
> {{ created_year }}/{{ document_type }}/{{ title }}
> ```
> 
> I lean safer. Correspondents can get messy and rename-heavy.
> 
> Recommended starter paths:
> 
> ```text
> Default
> Legal
> Finance
> Care
> Medical
> Tech
> Reference
> Needs Review
> ```
> 
> But again: storage path is internal Paperless storage. It is **not** QiNexus. QiNexus stays your broader source/backbone model.
> 
> ## Matching rules doctrine
> 
> Use matching carefully:
> 
> ### Good matching
> 
> For correspondents:
> 
> ```text
> IRS → "Internal Revenue Service" OR "Department of the Treasury"
> Chase → "JPMorgan Chase" OR "Chase"
> Court / Clerk → "Clerk" OR "Superior Court" OR "Circuit Court"
> ```
> 
> For document types:
> 
> ```text
> Statement → "statement period" OR "account summary"
> Receipt → "receipt" OR "total paid"
> Bill → "amount due" OR "due date"
> Court Notice → "notice of hearing" OR "summons"
> Tax Document → "Form 1099" OR "W-2" OR "Internal Revenue Service"
> ```
> 
> For tags:
> 
> ```text
> domain:finance → bank names, statement, payment, account
> domain:legal → court, case number, plaintiff, defendant, filing
> domain:care → care plan, caregiver, appointment, provider
> ```
> 
> ### Bad matching
> 
> Do not match broad words like:
> 
> ```text
> account
> date
> total
> notice
> payment
> document
> important
> medical
> legal
> ```
> 
> Those will over-tag everything. Paperless matching is powerful, but it will absolutely do exactly the dumb thing we accidentally told it to do. citeturn637081search0
> 
> ## What I need from you next
> 
> Send me the output from:
> 
> ```bash
> sudo docker inspect paperless --format '{{range .Config.Env}}{{println .}}{{end}}' | sort
> ```
> 
> and the object dump command.
> 
> Then I’ll give you the exact cleanup/create commands for Paperless so we can seed the taxonomy cleanly.

### User
> Welcome, qiadmin. View site / Change password / Log out Toggle theme (current theme: auto)
> Paperless-ngx administration
> Accounts
> Model name	Add link	Change or view list link
> Email addresses	
> Add
> Change
> Audit log
> Model name	Add link	Change or view list link
> Log entries		
> View
> Auth Token
> Model name	Add link	Change or view list link
> Tokens	
> Add
> Change
> Authentication and Authorization
> Model name	Add link	Change or view list link
> Groups	
> Add
> Change
> Users	
> Add
> Change
> Celery Results
> Model name	Add link	Change or view list link
> Group results	
> Add
> Change
> Task results	
> Add
> Change
> Documents
> Model name	Add link	Change or view list link
> Correspondents	
> Add
> Change
> Custom field instances	
> Add
> Change
> Custom fields	
> Add
> Change
> Document types	
> Add
> Change
> Documents		
> Change
> Notes	
> Add
> Change
> Paperless tasks	
> Add
> Change
> Saved views	
> Add
> Change
> Share links	
> Add
> Change
> Storage paths	
> Add
> Change
> Tags	
> Add
> Change
> MFA
> Model name	Add link	Change or view list link
> Authenticators	
> Add
> Change
> Paperless mail
> Model name	Add link	Change or view list link
> Mail accounts	
> Add
> Change
> Mail rules	
> Add
> Change
> Processed mails	
> Add
> Change
> Social Accounts
> Model name	Add link	Change or view list link
> Social accounts	
> Add
> Change
> Social application tokens	
> Add
> Change
> Social applications	
> Add
> Change
> Recent actions
> My actions
> None available

### Assistant
> Perfect — you’re in the **Django admin**, which is the power-user backend. Good for setup, but not the friendly Paperless UI. We can use it to seed the whole taxonomy fast.
> 
> You have the important admin sections available:
> 
> - **Correspondents**
> - **Document types**
> - **Storage paths**
> - **Tags**
> - **Custom fields**
> - **Auth Tokens**
> - **Saved views**
> - **Mail rules**
> 
> That’s exactly what we need.
> 
> ## First: do not add random tags manually yet
> 
> We’re going to set the taxonomy in a clean order:
> 
> 1. **Document Types** — what the document *is*
> 2. **Correspondents** — who it came from
> 3. **Tags** — why/domain/status/pipeline
> 4. **Storage Paths** — broad routing only
> 5. **Custom Fields** — structured metadata for later tables/vector/graph
> 6. **Auth Token** — for Paperless sync worker
> 
> ## Go here first: Document Types
> 
> In admin:
> 
> **Documents → Document types → Add**
> 
> Create these:
> 
> ```text
> Bill
> Receipt
> Statement
> Tax Document
> Legal Filing
> Court Notice
> Contract / Agreement
> Medical Record
> Care Document
> Insurance Document
> Identity / Vital Record
> Letter / Notice
> Report
> Technical Document
> Reference Material
> Unknown / Needs Review
> ```
> 
> For now, leave matching fields mostly blank unless there is an obvious match.
> 
> Exception examples:
> 
> ### Statement
> 
> Match:
> 
> ```text
> statement period
> account summary
> monthly statement
> ```
> 
> ### Receipt
> 
> Match:
> 
> ```text
> receipt
> total paid
> payment received
> ```
> 
> ### Court Notice
> 
> Match:
> 
> ```text
> notice of hearing
> summons
> court order
> ```
> 
> ### Tax Document
> 
> Match:
> 
> ```text
> Form 1099
> W-2
> Internal Revenue Service
> Department of the Treasury
> ```
> 
> Do **not** use broad single words like `notice`, `account`, `payment`, or `document`. Those will over-tag everything like a drunk intern.
> 
> ## Then: Correspondents
> 
> Go to:
> 
> **Documents → Correspondents → Add**
> 
> Create these:
> 
> ```text
> Unknown / Needs Review
> Court / Clerk
> FCFCU
> Chase
> IRS
> SSA
> Medicaid / Medicare
> Insurance Provider
> Utility Provider
> Medical Provider
> Paperless Test
> QiAccess / QiServer
> ```
> 
> Suggested match terms:
> 
> ### IRS
> 
> ```text
> Internal Revenue Service
> Department of the Treasury
> IRS
> ```
> 
> ### Chase
> 
> ```text
> JPMorgan Chase
> Chase
> ```
> 
> ### Court / Clerk
> 
> ```text
> Clerk
> Circuit Court
> Superior Court
> Court
> ```
> 
> Careful with `Court` because it may catch too much, but it is acceptable for early legal sorting if most court docs are truly court docs.
> 
> ### FCFCU
> 
> ```text
> Financial Center First Credit Union
> FCFCU
> ```
> 
> ## Then: Tags
> 
> Go to:
> 
> **Documents → Tags → Add**
> 
> Create domain tags:
> 
> ```text
> domain:care
> domain:legal
> domain:finance
> domain:tax
> domain:medical
> domain:tech
> domain:household
> domain:identity
> domain:business
> domain:reference
> ```
> 
> Create status tags:
> 
> ```text
> status:review-needed
> status:processed
> status:exported
> status:synced
> status:duplicate-check
> status:urgent
> ```
> 
> Create source tags:
> 
> ```text
> source:scan
> source:email
> source:download
> source:drive
> ```
> 
> Create pipeline tags:
> 
> ```text
> pipeline:nocodb
> pipeline:qdrant
> pipeline:neo4j
> ```
> 
> For now, the most important default tag is:
> 
> ```text
> status:review-needed
> ```
> 
> That gives us a triage queue.
> 
> ## Storage Paths
> 
> Go to:
> 
> **Documents → Storage paths → Add**
> 
> Create these:
> 
> ```text
> Default
> Legal
> Finance
> Care
> Medical
> Tech
> Reference
> Needs Review
> ```
> 
> Use simple paths for now:
> 
> ### Default
> 
> ```text
> {{ created_year }}/{{ document_type }}/{{ title }}
> ```
> 
> ### Legal
> 
> ```text
> legal/{{ created_year }}/{{ document_type }}/{{ title }}
> ```
> 
> ### Finance
> 
> ```text
> finance/{{ created_year }}/{{ document_type }}/{{ title }}
> ```
> 
> ### Care
> 
> ```text
> care/{{ created_year }}/{{ document_type }}/{{ title }}
> ```
> 
> ### Needs Review
> 
> ```text
> needs_review/{{ created_year }}/{{ title }}
> ```
> 
> Do not include correspondent in the path yet. Correspondents rename, merge, and get messy. Metadata can handle that better than folders.
> 
> ## Custom Fields
> 
> Go to:
> 
> **Documents → Custom fields → Add**
> 
> Create these fields:
> 
> ```text
> Qi Domain
> Qi Source System
> Qi Sync Status
> Qi External ID
> Qi Matter ID
> Qi Account ID
> Qi Event Date
> Qi Review Status
> Qi Notes
> ```
> 
> Recommended field types if the UI asks:
> 
> | Field | Type |
> |---|---|
> | Qi Domain | Text or Select |
> | Qi Source System | Text |
> | Qi Sync Status | Text or Select |
> | Qi External ID | Text |
> | Qi Matter ID | Text |
> | Qi Account ID | Text |
> | Qi Event Date | Date |
> | Qi Review Status | Text or Select |
> | Qi Notes | Text |
> 
> These are for the future pipeline so we can map Paperless docs into tables, Qdrant, and Neo4j without relying only on tags.
> 
> ## Auth Token
> 
> Later, go to:
> 
> **Auth Token → Tokens → Add**
> 
> Create token for user:
> 
> ```text
> cody
> ```
> 
> That token becomes the key for:
> 
> ```text
> paperless-sync worker → Paperless API
> ```
> 
> Don’t paste the token here unless you redact it. We only need to know it exists.
> 
> ## The clean operating model
> 
> Use this mental split:
> 
> ```text
> Document Type = what it is
> Correspondent = who sent it / institution
> Tag = domain, status, source, pipeline
> Storage Path = broad internal storage bucket
> Custom Field = structured metadata for sync/reporting
> ```
> 
> That’s the whole doctrine. Clean, durable, scalable.
> 
> ## Best next action
> 
> Start with **Document Types**, then **Tags**, then **Correspondents**. After those are created, we’ll ingest one test PDF and see if Paperless classifies it correctly before adding real docs.

### User
> i know there is a way to import these settings so we can do this quickly.

### Assistant
> Yep — you’re thinking correctly. Manually clicking all of that in Django admin is clown work. Paperless has management/import paths, and we can seed objects directly inside the container with a script.

### Assistant
> Yes — absolutely. There are two “fast” ways, and one is cleaner for **our** situation.
> 
> ## The real options
> 
> ### Option 1 — Paperless exporter/importer
> 
> Paperless has a **document exporter** that exports documents, thumbnails, metadata, and database contents, then can import them into a fresh instance. That’s great for backup/migration, but it’s overkill for just seeding taxonomy/settings. citeturn888582search1
> 
> Use this later for backups.
> 
> ### Option 2 — Seed through Django/Paperless models
> 
> This is the right move now.
> 
> Because you already have a running Paperless container, we can run a Python seed script inside it and create:
> 
> - tags
> - document types
> - correspondents
> - storage paths
> - custom fields
> 
> Fast, repeatable, no clicky-clicky nonsense.
> 
> Paperless supports managing tags, correspondents, document types, saved views, mail rules, workflows, and related objects through its management interfaces, and its REST API is documented too. citeturn888582search0turn888582search16
> 
> ## Recommended method: seed script inside container
> 
> Create the script on the server:
> 
> ```bash
> cat > /tmp/seed_paperless_qios.py <<'PY'
> from documents.models import Tag, Correspondent, DocumentType, StoragePath, CustomField
> 
> def get_model_field_names(model):
>     return {f.name for f in model._meta.fields}
> 
> def upsert_basic(model, name, **extra):
>     fields = get_model_field_names(model)
>     safe_extra = {k: v for k, v in extra.items() if k in fields}
>     obj, created = model.objects.get_or_create(name=name, defaults=safe_extra)
>     changed = False
>     for key, value in safe_extra.items():
>         if getattr(obj, key, None) != value:
>             setattr(obj, key, value)
>             changed = True
>     if changed:
>         obj.save()
>     print(("CREATED" if created else "UPDATED"), model.__name__, name)
> 
> document_types = [
>     "Bill",
>     "Receipt",
>     "Statement",
>     "Tax Document",
>     "Legal Filing",
>     "Court Notice",
>     "Contract / Agreement",
>     "Medical Record",
>     "Care Document",
>     "Insurance Document",
>     "Identity / Vital Record",
>     "Letter / Notice",
>     "Report",
>     "Technical Document",
>     "Reference Material",
>     "Unknown / Needs Review",
> ]
> 
> correspondents = [
>     "Unknown / Needs Review",
>     "Court / Clerk",
>     "FCFCU",
>     "Chase",
>     "IRS",
>     "SSA",
>     "Medicaid / Medicare",
>     "Insurance Provider",
>     "Utility Provider",
>     "Medical Provider",
>     "Paperless Test",
>     "QiAccess / QiServer",
> ]
> 
> tags = [
>     "domain:care",
>     "domain:legal",
>     "domain:finance",
>     "domain:tax",
>     "domain:medical",
>     "domain:tech",
>     "domain:household",
>     "domain:identity",
>     "domain:business",
>     "domain:reference",
>     "status:review-needed",
>     "status:processed",
>     "status:exported",
>     "status:synced",
>     "status:duplicate-check",
>     "status:urgent",
>     "source:scan",
>     "source:email",
>     "source:download",
>     "source:drive",
>     "pipeline:nocodb",
>     "pipeline:qdrant",
>     "pipeline:neo4j",
> ]
> 
> storage_paths = {
>     "Default": "{{ created_year }}/{{ document_type }}/{{ title }}",
>     "Legal": "legal/{{ created_year }}/{{ document_type }}/{{ title }}",
>     "Finance": "finance/{{ created_year }}/{{ document_type }}/{{ title }}",
>     "Care": "care/{{ created_year }}/{{ document_type }}/{{ title }}",
>     "Medical": "medical/{{ created_year }}/{{ document_type }}/{{ title }}",
>     "Tech": "tech/{{ created_year }}/{{ document_type }}/{{ title }}",
>     "Reference": "reference/{{ created_year }}/{{ document_type }}/{{ title }}",
>     "Needs Review": "needs_review/{{ created_year }}/{{ title }}",
> }
> 
> custom_fields = [
>     "Qi Domain",
>     "Qi Source System",
>     "Qi Sync Status",
>     "Qi External ID",
>     "Qi Matter ID",
>     "Qi Account ID",
>     "Qi Event Date",
>     "Qi Review Status",
>     "Qi Notes",
> ]
> 
> for name in document_types:
>     upsert_basic(DocumentType, name)
> 
> for name in correspondents:
>     upsert_basic(Correspondent, name)
> 
> for name in tags:
>     upsert_basic(Tag, name)
> 
> for name, path in storage_paths.items():
>     upsert_basic(StoragePath, name, path=path)
> 
> # CustomField internals vary a little by Paperless version, so use safe fields only.
> for name in custom_fields:
>     upsert_basic(CustomField, name)
> 
> print("DONE: QiOS/Paperless taxonomy seed complete.")
> PY
> ```
> 
> Now copy it into the container and run it through Django:
> 
> ```bash
> sudo docker cp /tmp/seed_paperless_qios.py paperless:/tmp/seed_paperless_qios.py
> 
> sudo docker exec -it paperless bash -lc 'python manage.py shell < /tmp/seed_paperless_qios.py'
> ```
> 
> ## Verify it worked
> 
> Run:
> 
> ```bash
> sudo docker exec -it paperless bash -lc 'python manage.py shell -c "
> from documents.models import Tag, Correspondent, DocumentType, StoragePath, CustomField
> print(\"Tags:\", Tag.objects.count())
> print(\"Correspondents:\", Correspondent.objects.count())
> print(\"Document types:\", DocumentType.objects.count())
> print(\"Storage paths:\", StoragePath.objects.count())
> print(\"Custom fields:\", CustomField.objects.count())
> "'
> ```
> 
> ## One warning
> 
> This seeds the objects, but it does **not** yet create smart matching rules.
> 
> That is intentional.
> 
> Paperless automatic matching can assign tags, correspondents, document types, and storage paths based on matching rules or the Auto algorithm, but we don’t want Auto learning before the taxonomy is clean. citeturn888582search2turn888582search7
> 
> So the order is:
> 
> 1. Seed taxonomy.
> 2. Upload 3–5 test docs.
> 3. Manually assign correct metadata.
> 4. Add narrow match rules.
> 5. Train classifier later.
> 6. Then bulk ingest.
> 
> Do not let Paperless “learn” from chaos. That’s how we summon the filing cabinet demon.

### User
> it worked i can see everything in paperless, now are you sure this is all we need, i know you said no soup but you know i have a lot of shit to ingest and organize. and this thing needs to rename things, keep it organized and readable, add the metadata, etc, and the rules last time were shit how can we make rules that actually help me versus giving me another job.

### Assistant
> Yes — you’re right to push back. The seed list is only the skeleton. For your volume, the real win is **rule design + staged ingestion + review queues**, otherwise Paperless becomes “another app that wants chores.”

### User
> also shouldnt the storage paths match our updated folder hiearchy for consistency and recognition.

### Assistant
> Yes. You’re right on both points.
> 
> The first seed was **not “all we need.”** It was the safe skeleton so Paperless had clean nouns. For your actual volume, we need **storage paths, filenames, match rules, review queues, and sync metadata** designed around QiNexus — otherwise Paperless becomes another chore machine with prettier buttons.
> 
> And yes: **storage paths should align with the updated QiNexus hierarchy for recognition**, but with one important caveat:
> 
> **Paperless storage paths should mirror QiNexus buckets conceptually, not become your whole Google Drive folder tree.**
> 
> Your blueprint defines QiNexus root order as `00_inbox`, `01_workbench`, `02_timeline`, `03_life`, `04_people`, `05_business`, `06_finance`, `07_legal`, `08_tech`, `09_assets`, `10_data`, `11_reference`, `12_archive`, and `13_system`. fileciteturn2file0
> 
> That should absolutely be reflected.
> 
> ## The corrected doctrine
> 
> Paperless should use:
> 
> ```text
> 00_inbox        = new/needs review
> 03_life         = household/life ops docs
> 04_people       = people/care/support docs
> 05_business     = business docs
> 06_finance      = statements, bills, receipts, tax docs
> 07_legal        = filings, notices, evidence, case docs
> 08_tech         = server/app/tool docs
> 10_data         = exports, structured source files, logs
> 11_reference    = guides, articles, manuals, reference docs
> 12_archive      = completed/inactive/historical docs
> 13_system       = Paperless/QiAccess/system records
> ```
> 
> I would **not** use `01_workbench`, `02_timeline`, or `09_assets` heavily inside Paperless at first.
> 
> Why?
> 
> Because Paperless is for **documents/records**, not every active draft, journal, timeline note, image, or media asset. The blueprint says active work belongs in `01_workbench`, journals/logs belong in `02_timeline`, assets belong in `09_assets`, and structured exports belong in `10_data`. fileciteturn2file0
> 
> So Paperless should not eat the entire universe. It should eat **record-like documents**.
> 
> ## Better Paperless storage paths
> 
> Replace the earlier broad paths with QiNexus-aligned paths:
> 
> ```text
> 00_inbox/needs_review/{{ created_year }}/{{ title }}
> 03_life/{{ created_year }}/{{ document_type }}/{{ title }}
> 04_people/{{ created_year }}/{{ document_type }}/{{ title }}
> 05_business/{{ created_year }}/{{ document_type }}/{{ title }}
> 06_finance/{{ created_year }}/{{ document_type }}/{{ title }}
> 07_legal/{{ created_year }}/{{ document_type }}/{{ title }}
> 08_tech/{{ created_year }}/{{ document_type }}/{{ title }}
> 10_data/{{ created_year }}/{{ document_type }}/{{ title }}
> 11_reference/{{ created_year }}/{{ document_type }}/{{ title }}
> 12_archive/{{ created_year }}/{{ document_type }}/{{ title }}
> 13_system/{{ created_year }}/{{ document_type }}/{{ title }}
> ```
> 
> This gives you recognition without folder insanity.
> 
> Do **not** put correspondent in the path yet. That sounds helpful until you have `Chase`, `JPMorgan Chase`, `JP Morgan`, and `Chase Bank` making duplicate folder branches. Metadata handles correspondent better.
> 
> ## Naming: Paperless should rename files too
> 
> Yes. We need filename formatting.
> 
> Recommended archive filename format:
> 
> ```text
> {{ created_year }}-{{ created_month }}-{{ created_day }}_{{ correspondent }}_{{ document_type }}_{{ title }}
> ```
> 
> Qi-flavored version:
> 
> ```text
> {{ created_year }}{{ created_month }}{{ created_day }}_{{ document_type }}_{{ correspondent }}_{{ title }}
> ```
> 
> For your system, I prefer this:
> 
> ```text
> {{ created_year }}{{ created_month }}{{ created_day }}_{{ document_type }}_{{ correspondent }}_{{ title }}
> ```
> 
> Reason: date-first, readable, sortable, and consistent with your “date in there somewhere” doctrine.
> 
> The title still matters, but the metadata becomes the real structure.
> 
> ## The actual automation strategy
> 
> Paperless rules should not try to be psychic. They should do **boring, high-confidence routing**.
> 
> ### Rule layer 1 — default safety
> 
> Every new document starts as:
> 
> ```text
> status:review-needed
> 00_inbox/needs_review
> ```
> 
> That way nothing silently disappears into the wrong bucket.
> 
> ### Rule layer 2 — obvious domain detection
> 
> Only use high-confidence terms.
> 
> Examples:
> 
> ```text
> 06_finance
> ```
> 
> Match terms:
> 
> ```text
> statement period
> account summary
> amount due
> minimum payment
> routing number
> account number
> payment due
> transaction summary
> ```
> 
> Tags applied:
> 
> ```text
> domain:finance
> status:review-needed
> ```
> 
> Document types:
> 
> ```text
> Statement
> Bill
> Receipt
> Tax Document
> ```
> 
> ---
> 
> ```text
> 07_legal
> ```
> 
> Match terms:
> 
> ```text
> cause number
> case number
> plaintiff
> defendant
> summons
> notice of hearing
> motion
> order of court
> clerk of court
> writ
> foreclosure
> ```
> 
> Tags:
> 
> ```text
> domain:legal
> status:review-needed
> ```
> 
> ---
> 
> ```text
> 04_people / 03_life / care-related
> ```
> 
> Match terms:
> 
> ```text
> care plan
> caregiver
> appointment summary
> provider
> patient instructions
> visit summary
> ```
> 
> Tags:
> 
> ```text
> domain:care
> status:review-needed
> ```
> 
> ---
> 
> ```text
> 08_tech
> ```
> 
> Match terms:
> 
> ```text
> server
> docker
> ssh
> api key
> backup
> cloudflare
> tailscale
> postgres
> qdrant
> neo4j
> ```
> 
> Tags:
> 
> ```text
> domain:tech
> status:review-needed
> ```
> 
> ### Rule layer 3 — correspondent detection
> 
> Use exact institution phrases.
> 
> Good:
> 
> ```text
> Internal Revenue Service
> Department of the Treasury
> JPMorgan Chase
> Financial Center First Credit Union
> Superior Court
> Circuit Court
> ```
> 
> Bad:
> 
> ```text
> bank
> court
> payment
> office
> account
> notice
> ```
> 
> Broad words create trash metadata. No thank you.
> 
> ### Rule layer 4 — review queue
> 
> The goal is not “perfect auto-sort.”
> 
> The goal is:
> 
> ```text
> 90% sorted close enough
> 10% lands in review
> 0% silently lost
> ```
> 
> That’s the grown-up system.
> 
> ## Should we use Auto matching?
> 
> Later. Not first.
> 
> Paperless can auto-assign tags, correspondents, document types, and storage paths based on matching algorithms, but the docs are clear that matching takes experimentation. citeturn216415search0
> 
> Also, if multiple document types or correspondents match, Paperless may not assign them unless override behavior is used. citeturn216415search14
> 
> So the right order is:
> 
> 1. create taxonomy
> 2. create storage paths
> 3. create conservative rules
> 4. ingest 25 mixed docs
> 5. manually correct them
> 6. train/adjust
> 7. then batch ingest
> 
> Not “dump 10,000 docs and pray.” That’s not automation. That’s digital confetti.
> 
> ## What we should do now
> 
> We should update Paperless from the first seed to a **QiNexus-aligned seed**.
> 
> This should:
> 
> 1. add QiNexus storage paths
> 2. add `bucket:*` tags
> 3. add better domain/status/source/pipeline tags
> 4. add starter match rules
> 5. set default review behavior
> 6. prepare metadata for sync to tables/vector/graph
> 
> ## Add these new tags
> 
> ```text
> bucket:00_inbox
> bucket:03_life
> bucket:04_people
> bucket:05_business
> bucket:06_finance
> bucket:07_legal
> bucket:08_tech
> bucket:10_data
> bucket:11_reference
> bucket:12_archive
> bucket:13_system
> ```
> 
> Keep existing domain tags too. Bucket tells us **where it belongs**. Domain tells us **what world it belongs to**.
> 
> Example:
> 
> A bank statement:
> 
> ```text
> bucket:06_finance
> domain:finance
> document_type:Statement
> correspondent:Chase
> status:review-needed
> ```
> 
> A court filing:
> 
> ```text
> bucket:07_legal
> domain:legal
> document_type:Legal Filing
> status:review-needed
> ```
> 
> A server PDF:
> 
> ```text
> bucket:08_tech
> domain:tech
> document_type:Technical Document
> status:review-needed
> ```
> 
> ## The rule that saves you work
> 
> Every rule should answer:
> 
> ```text
> Can this safely reduce Cody’s future decisions?
> ```
> 
> If not, don’t make the rule.
> 
> Bad rule:
> 
> ```text
> If document contains "account", tag finance.
> ```
> 
> That will tag medical portal accounts, court accounts, web accounts, everything. Trash.
> 
> Good rule:
> 
> ```text
> If document contains "statement period" OR "account summary" OR "minimum payment due", assign Statement + domain:finance + bucket:06_finance.
> ```
> 
> That actually helps.
> 
> ## Best next action
> 
> Run a second seed script that upgrades storage paths and bucket tags. Then we create match rules in a controlled way.
> 
> Say the word and I’ll give you the exact paste-ready script to update Paperless without deleting what you already created.

### User
> make sure you are mapping to the correct folders.

### Assistant
> Yes — and correction: the mapping should follow the **updated four-domain system**, not the older flat QiNexus-only root.
> 
> Your current map is:
> 
> ```text
> 10_core       = doctrine / rules / standards / registries
> 20_qinexus    = human source terrain / organized life files
> 30_qiarchive  = AI memory pipeline / ingestion / extraction / vectors / graphs
> 40_system     = operational logs / audits / backups / generated reports
> ```
> 
> So Paperless storage paths should mostly land under **`20_qinexus`**, while the later sync worker writes manifests and processed outputs into **`30_qiarchive`**. Paperless itself is documented as a capture service under `10_core/40_service_apps/30_capture/30_paperless.md`, and QiArchive specifically has `30_qiarchive/10_ingestion/10_paperless` for Paperless manifests and source references. fileciteturn4file0
> 
> ## Correct Paperless storage path doctrine
> 
> Paperless archive files should go here:
> 
> ```text
> 20_qinexus/...
> ```
> 
> Paperless sync/AI pipeline outputs should go here later:
> 
> ```text
> 30_qiarchive/10_ingestion/10_paperless
> 30_qiarchive/20_extraction/10_ocr_text
> 30_qiarchive/20_extraction/40_metadata
> 30_qiarchive/30_chunking/10_chunk_manifests
> 30_qiarchive/40_embeddings/10_qdrant
> 30_qiarchive/50_graphs/30_entity_maps
> 30_qiarchive/80_sync_backups/40_sync_manifests
> ```
> 
> Do **not** store normal scanned PDFs directly in `30_qiarchive`. That folder is for processed memory artifacts, not the original human-facing filing cabinet.
> 
> ## Correct Paperless folder mapping
> 
> | Paperless category | Correct folder |
> |---|---|
> | New / uncertain documents | `20_qinexus/00_inbox/30_pending_review` |
> | Downloads/mobile uploads needing review | `20_qinexus/00_inbox/40_mobile_uploads` or `20_unsorted_files` |
> | Home, utilities, routines, household docs | `20_qinexus/30_life/10_home` |
> | Wellness / personal ops docs | `20_qinexus/30_life/30_wellness` |
> | Family/care coordination docs | `20_qinexus/40_people/30_care_coordination` |
> | Communication plans / relationship context | `20_qinexus/40_people/40_communication_plans` or `50_relationship_context` |
> | Business docs | `20_qinexus/50_business/60_business_operations` |
> | Brand/client/offer docs | `20_qinexus/50_business/10_brand`, `30_clients`, `40_offers_products` |
> | Bills | `20_qinexus/60_finance/20_bills` |
> | Account docs | `20_qinexus/60_finance/30_accounts` |
> | Statements | `20_qinexus/60_finance/40_statements` |
> | Reports/reconciliations | `20_qinexus/60_finance/50_reconciliations` or `60_reports` |
> | General ledger source docs | `20_qinexus/60_finance/70_general_ledger` |
> | Tax docs | `20_qinexus/60_finance/80_tax` |
> | Legal matters | `20_qinexus/70_legal/10_matters` |
> | Filings | `20_qinexus/70_legal/20_filings` |
> | Evidence | `20_qinexus/70_legal/30_evidence` |
> | Legal timelines | `20_qinexus/70_legal/40_timelines` |
> | Motions/drafts | `20_qinexus/70_legal/50_motions_drafts` |
> | Legal research/reference | `20_qinexus/70_legal/60_research` or `110_reference/30_legal_references` |
> | Exhibits | `20_qinexus/70_legal/80_exhibits` |
> | Server/app/tool docs | `20_qinexus/80_tech/10_qiserver`, `20_apps`, `60_tooling` |
> | Repo/dev docs | `20_qinexus/80_tech/30_repos`, `70_dev_runbooks` |
> | Structured exports, CSV, JSON | `20_qinexus/100_data/10_csv`, `20_json`, `30_database_exports` |
> | Logs as source data | `20_qinexus/100_data/40_logs` |
> | External guides/articles/laws/examples | `20_qinexus/110_reference/...` |
> | Old inactive docs | `20_qinexus/120_archive/...` |
> | QiNexus rules/manifests | `20_qinexus/130_system/...` |
> 
> ## The Paperless storage paths I’d create
> 
> Use these exact names and path templates:
> 
> ```text
> 00 Inbox - Pending Review
> 20_qinexus/00_inbox/30_pending_review/{{ created_year }}/{{ title }}
> 
> 30 Life - Home
> 20_qinexus/30_life/10_home/{{ created_year }}/{{ document_type }}/{{ title }}
> 
> 30 Life - Wellness
> 20_qinexus/30_life/30_wellness/{{ created_year }}/{{ document_type }}/{{ title }}
> 
> 40 People - Care Coordination
> 20_qinexus/40_people/30_care_coordination/{{ created_year }}/{{ document_type }}/{{ title }}
> 
> 50 Business - Operations
> 20_qinexus/50_business/60_business_operations/{{ created_year }}/{{ document_type }}/{{ title }}
> 
> 60 Finance - Bills
> 20_qinexus/60_finance/20_bills/{{ created_year }}/{{ correspondent }}/{{ title }}
> 
> 60 Finance - Accounts
> 20_qinexus/60_finance/30_accounts/{{ created_year }}/{{ correspondent }}/{{ title }}
> 
> 60 Finance - Statements
> 20_qinexus/60_finance/40_statements/{{ created_year }}/{{ correspondent }}/{{ title }}
> 
> 60 Finance - Reports
> 20_qinexus/60_finance/60_reports/{{ created_year }}/{{ document_type }}/{{ title }}
> 
> 60 Finance - General Ledger
> 20_qinexus/60_finance/70_general_ledger/{{ created_year }}/{{ document_type }}/{{ title }}
> 
> 60 Finance - Tax
> 20_qinexus/60_finance/80_tax/{{ created_year }}/{{ document_type }}/{{ title }}
> 
> 70 Legal - Matters
> 20_qinexus/70_legal/10_matters/{{ created_year }}/{{ title }}
> 
> 70 Legal - Filings
> 20_qinexus/70_legal/20_filings/{{ created_year }}/{{ document_type }}/{{ title }}
> 
> 70 Legal - Evidence
> 20_qinexus/70_legal/30_evidence/{{ created_year }}/{{ document_type }}/{{ title }}
> 
> 70 Legal - Timelines
> 20_qinexus/70_legal/40_timelines/{{ created_year }}/{{ title }}
> 
> 70 Legal - Exhibits
> 20_qinexus/70_legal/80_exhibits/{{ created_year }}/{{ title }}
> 
> 80 Tech - Qiserver
> 20_qinexus/80_tech/10_qiserver/{{ created_year }}/{{ document_type }}/{{ title }}
> 
> 80 Tech - Apps
> 20_qinexus/80_tech/20_apps/{{ created_year }}/{{ document_type }}/{{ title }}
> 
> 80 Tech - Dev Runbooks
> 20_qinexus/80_tech/70_dev_runbooks/{{ created_year }}/{{ title }}
> 
> 100 Data - Database Exports
> 20_qinexus/100_data/30_database_exports/{{ created_year }}/{{ title }}
> 
> 100 Data - Logs
> 20_qinexus/100_data/40_logs/{{ created_year }}/{{ title }}
> 
> 110 Reference - Legal References
> 20_qinexus/110_reference/30_legal_references/{{ created_year }}/{{ title }}
> 
> 110 Reference - Technical Guides
> 20_qinexus/110_reference/40_technical_guides/{{ created_year }}/{{ title }}
> 
> 120 Archive - Historical Files
> 20_qinexus/120_archive/30_historical_files/{{ created_year }}/{{ title }}
> 
> 130 System - QiNexus Manifests
> 20_qinexus/130_system/20_folder_manifest/{{ created_year }}/{{ title }}
> ```
> 
> ## One key correction
> 
> I would **not** create Paperless paths for these unless there is a clear document type need:
> 
> ```text
> 10_core
> 30_qiarchive
> 40_system
> 20_qinexus/10_workbench
> 20_qinexus/20_timeline
> 20_qinexus/90_assets
> ```
> 
> Why?
> 
> Because:
> 
> - `10_core` is doctrine/standards/registries, not random ingested docs.
> - `30_qiarchive` is processed AI memory output, not original source storage.
> - `40_system` is operational logs/audits/backups/generated reports.
> - `10_workbench` is active drafts/projects; Paperless is bad as an active drafting space.
> - `20_timeline` should be generated or curated from events, not used as a dumping folder.
> - `90_assets` is media/templates/brand assets; Paperless is not the media asset manager.
> 
> So yes, consistency — but not blind mirroring. That’s how systems get bloated.
> 
> ## The clean rule
> 
> Paperless stores **source documents** in:
> 
> ```text
> 20_qinexus
> ```
> 
> Paperless sync worker stores **processed AI artifacts** in:
> 
> ```text
> 30_qiarchive
> ```
> 
> System logs/audits/backups go to:
> 
> ```text
> 40_system
> ```
> 
> Rules, standards, and documentation about Paperless go to:
> 
> ```text
> 10_core/40_service_apps/30_capture/30_paperless.md
> ```
> 
> That is the correct map.

### User
> ok, so we need to update the script and overwrite whats there correct.

### Assistant
> Correct. We update the seed script, but we do **not** blindly delete the taxonomy you already created. We’ll upsert the corrected QiNexus-aligned storage paths/tags, optionally retire the earlier generic paths, then verify counts.

### Assistant
> Yes — update the script and rerun it. But **do not nuke everything**. We want an **idempotent upgrade script**:
> 
> - creates missing QiNexus-aligned paths
> - creates bucket tags
> - updates existing storage path values
> - keeps existing docs/tags/types/correspondents
> - optionally renames old broad storage paths or leaves them harmless
> - does **not** delete documents
> 
> Your correct mapping is based on the updated four-domain model: `10_core`, `20_qinexus`, `30_qiarchive`, and `40_system`. Paperless archive files should mostly map into `20_qinexus`, while later sync/AI outputs go into `30_qiarchive`. Your map specifically places Paperless manifests under `30_qiarchive/10_ingestion/10_paperless` and Paperless service docs under `10_core/40_service_apps/30_capture/30_paperless.md`. fileciteturn3file0
> 
> ## Run this updated script
> 
> ```bash
> cat > /tmp/seed_paperless_qios_v2.py <<'PY'
> from documents.models import Tag, Correspondent, DocumentType, StoragePath, CustomField
> 
> def field_names(model):
>     return {f.name for f in model._meta.fields}
> 
> def upsert(model, name, **extra):
>     fields = field_names(model)
>     safe_extra = {k: v for k, v in extra.items() if k in fields}
> 
>     obj, created = model.objects.get_or_create(name=name, defaults=safe_extra)
> 
>     changed = False
>     for key, value in safe_extra.items():
>         if getattr(obj, key, None) != value:
>             setattr(obj, key, value)
>             changed = True
> 
>     if changed:
>         obj.save()
> 
>     print(("CREATED" if created else "UPDATED"), model.__name__, name)
>     return obj
> 
> # -------------------------
> # Document Types
> # -------------------------
> 
> document_types = [
>     "Bill",
>     "Receipt",
>     "Statement",
>     "Tax Document",
>     "Legal Filing",
>     "Court Notice",
>     "Contract / Agreement",
>     "Medical Record",
>     "Care Document",
>     "Insurance Document",
>     "Identity / Vital Record",
>     "Letter / Notice",
>     "Report",
>     "Technical Document",
>     "Reference Material",
>     "Database Export",
>     "System Log",
>     "Manifest",
>     "Unknown / Needs Review",
> ]
> 
> # -------------------------
> # Correspondents
> # -------------------------
> 
> correspondents = [
>     "Unknown / Needs Review",
>     "Court / Clerk",
>     "FCFCU",
>     "Chase",
>     "IRS",
>     "SSA",
>     "Medicaid / Medicare",
>     "Insurance Provider",
>     "Utility Provider",
>     "Medical Provider",
>     "Paperless Test",
>     "QiAccess / QiServer",
> ]
> 
> # -------------------------
> # Tags
> # -------------------------
> 
> domain_tags = [
>     "domain:care",
>     "domain:legal",
>     "domain:finance",
>     "domain:tax",
>     "domain:medical",
>     "domain:tech",
>     "domain:household",
>     "domain:identity",
>     "domain:business",
>     "domain:reference",
>     "domain:data",
>     "domain:system",
> ]
> 
> status_tags = [
>     "status:review-needed",
>     "status:processed",
>     "status:exported",
>     "status:synced",
>     "status:duplicate-check",
>     "status:urgent",
>     "status:archived",
> ]
> 
> source_tags = [
>     "source:scan",
>     "source:email",
>     "source:download",
>     "source:drive",
>     "source:mobile",
>     "source:paperless",
> ]
> 
> pipeline_tags = [
>     "pipeline:nocodb",
>     "pipeline:qdrant",
>     "pipeline:neo4j",
>     "pipeline:qiarchive",
>     "pipeline:pending-sync",
> ]
> 
> bucket_tags = [
>     "bucket:20_qinexus/00_inbox",
>     "bucket:20_qinexus/30_life",
>     "bucket:20_qinexus/40_people",
>     "bucket:20_qinexus/50_business",
>     "bucket:20_qinexus/60_finance",
>     "bucket:20_qinexus/70_legal",
>     "bucket:20_qinexus/80_tech",
>     "bucket:20_qinexus/100_data",
>     "bucket:20_qinexus/110_reference",
>     "bucket:20_qinexus/120_archive",
>     "bucket:20_qinexus/130_system",
> ]
> 
> all_tags = domain_tags + status_tags + source_tags + pipeline_tags + bucket_tags
> 
> # -------------------------
> # QiNexus-Aligned Storage Paths
> # -------------------------
> # Paperless archive/original source docs belong mostly under 20_qinexus.
> # Processed AI outputs belong later under 30_qiarchive via the sync worker, not Paperless storage paths.
> 
> storage_paths = {
>     "00 Inbox - Pending Review":
>         "20_qinexus/00_inbox/30_pending_review/{{ created_year }}/{{ title }}",
> 
>     "30 Life - Home":
>         "20_qinexus/30_life/10_home/{{ created_year }}/{{ document_type }}/{{ title }}",
> 
>     "30 Life - Wellness":
>         "20_qinexus/30_life/30_wellness/{{ created_year }}/{{ document_type }}/{{ title }}",
> 
>     "40 People - Care Coordination":
>         "20_qinexus/40_people/30_care_coordination/{{ created_year }}/{{ document_type }}/{{ title }}",
> 
>     "50 Business - Operations":
>         "20_qinexus/50_business/60_business_operations/{{ created_year }}/{{ document_type }}/{{ title }}",
> 
>     "60 Finance - Bills":
>         "20_qinexus/60_finance/20_bills/{{ created_year }}/{{ correspondent }}/{{ title }}",
> 
>     "60 Finance - Accounts":
>         "20_qinexus/60_finance/30_accounts/{{ created_year }}/{{ correspondent }}/{{ title }}",
> 
>     "60 Finance - Statements":
>         "20_qinexus/60_finance/40_statements/{{ created_year }}/{{ correspondent }}/{{ title }}",
> 
>     "60 Finance - Reconciliations":
>         "20_qinexus/60_finance/50_reconciliations/{{ created_year }}/{{ document_type }}/{{ title }}",
> 
>     "60 Finance - Reports":
>         "20_qinexus/60_finance/60_reports/{{ created_year }}/{{ document_type }}/{{ title }}",
> 
>     "60 Finance - General Ledger":
>         "20_qinexus/60_finance/70_general_ledger/{{ created_year }}/{{ document_type }}/{{ title }}",
> 
>     "60 Finance - Tax":
>         "20_qinexus/60_finance/80_tax/{{ created_year }}/{{ document_type }}/{{ title }}",
> 
>     "70 Legal - Matters":
>         "20_qinexus/70_legal/10_matters/{{ created_year }}/{{ title }}",
> 
>     "70 Legal - Filings":
>         "20_qinexus/70_legal/20_filings/{{ created_year }}/{{ document_type }}/{{ title }}",
> 
>     "70 Legal - Evidence":
>         "20_qinexus/70_legal/30_evidence/{{ created_year }}/{{ document_type }}/{{ title }}",
> 
>     "70 Legal - Timelines":
>         "20_qinexus/70_legal/40_timelines/{{ created_year }}/{{ title }}",
> 
>     "70 Legal - Motions Drafts":
>         "20_qinexus/70_legal/50_motions_drafts/{{ created_year }}/{{ title }}",
> 
>     "70 Legal - Research":
>         "20_qinexus/70_legal/60_research/{{ created_year }}/{{ title }}",
> 
>     "70 Legal - Regulatory Complaints":
>         "20_qinexus/70_legal/70_regulatory_complaints/{{ created_year }}/{{ title }}",
> 
>     "70 Legal - Exhibits":
>         "20_qinexus/70_legal/80_exhibits/{{ created_year }}/{{ title }}",
> 
>     "80 Tech - Qiserver":
>         "20_qinexus/80_tech/10_qiserver/{{ created_year }}/{{ document_type }}/{{ title }}",
> 
>     "80 Tech - Apps":
>         "20_qinexus/80_tech/20_apps/{{ created_year }}/{{ document_type }}/{{ title }}",
> 
>     "80 Tech - Repos":
>         "20_qinexus/80_tech/30_repos/{{ created_year }}/{{ title }}",
> 
>     "80 Tech - Scripts":
>         "20_qinexus/80_tech/40_scripts/{{ created_year }}/{{ title }}",
> 
>     "80 Tech - Deployments":
>         "20_qinexus/80_tech/50_deployments/{{ created_year }}/{{ title }}",
> 
>     "80 Tech - Tooling":
>         "20_qinexus/80_tech/60_tooling/{{ created_year }}/{{ title }}",
> 
>     "80 Tech - Dev Runbooks":
>         "20_qinexus/80_tech/70_dev_runbooks/{{ created_year }}/{{ title }}",
> 
>     "100 Data - CSV":
>         "20_qinexus/100_data/10_csv/{{ created_year }}/{{ title }}",
> 
>     "100 Data - JSON":
>         "20_qinexus/100_data/20_json/{{ created_year }}/{{ title }}",
> 
>     "100 Data - Database Exports":
>         "20_qinexus/100_data/30_database_exports/{{ created_year }}/{{ title }}",
> 
>     "100 Data - Logs":
>         "20_qinexus/100_data/40_logs/{{ created_year }}/{{ title }}",
> 
>     "100 Data - Datasets":
>         "20_qinexus/100_data/50_datasets/{{ created_year }}/{{ title }}",
> 
>     "100 Data - Source Tables":
>         "20_qinexus/100_data/60_source_tables/{{ created_year }}/{{ title }}",
> 
>     "110 Reference - Articles":
>         "20_qinexus/110_reference/10_articles/{{ created_year }}/{{ title }}",
> 
>     "110 Reference - Research":
>         "20_qinexus/110_reference/20_research/{{ created_year }}/{{ title }}",
> 
>     "110 Reference - Legal References":
>         "20_qinexus/110_reference/30_legal_references/{{ created_year }}/{{ title }}",
> 
>     "110 Reference - Technical Guides":
>         "20_qinexus/110_reference/40_technical_guides/{{ created_year }}/{{ title }}",
> 
>     "110 Reference - Examples":
>         "20_qinexus/110_reference/50_examples/{{ created_year }}/{{ title }}",
> 
>     "110 Reference - Citations":
>         "20_qinexus/110_reference/60_citations/{{ created_year }}/{{ title }}",
> 
>     "110 Reference - External Docs":
>         "20_qinexus/110_reference/70_external_docs/{{ created_year }}/{{ title }}",
> 
>     "120 Archive - Historical Files":
>         "20_qinexus/120_archive/30_historical_files/{{ created_year }}/{{ title }}",
> 
>     "120 Archive - Frozen Exports":
>         "20_qinexus/120_archive/40_frozen_exports/{{ created_year }}/{{ title }}",
> 
>     "120 Archive - Superseded Material":
>         "20_qinexus/120_archive/60_superseded_material/{{ created_year }}/{{ title }}",
> 
>     "130 System - Folder Manifest":
>         "20_qinexus/130_system/20_folder_manifest/{{ created_year }}/{{ title }}",
> 
>     "130 System - Sync Notes":
>         "20_qinexus/130_system/50_sync_notes/{{ created_year }}/{{ title }}",
> 
>     "130 System - Structure Docs":
>         "20_qinexus/130_system/60_structure_docs/{{ created_year }}/{{ title }}",
> }
> 
> # -------------------------
> # Custom Fields
> # -------------------------
> 
> custom_fields = [
>     "Qi Domain",
>     "Qi Bucket",
>     "Qi Source System",
>     "Qi Sync Status",
>     "Qi External ID",
>     "Qi Matter ID",
>     "Qi Account ID",
>     "Qi Event Date",
>     "Qi Review Status",
>     "Qi Notes",
>     "QiArchive Status",
>     "QiArchive Source ID",
>     "Qdrant Collection",
>     "Neo4j Node ID",
> ]
> 
> # -------------------------
> # Create / update objects
> # -------------------------
> 
> for name in document_types:
>     upsert(DocumentType, name)
> 
> for name in correspondents:
>     upsert(Correspondent, name)
> 
> for name in all_tags:
>     upsert(Tag, name)
> 
> for name, path in storage_paths.items():
>     upsert(StoragePath, name, path=path)
> 
> for name in custom_fields:
>     upsert(CustomField, name)
> 
> print("DONE: QiOS/Paperless v2 taxonomy seed complete.")
> print("NOTE: This script does not delete old generic paths. Review and remove/archive those manually after confirming no documents use them.")
> PY
> 
> sudo docker cp /tmp/seed_paperless_qios_v2.py paperless:/tmp/seed_paperless_qios_v2.py
> sudo docker exec -it paperless bash -lc 'python manage.py shell < /tmp/seed_paperless_qios_v2.py'
> ```
> 
> ## Verify it worked
> 
> ```bash
> sudo docker exec -it paperless bash -lc 'python manage.py shell -c "
> from documents.models import Tag, Correspondent, DocumentType, StoragePath, CustomField
> print(\"Tags:\", Tag.objects.count())
> print(\"Correspondents:\", Correspondent.objects.count())
> print(\"Document types:\", DocumentType.objects.count())
> print(\"Storage paths:\", StoragePath.objects.count())
> print(\"Custom fields:\", CustomField.objects.count())
> print(\"\\nStorage paths:\")
> [print(f\"- {x.name}: {x.path}\") for x in StoragePath.objects.all().order_by(\"name\")]
> "'
> ```
> 
> ## Important: don’t delete old paths yet
> 
> The old ones like:
> 
> ```text
> Default
> Legal
> Finance
> Care
> Medical
> Tech
> Reference
> Needs Review
> ```
> 
> can stay for now. After we confirm no documents use them, we can remove or rename them.
> 
> Next after this: we add **rules**, but only high-confidence ones. Storage paths are the shelves. Rules are the robotic librarian. We do not give the robotic librarian tequila.

### User
> lets try again, there is not way that is enought for everything we about to ingest and i dont see the matching rules either which is why everything ended up tagged the same way last time.

### Assistant
> You’re dead-on. The v2 script fixed shelf names, not the actual intelligence layer. For your ingestion volume, we need a **rules matrix**: narrow match terms, domain/bucket routing, document-type rules, correspondent rules, and “review-needed” fallback so nothing gets mislabeled into oblivion.

### Assistant
> Yep. This is the right objection.
> 
> The previous script was **not enough** for the volume you’re about to ingest. It created shelves. It did not create a reliable sorting brain.
> 
> Paperless matching works by comparing the `match` + `matching_algorithm` on **tags, correspondents, document types, and storage paths** against OCR text, and the official docs explicitly warn that the logic needs experimentation. The available algorithms include None, Any, All, Exact, Regular expression, Fuzzy, and Auto. citeturn776426view0
> 
> So the fix is:
> 
> 1. **Storage paths map to the correct updated folders**
> 2. **Tags use narrow high-confidence matching**
> 3. **Document types use pattern-specific matching**
> 4. **Correspondents use exact names only**
> 5. **Default everything unknown to review**
> 6. **Auto matching stays mostly off until we have clean examples**
> 7. **Batch ingestion happens in waves, not chaos-dump mode**
> 
> Paperless also uses OCR content for matching and stores consumed files inside its own file structure using configured storage paths, so we need this configured before dumping files in. citeturn776426view1
> 
> ## Correct map
> 
> Paperless original/archive documents should map to:
> 
> ```text
> 20_qinexus/...
> ```
> 
> The later AI pipeline outputs should map to:
> 
> ```text
> 30_qiarchive/...
> ```
> 
> Specifically, Paperless service documentation belongs under `10_core/40_service_apps/30_capture/30_paperless.md`, while Paperless ingestion manifests belong under `30_qiarchive/10_ingestion/10_paperless`. Your current map says QiArchive owns ingestion, extraction, chunking, embeddings, graphs, retrieval, and memory artifacts, while QiNexus is the human-facing source terrain. fileciteturn3file0
> 
> So no, we should not make Paperless paths for `10_core` or `30_qiarchive` as normal document storage. Paperless stores source documents into QiNexus-style paths. The sync worker later writes processed artifacts to QiArchive.
> 
> ## What the new v3 script needs to do
> 
> It should create/update:
> 
> 1. expanded document types
> 2. expanded correspondents
> 3. domain/status/source/bucket/pipeline tags
> 4. QiNexus-aligned storage paths
> 5. matching rules for document types
> 6. matching rules for correspondents
> 7. matching rules for tags
> 8. matching rules for storage paths
> 9. safe review fallback tags/paths
> 
> And it needs to use **exact/regex/all-word matching**, not broad any-word garbage.
> 
> ## Matching rule doctrine
> 
> Bad:
> 
> ```text
> finance = account payment statement
> ```
> 
> That catches everything.
> 
> Good:
> 
> ```text
> Statement = "statement period" OR "account summary" OR "transactions from"
> ```
> 
> Good:
> 
> ```text
> Legal Filing = "cause number" OR "case number" OR "plaintiff" OR "defendant"
> ```
> 
> Good:
> 
> ```text
> IRS = "Internal Revenue Service" OR "Department of the Treasury"
> ```
> 
> ## Paste-ready v3 seed script
> 
> This version updates the existing objects and adds actual matching rules. It does **not** delete documents.
> 
> ```bash
> cat > /tmp/seed_paperless_qios_v3_rules.py <<'PY'
> from documents.models import Tag, Correspondent, DocumentType, StoragePath, CustomField
> 
> def field_names(model):
>     return {f.name for f in model._meta.fields}
> 
> def choice_map(model, field_name):
>     try:
>         field = model._meta.get_field(field_name)
>         return {str(label).lower(): value for value, label in field.choices}
>     except Exception:
>         return {}
> 
> def resolve_matching_algorithm(model, preferred):
>     """
>     Resolve Paperless matching algorithm values without hardcoding enum integers.
>     preferred examples: none, any, all, exact, regular expression, fuzzy, auto
>     """
>     choices = choice_map(model, "matching_algorithm")
>     if not choices:
>         return None
> 
>     preferred = preferred.lower().strip()
> 
>     # Exact label match first
>     for label, value in choices.items():
>         if label == preferred:
>             return value
> 
>     # Friendly fallback matching
>     aliases = {
>         "regex": ["regular expression", "regex"],
>         "regular expression": ["regular expression", "regex"],
>         "any": ["any"],
>         "all": ["all"],
>         "exact": ["exact"],
>         "fuzzy": ["fuzzy"],
>         "auto": ["auto"],
>         "none": ["none"],
>     }
> 
>     for needle in aliases.get(preferred, [preferred]):
>         for label, value in choices.items():
>             if needle in label:
>                 return value
> 
>     print(f"WARNING: Could not resolve matching algorithm {preferred!r} for {model.__name__}. Choices={choices}")
>     return None
> 
> def upsert(model, name, **extra):
>     fields = field_names(model)
>     safe_extra = {k: v for k, v in extra.items() if k in fields}
> 
>     obj, created = model.objects.get_or_create(name=name, defaults=safe_extra)
> 
>     changed = False
>     for key, value in safe_extra.items():
>         if value is not None and getattr(obj, key, None) != value:
>             setattr(obj, key, value)
>             changed = True
> 
>     if changed:
>         obj.save()
> 
>     print(("CREATED" if created else "UPDATED"), model.__name__, name)
>     return obj
> 
> def set_match(model, name, match, algorithm):
>     algo = resolve_matching_algorithm(model, algorithm)
>     extra = {}
>     if "match" in field_names(model):
>         extra["match"] = match
>     if "matching_algorithm" in field_names(model):
>         extra["matching_algorithm"] = algo
>     return upsert(model, name, **extra)
> 
> # ------------------------------------------------------------
> # Matching helpers
> # ------------------------------------------------------------
> 
> REGEX_FLAGS = "(?is)"  # case-insensitive + dot matches newline
> 
> # ------------------------------------------------------------
> # Document Types
> # ------------------------------------------------------------
> 
> document_type_rules = {
>     "Bill": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(amount\s+due|payment\s+due|due\s+date|minimum\s+payment|current\s+charges|new\s+charges|autopay|statement\s+balance)",
>     },
>     "Receipt": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(receipt|total\s+paid|payment\s+received|order\s+total|subtotal|sales\s+tax|transaction\s+id|merchant\s+copy)",
>     },
>     "Statement": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(statement\s+period|account\s+summary|opening\s+balance|closing\s+balance|transaction\s+summary|deposits\s+and\s+withdrawals|monthly\s+statement)",
>     },
>     "Tax Document": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(\bW-?2\b|\b1099\b|\b1098\b|\b1040\b|tax\s+year|internal\s+revenue\s+service|department\s+of\s+the\s+treasury)",
>     },
>     "Legal Filing": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(cause\s+number|case\s+number|plaintiff|defendant|motion\s+to|petition|complaint|affidavit|certificate\s+of\s+service|filed\s+with\s+the\s+court)",
>     },
>     "Court Notice": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(notice\s+of\s+hearing|summons|subpoena|order\s+of\s+court|court\s+date|hearing\s+date|writ\s+of|clerk\s+of\s+court)",
>     },
>     "Contract / Agreement": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(agreement|contract|terms\s+and\s+conditions|party\s+of\s+the\s+first\s+part|effective\s+date|signature|signed\s+by)",
>     },
>     "Medical Record": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(visit\s+summary|after\s+visit\s+summary|patient\s+instructions|medical\s+record|clinical\s+summary|provider\s+notes|diagnosis|medication\s+list)",
>     },
>     "Care Document": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(care\s+plan|caregiver|home\s+care|care\s+coordination|plan\s+of\s+care|service\s+plan|daily\s+care)",
>     },
>     "Insurance Document": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(policy\s+number|claim\s+number|explanation\s+of\s+benefits|eob|coverage|premium|deductible|insurance)",
>     },
>     "Identity / Vital Record": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(birth\s+certificate|social\s+security|driver'?s\s+license|state\s+id|passport|vital\s+record|certificate\s+of)",
>     },
>     "Letter / Notice": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(notice|dear\s+[a-z ,.'-]+|this\s+letter|you\s+are\s+receiving\s+this|important\s+information)",
>     },
>     "Report": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(report|summary\s+report|analysis|findings|prepared\s+for|generated\s+on)",
>     },
>     "Technical Document": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(docker|server|api|database|postgres|qdrant|neo4j|cloudflare|tailscale|deployment|configuration|runbook)",
>     },
>     "Reference Material": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(guide|manual|reference|documentation|instructions|how\s+to|faq|overview)",
>     },
>     "Database Export": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(csv|json|export|database\s+export|table\s+export|records\s+export|ledger\s+export)",
>     },
>     "System Log": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(error\s+log|build\s+log|sync\s+log|deployment\s+log|docker\s+logs|traceback|exception)",
>     },
>     "Manifest": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(manifest|file\s+manifest|folder\s+manifest|sync\s+manifest|backup\s+manifest)",
>     },
>     "Unknown / Needs Review": {
>         "algorithm": "none",
>         "match": "",
>     },
> }
> 
> # ------------------------------------------------------------
> # Correspondents
> # Keep these exact or regex-narrow. No sloppy one-word nonsense.
> # ------------------------------------------------------------
> 
> correspondent_rules = {
>     "Unknown / Needs Review": {"algorithm": "none", "match": ""},
>     "Court / Clerk": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(clerk\s+of\s+(court|the\s+court)|circuit\s+court|superior\s+court|small\s+claims\s+court|county\s+clerk)",
>     },
>     "FCFCU": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(financial\s+center\s+first\s+credit\s+union|\bFCFCU\b)",
>     },
>     "Chase": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(jpmorgan\s+chase|jp\s*morgan\s+chase|chase\s+bank|chase\s+card|chase\s+freedom)",
>     },
>     "IRS": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(internal\s+revenue\s+service|department\s+of\s+the\s+treasury|\bIRS\b)",
>     },
>     "SSA": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(social\s+security\s+administration|\bSSA\b)",
>     },
>     "Medicaid / Medicare": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(medicaid|medicare|centers\s+for\s+medicare\s+(&|and)\s+medicaid|cms)",
>     },
>     "Insurance Provider": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(insurance\s+company|policyholder|policy\s+number|claim\s+number|explanation\s+of\s+benefits)",
>     },
>     "Utility Provider": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(electric\s+bill|gas\s+bill|water\s+bill|sewer|utility\s+bill|amount\s+due)",
>     },
>     "Medical Provider": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(medical\s+center|hospital|clinic|physician|provider|patient\s+portal|visit\s+summary)",
>     },
>     "Paperless Test": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(paperless\s+test|qiaccess\s+paperless\s+ocr\s+pipeline\s+test)",
>     },
>     "QiAccess / QiServer": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(qiaccess|qiserver|qios|qinexus|qiarchive|qdrant|neo4j|paperless\s+sync)",
>     },
> }
> 
> # ------------------------------------------------------------
> # Tags
> # Tags can stack. Make them careful.
> # ------------------------------------------------------------
> 
> tag_rules = {
>     # Domains
>     "domain:finance": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(statement\s+period|account\s+summary|minimum\s+payment|payment\s+due|routing\s+number|transaction\s+summary|tax\s+year|invoice|receipt)",
>     },
>     "domain:legal": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(cause\s+number|case\s+number|plaintiff|defendant|motion|summons|writ|foreclosure|court|clerk\s+of\s+court|affidavit)",
>     },
>     "domain:tax": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(\bW-?2\b|\b1099\b|\b1098\b|\b1040\b|tax\s+year|internal\s+revenue\s+service|department\s+of\s+the\s+treasury)",
>     },
>     "domain:medical": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(visit\s+summary|patient\s+instructions|medical\s+record|diagnosis|medication|provider\s+notes|clinical\s+summary)",
>     },
>     "domain:care": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(care\s+plan|caregiver|home\s+care|care\s+coordination|plan\s+of\s+care|daily\s+care|service\s+plan)",
>     },
>     "domain:tech": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(qiserver|qiaccess|docker|cloudflare|tailscale|portainer|cockpit|postgres|qdrant|neo4j|ollama|api|deployment)",
>     },
>     "domain:business": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(client|invoice|business|brand|offer|proposal|contractor|vendor|revenue)",
>     },
>     "domain:reference": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(guide|manual|reference|documentation|article|research|citation|example|faq)",
>     },
>     "domain:data": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(csv|json|dataset|database\s+export|table\s+export|ledger\s+export|records\s+export)",
>     },
>     "domain:system": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(manifest|sync\s+log|backup\s+manifest|system\s+log|folder\s+manifest|health\s+check)",
>     },
> 
>     # Status tags
>     # Keep review-needed as none. We will apply this manually/bulk or through inbox workflows later.
>     "status:review-needed": {"algorithm": "none", "match": ""},
>     "status:processed": {"algorithm": "none", "match": ""},
>     "status:exported": {"algorithm": "none", "match": ""},
>     "status:synced": {"algorithm": "none", "match": ""},
>     "status:duplicate-check": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(duplicate|copy\s+of|scan\s+copy|second\s+copy)",
>     },
>     "status:urgent": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(urgent|final\s+notice|past\s+due|immediate\s+action|required\s+by|deadline|notice\s+of\s+hearing)",
>     },
>     "status:archived": {"algorithm": "none", "match": ""},
> 
>     # Source tags mostly should not auto-match from content except obvious cases.
>     "source:scan": {"algorithm": "none", "match": ""},
>     "source:email": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(from:|to:|subject:|sent:|received:|email)",
>     },
>     "source:download": {"algorithm": "none", "match": ""},
>     "source:drive": {"algorithm": "none", "match": ""},
>     "source:mobile": {"algorithm": "none", "match": ""},
>     "source:paperless": {"algorithm": "none", "match": ""},
> 
>     # Pipeline tags are not content-derived. The sync worker should set these later.
>     "pipeline:nocodb": {"algorithm": "none", "match": ""},
>     "pipeline:qdrant": {"algorithm": "none", "match": ""},
>     "pipeline:neo4j": {"algorithm": "none", "match": ""},
>     "pipeline:qiarchive": {"algorithm": "none", "match": ""},
>     "pipeline:pending-sync": {"algorithm": "none", "match": ""},
> 
>     # Bucket tags
>     "bucket:20_qinexus/00_inbox": {"algorithm": "none", "match": ""},
>     "bucket:20_qinexus/30_life": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(home|household|utility|routine|personal\s+guide)",
>     },
>     "bucket:20_qinexus/40_people": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(care\s+coordination|family|support\s+network|communication\s+plan|relationship\s+context)",
>     },
>     "bucket:20_qinexus/50_business": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(client|business|brand|offer|proposal|marketing|vendor)",
>     },
>     "bucket:20_qinexus/60_finance": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(statement\s+period|account\s+summary|bill|receipt|invoice|tax\s+year|reconciliation|ledger)",
>     },
>     "bucket:20_qinexus/70_legal": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(case\s+number|cause\s+number|court|plaintiff|defendant|motion|filing|evidence|exhibit|complaint)",
>     },
>     "bucket:20_qinexus/80_tech": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(qiserver|docker|cloudflare|tailscale|qdrant|neo4j|postgres|deployment|runbook|api)",
>     },
>     "bucket:20_qinexus/100_data": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(csv|json|database\s+export|dataset|source\s+table|exported\s+records)",
>     },
>     "bucket:20_qinexus/110_reference": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(reference|manual|guide|article|research|citation|external\s+document)",
>     },
>     "bucket:20_qinexus/120_archive": {"algorithm": "none", "match": ""},
>     "bucket:20_qinexus/130_system": {
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(folder\s+manifest|sync\s+notes|structure\s+docs|system\s+manifest)",
>     },
> }
> 
> # ------------------------------------------------------------
> # Storage Paths
> # Storage paths can also match content.
> # These are intentionally narrower than tags.
> # ------------------------------------------------------------
> 
> storage_path_rules = {
>     "00 Inbox - Pending Review": {
>         "path": "20_qinexus/00_inbox/30_pending_review/{{ created_year }}/{{ title }}",
>         "algorithm": "none",
>         "match": "",
>     },
> 
>     "30 Life - Home": {
>         "path": "20_qinexus/30_life/10_home/{{ created_year }}/{{ document_type }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(utility\s+bill|electric\s+bill|gas\s+bill|water\s+bill|lease|home|household)",
>     },
>     "30 Life - Wellness": {
>         "path": "20_qinexus/30_life/30_wellness/{{ created_year }}/{{ document_type }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(wellness|routine|personal\s+care|health\s+plan)",
>     },
>     "40 People - Care Coordination": {
>         "path": "20_qinexus/40_people/30_care_coordination/{{ created_year }}/{{ document_type }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(care\s+plan|caregiver|home\s+care|care\s+coordination|plan\s+of\s+care|service\s+plan)",
>     },
>     "50 Business - Operations": {
>         "path": "20_qinexus/50_business/60_business_operations/{{ created_year }}/{{ document_type }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(business|client|proposal|invoice|vendor|contractor)",
>     },
> 
>     "60 Finance - Bills": {
>         "path": "20_qinexus/60_finance/20_bills/{{ created_year }}/{{ correspondent }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(amount\s+due|payment\s+due|due\s+date|minimum\s+payment|current\s+charges|new\s+charges)",
>     },
>     "60 Finance - Accounts": {
>         "path": "20_qinexus/60_finance/30_accounts/{{ created_year }}/{{ correspondent }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(account\s+number|routing\s+number|account\s+opening|account\s+agreement|cardmember\s+agreement)",
>     },
>     "60 Finance - Statements": {
>         "path": "20_qinexus/60_finance/40_statements/{{ created_year }}/{{ correspondent }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(statement\s+period|monthly\s+statement|account\s+summary|opening\s+balance|closing\s+balance|transaction\s+summary)",
>     },
>     "60 Finance - Reconciliations": {
>         "path": "20_qinexus/60_finance/50_reconciliations/{{ created_year }}/{{ document_type }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(reconciliation|reconciled|variance|cleared\s+transactions)",
>     },
>     "60 Finance - Reports": {
>         "path": "20_qinexus/60_finance/60_reports/{{ created_year }}/{{ document_type }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(financial\s+report|profit\s+and\s+loss|balance\s+sheet|cash\s+flow|summary\s+report)",
>     },
>     "60 Finance - General Ledger": {
>         "path": "20_qinexus/60_finance/70_general_ledger/{{ created_year }}/{{ document_type }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(general\s+ledger|ledger\s+export|chart\s+of\s+accounts|journal\s+entry)",
>     },
>     "60 Finance - Tax": {
>         "path": "20_qinexus/60_finance/80_tax/{{ created_year }}/{{ document_type }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(\bW-?2\b|\b1099\b|\b1098\b|\b1040\b|tax\s+year|internal\s+revenue\s+service)",
>     },
> 
>     "70 Legal - Matters": {
>         "path": "20_qinexus/70_legal/10_matters/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(matter|case\s+number|cause\s+number|plaintiff|defendant)",
>     },
>     "70 Legal - Filings": {
>         "path": "20_qinexus/70_legal/20_filings/{{ created_year }}/{{ document_type }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(motion\s+to|petition|complaint|filed|filing|certificate\s+of\s+service|affidavit)",
>     },
>     "70 Legal - Evidence": {
>         "path": "20_qinexus/70_legal/30_evidence/{{ created_year }}/{{ document_type }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(evidence|photograph|screenshot|recording|proof|receipt|exhibit)",
>     },
>     "70 Legal - Timelines": {
>         "path": "20_qinexus/70_legal/40_timelines/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(timeline|chronology|sequence\s+of\s+events|event\s+trail)",
>     },
>     "70 Legal - Motions Drafts": {
>         "path": "20_qinexus/70_legal/50_motions_drafts/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(draft\s+motion|motion\s+draft|memorandum|brief)",
>     },
>     "70 Legal - Research": {
>         "path": "20_qinexus/70_legal/60_research/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(statute|case\s+law|legal\s+research|rule\s+of\s+civil\s+procedure|citation)",
>     },
>     "70 Legal - Regulatory Complaints": {
>         "path": "20_qinexus/70_legal/70_regulatory_complaints/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(regulatory\s+complaint|consumer\s+complaint|cfpb|attorney\s+general|complaint\s+form)",
>     },
>     "70 Legal - Exhibits": {
>         "path": "20_qinexus/70_legal/80_exhibits/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(exhibit\s+[a-z0-9]|exhibit\s+list|marked\s+as\s+exhibit)",
>     },
> 
>     "80 Tech - Qiserver": {
>         "path": "20_qinexus/80_tech/10_qiserver/{{ created_year }}/{{ document_type }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(qiserver|ubuntu|docker|portainer|cockpit|tailscale|cloudflare\s+tunnel)",
>     },
>     "80 Tech - Apps": {
>         "path": "20_qinexus/80_tech/20_apps/{{ created_year }}/{{ document_type }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(qiaccess|moms?\s+care|application|app\s+architecture|frontend|backend)",
>     },
>     "80 Tech - Repos": {
>         "path": "20_qinexus/80_tech/30_repos/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(repository|github|repo|commit|branch|pull\s+request)",
>     },
>     "80 Tech - Scripts": {
>         "path": "20_qinexus/80_tech/40_scripts/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(script|python|bash|powershell|automation\s+script)",
>     },
>     "80 Tech - Deployments": {
>         "path": "20_qinexus/80_tech/50_deployments/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(deployment|deploy|build\s+log|cloudflare\s+pages|docker\s+compose)",
>     },
>     "80 Tech - Tooling": {
>         "path": "20_qinexus/80_tech/60_tooling/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(tooling|codex|aider|ollama|open\s+webui|paperless|n8n|solidtime)",
>     },
>     "80 Tech - Dev Runbooks": {
>         "path": "20_qinexus/80_tech/70_dev_runbooks/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(runbook|dev\s+runbook|setup\s+steps|install\s+guide|troubleshooting)",
>     },
> 
>     "100 Data - CSV": {
>         "path": "20_qinexus/100_data/10_csv/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(\.csv|comma-separated|csv\s+export)",
>     },
>     "100 Data - JSON": {
>         "path": "20_qinexus/100_data/20_json/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(\.json|json\s+export|json\s+data)",
>     },
>     "100 Data - Database Exports": {
>         "path": "20_qinexus/100_data/30_database_exports/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(database\s+export|sql\s+dump|table\s+export|records\s+export)",
>     },
>     "100 Data - Logs": {
>         "path": "20_qinexus/100_data/40_logs/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(log\s+file|error\s+log|sync\s+log|import\s+log|traceback|exception)",
>     },
>     "100 Data - Datasets": {
>         "path": "20_qinexus/100_data/50_datasets/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(dataset|data\s+set|source\s+data)",
>     },
>     "100 Data - Source Tables": {
>         "path": "20_qinexus/100_data/60_source_tables/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(source\s+table|table\s+schema|spreadsheet\s+export)",
>     },
> 
>     "110 Reference - Articles": {
>         "path": "20_qinexus/110_reference/10_articles/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(article|published|author|journal|newsletter)",
>     },
>     "110 Reference - Research": {
>         "path": "20_qinexus/110_reference/20_research/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(research|study|whitepaper|findings|methodology)",
>     },
>     "110 Reference - Legal References": {
>         "path": "20_qinexus/110_reference/30_legal_references/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(statute|case\s+law|legal\s+reference|rule\s+of\s+civil\s+procedure|usc|ic\s+\d)",
>     },
>     "110 Reference - Technical Guides": {
>         "path": "20_qinexus/110_reference/40_technical_guides/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(technical\s+guide|documentation|api\s+docs|manual|configuration)",
>     },
>     "110 Reference - Examples": {
>         "path": "20_qinexus/110_reference/50_examples/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(example|sample|template|demo)",
>     },
>     "110 Reference - Citations": {
>         "path": "20_qinexus/110_reference/60_citations/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(citation|bibliography|source\s+list|references)",
>     },
>     "110 Reference - External Docs": {
>         "path": "20_qinexus/110_reference/70_external_docs/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(external\s+document|downloaded\s+document|guide|manual)",
>     },
> 
>     "120 Archive - Historical Files": {
>         "path": "20_qinexus/120_archive/30_historical_files/{{ created_year }}/{{ title }}",
>         "algorithm": "none",
>         "match": "",
>     },
>     "120 Archive - Frozen Exports": {
>         "path": "20_qinexus/120_archive/40_frozen_exports/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(frozen\s+export|final\s+export|archive\s+copy)",
>     },
>     "120 Archive - Superseded Material": {
>         "path": "20_qinexus/120_archive/60_superseded_material/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(superseded|deprecated|old\s+version|replaced\s+by)",
>     },
> 
>     "130 System - Folder Manifest": {
>         "path": "20_qinexus/130_system/20_folder_manifest/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(folder\s+manifest|directory\s+tree|folder\s+map)",
>     },
>     "130 System - Sync Notes": {
>         "path": "20_qinexus/130_system/50_sync_notes/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(sync\s+notes|sync\s+status|sync\s+manifest)",
>     },
>     "130 System - Structure Docs": {
>         "path": "20_qinexus/130_system/60_structure_docs/{{ created_year }}/{{ title }}",
>         "algorithm": "regular expression",
>         "match": REGEX_FLAGS + r"(structure\s+doc|system\s+map|knowledge\s+system\s+map|folder\s+structure)",
>     },
> }
> 
> # ------------------------------------------------------------
> # Custom Fields
> # ------------------------------------------------------------
> 
> custom_fields = [
>     "Qi Domain",
>     "Qi Bucket",
>     "Qi Source System",
>     "Qi Sync Status",
>     "Qi External ID",
>     "Qi Matter ID",
>     "Qi Account ID",
>     "Qi Event Date",
>     "Qi Review Status",
>     "Qi Notes",
>     "QiArchive Status",
>     "QiArchive Source ID",
>     "Qdrant Collection",
>     "Neo4j Node ID",
> ]
> 
> # ------------------------------------------------------------
> # Apply all objects
> # ------------------------------------------------------------
> 
> for name, rule in document_type_rules.items():
>     set_match(DocumentType, name, rule["match"], rule["algorithm"])
> 
> for name, rule in correspondent_rules.items():
>     set_match(Correspondent, name, rule["match"], rule["algorithm"])
> 
> for name, rule in tag_rules.items():
>     set_match(Tag, name, rule["match"], rule["algorithm"])
> 
> for name, rule in storage_path_rules.items():
>     path = rule["path"]
>     algo = resolve_matching_algorithm(StoragePath, rule["algorithm"])
>     extra = {"path": path}
>     if "match" in field_names(StoragePath):
>         extra["match"] = rule["match"]
>     if "matching_algorithm" in field_names(StoragePath):
>         extra["matching_algorithm"] = algo
>     upsert(StoragePath, name, **extra)
> 
> for name in custom_fields:
>     upsert(CustomField, name)
> 
> print("DONE: QiOS/Paperless v3 rules seed complete.")
> print("This created/upserted taxonomy + conservative matching rules.")
> print("Next: ingest 10-25 mixed test documents, inspect bad matches, tighten rules.")
> PY
> 
> sudo docker cp /tmp/seed_paperless_qios_v3_rules.py paperless:/tmp/seed_paperless_qios_v3_rules.py
> sudo docker exec -it paperless bash -lc 'python manage.py shell < /tmp/seed_paperless_qios_v3_rules.py'
> ```
> 
> ## Verify the rules actually landed
> 
> ```bash
> sudo docker exec -it paperless bash -lc 'python manage.py shell -c "
> from documents.models import Tag, Correspondent, DocumentType, StoragePath
> 
> def show(model, title):
>     print(\"\\n\" + title)
>     for x in model.objects.all().order_by(\"name\"):
>         match = getattr(x, \"match\", \"\")
>         algo = getattr(x, \"matching_algorithm\", \"\")
>         path = getattr(x, \"path\", None)
>         if path:
>             print(f\"- {x.name} | algo={algo} | path={path} | match={match[:90]}\")
>         else:
>             print(f\"- {x.name} | algo={algo} | match={match[:90]}\")
> show(DocumentType, \"DOCUMENT TYPES\")
> show(Correspondent, \"CORRESPONDENTS\")
> show(Tag, \"TAGS\")
> show(StoragePath, \"STORAGE PATHS\")
> "'
> ```
> 
> ## But here’s the uncomfortable truth
> 
> Even this v3 is not “perfect.” It is a **much better first ruleset**, but the real system becomes good through a calibration loop.
> 
> You need this ingestion protocol:
> 
> ### Batch 1: 10–25 mixed docs
> 
> Include:
> 
> - 3 financial
> - 3 legal
> - 3 care/medical
> - 3 tech/reference
> - 3 random weird docs
> 
> Then review:
> 
> ```text
> Did it pick the right document type?
> Did it pick the right correspondent?
> Did it pick the right storage path?
> Did it over-tag anything?
> Did anything that should be review-needed slip into a confident folder?
> ```
> 
> ### Batch 2: 50 docs
> 
> Fix bad rules before going bigger.
> 
> ### Batch 3: 200 docs
> 
> Only after the first two batches look sane.
> 
> ### Bulk ingestion
> 
> Only after the rules stop being stupid.
> 
> ## Why this prevents last time’s mess
> 
> Last time everything got tagged the same because the rules were probably too broad, likely using “Any” with generic words. The official docs even say Any matches documents containing any provided word, which is exactly how `account payment notice` becomes a metadata lawn sprinkler. citeturn776426view0
> 
> This version uses regex phrases like:
> 
> ```text
> statement period
> account summary
> notice of hearing
> cause number
> internal revenue service
> visit summary
> care plan
> qiserver
> database export
> ```
> 
> That is way less dumb.
> 
> Still not magic. But now it helps instead of creating another job.

### User
> what about workflows

### Assistant
> Workflows are the missing layer between “metadata exists” and “Cody doesn’t have to babysit every import.” They should handle routing, review flags, and pipeline handoff — not try to replace careful matching rules.

### Assistant
> Yes — **workflows are the piece we should use**, but not as a replacement for matching rules.
> 
> Think of it like this:
> 
> ```text
> Matching rules = identify what the document probably is
> Workflows = take action after identification
> ```
> 
> Paperless workflows can assign title, tags, correspondent, document type, storage path, owner, permissions, and custom fields. They can also trigger from events/filters, so this is exactly where we make Paperless reduce work instead of creating another inbox monster. citeturn776019search2
> 
> ## What workflows should do for you
> 
> For your setup, workflows should handle five jobs:
> 
> 1. **Default triage**
>    Every new document gets:
>    `status:review-needed`, `pipeline:pending-sync`, and `bucket:20_qinexus/00_inbox`.
> 
> 2. **Domain routing**
>    If Paperless detects legal/finance/care/tech/tax/etc., workflow assigns the correct bucket tag and storage path.
> 
> 3. **Review queues**
>    If confidence is unclear, it stays in Pending Review instead of being misfiled.
> 
> 4. **Sync preparation**
>    Add `pipeline:pending-sync` so the future Paperless sync worker knows what to pick up.
> 
> 5. **Human cleanup loop**
>    After you review a doc, workflow/status can move from `status:review-needed` to `status:processed`.
> 
> ## Matching rules vs workflows
> 
> Here’s the split:
> 
> | Layer | Purpose | Example |
> |---|---|---|
> | Document type rules | Identify what it is | Statement, Bill, Legal Filing |
> | Correspondent rules | Identify who sent it | Chase, IRS, Court / Clerk |
> | Tag rules | Add domains/status/source | `domain:finance`, `status:urgent` |
> | Storage path rules | Suggest shelf | `60 Finance - Statements` |
> | Workflows | Apply bundles of actions | assign tags + path + custom fields |
> 
> So yes, workflows are where we make this actually useful.
> 
> ## Workflow set we should create
> 
> ### Workflow 01 — New Document Intake Default
> 
> Trigger:
> 
> ```text
> Document added
> ```
> 
> Actions:
> 
> ```text
> Add tag: status:review-needed
> Add tag: pipeline:pending-sync
> Add tag: bucket:20_qinexus/00_inbox
> Set storage path: 00 Inbox - Pending Review
> Set custom field Qi Sync Status: pending
> Set custom field Qi Review Status: needs_review
> Set custom field Qi Source System: paperless
> ```
> 
> This is the safety net. Nothing should enter Paperless naked.
> 
> ---
> 
> ### Workflow 02 — Finance Routing
> 
> Trigger filter should look for finance tags/document types, such as:
> 
> ```text
> Document type is Bill OR Receipt OR Statement OR Tax Document
> OR tag is domain:finance
> OR tag is domain:tax
> ```
> 
> Actions:
> 
> ```text
> Add tag: bucket:20_qinexus/60_finance
> Set custom field Qi Domain: finance
> Set custom field Qi Bucket: 20_qinexus/60_finance
> ```
> 
> Then sub-routing:
> 
> - Statement → `60 Finance - Statements`
> - Bill → `60 Finance - Bills`
> - Tax Document → `60 Finance - Tax`
> - Receipt → probably `60 Finance - Bills` or leave pending until we make a receipt-specific path
> 
> We should probably add:
> 
> ```text
> 60 Finance - Receipts
> 20_qinexus/60_finance/25_receipts/{{ created_year }}/{{ correspondent }}/{{ title }}
> ```
> 
> Because receipts are going to be high-volume. I’d add that. Otherwise bills and receipts get weirdly mashed together.
> 
> ---
> 
> ### Workflow 03 — Legal Routing
> 
> Trigger:
> 
> ```text
> Document type is Legal Filing OR Court Notice
> OR tag is domain:legal
> ```
> 
> Actions:
> 
> ```text
> Add tag: bucket:20_qinexus/70_legal
> Set custom field Qi Domain: legal
> Set custom field Qi Bucket: 20_qinexus/70_legal
> ```
> 
> Sub-routing:
> 
> - Legal Filing → `70 Legal - Filings`
> - Court Notice → `70 Legal - Filings` or `70 Legal - Matters`
> - Evidence-tagged docs → `70 Legal - Evidence`
> - Exhibit-tagged docs → `70 Legal - Exhibits`
> 
> This matters because legal docs need traceability, not vibes.
> 
> ---
> 
> ### Workflow 04 — Care / Medical Routing
> 
> Trigger:
> 
> ```text
> Document type is Care Document OR Medical Record
> OR tag is domain:care
> OR tag is domain:medical
> ```
> 
> Actions:
> 
> ```text
> Add tag: bucket:20_qinexus/40_people
> Set custom field Qi Domain: care
> Set custom field Qi Bucket: 20_qinexus/40_people/30_care_coordination
> ```
> 
> Sub-routing:
> 
> - Care Document → `40 People - Care Coordination`
> - Medical Record → I’d keep it in People/Care Coordination unless you want a separate medical storage path.
> 
> Honestly, for your system, **care docs should not scatter into Life and People randomly**. Care coordination is people-centered. Put most of it in:
> 
> ```text
> 20_qinexus/40_people/30_care_coordination
> ```
> 
> Medical reference docs can go to Reference later.
> 
> ---
> 
> ### Workflow 05 — Tech Routing
> 
> Trigger:
> 
> ```text
> Document type is Technical Document OR System Log OR Manifest
> OR tag is domain:tech
> ```
> 
> Actions:
> 
> ```text
> Add tag: bucket:20_qinexus/80_tech
> Set custom field Qi Domain: tech
> Set custom field Qi Bucket: 20_qinexus/80_tech
> ```
> 
> Sub-routing:
> 
> - qiserver docs → `80 Tech - Qiserver`
> - app docs → `80 Tech - Apps`
> - logs/data exports → maybe `100_data`, not `80_tech`
> 
> ---
> 
> ### Workflow 06 — Data / Export Routing
> 
> Trigger:
> 
> ```text
> Document type is Database Export OR System Log OR Manifest
> OR tag is domain:data
> ```
> 
> Actions:
> 
> ```text
> Add tag: bucket:20_qinexus/100_data
> Set custom field Qi Domain: data
> Set custom field Qi Bucket: 20_qinexus/100_data
> ```
> 
> Routes:
> 
> - CSV → `100 Data - CSV`
> - JSON → `100 Data - JSON`
> - Database Export → `100 Data - Database Exports`
> - Logs → `100 Data - Logs`
> 
> But be careful: operational logs generated by your system later belong in `40_system`. Imported source logs can live in `20_qinexus/100_data/40_logs`.
> 
> ---
> 
> ### Workflow 07 — QiArchive Sync Prep
> 
> Trigger:
> 
> ```text
> Document added OR document updated
> ```
> 
> Filters:
> 
> ```text
> Has tag pipeline:pending-sync
> ```
> 
> Actions:
> 
> ```text
> Add custom field QiArchive Status: pending
> Add tag pipeline:qiarchive
> ```
> 
> Later the worker changes:
> 
> ```text
> pipeline:pending-sync → status:synced
> QiArchive Status: synced
> QiArchive Source ID: QA...
> Qdrant Collection: ...
> Neo4j Node ID: ...
> ```
> 
> This is the bridge to tables/vector/graph.
> 
> ## Should we script workflows too?
> 
> Yes, but carefully.
> 
> Paperless has workflow models in Django, but they’re a little more complex than tags/storage paths because workflows have triggers and actions. The docs say workflow assignment actions can assign title, tags, correspondent, document type, storage path, owner, permissions, and custom fields. citeturn776019search2
> 
> Before I give you a script that writes workflow objects directly, we need to inspect the model fields in your installed Paperless version, because you’re on Paperless `v2.20.15` and I don’t want to guess field names. Guessing here is how we summon the metadata goblin again.
> 
> Run this:
> 
> ```bash
> sudo docker exec -it paperless bash -lc 'python manage.py shell -c "
> from django.apps import apps
> 
> for model_name in [\"Workflow\", \"WorkflowTrigger\", \"WorkflowAction\"]:
>     try:
>         model = apps.get_model(\"documents\", model_name)
>         print(\"\\n\", model_name)
>         for f in model._meta.fields:
>             print(f.name, f.__class__.__name__, getattr(f, \"choices\", None))
>     except Exception as e:
>         print(model_name, \"ERROR\", e)
> "'
> ```
> 
> Also run:
> 
> ```bash
> sudo docker exec -it paperless bash -lc 'python manage.py shell -c "
> from django.apps import apps
> for m in apps.get_app_config(\"documents\").get_models():
>     if \"Workflow\" in m.__name__:
>         print(m.__name__)
> "'
> ```
> 
> ## My recommendation
> 
> Do this in order:
> 
> 1. Finish v3 matching rules.
> 2. Add one missing storage path: `60 Finance - Receipts`.
> 3. Inspect workflow model fields.
> 4. Script workflows.
> 5. Ingest a small mixed test batch.
> 6. Use Paperless saved views for review queues.
> 
> ## Saved views we should create too
> 
> These are not optional. These are how you avoid “where did it go?”
> 
> Create saved views:
> 
> ```text
> Inbox - Needs Review
> Finance - Needs Review
> Legal - Needs Review
> Care - Needs Review
> Tech - Needs Review
> Pipeline - Pending Sync
> Pipeline - Synced
> Possible Duplicates
> Urgent / Deadlines
> ```
> 
> This gives you dashboards instead of doom scrolling.
> 
> ## Bottom line
> 
> Yes, workflows matter. The final architecture should be:
> 
> ```text
> Match rules identify
> Workflows route
> Saved views review
> Sync worker exports
> Qdrant retrieves
> Neo4j relates
> QiAccess displays
> ```
> 
> That’s the complete machine. Matching alone is not enough. Workflows are the “do something useful with the match” layer.

### User
> also you know im about to ingest a shit tone of medical records for my mom, also how do we automate this, do i really need to drop the files in, it would be nice if somethign woudl just watch my folders on my pc and ingest all new file formats that paperless can ingest and it automatically updates changes to files or something somehow.

### Assistant
> Yes — for Mom’s medical records, we need a separate intake lane with stronger privacy, review, and naming rules. And no, you should not have to manually drop files forever; we can automate folder watching from your Windows PC into Paperless.

### Assistant
> Yes. For **Mom’s medical records**, we need a stronger design than “drop random files into consume and hope Paperless behaves.” That is not a system. That is a Roomba in a paperwork hurricane.
> 
> ## First: supported file types
> 
> Paperless can ingest PDFs, PNG, JPEG, TIFF, GIF, WebP, and plain text. Office files like `.docx`, `.xlsx`, `.pptx`, `.odt`, etc. require Tika + Gotenberg to be enabled. citeturn168151search1turn168151search11
> 
> So for medical records, the best source formats are:
> 
> ```text
> PDF
> PNG
> JPG/JPEG
> TIFF
> WEBP
> TXT
> ```
> 
> If MyChart or portals give you PDFs, perfect. If they give you Office docs or emails, we add Tika/Gotenberg later.
> 
> ## No, you should not manually drop files forever
> 
> The clean automation options are:
> 
> ### Option A — Syncthing from your Windows PC to qiserver
> 
> This is my top recommendation.
> 
> Flow:
> 
> ```text
> Windows watched folders
> → Syncthing
> → qiserver intake folders
> → Paperless consume
> → Paperless OCR/classification
> → Paperless sync worker
> → SQL/Qdrant/Neo4j/QiArchive
> ```
> 
> Syncthing is built for continuous file sync between computers, and it avoids relying on Google Drive streaming weirdness. citeturn168151search27turn168151search19
> 
> Use this when you want:
> 
> - automatic LAN/tailnet sync
> - local-first behavior
> - less cloud weirdness
> - predictable ingestion
> 
> ### Option B — Google Drive watched folder with rclone
> 
> Possible, but I do **not** love it for initial ingestion.
> 
> Flow:
> 
> ```text
> Google Drive folder
> → rclone sync/mount on qiserver
> → Paperless consume
> ```
> 
> Problem: mounted cloud folders can behave weirdly with Paperless watchers, and consumed files may be moved/deleted depending on setup. People do it, but it has more sharp edges. Paperless troubleshooting specifically says to ensure files are placed in the watched consume folder configured in Docker. citeturn168151search15
> 
> ### Option C — API uploader script from Windows
> 
> Also good.
> 
> Flow:
> 
> ```text
> Windows watcher script
> → Paperless API /api/documents/post_document/
> → Paperless consumes document
> ```
> 
> Paperless supports posting documents directly to `/api/documents/post_document/`. citeturn168151search2
> 
> This is clean because it can:
> 
> - preserve original file location
> - avoid deleting files from your PC
> - attach tags/correspondent/document type at upload time
> - keep logs
> - avoid network share weirdness
> 
> But it requires a script/service on Windows.
> 
> ## My recommendation
> 
> Use **Syncthing for v1**, then add an API uploader later if needed.
> 
> Why? Because you already think in folders, you have a lot of files, and we need something robust fast.
> 
> ## The folder design
> 
> On your Windows PC, create one intake root:
> 
> ```text
> C:\QiPaperless_Inbox
> ```
> 
> Inside:
> 
> ```text
> C:\QiPaperless_Inbox
>   00_pending_review
>   10_mom_medical_records
>   20_mom_care_docs
>   30_finance
>   40_legal
>   50_tech
>   90_holding_unsupported
> ```
> 
> On qiserver:
> 
> ```text
> /srv/qios/intake/paperless
>   00_pending_review
>   10_mom_medical_records
>   20_mom_care_docs
>   30_finance
>   40_legal
>   50_tech
>   90_holding_unsupported
> ```
> 
> Then we use a small ingest mover script on qiserver:
> 
> ```text
> /srv/qios/intake/paperless/10_mom_medical_records
> → /srv/qios/data/paperless/consume/10_mom_medical_records
> ```
> 
> ## Important Paperless setting: subfolders as tags
> 
> Paperless has a setting called `PAPERLESS_CONSUMER_SUBDIRS_AS_TAGS`. That lets Paperless use consume subfolders as tags. This is exactly useful for lanes like:
> 
> ```text
> 10_mom_medical_records
> 20_mom_care_docs
> 30_finance
> 40_legal
> ```
> 
> So a file dropped into:
> 
> ```text
> consume/10_mom_medical_records/file.pdf
> ```
> 
> can get a tag from the folder lane. citeturn168151search24
> 
> I would use this, but carefully. Folder tags should be **intake lane tags**, not final truth.
> 
> Example tags:
> 
> ```text
> intake:mom_medical_records
> intake:mom_care_docs
> intake:finance
> intake:legal
> ```
> 
> Not messy tags like `mom`, `doctor`, `stuff`.
> 
> ## Medical records taxonomy
> 
> For Mom’s medical records, add these document types:
> 
> ```text
> Medical Record
> Visit Summary
> After Visit Summary
> Lab Result
> Imaging Report
> Medication List
> Discharge Paperwork
> Referral
> Care Plan
> Insurance EOB
> Prior Authorization
> Appointment Notice
> Provider Message
> Patient Instructions
> Medical Bill
> ```
> 
> Add tags:
> 
> ```text
> domain:medical
> domain:care
> person:mom
> bucket:20_qinexus/40_people
> care:medical-record
> care:visit-summary
> care:lab-result
> care:medication
> care:insurance
> care:provider-message
> care:appointment
> status:review-needed
> privacy:sensitive
> pipeline:pending-sync
> ```
> 
> Storage path:
> 
> ```text
> 20_qinexus/40_people/30_care_coordination/medical_records/{{ created_year }}/{{ document_type }}/{{ correspondent }}/{{ title }}
> ```
> 
> For labs:
> 
> ```text
> 20_qinexus/40_people/30_care_coordination/medical_records/{{ created_year }}/labs/{{ title }}
> ```
> 
> For medication lists:
> 
> ```text
> 20_qinexus/40_people/30_care_coordination/medical_records/{{ created_year }}/medications/{{ title }}
> ```
> 
> For EOB/insurance:
> 
> ```text
> 20_qinexus/40_people/30_care_coordination/insurance/{{ created_year }}/{{ title }}
> ```
> 
> ## Should Paperless “update changes to files”?
> 
> Careful. Paperless is an **archive system**, not a live file sync editor.
> 
> The safe doctrine:
> 
> ```text
> New file → ingest
> Changed source file → ingest as new version/copy or flag duplicate
> Original source remains untouched
> Paperless archive becomes searchable record
> ```
> 
> Do **not** expect Paperless to live-update a document every time you edit a file on Windows. That’s not how you want medical/legal records handled anyway.
> 
> For medical records especially, immutable is better:
> 
> ```text
> Downloaded record from portal on 2026-05-15 = source artifact
> Later corrected record = new source artifact
> Both traceable
> ```
> 
> No silent overwrites. Silent overwrites are how future-you gets betrayed by past-you.
> 
> ## Automation architecture
> 
> Use this:
> 
> ```text
> Windows folder watcher / Syncthing
> → qiserver intake folder
> → qiserver filter script
> → Paperless consume folder
> → Paperless workflows assign tags/path/custom fields
> → Paperless sync worker exports metadata/text
> → QiArchive/Qdrant/Neo4j
> ```
> 
> The qiserver filter script should:
> 
> 1. detect supported file types
> 2. ignore temp/partial files
> 3. wait until file size is stable
> 4. copy to Paperless consume lane
> 5. log the import
> 6. move unsupported files to holding
> 7. never delete source unless explicitly configured
> 
> ## Commands to create qiserver intake lanes
> 
> Run:
> 
> ```bash
> sudo mkdir -p /srv/qios/intake/paperless/{00_pending_review,10_mom_medical_records,20_mom_care_docs,30_finance,40_legal,50_tech,90_holding_unsupported}
> sudo mkdir -p /srv/qios/data/paperless/consume/{00_pending_review,10_mom_medical_records,20_mom_care_docs,30_finance,40_legal,50_tech}
> sudo chown -R qiadmin:qiadmin /srv/qios/intake/paperless
> sudo chown -R qiadmin:qiadmin /srv/qios/data/paperless/consume
> sudo chmod -R 775 /srv/qios/intake/paperless /srv/qios/data/paperless/consume
> ```
> 
> Then check whether subdir tags are enabled:
> 
> ```bash
> sudo docker inspect paperless --format '{{range .Config.Env}}{{println .}}{{end}}' | sort | grep PAPERLESS_CONSUMER
> ```
> 
> If `PAPERLESS_CONSUMER_SUBDIRS_AS_TAGS` is missing, we should add it to compose:
> 
> ```yaml
> PAPERLESS_CONSUMER_SUBDIRS_AS_TAGS: true
> ```
> 
> Then restart Paperless through compose.
> 
> ## But here’s the real answer
> 
> For your situation, I’d build three lanes:
> 
> ### Lane 1 — Medical controlled ingest
> 
> ```text
> 10_mom_medical_records
> ```
> 
> High privacy. Always review. Never auto-finalize.
> 
> ### Lane 2 — General docs
> 
> ```text
> 00_pending_review
> 30_finance
> 40_legal
> 50_tech
> ```
> 
> Can be semi-automated.
> 
> ### Lane 3 — Bulk backlog
> 
> ```text
> bulk_backlog_batch_001
> bulk_backlog_batch_002
> bulk_backlog_batch_003
> ```
> 
> Do not dump everything into one folder. Batch it. Otherwise you’ll create a searchable landfill.
> 
> ## Final call
> 
> Yes, automate it.
> 
> But for Mom’s medical records:
> 
> ```text
> auto-ingest = yes
> auto-delete source = no
> auto-finalize metadata = no
> auto-review queue = yes
> auto-sync to QiArchive = only after reviewed or privacy-approved
> ```
> 
> That gives you speed without making a medical-records confetti cannon.

### User
> This created/upserted taxonomy + conservative matching rules.
> Next: ingest 10-25 mixed test documents, inspect bad matches, tighten rules.
> qiadmin@qiserver:~$ sudo mkdir -p /srv/qios/intake/paperless/{00_pending_review,10_mom_medical_records,20_mom_care_docs,30_finance,40_legal,50_tech,90_holding_unsupported}
> 
> sudo mkdir -p /srv/qios/data/paperless/consume/{00_pending_review,10_mom_medical_records,20_mom_care_docs,30_finance,40_legal,50_tech}
> 
> sudo chown -R qiadmin:qiadmin /srv/qios/intake/paperless
> 
> sudo chown -R qiadmin:qiadmin /srv/qios/data/paperless/consume
> 
> sudo chmod -R 775 /srv/qios/intake/paperless /srv/qios/data/paperless/consumeqiadmin@qiserver:~$ 
> qiadmin@qiserver:~$ sudo docker inspect paperless --format '{{range .Config.Env}}{{println .}}{{end}}' | sort | grep PAPERLESS_CONSUMER
> PAPERLESS_CONSUMER_POLLING=30
> qiadmin@qiserver:~$

### Assistant
> Good. Intake folders exist. Paperless is polling every 30 seconds, but this confirms subfolder tagging is **not enabled yet**:
> 
> ```text
> PAPERLESS_CONSUMER_POLLING=30
> ```
> 
> So right now Paperless will watch the consume folder, but it will **not automatically turn subfolders into tags** unless we add:
> 
> ```text
> PAPERLESS_CONSUMER_SUBDIRS_AS_TAGS=true
> ```
> 
> ## Next: update Paperless compose
> 
> First open the compose file:
> 
> ```bash
> sudo nano /srv/qios/stacks/paperless/docker-compose.yml
> ```
> 
> Find the `paperless:` service and its `environment:` block.
> 
> Add this under the existing Paperless environment variables:
> 
> ```yaml
> PAPERLESS_CONSUMER_SUBDIRS_AS_TAGS: true
> ```
> 
> Also, if there is no explicit polling line in compose, add this too so the config is documented:
> 
> ```yaml
> PAPERLESS_CONSUMER_POLLING: 30
> ```
> 
> So that section should look roughly like:
> 
> ```yaml
> environment:
>   PAPERLESS_REDIS: redis://paperless-broker:6379
>   PAPERLESS_DBHOST: paperless-db
>   PAPERLESS_CONSUMER_POLLING: 30
>   PAPERLESS_CONSUMER_SUBDIRS_AS_TAGS: true
> ```
> 
> Do **not** copy that whole block blindly. Add only the missing lines into your existing environment block.
> 
> ## Restart Paperless through compose
> 
> ```bash
> cd /srv/qios/stacks/paperless
> sudo docker compose up -d
> ```
> 
> Then verify:
> 
> ```bash
> sudo docker inspect paperless --format '{{range .Config.Env}}{{println .}}{{end}}' | sort | grep PAPERLESS_CONSUMER
> ```
> 
> We want to see:
> 
> ```text
> PAPERLESS_CONSUMER_POLLING=30
> PAPERLESS_CONSUMER_SUBDIRS_AS_TAGS=true
> ```
> 
> ## Then create matching intake tags
> 
> Because folder names will become tags, create tags that match the folder lanes. Paperless may create them automatically, but I’d rather control the naming cleanly.
> 
> Run:
> 
> ```bash
> cat > /tmp/seed_paperless_intake_tags.py <<'PY'
> from documents.models import Tag
> 
> tags = [
>     "00_pending_review",
>     "10_mom_medical_records",
>     "20_mom_care_docs",
>     "30_finance",
>     "40_legal",
>     "50_tech",
> ]
> 
> for name in tags:
>     obj, created = Tag.objects.get_or_create(name=name)
>     print(("CREATED" if created else "EXISTS"), name)
> 
> print("DONE: intake lane tags ready.")
> PY
> 
> sudo docker cp /tmp/seed_paperless_intake_tags.py paperless:/tmp/seed_paperless_intake_tags.py
> sudo docker exec -it paperless bash -lc 'python manage.py shell < /tmp/seed_paperless_intake_tags.py'
> ```
> 
> ## Then test with a lane
> 
> Create a small test file:
> 
> ```bash
> echo "QiAccess Paperless test for mom medical records $(date)" > /tmp/mom_medical_test.txt
> cp /tmp/mom_medical_test.txt /srv/qios/data/paperless/consume/10_mom_medical_records/
> ```
> 
> Watch:
> 
> ```bash
> sudo docker logs -f paperless
> ```
> 
> If `.txt` gets rejected, use a PDF. The important test is whether the imported document gets the `10_mom_medical_records` tag.
> 
> ## One important correction
> 
> For Mom’s medical records, the folder tag should be treated as an **intake lane**, not final classification.
> 
> So this:
> 
> ```text
> 10_mom_medical_records
> ```
> 
> means:
> 
> ```text
> This arrived through the Mom medical record lane.
> ```
> 
> It does **not** replace:
> 
> ```text
> domain:medical
> domain:care
> person:mom
> privacy:sensitive
> status:review-needed
> bucket:20_qinexus/40_people
> ```
> 
> We still need workflows to add those. Subfolder tagging gets the document into the right “lane”; workflows make it useful.

### User
> CREATED StoragePath 70 Legal - Evidence
> CREATED StoragePath 70 Legal - Timelines
> CREATED StoragePath 70 Legal - Motions Drafts
> CREATED StoragePath 70 Legal - Research
> CREATED StoragePath 70 Legal - Regulatory Complaints
> CREATED StoragePath 70 Legal - Exhibits
> CREATED StoragePath 80 Tech - Qiserver
> CREATED StoragePath 80 Tech - Apps
> CREATED StoragePath 80 Tech - Repos
> CREATED StoragePath 80 Tech - Scripts
> CREATED StoragePath 80 Tech - Deployments
> CREATED StoragePath 80 Tech - Tooling
> CREATED StoragePath 80 Tech - Dev Runbooks
> CREATED StoragePath 100 Data - CSV
> CREATED StoragePath 100 Data - JSON
> CREATED StoragePath 100 Data - Database Exports
> CREATED StoragePath 100 Data - Logs
> CREATED StoragePath 100 Data - Datasets
> CREATED StoragePath 100 Data - Source Tables
> CREATED StoragePath 110 Reference - Articles
> CREATED StoragePath 110 Reference - Research
> CREATED StoragePath 110 Reference - Legal References
> CREATED StoragePath 110 Reference - Technical Guides
> CREATED StoragePath 110 Reference - Examples
> CREATED StoragePath 110 Reference - Citations
> CREATED StoragePath 110 Reference - External Docs
> CREATED StoragePath 120 Archive - Historical Files
> CREATED StoragePath 120 Archive - Frozen Exports
> CREATED StoragePath 120 Archive - Superseded Material
> CREATED StoragePath 130 System - Folder Manifest
> CREATED StoragePath 130 System - Sync Notes
> CREATED StoragePath 130 System - Structure Docs
> UPDATED CustomField Qi Domain
> CREATED CustomField Qi Bucket
> UPDATED CustomField Qi Source System
> UPDATED CustomField Qi Sync Status
> UPDATED CustomField Qi External ID
> UPDATED CustomField Qi Matter ID
> UPDATED CustomField Qi Account ID
> UPDATED CustomField Qi Event Date
> UPDATED CustomField Qi Review Status
> UPDATED CustomField Qi Notes
> CREATED CustomField QiArchive Status
> CREATED CustomField QiArchive Source ID
> CREATED CustomField Qdrant Collection
> CREATED CustomField Neo4j Node ID
> DONE: QiOS/Paperless v3 rules seed complete.
> This created/upserted taxonomy + conservative matching rules.
> Next: ingest 10-25 mixed test documents, inspect bad matches, tighten rules.
> qiadmin@qiserver:~$ sudo mkdir -p /srv/qios/intake/paperless/{00_pending_review,10_mom_medical_records,20_mom_care_docs,30_finance,40_legal,50_tech,90_holding_unsupported}
> 
> sudo mkdir -p /srv/qios/data/paperless/consume/{00_pending_review,10_mom_medical_records,20_mom_care_docs,30_finance,40_legal,50_tech}
> 
> sudo chown -R qiadmin:qiadmin /srv/qios/intake/paperless
> 
> sudo chown -R qiadmin:qiadmin /srv/qios/data/paperless/consume
> 
> sudo chmod -R 775 /srv/qios/intake/paperless /srv/qios/data/paperless/consumeqiadmin@qiserver:~$ 
> qiadmin@qiserver:~$ sudo docker inspect paperless --format '{{range .Config.Env}}{{println .}}{{end}}' | sort | grep PAPERLESS_CONSUMER
> PAPERLESS_CONSUMER_POLLING=30
> qiadmin@qiserver:~$ sudo nano /srv/qios/stacks/paperless/docker-compose.yml
> qiadmin@qiserver:~$ cd /srv/qios/stacks/paperless
> qiadmin@qiserver:/srv/qios/stacks/paperless$ sudo docker compose up -d
> [+] up 3/3
>  ✔ Container paperless-redis    Running                                                                                                                             0.0s
>  ✔ Container paperless-postgres Running                                                                                                                             0.0s
>  ✔ Container paperless          Started                                                                                                                             8.0s
> qiadmin@qiserver:/srv/qios/stacks/paperless$ sudo docker inspect paperless --format '{{range .Config.Env}}{{println .}}{{end}}' | sort | grep PAPERLESS_CONSUMER
> PAPERLESS_CONSUMER_POLLING=30
> PAPERLESS_CONSUMER_SUBDIRS_AS_TAGS=true
> qiadmin@qiserver:/srv/qios/stacks/paperless$ cat > /tmp/seed_paperless_intake_tags.py <<'PY'
> > 
> > from documents.models import Tag
> > 
> > 
> > 
> > tags = [
> > 
> >     "00_pending_review",
> > 
> >     "10_mom_medical_records",
> > 
> >     "20_mom_care_docs",
> > 
> >     "30_finance",
> > 
> >     "40_legal",
> > 
> >     "50_tech",
> > 
> > ]
> > 
> > 
> > 
> > for name in tags:
> > 
> >     obj, created = Tag.objects.get_or_create(name=name)
> > 
> >     print(("CREATED" if created else "EXISTS"), name)
> > 
> > 
> > 
> > print("DONE: intake lane tags ready.")
> > 
> > PY
> qiadmin@qiserver:/srv/qios/stacks/paperless$ 
> qiadmin@qiserver:/srv/qios/stacks/paperless$ 
> qiadmin@qiserver:/srv/qios/stacks/paperless$ 
> qiadmin@qiserver:/srv/qios/stacks/paperless$ sudo docker cp /tmp/seed_paperless_intake_tags.py paperless:/tmp/seed_paperless_intake_tags.py
> 
> sudo docker exec -it paperless bash -lc 'python manage.py shell < /tmp/seed_paperless_intake_tags.py'Successfully copied 359B (transferred 2.05kB) to paperless:/tmp/seed_paperless_intake_tags.py
> qiadmin@qiserver:/srv/qios/stacks/paperless$ 
> qiadmin@qiserver:/srv/qios/stacks/paperless$ echo "QiAccess Paperless test for mom medical records $(date)" > /tmp/mom_medical_test.txt
> qiadmin@qiserver:/srv/qios/stacks/paperless$ 
> qiadmin@qiserver:/srv/qios/stacks/paperless$ cp /tmp/mom_medical_test.txt /srv/qios/data/paperless/consume/10_mom_medical_records/
> cp: cannot create regular file '/srv/qios/data/paperless/consume/10_mom_medical_records/': Not a directory
> qiadmin@qiserver:/srv/qios/stacks/paperless$

### Assistant
> Yep — tiny snag, not a disaster.
> 
> This error:
> 
> ```text
> cp: cannot create regular file '/srv/qios/data/paperless/consume/10_mom_medical_records/': Not a directory
> ```
> 
> means one of two things:
> 
> 1. `10_mom_medical_records` was never created as a folder, **or**
> 2. something created it as a **file** instead of a directory.
> 
> Also I notice your earlier pasted command ended like this:
> 
> ```text
> sudo chmod -R 775 /srv/qios/intake/paperless /srv/qios/data/paperless/consumeqiadmin@qiserver:~$
> ```
> 
> That smells like the terminal/paste mashed the prompt onto the command. So let’s inspect and fix cleanly.
> 
> ## Run this
> 
> ```bash
> ls -lah /srv/qios/data/paperless/consume
> file /srv/qios/data/paperless/consume/10_mom_medical_records || true
> ```
> 
> ## Then repair the consume lane folders
> 
> This is safe. It only removes `10_mom_medical_records` **if it is a file**, not if it is a directory.
> 
> ```bash
> if [ -f /srv/qios/data/paperless/consume/10_mom_medical_records ]; then
>   rm /srv/qios/data/paperless/consume/10_mom_medical_records
> fi
> 
> sudo mkdir -p /srv/qios/data/paperless/consume/00_pending_review
> sudo mkdir -p /srv/qios/data/paperless/consume/10_mom_medical_records
> sudo mkdir -p /srv/qios/data/paperless/consume/20_mom_care_docs
> sudo mkdir -p /srv/qios/data/paperless/consume/30_finance
> sudo mkdir -p /srv/qios/data/paperless/consume/40_legal
> sudo mkdir -p /srv/qios/data/paperless/consume/50_tech
> 
> sudo chown -R qiadmin:qiadmin /srv/qios/data/paperless/consume
> sudo chmod -R 775 /srv/qios/data/paperless/consume
> 
> ls -lah /srv/qios/data/paperless/consume
> ```
> 
> ## Also rerun the intake tag seed without `-it`
> 
> Your previous `docker exec -it` didn’t show output. It may have run, but let’s make it boring and visible:
> 
> ```bash
> sudo docker exec paperless bash -lc 'python manage.py shell < /tmp/seed_paperless_intake_tags.py'
> ```
> 
> You should see:
> 
> ```text
> CREATED 10_mom_medical_records
> ```
> 
> or:
> 
> ```text
> EXISTS 10_mom_medical_records
> ```
> 
> ## Now test again
> 
> Important: `.txt` may or may not be accepted depending on Paperless config. Try it anyway because it’s fast:
> 
> ```bash
> echo "QiAccess Paperless test for mom medical records $(date)" > /tmp/mom_medical_test.txt
> cp /tmp/mom_medical_test.txt /srv/qios/data/paperless/consume/10_mom_medical_records/
> ls -lah /srv/qios/data/paperless/consume/10_mom_medical_records/
> ```
> 
> Watch logs:
> 
> ```bash
> sudo docker logs -f paperless
> ```
> 
> If Paperless rejects `.txt`, we’ll test with a PDF. The main thing we just fixed is the missing/bad subfolder. Since `PAPERLESS_CONSUMER_SUBDIRS_AS_TAGS=true` is now confirmed, that lane should tag imports from `10_mom_medical_records` once the folder exists correctly.

### User
> looks like it worked, now what.

### Assistant
> Beautiful. Now we move from “Paperless is configured” to **“Paperless is useful.”**
> 
> ## Current state
> 
> You now have:
> 
> - Paperless running
> - QiNexus-aligned storage paths
> - conservative matching rules
> - intake folders
> - subfolder tagging enabled
> - Mom medical intake lane working
> - pipeline-ready custom fields
> 
> That means the next job is **calibration**, not bulk ingest yet.
> 
> Your current map says QiNexus is the human source terrain and QiArchive is the AI memory pipeline, so we are correctly using Paperless as source-document intake first — not as the final AI brain. fileciteturn3file0
> 
> ## Next 5 moves
> 
> ### 1. Verify the test doc in Paperless UI
> 
> Open the test document and check:
> 
> - Did it get tag `10_mom_medical_records`?
> - Did it get `domain:medical` or `domain:care`?
> - Did it get `bucket:20_qinexus/40_people`?
> - Did it get `status:review-needed`?
> - Did it get the right document type?
> - Did it get the right storage path?
> 
> If it only got the folder tag, that’s fine. That means the intake lane works; workflows are next.
> 
> ---
> 
> ### 2. Inspect workflow model fields
> 
> Before scripting workflows, we need to inspect your exact Paperless version’s workflow models.
> 
> Run:
> 
> ```bash
> sudo docker exec paperless bash -lc 'python manage.py shell -c "
> from django.apps import apps
> 
> for model_name in [\"Workflow\", \"WorkflowTrigger\", \"WorkflowAction\"]:
>     try:
>         model = apps.get_model(\"documents\", model_name)
>         print(\"\\n\" + model_name)
>         for f in model._meta.fields:
>             print(f.name, f.__class__.__name__, getattr(f, \"choices\", None))
>     except Exception as e:
>         print(model_name, \"ERROR\", e)
> "'
> ```
> 
> Then:
> 
> ```bash
> sudo docker exec paperless bash -lc 'python manage.py shell -c "
> from django.apps import apps
> for m in apps.get_app_config(\"documents\").get_models():
>     if \"Workflow\" in m.__name__:
>         print(m.__name__)
> "'
> ```
> 
> Send me that output. Then we can script workflows without guessing. No metadata goblin today.
> 
> ---
> 
> ### 3. Add the missing medical-specific taxonomy
> 
> We need a medical/care v4 seed because Mom’s records are not generic “Medical Record.” That’s too blunt.
> 
> We need document types like:
> 
> ```text
> Visit Summary
> After Visit Summary
> Lab Result
> Imaging Report
> Medication List
> Discharge Paperwork
> Referral
> Care Plan
> Insurance EOB
> Prior Authorization
> Appointment Notice
> Provider Message
> Patient Instructions
> Medical Bill
> ```
> 
> And tags like:
> 
> ```text
> person:mom
> privacy:sensitive
> care:visit-summary
> care:lab-result
> care:imaging
> care:medication
> care:insurance
> care:appointment
> care:provider-message
> care:needs-review
> ```
> 
> This matters because medical records need retrieval by **type**, **date**, **provider**, and **purpose** later.
> 
> ---
> 
> ### 4. Create workflows
> 
> We want workflows for:
> 
> ```text
> 01 Intake Default
> 02 Mom Medical Intake
> 03 Mom Care Docs
> 04 Finance Routing
> 05 Legal Routing
> 06 Tech Routing
> 07 QiArchive Pending Sync
> ```
> 
> The big one right now is:
> 
> ```text
> 02 Mom Medical Intake
> ```
> 
> It should trigger when a document has tag:
> 
> ```text
> 10_mom_medical_records
> ```
> 
> Then assign:
> 
> ```text
> person:mom
> privacy:sensitive
> domain:medical
> domain:care
> bucket:20_qinexus/40_people
> status:review-needed
> pipeline:pending-sync
> Qi Domain = care/medical
> Qi Bucket = 20_qinexus/40_people/30_care_coordination
> Qi Review Status = needs_review
> Qi Sync Status = pending
> ```
> 
> Storage path:
> 
> ```text
> 20_qinexus/40_people/30_care_coordination/medical_records/{{ created_year }}/{{ document_type }}/{{ correspondent }}/{{ title }}
> ```
> 
> ---
> 
> ### 5. Start calibration batch
> 
> Do not bulk ingest yet. Do a **Mom medical test batch** first:
> 
> ```text
> 10–25 files max
> ```
> 
> Use a mix:
> 
> - visit summary
> - lab result
> - insurance/EOB
> - provider message
> - appointment notice
> - medication list
> - random scan/photo
> 
> Then review what Paperless did wrong. We tighten rules from real failures.
> 
> ## The next command I need from you
> 
> Run the workflow model inspection commands above.
> 
> Once I see the workflow fields, I’ll give you the exact workflow seed script. Then we can stop manually babysitting every import and turn this into an actual intake machine.
