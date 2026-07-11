# Le Site Shopify — Configuration, Paiements, Email & SMS

> La publicité a fait son travail. Mais ce clic n'est qu'une étape. Une fois sur le site, l'émotion doit être prolongée, amplifiée, et convertie en achat.

Le site n'est pas un simple catalogue produit. C'est le **prolongement direct de ta publicité** — il doit raconter la même histoire, dans le même ton, avec la même énergie. Un prospect qui arrive sur une page qui casse cette dynamique, c'est une vente perdue.

---

## A. Configuration de base

### L'abonnement Shopify

| Plan | Quand l'utiliser |
|---|---|
| **Basic** | Suffisant au lancement. Tout peut être mis en place, premières ventes sans limitation réelle. |
| **Growth** | Dès que tu travailles avec un associé ou des virtual assistants (plusieurs accès employés). |
| **Advanced** | Dès que tu scales sérieusement — compare régulièrement tes frais avec ce plan. À partir d'un certain volume de CA, les frais réduits par commande le rendent plus avantageux que le Basic. |
| **Plus** | Inutile dans la quasi-totalité des cas, même à très gros volume. Le seul avantage réel est la personnalisation du checkout, mais celui de base est déjà très bien optimisé pour la conversion. |

### Le thème

Le thème est souvent un sujet sur lequel les débutants passent trop de temps. **Ce n'est pas là que se gagne ou se perd une vente.**

Ce qui compte : un thème rapide, épuré, cohérent avec ton branding, qui ne nécessite pas une dizaine d'applications supplémentaires.

**Recommandation :** [Story](https://www.story-theme.com/?via=Rayane) — 20 €/mois, propre, bien structuré et suffisant pour lancer sérieusement.

**Tip concret :** Claude est aujourd'hui extrêmement puissant pour reproduire des sections de site entières à partir d'un simple screenshot. Tu vois une section qui te plaît sur le site d'un concurrent ? Tu fais un screen, tu le colles dans Claude, et il te génère le code correspondant en quelques secondes. C'est un gain de temps massif pour construire ou améliorer ton site sans aucune compétence technique.

⚠️ **À éviter dans le code Liquid :** tout ce qui est sensible (bundles, panier, etc.) — favoriser des apps pour ça, beaucoup plus simple pour éviter des bugs. La majorité sont gratuites jusqu'à un certain volume de vente.

### ⚠️ Retirer la taxe automatique de Shopify (tip important et peu connu)

Shopify prélève automatiquement une taxe sur chaque commande. La majorité des e-commerçants ne le savent pas et laissent de l'argent partir. Sur de gros volumes, ça représente une somme significative.

**Comment la désactiver :**
```
Paramètres → Taxes et frais de douane
→ Sélectionner tous les pays dans lesquels tu vends
→ Rétrograder le service → Manual Tax

Si tu vends en France/Belgique/Espagne/Italie/EU → sélectionne "Union Européenne"
(couvre l'ensemble des marchés d'un coup)
```

### Le nom de domaine

**N'achète pas ton nom de domaine via Shopify.** Ce n'est pas leur cœur de métier — moins de flexibilité, moins de contrôle.

Passe par un registrar externe et choisis **obligatoirement un .com**.

Pourquoi le .com ?
- Préserve ton anonymat (contrairement aux extensions nationales .fr/.de où les infos du propriétaire sont plus accessibles)
- Inspire confiance universellement, peu importe le marché
- N'impacte pas négativement la conversion, même si tu vends en France ou en Espagne

**Plateformes recommandées :**
- **Namecheap** → meilleur choix si tu veux un maximum d'anonymat
- **Ionos** → bonne alternative

❌ Évite les hébergeurs français comme OVH, LWS ou O2Switch si l'anonymat est une priorité.

---

## B. Les processeurs de paiement

Les processeurs de paiement sont le nerf de la guerre en e-commerce. Si tu te fais bloquer, c'est ton cashflow qui s'arrête — et dans certains cas, des fonds peuvent être gelés pendant plusieurs mois.

### La combinaison recommandée

**Shopify Payments + PayPal**

C'est la configuration la plus stable et la plus simple à maintenir. Elle couvre la quasi-totalité des situations au lancement et pendant le scaling.

⚠️ **Stripe** peut être ajouté en backup, mais avec précaution. **Stripe peut geler tes fonds pendant 6 mois** sans garantie de les récupérer. Ne l'utilise pas en processeur principal.

### Règles à respecter absolument

- Ne scale pas trop fort trop vite si ton processeur a **moins de 3 à 6 mois d'ancienneté**. Une croissance trop brutale déclenche des vérifications automatiques et peut entraîner un blocage.
- Si tu te fais bloquer Shopify Payments + PayPal + Stripe simultanément, tu entres dans une spirale de problèmes difficile à gérer. **Préserve tes comptes.**

✅ Il est possible de recréer un nouveau Shopify Payments, PayPal ou Stripe pour chaque nouvelle société créée. Mais ne compte pas là-dessus comme stratégie principale — mieux vaut maintenir des comptes sains dès le départ.

---

## C. Email & SMS Marketing

Une fois ton testing validé et ta boutique qui commence à tourner (5k/jour), deux leviers sont à mettre en place rapidement : **l'email et le SMS**.

Ce sont les canaux les plus sous-estimés en e-commerce, et pourtant ils représentent une part significative du CA total sur les boutiques qui les exploitent correctement.

**La logique :** Meta Ads te permet de scaler vite et de construire rapidement une base de données clients. Une fois cette base constituée, l'email et le SMS te permettent de la monétiser à un CPA bien inférieur à celui de la publicité payante. **Tu as déjà payé pour acquérir ces clients — autant les faire racheter sans repayer Meta à chaque fois.**

L'email marketing peut représenter jusqu'à **30% du chiffre d'affaires** pour des coûts infiniment inférieurs à ceux du cold traffic Meta.

### L'email marketing (Klaviyo)

**Outil à utiliser : Klaviyo** — la référence en email marketing e-commerce, intégré nativement à Shopify.

**Les 2 flows indispensables à mettre en place dès que le testing est validé :**

#### Flow panier abandonné

Beaucoup de clients ajoutent un produit au panier sans finaliser. Ce flow les relance automatiquement avec une séquence progressive :

| Email | Moment | Contenu |
|---|---|---|
| Email 1 | 30 min après l'ajout au panier | Simple rappel |
| Email 2 | 2h après | Réduction de 10% + urgence de stock |
| Email 3 | 24h après | Réduction de 20%, ton personnel, envoyé comme si c'était le fondateur de la marque |

#### Flow post-achat

**Rôle :** rassurer le client à chaque étape après son achat.

- Moins de questions au SAV
- Plus de confiance
- Des clients qui rachètent avant même d'avoir reçu leur première commande

### Le SMS marketing

Le SMS est un canal direct, ultra peu saturé, avec des taux d'ouverture sans commune mesure avec l'email. Là où un email peut rester non lu pendant des heures, un SMS est lu en moyenne dans les **3 minutes** suivant sa réception.

Mis en place au bon moment (une fois ta boutique qui tourne et ta base client constituée), il génère un ROI très solide à un CPA bien inférieur à Meta Ads.
