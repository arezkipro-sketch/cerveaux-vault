---
type: concept
title: Topical Authority (Autorité Thématique)
slug: topical-authority
tags:
  - seo
  - content-strategy
  - ai-seo
  - authority
sources:
  - "[[jotaro-seo-ia-x-seo]]"
  - "[[alexgroberman-62pct-beyond-top10]]"
  - "[[content-pruning]]"
  - "[[semrush-topical-authority]]"
  - "[[julien-gourdon-topical-authority-2026]]"
  - "[[jotaro-seo-strategie-ecommerce-2026]]"
  - "[[jotaro-seo-sans-backlinks]]"
source_count: 7
status: active
updated: 2026-07-06
---

# Topical Authority (Autorité Thématique)

**Definition:** The degree to which a website is recognized — by Google, by other sites, and by AI models — as the go-to reference on a specific subject. Built by publishing comprehensive, consistent content that covers a topic from every angle, using domain-specific vocabulary throughout.

## What we know
- A site with 10 articles on retrogaming has no topical authority. A site with 300 articles covering every sub-angle (history, consoles, emulators, ROM legality, buying guides, brand comparisons, configuration tutorials) builds authority that AI models recognize → [[jotaro-seo-ia-x-seo]].
- **Mechanism for AI models**: when an LLM processes thousands of queries on a subject and one site consistently appears in the relevant sources, that site becomes associated with the topic in the model's weights → [[jotaro-seo-ia-x-seo]].
- **Vocabulary signal**: content that doesn't use the exact domain terminology (e.g., an emulator article lacking "RetroArch", "Anbernic", "IPS resolution") is perceived as generic by both Google and LLMs → [[jotaro-seo-ia-x-seo]].
- Optimal publishing cadence for authority building: 1 article per day → [[jotaro-seo-ia-x-seo]] *(unsourced beyond thread)*. Pour la cadence détaillée par stade → voir section "Cadence de publication" ci-dessous.

## Preuves algorithmiques — la TA est mathématiquement mesurée

La topical authority n'est pas un concept flou : elle est brevetée et mesurée algorithmiquement.

- **Microsoft (2024) — US11874882B2 :** équation A(s,t) = score d'autorité d'un site *s* sur un sujet *t*. Première formalisation mathématique officielle.
- **Google US8458196B1 (2008) :** autorité thématique des auteurs via signatures cumulatives pondérées.
- **Google US9324112B2 (2011) :** ranking d'auteurs via scores probabilistes (originalité + impact réseau).
- **Knowledge Graph (2012) :** Google indexe en graphes d'entités nommées, pas en listes de mots-clés.

→ [[julien-gourdon-topical-authority-2026]]

## Google Leaks 2024 — métriques internes confirmées

Les fuites de mai 2024 ont révélé deux métriques directement liées à la TA :

**siteFocusScore** : score de focalisation thématique. Mesure la concentration sur un sujet principal. "siteRadius" faible = cohérence serrée. Les sites dispersés sont pénalisés.

**siteAuthority** : mesure globale de l'autorité. Agit comme un **multiplicateur de crédibilité**. Influencé par liens thématisés + engagement utilisateur + E-E-A-T. Version interne de ce que Moz appelle "Domain Authority".

**Conséquence opérationnelle :** Google évalue la réputation cumulative du site entier. La dispersion thématique est un signal négatif — se spécialiser sur 2 thèmes maîtrisés > 10 thèmes effleurés.

→ [[julien-gourdon-topical-authority-2026]]

## TA en 2025 : modèle multiplateforme

L'autorité thématique ne se construit plus uniquement sur le site — elle se joue sur toute la présence digitale : YouTube, LinkedIn, podcasts sectoriels.

**Stat Semrush 2025 :** marques actives sur 3+ plateformes = +50% de visibilité dans les AI Overviews.

→ [[julien-gourdon-topical-authority-2026]]

## 3 piliers d'évaluation par les IA génératives

ChatGPT, Perplexity et Google AI Overviews citent prioritairement les domaines à forte TA. Ils évaluent :
1. **Cohérence sémantique** — les contenus utilisent-ils le vocabulaire exact du domaine ?
2. **Fraîcheur** — les analyses suivent-elles les évolutions récentes ?
3. **Reconnaissance par les pairs** — le site est-il cité, repris, validé par d'autres experts ?

→ [[generative-engine-optimization]] pour le cadre GEO complet.

## Entités > mots-clés

Google pense en graphes de connaissances depuis 2012. Une page qui ne cite pas les entités clés d'un domaine (personnes, outils, concepts, organisations) est perçue comme générique — même si les mots-clés sont présents. Mentionner et contextualiser les entités phares est un signal de topical authority.

→ [[julien-gourdon-topical-authority-2026]]

## TA vs Domain Authority

| | Topical Authority | Domain Authority |
|---|---|---|
| Mesure | Expertise sur un sujet précis | Puissance générale du domaine |
| Source | Contenu + maillage + citations thématiques | Profil de backlinks global |
| Spécificité | Fort TA + faible DA possible | Fort DA + faible TA possible |

