---
type: concept
title: "Merchant Center — conformité et prévention de suspension"
slug: merchant-center-conformite
tags: [merchant-center, google-shopping, suspension, conformite, google-ads]
sources: ["[[lameute-google-ads-influence-2026]]"]
source_count: 1
status: active
updated: 2026-08-04
---

# Merchant Center — conformité et prévention de suspension

**Définition :** Le Merchant Center relie la boutique à Google Ads — sans lui, aucun accès à Google Shopping. Enjeu maximal pour tout e-commerçant visant [[google-ads-ecom]] : Google est de plus en plus strict, les motifs de refus/suspension sont souvent flous et le déblocage est difficile.

## La règle maîtresse
**Cohérence stricte et littérale entre le site et le Merchant Center.** Ce sont des systèmes automatisés qui comparent les deux côtés sans raisonner — un simple écart de format suffit à déclencher un rejet.

## Checklist
1. Feed produit propre : pas de prix erronés, descriptions et attributs remplis.
2. Informations d'entreprise réelles : adresse physique, téléphone, **email sur domaine propre** (jamais une adresse gratuite grand public).
3. Adresse identique **au caractère près** des deux côtés (rue, ville, code postal inclus).
4. Téléphone au même format (indicatif présent des deux côtés).
5. Mêmes coordonnées partout : CGV, mentions légales, page contact, politique de confidentialité.
6. Pages obligatoires : formulaire de contact, mentions légales rédigées (pas copiées), politique de confidentialité, page retours/remboursements, page livraison.
7. Politique de retour explicite : qui paie le retour, conditions, délais, procédure, mode de remboursement.
8. **Délais de livraison identiques** — piège principal : le Merchant Center **additionne le délai de traitement et le délai de livraison** et affiche une fourchette totale ; c'est cette fourchette totale qu'il faut reprendre sur la boutique. Attention à l'unité : "5 à 10 jours" ≠ "5 à 10 jours ouvrés".
9. Frais de port identiques des deux côtés, à l'euro près.

## Le motif de suspension n°1 : "misrepresentation"
Catégorie fourre-tout, à proscrire absolument :
- Des milliers d'avis sur un site qui a une semaine (incohérence flagrante).
- Fausses promotions : un prix barré jamais réellement pratiqué — Google sait si le produit n'a jamais été vendu à ce prix.
- Promesses abusives (résultats spectaculaires garantis).
- Au lancement : éviter la garantie affichée et le "satisfait ou remboursé" (préférer "remboursement sous 14/30 jours"), ainsi que les logos de paiement sécurisé trop en avant.

👉 **Convergence directe avec le principe zéro-tromperie** déjà documenté dans ce vault : ce que Google sanctionne ici (faux avis, fausses promos, promesses non tenues) est exactement ce qu'interdit déjà [[dropshipping-halal]]. S'y conformer protège mécaniquement le compte.

## En cas de suspension
Ne **pas** faire appel immédiatement — attendre quelques jours, auditer le site et le compte avec la checklist ci-dessus, corriger, **puis** faire appel. **Limite de 3 appels** avant clôture définitive du compte : un appel gaspillé est irrécupérable. Après déblocage, attendre d'avoir dépensé plusieurs dizaines à ~150€ avant de réintroduire avis, promotions et garanties.

## Configuration initiale
Revendiquer le domaine (email professionnel ou balise de vérification avant la fermeture du `<head>`), associer la boutique via l'app officielle Google/YouTube (qui contrôle au passage les prérequis), renseigner les règles de livraison et de retour, puis répliquer ces valeurs **mot pour mot** sur la boutique. Un statut "en cours d'examen" au début est normal. Intérêt au-delà du payant : le flux alimente aussi les fiches produits gratuites affichées sous les annonces sponsorisées.

## Relations
- Prérequis technique direct de [[google-ads-ecom]] — sans Merchant Center conforme, la campagne Shopping ne peut pas tourner.
- La logique "cohérence littérale" rejoint la rigueur déjà exigée côté halal (description fidèle au produit livré) → [[bay-salam]], [[dropshipping-halal]].

## Sources
- [[lameute-google-ads-influence-2026]] — formation La Meute module 10 (vidéo 116), via cerveau Obsidian Google d'un ami.
