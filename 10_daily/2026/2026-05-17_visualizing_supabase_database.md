---
layout: page
title: "Visualizing Supabase Database"
slug: "visualizing_supabase_database"
created_at: "2026-05-17 13:51:05"
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
uid: "6a0a0e13-df58-83ea-a1f7-3acc5b616043"
canonical_ref: ""
---

# Visualizing Supabase Database

## Overview
- **Date**: 2026-05-17 13:51:05
- **Conversation ID**: `6a0a0e13-df58-83ea-a1f7-3acc5b616043`
- **Source**: `Chat-Export-28513-2026/conversations-007.json`

## Chat History

### User
> chat how can i get a visual view of the entire supabase database base at any time. is there a script or app or something.

### Assistant
> Yeah — you want an “X-ray view” of the database, not clicking table-by-table like a raccoon in a filing cabinet. I’ll separate the options into: fastest built-in, best local app, and scriptable/exportable visual map.

### Assistant
> Yes. Since Supabase is Postgres under the hood, you’ve got several good options.
> 
> For **your workflow**, I’d do this:
> 
> ## Best setup
> 
> ### 1. Use Supabase Studio for quick visual checks
> 
> Supabase has a **Visual Schema Designer** inside Supabase Studio for visually creating/modifying PostgreSQL schemas, and it’s available for hosted and self-hosted Supabase. citeturn976178search12
> 
> Good for:
> - quick table/relationship checks
> - seeing foreign keys
> - editing structure without writing SQL
> 
> Not enough for:
> - full database documentation
> - exportable diagrams
> - versioned schema maps
> - “show me the whole system at a glance”
> 
> ### 2. Use DBeaver for the everyday “database map”
> 
> Install **DBeaver Community Edition**, connect it to Supabase using your Postgres connection string, then open ER Diagram view. DBeaver’s diagram editor can visually explore database structure, rearrange layouts, search diagrams, and export/print them. citeturn976178search2
> 
> This is probably your best daily answer.
> 
> Use it for:
> - full visual ERD
> - table relationships
> - inspecting columns
> - seeing what connects to what
> - exporting PNG/PDF diagrams
> - troubleshooting Supabase structure
> 
> ### 3. Use SchemaSpy for automatic documentation snapshots
> 
> SchemaSpy generates HTML database documentation with Entity Relationship diagrams. citeturn976178search3
> 
> This is the “QiAccess doctrine” option: generate a static snapshot of the database and save it into your knowledge system. That lines up with your blueprint rule that QiAccess needs a clear front door, map, library, and control panel, not just random apps scattered everywhere. fileciteturn0file0
> 
> Good for:
> - versioned DB docs
> - searchable HTML docs
> - saving snapshots before big schema changes
> - comparing structure over time
> - dropping output into `docs`, Wiki.js, or QiNexus
> 
> ## My recommendation
> 
> Use **DBeaver now**, then automate **SchemaSpy later**.
> 
> Clean stack:
> 
> | Need | Tool |
> |---|---|
> | Quick visual view inside Supabase | Supabase Studio Visual Schema Designer |
> | Daily database browser + ERD | DBeaver |
> | Automated exportable documentation | SchemaSpy |
> | Code/schema source control | Supabase CLI migrations/schema dumps |
> 
> ## Simple mental model
> 
> Supabase Studio = edit/check  
> DBeaver = explore/understand  
> SchemaSpy = document/archive  
> Supabase CLI = version/control  
> 
> That’s the grown-up setup. Not overbuilt, not goofy.
> 
> ## Practical next step
> 
> Install DBeaver, connect to Supabase Postgres, then generate the ER diagram from your schema. After that, create a script called something like:
> 
> `generate_supabase_schema_docs`
> 
> Have it output to:
> 
> `docs/02_architecture/database/`
> 
> or, for QiNexus:
> 
> `10_data/database_exports/supabase_schema_snapshots/`
> 
> This gives you a visual map anytime without depending on memory, vibe, or clicking around like Supabase owes you answers.

### User
> so do we instal debeaver server site or on my main pc or what

