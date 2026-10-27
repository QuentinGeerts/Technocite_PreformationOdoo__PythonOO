from models import Catalogue, Produit, Client, Commande

# 1.  Catalogue
catalogue = Catalogue()
catalogue.ajouter(Produit("CLA-01", "Clavier", 49.9))
catalogue.ajouter(Produit("SOU-01", "Souris", 19.9))
catalogue.ajouter(Produit("ECR-01", "Écran", 189.0))

clavier = catalogue.chercher("CLA-01")
souris = catalogue.chercher("SOU-01")
ecran = catalogue.chercher("ECR-01")

# 2.  Clients
alice = Client("Alice", "alice@test.com")
bob = Client("Bob", "bob@test.com")

# 3.  Commande d'Alice
c001 = Commande("C001", alice)
if clavier and souris:
  c001.ajouter(clavier, 2)
  c001.ajouter(souris, 1)
  c001.ajouter(clavier, 1)

# 4.  Commande de Bob
c002 = Commande("C002", bob)
if ecran and souris:
  c002.ajouter(ecran, 1)
  c002.ajouter(souris, 2)

# 5.  Affichage
print(c001)
print(c002)

# 6.  Suppression de la commande C001
del c001
print(f"C001 supprimée. Toujours au catalogue : {catalogue.chercher('CLA-01').nom}. Toujours client : {alice.nom}.")

# Question 3
souris.prix_unitaire = 24.9
print(f"Total de la commande c002: {c002.total:.2f} €")


c003 = Commande("C003", alice)
if souris and clavier and ecran:
  c003.ajouter(ecran, 2, 0.5)
  
print("Commande C003:", c003)