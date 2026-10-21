from .personne import Personne
from types import NoneType

class Adresse:
  
  def __init__(self, rue: str, numero: str, code_postal: int, ville: str) -> None:
    self.rue = rue
    self.numero = numero
    self.code_postal = code_postal
    self.ville = ville
    
  # Redéfinition de méthode
  # Changer l'ancien comportement par un nouveau
  def __str__(self) -> str:
    return f"{self.rue} {self.numero}, {self.code_postal} {self.ville}"

class Maison:
  
  def __init__(self, 
               adresse: Adresse, 
               proprietaire: Personne, 
               prix: float,
               en_location: bool = False,
               locataire: Personne | None = None,
               prix_location: float | None = None) -> None:
    self.adresse = adresse
    self.proprietaire = proprietaire
    self.prix = prix
    self.en_location = en_location
    self.locataire = locataire
    self.prix_location = prix_location

  @property
  def adresse(self):
      return self.__adresse

  @adresse.setter
  def adresse(self, value: Adresse):
    if not isinstance(value, Adresse):
      raise TypeError("L'adresse doit être une adresse valide.")
    self.__adresse = value

  @property
  def proprietaire(self):
    return self.__proprietaire

  @proprietaire.setter
  def proprietaire(self, value: Personne):
    if not isinstance(value, Personne):
      raise TypeError("Le propriétaire doit être une personne.")
    self.__proprietaire = value

  @property
  def prix(self):
    return self.__prix

  @prix.setter
  def prix(self, value: float):
    self.__prix = value

  @property
  def en_location(self):
    return self.__en_location

  @en_location.setter
  def en_location(self, value: bool):
    if not isinstance(value, bool):
      raise TypeError("Le type doit être un booléen.")
    self.__en_location = value

  @property
  def locataire(self):
    return self.__locataire

  @locataire.setter
  def locataire(self, value: Personne | None):
    if not isinstance(value, Personne) \
      and not isinstance(value, NoneType):
      raise TypeError("Le locataire doit être une personne.")
    self.__locataire = value

  @property
  def prix_location(self):
    return self.__prix_location

  @prix_location.setter
  def prix_location(self, value: float | None):
    if not isinstance(value, float) \
      and not isinstance(value, NoneType):
      raise TypeError("Le prix doit être une valeur numérique.")
    
    if value and value < 0:
      raise ValueError("Le prix doit être positif.")
    self.__prix_location = value

  
  def __str__(self) -> str:
    return f"Maison :" \
      f"\n - Adresse: {self.adresse}" \
      f"\n - Propriétaire: {self.proprietaire}" \
      f"\n - Prix: {self.prix} €"