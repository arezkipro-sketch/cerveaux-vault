---
type: source-note
title: "Stop Being the Loop. Here's How to Make Claude Work While You Sleep."
slug: raytar-loop-engineering-claude
page-type: source
domain: ai-tools
tags: [claude-code, loop-engineering, automation, workflow, agentic]
sources: ["[[raytar]]"]
related: ["[[loop-engineering]]", "[[agent-seo-ia]]", "[[multi-model-ai-workflow]]"]
source-url: "https://x.com/raytar/article/2069212188619805179"
source-type: article-x
author: "[[raytar]]"
date-published: 2026-06-23
date-accessed: 2026-07-17
raw-file: "raw/assets/Stop Being the Loop. Here's How to Make Claude Work While You Sleep..md"
status: processed
---

# Stop Being the Loop. Here's How to Make Claude Work While You Sleep.

**Source :** [[raytar]] — X article, 2026-06-23
**Inspiré de :** Boris Cherny (@bcherny), ingénieur qui a construit Claude Code chez Anthropic

## Overview

Le paradigme dominant — type un prompt, Claude fait quelque chose, tu vérifies, tu recolles l'erreur — fait de toi la boucle elle-même. La solution : le **loop engineering**, écrire des boucles qui font tourner Claude à ta place jusqu'à ce que le travail soit fini et vérifié. Deux commandes Claude Code : `/goal` (boucle jusqu'à l'état final) et `/loop` (boucle sur un rythme).

## Key Takeaways

1. **"Tu es la boucle"** — tu babysitts exactement ce que tu voulais déléguer : vérifier le travail, décider la prochaine étape, coller les erreurs
2. **Loop engineering ≠ prompting** : "Prompting is doing the work. Loop engineering is managing the worker."
3. **`/goal`** — Claude travaille en boucle jusqu'à ce qu'un état mesurable soit atteint ; après chaque tour, une seconde instance Claude vérifie si l'objectif est atteint
4. **`/loop`** — Claude répète une action sur un rythme défini (ex : toutes les 30 minutes)
5. **LOOP-STATE.md** — fichier d'état qui permet à la boucle de reprendre exactement là où elle s'est arrêtée
6. **La charte (charter)** — template structuré avec GOAL / WHERE / HOW TO WORK / HOW TO CHECK / HOW TO REMEMBER / WHEN TO STOP

## Detailed Notes

### Le problème : tu es la boucle

Workflow actuel :
1. Tu tapes un prompt
2. Claude édite un fichier
3. Tu lances le test
4. Ça casse
5. Tu colles l'erreur
6. Claude réessaie

Résultat : 20 minutes plus tard tu te rends compte que tu gardais la main sur exactement ce que tu voulais déléguer.

**Exemple concret — les sources fantômes :** demander à Claude un brief d'une page avec sources. Il livre quelque chose de propre et confiant. Mais certaines sources sont inventées — les liens mènent nulle part ou ne disent pas ce que Claude prétend. **Un seul prompt ne peut jamais attraper ça** parce que Claude reste confiant jusqu'à ce que quelque chose ouvre le lien.

**Avec `/goal` à la place :**
```
/goal write a one page brief on [topic]
where every claim has at least three sources and
every link opens to a real page that supports the claim.

Open each link to confirm it before you call it done.
Replace any source that is dead or does not back up the claim.
Stop only when every source on the page checks out.
```
Claude écrit le brief, puis va lien par lien, les ouvre, jette les morts et les faux, trouve des remplaçants, jusqu'à ce que toutes les sources soient vérifiables.

### Loop vs Cron job

| | Cron job | Loop |
|---|---|---|
| Lance | Un script fixe | Claude |
| Décision | Aucune — mêmes étapes à chaque fois | Claude évalue la situation, choisit l'action suivante |
| Sur erreur | Continue le script | Analyse, réessaie avec une approche différente |
| Résultat | Prévisible mais rigide | Adaptatif |

