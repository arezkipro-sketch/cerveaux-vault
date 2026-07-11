---
type: concept
title: "Meta Ads E-commerce"
slug: meta-ads-ecom
tags: [ecommerce, meta-ads, facebook-ads, instagram-ads, roas, cbo, testing, scaling]
sources: ["[[rayecom-guide-ecom-complet]]"]
source_count: 1
status: active
updated: 2026-06-28
---

# Meta Ads E-commerce

**Définition :** Système d'acquisition payante via Facebook + Instagram + Messenger + WhatsApp pour scaler un produit e-commerce. Canal recommandé par les praticiens francophones pour sa vitesse de feedback (48-72h) et son potentiel de scaling illimité.

## Ce qu'on sait (source : [[rayecom-guide-ecom-complet]])

### ROAS : les deux métriques structurantes

**ROAS Break-Even (BE)** = seuil minimum. En dessous : chaque euro investi crée une perte.
**ROAS Target** = retour générant 20-25% de marge nette → fenêtre de scaling.

**Calcul pondéré (obligatoire en multi-bundles) :**
1. Estimer la répartition des ventes par bundle (ex. 30% 1x / 50% 2x / 20% 3x)
2. COGS moyen = Σ(COGS bundle × % ventes)
3. Prix moyen = Σ(prix bundle × % ventes)
4. ROAS BE = Prix moyen / COGS moyen

→ Recalculer dès 50 ventes réelles, puis toutes les 2 semaines ou à chaque changement d'offre.

⚠️ **Erreur classique** : calculer le ROAS BE uniquement sur le bundle 1x. La répartition réelle peut rendre le business rentable (ou déficitaire) sans le savoir.

### Structure de testing (CBO)

| Paramètre | Valeur |
|---|---|
| Type de campagne | CBO (Campaign Budget Optimization) |
| Budget | 100 €/jour |
| Adsets | 1 seul, broad (aucun ciblage) |
| Objectif | ACHAT (pas ajout au panier) |
| Lancement | 00h le lendemain |
| Créatives | 10 à 15 dans l'adset |

### Règle de décision (testing)
- < ROAS BE → couper ou optimiser les créatives
- Entre BE et Target → maintenir + observer
- \> ROAS Target → augmenter budget (toutes les 24-48h)

⚠️ Ne jamais couper sur une métrique isolée. CPM élevé ≠ mauvais. La seule question : chaque euro investi rapporte-t-il suffisamment ?

### Paliers de scaling (EU uniquement)
100 → 200 → 300 → 400 → 500 → 700 → 1 000 → 1 500 €
Au-delà : paliers de +500 ou +1 000 selon les performances.

**Règle de gestion des CBO :** une CBO qui fonctionne → on n'y touche plus. On crée une nouvelle CBO en parallèle et on l'alimente avec de nouvelles créatives.

### Configuration compte Meta
- Profil Facebook "sain" : ancien compte avec activité OU compte récent chauffé 2-3 semaines
- Business Manager : 3 admins de backup (famille/proches) → filet de sécurité scaling
- Métriques setup : colonnes personnalisées incluant ROAS, CPA, CPM, CTR, CPC, ATC, CVR

## Signaux positifs vs négatifs

**Couper :** CPC > 4€ + CTR très faible + 0 ATC → aucune traction produit
**Laisser tourner :** CTR excellent + CPC bas + cost/ATC bas même si pas encore rentable → traction forte, optimiser le site

## Relations
- L'acquisition Meta est complémentaire au SEO ([[seo-roadmap]]) — Meta = trafic payant rapide, SEO = trafic organique long terme
- La créative est le cœur de la performance → [[creatif-ecom]]
- Le site et la conversion déterminent si le spend Meta est rentable → [[cro-ecom]]

## Sources
- [[rayecom-guide-ecom-complet]] — méthode CBO, ROAS BE/Target, testing, paliers de scaling
