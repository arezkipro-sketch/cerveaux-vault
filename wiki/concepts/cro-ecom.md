---
type: concept
title: "CRO E-commerce"
slug: cro-ecom
tags: [ecommerce, cro, conversion, aov, bundles, upsell, ab-test, shopify, landing-page]
sources: ["[[rayecom-guide-ecom-complet]]"]
source_count: 1
status: active
updated: 2026-06-28
---

# CRO E-commerce (Conversion Rate Optimization)

**Définition :** Ensemble des techniques visant à maximiser le taux de conversion et le panier moyen (AOV) d'une boutique e-commerce, sans augmenter le budget publicitaire. Chaque point de CVR gagné améliore directement la rentabilité de chaque euro investi en Meta Ads.

## Ce qu'on sait (source : [[rayecom-guide-ecom-complet]])

### Landing pages
5 types :
- **Page de collection** — présente une gamme de produits
- **LP classique** — fiche produit optimisée conversion
- **Listicle** — format "top X raisons de..." ou comparatif
- **Advertorial** — article éditorial sponsorisé
- **Quiz** — parcours personnalisé qui qualifie le prospect

⚠️ Il n'existe pas de format supérieur aux autres. La meilleure LP = celle que tes concurrents qui scalent utilisent. Analyser avant de construire.

### Augmenter l'AOV — bundles

**Offres en volume :**
- 1+1 (le plus populaire) / 2+2 / 2+1 offert / 3+2 offert

**Avec cadeaux :**
- Cadeau physique offert (à partir d'un certain montant)
- E-book offert (coût production ≈ 0, valeur perçue élevée)
- Combinaison cadeau + e-book → maximum de valeur perçue

**Principe clé :** le bundle rend l'offre irrésistible. Le prospect perçoit qu'il reçoit plus que ce qu'il paie → taux de conversion + AOV augmentent simultanément.

**Source d'inspiration upsells :** Amazon → "fréquemment achetés ensemble" → ajouter ces produits en upsell.

### Optimiser le panier

| Élément | Rôle | Impact |
|---|---|---|
| Timer (5-10 min) | Urgence → réduire abandons | Conversion |
| Barre de progression | "Plus que X€ pour la livraison gratuite" | AOV naturel |
| Bumps | Produit complémentaire dans le panier | AOV |
| Badges de réassurance (haut + bas panier) | Supprimer dernières hésitations | Conversion |

### Upsells post-achat
Intervient **juste après l'achat** — résistance psychologique au plus bas, carte déjà sortie.

- **Même produit à -50%** → 1 clic, pas de ressaisie de carte. Puissant sur produits consommables.
- **Produit complémentaire logique** → améliore directement le résultat du produit principal.

⚠️ **Règle d'or** : l'upsell doit sembler logique et dans l'intérêt du client. Forcé → méfiance → remboursements.

### A/B tests

**Conditions minimales :**
- Minimum **500 ventes par variante** avant d'analyser
- Test simultané sur le **même trafic** (pas comparaison semaine à semaine → conditions différentes)
- Outil recommandé : **IntelliGems** (éviter les apps Shopify classiques : données faussées)

**Métrique clé : marge nette par visiteur** (pas taux de conversion isolé ni CA par visiteur)
→ Exemple : CVR 2.6% × 52€ AOV = 1.40€ marge nette/visiteur > CVR 3% × 40€ AOV = 1.10€ marge nette/visiteur.
→ On scale la variante B même si elle convertit moins.

**Formule de fiabilité statistique :** Z ≥ 1.96 → 95% de confiance

### Microsoft Clarity (outil gratuit)
- Enregistre le parcours complet des visiteurs (heatmaps + replays)
- Gros taux de drop = endroit à optimiser en priorité
- Voir où les clients drop → savoir précisément où A/B tester

## Règles opérationnelles
1. Analyser les LP des concurrents qui scalent avant de construire la sienne
2. Calculer la marge nette par visiteur (pas le CVR seul) pour les A/B tests
3. Mettre en place Clarity dès le lancement pour identifier les zones de drop
4. Implémenter bundles + upsell dès que le testing est validé (avant d'optimiser les ads)

## Relations
- La LP prolonge l'émotion créée par la créative → [[creatif-ecom]]
- L'AOV améliore mécaniquement le ROAS Target → [[meta-ads-ecom]]
- Les emails post-achat (Klaviyo) prolongent la relation → source : [[rayecom-guide-ecom-complet]]

## Sources
- [[rayecom-guide-ecom-complet]] — types LP, bundles/upsells, optimisation panier, A/B tests, Clarity
