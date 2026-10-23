

class Canard:
  def parler(self) -> str:
    return "Coin-coin"
  
class Robot:
  def parler(self) -> str:
    return "Bip bop"

class Personne:
  def __init__(self, nom: str) -> None:
    self.nom = nom
  
  def parler(self) -> str:
    return f"Bonjour, je m'appelle {self.nom}"
  

class Jarod:
  pass

def faire_parler(x) -> None:
  print(f" {type(x).__name__:<10} : {x.parler()}")

for x in [Canard(), Robot(), Canard(), Personne('Alexis')]:
  faire_parler(x)

try:
  faire_parler(Jarod())
except AttributeError as e:
  print(f" Erreur: {e}")
  
  
# Python utilise le Duck Typing


class Compte:
  def __init__(self, numero: int) -> None:
    self.numero = numero
    
  def __len__(self): # len() appelle __len__
    return self.numero
  
  def __iter__(self): # for appelle __iter__
    return iter(range(self.numero))
  
c = Compte(3)


print(len(c))
print(list(c))

for x in c:
  print(f" - {x}")