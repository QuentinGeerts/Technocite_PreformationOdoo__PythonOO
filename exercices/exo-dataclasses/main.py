from dataclasses import FrozenInstanceError
from models import Adresse, Article, Entrepot, MouvementStock

from datetime import date

# 1.  Créez une adresse, puis essayez de modifier sa ville. Capturez l'erreur.

adresse = Adresse('Rue Henri Degorge 23', 7301, 'Hornu')

try:
  adresse.ville = 'Mons' # type: ignore
except FrozenInstanceError as e:
  print(f"Modification de la ville: {e}")
  
# 2.  Créez 4 articles : 
# Clavier (49,90 € × 10), 
# Souris (19,90 € × 25), 
# Écran (189 € × 0), 
# Casque (79 € × 4). 

clavier = Article('CLA-01', 'Clavier', 49.90, 10, ['périphérique', 'bureautique', 'clavier'])
souris = Article('SOU-01', 'Souris', 19.90, 25, ['périphérique', 'souris'])
ecran = Article('ECR-01', 'Écran', 189, 0)
casque = Article('CAS-01', 'Casque', 79, 4)

# Affichez-en un avec print.

print(f"clavier:", clavier)
print(f"souris:", souris)
print(f"ecran:", ecran)
print(f"casque:", casque)

# 3.  Créez un 2e clavier identique mais avec d'autres tags. Comparez-les avec == puis avec is.

clavier2 = Article('CLA-01', 'Clavier', 49.90, 10, ['gaming'])
print(f"==: {clavier == clavier2} | is: {clavier is clavier2}")

# 4.  Tentez de créer un article à -5 €. Capturez l'erreur.

try:
  Article('article -5€', 'Cadeau', -5)
except ValueError as e:
  print(f"Article invalide: {e}")
  
# 5.  Ajoutez les 4 articles à un entrepôt ; affichez sa valeur totale et les articles en rupture.

entrepot = Entrepot('Mon Business', adresse, [clavier, souris])

for article in [ecran, casque]:
  entrepot.ajouter(article)
  
print(f"Entrepot: {entrepot.nom} - Valeur totale: {entrepot.valeur_totale():.2f} €")
print(f"Articles en rupture: {[article.nom for article in entrepot.en_rupture()]}")

# 6.  Créez 4 mouvements dans le désordre, triez-les avec sorted() et affichez-les.

mouvements = [
  MouvementStock(date(2026, 10, 28), 'ECR-01', -3),
  MouvementStock(date(2026, 10, 2), 'CLA-01', 10),
  MouvementStock(date(2026, 10, 5), 'SOU-01', -5),
  MouvementStock(date(2026, 10, 12), 'CAS-01', 4),
]

for mouvement in sorted(mouvements):
  print(mouvement)