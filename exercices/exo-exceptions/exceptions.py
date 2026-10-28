
class BanqueError(Exception):
  pass

class MontantInvalideError(BanqueError):
  def __init__(self, montant: float) -> None:
    super().__init__(f"Montant invalide: {montant:.2f} €")
    self.montant = montant

class SoldeInsuffisantError(BanqueError): 
  def __init__(self, numero: str, disponible: float, demande: float) -> None:
    self.numero = numero
    self.disponible = disponible
    self.demande = demande
    super().__init__(f"Solde insuffisant sur {numero} (disponible {disponible} €, demandé {demande} €) - il manque {self.manque} €")
    
  @property
  def manque(self) -> float:
    return self.demande - self.disponible
  

class CompteBloqueError(BanqueError):
  def __init__(self, numero: str) -> None:
    super().__init__(f"Le compte {numero} est bloqué") 
    self.numero = numero

class CompteIntrouvableError(BanqueError):
  def __init__(self, numero: str) -> None:
    super().__init__(f"Compte {numero} est introuvable")


class CompteIdentiqueError(BanqueError):
  def __init__(self, numero: str) -> None:
    super().__init__(f"Les deux comptes {numero} sont identiques")
