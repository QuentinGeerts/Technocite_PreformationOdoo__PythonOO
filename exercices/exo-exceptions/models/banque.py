from exceptions import *
from models.compte import Compte

class Banque:
  
  def __init__(self) -> None:
    self.__comptes: dict[str, Compte] = {}
  
  
  def ouvrir(self, compte: Compte):
    self.__comptes[compte.numero] = compte
    
  def trouver(self, numero: str) -> Compte:
    try:
      return self.__comptes[numero]
    except KeyError as e:
      raise CompteIntrouvableError(numero) from e
  
  def virement(self, source: str, destination: str, montant: float):
    if source == destination:
      raise CompteIdentiqueError(source)
    
    compte_source = self.trouver(source)
    compte_destination = self.trouver(destination)
    
    compte_source.retirer(montant)
    try:
      compte_destination.deposer(montant)
    except BanqueError:
      compte_source.deposer(montant)
      raise
      