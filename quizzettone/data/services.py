from repository import get_file

def get_domanda_e_risposta_singola(file_path: str) -> str:
    with get_file(file_path) as file:
        content = file.read()
        return content


def get_lista_domande_e_risposte(file_path: str) -> list[str]:
    lista_domande: list[str] = []

    with get_file(file_path) as f:
        for i in f:
            lista_domande.append(i.strip())
    return lista_domande 


def estrai_indice_simbolo(content: str) -> int: 
    return content.index("£")

def estrai_domanda(content: str, index: int) -> str:
    return content[0:index]

def estrai_risposta(content: str, index: int) -> str:
    return content[index+1:]

def valida_scelta(scelta: str) -> bool:
    """
    Questa funzione prende un valore di tipo stringa e verifica che la risposta sia una delle opzioni tra A, B, C e D. 
    Se la risposta è una stringa vuota, restituisce false, idem se la risposta non è una di quelle sopra elencate.
    """
    scelta_tmp = scelta.upper()
    return scelta_tmp in ["A", "B", "C", "D"]

def is_risposta_esatta(scelta: str, risposta_esatta: str) -> bool:
    return scelta.upper() == risposta_esatta

def get_numero_domanda_corrente(value: int) -> int:
    """Restituisce l'indice della domanda corrente, più uno, per l'utente"""
    return value + 1

def get_counter_aggiornato(counter: int, input: str) -> int:
    """Restituisce il valore del counter aggiornato per proseguire sulla domanda successiva o precedente"""
    if input.upper() == "P":
        return counter - 1
    else:
        return counter + 1
    
def genera_statistiche(risultato_finale: list[dict[str, str | bool]]) -> dict[str, int]:
    statistica: dict[str, int] = {}

    risposte_esatte: int = 0
    risposte_non_esatte: int = 0

    for i in risultato_finale: 
        if i["risposta_corretta"]:
            risposte_esatte += 1
        else:
            risposte_non_esatte += 1

    statistica["risposte_esatte"] = risposte_esatte
    statistica["risposte_non_esatte"] = risposte_non_esatte
    return statistica

def calcola_percentuale(parte: int, totale: int) -> float:
    """Calcola la percentuale (0-100) date due quantità."""
    if totale == 0:
        return 0.0
    return (parte / totale) * 100

def verifica_superamento(percentuale: float, soglia: float = 60.0) -> bool:
    """Restituisce True se la percentuale è maggiore o uguale alla soglia."""
    return percentuale >= soglia

def recupera_dati_domanda(nome_file: str) -> dict[str, str]:
    """Gestisce il parsing di ogni domanda"""
    content: str = get_domanda_e_risposta_singola(f"domande_risposte/{nome_file}")
    index: int = estrai_indice_simbolo(content)
    return {
        "domanda" : estrai_domanda(content, index),
        "risposta" : estrai_risposta(content, index)
    }

def aggiorna_lista_risultati(lista_risultati: list, nuovo_risultato: dict, indice: int) -> None:
    """Aggiorna la lista dei risultati gestendo sia l'inserimento che la modifica."""
    if indice < len(lista_risultati):
        lista_risultati[indice] = nuovo_risultato
    else:
        lista_risultati.append(nuovo_risultato)