# Brief — Vérification des prix d'achat AliExpress (Harnais Chien Expert)

## Contexte
- Boutique Shopify : https://harnais-chien-expert.fr — **NE MODIFIER AUCUN PRIX**, analyse uniquement.
- Une 1re analyse existe : `tracking/analyse-prix-aliexpress-2026-10-05.xlsx` (76 produits), générée par `tracking/analyse_prix_aliexpress.py`.
- Limite de cette analyse : AliExpress était bloqué par le réseau. La colonne D « Prix AliExpress » contient le **coût par article Shopify** (taille M), marqué NON VÉRIFIÉ. La colonne E n'a que des liens de recherche par mots-clés.

## Mission
Remplacer les prix non vérifiés par les vrais prix AliExpress, produit par produit.

1. **Catalogue** : `https://harnais-chien-expert.fr/products.json?limit=250` (titre, URL, prix le plus bas, prix barré, `images[0].src`). Croiser avec l'onglet « Analyse prix » (colonnes S = URL boutique, T = URL photo).
2. **Recherche AliExpress** (Playwright, fr.aliexpress.com, livraison France, EUR) :
   - Recherche par image (icône appareil photo) avec la photo principale.
   - Si échec : mots-clés anglais (colonne R du fichier).
   - Garder les 3 annonces les plus ressemblantes, priorité ventes élevées + note ≥ 4,5.
   - Relever le prix taille M (ou médiane) et l'URL de chaque annonce.
   - Rien de clair → « NON TROUVÉ ». Ne jamais inventer.
   - Captcha → pause, puis continuer plus lentement. Ne pas abandonner.
   - Paralléliser : 1 agent par lot d'environ 10 produits.
3. **Mettre à jour l'Excel** : colonne D = meilleur prix trouvé, E = URL de l'annonce, Q = « VÉRIFIÉ » / « NON TROUVÉ », et ajouter les 2 autres annonces en commentaire ou dans de nouvelles colonnes. Le plus simple : adapter `analyse_prix_aliexpress.py` pour lire un CSV `produit;prix_ali;url1;url2;url3` et regénérer le fichier (les prix recommandés en dépendent).

## Règles de calcul (déjà dans le script)
- Coût de revient = prix Ali + 1,99 € si < 10 € + 3,60 € de taxe (toujours). Coefficient = prix TTC / coût.
- Coefficient minimum 2,5. Paliers : entrée 34,99–39,99 · cœur 44,99–49,99 · premium 59,99 max. Tactique → 39,99–44,99 si la marge le permet.
- Prix barrés réalistes (-15 à -25 %), conformes Omnibus (prix le plus bas des 30 derniers jours).
- Concurrents : Ruffwear Front Range ~60 € · Julius-K9 IDC dès ~24 € · Truelove 36–80 € · Rabbitgoo Amazon 27–41 € · Dog Copenhagen 38–50 €.

## Livrable
- Excel mis à jour (même structure : onglets Analyse prix / Résumé / Méthode).
- Liste des écarts > 20 % entre le coût Shopify et le vrai prix AliExpress.
- Entrée dans `log.md` : `## [YYYY-MM-DD] query | ...`, puis commit.
