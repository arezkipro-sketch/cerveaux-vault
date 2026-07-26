---
type: concept
title: "Site Health"
slug: site-health
tags: [seo, technical, site-audit, performance]
sources: ["[[semrush-site-health]]", "[[core-web-vitals]]"]
source_count: 2
status: active
updated: 2026-07-25
---

# Site Health

**Definition:** The foundation that lets a site perform — a composite score across security, usability and search-optimisation, measured via a site audit. → [[semrush-site-health]]

## What we know
- **Components:** crawlability, on-page SEO, technical SEO (structure, mobile), mobile-friendliness, speed. → [[semrush-site-health]]
- A healthy site → more traffic + conversions; tools produce an overall health score (weights vary). → [[semrush-site-health]]


## Règle apprise — faux positifs de crawl et rate limiting Shopify

Lorsqu'un outil d'audit remonte de très gros volumes de liens cassés ou de `canonical 404`, vérifier d'abord le statut HTTP exact. Sur harnais-chien-expert.fr (session PushRank 2026-07-25), les contrôles rapides ont surtout produit des `429` — signal de rate limiting — et non de vraies `404`. Une réponse `429` signifie que le serveur/CDN ralentit le crawler ; ce n'est pas une preuve que la page est cassée.

Règle opérationnelle : ne jamais corriger en masse des liens internes ou canonicals à partir d'un compteur agrégé. Échantillonner les URLs, vérifier lentement les statuts, puis corriger uniquement les `404` confirmées. Voir [[pushrank]], [[http-status-codes-seo]], [[crawl-budget]] et [[seo-audit]].

## Relations
- An aggregate over on/off/technical SEO ([[off-page-seo]], [[mobile-seo]]) + crawlability ([[google-bots]], [[crawl-budget]]); operationalised by [[seo-audit]] and monitored via [[google-search-console]].

## Tensions / open questions
- "Health score" is tool-specific, not a Google signal.

## Sources
- [[semrush-site-health]] — definition, audit components
- [[core-web-vitals]] — CWV (LCP/INP/CLS) + Page Experience as the measurable performance/UX layer of site health.
