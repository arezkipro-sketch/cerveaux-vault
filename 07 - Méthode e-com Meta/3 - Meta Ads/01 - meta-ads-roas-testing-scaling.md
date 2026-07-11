# Meta Ads — Configuration, ROAS, Testing, Scaling

> Meta Ads regroupe Facebook, Instagram, Messenger et WhatsApp. L'algorithme publicitaire le plus puissant du marché — résultats lisibles en 48 à 72 heures.

Quand l'algorithme détecte une forte traction sur un produit (bon taux de conversion, signaux de rentabilité clairs), il scale automatiquement. Il n'est pas rare de voir des boutiques passer de 0 à plusieurs milliers d'euros de CA en quelques jours, uniquement grâce à la puissance de l'algo.

---

## A. Configuration Meta Ads

Avant de lancer la moindre publicité : **configurer correctement ton écosystème Meta**. Un compte mal configuré = risque de bannissement permanent, campagnes instables, business fragilisé dès le départ.

**Métriques à setup pour l'ad account :** colonnes personnalisées incluant ROAS, CPA, CPM, CTR, CPC, coût par ATC (Add to Cart), taux de conversion.

---

## B. Setup Facebook

Beaucoup se perdent dans des setups ultra-complexes (comptes agence, proxies, structures à plusieurs couches). Pour débuter **et même pour scaler à des chiffres sérieux**, ce n'est pas nécessaire.

**Ce qui compte vraiment :**

**Un bon profil Facebook en bonne santé :** soit un compte personnel ancien avec de l'activité, soit un compte récent chauffé pendant 2 à 3 semaines en scrollant, likant, commentant comme un utilisateur normal. L'objectif : ne pas ressembler à un bot aux yeux de Meta.

**Pour le Business Manager :** ajouter **3 admins de backup** (proches, famille, peu importe). C'est ton filet de sécurité en cas de blocage. 5 minutes à mettre en place, peut sauver un scaling.

Il existe des solutions à tout en cas de problème (comptes agence, BM loués, structures alternatives). Mais y penser trop tôt, c'est se prendre la tête sur des problèmes que tu n'as pas encore. **80/20 : un compte sain, des admins de backup, et toute ton énergie sur ce qui génère du cash.**

---

## C. ROAS BE & ROAS Target

**Une seule métrique mesure la viabilité de ton business : le ROAS (Return on Ad Spend).** C'est lui qui dicte chaque décision budgétaire.

### Les deux métriques à maîtriser absolument

**ROAS Break-Even (BE)** → le seuil minimum. En dessous, chaque euro investi te coûte de l'argent. Si le ROAS BE n'est pas atteint, on ne scale pas.

**ROAS Target** → le retour sur investissement qui crée ta fenêtre de scaling. C'est le ROAS à partir duquel tu génères une marge nette suffisante pour réinvestir et accélérer sereinement. On vise généralement **20 à 25% de marge nette**.

### Comment calculer son ROAS BE en testing ?

En testing, tu n'as pas encore de data sur la répartition de tes ventes par bundle. La bonne approche : **estimation pondérée à vue d'œil**.

Tu demandes un quote à ton agent pour chaque bundle, tu estimes une répartition probable des ventes, et tu calcules un COGS moyen et un prix de vente moyen pondérés.

**Exemple concret (3 bundles) :**
```
Bundle 1x → COGS 10 € / Prix 45 € → estimation 30% des ventes
Bundle 2x → COGS 18 € / Prix 75 € → estimation 50% des ventes
Bundle 3x → COGS 25 € / Prix 99 € → estimation 20% des ventes

COGS moyen pondéré  = (10×30%) + (18×50%) + (25×20%) = 3 + 9 + 5 = 17 €
Prix moyen pondéré  = (45×30%) + (75×50%) + (99×20%) = 13,5 + 37,5 + 19,8 = 70,8 €
```
Ce n'est pas parfait — mais c'est suffisant pour lancer avec une base solide plutôt qu'au feeling.

### Une fois que tu as de la data

**Dès 50 ventes minimum** → recalcule tout proprement avec les chiffres réels. La répartition réelle peut être très différente de ton estimation.

