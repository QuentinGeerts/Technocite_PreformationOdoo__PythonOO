
class Moteur:
  def __init__(self, puissance: int) -> None:
    self.puissance = puissance
    self.en_marche = False
    
  def demarrer(self) -> str:
    self.en_marche = True
    return f"Le moteur de {self.puissance}cv démarre."
  
  def arreter(self) -> str:
    self.en_marche = False
    return f"Le moteur s'arrête."

class Roue:
  def __init__(self, position: str) -> None:
    self.position = position
    self.pression = 2.4
    
class GPS: 
  def calcul_itinerataire(self, destination: str) -> str:
    return f"Itinéraire calculé vers {destination}"    


class Voiture:
  def __init__(self, marque: str, puissance: int) -> None:
    self.marque = marque
    self.moteur = Moteur(puissance)
    self.roues = [Roue(position) for position in ["AVG", "AVD", "ARG", "ARD"]]
    self.gps = GPS()
    
  # Déléguer le travail aux composants
  def demarrer(self) -> str:
    return self.moteur.demarrer()
  
  def arreter(self) -> str:
    return self.moteur.arreter()
  
  def naviguer(self, destination: str) -> str:
    return self.gps.calcul_itinerataire(destination)
  
  def details_pression(self) -> list[str]:
    return [f"{roue.position}: {roue.pression} bar" for roue in self.roues]
  

# Instanciation de la voiture
v = Voiture("Kia", 115)

print(f"Démarrage: {v.demarrer()}")
print(f"État du moteur: {v.moteur.en_marche}")
print(f"Rouler jusqu'à la destination (Hornu): {v.naviguer('Hornu')}")
print(f"Arrêt: {v.arreter()}")
print(f"État du moteur: {v.moteur.en_marche}")


print(f"isinstance(v, Moteur): {isinstance(v, Moteur)}")


