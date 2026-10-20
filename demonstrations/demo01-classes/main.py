from models.voiture import Voiture
# from example.models.personne import Personne

v1 = Voiture()
v2 = Voiture("Kia", "Ceed")
v3 = Voiture(modele="Corsa", marque="Opel")
v4 = Voiture("Fiat", "Punto", kilometrage=2136)

v1.marque = "Volvo"

print("Voiture 1:", v1)
print("Voiture 2:", v2)
print("Voiture 3:", v3)

print("Voiture 1 - Marque:", v1.marque)
print("Voiture 2 - Marque:", v2.marque)
print("Voiture 3 - Marque:", v3.marque)

v1.rouler(150)
v2.rouler(450)
v3.rouler(50)
v4.rouler(70)


print(v1.se_decrire())
print(v2.se_decrire())
print(v3.se_decrire())
print(v4.se_decrire())
