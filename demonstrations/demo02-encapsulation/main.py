from models import titulaire, compte_bancaire

t1 = titulaire("Geerts", "Quentin")
c1 = compte_bancaire(t1, 0)

c1.deposer(500)
c1.retirer(200)
c1.retirer(20)

# Liste des transactions
for transaction in c1.obtenir_historique():
  print(" -", transaction)

# Récupération d'un champ protected
print("Solde du compte:", c1._solde) # 300 → À éviter hors de la classe

# Récupération d'un champ privé
try:
  print(c1.__historique)
except AttributeError as e:
  print("Erreur:", e)

# print("Historique des transactions:", c1._compte_bancaire__historique) # Fonctionne mais attention