### Assistant
> Install **DBeaver on your main PC**, not the server.
> 
> That’s the clean answer.
> 
> ## Why
> 
> DBeaver is a **desktop database client**. It should live on the machine where you work visually — your main Windows PC.
> 
> Your Supabase/Postgres database lives elsewhere:
> 
> - Supabase cloud, or
> - your qiserver if self-hosted later
> 
> DBeaver just connects to it.
> 
> ## Best setup for you
> 
> ### Main PC
> 
> Install:
> 
> **DBeaver Community Edition**
> 
> Use it to visually inspect:
> 
> - tables
> - columns
> - relationships
> - ER diagrams
> - queries
> - database structure
> 
> ### Server
> 
> Do **not** install DBeaver on qiserver unless you specifically want a remote desktop/browser-based setup, which you do not need right now.
> 
> Server should stay lean:
> 
> - Postgres / Supabase services
> - backups
> - schema export scripts
> - SchemaSpy later if we want auto-generated docs
> 
> ## Connection model
> 
> Main PC DBeaver → connects to → Supabase Postgres
> 
> Like this:
> 
> `Windows PC / DBeaver` → `Supabase database URL`
> 
> ## What you’ll need from Supabase
> 
> In Supabase:
> 
> `Project Settings` → `Database` → `Connection string`
> 
> Use the **Direct connection** or **Session pooler** string.
> 
> You’ll need:
> 
> - host
> - port
> - database name
> - username
> - password
> - SSL enabled
> 
> ## My recommendation
> 
> Do this order:
> 
> 1. Install **DBeaver Community** on your main PC.
> 2. Connect it to your current Supabase project.
> 3. Generate an ER diagram.
> 4. Later, add a server-side script for automated schema snapshots.
> 
> Do **not** put a GUI database app on the server right now. That’s clutter. DBeaver belongs on your workstation.

### User
> what about schema spy

### Assistant
> SchemaSpy is the “generate me a database manual” layer. Different job than DBeaver: DBeaver is interactive; SchemaSpy is a repeatable snapshot/report you can archive.

### Assistant
> SchemaSpy should go **server-side eventually**, but you can run it from either place.
> 
> Here’s the clean split:
> 
> ## DBeaver = main PC
> 
> Use when you want to **look around interactively**.
> 
> ## SchemaSpy = script/report generator
> 
> Use when you want a **snapshot of the whole database** as HTML docs with ER diagrams.
> 
> SchemaSpy generates browser-readable HTML documentation and entity relationship diagrams from database metadata. citeturn786113search5turn786113search6
> 
> ## Where should you install SchemaSpy?
> 
> For you: **qiserver later, main PC now if you want to test fast.**
> 
> ### Option A — Main PC
> 
> Best for first test.
> 
> Pros:
> - easy to run once
> - output opens locally
> - no server clutter
> - quick proof of concept
> 
> Cons:
> - not automated unless you schedule it on Windows
> 
> ### Option B — qiserver
> 
> Best final setup.
> 
> Pros:
> - can run nightly/weekly
> - output can go into Wiki.js, QiAccess docs, or a static folder
> - consistent automated “database map”
> - better for your QiAccess doctrine
> 
> Cons:
> - needs Docker/script setup
> - must protect credentials
> - must not publicly expose DB docs if they reveal sensitive schema info
> 
> ## My recommendation
> 
> Do this in two phases:
> 
> ### Phase 1: Test from main PC
> 
> Run SchemaSpy once against Supabase and see whether the output is useful.
> 
> ### Phase 2: Move it to qiserver
> 
> Create a folder like:
> 
> `/srv/qios/tools/schema_snapshots/supabase/`
> 
> Output to:
> 
> `/srv/qios/docs/generated/supabase_schema/`
> 
> Then later expose it privately through QiAccess Start or Wiki.js.
> 
> ## Practical command style
> 
> SchemaSpy has an official Docker image, and the docs say the latest image can be pulled with `schemaspy/schemaspy`. The Docker image includes drivers for PostgreSQL, MySQL, MariaDB, and JTDS, so Postgres/Supabase is covered. citeturn786113search1turn786113search9
> 
> Example shape:
> 
> ```bash
> docker run --rm \
>   -v "$PWD/output:/output" \
>   schemaspy/schemaspy:latest \
>   -t pgsql \
>   -host YOUR_SUPABASE_HOST \
>   -port 5432 \
>   -db postgres \
>   -u postgres \
>   -p YOUR_PASSWORD \
>   -s public \
>   -vizjs
> ```
> 
> But don’t paste that yet until we pull the real Supabase connection parts. Passwords in shell history are annoying little gremlins.
> 
> ## What SchemaSpy gives you
> 
> It generates a mini website with:
> 
> - all tables
> - columns
> - indexes
> - constraints
> - foreign keys
> - relationships
> - ER diagrams
> - orphan tables
> - anomalies/warnings
> 
> That is perfect for your “show me the whole database anytime” goal.
> 
> ## Final answer
> 
> Use **DBeaver on your main PC** for daily visual browsing.
> 
> Use **SchemaSpy on qiserver** for automated database documentation snapshots.
> 
> That gives you both:
> 
> `DBeaver = live cockpit`  
> `SchemaSpy = archived blueprint`

