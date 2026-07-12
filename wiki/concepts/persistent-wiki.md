---
type: concept
title: "Persistent Compounding Wiki"
slug: persistent-wiki
tags: [knowledge-management, methodology, second-brain]
sources: ["[[llm-wiki-pattern]]"]
source_count: 1
status: active
updated: 2026-06-14
---

# Persistent Compounding Wiki

**Definition:** A structured, interlinked collection of markdown files that an LLM builds and maintains between a human and their raw sources. Unlike query-time retrieval, the synthesis is compiled once when a source is ingested and then kept current — so cross-references, contradiction flags, and the overall thesis accumulate and compound over time.

## What we know
- It sits as a middle layer between immutable raw sources and the human → [[llm-wiki-pattern]].
- Built from three layers: raw sources (immutable), the wiki (LLM-owned), and a schema config → [[llm-wiki-pattern]].
- Maintained via four operations — ingest, query, lint, evolve — defined in this vault's `CLAUDE.md` → [[llm-wiki-pattern]].
- Its advantage over [[retrieval-augmented-generation]] is *accumulation*: nothing is re-derived per query → [[llm-wiki-pattern]].
- Modern realization of the [[memex]] vision, with the LLM doing maintenance → [[llm-wiki-pattern]].

## Relations
- Contrasts with [[retrieval-augmented-generation]].
- Descendant of [[memex]].
- Governed by the schema in `CLAUDE.md`.

## Tensions / open questions
- Navigation scaling: index-first works to ~hundreds of pages; beyond that may need search tooling *(unsourced beyond § Optional tools)*.

## Sources
- [[llm-wiki-pattern]] — defines the pattern in full.
