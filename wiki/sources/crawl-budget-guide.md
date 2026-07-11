---
type: source
title: "Crawl Budget : guide pour optimiser votre SEO"
slug: crawl-budget-guide
raw: "[[raw/assets/Crawl Budget  guide pour optimiser votre SEO.md]]"
source_url: "https://neilpatel.com/fr/blog/crawl-budget-le-guide/"
author: "Neil Patel (NP Digital)"
date_published: 2025-10-30
date_ingested: 2026-06-18
tags: [crawl-budget, technical-seo, crawling, indexation, robots-txt]
status: active
---

# Crawl Budget : guide pour optimiser votre SEO — Summary

**One-liner:** Crawl Budget is the finite resource Google spends crawling your site; this guide explains the Rate-Limit × Demand model and the technical levers (robots.txt, noindex, X-Robots-Tag, TTFB, error handling, sitemap) to eliminate Crawl Waste and steer Googlebot to revenue pages.

## Key takeaways
- **Crawl Budget = finite.** Misused → **Crawl Waste**: Googlebot burns resources on no-value pages and neglects strategic ones.
- **Two factors:** **Crawl Rate Limit** (server capacity — fast/stable raises it, slow/errors lowers it) × **Crawl Demand** (page relevance — recent/high-traffic/useful pages crawled more). A fast site alone isn't enough.
- **Crawl Waste sources:** infinite e-commerce filters, internal search pages, duplicate/parameter URLs, recurring server errors.
- **Access control:**
  - **robots.txt** — first contact; `User-agent` / `Disallow` (cart, internal search, filters) / `Allow` exceptions. Blocks *crawling*, not security.
  - **noindex meta** — allows crawl, blocks indexing; preserves internal-link relevance; for duplicates and low-value pages (privacy/ToS).
  - **X-Robots-Tag** — `noindex` via HTTP header for non-HTML files (PDF, images, video, spreadsheets).
- **TTFB (Time To First Byte):** lower TTFB → Googlebot trusts the server and raises crawl rate. Reduce via CDN, Gzip/Brotli, DB-query optimization, monitoring (PSI/GSC).
- **404 & 503 errors** waste budget and signal instability → reduced crawl frequency. Fix via GSC monitoring, broken-link repair, 301 redirects; keep 503 truly temporary.
- **Sitemap XML** = roadmap (priorities, hierarchy, update frequency); pair with logical internal structure/linking.

## Notable framing (with locations)
- "Optimizing Crawl Budget = a real business strategy, not just a technical practice" → better indexation, higher crawl frequency, **SEO ROI** *(§Optimiser… ROI)*.
- robots.txt blocks crawling; noindex blocks indexing but allows crawl — "the block that permits the crawl" *(§noindex)*.

## Entities introduced or touched
- [[neil-patel]], [[np-digital]] (closes with NP Digital France agency pitch)

## Concepts introduced or touched
- [[crawl-budget]], [[robots-txt]], [[robots-meta-directives]], [[ttfb]], [[google-bots]], [[http-status-codes-seo]], [[301-redirect]], [[xml-sitemap]], [[maillage-interne]], [[google-search-console]]

## Connections / contradictions
- Far richer than the earlier truncated [[jotaro-seo-google-bots]] crawl-budget mention — now the primary source for the concept.
- TTFB connects crawl budget to server performance → overlaps [[core-web-vitals]] (LCP server response).

## Open questions
- No site-size threshold given for when crawl budget actually matters (generally large sites).
