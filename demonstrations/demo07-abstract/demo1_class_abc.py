from abc import ABC, abstractmethod

class Animal(ABC):
  def __init__(self, nom: str) -> None:
    self.nom = nom
    
  @abstractmethod
  def crier(self) -> str: ...
  

class Chien(Animal):
  def crier(self) -> str:
    return "Wouaf!"

class Poisson(Animal):
  pass # Oublier d'implementer une méthode abstrait


# Instanciation des classes

# animal = Animal("Générique") # Impossible d'instancier une classe abstrait
chien = Chien('Snoopy')

try:
  poisson = Poisson('Dory')
except TypeError as e:
  print(f"Erreur:", e)
  

print(f"Méthodes abstraites d'Animal: {Animal.__abstractmethods__}")
print(f"Méthodes abstraites de Chien: {Chien.__abstractmethods__}")
print(f"Méthodes abstraites de Poisson: {Poisson.__abstractmethods__}")