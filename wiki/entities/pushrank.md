---
type: entity
entity_type: product
title: PushRank
slug: pushrank
aliases:
  - pushrank.io
  - Pushrank
tags:
  - seo
  - tool
  - ai-seo
  - french
sources:
  - "[[jotaro-seo-ia-x-seo]]"
  - "[[jotaro-seo-content-strategy]]"
  - "[[jotaro-seo-chatgpt-sales]]"
source_count: 3
status: active
updated: 2026-07-22
note: "MAJ 2026-07-22 : sorti de pré-lancement, usage réel confirmé sur harnais-chien-expert.fr via intégration MCP Claude Code. Voir section Usage réel."
---

# PushRank

**Definition:** Outil de monitoring et de recommandations SEO piloté par IA, développé par @JotaroSeo (Souleymane) et une équipe de devs (dont @hamada_fahari et @ArbieuL). Analyse quotidienne du site, monitoring concurrentiel, recommandations personnalisées actionnables.

## Ce qu'on sait (mis à jour après usage réel)

- **Sorti de la phase pré-lancement** décrite en 2026-06 → outil accessible via connecteur MCP dans Claude Code (`claude mcp add`), avec authentification OAuth côté claude.ai.
- **Connexion Google Search Console** : PushRank lit des snapshots GSC retenus (jamais d'appel live/URL Inspection). Rétention ~90 jours, jusqu'à 50 périodes disponibles.
- **Moteur d'opportunités** : classe chaque problème détecté en `type` + `severity` (high/medium/low) + `priorityScore`. Types rencontrés :
  - `quick_win` — page qui ranke déjà avec un défaut on-page corrigible.
  - `decay` — signal de baisse de performance. **Peu fiable sur un jeune projet** : nécessite un vrai historique GSC (volume absolu d'impressions), pas juste du temps écoulé — voir note fiabilité ci-dessous.
  - `winner` — page qui performe bien, recommandation de renforcement (CTA, maillage interne).
  - `new_query` — nouvelle requête détectée dans GSC, pas encore couverte par une page dédiée.
  - `ai_recommendation` — audits variés générés par IA (title trop long/court, meta hors fourchette, mot-clé absent du title, contenu insuffisant, CTR à améliorer). Le plus utile en pratique mais le moins prévisible dans son format (`pageUrl` parfois `null`).
  - `cannibalization`, `indexation`, `sitemap`, `internal_linking`, `content_creation`, `site_drop`, `trending_query`, `low_ctr` — types listés dans le schéma mais peu vus en usage réel.
- **Workflow de statut** : `todo` → `in_progress` / `done` / `ignored`. **Piège découvert** : un item marqué `ignored` peut être remis en `todo` automatiquement si PushRank le re-détecte lors d'un scan ultérieur — le statut "ignoré" n'est pas permanent, il faut le re-fermer à chaque réapparition.
- **Bug outil connu** : le paramètre `severity=low` (et `priority=low/high/medium`) de l'outil de listing renvoie systématiquement 0 résultat quel que soit le `status`, alors que le compteur global (`get_project_overview`) affiche bien des dizaines d'items en `low`. Aucun contournement trouvé via les paramètres disponibles — les items priorité basse restent inaccessibles par l'API/MCP, consultables seulement dans l'interface web.
- **Écart de comptage** : le total affiché par `get_project_overview` peut largement dépasser ce que `list_seo_opportunities` peut effectivement énumérer (ex: 136 annoncés vs 25 récupérables) — probablement des doublons d'historique de (re-)détection côté PushRank, pas un vrai delta d'items uniques.
- Panneau web **"Santé SEO technique"** (pages orphelines, meta trop longues, maillage insuffisant, heading hierarchy skip, title=H1...) — **non exposé** par les outils MCP disponibles ; consultation uniquement via l'interface web, aucun outil pour lister les URLs concernées par ce biais.
- Aucun outil MCP pour **relancer un crawl/audit manuellement** — tous les outils disponibles sont en lecture (ou changent un statut). Le rescan semble automatique/périodique côté PushRank (nouvelles opportunités observées apparaître spontanément entre deux sessions).

## Fiabilité du signal `decay` — leçon opérationnelle

Sur un projet PushRank jeune (GSC connecté depuis <48h au moment du diagnostic), la quasi-totalité des opportunités `decay` se sont révélées être du bruit statistique, pas une vraie tendance : les pages concernées avaient un volume d'impressions trop faible (2 à 15 sur 3 mois) pour qu'une comparaison avant/après ait un sens. **Ce n'est pas une question de temps écoulé** (PushRank retient jusqu'à ~3 mois d'historique GSC dès la connexion) mais de **volume absolu** — une page à 2 impressions/semaine reste bruitée même après plusieurs mois d'attente si son trafic ne grossit pas.

**Règle pratique retenue** : avant de traiter un item `decay`, croiser avec le volume réel de la page (dimension `page` du snapshot GSC) — n'agir/revérifier que sur les pages ayant déjà une base d'impressions notable (ex: >30-40 sur 3 mois). Sous ce seuil, ignorer et ne pas re-prioriser tant que le volume de base n'a pas grossi.

## Usage réel — harnais-chien-expert.fr (session 2026-07-21/22)

Premier gros audit + corrections réalisé sur ce store (voir aussi contexte [[maillage-interne]] pour les sessions précédentes sur le même site).

**Corrections appliquées suite aux recommandations PushRank :**
- Meta descriptions manquantes (`/blogs/news`) → ajoutées.
- H1 dupliqué sur 15 pages (14 pages statiques + 1 fiche produit, cause commune : bannière de thème + H1 dans le contenu) → détail complet dans [[h1-heading-tag]].
- Title trop long sur 108 pages → cause racine unique : bug de suffixe de marque dupliqué dans le thème Shopify (voir [[h1-heading-tag]] et [[canonical-tag]] pour les cas connexes), pas 108 corrections manuelles séparées. Retombé à 29 après le fix.
- 73 meta descriptions produits hors fourchette 150-160 caractères → réécrites en lot, voir [[meta-description]].
- Cannibalisation du mot-clé principal ("harnais chien" home vs collection) → analysée en profondeur, voir [[keyword-cannibalization]] pour le cas complet et l'erreur méthodologique commise (check SERP-similarity oublié initialement).
- Titre SEO ne contenant pas le mot-clé exact visé (mot inséré au milieu cassant le match exact, ex: "Harnais **Anti-Traction** Bouledogue Français" ne matche pas "harnais bouledogue français") → pattern à surveiller systématiquement sur les titles SEO e-commerce.

**Constat sur les recommandations `ai_recommendation` de type "renforcer le CTR"** : une reformulation orientée accroche (format question, bénéfice) peut faire perdre le mot-clé principal de la meta description si on n'y prête pas attention — corrigé après coup sur l'article guide des tailles. Toujours vérifier qu'une réécriture CTR conserve le mot-clé cible, pas seulement l'accroche.

## Relations
- Built by [[jotaro-seo]].
- Complements the strategies taught in [[jotaro-seo-ia-x-seo]] (AI SEO monitoring) and [[jotaro-seo-content-strategy]].
- Usage croisé avec [[ubersuggest]] sur le même projet (harnais-chien-expert.fr) : les deux outils remontent des listes de problèmes qui se recoupent partiellement (ex: title trop long) mais avec des seuils/méthodologies différents — utile de croiser les deux plutôt que de se fier à un seul.
- Voir [[seo-audit]] pour la méthodologie générale d'audit dans laquelle PushRank s'inscrit.

## Tensions / open questions
- Pricing toujours non confirmé en usage réel.
- Fiabilité du signal `decay` sur jeune domaine à réévaluer une fois plus de volume accumulé (voir section dédiée ci-dessus).
- Panneau "Santé SEO technique" (pages orphelines, maillage) reste une boîte noire côté API — dépendant de captures d'écran manuelles de l'utilisateur pour être exploité.

## Sources
- [[jotaro-seo-ia-x-seo]] — AI SEO monitoring positioned as a use case.
- [[jotaro-seo-content-strategy]] — fullest description of planned features.
- [[jotaro-seo-chatgpt-sales]] — mentioned in context of SEO automation.
- Usage réel session 2026-07-21/22 sur harnais-chien-expert.fr (pas de source `raw/` — expérience directe via l'intégration MCP).
