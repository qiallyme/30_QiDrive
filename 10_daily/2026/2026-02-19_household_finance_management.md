---
layout: page
title: "Household Finance Management"
slug: "household_finance_management"
created_at: "2026-02-19 12:21:03"
updated_at: "2026-07-16T06:49:30-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-004.json"
template_key: master-template
date: 2026-02-19
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69975473-06bc-8333-82fc-c39347c31bbb"
canonical_ref: ""
---

# Household Finance Management

## Overview
- **Date**: 2026-02-19 12:21:03
- **Conversation ID**: `69975473-06bc-8333-82fc-c39347c31bbb`
- **Source**: `Chat-Export-28513-2026/conversations-004.json`

## Chat History

### User
> so me my mom and zai are going to all move in together, what will be the best way to track finances, splits, balances, chores, ect, for the home

### Assistant
> You’re basically describing a **mini household operating system**. If you don’t structure this upfront, it turns into resentment, confusion, and “who paid for what” arguments in ~6 weeks. So let’s design this like a tiny company.
> 
> We need 4 systems:
> 1) Money (shared + personal)
> 2) Bills & reimbursements
> 3) Chores & responsibilities
> 4) Transparency dashboard
> 
> Keep it simple or you won’t use it.
> 
> ---
> 
> # 1) First decision: pick the financial model
> There are only 3 viable household models.
> 
> ### Model A — Split Everything Evenly
> Everyone pays ⅓ of shared costs.
> 
> Works if:
> - income is similar
> - expenses are simple
> 
> ### Model B — Proportional (recommended for you)
> Everyone contributes based on income.
> 
> Example:
> - Mom income: $1,200
> - You income: $4,000
> - Zai income: $2,800  
> Total = $8,000
> 
> Contribution ratio:
> - Mom = 15%
> - You = 50%
> - Zai = 35%
> 
> This prevents quiet resentment when incomes differ.
> 
> ### Model C — Role Based
> Example:
> - One pays rent
> - One pays groceries
> - One pays utilities
> 
> Simple but risky if expenses fluctuate.
> 
> **Realistic recommendation:**  
> Use **Proportional contributions + shared household fund.**
> 
> ---
> 
> # 2) The Household Fund (this is the keystone)
> You need one shared pot of money.
> 
> Open a **joint household account** (or a shared debit card / prepaid account).
> 
> Every month each person transfers their contribution.
> 
> This fund pays ONLY:
> - Rent / mortgage
> - Utilities
> - Internet
> - Groceries
> - Household supplies
> - Pet costs
> - Shared subscriptions
> 
> This eliminates:
> “Can you send me $42.17?” chaos.
> 
> ---
> 
> # 3) The tools (keep this minimal)
> You do NOT need a complicated app stack.
> 
> You need ONE shared hub:
> 👉 **Airtable OR Notion OR Google Sheets**
> 
> Given your ecosystem + need for automation:
> **Google Sheets = fastest and most frictionless.**
> 
> We’ll make 4 tabs.
> 
> ---
> 
> # 4) Sheet #1 — Household Budget
> Columns:
> 
> | Category | Monthly Budget | Paid From Fund? | Notes |
> |---|---|---|---|
> | Rent | $ | Yes | |
> | Electric | $ | Yes | |
> | Internet | $ | Yes | |
> | Groceries | $ | Yes | |
> | Household supplies | $ | Yes | |
> | Pet costs | $ | Yes | |
> | Streaming | $ | Yes | |
> 
> At top:
> ```
> Total Monthly Household Cost = $XXXX
> ```
> 
> Then calculate monthly contributions automatically:
> ```
> Mom pays: $___
> You pay: $___
> Zai pays: $___
> ```
> 
> This becomes the monthly transfer amount.
> 
> ---
> 
> # 5) Sheet #2 — Expense Tracker (reimbursements)
> Because real life happens.
> 
> Columns:
> 
> | Date | Person | Item | Category | Amount | Paid By | Reimbursed? |
> 
> Example:
> | Feb 19 | Cody | Costco run | Groceries | 145 | Cody | No |
> 
> Monthly, reimburse from the household fund.
> 
> This removes:
> “I buy everything and nobody pays me back.”
> 
> ---
> 
> # 6) Sheet #3 — Chore Board (this matters more than money)
> Money fights are loud.  
> Chore resentment is silent and worse.
> 
> Columns:
> 
> | Task | Frequency | Owner | Last Done | Notes |
> |---|---|---|---|---|
> | Trash | Weekly | Zai | | |
> | Vacuum | Weekly | Cody | | |
> | Bathroom clean | Weekly | Mom | | |
> | Kitchen deep clean | Weekly | Rotate | | |
> | Laundry towels | Weekly | Rotate | | |
> | Groceries | Weekly | Cody | | |
> | Pet care | Daily | Shared | | |
> 
> Important rule:
> 👉 Every adult has *default responsibilities*.
> Not “whoever notices it.”
> 
> ---
> 
> # 7) Sheet #4 — Household Dashboard (the magic tab)
> This is the “no secrets” page.
> 
> Shows:
> - Current household fund balance
> - Next bills due
> - Who paid last grocery run
> - Upcoming chores rotation
> 
> Transparency kills tension.
> 
> ---
> 
> # 8) House rules you must agree on upfront
> Have this conversation once. Save months of drama.
> 
> Decide:
> - Grocery style: shared vs personal snacks
> - Guest policy
> - Noise hours
> - Cleaning standards
> - Shared vs private supplies
> 
> Otherwise friction creeps in quietly.
> 
> ---
> 
> # 9) Weekly 10-minute household meeting
> Non-negotiable.
> 
> Agenda:
> - Money check
> - Grocery plan
> - Chore rotation
> - Upcoming expenses
> 
> 10 minutes prevents emotional blowups later.
> 
> ---
> 
> # Simple stack summary
> Use:
> - Joint household account
> - One Google Sheet with 4 tabs
> - Weekly 10-minute check-in
> 
> That’s it. Don’t over-engineer this.
> 
> ---
> 
> If you want, I can design the exact Google Sheet structure so you can copy/paste and be running today.

### User
> it must be an app using cloudflare and supabase

### Assistant
> Got it. If it **must** be an app on **Cloudflare + Supabase**, then build a **tiny household OS** with 4 modules: **Money, Balances, Chores, Ledger**. Keep the MVP tight or you’ll ship never.
> 
> Below is a clean, production-feasible blueprint (architecture + DB schema + RLS approach + UI pages + deployment).
> 
> ---
> 
> ## Architecture
> **Frontend:** Cloudflare Pages (Vite + React)  
> **Backend (optional):** Cloudflare Worker (thin API/proxy + webhooks)  
> **Data/Auth/Realtime:** Supabase (Postgres + Auth + RLS + Realtime)  
> **Files (optional):** Supabase Storage (receipts)  
> **Notifications:** Cloudflare Workers Cron + Supabase + (email/SMS later)
> 
> Why this works:
> - Supabase handles auth + row security + data integrity.
> - Cloudflare handles hosting + edge + cron + any “secret” server logic without exposing keys.
> - Realtime can push “balance changed / chore assigned” instantly.
> 
> ---
> 
> ## MVP Features (ship this first)
> ### 1) Household + Members
> - Create household
> - Invite members by email
> - Roles: `admin`, `member`, `viewer`
> 
> ### 2) Shared Ledger (expense tracker)
> - Add expense: amount, category, paid_by, date, memo
> - Split method per expense: **equal**, **percent**, **custom shares**
> - Auto-generate each member’s share lines
> 
> ### 3) Balances
> - “Who owes who” computed from shares vs payments
> - Simple settle-up: record a payment transfer
> 
> ### 4) Chores
> - Task list with frequency
> - Assignments + completion log
> - Rotation option (basic round-robin)
> 
> That’s enough to stop household chaos.
> 
> ---
> 
> ## Pages / Screens
> 1. **Login**
> 2. **Select Household / Create Household**
> 3. **Dashboard**
>    - Current month spend
>    - Top categories
>    - Balances summary
>    - Next chores due
> 4. **Ledger**
>    - Add expense
>    - Filter by month/category/person
> 5. **Balances**
>    - Net balances + “Settle up” entry
> 6. **Chores**
>    - Assignments + “Mark done”
> 7. **Settings**
>    - Members, roles, categories, split defaults
> 
> ---
> 
> ## Database Schema (Supabase Postgres)
> ### Core
> - `households`
>   - `id uuid pk`
>   - `name text`
>   - `created_by uuid`
>   - `created_at timestamptz`
> 
> - `household_members`
>   - `household_id uuid fk`
>   - `user_id uuid fk`
>   - `role text check in ('admin','member','viewer')`
>   - `display_name text`
>   - `is_active bool`
>   - `joined_at timestamptz`
>   - **pk:** `(household_id, user_id)`
> 
> ### Money
> - `categories`
>   - `id uuid pk`
>   - `household_id uuid`
>   - `name text`
>   - `kind text check in ('expense','income','transfer')` (mostly expense)
>   - `is_active bool`
> 
> - `expenses`
>   - `id uuid pk`
>   - `household_id uuid`
>   - `date date`
>   - `amount_cents int`
>   - `category_id uuid`
>   - `paid_by uuid` (user_id)
>   - `memo text`
>   - `receipt_path text null`
>   - `created_by uuid`
>   - `created_at timestamptz`
> 
> - `expense_shares` (the key table)
>   - `expense_id uuid fk`
>   - `user_id uuid`
>   - `share_cents int`
>   - **pk:** `(expense_id, user_id)`
> 
> - `settlements` (payments between members)
>   - `id uuid pk`
>   - `household_id uuid`
>   - `date date`
>   - `from_user uuid`
>   - `to_user uuid`
>   - `amount_cents int`
>   - `memo text`
>   - `created_by uuid`
>   - `created_at timestamptz`
> 
> ### Chores
> - `chores`
>   - `id uuid pk`
>   - `household_id uuid`
>   - `title text`
>   - `frequency text` (e.g. daily/weekly/monthly or cron-ish)
>   - `points int default 1`
>   - `is_active bool`
> 
> - `chore_assignments`
>   - `id uuid pk`
>   - `chore_id uuid`
>   - `user_id uuid`
>   - `due_date date`
>   - `status text check in ('open','done','skipped')`
>   - `done_at timestamptz null`
> 
> That’s it. Don’t add more tables unless you’re sure.
> 
> ---
> 
> ## Balances Logic (how you compute “who owes who”)
> For each household member:
> 
> **Net balance** =  
> (sum of **shares owed**) − (sum of **paid amounts**) + (sum of **settlements paid**) − (sum of **settlements received**)
> 
> - If net is positive: they owe the household (or others)
> - If net is negative: household owes them
> 
> You can compute this with a SQL view:
> - `v_member_balances` (group by household_id, user_id)
> 
> Then the UI just reads the view.
> 
> ---
> 
> ## Row Level Security (RLS) Rules (non-negotiable)
> Principle: a user can only read/write rows for households they belong to.
> 
> Create a helper view or function:
> - `is_household_member(household_id, auth.uid())`
> 
> Policies:
> - `SELECT` allowed if member
> - `INSERT/UPDATE/DELETE` allowed if member AND:
>   - expenses: member, and `created_by = auth.uid()` OR role is admin
>   - categories/chores: admin only
>   - settlements: member (with from/to also members)
> 
> This prevents “Zai sees another household’s stuff” disasters.
> 
> ---
> 
> ## Cloudflare + Supabase Secrets (how not to screw this up)
> - Frontend uses **Supabase anon key** (safe with RLS)
> - Cloudflare Worker (optional) uses **service role key** ONLY for admin automation tasks (cron, webhooks). Never expose service role to browser.
> 
> ---
> 
> ## Deployment Layout (clean)
> **Repo:**
> - `/apps/household-web` (Cloudflare Pages)
> - `/apps/household-worker` (Cloudflare Worker API + cron)
> - `/supabase` (migrations, SQL views, policies)
> 
> **Cloudflare Pages**
> - Build: `npm run build`
> - Output: `dist`
> - Env vars: `VITE_SUPABASE_URL`, `VITE_SUPABASE_ANON_KEY`
> 
> **Worker**
> - Routes: `/api/*`
> - Env vars: `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`
> 
> ---
> 
> ## MVP Build Order (don’t freestyle)
> 1) Supabase: tables + RLS + seed categories  
> 2) Auth + Household creation + invite flow  
> 3) Ledger add/list expenses + shares  
> 4) Balances view + UI  
> 5) Chores list + mark done  
> 6) Receipts + export later
> 
> ---
> 
> ## Two hard truths
> 1) If you don’t do **RLS correctly**, your app is unsafe.  
> 2) If you try to add “budgets, goals, reminders, analytics, gamification” in MVP, you won’t ship.
> 
> ---
> 
> If you want, I’ll generate:
> - the exact **SQL migrations** (tables + indexes + RLS + views)
> - the **Vite + React Pages skeleton**
> - the **Cloudflare Worker** (cron-ready) template
> 
> …and it’ll be ready to deploy.

### User
> actually I want something called Qione the Qiapps launcher and we will create the qihome app as a component of the app, instead becaue i dont want 20 apps, i want something like zoho one, where i can work on different modules and add or assign them to users to see the addtional functionality ect all from one launcher the idea is i only have one app, but what you see / can do depends on what is assigned to you.

