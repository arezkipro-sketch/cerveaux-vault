# Méthode e-com Google Ads — Vue d'ensemble

Méthode issue de la formation **La Meute | E-Commerce** (Skool), module 13 (fondamentaux/prérequis/setup/campagnes/pilotage) + live avancé Yassfox (05/02/26, ~10 ans d'e-commerce, 80% de son CA via Google Ads). Complémentaire à [[07 - Méthode e-com Meta/00 - Vue d'ensemble — Méthode e-com Meta|Méthode e-com Meta]] : Meta crée la demande (interruption), **Google capte une demande déjà exprimée** (intention).

Contenu source détaillé (analyse critique, chiffres non sourcés flagués) : → [[google-ads-fondamentaux]], [[google-ads-prerequis-et-equation]], [[google-ads-setup-et-shopping]], [[google-ads-campagnes]], [[google-ads-pilotage-et-scaling]], [[merchant-center-conformite]], [[retargeting]].

---

## 1 — Fondations et équation de validation

### Pourquoi Google plutôt que / en complément de Meta
| | Meta Ads | Google Ads |
|---|---|---|
| Modèle | Facturation dès l'impression | **CPC** — paiement au clic seulement |
| Intention | Froide — on crée la demande | **Chaude** — on capte une demande existante |
| Durée de vie créa | S'essouffle, production continue | Plus stable (mais pas "set and forget") |
| Contraintes créa halal | Vidéo, musique, présence féminine | **Juste une image produit + un titre** → contourne les contraintes GATE HALAL sur le contenu vidéo |

⚠️ Chiffres marché cités par la formation (80% part de marché PPC, ROAS moyen 4-8, CPC France 0,50-2,50€) sont `asserted`, non sourcés — ne pas les réutiliser comme référence.

### L'équation go/no-go (à calculer AVANT de dépenser un euro)
```
CPC moyen × visiteurs nécessaires pour 1 vente   <   marge unitaire   →  lancer
                                                  >   marge unitaire   →  ne pas lancer
```
- **CPC moyen** = (enchère haut de page basse + haute) / 2 — jamais le CPC bas (on se ment à soi-même). Source : Planificateur de mots-clés.
- **Visiteurs nécessaires** = inverse du taux de conversion : 0,5% → ×200 (hypothèse pessimiste par défaut) · 1% → ×100 · 1,5% → ×75 · 2% → ×50.
- **Marge unitaire** = prix de vente − (achat + **shipping et tous les coûts**, pas juste le COGS).
- **Grille de robustesse** : l'équation ne passe qu'au CPC bas → produit non validé. Passe au CPC moyen → bon produit, lançable. Passe même au CPC haut → produit excellent.
- **Piège du TC global** : un blog SEO écrase le taux de conversion global avec du trafic informationnel. Recalculer le TC **sur les seules requêtes transactionnelles** (Search Console) — un site à 0,2-0,5% global peut être à 1-1,2% en transactionnel, ce qui inverse le verdict.
- Si l'équation échoue : soit le CPC est trop élevé (changer de niche), soit le TC du site est trop bas (travailler le site avant de dépenser) — **jamais** un problème de réglages.

### Checklist des 5 prérequis avant de dépenser
1. **Volume** : cible **15 000-40 000 recherches/mois** sur le mot-clé principal. < quelques centaines = pas de demande. > 100-300k = trop concurrentiel.
2. **Intention transactionnelle** ("chaussettes blanches Nike", pas "comment choisir sa pointure").
3. **Pertinence** : 1 mot-clé = 1 annonce = 1 produit.
4. **Concurrence présente = bon signal** (marché validé). Si le test échoue alors que des concurrents vendent → le problème vient de vous, auditer leurs fiches/annonces/offres.
5. **ROAS break-even calculé**.

⚠️ **Base zéro Yassfox** : Google Ads suppose une **grosse marge** (les niches SEO à 50% de marge cassent sous Ads) et **des centaines de produits déjà sourcés et rentables** (jamais sourcer au hasard — viser 100-200 produits ciblés, pas 3000 produits SEO). Marge faible + CPC élevé = changer de niche, pas insister.

