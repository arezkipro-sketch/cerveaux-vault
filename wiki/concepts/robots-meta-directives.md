---
type: concept
title: "Robots Meta Directives (noindex / X-Robots-Tag)"
slug: robots-meta-directives
tags: [seo, technical-seo, indexation, noindex]
sources: ["[[crawl-budget-guide]]"]
source_count: 1
status: active
updated: 2026-06-18
---

# Robots Meta Directives (noindex / X-Robots-Tag)

**Definition:** Page- and file-level instructions that control **indexing** (vs [[robots-txt]], which controls crawling). The `noindex` directive lets Google crawl a page but keeps it out of search results — "the block that permits the crawl" → [[crawl-budget-guide]].

## What we know
- **`noindex` meta tag** (HTML pages): Google may visit and understand the page's role, but won't show it in results. Strategic uses → [[crawl-budget-guide]]:
  - Pass internal-link relevance to other pages while staying unlisted.
  - Avoid duplicate near-identical categories competing with each other.
  - Keep mandatory/low-value pages out of the index (privacy policy, ToS, technical pages).
- **`X-Robots-Tag`** (HTTP header): applies `noindex` / `nofollow` / `noarchive` to **non-HTML files** (PDF, images, video, spreadsheets) that would otherwise get indexed → [[crawl-budget-guide]].

## Relations
- Complements [[robots-txt]] (crawl control) in managing [[crawl-budget]] and indexation.
- Distinct from [[canonical-tag]] (dedup hint) — noindex is a hard exclusion from results.

## Tensions / open questions
- A page must be crawlable for Google to *see* a `noindex` — don't also block it in robots.txt, or the directive is never read.

## Sources
- [[crawl-budget-guide]] — noindex vs robots.txt; X-Robots-Tag for non-HTML files.
