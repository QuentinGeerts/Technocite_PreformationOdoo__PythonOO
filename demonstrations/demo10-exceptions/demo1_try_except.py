# Exception
# → Une exception est un objet levé quand quelque chose se passe mal.
# <!> Si personne ne l'attrape, le programme s'arrête avec un traceback


# 1.  Sans gestion : le programme planterait

# print(10 / 0) # ZeroDivisionError
# int("a") # ValueError
# [1, 2, 3][3] #IndexError
# { "a": 0 }["b"] # KeyError


# 2.  try / except [de base]

try:
  resultat = 10 / 0
except ZeroDivisionError:
  print(f"1.  Division par zéro impossible")
  
# 3.  Récupérer l'objet exception avec le mot-clef "as"

try:
  int("a")
except ValueError as e:
  print(f"2.  Type: {type(e).__name__} | message: {e}")  
  

# 4.  Plusieurs except : le premier qui correspond qui gagne

def lire_note(saisies: list[str], index: int) -> float: 
  try:
    note = float(saisies[index])
    return 20 / note
  except IndexError:
    print(f"  Pas de saisie à l'index {index}")
  except ValueError:
    print(f"  '{saisies[index]}' n'est pas un nombre")
  except ZeroDivisionError:
    print(f"  La note ne peut pas être 0")

  return 0.0

saisies = ["10", "a", "0"]
for i in range(len(saisies)):
  note = lire_note(saisies, i)
  print(f"Note: {note}")
  

# 5.  Un même except pour plusieurs types (tuple)
print(f"--- 5.  Un même except pour plusieurs types (tuple) ---")

for valeur in ["12", "x", None]:
  try:
    print(f"{valeur} → {int(valeur)}")
  except (ValueError, TypeError) as e:
    print(f"  {valeur!r} → conversion impossible ({type(e).__name__})")
    
    
# 6.  else et finally
# else: exécuté seulement si aucune exception n'a été levée
# finally: exécuté dans tous les cas (succès, erreur, return, ...)

print(f"--- 6.  else et finally ---")

def diviser(a: float, b: float) -> float:
  try: 
    resultat = a / b
  except ZeroDivisionError:
    print(f"{a} / {b} → division par 0 impossible")
  else:
    print(f"{a} / {b} = {resultat}")
    return resultat
  finally:
    print("Fin du calcul")
    
  return 0.0

resultat = diviser(42, 2) # 21
resultat = diviser(42, 0) # 0

# 7.  Hierarchie des exceptions
# BaseException
#  ├── BaseExceptionGroup
#  ├── GeneratorExit
#  ├── KeyboardInterrupt
#  ├── SystemExit
#  └── Exception
#       ├── ArithmeticError
#       │    ├── FloatingPointError
#       │    ├── OverflowError
#       │    └── ZeroDivisionError
#       ├── AssertionError
#       ├── AttributeError
#       ├── BufferError
#       ├── EOFError
#       ├── ExceptionGroup
#       ├── ImportError
#       │    └── ModuleNotFoundError
#       ├── LookupError
#       │    ├── IndexError
#       │    └── KeyError
#       ├── MemoryError
#       ├── NameError
#       │    └── UnboundLocalError
#       ├── ReferenceError
#       ├── RuntimeError
#       │    ├── NotImplementedError
#       │    └── RecursionError
#       ├── StopAsyncIteration
#       ├── StopIteration
#       ├── SyntaxError
#       │    └── IndentationError
#       │         └── TabError
#       ├── SystemError
#       ├── TypeError
#       ├── ValueError
#       │    └── UnicodeError
#       │         ├── UnicodeDecodeError
#       │         ├── UnicodeEncodeError
#       │         └── UnicodeTranslateError
#       └── OSError
#            ├── ConnectionError
#            │    ├── BrokenPipeError
#            │    ├── ConnectionAbortedError
#            │    ├── ConnectionRefusedError
#            │    └── ConnectionResetError
#            ├── FileExistsError
#            ├── FileNotFoundError
#            ├── InterruptedError
#            ├── IsADirectoryError
#            ├── NotADirectoryError
#            ├── PermissionError
#            ├── ProcessLookupError
#            └── TimeoutError


print(f"ZeroDivisionError hérite de ArithmeticError: {issubclass(ZeroDivisionError, ArithmeticError)}")

try:
  {'a': 0}['b']
except LookupError as e:
  print(f"Attrapé via le parent LookupError: {type(e).__name__}")
  

try:
  [1][1]
except Exception: # A ne pas placer en premier → toujours en dernier
  print("Exception (générique) qui attrape TOUTE exception")
except IndexError:
  print("IndexError (spécifique) attrapé en premier")