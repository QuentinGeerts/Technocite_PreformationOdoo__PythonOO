class Produit:
  def __init__(self, reference: str, nom: str, prix_unitaire: float) -> None:
    self.reference = reference
    self.nom = nom
    self.prix_unitaire = prix_unitaire
    
  @property
  def reference(self) -> str:
    return self.__reference
  
  @reference.setter
  def reference(self, reference: str) -> None:
    if not isinstance(reference, str):
      raise TypeError("La référence doit être une chaîne de caractères.")
    if not reference:
      raise ValueError("La référence doit avoir une valeur.")
    self.__reference = reference
  
  @property
  def nom(self) -> str:
    return self.__nom
  
  @nom.setter
  def nom(self, nom: str) -> None:
    if not isinstance(nom, str):
      raise TypeError("Le nom doit être une chaîne de caractères.")
    if not nom:
      raise ValueError("Le nom doit avoir une valeur.")
    self.__nom = nom
  
  @property
  def prix_unitaire(self) -> float:
    return self.__prix_unitaire
  
  @prix_unitaire.setter
  def prix_unitaire(self, prix_unitaire: float) -> None:
    if not isinstance(prix_unitaire, float):
      raise TypeError("Le prix unitaire doit être une valeur numérique.")
    if prix_unitaire <= 0:
      raise ValueError("Le prix unitaire doit être positif.")
    self.__prix_unitaire = prix_unitaire
  
  
  def __str__(self) -> str:
    return f"{self.reference} {self.nom}"