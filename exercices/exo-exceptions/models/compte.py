from exceptions import *

class Compte:
  
  def __init__(self, numero: str, titulaire: str, solde: float, decouvert_autorise: int = 0) -> None:
    self.numero = numero
    self.titulaire = titulaire
    self.__solde = solde
    self.decouvert_autorise = decouvert_autorise
    self.__bloque = False
  
  @property
  def solde(self) -> float:
    return self.__solde
  
  @property
  def bloque(self) -> bool:
    return self.__bloque
  
  def bloquer(self):
    self.__bloque = True
    
  def debloquer(self):
    self.__bloque = False
  
  def deposer(self, montant: float) -> None:
    self.__verifier(montant)
    self.__solde += montant

  def retirer(self, montant: float) -> None:
    self.__verifier(montant)
    disponible = self.__solde + self.decouvert_autorise
    if montant > disponible:
      raise SoldeInsuffisantError(self.numero, disponible, montant)
    self.__solde -= montant
    

  def __verifier(self, montant):
    if montant <= 0:
      raise MontantInvalideError(montant)
    if self.__bloque:
      raise CompteBloqueError(self.numero)

  