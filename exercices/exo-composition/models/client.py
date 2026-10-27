class Client:
  def __init__(self, nom: str, email: str) -> None:
    self.nom = nom
    self.email = email

  def __str__(self) -> str:
    return f"{self.nom} ({self.email})"
  