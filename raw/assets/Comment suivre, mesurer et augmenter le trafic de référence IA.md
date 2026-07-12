---
title: "Comment suivre, mesurer et augmenter le trafic de référence IA"
source: "https://fr.semrush.com/blog/ai-referral-traffic/"
author:
  - "Carlos Silva"
  - "[[Christine Skopec]]"
published: 2025-05-13
created: 2026-06-15
description: "Découvrez ce qu'est le trafic de référence IA, comment le suivre et les tactiques pour obtenir plus de visites provenant des plateformes d'IA."
tags:
  - "clippings"
---
Nous avons traduit cet article de l'anglais. [Clique ici](https://www.semrush.com/blog/ai-referral-traffic/) pour lire l'article original. Si tu remarques des problèmes dans le contenu, n'hésite pas à nous contacter à [report-osteam@semrush.com](mailto:report-osteam@semrush.com).

## Qu'est-ce que le trafic de référence IA?

Le trafic de référence IA désigne les visites de sites Web provenant de liens cités dans les réponses générées par l'IA de plateformes telles que ChatGPT, Perplexity, Claude et les aperçus de l'IA de Google.

Si un utilisateur clique sur un lien dans un outil de modélisation du langage (LLM) de grande taille, comme l'un de ceux présentés ci-dessous, pour visiter votre site, il s'agit de trafic de référence IA.

