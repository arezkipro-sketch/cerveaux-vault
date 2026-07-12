---
title: "Comment connecter Google Search Console à Google Analytics 4"
source: "https://fr.semrush.com/blog/comment-connecter-google-search-console-a-google-analytics/"
author:
  - "[[Zack Duncan]]"
published: 2025-05-13
created: 2026-06-15
description: "Apprends à connecter Google Search Console à GA4 pour analyser tes principales requêtes de recherche et pages d'atterrissage."
tags:
  - "clippings"
---
Nous avons traduit cet article de l'anglais. [Clique ici](https://www.semrush.com/blog/connect-google-search-console-analytics/) pour lire l'article original. Si tu remarques des problèmes dans le contenu, n'hésite pas à nous contacter à [report-osteam@semrush.com](mailto:report-osteam@semrush.com).

Tu peux connecter Google Search Console à Google Analytics 4 (GA4) pour obtenir des données de recherche organique dans ta propriété GA4.

L'intégration étend le niveau de détail que tu peux obtenir de Google Analytics. Une fois que les deux plateformes sont connectées, tu obtiendras des données de performance et de classement pour des requêtes de recherche spécifiques et des pages d'atterrissage. Tout au même endroit.

Dans ce guide, tu apprendras comment connecter les deux plateformes. Et comment tirer le meilleur parti des rapports intégrés.

## Pourquoi devrais-tu connecter Search Console à Google Analytics?

Google Search Console (GSC) t'aide à mesurer [la performance de recherche organique](https://www.semrush.com/blog/organic-traffic/) dans Google. Pour que tu puisses découvrir des opportunités SEO pour ton site.

Tu peux connecter GSC à Google Analytics pour obtenir ces données de performance de recherche organique dans ta propriété GA4. Où tu peux l'utiliser pour des tâches SEO courantes telles que:

- Partager des rapports détaillés avec les parties prenantes
- Générer de nouvelles idées de contenu
- Prioriser les pages nécessitant une mise à jour du contenu

### Les données que tu obtiens lorsque tu connectes Search Console à Google Analytics

Le rapport "Résultats de recherche" dans GSC affiche des données pour quatre indicateurs de performance clés:

