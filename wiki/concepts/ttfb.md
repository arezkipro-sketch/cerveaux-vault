---
type: concept
title: "TTFB (Time To First Byte)"
slug: ttfb
tags: [seo, technical-seo, performance, server]
sources: ["[[crawl-budget-guide]]", "[[shopify-debug-slow-loading]]"]
source_count: 2
status: active
updated: 2026-06-20
---

# TTFB (Time To First Byte)

**Definition:** The delay between a request (click/bot fetch) and the arrival of the first byte of content — the server's initial response time. Low TTFB signals a responsive server, which raises both UX and crawl efficiency → [[crawl-budget-guide]].

## What we know
- **Crawl lever:** slow TTFB → Googlebot throttles down (won't force the pace) → lower [[crawl-budget]]. Fast TTFB → Googlebot raises crawl rate → more pages crawled per visit → [[crawl-budget-guide]].
- **How to reduce it** → [[crawl-budget-guide]]: use a **CDN**, enable **Gzip/Brotli** compression, optimize database queries, monitor continuously (PageSpeed Insights, Google Search Console).
- Also a UX issue (the "silence" before content appears) — not only technical SEO.

## Causes TTFB lent sur Shopify Liquid

Seuil "good" : < 0.8 s. Les storefronts Liquid Shopify sont généralement rapides côté serveur. Quand le TTFB est lent, 2 causes principales :

1. **Liquid complexe** — boucles imbriquées (nested loops) ou appels de données inutiles → rendu côté serveur ralenti. Diagnostic : Theme Inspector Chrome Extension → flame graph. Remédiation : simplifier le code ou architecture hybride (Liquid pour le visible + JS asynchrone pour le reste).

2. **Problème serveur Shopify temporaire** — rare, hors du contrôle du développeur. Signal : baisse simultanée sur plusieurs boutiques.

→ [[shopify-debug-slow-loading]], [[shopify-liquid-performance]]

## Relations
- Drives [[crawl-budget]] (Rate Limit) and feeds server-response time in [[core-web-vitals]] (LCP).
- Monitored via [[google-search-console]] / PageSpeed Insights.
- Causes Shopify-spécifiques → [[shopify-liquid-performance]].

## Tensions / open questions
- No "good" TTFB threshold given in the source (Google guidance commonly cites ~0.8 s).

## Sources
- [[crawl-budget-guide]] — TTFB as the key to raising the crawl rate limit; reduction tactics.
- [[shopify-debug-slow-loading]] — Liquid complexe (nested loops) comme cause principale de TTFB lent sur Shopify ; méthode de diagnostic Theme Inspector.