### User
> how do i connect my db to beaver supabase is not an option

### Assistant
> Supabase is **not supposed to show as “Supabase”** in DBeaver.
> 
> Pick **PostgreSQL**.
> 
> Supabase = managed PostgreSQL. DBeaver connects to it like any other Postgres database.
> 
> ## Steps in DBeaver
> 
> 1. Open **DBeaver**
> 2. Click **New Database Connection**
> 3. Search/select **PostgreSQL**
> 4. Click **Next**
> 
> Now go to Supabase:
> 
> `Supabase Dashboard` → your project → **Project Settings** → **Database**
> 
> Find the connection info.
> 
> ## Use these fields in DBeaver
> 
> ### Main tab
> 
> | DBeaver field | Supabase value |
> |---|---|
> | Host | Supabase database host |
> | Port | `5432` |
> | Database | usually `postgres` |
> | Username | usually `postgres` |
> | Password | your database password |
> 
> ## Important: SSL
> 
> Go to the **SSL** tab in DBeaver.
> 
> Set:
> 
> - **Use SSL**: enabled
> - **SSL mode**: `require`
> 
> Supabase usually requires SSL. If SSL is off, DBeaver may fail even if everything else is correct.
> 
> ## Which Supabase connection should you use?
> 
> Use **Direct connection** first.
> 
> It will look conceptually like:
> 
> `postgresql://postgres:[password]@db.xxxxx.supabase.co:5432/postgres`
> 
> Break it apart:
> 
> | Part | Meaning |
> |---|---|
> | `postgres` before password | username |
> | `[password]` | database password |
> | `db.xxxxx.supabase.co` | host |
> | `5432` | port |
> | final `/postgres` | database name |
> 
> ## If Direct connection fails
> 
> Use the **Session pooler** connection instead.
> 
> That may use:
> 
> - port `5432` or `6543`
> - username like `postgres.xxxxx`
> - host like `aws-0-us-east-...pooler.supabase.com`
> 
> DBeaver does not care. Still choose **PostgreSQL**.
> 
> ## After it connects
> 
> In DBeaver:
> 
> Right-click your database → **ER Diagram** / **View Diagram**
> 
> Or expand:
> 
> `Databases` → `postgres` → `Schemas` → `public` → `Tables`
> 
> That’s where your Supabase tables live.
> 
> ## Do not use these
> 
> Do **not** use:
> 
> - Supabase API URL
> - anon key
> - service role key
> - project URL
> - REST endpoint
> 
> Those are for the app/API side.
> 
> DBeaver needs the **Postgres database connection**, not the Supabase API credentials.

### User
> i cant connect to it

### Assistant
> Okay, we’ll debug this like a connection problem, not a “you did it wrong” problem. The usual culprit is one of four things: wrong password, IPv6/direct connection issue, SSL not enabled, or using the API URL instead of the Postgres host.

