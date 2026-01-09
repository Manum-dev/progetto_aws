'''📜 Dev 2 (Storage)
Obiettivo: Non perdere i dati.
Importa il modulo json.
Crea salva_personaggio(personaggio): apre db.json in scrittura e scarica la lista.
Crea carica_personaggi(): apre db.json in lettura.
Trappola: Cosa succede se il file db.json non esiste ancora (primo avvio)? 
Dovrai gestire l'eccezione FileNotFoundError o controllare se il file esiste con os.path.'''

import json
import os
def salva_personaggio(nuovi_dati):
    """
    Aggiunge i nuovi dati a quelli esistenti e salva il file db.json.
    Accetta sia un singolo dizionario che una lista di dizionari.
    
    Restituisce una tupla: (successo: bool, errore: str|None, totale_record: int)
    """
    try:
        # Carica dati esistenti
        personaggi = carica_personaggi()
        
        # Aggiunge i nuovi dati
        if isinstance(nuovi_dati, list):
            personaggi.extend(nuovi_dati)
        else:
            personaggi.append(nuovi_dati)
            
        # Salva tutto
        with open('db.json', 'w') as f:
            json.dump(personaggi, f, indent=4)
            
        return (True, None, len(personaggi))
        
    except Exception as e:
        return (False, str(e), 0)
def carica_personaggi():
    """
    Carica la lista dei personaggi dal file db.json.
    Restituisce una lista vuota se il file non esiste.
    """
    if os.path.exists('db.json'):
        try:
            with open('db.json', 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return [] # Restituisce lista vuota se il file è corrotto o vuoto
    else:
        return []