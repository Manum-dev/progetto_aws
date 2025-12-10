def mostra_feedback(messaggio: str) -> None:
    """
    Restituisce il feedback formattato nella maniera desiderata.
    """
    simbol: str = "*"*30
    print(f"""
{simbol}
{messaggio}
{simbol}
""")

def mostra_domanda(domanda: str) -> None: 
    """
    Questa funzione restituisce la domanda e le opzioni della riposta. 
    """
    
    print(domanda)

def print_numero_domanda(valore_domanda_corrente: int, valore_domande_totali: int) -> None:
    """Restituisce l'indicatore della domanda corrente rispetto al numero di domande totali"""
    print("------------------------------")
    print(f"Domanda {valore_domanda_corrente} di {valore_domande_totali}")
    print("------------------------------")


def print_gioco_terminato() -> None:
    print("*"*30)
    print("Gioco terminato. Ecco i risultati:")
    print("*"*30)


def genera_feedback(is_corretta: bool) -> str:
    """
    Restituisce il messaggio che indica all'utente se ha indovinato la risposta oppure no.
    Questa funzione viene eseguita solo se la funzione di validazione restituisce true. 
    """
    if is_corretta == True:
        return "Hai indovinato!"
    else:
        return "Non hai indovinato."


def raccogli_risposta() -> str:
    """
    Questa funzione si occupa solamente di prendere l'input dell'utente. 
    Il controllo di tale valore avverrà attraverso una funzione dedicata.
    """ 
    return input("Inserisci la tua scelta: ")
    
def mostra_riepilogo(risultati: list[dict[str, str | bool]]) -> None:
    print("\n--- RIEPILOGO RISPOSTE ---")
    for i, ris in enumerate(risultati):
        print(f"{i + 1}. {ris['domanda']} - La tua risposta: {ris.get('scelta_utente', 'N/A')}")
    print("--------------------------")

def mostra_risultati_finali(esatte: int, errate: int, totale: int, percentuale: float, superato: bool) -> None:
    print("\n" + "="*40)
    print("           RISULTATO FINALE")
    print("="*40)
    print(f"Domande totali:    {totale}")
    print(f"Risposte esatte:   {esatte}")
    print(f"Risposte errate:   {errate}")
    print("-" * 40)
    print(f"Punteggio:         {percentuale:.1f}%") 
    print("-" * 40)
    
    if superato:
        print("ESITO:             SUPERATO!")
    else:
        print("ESITO:             NON SUPERATO")
    print("="*40 + "\n")


def gestisci_menu_fine_gioco(counter_attuale: int, totale_domande: int, risultati: list) -> int | None:
    """
    Gestisce la logica di fine gioco. 
    Restituisce None se l'utente vuole uscire, oppure il nuovo indice se vuole rivedere una domanda.
    """
    mostra_riepilogo(risultati)
    scelta = input("\nInserisci il numero della domanda da rivedere o premi INVIO per terminare: ")
    
    if scelta == "":
        return None
    elif scelta.isdigit():
        numero = int(scelta)
        if 1 <= numero <= totale_domande:
            print(f"Torna alla domanda {numero}...")
            return numero - 1 
        else:
            print("Numero non valido.")
            return counter_attuale
    else:
        print("Input non valido.")
        return counter_attuale