from dataclasses import dataclass, FrozenInstanceError, replace

@dataclass(frozen=True)
class Coordonnee:
  lat: float
  lon: float 


# frozen=True → immuable
hornu = Coordonnee(50, 3)

try:
  hornu.lat = 50.5
except FrozenInstanceError as e:
  print(f"Erreur: {e}")
  
nouveauHornu = replace(hornu, lon=4.2)
print(f"{hornu} → {nouveauHornu}")

villes = {
  hornu: 'Hornu'
}

# ---------------------------------------
# order=True → permet la comparaison par champ, dans l'ordre
@dataclass(order=True)
class Eleve:
  note: float # Attention, premier champ = critère de tri
  nom: str
  
  
classe = [
  Eleve(14, "Bernard"), 
  Eleve(17, "Damien"), 
  Eleve(17, "Gérard"), 
  Eleve(7, "Pierre"), 
]

for e in sorted(classe, reverse=True):
  print(f"  {e.note} {e.nom}")
  
print(f"Meilleur élève: {max(classe)}")

print("classe:", classe)