**La différence clé :** il y a un décideur à l'intérieur de la boucle.

### Les 5 temps de toute boucle

1. **Trouver le travail** — tâches ouvertes, tests en échec, emails non lus, fichiers dans un dossier
2. **Le faire** — Claude traite un item à la fois, jusqu'au bout
3. **Se vérifier** — une deuxième passe confirme que le travail est fait ET correct (pas juste produit)
4. **Se souvenir** — écrire ce qui est terminé pour ne jamais refaire ou perdre sa place
5. **Recommencer** — répéter jusqu'à ce qu'il n'y ait plus rien, puis s'arrêter ou alerter

### `/goal` — la boucle avec ligne d'arrivée

Tu décris l'état final mesurable. Claude travaille en autonomie, tour après tour. Après chaque tour, une **seconde instance de Claude vérifie silencieusement** : est-ce qu'on a atteint l'objectif ? Si non, elle explique pourquoi au premier, et le travail continue. Dès que l'objectif est atteint, la boucle s'arrête seule.

Usage : quand il y a une ligne d'arrivée claire. *"Travaille jusqu'à ce que ceci soit vrai."*

### `/loop` — la boucle sur un rythme

```
/loop 30m check whether my live site is back up by loading the homepage.
The moment it returns a normal page, tell me and stop checking.
```

Usage : quand il n'y a pas de ligne d'arrivée, juste un rythme. *"Vérifie ça encore et encore."*

### La charte complète (template à coller)

```
You are running as a loop, not answering one prompt. Here is your charter.

GOAL
[État final en 1-2 phrases. Être spécifique sur ce que DONE signifie, et le rendre mesurable.]

WHERE THE WORK IS
[Où chercher. Ex: "Scan le dossier /pages", "Lis TODO.md et traite chaque case non cochée", "Check mon task board pour les items taggés ai"]

HOW TO WORK
- Traiter un item à la fois. Le finir entièrement avant de passer au suivant.
- Suivre les patterns des fichiers existants. Ne pas en inventer de nouveaux.
- Si un item nécessite une décision que seul je peux prendre (dépenser de l'argent, supprimer des choses, envoyer un email), s'arrêter sur cet item, l'ajouter à une liste "needs me", et passer au suivant.

HOW TO CHECK YOURSELF
Après chaque item, prouver qu'il est fait avant de le marquer comme done.
[Choisir ce qui convient: "lancer les tests" / "relire le fichier et confirmer qu'il remplit l'objectif" / "ouvrir le lien et confirmer qu'il se charge".]
Si la vérification échoue, corriger et vérifier à nouveau. 3 essais par item, puis logger comme bloqué et passer.

HOW TO REMEMBER
Garder un fichier LOOP-STATE.md.
Après chaque item, écrire : nom de l'item, statut (done / blocked / needs me), ce qui a changé, ce que la prochaine exécution doit savoir.
Lire ce fichier EN PREMIER à chaque exécution pour ne jamais refaire du travail terminé.

WHEN TO STOP
S'arrêter quand tous les items sont done ou logged comme bloqués, ou quand [N] items ont été traités cette exécution.
Puis donner un rapport court : ce qui a été fait, ce qui est bloqué, ce qui nécessite ma décision.

Commencer par lire LOOP-STATE.md s'il existe, puis trouver le travail.
```

### Quand NE PAS construire une boucle

1. **Tâches ponctuelles** — un seul prompt est plus rapide ; les boucles valent leur coût de setup sur du travail qui se répète ou a beaucoup de morceaux
2. **Les boucles coûtent plus** — une boucle qui se vérifie et réessaie fait tourner Claude plusieurs fois par item → limite de quota atteinte plus vite
3. **Travail vague** — "Pense à une meilleure stratégie produit" n'est pas une boucle. D'abord définir l'objectif réel.

## Sources

- [[raytar]] — guide complet loop engineering : Boris Cherny quote, exemple brief avec sources, /goal vs /loop, charter template, LOOP-STATE.md
