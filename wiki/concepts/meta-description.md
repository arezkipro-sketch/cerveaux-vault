---
type: concept
title: "Meta Description"
slug: meta-description
tags: [seo, on-page-seo, ctr, serp, e-commerce]
sources: []
source_count: 0
status: active
updated: 2026-07-22
note: "Stub enrichi 2026-07-22 avec retours d'usage réel (PushRank/Shopify, harnais-chien-expert.fr) — toujours aucune source `raw/` dédiée."
---

# Meta Description

**Definition :** Balise HTML résumant le contenu d'une page, affichée sous le titre dans les résultats Google — n'influence pas directement le classement mais impacte le [[click-through-rate]]. Distincte de la [[canonical-tag]] et des [[donnees-structurees]] (autres signaux à Google, rôles différents).

## Longueur cible

**150-160 caractères.** En dessous de 150, Google a de la marge pour tronquer ou compléter automatiquement le snippet avec un autre extrait de la page (perte de contrôle sur le message) ; au-dessus de 160, le texte est tronqué avec "...". Une meta description à 92-149 caractères n'est pas "fausse" mais laisse de la valeur sur la table — Google College partiellement le vide.

## Le piège CTR vs mot-clé

Une reformulation pensée uniquement pour l'accroche (bénéfice, urgence, question) peut faire disparaître le mot-clé cible de la meta description. **Les deux objectifs doivent cohabiter, pas se remplacer** : le mot-clé aide la pertinence perçue (et Google le met en gras dans le snippet, ce qui *aussi* améliore le CTR) ; l'accroche améliore la conversion au clic. Une meta optimisée uniquement pour l'un des deux est une meta à moitié optimisée.

*Cas vécu (2026-07-22, harnais-chien-expert.fr) : réécriture d'une meta description pour la rendre plus accrocheuse ("Mesurez en 2 minutes et trouvez la taille parfaite...") a fait disparaître le mot "harnais" du texte — erreur repérée après coup et corrigée. Toujours relire une meta réécrite en se demandant "est-ce que le mot-clé cible y est encore ?" avant de la considérer terminée.*

## Implémentation Shopify

Shopify n'a pas de champ "meta description" natif direct sur tous les types de ressource dans l'admin classique — le mécanisme réel est un metafield `global.description_tag` (namespace `global`, clé `description_tag`, type `single_line_text_field`) posé sur la ressource (produit, collection, page, article, blog). Shopify peuple automatiquement `page_description` dans le thème à partir de ce metafield. Sans ce metafield, la balise `<meta name="description">` peut soit être absente, soit retomber sur un extrait automatique du contenu de la page (comportement observé sur une page FAQ sans metafield : le contenu brut de la page fuitait dans la balise meta).

Pour un lot de fiches produits (ex: 73 produits) déjà bien rédigées mais toutes légèrement sous la fourchette cible, la correction efficace n'est pas de tout réécrire : calculer l'écart exact par produit et compléter par une phrase de clôture de longueur variable (banque de formulations de longueurs différentes, choisies pour atterrir précisément dans 150-160) — préserve le contenu unique déjà existant, évite la sur-optimisation en une passe automatisée.

## Relations
- [[click-through-rate]] — impact indirect principal de la meta description.
- [[canonical-tag]] — autre signal on-page, rôle distinct (duplication de contenu, pas de résumé).
- [[keyword-cannibalization]] — une meta description qui ne contient plus le mot-clé cible affaiblit le signal de pertinence de la page pour ce mot-clé, un facteur à surveiller en parallèle d'une vérification de cannibalisation.
- Fait partie du triptyque on-page avec [[h1-heading-tag]] et le title tag — les trois doivent être cohérents entre eux, pas traités isolément.

## Sources
- Usage réel session 2026-07-21/22 sur harnais-chien-expert.fr (pas de source `raw/` — expérience directe via l'intégration MCP PushRank/Shopify Admin API).
