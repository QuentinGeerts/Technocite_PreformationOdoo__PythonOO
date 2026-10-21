from .maison import Adresse, Maison
from .personne import Personne

class Village:
  
  def __init__(self, nom: str) -> None:
    self.nom = nom
    self.__maisons: dict[Adresse, Maison] = {}
    
  # Getters / Setters
  
  @property
  def nom(self) -> str:
    return self.__nom
  
  @nom.setter
  def nom(self, nom: str) -> None:
    self.__nom = nom
  
  @property
  def maisons(self) -> list[Maison]:
    return list(self.__maisons.values())
  
  # Actions
  
  def construire(self, adresse: Adresse, proprietaire: Personne, prix: float) -> Maison:
    if adresse in self.__maisons.keys():
      raise ValueError("L'adresse est déjà prise.")
    
    maison = Maison(adresse, proprietaire, prix)
    self.__maisons[adresse] = maison
    print(f"Maison construite à {adresse}")
    return maison
  
  def demolir(self, adresse: Adresse) -> None:
    if adresse not in self.__maisons.keys():
          raise ValueError("L'adresse est introuvable.")
        
    del self.__maisons[adresse]
    print(f"Maison détruite à {adresse}")
    
  def afficher(self) -> None:
    print(f"Liste des maisons de {self.nom}")
    if not self.__maisons:
      print("Aucun maison actuellement")
    else:
      for maison in self.maisons:
        print(f"{maison}\n")