**Recalculer toutes les 2 semaines** ou à chaque changement d'offre (remise, upsell, nouveau bundle).

⚠️ **Erreur la plus courante :** calculer son ROAS BE uniquement sur le bundle 1x. C'est une erreur coûteuse — la répartition réelle des ventes entre tes bundles a un impact direct sur ta marge moyenne.

---

## D. Le testing

Le testing est la phase la plus importante du processus. **Objectif : dépenser le moins possible pour obtenir le maximum de signaux.** On ne cherche pas à faire du profit à ce stade, on cherche à savoir si le produit a de la traction.

⚠️ TOUT CE QUI CONCERNE LE TESTING/SCALING EST VALABLE POUR LE MARCHÉ EU UNIQUEMENT.

### Type de campagne : CBO

Avec un petit budget, la CBO (Campaign Budget Optimization) est la seule option viable. Tu laisses Meta répartir librement le budget entre toutes tes créatives — il teste différentes combinaisons et remonte les premiers signaux sans que tu aies à gérer manuellement la répartition.

### Paramétrage de la campagne

| Paramètre | Valeur |
|---|---|
| Type | CBO |
| Budget | 100 €/jour |
| Adset | 1 seul, en broad, **aucun** ciblage âge/sexe/intérêts |
| Objectif | **ACHAT** (pas ajout au panier) |
| Lancement | À 00h le lendemain |
| Créatives | 10 à 15 différentes dans l'adset |

💡 Plus tu donnes de matière à Meta, plus il identifie rapidement les premiers signaux positifs. **1 excellente créative > 100 mauvaises créas.**

### Règle de décision budgétaire

| ROAS vs seuils | Action |
|---|---|
| < ROAS BE | Couper ou optimiser les créatives |
| Entre BE et Target | Maintenir et observer |
| > ROAS Target | Augmenter progressivement le budget |

**Signaux pour couper (métriques catastrophiques) :**
- Coût par clic > 4 € + CTR très très faible + 0 ATC → aucune traction sur le produit (du moins avec les ads actuelles)

**Signaux pour laisser tourner (traction forte même sans rentabilité) :**
- CTR excellents + CPC très peu cher + coût par ATC bas → laisser encore tourner quelques jours et tenter des optimisations sur la boutique

⚠️ **Ne te focalise jamais sur une seule métrique.** Un CPM élevé peut simplement signifier que Meta achète un trafic de meilleure qualité. Un CPC élevé n'a aucune importance si les gens qui cliquent achètent derrière.

**La seule question à se poser :** est-ce que chaque euro investi me rapporte suffisamment d'argent ?

### Paliers de scaling

```
100 € → 200 € → 300 € → 400 € → 500 € → 700 € → 1 000 € → 1 500 €
Au-delà : paliers de +500 € ou +1 000 € selon les performances
```

On augmente toutes les 24 à 48 heures, en analysant les résultats des 3 à 4 derniers jours. Si la campagne maintient son ROAS Target sur cette période, on peut poursuivre.

**Règle de gestion des CBO :** dès qu'une CBO fonctionne bien, on n'y touche plus. On crée une nouvelle CBO en parallèle qu'on alimente avec de nouvelles créatives. Le but : éviter de perturber ce qui fonctionne déjà.

---

## E. Les créas — L'ad copy

*(Pour le détail de la production créative : voir le dossier 4 - Créatives)*

L'ad copy est souvent négligée, à tort. Elle ne fait pas le travail de la créative, mais elle augmente la valeur perçue du produit et pousse le prospect à passer à l'action.

**Structure qui fonctionne bien (static et vidéo) :**
- **Accroche** → une question qui tape directement sur le pain point du prospect
- **Corps** → le bénéfice principal du produit, court et direct
- **CTA** → une offre claire avec une raison d'agir maintenant

**Pour le titre** → appuie sur le pain point. Le prospect doit se reconnaître immédiatement.

**Pour la description** → une promo avec du FOMO. Une réduction limitée dans le temps, un stock qui diminue, une offre qui expire. Ça fonctionne systématiquement.