1. **Clics totaux**: Le nombre de clics vers ton site provenant de la recherche organique de Google
2. **Impressions totales**: Le nombre de fois que tes pages sont apparues dans les résultats de recherche Google
3. **CTR moyen**: Le nombre de clics divisé par le nombre d'impressions (multiplié par 100 pour obtenir un pourcentage)
4. **Position moyenne**: La position moyenne où tes résultats de recherche sont apparus sur Google (sur toutes les impressions)
![Performance sur les métriques et le graphique des résultats de recherche dans GSC](https://static.semrush.com/blog/uploads/media/6d/72/6d72088245822ee64e68ada5ed72a88f/218c3d4065fb5182d72c299688891507/original.png)

Performance sur les métriques et le graphique des résultats de recherche dans GSC

Par défaut, le rapport "Résultats de recherche" affichera un graphique des **clics totaux** et des **impressions totales**. Tu peux visualiser différentes métriques en cliquant sur n'importe laquelle des quatre métriques.

Par exemple, voici ce que tu verras lorsque tu désactives les clics et les impressions et actives **la position moyenne**:

![Performance sur le graphique des résultats de recherche dans GSC, montrant les données de position moyenne](https://static.semrush.com/blog/uploads/media/ca/28/ca28ce87fe4846f23a831482ff7623d5/a66f0ebf0e24aeb3d4d31d61691d44dd/original.png)

Performance sur le graphique des résultats de recherche dans GSC, montrant les données de position moyenne

Ces métriques fournissent une vue agrégée de ta performance. Search Console fournit des informations au niveau des requêtes sur les mêmes quatre métriques de performance.

Les requêtes sont les termes de recherche spécifiques que les visiteurs ont tapés dans Google avant de trouver ton site (c'est-à-dire, les mots-clés). Voici un exemple montrant les principales requêtes de recherche.

![Section "Requêtes" du rapport Performance sur les résultats de recherche dans GSC](https://static.semrush.com/blog/uploads/media/81/09/8109f06f108e3a6d751e068c92e2e058/1e87c1cc6361a1092e85f31084ed9686/original.png)

Section "Requêtes" du rapport Performance sur les résultats de recherche dans GSC

À lui seul, Google Analytics ne peut pas afficher ces données granulaires au niveau des mots-clés.

### Pourquoi Google Analytics a besoin des données de Search Console

Google Analytics est un outil gratuit de [web analytics](https://www.semrush.com/blog/web-analytics/) qui peut t'aider à comprendre la performance de ton site Web et les visiteurs qui y viennent.

Comme où ils vivent, à quelle fréquence ils visitent, comment ils arrivent, et ce qu'ils font sur le site.

![Un tableau de bord dans Google Analytics montrant les informations sur les visiteurs du site Web](https://static.semrush.com/blog/uploads/media/6d/c7/6dc7e7e758d8c859cc6963cb8addbc4f/1c80aa052ed277f2093ec3c741d32859/original.png)

Un tableau de bord dans Google Analytics montrant les informations sur les visiteurs du site Web

Mais sans connecter Google Search Console à Google Analytics, tu ne pourras pas voir ces données de requêtes si importantes aux côtés de tes métriques de comportement des utilisateurs.

Alors découvrons comment combiner les deux plateformes.

## Comment connecter Google Search Console à Google Analytics

Tu auras besoin d'un accès de niveau éditeur à ta propriété Google Analytics 4 avant de commencer.

### 1\. Vérifie ta propriété Google Search Console

Tu dois être un propriétaire vérifié de ta propriété Google Search Console pour la lier à ta propriété GA4.

Tu peux vérifier la propriété de différentes manières selon la façon spécifique dont tu l'as configurée. Ceci inclut la vérification via des balises HTML ou en ajoutant un enregistrement TXT via ton fournisseur DNS (système de noms de domaine).

Pour un guide complet sur la configuration de GSC si tu ne l'as pas déjà fait, consulte notre [tutoriel Google Search Console](https://www.semrush.com/blog/google-search-console/).

### 2\. Va dans Google Analytics et accède à 'Liens Search Console'

Connecte-toi à [Google Analytics](https://analytics.google.com/) en utilisant le même compte Google que tu utilises pour Google Search Console.

À partir de l'écran d'accueil, clique sur l'icône de réglage en bas à gauche pour accéder à la section “ **Admin** ”.

![Navigation vers la section admin de Google Analytics](https://static.semrush.com/blog/uploads/media/1e/b1/1eb16fca4b076be834e4c96894af5340/a0606d495e3465339d52c211bb9ff9a5/original.png)

Navigation vers la section admin de Google Analytics

Clique sur “ **Liens produits** ” sous tes “Paramètres de propriété.”

Fais défiler vers le bas et clique sur “ **Liens Search Console**.”

![Section "Liens Search Console" dans l'Admin de Google Analytics](https://static.semrush.com/blog/uploads/media/f5/fa/f5fae000d50602a51cd222651873703a/8314b8ef1d88fa1af40458900a40a0da/original.png)

Section "Liens Search Console" dans l'Admin de Google Analytics

### 3\. Choisis ta propriété Search Console à lier

Sur l'écran “Liens Search Console”, clique sur le bouton “ **Lier** ” du côté droit.

Tu ne pourras lier une propriété Search Console à une seule propriété GA4.

![Bouton "Lier" mis en évidence dans la section "Liens Search Console"](https://static.semrush.com/blog/uploads/media/60/7d/607d5ec5e234c9eeb28db8d9aec6b333/23f744af6b18ef3a46a81a4a7a6a85d0/original.png)

Bouton "Lier" mis en évidence dans la section "Liens Search Console"

Tu verras une page de configuration de lien comme celle ci-dessous.

Clique sur “ **Choisir des comptes** ” pour voir une liste de propriétés Search Console. Tu verras toutes les propriétés pour lesquelles ton adresse e-mail est un propriétaire vérifié.

![Option "Lier aux propriétés Search Console que je gère" sélectionnée sur la page de configuration de "Lier"](https://static.semrush.com/blog/uploads/media/0d/71/0d71eb87225019ade88e01045c59a2bf/0609c64cd5be628defef9a2dc40b6332/original.png)

Option "Lier aux propriétés Search Console que je gère" sélectionnée sur la page de configuration de "Lier"

Trouve ta propriété et sélectionne-la en utilisant la case à cocher à gauche du “Nom de propriété.” Ensuite, clique sur “ **Confirmer**.”

![Sélectionne la propriété GSC que tu souhaites connecter à Google Analytics](https://static.semrush.com/blog/uploads/media/52/89/528908d333a8f023cb61ce7a51aaeb27/27173bfde046dd97302946f5cf5c97a7/original.png)

Sélectionne la propriété GSC que tu souhaites connecter à Google Analytics

### 4\. Associe ta propriété Search Console à ton flux de données web GA4

Ensuite, tu associeras ta propriété Search Console à ton flux de données web Google Analytics.

Un flux de données est l'endroit d'où proviennent tes données Google Analytics. Google Analytics 4 a trois types de flux de données:

1. **application iOS**
2. **application Android**
3. **Web**

Tu ne peux connecter Google Search Console qu'à un flux web Google Analytics 4 (c'est-à-dire, pour un site web, pas une application). Cliquez sur « **Suivant** ».

![Bouton "Suivant" mis en évidence sous la page "Configuration de lien"](https://static.semrush.com/blog/uploads/media/93/3c/933cc3b06e77105243fcd96381cdcde4/2861e53aa393d68ddc9a3e3f9559be1c/original.png)

Bouton "Suivant" mis en évidence sous la page "Configuration de lien"

Ensuite, clique sur “ **Sélectionner** ” pour choisir ton flux de données web Google Analytics.

![Étape 2 "Sélectionner le flux web" mise en évidence sous la page "Configuration de lien"](https://static.semrush.com/blog/uploads/media/1a/50/1a5017481ccc8a5930013c7630642437/efea8715d806d5571a1b4959d2a50018/original.png)

Étape 2 "Sélectionner le flux web" mise en évidence sous la page "Configuration de lien"

Tu verras le flux de données web pertinent dans ta propriété GA4. Cliquez dessus.

Clique à nouveau sur “ **Suivant** ”.

![Sélectionne le flux web et clique sur "Suivant"](https://static.semrush.com/blog/uploads/media/16/5b/165bbbbc92b54d0351ec395932ac8f75/32fe4ed47a5c07a5d546c94f4c1b64e6/original.png)

Sélectionne le flux web et clique sur "Suivant"

### 5\. Examine et soumets ton lien Search Console

Tu verras un écran de révision final comme celui ci-dessous.

Clique sur “ **Soumettre** ” pour compléter l'intégration de Search Console.

![Bouton "Soumettre" mis en évidence sous la page "Configuration de lien"](https://static.semrush.com/blog/uploads/media/a4/a1/a4a193df83e640c78f12152f52f69947/a7d47127a347681406a5bf827e639a8f/original.png)

Bouton "Soumettre" mis en évidence sous la page "Configuration de lien"

### 6\. Publie tes rapports

Tu dois publier tes rapports Search Console afin de pouvoir les trouver dans la zone “Rapports” de la navigation à gauche dans GA4.

Pour ce faire, clique sur “ **Rapports**.”

![Zone "Rapports" dans la navigation à gauche de GA4](https://static.semrush.com/blog/uploads/media/0a/a1/0aa1ff33324aa32f526fe9a2e4b2b294/a9f51e43452304e27a1232f9795fc0a6/original.png)

Zone "Rapports" dans la navigation à gauche de GA4

Ensuite, clique sur “ **Bibliothèque** ” pour accéder à tes rapports disponibles.

!["Bibliothèque" sélectionnée dans la barre latérale de GA4](https://static.semrush.com/blog/uploads/media/ba/17/ba17b39b1a8a2c92ac55e1fdd6713700/84aacc0a84fc71f4d4959681d0c228c6/original.png)

"Bibliothèque" sélectionnée dans la barre latérale de GA4

Tu verras “ **Search Console** ” dans ta “Collection.” Cela peut afficher un statut “Non publié”. (S'il apparaît comme “Publié”, Google a déjà fait le travail pour toi, et tu n'as rien à faire ici.)

Clique sur l'icône verticale à trois points.

![Widget "Search Console" mis en évidence dans la section “Collection" sous la page "Bibliothèque"](https://static.semrush.com/blog/uploads/media/fe/24/fe242f65899ce9a7868dd49d55b7768b/35c302801ebda71f0339b087f8f4c463/original.png)

Widget "Search Console" mis en évidence dans la section “Collection" sous la page "Bibliothèque"

Puis, cliquez sur « **Publier** ».

![Option "Publier" sélectionnée dans le menu déroulant "Search Console"](https://static.semrush.com/blog/uploads/media/c9/04/c9046da95c5188c4ac4b00a78990e0d7/92fb95f0e685c4e8641affc40ae5b653/original.png)

Option "Publier" sélectionnée dans le menu déroulant "Search Console"

Maintenant que tu as connecté GSC et GA4, voyons comment tu peux utiliser tes nouvelles données.

## Comment utiliser les rapports de la Search Console dans GA4

Tes données de Search Console apparaissent dans deux rapports différents dans GA4:

- Rapport sur les requêtes
- Rapport sur le trafic de recherche organique de Google

Tu peux maintenant trouver ces deux rapports en cliquant sur " **Rapports** " dans la navigation principale à gauche.

![« Rapports » sélectionné dans la navigation à gauche de GA4](https://static.semrush.com/blog/uploads/media/03/e7/03e72c785a5bf5fcd60f800c8ac08715/9b15a87570b908353c1dfeb55cdf5693/original.png)

« Rapports » sélectionné dans la navigation à gauche de GA4

Tu verras ta section « **Search Console** » en dessous de tes rapports « Cycle de vie ». Clique dessus pour développer les rapports individuels.

![Section « Search Console » mise en surbrillance sous les rapports « Cycle de vie » dans GA4](https://static.semrush.com/blog/uploads/media/da/e6/dae623b84572982fb29d9e8cb04811a1/f65e06e1500400bc75875541649cf3cf/original.png)

Section « Search Console » mise en surbrillance sous les rapports « Cycle de vie » dans GA4

Tu verras à la fois le rapport « Requêtes » avec des données au niveau des mots-clés, et le « rapport sur le trafic de recherche organique de Google », qui contient des données sur les pages d'atterrissage.

Commençons par examiner le rapport sur les requêtes.

### Rapport sur les requêtes de la Search Console

Le rapport sur les requêtes te dit quels sont les termes de recherche spécifiques que tes visiteurs ont saisis dans Google avant de trouver ton site.

Il peut t'aider à mieux comprendre les besoins de tes visiteurs. Et suivre comment ton site se classe sur Google pour les mots-clés individuels qu'ils recherchent.

Tu peux aussi identifier les pages où tes classements diminuent. Cela peut être de très bons endroits pour [mettre à jour tes efforts SEO](https://www.semrush.com/blog/on-page-seo/).

Le rapport montre les mêmes quatre métriques que nous avons examinées précédemment dans cet article, bien que sous des noms légèrement différents:

1. **Clics organiques de recherche Google**
2. **Impressions organiques de recherche Google**
3. **Taux de clics organiques de recherche Google**
4. **Position moyenne de recherche organique de Google**

Par défaut, tu verras tes 10 premières requêtes de recherche organiques Google classées par le nombre de clics que chacune a reçus dans la période donnée.

Tu peux cliquer sur la flèche déroulante à droite de "Lignes par page" pour afficher plus de requêtes.

![Rapport de requêtes organiques de recherche Google montré dans GA4](https://static.semrush.com/blog/uploads/media/57/b8/57b8279f03333a051dc0f6bdc1b651fb/cfe4e0a4cb193703b2f72c8ddc223e69/original.png)

Rapport de requêtes organiques de recherche Google montré dans GA4

À lui seul, le rapport fournit un instantané de la performance de recherche organique de Google de ton site. Tu peux utiliser le sélecteur de plage de dates pour analyser ta performance dans le temps.

![Le sélecteur de plage de dates mis en surbrillance dans le coin supérieur droit du rapport de requêtes : rapport de requêtes organiques de recherche Google](https://static.semrush.com/blog/uploads/media/97/75/977545c7952f986949b903155e7a532e/b6278b7f93bdf48b89932822c2d14448/original.png)

Le sélecteur de plage de dates mis en surbrillance dans le coin supérieur droit du rapport de requêtes: rapport de requêtes organiques de recherche Google

Par défaut, tu verras les données des 28 derniers jours. Tu peux obtenir des informations plus détaillées en ajoutant une comparaison à ta plage de dates.

Par exemple, tu pourrais vouloir comparer ta performance récente à celle de la période de 28 jours précédente.

Utilise le bascule « **Comparer** » pour ajouter une comparaison de plage de dates.

La comparaison par défaut est celle de la période immédiatement précédente. Dans notre cas, les 28 jours précédant la période de 28 jours la plus récente. Tu peux faire une analyse annuelle ou utiliser une période personnalisée.

Nous allons utiliser la comparaison par défaut. Cliquez sur « **Appliquer** ».

![Configuration de l'option de comparaison par défaut sous la fenêtre du sélecteur de plage de dates](https://static.semrush.com/blog/uploads/media/f9/91/f991ac8304c0ccda8772fa9b55fb4bd2/37335f4e5757a6d59c49f88f6ab25068/original.png)

Configuration de l'option de comparaison par défaut sous la fenêtre du sélecteur de plage de dates

Tu verras trois rangées pour chacune de tes requêtes de recherche:

- Ta plage horaire principale
- Ta plage horaire de comparaison
- Le pourcentage de changement dans le temps

La troisième requête de recherche se distingue dans cet exemple:

![Rapport de requêtes de recherche organiques de Google dans GA4, montrant la comparaison pour la plage de dates sélectionnée](https://static.semrush.com/blog/uploads/media/14/b6/14b6ea2c56d852402f71a82e3096e3a7/f02d363b9bb05e19da98058db547f85a/original.png)

Rapport de requêtes de recherche organiques de Google dans GA4, montrant la comparaison pour la plage de dates sélectionnée

Tu remarqueras que c'est l'un des meilleurs performeurs en termes de clics du site malgré son faible taux de clics. Il représente presque la moitié de toutes les impressions organiques de recherche Google du site (473 990 sur 958 562).

Les clics ont également augmenté de 9,55 %, malgré la baisse des classements pendant cette période (passant d'une position moyenne de 6,19 à 6,35).

Cela indique que l'intérêt pour cette recherche augmente, mais la page n'est probablement pas bien optimisée. Ce que nous pouvons déduire du faible taux de clics et de la chute des classements.

Il pourrait être judicieux de revoir ce contenu pour voir si tu peux l'optimiser davantage pour cette requête de recherche et augmenter ton trafic organique. Et tu peux utiliser Semrush pour t'aider avec cela.

Dans cet exemple, nous allons utiliser l' [outil Vue d’ensemble des mots clés](https://www.semrush.com/analytics/keywordoverview/) pour en apprendre davantage sur le mot-clé « emoji kitchen ».

Saisis ton mot-clé dans le champ vide. Puis, cliquez sur « **Recherche** ».

![Mot-clé "emoji kitchen" saisi dans l'outil Vue d’ensemble des mots clés](https://static.semrush.com/blog/uploads/media/01/a2/01a215125b8d063b4c1d11246bfcbe10/59d18a653a1056b53aecb81f09bb59b9/original.png)

Mot-clé "emoji kitchen" saisi dans l'outil Vue d’ensemble des mots clés

Tu obtiendras alors des métriques utiles concernant le mot-clé. Dans ce cas, deux informations sont particulièrement intéressantes:

- Le volume (le nombre moyen de recherches mensuelles) est de 135k aux États-Unis, mais si tu regardes le « Volume global », tu vois qu'il y a trois autres pays qui ont au moins ce niveau d'intérêt de recherche
- La tendance montre l'intérêt estimé pendant les 12 mois précédents (l'intérêt pour cela a récemment explosé).
![Résultats de l'outil Vue d’ensemble des mots clés pour "emoji kitchen" avec les métriques "Volume," "Volume global," et "Tendance" mises en surbrillance](https://static.semrush.com/blog/uploads/media/c3/30/c3301591810defe229c84b0b40b3428c/01a793bd58932e24e4c684f1598f1ac3/original.png)

Résultats de l'outil Vue d’ensemble des mots clés pour "emoji kitchen" avec les métriques "Volume," "Volume global," et "Tendance" mises en surbrillance

Tu ne sais pas à quoi ressemblera la tendance future. Mais si tu optimises pour le mot-clé maintenant, tu seras mieux placé pour capturer une plus grande part de clics si cette tendance se poursuit.

Et tu pourrais vouloir envisager d'optimiser pour la recherche en Turquie, en Inde et au Japon, où le volume de recherche est égal ou supérieur à celui des États-Unis. pour ce terme.

La section « Idées de mots-clés » du rapport peut fournir des idées pour optimiser davantage ta page existante.

Une façon simple de le faire est d'utiliser les données « Questions ». Ce sont des questions de recherche qui incluent une variante de ton mot-clé.

![« Widget Questions » dans l'outil Vue d’ensemble des mots clés montrant les questions de recherche qui incluent une variante du mot-clé "emoji kitchen"](https://static.semrush.com/blog/uploads/media/ba/ec/baec478d1c3ee290db86f747720daeae/f8e14a01dd7b4dab2353f92e7117e51a/original.png)

« Widget Questions » dans l'outil Vue d’ensemble des mots clés montrant les questions de recherche qui incluent une variante du mot-clé "emoji kitchen"

Tu pourrais utiliser ces termes pour ajouter une section FAQ au bas de ta page afin de répondre à ces questions spécifiques. Cela pourrait aider ta page à bien se classer pour ces mots-clés associés, tout en apportant une valeur ajoutée à tes lecteurs.

Obtenir des informations précieuses sur les mots-clés

avec l'outil Vue d’ensemble des mots clés

[Essaie gratuitement](https://www.semrush.com/analytics/keywordoverview/)

### Rapport sur le trafic de recherche organique de Google

Le rapport sur le trafic de recherche organique te parle de tes meilleures pages d'atterrissage dans la recherche organique de Google.

Il utilise les mêmes quatre métriques que le rapport sur les requêtes et les combine avec plus de métriques de Google Analytics. Ces métriques GA4 te donnent des informations telles que le taux d'engagement de chaque page, et le nombre d' [événements GA4](https://www.semrush.com/blog/google-analytics-4-events/) suivis sur chaque page.

![Un rapport dans GA4 montrant "Page d'atterrissage + chaîne de requête"](https://static.semrush.com/blog/uploads/media/75/5d/755d248db514ae09540ad140409d3bf2/7ceedb7bb589d77c732eee30aec33b5b/original.png)

Un rapport dans GA4 montrant "Page d'atterrissage + chaîne de requête"

La cinquième page d'atterrissage de la liste semble être la page où le mot-clé "emoji kitchen" se classe. Le « Taux d'engagement » pour cette page (42,47 %) se distingue car il est beaucoup plus bas que la moyenne de toutes les pages (64,32 %).

Le taux d'engagement est le pourcentage de sessions où un visiteur a satisfait au moins une des conditions suivantes:

- Avoir consulté plus d'une page
- S'être engagé activement avec la page pendant au moins 10 secondes
- Avoir complété une conversion (comme acheter quelque chose ou remplir un formulaire)

Le faible taux d'engagement nous indique que ce type de visites précieuses se produit moins fréquemment sur cette page. Cela suggère que tu pourrais vouloir mettre à jour cette page pour la rendre plus utile pour tes lecteurs.

## Pousse tes données de recherche organique plus loin avec Semrush

Obtiens des informations utiles sur les mots-clés aux côtés de tes données de Google Search Console et Google Analytics, le tout en un seul endroit avec Semrush.

[Les insights sur le trafic organique](https://www.semrush.com/organic_traffic_insights/) combinent trois sources d'informations importantes:

- Données de Google Search Console et Google Analytics pour tes meilleures pages d'atterrissage
- Données de conversion de Google Analytics pour que tu puisses voir lesquelles de ces pages génèrent le plus de conversions
- Idées de mots-clés alimentées par Semrush pour que tu puisses trouver des moyens de générer plus de trafic et d'obtenir plus de conversions
![Rapport sur le "Trafic de recherche organique" dans l'outil Insights sur le trafic organique](https://static.semrush.com/blog/uploads/media/b0/1d/b01d7784da55a4b69fa5c0fa99bd6a9d/722179ca900a493b1227307b7078d7b5/original.png)

Rapport sur le "Trafic de recherche organique" dans l'outil Insights sur le trafic organique

Regarde la deuxième page d'atterrissage de la liste. Elle représente plus de 35 % de toutes tes conversions de recherche organique (41 sur 116) et 2,4 % de toutes les sessions pour cette page se traduisent par une conversion (41 sur 1 708). Tu vois aussi que tes sessions et tes conversions diminuent.

Tu veux utiliser les données de mots-clés pour trouver des opportunités afin d'améliorer tes classements et de générer plus de trafic. Pour ce faire, clique sur le numéro hyperlié (129 dans ce cas) pour afficher les mots-clés de Semrush qui génèrent du trafic vers cette page.

![Section "Pages d'atterrissage" du rapport sur le trafic de recherche organique](https://static.semrush.com/blog/uploads/media/5d/4b/5d4b29d9862b662ed6a238d4bd567d15/a4416a52cbc5bb51e1507f50252fb95e/original.png)

Section "Pages d'atterrissage" du rapport sur le trafic de recherche organique

Cela te mènera à une page montrant des mots-clés ainsi que divers métriques pour chacun, y compris deux que Google Search Console ne montre pas:

1. Volume (nombre estimé de recherches mensuelles)
2. Difficulté du mot clé (une estimation de la difficulté à bien se classer pour chaque mot clé dans les résultats de recherche organique)

Tu peux utiliser ces deux métriques pour trouver de nouveaux mots clés à cibler. Tu te concentres sur le cinquième mot clé de la liste, "utilisateurs actifs ga4".

![Les mots clés "utilisateurs actifs ga4" mis en évidence dans le tableau des mots clés Semrush](https://static.semrush.com/blog/uploads/media/77/5d/775d55cd275bbc0f200361fb6ab8d3ac/4a48d765651fd00558b56edc15ca9ee5/original.png)

Les mots clés "utilisateurs actifs ga4" mis en évidence dans le tableau des mots clés Semrush

Tu vois qu'il a une difficulté de mot clé de 20 %, ce qui est inférieur à celui des mots clés pour lesquels tu es déjà classé en première position sur Google. Pourtant, ta page n'est classée qu'à la sixième position sur Google pour ce terme.

Cela pourrait en faire un candidat idéal pour une mise à jour de contenu afin d'améliorer ton classement pour ce mot clé, d'augmenter ton taux de clics et d'obtenir plus de conversions.

Veux-tu bénéficier de ce type de données sur ton propre site Web? Essaie [Organic Traffic Insights](https://www.semrush.com/organic_traffic_insights/) gratuitement aujourd'hui.

Combine GSC, GA4, et les données de mots clés précieuses

avec l'outil Organic Traffic Insights

[Essaie gratuitement](https://www.semrush.com/organic_traffic_insights/)

*Cet article a été mis à jour en 2024. Des extraits de l'article original par Amit Panchal peuvent rester.*