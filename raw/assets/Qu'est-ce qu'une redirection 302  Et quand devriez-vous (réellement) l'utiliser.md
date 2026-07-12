---
title: "Qu'est-ce qu'une redirection 302 ? Et quand devriez-vous (réellement) l'utiliser ?"
source: "https://fr.semrush.com/blog/302-redirect/"
author:
  - "[[Semrush Team]]"
published: 2025-05-13
created: 2026-06-15
description: "Vous ne savez pas quand utiliser les redirections 302 ? Découvrez les meilleures pratiques et les erreurs courantes grâce à notre guide détaillé."
tags:
  - "clippings"
---
Nous avons traduit cet article de l'anglais. [Clique ici](https://www.semrush.com/blog/302-redirect/) pour lire l'article original. Si tu remarques des problèmes dans le contenu, n'hésite pas à nous contacter à [report-osteam@semrush.com](mailto:report-osteam@semrush.com).

Une redirection 302 est un moyen temporaire de rediriger les utilisateurs d'une page de votre site vers une autre page.

C'est important pour le référencement naturel car cela permet de rediriger le trafic vers une autre page tout en conservant le classement des mots clés et la valeur des liens de la page d'origine.

Dans ce guide, nous expliquerons quand, pourquoi et comment utiliser correctement les redirections 302.

## Comment fonctionnent les redirections 302?

Une redirection 302 est un peu comme un message d'absence du bureau.

Il ne s'agit pas d'un changement d'adresse permanent. Mais cela permet de garantir que les utilisateurs et les robots puissent toujours accéder à votre site si une page ou une ressource spécifique est indisponible.

Une redirection 302 peut améliorer l'expérience utilisateur (UX) sur votre site web en veillant à ce que les utilisateurs n'atterrissent pas sur des pages obsolètes, manquantes de fonctionnalités ou en construction.

Ce code d'état de réponse HTTP (302 - Trouvé) indique qu'une page a été déplacée. Toute personne tentant d'accéder à cette page est automatiquement [redirigée](https://www.semrush.com/blog/redirects/) vers la nouvelle page tant que la redirection 302 est en vigueur.

## Redirections 301 vs. Redirections 302

Faut-il utiliser une redirection 301 ou 302? C'est une question courante.

Voici la différence:

