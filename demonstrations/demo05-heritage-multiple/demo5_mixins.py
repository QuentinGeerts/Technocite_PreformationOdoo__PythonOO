
# Un mixin ajoute un comportement à une classe
# Il n'a pas d'init → il n'est jamais instancié

import json

class JsonMixin:
  def to_json(self) -> str:
    return json.dumps(vars(self), ensure_ascii=False)
  
class ReprMixin:
  def __repr__(self) -> str:
    attributs = ', '.join(f"{k}={v!r}" for k, v in vars(self).items())
    return f"{type(self).__name__}({attributs})"


# Les mixins doivent TOUJOURS être placées avant les classes
class Product(JsonMixin, ReprMixin):
  def __init__(self, name: str, price: float) -> None:
    self.name = name;
    self.price = price
    
class Client (JsonMixin, ReprMixin):
  def __init__(self, nom: str, ville: str) -> None:
    self.nom = nom
    self.ville = ville
    
    
p1 = Product("Clavier", 49.99)
p2 = Product("Carte graphique", 549.99)
c1 = Client("Quentin", "Virelles")

print(f" --- JsonMixin --- ")
print(p1.to_json())
print(p2.to_json())
print(c1.to_json())

print(f" --- ReprMixin --- ")
print(repr(p1))
print(repr(p2))
print(f"{c1!r}")