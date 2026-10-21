
class SansRien:
  # Constructeur vide
  # Remplacer le constructeur par défaut par le vide
  # def __init__(self) -> None:
  #   pass
  
  # Remplacer le constructeur vide par celui-ci
  def __init__(self, nom: str) -> None:
    self.nom = nom

print(f" --- sans rien --- ")

# sr = SansRien() # Utilisation du constructeur par défaut
sr = SansRien("Test") # Utilisation du constructeur par défaut


# -------------------------------------------------------------------

class Produit:
  
  def __init__(self, nom: str, prix: float) -> None:
    self.nom = nom
    self.prix = prix
    
  def __str__(self) -> str:
    """Représentation pour l'utilisateur = lisible"""
    return f"{self.nom} à {self.prix} €"
  
  def __repr__(self) -> str:
    """Représentation pour le développeur = précis"""
    return f"Produit(nom={self.nom}, prix={self.prix})"
  
  def __format__(self, format_spec: str) -> str:
    # Formats customs pour les f-string
    if format_spec == "court":
      return self.nom
    if format_spec == "ticket":
      return f"{self.nom:.<20}{self.prix:>8.2f} €"

    return self.nom
  
p = Produit("Carte graphique", 534.99)

# Version str
print(" --- __str__ ---")
print(p)
print(p.__str__())
print(str(p))

# Version repr
print(" --- __repr__ ---")
print(f"{p!r}")
print(p.__repr__())
print(repr(p))

# Version format
print(" --- __format__ ---")
print(f"{p:court}")
print(f"{p:ticket}")
print(f"{Produit("Souris", 180):ticket}")
print(f"{Produit("RTX 5080", 1749.99):ticket}")