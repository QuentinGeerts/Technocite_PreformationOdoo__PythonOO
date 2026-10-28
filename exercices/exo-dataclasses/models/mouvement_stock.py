from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True, order=True)
class MouvementStock:
  date: date # 1er car critère de tri principal
  reference: str
  quantite: int
  