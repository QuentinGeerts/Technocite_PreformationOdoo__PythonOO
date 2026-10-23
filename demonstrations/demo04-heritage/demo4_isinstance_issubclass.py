
class Animal: ...
class Chien(Animal): ...
class Chat(Animal): ...

rex = Chien()

print("\n --- isinstance(object, class) -> bool --- ")
print(f"rex est un Chien ? {isinstance(rex, Chien)}") # True
print(f"rex est un Chat ? {isinstance(rex, Chat)}") # False
print(f"rex est un Animal ? {isinstance(rex, Animal)}") # True
print(f"rex est un object ? {isinstance(rex, object)}") # True

print(f"\n --- isinstance avec un tuple de classes --- ")
print(f"rex est un Chat ou Chien ? {isinstance(rex, (Chien, Chat))}") # True

print(f"\n --- type() ne tient pas compte de l'héritage --- ")
print(f"type(rex) is Chien : {type(rex) is Chien}") # True
print(f"type(rex) is Animal : {type(rex) is Animal}") # False
print(f" → préférez isinstance() pour tester un type")

print(f"\n --- issubclass(class, class) -> bool --- ")
print(f"issubclass(Chien, Animal) : {issubclass(Chien, Animal)}") # True
print(f"issubclass(Animal, Chien) : {issubclass(Animal, Chien)}") # False
print(f"issubclass(Chien, Chien) : {issubclass(Chien, Chien)}") # True : une classe est sa propre sous-classe

print("Animal.__subclasses__():", Animal.__subclasses__()) # Permet d'obtenir la liste des sous-classes