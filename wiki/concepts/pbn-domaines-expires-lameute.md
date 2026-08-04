---
type: concept
title: "PBN & domaines expirés — méthode enseignée par La Meute et analyse de risque"
slug: pbn-domaines-expires-lameute
tags: [seo, netlinking, pbn, domaines-expires, black-hat, risque]
sources: ["[[lameute-google-ads-influence-2026]]"]
source_count: 1
status: active
updated: 2026-08-04
---

# PBN & domaines expirés — méthode La Meute et analyse de risque

> 🔴 **Documenté pour mémoire, non recommandé.** Ce module enseigne le montage d'un **PBN** (réseau de sites qu'on possède, pointant vers sa boutique) et la **dissimulation de liens en CSS**. Le PBN est explicitement classé *link spam* par Google ; un lien invisible pour l'utilisateur mais suivi par le robot relève des liens cachés. Cohérent avec la position déjà tranchée dans ce vault → [[black-hat-seo]], [[pbn]]. **Le risque est asymétrique : il pèse sur la boutique qui génère le CA, pas sur les sites du réseau, jetables.**

## La thèse de l'intervenant (formation)
Plutôt que louer des liens chez des éditeurs (dépendance, liens supprimés, coût récurrent), acheter des **noms de domaine expirés** peu chers, les héberger en masse chez un seul hébergeur, y publier une page générée par IA, et y placer ses propres liens. Argument économique : quelques euros par lien "à vie" contre 10-15€ par lien acheté à l'unité. Argument de contrôle : modifier ancres et liens sans dépendre d'un tiers.

## Méthode de sélection décrite
Chasse sur un service de domaines expirés, filtres sur l'extension (.fr privilégié — peu cher et peu spammé, contrairement aux extensions à 2€ jugées spam), puis seuils sur métriques tierces (Trust Flow, Citation Flow, domaines référents). Vérification manuelle présentée comme indispensable : domaine encore indexé (`site:`), historique propre (ancres entrantes adulte/casino/streaming = domaine spammé, à jeter), exclusion des marques déposées et noms de personnes réelles (risque juridique, pas seulement SEO).

## Ce que la formation dit du risque — et ce qu'il en est réellement
| Point | Ce que dit la formation | Réalité |
|---|---|---|
| PBN | "niveau expert", "ça marche très bien" | Link spam explicite ; sanction possible sur le réseau **et** la boutique |
| Empreinte commune (même hébergeur/template/IP) | "peut poser problème, mais pas pénalisable" | **C'est précisément le vecteur de détection** — tout est ici mutualisé, empreinte maximale |
| Détection | réduite au risque qu'un concurrent la remarque | Occulte la détection algorithmique de Google elle-même |
| **Dissimulation du lien en CSS** | enseignée comme astuce pour brouiller le concurrent | **Le point le plus grave** : liens cachés = violation directe, circonstance aggravante en cas d'action manuelle |
| Contenu 100% IA | risque anticipé, réponse = "humaniser" le texte | Camouflage, pas une réponse au problème de fond |

**Trois absences majeures dans la formation** : jamais mention des actions manuelles, du fichier de désaveu, ni de la demande de réexamen. Elle déconseille même d'ajouter les sites du réseau à la Search Console — ce qui prive de toute visibilité sur une sanction éventuelle. Aucun plan de repli en cas de démasquage.

**Conflit d'intérêts relevé** : l'intervenant dirige une plateforme de vente de backlinks et enseigne à ne pas en acheter, reproduisant en fait le modèle économique de son propre métier.

**Coûts sous-estimés** dans les calculs présentés : renouvellement annuel des domaines, retour au tarif plein de l'hébergement après promotion, temps d'analyse manuelle (l'intervenant indique une personne employée à temps plein sur cette tâche dans sa propre structure).

## Ce qui est conforme et à retenir malgré tout
Le séquencement du netlinking et le choix des ancres, présentés dans le même module, sont de bonne facture et sans risque — repris dans [[netlinking-lameute]] et déjà dans le PLAYBOOK du cerveau ami.

## Relations
- Verdict déjà tranché de façon générale dans ce vault → [[pbn]], [[black-hat-seo]], [[toxic-backlinks]].
- Contexte d'usage (footprints qui trahissent un PBN concurrent) → [[footprints-seo-concurrence]].

## Sources
- [[lameute-google-ads-influence-2026]] — formation La Meute module 12 (vidéos 146-150), via cerveau Obsidian Google d'un ami.
