# Exercices - Python OO

## Composition & Agrégation

On modélise des bons de commande, sur le même principe que les commandes de vente d'Odoo.
> Produit : reference, nom, prix_unitaire.

Client : nom, email.
Catalogue : regroupe des produits existants.
• ajouter(produit) et chercher(reference) (retourne le produit ou None).
LigneCommande : un produit et une quantite.
• Propriété sous_total = prix × quantité.
Commande : un numero, un client et une liste privée de lignes.
• ajouter(produit, quantite) crée la ligne elle-même. Si le produit est déjà dans la commande, on augmente la quantité au lieu de créer une 2e ligne.
• retirer(reference) supprime la ligne de ce produit.
• Propriété lignes → un tuple des lignes (lecture seule).
• Propriété total et __len__ (nombre de lignes).
• __str__ affiche le bon de commande complet.
Règle importante : main.py ne crée jamais de LigneCommande directement. Seule Commande en fabrique.

Dans main.py
1. Remplissez un catalogue : Clavier (49,90 €), Souris (19,90 €), Écran (189,00 €).
2. Créez deux clients, Alice et Bob.
3. Commande C001 pour Alice : 2 claviers, 1 souris, puis encore 1 clavier.
4. Commande C002 pour Bob : 1 écran et 2 souris (récupérés via catalogue.chercher).
5. Affichez les deux commandes.
6. Supprimez C001 avec del, puis prouvez que le clavier existe toujours dans le catalogue et qu'Alice existe toujours.

Résultat attendu
Commande C001 — Alice (alice@mail.be)
  CLA-01  Clavier  3 × 49.90 € =  149.70 €
  SOU-01  Souris   1 × 19.90 € =   19.90 €
  Total : 169.60 € (2 lignes)

Commande C002 — Bob (bob@mail.be)
  ECR-01  Écran    1 × 189.00 € = 189.00 €
  SOU-01  Souris   2 × 19.90 €  =  39.80 €
  Total : 228.80 € (2 lignes)

C001 supprimée. Toujours au catalogue : Clavier. Toujours client : Alice.

Questions (à répondre en commentaire dans main.py)
1. Pour chaque relation, composition ou agrégation ? Justifiez en une phrase : Catalogue–Produit, Commande–Client, Commande–LigneCommande, LigneCommande–Produit.
2. Pourquoi lignes renvoie-t-il un tuple plutôt que la liste elle-même ?
3. Passez le prix de la souris à 24,90 € après avoir créé C002. Que devient son total ? Est-ce le comportement voulu pour une commande déjà passée ?
Bonus
• Corrigez le problème de la question 3 : la ligne mémorise le prix au moment de l'ajout.
• Ajoutez une remise en % par ligne, appliquée dans sous_total.