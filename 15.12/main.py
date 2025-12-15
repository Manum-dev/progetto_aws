
def lista_spesa_filled(lista_utente: list[str]) ->bool:
    return len(lista_utente) == 4

    
def get_prodotto_inserito(prodotto: str)->str:
    if not prodotto:
        raise ValueError("Prodotto Vuoto", "ALERT")
    return prodotto.strip().lower()
    
def get_input_from_utente(text: str) -> str:
    if not text:
        raise ValueError("Testo prompt vuoto")
    return input(text)
    

def log_message(message: str, type: str) -> str:
    if not message:
        raise ValueError("Messaggio vuoto")
    match type:
        case "ALERT":
            icon = "⚠️"
        case "INFO":
            icon = "ℹ️"
        case "SUCCESS":
            icon = "🎉"
        case _:  # Caso default (opzionale ma consigliato)
            icon = "📝"
    
    print (f"{icon} {message}")

def carrello_aperto()-> type:
    log_message("carrello aperto")
    
def main() -> None: 
    log_message("Start del programa", "INFO")

    
    lista_spesa: list[str] = ["cipolle","latte","lattughe","birra"]
    lista_utente: list[str]=[]

    print(f"La tua lista della spesa è composta da {lista_spesa}")

    while not lista_spesa_filled(lista_utente):

        #input
        prodotto = get_input_from_utente("Inserisci un prodotto da inserire nel carrello: ")

        if not prodotto.strip():
            log_message("input vuoto", "Alert")
            continue


      # Normalizzazione
        try:
            prodotto_inserito = get_prodotto_inserito(prodotto)
        except ValueError as e:
            log_message(str(e), "ALERT")
            continue
        
        # Controllo: è nella lista della spesa?
        if prodotto_inserito not in lista_spesa:
            log_message(f"'{prodotto_inserito}' non è nella lista!", "ALERT")
            continue
        
        # Controllo: già inserito?
        if prodotto_inserito in lista_utente:
            log_message(f"'{prodotto_inserito}' già inserito!", "ALERT")
            continue

        if prodotto_inserito in lista_spesa:
            carrello_aperto = [p for p in lista_spesa if p in lista_spesa]
            print(f"{prodotto_inserito},  apertura del carello in corso")

        
        # Aggiungi alla lista UTENTE (non lista_spesa!)
        lista_utente.append(prodotto_inserito)
        log_message(f"'{prodotto_inserito}' aggiunto!", "SUCCESSS")
       
        # Feedback progresso
        log_message(f"Carrello: {len(lista_utente)}/4 prodotti", "INFO")
        
        # Mostra cosa manca
        if not lista_spesa_filled(lista_utente):
            mancanti = [p for p in lista_spesa if p not in lista_utente]
            log_message(f"Mancano: {mancanti}", "INFO")
        print()  # Riga vuota per leggibilità

    


    
    # Spesa completata!
    print("\n" + "=" * 50)
    log_message("🎉 Tutti i prodotti inseriti!", "SUCCESS")
    log_message("🚀 CARRELLO APERTO!", "SUCCESS")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()
                

