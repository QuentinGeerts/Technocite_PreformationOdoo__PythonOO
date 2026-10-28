from dataclasses import dataclass, field

# Une exception custom = une classe qui hérite d'exception


# 1.  Classe de base du système : vide → servir à regrouper les erreurs
class BibliothequeError(Exception):
  """Classe mère de toutes les erreurs de la bibliothèque"""
  
  
# 2.  Exception avec attributs : message d'erreur qui est construit avec un attribut fournit

class LivreIntrouvableError(BibliothequeError):
  def __init__(self, isbn: str) -> None:
    self.isbn = isbn
    super().__init__(f"Aucun livre avec l'ISBN {isbn}")
    
class LivreIndisponibleError(BibliothequeError):
  def __init__(self, titre: str, emprunteur: Membre) -> None:
    self.titre = titre
    self.emprunteur = emprunteur
    super().__init__(f"{titre} est déjà emprunté par {emprunteur}")
    

# 3.  Exception avec une propriété calculée

class QuotaDepasseError(BibliothequeError):
  def __init__(self, membre: Membre, quota: int, en_cours: int) -> None:
    self.membre = membre
    self.quota = quota
    self.en_cours = en_cours
    super().__init__(f"{membre.prenom} {membre.nom} a atteint son quota ({en_cours} / {quota} livres)")
    
  @property
  def actuel(self) -> int:
    return self.en_cours - self.quota + 1

# Modèles pour tester les exceptions

@dataclass(frozen=True)
class Membre:
  nom: str
  prenom: str

@dataclass
class Livre:
  isbn: str
  titre: str
  emprunteur: Membre | None = field(init=False, default=None)
  
class Bibliotheque:
  QUOTA = 2
  
  def __init__(self) -> None:
    self.__livres: dict[str, Livre] = {}
    self.__emprunts: dict[Membre, int] = {}
  
  def ajouter(self, livre: Livre) -> None:
    self.__livres[livre.isbn] = livre
    
  def emprunter(self, isbn: str, membre: Membre) -> Livre:
    """Fait emprunter un livre de la bibliothèque par un membre.

    Args:
        isbn (str): ISBN du livre à emprunter.
        membre (Membre): Membre qui emprunte le livre.

    Raises:
        LivreIntrouvableError: Si aucun livre ne correspond à l'ISBN.
        LivreIndisponibleError: Si le livre est déjà emprunté.
        QuotaDepasseError: Si le membre a atteint le quota d'emprunts (QUOTA).

    Returns:
        Livre: Le livre emprunté, avec le membre comme emprunteur.
    """
    if isbn not in self.__livres:
      raise LivreIntrouvableError(isbn)
    
    livre = self.__livres[isbn]
    if livre.emprunteur is not None:
      raise LivreIndisponibleError(livre.titre, livre.emprunteur)
    
    en_cours = self.__emprunts.get(membre, 0)
    if en_cours >= self.QUOTA:
      raise QuotaDepasseError(membre, self.QUOTA, en_cours)
    
    livre.emprunteur = membre
    self.__emprunts[membre] = en_cours + 1
    return livre
    
    
biblio = Bibliotheque()
biblio.ajouter(Livre("987654321", "L'épée de vérité"))
biblio.ajouter(Livre("987654322", "Python pour les nuls"))
biblio.ajouter(Livre("987654323", "Tout JavaScript"))
biblio.ajouter(Livre("987654324", "Seigneur des anneaux"))


demandes = [
  ('987654321', Membre('Geerts', 'Quentin')), # premier emprunt
  ('987654321', Membre('Doe', 'John')), # déjà emprunt
  ('987654322', Membre('Geerts', 'Quentin')), # deuxième emprunt
  ('987654323', Membre('Geerts', 'Quentin')), # quota atteint
  ('987654325', Membre('Doe', 'John')), # ISBN non reconnu
]

for isbn, membre in demandes:
  try:
    livre = biblio.emprunter(isbn, membre)
  except LivreIndisponibleError as e:
    print(f"{e.titre} est pris par {e.emprunteur.prenom} {e.emprunteur.prenom}")
  except QuotaDepasseError as e:
    print(f"{e} - rendez {e.actuel} pour emprunter à nouveau")
  except BibliothequeError as e:
    print(f"Erreur: {e}")
  else:
    print(f"{isbn} → {livre.titre}")