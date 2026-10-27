from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar

@dataclass
class Commande:
  client: str
  articles: list[str] = field(default_factory=list)
  # compare=False → permet de l'ignorer dans la méthode __eq__ générée
  # repr=False → permet de l'ignorer dans la méthode __repr__ générée
  cree_le: datetime = field(default_factory=datetime.now, compare=False, repr=False)
  remise: float = 0.0
  total: float = field(init=False, default=0.0)
  TVA = 0.21
  TVA2: ClassVar[float] = 0.06
  
  # Méthode appelée automatiquement à la fin du __init__ générée
  def __post_init__ (self) -> None:
    if not 0 <= self.remise <= 1:
      raise ValueError(f"Remise invalide: {self.remise}")
    self.client = self.client.strip().capitalize()
    
  def ajouter(self, article: str, prix: float) -> None:
    self.articles.append(article)
    self.total += prix * (1 + Commande.TVA) * (1 - self.remise)
  
c1 = Commande("    quENtin     ", remise=0.5)
print(f"c1:", c1)

c1.ajouter("Clavier", 250)
print(f"c1:", c1)

print(f"{Commande("Quentin") == Commande("Quentin")}")

print(Commande.TVA)
print(Commande.TVA2)

print(Commande.__annotations__)