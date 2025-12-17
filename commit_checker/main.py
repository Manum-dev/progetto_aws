from requests import get
import re
import uuid
import datetime
import json

# CONFIGURAZIONE
FILE_PATH = "db_commits.json"

def save_to_db(record):
    db_content = []
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as f:
            db_content = json.load(f)
    except:
        pass
    db_content.append(record)
    with open(FILE_PATH, "w", encoding='utf-8') as f:
        json.dump(db_content, f, indent=4, ensure_ascii=False)

def main():
    # RICHIESTA INPUT UTENTE
    print("=" * 60)
    print("🔍 SCRAPER COMMIT GITHUB")
    print("=" * 60)
    repo_url = input("\n📂 Inserisci l'URL della repository GitHub (es. https://github.com/user/repo/commits/branch): ").strip()
    
    if not repo_url:
        print("❌ URL non valido. Operazione annullata.")
        return


    print(f"\n📡 Tentativo di connessione a: {repo_url}")
    response = get(repo_url)
    
    # Salviamo l'HTML per capire cosa succede
    with open("debug_page.html", "w", encoding='utf-8') as f:
        f.write(response.text)

    if response.status_code != 200:
        print(f"❌ Errore HTTP {response.status_code}. GitHub ha bloccato la connessione.")
        return

    # Estraiamo username e repo dall'URL per le regex
    url_match = re.search(r'github\.com/([^/]+)/([^/]+)', repo_url)
    if not url_match:
        print("❌ URL non valido. Impossibile estrarre username e repository.")
        return
    
    username = url_match.group(1)
    repo_name = url_match.group(2)

    msgs = re.findall(rf'href="/{username}/{repo_name}/commit/[^>]*>(.*?)</a>', response.text)
    # Cerchiamo gli autori
    authors = re.findall(r'href="/([^/"]+)"[^>]*data-hovercard-type="user"', response.text)

    print(f"\nDebug: Trovati {len(msgs)} messaggi e {len(authors)} potenziali autori.")

    if not msgs:
        print("❌ Nessun commit trovato. Controlla il file 'debug_page.html' per vedere cosa ha risposto GitHub.")
        return

    commits_pagina = []
    # Usiamo un ciclo semplice per accoppiare i dati
    for i in range(len(msgs)):
        msg_clean = re.sub(r'<[^>]+>', '', msgs[i]).strip()
        author = authors[i] if i < len(authors) else "Unknown"
        commits_pagina.append({"autore": author, "messaggio": msg_clean})

    record = {
        "id": str(uuid.uuid4()),
        "createdAt": datetime.datetime.now().isoformat(),
        "repository": repo_url,
        "commits": commits_pagina
    }
    
    save_to_db(record)
    print(f"\n✅ Successo! {len(commits_pagina)} commit salvati in {FILE_PATH}")
    print("=" * 60)

if __name__ == "__main__":
    main()