### Assistant
> Good. “One app, many modules” is the right move. Twenty separate apps is how you end up with twenty half-broken auth flows and no adoption.
> 
> Here’s the clean way to design **QiOne (QiApps Launcher)** with **QiHome** as just one module.
> 
> ---
> 
> ## Core concept
> **QiOne = a shell + permissions + navigation.**  
> Everything else is a **module** that plugs in.
> 
> What a user can see/do is determined by:
> - which **tenants/workspaces** they belong to (Home, Biz, Client, etc.)
> - which **modules** are **assigned** to them
> - which **roles/permissions** they have inside that tenant
> 
> This is basically: *Zoho One meets “feature flags” meets multi-tenant RBAC.*
> 
> ---
> 
> ## Architecture (Cloudflare + Supabase)
> **Frontend:** Cloudflare Pages (React + Vite)  
> **Data/Auth/RLS:** Supabase Postgres + Auth + RLS  
> **Optional server:** Cloudflare Worker for anything needing service-role (invites, cron, admin ops)
> 
> Key principle:
> - Browser uses Supabase **anon** key (safe with strong RLS)
> - Only the Worker uses **service role**
> 
> ---
> 
> ## Data model (minimal but scalable)
> 
> ### 1) Tenancy
> You need “spaces” (home vs business vs client portal) without making separate apps.
> 
> **tenants**
> - `id uuid pk`
> - `name text`
> - `type text` (e.g. `home`, `business`, `client`)
> - `created_by uuid`
> - `created_at`
> 
> **tenant_members**
> - `tenant_id uuid`
> - `user_id uuid`
> - `status text` (`active`, `invited`, `disabled`)
> - `pk (tenant_id, user_id)`
> 
> ### 2) Modules catalog
> A global list of modules that exist in QiOne.
> 
> **modules**
> - `key text pk` (e.g. `qihome`, `qicase`, `qinote`, `qifinance`)
> - `name text`
> - `description text`
> - `icon text`
> - `route text` (e.g. `/m/qihome`)
> - `is_active bool`
> 
> ### 3) Module enablement per tenant
> Tenant admin decides which modules are available in that tenant.
> 
> **tenant_modules**
> - `tenant_id uuid`
> - `module_key text`
> - `is_enabled bool`
> - `settings jsonb` (optional)
> - `pk (tenant_id, module_key)`
> 
> ### 4) Role-based access control per module (don’t overbuild)
> Start with roles, then add granular permissions later if needed.
> 
> **roles**
> - `id uuid pk`
> - `tenant_id uuid`
> - `name text` (e.g. `Owner`, `Caregiver`, `Member`, `Viewer`)
> - `rank int` (optional ordering)
> 
> **member_roles**
> - `tenant_id uuid`
> - `user_id uuid`
> - `role_id uuid`
> - `pk (tenant_id, user_id, role_id)`
> 
> **module_role_access**
> - `tenant_id uuid`
> - `module_key text`
> - `role_id uuid`
> - `access text` (`none`, `read`, `write`, `admin`)
> - `pk (tenant_id, module_key, role_id)`
> 
> That is enough to drive:
> - what shows up in the launcher
> - what actions a user can do inside a module
> 
> ### 5) Optional: per-user assignments (feature toggles)
> If you want “this user gets the module even if others don’t”:
> 
> **member_module_assignments**
> - `tenant_id uuid`
> - `user_id uuid`
> - `module_key text`
> - `assigned bool`
> - `pk (tenant_id, user_id, module_key)`
> 
> Rule of thumb:
> - use **roles** for 90%
> - use **per-user assignment** only when you must
> 
> ---
> 
> ## RLS strategy (the non-negotiable)
> Every module table must include:
> - `tenant_id`
> 
> And every policy boils down to:
> - user must be a member of that `tenant_id`
> - user must have module access for that module
> 
> You’ll implement a Postgres helper function like:
> - `is_tenant_member(tenant_id, auth.uid())`
> - `module_access_level(tenant_id, module_key, auth.uid())`
> 
> Then policies become simple and consistent.
> 
> ---
> 
> ## Frontend structure (how QiOne stays one app)
> **Routes:**
> - `/` → Launcher (shows allowed modules)
> - `/t/:tenantId` → Tenant dashboard
> - `/m/:moduleKey/*` → Module router
> 
> **Module contract:**
> Each module exports:
> - `ModuleHome` page
> - `NavItems` (optional)
> - `Permissions` required for each action (read/write/admin)
> - `SettingsPanel` (optional)
> 
> So adding a module is “register in catalog + mount route + add DB tables”.
> 
> ---
> 
> ## QiHome module (your household OS)
> QiHome is a tenant module of type `home`.
> 
> Start with these features:
> - **Ledger** (expenses, shares, settlements)
> - **Chores**
> - **Dashboard**
> - **Documents** (optional: receipts, lease scans)
> 
> All QiHome tables will include `tenant_id` and use the same RBAC.
> 
> ---
> 
> ## UX rules (so it doesn’t become a mess)
> 1) **Tenant first**: user picks “Home” vs “Biz” vs “Client” context.
> 2) Launcher shows **only modules enabled + allowed** for that tenant.
> 3) Inside a module, hide UI actions the user can’t perform (but still enforce via RLS).
> 
> ---
> 
> ## Build order (fast path)
> 1) Auth + create tenant + invite member
> 2) Modules catalog + tenant_modules enable/disable
> 3) Roles + module_role_access (read/write/admin)
> 4) Launcher that queries “what I can access”
> 5) Implement QiHome MVP (ledger + balances + chores)
> 6) Add “assignment overrides” only if needed
> 
> ---
> 
> ## Naming check
> You wrote **“Qione”**. If you want it consistent with the brand system you’ve used:
> - **QiOne** = the suite shell/launcher
> - **QiHome** = a module inside QiOne
> - “QiApps Launcher” can be the tagline
> 
> If you want it spelled differently, lock it now and never change it again.
> 
> ---
> 
> If you want me to make this real in your repo, I can give you **(1)** the exact Supabase SQL migrations (tables + helper functions + RLS policies) and **(2)** the React app skeleton with a working launcher + module routing.
> 
> Just say: **“generate migrations + app skeleton”** and I’ll output both in copy-paste-ready blocks.

### User
> generate migrations + app skeleton

