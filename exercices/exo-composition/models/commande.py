from models.client import Client
from models.ligne_commande import LigneCommande
from models.produit import Produit

class Commande :
  def __init__(self, numero: str, client: Client) -> None:
    self.numero = numero
    self.client = client
    self.__lignes: list[LigneCommande] = []
    
  def ajouter(self, produit: Produit, quantite: int = 1, remise: float = 0.0) -> None:
    for ligne in self.__lignes:
      if ligne.produit.reference == produit.reference:
        ligne.quantite += quantite
        return
    self.__lignes.append(LigneCommande(produit, quantite, remise))
  
  def retirer(self, reference: str) -> None:
    self.__lignes = [l for l in self.__lignes if l.produit.reference != reference]
    
  @property
  def lignes(self) -> tuple[LigneCommande, ...]:
    return tuple(self.__lignes)
  
  @property
  def total(self) -> float:
    return sum([ligne.sous_total for ligne in self.__lignes])
  
  def __len__(self) -> int:
    return len(self.__lignes)
  
    """
    Commande C001 — Alice (alice@mail.be)
      CLA-01  Clavier  3 × 49.90 € =  149.70 €
      SOU-01  Souris   1 × 19.90 € =   19.90 €
      Total : 169.60 € (2 lignes)
    """
  
  def __str__(self) -> str:
    texte = f"Commande {self.numero} - {self.client}\n"
    for ligne in self.__lignes:
      texte += f"  {ligne}\n"
    texte += f"  Total : {self.total:.2f} € ({len(self)} lignes)"
    return texte
  