---

## 2 — Setup compte, tracking et campagne Shopping

### Configuration du compte (avant tout lancement)
- App officielle Google/YouTube sur Shopify + **compte Google professionnel**.
- Prérequis Merchant Center : moyen de paiement valide, **mot de passe boutique supprimé**, CGV/CGU présentes, coordonnées confirmées.
- **Refuser la Performance Max** imposée par les deux assistants (Shopify puis Ads) → créer la campagne forcée, la **mettre en pause immédiatement**.
- **Deux moyens de paiement obligatoires** (CB + prélèvement) : un plafond CB atteint = campagnes coupées alors que le compte est approvisionné.
- Vérification annonceur (documents + identité) avant de lancer.

### Tracking — l'étape la plus critique
- Pixel Shopify (Événements clients) → conteneur **Google Tag Manager**.
- Action de conversion **Achat** en config manuelle ; sur compte neuf, **supprimer toute action "Achat" préexistante** (sinon double comptage, ROAS surévalué).
- **Valeur de conversion dynamique** obligatoire ("valeurs différentes pour chaque conversion") — jamais "même valeur" (ROAS inutilisable).
- Remplacer identifiant + libellé sur **les deux balises** (conversion ET remarketing), puis **publier le conteneur**.

### Campagne Shopping (la campagne principale)
| Paramètre | Valeur |
|---|---|
| Part du budget compte | **≥ 80%** |
| Sous-type | **Shopping standard** — jamais Performance Max |
| Objectif | Ventes, 1 seule action de conversion (Achat) |
| Budget quotidien | **CPC moyen × 50** (viser ~50 clics/j, usuellement 20-40 €/j) |
| Enchère | **CPC manuel réglé sur le CPC MOYEN** — jamais le bas (cause n°1 d'une campagne qui ne diffuse pas). C'est un plafond, pas un coût payé. |
| Ciblage | Géographique + option **"Présence"** (pas "présence ou intérêt") |
| Produits | Tout le catalogue, ou sélection par ID (best-sellers) si budget serré |
| Protocole | **Laisser tourner 5-7 jours sans rien toucher** |

### Sourcer les candidats niche
Repérer les boutiques qui font déjà du Google Ads (apps de flux Shopping) → vérifier leur activité dans le **Google Ads Transparency Center**. Bon signal = Shopping + Search + Display. Mauvais signal = uniquement campagnes sur leur propre marque (défensif, pas d'acquisition). Le Transparency Center révèle aussi **sur quels produits** ils diffusent (best-sellers présumés). ⚠️ Dans le Planificateur de mots-clés, **ne jamais saisir d'accents** (traités comme un autre mot-clé).

---

## 3 — Campagnes complémentaires (20% du budget restant)

Répartition de référence : **Shopping 80% / Search + reste 20%**.

### Search Acquisition (offensive)
- Mots-clés via Planificateur → "Commencer avec un site web" → coller **l'URL de la collection** (pas le domaine). Fort volume + intention transactionnelle uniquement.
- **URL finale = la page de collection**, jamais l'accueil.
- Correspondances au lancement : **exact `[ ]` ET expression exacte `" "`**, jamais requête large (réservée au scaling de fin de parcours).
- Stratégie "Maximiser les clics" au lancement · décocher partenaires + Display · ciblage "Présence".

### Branding (défensive)
Seulement si vraie marque avec volume de recherche (inutile en EMD). Taux d'impression cible 90%, budget ≤ 20€/j, mots-clés = marque + produit + **toutes les fautes de frappe**.

### Performance Max feed-only
- **Seulement au plafond de verre** du Shopping (taux d'impression réseau de recherche 80-95%).
- **Aucun asset** (titre/image/vidéo) → force la diffusion 100% Shopping, sinon le budget part en Display/YouTube.
- **Exclusion de marque obligatoire** (sinon capte les clients déjà acquis, gonfle artificiellement le ROAS).
- Signaux = mots-clés rentables issus des termes de recherche Shopping + données first-party.

---

## 4 — Pilotage, kill/scale et scaling

### La métrique pivot
**ROAS break-even** = seuil où on ne perd ni ne gagne. Sans lui, aucune décision n'est possible. Piloter sur la **rentabilité**, pas sur le ROAS dans l'absolu (un ROAS de 2 n'est pas mauvais en soi si le break-even est à 1,5).

### Métriques et repères
| Métrique | Repère |
|---|---|
| CTR | Search ~10% · Shopping ~1% |
| Impressions | 0 après 5j = CPC trop bas ou problème de pertinence |
| Taux d'impression réseau recherche | 20% = 80% du marché raté · 80-95% = plafond de verre |

### Règle d'or — ne jamais trancher sur trop peu de data
- Durée minimum d'un test : **7-10 jours**.
- Produit : pas de conclusion sous **30-60€** de dépense.
- Mot-clé : pas de coupe sous **50-100€** cumulés.
- **Ne jamais s'arrêter au ROAS global** — descendre au niveau produit et mot-clé (une campagne à 1,07 pour un break-even 1,5 peut cacher des produits à 3,7 et 6,6).

### Gestion fine des CPC (Yassfox, ±20%)
- Produit qui **dépense sans être rentable** → CPC **−20%**.
- Produit **rentable qui ne dépense pas** → CPC **+20%** (signal d'intérêt sous-exploité).
- Produits "zombies" (ne dépensent jamais) → +20% ou isolement dans une campagne de test dédiée.
- **Piège des variantes de mots-clés** : dépense réelle éclatée sur des dizaines de variantes à 0,10-0,50€/mot-clé (fuite invisible) → exporter les termes de recherche, dédupliquer/regrouper via ChatGPT (trier par dépense décroissante + grouper les variantes similaires), puis couper un mot-clé racine dès qu'il dépasse **0,7× le prix de vente moyen** cumulé.

### Isolement et scaling
- **Règle des 3** : ≥3 ventes et ROAS ≥ 1,5× break-even → isoler le produit dans sa propre campagne (par groupes de 3). Ultra-winner (ROAS 4-5+) → directement en Performance Max dédiée.
- **ROAS cible (smart bidding)** : viser **180-220%**, au plus proche de la moyenne réelle des produits isolés. Trop haut → la diffusion s'arrête (baisser la cible). Budget non consommé = objectif atteint plus tôt, pas un problème.
- **Budget** : +15-20% tous les 3-4 jours (socle) ou +20% tous les 10 jours (scaling avancé) — jamais de doublement brutal (casse l'apprentissage).
- **Ratio testing/scaling : ~20/80.** Un split 50/50 rend la rentabilité mathématiquement impossible (ex. concret : 20€/j de test + 20€/j de scaling = jamais rentable ; il faut ~100€/j en scaling pour 20€/j de test).
- **Segmenter en 3 campagnes** : best-sellers · autour du break-even (2e chance) · nouveaux tests.
- Horizon réaliste : 3-6 mois + budget de perte à absorber. Lancer les Ads **1-2 mois après le SEO** (site trop neuf = risque de refus Merchant Center).

### Les 8 erreurs fatales
1. Trop de modifications à la fois. 2. Couper en phase d'apprentissage. 3. Balise de conversion mal installée. 4. Annonces trop générales (détruit le Quality Score). 5. Ignorer le ROAS break-even. 6. Ne pas faire l'équation avant de lancer. 7. Couper avant 7-10 jours. 8. Ne pas analyser le site (CTR/CPC bons + zéro conversion = problème site, pas Ads → enregistreur de session).

---

## 5 — Merchant Center : conformité et anti-suspension

**Enjeu maximal** : sans Merchant Center, aucun accès à Google Shopping.

### Règle maîtresse
**Cohérence stricte et littérale entre le site et le Merchant Center** — ce sont des systèmes automatisés qui confrontent, ne raisonnent pas.

### Checklist
1. Feed produit propre (prix, descriptions, attributs).
2. Coordonnées réelles, **email sur domaine propre** (pas gratuit grand public).
3. Adresse identique **au caractère près** des deux côtés (code postal inclus).
4. Téléphone même format (indicatif inclus).
5. Mêmes coordonnées partout (CGV, mentions légales, contact, confidentialité).
6. Pages obligatoires : contact, mentions légales, confidentialité, retours/remboursements, livraison.
7. Politique de retour explicite (qui paie, conditions, délais).
8. **Délais de livraison identiques** — piège : le Merchant Center **additionne traitement + livraison**, c'est cette fourchette totale qu'il faut recopier sur le site. Attention "jours" vs "jours ouvrés".
9. Frais de port identiques à l'euro près.

### Motif de suspension n°1 : "misrepresentation"
À proscrire : milliers d'avis sur un site d'une semaine · prix barré jamais pratiqué · promesses spectaculaires garanties · garantie/"satisfait ou remboursé" affichée au lancement (préférer "remboursement sous 14/30 jours"). **Convergence directe avec le GATE HALAL** : ce que Google sanctionne ici est exactement ce que "zéro tromperie" interdit déjà.

### En cas de suspension
Ne pas faire appel immédiatement — corriger d'abord avec la checklist, **puis** appeler. **Limite de 3 appels** avant clôture définitive.

---

## 6 — Retargeting (Meta/TikTok, sur trafic Google)

Recibler les **97-99% de visiteurs Google Ads/SEO qui ne convertissent pas** au premier passage — un achat demande 7-15 points de contact, le trafic Google est qualifié mais froid.

- **Canaux** : Meta + TikTok sur l'audience des visiteurs du site. Pixels posés **dès le départ**, même sans budget paid.
- **6 types de créas** : preuve sociale · démonstration produit · traitement d'objections · rappel/relance douce · storytelling (facultatif) · offre en urgence réelle.
- **Adapter par plateforme** : Meta accepte les créas Google telles quelles ; **TikTok exige du natif/vidéo/tendance** (réutiliser du contenu Meta y donne un CTR faible).
- Repères cités : CPM retargeting ~11€/1000 (Meta), ~2,55€ (TikTok). Ne fonctionne **que si l'offre et le prix sont déjà bons**.

---

## Checklist de démarrage

### Phase 0 — Avant Google Ads
- [ ] Niche validée SEO **avec grosse marge** (pas les niches à 50% de marge type SEO pur)
- [ ] Équation go/no-go calculée (CPC moyen × visiteurs nécessaires < marge unitaire), au pessimiste (0,5%)
- [ ] 100-200 produits sourcés et ciblés (pas de sourcing aléatoire massif)
- [ ] Site lancé depuis 1-2 mois minimum (SEO d'abord, Ads après)
- [ ] Merchant Center conforme (checklist cohérence littérale)
- [ ] Tracking GTM installé : conversion Achat manuelle, valeur dynamique, doublons supprimés

### Phase 1 — Lancement
- [ ] Campagne Shopping standard, CPC manuel = CPC moyen, budget = CPC moyen × 50
- [ ] Deux moyens de paiement actifs
- [ ] PMax forcée mise en pause
- [ ] 5-7 jours sans rien toucher

### Phase 2 — Optimisation et scaling
- [ ] Gestion CPC ±20% par produit (dépense/rentabilité)
- [ ] Dédup des variantes de mots-clés (export + ChatGPT)
- [ ] Isolement règle des 3 (≥3 ventes, ROAS ≥1,5× BE)
- [ ] ROAS cible 180-220% sur campagnes isolées
- [ ] Ratio testing/scaling 20/80
- [ ] Retargeting Meta/TikTok activé sur trafic non converti

---

## Sources
Formation La Meute | E-Commerce (Skool), module 13 + live Yassfox 05/02/26 — transcrite et synthétisée dans le cerveau Obsidian Google d'un ami (2026-07-22/23), fusionnée dans ce vault le 2026-08-04. Détail critique complet : → [[google-ads-fondamentaux]], [[google-ads-prerequis-et-equation]], [[google-ads-setup-et-shopping]], [[google-ads-campagnes]], [[google-ads-pilotage-et-scaling]], [[merchant-center-conformite]], [[retargeting]].
