from models import *
from exceptions import *

# Création de la banque et ouverture des comptes 

banque = Banque()
banque.ouvrir(Compte('BE01', 'Alice', 500, 100))
banque.ouvrir(Compte('BE02', 'Bob', 50))

# Traitez les opérations suivants :

operations = [
  ("depot", "BE01", -20),
  ("retrait", "BE01", 700),
  ("retrait", "BE01", 550),
  ("bloquer", "BE02", 0),
  ("virement", "BE01", "BE02", 30),
  ("virement", "BE01", "BE99", 30),
]

traitees = 0
reussies = 0

# Résultat attendu :
# 1. depot BE01 -20         → ERREUR : Montant invalide : -20.00 €
# 2. retrait BE01 700       → ERREUR : Solde insuffisant sur BE01 (disponible 600.00 €, demandé 700.00 €) — il manque 100.00 €
# 3. retrait BE01 550       → OK
# 4. bloquer BE02           → OK
# 5. virement BE01 → BE02 30 → ERREUR : Le compte BE02 est bloqué
# 6. virement BE01 → BE99 30 → ERREUR : Compte BE99 introuvable (cause : KeyError)
# Soldes : BE01 = -50.00 € | BE02 = 50.00 €
# Bilan : 6 opérations, 2 réussies, 4 échouées

for i, operation in enumerate(operations, start=1):
  
  type_operation = operation[0]

  # Extraction des données
  match type_operation:
    case "bloquer":
      _, numero, _ = operation
      libelle = f"{type_operation} {numero}"
    case "virement":
      _, source, destination, montant = operation
      libelle = f"{type_operation} {source} {destination} {montant}"
    case _:
      _, numero, montant = operation
      libelle = f"{type_operation} {numero} {montant}"
      

  # Effectuer les transactions
  try:
    match type_operation:
      case "depot":
        banque.trouver(numero).deposer(montant)

      case "retrait":
        banque.trouver(numero).retirer(montant)

      case "bloquer":
        banque.trouver(numero).bloquer()
      case "virement":
        banque.virement(source, destination, montant)
  
  except CompteIntrouvableError as e:
    print(f"{i}. {libelle} → ERREUR : {e} (cause : {type(e.__cause__).__name__})")
  except BanqueError as e:
    print(f"{i}. {libelle} → ERREUR : {e}")
  else:
    print(f"{i}. {libelle} → OK")
    reussies += 1
  finally:
    traitees += 1
    

print(f"Soldes: BE01 = {banque.trouver('BE01').solde:.2f} € | BE02 = {banque.trouver('BE02').solde:.2f} €")
print(f"Bilan : {traitees} opérations, {reussies} réussies, {traitees-reussies} échouées")
