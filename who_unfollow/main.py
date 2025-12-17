from requests import get
import re
import uuid
import datetime
import json

"""
1. ho bisogno di una funzione di modellazione della lista che trasforma la lista in un oggetto come segue
[
  {
    id: "dkdxkkdkd"
    createdAt: data e ora
    users: []
    numberOfUsers
  }
]

2. apro il mio db con open, estraggo il contenuto, che è una lista
3. faccio append del nuovo elemento sulla lista che ho appena preso dal db
4. sovrascrivo il vecchio db con il dato aggiornato
"""

BASE_URL: int = "https://github.com" 
END_URL: str = "tab=followers" 

PATTERN = r'<a\s+[^>]*href="https://github\.com/([^/]+)\?page=(\d+)&amp;tab=followers"[^>]*>Next</a>'
PATTERN_USER = r'<span class="Link--secondary(?: pl-1)?">([^<]+)</span>' 


def save(db_name: str, new_value: dict[str, str]) -> bool:
  db: list[str] = []
  with open(f"db/{db_name}", "r") as f:
    value = json.load(f)
    db.extend(value)
  
  db.append(new_value)

  with open(f"db/{db_name}", "w", encoding='utf-8') as f:
    json.dump(db, f, indent=4, ensure_ascii=False)

  return bool

def create_record_object(user_list: list[str]) -> dict[str, str]:
    if not user_list:
        return None
    
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    clean_date = now_utc.isoformat(timespec='milliseconds').replace('+00:00', 'Z')

    return {
        'id': str(uuid.uuid4()),  
        'createdAt': clean_date,  
        'users': user_list,
        'numberOfUsers': len(user_list)
    }

def is_next_button_present(text: str) -> bool:
  if not text:
    raise ValueError("La stringa non puo essere vuota!")

  return bool(re.search(PATTERN, text))

def main() -> None:
  
  print("Start del programma")

  controller: bool = False
  counter: int = 0

  # ==================
  # Primo while
  # ==================

  while True:

    try:
      nome_utente: str = input("Inserisci lo username del profilo github che vuoi analizzare:")

      if not nome_utente:
        raise ValueError("Il nome utente non può essere vuoto")
      
      # TODO: il nome exit esiste già come profilo  
      if nome_utente.strip().lower() == "exit":
        break

      print(f"Stai cercando: {nome_utente}")

      response = get(f"{BASE_URL}/{nome_utente}")

      if response.status_code == 404:
        print("Il profilo non esiste")
      else:
        print(f"Profilo {nome_utente} trovato")
        controller = True
        break 

    except Exception as e:
      print(f"OPS! Qualcosa è andato storto: {e}")
      
  # ==================
  # Secondo while
  # ==================

  while controller:
    counter += 1
    url = f"{BASE_URL}/{nome_utente}?page={counter}&{END_URL}"
    try:
      response = get(url)
      print(response.status_code)

      with open(f"tmp/pagina-{counter}.txt", "w") as f:
        f.write(response.text)
        controller = is_next_button_present(response.text)
        print("File salvato")

    except Exception as e:
      print(f"Errore: {e}") 

  lista_utenti: list[str] = [] 

  for i in range(counter):
    print(f"Counter: {i+1}")
    with open(f"tmp/pagina-{i+1}.txt", "r") as f:
      text = f.read()
      lista_utenti.extend(re.findall(PATTERN_USER, text))

  save("db.json", create_record_object(lista_utenti))
  print("Fine programma, arrivederci.")
 
if __name__ == "__main__":
  main()