from dataclasses import dataclass, field

@dataclass
class Article:
  reference: str
  nom: str
  prix: float
  quantite: int = 0
  tags: list[str] = field(default_factory=list, compare=False)
  
  def __post_init__(self) -> None:
    if self.prix <= 0: 
      raise ValueError(f"Le prix doit être positif. (reçu: {self.prix})")
    if self.quantite < 0:
      raise ValueError(f"La quantité doit être positive. (reçu: {self.quantite})")
    self.nom = self.nom.strip().capitalize()
    
  @property
  def valeur_stock(self) -> float:
    return self.prix * self.quantite
  