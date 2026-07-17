---
type: concept
title: "Loop Engineering (Ingénierie de Boucles)"
slug: loop-engineering
tags: [claude-code, automation, agentic, workflow, loop]
sources: ["[[raytar-loop-engineering-claude]]"]
source_count: 1
status: active
updated: 2026-07-17
---

# Loop Engineering

**Définition :** Paradigme d'utilisation de Claude où l'on écrit des boucles qui font tourner Claude à sa place, au lieu de taper des prompts un par un. "Prompting is doing the work. Loop engineering is managing the worker." → [[raytar-loop-engineering-claude]]

**Origine :** Boris Cherny (@bcherny), ingénieur qui a construit Claude Code chez Anthropic — juin 2026 : "Je ne prompts plus Claude. Des boucles promptent Claude pour moi. Mon travail est maintenant d'écrire des boucles."

**Différence fondamentale avec le prompting :**

| Prompting | Loop Engineering |
|---|---|
| Tu vérifies le travail | La boucle vérifie le travail |
| Tu décides la prochaine étape | Claude décide la prochaine étape |
| Tu colles les erreurs | La boucle gère les erreurs |
| Tu es la boucle | Tu écris la boucle |

## Les 5 temps de toute boucle

1. **Trouver le travail** — tâches ouvertes, tests en échec, fichiers dans un dossier, emails non lus
2. **Le faire** — traiter un item à la fois, jusqu'au bout
3. **Se vérifier** — une deuxième passe confirme que c'est done ET correct (preuve, pas confiance)
4. **Se souvenir** — écrire l'état dans LOOP-STATE.md pour ne jamais repartir de zéro
5. **Recommencer** — répéter jusqu'à épuisement, puis alerter

## Loop vs Cron job

Un cron job lance un script fixe — mêmes étapes à chaque fois, aucune décision. Une boucle lance Claude — Claude regarde la situation actuelle, choisit l'action suivante, vérifie le résultat, décide de continuer/réessayer/s'arrêter. **Il y a un décideur à l'intérieur.** Cela n'était pas possible avant que les LLMs soient capables de prendre de vrais jugements en cours de tâche.

## Les deux commandes Claude Code

### `/goal` — boucle avec ligne d'arrivée

Tu décris un état final mesurable. Claude travaille en autonomie, tour après tour. Après chaque tour, **une seconde instance Claude vérifie silencieusement** : est-ce que l'objectif est atteint ? Si non, elle explique pourquoi et le travail continue. Dès que l'objectif est atteint, la boucle s'arrête seule.

```
/goal [état final mesurable en 1-2 phrases]
[conditions supplémentaires]
[critère d'arrêt explicite]
```

Exemple :
```
/goal write a one page brief on [topic]
where every claim has at least three sources and
every link opens to a real page that supports the claim.
Open each link to confirm it before you call it done.
Stop only when every source checks out.
```

**Usage :** quand il y a une ligne d'arrivée. *"Travaille jusqu'à ce que X soit vrai."*

### `/loop` — boucle sur un rythme

```
/loop [intervalle] [action à répéter]
[condition d'arrêt]
```

Exemple :
```
/loop 30m check whether my live site is back up by loading the homepage.
The moment it returns a normal page, tell me and stop checking.
```

**Usage :** quand il n'y a pas de fin, juste un rythme. *"Vérifie ça encore et encore."*

La plupart des boucles puissantes commencent par `/goal`.

## La charte complète (template opérationnel)

Copier-coller dans Claude Code, remplir les crochets :

