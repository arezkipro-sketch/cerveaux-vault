---
type: concept
title: "Boutique Shopify — paramétrage, branding & DNS (La Meute)"
slug: boutique-shopify-branding-lameute
tags: [shopify, branding, fiche-produit, dns, conformite, logo, la-meute]
sources: ["[[lameute-google-ads-influence-2026]]"]
source_count: 1
status: active
updated: 2026-08-04
---

# Boutique Shopify — paramétrage, branding & DNS

**Définition :** Configuration technique et identité de marque d'une boutique Shopify neuve.

## Paramétrage Shopify — points qui comptent
- **Devise** : symbole € à droite sur les quatre champs (le défaut Shopify est anglophone).
- **Checkout** : contact par email uniquement, pas de compte obligatoire, **nom complet et téléphone obligatoires** pour la livraison, pourboire désactivé, limite d'ajout au panier activée (empêche les concurrents de sonder le stock).
- **Politiques légales** : modèles Shopify pour pré-remplir, puis **désactiver l'automatisation et tout relire à la main**. Politique de remboursement alignée mot pour mot sur la règle de retour configurée. **Rétractation : 14 jours minimum** (légal).
- **Bannière cookies** : indispensable — sans elle, le tracking Shopify se fausse (visites, ventes, taux de conversion mal comptés).
- **Livraison** : supprimer les zones par défaut, créer sa zone, un seul modèle (payante fixe / gratuite / gratuite au-dessus d'un seuil), délai affiché cohérent avec celui des fournisseurs.
- ⚠️ **Ne jamais copier-coller les textes légaux depuis un autre shop** — crée une empreinte qui relie les sites entre eux → [[footprints-seo-concurrence]].

## Nom de domaine et DNS
Registrar classique (jamais Shopify, jamais les registrars à 1$/an qui bloquent le transfert). **.com et .fr** si possible, jamais d'accent, engagement 1 an (pas pluriannuel par défaut). DNS : enregistrement **A** sur `@` vers l'IP Shopify, **CNAME** sur `www` vers l'adresse myshopify. Domaine principal **sans `www`**. Email pro : boîte dédiée à la boutique plutôt qu'une simple redirection d'alias.

## Branding assisté par IA
- **Naming** : IA positionnée en expert branding **premium**, avec concurrents et contexte produit, noms courts (1-2 mots), mémorables, internationaux — puis lui faire trancher et justifier.
- **Palette** : deux couleurs de base + une couleur d'action réservée aux boutons (3-4 couleurs max), éviter les couleurs déjà saturées dans la niche.
- **Logo** : rester simple (souvent typo + nom), faire critiquer par une IA. Approche 80/20 — ne pas y passer des jours au lancement, le marketing prime. Livrable utile : 4 versions (complet/symbole, noir/blanc, fond transparent).

## Fiche produit brandée — principes de structure
Analyser le best-seller d'un bon concurrent en version mobile, dans l'ordre de perception image → prix → titre → structure. **Au-dessus de la ligne de flottaison** (80-90% des achats mobile) : titre brandé répondant à l'objection n°1, spécification clé, prix/offre, images/vidéo, bullet points, variantes aux noms brandés, avis, garanties. **Avis** : ne retenir que ceux qui détruisent une objection précise.

## Halal / vigilance
Bon réflexe sur la conformité légale (politiques relues, rétractation, cookies). Deux points à arbitrer : l'achat d'articles de presse pour afficher des logos "vu dans" (preuve sociale achetée), et la consigne d'afficher "excellent ou rien" sur les notes d'avis — qui ne doit jamais conduire à masquer des avis réels → [[copywriting-positionnement-lameute]].

## Relations
- Complète [[seo-on-site-lameute]] côté technique et [[page-produit-conversion-lameute]] côté structure de conversion.
- L'empreinte des textes légaux copiés rejoint directement [[footprints-seo-concurrence]].

## Sources
- [[lameute-google-ads-influence-2026]] — formation La Meute module 10 (vidéos 109-114), via cerveau Obsidian Google d'un ami.
