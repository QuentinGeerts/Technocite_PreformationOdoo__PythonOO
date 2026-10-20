class titulaire:
  
  def __init__(self, nom: str, prenom: str) -> None:
    self.__nom = nom
    self.__prenom = prenom
    
  # Version avec @property et @nom.setter
  @property
  def nom(self) -> str:
    return self.__nom
  
  @nom.setter
  def nom(self, nouveau_nom: str) -> None:
    self.__nom = nouveau_nom

  # Version avec property(...)
  def get_prenom(self) -> str:
    return self.__prenom

  def set_prenom(self, nouveau_prenom: str) -> None:
    self.__prenom = nouveau_prenom
    
  # prenom = property(get_prenom) # Lecture seule
  prenom = property(get_prenom, set_prenom) # Lecture et écriture
  
  
if __name__ == '__main__':
  
  t = titulaire('Geerts', 'Quentin')
  
  # Getter / Accesseur
  print("nom:", t.nom)
  # print("nom:", t.__nom) # Erreur
  print("prenom:", t.prenom)
  
  # Setter / Mutateur
  t.nom = 'Geerts'
  t.prenom = 'Quentin'
  