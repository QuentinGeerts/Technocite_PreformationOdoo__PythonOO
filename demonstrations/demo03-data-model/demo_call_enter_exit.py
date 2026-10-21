

# call: permet d'utiliser un objet comme fonction


from typing import Any


class Multiplicateur:
  
  def __init__(self, facteur: float) -> None:
    self.facteur = facteur

  def __call__(self, value: float) -> float:
    return value * self.facteur

    
    
print(" --- call --- ")

doubler = Multiplicateur(2)
quadrupler = Multiplicateur(4)
print(list(map(doubler, [2, 3, 4, 5, 6, 7, 8, 9, 10])))
print(doubler(4))
print(callable(doubler))


# ------------------------------------------------------------------------

class FileReader:
  
  def __init__(self, path: str, mode = "r") -> None:
    self.path = path
    self.mode = mode
    
  def __enter__(self):
    self.file = open(self.path, self.mode, encoding="UTF-8")
    return self.file
  
  def __exit__(self, exc_type, exc, tb):
    self.file.close()

with FileReader("demonstrations/demo03-data-model/data.txt") as file:
  for line in file.readlines():
    print("line:", line)
