---
layout: page
title: Single Financial Universe
slug: ""
summary: ""
status: publish
created_at: ""
updated_at: ""
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ""
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Single Financial Universe Doctrine

## Doctrine Statement

QiFinance treats a person's financial life as one economic universe.

Personal money, gig-work money, business money, family obligations, reimbursements, debts, assets, and informal IOUs all belong to the same financial reality. The system should not force users to split their life into separate apps or separate databases just because the activity has different reporting purposes.

## Core Rule

Personal and business data should not be isolated into separate databases.

Separation happens through:

- accounts
- account types
- tags
- classifications
- counterparties
- views
- reports
- tax treatment metadata

The same underlying event can support multiple views without duplicating the event.

## Why This Matters

Modern users often have blended financial lives:

- gig work income
- personal bills
- vehicle expenses used partly for work
- family caregiving costs
- reimbursements
- informal loans
- subscriptions
- cash transfers
- multiple cards and bank accounts

Traditional software usually asks: "Is this personal or business?"

QiFinance asks: "What happened, who was involved, what accounts changed, what evidence exists, and how should this be reported?"

## Product Implication

The user should enter or import a transaction once. QiFinance should allow that transaction to appear in different contexts:

- personal budget
- business profit/loss
- tax deduction report
- reimbursement tracker
- counterparty history
- evidence packet
- cash-flow forecast

## Non-Negotiable

Do not create separate personal and business ledgers as isolated systems.

A business view can be filtered. A personal view can be filtered. A tax view can be filtered. But the financial universe remains unified.
