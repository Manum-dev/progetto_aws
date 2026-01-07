import json
import os
from config import FILE_DATABASE

def carica_dati(): # <--- Verifica questo nome
    if not os.path.exists(FILE_DATABASE):
        return {"corsi": [], "partecipanti": []}
    with open(FILE_DATABASE, 'r', encoding='utf-8') as f:
        return json.load(f)

def salva_dati(dati):
    with open(FILE_DATABASE, 'w', encoding='utf-8') as f:
        json.dump(dati, f, indent=4, ensure_ascii=False)