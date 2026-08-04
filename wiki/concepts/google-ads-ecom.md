---
type: concept
title: "Google Ads E-commerce"
slug: google-ads-ecom
tags: [ecommerce, google-ads, sea, shopping, merchant-center, roas, retargeting]
sources: ["[[lameute-google-ads-influence-2026]]"]
source_count: 1
status: active
updated: 2026-08-04
---

# Google Ads E-commerce

**Définition :** Système d'acquisition payante qui capte une **demande déjà exprimée** (mots-clés, Shopping) plutôt que de la créer — à l'inverse de [[meta-ads-ecom]]. Facturation au clic (CPC) : on ne paie que si l'utilisateur clique, contrairement à Meta qui facture dès l'impression.

## L'équation de validation (avant de dépenser un euro)
```
CPC moyen × visiteurs nécessaires pour 1 vente  <  marge unitaire  →  lancer
```
- CPC moyen = (enchère haut de page basse + haute) / 2 — **jamais le CPC bas**.
- Visiteurs nécessaires = inverse du taux de conversion (0,5% → ×200, hypothèse pessimiste par défaut).
- Marge unitaire = prix de vente − (achat + shipping + tous les coûts).
- ⚠️ Piège : ne pas utiliser le taux de conversion **global** d'un site avec blog SEO (le trafic informationnel l'écrase) — recalculer sur les **requêtes transactionnelles** via Search Console.

## Campagne Shopping (80% du budget)
CPC manuel réglé sur le CPC **moyen** (jamais le bas — cause n°1 d'une campagne qui ne diffuse pas, c'est un plafond pas un coût payé). Budget quotidien = CPC moyen × 50. Sous-type Shopping standard, jamais Performance Max en direct. Laisser tourner 5-7 jours sans y toucher.

## Merchant Center — la règle qui conditionne tout
**Cohérence stricte et littérale** entre le site et le Merchant Center (adresse au caractère près, délais = traitement + livraison additionnés, frais de port identiques). Motif de suspension n°1 : "misrepresentation" (faux avis, prix barrés jamais pratiqués, promesses non tenues) — **convergence directe avec le principe zéro-tromperie** du GATE HALAL de ce vault. Détail complet → [[merchant-center-conformite]].

## Pilotage : la métrique pivot
**ROAS break-even**, pas le ROAS dans l'absolu. Ne jamais trancher avant 7-10 jours ou moins de 30-60€ de dépense par produit. Isoler un produit dès **3 ventes et ROAS ≥ 1,5× break-even** (règle des 3). Ratio budget testing/scaling : **~20/80** (un 50/50 rend la rentabilité mathématiquement impossible).

## Retargeting complémentaire
97-99% des visiteurs Google Ads/SEO ne convertissent pas au premier passage (trafic qualifié mais froid, 7-15 points de contact nécessaires) → recibler sur Meta/TikTok. Détail → [[retargeting]].

## Relations
- Complémentaire à [[meta-ads-ecom]] : Meta = intention froide/création de demande, Google = intention chaude/capture de demande. Beaucoup de praticiens lancent Google Ads 1-2 mois après avoir validé le SEO ([[seo-roadmap]]), le site étant trop jeune pour le Merchant Center sinon.
- Mots-clés transactionnels courts/moyens visés en Search Acquisition rejoignent la logique [[long-tail-keywords]] côté SEO (longue traîne = fiches produit, traîne moyenne/courte = Search Ads).
- Convergence gate qualité : ce que Google sanctionne sur Merchant Center (faux avis, fausse urgence) recoupe exactement les signaux de pénalité déjà documentés côté SEO → [[black-hat-seo]].
- Détail opérationnel complet (setup, campagnes, pilotage, checklist) → [[09 - Méthode e-com Google Ads/00 - Vue d'ensemble — Méthode e-com Google Ads]].

## Sources
- [[lameute-google-ads-influence-2026]] — formation La Meute module 13 + live Yassfox, via cerveau Obsidian Google d'un ami.
