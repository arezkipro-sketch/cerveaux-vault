---
type: concept
title: "Retrieval-Augmented Generation (RAG)"
slug: retrieval-augmented-generation
tags: [llm, retrieval, methodology]
sources: ["[[llm-wiki-pattern]]"]
source_count: 1
status: active
updated: 2026-06-14
---

# Retrieval-Augmented Generation (RAG)

**Definition:** The common pattern for LLMs over documents — files are indexed (often as embeddings), relevant chunks are retrieved at query time, and the LLM generates an answer from them. Works, but the LLM rediscovers knowledge from scratch on every question; nothing accumulates between queries.

## What we know
- It is the **foil** the [[persistent-wiki]] pattern defines itself against → [[llm-wiki-pattern]].
- Same inputs as the wiki approach (a collection of sources), opposite philosophy: re-derive per query vs. compile once and maintain → [[llm-wiki-pattern]].
- NotebookLM, ChatGPT file uploads, and most document-QA systems work this way → [[llm-wiki-pattern]].
- Weakness called out: a subtle question synthesizing five documents must re-find and re-piece fragments every time → [[llm-wiki-pattern]].

## Relations
- Contrasts with [[persistent-wiki]].
- Optional wiki tooling (`qmd`) reintroduces hybrid BM25/vector retrieval *within* the wiki approach at scale → [[llm-wiki-pattern]].

## Tensions / open questions
- Not strictly either/or: the wiki can use retrieval as a navigation aid once it grows large.

## Sources
- [[llm-wiki-pattern]] — describes RAG as the baseline being improved upon.
