# Exercices - Python OO


## Exercice 2 — Composition vs agrégation : bons de commande

### Énoncé
 
On modélise des bons de commande, sur le même principe que les commandes de vente d'Odoo.
 
**`Produit`** : `reference`, `nom`, `prix_unitaire`.
 
**`Client`** : `nom`, `email`.
 
**`Catalogue`** : regroupe des produits existants.
 - `ajouter(produit)` et `chercher(reference)` (retourne le produit ou `None`).

**`LigneCommande`** : un produit et une `quantite`.
- Propriété `sous_total` = prix × quantité.

**`Commande`** : un `numero`, un `client` et une liste **privée** de lignes.
 
- `ajouter(produit, quantite)` crée la ligne elle-même. Si le produit est déjà dans la commande, on augmente la quantité au lieu de créer une 2e ligne.
- `retirer(reference)` supprime la ligne de ce produit.
- Propriété `lignes` → un **tuple** des lignes (lecture seule).
- Propriété `total` et `__len__` (nombre de lignes).
- `__str__` affiche le bon de commande complet.
Règle importante : `main.py` ne crée **jamais** de `LigneCommande` directement. Seule `Commande` en fabrique.
 
**Dans `main.py`**
 
1. Remplissez un catalogue : Clavier (49,90 €), Souris (19,90 €), Écran (189,00 €).
2. Créez deux clients, Alice et Bob.
3. Commande C001 pour Alice : 2 claviers, 1 souris, puis encore 1 clavier.
4. Commande C002 pour Bob : 1 écran et 2 souris (récupérés via `catalogue.chercher`).
5. Affichez les deux commandes.
6. Supprimez C001 avec `del`, puis prouvez que le clavier existe toujours dans le catalogue et qu'Alice existe toujours.
### Résultat attendu
 
```
Commande C001 — Alice (alice@mail.be)
  CLA-01  Clavier  3 × 49.90 € =  149.70 €
  SOU-01  Souris   1 × 19.90 € =   19.90 €
  Total : 169.60 € (2 lignes)
 
Commande C002 — Bob (bob@mail.be)
  ECR-01  Écran    1 × 189.00 € = 189.00 €
  SOU-01  Souris   2 × 19.90 €  =  39.80 €
  Total : 228.80 € (2 lignes)
 
C001 supprimée. Toujours au catalogue : Clavier. Toujours client : Alice.
```
 
### Questions (à répondre en commentaire dans `main.py`)
 
1. Pour chaque relation, composition ou agrégation ? Justifiez en une phrase : Catalogue–Produit, Commande–Client, Commande–LigneCommande, LigneCommande–Produit.
2. Pourquoi `lignes` renvoie-t-il un tuple plutôt que la liste elle-même ?
3. Passez le prix de la souris à 24,90 € après avoir créé C002. Que devient son total ? Est-ce le comportement voulu pour une commande déjà passée ?
### Bonus
 
- Corrigez le problème de la question 3 : la ligne mémorise le prix au moment de l'ajout.
- Ajoutez une remise en % par ligne, appliquée dans `sous_total`.


## Exercice 3 — Data classes : gestion de stock

### Énoncé
 
On gère le stock d'un entrepôt. Toutes les classes de l'exercice sont des data classes : pas de `__init__`, `__repr__` ni `__eq__` écrits à la main.
 
**`Adresse`** — non modifiable
- `rue`, `code_postal`, `ville`.

**`Article`** 
- `reference`, `nom`, `prix` (float), `quantite` (int, 0 par défaut), `tags` (liste de str, vide par défaut).
- Les `tags` ne comptent pas dans la comparaison `==`.
- `__post_init__` : lève une `ValueError` si le prix est ≤ 0 ou la quantité négative ; met le nom en forme (`"  clavier "` → `"Clavier"`).
- Propriété `valeur_stock` = prix × quantité.

