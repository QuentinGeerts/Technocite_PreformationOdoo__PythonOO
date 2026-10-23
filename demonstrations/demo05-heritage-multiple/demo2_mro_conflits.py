
class A:
  def decrire(self) -> str:
    return "A"

  def seulement_a(self) -> str:
    return "méthode présente uniquement dans A"
  
class B:
  def decrire(self) -> str:
    return "B"

  def seulement_b(self) -> str:
    return "méthode présente uniquement dans B"
  

class AB (A, B): ...
class BA (B, A): ...
class ABRedefini(A, B):
  def decrire(self) -> str:
    return f"ABRedefini (super: {super().decrire()})"
  

def mro(cls: type) -> str:
  return " → ".join(c.__name__ for c in cls.__mro__)

print(" --- Ordre de résolution des méthodes --- ")
print(f"AB().decrire(): {AB().decrire()} | MRO: {mro(AB)}")
print(f"BA().decrire(): {BA().decrire()} | MRO: {mro(BA)}")

print(" --- La classe elle-même passera toujours en premier --- ")
print(f"ABRedefini().decrire(): {ABRedefini().decrire()} | MRO: {mro(ABRedefini)}")

print(" --- --- ")
print(f"AB().seulement_a(): {AB().seulement_a()}")
print(f"AB().seulement_a(): {AB().seulement_b()}")


ab = AB()
print(f"B.decrire(obj): {B.decrire(ab)}")