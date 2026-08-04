---
type: concept
title: "IA (Claude) pour l'e-commerce — texte & visuels (La Meute)"
slug: ia-claude-ecommerce-lameute
tags: [ia, claude, prompting, visuels, contenu, shopify, la-meute]
sources: ["[[lameute-google-ads-influence-2026]]"]
source_count: 1
status: active
updated: 2026-08-04
---

# IA (Claude) pour l'e-commerce — texte & visuels

**Définition :** Usage de Claude comme partenaire opérationnel. Principe transversal : la valeur est dans la direction (contexte précis pour le texte, direction artistique pour l'image), pas dans l'outil.

## Trois modes de travail avec Claude
- **Exécution** : instruction précise + contexte + règles + format.
- **Partenaire** (le plus puissant) : aller-retour, laisser proposer, itérer.
- **Agency** : configurer une fois (projet + instructions permanentes + docs) → appliqué automatiquement.

## Structure de prompt texte (3 niveaux)
Base = Contexte + Tâche + Règles. Pro = structure en 8 points (contexte tâche, contexte de ton, background data, tâche+règles, exemple de style, description immédiate, format obligatoire, auto-vérification). La différence débutant/pro est la **précision**, pas la complexité. Fiches produits : 150-200 mots, ton factuel, interdits "premium/confort/robustesse" (mots vides de preuve).

## Projets, Skills, Connecteurs
**Projet** = contexte permanent ; **Skill** = méthode encodée, déclenchée automatiquement. Projet + Skill = production industrialisée (article de blog en ~30s). Connecteurs cités : Gmail, Drive, Figma, Notion, Stripe ; Claude for Chrome pour la navigation/extraction d'avis/analyse concurrent par URL.

## Reproduire une section Shopify sans développeur
Screenshot PC+mobile + copier le HTML (Inspecter) → envoyer à Claude cadré "expert Shopify Liquid" → génère le `.liquid` complet + instructions d'intégration (dupliquer le thème → Modifier le code → dossier sections → coller). Demander de garder ses propres typos.

## Visuels produit par IA
- **Lire le marché** : 5 concurrents, 10 screenshots/concurrent des visuels les plus utilisés (pubs Meta = testés/qui convertissent).
- **Univers visuel** : 4 dimensions (mood, lumière, textures, énergie), moodboard 8-15 images analysé par Claude → style + mots-clés par catégorie.
- **Prompt image en 5 blocs** (toujours dans l'ordre) : sujet → ambiance+lumière → style → palette+texture → paramètres. Max 8 mots-clés, prompts en anglais, affiner une variable à la fois. **Negative prompt** (texte, watermark, logo, distorsion).
- **Reverse prompting** : uploader une image inspirante à Claude → il en extrait le prompt (reproductible à ~80% en 30s).
- **Finition** (jamais l'étape finale) : upscale, sublimation, détourage.

## Point de vigilance majeur : hallucinations branding
L'IA altère/invente texte, logos, mentions légales sur le produit — **ne jamais publier un visuel IA aux mentions légales sans vérifier**. Solutions : masque/inpainting, recomposer le texte en post-production, angles cachant le packaging, ou **générer la scène vide puis intégrer le vrai produit** (le plus propre).

## Halal
**Mannequins IA avec visage** : abstention recommandée tant qu'il n'y a pas de position claire des savants de l'écosystème sur la représentation figurée — rester sur packshot/lifestyle/UGC/statics. Zéro tromperie : description fidèle, alignement visuel↔produit reçu, mentions légales jamais altérées.

## Relations
- Applique directement le principe déjà utilisé pour la recherche produit → [[recherche-produit-ia-claude]].
- Alimente [[copywriting-positionnement-lameute]] et [[boutique-shopify-branding-lameute]].

## Sources
- [[lameute-google-ads-influence-2026]] — formation La Meute module 7, via cerveau Obsidian Google d'un ami.
