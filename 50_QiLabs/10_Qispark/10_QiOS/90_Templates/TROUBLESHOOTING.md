---
layout: page
title: QiMemory Worker Troubleshooting Guide
slug: qimemory-worker-troubleshooting-guide
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

# QiMemory Worker Troubleshooting Guide

## Embeddings Failing

### Symptoms

- Worker returns `502` with `error: "EmbeddingFailed"`
- Logs show `EmbeddingFailed` in `wrangler tail`

### Solutions

1. **Verify OpenAI API Key:**
   ```bash
   wrangler secret list
   ```
   Ensure `OPENAI_API_KEY` is set. If missing:
   ```bash
   wrangler secret put OPENAI_API_KEY
   # or use sync-secrets.sh/.ps1
   ```

2. **Check Model Name:**
   The Worker uses `text-embedding-3-large`. Ensure this model is available in your OpenAI account.

3. **Input Length:**
   - Queries longer than 8000 characters will return `400` with `error: "InputTooLarge"`
   - Split long queries or truncate before sending

4. **Rate Limits (429):**
   - The Worker includes automatic retry logic (2 retries with 250ms backoff) for 429/500 errors
   - If you see frequent 429 errors:
     - Slow down batch ingest operations
     - Check your OpenAI rate limits in the dashboard
     - Consider implementing exponential backoff in your client

5. **Network Issues:**
   - If `wrangler dev` works but deployed Worker fails:
     - Check Cloudflare Worker logs: `wrangler tail`
     - Verify secrets are synced: `wrangler secret list`
     - Check for differences in environment between local and deployed

6. **Error Details:**
   Check the response `details` field for specific OpenAI error codes:
   - `insufficient_quota` - API key has no credits
   - `invalid_api_key` - API key is invalid
   - `rate_limit_exceeded` - Too many requests (retry logic should handle this)

## No Matches Returned

### Symptoms

- Worker returns `200` but `matches` array is empty
- Query completes but no relevant content found

### Solutions

1. **Verify Supabase Setup:**
   - Ensure `01_init.sql` has been run in Supabase SQL Editor
   - Check that `kb_embeddings` table exists:
     ```sql
     SELECT COUNT(*) FROM kb_embeddings;
     ```
   - Verify `match_kb` RPC function exists:
     ```sql
     SELECT * FROM pg_proc WHERE proname = 'match_kb';
     ```

2. **Test RPC Directly:**
   Test the Supabase RPC function in SQL Editor:
   ```sql
   -- Generate a test embedding (dummy vector)
   SELECT * FROM match_kb(
     ARRAY[0.1, 0.2, 0.3, ...]::vector(3072),  -- 3072 dimensions for text-embedding-3-large
     3
   );
   ```

   If this fails, check:
   - Vector extension is installed: `CREATE EXTENSION IF NOT EXISTS vector;`
   - Table structure matches expected schema
   - RLS policies allow access

3. **Verify Embedding Dimensions:**
   - `text-embedding-3-large` produces 3072-dimensional vectors
   - Ensure your Supabase `kb_embeddings.embedding` column is `vector(3072)`
   - Check existing data:
     ```sql
     SELECT array_length(embedding::float[], 1) as dims
     FROM kb_embeddings
     LIMIT 1;
     ```

4. **Check Data Exists:**
   - Verify embeddings have been ingested:
     ```sql
     SELECT COUNT(*) FROM kb_embeddings WHERE embedding IS NOT NULL;
     ```
   - If empty, run your ingest script to populate data

5. **Similarity Threshold:**
   - Very specific queries may not match existing content
   - Try broader queries or check if your content is relevant
   - Adjust `k` parameter (default 6, max 20) to get more matches

## Worker Returns 500

### Symptoms

- `500` status with `error: "Missing env"`
- Logs show missing environment variables

### Solutions

1. **Check Secrets:**
   ```bash
   wrangler secret list
   ```

   Required secrets:
   - `OPENAI_API_KEY`
   - `SUPABASE_URL`
   - `SUPABASE_ANON_KEY`

   If missing, sync secrets:
   ```bash
   # macOS/Linux
   ./sync-secrets.sh

   # Windows
   .\sync-secrets.ps1
   ```

2. **Check Logs:**
   ```bash
   wrangler tail
   ```

   Look for the request ID and error details:
   ```
   [requestId] Missing env vars: OPENAI_API_KEY, SUPABASE_URL
   ```

