---
title: "Improving your online store performance"
slug: shopify-improve-store-performance
page-type: source-note
domain: seo
tags: [seo, technical-seo, performance, shopify, core-web-vitals, lcp, inp, cls, ecommerce]
sources: []
related:
  - "[[shopify-liquid-performance]]"
  - "[[shopify-debug-slow-loading]]"
  - "[[core-web-vitals]]"
source-url: "https://help.shopify.com/en/manual/online-store/web-performance/improving-web-performance"
source-type: web-article
author: "Shopify (documentation officielle)"
date-published:
date-accessed: 2026-06-20
raw-file: "raw/assets/Improving your online store performance.md"
---

# Improving your online store performance

Guide officiel Shopify pour marchands (help.shopify.com). Source complémentaire à [[shopify-debug-slow-loading]] — vision plus macro et orientée marchand (non-développeur). Apporte : la liste des optimisations déjà intégrées dans Shopify (protection contre les faux positifs des outils de scan), les 3 facteurs principaux d'impact, un workflow de troubleshooting 3 étapes, et les orientations INP.

**Valeur spécifique :** source officielle Shopify. Point de vue "défaut sain" : la plateforme est optimisée par défaut — les problèmes viennent du thème, des apps, et du code tiers. Mise en garde critique sur les outils de scan tiers qui suggèrent des optimisations déjà intégrées.

## Contexte

Les 3 Core Web Vitals mesurés sur Shopify :
- **LCP** — loading speed (< 2.5 s)
- **CLS** — layout stability (< 0.1)
- **INP** — responsiveness to interaction (< 100 ms)

## Optimisations déjà intégrées dans Shopify (ne rien faire)

| Optimisation | Ce que Shopify fait déjà |
|---|---|
| **CDN** | CDN mondial Cloudflare, assets en HTTP/2 |
| **Browser caching** | Cache 1 an pour toutes les ressources cacheables |
| **Gzip compression** | CSS, JS, HTML, pages — tous compressés |
| **Image CDN** | Images compressées + WebP + redimensionnées automatiquement |
| **Minification** | CSS et JS minifiés automatiquement à la demande |
| **Hébergement** | Serveurs rapides sans limite de bande passante |

**Conséquence pratique :** les outils de scan tiers (Lighthouse, GTMetrix, etc.) peuvent suggérer d'activer CDN, Gzip, ou cache — ces recommandations **ne s'appliquent pas** aux stores Shopify. Elles sont déjà en place. Ignorer et se concentrer sur ce qui dépend du marchand.

## Les 3 facteurs principaux d'impact (dans l'ordre de priorité)

1. **Le thème** — premier levier d'amélioration
2. **Les apps installées** — chaque app charge des assets sur le storefront
3. **Le code tiers ajouté manuellement** — tag managers et tags inclus

## Recommandations par facteur

### Thème

- Utiliser un thème récent et optimisé (famille Horizon, thèmes Online Store 2.0 de Shopify = gratuits + optimisés)
- Consulter le [Theme Performance Data Table](https://performance.shopify.com/pages/theme-performance-data-table) pour comparer les thèmes
- Tester avant/après l'activation des **transitions de pages ou animations** — elles peuvent ralentir
- Limiter le nombre de sections sur les templates de pages
- Activer la **pagination** sur les collections avec beaucoup de produits

### Apps

- Évaluer si la valeur de chaque app justifie son impact sur les performances
- Supprimer les apps non essentielles
- Note : désinstaller une app ne supprime pas automatiquement son code du thème → contacter le développeur pour nettoyage complet

### Code tiers / tag managers

- Auditer les tags dans le tag manager → supprimer les tags inutilisés ou à faible valeur
- Référence : [Tag best practices (web.dev)](https://web.dev/articles/tag-best-practices)

## Workflow de troubleshooting : 3 étapes

### Étape 1 : Vérifier le problème

1. Tester depuis différents appareils et connexions internet
2. Faire tester par d'autres personnes (exclure un problème de connexion locale)
3. Utiliser PageSpeed Insights pour des métriques précises

### Étape 2 : Identifier la cause

| Symptôme | Cause probable |
|---|---|
| Trop d'apps | Assets de trop d'apps chargés sur le storefront |
| Images volumineuses | Nombreuses images haute qualité sur la page |
| Page blanche avant chargement | Scripts lents — utiliser les DevTools navigateur pour identifier |

### Étape 3 : Agir

- **Apps :** supprimer les apps non essentielles + s'assurer du nettoyage complet du code
- **Images :** JPG pour photos, PNG pour graphiques avec transparence ; redimensionner à la taille affichée
- **Thème :** passer à un thème optimisé si le thème actuel est la cause principale

## INP — Responsivité (Interaction to Next Paint)

Cause principale d'un INP dégradé sur Shopify : **trop de JavaScript** (code du thème + code des apps + code tiers / tag managers).

Approche de résolution :
1. Identifier les pires offenseurs JS
2. Référence : "[3 ways to find your worst JavaScript offenders for page load](https://performance.shopify.com/blogs/blog/3-ways-to-find-your-worst-javascript-offenders-for-page-load)"
3. Ressource complémentaire : web.dev/articles/inp

## Outils recommandés

| Outil | Rôle |
|---|---|
| **Web Performance Reports** (Shopify natif) | Données RUM réelles sur les Core Web Vitals par page type |
| **PageSpeed Insights** | Métriques détaillées lab + field |
| **Chrome DevTools** | Identifier les scripts lents (page blanche avant chargement) |

**Note :** Shopify dispose de ses propres Web Performance Reports dans l'admin → source de données RUM native à utiliser en premier.

## CLS — Stabilité visuelle

L'article mentionne CLS mais ne le développe pas — référence vers un article dédié : "How to optimize Cumulative Layout Shift (CLS) on Shopify sites" (performance.shopify.com). À ingérer si nécessaire.

## Voir aussi
- [[shopify-liquid-performance]] — diagnostic LCP/FCP/TTFB par causes Shopify-spécifiques
- [[shopify-debug-slow-loading]] — guide de debug détaillé (Sia Karamalegos)
- [[core-web-vitals]] — seuils LCP/INP/CLS
- [[ttfb]] — TTFB comme signal crawl + UX
