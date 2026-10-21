from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from .maison import Maison


class Personne:
  
  def __init__(self, nom: str, argent: float) -> None:
    self.nom = nom
    self.argent = argent
    
    
  # Getters / setters
  @property
  def nom(self) -> str:
    return self.__nom
  
  @nom.setter
  def nom(self, nom: str) -> None:
    if not nom or not nom.strip():
      raise ValueError("Le nom ne peut pas être vide")
    self.__nom = nom.strip()
  
  @property
  def argent(self) -> float:
    return self.__argent
  
  @argent.setter
  def argent(self, argent: float) -> None:
    if not type(argent) in [float, int]:
      raise TypeError("L'argent doit être une valeur numérique.")
    if argent < 0:
      raise ValueError("L'argent doit être positif.")
    self.__argent = argent
  
  def __str__(self) -> str:
    return f"{self.nom} (capital: {self.argent} €)"
  
  # Actions
  
  def acheter (self, maison: Maison):
    if maison.prix > self.argent:
      raise ValueError(f"{self.nom} n'a pas assez d'argent pour acheter la maison. (requis: {maison.prix})")
    if maison.proprietaire is self:
      raise ValueError(f"{self.nom} est déjà le propriétaire de la maison.")

    self.argent -= maison.prix
    ancien_proprietaire = maison.proprietaire
    ancien_proprietaire.argent += maison.prix
    maison.proprietaire = self
    print(f"{self.nom} a acheté à {ancien_proprietaire.nom} la maison située à {maison.adresse} pour un prix de {maison.prix} €")