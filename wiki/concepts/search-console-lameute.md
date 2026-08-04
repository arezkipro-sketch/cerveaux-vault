---
type: concept
title: "Search Console (méthode La Meute) — indexation, mesure, nettoyage"
slug: search-console-lameute
tags: [search-console, indexation, mesure, seo, sitemap]
sources: ["[[lameute-google-ads-influence-2026]]"]
source_count: 1
status: active
updated: 2026-08-04
---

# Search Console (méthode La Meute)

**Définition :** Présentée comme l'outil le plus important en SEO — seule source de données **exactes** (clics, impressions, CTR, position moyenne), là où les outils tiers ne donnent que des estimations. Complète [[google-search-console]] déjà présent dans ce vault avec le protocole de mise en place et d'exploitation détaillé.

Trois usages : **indexer** (sans soumission, un site neuf peut rester hors index), **mesurer**, **nettoyer**.

## Les 4 métriques
- **Impression** : apparition en résultats sans clic — mesure la visibilité brute.
- **Clic** : trafic SEO réel.
- **CTR moyen** : part des impressions transformées en clics — **le levier le moins cher** (réécrire titre/meta fait gagner des clics sans changer de position).
- **Position moyenne** : seule métrique où plus bas est meilleur (1 = top 1).

## Mise en place
1. Propriété type **Domaine**, validée par enregistrement **TXT** en zone DNS. Un échec immédiat est normal (propagation) — attendre plutôt que multiplier les entrées.
2. **Demander l'indexation manuellement** : accueil d'abord, puis collections. **~10 URL/jour maximum** → prioriser, puis indexer les premiers articles ; ensuite le maillage interne fait découvrir le reste.
3. **Soumettre le `sitemap.xml`** (index de 4 sous-sitemaps sur Shopify : produits, pages, collections, blogs) — premier point d'entrée du robot, à ne pas confondre avec le sitemap HTML destiné aux visiteurs → [[maillage-interne-cocon-lameute]].
4. Vérifier avec une requête `site:` — vide au début, c'est normal (données à J+quelques jours).

## Exploitation récurrente — l'essentiel se joue dans "Requêtes" et "Pages"
- **Requêtes** triées par **clics** = d'où vient réellement le trafic. Triées par **impressions** = où l'on est visible sans être cliqué → réécrire titre et meta pour gagner du CTR sans bouger de position.
- **Pages** : identifier ce qui rapporte. Cas d'école cité : ~70% du top 10 des pages sont des articles de blog, ce qui valide la stratégie éditoriale — et impose d'y placer CTA et liens internes vers les fiches produits → [[blogs-redaction-seo-lameute]].
- **Appareils** : sert surtout à confirmer la priorité mobile.
- **Recommandations** : Google signale les chutes anormales → croiser avec les modifications récentes du site pour identifier la cause.

## Nettoyage
- **404 : priorité haute** → redirections.
- **"Explorée, actuellement non indexée"** : à traiter — c'est là que se trouvent les pages qu'on veut voir rankées → inspecter et demander l'indexation.
- **"Autre page avec balise canonique correcte"** : à ignorer — variantes produits, non-indexation normale en e-commerce (pas un bug malgré le volume apparent).
- **Core Web Vitals** : pages lentes → premier réflexe, les images → [[seo-on-site-lameute]].
- **Arbitrage** : une page en ligne depuis ~1 an qui ne ranke pas et n'a jamais vendu → la retravailler ou la supprimer.

## Limite
La valeur de l'outil dépend de l'existence de contenu — sans articles, les onglets Requêtes et Pages restent pauvres.

## Relations
- Version déjà présente dans ce vault : [[google-search-console]].
- Alimente le pilotage kill/scale côté SEO comme côté [[google-ads-ecom]] (même logique de mesure avant décision).

## Sources
- [[lameute-google-ads-influence-2026]] — formation La Meute module 10 (vidéo 125), via cerveau Obsidian Google d'un ami.
