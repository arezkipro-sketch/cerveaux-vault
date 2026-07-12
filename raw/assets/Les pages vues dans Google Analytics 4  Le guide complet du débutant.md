---
title: "Les pages vues dans Google Analytics 4 : Le guide complet du débutant"
source: "https://fr.semrush.com/blog/pages-vues/"
author:
  - "Aida Knezevic"
published: 2024-08-02
created: 2026-06-15
description: "Apprends où trouver les pages vues dans Google Analytics 4. Découvre comment utiliser ces données pour améliorer le trafic sur le site web."
tags:
  - "clippings"
---
Nous avons traduit cet article de l'anglais. [Clique ici](https://www.semrush.com/blog/pageviews/) pour lire l'article original. Si tu remarques des problèmes dans le contenu, n'hésite pas à nous contacter à [report-osteam@semrush.com](mailto:report-osteam@semrush.com).

En tant que propriétaire de site Web, le suivi des pages vues dans Google Analytics 4 est probablement en tête de ta liste de priorités.

Tu as consacré beaucoup d'efforts à la construction de ton site Internet et à son optimisation pour une excellente expérience utilisateur. Et les données sur les pages vues te permettent de mesurer le succès de tes efforts et de trouver des domaines à améliorer.

Dans ce guide, nous allons te montrer où trouver les données sur les pages vues et comment les utiliser pour améliorer les performances de ton site Web.

## Qu'est-ce qu'une page vue dans Google Analytics 4?

Dans Google Analytics 4 (GA4), une page vue est un événement qui se déclenche lorsqu'un utilisateur consulte une page de ton site Web.

Voici un exemple de rapport de pages vues dans GA4:

