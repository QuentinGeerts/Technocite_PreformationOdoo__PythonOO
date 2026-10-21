
class SansRien:
  def __init__(self, value: int) -> None:
    self.value = value
    
    
print(" --- SansRien ---")

sr1 = SansRien(3)
sr2 = SansRien(3)

# == Vérifie le contenu de la variable
# → Avec des objets, le contenu est la référence mémoire
print(sr1 == sr2) # False
print(sr1)
print(sr2) # Référence différente

# --------------------------------------------------------------------

class Rating:
  def __init__(self, value: int) -> None:
    self.value = value
    
  def __eq__(self, value: object) -> bool:
    if not isinstance(value, Rating):
      return False
    return self.value == value.value
  
  # Vous n'êtes pas obligé de redéfinir not equal car il est lié à equal
  # def __ne__(self, value: object) -> bool:
  #   if not isinstance(value, Rating):
  #     return False
  #   return not (self == value)
  
  # lt est lié à gt
  def __lt__(self, value: object) -> bool:
    if not isinstance(value, Rating):
      return False
    return self.value < value.value
  
  # le est lié à ge
  def __le__(self, value: object) -> bool:
    if not isinstance(value, Rating):
      return False
    return self.value <= value.value
  
  def __hash__(self) -> int:
    return hash(self.value)
  
  
print(" --- Rating --- ")

r1 = Rating(4)
r2 = Rating(4)
r3 = Rating(1)
r4 = Rating(5)


print(r1 == r2) # True
print(r1 != r2) # False

print("r1 > r2:", r1 > r2) # 
print("r1 >= r2:", r1 >= r2) # 
print("r1 < r2:", r1 < r2) # 
print("r1 <= r2:", r1 <= r2) # 


rating_unique = { r1, r2, r3, r4 }

print(rating_unique)