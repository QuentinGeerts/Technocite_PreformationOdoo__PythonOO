
class Animal:
  def __init__(self, nom: str) -> None:
    self.nom = nom
    
  def crier(self) -> str: 
    return "..."
  
  def se_presenter(self) -> str:
    return f"Je suis {self.nom}"

class Canari(Animal):
  
  # Redéfinir : on remplace complètement le comportement
  def crier(self) -> str:
    return "Cui-cui !"

  # Étendre : on garde le comportement du parent et on ajoute
  def se_presenter(self) -> str:
    texte_parent = super().se_presenter()
    return f"{texte_parent}, je suis un canari et je fais {self.crier()}"
    
a = Animal("Pierre")
c = Canari("Titi")

print(f" --- Redéfinition --- ")
print(f"Animal: {a.crier()}")
print(f"Canari: {c.crier()}")

print(f" --- Extension --- ")
print(f"Animal: {a.se_presenter()}")
print(f"Canari: {c.se_presenter()}")

print(f"Appler la version du parent explicitement")
print(Animal.se_presenter(c))
