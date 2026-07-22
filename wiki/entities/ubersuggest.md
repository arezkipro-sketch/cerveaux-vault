---
type: entity
title: "Ubersuggest"
slug: ubersuggest
tags: [tool, seo, keyword-research, marketing-tools]
sources: ["[[apercu-ia-guide]]", "[[ai-visibility-tools]]"]
source_count: 2
status: active
updated: 2026-07-22
note: "MAJ 2026-07-22 : usage réel confirmé (site audit + SEO opportunities) via MCP, harnais-chien-expert.fr."
---

# Ubersuggest

**Definition:** SEO / keyword-research tool from [[neil-patel]] and [[np-digital]], credited as co-author/publisher on neilpatel.com content → [[apercu-ia-guide]].

## What we know
- Used for keyword research and SEO data analysis (the kind of "keyword opportunities" Patel cites AI surfacing) → [[apercu-ia-guide]].
- Sits in the keyword/SEO tooling category of [[marketing-tools-landscape]]; a competitor to [[semrush]], [[ahrefs]].
- **AI Visibility** features added to the suite: Brand Visibility, Industry Rank, Top Prompts, Competitor Visibility; flat monthly price + **unlimited projects** (agency-friendly) → [[ai-visibility-tools]]. *(Ranked #1 in NP Digital's own listicle — promotional.)*

## Usage réel via MCP (session 2026-07-21/22, harnais-chien-expert.fr)

- **Site Audit** (`site_audit` → poll `site_audit_status` → `site_audit_results` par issue id) : crawl jusqu'à 150 pages (plan gratuit), score de santé global (0-100), catégorise en `errors` / `warnings` / `recommendations`. Issues concrètes rencontrées : `have_title_duplicates`, `meta_description_empty`, `title_long`, `title_short`, `seo_non_friendly_url`.
  - **Cache non instantané** : après une correction, le score/les issues ne se mettent pas à jour immédiatement — besoin d'un `recrawl: true` explicite, et même là le crawl prend plusieurs minutes (150 pages). Toujours vérifier la fraîcheur (`last_crawled`) avant de conclure qu'un fix n'a pas marché.
  - A servi à confirmer à grande échelle qu'un bug de thème (suffixe de marque dupliqué dans le `<title>`) faisait remonter 108 pages en "title trop long" d'un coup — corriger la cause racine a fait retomber le chiffre à 29, sans toucher aux 108 pages une par une.
- **SEO Opportunities** (`seo_opportunities`, nécessite un `project_id` via `list_projects`) : combine deux familles de données dans une seule réponse —
  - `SITE_AUDIT` : recoupe (avec des seuils parfois différents) les mêmes catégories que le site audit brut.
  - `KEYWORD_OPPORTUNITY` : sous-types `quick_win` (mot-clé déjà positionné avec du volume, gain rapide possible), `new_content` (mot-clé à volume réel sans page qui ranke dessus — vrai trou de contenu), `existing_content` (page existante à renforcer). Chaque item porte `impact`/`effort` (low/medium/high) — utile pour prioriser sans deviner.
  - Recoupé avec [[pushrank]] sur le même site : les deux outils remontent des listes qui se chevauchent partiellement (ex: mêmes pages en `decay`/`quick_win`) mais avec des critères différents — croiser les deux plutôt que se fier à un seul.
- **Fiabilité de service observée** : plusieurs erreurs 503/504 (Gateway Timeout) sur `serp_analysis` et `domain_top_pages` lors d'usage intensif en session — ne pas insister en boucle, réessayer une fois puis basculer sur une autre méthode si le service reste indisponible.

## Relations
- Owned by [[np-digital]] / [[neil-patel]].
- Category peer of [[semrush]] in [[marketing-tools-landscape]].
- Usage croisé avec [[pushrank]] sur le même projet e-commerce ; voir aussi [[seo-audit]] pour la méthodologie générale.

## Sources
- [[apercu-ia-guide]] — bylined publisher/tool.
- [[ai-visibility-tools]] — Ubersuggest AI Visibility features + pricing model.
- Usage réel session 2026-07-21/22 sur harnais-chien-expert.fr (pas de source `raw/` — expérience directe via l'intégration MCP).