**`MouvementStock`** — non modifiable et triable 
- `date` (`datetime.date`), `reference` (de l'article), `quantite` (positive = entrée, négative = sortie).
- Trier une liste de mouvements doit les ranger par date.

**`Entrepot`** 
- `nom`, `adresse` (une `Adresse`), `articles` (liste vide par défaut).
- `ajouter(article)`, `valeur_totale()`, `en_rupture()` → la liste des articles à quantité 0.

**Dans `main.py`** 
1. Créez une adresse, puis essayez de modifier sa ville. Capturez l'erreur.
2. Créez 4 articles : Clavier (49,90 € × 10), Souris (19,90 € × 25), Écran (189 € × 0), Casque (79 € × 4). Affichez-en un avec `print`.
3. Créez un 2e clavier identique mais avec d'autres tags. Comparez-les avec `==` puis avec `is`.
4. Tentez de créer un article à -5 €. Capturez l'erreur.
5. Ajoutez les 4 articles à un entrepôt ; affichez sa valeur totale et les articles en rupture.
6. Créez 4 mouvements dans le désordre, triez-les avec `sorted()` et affichez-les.
### Résultat attendu
 
```
Modification refusée : cannot assign to field 'ville'
Article(reference='CLA-01', nom='Clavier', prix=49.9, quantite=10, tags=['bureautique'])
== : True | is : False
Article invalide : Le prix doit être positif (reçu : -5)
Entrepôt Nord — valeur totale : 1312.50 €
En rupture : ['Écran']
MouvementStock(date=datetime.date(2026, 9, 28), reference='ECR-01', quantite=-3)
MouvementStock(date=datetime.date(2026, 10, 2), reference='CLA-01', quantite=10)
MouvementStock(date=datetime.date(2026, 10, 5), reference='SOU-01', quantite=-5)
MouvementStock(date=datetime.date(2026, 10, 12), reference='CAS-01', quantite=4)
```


## Exercice 4 — Exceptions personnalisées : la banque

### Énoncé
 
On reprend le compte bancaire de la démo encapsulation. Plus aucun `print("Erreur...")` ni `return False` dans les modèles : chaque problème lève une exception métier, et c'est `main.py` qui décide quoi afficher.
 
**Hiérarchie à créer** (dans `models/exceptions.py`)
 
```
BanqueError
├── MontantInvalideError
├── SoldeInsuffisantError     → attributs : disponible, demande, manque (propriété)
├── CompteBloqueError         → attribut : numero
└── CompteIntrouvableError    → attribut : numero
```
 
Chaque exception construit elle-même son message à partir de ses attributs.
 
**`Compte`**
- `numero`, `titulaire`, solde privé, `decouvert_autorise` (0 par défaut), `bloque` (False par défaut).
- `deposer(montant)` et `retirer(montant)` : `MontantInvalideError` si montant ≤ 0, `CompteBloqueError` si le compte est bloqué, `SoldeInsuffisantError` si le retrait dépasse solde + découvert.
- `bloquer()` / `debloquer()`.

**`Banque`**
- Un dictionnaire privé `{numero: Compte}`.
- `ouvrir(compte)` et `trouver(numero)`. `trouver` attrape la `KeyError` du dictionnaire et lève à la place une `CompteIntrouvableError`, chaînée avec `from`.
- `virement(source, destination, montant)` : retire puis dépose. Si le dépôt échoue, le retrait doit être annulé, puis l'exception relancée. Un virement est tout ou rien.

**Dans `main.py`**
Ouvrez deux comptes : BE01 (Alice, 500 €, découvert 100 €) et BE02 (Bob, 50 €). Puis traitez cette liste d'opérations dans une boucle, avec un seul bloc `try/except/else/finally` :
 
```python
operations = [
    ("depot", "BE01", -20),
    ("retrait", "BE01", 700),
    ("retrait", "BE01", 550),
    ("bloquer", "BE02", 0),
    ("virement", "BE01", "BE02", 30),
    ("virement", "BE01", "BE99", 30),
]
```
 
- `except` spécifique pour `SoldeInsuffisantError` : afficher combien il manque.
- `except` spécifique pour `CompteIntrouvableError` : afficher aussi le type de sa cause (`e.__cause__`).
- `except BanqueError` pour toutes les autres erreurs métier.
- `else` : afficher "OK" ; `finally` : compter les opérations traitées.
À la fin, affichez les deux soldes et le bilan.
 
### Résultat attendu
 
```
1. depot BE01 -20         → ERREUR : Montant invalide : -20.00 €
2. retrait BE01 700       → ERREUR : Solde insuffisant sur BE01 (disponible 600.00 €, demandé 700.00 €) — il manque 100.00 €
3. retrait BE01 550       → OK
4. bloquer BE02           → OK
5. virement BE01 → BE02 30 → ERREUR : Le compte BE02 est bloqué
6. virement BE01 → BE99 30 → ERREUR : Compte BE99 introuvable (cause : KeyError)
Soldes : BE01 = -50.00 € | BE02 = 50.00 €
Bilan : 6 opérations, 2 réussies, 4 échouées
```
 
Le solde de BE01 reste à -50 € après l'opération 5 : la preuve que le virement a bien été annulé.

## Exercice 5 — Énumérations : helpdesk

 
### Énoncé
 
Un service informatique gère ses tickets de support. Aucune chaîne de caractères ne doit servir à représenter un statut, une priorité ou une catégorie : uniquement des énumérations.
 
**`Priorite`** (`IntEnum`) : `BASSE` = 1, `NORMALE` = 2, `HAUTE` = 3, `CRITIQUE` = 4.
 
- Propriété `delai_heures` : 72, 24, 8 et 2 h.
**`Categorie`** (`Enum` avec `auto()`) : `MATERIEL`, `LOGICIEL`, `RESEAU`, `COMPTE`.
 
**`Statut`** (`Enum`) : la valeur est le libellé affiché.
 
| Membre | Valeur | Peut passer à |
| --- | --- | --- |
| `NOUVEAU` | "Nouveau" | `EN_COURS`, `FERME` |
| `EN_COURS` | "En cours" | `EN_ATTENTE`, `RESOLU` |
| `EN_ATTENTE` | "En attente client" | `EN_COURS` |
| `RESOLU` | "Résolu" | `FERME`, `EN_COURS` (réouverture) |
| `FERME` | "Fermé" | — |
 
- Méthode `peut_passer_a(autre)` → bool, basée sur ce tableau.
- Propriété `est_termine` → `True` pour `RESOLU` et `FERME`.
**`Ticket`**
 
- `numero`, `titre`, `priorite`, `categorie`, `statut` (`NOUVEAU` au départ), un historique des statuts.
- `changer_statut(nouveau)` : lève une `ValueError` si la transition est interdite, sinon change le statut et l'ajoute à l'historique.

**`Helpdesk`**
- `ajouter(ticket)`.
- `par_priorite()` → tickets du plus urgent au moins urgent.
- `repartition()` → un dictionnaire `{Statut: nombre}` contenant **tous** les statuts, même ceux à 0.

**Dans `main.py`**
1. Affichez tous les libellés de statut en parcourant l'énumération (pas de liste écrite à la main).
2. Créez 4 tickets : #1 Serveur mail en panne (`CRITIQUE`, `RESEAU`), #2 Imprimante bloquée (`NORMALE`, `MATERIEL`), #3 VPN instable (`HAUTE`, `RESEAU`), #4 Nouveau fond d'écran (`BASSE`, `LOGICIEL`).
3. Faites passer #1 par `EN_COURS`, `RESOLU` puis `FERME` ; #2 par `EN_COURS` puis `EN_ATTENTE`.
4. Tentez de passer #3 directement à `RESOLU`. Capturez l'erreur.
5. Affichez les tickets par priorité, puis la répartition.
6. Convertissez des saisies utilisateur en priorité : `"haute"`, `4` et `"urgente"` (cette dernière doit être gérée proprement).
7. Affichez l'historique de #1.
### Résultat attendu
 
```
Statuts : Nouveau, En cours, En attente client, Résolu, Fermé
Transition refusée pour #3 : Nouveau → Résolu
Tickets par priorité :
  #1 CRITIQUE (2 h)  — Serveur mail en panne — Fermé
  #3 HAUTE (8 h)     — VPN instable — Nouveau
  #2 NORMALE (24 h)  — Imprimante bloquée — En attente client
  #4 BASSE (72 h)    — Nouveau fond d'écran — Nouveau
Répartition : Nouveau: 2 | En cours: 0 | En attente client: 1 | Résolu: 0 | Fermé: 1
"haute" → HAUTE | 4 → CRITIQUE | "urgente" → priorité inconnue
Historique #1 : Nouveau → En cours → Résolu → Fermé
```
 