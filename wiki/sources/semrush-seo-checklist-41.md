---
title: "Checklist SEO : 41 Conseils pour Optimiser votre Site Web"
slug: semrush-seo-checklist-41
page-type: source-note
domain: seo
tags: [seo, checklist, technical-seo, on-page, off-page, keyword-research, site-audit]
sources: []
related:
  - "[[what-is-seo]]"
  - "[[seo-audit]]"
  - "[[keyword-research]]"
  - "[[keyword-mapping]]"
  - "[[maillage-interne]]"
  - "[[xml-sitemap]]"
  - "[[robots-txt]]"
  - "[[core-web-vitals]]"
  - "[[mobile-seo]]"
  - "[[301-redirect]]"
  - "[[302-redirect]]"
  - "[[keyword-cannibalization]]"
  - "[[backlinks]]"
  - "[[off-page-seo]]"
  - "[[google-business-profile]]"
  - "[[google-search-console]]"
  - "[[google-analytics-4]]"
source-url: "https://fr.semrush.com/blog/checklist-seo-bonnes-pratiques/"
source-type: web-article
author: "[[semrush]]"
date-published: 2022-08-01
date-accessed: 2026-06-19
raw-file: "raw/assets/Checklist SEO  41 Conseils pour Optimiser votre Site Web.md"
---

# Checklist SEO : 41 Conseils pour Optimiser votre Site Web

Checklist opérationnelle Semrush en 41 points couvrant les 5 grands domaines du SEO. Référence de pratique courante — tous les contrôles fondamentaux qu'un site devrait passer avant de construire une stratégie avancée.

## Overview

Checklist en 5 sections : Bases, Mots clés, SEO technique, On-page/Contenu, Off-page/Link building. Chaque point pointe vers un outil Semrush — biais commercial notable mais la liste des contrôles reste valide indépendamment de l'outil.

## Key Takeaways

1. **Bases non négociables** : GSC + Bing Webmaster Tools + GA4 + robots.txt + sitemap XML soumis. Sans ça, on travaille à l'aveugle.
2. **Keyword mapping** = chaque groupe de mots clés doit être associé à une page précise. Pas de mapping = pas de structure claire pour Google.
3. **Profondeur de page max 3 clics** depuis la home — au-delà Google ne crawle pas efficacement.
4. **H1 unique par page** contenant le mot clé cible ; balises title ≤ 60 caractères.
5. **Redirections 302** utilisées à tort à la place de 301 sont un problème courant à corriger.
6. **Pages orphelines** (aucun lien interne) = invisibles pour Google sauf via sitemap ou backlink externe.
7. **Mentions sans lien** → opportunité link building à faible friction (le site a déjà mentionné votre marque).
8. **Google Business Profile** = seul élément off-page incontournable pour le local.

## Detailed Notes

### Section 1 — Bases du SEO (7 points)

| # | Tâche | Outil / Méthode |
|---|---|---|
| 1 | Configurer Google Search Console | search.google.com/search-console |
| 2 | Configurer Bing Webmaster Tools | bing.com/toolbox/webmaster |
| 3 | Configurer Google Analytics (GA4) | analytics.google.com |
| 4 | Plugin SEO WordPress (Yoast / Rank Math / SWA) | — |
| 5 | Créer et soumettre un sitemap XML | GSC + Bing WMT |
| 6 | Créer un fichier robots.txt | — |
| 7 | Vérifier les actions manuelles dans GSC | GSC → Sécurité & actions manuelles |
| 8 | Vérifier que Google peut indexer le site | Semrush Audit de site → Explorabilité |

### Section 2 — Recherche de mots clés (7 points)

| # | Tâche | Note |
|---|---|---|
| 8 | Identifier les concurrents | Semrush Possibilités de mots clés → "Manquants" + "Faibles" |
| 9 | Trouver mots clés "money" (commercial + transactionnel) | Vue d'ensemble du domaine → Meilleurs mots clés organiques |
| 10 | Trouver des variantes longue traîne | Keyword Magic Tool → filtre Questions |
| 11 | Créer une carte de mots clés (keyword mapping) | Grouper par intention → 1 URL = 1 intention |
| 12 | Analyser l'intention des pages qui rankent | Vue d'ensemble des mots clés → champ "Intention" |
| 13 | Identifier les questions posées par l'audience | Keyword Magic Tool + filtre Questions + AlsoAsked.com |
| 14 | Évaluer la difficulté du mot clé (KD) | Vue d'ensemble des mots clés → KD score |