### Assistant
> Yep, this is usually the Supabase gotcha: **Direct connection often fails because it uses IPv6.** Your Windows/network setup may not support that path cleanly. Supabase says the default direct DB connection maps to IPv6, and for IPv4 you should use the **Supavisor Session pooler** instead. citeturn532107search0turn532107search3
> 
> ## Do this: use Session Pooler, not Direct
> 
> In Supabase:
> 
> **Project Dashboard → Connect**
> 
> Look for:
> 
> **Session pooler**
> 
> It will look roughly like:
> 
> `postgresql://postgres.PROJECTREF:PASSWORD@aws-0-us-east-1.pooler.supabase.com:5432/postgres`
> 
> In DBeaver choose:
> 
> **PostgreSQL**
> 
> Then enter:
> 
> | DBeaver field | Value |
> |---|---|
> | Host | `aws-0-...pooler.supabase.com` |
> | Port | `5432` |
> | Database | `postgres` |
> | Username | `postgres.PROJECTREF` |
> | Password | your database password |
> | SSL | enabled |
> | SSL mode | `require` |
> 
> Supabase’s DBeaver docs specifically point you to the **session pooler host and username**, and say direct connection is mainly for IPv6 environments or when you have the IPv4 add-on. citeturn532107search4
> 
> ## DBeaver SSL setting
> 
> In the connection setup:
> 
> 1. Go to the **SSL** tab.
> 2. Check **Use SSL**.
> 3. Set SSL mode to **require**.
> 
> If DBeaver gives you driver prompts, let it download the PostgreSQL driver.
> 
> ## Common mistakes
> 
> Do **not** use these:
> 
> - `https://xxxx.supabase.co`
> - anon key
> - service role key
> - REST API URL
> - project API URL
> 
> Those are app/API credentials. DBeaver needs the **Postgres connection string**.
> 
> ## If password is the problem
> 
> In Supabase:
> 
> **Project Settings → Database → Database Password**
> 
> Reset it if needed.
> 
> Then update DBeaver.
> 
> ## Fast diagnosis
> 
> Tell me the **exact error message** DBeaver gives you. Not the password or full connection string — just the error text.
> 
> But if I had to bet right now: you used the **Direct connection**, and your network/DBeaver path is choking on IPv6. Use **Session pooler port 5432** and SSL require.

### User
> now it look like it is my password how do i check my db password.

### Assistant
> You usually **cannot view the existing Supabase DB password** after setup. You either already saved it somewhere, or you **reset it**.
> 
> Supabase’s docs say if you get `FATAL: Password authentication failed`, double-check the username/password in the dashboard, and if it still fails, reset the database password from project settings. citeturn977407search4
> 
> ## Where to reset it
> 
> In Supabase:
> 
> **Dashboard → Your Project → Project Settings → Database**
> 
> Look for:
> 
> **Database Password** / **Reset database password**
> 
> Supabase’s troubleshooting docs say the database password can be reset from the **Database Settings** page. citeturn977407search0
> 
> ## Important distinction
> 
> This is **not** your Supabase login password.
> 
> It is the **Postgres database password** used for:
> 
> - DBeaver
> - pgAdmin
> - psql
> - SchemaSpy
> - external DB tools
> 
> ## After resetting
> 
> Update DBeaver with the new password.
> 
> Use:
> 
> | Field | Value |
> |---|---|
> | Driver | PostgreSQL |
> | Host | Session pooler host |
> | Port | `5432` |
> | Database | `postgres` |
> | Username | usually `postgres.PROJECTREF` |
> | Password | new DB password |
> | SSL mode | `require` |
> 
> Supabase notes password resets can take a few minutes to take effect, especially if you reset more than once. citeturn977407search9
> 
> ## Tiny trap
> 
> If you are using the **session pooler**, the username is often **not just**:
> 
> `postgres`
> 
> It is usually:
> 
> `postgres.yourprojectref`
> 
> That one little dot has wasted many lives.

### User
> ok forget this for now, give me a command to get the details i need to create the erd using markmind.