![Un rapport de pageview dans GA4](https://static.semrush.com/blog/uploads/media/a8/5c/a85c854a546cfdd1f7c2c1dc18a1f175/734552ffee0be3a258c6cf1e99d14bc6/original.png)

Un rapport de pageview dans GA4

Techniquement, l'événement s'écrit "page\_view". Mais par souci de lisibilité, nous l'épelerons également sans le trait de soulignement tout au long de cet article.

L'événement pageview se déclenche chaque fois que le navigateur de l'utilisateur charge ou recharge une page. Ainsi, si un utilisateur voit la même page plusieurs fois, GA4 comptera toujours les vues répétées.

GA4 recueille automatiquement les données sur les pages vues - tu n'as pas besoin de configurer quoi que ce soit manuellement dans ton compte.

Cet événement peut t'aider à comprendre quelles sont les pages de ton site Internet qui reçoivent le plus de trafic. Il te permet également de comparer les chiffres du trafic au fil du temps:

![Une section du rapport de pageview dans GA4, avec les dates et les métriques de comparaison mises en évidence.](https://static.semrush.com/blog/uploads/media/f2/1b/f21beabd6d0b427923b5510596206cf0/dd86ab696fe9396210e511aeb34b5a56/original.png)

Une section du rapport de pageview dans GA4, avec les dates et les métriques de comparaison mises en évidence.

La comparaison des données sur les pages vues te permet d'analyser le succès de ta stratégie de référencement, d'identifier les tendances du trafic et de prendre des décisions fondées sur des données.

Mais garde à l'esprit que les pages vues en elles-mêmes ne donnent pas une image complète. Tu dois prendre en compte d'autres paramètres comme les conversions et le temps d'engagement pour une analyse plus approfondie.

Il se peut que tu obtiennes un nombre élevé de pages vues. Mais si ces pages vues ne conduisent pas à un engagement avec ton contenu ou à des conversions (comme des ventes ou des inscriptions à des courriels), cela peut être le signe de problèmes plus profonds avec ton contenu ou ton site Web.

***Autres lectures****:* [*Optimisation du taux de conversion: 9 tactiques qui fonctionnent.*](https://www.semrush.com/blog/conversion-rate-optimization/)

### Explication des paramètres de l'événement GA4 Pageview

Chaque fois que ton site Web reçoit une page vue, Google Analytics recueille également des informations supplémentaires sur cette interaction. C'est ce qu'on appelle les paramètres de l'événement.

Ils offrent "un contexte et des détails précieux sur l'interaction", [selon Google](https://support.google.com/analytics/answer/13675006?hl=en).

GA4 recueille ces paramètres de l'événement page\_view:

- **page\_location** (l'URL de la page)
- **page\_referrer** (l'URL de la page sur laquelle l'utilisateur se trouvait auparavant)

Ces paramètres sont importants car ils fournissent des informations supplémentaires sur l'expérience du visiteur sur ton site.

Avant d'entrer dans les détails de la recherche de données sur les pages vues dans GA4, nous devons comprendre quelques autres métriques.

## GA4 Vues vs. Sessions vs. Utilisateurs

Les vues, les sessions et les utilisateurs correspondent tous à des mesures différentes dans Google Analytics 4:

- **Vues**: La somme des pages et des écrans que tes utilisateurs ont vus (une vue d'écran est la même chose qu'une vue de page - juste pour les applications, plutôt que pour les pages Web). Il comprend des vues répétées d'une page ou d'un écran.
- **Sessions**: La période de temps pendant laquelle un utilisateur interagit avec ton site web (ou ton appli). Elle commence à partir du moment où un visiteur ouvre ton site Internet et se termine après 30 minutes d'inactivité.
- **Utilisateurs**: Une personne qui a visité ton site web ou ton appli. Dans GA4, la principale mesure de l'utilisateur est "Utilisateurs actifs". Il s'agit des utilisateurs qui ont eu une session engagée. Une session engagée dure au moins 10 secondes ou comprend au moins un événement de conversion, ou au moins deux screen/pageviews.

***Autres lectures****:* [*12 mesures clés de Google Analytics à suivre*](https://www.semrush.com/blog/metrics-in-google-analytics/)

## Pages vues de Universal Analytics vs. Vues de GA4

Il existe de nombreuses différences entre Universal Analytics (UA) et Google Analytics 4. Mais la mesure du nombre de pages vues est restée en grande partie la même.

Dans UA, "Pageviews" faisait référence au nombre total de **pages** qu'un visiteur a consultées sur ton site Web. Il s'agit notamment de vues répétées.

Dans GA4, le terme "Vues" désigne le nombre de **pages et/ou d'écrans d'appli** qu'un utilisateur voit sur ton site web ou ton appli. Il compte également les vues répétées.

Auparavant, UA mesurait les données de l'appli (comme les vues d'écran) dans une propriété différente. GA4 fusionne les données du site web et de l'appli dans la même propriété. Donc, si tu suis ton site web et ton appli dans GA4, n'oublie pas que la métrique des vues contient les données des deux.

### Y a-t-il des pages vues uniques dans GA4?

Contrairement à UA, GA4 n'a pas de "pages vues uniques" comme mesure.

Au lieu de cela, le rapport sur les pages et les écrans contient des "vues", des "utilisateurs" et des "vues par utilisateur", ainsi que d'autres mesures.

![Les pages et les écrans sont présentés en format GA4, avec les noms des colonnes métriques en surbrillance.](https://static.semrush.com/blog/uploads/media/f8/d6/f8d6755a74a52817e99553985ff188f5/97b70a47fb7303c2e743be13e2b843e4/original.png)

Les pages et les écrans sont présentés en format GA4, avec les noms des colonnes métriques en surbrillance.

Certains spécialistes du marketing s'appuient sur la mesure "Utilisateurs" comme alternative aux pages vues uniques. Il s'agit du nombre total d'utilisateurs actifs uniques qui ont consulté une page donnée.

## Comment voir les pages vues dans Google Analytics 4

Il y a plusieurs façons de voir les pages vues dans les différents rapports GA4. Nous couvrons les deux principales méthodes ci-dessous:

### 1\. Rapport sur les pages et les écrans

Le rapport sur les pages et les écrans affiche des données sur les pages que les utilisateurs ont visitées sur ton site web. Si tu suis également une application dans GA4, ce rapport comprendra également des données sur les écrans spécifiques que les utilisateurs ont consultés.

Pour trouver le rapport sur les pages et les écrans, trouve la barre latérale dans le [tableau de bord GA4](https://www.semrush.com/blog/google-analytics-dashboard/) et clique sur " **Rapports**."

![Naviguer vers "Rapports" dans la barre latérale de GA4](https://static.semrush.com/blog/uploads/media/b2/9c/b29cb05c51aa182be15572d09d7477fa/a115d49dc2294f1a817cabcc951aa481/original.png)

Naviguer vers "Rapports" dans la barre latérale de GA4

Clique sur " **Cycle de vie** " > " **Engagement** " > " **Pages et écrans** ".

![Naviguer vers "Pages et écrans" dans la barre latérale de GA4](https://static.semrush.com/blog/uploads/media/07/db/07db8f2176b92e9e85c6d75d31315476/54aa9f68510cc640d9b9cc6904eee355/original.jpeg)

Naviguer vers "Pages et écrans" dans la barre latérale de GA4

Cela te permettra d'accéder au rapport sur les pages et les écrans.

![Une section graphique du rapport des pages et des écrans dans GA4](https://static.semrush.com/blog/uploads/media/a0/ca/a0cad2ae0f7f3de72ccf6df258da20d4/1ca1e9cc48374bd068e4973751ce3265/original.jpeg)

Une section graphique du rapport des pages et des écrans dans GA4

Le tableau situé sous le graphique comprend des données sur les "vues", les "utilisateurs", les "vues par utilisateur" et d'autres paramètres. (N'oublie pas que la mesure "Vues" comprend les pages vues et les vues d'écran).

![Une section de tableau du rapport des pages et des écrans dans GA4](https://static.semrush.com/blog/uploads/media/1a/99/1a991a8b298c5ab5dcefdfd515c5274f/05f10c82afb661e372e2840483da5d63/original.jpeg)

Une section de tableau du rapport des pages et des écrans dans GA4

Tu peux filtrer le rapport du tableau à l'aide de la barre de recherche. Tu peux rechercher des mots individuels ou des chemins d'accès URL spécifiques.

Tape le mot-clé ou le chemin que tu souhaites analyser et appuie sur entrée. Maintenant, tu ne verras que les données relatives à cette page ou à ce groupe de pages.

![Recherche dans le rapport des pages et des écrans pour "/Google+Redesign/"](https://static.semrush.com/blog/uploads/media/f5/46/f546b3e7b17e2b5f7b467e7cbfebe5a5/315973b741980b91b5861a3203531a5e/original.jpeg)

Recherche dans le rapport des pages et des écrans pour "/Google+Redesign/"

### 2\. Rapport sur les événements

Le rapport sur les événements contient des données sur tous les événements que les utilisateurs ont déclenchés sur ton site Web. C'est ici que tu peux trouver le nombre total de vues sur toutes les pages de ton site.

Pour trouver le rapport sur les événements, ouvre le menu de gauche dans ton tableau de bord GA4. Clique sur " **Rapports** ".

![Naviguer vers "Rapports" dans la barre latérale de GA4](https://static.semrush.com/blog/uploads/media/e3/fd/e3fdc890395cca8af8c49d8a695a4a26/b30e2ca5d549b666d869a067cbb47931/original.png)

Naviguer vers "Rapports" dans la barre latérale de GA4

Ensuite, clique sur " **Cycle de vie** " > " **Engagement** " > " **Événements** ".

![Naviguer vers "Requêtes" dans la barre latérale de GA4](https://static.semrush.com/blog/uploads/media/5c/39/5c39d0a8dd376303a964056e52b7b473/413b58b1a852f1a6e774ac506d241902/original.jpeg)

Naviguer vers "Requêtes" dans la barre latérale de GA4

Cela te permettra d'accéder au rapport des événements. En plus de l'événement "page\_view", tu verras des données concernant "user\_engagement" et d'autres événements liés à ta propriété.

![Une section graphique du rapport d'événements dans GA4](https://static.semrush.com/blog/uploads/media/7c/d4/7cd4852838110a74db62718acb7de0d6/cb3428d12a5b1f34e29b618a65db3de7/original.jpeg)

Une section graphique du rapport d'événements dans GA4

Fais défiler vers le bas pour voir un tableau récapitulatif des données de ton événement. Clique sur " **page\_view** " pour accéder à un autre rapport contenant uniquement des données sur les pages vues.

![Une section de tableau du rapport d'événements dans GA4](https://static.semrush.com/blog/uploads/media/6b/d2/6bd2ce9451bc4f4ac542e67329704f13/4f65c3746877f0057aa058324bdf7a23/original.jpeg)

Une section de tableau du rapport d'événements dans GA4

Dans le rapport page\_view, tu peux apprendre combien de vues ton site web a reçu au cours d'une période donnée. Si tu veux que le graphique affiche plutôt les utilisateurs, clique sur " **Total des utilisateurs** " en haut du graphique.

![Le widget "Total des utilisateurs" affiche 29K en surbrillance sous le rapport page_view dans GA4.](https://static.semrush.com/blog/uploads/media/26/ce/26ce9f9cfffd4f878ddc8dc25341886f/5fda1aca8f90c2503d8f20037ac2df83/original.jpeg)

Le widget "Total des utilisateurs" affiche 29K en surbrillance sous le rapport page\_view dans GA4.

Fais défiler vers le bas pour voir des données supplémentaires, comme la répartition géographique de tes pages vues.

![Une section du rapport montrant la répartition géographique des pages vues.](https://static.semrush.com/blog/uploads/media/2b/e6/2be61046beee7ff1ce9964ee45678cc3/5f9cab07dcbb39caebcd8414054db5e2/original.jpeg)

Une section du rapport montrant la répartition géographique des pages vues.

## Comment utiliser les données des vues GA4 pour auditer et augmenter le trafic de ton site Web?

Maintenant que tu sais où trouver les pages vues dans GA4, il est temps d'utiliser ces données pour analyser et booster tes chiffres de trafic. Voici quelques façons de procéder:

### Identifie les pages les plus populaires

Mesurer les pages vues sur Google Analytics peut t'aider à identifier les pages les plus performantes. Et cela te permet de savoir quel type de contenu attire le plus de visiteurs sur ton site Internet.

Tu peux ensuite suivre un schéma similaire lors de la création ou de la mise à jour d'autres pages de ton site.

Une page avec beaucoup de vues pourrait tout de même avoir un faible taux de conversion. Et c'est un signe potentiel d'une mauvaise expérience utilisateur.

!["Temps d'engagement moyen" et colonnes "Conversions" mis en évidence dans le rapport sur le chemin de page et la classe d'écrans.](https://static.semrush.com/blog/uploads/media/db/1e/db1ee0ca30a082c7d81b2873a3f5d54a/3e822d58e19db6983371cb1b852f8100/original.jpeg)

"Temps d'engagement moyen" et colonnes "Conversions" mis en évidence dans le rapport sur le chemin de page et la classe d'écrans.

Comme les données sur les vues contiennent du trafic provenant de tous les canaux, elles ne conviennent pas à tous les types d'analyse.

Si tu veux analyser le succès de ta [stratégie de référencement](https://www.semrush.com/blog/seo-strategy/), par exemple, tu devras examiner spécifiquement le trafic organique.

Tu peux trouver et analyser tes données de trafic organique en toute simplicité à l'aide d'un outil comme [Organic Traffic Insights](https://www.semrush.com/organic_traffic_insights/) de Semrush.

Pour commencer, entre ton domaine dans la barre de recherche. Puis clique sur " **Obtenir des informations** ".

![Barre de recherche Organic Traffic Insights](https://static.semrush.com/blog/uploads/media/7b/fa/7bfae928ae4c64b8d5e7cdc4fc498d29/5e1a8152bea817c779121dd390893a41/original.png)

Barre de recherche Organic Traffic Insights

Ensuite, connecte tes comptes Google Analytics et Google Search Console à Semrush. Cette étape est importante pour combiner toutes tes données de trafic organique en un seul endroit. Et pour découvrir tous les mots-clés qui conduisent les chercheurs vers ton site.

Pour ce faire, clique sur " **Connecter un compte Google** " et suis les instructions de configuration.

!["Connecter ton compte Google" étape dans les paramètres de Organic Traffic Insights.](https://static.semrush.com/blog/uploads/media/e5/6d/e56d637f468a9e2648adfe5a9cc41427/aea21b87e76cb3009dd568ca64208fb4/original.png)

"Connecter ton compte Google" étape dans les paramètres de Organic Traffic Insights.

Après avoir terminé le processus de configuration, regarde la colonne "Sessions" pour trouver des données importantes sur le trafic organique, notamment les "Sessions engagées" et le "Temps d'engagement moyen."

!["Sessions" colonnes mises en évidence dans le rapport "Pages d'atterrissage" dans Organic Traffic Insights.](https://static.semrush.com/blog/uploads/media/4c/f4/4cf49a2765d463ad9d3de0fa2c102689/a68692ec9ae3d4d2686bbd14a37c861a/original.jpeg)

"Sessions" colonnes mises en évidence dans le rapport "Pages d'atterrissage" dans Organic Traffic Insights.

En utilisant à la fois les données sur les pages vues et Organic Traffic Insights pour analyser ton site Web, tu auras une vue d'ensemble granulaire des performances des pages. Et cela permet de mettre en lumière les problèmes potentiels.

Par exemple, une page avec beaucoup de sessions mais un temps d'engagement moyen faible pourrait signifier que la page ne capte pas l'attention des utilisateurs.

Tu peux également analyser les données relatives aux mots-clés dans l'outil. Cela t'aidera à comprendre quelles requêtes de recherche sont responsables de l'envoi du trafic organique vers tes pages les plus populaires.

Comme Organic Traffic Insights rassemble toutes tes données de mots-clés en un seul endroit, tu peux explorer à la fois les données de Semrush et celles de Google Search Console à partir d'un seul tableau de bord.

Clique sur le nombre de mots-clés dans la colonne de gauche pour accéder au rapport Semrush.

![Colonne "Semrush" mise en évidence dans le tableau "Pages d'atterrissage".](https://static.semrush.com/blog/uploads/media/db/be/dbbe70c62c4dac3a4f7f1264bdf99787/635f9e7fc16466553eb0ea27cf83eb83/original.jpeg)

Colonne "Semrush" mise en évidence dans le tableau "Pages d'atterrissage".

Tu verras une liste des principaux mots-clés pour lesquels ta page se classe et sa position dans la recherche. Il répertorie également la part de trafic pour chaque mot-clé, indiquant la proportion du trafic de cette page qui provient de mots-clés spécifiques.

![Une liste des principaux mots-clés, avec les colonnes "Position" et "Part de trafic" en surbrillance.](https://static.semrush.com/blog/uploads/media/d5/22/d522612d135c6982a0860947f47398f6/cd5c9fddd195f5cbc3fe23542c624c37/original.jpeg)

Une liste des principaux mots-clés, avec les colonnes "Position" et "Part de trafic" en surbrillance.

Ces données peuvent fournir un moyen simple de comprendre quels sont les mots-clés qui génèrent des pages vues pour ton contenu. Tu peux utiliser ces informations pour optimiser davantage chaque page pour tes mots-clés cibles, tout en les suivant au fil du temps dans l'outil.

Analyze Bounce Rate, Sessions, and More

with the Organic Traffic Insights Tool

[Try for Free](https://fr.semrush.com/organic_traffic_insights/)

### Trouve les pages qui perdent des vues

Le suivi des pages vues dans GA4 te permet également de voir facilement quelles pages perdent du trafic au fil du temps. C'est utile car tu peux rapidement identifier les pages que tu pourrais vouloir mettre à jour.

Dirige-toi vers le rapport sur les pages et les écrans que nous avons décrit dans la section précédente.

Dans le coin supérieur droit, tu trouveras une plage de dates. Ici, il est réglé pour afficher les données des 28 derniers jours.

![Une plage de dates indiquant "9 janvier - 5 février 2024" dans le coin supérieur droit.](https://static.semrush.com/blog/uploads/media/63/1a/631a5fd754d3f212de15bac91496c88b/63242a57946d1835649be8ff1a8b39dd/original.png)

Une plage de dates indiquant "9 janvier - 5 février 2024" dans le coin supérieur droit.

Clique sur la date pour faire apparaître une fenêtre dans laquelle tu peux personnaliser les dates. Clique sur la bascule à côté de " **Comparer** ". Cela réglera automatiquement la date de comparaison sur les 28 jours précédents.

N'hésite pas à personnaliser cette fourchette pour qu'elle corresponde à ton analyse. Quand tu as terminé, clique sur " **Appliquer** ".

![Personnalise la fenêtre des dates](https://static.semrush.com/blog/uploads/media/46/27/46270d4de7ff8c41a6412d6476890baf/cd963362a6aa3c869899836a12690b2f/original.jpeg)

Personnalise la fenêtre des dates

Le tableau de bord mis à jour contiendra désormais deux ensembles de données: bleu foncé pour la période la plus récente et bleu clair pour la période précédente.

![Un graphique dans les pages et le rapport des écrans contenant deux ensembles de données, affichés en bleu foncé et en bleu clair.](https://static.semrush.com/blog/uploads/media/32/d9/32d9b9323e14896c195505244a3f2924/c12cd884eaf707799afb66e6931367a4/original.jpeg)

Un graphique dans les pages et le rapport des écrans contenant deux ensembles de données, affichés en bleu foncé et en bleu clair.

Fais défiler le tableau pour voir si les pages vues ont augmenté ou diminué par rapport à la période précédente pour chaque chemin de page.

![Un tableau dans un rapport de pages et d'écrans contenant deux ensembles de données.](https://static.semrush.com/blog/uploads/media/b3/60/b3600d1c52cfea8513081108b50564ec/ac4db3a1fef126364fcbd867e0b79c60/original.jpeg)

Un tableau dans un rapport de pages et d'écrans contenant deux ensembles de données.

Tu peux utiliser la barre de recherche pour taper un mot ou une URL afin d'isoler les données sur les vues d'une page ou d'un groupe de pages spécifique.

![Recherche "/Google+Redesign/Apparel" dans le rapport](https://static.semrush.com/blog/uploads/media/d7/6e/d76e46cc5be4f2703ba171b874309c41/d38de19f4b5e897fb8bb192c149e4971/original.jpeg)

Recherche "/Google+Redesign/Apparel" dans le rapport

Si tu ne veux voir que le pourcentage de variation dans le temps, clique sur l'option " **Afficher toutes les lignes** " puis sélectionne " **Afficher le % de variation** ".

![L'option "Show % Change" est sélectionnée dans le menu déroulant "Show All Rows".](https://static.semrush.com/blog/uploads/media/42/de/42de585e1a1042d2ab4dc333dcc2649a/7fb69d191538e5fc11a9151aff4f8186/original.jpeg)

L'option "Show % Change" est sélectionnée dans le menu déroulant "Show All Rows".

C'est pratique pour identifier rapidement les pages qui ont perdu un trafic important au fil du temps. Dans l'exemple ci-dessous, la deuxième ligne se distingue par le fait que ses vues ont chuté de 77,69 %.

Il pourrait être intéressant d'analyser cette page pour comprendre les raisons d'un tel déclin. Et la mettre à jour si nécessaire.

![La colonne "Views" du deuxième résultat est mise en évidence, montrant une baisse de 77,69 % des vues.](https://static.semrush.com/blog/uploads/media/55/e1/55e176def73bb136018bcfbd2146a01e/54e475abea60bb7be9dec6d2155bef41/original.jpeg)

La colonne "Views" du deuxième résultat est mise en évidence, montrant une baisse de 77,69 % des vues.

Lorsque tu trouves des pages que tu veux mettre à jour pour augmenter leur nombre de pages vues, tu peux stimuler tes efforts avec un outil comme le [vérificateur de référencement sur la page de](https://www.semrush.com/on-page-seo-checker/) Semrush.

Il analysera tes pages Web et identifiera les faiblesses en matière de référencement qui peuvent avoir un impact sur les performances de ton contenu dans la recherche. Ensuite, tu recevras des recommandations sur mesure pour les corriger rapidement et favoriser l'augmentation de ton trafic.

Commence par saisir ton [nom de domaine](https://www.semrush.com/blog/changing-domain-name-seo/) dans la barre de recherche et clique sur " **Obtenir des idées** ". (Si tu as déjà utilisé l'outil, tu devras plutôt cliquer sur " **\+ Créer un projet** ").

![Barre de recherche On Page SEO Checker](https://static.semrush.com/blog/uploads/media/18/be/18be333dd5e3ebeff6bb7af57690d0a7/9f2095e0ff99b761081ae7302ce9f835/original.png)

Barre de recherche On Page SEO Checker

Ensuite, sélectionne ton emplacement cible et clique sur " **Continuer** ".

![Fenêtre "Sélectionner l'emplacement cible" dans les paramètres de On Page SEO Checker.](https://static.semrush.com/blog/uploads/media/05/6e/056e37bfe910c4c838c7e1aa83e5f2a2/58bcf714f1ae094ae5cbbc69274768f4/original.png)

Fenêtre "Sélectionner l'emplacement cible" dans les paramètres de On Page SEO Checker.

Ajoute les pages que tu veux optimiser. Semrush génère automatiquement une liste pour toi, mais tu peux aussi importer un fichier CSV, ou utiliser les données de Google Search Console (GSC) ou d'Organic Rankings.

Quand tu es prêt, clique sur " **Recueillir des idées** ".

![Fenêtre "Ajouter des pages à optimiser" dans les paramètres de On Page SEO Checker.](https://static.semrush.com/blog/uploads/media/26/fd/26fde8fecde62def50848ec31c9b03b1/db5990223fec7b4a73c2361988d75f72/original.png)

Fenêtre "Ajouter des pages à optimiser" dans les paramètres de On Page SEO Checker.

Lorsque ton tableau de bord est prêt, clique sur l'onglet " **Idées d'optimisation** " pour explorer les suggestions.

!["Idées d'optimisation" onglet mis en évidence dans le vérificateur de référencement sur la page.](https://static.semrush.com/blog/uploads/media/bd/c5/bdc5576a39eca2364dfee8f76f40ed20/09a79e4f2864e8cf05137279ff3ea21a/original.jpeg)

"Idées d'optimisation" onglet mis en évidence dans le vérificateur de référencement sur la page.

Clique sur les **boutons bleus** de la colonne "Toutes les idées" pour voir les suggestions d'optimisation pour chaque page.

![Le bouton "7 idées" est surligné à côté du résultat "www.nasa.gov" sous l'onglet "Idées d'optimisation".](https://static.semrush.com/blog/uploads/media/85/81/85813aacac29aa754e7a8c8bd9a27647/36d065da17ccd4ae50e0e4dc340b1c3f/original.jpeg)

Le bouton "7 idées" est surligné à côté du résultat "www.nasa.gov" sous l'onglet "Idées d'optimisation".

Dans cet exemple, les suggestions de contenu comprennent l'amélioration de la lisibilité et l'ajout de mots-clés cibles à différentes parties de la page. Tu peux cliquer sur le bouton "Voir l'analyse détaillée" pour en savoir plus sur chaque recommandation.

![Une section de suggestions de "contenu" dans On Page SEO Checker](https://static.semrush.com/blog/uploads/media/aa/63/aa63a889139de184d5e2b7a3165f299d/f7637351ac07c0ab8529b9189ebe6df2/original.png)

Une section de suggestions de "contenu" dans On Page SEO Checker

Maintenant, tu es prêt à mettre en œuvre ces idées d'optimisation pour améliorer ton classement dans les moteurs de recherche et attirer plus de visiteurs sur ton site.

Find Out What Ranks

with the Topic Research Tool

[Try for Free](https://www.semrush.com/on-page-seo-checker/)

## Amplifie ton analyse des pages vues avec Semrush

Les données sur les pages vues sont essentielles pour analyser et améliorer les performances de ton site Web.

Et grâce aux outils de Semrush tels que [Organic Traffic Insights](https://www.semrush.com/organic_traffic_insights/) et le [On Page SEO Checker](https://www.semrush.com/on-page-seo-checker/), tu peux obtenir des [informations](https://www.semrush.com/blog/seo-insights/) et des conseils précieux en [matière de référencement](https://www.semrush.com/blog/seo-insights/) pour aller plus loin dans ton analyse.

Inscris-toi pour [un essai gratuit](https://www.semrush.com/signup/get-free-trial/) aujourd'hui.

Accède à tout ce dont tu as besoin

sur une seule plateforme avec Semrush