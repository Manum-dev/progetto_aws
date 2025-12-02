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

def is_risposta_esatta(scelta: str) -> bool:
    if scelta.upper() == "A":
        return True
    else:
        return False


def genera_feedback(is_corretta: bool) -> str:
    """
    Restituisce il messaggio che indica all'utente se ha indovinato la risposta oppure no.
    Questa funzione viene eseguita solo se la funzione di validazione restituisce true. 
    """
    if is_corretta == True:
        return "Hai indovinato!"
    else:
        return "Non hai indovinato. Ritenta!"

def valida_scelta(scelta: str) -> bool:
    """
    Questa funzione prende un valore di tipo stringa e verifica che la risposta sia una delle opzioni tra A, B, C e D. 
    Se la risposta è una stringa vuota, restituisce false, idem se la risposta non è una di quelle sopra elencate.
    """
    scelta_tmp = scelta.upper()
    if scelta_tmp == "A" or scelta_tmp == "B" or scelta_tmp == "C" or scelta_tmp == "D":
        return True
    else: 
        return False

def mostra_domanda() -> None: 
    """
    Questa funzione restituisce la domanda e le opzioni della riposta. 
    """
    
    print(
"""
Chi parteciperà a Sanremo 2026?

A. Nayt
B. La Nina
C. Nilla Pizzi
D. Rocco Papaleo
"""
    )

def raccogli_risposta() -> str:
    """
    Questa funzione si occupa solamente di prendere l'input dell'utente. 
    Il controllo di tale valore avverrà attraverso una funzione dedicata.
    """ 
    return input("Inserisci la tua scelta: ")
    

def main():
    is_risposta_corretta: bool = False
    while True:
        mostra_domanda()
        risposta_da_validare: str = raccogli_risposta()
        risposta_validata: bool = valida_scelta(risposta_da_validare)
        feedback: str = ""

        if risposta_validata == True:
            is_risposta_corretta = is_risposta_esatta(risposta_da_validare)
            feedback = genera_feedback(is_risposta_corretta)
        else: 
            feedback = "Inserisci solo la risposta tra le opzioni elencate"

        mostra_feedback(feedback)
        if is_risposta_corretta == True: 
            break

# Entry point del nostro programma
main()