3. **Verify Step:**
   Check the error response `step` field:
   - `env_check` - Missing environment variables
   - `embeddings` - Embedding generation failed
   - `supabase_rpc` - Supabase RPC call failed
   - `chat_completion` - Chat generation failed (non-fatal, still returns matches)

## Supabase RPC Errors

### Symptoms

- `502` with `error: "SupabaseRPCFailed"`
- Logs show Supabase connection or RPC errors

### Solutions

1. **Verify Supabase URL:**
   ```bash
   wrangler secret list
   ```
   Ensure `SUPABASE_URL` is correct (e.g., `https://xxxxx.supabase.co`)

2. **Check Supabase Anon Key:**
   - Get from Supabase Dashboard → Settings → API
   - Sync to Worker: `wrangler secret put SUPABASE_ANON_KEY`

3. **Test RPC Directly:**
   Use Supabase REST API directly:
   ```bash
   curl -X POST "https://YOUR_SUPABASE_URL/rest/v1/rpc/match_kb" \
     -H "apikey: YOUR_ANON_KEY" \
     -H "Authorization: Bearer YOUR_ANON_KEY" \
     -H "Content-Type: application/json" \
     -d '{"query_embedding": [0.1, 0.2, ...], "match_count": 3}'
   ```

4. **Check RLS Policies:**
   - Ensure `02_policies.sql` has been applied
   - Verify anonymous access is allowed for `match_kb` function
   - Check Supabase logs for RLS violations

5. **Vector Dimensions Mismatch:**
   - Ensure embedding vector length matches table schema
   - `text-embedding-3-large` = 3072 dimensions
   - Check table: `SELECT vector_dims(embedding) FROM kb_embeddings LIMIT 1;`

## Chat Completion Fails

### Symptoms

- Worker returns `200` but `answer` is empty or "(generation failed)"
- Logs show chat completion errors

### Solutions

1. **CHAT_MODEL Not Set:**
   - If `CHAT_MODEL` secret is not set, the Worker will return `answer: "(CHAT_MODEL not configured)"`
   - Set the secret: `wrangler secret put CHAT_MODEL gpt-4o-mini`

2. **OpenAI Chat API Errors:**
   - Check OpenAI API key has sufficient credits
   - Verify model name is valid (e.g., `gpt-4o-mini`, `gpt-4o`)
   - Check rate limits and quotas

3. **Context Too Large:**
   - Context is automatically truncated to 6000 characters
   - If truncation is happening, logs will show: `Context truncated from X to 6000 chars`
   - Consider reducing `k` parameter to get fewer, more relevant matches

4. **Non-Fatal Error:**
   - Chat completion failures are non-fatal
   - Worker still returns matches even if answer generation fails
   - Check logs for specific error details

## General Debugging

### Enable Detailed Logging

The Worker logs detailed information for each request:
- Request ID (for tracing)
- Query length and token estimates
- Timing for each step (embeddings, Supabase RPC, chat)
- Error details with diagnostic information

View logs:
```bash
wrangler tail
```

### Test Locally First

Always test locally before deploying:
```bash
cd cloud/worker
wrangler dev
```

Then test in another terminal:
```bash
curl -X POST http://127.0.0.1:8787/query \
  -H "Content-Type: application/json" \
  -d '{"query":"test"}'
```

### Verify Configuration

Check all configuration:
```bash

# List secrets

wrangler secret list

# Check wrangler.toml

cat wrangler.toml

# Verify Worker code

cat src/index.ts
```

## Common Error Codes

| Error Code | Status | Meaning | Solution |
|------------|--------|---------|----------|
| `Missing env` | 500 | Missing required environment variables | Sync secrets |
| `InputTooLarge` | 400 | Query > 8000 characters | Truncate query |
| `InvalidInput` | 400 | Invalid JSON or missing query | Check request body |
| `ParseError` | 400 | Invalid JSON body | Fix JSON format |
| `EmbeddingFailed` | 502 | OpenAI embeddings API error | Check API key, rate limits |
| `SupabaseRPCFailed` | 502 | Supabase RPC call failed | Check URL, key, RLS policies |
| `Not found` | 404 | Unknown route | Use `/query` or `/health` |

## Getting Help

1. Check `wrangler tail` for detailed error logs
2. Verify all secrets are set: `wrangler secret list`
3. Test Supabase RPC directly in SQL Editor
4. Test OpenAI API key independently
5. Review Worker code in `cloud/worker/src/index.ts` for error handling logic
