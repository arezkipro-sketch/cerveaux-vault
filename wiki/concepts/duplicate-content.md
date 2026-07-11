---
title: "Contenu dupliqué (Duplicate Content)"
slug: duplicate-content
page-type: concept
domain: seo
tags: [seo, duplicate-content, canonical, indexation, technique]
sources:
  - "[[reussir-referencement-web-andrieu-2020]]"
related:
  - "[[canonical-tag]]"
  - "[[hreflang]]"
  - "[[robots-meta-directives]]"
  - "[[crawl-budget]]"
  - "[[reussir-referencement-web-andrieu-2020]]"
---

# Contenu dupliqué (Duplicate Content)

Situation où le même contenu est accessible via plusieurs URLs différentes. Google ne sait quelle version indexer et peut diluer le PageRank ou ignorer les doublons.

## Causes principales
- HTTP vs HTTPS (non-redirigé)
- www vs non-www (non-unifié)
- Paramètres d'URL (`?sort=price`, `?ref=newsletter`)
- Pagination (`/page/2`, `/page/3`)
- Sessions IDs dans l'URL
- Versions mobile/desktop séparées (non-responsive)
- Reprises de contenu identique sur plusieurs pages

## Solutions
1. **Balise canonical** `<link rel="canonical" href="URL-de-référence">` — indique à Google l'URL à indexer
2. **Redirection 301** — fusionne le PageRank vers une URL unique (www → non-www, HTTP → HTTPS)
3. **Paramètres GSC** — déclarer les paramètres d'URL à ignorer dans Search Console
4. **noindex** — sur les pages dupliquées volontairement maintenues
5. **Hreflang** — pour les versions linguistiques (évite qu'elles soient considérées comme duplication)

## Règle clé
Une page = une URL canonique. Toute autre URL menant au même contenu doit rediriger ou porter un canonical.