### Assistant
> ```txt
> repo/
>   apps/
>     qione-web/
>       package.json
>       vite.config.ts
>       tsconfig.json
>       index.html
>       public/
>       src/
>         main.tsx
>         app.tsx
>         env.d.ts
>         lib/
>           supabase.ts
>           access.ts
>           money.ts
>         routes/
>           auth.tsx
>           tenant_select.tsx
>           tenant_home.tsx
>           launcher.tsx
>           module_router.tsx
>         modules/
>           registry.ts
>           qihome/
>             index.tsx
>             pages/
>               dashboard.tsx
>               ledger.tsx
>               chores.tsx
>         components/
>           layout.tsx
>           require_auth.tsx
>           toast.tsx
>   supabase/
>     migrations/
>       001_init_qione.sql
>       002_qihome_mvp.sql
> ```
> 
> ---
> 
> ## 1) Supabase migrations
> 
> ### `supabase/migrations/001_init_qione.sql`
> ```sql
> -- QiOne core: tenants + modules + RBAC + membership + launcher visibility
> -- Safe defaults: browser uses anon key; all access controlled via RLS.
> 
> begin;
> 
> -- Extensions
> create extension if not exists "pgcrypto";
> 
> -- =========
> -- Core tables
> -- =========
> 
> create table if not exists public.tenants (
>   id uuid primary key default gen_random_uuid(),
>   name text not null,
>   type text not null check (type in ('home','business','client')),
>   created_by uuid not null,
>   created_at timestamptz not null default now()
> );
> 
> create table if not exists public.tenant_members (
>   tenant_id uuid not null references public.tenants(id) on delete cascade,
>   user_id uuid not null references auth.users(id) on delete cascade,
>   status text not null default 'active' check (status in ('active','invited','disabled')),
>   display_name text,
>   joined_at timestamptz not null default now(),
>   primary key (tenant_id, user_id)
> );
> 
> -- Global module catalog (one row per module key)
> create table if not exists public.modules (
>   key text primary key,
>   name text not null,
>   description text,
>   icon text,
>   route text not null,
>   is_active boolean not null default true
> );
> 
> -- Which modules are enabled for a tenant
> create table if not exists public.tenant_modules (
>   tenant_id uuid not null references public.tenants(id) on delete cascade,
>   module_key text not null references public.modules(key) on delete cascade,
>   is_enabled boolean not null default true,
>   settings jsonb not null default '{}'::jsonb,
>   primary key (tenant_id, module_key)
> );
> 
> -- Tenant-local roles
> create table if not exists public.roles (
>   id uuid primary key default gen_random_uuid(),
>   tenant_id uuid not null references public.tenants(id) on delete cascade,
>   name text not null,
>   rank int not null default 100,
>   unique (tenant_id, name)
> );
> 
> -- Member-role mapping (many-to-many)
> create table if not exists public.member_roles (
>   tenant_id uuid not null references public.tenants(id) on delete cascade,
>   user_id uuid not null references auth.users(id) on delete cascade,
>   role_id uuid not null references public.roles(id) on delete cascade,
>   primary key (tenant_id, user_id, role_id)
> );
> 
> -- RBAC per module (per tenant)
> create table if not exists public.module_role_access (
>   tenant_id uuid not null references public.tenants(id) on delete cascade,
>   module_key text not null references public.modules(key) on delete cascade,
>   role_id uuid not null references public.roles(id) on delete cascade,
>   access text not null check (access in ('none','read','write','admin')),
>   primary key (tenant_id, module_key, role_id)
> );
> 
> -- Optional per-user module assignment override (feature flag)
> create table if not exists public.member_module_assignments (
>   tenant_id uuid not null references public.tenants(id) on delete cascade,
>   user_id uuid not null references auth.users(id) on delete cascade,
>   module_key text not null references public.modules(key) on delete cascade,
>   assigned boolean not null default true,
>   primary key (tenant_id, user_id, module_key)
> );
> 
> -- =========
> -- Helper functions (security definer)
> -- =========
> 
> create or replace function public.is_tenant_member(p_tenant uuid, p_user uuid)
> returns boolean
> language sql
> stable
> security definer
> set search_path = public
> as $$
>   select exists (
>     select 1 from public.tenant_members tm
>     where tm.tenant_id = p_tenant
>       and tm.user_id = p_user
>       and tm.status = 'active'
>   );
> $$;
> 
> -- Returns best access level for a user in a tenant/module via roles + optional assignment override
> -- priority: admin > write > read > none
> create or replace function public.module_access_level(p_tenant uuid, p_module text, p_user uuid)
> returns text
> language plpgsql
> stable
> security definer
> set search_path = public
> as $$
> declare
>   v_enabled boolean;
>   v_assigned boolean;
>   v_level text := 'none';
> begin
>   -- module must be enabled for tenant
>   select coalesce(is_enabled, false)
>     into v_enabled
>   from public.tenant_modules
>   where tenant_id = p_tenant and module_key = p_module;
> 
>   if not v_enabled then
>     return 'none';
>   end if;
> 
>   if not public.is_tenant_member(p_tenant, p_user) then
>     return 'none';
>   end if;
> 
>   -- assignment override (if row exists and assigned=false, it blocks; if assigned=true, it allows)
>   select mma.assigned into v_assigned
>   from public.member_module_assignments mma
>   where mma.tenant_id = p_tenant and mma.user_id = p_user and mma.module_key = p_module;
> 
>   if v_assigned is not null and v_assigned = false then
>     return 'none';
>   end if;
> 
>   -- compute best role-based access
>   with access_rows as (
>     select mra.access
>     from public.member_roles mr
>     join public.module_role_access mra
>       on mra.tenant_id = mr.tenant_id
>      and mra.role_id = mr.role_id
>      and mra.module_key = p_module
>     where mr.tenant_id = p_tenant
>       and mr.user_id = p_user
>   )
>   select
>     case
>       when exists (select 1 from access_rows where access = 'admin') then 'admin'
>       when exists (select 1 from access_rows where access = 'write') then 'write'
>       when exists (select 1 from access_rows where access = 'read') then 'read'
>       else 'none'
>     end
>   into v_level;
> 
>   -- if user has explicit assignment true but no role mapping, allow read by default
>   if v_level = 'none' and v_assigned = true then
>     v_level := 'read';
>   end if;
> 
>   return v_level;
> end;
> $$;
> 
> create or replace function public.has_module_access(p_tenant uuid, p_module text, p_user uuid, p_min text)
> returns boolean
> language plpgsql
> stable
> security definer
> set search_path = public
> as $$
> declare
>   lvl text;
>   minv int;
>   lv int;
> begin
>   lvl := public.module_access_level(p_tenant, p_module, p_user);
> 
>   -- map levels
>   minv := case p_min when 'read' then 1 when 'write' then 2 when 'admin' then 3 else 999 end;
>   lv   := case lvl   when 'read' then 1 when 'write' then 2 when 'admin' then 3 else 0 end;
> 
>   return lv >= minv;
> end;
> $$;
> 
> -- =========
> -- Views
> -- =========
> 
> -- What modules should show in launcher for a user in a tenant
> create or replace view public.v_launcher_modules as
> select
>   tm.tenant_id,
>   tm.user_id,
>   m.key as module_key,
>   m.name,
>   m.description,
>   m.icon,
>   m.route,
>   public.module_access_level(tm.tenant_id, m.key, tm.user_id) as access_level
> from public.tenant_members tm
> join public.tenant_modules tenm on tenm.tenant_id = tm.tenant_id and tenm.is_enabled = true
> join public.modules m on m.key = tenm.module_key and m.is_active = true
> where tm.status = 'active';
> 
> -- =========
> -- RLS
> -- =========
> alter table public.tenants enable row level security;
> alter table public.tenant_members enable row level security;
> alter table public.modules enable row level security;
> alter table public.tenant_modules enable row level security;
> alter table public.roles enable row level security;
> alter table public.member_roles enable row level security;
> alter table public.module_role_access enable row level security;
> alter table public.member_module_assignments enable row level security;
> 
> -- Tenants: a user can see tenants they belong to
> create policy "tenants_select_if_member"
> on public.tenants
> for select
> to authenticated
> using (public.is_tenant_member(id, auth.uid()));
> 
> -- Tenants: create allowed (creator becomes owner via app logic)
> create policy "tenants_insert_self"
> on public.tenants
> for insert
> to authenticated
> with check (created_by = auth.uid());
> 
> -- Tenant members: read if member of that tenant
> create policy "tenant_members_select_if_member"
> on public.tenant_members
> for select
> to authenticated
> using (public.is_tenant_member(tenant_id, auth.uid()));
> 
> -- Tenant members: insert/update/delete restricted to admins of any enabled module 'core' (we’ll define core module)
> -- For MVP, treat 'qione_admin' module as admin gate; you can tighten later.
> -- If you don’t like this, move invites into a Worker with service role.
> create policy "tenant_members_mutate_admin_only"
> on public.tenant_members
> for all
> to authenticated
> using (public.has_module_access(tenant_id, 'qione_admin', auth.uid(), 'admin'))
> with check (public.has_module_access(tenant_id, 'qione_admin', auth.uid(), 'admin'));
> 
> -- Modules catalog: readable by all authenticated (or even anon if you want)
> create policy "modules_select_all"
> on public.modules
> for select
> to authenticated
> using (true);
> 
> -- Modules catalog: mutation locked down (do in SQL or service role)
> create policy "modules_mutation_denied"
> on public.modules
> for insert
> to authenticated
> with check (false);
> 
> create policy "modules_update_denied"
> on public.modules
> for update
> to authenticated
> using (false);
> 
> create policy "modules_delete_denied"
> on public.modules
> for delete
> to authenticated
> using (false);
> 
> -- Tenant modules: read if member; write if admin
> create policy "tenant_modules_select_if_member"
> on public.tenant_modules
> for select
> to authenticated
> using (public.is_tenant_member(tenant_id, auth.uid()));
> 
> create policy "tenant_modules_mutate_admin_only"
> on public.tenant_modules
> for all
> to authenticated
> using (public.has_module_access(tenant_id, 'qione_admin', auth.uid(), 'admin'))
> with check (public.has_module_access(tenant_id, 'qione_admin', auth.uid(), 'admin'));
> 
> -- Roles: read if member; write if admin
> create policy "roles_select_if_member"
> on public.roles
> for select
> to authenticated
> using (public.is_tenant_member(tenant_id, auth.uid()));
> 
> create policy "roles_mutate_admin_only"
> on public.roles
> for all
> to authenticated
> using (public.has_module_access(tenant_id, 'qione_admin', auth.uid(), 'admin'))
> with check (public.has_module_access(tenant_id, 'qione_admin', auth.uid(), 'admin'));
> 
> -- Member roles: read if member; write if admin
> create policy "member_roles_select_if_member"
> on public.member_roles
> for select
> to authenticated
> using (public.is_tenant_member(tenant_id, auth.uid()));
> 
> create policy "member_roles_mutate_admin_only"
> on public.member_roles
> for all
> to authenticated
> using (public.has_module_access(tenant_id, 'qione_admin', auth.uid(), 'admin'))
> with check (public.has_module_access(tenant_id, 'qione_admin', auth.uid(), 'admin'));
> 
> -- Module role access: read if member; write if admin
> create policy "module_role_access_select_if_member"
> on public.module_role_access
> for select
> to authenticated
> using (public.is_tenant_member(tenant_id, auth.uid()));
> 
> create policy "module_role_access_mutate_admin_only"
> on public.module_role_access
> for all
> to authenticated
> using (public.has_module_access(tenant_id, 'qione_admin', auth.uid(), 'admin'))
> with check (public.has_module_access(tenant_id, 'qione_admin', auth.uid(), 'admin'));
> 
> -- Member module assignments: read if member; write if admin
> create policy "member_module_assignments_select_if_member"
> on public.member_module_assignments
> for select
> to authenticated
> using (public.is_tenant_member(tenant_id, auth.uid()));
> 
> create policy "member_module_assignments_mutate_admin_only"
> on public.member_module_assignments
> for all
> to authenticated
> using (public.has_module_access(tenant_id, 'qione_admin', auth.uid(), 'admin'))
> with check (public.has_module_access(tenant_id, 'qione_admin', auth.uid(), 'admin'));
> 
> -- Launcher view: expose via security barrier by RLS on base tables (ok)
> -- (No RLS on views.)
> 
> -- =========
> -- Seed module catalog
> -- =========
> insert into public.modules (key, name, description, icon, route, is_active)
> values
>   ('qione_admin', 'QiOne Admin', 'Tenant settings, members, roles, modules', 'settings', '/t/:tenantId/settings', true),
>   ('qihome', 'QiHome', 'Household: money, balances, chores', 'home', '/m/qihome', true)
> on conflict (key) do nothing;
> 
> commit;
> ```
> 
> ### `supabase/migrations/002_qihome_mvp.sql`
> ```sql
> -- QiHome MVP: ledger + settlements + chores
> begin;
> 
> -- =========
> -- Money
> -- =========
> create table if not exists public.qihome_categories (
>   id uuid primary key default gen_random_uuid(),
>   tenant_id uuid not null references public.tenants(id) on delete cascade,
>   name text not null,
>   is_active boolean not null default true,
>   unique (tenant_id, name)
> );
> 
> create table if not exists public.qihome_expenses (
>   id uuid primary key default gen_random_uuid(),
>   tenant_id uuid not null references public.tenants(id) on delete cascade,
>   date date not null,
>   amount_cents int not null check (amount_cents > 0),
>   category_id uuid references public.qihome_categories(id),
>   paid_by uuid not null references auth.users(id),
>   memo text,
>   receipt_path text,
>   created_by uuid not null references auth.users(id),
>   created_at timestamptz not null default now()
> );
> 
> create table if not exists public.qihome_expense_shares (
>   expense_id uuid not null references public.qihome_expenses(id) on delete cascade,
>   user_id uuid not null references auth.users(id) on delete cascade,
>   share_cents int not null check (share_cents >= 0),
>   primary key (expense_id, user_id)
> );
> 
> create table if not exists public.qihome_settlements (
>   id uuid primary key default gen_random_uuid(),
>   tenant_id uuid not null references public.tenants(id) on delete cascade,
>   date date not null,
>   from_user uuid not null references auth.users(id),
>   to_user uuid not null references auth.users(id),
>   amount_cents int not null check (amount_cents > 0),
>   memo text,
>   created_by uuid not null references auth.users(id),
>   created_at timestamptz not null default now()
> );
> 
> -- =========
> -- Chores
> -- =========
> create table if not exists public.qihome_chores (
>   id uuid primary key default gen_random_uuid(),
>   tenant_id uuid not null references public.tenants(id) on delete cascade,
>   title text not null,
>   frequency text not null default 'weekly', -- daily/weekly/monthly/custom
>   points int not null default 1,
>   is_active boolean not null default true
> );
> 
> create table if not exists public.qihome_chore_assignments (
>   id uuid primary key default gen_random_uuid(),
>   tenant_id uuid not null references public.tenants(id) on delete cascade,
>   chore_id uuid not null references public.qihome_chores(id) on delete cascade,
>   user_id uuid not null references auth.users(id),
>   due_date date not null,
>   status text not null default 'open' check (status in ('open','done','skipped')),
>   done_at timestamptz
> );
> 
> -- =========
> -- Balance view (net per user)
> -- net = shares_owed - paid + settlements_sent - settlements_received
> -- positive => user owes; negative => user is owed
> create or replace view public.v_qihome_member_balances as
> with shares as (
>   select e.tenant_id, s.user_id, sum(s.share_cents)::bigint as shares_owed
>   from public.qihome_expense_shares s
>   join public.qihome_expenses e on e.id = s.expense_id
>   group by e.tenant_id, s.user_id
> ),
> paid as (
>   select tenant_id, paid_by as user_id, sum(amount_cents)::bigint as paid_total
>   from public.qihome_expenses
>   group by tenant_id, paid_by
> ),
> sent as (
>   select tenant_id, from_user as user_id, sum(amount_cents)::bigint as sent_total
>   from public.qihome_settlements
>   group by tenant_id, from_user
> ),
> received as (
>   select tenant_id, to_user as user_id, sum(amount_cents)::bigint as recv_total
>   from public.qihome_settlements
>   group by tenant_id, to_user
> ),
> members as (
>   select tenant_id, user_id
>   from public.tenant_members
>   where status = 'active'
> )
> select
>   m.tenant_id,
>   m.user_id,
>   coalesce(sh.shares_owed, 0) as shares_owed,
>   coalesce(p.paid_total, 0) as paid_total,
>   coalesce(se.sent_total, 0) as settlements_sent,
>   coalesce(r.recv_total, 0) as settlements_received,
>   (coalesce(sh.shares_owed, 0)
>    - coalesce(p.paid_total, 0)
>    + coalesce(se.sent_total, 0)
>    - coalesce(r.recv_total, 0)) as net_cents
> from members m
> left join shares sh on sh.tenant_id = m.tenant_id and sh.user_id = m.user_id
> left join paid p on p.tenant_id = m.tenant_id and p.user_id = m.user_id
> left join sent se on se.tenant_id = m.tenant_id and se.user_id = m.user_id
> left join received r on r.tenant_id = m.tenant_id and r.user_id = m.user_id;
> 
> -- =========
> -- RLS
> -- =========
> alter table public.qihome_categories enable row level security;
> alter table public.qihome_expenses enable row level security;
> alter table public.qihome_expense_shares enable row level security;
> alter table public.qihome_settlements enable row level security;
> alter table public.qihome_chores enable row level security;
> alter table public.qihome_chore_assignments enable row level security;
> 
> -- Categories: read if can read qihome; mutate if write
> create policy "qihome_categories_read"
> on public.qihome_categories
> for select
> to authenticated
> using (public.has_module_access(tenant_id, 'qihome', auth.uid(), 'read'));
> 
> create policy "qihome_categories_write"
> on public.qihome_categories
> for all
> to authenticated
> using (public.has_module_access(tenant_id, 'qihome', auth.uid(), 'write'))
> with check (public.has_module_access(tenant_id, 'qihome', auth.uid(), 'write'));
> 
> -- Expenses: read if can read; insert/update/delete if write (creator or admin)
> create policy "qihome_expenses_read"
> on public.qihome_expenses
> for select
> to authenticated
> using (public.has_module_access(tenant_id, 'qihome', auth.uid(), 'read'));
> 
> create policy "qihome_expenses_write"
> on public.qihome_expenses
> for insert
> to authenticated
> with check (
>   public.has_module_access(tenant_id, 'qihome', auth.uid(), 'write')
>   and created_by = auth.uid()
> );
> 
> create policy "qihome_expenses_update_delete"
> on public.qihome_expenses
> for update
> to authenticated
> using (
>   public.has_module_access(tenant_id, 'qihome', auth.uid(), 'write')
>   and (created_by = auth.uid() or public.has_module_access(tenant_id, 'qihome', auth.uid(), 'admin'))
> )
> with check (
>   public.has_module_access(tenant_id, 'qihome', auth.uid(), 'write')
> );
> 
> create policy "qihome_expenses_delete"
> on public.qihome_expenses
> for delete
> to authenticated
> using (
>   public.has_module_access(tenant_id, 'qihome', auth.uid(), 'write')
>   and (created_by = auth.uid() or public.has_module_access(tenant_id, 'qihome', auth.uid(), 'admin'))
> );
> 
> -- Shares: read if can read; write if write
> create policy "qihome_shares_read"
> on public.qihome_expense_shares
> for select
> to authenticated
> using (
>   exists (
>     select 1
>     from public.qihome_expenses e
>     where e.id = expense_id
>       and public.has_module_access(e.tenant_id, 'qihome', auth.uid(), 'read')
>   )
> );
> 
> create policy "qihome_shares_write"
> on public.qihome_expense_shares
> for all
> to authenticated
> using (
>   exists (
>     select 1
>     from public.qihome_expenses e
>     where e.id = expense_id
>       and public.has_module_access(e.tenant_id, 'qihome', auth.uid(), 'write')
>   )
> )
> with check (
>   exists (
>     select 1
>     from public.qihome_expenses e
>     where e.id = expense_id
>       and public.has_module_access(e.tenant_id, 'qihome', auth.uid(), 'write')
>   )
> );
> 
> -- Settlements: read if read; write if write
> create policy "qihome_settlements_read"
> on public.qihome_settlements
> for select
> to authenticated
> using (public.has_module_access(tenant_id, 'qihome', auth.uid(), 'read'));
> 
> create policy "qihome_settlements_write"
> on public.qihome_settlements
> for all
> to authenticated
> using (public.has_module_access(tenant_id, 'qihome', auth.uid(), 'write'))
> with check (
>   public.has_module_access(tenant_id, 'qihome', auth.uid(), 'write')
>   and created_by = auth.uid()
> );
> 
> -- Chores: read if read; write if write
> create policy "qihome_chores_read"
> on public.qihome_chores
> for select
> to authenticated
> using (public.has_module_access(tenant_id, 'qihome', auth.uid(), 'read'));
> 
> create policy "qihome_chores_write"
> on public.qihome_chores
> for all
> to authenticated
> using (public.has_module_access(tenant_id, 'qihome', auth.uid(), 'write'))
> with check (public.has_module_access(tenant_id, 'qihome', auth.uid(), 'write'));
> 
> -- Assignments: read if read; write if write (or self mark done if read)
> create policy "qihome_assignments_read"
> on public.qihome_chore_assignments
> for select
> to authenticated
> using (public.has_module_access(tenant_id, 'qihome', auth.uid(), 'read'));
> 
> create policy "qihome_assignments_write_admin"
> on public.qihome_chore_assignments
> for all
> to authenticated
> using (public.has_module_access(tenant_id, 'qihome', auth.uid(), 'write'))
> with check (public.has_module_access(tenant_id, 'qihome', auth.uid(), 'write'));
> 
> create policy "qihome_assignments_self_mark_done"
> on public.qihome_chore_assignments
> for update
> to authenticated
> using (
>   public.has_module_access(tenant_id, 'qihome', auth.uid(), 'read')
>   and user_id = auth.uid()
> )
> with check (
>   public.has_module_access(tenant_id, 'qihome', auth.uid(), 'read')
>   and user_id = auth.uid()
> );
> 
> -- Seed default categories (optional)
> insert into public.qihome_categories (tenant_id, name)
> select t.id, v.name
> from public.tenants t
> cross join (values ('Rent'),('Utilities'),('Groceries'),('Household'),('Medical'),('Transport')) as v(name)
> where t.type = 'home'
> on conflict do nothing;
> 
> commit;
> ```
> 
> **Important:** After creating a tenant you must also create:
> - at least one role (ex: `Owner`)
> - assign yourself that role
> - enable modules for the tenant (`tenant_modules`)
> - grant role access (`module_role_access`)
> 
> If you don’t, your launcher will show nothing (by design).
> 
> ---
> 
> ## 2) Web app skeleton (React + Vite)
> 
> ### `apps/qione-web/package.json`
> ```json
> {
>   "name": "qione-web",
>   "private": true,
>   "version": "0.1.0",
>   "type": "module",
>   "scripts": {
>     "dev": "vite",
>     "build": "tsc -b && vite build",
>     "preview": "vite preview"
>   },
>   "dependencies": {
>     "@supabase/supabase-js": "^2.49.0",
>     "react": "^18.3.1",
>     "react-dom": "^18.3.1",
>     "react-router-dom": "^6.26.2"
>   },
>   "devDependencies": {
>     "@types/react": "^18.3.5",
>     "@types/react-dom": "^18.3.0",
>     "typescript": "^5.6.2",
>     "vite": "^5.4.3"
>   }
> }
> ```
> 
> ### `apps/qione-web/vite.config.ts`
> ```ts
> import { defineConfig } from "vite";
> import react from "@vitejs/plugin-react";
> 
> export default defineConfig({
>   plugins: [react()],
> });
> ```
> 
> ### `apps/qione-web/tsconfig.json`
> ```json
> {
>   "compilerOptions": {
>     "target": "ES2022",
>     "lib": ["ES2022", "DOM", "DOM.Iterable"],
>     "module": "ESNext",
>     "moduleResolution": "Bundler",
>     "jsx": "react-jsx",
>     "strict": true,
>     "skipLibCheck": true,
>     "types": ["vite/client"]
>   },
>   "include": ["src"]
> }
> ```
> 
> ### `apps/qione-web/src/env.d.ts`
> ```ts
> /// <reference types="vite/client" />
> 
> interface ImportMetaEnv {
>   readonly VITE_SUPABASE_URL: string;
>   readonly VITE_SUPABASE_ANON_KEY: string;
> }
> interface ImportMeta {
>   readonly env: ImportMetaEnv;
> }
> ```
> 
> ### `apps/qione-web/src/lib/supabase.ts`
> ```ts
> import { createClient } from "@supabase/supabase-js";
> 
> const url = import.meta.env.VITE_SUPABASE_URL;
> const anon = import.meta.env.VITE_SUPABASE_ANON_KEY;
> 
> if (!url || !anon) {
>   throw new Error("Missing VITE_SUPABASE_URL or VITE_SUPABASE_ANON_KEY");
> }
> 
> export const supabase = createClient(url, anon, {
>   auth: { persistSession: true, autoRefreshToken: true },
> });
> ```
> 
> ### `apps/qione-web/src/lib/money.ts`
> ```ts
> export function cents(n: number): number {
>   return Math.round(n * 100);
> }
> export function dollars(c: number): string {
>   const sign = c < 0 ? "-" : "";
>   const abs = Math.abs(c);
>   return `${sign}$${(abs / 100).toFixed(2)}`;
> }
> ```
> 
> ### `apps/qione-web/src/lib/access.ts`
> ```ts
> export type AccessLevel = "none" | "read" | "write" | "admin";
> 
> export function allows(level: AccessLevel, min: Exclude<AccessLevel, "none">): boolean {
>   const map: Record<AccessLevel, number> = { none: 0, read: 1, write: 2, admin: 3 };
>   return map[level] >= map[min];
> }
> ```
> 
> ### `apps/qione-web/src/modules/registry.ts`
> ```ts
> import QiHome from "./qihome";
> export type ModuleKey = "qihome" | "qione_admin";
> 
> export type ModuleDef = {
>   key: ModuleKey;
>   name: string;
>   basePath: string; // /m/qihome
>   Component: React.ComponentType;
> };
> 
> export const MODULES: Record<ModuleKey, ModuleDef> = {
>   qihome: { key: "qihome", name: "QiHome", basePath: "/m/qihome", Component: QiHome },
>   qione_admin: {
>     key: "qione_admin",
>     name: "QiOne Admin",
>     basePath: "/t/:tenantId/settings",
>     Component: () => null // stub for now
>   },
> };
> ```
> 
> ### `apps/qione-web/src/modules/qihome/index.tsx`
> ```tsx
> import React from "react";
> import { Link, Route, Routes, useParams } from "react-router-dom";
> import Dashboard from "./pages/dashboard";
> import Ledger from "./pages/ledger";
> import Chores from "./pages/chores";
> 
> export default function QiHome() {
>   const { tenantId } = useParams();
>   return (
>     <div style={{ padding: 16 }}>
>       <h2>QiHome</h2>
>       <div style={{ display: "flex", gap: 12, marginBottom: 12 }}>
>         <Link to={`/m/qihome/${tenantId}/dashboard`}>Dashboard</Link>
>         <Link to={`/m/qihome/${tenantId}/ledger`}>Ledger</Link>
>         <Link to={`/m/qihome/${tenantId}/chores`}>Chores</Link>
>       </div>
> 
>       <Routes>
>         <Route path=":tenantId/dashboard" element={<Dashboard />} />
>         <Route path=":tenantId/ledger" element={<Ledger />} />
>         <Route path=":tenantId/chores" element={<Chores />} />
>       </Routes>
>     </div>
>   );
> }
> ```
> 
> ### `apps/qione-web/src/modules/qihome/pages/dashboard.tsx`
> ```tsx
> import React, { useEffect, useState } from "react";
> import { useParams } from "react-router-dom";
> import { supabase } from "../../../lib/supabase";
> import { dollars } from "../../../lib/money";
> 
> type BalRow = {
>   user_id: string;
>   net_cents: number;
>   shares_owed: number;
>   paid_total: number;
> };
> 
> export default function Dashboard() {
>   const { tenantId } = useParams();
>   const [rows, setRows] = useState<BalRow[]>([]);
>   const [err, setErr] = useState<string | null>(null);
> 
>   useEffect(() => {
>     if (!tenantId) return;
>     (async () => {
>       setErr(null);
>       const { data, error } = await supabase
>         .from("v_qihome_member_balances")
>         .select("user_id, net_cents, shares_owed, paid_total")
>         .eq("tenant_id", tenantId);
> 
>       if (error) setErr(error.message);
>       else setRows((data ?? []) as BalRow[]);
>     })();
>   }, [tenantId]);
> 
>   return (
>     <div>
>       <h3>Balances</h3>
>       {err && <p style={{ color: "crimson" }}>{err}</p>}
>       {!rows.length ? (
>         <p>No balance data yet. Add expenses with shares.</p>
>       ) : (
>         <ul>
>           {rows.map((r) => (
>             <li key={r.user_id}>
>               {r.user_id.slice(0, 8)}… → net {dollars(r.net_cents)}
>             </li>
>           ))}
>         </ul>
>       )}
>     </div>
>   );
> }
> ```
> 
> ### `apps/qione-web/src/modules/qihome/pages/ledger.tsx`
> ```tsx
> import React, { useEffect, useState } from "react";
> import { useParams } from "react-router-dom";
> import { supabase } from "../../../lib/supabase";
> import { cents, dollars } from "../../../lib/money";
> 
> type Expense = {
>   id: string;
>   date: string;
>   amount_cents: number;
>   memo: string | null;
>   paid_by: string;
> };
> 
> export default function Ledger() {
>   const { tenantId } = useParams();
>   const [items, setItems] = useState<Expense[]>([]);
>   const [amount, setAmount] = useState<string>("0");
>   const [memo, setMemo] = useState<string>("");
>   const [err, setErr] = useState<string | null>(null);
> 
>   async function load() {
>     if (!tenantId) return;
>     const { data, error } = await supabase
>       .from("qihome_expenses")
>       .select("id,date,amount_cents,memo,paid_by")
>       .eq("tenant_id", tenantId)
>       .order("date", { ascending: false })
>       .limit(25);
> 
>     if (error) setErr(error.message);
>     else setItems((data ?? []) as Expense[]);
>   }
> 
>   useEffect(() => {
>     setErr(null);
>     load();
>   }, [tenantId]);
> 
>   async function addExpense() {
>     if (!tenantId) return;
>     setErr(null);
> 
>     const { data: session } = await supabase.auth.getSession();
>     const uid = session.session?.user.id;
>     if (!uid) return setErr("Not signed in.");
> 
>     const amt = Number(amount);
>     if (!Number.isFinite(amt) || amt <= 0) return setErr("Amount must be > 0");
> 
>     const { error } = await supabase.from("qihome_expenses").insert({
>       tenant_id: tenantId,
>       date: new Date().toISOString().slice(0, 10),
>       amount_cents: cents(amt),
>       paid_by: uid,
>       memo: memo || null,
>       created_by: uid,
>     });
> 
>     if (error) return setErr(error.message);
> 
>     setAmount("0");
>     setMemo("");
>     await load();
>   }
> 
>   return (
>     <div>
>       <h3>Ledger</h3>
>       {err && <p style={{ color: "crimson" }}>{err}</p>}
> 
>       <div style={{ display: "flex", gap: 8, alignItems: "center", marginBottom: 12 }}>
>         <input
>           value={amount}
>           onChange={(e) => setAmount(e.target.value)}
>           placeholder="Amount (e.g. 42.50)"
>         />
>         <input value={memo} onChange={(e) => setMemo(e.target.value)} placeholder="Memo" />
>         <button onClick={addExpense}>Add</button>
>       </div>
> 
>       {!items.length ? (
>         <p>No expenses yet.</p>
>       ) : (
>         <ul>
>           {items.map((e) => (
>             <li key={e.id}>
>               {e.date} — {dollars(e.amount_cents)} — {e.memo ?? "(no memo)"}
>             </li>
>           ))}
>         </ul>
>       )}
> 
>       <p style={{ opacity: 0.8 }}>
>         Next step: when adding an expense, also create <code>qihome_expense_shares</code> rows
>         (equal split / custom split). Right now balances will stay empty until shares exist.
>       </p>
>     </div>
>   );
> }
> ```
> 
> ### `apps/qione-web/src/modules/qihome/pages/chores.tsx`
> ```tsx
> import React, { useEffect, useState } from "react";
> import { useParams } from "react-router-dom";
> import { supabase } from "../../../lib/supabase";
> 
> type Chore = { id: string; title: string; frequency: string };
> 
> export default function Chores() {
>   const { tenantId } = useParams();
>   const [items, setItems] = useState<Chore[]>([]);
>   const [title, setTitle] = useState("");
>   const [err, setErr] = useState<string | null>(null);
> 
>   async function load() {
>     if (!tenantId) return;
>     const { data, error } = await supabase
>       .from("qihome_chores")
>       .select("id,title,frequency")
>       .eq("tenant_id", tenantId)
>       .eq("is_active", true)
>       .order("title");
> 
>     if (error) setErr(error.message);
>     else setItems((data ?? []) as Chore[]);
>   }
> 
>   useEffect(() => {
>     setErr(null);
>     load();
>   }, [tenantId]);
> 
>   async function addChore() {
>     if (!tenantId) return;
>     setErr(null);
> 
>     if (!title.trim()) return setErr("Chore title required.");
> 
>     const { error } = await supabase.from("qihome_chores").insert({
>       tenant_id: tenantId,
>       title: title.trim(),
>       frequency: "weekly",
>       points: 1,
>       is_active: true,
>     });
> 
>     if (error) return setErr(error.message);
> 
>     setTitle("");
>     await load();
>   }
> 
>   return (
>     <div>
>       <h3>Chores</h3>
>       {err && <p style={{ color: "crimson" }}>{err}</p>}
> 
>       <div style={{ display: "flex", gap: 8, marginBottom: 12 }}>
>         <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="New chore" />
>         <button onClick={addChore}>Add</button>
>       </div>
> 
>       {!items.length ? (
>         <p>No chores yet.</p>
>       ) : (
>         <ul>
>           {items.map((c) => (
>             <li key={c.id}>
>               {c.title} <span style={{ opacity: 0.7 }}>({c.frequency})</span>
>             </li>
>           ))}
>         </ul>
>       )}
>     </div>
>   );
> }
> ```
> 
> ---
> 
> ## 3) Router + auth shell
> 
> ### `apps/qione-web/src/components/require_auth.tsx`
> ```tsx
> import React, { useEffect, useState } from "react";
> import { supabase } from "../lib/supabase";
> import { Navigate } from "react-router-dom";
> 
> export default function RequireAuth({ children }: { children: React.ReactNode }) {
>   const [ready, setReady] = useState(false);
>   const [signedIn, setSignedIn] = useState(false);
> 
>   useEffect(() => {
>     (async () => {
>       const { data } = await supabase.auth.getSession();
>       setSignedIn(!!data.session);
>       setReady(true);
>     })();
> 
>     const { data: sub } = supabase.auth.onAuthStateChange((_evt, session) => {
>       setSignedIn(!!session);
>       setReady(true);
>     });
> 
>     return () => sub.subscription.unsubscribe();
>   }, []);
> 
>   if (!ready) return <div style={{ padding: 16 }}>Loading…</div>;
>   if (!signedIn) return <Navigate to="/auth" replace />;
>   return <>{children}</>;
> }
> ```
> 
> ### `apps/qione-web/src/routes/auth.tsx`
> ```tsx
> import React, { useState } from "react";
> import { supabase } from "../lib/supabase";
> import { useNavigate } from "react-router-dom";
> 
> export default function AuthPage() {
>   const nav = useNavigate();
>   const [email, setEmail] = useState("");
>   const [err, setErr] = useState<string | null>(null);
>   const [sent, setSent] = useState(false);
> 
>   async function signIn() {
>     setErr(null);
>     const { error } = await supabase.auth.signInWithOtp({
>       email,
>       options: { emailRedirectTo: window.location.origin },
>     });
>     if (error) setErr(error.message);
>     else setSent(true);
>   }
> 
>   async function signOut() {
>     await supabase.auth.signOut();
>     nav("/auth");
>   }
> 
>   return (
>     <div style={{ padding: 16, maxWidth: 520 }}>
>       <h2>QiOne</h2>
>       <p>Sign in with email link.</p>
>       {err && <p style={{ color: "crimson" }}>{err}</p>}
>       {sent ? (
>         <p>Check your email for the sign-in link.</p>
>       ) : (
>         <div style={{ display: "flex", gap: 8 }}>
>           <input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="you@email.com" />
>           <button onClick={signIn}>Send Link</button>
>         </div>
>       )}
>       <div style={{ marginTop: 12 }}>
>         <button onClick={signOut}>Sign out</button>
>       </div>
>     </div>
>   );
> }
> ```
> 
> ### `apps/qione-web/src/routes/tenant_select.tsx`
> ```tsx
> import React, { useEffect, useState } from "react";
> import { supabase } from "../lib/supabase";
> import { useNavigate } from "react-router-dom";
> 
> type Tenant = { id: string; name: string; type: string };
> 
> export default function TenantSelect() {
>   const nav = useNavigate();
>   const [tenants, setTenants] = useState<Tenant[]>([]);
>   const [name, setName] = useState("Home");
>   const [type, setType] = useState<"home" | "business" | "client">("home");
>   const [err, setErr] = useState<string | null>(null);
> 
>   async function load() {
>     setErr(null);
>     const { data, error } = await supabase.from("tenants").select("id,name,type").order("created_at", { ascending: false });
>     if (error) setErr(error.message);
>     else setTenants((data ?? []) as Tenant[]);
>   }
> 
>   useEffect(() => { load(); }, []);
> 
>   async function createTenant() {
>     setErr(null);
>     const { data: session } = await supabase.auth.getSession();
>     const uid = session.session?.user.id;
>     if (!uid) return setErr("Not signed in.");
> 
>     // Create tenant
>     const { data: t, error: e1 } = await supabase
>       .from("tenants")
>       .insert({ name, type, created_by: uid })
>       .select("id")
>       .single();
>     if (e1) return setErr(e1.message);
> 
>     const tenantId = t.id as string;
> 
>     // Bootstrap: enable qihome + qione_admin modules, create Owner role, grant admin, assign user
>     // NOTE: these tables are admin-gated by qione_admin access. On a brand-new tenant you don't have that yet.
>     // Best practice: do this bootstrap with SQL (supabase dashboard) or a Cloudflare Worker using service role.
>     // For now, we do the minimal membership insert only (allowed by RLS? no — tenant_members is admin-gated).
>     // So: you MUST bootstrap once with SQL or service role. (I’m not going to lie to you here.)
> 
>     nav(`/t/${tenantId}`);
>   }
> 
>   return (
>     <div style={{ padding: 16 }}>
>       <h2>Select Tenant</h2>
>       {err && <p style={{ color: "crimson" }}>{err}</p>}
> 
>       <div style={{ display: "flex", gap: 8, marginBottom: 16 }}>
>         <input value={name} onChange={(e) => setName(e.target.value)} />
>         <select value={type} onChange={(e) => setType(e.target.value as any)}>
>           <option value="home">home</option>
>           <option value="business">business</option>
>           <option value="client">client</option>
>         </select>
>         <button onClick={createTenant}>Create</button>
>       </div>
> 
>       <h3>Your tenants</h3>
>       {!tenants.length ? (
>         <p>No tenants found (yet).</p>
>       ) : (
>         <ul>
>           {tenants.map((t) => (
>             <li key={t.id}>
>               <button onClick={() => nav(`/t/${t.id}`)}>{t.name}</button> <span style={{ opacity: 0.7 }}>({t.type})</span>
>             </li>
>           ))}
>         </ul>
>       )}
> 
>       <p style={{ marginTop: 16, opacity: 0.85 }}>
>         ⚠️ Bootstrap note: creating a tenant is not enough. You need a one-time bootstrap (membership + role + module enablement),
>         ideally via a Worker with service-role. See “Bootstrap SQL” below.
>       </p>
>     </div>
>   );
> }
> ```
> 
> ### `apps/qione-web/src/routes/tenant_home.tsx`
> ```tsx
> import React from "react";
> import { Link, useParams } from "react-router-dom";
> 
> export default function TenantHome() {
>   const { tenantId } = useParams();
>   return (
>     <div style={{ padding: 16 }}>
>       <h2>Tenant</h2>
>       <p>tenantId: <code>{tenantId}</code></p>
>       <div style={{ display: "flex", gap: 12 }}>
>         <Link to={`/t/${tenantId}/launcher`}>Open Launcher</Link>
>         <Link to={`/m/qihome/${tenantId}/dashboard`}>QiHome</Link>
>       </div>
>     </div>
>   );
> }
> ```
> 
> ### `apps/qione-web/src/routes/launcher.tsx`
> ```tsx
> import React, { useEffect, useState } from "react";
> import { useNavigate, useParams } from "react-router-dom";
> import { supabase } from "../lib/supabase";
> 
> type LauncherRow = {
>   module_key: string;
>   name: string;
>   description: string | null;
>   route: string;
>   access_level: string;
> };
> 
> export default function Launcher() {
>   const nav = useNavigate();
>   const { tenantId } = useParams();
>   const [mods, setMods] = useState<LauncherRow[]>([]);
>   const [err, setErr] = useState<string | null>(null);
> 
>   useEffect(() => {
>     if (!tenantId) return;
>     (async () => {
>       setErr(null);
>       const { data: session } = await supabase.auth.getSession();
>       const uid = session.session?.user.id;
>       if (!uid) return setErr("Not signed in.");
> 
>       const { data, error } = await supabase
>         .from("v_launcher_modules")
>         .select("module_key,name,description,route,access_level")
>         .eq("tenant_id", tenantId)
>         .eq("user_id", uid);
> 
>       if (error) setErr(error.message);
>       else setMods((data ?? []) as LauncherRow[]);
>     })();
>   }, [tenantId]);
> 
>   function open(m: LauncherRow) {
>     // routes stored in catalog are base routes; for modules we pass tenantId in the actual URL
>     if (m.module_key === "qihome") nav(`/m/qihome/${tenantId}/dashboard`);
>     else nav(`/t/${tenantId}/settings`); // admin stub
>   }
> 
>   return (
>     <div style={{ padding: 16 }}>
>       <h2>Launcher</h2>
>       {err && <p style={{ color: "crimson" }}>{err}</p>}
>       {!mods.length ? (
>         <p>No modules visible. This usually means the tenant wasn’t bootstrapped (roles/access/modules).</p>
>       ) : (
>         <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))", gap: 12 }}>
>           {mods.map((m) => (
>             <div key={m.module_key} style={{ border: "1px solid #333", borderRadius: 12, padding: 12 }}>
>               <div style={{ fontWeight: 700 }}>{m.name}</div>
>               <div style={{ opacity: 0.8, margin: "8px 0" }}>{m.description ?? ""}</div>
>               <div style={{ opacity: 0.7 }}>Access: {m.access_level}</div>
>               <button style={{ marginTop: 10 }} onClick={() => open(m)}>Open</button>
>             </div>
>           ))}
>         </div>
>       )}
>     </div>
>   );
> }
> ```
> 
> ### `apps/qione-web/src/routes/module_router.tsx`
> ```tsx
> import React from "react";
> import { Navigate, Route, Routes } from "react-router-dom";
> import QiHome from "../modules/qihome";
> 
> export default function ModuleRouter() {
>   return (
>     <Routes>
>       <Route path="/m/qihome/*" element={<QiHome />} />
>       <Route path="*" element={<Navigate to="/" replace />} />
>     </Routes>
>   );
> }
> ```
> 
> ### `apps/qione-web/src/app.tsx`
> ```tsx
> import React from "react";
> import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
> import RequireAuth from "./components/require_auth";
> import AuthPage from "./routes/auth";
> import TenantSelect from "./routes/tenant_select";
> import TenantHome from "./routes/tenant_home";
> import Launcher from "./routes/launcher";
> import ModuleRouter from "./routes/module_router";
> 
> export default function App() {
>   return (
>     <BrowserRouter>
>       <Routes>
>         <Route path="/auth" element={<AuthPage />} />
> 
>         <Route
>           path="/"
>           element={
>             <RequireAuth>
>               <TenantSelect />
>             </RequireAuth>
>           }
>         />
> 
>         <Route
>           path="/t/:tenantId"
>           element={
>             <RequireAuth>
>               <TenantHome />
>             </RequireAuth>
>           }
>         />
> 
>         <Route
>           path="/t/:tenantId/launcher"
>           element={
>             <RequireAuth>
>               <Launcher />
>             </RequireAuth>
>           }
>         />
> 
>         {/* Module routes */}
>         <Route
>           path="/m/*"
>           element={
>             <RequireAuth>
>               <ModuleRouter />
>             </RequireAuth>
>           }
>         />
> 
>         <Route path="*" element={<Navigate to="/" replace />} />
>       </Routes>
>     </BrowserRouter>
>   );
> }
> ```
> 
> ### `apps/qione-web/src/main.tsx`
> ```tsx
> import React from "react";
> import ReactDOM from "react-dom/client";
> import App from "./app";
> 
> ReactDOM.createRoot(document.getElementById("root")!).render(
>   <React.StrictMode>
>     <App />
>   </React.StrictMode>
> );
> ```
> 
> ---
> 
> ## 4) The one-time bootstrap (do this once per tenant)
> Because we locked down admin tables (correctly), you need a bootstrap path. Fastest: run this in Supabase SQL editor after creating a tenant row (or do it via a Worker later).
> 
> ### Bootstrap SQL template
> ```sql
> -- Fill in:
> --   :tenant_id
> --   :your_user_id
> -- Then run.
> 
> begin;
> 
> -- 1) Create Owner role
> insert into public.roles (tenant_id, name, rank)
> values (:'tenant_id', 'Owner', 1)
> on conflict (tenant_id, name) do nothing;
> 
> -- 2) Add yourself as member (active)
> insert into public.tenant_members (tenant_id, user_id, status, display_name)
> values (:'tenant_id', :'your_user_id', 'active', 'Owner')
> on conflict (tenant_id, user_id) do update set status='active';
> 
> -- 3) Assign Owner role to you
> insert into public.member_roles (tenant_id, user_id, role_id)
> select :'tenant_id', :'your_user_id', r.id
> from public.roles r
> where r.tenant_id = :'tenant_id' and r.name = 'Owner'
> on conflict do nothing;
> 
> -- 4) Enable modules for tenant
> insert into public.tenant_modules (tenant_id, module_key, is_enabled)
> values
>   (:'tenant_id', 'qione_admin', true),
>   (:'tenant_id', 'qihome', true)
> on conflict (tenant_id, module_key) do update set is_enabled = true;
> 
> -- 5) Grant Owner admin access to modules
> insert into public.module_role_access (tenant_id, module_key, role_id, access)
> select :'tenant_id', m.key, r.id, 'admin'
> from public.modules m
> join public.roles r on r.tenant_id = :'tenant_id' and r.name = 'Owner'
> where m.key in ('qione_admin','qihome')
> on conflict (tenant_id, module_key, role_id) do update set access='admin';
> 
> commit;
> ```
> 
> Once that’s done:
> - launcher populates
> - you can add chores/expenses
> - you can invite and assign access later
> 
> ---
> 
> ## 5) Cloudflare Pages config
> Set env vars in Cloudflare Pages project:
> - `VITE_SUPABASE_URL`
> - `VITE_SUPABASE_ANON_KEY`
> 
> Build settings:
> - Framework: Vite
> - Build command: `npm run build`
> - Output: `dist`
> - Root directory: `apps/qione-web`
> 
> ---
> 
> ## Quick truth: your current skeleton ships, but it’s intentionally “MVP ugly”
> If you want it to feel like Zoho One (polished launcher, tiles, theming, module settings UI), that’s UI work on top of this core.
> 
> If you want the next step, say:
> **“Add the Worker bootstrap + invite flow”**  
> …and I’ll give you the Cloudflare Worker that creates tenant + membership + role + access in one API call (no manual SQL).

