import services

def mostra_menu():
    print("\n--- 🏆 GESTIONALE PREMIAZIONI ---")
    print("1. Aggiungi nuovo corso")
    print("2. Iscrivi partecipante")
    print("3. Assegna Goleador")
    print("4. Guarda statistiche + Commento AI")
    print("0. Esci")

def esegui_scelta(scelta):
    # ... (scelte 1, 2, 3 rimangono uguali) ...
    
    if scelta == "4":
        s = services.calcola_statistiche()
        if not s:
            print("Non ci sono ancora dati da mostrare.")
        else:
            print("\n--- 📊 RISULTATI ---")
            for corso, tot in s["per_corso"].items():
                print(f"🔹 {corso}: {tot} Goleador")
            print(f"\n🥇 Miglior Risultato: {s['top_scorer']['nome']} ({s['top_scorer']['totale']} caramelle)")
            
            # Parte Nuova: Integrazione Gemini
            print("\n🤖 Suggerimento di Gemini AI:")
            commento = services.genera_commento_motivazionale()
            print(commento)

    elif scelta == "0":
        print("Chiusura programma. A presto!")
        return False
    # ...