import repository
from datetime import datetime
from config import CHIAVE_API_GEMINI

# Gestione sicura di Gemini AI con la NUOVA libreria
try:
    from google import genai  # ← NUOVO import
    client = genai.Client(api_key=CHIAVE_API_GEMINI) 
    AI_ATTIVA = True
except (ImportError, Exception) as e:
    print(f"DEBUG AI: Errore durante l'avvio di Gemini: {e}")
    AI_ATTIVA = False

def aggiungi_corso(nome_corso):
    dati = repository.carica_dati()
    if nome_corso.lower() in [c.lower() for c in dati["corsi"]]:
        return False, f"Il corso '{nome_corso}' esiste già."
    dati["corsi"].append(nome_corso)
    repository.salva_dati(dati)
    return True, f"Corso '{nome_corso}' creato con successo!"

def iscrivi_nuova_partecipante(nome, cognome, nome_corso):
    dati = repository.carica_dati()
    corsi_min = [c.lower() for c in dati["corsi"]]
    if nome_corso.lower() not in corsi_min:
        return False, f"Il corso '{nome_corso}' non esiste."
    
    indice = corsi_min.index(nome_corso.lower())
    nome_corso_corretto = dati["corsi"][indice]

    nuova_p = {
        "nome": nome, 
        "cognome": cognome, 
        "corso": nome_corso_corretto,  # ← Corretto
        "premi": []
    }
    dati["partecipanti"].append(nuova_p)
    repository.salva_dati(dati)
    return True, f"{nome} iscritta correttamente a {nome_corso_corretto}!"

def registra_vincita_goleador(nome, cognome, quantita):
    dati = repository.carica_dati()
    for p in dati["partecipanti"]:
        if p["nome"].lower() == nome.lower() and p["cognome"].lower() == cognome.lower():
            p["premi"].append({
                "quantita": quantita,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            })
            repository.salva_dati(dati)
            return True, f"Assegnate {quantita} Goleador!"
    return False, "Partecipante non trovata."

def calcola_statistiche():
    dati = repository.carica_dati()
    if not dati["partecipanti"]:
        return None

    stats = {
        "per_corso": {corso: 0 for corso in dati["corsi"]},
        "top_scorer": {"nome": "Nessuna", "totale": 0}
    }

    for p in dati["partecipanti"]:
        totale_p = sum(premio["quantita"] for premio in p["premi"])
        stats["per_corso"][p["corso"]] += totale_p
        if totale_p > stats["top_scorer"]["totale"]:
            stats["top_scorer"] = {"nome": f"{p['nome']} {p['cognome']}", "totale": totale_p}
    return stats

def genera_commento_motivazionale():
    if not AI_ATTIVA:
        return "Bravissime tutte! Continuate a programmare per vincere altre Goleador!"
    
    stats = calcola_statistiche()
    if not stats: 
        return "Inizia a inserire dati per ricevere consigli dall'AI!"
    
    try:
        prompt = f"Scrivi un micro-commento motivante per queste studentesse: {stats['per_corso']}. La migliore è {stats['top_scorer']['nome']}."
        # ← NUOVO modo di chiamare l'API
        risposta = client.models.generate_content(
            model='gemini-2.0-flash-exp',
            contents=prompt
        )
        return risposta.text
    except Exception as e:
        return f"Errore AI: {e}"

def genera_report_testuale():
    stats = calcola_statistiche()
    if not stats:
        return False, "⚠️ Nessun dato disponibile per generare il report."

    nome_file = "report_academy.txt"
    try:
        with open(nome_file, "w", encoding="utf-8") as f:
            f.write(f"=== GOLEADOR ACADEMY REPORT ===\n")
            f.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n")
            f.write(f"Top Scorer: {stats['top_scorer']['nome']} con {stats['top_scorer']['totale']} Goleador\n")
            f.write("-" * 30 + "\n")
            for corso, tot in stats["per_corso"].items():
                f.write(f"Corso {corso}: {tot} Goleador totali\n")
        return True, f"Report salvato in {nome_file}"
    except Exception as e:
        return False, f"Errore durante il salvataggio: {e}"