
class Base:
  def __init__(self) -> None:
    print(f" Base.__init__")

class Gauche(Base):
  def __init__(self) -> None:
    print(f" Gauche.__init__")
    super().__init__()

class Droite(Base):
  def __init__(self) -> None:
    print(f" Droite.__init__")
    super().__init__()

class Bas(Gauche, Droite):
  def __init__(self) -> None:
    print(f" Bas.__init__")
    super().__init__()


def mro(cls: type) -> str:
  return " → ".join(c.__name__ for c in cls.__mro__)


print(" --- Avec super() partout : chaque classe est exécutée une fois en suivant l'ordre MRO")
print(f"MRO de Bas: {mro(Bas)}")
Bas()

class BasMauvais(Gauche, Droite):
  def __init__(self) -> None:
    print(" BasMauvais.__init__")
    Gauche.__init__(self)
    Droite.__init__(self)

print(" --- Avec appels directs : Droite et Base sont exécutées 2 fois --- ")

BasMauvais()

# Pourquoi Droite et Base apparaissent 2 fois ? 
# Le super() dans Gauche ne pointe pas vers Base mais vers la classe suivante dans le MRO de l'instance, c'est à dire Droite
# Gauche n'hériste pas de Droite, et pourtant son super() l'appelle (Merci MRO)