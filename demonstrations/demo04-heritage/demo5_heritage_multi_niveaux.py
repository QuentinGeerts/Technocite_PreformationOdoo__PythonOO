
class Vehicule:
  def __init__(self, marque: str) -> None:
    self.marque = marque
    
  def decrire(self) -> str:
    return f"Véhicule {self.marque}"
  
  
class VehiculeMotorise(Vehicule):
  def __init__(self, marque: str, puissance: int) -> None:
    super().__init__(marque)
    self.puissance = puissance
    
  def decrire(self) -> str:
    return f"{super().decrire()}, {self.puissance} chevaux";
  
class Voiture(VehiculeMotorise):
  def __init__(self, marque: str, puissance: int, nb_portes:int = 3) -> None:
    super().__init__(marque, puissance)
    self.nb_portes = nb_portes
    
class Velo (Vehicule):
  def decrire(self) -> str:
    return f"{super().decrire()} (sans moteur)"
  
print(f" --- ")
for v in [ Vehicule("Base"), VehiculeMotorise("Yamaha", 90), Voiture("BYD", 180, 5), Velo("Btwin") ]:
  print(f"{type(v).__name__:<20} → {v.decrire()}")
  
print(Voiture.__mro__) # tuple des classes qui sont appelées dans l'ordre d'execution (Method Resolution Order)
print(' → '.join(v.__name__ for v in Voiture.__mro__))