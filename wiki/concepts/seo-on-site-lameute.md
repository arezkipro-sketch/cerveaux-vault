---
type: concept
title: "SEO on-site Shopify (méthode La Meute) — domaine, images, fiches, structure HTML"
slug: seo-on-site-lameute
tags: [seo, on-page, shopify, fiche-produit, images, structure-html]
sources: ["[[lameute-google-ads-influence-2026]]"]
source_count: 1
status: active
updated: 2026-08-04
---

# SEO on-site Shopify (méthode La Meute)

**Définition :** Application opérationnelle du SEO on-page à une boutique Shopify. Fil rouge post-AI Overview : Google récompense l'**expérience client** (branding, avis, garanties, vitesse) et le **contenu digestible** (listes, tableaux, FAQ) plutôt que le bourrage de mots-clés. Complète [[technical-seo]] et [[seo-audit]] déjà présents dans ce vault avec le détail Shopify.

## Nom de domaine
Tester d'abord l'EMD ; sinon semi-EMD (mot-clé + mot brandé) ; 2-3 mots max, extension .com ou .fr uniquement. **Tiret dans les noms composés** (Google lit les mots séparément). **Acheter chez un registrar externe (type OVH), jamais chez Shopify** — sinon le domaine appartient légalement à Shopify. Le bonus EMD décroît depuis le filtre 2012 ; arbitrer avec le branding (un EMD trop littéral peut donner un effet "site jetable").

## Images
- **WebP obligatoire, 100-200 Ko idéal (300 max), format carré** (800×800) sauf bannières. Page > 3s = trop lente.
- Nommer le fichier avec des **mots-clés variés** dérivés du titre produit (jamais le même nom partout) → ranking sur la longue traîne d'images.
- **Alt text** : décrire l'image entière, pas seulement le produit.
- **Au moins une image sans texte par produit** — obligatoire pour Merchant Center ([[merchant-center-conformite]]).
- Chaîne de production : récupérer en haute qualité → nettoyer les textes incrustés (cleanup.pictures) → convertir en WebP (Squoosh, qualité ~75) → vérifier dans Contenu → Fichiers (un fichier nommé .webp peut être resté un PNG lourd en interne).

## Fiche collection
- Volume cible **1000-8000** (éviter les 50 000+, trop concurrentiels pour une collection).
- **Type de collection : toujours manuel** — un tri automatique change l'ordre à chaque vente et casse le maillage produit→produit.
- **Anti-cannibalisation** : si deux requêtes donnent ≥8 résultats identiques sur 10 → une seule page (garder celle avec le plus de volume/produits), sinon redirection propre.
- Description : mots-clés principaux + LSI + 3-4 questions PAA en H2/H3. Texte SEO court (~200 caractères) juste sous le H1 (premier texte lu par le crawler).
- Meta title ~60 caractères ; meta description <150-155 caractères commençant par un verbe d'action (pas de poids SEO direct, joue sur le CTR).

## Fiche produit
- Titre en longue traîne même à très faible volume (10, voire 1-2 recherches/mois) → trafic ultra-qualifié, position 1 facile. **Commencer par le nom de la collection** ("Sac à dos" → "Sac à dos noir pour homme").
- **Le nombre de produits d'une collection est un facteur de classement**, à condition que les noms soient sémantiquement liés.
- Description 150-200 mots, pensée d'abord pour l'utilisateur. `<strong>` réservé aux mots-clés à valeur SEO, le reste en `<b>` — jamais de `<strong>` dans un Hn.
- Liens de maillage **contextuels dans le corps du texte**, pas en bloc dupliqué en bas de page.
- Meta title ≤ 70 caractères (convention unique sur tout le site) ; slug propre, accents supprimés.

## Structure HTML — nettoyage du thème
Cible : un seul H1 avec le mot-clé, H2→H3 sans doublons ni Hn parasites (logo en H1, panier tiroir, cartes collection en double, FAQ, footer). Auditer avec une extension type Detailed SEO (onglet Headings). **Règle critique : ne jamais mettre à jour le thème après modification du code Liquid** (perte des optimisations) — toujours dupliquer le thème avant intervention.

## Balise `<details>`/`<summary>`
Accordéon HTML : texte masqué à l'utilisateur mais lu par le crawler. Usage en bas de page d'accueil pour donner de la matière textuelle sans casser le design — mot-clé dans le `<summary>`, liens internes dans le texte.

## Diviser les produits (SEO Variants)
Une fiche par variante (couleur/dimension) plutôt qu'une fiche à N variantes — permet de passer de ~50 à 200+ produits, chaque fiche captant sa propre longue traîne. Faire varier les images entre variantes.

## Halal
Spécifier tous les matériaux et caractéristiques réels (matière, dimensions, capacité) ; en cas de sources contradictoires, annoncer la valeur la plus basse ; supprimer toute donnée non vérifiée ; pas de faux compteur de stock. Cohérent avec [[dropshipping-halal]].

## Relations
- Version générale déjà présente dans ce vault : [[technical-seo]], [[seo-audit]], [[image-seo]], [[h1-heading-tag]], [[canonical-tag]].
- S'articule avec [[maillage-interne-cocon-lameute]] (liens internes), [[mega-menu-collections-shopify]] (arborescence collections) et [[recherche-mots-cles-lameute]] (mapping page↔mot-clé).

## Sources
- [[lameute-google-ads-influence-2026]] — formation La Meute module 9, via cerveau Obsidian Google d'un ami.
