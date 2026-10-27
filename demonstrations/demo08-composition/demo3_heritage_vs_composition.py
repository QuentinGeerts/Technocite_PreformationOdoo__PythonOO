

# Héritage: Explosion des combinaisons (Pas bien)
class Notification:
  def envoyer(self, message: str) -> str: ...

class EmailTexte(Notification):
  def envoyer(self, message: str) -> str:
    return f"[Email] {message}"
  
class EmailHtml(Notification):
  def envoyer(self, message: str) -> str:
    return f"[Email] <p>{message}</p>"
  
class SmsTexte(Notification):
  def envoyer(self, message: str) -> str:
    return f"[SMS] {message}"

class SmsHtml(Notification):
  def envoyer(self, message: str) -> str:
    return f"[SMS] <p>{message}</p>"
  
class DiscordTexte(Notification):
  def envoyer(self, message: str) -> str:
    return f"[DISCORD] {message}"

class DiscordHtml(Notification):
  def envoyer(self, message: str) -> str:
    return f"[DISCORD] <p>{message}</p>"
  
  
# Composition (agrégation)

class Notification2:
  def __init__(self, canal, format_) -> None:
    self.canal = canal
    self.format = format_
    
  def envoyer(self, msg: str) -> str:
    return self.canal.transmettre(self.format.formater(msg))
  
# Définition des différents formatages
class FormatTexte:
  def formater(self, msg: str) -> str:
    return msg
    
class FormatHtml:
  def formater(self, msg: str) -> str:
    return f"<p>{msg}</p>"
    
class FormatMarkdown:
  def formater(self, msg: str) -> str:
    return f"**{msg}**"
  
# Définition des différents canaux

class CanalEmail:
  def transmettre(self, contenu: str) -> str:
    return f"[EMAIL] {contenu}"

class CanalDiscord:
  def transmettre(self, contenu: str) -> str:
    return f"[DISCORD] {contenu}"

class CanalSms:
  def transmettre(self, contenu: str) -> str:
    return f"[SMS] {contenu}"
  
  

for canal in [CanalDiscord(), CanalEmail(), CanalSms()]:
  for f in [FormatHtml(), FormatMarkdown(), FormatTexte()]:
    print(Notification2(canal, f).envoyer("J'ai faim"))