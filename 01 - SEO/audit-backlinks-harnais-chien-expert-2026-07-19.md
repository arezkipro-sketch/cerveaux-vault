---
type: reference
title: "Audit du profil de backlinks — harnais-chien-expert.fr (liens PBN spam + grille marché des animaux)"
slug: audit-backlinks-harnais-chien-expert
tags: [seo, backlinks, netlinking, harnais-chien-expert, toxic-links, disavow, audit]
sources: ["ubersuggest anchor_texts export 2026-07-19", "[[analyse-penetrabilite-marche-harnais-chien-2026-07-19]]"]
updated: 2026-07-19
---

# Audit du profil de backlinks — harnais-chien-expert.fr

Date : 2026-07-19. Site : harnais-chien-expert.fr (DA 3, 6 backlinks, 5 domaines référents, Ubersuggest). Ce rapport répond à deux demandes : (1) vérifier 4 liens entrants dont l'ancre est un texte publicitaire spam/PBN non sollicité par Arezki, et donner un verdict disavow oui/non ; (2) produire une grille de vérification pour 8 nouveaux backlinks achetés sur une marketplace niche animaux, livraison à venir.

## 0. Résumé exécutif

- **4 des 5 domaines référents actuels** portent une ancre qui est en réalité une publicité auto-promotionnelle pour un service de vente de liens PBN. Ce ne sont pas des liens achetés par Arezki : c'est du démarchage spam classique (des sites qui linkent au hasard en espérant qu'on les paie ensuite). **Verdict : pas de disavow nécessaire à ce stade.**
- Données disponibles : Tier 0 uniquement (Common Crawl + crawler de vérification, confirmé par `backlinks_auth.py --check`). Pas de clé Moz ni Bing configurée sur cette machine, donc pas de DA/Spam Score exact par domaine pour l'instant.
- Les 8 nouveaux liens ne sont pas encore livrés (pas d'URLs disponibles). La grille de la partie 2 est prête à l'emploi dès réception.

---

## 1. Méthodologie et limites (à lire avant le reste)

**Tier de données : Tier 0** (`python scripts/backlinks_auth.py --check --json` exécuté ce jour). Aucune clé Moz ou Bing Webmaster n'est configurée. Confidence par défaut : 0.50 sur tout ce qui vient de Common Crawl.

- Common Crawl interrogé sur `harnais-chien-expert.fr` : le domaine n'est pas présent dans l'index (`in_crawl: false`, `in_rankings: false`). Point important : cela ne veut **pas** dire "autorité faible", cela veut dire que Common Crawl n'a tout simplement pas encore crawlé ce site (normal pour un domaine aussi jeune, avec seulement 6 backlinks). Ce risque de mauvaise interprétation a été vérifié avec le validateur automatique du dépôt claude-seo (`scripts/validate_backlink_report.py`), qui confirme qu'il ne faut pas en tirer de conclusion négative sur l'autorité du site.
- **Limite importante pour la partie 1** : les 4 domaines problématiques ont été identifiés via l'export "anchor_texts" d'Ubersuggest, mais les noms de domaine exacts n'ont pas été transmis, seulement le texte de l'ancre. Sans ces noms, impossible de lancer une vérification automatisée domaine par domaine (Moz, Bing, crawl direct de la page source). Le verdict ci-dessous s'appuie donc sur l'analyse du pattern lui-même (qui est en réalité le signal le plus parlant) et sur la doctrine publique de Google. Si une vérification domaine par domaine est souhaitée (DA réel, follow/nofollow, contenu exact de la page source), transmettre les 4 URLs ou noms de domaine permettra de relancer un audit ciblé.

---

## 2. Partie 1 : audit des 4 domaines spam/PBN

### 2.1 Ce que dit l'ancre elle-même : le signal le plus fort disponible

Ancre relevée (Ubersuggest anchor_texts, texte brut, confidence 0.50 sur l'outil mais le contenu de l'ancre est un fait constaté, pas une inférence) :

> "high quality dofollow backlinks da 50 pa 40 premium pbn network service harnais-chien-expert.com rank first page google fast seo link building buy backlinks online cheap"

Ce n'est pas une ancre normale (nom de marque, mot-clé, URL). C'est littéralement une publicité pour un service de vente de liens, avec le nom de domaine du site inséré dedans. C'est un pattern documenté dans les références du dépôt claude-seo (`skills/seo/references/backlink-quality.md`, liste des 30 indicateurs de liens toxiques) et dans le vault (`wiki/concepts/toxic-backlinks.md`) :

- Pattern proche du #4 : ancre exact-match/promotionnelle répétée sur plusieurs domaines non liés entre eux.
- Pattern #7 : liens provenant de réseaux de liens connus (PBN).
- Pattern #19 : liens provenant de réseaux de vente de liens/guest post de basse qualité.

### 2.2 Le mécanisme réel derrière ces liens

Ces sites ne linkent pas par intérêt éditorial. C'est un schéma de démarchage automatisé très répandu chez les vendeurs de liens low-cost : un réseau (souvent un même opérateur gérant des centaines de domaines expirés ou de sites satellites) crée des pages qui pointent vers des milliers de domaines pris au hasard (scrapés depuis des registrars, des sitemaps publics, ou des sites récemment enregistrés comme celui d'Arezki), avec une ancre qui est en fait leur propre argumentaire commercial. Le but : que le propriétaire du site tombe dessus (via Ubersuggest, Ahrefs ou GSC, comme c'est le cas ici), s'inquiète, et finisse par les payer pour "plus de liens" ou pour un "retrait". C'est une tactique de peur commerciale, pas une attaque ciblée.

### 2.3 Vérifications effectuées (Tier 0, sans les noms de domaine exacts)

| Vérification | Résultat | Source | Confidence |
|---|---|---|---|
| Common Crawl sur harnais-chien-expert.fr | Domaine non indexé dans Common Crawl (trop jeune/petit, pas encore crawlé). Ne permet pas de corroborer ou d'infirmer les 4 domaines spam faute de graphe disponible. | Common Crawl (domain-level) | 0.50 |
| Moz DA/PA/Spam Score des 4 domaines | Non exécutable, pas de clé Moz configurée sur cette machine (Tier 0). | — | n/a |
| Bing Webmaster (liens entrants) | Non exécutable, pas de clé Bing configurée. | — | n/a |
| Crawl direct des 4 pages sources (follow/nofollow, contenu, contexte) | Non exécutable, noms de domaine non fournis. | — | n/a |

Il n'a donc pas été possible de confirmer chaque domaine techniquement, un par un. Ce n'est toutefois pas bloquant pour répondre à la question "disavow ou pas" : le pattern d'ancre suffit à lui seul comme signal diagnostique, et la doctrine Google est claire sur le seuil qui justifie un disavow.

### 2.4 Verdict : pas de disavow nécessaire actuellement

Le raisonnement :

1. **Volume.** 4 liens sur un total de 6 backlinks / 5 domaines référents. En proportion cela semble énorme (80 % du profil), mais en valeur absolue c'est 4 liens. Le disavow est un outil prévu pour de gros volumes de liens toxiques ou face à un signe clair d'attaque de negative SEO ciblée, pas pour quelques liens isolés.
2. **Absence de signature negative SEO.** Une vraie attaque de negative SEO cible un site avec un volume important de liens toxiques concentrés sur une courte période, en général avec des ancres exact-match sur les mots-clés cibles du site attaqué (par exemple "harnais chien pas cher" en masse), pour faire ressembler le profil de liens à du spam volontaire. Ici, l'ancre ne cible même pas les mots-clés de Harnais Chien Expert : elle fait la publicité du service du spammeur lui-même. C'est le signe que ce n'est pas une attaque dirigée, mais du bruit de fond automatisé qui touche des dizaines de milliers de domaines au hasard.
3. **Doctrine publique de Google** (rappelée aussi dans `toxic-backlinks.md` du vault) : ne pas désavouer, sauf gros volume toxique ou negative SEO avérée. Ce type de lien de spam de masse est généralement filtré et ignoré par l'algorithme : il ne transmet pas d'autorité et ne déclenche pas de pénalité algorithmique par sa simple présence.
4. **Coût/bénéfice.** Construire et maintenir un fichier disavow demande du suivi (revérifier, mettre à jour). Sur un profil de 6 backlinks, avec un chantier de netlinking prioritaire à construire (priorité 3 de la roadmap du 2026-07-19), le temps est mieux investi dans l'acquisition de liens de qualité que dans la gestion défensive de 4 liens sans impact réel.

**Recommandations concrètes :**

- Ne rien désavouer pour l'instant.
- Vérifier une fois, 5 minutes, dans Google Search Console : Sécurité et actions manuelles, pour confirmer l'absence de pénalité liée au spam de liens. C'est le seul signal qui changerait ce verdict.
- Ne jamais répondre ni payer si ces sites (ou des sites similaires) proposent un formulaire de "retrait de lien contre paiement". Toute interaction confirme que l'adresse est surveillée et peut générer davantage de sollicitations.
- Surveiller, pas agir : si ce type de lien PBN passe d'un phénomène ponctuel (4 liens) à un afflux répété et croissant (par exemple 20 à 30 nouveaux domaines de ce type en quelques semaines), la nature du problème change (volume) et justifierait de reconsidérer un disavow ciblé. Refaire cette vérification via l'export Ubersuggest anchor_texts tous les 1 à 2 mois suffit à ce stade.
- Si une vérification technique domaine par domaine est souhaitée (DA réel via Moz gratuit, follow/nofollow, contenu de la page source), transmettre les 4 noms de domaine exacts permettra d'activer Moz (clé API gratuite, 2 500 lignes/mois, voir `/seo backlinks setup`) et de relancer un audit en Tier 1.

---

## 3. Partie 2 : grille de vérification des 8 backlinks "marché des animaux"

À appliquer dès réception des URLs (probablement sous forme d'un rapport de livraison de la marketplace). Objectif : distinguer un bon achat ciblé pet/animaux d'un nouveau réseau PBN déguisé en marketplace propre.

### 3.1 Grille par lien (à remplir pour chacun des 8)

| # | Critère | Ce qu'il faut voir | Seuil / signal d'alerte | Comment vérifier |
|---|---|---|---|---|
| 1 | Pertinence thématique du site source | Site dédié animaux/chiens (blog canin, forum d'éleveurs, pension, éducateur, e-commerce animalier) | Alerte si site généraliste hors sujet (finance, tech, casino, "actualités" fourre-tout) ou multi-thématique décousu (signe de PBN/réseau de liens) | Visiter le site, regarder les 5 à 10 derniers articles publiés : sont-ils tous sur des sujets différents sans cohérence ? |
| 2 | Autorité minimale acceptable | DA/DR du site source nettement supérieur au DA3 actuel du site | Un lien depuis un site DA 15-25+ est déjà utile ; en dessous de DA 10, l'apport est marginal. Attention : DA élevé (50+) sur un site créé récemment ou sans trafic réel = DA gonflé artificiellement, à traiter comme un signal négatif, pas un bonus | Moz Link Explorer gratuit, ou Ahrefs Free Backlink Checker (benchmark PME du vault : DR > 30 = belle opportunité) |
| 3 | Trafic réel (pas juste un DA gonflé) | Trafic organique mensuel réel, même modeste (quelques centaines de sessions) | Alerte si DA élevé mais trafic proche de zéro : signe classique de PBN (domaine expiré racheté pour son autorité historique, sans audience réelle) | Ubersuggest ou Semrush sur le domaine (trafic organique estimé) ; à défaut, similarweb.com en gratuit donne un ordre de grandeur |
| 4 | Follow vs nofollow | Vérifier l'attribut du lien dans le code source de la page qui linke vers le site | Un lot de 8 liens tous nofollow n'a quasi aucune valeur SEO directe (pas de transfert d'autorité). Acceptable seulement si annoncé clairement et facturé en conséquence par le vendeur | Clic droit, "Afficher le code source" sur la page, chercher `rel="nofollow"` sur le lien concerné |
| 5 | Ancre utilisée | Mélange naturel : marque ("Harnais Chien Expert"), URL nue, ancre générique ("en savoir plus", "ce site"), ancre semi-optimisée | Alerte si plusieurs des 8 liens utilisent la même ancre exact-match "harnais chien" ou des variantes trop proches : sur-optimisation détectable par Google. Benchmark e-commerce du vault : ancres exactes 5-10 % max, ancres marque/générique 35-45 % et plus | Lire l'ancre exacte de chacun des 8 liens une fois livrés, comparer à cette répartition |
| 6 | Contexte éditorial de la page | Lien inséré dans un article de fond, cohérent avec le sujet (exemple : "guide pour choisir un harnais anti-traction" dans un article sur l'éducation canine) | Alerte si le lien est noyé dans une longue liste de liens sortants sans rapport entre eux ("page ressources" fourre-tout, ou page créée uniquement pour héberger des liens vendus) | Lire la page entière, compter les liens sortants : au-delà de 10-15 liens vers des sites sans rapport entre eux, c'est un signal de "page vendue à plusieurs clients" |
| 7 | Âge et historique du domaine | Domaine à l'historique cohérent, pas un domaine expiré racheté récemment juste pour son autorité passée | Alerte si le site a manifestement changé de thématique (whois montre un enregistrement récent, mais la Wayback Machine montre un tout autre sujet il y a 2 ans) | web.archive.org/web/*/domaine.com (gratuit) et whois domaine.com |
| 8 | Vitesse d'apparition / groupage | Les 8 liens apparaissent de façon échelonnée sur plusieurs jours ou semaines, pas tous le même jour sur le même type de site | Alerte si les 8 liens apparaissent exactement le même jour et proviennent de sites qui se ressemblent trop (même thème visuel, même CMS, même structure de page) : signe de réseau privé plutôt que de marketplace de sites réellement indépendants | Comparer les dates de première détection dans Ubersuggest/GSC sur les 2-3 semaines suivant la livraison |
| 9 | Indexation Google de la page qui linke | La page qui linke doit être indexée par Google, sinon le lien ne compte pour rien | Alerte si `site:URL-exacte-de-la-page` ne remonte aucun résultat | Recherche Google `site:domaine.com/chemin-de-la-page` |
| 10 | Diversité des hébergeurs entre les 8 sites | Les 8 sites ne devraient pas tous être hébergés sur la même IP ou le même petit bloc d'IP | Alerte si plusieurs sites partagent la même IP : même propriétaire déguisé en "marketplace multi-sites" | Outil gratuit type whatsmyip.org, ou commande nslookup/dig sur chaque domaine |

### 3.2 Verdict global à produire une fois les 8 liens livrés

Compter combien de liens sur 8 passent les critères 1, 2, 3, 4, 7 et 9 (les critères les plus factuels, sans marge d'interprétation) :

- **7-8/8 OK** : achat de qualité, à traiter comme un socle solide pour la priorité 3 de la roadmap netlinking (voir `analyse-penetrabilite-marche-harnais-chien-2026-07-19.md`).
- **4-6/8 OK** : lot mitigé. Garder les bons liens, surveiller les faibles, ne pas racheter chez ce fournisseur pour un futur lot.
- **0-3/8 OK** : lot proche du profil PBN détecté en partie 1. Ne pas racheter chez ce fournisseur. Pas de disavow immédiat (même logique qu'en partie 1 : petit volume), mais à surveiller de près si combiné aux 4 liens spam déjà présents.

Point d'attention spécifique à ce dossier : le profil actuel compte déjà 4 liens PBN de bruit en toile de fond. Si les 8 nouveaux liens s'avèrent également faibles ou de type PBN, le site se retrouverait avec 12 liens sur environ 13 domaines référents qui ne sont pas de qualité. Ce volume commencerait à justifier de reconsidérer la question du disavow, ce qui n'est pas encore le cas aujourd'hui.

---

## 4. Priorisation des actions

| Priorité | Action | Effort |
|---|---|---|
| Haute | Vérifier GSC : Sécurité et actions manuelles (une fois) pour écarter toute pénalité liée aux 4 liens spam | 5 min |
| Haute | Appliquer la grille de la section 3.1 dès réception des 8 nouveaux liens, avant de considérer l'achat comme validé | 30-45 min une fois livré |
| Moyenne | Transmettre les 4 noms de domaine des liens PBN pour une vérification technique complète (activer Moz gratuit, Tier 1) | 15 min de mise en place, 10 min d'analyse |
| Basse | Ne rien désavouer pour l'instant : aucun fichier disavow à créer | — |
| Basse | Renouveler l'export Ubersuggest anchor_texts tous les 1 à 2 mois pour surveiller l'évolution du volume de liens spam entrants | 5 min/mois |

---

## 5. Sources et confidence

| Donnée | Source | Confidence | Fraîcheur |
|---|---|---|---|
| 6 backlinks / 5 domaines référents, ancre spam PBN sur 4 domaines | Ubersuggest (export anchor_texts fourni par Arezki), confirmation orale qu'aucun achat n'a été fait | 0.50 (outil tiers, non recroisé) | 2026-07-19 |
| Domaine non trouvé dans Common Crawl | Common Crawl (domain-level graph, `commoncrawl_graph.py`) | 0.50 | Release cc-main-2026-jan-feb-mar (trimestrielle) |
| DA/PA/Spam Score des 4 domaines spam | Non disponible (Tier 0, Moz/Bing non configurés sur cette machine) | n/a | n/a |
| Doctrine disavow Google / pattern PBN | Connaissance SEO générale, croisée avec `wiki/concepts/toxic-backlinks.md` et `skills/seo/references/backlink-quality.md` du dépôt claude-seo | Référence méthodologique, pas une mesure chiffrée | — |
| Roadmap netlinking / écart DA vs concurrents | `analyse-penetrabilite-marche-harnais-chien-2026-07-19.md` (même vault) | Document interne déjà validé le même jour | 2026-07-19 |

---

## 6. Ce qui manque pour aller plus loin

- Les 4 noms de domaine exacts des liens PBN spam, pour une vérification Moz/Bing/crawl direct ciblée.
- Activation de la clé Moz API gratuite (`/seo backlinks setup`) pour passer en Tier 1 et disposer d'un DA/Spam Score réel plutôt que d'une estimation Ubersuggest sur l'ensemble du profil.
- Les URLs des 8 nouveaux liens dès leur livraison, pour appliquer la grille de la section 3.

---

Rappel : ce chantier ne remplace pas la priorité 3 de la roadmap (`analyse-penetrabilite-marche-harnais-chien-2026-07-19.md`), qui reste l'action structurante : obtenir 4 à 6 nouveaux domaines référents de qualité sur 90 jours. Cet audit sert à protéger l'existant (partie 1) et à s'assurer que les 8 liens achetés (partie 2) contribuent réellement à cet objectif plutôt que d'ajouter du bruit supplémentaire au profil.