![Mode IA de Google avec les liens des sites web utilisés dans sa réponse apparaissant sur la droite.](https://static.semrush.com/blog/uploads/media/10/4c/104c2998cb27160bb98632893fa178ff/e2f748b2bf044f12002f18cfdd8890e0/original.png)

Mode IA de Google avec les liens des sites web utilisés dans sa réponse apparaissant sur la droite.

## Pourquoi le trafic de référence IA est-il important?

Le trafic de référence de l'IA est important car nos recherches suggèrent que les visiteurs de recherche IA [surpasseront les visiteurs de recherche traditionnels](https://www.semrush.com/blog/ai-search-seo-traffic-study/) d'ici 2028. Le suivi de votre trafic de référence IA peut vous aider à identifier des opportunités pour garder une longueur d'avance sur vos concurrents.

![Prévisions du nombre annuel de visiteurs par source de 2025 à 2029 pour la recherche organique traditionnelle par rapport aux LLM.](https://static.semrush.com/blog/uploads/media/14/ff/14ff98c501dd4f84da912565798a3fa1/c2b5e1aed214f7f7259a2f96eb692925/original.png)

Prévisions du nombre annuel de visiteurs par source de 2025 à 2029 pour la recherche organique traditionnelle par rapport aux LLM.

Le hic?

De nombreux clics d'IA apparaissent comme du trafic « direct » dans Google Analytics 4 (GA4) car les plateformes d'IA ne transmettent pas toujours les informations de référent. Cela signifie que vous recevez probablement plus de trafic IA que ce que vos rapports indiquent.

![Rapport par source de session sur GA4 avec la ligne de trafic « direct » mise en évidence.](https://static.semrush.com/blog/uploads/media/37/f9/37f937b7775ff384e0248eaefcff3c3b/e4e252f047e7dfd5ed8ec5c5d5cd2bce/original.png)

Rapport par source de session sur GA4 avec la ligne de trafic « direct » mise en évidence.

Plusieurs façons, en fait.

## Quelles plateformes d'IA génèrent le plus de trafic?

Suivis par Gemini, Perplexity, CoPilot et Grok.

![Plateformes d'IA classées selon le volume de trafic de recherche qu'elles génèrent : ChatGPT, Gemini, Perplexity, CoPilot et Grok.](https://static.semrush.com/blog/uploads/media/dc/ff/dcff0d7fabfe38967b6c9c050967e85e/966422a0d77876d7ca71c8a7f4e2f745/original.png)

Plateformes d'IA classées selon le volume de trafic de recherche qu'elles génèrent: ChatGPT, Gemini, Perplexity, CoPilot et Grok.

| **Plateforme AT** | **Visites de juillet 2025** | **Part de trafic %** |
| --- | --- | --- |
| chatgpt.com | 5 244 855 278 | 85,79% |
| gemini.google.com | 287 535 861 | 4,70% |
| perplexité.ai | 173 581 751 | 2,84% |
| grok.com | 153 011 519 | 2,50% |
| claude.ai | 136 577 834 | 2,23% |
| copilot.microsoft.com | 97 802 733 | 1,60% |
| méta.ai | 16 599 298 | 0,27% |
| yiyan.baidu.com | 3 327 311 | 0,05% |
| deepseek.ai | 243 299 | 0,00% |
| brave.com/leo/ | 55 803 | 0,00% |

L'optimisation du contenu pour ChatGPT pourrait donc être un bon point de départ.

Nous vous recommandons toutefois d'analyser vos concurrents pour voir quelles plateformes leur envoient le plus de trafic. Ensuite, optimisez votre contenu pour ces plateformes. Pour tenter de capter une partie du trafic de vos concurrents.

## Comment suivre le trafic de référence IA

La mise en place de rapports personnalisés, de groupes personnalisés et l'utilisation d'un outil de suivi IA dédié vous aident à suivre le trafic IA (comme les références ChatGPT), afin d'obtenir des données précises à analyser.

[Celia Harding](https://www.linkedin.com/in/celiaharding/) est la fondatrice de Leoprd, une agence spécialisée dans le développement de la reconnaissance dans les LLM. Elle dit:

> *Utilisez GA4 pour voir si vous recevez du trafic provenant de modèles d'IA ou si vous êtes complètement ignoré. Ensuite, comparez votre part de marché en termes de modèles avec celle de vos concurrents.*

Voici comment procéder:

### Configurer les filtres Regex dans GA4

L'utilisation d'expressions régulières ou de modèles « regex » (séquences de caractères définissant des modèles de recherche) pour créer un filtre personnalisé peut vous aider à surveiller avec précision le trafic de référence de l'IA.

Dans Google Analytics 4 (GA4), accédez à « **Rapports** » > « **Acquisition** » > « **Acquisition de trafic** ».

Cliquez sur « **Ajouter un filtre +** » et remplissez le filtre comme ceci:

- **Dimension**: Source/support de session
- **Type de correspondance**: correspond à l'expression régulière
- **Valeur**:.\*(chatgpt\\.com|openai\\.com|perplexity\\.ai|claude\\.ai|gemini\\.google\\.com|bard\\.google\\.com|you\\.com|search\\.brave\\.com|copilot\\.microsoft\\.com).\*
![Ajout d'un filtre regex à GA4 en personnalisant la dimension, le type de correspondance et la valeur.](https://static.semrush.com/blog/uploads/media/22/0c/220ca8e542529fddc08d2bd6a0bac380/12c23a165cf1319184f891ac29123d9e/original.png)

Ajout d'un filtre regex à GA4 en personnalisant la dimension, le type de correspondance et la valeur.

Cliquez sur « **Appliquer**. »

Cette expression régulière capture le trafic provenant des principales plateformes d'IA telles que ChatGPT, Perplexity, Claude, etc. (Vous pouvez ajuster l'expression régulière pour afficher d'autres LLM si nécessaire.)

Vous pouvez voir les pages vers lesquelles les LLM envoient du trafic en cliquant sur « **+** » > « **Page de destination + chaîne de requête**. »

![Rapport GA4 avec le filtre regex appliqué pour afficher toutes les principales plateformes d'IA comme ChatGPT, Perplexity, etc.](https://static.semrush.com/blog/uploads/media/2f/da/2fda682e56da9e8cab39c8da31ac0c7b/a464fd0089f21a49de22899d6cb84e2b/original.png)

Rapport GA4 avec le filtre regex appliqué pour afficher toutes les principales plateformes d'IA comme ChatGPT, Perplexity, etc.

### Créer des groupes de canaux de trafic IA personnalisés dans GA4

La mise en place d'un groupe de canaux IA dédié vous permet d'analyser les performances de l'IA parallèlement à la recherche organique, aux médias sociaux et aux canaux payants. Et vous pouvez l'utiliser dans tous vos rapports.

Dans GA4, accédez à « **Admin,**» trouvez la section **«** Affichage des données **»**, sélectionnez « **Groupes de canaux** » et sélectionnez soit votre groupe de canaux par défaut, soit votre propre groupe personnalisé.

Nommez votre groupe quelque chose comme « Groupe de canaux avec IA ». Cliquez ensuite sur « **Ajouter un nouveau canal**. »

![Fenêtre « Créer un nouveau groupe de chaînes » sur GA4 avec un nom de groupe saisi et « Ajouter une nouvelle chaîne » cliqué.](https://static.semrush.com/blog/uploads/media/c8/47/c847ac9ff16bf0c08dbbad7a43bf3412/d1ed2067637f385bdd9d82fb2a00a1f1/original.png)

Fenêtre « Créer un nouveau groupe de chaînes » sur GA4 avec un nom de groupe saisi et « Ajouter une nouvelle chaîne » cliqué.

Nommez le groupe de canaux « Trafic de référence IA » et cliquez sur « **\+ Ajouter un groupe de conditions** ».

Sélectionnez « **Source** », puis « **correspond à l'expression régulière** » et appuyez sur Entrée.

**Source correspond à l'expression régulière**:.\*(chatgpt\\.com|openai\\.com|perplexity\\.ai|claude\\.ai|gemini\\.google\\.com|bard\\.google\\.com|you\\.com|search\\.brave\\.com|copilot\\.microsoft\\.com).\*

Cliquez sur « **Enregistrer le canal** » puis cliquez sur « **Enregistrer le groupe** ».

![fenêtre « Créer un nouveau canal » sur GA4 avec un nom de canal & conditions de canal saisies et « Enregistrer le canal » cliqué.](https://static.semrush.com/blog/uploads/media/53/b0/53b0e10829920b39e16c53d2bcf2726c/ec0a586a9c38171d3c318674a28ea665/original.png)

fenêtre « Créer un nouveau canal » sur GA4 avec un nom de canal & conditions de canal saisies et « Enregistrer le canal » cliqué.

Pour afficher ce filtre, accédez à « **Rapports** » > « **Acquisition** » > « **Acquisition de trafic** ». Sélectionnez votre chaîne dans le menu déroulant.

![Navigation vers le groupe de canaux de session avec l'IA dans le rapport d'acquisition de trafic sur GA4.](https://static.semrush.com/blog/uploads/media/8c/1f/8c1fc45772653f172635884eb42e773a/cdf511312877ff2bcc7980c9cf645186/original.png)

Navigation vers le groupe de canaux de session avec l'IA dans le rapport d'acquisition de trafic sur GA4.

Vous pouvez désormais comparer le trafic IA avec d'autres sources de trafic.

![Le « trafic de référence IA » est mis en évidence pour permettre de le comparer à d'autres sources de trafic.](https://static.semrush.com/blog/uploads/media/93/2b/932bb7a32b21825456aba0c37f1c400c/df8f733cfcd929a247ca34ee85b54188/original.png)

Le « trafic de référence IA » est mis en évidence pour permettre de le comparer à d'autres sources de trafic.

### Utilisez le tableau de bord de trafic IA de Semrush

Le tableau de bord [AI Traffic](https://www.semrush.com/analytics/traffic/ai-traffic/) de Semrush vous permet d'analyser le trafic de référence IA vers votre domaine et les domaines concurrents, afin que vous puissiez voir comment vous vous comparez à vos rivaux.

Commencez par saisir votre domaine et jusqu'à quatre concurrents. Cliquez sur « **Analyser**. »

![L'outil AI Traffic commence par la saisie de deux domaines concurrents, puis en cliquant sur « Analyser ».](https://static.semrush.com/blog/uploads/media/52/c1/52c1696e7dd5d91d9f808495b1ce1fab/4c552387d08ebcc4bbd4bce5f9f6004e/original.png)

L'outil AI Traffic commence par la saisie de deux domaines concurrents, puis en cliquant sur « Analyser ».

Vous verrez les données de tous les sites spécifiés. Comme le flux de trafic provenant de différents LLM vers le domaine sélectionné.

![Rapport de trafic IA sur Semrush indiquant le pourcentage de trafic que chaque site saisi reçoit des LLM.](https://static.semrush.com/blog/uploads/media/2f/80/2f8099ff3f943d3b8718ffc214230ef0/2968209b677d986a03932e16874ddbc0/original.png)

Rapport de trafic IA sur Semrush indiquant le pourcentage de trafic que chaque site saisi reçoit des LLM.

La section « Toutes les sources » indique le nombre de visites que chaque domaine a reçues d'un LLM spécifique par rapport aux autres. Il suffit de survoler la barre de répartition du trafic pour en voir le détail.

![La section « Toutes les sources » du rapport AI Traffic indique le nombre de visites reçues par chaque domaine provenant de différents LLM.](https://static.semrush.com/blog/uploads/media/7a/81/7a81d131b9c02aae389b309e30ec712f/33d7d39bb572f1af07b79263e1d4b12c/original.png)

La section « Toutes les sources » du rapport AI Traffic indique le nombre de visites reçues par chaque domaine provenant de différents LLM.

## Comment augmenter le trafic de référence IA vers votre site web

Le fait d'obtenir que les plateformes d'IA citent votre contenu s'appelle [l'optimisation générative des moteurs](https://www.semrush.com/blog/generative-engine-optimization/) (GEO), et c'est similaire au référencement traditionnel mais avec un accent supplémentaire sur les performances techniques et les formats de contenu axés sur les réponses.

Voici les points sur lesquels il faut se concentrer:

### Optimiser la vitesse de la page

Assurez-vous que vos pages Web se chargent rapidement, afin que les robots d'IA puissent explorer (trouver et lire) davantage de vos pages et augmenter leurs chances d'apparaître dans les réponses générées par l'IA.

Ciblez ces points de repère pour [Core Web Vital](https://www.semrush.com/blog/core-web-vitals/) (métriques qui décrivent l'utilisabilité de votre site):

- **Largest Contentful Paint (LCP)**: Temps nécessaire pour que le plus grand élément à l'écran (image ou vidéo, par exemple) s'affiche entièrement après l'ouverture de la page.
- **Interaction avec affichage suivant (INP)**: Délai entre le moment où un utilisateur clique, appuie ou tape et le moment où la page répond visuellement
- **Décalage cumulatif de la mise en page (CLS)**: Mesure le déplacement du contenu pendant le chargement de la page, par exemple lorsque des boutons ou des images changent soudainement de position
![Rapport d'évaluation des indicateurs Web essentiels pour un domaine sur Google PageSpeed Insights.](https://static.semrush.com/blog/uploads/media/aa/90/aa90ab468fb00883e200cefa4141129a/2ed64ff39fb626b2b6041a0db987e753/original.png)

Rapport d'évaluation des indicateurs Web essentiels pour un domaine sur Google PageSpeed Insights.

Faites défiler vers le bas jusqu'aux sections « Insights » et « Diagnostics » pour voir une liste d'éléments que vous pouvez corriger pour améliorer vos [Core Web Vitals](https://www.semrush.com/blog/core-web-vitals/).

![Les sections « Informations » et « Diagnostics » présentent une liste d’éléments qu’un site peut corriger pour améliorer ses indicateurs clés et sa vitesse de chargement.](https://static.semrush.com/blog/uploads/media/13/96/13962b4b5d4f2b2220cfee61f613eaf3/9dd554690cc907b6fcacec4dc22a445b/original.png)

Les sections « Informations » et « Diagnostics » présentent une liste d’éléments qu’un site peut corriger pour améliorer ses indicateurs clés et sa vitesse de chargement.

Certaines solutions sont simples. Par exemple, vous pouvez améliorer la diffusion des images en réduisant la taille des fichiers image.

Une modification telle que la minimisation de JavaScript peut nécessiter l'aide d'un développeur. Mais cela vaut la peine d'être tenté, surtout si l'on considère que les pages riches en JavaScript peuvent être difficiles à afficher pour les LLM.

### Cibler les requêtes de recherche conversationnelle

Ciblez les questions que les gens se posent naturellement (par exemple: « comment faire cuire un brisket le plus rapidement possible? »). au lieu de fragments de mots clés (par exemple, « cuire la poitrine de bœuf rapidement »).

Les systèmes d'IA extraient souvent des réponses directes de contenus qui posent clairement des questions et fournissent des réponses immédiates.

Mettez en forme votre contenu avec:

- Des questions sous forme de sous-titres qui reflètent la façon dont les gens parlent réellement.
- Un langage naturel et une terminologie variée plutôt que des phrases bourrées de mots-clés.
- Réponses directes immédiatement après chaque question et détails complémentaires qui développent la réponse principale.
![Utiliser une question en guise de sous-titre et une réponse directe en langage naturel pour augmenter les chances de citation des LLM.](https://static.semrush.com/blog/uploads/media/dc/53/dc530019a9a694554b6e7f7092f7ffa7/1b173d3ac5d75b73c373f56cafee5161/original.png)

Utiliser une question en guise de sous-titre et une réponse directe en langage naturel pour augmenter les chances de citation des LLM.

Cette approche crée des blocs de contenu que les plateformes d'IA peuvent facilement extraire et attribuer à votre site.

Vous pouvez trouver des mots-clés sous forme de questions en consultant les encadrés « Autres questions posées » dans les résultats de recherche Google.

![Page de résultats de recherche Google (SERP) avec un terme de recherche saisi et la section « Autres questions posées » mise en évidence.](https://static.semrush.com/blog/uploads/media/f3/7b/f37b0ff0a7bf201f6118e983f47feae9/a689cc7afcffd55330bf7f5d60bbb6d8/original.png)

Page de résultats de recherche Google (SERP) avec un terme de recherche saisi et la section « Autres questions posées » mise en évidence.

Ouvrez l'outil et entrez un mot-clé de départ (un terme général lié à votre niche) et cliquez sur « **Questions** » pour des idées de mots-clés.

![Rapport de l'outil Keyword Magic avec le filtre « Questions » appliqué, affichant des idées de mots clés sous forme de questions pour AEO.](https://static.semrush.com/blog/uploads/media/6f/1b/6f1bf021be36651cd8fa270ad166e56e/8882ede282b79e4380f69c124a1bf645/original.png)

Rapport de l'outil Keyword Magic avec le filtre « Questions » appliqué, affichant des idées de mots clés sous forme de questions pour AEO.

### Établir des signaux d'autorité

Les mentions de votre marque ne vous apporteront peut-être pas de trafic de référence direct, mais elles peuvent globalement améliorer votre visibilité dans les LLM et vous aider à développer la notoriété de votre marque.

Une étude de [Leoprd](https://www.leoprd.io/post/leo-report-2025-reputation-to-revenue-building-trust-authority-and-visibility-in-and-ai-era) a révélé que 61,9 % des citations mentionnant une marque proviennent de la couverture éditoriale, des prix et des critiques, et non du contenu publié par la marque elle-même.

Et les mentions organiques sur des forums comme Reddit peuvent aider votre marque à obtenir davantage de mentions au sein des LLM.

Vous pouvez renforcer votre autorité grâce à:

- Recherches originales ou études de données citées par d'autres sites
- Mentions dans des publications de référence et des synthèses d'experts
- Présence de marque cohérente sur toutes les plateformes, avec des liens vers votre site principal
- [Création de backlinks](https://www.semrush.com/blog/link-building/) et de mentions provenant de sites à forte autorité

L'objectif est d'établir votre contenu comme une source primaire que d'autres experts consultent et citent. Ce qui indique aux plateformes d'IA que vous êtes une voix faisant autorité dans votre domaine.

### Implémenter le balisage de schéma

[Balisage Schema](https://www.semrush.com/blog/schema-markup/) (code que vous ajoutez à votre site Web pour aider les robots d'exploration à comprendre son contenu) aide les plateformes d'IA à mieux comprendre votre contenu, ce qui permet aux LLM de citer votre site lorsque cela est pertinent.

Par exemple, l'avis ci-dessous comporte un balisage de schéma qui affiche des informations telles qu'une note en étoiles, le nom du rédacteur de l'avis et une liste de points positifs et négatifs.

![Une fiche SERP avec balisage de schéma affichant une note par étoiles, le nom du rédacteur et une liste de points positifs et négatifs.](https://static.semrush.com/blog/uploads/media/56/e3/56e3b2ac6b1a846bf32df178035bbda6/b15e11686579d9fe5f7bd128dc0bc970/original.png)

Une fiche SERP avec balisage de schéma affichant une note par étoiles, le nom du rédacteur et une liste de points positifs et négatifs.

Pensez à ajouter ces types de schémas à vos pages, le cas échéant:

- Schéma de structure des articles de blog et des guides
- Schéma de la FAQ pour les sections de questions-réponses
- Schéma d'organisation des informations et des identifiants de l'entreprise pour des pages comme la page « À propos ».
- Schéma d'auteur pour les informations et l'expertise de l'auteur
- Schéma produit pour les avis et les recommandations

### Créez du contenu original et utile

Les programmes de maîtrise en droit (LLM) mettent en avant un contenu qui témoigne d'une véritable expertise, et la création de contenu original pourrait améliorer vos chances d'être mentionné dans ces programmes.

Créez du contenu original en:

- Y compris des exemples et des applications pratiques
- Ajouter des données et des résultats de recherche à l'appui de vos propres recherches
- Y compris les opinions personnelles d'experts de votre organisation (comme votre PDG)
- Partager des exemples concrets de clients illustrant comment les gens utilisent votre produit

### Mettez régulièrement à jour votre contenu

Les plateformes d'IA privilégient les contenus récents et à jour, ce qui signifie que maintenir votre contenu à jour pourrait améliorer votre visibilité dans les LLM.

Maintenez le contenu à jour en:

- Mise à jour régulière des statistiques et des données
- Ajout de nouveaux exemples et études de cas
- Mise à jour des captures d'écran et des références d'interface
- Y compris les développements récents dans votre secteur d'activité
- Ajout des dates de publication et des horodatages de « dernière mise à jour »

Établissez un calendrier pour examiner et mettre à jour votre contenu le plus important. La fréquence à laquelle vous effectuerez cette opération dépendra du type de contenu, de votre secteur d'activité et d'autres facteurs.

## Commencez dès aujourd'hui à capter votre trafic de référence IA.

À mesure que de plus en plus de personnes se tournent vers l'IA pour répondre à leurs questions, vous pouvez garder une longueur d'avance sur vos concurrents en suivant le trafic de référence de votre IA et en optimisant pour différentes plateformes d'IA.

Voici votre plan d'action:

1. **Configurez d'abord le suivi.** Créez le filtre regex GA4 et le groupe de canaux personnalisés que nous avons abordés pour commencer à visualiser votre volume réel de trafic IA. On ne peut optimiser ce qu'on ne peut mesurer.
2. **Découvrez quelles plateformes d'IA envoient le plus de trafic à vos concurrents**. Cela vous donne une idée des plateformes pour lesquelles vous pourriez vouloir optimiser en premier.
3. **Vérifiez les bases techniques de vos pages les plus importantes** — vitesse de chargement de la page inférieure à deux secondes, formatage clair des questions-réponses et balisage de schéma approprié. Concentrez-vous sur vos cinq pages les plus performantes qui reçoivent déjà du trafic via les plateformes d'IA.

Vous voulez savoir quelles plateformes d'IA génèrent le plus de trafic pour vos concurrents?

Essayez Semrush dès aujourd'hui.