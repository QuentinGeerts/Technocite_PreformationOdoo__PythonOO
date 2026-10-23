
class Personne:
  def __init__(self, nom: str, **kwargs) -> None:
    print(f" Personne: ({nom=}, reste={kwargs})")
    self.nom = nom
    
class Employe(Personne):
  def __init__(self, salaire: float, **kwargs) -> None:
    print(f" Employe: ({salaire=}, reste={kwargs})")
    super().__init__(**kwargs)
    self.salaire = salaire
    
class Etudiant(Personne):
  def __init__(self, ecole: str, **kwargs) -> None:
    print(f" Etudiant: ({ecole=}, reste={kwargs})")
    super().__init__(**kwargs)
    self.ecole = ecole
    
class Alternant(Employe, Etudiant):
  def __str__(self) -> str:
    return f"{self.nom} {self.ecole} {self.salaire} €"

print(f"Alternant.__mro__: {' → '.join(c.__name__ for c in Alternant.__mro__)}")

print(f" --- Chaque classe consomme son paramètre et passe le reste --- ")
loic = Alternant(nom="Loic", salaire=4.59, ecole="Technocite")
print(f"Loic: {loic}")

print(" --- Les classes restent utilisables seules --- ")
print(vars(Employe(nom="Quentin", salaire=1)))