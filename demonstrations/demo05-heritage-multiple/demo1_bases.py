


class Nageur:
  def nager(self) -> str:
    return f"{self.nom} nage."
  
class Marcheur:
  def marcher(self) -> str:
    return f"{self.nom} marche."
  
class Volant:
  def voler(self) -> str:
    return f"{self.nom} vole."
  
  
  
class Canard(Nageur, Marcheur, Volant):
  def __init__(self, nom: str) -> None:
    self.nom = nom

class Poule(Nageur, Marcheur):
  def __init__(self, nom: str) -> None:
    self.nom = nom

donald = Canard("Donald")
susanne = Poule("Susanne")


print(" --- Canard cumule 3 actions --- ")
print(donald.marcher(), donald.voler(), donald.nager())

print(" --- Poule cumule 2 actions --- ")
print(susanne.marcher(), susanne.nager())
print(f"Est-ce que la poule peut voler : {hasattr(susanne, 'voler')}")

print(f"isinstance(donald, Nageur): {isinstance(donald, Nageur)}")
print(f"isinstance(donald, Marcheur): {isinstance(donald, Marcheur)}")
print(f"isinstance(donald, Volant): {isinstance(donald, Volant)}")

print(f"isinstance(susanne, Nageur): {isinstance(susanne, Nageur)}")
print(f"isinstance(susanne, Marcheur): {isinstance(susanne, Marcheur)}")
print(f"isinstance(susanne, Volant): {isinstance(susanne, Volant)}")