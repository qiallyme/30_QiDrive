---
layout: page
title: Supabase RLS (Row Level Security) Policies
slug: supabase-rls-row-level-security-policies
status: publish
updated_at: "2026-06-29"
tags:
  - qispark
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

# Supabase RLS (Row Level Security) Policies

## Current Setup

### Roles

1. **`anon`** (Anonymous/Public Role)
   - Used by: Cloudflare Worker, API clients, read operations
   - Key: `SUPABASE_ANON_KEY` (public, safe to expose)
   - Permissions: Read (SELECT) and Execute `match_kb` function

2. **`service_role`** (Service Role)
   - Used by: Ingestion scripts (writes)
   - Key: `SUPABASE_SERVICE_ROLE` (secret, never expose)
   - Permissions: **Bypasses RLS entirely** - full access to all tables

## RLS Policies Explained

### For `kb_embeddings` Table

```sql
-- Read: Allow anon to read (for Worker/API queries)
create policy "read-embeddings" on kb_embeddings for select to anon using (true);

-- Write: Allow anon to insert/update (for development/testing)
create policy "write-embeddings" on kb_embeddings for all to anon using (true) with check (true);
```

**Important Notes:**
- The `write-embeddings` policy allows anon to write, which is **permissive** (good for dev, less secure for production)
- If you're using `service_role` key for ingestion (recommended), **you don't need the write policy** - service_role bypasses RLS
- The write policy is only needed if you want to use anon key for writes (not recommended)

### For `match_kb` Function

```sql
grant execute on function match_kb to anon;
```

This allows the Worker/API to call the RPC function using the anon key.

## Recommended Setup

### Production (Secure)

1. **Ingestion Scripts**: Use `service_role` key
   - Bypasses RLS automatically
   - No write policies needed
   - More secure (service_role key is secret)

2. **Worker/API**: Use `anon` key
   - Can only read (SELECT policy)
   - Can execute `match_kb` function
   - Safe to expose in frontend/client code

3. **RLS Policies**:
   ```sql
   -- Only read policy needed
   create policy "read-embeddings" on kb_embeddings for select to anon using (true);
   grant execute on function match_kb to anon;
   ```

### Development (Permissive)

If you want to use anon key for both reads and writes during development:

```sql
-- Read policy
create policy "read-embeddings" on kb_embeddings for select to anon using (true);

-- Write policy (for dev only)
create policy "write-embeddings" on kb_embeddings for all to anon using (true) with check (true);

-- Function permission
grant execute on function match_kb to anon;
```

## Security Best Practices

1. **Never expose service_role key** in:
   - Frontend code
   - Client-side JavaScript
   - Public repositories
   - Environment variables accessible to clients

2. **Anon key is safe to expose** in:
   - Frontend code
   - Cloudflare Worker (public)
   - Client-side applications

3. **For production**: Remove write policies for anon role, use service_role for all writes

4. **For multi-user**: Add authenticated user policies:
   ```sql
   -- Example: Allow authenticated users to read their own data
   create policy "user-embeddings" on kb_embeddings
     for select to authenticated
     using (auth.uid() = user_id);
   ```

## Checking Current Policies

```sql
-- List all policies on kb_embeddings
SELECT * FROM pg_policies WHERE tablename = 'kb_embeddings';

-- Check function permissions
SELECT grantee, privilege_type
FROM information_schema.routine_privileges
WHERE routine_name = 'match_kb';
```
