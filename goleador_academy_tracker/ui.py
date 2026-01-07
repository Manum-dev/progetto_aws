import services

def mostra_menu():
    print("\n" + "="*30)
    print("      MENU PRINCIPALE")
    print("="*30)
    print("1. 🏫 Crea Nuovo Corso")
    print("2. 👤 Iscrivi Partecipante")
    print("3. 🍬 Assegna Goleador")
    print("4. 📊 Statistiche e AI")
    print("5. 📄 Esporta Report .txt")
    print("0. 🚪 Esci")

def esegui_scelta(scelta):
    if scelta == "1":
        nome_corso = input("\nNome del nuovo corso (es. Python Junior): ").strip()
        if nome_corso:
            successo, messaggio = services.aggiungi_corso(nome_corso)
            print(f" messaggio: {messaggio}")
        else:
            print("⚠️ Il nome del corso non può essere vuoto.")

    elif scelta == "2":
        print("\n--- ISCRIZIONE PARTECIPANTE ---")
        nome = input("Nome: ").strip()
        cognome = input("Cognome: ").strip()
        corso = input("In quale corso vuoi iscriverla? ").strip()
        
        if nome and cognome and corso:
            successo, messaggio = services.iscrivi_nuova_partecipante(nome, cognome, corso)
            print(f" risultato: {messaggio}")
        else:
            print("⚠️ Tutti i campi sono obbligatori.")

    elif scelta == "3":
        print("\n--- ASSEGNAZIONE PREMIO ---")
        n = input("Nome partecipante: ")
        c = input("Cognome partecipante: ")
        try:
            q = int(input("Quante Goleador ha vinto? "))
            successo, messaggio = services.registra_vincita_goleador(n, c, q)
            print(messaggio)
        except ValueError:
            print("❌ Errore: Inserisci un numero intero per le caramelle.")

    elif scelta == "4":
        s = services.calcola_statistiche()
        if not s:
            print("\n⚠️ Nessun dato presente. Inizia creando un corso e una partecipante!")
        else:
            print("\n" + "—"*20)
            print(f"🏆 TOP SCORER: {s['top_scorer']['nome']} con {s['top_scorer']['totale']} Goleador")
            print("—"*20)
            print("🤖 COMMENTO AI:")
            print(services.genera_commento_motivazionale())

    elif scelta == "5":
        successo, messaggio = services.genera_report_testuale()
        print(f"\n{messaggio}")

    elif scelta == "0":
        return False
    else:
        print("\n⚠️ Opzione non valida, riprova.")
    
    return True