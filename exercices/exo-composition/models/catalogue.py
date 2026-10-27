from models.produit import Produit

# Agrégation: les produits sont créés à l'extérieur de la classe Catalogue
class Catalogue:
  def __init__(self) -> None:
    self.__produits: dict[str, Produit] = {}
    
  def ajouter(self, produit: Produit) -> None:
    self.__produits[produit.reference] = produit;
    
  def chercher(self, reference: str) -> Produit | None:
    return self.__produits.get(reference)