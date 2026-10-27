from dataclasses import dataclass

# Sans dataclass
class PointClassique:
  def __init__(self, x: float, y: float, z: float = 0.0) -> None:
    self.x = x
    self.y = y
    self.z = z
    
  def __repr__(self) -> str:
    return f"pointClassique(x={self.x!r}, y={self.y!r}, z={self.z!r})"
  
  def __eq__(self, value: object) -> bool:
    if not isinstance(value, PointClassique):
      return False
    return (self.x, self.y, self.z) == (value.x, value.y, value.z)
  
  
# Avec Dataclass
@dataclass
class Point:
  x: float
  y: float
  z: float = 0.0
  
  def distance_origine(self) -> float:
    return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
  
  
p = Point(2, 5) # __init__ qui a été généré

print(p) # __repr__ qui a été généré

print(Point(1, 2, 3) == Point(1, 2, 3)) # __eq__ qui a été généré

print(f"p.distance_origin():", p.distance_origine())

p_casse = Point("a", "b")
print("p_casse:", p_casse) # → __post_init__