from models.produit import Produit

class LigneCommande:
  
  def __init__(self, produit: Produit, quantite: int, remise: float = 0.0) -> None:
    self.produit = produit
    self.quantite = quantite
    self.prix = produit.prix_unitaire
    self.remise = remise
    
  @property
  def remise(self) -> float:
    return self.__remise
  
  @remise.setter
  def remise(self, remise: float) -> None:
    if not isinstance(remise, float):
      raise TypeError("La remise doit être une valeur numérique.")
    if not 0 <= remise <= 1:
      raise ValueError("La remise doit être comprise entre 0 et 1.")
    self.__remise = remise
  
    
  @property
  def sous_total(self) -> float:
    return (self.prix * self.quantite) * (1 - self.remise)
  
  
  def __iter__(self):
    return iter(self)
  
  def __str__(self) -> str:
    return f"{self.produit} {self.quantite} x {self.prix:.2f} €" \
      f" = {self.sous_total:>8.2f} €" \
        f"(Remise: {self.remise * 100}%)" if self.remise > 0 else ""