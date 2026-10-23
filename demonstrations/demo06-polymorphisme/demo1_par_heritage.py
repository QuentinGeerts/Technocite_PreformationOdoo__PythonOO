import math

class Forme:
  def aire(self) -> float:
    return 0.0
  
  def decrire(self) -> str:
    return f"{type(self).__name__} aire = {self.aire()}"


class Cercle (Forme):
  def __init__(self, rayon: float) -> None:
    self.rayon = rayon
    
  # Polymorphisme d'héritage = redéfinition de méthode
  def aire(self) -> float:
    return math.pi * self.rayon ** 2
  
class Rectangle (Forme):
  def __init__(self, largeur: float, hauteur: float) -> None:
    self.largeur = largeur
    self.hauteur = hauteur
    
  def aire(self) -> float:
    return self.largeur * self.hauteur
  
class Triangle(Forme):
  def __init__(self, base: float, hauteur: float) -> None:
    self.base = base
    self.hauteur = hauteur

# Un cercle est une forme, un rectangle est une forme
# → Ils sont considérés comme des formes
formes: list[Forme] = [
  Cercle(1), Rectangle(3, 4), Cercle(3.5),
  Triangle(3, 5)
]

print(" --- Même appel, comportements différents --- ")
for forme in formes:
  print(f" - {forme.decrire()}")