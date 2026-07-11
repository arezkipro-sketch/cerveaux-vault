---
type: concept
title: "HTTP Status Codes and SEO"
slug: http-status-codes-seo
tags: [seo, technical-seo, http, crawling, indexation]
sources: ["[[jotaro-seo-http-errors]]", "[[crawl-budget-guide]]", "[[noiise-fiches-produits-seo]]"]
source_count: 3
status: active
updated: 2026-06-19
---

# HTTP Status Codes and SEO

**Definition:** HTTP status codes are 3-digit server responses to requests. In an SEO context they determine whether pages are crawlable, indexable, and authoritative — making them a core technical SEO concern.

## Code families
- **1xx** — informational signals.
- **2xx** — success (page served correctly).
- **3xx** — redirects (301 permanent redirect is SEO-safe; passes link juice).
- **4xx** — client errors (404 = page not found; most damaging for SEO). **410 = Gone** : ressource volontairement et définitivement supprimée. Plus fort signal que 404 → sortie plus rapide de l'index, préserve le budget de crawl. Cas e-commerce : gamme/catégorie de produits totalement arrêtée → 410 plutôt que 301 → [[noiise-fiches-produits-seo]], [[crawl-budget]].
- **5xx** — server errors (500 = internal; **503 = temporary unavailable**). Recurring 503s signal an unstable/poorly-maintained site → Google cuts crawl frequency → [[crawl-budget-guide]].

## SEO implications
- **Crawling**: errors prevent robots from accessing pages → those pages are not indexed → lost SERP visibility → [[jotaro-seo-http-errors]].
- **Link juice**: a 404 on an inbound-linked page **breaks authority transfer** — the link equity is lost → [[link-juice]] → [[jotaro-seo-http-errors]].
- **User experience**: broken pages → high bounce rate → engines perceive lower quality → [[jotaro-seo-http-errors]].
- **Crawl budget**: frequent errors waste crawl budget on unreachable pages → [[jotaro-seo-http-errors]].

## Recommended practices
- Monitor: Screaming Frog (crawl tool), Google Search Console (GSC) → [[jotaro-seo-http-errors]].
- Fix 404s with **301 redirect** to a relevant live page — but **not every 404 needs a redirect**; legitimately deprecated pages can stay 404 → [[jotaro-seo-http-errors]].
- Resolve 500 errors at the server/infrastructure level.

## Relations
- Part of [[technical-seo]] *(TODO: create page)*.
- Mentioned alongside [[link-juice]] and user experience / SXO.

## Tensions / open questions
- Crawl budget impact depth varies by site size — not addressed in the source. Candidate for a deeper technical SEO source.

## Sources
- [[jotaro-seo-http-errors]] — primary source; 8-part X thread with practical advice.
- [[crawl-budget-guide]] — 404/503 as crawl-budget waste + instability signal; keep 503 truly temporary; fix via GSC + 301.
- [[noiise-fiches-produits-seo]] — 410 Gone pour gamme produit arrêtée (vs 301 vers similaire/catégorie mère) en gestion de rupture de stock e-commerce.
