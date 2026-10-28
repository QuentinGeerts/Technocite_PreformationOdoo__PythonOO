from dataclasses import dataclass

@dataclass(frozen=True)
class Adresse:
  rue: str
  code_postal: int
  ville: str