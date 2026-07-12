---
title: "Erreurs de Google Search Console : comment les identifier et les corriger"
source: "https://fr.semrush.com/blog/google-search-console-errors/"
author:
  - "[[Rachel Baker]]"
  - "[[Karla Margeson]]"
published: 2025-05-13
created: 2026-06-15
description: "Un guide étape par étape pour identifier et corriger les erreurs courantes de Google Search Console, telles que les redirections et les erreurs 404."
tags:
  - "clippings"
---
Nous avons traduit cet article de l'anglais. [Clique ici](https://www.semrush.com/blog/google-search-console-errors/) pour lire l'article original. Si tu remarques des problèmes dans le contenu, n'hésite pas à nous contacter à [report-osteam@semrush.com](mailto:report-osteam@semrush.com).

Google Search Console est un service web qui vous permet de surveiller et de gérer la présence de votre site web dans les résultats de recherche Google.

Cela vous aide également à identifier les erreurs potentiellement importantes de votre site web. Voici ce que vous devez savoir sur ces erreurs et comment les corriger.

Trouvez et corrigez les problèmes de votre site web

avec l'outil d'audit de site

[Essayez-le gratuitement](https://www.semrush.com/siteaudit/)

## Comprendre les erreurs de Google Search Console

Si Googlebot rencontre des problèmes lors de l'exploration de votre site, ces problèmes peuvent être signalés comme des erreurs dans Google Search Console.

Il est important d'examiner ces points.

Pourquoi?

D'une part, ils peuvent avoir un impact négatif sur la visibilité de votre site dans les pages de résultats des moteurs de recherche ([SERPs](https://www.semrush.com/blog/serp/)).

Par exemple, des erreurs non résolues peuvent empêcher Google d'indexer correctement votre site web. Les pages non indexées n'apparaîtront pas dans les résultats de recherche.

Les erreurs non résolues sur un site web peuvent également avoir un impact négatif sur l'expérience utilisateur. C'est mauvais pour les visiteurs. Et c'est un facteur de classement clé pour Google, donc de mauvaises performances dans ce domaine peuvent également entraîner un classement plus bas dans les résultats de recherche.

Voyons comment corriger les erreurs de Google Search Console.

## Types d'erreurs de Google Search Console et comment les corriger

### Erreurs de code d'état

Les erreurs de code d'état dans Google Search Console sont liées aux codes d'état HTTP renvoyés lorsque Googlebot tente d'explorer vos pages Web.

Les codes d'état HTTP sont relayés à chaque chargement de site. Lorsqu'un utilisateur saisit une URL ou qu'un robot visite le site, une requête est envoyée au serveur de ce site. Le serveur répond par un code d'état HTTP qui indique au navigateur (ou au robot) plus de détails sur cette page.

Les codes d'état HTTP sont des nombres à trois chiffres. Par exemple, « 200 », « 301 » ou « 404 ».

![L'erreur de code d'état HTTP 404 a été détectée dans GSC.](https://static.semrush.com/blog/uploads/media/eb/17/eb176b21d5f2a46df340fa2a7748979b/931fca94be41458daedc7c8a490afab9/original.jpeg)

L'erreur de code d'état HTTP 404 a été détectée dans GSC.

Les différents codes d'état véhiculent différentes informations sur la réussite ou l'échec d'une requête.

Par exemple, le code d'état « 200 » indique que tout est en ordre et que la page est accessible comme prévu.

Cependant, certains codes d'état indiquent des problèmes d'accès à la page web. Ces erreurs apparaissent dans Google Search Console. Car elles peuvent nuire à la capacité des robots d'exploration et des utilisateurs à accéder à votre site.

Pour vérifier si vous avez des erreurs de code d'état, ouvrez [Google Search Console](https://search.google.com/search-console/about) et cliquez sur « **Pages** » dans le menu de gauche.

![« Pages » sélectionné dans le menu Google Search Console](https://static.semrush.com/blog/uploads/media/c9/80/c980ea21a38267d34b788d9c9a484d74/0ecb89d7294e77fd28dc34e6bbfab839/original.jpeg)

« Pages » sélectionné dans le menu Google Search Console

Vous verrez une ventilation des pages de votre site web selon qu'elles sont « indexées » ou « non indexées ».

Il est possible que certaines pages n'aient pas été indexées en raison d'une erreur de code d'état.

Pour vérifier si c'est le cas, faites défiler jusqu'en bas du rapport. Vous verrez un tableau intitulé « Pourquoi les pages ne sont pas indexées ».

![](https://static.semrush.com/blog/uploads/media/bb/09/bb09565db49b2c27e140e3b4246d58a0/b7b2d1b9799cdc5eab97355036e44a2a/original.jpeg)

En cas d'erreur d'état, vous verrez l'un des éléments suivants sous « Raison »:

- Erreur serveur (5xx)
- Introuvable (404)
- Requête non autorisée (401)
- 404 souple
- Erreur de redirection (3xx)

Passons en revue la signification des différents codes d'erreur et comment les corriger.

#### Erreurs serveur (5xx)

Un code d'état à trois chiffres commençant par « 5 » indique une erreur serveur. Cela indique un problème avec le serveur hébergeant votre site web.

Voici à quoi ressemble une erreur de serveur dans Google Search Console:

![« Erreur serveur (5xx) » dans Google Search Console](https://static.semrush.com/blog/uploads/media/3e/17/3e17ac2c729b6bf53db083d36793b02c/ed1aaa74d26cbec905458b8df0c2ac54/original.jpeg)

« Erreur serveur (5xx) » dans Google Search Console

Les causes courantes d'un statut 5xx incluent:

- **Erreurs de programmation**: Bugs ou erreurs de codage dans les scripts côté serveur (par exemple, PHP, Python, Ruby) qui alimentent votre site web
- **Problèmes de configuration du serveur**: Mauvaises configurations dans les paramètres du serveur ou le logiciel du serveur Web (par exemple, Apache, Nginx)
- **Épuisement des ressources**: Si le serveur manque de ressources (comme la mémoire ou la puissance de traitement), il peut avoir des difficultés à traiter les requêtes, ce qui entraîne des erreurs internes du serveur.
- **Problèmes de base de données**: Des problèmes avec la base de données sur laquelle repose votre site web, tels que des problèmes de connexion ou des erreurs de serveur de base de données, peuvent déclencher une erreur 5xx.

#### Comment résoudre une erreur serveur (5xx) dans Google Search Console

- **Consultez les modifications récentes.** Si l'erreur a commencé à se produire après des mises à jour ou des modifications récentes de votre site Web, envisagez de revenir à la version précédente de ces modifications pour voir si le problème est résolu.
- **Contactez votre fournisseur d'hébergement.** Si vous ne savez pas comment résoudre l'erreur serveur ou si elle est liée à l'infrastructure du serveur, contactez votre fournisseur d'hébergement pour obtenir de l'aide. Ils pourront peut-être identifier et résoudre le problème.
- **Testez les ressources du serveur.** Assurez-vous que votre serveur dispose de ressources suffisantes (processeur, mémoire, espace disque) pour gérer le trafic et les requêtes vers votre site web. Envisagez de passer à un forfait d'hébergement supérieur si nécessaire.

Une fois que vous avez identifié et résolu la cause sous-jacente de l'erreur serveur 5xx, utilisez Google Search Console pour demander une nouvelle exploration des pages concernées.

Pour ce faire, saisissez l'URL concernée dans le champ de recherche situé en haut de Google Search Console:

![La zone de recherche en haut de Google Search Console](https://static.semrush.com/blog/uploads/media/12/42/1242130258d8ef57243daed6b390cced/d278649cfa33fb89c823bd23a9a44275/original.png)

La zone de recherche en haut de Google Search Console

Cliquez ensuite sur « **DEMANDE D'INDEXATION** »:

![Bouton « DEMANDER L'INDEXATION » dans Google Search Console](https://static.semrush.com/blog/uploads/media/65/50/6550fe147450caeb8dbec445eac9e2ab/dc568e4091f17cd3e4ebd36184bf85df/original.jpeg)

Bouton « DEMANDER L'INDEXATION » dans Google Search Console

Cela demande à Googlebot de revisiter les pages et de mettre à jour son index avec les informations corrigées.

#### Erreurs 404 (Page introuvable)

L'erreur « 404 Not Found » est un code de réponse HTTP standard renvoyé lorsqu'un serveur ne trouve pas le contenu associé à l'URL demandée.

Dans le contexte de Google Search Console, cela signifie que Googlebot a tenté d'explorer une page de votre site, mais que le serveur a renvoyé une erreur 404 car il n'a pas pu trouver le contenu de la page.

Voici quelques raisons courantes pour lesquelles une erreur 404 peut se produire:

- **Modifications d'URL sans redirections appropriées**: Si vous avez modifié la structure des URL de votre site web sans mettre en place de redirections appropriées (par exemple, des redirections 301), les anciennes URL peuvent générer des erreurs 404.
- **Faute de frappe ou URL mal saisie**: Il est possible qu'il y ait eu une faute de frappe ou une erreur dans l'URL fournie à Googlebot. Vérifiez que les URL de votre plan de site et de vos liens internes sont correctes et mènent vers des pages existantes.

#### Comment trouver les erreurs 404 dans Google Search Console

![« Pages » sélectionné dans le menu Google Search Console](https://static.semrush.com/blog/uploads/media/11/05/1105d9ed3ed06cfcb43d2b3157ca86fa/6b081d97644fd246a4a058af4c6f453a/original.jpeg)

« Pages » sélectionné dans le menu Google Search Console

Faites défiler vers le bas pour voir « Pourquoi les pages ne sont pas indexées ». Ici, vous pourrez voir si des pages présentent une erreur 404.

![Erreur « Introuvable (404) » détectée dans Google Search Console](https://static.semrush.com/blog/uploads/media/ba/14/ba14052d7c4e569ce08ab0252f4f1393/8aec674fd88b577cfb948b9f0cdc0fe8/original.jpeg)

Erreur « Introuvable (404) » détectée dans Google Search Console

#### Comment corriger une erreur 404 dans Google Search Console

- **Implémenter les redirections 301.** Si vous avez délibérément et définitivement déplacé une page vers un nouvel emplacement, utilisez [301 redirections](https://www.semrush.com/blog/301-redirects/) pour faire pointer l'ancienne URL vers la nouvelle.
- **Mettre à jour les liens internes.** Si votre site web contient des liens vers des pages supprimées, mettez à jour ces liens pour qu'ils pointent vers des URL valides. Vous pouvez trouver ces liens en utilisant [Site Audit](https://www.semrush.com/siteaudit///) de Semrush.
- **Vérifier les liens externes.** Si des sites web externes renvoient vers des pages inexistantes de votre site, envisagez de contacter ces sites et de leur demander de mettre à jour leurs liens.
- **Soumettre un plan du site.** Assurez-vous que le plan de site de votre site web est à jour et reflète fidèlement sa structure actuelle. Ensuite, [soumettez le sitemap](https://www.semrush.com/blog/submit-sitemap-to-google/) à Google Search Console.

#### Erreurs de requête non autorisée (401)

Une erreur avec le code d'état HTTP « 401 » dans Google Search Console indique qu'une requête n'était pas autorisée.

![Erreur « Accès bloqué en raison d'une requête non autorisée (401) » dans Google Search Console](https://static.semrush.com/blog/uploads/media/3d/68/3d68e1cbf0ac41515883caf3afe960f4/003e8a8f4df846b539dd792e1436a671/original.png)

Erreur « Accès bloqué en raison d'une requête non autorisée (401) » dans Google Search Console

Source de l'image: [Seul](https://www.onely.com/blog/how-to-fix-blocked-due-to-unauthorized-request-401/)

Les erreurs 401 apparaissent lorsque:

- La page contient du contenu protégé par mot de passe, ce qui signifie que Googlebot et les autres robots d'exploration ne peuvent pas y accéder.
- Des blocages d'adresse IP ou des restrictions d'accès empêchent les adresses IP de Googlebot d'accéder à la page.
- Des problèmes de configuration spécifiques au robot d'exploration ont été accidentellement créés.

#### Comment corriger une erreur 401 (Non autorisé) dans Google Search Console

- **Vérifiez les paramètres d'authentification.** Si la page nécessite une authentification (par exemple, vous devez vous connecter pour consulter le contenu), vérifiez les paramètres d'authentification pour vous assurer qu'ils sont correctement configurés.
- **Accès de test.** Testez manuellement l'accès aux pages concernées en tentant d'y accéder via un navigateur Web ou en utilisant des outils comme la fonctionnalité « Explorer comme Google » dans Google Search Console. Cela peut aider à identifier tout problème d'accès.
- **Consulter les restrictions d'accès.** Vérifiez si votre serveur ou site web bloque les adresses IP ou impose des restrictions d'accès. Assurez-vous que les adresses IP de Googlebot ne sont pas bloquées et que les autorisations nécessaires à l'exploration sont en place.
- **Vérifier l'accès de l'agent utilisateur.** Vérifiez que la configuration de votre site web autorise l'accès aux agents utilisateurs des moteurs de recherche courants, notamment Googlebot. S'il existe des règles limitant l'accès à certains agents utilisateurs, assurez-vous qu'elles sont correctement configurées.

Après avoir résolu le problème d'accès non autorisé, utilisez Google Search Console pour demander une nouvelle exploration des pages concernées.

#### Erreurs 404 logicielles

Les erreurs 404 logicielles dans Google Search Console se produisent lorsqu'une page ressemble à une page normale (renvoie un code d'état 200), mais que son contenu ou certains signaux indiquent qu'elle doit être traitée comme si elle n'existait pas.

![Erreur « Soft 404 » dans Google Search Console](https://static.semrush.com/blog/uploads/media/1a/bf/1abf9fe72d2f9911784fb8a11603c6ac/74dcedebe8a8252ff20a173d11b82fa7/original.jpeg)

Erreur « Soft 404 » dans Google Search Console

Cela peut prêter à confusion pour les moteurs de recherche comme Google. Et cela peut avoir un impact sur la façon dont vos pages sont indexées et affichées dans les résultats de recherche. Google Search Console les signale comme des erreurs.

Les scénarios courants conduisant à des erreurs 404 temporaires incluent:

- **Pages vides**: Les pages vides ou contenant très peu de contenu peuvent déclencher des erreurs 404 logicielles. Bien que le serveur renvoie un code d'état « 200 OK », l'absence de contenu suggère que la page ne fournit pas d'informations pertinentes aux utilisateurs.

#### Comment corriger une erreur 404 logicielle dans Google Search Console

- **Consultez le contenu de la page.** Examinez le contenu des pages signalées comme erreurs 404 temporaires. Veillez à ce qu'ils fournissent des informations pertinentes aux utilisateurs. Si le contenu est insuffisant, envisagez de l'améliorer ou de rediriger les utilisateurs vers une page plus pertinente.
- **Vérifier les redirections.** Si une page est redirigée, assurez-vous que l'URL de destination contienne un contenu pertinent. Évitez de rediriger les utilisateurs vers des pages qui n'ont aucun rapport avec le contenu de la page d'origine.
- **Vérifier les pages d'erreur personnalisées.** Si votre site web utilise des pages d'erreur personnalisées, assurez-vous qu'elles fournissent des informations utiles et qu'elles ne soient pas confondues avec un contenu vide ou non pertinent.

### Erreurs de redirection

Les redirections envoient les utilisateurs et les robots des moteurs de recherche d'une URL à une autre.

Les erreurs de redirection surviennent lorsqu'une redirection échoue pour une raison quelconque. Ces erreurs peuvent avoir un impact négatif sur la façon dont les moteurs de recherche comme Google explorent, indexent et classent votre site web.

![Erreur « Page avec redirection » dans Google Search Console](https://static.semrush.com/blog/uploads/media/fc/2c/fc2c544b17567e44c85cbf9d0d23e875/e6e167ff07af06111a3933a69d0292f2/original.jpeg)

Erreur « Page avec redirection » dans Google Search Console

Les erreurs de redirection courantes incluent:

- **Chaînes de redirection**: C'est lorsqu'une URL redirige vers une autre, puis que cette deuxième URL redirige vers une troisième, formant ainsi une séquence de redirections. Les chaînes de redirection peuvent ralentir le chargement des pages et impacter négativement l'expérience utilisateur et l'efficacité de l'exploration par les moteurs de recherche.
- **Boucles de redirection**: Elles se produisent lorsque l'URL de destination finale redirige vers une URL précédente dans la chaîne. Cela peut provoquer une boucle infinie de redirections, empêchant le chargement de la page et entraînant des erreurs d'exploration.
- **Redirections incorrectes**: Si une page est redirigée vers une URL incorrecte ou non pertinente, cela peut entraîner une erreur de redirection. Les redirections doivent être configurées avec précision et diriger les utilisateurs et les moteurs de recherche vers une URL de destination pertinente.

### Comment corriger une erreur de redirection dans Google Search Console

Identifiez les erreurs de redirection dans Google Search Console en consultant le rapport « **Pages** ». Faites défiler vers le bas pour voir « Pourquoi les pages ne sont pas indexées ».

- **Analyser les chaînes de redirection.** Si des chaînes de redirection sont identifiées, examinez-les et simplifiez-les. Idéalement, une redirection devrait mener directement à la destination finale sans étapes intermédiaires inutiles.
- **Corriger les boucles de redirection.** Si des boucles de redirection sont détectées, identifiez la source de la boucle et corrigez les configurations de redirection pour la rompre. Vérifiez que l'URL de destination finale est correcte.
- **Vérifier les cibles de redirection.** Vérifiez que les URL vers lesquelles les pages sont redirigées sont exactes et pertinentes. Des redirections incorrectes peuvent induire en erreur les utilisateurs et les moteurs de recherche.
- **Mettre à jour les liens internes.** Si vous avez modifié les URL et mis en place des redirections, mettez à jour les liens internes de votre site pour qu'ils pointent directement vers les nouvelles URL, réduisant ainsi le besoin de redirections.
- **Utilisez les codes d'état de redirection appropriés.** Lors de la mise en œuvre de redirections, utilisez les codes d'état HTTP appropriés. Par exemple, une redirection 301 indique un déplacement permanent, tandis qu'une redirection 302 signale un déplacement temporaire.

## Problèmes d'exploration et d'indexation

Les problèmes d'exploration et d'indexation surviennent lorsque les robots d'exploration de Google ne parviennent pas à accéder à une page à laquelle ils devraient pouvoir accéder. Ou lorsqu'un élément les empêche d'ajouter une page à leur index.

Vous pouvez vérifier ces problèmes dans le rapport « **Pages** ».

Ouvrez le rapport et faites défiler vers le bas jusqu'au tableau « Pourquoi les pages ne sont pas indexées ».

Vous pourriez rencontrer les problèmes suivants.

### Bloqué par Robots.txt

Si une page est bloquée par le fichier robots.txt, cela peut poser problème. Mais seulement si vous ne souhaitez pas que cette page soit bloquée. Certaines pages sont bloquées intentionnellement.

![Erreur « Bloqué par robots.txt » dans Google Search Console](https://static.semrush.com/blog/uploads/media/7e/02/7e02fb69f0bdada79425ac0cf41acf31/b7be562ff49a592fd6b971e583f3a0e6/original.jpeg)

Erreur « Bloqué par robots.txt » dans Google Search Console

Le fichier robots.txt se trouve sur votre site web et contient des instructions pour les robots d'exploration des moteurs de recherche. C'est généralement la première page qu'ils consultent sur votre site web.

Vous pouvez inclure des instructions dans le fichier robots.txt pour indiquer aux robots d'exploration de ne pas explorer certaines pages. Par exemple, les pages d'administration qui ne sont pas accessibles sans connexion.

Vous faites cela en utilisant une directive « disallow ».

![Une directive « disallow » dans le fichier robots.txt](https://static.semrush.com/blog/uploads/media/83/f0/83f09ddd0342a2b428bc0e6ccb6a5099/3abf5d67d73651079e0006aec639cde0/original.png)

Une directive « disallow » dans le fichier robots.txt

Cependant, il est possible qu'une page soit bloquée par erreur par le fichier robots.txt.

Dans Google Search Console, si vous voyez une page indiquant « bloquée par robots.txt » mais que vous souhaitez que Google explore cette page, vous pouvez modifier le fichier robots.txt. Ensuite, utilisez Google Search Console pour demander une nouvelle exploration des pages concernées.

### Comment résoudre le problème des pages bloquées par robots.txt

Vous pouvez examiner et corriger tout problème lié à votre fichier robots.txt à l'aide de l'outil [Site Audit](https://www.semrush.com/siteaudit///).

Ouvrez l'outil et cliquez sur « **\+ Créer un projet**.

![Bouton « + Créer un projet » dans l’outil d’audit de site](https://static.semrush.com/blog/uploads/media/f6/9d/f69db4e86eaf67d4e94a6fa77a670e07/020fff1a4799671f4c948a46111dd5ea/original.jpeg)

Bouton « + Créer un projet » dans l’outil d’audit de site

Saisissez le domaine de votre site web. Si vous le souhaitez, vous pouvez également donner un nom au projet.

Cliquez sur le bouton « **Créer un projet** ».

!["Créer un projet ! fenêtre dans l'outil d'audit de site](https://static.semrush.com/blog/uploads/media/2d/39/2d397c3601bbc1499b4d35f7abdd5e79/c104cc8541d21444f59563e436eecec1/original.png)

"Créer un projet! fenêtre dans l'outil d'audit de site

Configurez les paramètres supplémentaires que vous souhaitez pour l'audit du site. Cliquez ensuite sur « **Démarrer l’audit du site**. »

![fenêtre « Paramètres d’audit du site »](https://static.semrush.com/blog/uploads/media/fd/32/fd32eb9e2e90316a5f295ac560d6c551/78d471701ea45fabbe4e6281ac826536/original.jpeg)

fenêtre « Paramètres d’audit du site »

Une fois l'audit terminé, allez dans l'onglet « **Problèmes** » et recherchez « robots.txt ».

![Résultats pour « robots.txt » sous l'onglet « Problèmes » de l'outil d'audit du site](https://static.semrush.com/blog/uploads/media/01/1a/011a9bbced87292e3c18b373bdfa5f48/c1edc528fc0f39cb7f7103b30ee2b484/original.jpeg)

Résultats pour « robots.txt » sous l'onglet « Problèmes » de l'outil d'audit du site

Cliquez sur les problèmes liés à votre fichier robots.txt, tels que « Le fichier robots.txt contient des erreurs de format ».

![Problème « Le fichier Robots.txt présente des erreurs de format » dans l'outil d'audit de site](https://static.semrush.com/blog/uploads/media/7f/5a/7f5aee27ad845c05cb0a53fa3fecf027/0f0bcf3f0055b5fb8a31386eeab9cd3d/original.jpeg)

Problème « Le fichier Robots.txt présente des erreurs de format » dans l'outil d'audit de site

Une liste des lignes invalides du fichier sera affichée.

Cliquez sur « **Pourquoi et comment y remédier** » pour obtenir des instructions spécifiques sur la façon de résoudre l'erreur.

Trouvez et corrigez les problèmes de votre site web

avec l'outil d'audit de site

[Inscrivez-vous maintenant](https://www.semrush.com/siteaudit/)

## Problèmes d'expérience utilisateur et d'utilisabilité

Les problèmes rencontrés sur un site web et qui entraînent une mauvaise expérience utilisateur sont préoccupants pour deux raisons.

Tout d'abord, vous ne voulez pas que les visiteurs de votre site aient une mauvaise expérience. Cela engendre la méfiance envers votre marque. Et cela diminue les chances que cette personne interagisse à nouveau avec votre contenu.

Une mauvaise expérience utilisateur est également néfaste car une expérience utilisateur positive constitue un facteur de classement important pour Google Search. Les pages offrant une mauvaise expérience utilisateur seront moins bien référencées dans les résultats de recherche.

### Problèmes liés aux indicateurs Web essentiels

Les Core Web Vitals sont un ensemble de mesures centrées sur l'utilisateur qui évaluent les performances de chargement, l'interactivité et la stabilité visuelle d'une page.

En résumé, les Core Web Vitals mesurent la rapidité et l'agrément d'utilisation d'un site web.

Les trois principaux indicateurs sont:

- **Largest Contentful Paint (LCP)**: Temps nécessaire pour que le plus grand élément de contenu (comme une image ou un bloc de texte) devienne visible à l'écran de l'utilisateur
- **Interaction avec le prochain affichage (INP)**: Qualité de la réactivité de la page web aux interactions de l'utilisateur
- **Décalage cumulatif de la mise en page (CLS)**: Nombre de décalages de la page lors de son chargement

Google Search Console vous signale les problèmes de performances liés aux Core Web Vitals.

![Problèmes de performance des indicateurs Web essentiels dans GSC](https://static.semrush.com/blog/uploads/media/8d/f3/8df31420cb46dd238d11dd2bfbff0659/c5e0e6dd4d28ea6e9229a6928df4363a/original.jpeg)

Problèmes de performance des indicateurs Web essentiels dans GSC

Vous pouvez identifier ces problèmes à l'aide de l'outil [Site Audit](https://www.semrush.com/siteaudit//). Et obtenez des conseils sur la façon de les réparer.

### Comment résoudre les problèmes liés aux indicateurs Web essentiels

Ouvrir [Audit du site](https://www.semrush.com/siteaudit//). Choisissez un projet existant ou cliquez sur « **\+ Créer un projet** ».

Configurez les paramètres et cliquez sur « **Démarrer l'audit du site**.

![fenêtre « Paramètres d’audit du site »](https://static.semrush.com/blog/uploads/media/d7/3d/d73db57b3551ca0dcb96402c91c4fdb0/f2f75b7601783b5c94c3d087a64c8cdc/original.jpeg)

fenêtre « Paramètres d’audit du site »

Dans quelques minutes, vous verrez vos résultats.

Dans le rapport « Vue d'ensemble », vous verrez un widget à droite appelé « Indicateurs Web essentiels ». Cliquez sur « **Afficher les détails**. »

!["Widget des indicateurs Web essentiels" mis en évidence dans le tableau de bord de présentation de l'audit de site](https://static.semrush.com/blog/uploads/media/f2/47/f247f24cdfa018c3f8b5eb9560e2d581/8cf1484c6170480790733e6eb4d2a1ed/original.png)

"Widget des indicateurs Web essentiels" mis en évidence dans le tableau de bord de présentation de l'audit de site

Vous pourrez comparer vos performances aux indicateurs clés Web Vitals pour 10 pages de votre site.

![Rapport de performance des indicateurs Web essentiels dans l'outil d'audit de site](https://static.semrush.com/blog/uploads/media/1e/f2/1ef2e7ff40e2b8cf57599ab425082e72/b0e702dac8ed58724173b63fe97d2b70/original.jpeg)

Rapport de performance des indicateurs Web essentiels dans l'outil d'audit de site

Faites défiler vers le bas jusqu'à « Métriques » et vous pourrez voir les performances ventilées selon les trois indicateurs Web essentiels.

Sous chaque élément, vous trouverez une liste intitulée « Principales améliorations » contenant des suggestions pour améliorer vos performances dans ce domaine.

### Erreurs HTTPS dans Google Search Console

Google privilégie les sites disposant d'un certificat SSL. Il s'agit d'un certificat de sécurité qui chiffre les données transmises entre un site web et un navigateur.

Une fois que vous disposez d'un certificat SSL, toutes les pages de votre site Web doivent commencer par « https:// ».

Toute page commençant par « http:// » pourrait indiquer des problèmes de sécurité aux moteurs de recherche. Il est donc préférable de les corriger dès leur apparition.

Ouvrez Google Search Console et cliquez sur « HTTPS » dans le menu de gauche.

![« HTTPS » mis en évidence dans le menu GSC](https://static.semrush.com/blog/uploads/media/22/c2/22c2046887284e196b1b805cd2d296e7/272e4dc8b07a8845cb8348722b2ac012/original.jpeg)

« HTTPS » mis en évidence dans le menu GSC

Le tableau indiquera si votre site contient des URL non HTTPS.

![URL non HTTPS affichant 0 dans GSC](https://static.semrush.com/blog/uploads/media/d6/57/d657ac1750c49bdfdc2b4d4ef160c08c/27a0eb15945572e71a6d5ddee457ccac/original.jpeg)

URL non HTTPS affichant 0 dans GSC

### Comment corriger les erreurs HTTPS dans Google Search Console

Si vous rencontrez des erreurs HTTPS, faites défiler vers le bas la page HTTPS dans Google Search Console. Vous verrez un tableau intitulé « Pourquoi les pages ne sont pas servies via HTTPS ».

Cliquez sur la ligne du problème pour voir quelles URL sont concernées.

![Erreur « HTTPS non évalué » dans Google Search Console](https://static.semrush.com/blog/uploads/media/2e/27/2e27842c047b53b1ea5869df42afc60f/b5c181ab603a109a857ae00a16079e5c/original.png)

Erreur « HTTPS non évalué » dans Google Search Console

Une fois la liste des URL affichée, vous pouvez supprimer tous les liens vers ces pages de votre site web et demander à Google Search Console d'explorer à nouveau votre site.

## Actions manuelles dans Google Search Console

Les actions manuelles dans Google Search Console font référence aux sanctions imposées à un site web par des examinateurs humains travaillant chez Google. Lorsque ces examinateurs identifient des violations des règles de Google, ils peuvent prendre des mesures manuelles pour sanctionner le site.

Les actions manuelles diffèrent des pénalités algorithmiques, qui sont appliquées automatiquement par les algorithmes de Google.

Les raisons courantes justifiant une intervention manuelle sont les suivantes:

- **Liens non naturels**: Si un site est impliqué dans des systèmes de liens frauduleux, a acheté des liens ou participe à des échanges de liens qui enfreignent les consignes de Google, il peut faire l'objet d'une action manuelle.
- **Contenu de faible qualité ou dupliqué**: Les sites web proposant du contenu de faible qualité ou dupliqué peuvent faire l'objet de mesures manuelles pour non-respect des règles de qualité du contenu.
- **Masquage ou redirections trompeuses**: Si un site affiche un contenu différent aux utilisateurs et aux moteurs de recherche ou utilise des redirections trompeuses, il peut faire l'objet d'une action manuelle.
- **Balisage structuré indésirable**: L'utilisation incorrecte du balisage de données structurées (schema.org) pour manipuler les résultats de recherche peut entraîner des actions manuelles
- **Spam généré par les utilisateurs**: Les sites web qui permettent aux utilisateurs de générer du contenu (commentaires, forums) peuvent faire l'objet de mesures manuelles s'ils ne parviennent pas à modérer et à contrôler efficacement le spam.
- **Contenu piraté**: Si un site est compromis et contient du contenu nuisible ou non pertinent, Google peut prendre des mesures manuelles pour protéger les utilisateurs

Si une action manuelle est imposée, vous en serez informé via Google Search Console.

![Actions manuelles dans Google Search Console](https://static.semrush.com/blog/uploads/media/c0/ea/c0eafc8d2cc7bdc7c5c5c5d294c634e5/093471a7976bb3de7d5ec81c18107a1a/original.png)

Actions manuelles dans Google Search Console

**Source de l'image**: [Google](https://support.google.com/webmasters/thread/7879895/regarding-manual-actions-in-search-console?hl=en)

La notification vous donnera des détails sur le problème. Ainsi que des conseils sur la manière de le corriger et les étapes à suivre pour demander une révision après les corrections.

Une fois le problème résolu, saisissez-le dans Google Search Console et cliquez sur « **Demander un examen**.

Si vous avez correctement résolu le problème, l'équipe de Google le marquera comme résolu et les pénalités pourront être levées.

### Problèmes de sécurité dans Google Search Console

Lorsque des problèmes de sécurité sont identifiés, ils peuvent avoir un impact négatif sur la visibilité de votre site dans les résultats de recherche. De plus, Google peut signaler votre site comme potentiellement nuisible aux utilisateurs.

Le rapport sur les problèmes de sécurité dans Google Search Console fournit des informations sur les menaces ou problèmes de sécurité potentiels détectés sur votre site web.

Les problèmes de sécurité les plus fréquemment signalés dans Google Search Console incluent:

- **Infections par des logiciels malveillants**: Google peut détecter des logiciels malveillants sur votre site, indiquant qu'il a été compromis. Et il existe des logiciels malveillants susceptibles de nuire aux visiteurs.
- **Contenu piraté**: Si votre site Web a été piraté, les attaquants peuvent injecter du contenu ou des liens indésirables. Google vous alertera en cas de détection de contenu piraté.
- **Ingénierie sociale**: Google identifie les cas où votre site peut être impliqué dans des attaques d'ingénierie sociale, telles que le phishing ou les pratiques trompeuses

### Mesures à prendre pour résoudre les problèmes de sécurité:

Utilisez Google Search Console pour identifier et corriger les problèmes de sécurité.

Ouvrez Google Search Console. Accédez à la section Actions manuelles de sécurité & sur le côté gauche de l'écran. Cliquez sur « **Problèmes de sécurité**. »

![« Problèmes de sécurité » dans Google Search Console](https://static.semrush.com/blog/uploads/media/95/9d/959d2f5774eee1427e0833bce43db4d4/2343556e216f4e69caf2a2e27a38af56/original.png)

« Problèmes de sécurité » dans Google Search Console

Si des problèmes ont été signalés, vous les verrez ici.

Google fournira des informations sur le type de problèmes de sécurité détectés. Ainsi que des recommandations ou des actions pour résoudre les problèmes.

Si un logiciel malveillant ou un contenu piraté est détecté, nettoyez et sécurisez votre site web. Supprimez tout code malveillant, mettez à jour les mots de passe et mettez en œuvre des mesures de sécurité supplémentaires.

Après avoir résolu les problèmes de sécurité, soumettez votre site à un examen via Google Search Console. Google évaluera si les problèmes ont été traités de manière adéquate.

## Prévention des erreurs de Google Search Console

Suivez ces bonnes pratiques pour éviter les erreurs de Google Search Console.

- **Effectuez des audits réguliers du site.** Effectuez des audits réguliers de votre site web afin d'identifier et de résoudre rapidement les problèmes techniques.
- **Maintenez votre sitemap XML à jour.** Assurez-vous que votre site web possède un sitemap XML qui inclut toutes les pages pertinentes. Soumettez le sitemap aux moteurs de recherche via Google Search Console pour faciliter l'exploration et l'indexation.
- **Optimisez votre fichier robots.txt.** Utilisez un fichier robots.txt bien structuré pour contrôler quelles parties de votre site doivent être explorées par les moteurs de recherche. Veuillez consulter et mettre à jour régulièrement ce fichier.
- **Assurez-vous de disposer d'un certificat SSL valide.** Assurez-vous que votre site web possède un certificat SSL valide, assurant une connexion sécurisée (HTTPS). Google privilégie les sites sécurisés, ce qui a un impact positif sur leur classement.
- **Optimiser les images.** Optimisez les images pour un chargement plus rapide. Utilisez des noms de fichiers descriptifs et incluez un texte alternatif pour l'accessibilité et le référencement naturel.
- **Utilisez une structure d'URL forte.** Veillez à ce que vos URL soient simples, descriptives et conviviales. Évitez autant que possible d'utiliser des paramètres d'URL complexes.

Les outils Semrush vous aident à optimiser les performances techniques SEO de votre site web. Grâce à elles, vous pouvez déceler les problèmes avant qu'ils ne s'aggravent.

Utilisez [Audit de site](https://www.semrush.com/siteaudit//) pour connaître les problèmes actuels de votre site. Et comment les réparer.

De plus, vous recevrez des courriels automatiques dès qu'un nouveau problème potentiel surviendra. Vous restez ainsi toujours au fait de vos performances SEO.

Accédez à plus de 55 outils

avec un compte Semrush gratuit

[Inscrivez-vous maintenant](https://www.semrush.com/signup/)