
class Animal:
  def __init__(self, nom: str, age: int) -> None:
    print(f"Animal.__init__({nom=}, {age=})")
    self.nom = nom
    self.age = age
    
class Chien(Animal):
  def __init__(self, nom: str, age: int, race: str) -> None:
    print(f"Chien.__init__({race=})")
    super().__init__(nom, age) # déléguer au parent
    self.race = race
    
    
beethoven = Chien("Beethoven", 12, "Saint-Bernard")
print(vars(beethoven))


class ChienCasse(Animal):
  def __init__(self, nom: str, age: int, race: str) -> None:
    print(f"Chien.__init__({race=})")
    self.race = race

chien_casse = ChienCasse("bug", 1, "inconnue")
print(vars(chien_casse))
try:
  print(chien_casse.nom)
except AttributeError as e:
  print(f"Erreur: {e}")