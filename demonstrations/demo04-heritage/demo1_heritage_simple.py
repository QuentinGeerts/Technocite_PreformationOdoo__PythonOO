
class Animal:
  
  def __init__(self, nom: str, age: int, couleur: str, nb_heure_sommeil: int) -> None:
    self.nom = nom
    self.age = age
    self._couleur = couleur
    self.__nb_heure_sommeil = nb_heure_sommeil
    
  def se_presenter(self) -> str:
    return f"Je m'appelle {self.nom} et j'ai {self.age} an(s)."

  def dormir(self) -> str:
    return f"{self.nom} dort. Zzzz"

# Création d'une classe fille sans rien ajouter
class Chat(Animal):
  pass


noirau = Chat("Noirau", 6, "noir", 15) # la classe "Chat" hérite du constructeur

print("Nom:", noirau.nom)
print(f"{noirau.age=}")
print(f"{noirau._couleur=}")
# print(f"{noirau.__nb_heure_sommeil=}") # Erreur (car privé)
# print(f"{noirau._Animal__nb_heure_sommeil=}") # Fonctionne (attention l'erreur est levée par Pylance)
print(noirau.se_presenter())
print(noirau.dormir())


print("Dans Animal.__dict__", Animal.__dict__)
print("Dans Chat.__dict__", Chat.__dict__)

print("vars(noirau):", vars(noirau))

# print("Nombre d'heures de sommeil:", noirau._Animal__nb_heure_sommeil) # Accessible via animal

print("Chat.__bases__:", Chat.__bases__)
print("Animal.__bases__:", Animal.__bases__)