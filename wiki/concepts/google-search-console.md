---
type: concept
title: "Google Search Console (GSC)"
slug: google-search-console
tags: [seo, technical, search-console, indexation]
sources: ["[[semrush-gsc-errors]]", "[[core-web-vitals]]", "[[vengeonsp-12-agents-seo-ia]]"]
source_count: 3
status: active
updated: 2026-07-07
---

# Google Search Console (GSC)

**Definition:** Google's free service to monitor and manage a site's presence in search results — and to surface crawl/index errors Googlebot encounters. → [[semrush-gsc-errors]]

## What we know
- **Why fix errors:** unresolved errors block indexing (pages won't appear) and hurt UX → lower rankings. → [[semrush-gsc-errors]]
- **Common errors:** 404s, redirect errors, indexing/coverage issues. → [[semrush-gsc-errors]]
- Also exposes the link report (free backlink source) and search performance (impressions/clicks/CTR/position).
- **Core Web Vitals report:** shows each page as good / needs-work / poor using **field data** (real users), per LCP/INP/CLS → [[core-web-vitals]].

## Les 6 analyses GSC à faire en priorité — [[vengeonsp-12-agents-seo-ia]]

**Principe : 80% des gains du prochain trimestre se cachent dans les pages déjà existantes.** Les exécuter dans cet ordre (du plus actionnable au plus complexe) :

| # | Analyse | Ce qu'on cherche | Action |
|---|---|---|---|
| **a** | **Striking distance** | Pages/requêtes aux positions 4-15 | 1-2 optimisations on-page → page 1 |
| **b** | **Pages en déclin** | Pages perdant le plus de clics vs période précédente | Diagnostiquer cause (algo / concurrent / content decay / cannibalisation) |
| **c** | **Outliers CTR** | Pages top 10 avec CTR sous benchmark de position | Réécriture title/meta uniquement |
| **d** | **Fuites d'impressions** | Fortes impressions + peu de clics | Mismatch d'intention de recherche ou feature SERP absente |
| **e** | **Intention cachée** | Requêtes où la page rank sans les avoir intentionnellement ciblées | Parfois la plus grosse opportunité non visible |
| **f** | **Cannibalisation** | Plusieurs URLs en compétition sur la même requête | → [[keyword-cannibalization]] |

**Input nécessaire :** rapport Performance GSC → 90 derniers jours vs 90 jours précédents → dimensions Page + Requête → export CSV.

**Priorité opérationnelle :** commencer par la striking distance (a) → les wins les plus rapides. Puis déclin (b) → stopper la perte. Puis CTR outliers (c) → gains de trafic sans changer les rankings.

## Relations
- The search-side counterpart of [[google-analytics-4]]; errors tie to [[http-status-codes-seo]], [[301-redirect]]/[[302-redirect]], [[google-bots]], [[crawl-budget]].
- Free alternative to paid backlink/audit tools ([[backlinks]], [[seo-audit]]).

## Tensions / open questions
- Per-error-type fixes not all captured here.

## Sources
- [[semrush-gsc-errors]] — GSC errors, why they matter, common types
- [[core-web-vitals]] — GSC CWV report (field data) as the primary monitoring tool.
- [[vengeonsp-12-agents-seo-ia]] — les 6 analyses GSC structurées (striking distance / déclin / CTR outliers / fuites / intention cachée / cannibalisation).
