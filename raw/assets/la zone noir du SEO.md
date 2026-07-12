---
title: "Post by @JotaroSeo on X"
source: "https://x.com/JotaroSeo/status/1724124943300886932"
author:
  - "[[@JotaroSeo]]"
published: 2023-11-13
created: 2026-06-15
description: "[Thread] Vient découvrir une partie de la zone noir du SEO avec la technique \"Cloaking ID\" ! Lecture : 4min"
tags:
  - "clippings"
---
\[Thread\]

🔎 Vient découvrir une partie de la zone noir du SEO avec la technique "Cloaking ID" ! 👇👇

Lecture : 4min ⏱️

![Image](https://pbs.twimg.com/media/F-1Sfv2WYAA1cBS?format=jpg&name=large)

---

1/ Qu’est-ce que le cloaking ID ? 🕵️‍♂️💻

Tout d’abord, je voulais être clair sur une chose c’est qu’il y a plusieurs types de cloaking et tous ne sont pas des techniques black hat !

Bref, le cloaking ID est une technique black hat

---

Son objectif est de présenter un contenu du site qui varie en fonction du type de visiteur (robot ou internaute).

Laisse-moi t’expliquer plus en détails 👇👇

---

2/ Les User agent🤖

Tout part du champ d'en-tête inclus dans la requête HTTP qu’on appelle “User Agent” il sert à savoir qui vient d’entrer sur le serveur du site. Notre but ce serait de manipuler cet en-tête en mettant du contenu différent en fonction de l’utilisateur identifié

---

En gros ce champ d’en-tête va te servir de carte d'identité électronique qui informe le serveur sur le type de visiteur.

Cela va nous permettre de présenter un contenu spécifique aux robots tout en montrant quelque chose de différent aux internautes.

---

Exemple d’en-tête “User-Agent" :

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36

---

2.1/ Une autre technique pour savoir le type de visiteur 🔍

👉 Certains sites peuvent utiliser des scripts côté serveur pour analyser d'autres aspects de la connexion, comme l'adresse IP ou d'autres informations dans la requête, pour essayer de déduire le type du visiteur.

---

Mais la plupart du temps l'en-tête "User-Agent" reste la méthode standard et la plus fiable pour identifier si le visiteur du site est un robot ou un internaute lambda (un humain).

---

3/ Exemple de pourquoi les gens utilisent le cloaking ID 🔎

Imaginons que nous voulons optimiser au maximum notre SEO mais le problème est que nous avons du contenus comme des vidéos, des fichiers audios et des images (sans balise alt).

---

Le cloaking ID pourrait entrer en jeu ! Pourquoi ? Car ce sont des contenus que les googlebots ont du mal à analyser.

Tu me suis ? mdrr

On aurait donc :

---

👉 Site pour les bots :

On ne placera aucun contenu sur lequel il aura du mal à analyser (vidéos, fichier…) mais il y aura beaucoup de textes, une bonne structuration des HN, opti du netlinking interne…

D’ailleurs c’est sur cette version que le SEO est le plus optimisé.

---

👉 Site pour les internautes :

Garder tout l’aspect design qu’on aura enlevé sur le site pour les robots, pour avoir la meilleur expérience utilisateur possible, bien-sûr en respectant les core web vitals.

D’ailleurs, on remettra le contenu que les bots ont du mal à analyser

![Image](https://pbs.twimg.com/media/F-1ShoKWYAAqmxE?format=jpg&name=large)

---

C’est l’heure d’un petit résumé ! 👇

Pour l’instant nous avons vu :

👉 Qu’est-ce que le cloaking ID

👉 L’importance du champ "User-Agent" pour savoir le type de visiteur

👉 Enfin, je t’ai montré pourquoi cette stratégie est intéressante