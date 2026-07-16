---
layout: page
title: Entities
slug: entities
summary: ""
status: publish
created_at: "2026-07-16T06:19:39-04:00"
updated_at: "2026-07-16T06:19:39-04:00"
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: f395961965134e83b7d45d7eda2d59f5
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Domain Entities

## Workspace

Container for financial data ownership.

## User/Profile

Person using the system. Static during MVP, authenticated later.

## Account

A ledger account. Can represent bank accounts, cash, credit cards, loans, income, expenses, assets, liabilities, equity, or tax categories.

## Transaction

A real-world financial event.

## Split

One accounting line inside a transaction. Holds debit or credit amount and account reference.

## Payee

Person, company, platform, or counterparty.

## Rule

Instruction for automatic classification or split suggestion.

## Attachment

Receipt, statement, screenshot, or supporting file.
