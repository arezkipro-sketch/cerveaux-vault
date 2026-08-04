---
type: concept
title: "Méga-menu et collections mère/fille (architecture Shopify)"
slug: mega-menu-collections-shopify
tags: [seo, shopify, mega-menu, collections, siloing, architecture]
sources: ["[[lameute-google-ads-influence-2026]]"]
source_count: 1
status: active
updated: 2026-08-04
---

# Méga-menu et collections mère/fille (architecture Shopify)

**Définition :** Application du [[cocon-semantique]] (page mère / pages filles) à la navigation d'une boutique Shopify : le méga-menu porte le maillage interne, le siloing thématique, l'UX et la conversion — considéré comme un prérequis, pas une option, une fois la [[recherche-de-niche-lameute]] et le tri des mots-clés faits.

## Collections mères et filles
- **Collection mère** : affichée en haut du menu, plus fort volume, englobante (ex. "Gigoteuse par âge").
- **Collections filles** : rangées dessous **par ordre de volume décroissant** — l'ordre distribue le jus SEO, exactement comme les pages filles d'un cocon sémantique classique irriguent la page mère, sauf qu'ici le sens du jus va de la structure de navigation vers les pages de collection.
- Le nom affiché peut différer du nom réel de la collection. Une fille peut avoir plus de volume que sa mère sans problème ; ne jamais inverser la hiérarchie logique du regroupement.
- Sans collection englobante naturelle : utiliser un intitulé de tri sans volume propre ("Gigoteuse par saison/âge") comme mère de façade.

## Construction
1. Bâtir le menu sur un outil de mind-mapping (mode organigramme) avec les volumes affichés à côté de chaque collection. **Ne jamais mélanger deux sources de volume** (SEMrush OU Ubersuggest, jamais les deux dans le même arbre — ça fausse le ratio relatif entre collections).
2. Shopify : créer d'abord les collections en **mode manuel** (jamais automatique — casse le maillage produit-produit, voir [[maillage-interne]]), puis les assembler dans Contenu → Menus.

## Piège technique connu (thème Dawn et dérivés)
Sur certains thèmes, cliquer sur la collection mère dans le méga-menu ne l'ouvre pas (elle ne sert que de conteneur visuel pour les filles). Contournement observé : lien `#` vide sur la mère + élément "Tout" pointant vers la collection réelle — sous-optimal en SEO (l'ancre "Tout" n'est pas descriptive). Correction propre : modifier le Liquid du thème pour rendre la mère cliquable directement.

## Relations
- Application e-commerce directe du principe déjà documenté pour le contenu éditorial → [[cocon-semantique]] : même logique mère/fille, cible différente (navigation transactionnelle vs cluster d'articles).
- Dépend de l'arborescence de mots-clés triée en amont → [[recherche-de-niche-lameute]].
- Le maillage produit-produit à l'intérieur des collections reste un sujet distinct → [[maillage-interne]].

## Sources
- [[lameute-google-ads-influence-2026]] — formation La Meute module 5 (vidéo 061) + module 9, via cerveau Obsidian Google d'un ami.