### Section 3 — SEO technique (12 points)

| # | Tâche | Note |
|---|---|---|
| 15 | HTTPS implémenté (cadenas ≠ risque de sécurité) | Signal de classement depuis 2014 |
| 16 | Une seule version du site indexée (www vs non-www) | Toutes autres versions → 301 vers version principale |
| 17 | Corriger les erreurs de crawl (404, mauvais canoniques) | GSC → Indexation → Pages → Non indexées |
| 18 | Vitesse du site / Core Web Vitals | PageSpeed Insights + Semrush Audit → CWV |
| 19 | Corriger les liens brisés internes et externes (404) | Semrush Audit → Liens internes |
| 20 | Corriger les liens HTTP sur pages HTTPS | Semrush Audit → rapport HTTPS |
| 21 | Site mobile-friendly (responsive) | Google Test d'optimisation mobile |
| 22 | Structure d'URL SEO-friendly | Traits d'union, pas de tirets bas, courtes, descriptives |
| 23 | Données structurées Schema.org (FAQPage, Article…) | schema.org |
| 24 | Profondeur de page ≤ 3 clics depuis la home | Semrush Audit → Liens internes → Profondeur |
| 25 | Corriger les redirections 302 temporaires abusives | → Remplacer par 301 si permanent |
| 26 | Corriger les chaînes et boucles de redirection | A → B → C doit devenir A → C directement |

### Section 4 — On-Page et Contenu (10 points)

| # | Tâche | Règle |
|---|---|---|
| 27 | Balises title : pas de doublons, pas de tronquées | Max ~60 caractères |
| 28 | Meta descriptions : pas de doublons, pas de manquantes | Google les réécrit 70 % du temps → rédiger quand même |
| 29 | H1 : unique par page, contient le mot clé cible | Pas de double H1 |
| 30 | Optimiser titles/meta pour mots clés secondaires | GSC : fort impressions + faible clics → enrichir contenu |
| 31 | Audit de contenu existant (trafic, engagement, pertinence) | GA4 + On Page SEO Checker |
| 32 | Balises alt sur toutes les images | Semrush Audit → Problèmes → "attributs alt" |
| 33 | Améliorer le maillage interne | Ajouter liens vers pages n'ayant qu'un seul lien interne |
| 34 | Corriger la cannibalisation de mots clés | 1 keyword = 1 page ; fusionner/redirectionner/canonicaliser |
| 35 | Corriger les pages orphelines | Toute page doit avoir ≥ 1 lien interne |
| 36 | Maintenir le contenu à jour | Contenu obsolète = mauvaise UX = risque de déclassement |

### Section 5 — Off-Page et Link Building (5 points)

| # | Tâche | Note |
|---|---|---|
| 37 | Analyser les profils de liens des concurrents | Semrush Analyse de backlinks |
| 38 | Analyse des intersections de liens (link gap) | Semrush Possibilités de backlinks |
| 39 | Mentions sans lien → demander backlink | Semrush Brand Monitoring → contacter l'auteur |
| 40 | Nouvelles opportunités de link building | Semrush Link Building Tool |
| 41 | Google Business Profile (local) | Fiche optimisée → photos + précision + unicité |

## Notes

- **Biais commercial** : chaque point pointe vers un outil Semrush payant. La checklist elle-même est valide ; les outils alternatifs (Ahrefs, GSC natif, Screaming Frog, etc.) couvrent les mêmes vérifications.
- **Date** : publié 2022 — les fondamentaux tiennent mais les fonctionnalités Semrush ont pu évoluer.
- **Auteur** : Olivier Amici (Semrush FR) — non listé comme entité car profil rédactionnel interne.
