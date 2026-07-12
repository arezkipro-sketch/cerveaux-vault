---
type: source
title: LLM Wiki — A Pattern for Personal Knowledge Bases
slug: llm-wiki-pattern
raw: "[[llm-wiki-idea]]"
source-url: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
source-type: gist
author: Andrej Karpathy
date_published: 2026-06-14
date_ingested: 2026-06-14
tags:
  - knowledge-management
  - llm
  - second-brain
  - wiki
  - methodology
status: active
---

# LLM Wiki — A Pattern for Personal Knowledge Bases — Summary

**One-liner:** An LLM incrementally builds and maintains a persistent, interlinked markdown wiki between you and your raw sources — compiling knowledge once and keeping it current, instead of re-deriving it on every query like RAG.

## Key takeaways
- The wiki is a **compounding artifact**: cross-references, contradiction flags, and synthesis are built up over time, not regenerated per question. This is the core break from [[retrieval-augmented-generation]].
- Three layers: immutable **raw sources**, an LLM-owned **wiki**, and a **schema** config that disciplines the LLM. See [[persistent-wiki]].
- Four operations: **ingest**, **query**, **lint**, (and evolve the schema). A single ingest may touch 10–15 wiki pages.
- Division of labor: human curates/directs/asks; LLM reads/summarizes/cross-references/files/maintains.
- `index.md` (content catalog) + `log.md` (chronological, greppable) navigate the wiki without embedding-based RAG at moderate scale.
- The pattern is a modern realization of Vannevar Bush's [[memex]] — solving the maintenance problem Bush couldn't.

## Notable claims (with locations)
- "Humans abandon wikis because the maintenance burden grows faster than the value." — *(§ Why it works)*
- Index-first navigation works at ~100 sources / hundreds of pages without vector search. — *(§ Indexing and logging)*
- "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase." — *(§ The core idea)*

## Entities introduced or touched
- [[memex]] (Vannevar Bush, 1945) — intellectual ancestor.
- Tooling mentioned: Obsidian, Obsidian Web Clipper, Dataview, Marp, `qmd`.

## Connections / contradictions
- Defines itself **in contrast to** [[retrieval-augmented-generation]] — same inputs, opposite philosophy (accumulate vs. re-derive).
- Operationalized by this vault's `CLAUDE.md` schema. See [[persistent-wiki]].
- No internal contradictions; it is the founding/normative document for this vault.

## Open questions
- At what scale does index-first navigation break and require `qmd` / vector search here?
- Should this vault's wiki pages be written in French (vault locale) or English (current default)?
