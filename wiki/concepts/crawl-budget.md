---
type: concept
title: "Crawl Budget (Budget de Crawl)"
slug: crawl-budget
tags: [seo, technical-seo, crawling, indexation]
sources: ["[[jotaro-seo-google-bots]]", "[[crawl-budget-guide]]", "[[content-pruning]]"]
source_count: 3
status: active
updated: 2026-06-19
---

# Crawl Budget

**Definition:** The finite resources Google's [[google-bots]] allocate to crawling a given site in a given period. Mismanaged, it produces **Crawl Waste** — Googlebot spending budget on no-value pages while strategic ones go uncrawled → [[crawl-budget-guide]].

## The two factors (Rate Limit × Demand)
- **Crawl Rate Limit:** Googlebot's technical capacity to crawl without overloading the server. Fast/stable server → higher limit; slowness/errors → Google throttles down → [[crawl-budget-guide]].
- **Crawl Demand:** perceived relevance of pages. Recent, high-traffic, useful pages are crawled more often → [[crawl-budget-guide]].
- Implication: a fast site is not enough — pages must also *deserve* attention → [[crawl-budget-guide]].

## Crawl Waste — common causes
- Infinite e-commerce filters (color/size/price), internal search-result pages, duplicate/parameter URLs, recurring server errors → [[crawl-budget-guide]].
- Also (earlier source): 404s, redirect chains, paginated/duplicate/thin content → [[jotaro-seo-google-bots]].
- Test each page: ranking potential? qualified organic traffic? contributes to strategy? If "no" → block crawl/index → [[crawl-budget-guide]].

## Access-control levers
- **[[robots-txt]]** — first contact; Disallow no-SEO routes (cart, internal search, filters), Allow exceptions; blocks *crawling* → [[crawl-budget-guide]].
- **[[robots-meta-directives]]** — `noindex` (crawl allowed, indexing blocked; preserves internal-link relevance) and `X-Robots-Tag` (noindex via HTTP header for non-HTML: PDF/images/video) → [[crawl-budget-guide]].
- **[[ttfb]]** — lower Time To First Byte → Googlebot raises crawl rate → [[crawl-budget-guide]].
- Fix **404/503** errors (waste + instability signal) via [[google-search-console]] + [[301-redirect]] → [[crawl-budget-guide]].
- **[[xml-sitemap]]** (roadmap: priorities/hierarchy/update freq) + logical [[maillage-interne]] → [[crawl-budget-guide]].

## Relations
- Wasted by [[http-status-codes-seo]] errors; conserved by [[canonical-tag]], [[robots-txt]], [[robots-meta-directives]].
- Guided by [[maillage-interne]] + [[xml-sitemap]]; throttled by server speed → ties to [[ttfb]] / [[core-web-vitals]].
- Part of the [[seo-audit]] technical checklist; framed as a **business/ROI** lever, not just hygiene.

## Tensions / open questions
- Matters mainly for larger sites (generally > ~1000 pages); Google's exact allocation formula is undocumented.
- Source closes with an NP Digital agency pitch.

## Sources
- [[jotaro-seo-google-bots]] — introduces concept (truncated, limited detail).
- [[crawl-budget-guide]] — full model: Rate Limit × Demand, Crawl Waste, robots.txt/noindex/X-Robots-Tag, TTFB, 404/503, sitemap+structure.
- [[content-pruning]] — removing useless URLs frees crawl budget for strategic pages.