```
You are running as a loop, not answering one prompt. Here is your charter.

GOAL
[État final en 1-2 phrases. Spécifique et mesurable.
Ex: "Chaque page produit dans /pages a le nouveau pricing et chaque lien s'ouvre."]

WHERE THE WORK IS
[Où chercher le travail.
Ex: "Scan le dossier /pages pour les fichiers avec l'ancien prix."
Ou: "Lis TODO.md et traite chaque case non cochée comme une tâche."
Ou: "Check mon task board pour les items taggés ai."]

HOW TO WORK
- Traiter un item à la fois. Le finir entièrement avant de passer au suivant.
- Suivre les patterns des fichiers existants. Ne pas en inventer de nouveaux.
- Si un item nécessite une décision que seul je peux prendre (dépenser de l'argent,
  supprimer des choses, envoyer un email à quelqu'un), s'arrêter sur cet item,
  l'ajouter à une liste "needs me", et passer au suivant.

HOW TO CHECK YOURSELF
Après chaque item, prouver qu'il est done avant de le marquer comme done.
[Choisir : "lancer les tests" / "relire le fichier et confirmer qu'il remplit l'objectif"
/ "ouvrir le lien et confirmer qu'il se charge". Vérifier = preuves, pas confiance.]
Si la vérification échoue, corriger et vérifier à nouveau.
3 essais par item, puis logger comme bloqué et passer.

HOW TO REMEMBER
Garder un fichier LOOP-STATE.md.
Après chaque item, écrire : nom, statut (done / blocked / needs me),
ce qui a changé, ce que la prochaine exécution doit savoir.
Lire ce fichier EN PREMIER à chaque exécution.

WHEN TO STOP
S'arrêter quand tous les items sont done ou bloqués, ou quand [N] items ont été traités.
Rapport final : ce qui est fait, ce qui est bloqué, ce qui nécessite ma décision.

Commencer par lire LOOP-STATE.md s'il existe, puis trouver le travail.
```

## LOOP-STATE.md — le héros silencieux

Sans fichier d'état, chaque exécution repart de zéro. Avec LOOP-STATE.md, la boucle reprend exactement là où elle s'est arrêtée, même sur une exécution planifiée. Format minimal :

```markdown
# Loop State

## Dernière exécution : 2026-07-17

| Item | Statut | Ce qui a changé | Notes |
|---|---|---|---|
| Page produit A | done | Prix mis à jour, lien vérifié | — |
| Page produit B | blocked | Lien mort, aucun remplaçant trouvé | Nécessite décision humaine |
| Page produit C | needs me | Demande approbation avant suppression | — |
```

## Quand NE PAS utiliser une boucle

1. **Tâche ponctuelle** — un seul prompt est plus rapide ; la boucle vaut son coût de setup sur du travail répétitif ou à nombreux items
2. **Coût API plus élevé** — une boucle qui vérifie et réessaie lance Claude plusieurs fois par item → limite de quota atteinte plus vite
3. **Objectif vague** — "Améliore ma stratégie" n'est pas une boucle. Définir d'abord ce que done veut dire concrètement.

## Applications directes

**SEO (lien avec [[agent-seo-ia]]):**
```
/goal audit les 50 articles du blog harnais-chien-expert.fr
Vérifier pour chacun : title tag < 60 car, meta description 150-160 car, 1 lien interne vers page produit.
Logger chaque article avec son statut et les corrections à faire.
Stop quand tous les articles sont audités.
```

**Vault ([[persistent-wiki]]):**
```
/goal ingère tous les fichiers .md dans raw/assets/ qui n'ont pas encore de source-note dans wiki/sources/
Vérifier après chaque ingest que la source-note existe et a ≥3 wikilinks.
Logger dans LOOP-STATE.md.
```

**Contenu :**
```
/loop every morning at 9am check my GSC for pages in striking distance (positions 4-15)
and draft one optimization recommendation for the top opportunity.
```

## Relations

- [[agent-seo-ia]] — même logique de spécialisation et d'autonomie, appliquée au SEO avec 12 agents
- [[multi-model-ai-workflow]] — la mémoire partagée entre outils est le pendant cross-tools du LOOP-STATE.md
- [[persistent-wiki]] — le vault est une forme de mémoire externe ; le skill `/ingest` peut lui-même devenir une boucle
- [[prompt-engineering]] — le loop engineering est l'étape suivante : écrire des systèmes qui promptent, pas des prompts

## Tensions / open questions

- `/goal` et `/loop` sont des fonctionnalités récentes de Claude Code (juin 2026) — mettre à jour Claude Code si les commandes ne sont pas disponibles
- Les boucles coûtent plusieurs fois plus en tokens/quota qu'un prompt unique — à calibrer selon le plan Claude
- La qualité de la vérification dépend de comment on définit "done" — un critère vague produit une boucle qui se termine prématurément

## Sources

- [[raytar-loop-engineering-claude]] — paradigme complet, /goal vs /loop, charter template, LOOP-STATE.md, 3 cas à éviter
