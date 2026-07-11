---
title: "Réussir son référencement web — Stratégies et techniques SEO (10e éd. 2020-2021)"
slug: reussir-referencement-web-andrieu-2020
page-type: source-note
domain: seo
tags: [seo, seo-technique, on-page, off-page, netlinking, mots-cles, longue-traine, penalites, panda, penguin, indexation, duplicate-content, hreflang, schema-org, multisupport, mobile, vitesse]
sources: []
related:
  - "[[backlinks]]"
  - "[[off-page-seo]]"
  - "[[keyword-research]]"
  - "[[canonical-tag]]"
  - "[[crawl-budget]]"
  - "[[robots-txt]]"
  - "[[robots-meta-directives]]"
  - "[[xml-sitemap]]"
  - "[[donnees-structurees]]"
  - "[[core-web-vitals]]"
  - "[[olivier-andrieu]]"
  - "[[duplicate-content]]"
  - "[[longue-traine]]"
  - "[[google-algorithmic-filters]]"
  - "[[hreflang]]"
source-url: ""
source-type: book
author: "[[olivier-andrieu]]"
date-published: 2020-06-18
date-accessed: 2026-06-22
raw-file: "raw/reussir-referencement-web-2020-2021.pdf"
---

# Réussir son référencement web — Olivier Andrieu (10e éd. 2020-2021)

Référence francophone du SEO. 809 pages, Éditions Eyrolles. Préface de Vincent Courson (Google Trust & Safety). PDF scannérisé (images), non OCR. Andrieu est fondateur d'Abondance.com, meilleur référenceur francophone selon le Journal du Net.

**Valeur spécifique :** encyclopédie SEO la plus complète en français — couvre les fondamentaux immuables (balises, liens, indexation, pénalités) avec une profondeur rarement égalée. Certaines parties datées (2020) mais les chapitres technique/netlinking/pénalités restent valides.

---

## Overview

3 parties, 16 chapitres + annexes :

- **Partie A** — Bases du référencement naturel (Ch1-3) : fonctionnement des moteurs, méthodologie, mots-clés
- **Partie B** — SEO en pratique (Ch4-10) : balises HTML, URL, liens, multimédia, suivi, social, international
- **Partie C** — Devenir un as du SEO (Ch11-16) : rich snippets, indexation, duplicate content, pénalités, désindexation

---

## Key Takeaways

### Ch1 — Le référencement aujourd'hui
- **SEO ≠ SEM** : référencement naturel (organique) vs payant. Les deux sont complémentaires mais méthodes différentes.
- **3 étapes d'un référencement** : Crawl → Indexation → Ranking.
- **Spamdexing** = optimisation déloyale (black hat). Le livre ne couvre que l'optimisation loyale.
- **Triangle d'or de Google** : concept de zone de visibilité maximale sur la première page SERP (historique, layout modifié depuis 2016 avec les annonces Google Ads intégrées).

### Ch2 — Fonctionnement des moteurs
- Google index = **100 milliards de pages web**, 20+ milliards crawlées/jour.
- 4 phases : Crawl (spiders) → Rendering HTML/JS → Indexation → Ranking.
- **Caffeine** (2010) = index de fraîcheur de Google — permet d'indexer les nouvelles pages beaucoup plus vite.
- Le moteur d'indexation de Google est distinct du moteur de ranking.
- **Focus Google** : seul moteur qui compte vraiment en France (>90% de parts).

### Ch3 — Préparation & mots-clés
- **Longue traîne** : mots-clés spécifiques (3+ mots), faible volume mais forte conversion et faible compétition. Représentent 70%+ du trafic total possible.
- **Fautes de frappe** = source de trafic non négligeable, à ne pas exclure de la stratégie.
- **Concurrence** estimée via nombre de résultats Google :
  - < 1 000 résultats → très faible
  - 5 000-10 000 → modéré
  - > 10 000 → difficile
- **Outils** : Google Suggest, Google Keyword Planner (gratuit via Google Ads), Google Trends, KSE (Keyword Search Engine — outil français).
- **Univers sémantique** : définir un univers thématique simple (1 concept central + mots associés) avant de cibler des mots-clés. Étapes : recherche prédictive → inflexion → contenu thématique mensuel.
- **Recherche prédictive** (Google Suggest) : anticiper les requêtes avant de les taper.

