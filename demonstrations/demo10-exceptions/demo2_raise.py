# Pour lever manuellement une exception: raise

class Thermostat:
  MIN = 5
  MAX = 30
  
  def __init__(self, piece: str) -> None:
    self.piece = piece
    self.__temperature = 20.0
    
  @property
  def temperature(self) -> float:
    return self.__temperature
  
  def regler(self, valeur: float) -> None:
    # Mauvais type → TypeError
    if not isinstance(valeur, (int, float)):
      raise TypeError(f"Température attendue doit être un nombre (reçu: {type(valeur).__name__})")
    
    # Bon type mais valeur hors limite → ValueError
    if not self.MIN <= valeur <= self.MAX:
      raise ValueError(f"'{valeur}' °C est hors limites ({self.MIN}-{self.MAX} °C)")
    
    # Bon type et bonne valeur
    self.__temperature = float(valeur)
    
    
# 1. L'élément qui appelle qui gère les erreurs
salon = Thermostat("salon")

for valeur in [22, 50, "erreur"]:
  try:
    salon.regler(valeur)
  except (TypeError, ValueError) as e:
    print(f"regler({valeur}) → Erreur: {e}")
  else:
    print(f"regler({valeur}) → Ok: {salon.temperature}")
    

# 2.  Relancer une exception avec "raise" seul

def regler_avec_log(thermostat: Thermostat, valeur: float) -> None:
  try:
    thermostat.regler(valeur)
  except ValueError:
    print(f"[LOG] Réglage refusé sur {thermostat.piece}")
    raise # relance la même exception: traceback intact
  
try:
  regler_avec_log(salon, 110)
except ValueError as e:
  print(f"On a reçu : {e}")
  
# 3.  L'exception remonte toute la pile des appels
# Si une fonction n'attrape pas l'exception, elle remonte à l'appelant
# Puis à l'appelant de l'appelant... jusqu'à un try/except (ou le crash)

def niveau3() -> None:
  raise RuntimeError("Problème au niveau 3")

def niveau2():
  niveau3()
  
  
def niveau1 ():
  try:
    niveau2()
  except RuntimeError as e:
    print(f"Exception attrapée au niveau 1: {e}")
  
niveau1()

# 4.  finally s'exécute même avec un return

def lire_config(chemin: str) -> str:
  print(f"Ouverture du {chemin}")
  
  try:
    if not chemin.endswith('.ini'):
      raise ValueError("Format non supporté")
    return "Config chargée"
  finally:
    print("Fermeture (toujours exécuté)")
    
try:
  lire_config("app.txt")
except ValueError as e:
  print(f"Erreur: {e}")
    
