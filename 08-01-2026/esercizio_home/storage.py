import json
import os

def load_data(filepath):
    """
    Carica i dati dal file JSON se esiste, altrimenti restituisce una lista vuota.
    Gestisce errori di file non trovato o JSON corrotto restituendo una lista vuota.
    """
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                if content.strip():
                    data = json.loads(content)
                    if isinstance(data, list):
                        return data
        except (json.JSONDecodeError, OSError):
            # In caso di file corrotto o errori IO, ripartiamo da lista vuota
            pass
    return []

def save_data(filepath, new_data):
    """
    Aggiunge i nuovi dati a quelli esistenti e salva il file.
    Restituisce una tupla: (successo: bool, errore: str|None, totale_record: int)
    """
    if not new_data:
        return False, "Nessun dato da salvare", 0

    try:
        existing_data = load_data(filepath)
        final_data = existing_data + new_data
        
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(final_data, f, indent=4)
        
        return True, None, len(final_data)
    except Exception as e:
        return False, str(e), 0
