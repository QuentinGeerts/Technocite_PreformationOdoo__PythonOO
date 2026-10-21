class Article:
  def __init__(self, nom: str, prix: float) -> None:
    self.nom = nom
    self.prix = prix
    
  def __eq__(self, value: object) -> bool:
    if not isinstance(value, Article):
      raise TypeError("L'élément comparé doit être un article.")
    return self.nom == value.nom
  
  def __hash__(self) -> int:
    return hash(self.nom)
  
  
class Panier:
  def __init__(self) -> None:
    self.__articles: dict[Article, int] = {}
    
  @property
  def articles(self) -> dict[Article, int]:
    return dict(self.__articles)
    
  @property
  def total(self) -> float:
    somme = 0
    for article, quantity in self.__articles.items():
      somme += article.prix * quantity
    return somme
  
  def __add__(self, other: object) -> Panier:
    if not isinstance(other, (Panier, Article)):
      return self
    
    if isinstance(other, Article):
      self.__ajouter_article(other)
    
    if isinstance(other, Panier):
      for article, quantity in other.articles.items():
        self.__ajouter_article(article, quantity)
        
    return self
  
  def __ajouter_article (self, article: Article, quantity: int = 1):
    if article in self.__articles:
      self.__articles[article] += quantity
    else:
      self.__articles[article] = quantity
      
      
  def __str__(self) -> str:
    result = f"Panier:"
    for article, quantity in self.articles.items():
      result += f"\n - {quantity}x {article.nom} - {article.prix} €/u | {article.prix * quantity} €"
    result += f"\nTotal: {self.total} €\n"
      
    return result
      
# ---------------------------------


p1 = Panier()
p2 = Panier()

a1 = Article('Carte graphique', 549)
a2 = Article('Souris gaming', 59.99)
a3 = Article('Clavier', 129.99)

p1 = p1 + a1 + a2 + a2
p2 += a3

print("p1:", p1)
print("p2:", p2)

p3 = Panier()
p3 += p1 + p2
print("p3:", p3)

p4 = Panier()
p4 += p1 + a3 + a3 + a3
print("p4:", p4)
print(p4 == p1)