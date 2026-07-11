# CLAUDE.md — Règles du vault Cerveaux

Ce fichier est lu par le skill `ingest` (Step 4) à chaque ingestion, et doit être lu par Claude en début de toute session touchant ce vault. Il encode les règles opérationnelles du vault — pas le contenu (voir `index.md` pour le catalogue).

## Domaine par défaut
Pas de domaine unique : vault multi-thématique (SEO, GEO/IA, e-commerce Shopify, business halal, copywriting, marketing, méthode Meta Ads, création de site web). Toujours taguer une page avec son domaine dans le frontmatter (`domain:`).

## Structure

- `raw/` — source brute extraite (PDF texte, tweet JSON→md, transcript...). **Jamais édité après création**, ni par l'utilisateur ni par Claude. C'est la couche géologique : si besoin de reformuler, créer une nouvelle page dans `wiki/`, ne pas toucher `raw/`.
- `wiki/sources/` — une note par source ingérée (résumé structuré, toujours liée à sa source `raw/`).
- `wiki/concepts/` — une page par idée/technique/pattern réutilisable.
- `wiki/entities/` — une page par personne/outil/organisation notable.
- `wiki/topics/` — synthèses transverses qui agrègent plusieurs sources/concepts.
- `index.md` — catalogue complet. **Toujours lu en premier** en début de session ou avant une requête sur le vault. Mis à jour à chaque ingest.
- `log.md` — historique append-only. Format : `## [YYYY-MM-DD] <op> | <titre>` avec `<op>` ∈ {ingest, query, lint, schema, maint, synthesis}.

## Règle des backlinks (obligatoire à chaque ingest)

Toute nouvelle page (`source`, `concept`, `entity`, `topic`) doit contenir **au moins 3 wikilinks** vers des pages existantes du vault, dont **au moins 1 vers une page vieille de 2+ mois**. Une page sans lien entrant/sortant est un fichier mort, pas un nœud du graphe — ne pas la laisser orpheline. Chercher activement dans `wiki/concepts/` et `wiki/entities/` avant de conclure qu'aucun lien n'existe.

## Maintenance périodique (op `maint`)

À faire quand demandé, ou proactivement si plus de 2 semaines depuis le dernier `maint` (voir `log.md`) :
1. Chercher les wikilinks cassés : `grep -rohE '\[\[[^]]+\]\]' wiki/ | sort -u` puis vérifier que chaque cible a un fichier correspondant.
2. Chercher les pages orphelines (0 backlink entrant) dans `wiki/concepts/` et `wiki/entities/`.
3. Vérifier que `index.md` référence bien tous les fichiers présents dans `wiki/` (pas de fichier créé sans entrée d'index).
4. Logger le résultat dans `log.md` sous `## [YYYY-MM-DD] maint | ...`.

## Synthèse périodique (op `synthesis`)

Sur demande (pas d'automatisation cron active pour l'instant) : relire les entrées `log.md` des 7 derniers jours, produire `wiki/topics/synthese-YYYY-Www.md` — thèmes récurrents entre les sources ingérées, contradictions avec des pages existantes, questions ouvertes. Lier vers les sources concernées.

## Notes

- Vault non versionné avec git avant 2026-07-11 — les commits auto du skill `ingest` (Step 8) ne s'appliquaient pas silencieusement. Vérifier `git status` avant de compter dessus.
- `index.md` référence `[[overview]]` comme point d'entrée mais `wiki/overview.md` n'existe pas — lien cassé à corriger en priorité au prochain `maint`.