**Une [redirection 301](https://www.semrush.com/blog/301-redirects/) est une redirection permanente**.

**Une redirection 302 est une redirection temporaire**.

![Infographie « Avez-vous besoin de mettre en place une redirection ? »](https://static.semrush.com/blog/uploads/media/13/49/13490d6c02fec443fc29b78cb1340996/original.png)

Infographie « Avez-vous besoin de mettre en place une redirection? »

Par exemple, si vous déplacez définitivement le contenu de **example.com/page-1** vers **example.com/page-2**.

Vous souhaitez informer les utilisateurs et les robots des moteurs de recherche que votre ancienne page n'existe plus et qu'ils peuvent trouver le contenu à une nouvelle adresse.

Sinon, une redirection 302 convient aux cas d'utilisation temporaires.

Par exemple, vous utiliseriez une redirection 302 pour des choses comme: les tests A/B, les pages de vente temporaires ou la maintenance du site web.

Nous aborderons plus d'exemples de [quand utiliser une 302](#when-to-use-a-302-redirect) ci-dessous.

### 302 vs. 301 pour le référencement naturel

Du point de vue du référencement, les redirections 301 sont utiles pour consolider et préserver « l'autorité des liens » ou « le jus de lien », comme on l'appelle parfois. Une redirection 301 indique aux moteurs de recherche de traiter les liens retour pointant vers l'ancienne page comme s'ils pointaient désormais vers la nouvelle page.

C’est pourquoi il est recommandé d’utiliser une redirection 301 pour résoudre les problèmes de référencement comme la fusion de contenu dupliqué ou la modification permanente des URL.

Mais utiliser une 302 à la place n'est généralement pas catastrophique.

[Google traite les deux types de redirection](https://twitter.com/JohnMu/status/1380037034077794304) de presque la même manière, selon John Mueller, défenseur de la recherche Google. Ils utilisent d'autres signaux pour déterminer si l'URL d'origine ou la nouvelle URL doit être considérée comme canonique.

S’il apparaît clairement qu’une « redirection temporaire » est censée être permanente, ils parviennent généralement à le comprendre avec le temps et à agir en conséquence.

## Quand utiliser une redirection 302

Le mot le plus important en matière de redirections 302?

**Temporaire**.

Si vous hésitez encore à choisir une procédure 302, demandez-vous simplement s'il s'agit d'un changement temporaire ou d'un changement permanent.

Il n'existe pas de durée précise définissant ce qui est « temporaire ». Mais Google recommande d'utiliser une redirection permanente lorsque « vous êtes sûr que la redirection ne sera pas annulée ».

Cela signifie que vous devriez probablement utiliser un 302 dans tous les autres cas.

Par exemple:

### Maintenance ou refonte de site web

Vous travaillez sur une mise à jour importante de votre page à l'adresse **www.example.com/my-page** et vous ne voulez pas que quiconque la voie avant qu'elle ne soit prête.

Utilisez une redirection 302 pour rediriger les visiteurs vers une autre page pendant la durée des travaux.

### Tests A/B

Vous testez une nouvelle version d'une page de destination pour voir si elle est plus performante que la page existante.

Vous voudrez envoyer un certain pourcentage de votre trafic de la page existante (**example.com/page-1**) vers la version de test (**example.com/page-2**).

![Infographie illustrant le test A/B, où la moitié du trafic est dirigée vers la page A et l'autre moitié vers la page B.](https://static.semrush.com/blog/uploads/media/30/61/30611420dcf1817a32bbc999d0f41acb/original.png)

Infographie illustrant le test A/B, où la moitié du trafic est dirigée vers la page A et l'autre moitié vers la page B.

Utilisez une redirection 302 car il s'agit d'une expérience temporaire et la page n'a pas été déplacée de façon permanente.

### Pages promotionnelles temporaires

Vous organisez une vente à durée limitée et avez créé une page spéciale à cet effet.

Lorsqu'une personne clique sur « Chaussures », vous souhaitez l'envoyer vers votre nouvelle page de promotion spéciale (**example.com/shoe-sale**) pendant la durée de la vente.

Encore une fois: Temporaire = 302.

(N'oubliez pas de supprimer la redirection une fois la promotion terminée.)

### Tests en direct

Vous créez un nouveau parcours utilisateur sur votre site web, où les utilisateurs emprunteront un chemin différent pour trouver des informations ou effectuer une action. Vous souhaitez tester le nouveau flux depuis le site web en production avant son lancement définitif.

Utilisez une redirection 302 pour envoyer le trafic de **example.com/page** vers **example.com/page-test** et obtenir des commentaires ou collecter des données temporairement.

Ensuite, redirigez définitivement ou remplacez le contenu de la page une fois que vous serez prêt à déployer cette mise à jour.

## Comment mettre en place une redirection 302

Si vous avez lu ces scénarios et déterminé que 302 est l'appel approprié, il est temps de l'implémenter correctement.

Suivez attentivement les instructions et n'apportez que les modifications que vous êtes sûr de pouvoir corriger en cas de problème!

### WordPress

Mais même sans plugin, vous pouvez les implémenter directement, avec les connaissances appropriées.

#### Plugin Yoast SEO Premium

Le gestionnaire de redirections [Yoast SEO](https://yoast.com/) vous permet d'ajouter ou de supprimer rapidement des redirections 302. Vous aurez besoin d'un abonnement Yoast Premium.

![Redirection de page dans Yoast SEO](https://static.semrush.com/blog/uploads/media/1c/fb/1cfb122f36b4e9c54f216e6971e1df86/original.png)

Redirection de page dans Yoast SEO

Dans la barre latérale WordPress:

« **Yoast SEO** » > « **Redirections**. »

Remplissez ensuite les champs:

**Type** = 302

**Ancienne** **URL** = L'URL de la page d'origine sans le domaine racine (par exemple, « /page-1 »)

**URL** = L'URL de la nouvelle page sans le domaine racine (par exemple, « /page-2 »)

Cliquez sur « **Ajouter** **Redirection**. »

#### Plugin de redirection

[Redirection](https://wordpress.org/plugins/redirection/) est un autre plugin WordPress extrêmement populaire qui simplifie la mise en œuvre ou la suppression des 302.

Dans la barre latérale WordPress:

« **Outils** » > « **Redirection**. »

Sur la page « Redirections », recherchez le formulaire « Ajouter une nouvelle redirection ».

![Formulaire « Ajouter une nouvelle redirection » dans Yoast SEO](https://static.semrush.com/blog/uploads/media/94/7c/947c3ebc87001dd6506bd16d813f4bc4/original.png)

Formulaire « Ajouter une nouvelle redirection » dans Yoast SEO

Remplissez les champs:

**Source** **URL** = L'URL de la page d'origine sans le domaine racine (par exemple, « /page-1 »)

**Cible** **URL** = L'URL de la nouvelle page sans le domaine racine (par exemple, « /page-2 »)

**HTTP** **code** = 302

Cliquez ensuite sur « **Ajouter** **Redirection**. »

#### Plugin de calcul de classement

[Rank Math](https://rankmath.com/) est un autre plugin SEO populaire qui facilite la mise en œuvre d'une redirection 302.

Dans la barre latérale WordPress:

« **Rang** **Mathématiques** » > « **Redirections**. »

Depuis la page « Redirections », cliquez sur « **Ajouter** **Nouveau**.

![Page « Ajouter des redirections » du plugin Rank Math](https://static.semrush.com/blog/uploads/media/aa/74/aa745aeb5ea5acbf9635b1f05e04b051/original.png)

Page « Ajouter des redirections » du plugin Rank Math

**URL sources** = L'URL de la page d'origine sans le domaine racine (par exemple, « /page-1 »)

**URL de destination** = L'URL de la nouvelle page sans le domaine racine (par exemple, « /page-2 »)

**Type de redirection** = 302 Déplacement temporaire

Cliquez ensuite sur « **Ajouter** **Redirection**. »

#### Redirections PHP

***Avertissement:** Cette option vous obligera à modifier les fichiers de votre thème et votre code PHP. Son utilisation est recommandée uniquement aux utilisateurs avancés de WordPress à l'aise avec ce type de modifications.*

Si vous ne souhaitez pas ajouter l'un de ces plugins, vous pouvez implémenter la redirection manuellement.

Vous ajouteriez un code comme celui-ci tout en haut de votre en-tête PHP, avant toute fonction HTML ou echo:

`<?php   // Vérifier si la page demandée est page-1   if ($_SERVER['REQUEST_URI']=== '/page-1') {   // Rediriger de example.com/page-1 vers example.com/page-2   header("HTTP/1.1 302 Found");   header("Location: http://example.com/page-2");   exit;   }   ?>`

Dans cet exemple, nous redirigeons de **example.com/page-1** vers **example.com/page-2**.

Comme vous pouvez probablement l'imaginer, la mise en œuvre ou la maintenance de plusieurs de ces redirections spécifiques en PHP peut vite devenir compliquée. Mais c'est faisable.

### Apache

***Avertissement:** Cette méthode de redirection 302 est réservée aux experts. Des erreurs à ce niveau peuvent causer de gros problèmes à votre site web. Si vous n'êtes pas un expert, procédez avec une extrême prudence ou faites appel à un expert qui pourra vous aider.*

Tout d'abord, assurez-vous que [mod\_rewrite](https://httpd.apache.org/docs/2.4/mod/mod_rewrite.html) est activé. Utilisez ensuite RewriteEngine pour configurer vos redirections.

#### Rediriger une seule page

Si vous avez simplement besoin de rediriger une page vers une nouvelle page, vous pouvez écrire un code comme celui-ci:

`RewriteEngine sur   RewriteRule ^page-1$ /page-2 [R=302,L]`

Cela redirigera une page qui correspond exactement à l'URL **/page-1** vers **/page-2**.

Il convient de noter que vous pouvez également utiliser [mod\_alias](https://httpd.apache.org/docs/2.4/mod/mod_alias.html) pour des redirections simplifiées:

`Redirection 302 /page-1 /` page-2

#### Rediriger un répertoire entier

Si vous souhaitez rediriger temporairement un répertoire entier, vous pouvez le faire soit en redirigeant chaque page vers une nouvelle URL spécifique au sein du nouveau répertoire:

`RewriteEngine On   RewriteRule ^old-directory/(.*)$ /new-directory/$1 [R=302,L]`

Ce code, par exemple, redirigerait **/old-directory/page-1** vers **/new-directory/page-1**.

Ou vous pouvez rediriger *toutes les pages* de ce répertoire vers une seule nouvelle page:

`RewriteEngine On   RewriteRule ^old-directory/(.*)$ /new-page [R=302,L]`

Cette règle de réécriture redirigerait à la fois **/old-directory/page-1** et **/old-directory/page-2** vers la nouvelle URL, **/new-page**.

### Nginx

***Avertissement:** Cette méthode de redirection 302 est réservée aux experts. Des erreurs à ce niveau peuvent causer de gros problèmes à votre site web. Si vous n'êtes pas un expert, procédez avec une extrême prudence ou faites appel à un expert qui pourra vous aider.*

Les redirections Nginx sont configurées dans le fichier [.conf](https://docs.nginx.com/nginx/admin-guide/basic-functionality/managing-configuration-files/), généralement situé dans le répertoire racine de votre serveur.

#### Rediriger une seule page

`serveur {   écoute 80;   nom_serveur example.com;   emplacement /page-1 {   réécriture ^ /page-2 redirection;   }   # autres blocs d'emplacement et configuration...   }`

Cela redirigera **/page-1** vers **/page-2**.

#### Rediriger un répertoire entier

Rediriger toutes les pages d'un répertoire vers une nouvelle page dans un nouveau répertoire.

`serveur {   écoute 80;   nom_serveur example.com;   emplacement ~* ^/ancien-répertoire/ {   réécriture ^/ancien-répertoire/(.*)$ /nouveau-répertoire/$1 redirection;   }   # autres blocs d'emplacement et configuration...   }`

Par exemple, **/old-directory/page-1** redirige vers **/new-directory/page-1** et **/old-directory/page-2** redirige vers **/new-directory/page-2**.

Redirigez toutes les pages d'un répertoire vers un nouvel emplacement unique:

`serveur {   écoute 80;   nom_serveur example.com;   emplacement ~* ^/ancien-répertoire/ {   réécriture ^/ancien-répertoire/(.*)$ /nouvelle-page redirection;   }   # autres blocs d'emplacement et configuration...   }`

Par exemple, **/old-directory/page-1** et **/old-directory/page-2** redirigent tous deux vers la nouvelle URL, **/new-page**.

### Serveur Windows avec ASP.NET

***Avertissement:** Cette méthode de redirection 302 est réservée aux experts. Des erreurs à ce niveau peuvent causer de gros problèmes à votre site web. Si vous n'êtes pas un expert, procédez avec une extrême prudence ou faites appel à un expert qui pourra vous aider.*

Sur un serveur Windows, les redirections sont configurées dans le fichier web.config .

#### Rediriger une seule page

`<configuration>   <system.webServer>   <rewrite>   <rules>   <rule name="Redirect page-1 to page-2" stopProcessing="true">   <match url="^page-1$" />   <action type="Redirect" url="/page-2" redirectType="Found" />   </rule>   </rules>   </rewrite>   </system.webServer>   </configuration>`

Cela redirigera **/page-1** vers **/page-2**.

#### Rediriger un répertoire entier

Rediriger toutes les pages d'un répertoire vers une nouvelle page dans un nouveau répertoire.

`<configuration>   <system.webServer>   <rewrite>   <rules>   <rule name="Redirect old-directory to new-directory" stopProcessing="true">   <match url="^old-directory/(.*)" />   <action type="Redirect" url="/new-directory/{R:1}" redirectType="Found" />   </rule>   </rules>   </rewrite>   </system.webServer>   </configuration>`

Par exemple, **/old-directory/page-1** redirige vers **/new-directory/page-1** et **/old-directory/page-2** redirige vers **/new-directory/page-2**.

Redirigez toutes les pages d'un répertoire vers un nouvel emplacement unique:

`<configuration>   <system.webServer>   <rewrite>   <rules>   <rule name="Redirect old-directory to new-page" stopProcessing="true">   <match url="^old-directory/(.*)" />   <action type="Redirect" url="/new-page" redirectType="Found" />   </rule>   </rules>   </rewrite>   </system.webServer>   </configuration>`

Par exemple, **/old-directory/page-1** et **/old-directory/page-2** redirigent tous deux vers la nouvelle URL, **/new-page**.

## L'impact des redirections 302 sur le référencement naturel

### Impacts positifs du référencement naturel

N'oubliez pas que les redirections 302 ne sont pas destinées à corriger ou à améliorer les problèmes techniques de référencement (SEO) que rencontre votre site web.

Une redirection 302 est destinée à améliorer l'expérience utilisateur dans des situations temporaires.

- Consolidation du contenu dupliqué
- Correction des problèmes d'URL canoniques
- Redirection de la version avec www vers la version sans www de la même page
- Améliorer l'architecture de votre site

Mais la mise en place d'une redirection 302 permet de préserver vos liens et votre classement lorsqu'une page Web est temporairement indisponible ou en maintenance. Sans utiliser de redirection 302, votre page pourrait être indexée avec des problèmes d'utilisabilité ou un contenu incomplet, ce qui pourrait nuire à votre référencement.

Mais elle peut avoir un impact négatif si elle est mal mise en œuvre.

### Impacts négatifs sur le référencement naturel

En théorie, une utilisation incorrecte des redirections 302 pourrait créer des problèmes pour le référencement naturel de votre site web.

Par exemple, cela pourrait entraîner l'indexation d'une version incorrecte d'une page et son affichage dans les SERP (pages de résultats des moteurs de recherche).

En réalité?

Les impacts négatifs seraient probablement faibles et temporaires.

Google [traite une redirection 302](https://developers.google.com/search/docs/crawling-indexing/301-redirects) comme « un signal faible indiquant que la cible de redirection devrait être canonique ».

Voilà ce qu'on attend d'un 302.

Mais, s’il existe d’autres signaux indiquant que la nouvelle URL est en fait la version « principale » de ce contenu (l’URL canonique ), elle pourrait être traitée davantage comme une redirection permanente.

Donc, même si une redirection 302 est appliquée incorrectement, il y a de fortes chances que Google s'en aperçoive quand même.

Mais cela pourrait tout de même causer un problème temporaire avec votre site, votre classement et votre trafic.

De plus, il est préférable d'utiliser le type de redirection approprié si possible.

## 5 problèmes courants liés aux redirections 302

### 1: Utilisation d'un formulaire 302 pour des modifications permanentes

L'erreur la plus courante est peut-être d'utiliser un code 302 pour une modification permanente.

Comme nous l'avons évoqué, les 302 sont censés être temporaires.

Si vous utilisez une redirection 302 pour rediriger une page et que le changement devient permanent, il est recommandé de mettre à jour la redirection en une redirection 301.

Vous pouvez facilement identifier toutes les pages avec des 302 en utilisant l'outil Site Audit de Semrush .

Dans le menu de gauche, cliquez sur « **Site** **Audit** » sous « On Page & Tech SEO ».

Si votre site n'est pas déjà répertorié sous « Projets », saisissez votre domaine racine pour que Semrush puisse explorer et auditer votre site web.

![barre de recherche dans l'outil d'audit de site de Semrush](https://static.semrush.com/blog/uploads/media/0e/2d/0e2d4bdda97e4294c0d90228466fdc94/original.png)

barre de recherche dans l'outil d'audit de site de Semrush

Une fois l'audit terminé, cliquez sur le nom du « Projet » et recherchez le rapport « Pages explorées » sous « Santé du site ».

Cliquez sur le numéro affiché sur la ligne « Redirections » pour ouvrir un rapport des pages qui renvoient un code d'état HTTP de redirection.

![Ligne « Redirections » mise en évidence dans le rapport « Pages explorées »](https://static.semrush.com/blog/uploads/media/99/e3/99e3846241b2e1ad13afe6b511df1e59/original.png)

Ligne « Redirections » mise en évidence dans le rapport « Pages explorées »

Examinez la liste des URL avec des redirections et vérifiez si certaines d'entre elles renvoient un code 302.

![Liste des URL mises en évidence dans le rapport, indiquant le type de redirection (par exemple, redirection 301 ou 302).](https://static.semrush.com/blog/uploads/media/f1/58/f1584517b65a359d67ef033aec78f5e0/original.png)

Liste des URL mises en évidence dans le rapport, indiquant le type de redirection (par exemple, redirection 301 ou 302).

***Astuce de pro:** Vous pouvez appliquer un filtre de code d’état HTTP à ce rapport pour n’afficher que les pages qui renvoient un code d’état « 3xx temporaire ».*

Si des redirections 302 apparaissent alors qu'elles ne devraient pas exister, cela signifie probablement qu'elles ont été configurées par un autre membre de votre équipe ou par quelqu'un qui a travaillé sur le site par le passé.

Si la redirection n'est pas nécessaire ou est mal configurée (par exemple, s'il s'agit d'une modification permanente plutôt que temporaire), vous devrez examiner comment elle est mise en œuvre afin d'effectuer des ajustements.

Reportez-vous aux étapes décrites dans la section « [Comment implémenter une redirection 302](#how-to-implement-a-302-redirect) » ci-dessus.

Vous pouvez commencer par consulter votre panneau d'administration WordPress ou CMS. Si vous ne trouvez pas les redirections 302 répertoriées dans le rapport, envisagez de consulter une personne capable de vérifier l'implémentation côté serveur.

***Remarque:** Vous devez également éviter d'utiliser une redirection 301 pour des modifications qui ne sont que temporaires. Vous pouvez identifier ces problèmes en utilisant l'outil d'audit de site que nous venons de passer en revue. Si vous identifiez une page qui a été redirigée définitivement par erreur, supprimez la redirection 301 et mettez en place une redirection temporaire à la place.*

Trouvez et corrigez les problèmes de redirection

avec l'outil d'audit de site

[Essayez gratuitement](https://www.semrush.com/siteaudit/)

### 2: Chaînes de redirection

Les chaînes de redirection se produisent lorsqu'une page possède une redirection 302 qui pointe vers une autre page, laquelle possède également une redirection 302 qui pointe vers une autre page.

Comme ça:

**/page-1** a un 302 qui pointe vers **/page-2**.

**/page-2** a un 302 qui pointe vers **/page-3**.

L'utilisateur passe d'une page à l'autre. Et puis le suivant. (Et puis le suivant.)

Cela peut engendrer des problèmes de performance du site, comme des temps de chargement de page lents.

De plus, c'est tout simplement une mauvaise pratique.

En utilisant l'outil Semrush [Site Audit](https://www.semrush.com/siteaudit/), vous pouvez facilement identifier les chaînes de redirection que vous devez corriger.

Depuis Semrush:

Cliquez sur « **Site** **Audit** » sous « Référencement technique sur page &».

Cliquez sur l'URL de votre site sous « Projet ». Ou saisissez votre domaine pour créer un projet s'il n'est pas déjà répertorié.

![barre de recherche dans l'outil d'audit de site de Semrush](https://static.semrush.com/blog/uploads/media/0e/2d/0e2d4bdda97e4294c0d90228466fdc94/original.png)

barre de recherche dans l'outil d'audit de site de Semrush

(Si vous créez le projet à partir de zéro, vous saisirez votre domaine racine et Semrush explorera et auditera votre site. Une fois l'exploration terminée, cliquez sur l'URL du site sous « Projet ».

Depuis le « Tableau de bord du projet », cliquez sur « **Afficher le rapport complet** » dans la section « Audit du site ».

![Onglet « Problèmes » de l’outil d’audit de site avec le résultat « 27 chaînes et boucles de redirection ».](https://static.semrush.com/blog/uploads/media/99/c0/99c0cea91ef6cbd2aebc9d3a68be849c/original.png)

Onglet « Problèmes » de l’outil d’audit de site avec le résultat « 27 chaînes et boucles de redirection ».

La liste « Erreurs » vous indiquera tous les problèmes que Semrush a détectés sur votre site. Dans cette liste, vous trouverez une entrée pour « chaînes de redirection et boucles » si des cas ont été détectés.

Cliquez sur l'élément de la liste pour ouvrir le rapport complet.

Une fois que vous avez identifié les chaînes de redirection, vous pouvez simplement mettre à jour les redirections 302 existantes pour qu'elles pointent vers l'URL cible finale et ignorer les étapes de redirection supplémentaires.

### 3: Boucles de redirection (Trop de redirections)

Si votre redirection est mal configurée, vous risquez de vous retrouver dans une boucle de redirection.

Une boucle de redirection se produit lorsque vos redirections 302 renvoient sans cesse les utilisateurs entre deux pages ou plus.

![Infographie de Semrush : « Qu’est-ce qu’une boucle de redirection ? »](https://static.semrush.com/blog/uploads/media/c4/5b/c45b469e41e29946dfa0800557dc4847/original.png)

Infographie de Semrush: « Qu’est-ce qu’une boucle de redirection? »

Par exemple:

**/page-1** a un 302 qui pointe vers **/page-2**.

**/page-2** a un 302 qui pointe vers **/page-1**.

Le navigateur ne saura pas quelle page afficher. Vous recevrez une erreur ERR\_TOO\_MANY\_REDIRECTS ou « trop de redirections » et vous verrez une page qui ressemble à ceci dans Google Chrome:

![Exemple d'erreur « Cette page ne fonctionne pas »](https://static.semrush.com/blog/uploads/media/a8/4d/a84de8ecf4b19205d2354150f0a11f67/original.png)

Exemple d'erreur « Cette page ne fonctionne pas »

Vous pouvez identifier et résoudre ce problème à l'aide de l'outil Semrush [Site Audit](https://www.semrush.com/siteaudit/).

Dans le menu de gauche, cliquez sur « **Site** **Audit** » sous « On Page & Tech SEO ».

Si votre site n'est pas répertorié sur la page « Audit de site », saisissez votre domaine racine pour lancer une analyse et un audit.

![barre de recherche dans l'outil d'audit de site Semrush](https://static.semrush.com/blog/uploads/media/0e/2d/0e2d4bdda97e4294c0d90228466fdc94/original.png)

barre de recherche dans l'outil d'audit de site Semrush

Une fois l'exploration terminée, cliquez sur l'URL du site sous « Projet ».

(Si votre site figure déjà dans la liste des « Projets », cliquez sur l’URL.)

Depuis le « Tableau de bord du projet », cliquez sur « **Afficher le rapport complet** » dans la section « Audit du site ».

![Onglet « Problèmes » de l’outil d’audit de site avec le résultat « 27 chaînes et boucles de redirection ».](https://static.semrush.com/blog/uploads/media/f7/55/f7554a14e538fcb1fe2d86fa75b8f6fb/original.png)

Onglet « Problèmes » de l’outil d’audit de site avec le résultat « 27 chaînes et boucles de redirection ».

La liste « Erreurs » vous indiquera si Semrush a détecté une chaîne de redirection ou une boucle.

Cliquez sur la liste pour afficher la liste complète et trouver les boucles de redirection.

Si vous avez implémenté des redirections 302 et que vous recevez cette erreur, cela signifie probablement qu'il y a un problème avec la configuration.

Voici quelques éléments à rechercher:

- **Redirections conflictuelles**. Avez-vous créé par inadvertance des redirections qui tentent d'envoyer les utilisateurs d'une page vers plusieurs pages différentes? Ou avez-vous des redirections qui pointent les unes vers les autres? Examinez attentivement les redirections afin de repérer les situations susceptibles de créer un conflit.
- **Plugins en conflit**. Si vous utilisez un plugin de redirection ou un outil tiers, il est possible que ces plugins soient en conflit les uns avec les autres. Essayez de les désactiver un par un et voyez si cela résout le problème.

Si vous n'avez pas mis en place de redirection et que vous recevez cette erreur, il peut s'agir d'un problème local ou côté client. Cela signifie que la redirection est correctement configurée sur le serveur, mais qu'un problème survient du côté de l'utilisateur.

Essayer:

- **Effacer le cache et les cookies du navigateur**. Il est possible qu'une directive de redirection soit mise en cache même si elle n'est plus utilisée. Les problèmes de mise en cache peuvent également provenir d'un CDN ou d'une autre configuration réseau qui pourrait nécessiter un dépannage supplémentaire.
- **Désactiver les extensions du navigateur**. Dans certains cas, vos extensions de navigateur peuvent déclencher des redirections et rendre certaines pages inaccessibles.

### 4: Laisser les redirections 302 en place

En clair: n'oubliez pas de supprimer les redirections 302 lorsqu'elles ne sont plus nécessaires.

Le fait de le maintenir en place pendant une période prolongée pourrait amener les moteurs de recherche à le considérer comme une redirection permanente. Cela pourrait également engendrer une mauvaise expérience utilisateur.

Effectuez un audit régulier de votre site avec Semrush pour vous assurer de ne pas oublier de supprimer les redirections après une modification temporaire de votre site web.

### 5: Perte des paramètres d'URL lors d'une redirection

Dans certains cas, une redirection est nécessaire pour transmettre des paramètres d'URL spécifiques ou des codes de suivi à la nouvelle URL vers laquelle vous redirigez vos visiteurs.

Par exemple, si vous utilisez une convention UTM spécifique pour suivre les visiteurs lorsqu'ils naviguent sur votre site web. Ou si votre fonctionnalité de recherche et de filtrage transmet des spécifications via des paramètres d'URL.

Selon la manière dont vous avez implémenté les redirections, elles peuvent ou non transmettre des paramètres de l'URL d'origine à la nouvelle destination.

Transmettez-les ensuite lorsque l'utilisateur est redirigé.

## FAQ sur les redirections 302

### Quelle est la différence entre une redirection 302 et une redirection 301?

Une redirection 302 sert à signaler des modifications temporaires de votre site web, comme une page en construction ou un test A/B. Une redirection 301 sert à effectuer des modifications permanentes, comme le déplacement d'un contenu d'une ancienne URL vers une nouvelle URL.

### Quel est l'avantage d'une redirection 302?

L'utilité principale d'une redirection 302 est d'améliorer l'expérience utilisateur de votre site. Vous pouvez temporairement rediriger les utilisateurs vers une nouvelle URL afin d'éviter qu'ils n'atterrissent sur des pages obsolètes, incomplètes ou en construction. Il permet également de préserver le classement et la valeur du lien de l'URL d'origine pendant la durée de la redirection.

### Comment puis-je configurer une redirection 302 sur mon site web?

Si vous utilisez WordPress et la plupart des CMS courants, vous pouvez implémenter une redirection 302 à l'aide d'un plugin ou d'une extension. Dans d'autres cas, vous devrez configurer la redirection côté serveur.

### Comment Google gère-t-il les redirections 302?

Google traite une redirection 302 de la même manière qu'une redirection 301. Toutefois, dans les cas où il s'agit d'un changement temporaire, l'URL d'origine (et non la nouvelle URL) continuera d'être affichée dans les résultats de recherche.

Dans ce cas, ils ne transmettront ni le PageRank ni les liens vers la nouvelle URL à moins qu'il ne devienne clair que le changement est très probablement permanent.

### Les redirections 302 peuvent-elles nuire à mon référencement?

Oui. Une utilisation incorrecte d'une redirection 302 peut avoir un impact négatif sur votre classement dans les résultats de recherche et sur votre trafic. Par exemple, cela pourrait entraîner l'indexation de la mauvaise version de votre page et provoquer une baisse de votre classement et de votre trafic.

Si vous craignez que les redirections n'affectent négativement votre classement ou si vous cherchez à résoudre les problèmes de redirection sur votre site, la première étape consiste à effectuer un audit.

Utilisez l'outil Semrush [Site Audit](https://www.semrush.com/siteaudit/) pour identifier les configurations de redirection incorrectes, les boucles et chaînes de redirection, et des centaines d'autres problèmes qui pourraient freiner votre site.

Trouvez et corrigez les problèmes de redirection

avec l'outil d'audit de site

[Essayez gratuitement](https://www.semrush.com/siteaudit/)