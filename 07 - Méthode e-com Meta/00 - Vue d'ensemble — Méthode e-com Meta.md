# Méthode e-com Meta — Vue d'ensemble

Méthode e-commerce documentée par la communauté RayEcom. Objectif : passer de 0 à plusieurs millions de CA via Meta Ads + boutique de niche brandée. Les sections ci-dessous suivent le parcours chronologique — du mindset au scaling.

---

## 1 — Fondations et stratégie

### Budget de départ
| Budget dispo     | Ce que ça permet                              |
| ---------------- | --------------------------------------------- |
| < 3 000 €        | ❌ Ne pas lancer Meta Ads — économiser d'abord |
| 3 000 – 5 000 €  | ✅ Premiers tests sérieux                      |
| 5 000 – 15 000 € | ✅ Tester vite + itérer + décisions sereines   |
| +15 000 €        | ✅ Plusieurs marchés simultanément             |

### Stratégie recommandée : boutique de niche brandée
- 1 produit en scaling → construire la niche autour progressivement
- Objectif stable : 3 000 € à 20 000 € CA/jour
- Duplication pays dès que le modèle est validé (FR → ES → IT)
- Délégation progressive : SAV + créatives + commandes → toi = stratégie uniquement

### Canal : Meta Ads (Facebook + Instagram)
- Résultats lisibles en **48-72h** (vs Google Ads : plusieurs semaines)
- TikTok / Google / Pinterest : uniquement après validation Meta, en phase de scaling

---

## 2 — Recherche produit

### 4 critères du winning product

**Critère 1 — Marge ≥ x4.5**
- COGS 10 € → prix de vente minimum 45 €
- La marge descend en scaling (audiences plus froides) → partir haut
- Améliorer : négocier COGS au volume / augmenter AOV avec bundles

**Critère 2 — Demande croissante depuis ≥ 3 mois**
- Plusieurs concurrents qui scalent = marché éduqué = validation gratuite
- Boutique à 5 000-10 000 €/jour de spend sur 3 mois = signal fort

**Critère 3 — Bon Time-to-Market**
- Produit en explosion depuis < 3 mois OU saisonnier (même période les années précédentes)
- Semaines 4 à 8 = 60-70% de la valeur disponible sur le produit

**Critère 4 — Contenu disponible**
- TikTok organique + pubs concurrentes = matière réutilisable → coût créative ≈ 0
- Sans contenu : 3 000-5 000 € de production avant même de tester

### Patterns TrendTrack
```
ENTRER      : courbe en forte hausse (0 → 1000 ads, <6 mois)
ANALYSER    : pic puis stabilisation — vérifier si nouvelles boutiques se placent
PASSER      : courbe plate depuis 1 an — trop mature pour débutant
ÉLIMINER    : courbe rouge / décroissante — sans exception
```

### Choix du marché
- Débutant → France, Espagne, Italie (codes marketing similaires, CPM accessibles)
- Budget limité → République Tchèque, Finlande, Pologne (CPM bas)
- Expérimenté (+15k€) → Big 5 (US/UK/CA/AU) ou Allemagne

---

## 3 — Meta Ads

### Calculer son ROAS BE (pondéré sur les bundles)
```
COGS moyen = Σ(COGS bundle × % ventes estimé)
Prix moyen = Σ(prix bundle × % ventes estimé)
ROAS BE    = Prix moyen / COGS moyen
```
Répartition par défaut : 30% bundle 1x / 50% bundle 2x / 20% bundle 3x.
Recalculer dès 50 ventes réelles, puis toutes les 2 semaines.

### Structure de testing (CBO)
```
Type      : CBO (Campaign Budget Optimization)
Budget    : 100 €/jour
Adset     : 1 seul · broad · aucun ciblage
Objectif  : ACHAT (pas ajout au panier)
Lancement : 00h le lendemain
Créatives : 10 à 15 dans l'adset
```

### Règles de décision
| ROAS vs seuils | Action |
|---|---|
| < ROAS BE | Couper ou optimiser créatives |
| Entre BE et Target | Maintenir + observer |
| > ROAS Target | Augmenter budget |

**Paliers de scaling :** 100 → 200 → 300 → 400 → 500 → 700 → 1 000 → 1 500 €, puis +500/+1 000.

⚠️ Ne jamais couper sur une métrique isolée. CPM élevé ≠ mauvais si les gens achètent.

---

## 4 — Créatives

### Funnel TOFU / MOFU / BOFU
```
TOFU → prospect froid  → capter attention + émotion (natives, contenus organiques)
MOFU → prospect tiède  → montrer que ton produit = la solution (vidéos + statics)
BOFU → prospect chaud  → lever les dernières objections (statics + preuves sociales)
```

### 3 types de créatives

**Static (image)**
- Arrête le scroll → visuel fort + texte court + offre FOMO
- Outils : ChatGPT / Higgsfield / Nano Banana

**Vidéo (rework de contenu existant)**
Partir de contenu concurrent validé, puis appliquer 4 modifications :
```
1. Voix off IA     → Kapwing (changer langue + ton)
2. Flip horizontal → CapCut
3. Filtre nuit 5%  → modifie métadonnées → CPM plus bas
4. Sous-titres     → retravaillés + animés → +temps de visionnage
```