### User
> Add the Worker bootstrap + invite flow

### Assistant
> Alright. Here’s a **Cloudflare Worker** that does two things using your **Supabase Service Role** (so no manual SQL bootstrap):
> 
> 1) **Bootstrap** a tenant (create tenant + owner role + membership + enable modules + grant admin access)
> 2) **Invite** a user by email + attach them to a tenant + assign a role + grant module access (via role)
> 
> This is the “Zoho One launcher” backbone.
> 
> ---
> 
> # A) Add the Worker app to your repo
> 
> ```txt
> apps/
>   qione-worker/
>     package.json
>     tsconfig.json
>     wrangler.toml
>     src/
>       index.ts
> ```
> 
> ## `apps/qione-worker/package.json`
> ```json
> {
>   "name": "qione-worker",
>   "private": true,
>   "version": "0.1.0",
>   "type": "module",
>   "scripts": {
>     "dev": "wrangler dev",
>     "deploy": "wrangler deploy"
>   },
>   "dependencies": {
>     "@supabase/supabase-js": "^2.49.0"
>   },
>   "devDependencies": {
>     "typescript": "^5.6.2",
>     "wrangler": "^3.80.0"
>   }
> }
> ```
> 
> ## `apps/qione-worker/tsconfig.json`
> ```json
> {
>   "compilerOptions": {
>     "target": "ES2022",
>     "module": "ESNext",
>     "moduleResolution": "Bundler",
>     "strict": true,
>     "types": ["@cloudflare/workers-types"]
>   },
>   "include": ["src"]
> }
> ```
> 
> ## `apps/qione-worker/wrangler.toml`
> ```toml
> name = "qione-worker"
> main = "src/index.ts"
> compatibility_date = "2026-02-19"
> 
> [vars]
> SUPABASE_URL = "https://YOUR_PROJECT_REF.supabase.co"
> SUPABASE_ANON_KEY = "YOUR_ANON_KEY"
> SUPABASE_REDIRECT_TO = "https://YOUR_PAGES_DOMAIN" # for magic link + invites
> 
> # Put this in Cloudflare Secrets (NOT vars):
> # wrangler secret put SUPABASE_SERVICE_ROLE_KEY
> ```
> 
> ---
> 
> # B) Worker code
> 
> ## `apps/qione-worker/src/index.ts`
> ```ts
> import { createClient, SupabaseClient } from "@supabase/supabase-js";
> 
> type Env = {
>   SUPABASE_URL: string;
>   SUPABASE_ANON_KEY: string;
>   SUPABASE_SERVICE_ROLE_KEY: string; // secret
>   SUPABASE_REDIRECT_TO?: string;
> };
> 
> type Json = Record<string, unknown>;
> 
> function json(data: unknown, status = 200, extraHeaders: HeadersInit = {}) {
>   return new Response(JSON.stringify(data), {
>     status,
>     headers: {
>       "content-type": "application/json; charset=utf-8",
>       ...extraHeaders,
>     },
>   });
> }
> 
> function corsHeaders(req: Request) {
>   const origin = req.headers.get("origin") ?? "*";
>   return {
>     "access-control-allow-origin": origin,
>     "access-control-allow-methods": "GET,POST,OPTIONS",
>     "access-control-allow-headers": "content-type,authorization",
>     "access-control-allow-credentials": "true",
>     "vary": "origin",
>   };
> }
> 
> function requireJson(req: Request) {
>   const ct = req.headers.get("content-type") || "";
>   if (!ct.includes("application/json")) throw new Error("Expected application/json");
> }
> 
> function getBearer(req: Request): string | null {
>   const h = req.headers.get("authorization");
>   if (!h) return null;
>   const m = /^Bearer\s+(.+)$/i.exec(h);
>   return m?.[1] ?? null;
> }
> 
> /**
>  * Validate the caller's Supabase access token by calling Supabase Auth "get user".
>  * This avoids JWT verification in Worker (no JWT secret needed).
>  */
> async function getCallerUser(env: Env, accessToken: string) {
>   const url = `${env.SUPABASE_URL}/auth/v1/user`;
>   const res = await fetch(url, {
>     headers: {
>       apikey: env.SUPABASE_ANON_KEY,
>       authorization: `Bearer ${accessToken}`,
>     },
>   });
>   if (!res.ok) return null;
>   return (await res.json()) as { id: string; email?: string };
> }
> 
> function sbService(env: Env): SupabaseClient {
>   return createClient(env.SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY, {
>     auth: { persistSession: false, autoRefreshToken: false },
>   });
> }
> 
> async function assertTenantAdmin(sb: SupabaseClient, tenantId: string, userId: string) {
>   // Must have admin access on qione_admin for this tenant
>   const { data, error } = await sb.rpc("has_module_access", {
>     p_tenant: tenantId,
>     p_module: "qione_admin",
>     p_user: userId,
>     p_min: "admin",
>   });
>   if (error) throw new Error(error.message);
>   if (data !== true) throw new Error("Not authorized (admin required).");
> }
> 
> async function ensureOwnerRole(sb: SupabaseClient, tenantId: string) {
>   // idempotent create
>   const { data: roleRow, error } = await sb
>     .from("roles")
>     .upsert({ tenant_id: tenantId, name: "Owner", rank: 1 }, { onConflict: "tenant_id,name" })
>     .select("id")
>     .single();
>   if (error) throw new Error(error.message);
>   return roleRow.id as string;
> }
> 
> async function enableCoreModules(sb: SupabaseClient, tenantId: string) {
>   const { error } = await sb.from("tenant_modules").upsert(
>     [
>       { tenant_id: tenantId, module_key: "qione_admin", is_enabled: true, settings: {} },
>       { tenant_id: tenantId, module_key: "qihome", is_enabled: true, settings: {} },
>     ],
>     { onConflict: "tenant_id,module_key" }
>   );
>   if (error) throw new Error(error.message);
> }
> 
> async function grantRoleAdminForCore(sb: SupabaseClient, tenantId: string, roleId: string) {
>   const { error } = await sb.from("module_role_access").upsert(
>     [
>       { tenant_id: tenantId, module_key: "qione_admin", role_id: roleId, access: "admin" },
>       { tenant_id: tenantId, module_key: "qihome", role_id: roleId, access: "admin" },
>     ],
>     { onConflict: "tenant_id,module_key,role_id" }
>   );
>   if (error) throw new Error(error.message);
> }
> 
> async function addMember(sb: SupabaseClient, tenantId: string, userId: string, displayName?: string, status: "active" | "invited" | "disabled" = "active") {
>   const { error } = await sb.from("tenant_members").upsert(
>     { tenant_id: tenantId, user_id: userId, status, display_name: displayName ?? null },
>     { onConflict: "tenant_id,user_id" }
>   );
>   if (error) throw new Error(error.message);
> }
> 
> async function assignRole(sb: SupabaseClient, tenantId: string, userId: string, roleId: string) {
>   const { error } = await sb.from("member_roles").upsert(
>     { tenant_id: tenantId, user_id: userId, role_id: roleId },
>     { onConflict: "tenant_id,user_id,role_id" }
>   );
>   if (error) throw new Error(error.message);
> }
> 
> async function findRoleIdByName(sb: SupabaseClient, tenantId: string, name: string) {
>   const { data, error } = await sb.from("roles").select("id").eq("tenant_id", tenantId).eq("name", name).single();
>   if (error) throw new Error(`Role not found: ${name}`);
>   return data.id as string;
> }
> 
> export default {
>   async fetch(req: Request, env: Env): Promise<Response> {
>     const cors = corsHeaders(req);
>     if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: cors });
> 
>     try {
>       const url = new URL(req.url);
>       const path = url.pathname;
> 
>       // Require caller auth for everything except health
>       if (path === "/health") return json({ ok: true }, 200, cors);
> 
>       const token = getBearer(req);
>       if (!token) return json({ error: "Missing Authorization: Bearer <access_token>" }, 401, cors);
> 
>       const caller = await getCallerUser(env, token);
>       if (!caller?.id) return json({ error: "Invalid/expired token" }, 401, cors);
> 
>       const sb = sbService(env);
> 
>       // --------
>       // POST /api/bootstrap
>       // body: { name, type } -> returns { tenant_id }
>       // Creates tenant + makes caller Owner + enables core modules + grants admin access
>       // --------
>       if (path === "/api/bootstrap" && req.method === "POST") {
>         requireJson(req);
>         const body = (await req.json()) as { name?: string; type?: "home" | "business" | "client" };
> 
>         const name = (body.name ?? "Home").trim();
>         const type = body.type ?? "home";
> 
>         if (!name) return json({ error: "name required" }, 400, cors);
> 
>         // 1) create tenant
>         const { data: t, error: e1 } = await sb
>           .from("tenants")
>           .insert({ name, type, created_by: caller.id })
>           .select("id")
>           .single();
>         if (e1) throw new Error(e1.message);
> 
>         const tenantId = t.id as string;
> 
>         // 2) member active
>         await addMember(sb, tenantId, caller.id, "Owner", "active");
> 
>         // 3) owner role
>         const ownerRoleId = await ensureOwnerRole(sb, tenantId);
> 
>         // 4) assign owner role
>         await assignRole(sb, tenantId, caller.id, ownerRoleId);
> 
>         // 5) enable core modules
>         await enableCoreModules(sb, tenantId);
> 
>         // 6) grant Owner admin on core modules
>         await grantRoleAdminForCore(sb, tenantId, ownerRoleId);
> 
>         return json({ tenant_id: tenantId }, 200, cors);
>       }
> 
>       // --------
>       // POST /api/tenants/:tenantId/invite
>       // body: { email, display_name?, role_name?, module_keys? }
>       //
>       // Invites user via Supabase Auth Admin invite
>       // Adds (invited) membership + assigns role (optional) + enables modules (optional)
>       // Requires caller to be qione_admin admin in that tenant.
>       // --------
>       const inviteMatch = path.match(/^\/api\/tenants\/([0-9a-fA-F-]{36})\/invite$/);
>       if (inviteMatch && req.method === "POST") {
>         requireJson(req);
>         const tenantId = inviteMatch[1];
> 
>         await assertTenantAdmin(sb, tenantId, caller.id);
> 
>         const body = (await req.json()) as {
>           email?: string;
>           display_name?: string;
>           role_name?: string; // e.g. "Member", "Caregiver", "Viewer"
>           module_keys?: string[]; // optional enable for tenant
>         };
> 
>         const email = (body.email ?? "").trim().toLowerCase();
>         if (!email) return json({ error: "email required" }, 400, cors);
> 
>         // invite via Supabase Admin API
>         const redirectTo = env.SUPABASE_REDIRECT_TO || undefined;
>         const { data: invited, error: invErr } = await sb.auth.admin.inviteUserByEmail(email, {
>           redirectTo,
>         });
>         if (invErr) throw new Error(invErr.message);
> 
>         const invitedUserId = invited.user?.id;
>         if (!invitedUserId) throw new Error("Invite created but user id missing.");
> 
>         // Add membership as invited
>         await addMember(sb, tenantId, invitedUserId, body.display_name ?? null, "invited");
> 
>         // Optional: enable modules for tenant (if you want the invite to turn on QiHome, etc.)
>         if (Array.isArray(body.module_keys) && body.module_keys.length) {
>           const rows = body.module_keys.map((k) => ({
>             tenant_id: tenantId,
>             module_key: k,
>             is_enabled: true,
>             settings: {},
>           }));
>           const { error } = await sb.from("tenant_modules").upsert(rows, { onConflict: "tenant_id,module_key" });
>           if (error) throw new Error(error.message);
>         }
> 
>         // Optional: role assignment
>         if (body.role_name && body.role_name.trim()) {
>           const roleId = await findRoleIdByName(sb, tenantId, body.role_name.trim());
>           await assignRole(sb, tenantId, invitedUserId, roleId);
>         }
> 
>         return json(
>           {
>             ok: true,
>             invited_user_id: invitedUserId,
>             email,
>             status: "invited",
>           },
>           200,
>           cors
>         );
>       }
> 
>       return json({ error: "Not found" }, 404, cors);
>     } catch (e: any) {
>       return json({ error: e?.message ?? "Server error" }, 500, corsHeaders(req));
>     }
>   },
> };
> ```
> 
> ---
> 
> # C) Required Supabase changes (small but important)
> 
> ## 1) Fix your RPC signatures (so Worker can call them cleanly)
> Your migration created `has_module_access(p_tenant uuid, p_module text, p_user uuid, p_min text)`.
> 
> Supabase RPC expects argument names EXACTLY. The Worker uses those names.
> 
> If your function names differ, update Worker or rename function args.
> 
> ## 2) Add a couple roles besides Owner (recommended)
> Run this once per tenant or make it part of bootstrap later:
> 
> ```sql
> insert into public.roles (tenant_id, name, rank)
> values
>   (:'tenant_id','Member', 50),
>   (:'tenant_id','Viewer', 90)
> on conflict (tenant_id, name) do nothing;
> ```
> 
> And set default module access for them (example: Member write on qihome, Viewer read):
> 
> ```sql
> insert into public.module_role_access (tenant_id, module_key, role_id, access)
> select :'tenant_id', 'qihome', r.id,
>   case r.name when 'Member' then 'write' when 'Viewer' then 'read' else 'none' end
> from public.roles r
> where r.tenant_id = :'tenant_id' and r.name in ('Member','Viewer')
> on conflict (tenant_id, module_key, role_id) do update set access = excluded.access;
> ```
> 
> ---
> 
> # D) Wire the web app to call the Worker
> 
> ### 1) Add env var in Cloudflare Pages
> In **Pages** add:
> - `VITE_API_BASE=https://<your-worker-domain>`
> 
> ### 2) Client helper (add to `qione-web/src/lib/api.ts`)
> ```ts
> import { supabase } from "./supabase";
> 
> const API_BASE = import.meta.env.VITE_API_BASE;
> 
> export async function apiPost(path: string, body: unknown) {
>   const { data } = await supabase.auth.getSession();
>   const token = data.session?.access_token;
>   if (!token) throw new Error("Not signed in.");
> 
>   const res = await fetch(`${API_BASE}${path}`, {
>     method: "POST",
>     headers: {
>       "content-type": "application/json",
>       authorization: `Bearer ${token}`,
>     },
>     body: JSON.stringify(body),
>   });
> 
>   const j = await res.json();
>   if (!res.ok) throw new Error(j?.error ?? "API error");
>   return j;
> }
> ```
> 
> ### 3) Use bootstrap in `TenantSelect`
> Replace your createTenant logic with:
> 
> ```ts
> import { apiPost } from "../lib/api";
> 
> const out = await apiPost("/api/bootstrap", { name, type });
> nav(`/t/${out.tenant_id}`);
> ```
> 
> ### 4) Add invite UI later (or quick test)
> Call:
> ```ts
> await apiPost(`/api/tenants/${tenantId}/invite`, {
>   email: "mom@example.com",
>   display_name: "Mom",
>   role_name: "Member",
>   module_keys: ["qihome"]
> });
> ```
> 
> ---
> 
> # E) Security reality check (so you don’t shoot yourself)
> - Worker endpoints are protected by **Supabase access tokens** validated against `/auth/v1/user`.
> - Tenant invites require the caller to have **admin access** to `qione_admin` in that tenant.
> - Service role key stays inside Worker **only**.
> 
> This is the right pattern.
> 
> ---
> 
> # Next steps I’d do immediately
> 1) Add a simple **Settings → Members** screen that lists `tenant_members` + an Invite form (hits Worker).
> 2) Add **“accept invite”** behavior: when invited user first signs in, flip `tenant_members.status` from `invited` → `active` (Worker endpoint `/api/tenants/:id/accept` or do it in-app via admin-only policy—Worker is cleaner).
> 3) Add “module toggles” UI for tenant admins (update `tenant_modules`).
> 
> If you want, I’ll drop the next Worker endpoints + the members/settings UI skeleton:
> - `POST /api/tenants/:id/accept`
> - `GET /api/tenants/:id/members`
> - `POST /api/tenants/:id/roles` / `POST /api/tenants/:id/access`

