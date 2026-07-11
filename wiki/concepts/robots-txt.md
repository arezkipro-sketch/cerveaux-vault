---
type: concept
title: "robots.txt"
slug: robots-txt
tags: [seo, technical-seo, crawling, indexation]
sources: ["[[crawl-budget-guide]]"]
source_count: 1
status: active
updated: 2026-06-18
---

# robots.txt

**Definition:** A text file at the site root — Googlebot's **first point of contact** — that instructs crawlers which areas may or may not be crawled. It steers [[crawl-budget]] but is **not a security tool** (anyone can read it) → [[crawl-budget-guide]].

## What we know
- Directives → [[crawl-budget-guide]]:
  - **User-agent:** which bot the rules apply to (Googlebot, Bingbot…).
  - **Disallow:** routes/directories not to crawl (cart, internal search, infinite filters).
  - **Allow:** exceptions inside a blocked directory to keep crawlable.
- Blocks **crawling** (vs `noindex`, which blocks *indexing* but allows crawl) → [[robots-meta-directives]].
- Example: `Disallow: /panier/` + `Disallow: /filtres/` + `Allow: /filtres/categorie-populaire/`.

## Relations
- Primary lever for [[crawl-budget]] / Crawl Waste; complements [[robots-meta-directives]] and [[canonical-tag]].
- Read by [[google-bots]]; sits alongside the [[xml-sitemap]] in technical SEO setup.

## Tensions / open questions
- A `Disallow`-blocked page can still be indexed if linked elsewhere (no crawl ≠ no index) — use `noindex` to keep out of results.

## Sources
- [[crawl-budget-guide]] — robots.txt as crawl-budget steering; directive syntax + example.
