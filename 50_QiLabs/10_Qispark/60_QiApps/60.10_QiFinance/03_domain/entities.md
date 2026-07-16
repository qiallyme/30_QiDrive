---
layout: page
title: Entities
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