### User
> yes, 1, 2, 3

### Assistant
> Cool. Here are the **Worker endpoints** + a **Settings UI skeleton** that covers:
> 
> 1) **Members screen** (list + invite)
> 2) **Accept invite** (invited user activates themselves)
> 3) **Module toggles + roles/access** (basic admin panels)
> 
> I’m keeping it **MVP-clean**: works, secure, not fancy.
> 
> ---
> 
> # 1) Worker: add endpoints 2/3 + members list + roles/access + module toggles
> 
> ## A) Update `apps/qione-worker/src/index.ts`
> Replace your file with this (it includes your existing `/api/bootstrap` + `/invite`, plus new endpoints):
> 
> ```ts
> import { createClient, SupabaseClient } from "@supabase/supabase-js";
> 
> type Env = {
>   SUPABASE_URL: string;
>   SUPABASE_ANON_KEY: string;
>   SUPABASE_SERVICE_ROLE_KEY: string; // secret
>   SUPABASE_REDIRECT_TO?: string;
> };
> 
> function json(data: unknown, status = 200, extraHeaders: HeadersInit = {}) {
>   return new Response(JSON.stringify(data), {
>     status,
>     headers: {
>       "content-type": "application/json; charset=utf-8",
>       ...extraHeaders,
>     },
>   });
> }
> 
> function corsHeaders(req: Request) {
>   const origin = req.headers.get("origin") ?? "*";
>   return {
>     "access-control-allow-origin": origin,
>     "access-control-allow-methods": "GET,POST,PATCH,OPTIONS",
>     "access-control-allow-headers": "content-type,authorization",
>     "access-control-allow-credentials": "true",
>     vary: "origin",
>   } as HeadersInit;
> }
> 
> function requireJson(req: Request) {
>   const ct = req.headers.get("content-type") || "";
>   if (!ct.includes("application/json")) throw new Error("Expected application/json");
> }
> 
> function getBearer(req: Request): string | null {
>   const h = req.headers.get("authorization");
>   if (!h) return null;
>   const m = /^Bearer\s+(.+)$/i.exec(h);
>   return m?.[1] ?? null;
> }
> 
> async function getCallerUser(env: Env, accessToken: string) {
>   const url = `${env.SUPABASE_URL}/auth/v1/user`;
>   const res = await fetch(url, {
>     headers: {
>       apikey: env.SUPABASE_ANON_KEY,
>       authorization: `Bearer ${accessToken}`,
>     },
>   });
>   if (!res.ok) return null;
>   return (await res.json()) as { id: string; email?: string };
> }
> 
> function sbService(env: Env): SupabaseClient {
>   return createClient(env.SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY, {
>     auth: { persistSession: false, autoRefreshToken: false },
>   });
> }
> 
> async function assertTenantAdmin(sb: SupabaseClient, tenantId: string, userId: string) {
>   const { data, error } = await sb.rpc("has_module_access", {
>     p_tenant: tenantId,
>     p_module: "qione_admin",
>     p_user: userId,
>     p_min: "admin",
>   });
>   if (error) throw new Error(error.message);
>   if (data !== true) throw new Error("Not authorized (admin required).");
> }
> 
> async function assertTenantMember(sb: SupabaseClient, tenantId: string, userId: string) {
>   const { data, error } = await sb.rpc("is_tenant_member", { p_tenant: tenantId, p_user: userId });
>   if (error) throw new Error(error.message);
>   if (data !== true) throw new Error("Not authorized (member required).");
> }
> 
> async function ensureRole(sb: SupabaseClient, tenantId: string, name: string, rank = 50) {
>   const { data, error } = await sb
>     .from("roles")
>     .upsert({ tenant_id: tenantId, name, rank }, { onConflict: "tenant_id,name" })
>     .select("id")
>     .single();
>   if (error) throw new Error(error.message);
>   return data.id as string;
> }
> 
> async function addMember(
>   sb: SupabaseClient,
>   tenantId: string,
>   userId: string,
>   displayName?: string | null,
>   status: "active" | "invited" | "disabled" = "active"
> ) {
>   const { error } = await sb.from("tenant_members").upsert(
>     { tenant_id: tenantId, user_id: userId, status, display_name: displayName ?? null },
>     { onConflict: "tenant_id,user_id" }
>   );
>   if (error) throw new Error(error.message);
> }
> 
> async function assignRole(sb: SupabaseClient, tenantId: string, userId: string, roleId: string) {
>   const { error } = await sb.from("member_roles").upsert(
>     { tenant_id: tenantId, user_id: userId, role_id: roleId },
>     { onConflict: "tenant_id,user_id,role_id" }
>   );
>   if (error) throw new Error(error.message);
> }
> 
> async function findRoleIdByName(sb: SupabaseClient, tenantId: string, name: string) {
>   const { data, error } = await sb
>     .from("roles")
>     .select("id")
>     .eq("tenant_id", tenantId)
>     .eq("name", name)
>     .single();
>   if (error) throw new Error(`Role not found: ${name}`);
>   return data.id as string;
> }
> 
> async function enableModules(sb: SupabaseClient, tenantId: string, moduleKeys: string[], enabled: boolean) {
>   const rows = moduleKeys.map((k) => ({
>     tenant_id: tenantId,
>     module_key: k,
>     is_enabled: enabled,
>     settings: {},
>   }));
>   const { error } = await sb.from("tenant_modules").upsert(rows, { onConflict: "tenant_id,module_key" });
>   if (error) throw new Error(error.message);
> }
> 
> async function setRoleAccess(
>   sb: SupabaseClient,
>   tenantId: string,
>   moduleKey: string,
>   roleId: string,
>   access: "none" | "read" | "write" | "admin"
> ) {
>   const { error } = await sb.from("module_role_access").upsert(
>     { tenant_id: tenantId, module_key: moduleKey, role_id: roleId, access },
>     { onConflict: "tenant_id,module_key,role_id" }
>   );
>   if (error) throw new Error(error.message);
> }
> 
> export default {
>   async fetch(req: Request, env: Env): Promise<Response> {
>     const cors = corsHeaders(req);
>     if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: cors });
> 
>     try {
>       const url = new URL(req.url);
>       const path = url.pathname;
> 
>       if (path === "/health") return json({ ok: true }, 200, cors);
> 
>       const token = getBearer(req);
>       if (!token) return json({ error: "Missing Authorization: Bearer <access_token>" }, 401, cors);
> 
>       const caller = await getCallerUser(env, token);
>       if (!caller?.id) return json({ error: "Invalid/expired token" }, 401, cors);
> 
>       const sb = sbService(env);
> 
>       // --------------------
>       // POST /api/bootstrap
>       // --------------------
>       if (path === "/api/bootstrap" && req.method === "POST") {
>         requireJson(req);
>         const body = (await req.json()) as { name?: string; type?: "home" | "business" | "client" };
> 
>         const name = (body.name ?? "Home").trim();
>         const type = body.type ?? "home";
>         if (!name) return json({ error: "name required" }, 400, cors);
> 
>         const { data: t, error: e1 } = await sb
>           .from("tenants")
>           .insert({ name, type, created_by: caller.id })
>           .select("id")
>           .single();
>         if (e1) throw new Error(e1.message);
> 
>         const tenantId = t.id as string;
> 
>         // Create default roles
>         const ownerRoleId = await ensureRole(sb, tenantId, "Owner", 1);
>         const memberRoleId = await ensureRole(sb, tenantId, "Member", 50);
>         const viewerRoleId = await ensureRole(sb, tenantId, "Viewer", 90);
> 
>         // Add caller as active + Owner role
>         await addMember(sb, tenantId, caller.id, "Owner", "active");
>         await assignRole(sb, tenantId, caller.id, ownerRoleId);
> 
>         // Enable core modules by default
>         await enableModules(sb, tenantId, ["qione_admin", "qihome"], true);
> 
>         // Role access defaults:
>         // Owner admin on admin + qihome
>         await setRoleAccess(sb, tenantId, "qione_admin", ownerRoleId, "admin");
>         await setRoleAccess(sb, tenantId, "qihome", ownerRoleId, "admin");
> 
>         // Member: no admin panel, but write qihome
>         await setRoleAccess(sb, tenantId, "qione_admin", memberRoleId, "none");
>         await setRoleAccess(sb, tenantId, "qihome", memberRoleId, "write");
> 
>         // Viewer: read-only qihome
>         await setRoleAccess(sb, tenantId, "qione_admin", viewerRoleId, "none");
>         await setRoleAccess(sb, tenantId, "qihome", viewerRoleId, "read");
> 
>         return json({ tenant_id: tenantId }, 200, cors);
>       }
> 
>       // --------------------
>       // GET /api/tenants/:tenantId/members
>       // Admin-only. Returns tenant_members + email (from auth admin API).
>       // --------------------
>       const membersMatch = path.match(/^\/api\/tenants\/([0-9a-fA-F-]{36})\/members$/);
>       if (membersMatch && req.method === "GET") {
>         const tenantId = membersMatch[1];
>         await assertTenantAdmin(sb, tenantId, caller.id);
> 
>         const { data: mem, error } = await sb
>           .from("tenant_members")
>           .select("tenant_id,user_id,status,display_name,joined_at")
>           .eq("tenant_id", tenantId)
>           .order("joined_at", { ascending: true });
> 
>         if (error) throw new Error(error.message);
> 
>         // Enrich with email using admin API (small N, fine)
>         const enriched = await Promise.all(
>           (mem ?? []).map(async (m) => {
>             const { data: u } = await sb.auth.admin.getUserById(m.user_id);
>             return { ...m, email: u.user?.email ?? null };
>           })
>         );
> 
>         return json({ members: enriched }, 200, cors);
>       }
> 
>       // --------------------
>       // POST /api/tenants/:tenantId/invite
>       // Admin-only. Invites + adds membership "invited" + role assignment.
>       // body: { email, display_name?, role_name? }
>       // --------------------
>       const inviteMatch = path.match(/^\/api\/tenants\/([0-9a-fA-F-]{36})\/invite$/);
>       if (inviteMatch && req.method === "POST") {
>         requireJson(req);
>         const tenantId = inviteMatch[1];
>         await assertTenantAdmin(sb, tenantId, caller.id);
> 
>         const body = (await req.json()) as {
>           email?: string;
>           display_name?: string;
>           role_name?: string; // Owner/Member/Viewer/custom
>         };
> 
>         const email = (body.email ?? "").trim().toLowerCase();
>         if (!email) return json({ error: "email required" }, 400, cors);
> 
>         const redirectTo = env.SUPABASE_REDIRECT_TO || undefined;
>         const { data: invited, error: invErr } = await sb.auth.admin.inviteUserByEmail(email, { redirectTo });
>         if (invErr) throw new Error(invErr.message);
> 
>         const invitedUserId = invited.user?.id;
>         if (!invitedUserId) throw new Error("Invite created but user id missing.");
> 
>         await addMember(sb, tenantId, invitedUserId, body.display_name ?? null, "invited");
> 
>         if (body.role_name && body.role_name.trim()) {
>           const roleId = await findRoleIdByName(sb, tenantId, body.role_name.trim());
>           await assignRole(sb, tenantId, invitedUserId, roleId);
>         }
> 
>         return json({ ok: true, invited_user_id: invitedUserId, email, status: "invited" }, 200, cors);
>       }
> 
>       // --------------------
>       // POST /api/tenants/:tenantId/accept
>       // Invited user self-activates (member-only, but checks invited status).
>       // body: { display_name? }
>       // --------------------
>       const acceptMatch = path.match(/^\/api\/tenants\/([0-9a-fA-F-]{36})\/accept$/);
>       if (acceptMatch && req.method === "POST") {
>         requireJson(req);
>         const tenantId = acceptMatch[1];
> 
>         // must have a membership row (invited or active)
>         const { data: row, error } = await sb
>           .from("tenant_members")
>           .select("status")
>           .eq("tenant_id", tenantId)
>           .eq("user_id", caller.id)
>           .maybeSingle();
>         if (error) throw new Error(error.message);
>         if (!row) throw new Error("No invite found for this tenant.");
> 
>         const body = (await req.json()) as { display_name?: string };
> 
>         // if invited -> activate
>         if (row.status === "invited") {
>           const { error: upErr } = await sb
>             .from("tenant_members")
>             .update({
>               status: "active",
>               display_name: body.display_name ?? null,
>             })
>             .eq("tenant_id", tenantId)
>             .eq("user_id", caller.id);
>           if (upErr) throw new Error(upErr.message);
>         }
> 
>         return json({ ok: true, status: "active" }, 200, cors);
>       }
> 
>       // --------------------
>       // GET /api/tenants/:tenantId/modules
>       // member-only: list modules enabled + access level (for settings UI)
>       // --------------------
>       const modListMatch = path.match(/^\/api\/tenants\/([0-9a-fA-F-]{36})\/modules$/);
>       if (modListMatch && req.method === "GET") {
>         const tenantId = modListMatch[1];
>         await assertTenantMember(sb, tenantId, caller.id);
> 
>         const { data, error } = await sb
>           .from("tenant_modules")
>           .select("module_key,is_enabled,settings,modules(name,description,route,icon,is_active)")
>           .eq("tenant_id", tenantId);
> 
>         if (error) throw new Error(error.message);
> 
>         return json({ tenant_modules: data ?? [] }, 200, cors);
>       }
> 
>       // --------------------
>       // PATCH /api/tenants/:tenantId/modules
>       // admin-only: toggle modules
>       // body: { module_key, is_enabled }
>       // --------------------
>       const modPatchMatch = path.match(/^\/api\/tenants\/([0-9a-fA-F-]{36})\/modules$/);
>       if (modPatchMatch && req.method === "PATCH") {
>         requireJson(req);
>         const tenantId = modPatchMatch[1];
>         await assertTenantAdmin(sb, tenantId, caller.id);
> 
>         const body = (await req.json()) as { module_key?: string; is_enabled?: boolean };
>         if (!body.module_key) throw new Error("module_key required");
>         if (typeof body.is_enabled !== "boolean") throw new Error("is_enabled required");
> 
>         await enableModules(sb, tenantId, [body.module_key], body.is_enabled);
>         return json({ ok: true }, 200, cors);
>       }
> 
>       // --------------------
>       // GET /api/tenants/:tenantId/roles
>       // admin-only: list roles + current access rules
>       // --------------------
>       const rolesListMatch = path.match(/^\/api\/tenants\/([0-9a-fA-F-]{36})\/roles$/);
>       if (rolesListMatch && req.method === "GET") {
>         const tenantId = rolesListMatch[1];
>         await assertTenantAdmin(sb, tenantId, caller.id);
> 
>         const { data: roles, error: rErr } = await sb
>           .from("roles")
>           .select("id,name,rank")
>           .eq("tenant_id", tenantId)
>           .order("rank", { ascending: true });
> 
>         if (rErr) throw new Error(rErr.message);
> 
>         const { data: access, error: aErr } = await sb
>           .from("module_role_access")
>           .select("module_key,role_id,access")
>           .eq("tenant_id", tenantId);
> 
>         if (aErr) throw new Error(aErr.message);
> 
>         return json({ roles: roles ?? [], access: access ?? [] }, 200, cors);
>       }
> 
>       // --------------------
>       // POST /api/tenants/:tenantId/roles
>       // admin-only: create role
>       // body: { name, rank? }
>       // --------------------
>       const roleCreateMatch = path.match(/^\/api\/tenants\/([0-9a-fA-F-]{36})\/roles$/);
>       if (roleCreateMatch && req.method === "POST") {
>         requireJson(req);
>         const tenantId = roleCreateMatch[1];
>         await assertTenantAdmin(sb, tenantId, caller.id);
> 
>         const body = (await req.json()) as { name?: string; rank?: number };
>         const name = (body.name ?? "").trim();
>         if (!name) throw new Error("role name required");
> 
>         const roleId = await ensureRole(sb, tenantId, name, body.rank ?? 50);
>         return json({ ok: true, role_id: roleId }, 200, cors);
>       }
> 
>       // --------------------
>       // POST /api/tenants/:tenantId/access
>       // admin-only: set role access for module
>       // body: { role_id, module_key, access }
>       // --------------------
>       const accessSetMatch = path.match(/^\/api\/tenants\/([0-9a-fA-F-]{36})\/access$/);
>       if (accessSetMatch && req.method === "POST") {
>         requireJson(req);
>         const tenantId = accessSetMatch[1];
>         await assertTenantAdmin(sb, tenantId, caller.id);
> 
>         const body = (await req.json()) as {
>           role_id?: string;
>           module_key?: string;
>           access?: "none" | "read" | "write" | "admin";
>         };
> 
>         if (!body.role_id) throw new Error("role_id required");
>         if (!body.module_key) throw new Error("module_key required");
>         if (!body.access) throw new Error("access required");
> 
>         await setRoleAccess(sb, tenantId, body.module_key, body.role_id, body.access);
>         return json({ ok: true }, 200, cors);
>       }
> 
>       return json({ error: "Not found" }, 404, cors);
>     } catch (e: any) {
>       return json({ error: e?.message ?? "Server error" }, 500, corsHeaders(req));
>     }
>   },
> };
> ```
> 
> ### Worker routes you now have
> - `POST /api/bootstrap`
> - `GET /api/tenants/:tenantId/members`
> - `POST /api/tenants/:tenantId/invite`
> - `POST /api/tenants/:tenantId/accept`
> - `GET /api/tenants/:tenantId/modules`
> - `PATCH /api/tenants/:tenantId/modules`
> - `GET /api/tenants/:tenantId/roles`
> - `POST /api/tenants/:tenantId/roles`
> - `POST /api/tenants/:tenantId/access`
> 
> ---
> 
> # 2) Web: API helpers (GET + PATCH)
> 
> ## `apps/qione-web/src/lib/api.ts`
> ```ts
> import { supabase } from "./supabase";
> 
> const API_BASE = import.meta.env.VITE_API_BASE;
> 
> async function authHeaders() {
>   const { data } = await supabase.auth.getSession();
>   const token = data.session?.access_token;
>   if (!token) throw new Error("Not signed in.");
>   return {
>     "content-type": "application/json",
>     authorization: `Bearer ${token}`,
>   };
> }
> 
> export async function apiGet(path: string) {
>   const res = await fetch(`${API_BASE}${path}`, { headers: await authHeaders() });
>   const j = await res.json();
>   if (!res.ok) throw new Error(j?.error ?? "API error");
>   return j;
> }
> 
> export async function apiPost(path: string, body: unknown) {
>   const res = await fetch(`${API_BASE}${path}`, {
>     method: "POST",
>     headers: await authHeaders(),
>     body: JSON.stringify(body),
>   });
>   const j = await res.json();
>   if (!res.ok) throw new Error(j?.error ?? "API error");
>   return j;
> }
> 
> export async function apiPatch(path: string, body: unknown) {
>   const res = await fetch(`${API_BASE}${path}`, {
>     method: "PATCH",
>     headers: await authHeaders(),
>     body: JSON.stringify(body),
>   });
>   const j = await res.json();
>   if (!res.ok) throw new Error(j?.error ?? "API error");
>   return j;
> }
> ```
> 
> Also add env var in Pages:
> - `VITE_API_BASE=https://<your-worker-domain>`
> 
> ---
> 
> # 3) Web: Settings UI (Members + Modules + Roles)
> 
> ## A) Add route: `/t/:tenantId/settings`
> Update `apps/qione-web/src/app.tsx` (add this route):
> 
> ```tsx
> import TenantSettings from "./routes/tenant_settings";
> 
> // inside <Routes>:
> <Route
>   path="/t/:tenantId/settings"
>   element={
>     <RequireAuth>
>       <TenantSettings />
>     </RequireAuth>
>   }
> />
> ```
> 
> ## B) Create `apps/qione-web/src/routes/tenant_settings.tsx`
> ```tsx
> import React, { useEffect, useState } from "react";
> import { useParams } from "react-router-dom";
> import { apiGet, apiPatch, apiPost } from "../lib/api";
> 
> type Member = {
>   user_id: string;
>   email: string | null;
>   status: string;
>   display_name: string | null;
>   joined_at: string;
> };
> 
> type TenantModule = {
>   module_key: string;
>   is_enabled: boolean;
>   settings: any;
>   modules: { name: string; description: string | null; icon: string | null; is_active: boolean; route: string } | null;
> };
> 
> type Role = { id: string; name: string; rank: number };
> type AccessRow = { module_key: string; role_id: string; access: "none" | "read" | "write" | "admin" };
> 
> export default function TenantSettings() {
>   const { tenantId } = useParams();
>   const [tab, setTab] = useState<"members" | "modules" | "roles">("members");
> 
>   return (
>     <div style={{ padding: 16 }}>
>       <h2>Settings</h2>
>       <div style={{ display: "flex", gap: 10, marginBottom: 12 }}>
>         <button onClick={() => setTab("members")}>Members</button>
>         <button onClick={() => setTab("modules")}>Modules</button>
>         <button onClick={() => setTab("roles")}>Roles & Access</button>
>       </div>
> 
>       {tab === "members" && tenantId && <MembersTab tenantId={tenantId} />}
>       {tab === "modules" && tenantId && <ModulesTab tenantId={tenantId} />}
>       {tab === "roles" && tenantId && <RolesTab tenantId={tenantId} />}
>     </div>
>   );
> }
> 
> function MembersTab({ tenantId }: { tenantId: string }) {
>   const [members, setMembers] = useState<Member[]>([]);
>   const [err, setErr] = useState<string | null>(null);
> 
>   const [email, setEmail] = useState("");
>   const [displayName, setDisplayName] = useState("");
>   const [roleName, setRoleName] = useState("Member");
> 
>   async function load() {
>     setErr(null);
>     try {
>       const out = await apiGet(`/api/tenants/${tenantId}/members`);
>       setMembers(out.members ?? []);
>     } catch (e: any) {
>       setErr(e.message);
>     }
>   }
> 
>   useEffect(() => { load(); }, [tenantId]);
> 
>   async function invite() {
>     setErr(null);
>     try {
>       await apiPost(`/api/tenants/${tenantId}/invite`, {
>         email,
>         display_name: displayName || undefined,
>         role_name: roleName || undefined,
>       });
>       setEmail("");
>       setDisplayName("");
>       await load();
>     } catch (e: any) {
>       setErr(e.message);
>     }
>   }
> 
>   return (
>     <div>
>       <h3>Members</h3>
>       {err && <p style={{ color: "crimson" }}>{err}</p>}
> 
>       <div style={{ display: "flex", gap: 8, alignItems: "center", marginBottom: 12, flexWrap: "wrap" }}>
>         <input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="email@domain.com" />
>         <input value={displayName} onChange={(e) => setDisplayName(e.target.value)} placeholder="Display name (optional)" />
>         <select value={roleName} onChange={(e) => setRoleName(e.target.value)}>
>           <option>Owner</option>
>           <option>Member</option>
>           <option>Viewer</option>
>         </select>
>         <button onClick={invite}>Invite</button>
>       </div>
> 
>       {!members.length ? (
>         <p>No members.</p>
>       ) : (
>         <table style={{ width: "100%", borderCollapse: "collapse" }}>
>           <thead>
>             <tr>
>               <th style={{ textAlign: "left", borderBottom: "1px solid #333" }}>Name</th>
>               <th style={{ textAlign: "left", borderBottom: "1px solid #333" }}>Email</th>
>               <th style={{ textAlign: "left", borderBottom: "1px solid #333" }}>Status</th>
>             </tr>
>           </thead>
>           <tbody>
>             {members.map((m) => (
>               <tr key={m.user_id}>
>                 <td style={{ padding: "6px 0" }}>{m.display_name ?? "—"}</td>
>                 <td style={{ padding: "6px 0" }}>{m.email ?? "—"}</td>
>                 <td style={{ padding: "6px 0" }}>{m.status}</td>
>               </tr>
>             ))}
>           </tbody>
>         </table>
>       )}
>     </div>
>   );
> }
> 
> function ModulesTab({ tenantId }: { tenantId: string }) {
>   const [mods, setMods] = useState<TenantModule[]>([]);
>   const [err, setErr] = useState<string | null>(null);
> 
>   async function load() {
>     setErr(null);
>     try {
>       const out = await apiGet(`/api/tenants/${tenantId}/modules`);
>       setMods(out.tenant_modules ?? []);
>     } catch (e: any) {
>       setErr(e.message);
>     }
>   }
> 
>   useEffect(() => { load(); }, [tenantId]);
> 
>   async function toggle(moduleKey: string, isEnabled: boolean) {
>     setErr(null);
>     try {
>       await apiPatch(`/api/tenants/${tenantId}/modules`, { module_key: moduleKey, is_enabled: isEnabled });
>       await load();
>     } catch (e: any) {
>       setErr(e.message);
>     }
>   }
> 
>   return (
>     <div>
>       <h3>Modules</h3>
>       {err && <p style={{ color: "crimson" }}>{err}</p>}
> 
>       {!mods.length ? (
>         <p>No modules rows. (Bootstrap should create core ones.)</p>
>       ) : (
>         <div style={{ display: "grid", gap: 10 }}>
>           {mods.map((m) => (
>             <div key={m.module_key} style={{ border: "1px solid #333", borderRadius: 12, padding: 12 }}>
>               <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", gap: 10 }}>
>                 <div>
>                   <div style={{ fontWeight: 700 }}>{m.modules?.name ?? m.module_key}</div>
>                   <div style={{ opacity: 0.75 }}>{m.modules?.description ?? ""}</div>
>                 </div>
>                 <label style={{ display: "flex", gap: 8, alignItems: "center" }}>
>                   <span style={{ opacity: 0.8 }}>{m.is_enabled ? "On" : "Off"}</span>
>                   <input
>                     type="checkbox"
>                     checked={m.is_enabled}
>                     onChange={(e) => toggle(m.module_key, e.target.checked)}
>                   />
>                 </label>
>               </div>
>             </div>
>           ))}
>         </div>
>       )}
>     </div>
>   );
> }
> 
> function RolesTab({ tenantId }: { tenantId: string }) {
>   const [roles, setRoles] = useState<Role[]>([]);
>   const [access, setAccess] = useState<AccessRow[]>([]);
>   const [err, setErr] = useState<string | null>(null);
> 
>   const [newRole, setNewRole] = useState("");
> 
>   async function load() {
>     setErr(null);
>     try {
>       const out = await apiGet(`/api/tenants/${tenantId}/roles`);
>       setRoles(out.roles ?? []);
>       setAccess(out.access ?? []);
>     } catch (e: any) {
>       setErr(e.message);
>     }
>   }
> 
>   useEffect(() => { load(); }, [tenantId]);
> 
>   async function createRole() {
>     setErr(null);
>     try {
>       await apiPost(`/api/tenants/${tenantId}/roles`, { name: newRole, rank: 60 });
>       setNewRole("");
>       await load();
>     } catch (e: any) {
>       setErr(e.message);
>     }
>   }
> 
>   function getAccess(roleId: string, moduleKey: string) {
>     return access.find((a) => a.role_id === roleId && a.module_key === moduleKey)?.access ?? "none";
>   }
> 
>   async function setAccessLevel(roleId: string, moduleKey: string, level: AccessRow["access"]) {
>     setErr(null);
>     try {
>       await apiPost(`/api/tenants/${tenantId}/access`, { role_id: roleId, module_key: moduleKey, access: level });
>       await load();
>     } catch (e: any) {
>       setErr(e.message);
>     }
>   }
> 
>   const moduleKeys = ["qione_admin", "qihome"]; // MVP; later pull from /modules
> 
>   return (
>     <div>
>       <h3>Roles & Access</h3>
>       {err && <p style={{ color: "crimson" }}>{err}</p>}
> 
>       <div style={{ display: "flex", gap: 8, marginBottom: 12 }}>
>         <input value={newRole} onChange={(e) => setNewRole(e.target.value)} placeholder="New role name" />
>         <button onClick={createRole}>Create Role</button>
>       </div>
> 
>       {!roles.length ? (
>         <p>No roles.</p>
>       ) : (
>         <table style={{ width: "100%", borderCollapse: "collapse" }}>
>           <thead>
>             <tr>
>               <th style={{ textAlign: "left", borderBottom: "1px solid #333" }}>Role</th>
>               {moduleKeys.map((k) => (
>                 <th key={k} style={{ textAlign: "left", borderBottom: "1px solid #333" }}>{k}</th>
>               ))}
>             </tr>
>           </thead>
>           <tbody>
>             {roles.map((r) => (
>               <tr key={r.id}>
>                 <td style={{ padding: "8px 0", fontWeight: 700 }}>{r.name}</td>
>                 {moduleKeys.map((k) => (
>                   <td key={k} style={{ padding: "8px 0" }}>
>                     <select
>                       value={getAccess(r.id, k)}
>                       onChange={(e) => setAccessLevel(r.id, k, e.target.value as any)}
>                     >
>                       <option value="none">none</option>
>                       <option value="read">read</option>
>                       <option value="write">write</option>
>                       <option value="admin">admin</option>
>                     </select>
>                   </td>
>                 ))}
>               </tr>
>             ))}
>           </tbody>
>         </table>
>       )}
>     </div>
>   );
> }
> ```
> 
> ---
> 
> # 4) Invite acceptance flow (how users activate themselves)
> 
> When Mom/Zai clicks the Supabase invite email link and signs in, your app should show:
> 
> - “You have pending invites” → call `/api/tenants/:tenantId/accept`
> 
> MVP hack: add an “Accept invite” button somewhere if you already know the tenantId.
> 
> If you want it automatic, the next step is: store pending tenant invites by email and let the app discover them. (We can add that later; not needed for first ship.)
> 
> For now, simplest is: you (Owner) invite them, then you text them the tenant link:
> `https://your-app/t/<tenantId>/launcher`
> They sign in, then hit “Accept” (we can add that button next).
> 
> ---
> 
> # 5) Two small config requirements
> ### Cloudflare Worker secrets
> Run:
> ```bash
> cd apps/qione-worker
> wrangler secret put SUPABASE_SERVICE_ROLE_KEY
> ```
> 
> ### Cloudflare Pages env
> Set:
> - `VITE_SUPABASE_URL`
> - `VITE_SUPABASE_ANON_KEY`
> - `VITE_API_BASE` (worker URL)
> 
> ---
> 
> # What you get now
> - You can create a tenant with one click (bootstrap, no manual SQL)
> - You can invite Mom/Zai from Settings → Members
> - They can accept invites and become active
> - You can toggle modules on/off per tenant
> - You can create roles and set per-module access
> 
> If you want the next *useful* thing: I’d add **“Assign role to member”** in the Members tab (so you don’t have to pick role only at invite time).

