---
type: concept
title: "Core Web Vitals (CWV)"
slug: core-web-vitals
tags: [core-web-vitals, technical-seo, performance, ux, mobile-seo, google]
sources: ["[[core-web-vitals]]", "[[shopify-debug-slow-loading]]"]
source_count: 2
status: active
updated: 2026-06-20
---

# Core Web Vitals (CWV)

**Definition:** Google's set of three UX performance metrics — loading, interactivity, and visual stability — that quantify how a page *feels* to a real user. A confirmed Google ranking factor since **May 2021**, within the broader Page Experience signals → [[core-web-vitals]].

## FCP (First Contentful Paint) — métrique diagnostique intermédiaire

**FCP** n'est pas un Core Web Vital, mais c'est une métrique de chargement clé pour le diagnostic. Même point de départ que TTFB et LCP.

- **Définition :** temps entre la requête et le premier rendu de contenu à l'écran
- **Seuil "good" :** < 1.8 s
- **Rôle :** le gap TTFB→FCP pointe vers des problèmes de rendu initial (render-blocking, anti-flicker) ; le gap FCP→LCP pointe vers des problèmes spécifiques à l'élément LCP

→ [[shopify-debug-slow-loading]]

## The three pillars (+ "good" thresholds)
- **LCP — Largest Contentful Paint:** time to render the largest visible element (loading). **< 2.5 s** → [[core-web-vitals]].
- **INP — Interaction to Next Paint:** responsiveness across *all* interactions in a visit. **< 100 ms**. Replaced **FID** (First Input Delay) as a Core Web Vital from **March 2024** — FID measured only the first interaction and was inaccurate on Android → [[core-web-vitals]].
- **CLS — Cumulative Layout Shift:** sum of unexpected layout movements (visual stability). **< 0.1** → [[core-web-vitals]].

## Field data vs lab data
- **Lab data** = controlled environment (Lighthouse, Chrome DevTools) — good for debugging.
- **Field data** = real users via **CrUX** (Chrome User Experience Report) — *this is what Google uses to score CWV*. Lab-only optimization misleads → [[core-web-vitals]].

## Measurement tools
- Google **Search Console** CWV report (field), **PageSpeed Insights** (field+lab+score), **Lighthouse** (open-source, lab, 0-100), **CrUX** (public field DB, competitor comparison) → [[core-web-vitals]].

## Optimization levers
- **LCP:** fast server + CDN, minify CSS/JS/HTML, defer/reduce JS, inline critical CSS, lazy-load media, preload fonts → [[core-web-vitals]].
- **INP:** minimize JS, split long tasks, Web Workers, CSS animations over JS, avoid costly CSS props → [[core-web-vitals]].
- **CLS:** explicit image/video dimensions, reserve space for ads/dynamic content, font-display: swap + preload, no late content insertion → [[core-web-vitals]].

## Lecture des gaps TTFB→FCP→LCP (méthode RUM)

Les trois métriques partagent le même point de départ. Lire les gaps entre elles oriente le diagnostic :

| Gap dominant | Cause probable |
|---|---|
| TTFB lent | Serveur / Liquid complexe (Shopify) |
| TTFB rapide → FCP très lent | Render-blocking / anti-flicker snippet |
| FCP rapide → LCP très lent | Problème sur l'élément LCP (lazy-load, transition, JS rendering) |

Outil : TREO sitespeed (données CrUX gratuites). Analyser par type de page et mobile vs desktop séparément.

→ [[shopify-debug-slow-loading]], [[shopify-liquid-performance]]

## Relations
- A technical pillar of [[site-health]] and the [[seo-audit]]; part of [[what-is-seo]]'s technical pillar.
- Mobile-first dependence ties to [[mobile-seo]]; field data surfaces in [[google-search-console]].
- Server response time ([[ttfb]]) feeds LCP and also gates [[crawl-budget]].
- Good CWV → lower bounce, higher conversion → supports [[landing-page]] UX.
- Speed reduces pogo-sticking → feeds Google's behavioral [[navboost]] layer.

## Tensions / open questions
- Possible future 4th metric (animation smoothness) and AI-driven optimization are speculative.
- Page Experience is one signal among many — not a silver bullet for ranking.

## Sources
- [[core-web-vitals]] — Neil Patel FR guide: pillars, thresholds, tools, per-metric optimization, mistakes.
- [[shopify-debug-slow-loading]] — Sia Karamalegos (performance.shopify.com) : FCP comme métrique diagnostique, méthode RUM gap analysis, causes Shopify-specific par métrique.
