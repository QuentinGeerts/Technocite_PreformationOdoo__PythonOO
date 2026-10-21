from models import Maison, Personne, Village, Adresse

# Exo2 maison

# Simuler la vie dans un petit village dans lequel des maisons peuvent être construites à
# des adresses bien précises ou qu’elles peuvent être également détruites.
# Assurez-vous que les attributs de vos différentes classes possèdent un getter et un
# setter bien défini.

# Bonus :
# Ajouter des propriétaires aux maisons. Les propriétaires peuvent acheter et vendre les
# maisons ou bien les louer à d’autres personnes.

# Création du village
hornu = Village("Hornu")

# Création des personnes
try:
  p1 = Personne("John", 200_000)
  p2 = Personne("Jane", 250_000)
  p3 = Personne("Quentin", 200_000)
  
  # Création des adresses et maisons

  adresse1 = Adresse("Rue de la rue", "1", 7300, "Hornu")
  adresse2 = Adresse("Rue de la rue", "2", 7300, "Hornu")

  hornu.construire(adresse=adresse1, proprietaire=p1, prix=125_000)
  hornu.construire(adresse2, p2, 249_000)

  # Liste des maisons du village
  hornu.afficher()

  # Achats de maison
  p3.acheter(list(filter(lambda maison : maison.proprietaire.nom == 'John', hornu.maisons))[0])

  # Liste des maisons du village
  hornu.afficher()


except Exception as e:
  print(f"Erreur: {e}")