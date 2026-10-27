

# ---- Composition:
# → Une classe possède des composants
# → Si la classe disparait, les composants disparaisent également

class Piece:
  def __init__(self, nom: str, surface: float) -> None:
    self.nom = nom
    self.surface = surface
    
class Maison:
  def __init__(self, adresse: str, pieces: dict[str, float]) -> None:
    self.adresse = adresse
    self.pieces = [Piece(n, s) for n, s in pieces.items()]
  
# Composition
maison = Maison('Rue de ma rue', {'salon': 20, 'chambre1': 15, 'cuisine': 30})


# ---- Agregation
# → Une classe qui possède des composants
# → Les composants existent avant la création de la classe
# → Si la classe qui possède les composants vient à être supprimée, les composants restent

class Professeur:
  def __init__(self, nom: str) -> None:
    self.nom = nom
    
class Cours:
  def __init__(self, intitule: str, professeur: Professeur) -> None:
    self.intitule = intitule
    self.professeur = professeur # récupéré depuis l'extérieur


prof = Professeur("Quentin")
cours_python = Cours("Python", prof)
cours_psql = Cours("PostgreSQL", prof)

print(f"{cours_python.intitule} → {cours_python.professeur.nom}")
print(f"{cours_psql.intitule} → {cours_psql.professeur.nom}")

print(f"Même objet ? {cours_python.professeur is cours_psql.professeur}")

prof.nom = 'Benjamin'
print(f"{cours_psql.intitule} → {cours_psql.professeur.nom}")

del cours_python
print(f"{cours_psql.intitule} → {cours_psql.professeur.nom}")
