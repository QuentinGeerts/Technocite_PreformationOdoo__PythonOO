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
    for article, quantite in self.__articles.items():
      somme += article.prix * quantite
    return somme
  
  # panier[article] = valeur
  def __setitem__(self, article: Article, quantite: int) -> None:
    if quantite < 0:
      raise ValueError("La quantité doit être positive.")
    if quantite == 0:
      # self.__articles.pop(article)
      del self.__articles[article]
    else:
      self.__articles[article] = quantite
      
  # panier[article]
  def __getitem__(self, article: Article) -> int:
    return self.__articles[article]
    
  # len(panier)
  def __len__(self) -> int:
    return sum(self.__articles.values())
  
  def __contains__(self, article: Article) -> bool:
    return article in self.__articles
  
  def __iter__(self):
    return iter(self.__articles)
  
  def __bool__(self) -> bool:
    return bool(self.__articles)
      
  def __str__(self) -> str:
    result = f"Panier:"
    for article, quantite in self.articles.items():
      result += f"\n - {quantite}x {article.nom} - {article.prix} €/u | {article.prix * quantite} €"
    result += f"\nTotal: {self.total} €\n"
      
    return result
      
# ---------------------------------


p1 = Panier()
p2 = Panier()

a1 = Article('Carte graphique', 549)
a2 = Article('Souris gaming', 59.99)
a3 = Article('Clavier', 129.99)

p1[a1] = 2
p1[a2] = 3

print("p1:", p1)

print("Nombre de lignes:", len(p1.articles)) # 2
# print("Nombre d'articles:", len(p1)) # 5

print("p1 contient a2", a2 in p1)


print("Liste des articles du panier:")

for article in p1:
  print(f" - {article.nom} {article.prix} €")
  

if p1:
  print("P1 a au moins un article")
  
if p2:
  print("P2 a au moins un article")
  