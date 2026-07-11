---
type: concept
title: "URL Structure (SEO-Friendly)"
slug: url-structure
tags: [seo, technical-seo, architecture, crawling]
sources: ["[[semrush-seo-checklist-41]]"]
source_count: 1
status: active
updated: 2026-06-19
---

# URL Structure (SEO-Friendly)

**Definition:** The format and composition of page URLs, optimized to help both search engines and users understand page content at a glance.

## What we know

**Good URL:**
```
https://www.domaine.com/chaussures-rouges/
```

**Bad URL (chaîne de requête non descriptive):**
```
https://www.domaine.com/categorie.php?id=32
```

**Rules:**
- Use **hyphens** (`-`) to separate words. ❌ underscores (`_`), ❌ spaces.
- Keep URLs as **short** as possible — Backlinko study: shorter URLs tend to rank higher.
- Make URLs **descriptive** — humans and crawlers should understand the topic from the URL alone.
- Use **lowercase** (avoid mixed case — URL is case-sensitive on most servers).
- Avoid parameters and session IDs where possible.

## Relations
- One of the 12 Technical SEO checkpoints in [[semrush-seo-checklist-41]].
- Works alongside [[xml-sitemap]] (sitemap lists canonical URLs) and [[canonical-tag]] (de-duplicates near-identical URLs).
- A clean URL structure reduces [[crawl-budget]] waste: crawlers parse meaningful path segments faster.
- Short, keyword-rich URLs reinforce [[keyword-mapping]] signals.

## Tensions / open questions
- How much does URL length still matter vs. other signals? Correlation exists but causation unclear.
- Category-prefix URLs (`/blog/post-name`) vs. flat URLs (`/post-name`) — trade-off between hierarchy clarity and URL length.

## Sources
- [[semrush-seo-checklist-41]] — étape 22 ; règles URL SEO-friendly : traits d'union, courtes, descriptives.
