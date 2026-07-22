---
type: concept
title: "Balise H1 et Hiérarchie de Titres (Heading Tags)"
slug: h1-heading-tag
tags: [seo, on-page-seo, technical-seo, e-commerce]
sources: []
source_count: 0
status: active
updated: 2026-07-22
note: "Créé 2026-07-22 à partir de cas vécus PushRank/Ubersuggest sur harnais-chien-expert.fr — pas de source `raw/` dédiée pour l'instant."
---

# Balise H1 et Hiérarchie de Titres (Heading Tags)

**Definition :** Le H1 est le titre principal visible d'une page — le signal on-page le plus fort après le title tag pour indiquer à Google le sujet de la page. Les balises H2/H3/H4... structurent le contenu en sous-sections. Contrairement au title tag (invisible pour le visiteur, affiché dans l'onglet/SERP), le H1 est lu directement par l'utilisateur sur la page.

## Règles de base

- **Un seul H1 par page.** Plusieurs H1 diluent le signal de pertinence — Google doit deviner lequel est "le" sujet principal.
- **Pas de saut de niveau** (ex: H1 → H3 directement, sans H2). Casse la lisibilité de la structure sémantique pour les crawlers et les technologies d'accessibilité (lecteurs d'écran).
- **Title tag ≠ H1, idéalement.** Les deux peuvent partager le mot-clé principal, mais les faire identiques mot pour mot gâche une occasion : le title tag (plus contraint en longueur, visible en SERP) bénéficie d'ajouts que le H1 n'a pas besoin de porter — marque, différenciateur, variante de mot-clé. Un H1 et un title strictement identiques ne sont pas une erreur grave, mais un signal sous-exploité.

## Piège Shopify : H1 dupliqué par la bannière du thème

Cas rencontré sur harnais-chien-expert.fr (2026-07-21, remonté par [[pushrank]]) sur 15 pages (14 pages statiques type FAQ/CGV/mentions-légales + 1 fiche produit) : le thème Shopify affiche automatiquement un H1 "bannière" reprenant `page.title` en haut de la page (ex: `<h1>FAQ</h1>` généré par la section de header) — **et** le contenu de la page (`body_html`, rédigé dans l'éditeur Shopify) contenait *lui aussi* un H1 manuel en première ligne (ex: `<h1>Foire aux questions</h1>`). Deux H1 réels sur la même page, l'un généré par le thème, l'autre par l'éditeur de contenu — invisible à l'œil si on ne regarde pas le HTML rendu.

**Diagnostic** : inspecter le HTML rendu (pas l'éditeur Shopify) pour compter les occurrences réelles de `<h1>` — le bug n'est pas visible dans l'admin, seulement dans la sortie finale.

**Correctif appliqué** : repasser le H1 du contenu en H2 (`<h1>` → `<h2>`) via l'API Shopify (`body_html`), en laissant le H1 de bannière du thème comme unique titre principal sémantique. Ne jamais toucher à la section de thème pour ce cas — le contenu éditorial doit s'aligner sur la structure du thème, pas l'inverse (le thème est partagé par toutes les pages, le contenu est spécifique).

**Variante rencontrée sur une fiche produit** : le doublon ne venait pas du contenu principal mais d'une **popup cachée** (bloc "Size Chart" dans une modale, invisible par défaut) codée en dur dans une section du thème (`<h1 class="h2">{{ block.settings.chart_id }}</h1>`) — la classe CSS `h2` habillait déjà le texte visuellement en H2, seule la balise sémantique était fautive. Correctif : renommer la balise `h1`→`h2` dans le fichier de section du thème (edit d'une ligne, zéro changement visuel puisque le style était déjà celui d'un H2). Leçon : un doublon de H1 peut être **invisible visuellement** (masqué dans une modale, un onglet, un accordéon fermé) — ne pas se fier à ce qui est visible au premier chargement de la page pour auditer les headings.

## Ouvert : "heading hierarchy skip" et "title equals h1"

Deux issues détectées par un audit [[ubersuggest]] (`heading_hierarchy_skip` ×27 pages, `title_equals_h1` ×17 pages) sur harnais-chien-expert.fr le 2026-07-22, mais **pas encore diagnostiquées en détail** — l'outil ne remonte qu'un compteur agrégé sans liste d'URLs pour ces deux catégories précises (contrairement à `title_long`/`meta_description_empty` où le détail par URL était accessible). Nécessite soit un export manuel depuis l'interface web, soit un audit ad hoc page par page. À date, hypothèse non vérifiée : `title_equals_h1` concerne probablement les pages où aucun metafield `global.title_tag` n'a été positionné (le title retombe alors par défaut sur le même texte que le H1) — cohérent avec le pattern déjà observé sur [[meta-description]] pour les pages sans metafield SEO dédié.

## Relations
- [[meta-description]] — même famille de signaux on-page ; les deux souffrent du même pattern Shopify "pas de metafield SEO dédié → repli sur une valeur par défaut peu optimisée".
- [[canonical-tag]] — autre cas de duplication détecté sur le même site (pages légales `/policies/*` vs `/pages/*|`), racine différente (architecture Shopify) mais même famille de symptôme (duplicate content signal).
- [[keyword-cannibalization]] — un H1 mal aligné avec le mot-clé cible réel de la page peut contribuer à un flou de pertinence, à vérifier conjointement lors d'un diagnostic de cannibalisation.
- [[maillage-interne]] — la structure de heading fait partie du même audit technique global que le maillage interne (cf. panneau "Santé SEO technique" [[pushrank]]).
- [[jotaro-seo-keyword-cannibalization]] — rappel du principe général : un signal de pertinence dupliqué/dilué (ici le H1) affaiblit la même mécanique que la cannibalisation de mots-clés, à une échelle différente (une page vs plusieurs pages).

## Tensions / open questions
- Faut-il systématiquement différencier title et H1, ou est-ce un gain marginal ne valant pas l'effort sur un site avec beaucoup de pages ? Pas de réponse tranchée à date.
- `heading_hierarchy_skip` et `title_equals_h1` restent à diagnostiquer précisément (pas de liste d'URLs récupérée à date) — prochaine session PushRank/Ubersuggest à documenter ici une fois fait.

## Sources
- Usage réel sessions 2026-07-21/22 sur harnais-chien-expert.fr (pas de source `raw/` — expérience directe via PushRank/Ubersuggest MCP + API Shopify Admin).
