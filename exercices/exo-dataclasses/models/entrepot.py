from dataclasses import dataclass, field

from models.adresse import Adresse
from models.article import Article

@dataclass
class Entrepot:
  nom: str
  adresse: Adresse
  articles: list[Article] = field(default_factory=list)

  def ajouter(self, article: Article) -> None:
    self.articles.append(article)
    
  def valeur_totale(self) -> float:
    return sum([article.valeur_stock for article in self.articles])
  
  def en_rupture(self) -> list[Article]:
    return [article for article in self.articles if article.quantite == 0]