---
type: concept
title: "Maillage Interne (Internal Linking)"
slug: maillage-interne
tags: [seo, internal-linking, architecture, crawling]
sources: ["[[jotaro-seo-google-bots]]", "[[jotaro-seo-content-strategy]]", "[[jotaro-seo-keyword-cannibalization]]", "[[jotaro-seo-4-months-textile]]", "[[jotaro-seo-301-redirects]]", "[[crawl-budget-guide]]", "[[semrush-seo-checklist-41]]", "[[jotaro-seo-strategie-ecommerce-2026]]"]
source_count: 8
status: active
updated: 2026-06-18
---

# Maillage Interne (Internal Linking)

**Definition:** The network of hyperlinks connecting pages within the same website. Serves three purposes simultaneously: guides Googlebot through the site (crawlability), distributes [[link-juice]] between pages (authority flow), and reduces [[keyword-cannibalization]] by creating clear thematic hierarchies.

## What we know
- **Googlebot navigation**: bots follow links page-to-page; strong internal linking ensures all priority pages are discovered and crawled. "D'où l'importance d'avoir un bon maillage interne !" — *(explicitly cited as critical in [[jotaro-seo-google-bots]])*.
- **Link juice flow**: internal links pass authority from high-authority pages to strategic commercial pages — the core mechanism of [[cocon-semantique]] → [[jotaro-seo-keyword-cannibalization]].
- **Cannibalization prevention**: well-structured internal links + cocon sémantique signal to Google which page should rank for which keyword → [[jotaro-seo-keyword-cannibalization]].
- **Technical audit check**: internal linking quality is one of the first things checked in an [[seo-audit]] → [[jotaro-seo-4-months-textile]].
- **Anchor text rule (absolute)**: anchor = exact keyword of the destination page. ❌ "cliquez ici", "en savoir plus" ✅ "console retrogaming portable", "formation copywriting en ligne" → [[jotaro-seo-content-strategy]].
- **Quantity rule**: 1-2 internal links per article maximum. More = diluted value per link → [[jotaro-seo-content-strategy]].
- **Direction priority**: link toward the most relevant commercial page (collection, service page, product page) → [[jotaro-seo-content-strategy]].

## Règle de distribution des liens internes (articles de blog)

Parmi les 2-3 liens internes d'un article de blog, **au moins un doit pointer vers un autre article de blog** (pas uniquement vers des pages piliers ou des fiches produit). Cela maintient le lecteur dans l'écosystème éditorial du site et renforce la cohérence sémantique entre articles.

Distribution recommandée pour un article de blog :
- 1 lien → **autre article de blog** (contenu éditorial connexe)
- 1-2 liens → **page pilier ou page commerciale** (produit, service, collection)

## Pages orphelines

Une **page orpheline** = page sans aucun lien interne. Elle est invisible pour Google sauf si elle est dans le sitemap ou dispose de backlinks externes. Toute page doit avoir ≥ 1 lien interne entrant depuis une page pertinente → [[semrush-seo-checklist-41]].

Semrush Audit de site → Problèmes → "pages orphelines" (nécessite Google Analytics connecté).

**Nuance orpheline stricte vs faiblement liée (session 2026-07-07, harnais-chien-expert.fr) :** un produit listé dans une collection elle-même présente dans le menu n'est PAS orphelin strict — Google l'atteint via `menu → collection → produit`. Le vrai problème actionnable est le produit **faiblement lié** : 0 lien de *contenu* entrant (aucune fiche produit ni article ne pointe dessus), donc il ne reçoit du jus que des pages-listes. À traiter au même titre.

**Détection sans Semrush/GA — via l'API Shopify (méthode session) :** tirer le `body_html` de tous les produits/collections/articles (GraphQL), extraire les `href`, construire la map `cible → sources`. Tout produit avec 0 source de contenu = à retisser. Sur les 88 produits du store : 11 faiblement liés détectés ainsi (dont 4 accessoires hors chaîne).

**Règle anti-orpheline = fermer l'anneau.** Une chaîne produit→produit non bouclée casse en segments : les « têtes » de segment ont 0 lien entrant. Un **anneau fermé** (1→2→…→N→1) garantit mathématiquement ≥1 entrée par nœud. Vérifier après coup : `inbound[chaque produit] ≥ 1`.

**Piège du produit ajouté après coup :** un SKU créé après la mise en place de la chaîne n'y est pas inséré automatiquement → il devient faiblement lié. À chaque nouveau produit : lui donner 1 lien entrant depuis un voisin **de la même collection** (thématique, pas ordre de catalogue arbitraire) + son lien vers la collection mère.

## Structure en silo (3 niveaux) — appliqué e-commerce

Approche JotaroSEO pour les boutiques e-commerce. Les liens circulent du bas vers le haut pour concentrer l'autorité SEO sur les pages les plus importantes.

**Niveau 1 — Page pilier :** page d'accueil ou collection principale ciblant le mot-clé principal (ex : "cagoule", "ours en briques décoratif").

**Niveau 2 — Collections secondaires :** pages ciblant les variantes (ex : "cagoule en laine", "cagoule ski", "ours en briques noir").

**Niveau 3 — Produits et articles de blog :** fiches produit individuelles + articles blog (ex : "cagoule laine mérinos homme", "comment choisir sa cagoule pour le ski").

Flux d'autorité : Niveau 3 → Niveau 2 → Niveau 1.

→ [[jotaro-seo-strategie-ecommerce-2026]]

## Règle des 2 liens sur chaque fiche produit (e-commerce)

Sur chaque fiche produit, intégrer systématiquement 2 liens internes :
- **Lien 1** → vers le produit suivant dans la même collection (ex : "cagoule en laine noire" → "cagoule en laine grise")
- **Lien 2** → vers la page de collection parente

Cette règle crée une chaîne de maillage qui fait circuler l'autorité entre tous les produits d'une collection et remonte cette autorité vers la page collection.

→ [[jotaro-seo-strategie-ecommerce-2026]]

## Relations
- Foundation of [[cocon-semantique]]: pages filles link to page mère = concentrated authority.
- Preserves [[link-juice]] within the site without depending on external backlinks.
- Guides [[google-bots]] to crawl priority pages first.
- Solution to [[keyword-cannibalization]]: clear linking hierarchy disambiguates which page targets which keyword.
- Must be maintained after [[301-redirect]] migrations to avoid broken internal link chains.

## Tensions / open questions
- **Contradiction de sources** : JotaroSeo recommande **1-2 liens internes maximum** par article (pour ne pas diluer la valeur) → [[jotaro-seo-content-strategy]] ; Sédestral recommande **2-3 liens internes minimum** par article → [[sedestral-blog-article-seo-2026]]. Règle probable : 2-3 liens pour les longs formats (>1 500 mots), 1-2 pour les courts.
- At what internal link density does Google start treating links as noise rather than signals?

## Sources
- [[jotaro-seo-google-bots]] — bots follow internal links; critical for indexation.
- [[jotaro-seo-content-strategy]] — exact anchor text rule; 1-2 links max per article.
- [[jotaro-seo-keyword-cannibalization]] — internal linking as solution to cannibalization.
- [[jotaro-seo-4-months-textile]] — internal linking as audit checkpoint.
- [[jotaro-seo-301-redirects]] — 301s repair broken internal link chains.
- [[crawl-budget-guide]] — logical internal structure + sitemap so Googlebot doesn't waste crawl budget; "road network" metaphor.