### Ch4 — Critères in-page : balises HTML & URL
- **Zones chaudes** (ordre d'importance) :
  1. Balise `<title>` — la plus importante, 60-70 chars max
  2. Balises `<h1>` — un seul par page, reprend le mot-clé principal
  3. Balises `<h2>` à `<h6>` — hiérarchie du contenu
  4. Corps du texte — densité naturelle, champ sémantique
  5. Attribut `alt` des images
- **Meta description** : ne contribue pas directement au ranking mais influence le taux de clic (CTR). Longueur : ~155-160 chars. À soigner comme une accroche publicitaire.
- **URL** : courte, descriptive, mots-clés inclus, tirets comme séparateurs. L'ancienneté d'une URL est un signal.
- **Schema.org / données structurées** : JSON-LD recommandé par Google. Permet rich snippets (étoiles, prix, FAQ, etc.) — voir [[donnees-structurees]].
- Balise `<title>` unique par page obligatoire — le contenu dupliqué dans les titles dilue le signal.

### Ch5 — Critères off-page : liens
- **PageRank** (PR) = algorithme de popularité basé sur les liens entrants. Échelle 0-10 masquée publiquement depuis 2016 mais toujours utilisé en interne.
- **Ancre de lien** = texte du lien = signal fort pour le mot-clé ciblé. Diversifier les ancres (exact match < 20% recommandé, sinon risque Penguin).
- **TrustRank** = mesure de confiance basée sur la proximité aux sites de référence (Wikipedia, gouvernements, universités…).
- **Liens internes** : structurent le PageRank interne. La page d'accueil = hub principal, les pages importantes doivent recevoir plus de liens internes.
- **Qualité > Quantité** : 1 lien depuis un domaine de référence unique vaut mieux que 100 liens depuis le même domaine.
- **Ciblage international** : liens depuis des sites du pays cible = signal géographique fort.
- Voir [[backlinks]] et [[off-page-seo]] pour les détails.

### Ch6 — Référencement multimédia & multisupport
- **Images** : attribut alt obligatoire, nom de fichier descriptif, format WebP recommandé, sitemap images.
- **Vidéos** : YouTube = 2e moteur de recherche mondial. Optimiser titre, description, tags, transcription.
- **Mobile-first** : Google indexe en priorité la version mobile depuis 2018. Site responsive indispensable.
- **AMP** (Accelerated Mobile Pages) : technologie Google pour pages ultra-rapides sur mobile (pertinence réduite depuis Core Web Vitals 2021).
- **Progressive Web App (PWA)** : hybride app/site, bon pour l'expérience mobile.

### Ch7 — Suivi du référencement
- **Google Search Console** = outil indispensable : positions, impressions, CTR, erreurs d'indexation, liens entrants.
- **Google Analytics** = trafic, comportement, conversions. Intégrer avec la GSC.
- **Outils de rank tracking** : SERPRobot, Rank Math, SEMrush, Ahrefs, Majestic.
- **ROI du référencement** : calculer le coût par visite organique vs payant. L'organique amorti sur la durée.

### Ch9 — SMO : réseaux sociaux
- **Twitter/X, Facebook, LinkedIn, YouTube** = indispensables au SEO indirect (trafic, notoriété, liens naturels).
- **Corrélation ≠ causalité** : les signaux sociaux ne sont pas des facteurs de ranking directs chez Google, mais génèrent des liens naturels.
- **Google Business Profile** (ex-Google My Business) = essentiel pour le référencement local.

### Ch10 — Internationalisation
- **3 solutions** pour un site international :
  1. **ccTLD** (`.fr`, `.de`…) — signal géographique fort, coûteux à maintenir
  2. **Sous-domaines** (`fr.domaine.com`) — géolocalisation possible dans GSC
  3. **Répertoires** (`domaine.com/fr/`) — **recommandé** — mutualise l'autorité du domaine
- **Hreflang** = attribut HTML/sitemap indiquant la langue et le pays cible d'une page. Voir [[hreflang]].
- **Ciblage international** dans Google Search Console pour les sous-domaines et répertoires.

### Ch11 — Visibilité dans les résultats
- **Rich snippets** = résultats enrichis (étoiles, prix, FAQ, recettes) via Schema.org — voir [[donnees-structurees]].
- **Featured snippets** = position 0 — répond directement à la question dans la SERP.
- **Knowledge Graph** = base de connaissances Google (entités, marques, personnes).
- **POI (Point of Interest)** = fiche établissement dans Google Maps/Search.
- **Authorship** : schema.org `author` pour les articles de blog.

### Ch12 — Optimisation de l'indexation
- **Sitemap XML** : aide Google à découvrir les URLs mais ne garantit pas l'indexation. Soumettre via GSC. Voir [[xml-sitemap]].
- **robots.txt** : bloque le crawl (≠ désindexation). Une page bloquée par robots.txt peut encore apparaître en résultats si des liens pointent vers elle. Voir [[robots-txt]].
- **Crawl budget** : nombre de pages crawlées/jour, limité par la taille et l'autorité du site. Optimiser en supprimant les URLs inutiles. Voir [[crawl-budget]].
- **Freshnez** : pages récemment modifiées crawlées plus fréquemment (signal de fraîcheur Caffeine).
- **Fichier Sitemap + robots.txt** : complémentaires, à utiliser ensemble.

### Ch13 — Contenu dupliqué
- **Duplicate content** = même contenu accessible via plusieurs URLs. Problème majeur pour Google qui ne sait quelle version indexer. Voir [[duplicate-content]].
- **Causes** : HTTP vs HTTPS, www vs non-www, paramètres d'URL (`?id=123`), pagination, versions mobile/desktop séparées.
- **Solutions** :
  1. Balise `<link rel="canonical">` — indique l'URL de référence
  2. Redirections 301 — fusionne le PageRank vers une URL unique
  3. Répertoires par pays — évite le duplicate cross-domaine
  4. Paramètres d'URL dans GSC — indiquer les paramètres à ignorer
- **Balises multilingues** (`hreflang`) : évitent que des versions linguistiques soient considérées comme duplicate content. Voir [[hreflang]].

### Ch14 — Freins au référencement
- **JavaScript** : Googlebot exécute le JS mais avec délai (deferred indexing). Contenu critique = ne pas dépendre du JS.
- **HTTPS** : signal de ranking depuis 2014. Migrer en HTTPS + redirections 301 correctes obligatoire.
- **Temps de chargement** : facteur de ranking depuis 2010 (mobile depuis 2018). Core Web Vitals (LCP, FID/INP, CLS) depuis 2021. Voir [[core-web-vitals]].
- **Frames** : à éviter — le contenu dans un `<iframe>` n'est pas indexé comme appartenant à la page mère.
- **CSS** : inliner les CSS critiques above-the-fold pour éviter le render-blocking.
- **Redirections** : chaînes de redirections = perte de PageRank. 1 seule redirection 301 max.

### Ch15 — Spam, pénalités, Panda & Penguin
- **Actions manuelles** (≠ filtres algorithmiques) : infligées par un Googler après vérification manuelle. Visible dans la Search Console. Dénonciation possible via le formulaire Google.
- **Filtres algorithmiques** (Panda, Penguin, EMD…) : appliqués automatiquement à chaque mise à jour.
- Voir [[google-algorithmic-filters]] pour les détails Panda/Penguin/EMD.

### Ch16 — Comment ne pas être référencé
- **robots.txt** : `Disallow: /` bloque tout le crawl mais ne désindexe pas.
- **Balise meta robots** `noindex` : empêche l'indexation de la page. Voir [[robots-meta-directives]].
- **X-Robots-Tag** : équivalent HTTP header pour les fichiers non-HTML (PDF, images…).
- **Procédure d'urgence** : Google Search Console → Suppressions → URL temporaire (24h) ou page (6 mois).
- **Désindexation totale** : `noindex` sur toutes les pages + `robots.txt Disallow: /` + soumission de suppression dans GSC.

---

## Detailed Notes

### La "recette de gâteau" du SEO (métaphore Andrieu)
Le SEO = une recette : les ingrédients (mots-clés, balises, liens) sont connus de tous, mais le dosage et la cuisson (l'exécution) font la différence. Il n'y a pas de formule magique.

### Le PageRank aujourd'hui
Google ne publie plus le PageRank externe depuis 2016. Mais en interne, une forme de PageRank est toujours utilisée. Les proxys actuels : Domain Rating (Ahrefs), Domain Authority (Moz), Trust Flow (Majestic).

### Google Panda vs Penguin — distinction clé
| Critère | Panda | Penguin |
|---------|-------|---------|
| Cible | Qualité du **contenu** | Qualité des **liens** |
| Historique | 29 mises à jour (2011-2015) | 7 mises à jour (2012-2016) |
| Mode actuel | Intégré au core algo | Temps réel depuis 2016 |
| Signal principal | Taux de rebond, contenu mince | Ancres spam, liens artificiels |

### KSE — Outil SEO français notable
KSE (Keyword Search Engine) = logiciel de référencement français qui facilite l'analyse et la mise en place de backlinks. Mentionné comme alternative à SEMrush pour l'écosystème francophone.

---

## Sources

- Olivier Andrieu, *Réussir son référencement web*, 10e édition 2020-2021, Éditions Eyrolles. ISBN 978-2-212-67903-8.
