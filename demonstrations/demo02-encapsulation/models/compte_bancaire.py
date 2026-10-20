try:
  # Import via le package (ex: depuis main.py)
  from .titulaire import titulaire
except ImportError:
  # Exécution directe du fichier (python models/compte_bancaire.py)
  from titulaire import titulaire

class compte_bancaire:

  def __init__(self, titulaire: titulaire, solde_initial: float = 0) -> None:
    if solde_initial < 0:
      raise ValueError("Le solde initial ne peut pas être négatif.")
    
    self.titulaire = titulaire # public
    self._solde = solde_initial # protected
    self.__historique: list[str] = [] # private
  
  # Méthodes publiques - Interface du compte
  
  def deposer(self, montant: float) -> None:
    if montant <= 0:
      raise ValueError("Le montant du dépôt doit être positif.")
    
    self._solde += montant
    self.__ajouter_transaction(f"Dépôt: {montant} €")
  
  def retirer(self, montant: float) -> None:
    if montant <= 0:
      raise ValueError("Le montant du retrait doit être positif.")
    if montant > self._solde:
      raise ValueError("Solde insuffisant.")
    
    self._solde -= montant
    self.__ajouter_transaction(f"Retrait: {montant} €")
    
  def obtenir_solde(self) -> float:
    return self._solde
  
  def obtenir_historique(self) -> list[str]:
    return list(self.__historique)
  
  # Méthodes internes - Accessibles uniquement dans le compte
  
  def __ajouter_transaction(self, description: str) -> None:
    self.__historique.append(description)
  
  
if __name__ == '__main__':
  t = titulaire('Test', 'Test')
  cb = compte_bancaire(t)
  
  cb.deposer(500)
  cb.retirer(20)