Un site niche peut surclasser un domaine puissant mais dispersé — c'est le mécanisme "Knit Picks #1 devant Amazon" (→ [[semrush-topical-authority]]).

## Backlinks : thématisés > puissants mais génériques

Mieux vaut un backlink d'un expert sectoriel qu'un backlink d'un domaine générique ultra-puissant. La thématisation du profil de backlinks est un signal de TA. → [[backlinks]]

## Timeline réaliste

**6 à 18 mois** selon la compétitivité du secteur pour une TA reconnue. Une fois acquise, elle s'auto-renforce (boucle vertueuse). → [[julien-gourdon-topical-authority-2026]]

## Pourquoi ça compte — 3 bénéfices SEO concrets

1. **Trust moteurs + utilisateurs** : Google classe les sources autorisées en haut des SERPs → CTR plus élevé → signal de retour → encore plus de rankings.
2. **Link building naturel** : les sites te perçoivent comme référent → liens éditoriaux spontanés → boucle auto-alimentée.
3. **Réduction coûts marketing** : un site niche peut dépasser un géant sur son topic (ex : Knit Picks #1 devant Amazon pour "knitting needles") → moins de budget paid ads.

→ [[semrush-topical-authority]]

## Timeline Google : l'autorité thématique est un concept de 15 ans

| Année | Update | Impact |
|---|---|---|
| 2011 | Panda | Pénalise contenu bas de gamme, copié, inutile |
| 2013 | Hummingbird | Naissance recherche sémantique — Google comprend l'intention |
| 2022 | Helpful Content + E-E-A-T | Ajout "Experience" → récompense expérience firsthand |
| 2023 | Helpful Content v2 | Réduit contenu thin/AI-généré sans valeur |
| 2024 | Core Ranking System | Helpful Content intégré au core → permanent |

→ [[semrush-topical-authority]]

## Comment construire — approche pratique

**Principe fondamental : niché > large.** Dominer "patterns de tricot débutant" est infiniment plus rentable que "tricot" en général. La spécialisation précède l'élargissement.

**4 étapes (Semrush) :**
1. **Trouver les groupes thématiques** (Keyword Strategy Builder → piliers + sous-pages + clusters)
2. **Keyword research thématique** (Keyword Magic Tool → filtre PKD% "Very Easy" → opportunités personnalisées)
3. **Construire les backlinks** (→ [[backlinks]])
4. **Contenu qui résout des problèmes** : études de cas, prises de position contraires, interviews experts, FAQs oubliées, recherches originales. Outil : [AlsoAsked.com](https://alsoasked.com/) → arbre PAA sur n'importe quel sujet.

→ [[semrush-topical-authority]]

## PKD% — proxy de mesure de la TA

**Personal Keyword Difficulty (Semrush)** : contrairement au KD% standard (difficulté pour tous les sites), le PKD% est **personnalisé à ton domaine**. PKD% = 0 → très forte probabilité de ranker sur ce mot-clé avec un bon contenu. Plus la TA grandit, plus les PKD% baissent — boucle vertueuse mesurable.

Score TA Semrush : Low → Moderate → Relevant → **High** (mesuré dans Keyword Overview : ton domaine + un keyword cible).

→ [[semrush-topical-authority]]

## 7 catégories de silos thématiques e-commerce (JotaroSEO)

Pour chaque produit/niche, couvrir ces 7 catégories = garantir un champ sémantique complet qui signale l'autorité à Google.

| Catégorie | Description | Exemple (cagoule) |
|---|---|---|
| **Types** | Variantes matière/modèle | laine, coton, polaire, mérinos, bambou |
| **Usages** | Contextes d'utilisation | ski, running, randonnée, cyclisme, quotidien, enfant |
| **Guides d'achat** | Comment choisir | selon usage, selon météo |
| **Comparatifs** | Versus, quelle matière | laine vs coton, mérinos vs polaire |
| **Entretien** | Conseils pratiques | comment laver, sécher, conserver |
| **FAQ** | Questions fréquentes | taille, allergie, durée de vie |
| **Saisonniers** | Articles liés à la saison | meilleures cagoules hiver 2025, tendances |

Une fois ces 7 catégories couvertes → Google reconnaît le site comme LA référence et positionne naturellement sur les mots-clés principaux, même sans contenu direct sur chacun.

→ [[jotaro-seo-strategie-ecommerce-2026]]

## Champ lexical : carburant du Topical SEO

Chaque page doit utiliser le champ lexical complet de son sujet — pas uniquement répéter le mot-clé principal. Google interprète les termes sémantiquement proches comme preuve de maîtrise du sujet.

Exemple pour un article "cagoule en laine" : *laine mérinos, isolation thermique, respirant, lavage doux, tricot, douceur, hiver, froid, col, taille unique, séchage rapide, légèreté, antiallergique, fibres naturelles, entretien délicat.*

Si le champ lexical est absent → Google classera comme contenu mince et superficiel (thin content).

→ [[jotaro-seo-strategie-ecommerce-2026]]

## Relations
- The structural implementation of topical authority in French SEO = [[cocon-semantique]] (daughter pages → mother page).
- In English SEO literature: equivalent to **pillar + cluster model** *(unsourced)*.
- Central lever in [[ai-seo]]: topical authority is listed as the foundation — "without it, everything else is cosmetic."
- Overlaps with [[e-e-a-t]]: topical depth is how expertise is demonstrated at the site level.

## Quantified depth: 40-60 sub-question pages per category

Previously an open question; now answered by Ahrefs data via [[alexgroberman-62pct-beyond-top10]]:
- Google Gemini 3 decomposes queries into internal sub-queries, each drawing sources independently.
- **62 % of AI Overview citations go to pages NOT in the original query's top-10**. They go to pages that specifically answer a sub-question.
- **Recommended coverage**: 40-60 pages per category covering every sub-question a buyer in that category asks (comparisons, specs, pricing, use cases, integrations, FAQs per audience type).
- Example: "best CRM for small business" → sub-questions: onboarding time comparison, pricing <10 people, multi-state compliance, integration with accounting tools, review of each vendor, etc.
- **Domain authority still required**: sub-query ranking needs domain-level authority to even be considered, so link-building and classic [[seo-audit]] work remain foundations → [[alexgroberman-62pct-beyond-top10]].

## Pruning the other direction
- Authority isn't only built by adding — [[content-pruning]] removes thin/duplicate/cannibalizing pages so authority **concentrates** on the strongest URLs; "3 strong articles > 10 mediocre." Pairs with the 40-60 depth target: distinct sub-question pages in, mediocre overlap out → [[content-pruning]].

## Tensions / open questions
- ~~How many articles / what coverage % is required before meaningful authority accrues?~~ **Resolved**: 40-60 sub-question pages per category (Ahrefs / Google Gemini 3 sub-query data) → [[alexgroberman-62pct-beyond-top10]].
- Does a site need to cover all angles *before* gaining authority, or does authority build incrementally?
- Tension with "scaled content abuse" risk: 40-60 pages sounds like scale. Resolution: each page must address a genuinely distinct sub-question with unique information — not the same answer with city/keyword swapped → [[e-e-a-t]], [[irentdumpsters-google-ai-guide]].

## Cadence de publication et indexation manuelle — [[jotaro-seo-sans-backlinks]]

**Pourquoi la constance compte algorithmiquement :** un site qui publie régulièrement est crawlé plus fréquemment (Googlebot revient plus souvent). Les nouvelles pages s'indexent plus vite. La TA se construit progressivement. Un site qui publie 3 articles corrects par semaine **sera toujours devant** un concurrent qui publie 1 article exceptionnel par mois sur le même sujet.

**Cadence recommandée selon le stade :**

| Stade | Période | Cadence |
|---|---|---|
| Lancement | Mois 1 à 3 | 1 article/jour si possible, **3 minimum par semaine** |
| Croissance | Mois 4 à 12 | **3 articles/semaine** + indexation manuelle GSC systématique |
| Maturité | Après 12 mois | **2 nouveaux articles/semaine** + 1 article mis à jour/semaine |

**Indexation manuelle dans la GSC (action la plus sous-exploitée) :**
- Google alloue **10 demandes par jour** gratuitement dans la Search Console
- Chaque nouvel article publié → soumettre l'URL manuellement dans la GSC **le jour même**
- Résultat : délai d'indexation divisé par 10 → **24 à 72 heures** au lieu de 2 à 6 semaines
- Concrètement : copier l'URL dans la barre "Inspecter une URL" de la GSC → "Demander l'indexation"

→ Cette seule action peut faire la différence sur un site en phase de lancement où chaque page compte.

## Sources
- [[jotaro-seo-ia-x-seo]] — defines the concept with a worked retrogaming example; frames it as the foundation of AI SEO.
- [[alexgroberman-62pct-beyond-top10]] — Ahrefs 863K SERPs; quantifies 40-60 page depth; sub-query decomposition root cause.
- [[content-pruning]] — concentrate authority by removing thin/duplicate pages (quality > quantity).
- [[semrush-topical-authority]] — définition fondatrice, 3 bénéfices SEO, timeline Google (Panda→Core 2024), 4 étapes build, PKD%, AlsoAsked, score TA Low→High.
- [[julien-gourdon-topical-authority-2026]] — preuves algorithmiques (brevets MS/Google), Google Leaks (siteFocusScore, siteAuthority), TA multiplateforme (+50% AI Overviews), 3 piliers IA, entités > mots-clés, 6-18 mois timeline.
- [[jotaro-seo-sans-backlinks]] — cadence de publication par stade (lancement/croissance/maturité) ; indexation manuelle GSC (10/jour → 24-72h vs 2-6 semaines).
