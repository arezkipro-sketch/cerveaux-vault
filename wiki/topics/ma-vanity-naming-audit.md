---
type: topic
title: "Ma-Vanity — Audit & Correction Nommage Fiches Produits"
slug: ma-vanity-naming-audit
tags: [seo, e-commerce, fiche-produit, shopify, ma-vanity, naming, on-page-seo]
sources: ["[[fiche-produit-seo]]", "[[benjamin-thiers-fiches-produits]]", "[[keyword-cannibalization]]", "[[cocon-semantique]]", "[[boutique-vanity-persona]]", "[[url-structure]]", "[[301-redirect]]"]
status: active
updated: 2026-06-21
---

# Ma-Vanity — Audit & Correction Nommage Fiches Produits

**One-liner:** Correction SEO complète des fiches produits de la boutique Shopify ma-vanity.com (puwww1-vg) via Admin GraphQL API : `seo.title`, `meta description`, couleurs, anglais résiduel, et fusion d'un doublon-concept. Réalisé 2026-06-21.

## Contexte
- Store : `puwww1-vg.myshopify.com` (= ma-vanity.com). 166 produits, 24 collections au départ.
- Persona cible : femme 30-50, déclencheur **voyage**, motivation **organisation/gain de temps** → [[boutique-vanity-persona]].
- Cocon préservé : collection = terme tête (générique), produit = couleur longue traîne → [[cocon-semantique]], [[keyword-cannibalization]].

## Baseline (avant) → Final (après)
| Métrique | Avant (2026-06-21) | Après |
|---|---|---|
| Produits | 166 | **164** (fusion −2) |
| Méta dupliquées | 147/166 (8 groupes, 103 génériques) | **0** |
| Méta vides / >160 car | 0 / 0 | **0 / 0** |
| seo.title tronqués à 60 mid-word | 75 | **0** |
| seo.title sans `\| Ma-Vanity` | 147 | **0** |
| seo.title dupliqués | — | **0** |
| Couleur titre ≠ variante | 3 | **0** |
| Anglais dans option values | 10 valeurs | **0** |
| Collection titre anglais | 1 | **0** |

## Décisions de nommage (règles appliquées)
- **Pattern seo.title** (≤60, finit par `| Ma-Vanity`) : `{Catégorie tête} {Attribut} {Couleur} | Ma-Vanity`. Repli : drop attribut, puis `{Catégorie} {Couleur}`. Conforme [[benjamin-thiers-fiches-produits]] (55-65) et [[fiche-produit-seo]].
- **Mener par le vrai terme tête** : garde "Vanity" si le produit EST un vanity (rigide / valise / souple / à code / cuir / homme / personnalisé) ; sinon mène par Trousse / Pochette / Boîte / Coffret / Organiseur. La couleur différencie chaque fille → 0 cannibalisation vs la collection mère.
- **Méta unique ≤160** : template `{Type}, coloris {couleur} : {bénéfice voyage/organisation persona}. {matière/atout}. Livraison rapide Ma-Vanity.` — bénéfice adapté par famille (38 familles).
- **Couleurs** : valeur variante = source de vérité ; casse Title-Case en SERP ("Or Rose", "Vert Foncé") ; nuances longue traîne gardées ("Rose Poudré", "Bleu Lagon").

## Corrections couleur (titre ↔ variante)
- `vanity-a-code-16-or-rose` : titre "Rose" (tronqué/faux) → **"Or Rose"** (variante réelle).
- `vanity-trousse-de-toilette-femme-rose-poudre` : variante "Rose" → **"Rose poudré"** (différencie de la fiche "Femme Rose").
- `vanity-souple-blanc-casse` : variante "Blanc lait" → **"Blanc cassé"** (cohérent handle/titre).
- `vanity-cuir-croco-assorti` : variante "Coloris photo" → **"Assorti"**.

## Anglais résiduel → FR (option values)
`14Inches 350mm→35 cm`, `16Inches 400mm→40 cm`, `22x15x16CM→22 × 15 × 16 cm` (+ variantes), `combination lock→Avec cadenas`, `No combination lock→Sans cadenas`, `Handbag→Sac à main`, `Tote→Cabas`, `Small→Petit`. Collection `Vanity with mirror & lights` → titre **"Vanity miroir lumineux LED"** (handle inchangé).

## Doublons-concept (Phase 4)
- **Miroir LED (5) vs Miroir Lumineux (2)** → **FUSION** validée par l'humain : les 2 Lumineux (Noir, Rose) supprimés, **301** vers le LED même couleur. Cf [[301-redirect]] :
  - `/products/vanity-miroir-lumineux-noir` → `/products/vanity-miroir-led-noir`
  - `/products/vanity-miroir-lumineux-rose` → `/products/vanity-miroir-led-rose`
- **4 autres groupes** (Toilette Femme vs Toilette ; Voyage vs Maquillage Voyage ; Personnalisé Cuir/Zippé/Femme ; Transparent PVC vs Carré) → **différenciés par attribut réel** (forme/matière/intention), aucune fusion. Décision humaine : OK différencier.

## Handles (Phase 5)
23 handles pollués (`-1`, `-16-`) + handle anglais `vanity-with-mirror-lights` → **laissés tels quels** (décision humaine) : renommer = risque SEO sans gain. Documenté, non touché (pas de 301 inutile). Voir [[url-structure]].

## Garde-fous respectés
- `raw/` du wiki non touché. Sans-risque (seo) librement ; medium (titre/option) avec diff + re-query ; irréversible (delete + 301) seulement après OK humain explicite horodaté.
- Lots de 10, vérif `userErrors` + re-query après chaque mutation.
- Changelog complet (`_mavanity/changelog.json`, 338 entrées) pour rollback.

## Open questions
- LED vs Lumineux supposés produits identiques (validé par l'humain pour fusion) ; à confirmer si une différence physique existait.
- Variantes "Taille" de la trousse de toilette (S/M/L) vs versions "Femme" couleur unique : intentions proches, gardées séparées — à surveiller en GSC (cannibalisation Noir/Rose résiduelle).
- Corps de fiche (descriptionHtml) non réécrit dans cette passe : structure existante préservée, bénéfice persona porté par la méta.