### Assistant
> Yep. Forget DBeaver for now. Use **Supabase SQL Editor** and generate a **Markmind-ready Markdown map** directly from the database metadata.
> 
> Go to:
> 
> **Supabase → SQL Editor → New query**
> 
> Run this:
> 
> ```sql
> WITH
> tables AS (
>   SELECT
>     c.table_schema,
>     c.table_name,
>     c.column_name,
>     c.data_type,
>     c.udt_name,
>     c.is_nullable,
>     c.column_default,
>     c.ordinal_position
>   FROM information_schema.columns c
>   WHERE c.table_schema = 'public'
> ),
> pk_cols AS (
>   SELECT
>     kcu.table_schema,
>     kcu.table_name,
>     kcu.column_name
>   FROM information_schema.table_constraints tc
>   JOIN information_schema.key_column_usage kcu
>     ON tc.constraint_name = kcu.constraint_name
>    AND tc.table_schema = kcu.table_schema
>   WHERE tc.constraint_type = 'PRIMARY KEY'
>     AND tc.table_schema = 'public'
> ),
> fk_cols AS (
>   SELECT
>     kcu.table_schema,
>     kcu.table_name,
>     kcu.column_name,
>     ccu.table_name AS foreign_table_name,
>     ccu.column_name AS foreign_column_name
>   FROM information_schema.table_constraints tc
>   JOIN information_schema.key_column_usage kcu
>     ON tc.constraint_name = kcu.constraint_name
>    AND tc.table_schema = kcu.table_schema
>   JOIN information_schema.constraint_column_usage ccu
>     ON ccu.constraint_name = tc.constraint_name
>    AND ccu.table_schema = tc.table_schema
>   WHERE tc.constraint_type = 'FOREIGN KEY'
>     AND tc.table_schema = 'public'
> ),
> table_blocks AS (
>   SELECT
>     t.table_name,
>     '## ' || t.table_name || E'\n' ||
>     string_agg(
>       '- ' ||
>       t.column_name ||
>       ' : `' ||
>       COALESCE(t.udt_name, t.data_type) ||
>       '`' ||
>       CASE WHEN pk.column_name IS NOT NULL THEN ' 🔑 PK' ELSE '' END ||
>       CASE WHEN fk.column_name IS NOT NULL THEN ' 🔗 FK → ' || fk.foreign_table_name || '.' || fk.foreign_column_name ELSE '' END ||
>       CASE WHEN t.is_nullable = 'NO' THEN ' NOT NULL' ELSE '' END ||
>       CASE WHEN t.column_default IS NOT NULL THEN ' DEFAULT `' || replace(t.column_default, E'\n', ' ') || '`' ELSE '' END,
>       E'\n'
>       ORDER BY t.ordinal_position
>     ) AS md
>   FROM tables t
>   LEFT JOIN pk_cols pk
>     ON pk.table_schema = t.table_schema
>    AND pk.table_name = t.table_name
>    AND pk.column_name = t.column_name
>   LEFT JOIN fk_cols fk
>     ON fk.table_schema = t.table_schema
>    AND fk.table_name = t.table_name
>    AND fk.column_name = t.column_name
>   GROUP BY t.table_name
> ),
> relationship_block AS (
>   SELECT
>     '## Relationships' || E'\n' ||
>     COALESCE(
>       string_agg(
>         '- ' || table_name || '.' || column_name ||
>         ' → ' || foreign_table_name || '.' || foreign_column_name,
>         E'\n'
>         ORDER BY table_name, column_name
>       ),
>       '- No foreign keys found'
>     ) AS md
>   FROM fk_cols
> )
> SELECT
>   '# Supabase Database ERD Map' || E'\n\n' ||
>   '## Schema' || E'\n' ||
>   '- public' || E'\n\n' ||
>   (
>     SELECT string_agg(md, E'\n\n' ORDER BY table_name)
>     FROM table_blocks
>   ) || E'\n\n' ||
>   (
>     SELECT md
>     FROM relationship_block
>   ) AS markmind_markdown;
> ```
> 
> Then copy the result from the `markmind_markdown` column into a file like:
> 
> `2026-05-17_supabase_public_schema_erd_map.md`
> 
> Open that in Obsidian with **Markmind / Markmap**.
> 
> ## What it gives you
> 
> It creates a Markdown map like:
> 
> - database
> - schema
> - tables
> - columns
> - data types
> - primary keys
> - foreign keys
> - defaults
> - required fields
> - relationship list
> 
> This is the fastest no-DBeaver, no-password-drama path. Supabase already knows the schema, so let Postgres snitch on itself.

### User
> um its not all the tables, there are multiple schemas many amny tables. and fields.

### Assistant
> Yep — that query was scoped to `public`, so it only showed `public` schema. That was too narrow for your setup.
> 
> Use this one instead. It pulls **all non-system schemas**, all tables, all columns, primary keys, foreign keys, row counts estimate, and relationships.
> 
> Run in **Supabase SQL Editor**:
> 
> ```sql
> WITH
> schemas AS (
>   SELECT schema_name
>   FROM information_schema.schemata
>   WHERE schema_name NOT IN (
>     'pg_catalog',
>     'information_schema',
>     'pg_toast',
>     'pg_temp_1',
>     'pg_toast_temp_1',
>     'extensions',
>     'graphql',
>     'graphql_public',
>     'pgbouncer',
>     'supabase_functions',
>     'supabase_migrations',
>     'net',
>     'vault'
>   )
>   AND schema_name NOT LIKE 'pg_%'
> ),
> tables AS (
>   SELECT
>     c.table_schema,
>     c.table_name,
>     c.column_name,
>     c.data_type,
>     c.udt_name,
>     c.is_nullable,
>     c.column_default,
>     c.ordinal_position
>   FROM information_schema.columns c
>   JOIN schemas s
>     ON s.schema_name = c.table_schema
> ),
> table_meta AS (
>   SELECT
>     n.nspname AS table_schema,
>     cls.relname AS table_name,
>     cls.reltuples::bigint AS estimated_rows,
>     obj_description(cls.oid) AS table_comment
>   FROM pg_class cls
>   JOIN pg_namespace n
>     ON n.oid = cls.relnamespace
>   JOIN schemas s
>     ON s.schema_name = n.nspname
>   WHERE cls.relkind IN ('r', 'p')
> ),
> pk_cols AS (
>   SELECT
>     kcu.table_schema,
>     kcu.table_name,
>     kcu.column_name
>   FROM information_schema.table_constraints tc
>   JOIN information_schema.key_column_usage kcu
>     ON tc.constraint_name = kcu.constraint_name
>    AND tc.table_schema = kcu.table_schema
>    AND tc.table_name = kcu.table_name
>   JOIN schemas s
>     ON s.schema_name = tc.table_schema
>   WHERE tc.constraint_type = 'PRIMARY KEY'
> ),
> fk_cols AS (
>   SELECT
>     kcu.table_schema,
>     kcu.table_name,
>     kcu.column_name,
>     ccu.table_schema AS foreign_table_schema,
>     ccu.table_name AS foreign_table_name,
>     ccu.column_name AS foreign_column_name
>   FROM information_schema.table_constraints tc
>   JOIN information_schema.key_column_usage kcu
>     ON tc.constraint_name = kcu.constraint_name
>    AND tc.table_schema = kcu.table_schema
>    AND tc.table_name = kcu.table_name
>   JOIN information_schema.constraint_column_usage ccu
>     ON ccu.constraint_name = tc.constraint_name
>    AND ccu.constraint_schema = tc.constraint_schema
>   JOIN schemas s
>     ON s.schema_name = tc.table_schema
>   WHERE tc.constraint_type = 'FOREIGN KEY'
> ),
> table_blocks AS (
>   SELECT
>     t.table_schema,
>     t.table_name,
>     '### ' || t.table_schema || '.' || t.table_name || E'\n' ||
>     '- Estimated rows: `' || COALESCE(tm.estimated_rows, 0) || '`' || E'\n' ||
>     CASE
>       WHEN tm.table_comment IS NOT NULL
>       THEN '- Comment: ' || tm.table_comment || E'\n'
>       ELSE ''
>     END ||
>     '- Fields' || E'\n' ||
>     string_agg(
>       '  - ' ||
>       t.column_name ||
>       ' : `' ||
>       COALESCE(t.udt_name, t.data_type) ||
>       '`' ||
>       CASE WHEN pk.column_name IS NOT NULL THEN ' 🔑 PK' ELSE '' END ||
>       CASE WHEN fk.column_name IS NOT NULL THEN ' 🔗 FK → ' || fk.foreign_table_schema || '.' || fk.foreign_table_name || '.' || fk.foreign_column_name ELSE '' END ||
>       CASE WHEN t.is_nullable = 'NO' THEN ' NOT NULL' ELSE '' END ||
>       CASE WHEN t.column_default IS NOT NULL THEN ' DEFAULT `' || replace(t.column_default, E'\n', ' ') || '`' ELSE '' END,
>       E'\n'
>       ORDER BY t.ordinal_position
>     ) AS md
>   FROM tables t
>   LEFT JOIN table_meta tm
>     ON tm.table_schema = t.table_schema
>    AND tm.table_name = t.table_name
>   LEFT JOIN pk_cols pk
>     ON pk.table_schema = t.table_schema
>    AND pk.table_name = t.table_name
>    AND pk.column_name = t.column_name
>   LEFT JOIN fk_cols fk
>     ON fk.table_schema = t.table_schema
>    AND fk.table_name = t.table_name
>    AND fk.column_name = t.column_name
>   GROUP BY
>     t.table_schema,
>     t.table_name,
>     tm.estimated_rows,
>     tm.table_comment
> ),
> schema_blocks AS (
>   SELECT
>     table_schema,
>     '## Schema: ' || table_schema || E'\n\n' ||
>     string_agg(md, E'\n\n' ORDER BY table_name) AS md
>   FROM table_blocks
>   GROUP BY table_schema
> ),
> relationship_block AS (
>   SELECT
>     '## Relationships' || E'\n' ||
>     COALESCE(
>       string_agg(
>         '- ' || table_schema || '.' || table_name || '.' || column_name ||
>         ' → ' || foreign_table_schema || '.' || foreign_table_name || '.' || foreign_column_name,
>         E'\n'
>         ORDER BY table_schema, table_name, column_name
>       ),
>       '- No foreign keys found'
>     ) AS md
>   FROM fk_cols
> ),
> summary_block AS (
>   SELECT
>     '## Summary' || E'\n' ||
>     '- Schemas: `' || COUNT(DISTINCT table_schema) || '`' || E'\n' ||
>     '- Tables: `' || COUNT(DISTINCT table_schema || '.' || table_name) || '`' || E'\n' ||
>     '- Fields: `' || COUNT(*) || '`' AS md
>   FROM tables
> )
> SELECT
>   '# Supabase Database Full ERD Map' || E'\n\n' ||
>   (
>     SELECT md
>     FROM summary_block
>   ) || E'\n\n' ||
>   (
>     SELECT string_agg(md, E'\n\n' ORDER BY table_schema)
>     FROM schema_blocks
>   ) || E'\n\n' ||
>   (
>     SELECT md
>     FROM relationship_block
>   ) AS markmind_markdown;
> ```
> 
> ## What changed
> 
> The first version only did:
> 
> `WHERE c.table_schema = 'public'`
> 
> That’s baby mode.
> 
> This version grabs everything except system/internal schemas. It should include your app schemas like:
> 
> - `public`
> - `auth`
> - `storage`
> - custom schemas
> - app-specific schemas
> - anything not filtered out
> 
> ## If you want truly everything, including Supabase internals
> 
> Remove or shrink this exclusion list:
> 
> ```sql
> WHERE schema_name NOT IN (...)
> AND schema_name NOT LIKE 'pg_%'
> ```
> 
> But fair warning: that gets noisy fast. Supabase has internal tables that will make the Markmind map look like a conspiracy wall with yarn and unpaid taxes.
> 
> ## Better approach for huge DBs
> 
> For Markmind, I’d generate **three maps**:
> 
> 1. **Full schema inventory**
> 2. **App tables only**
> 3. **Relationships only**
> 
> Because one monster map with hundreds of fields is technically complete but visually useless. That’s not a map — that’s a hairball.
> 
> For now, run the big query above. Then we can trim it into a clean Markmind view after you see what it outputs.
