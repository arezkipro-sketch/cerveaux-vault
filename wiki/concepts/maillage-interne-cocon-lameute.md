---
type: concept
title: "Maillage interne, cocon sémantique & sitemap (méthode La Meute)"
slug: maillage-interne-cocon-lameute
tags: [seo, maillage-interne, cocon-semantique, silo, sitemap, crawl]
sources: ["[[lameute-google-ads-influence-2026]]"]
source_count: 1
status: active
updated: 2026-08-04
---

# Maillage interne, cocon sémantique & sitemap (méthode La Meute)

**Définition :** Comment les liens internes guident le crawler et distribuent l'autorité sur une boutique Shopify. Application e-commerce du principe déjà documenté dans [[maillage-interne]] et [[cocon-semantique]].

## Les 5 principes
1. Un seul et même domaine (par opposition aux backlinks, traités en off-site → [[backlinks]]).
2. Quantité et qualité : trop de liens dilue le jus, trop peu prive les pages profondes.
3. **Règle des 3 clics** : aucune page à plus de 3 clics de l'accueil — le crawler a un budget de crawl limité.
4. **Aucune page orpheline** : toute page doit recevoir au moins un lien entrant.
5. Hiérarchie : plus un lien est haut dans la page, plus il transmet de force.

**Ancres** : en interne, les ancres exactes sont acceptables (pas de sur-optimisation sur son propre site, contrairement au netlinking externe). Privilégier des liens contextuels naturels dans le texte plutôt qu'une phrase-type dupliquée en bas de chaque fiche (signal de contenu identique partout).

## Cocon sémantique / architecture en silo appliquée à Shopify
Trois niveaux : **page pilier (accueil) → pages intermédiaires (collections) → pages finales (produits)**.
- Les pages sœurs se lient entre elles : collections avec collections, produits avec produits **d'une même collection** — pas de liens entre produits de familles différentes.
- Boucle de collections fermée au sein d'une famille ; boucle de produits dans l'ordre manuel de la collection.
- **2 liens par fiche produit** : 1 vers le produit suivant + 1 vers la collection mère (3 liens = trop, dilue).
- **Le dernier produit ne reboucle pas sur le premier** — il pointe uniquement vers la collection (sinon toute la boucle serait à refaire à chaque nouveau produit).
- Hiérarchie de puissance : accueil > collections > produits.

## Quand le faire
**Dès la création du site.** Le faire en cours de route génère des 404 (URL modifiées après indexation) — red flag à corriger en identifiant toutes les pages qui pointaient vers l'ancienne URL. Bénéfice caché : mailler oblige à visiter chaque page une par une, ce qui fait remonter doublons et cannibalisations.

## Sitemap
- **XML** : généré automatiquement par Shopify (`/sitemap.xml`, index de 4 sous-sitemaps : produits, pages, collections, blogs) — à conserver tel quel, sert aussi à analyser les concurrents.
- **HTML** : page à créer soi-même, listant toutes les URL du site, liée depuis le footer — rattrape les pages isolées que le maillage n'a pas atteintes.

## Relations
- Le principe général (page mère/pages filles côté contenu éditorial) est déjà documenté → [[cocon-semantique]], [[maillage-interne]].
- Application spécifique à la navigation/collections Shopify → [[mega-menu-collections-shopify]].
- Le jus SEO distribué ici rejoint la mécanique détaillée dans [[e-e-a-t-jus-seo-lameute]].

## Sources
- [[lameute-google-ads-influence-2026]] — formation La Meute module 9 (vidéos 104-105), via cerveau Obsidian Google d'un ami.
