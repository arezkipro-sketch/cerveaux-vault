---
type: concept
title: "Google Search Console (GSC)"
slug: google-search-console
tags: [seo, technical, search-console, indexation]
sources: ["[[semrush-gsc-errors]]", "[[core-web-vitals]]"]
source_count: 2
status: active
updated: 2026-06-18
---

# Google Search Console (GSC)

**Definition:** Google's free service to monitor and manage a site's presence in search results — and to surface crawl/index errors Googlebot encounters. → [[semrush-gsc-errors]]

## What we know
- **Why fix errors:** unresolved errors block indexing (pages won't appear) and hurt UX → lower rankings. → [[semrush-gsc-errors]]
- **Common errors:** 404s, redirect errors, indexing/coverage issues. → [[semrush-gsc-errors]]
- Also exposes the link report (free backlink source) and search performance (impressions/clicks/CTR/position).
- **Core Web Vitals report:** shows each page as good / needs-work / poor using **field data** (real users), per LCP/INP/CLS → [[core-web-vitals]].

## Relations
- The search-side counterpart of [[google-analytics-4]]; errors tie to [[http-status-codes-seo]], [[301-redirect]]/[[302-redirect]], [[google-bots]], [[crawl-budget]].
- Free alternative to paid backlink/audit tools ([[backlinks]], [[seo-audit]]).

## Tensions / open questions
- Per-error-type fixes not all captured here.

## Sources
- [[semrush-gsc-errors]] — GSC errors, why they matter, common types
- [[core-web-vitals]] — GSC CWV report (field data) as the primary monitoring tool.
