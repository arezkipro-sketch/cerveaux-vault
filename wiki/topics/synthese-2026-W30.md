---
type: topic
title: "Synthèse hebdomadaire — Semaine 2026-W30"
slug: synthese-2026-w30
tags: [synthese, seo, pushrank, ubersuggest, shopify, e-commerce, keyword-cannibalization]
sources: ["[[pushrank]]", "[[ubersuggest]]", "[[meta-description]]", "[[keyword-cannibalization]]", "[[canonical-tag]]", "[[h1-heading-tag]]"]
source_count: 1
status: active
updated: 2026-07-26
---

# Synthèse hebdomadaire — Semaine 2026-W30 (2026-07-19 → 2026-07-26)

**1 ingest cette semaine**, sans `raw/` associé — capitalisation directe d'usage réel plutôt qu'ingestion d'une source externe :
- **Capitalisation SEO — usage réel PushRank/Ubersuggest** (07-22, harnais-chien-expert.fr) — premier audit complet du store via intégration MCP (PushRank + Ubersuggest + API Shopify Admin). A mis à jour [[pushrank]] et [[ubersuggest]] (entities), enrichi [[meta-description]], [[keyword-cannibalization]], [[canonical-tag]] et créé [[h1-heading-tag]].

*(Note : les entrées `## update |` du 07-22/07-25 et `## maint |` du 07-26 sur le même chantier harnais-chien-expert.fr prolongent ce même fil — voir thème 4 ci-dessous — mais ne sont pas des `ingest` au sens strict de `CLAUDE.md` ; elles ne sont donc pas comptées dans le total ci-dessus, seulement mentionnées pour contexte.)*

## Thèmes récurrents

### 1. L'outil SEO comme déclencheur d'audit, pas comme pilote automatique
Le fil conducteur de toute la semaine, répété dans chaque page touchée : ne jamais exécuter une recommandation d'outil sans vérification humaine.
- [[pushrank]] : règle explicite adoptée — chaque suggestion documentée avec signal détecté / décision prise / raison SEO-business / changement appliqué, précisément pour éviter d'« obéir mécaniquement à l'outil ».
- [[keyword-cannibalization]] : une recommandation `content_creation` PushRank s'est révélée être un faux positif sur 6 mots-clés sur 7 — les collections Shopify canoniques existaient déjà, PushRank n'avait simplement pas fait le mapping (`primaryArticle: null`).
- Le signal `decay` lui-même est jugé peu fiable sur un jeune site sans volume d'impressions suffisant (voir section dédiée dans [[pushrank]]).

### 2. Cannibalisation : un seul check ne suffit pas
Cas vécu documenté dans [[keyword-cannibalization]] : la vérification GSC seule ("quelles pages rankent déjà") a conclu à tort à l'absence de cannibalisation sur "harnais chien" vs "harnais pour chien". La vérification SERP-similarity (12pages.com, oubliée dans un premier temps) a montré 80% de recoupement — seuil de fusion. Les deux checks sont désormais systématiques dans le vault, pas seulement recommandés.

### 3. Le pattern Shopify qui revient partout : pas de metafield SEO dédié → repli par défaut dégradé
Trois pages distinctes documentent la même cause racine sous des symptômes différents :
- [[meta-description]] : sans metafield `global.description_tag`, le contenu brut de la page peut fuiter dans la balise meta (cas observé sur une page FAQ).
- [[h1-heading-tag]] : hypothèse (non encore vérifiée) que `title_equals_h1` vient de pages sans metafield `global.title_tag`, le title retombant par défaut sur le même texte que le H1.
- [[canonical-tag]] : les pages système `/policies/*` générées par Shopify dupliquent les pages `/pages/*` équivalentes créées manuellement — même famille de symptôme (duplicate content), racine différente (architecture Shopify plutôt que metafield manquant).

Trois diagnostics indépendants convergent vers le même conseil : sur Shopify, chercher d'abord si un champ SEO dédié est réellement rempli avant de traiter le symptôme en surface.

### 4. Croiser deux outils SEO révèle plus qu'un seul, mais avec des frictions opérationnelles propres
[[pushrank]] et [[ubersuggest]] tournés sur le même site (harnais-chien-expert.fr) remontent des listes qui se recoupent partiellement (ex : title trop long détecté par les deux) mais avec des seuils différents — croiser les deux plutôt que se fier à un seul devient une règle explicite. Chaque outil a cependant ses propres pièges opérationnels observés cette semaine : bug `severity=low` qui renvoie 0 résultat côté PushRank, cache non instantané nécessitant un `recrawl: true` explicite côté Ubersuggest, erreurs 503/504 en usage intensif. La suite du chantier (sessions du 07-25/07-26, hors périmètre `ingest` strict) montre que cette prudence méthodologique tient dans la durée : les alertes `broken internal link`/`canonical 404` en volume ont été mises de côté cette semaine après qu'un contrôle rapide a surtout révélé des `429` (rate-limit), pas de vraies 404.

## Tension / point non résolu

Aucune contradiction de fond avec des pages existantes du vault cette semaine. Un point de vigilance opérationnel plutôt qu'une tension fiqh/conceptuelle : l'OAuth du MCP PushRank a expiré en cours de semaine (session du 07-25, puis de nouveau signalé le 07-26), empêchant de repasser les opportunités traitées en `done` côté outil — le vault documente les décisions prises mais l'état PushRank lui-même reste en décalage jusqu'au renouvellement de l'autorisation.

## Questions ouvertes

- `heading_hierarchy_skip` (×27 pages) et `title_equals_h1` (×17 pages), détectés par Ubersuggest le 07-22, restent non diagnostiqués en détail faute de liste d'URLs exploitable — export manuel ou audit page par page à faire dans une prochaine session, cf. [[h1-heading-tag]].
- Le panneau web PushRank "Santé SEO technique" (pages orphelines, maillage faible) reste une boîte noire côté MCP/API — seule l'interface web donne le détail par URL, point déjà ouvert la semaine précédente et toujours non résolu.
- `ceinture chien voiture` reste en `todo` côté PushRank : intention potentiellement distincte de `harnais chien voiture`, à trancher seulement si une offre produit dédiée existe (cf. [[keyword-cannibalization]]).
- Observation de fonctionnement du vault, pas liée au contenu SEO : plusieurs entrées `log.md` de la semaine utilisent l'op `update`, absent de la taxonomie `{ingest, query, lint, schema, maint, synthesis}` définie dans `CLAUDE.md`. À trancher lors d'un prochain `maint` — soit ajouter `update` à la taxonomie officielle, soit reclasser ces entrées.

## Sources couvertes
[[pushrank]] · [[ubersuggest]] · [[meta-description]] · [[keyword-cannibalization]] · [[canonical-tag]] · [[h1-heading-tag]]

Pages liées pour contexte (chantier continué hors fenêtre `ingest` stricte) : [[site-health]], [[maillage-interne]], [[seo-audit]]

Concept ancien lié (règle des backlinks, page 2+ mois) : [[persistent-wiki]] — le principe de capitaliser l'usage réel d'un outil directement dans le vault (sans source `raw/` externe) est une instance concrète de la mémoire externe compoundée que [[persistent-wiki]] posait comme thèse fondatrice du vault (2026-06-14).