**Native ad** (le plus puissant — ressemble à du contenu organique)
Structure en 6 étapes :
```
1. Identification  → "c'est exactement ma situation"
2. Problème        → ce qu'il a déjà essayé (avec prix + résultats décevants)
3. Révélation      → pourquoi ça n'a pas marché (mauvais mécanisme)
4. Produit         → conclusion logique de la révélation (jamais avant)
5. Résultats       → progressifs + spécifiques (détails = crédibilité)
6. CTA             → naturel, sans pression
```
Test de validation : "quelqu'un peut-il penser pendant 10 secondes que c'est un vrai post ?"

---

## 5 — Site Shopify

### Configuration critique
- [ ] **Désactiver la taxe automatique** : Paramètres → Taxes → Union Européenne → Manual Tax
- [ ] **Nom de domaine .com** via Namecheap ou Ionos (jamais via Shopify, jamais OVH/LWS)
- [ ] **Thème** : Story (20€/mois) suffisant au lancement. Claude peut reproduire des sections depuis screenshot.
- [ ] **Processeurs** : Shopify Payments + PayPal. Stripe = backup uniquement (gèle fonds 6 mois).
- [ ] **Business Manager** : 3 admins de backup

### Plans Shopify
- Basic → lancement / Growth → dès que tu as des VAs / Advanced → comparer frais au volume

### Email marketing — 2 flows obligatoires (Klaviyo)
Mettre en place dès 5 000 €/jour :
```
Flow panier abandonné :
  Email 1 → rappel simple (30 min après)
  Email 2 → -10% + urgence stock (2h après)
  Email 3 → -20% + ton fondateur (24h après)

Flow post-achat :
  → rassurer à chaque étape de livraison → moins de SAV + fidélisation
```
Email = jusqu'à 30% du CA avec CPA bien inférieur à Meta Ads.

---

## 6 — CRO et Optimisation

### Augmenter l'AOV (Average Order Value)

**Bundles (offres en volume)**
```
1+1 offert    → le plus populaire
2+2           → réduction plus agressive
2+1 offert    → "offert" = fort psychologiquement
3+2 offert    → panier très élevé
```

**Avec cadeaux**
- Cadeau physique + e-book offert + combo = maximum de valeur perçue

### Optimiser le panier
```
Timer 5-10 min         → urgence → réduire abandons
Barre de progression   → "X€ pour livraison gratuite" → AOV naturel
Bumps                  → produit complémentaire dans le panier
Badges de réassurance  → haut ET bas du panier (garantie, livraison, paiement)
```

### Upsells post-achat
- **Même produit à -50%** (1 clic, carte déjà sortie) = le plus efficace
- **Produit complémentaire** = logique et dans l'intérêt du client

**Trouver des idées upsell :** Amazon → rechercher son produit → "fréquemment achetés ensemble"

### A/B tests
```
Outil        : IntelliGems (pas les apps classiques Shopify)
Minimum      : 500 ventes par variante
Métrique clé : marge nette par visiteur (pas CVR isolé)
```

### Microsoft Clarity (gratuit)
- Heatmaps + replays → voir où les clients droppent
- Gros taux de drop = zone prioritaire à A/B tester

---

## 7 — Agents et Sourcing

### ❌ AliExpress : à éviter
- Prix gonflés (intermédiaires), délais imprévisibles, qualité non contrôlable, aucun branding possible

### Quel agent selon volume
| Volume | Type d'agent |
|---|---|
| 0-10 commandes/jour | Agent spécialisé débutant (Discord RayEcom) |
| +10 commandes/jour | Agent privé chinois : négociation COGS + stocks tampons + packaging brandé + QC |

À +10 commandes/jour, l'agent devient un avantage compétitif réel.

---

## Checklist de démarrage

### Phase 0 — Avant de lancer
- [ ] Budget disponible ≥ 3 000 €
- [ ] Compte Facebook "sain" + Business Manager configuré (3 admins backup)
- [ ] Nom de domaine .com (Namecheap) + thème Shopify installé
- [ ] Taxe automatique Shopify désactivée
- [ ] Processeurs configurés : Shopify Payments + PayPal

### Phase 1 — Testing produit
- [ ] Produit validé sur les 4 critères (marge x4.5 / demande 3 mois / TTM / contenu)
- [ ] Marché sélectionné selon profil
- [ ] Agent sourcing contacté (Discord RayEcom)
- [ ] ROAS BE calculé (pondéré sur les bundles)
- [ ] CBO créée : 100€/jour / 1 adset broad / 10-15 créatives / objectif ACHAT
- [ ] Microsoft Clarity installé

### Phase 2 — Scaling
- [ ] ≥ 50 ventes → recalculer ROAS BE réel
- [ ] > ROAS Target → augmenter budget par paliers (24-48h entre chaque)
- [ ] Klaviyo configuré : flow panier abandonné + flow post-achat
- [ ] Bundles + upsells post-achat en place
- [ ] A/B test LP dès 500 ventes/variante (IntelliGems)
- [ ] Duplicate boutique sur 2ème marché dès le modèle stabilisé

---

## Sources
Guide RayEcom FREE (Notion) — Rayane, fondateur de la RayEcom, 2026-06-28.