### User
> Assign role to membe

### Assistant
> Yup. You need **role assignment after the fact**, not just at invite time.
> 
> Below is the minimal, clean implementation:
> 
> - **Worker**: `POST /api/tenants/:tenantId/members/:userId/role` to set a member’s role (replace their roles or add)
> - **Web UI**: add a Role dropdown per member row + “Save”
> 
> I’m going to do **replace** semantics by default (most households want one role per person). If you want multi-role later, you can switch.
> 
> ---
> 
> # 1) Worker: add endpoint to set member role
> 
> ## A) Add a helper to clear roles
> In `apps/qione-worker/src/index.ts`, add this helper near the other helpers:
> 
> ```ts
> async function replaceMemberRoles(sb: SupabaseClient, tenantId: string, userId: string, roleId: string) {
>   // Remove all existing roles for this member in this tenant
>   const { error: delErr } = await sb
>     .from("member_roles")
>     .delete()
>     .eq("tenant_id", tenantId)
>     .eq("user_id", userId);
>   if (delErr) throw new Error(delErr.message);
> 
>   // Add the new role
>   const { error: insErr } = await sb.from("member_roles").insert({
>     tenant_id: tenantId,
>     user_id: userId,
>     role_id: roleId,
>   });
>   if (insErr) throw new Error(insErr.message);
> }
> ```
> 
> ## B) Add the endpoint
> Add this block in your `fetch()` routing section (before the final 404):
> 
> ```ts
> // --------------------
> // POST /api/tenants/:tenantId/members/:userId/role
> // admin-only: replace member roles with a single role (default behavior)
> // body: { role_name? , role_id? }
> // --------------------
> const setRoleMatch = path.match(/^\/api\/tenants\/([0-9a-fA-F-]{36})\/members\/([0-9a-fA-F-]{36})\/role$/);
> if (setRoleMatch && req.method === "POST") {
>   requireJson(req);
>   const tenantId = setRoleMatch[1];
>   const targetUserId = setRoleMatch[2];
> 
>   await assertTenantAdmin(sb, tenantId, caller.id);
> 
>   const body = (await req.json()) as { role_name?: string; role_id?: string };
> 
>   let roleId = body.role_id?.trim();
>   if (!roleId) {
>     const roleName = (body.role_name ?? "").trim();
>     if (!roleName) throw new Error("role_name or role_id required");
>     roleId = await findRoleIdByName(sb, tenantId, roleName);
>   }
> 
>   // Ensure the target is at least a member row
>   await addMember(sb, tenantId, targetUserId, null, "active");
> 
>   await replaceMemberRoles(sb, tenantId, targetUserId, roleId);
> 
>   return json({ ok: true }, 200, cors);
> }
> ```
> 
> That’s it. Now roles can be changed anytime.
> 
> ---
> 
> # 2) Worker: include current role in members list (so UI can display it)
> 
> Right now `GET /members` returns membership + email, but not role.
> 
> Update that endpoint to also fetch role names.
> 
> Inside the existing `GET /api/tenants/:tenantId/members` handler, after `mem` is fetched, add:
> 
> ```ts
> const userIds = (mem ?? []).map((m) => m.user_id);
> 
> // fetch roles per user
> const { data: mr, error: mrErr } = await sb
>   .from("member_roles")
>   .select("user_id, role_id, roles(name)")
>   .eq("tenant_id", tenantId)
>   .in("user_id", userIds);
> 
> if (mrErr) throw new Error(mrErr.message);
> 
> const roleByUser = new Map<string, string>();
> for (const row of mr ?? []) {
>   // replace semantics: take first role name
>   const name = (row as any).roles?.name as string | undefined;
>   if (name && !roleByUser.has((row as any).user_id)) roleByUser.set((row as any).user_id, name);
> }
> ```
> 
> Then when you build `enriched`, add `role_name`:
> 
> ```ts
> return { ...m, email: u.user?.email ?? null, role_name: roleByUser.get(m.user_id) ?? null };
> ```
> 
> ---
> 
> # 3) Web UI: add role dropdown + save button
> 
> ## A) Update Member type
> In `apps/qione-web/src/routes/tenant_settings.tsx`, change the `Member` type:
> 
> ```ts
> type Member = {
>   user_id: string;
>   email: string | null;
>   status: string;
>   display_name: string | null;
>   joined_at: string;
>   role_name: string | null;
> };
> ```
> 
> ## B) Load roles for dropdown
> In `MembersTab`, add roles state + load it:
> 
> Add:
> 
> ```ts
> const [roles, setRoles] = useState<string[]>(["Owner", "Member", "Viewer"]);
> ```
> 
> Then in `load()` after members load, fetch roles list:
> 
> ```ts
> const r = await apiGet(`/api/tenants/${tenantId}/roles`);
> setRoles((r.roles ?? []).map((x: any) => x.name));
> ```
> 
> ## C) Add a per-row role picker + save
> In the members table body, add a dropdown and a Save button.
> 
> Replace your `<tbody>` mapping with this:
> 
> ```tsx
> <tbody>
>   {members.map((m) => (
>     <MemberRow
>       key={m.user_id}
>       tenantId={tenantId}
>       member={m}
>       roles={roles}
>       onSaved={load}
>     />
>   ))}
> </tbody>
> ```
> 
> Add this component at the bottom of the file:
> 
> ```tsx
> function MemberRow({
>   tenantId,
>   member,
>   roles,
>   onSaved,
> }: {
>   tenantId: string;
>   member: Member;
>   roles: string[];
>   onSaved: () => Promise<void>;
> }) {
>   const [role, setRole] = useState(member.role_name ?? "Member");
>   const [saving, setSaving] = useState(false);
>   const [err, setErr] = useState<string | null>(null);
> 
>   async function save() {
>     setErr(null);
>     setSaving(true);
>     try {
>       await apiPost(`/api/tenants/${tenantId}/members/${member.user_id}/role`, {
>         role_name: role,
>       });
>       await onSaved();
>     } catch (e: any) {
>       setErr(e.message);
>     } finally {
>       setSaving(false);
>     }
>   }
> 
>   return (
>     <tr>
>       <td style={{ padding: "6px 0" }}>{member.display_name ?? "—"}</td>
>       <td style={{ padding: "6px 0" }}>{member.email ?? "—"}</td>
>       <td style={{ padding: "6px 0" }}>{member.status}</td>
>       <td style={{ padding: "6px 0" }}>
>         <select value={role} onChange={(e) => setRole(e.target.value)} disabled={saving}>
>           {roles.map((r) => (
>             <option key={r} value={r}>
>               {r}
>             </option>
>           ))}
>         </select>
>         <button onClick={save} disabled={saving} style={{ marginLeft: 8 }}>
>           {saving ? "Saving…" : "Save"}
>         </button>
>         {err && <div style={{ color: "crimson" }}>{err}</div>}
>       </td>
>     </tr>
>   );
> }
> ```
> 
> Also update the table header to include “Role”:
> 
> ```tsx
> <th style={{ textAlign: "left", borderBottom: "1px solid #333" }}>Role</th>
> ```
> 
> ---
> 
> # 4) One blunt warning (so you don’t get surprised)
> If you keep **multi-role** capability in DB but UI uses **replace role**, that’s fine. But make sure your RBAC logic (in SQL) handles multiple roles (it already does). Replace-role is just your UX decision.
> 
> ---
> 
> If you want the next improvement that actually matters: **“disable member”** (set status to disabled) and **“resend invite”** buttons—those are the two admin actions you’ll need in real life.
