utenti: dict[str,str] = {
    "alice": "admin",
    "bob": "user",
    "charlie": "guest",
}

for username, ruolo in utenti.items():
    print(f"Username: {username}, Ruolo: {ruolo}")