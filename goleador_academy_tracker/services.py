import repository
import google.generativeai as genai
from config import CHIAVE_API_GEMINI, FILE_DATABASE
from datetime import datetime

# Configurazione Gemini
genai.configure(api_key=CHIAVE_API_GEMINI)
modello = genai.GenerativeModel('gemini-1.5-flash')

# ... (tieni le altre funzioni precedenti uguali) ...

def genera_commento_motivazionale():
    stats = calcola_statistiche()
    if not stats:
        return "Ancora nessun dato disponibile per un commento."

    # Prepariamo il testo da inviare a Gemini
    testo_per_ai = f"Queste sono le statistiche attuali dei corsi: {stats['per_corso']}. "
    testo_per_ai += f"La miglior partecipante è {stats['top_scorer']['nome']} con {stats['top_scorer']['totale']} Goleador."
    
    prompt = (
        f"Agisci come un tutor di programmazione simpatico e motivante. "
        f"Basandoti su questi dati: {testo_per_ai}, scrivi un commento brevissimo (max 2 frasi) "
        f"per incoraggiare le ragazze del corso a dare il massimo."
    )

    try:
        risposta = modello.generate_content(prompt)
        return risposta.text
    except Exception as e:
        return "Continuate così, il codice non ha segreti per voi! (Commento AI non disponibile)"