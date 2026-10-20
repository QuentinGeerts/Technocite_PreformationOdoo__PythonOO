class Voiture:
  """Plan de la voiture"""

  def __init__(
      self, 
      marque: str = "", 
      modele: str = "", 
      type_carburant: str = "Diesel",
      kilometrage: int = 0) -> None:
    self.marque = marque
    self.modele = modele
    self.type_carburant = type_carburant
    self.kilometrage = kilometrage

  def rouler (self, distance: int) -> None:
    """Méthode qui modifie le kilomètrage de la voiture sur une certaine distance

    Args:
        distance (int): La distance parcourue
    """
    self.kilometrage += distance
    print(f"La voiture roule {self.kilometrage} km")

  def se_decrire(self) -> str:
    return f"Voiture {self.marque} {self.modele} ({self.type_carburant}) " \
      f"avec {self.kilometrage} km."