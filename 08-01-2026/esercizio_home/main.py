import sys
import argparse
import json
import os
import services
import ui

def main():
    parser = argparse.ArgumentParser(description="SiteCheck con Export JSON")
    parser.add_argument("urls", nargs="*", help="Lista URL")
    parser.add_argument("-f", "--file", type=str, help="File input")
    parser.add_argument("--output", type=str, default="report_network.json", help="Nome file JSON output")
    
    args = parser.parse_args()
    
    # Lista che conterrà i NUOVI risultati di questa esecuzione
    new_report_data = []

    print(f"📡  Monitor Network attivo\n{'='*60}")
    
    # Funzione helper per processare un singolo URL
    def processa_url(url_target):
        if not url_target: return
        risultato = services.ottieni_dati_sito(url_target)
        ui.stampa_risultato(risultato)
        new_report_data.append(risultato)

    # 1. Input da argomenti
    for url in args.urls:
        processa_url(url)

    # 2. Input da file
    if args.file:
        try:
            with open(args.file, "r") as f:
                for line in f:
                    processa_url(line.strip())
        except FileNotFoundError:
            print("File non trovato.")

    # 3. Input interattivo (se non ci sono argomenti)
    if not args.urls and not args.file:
        print("Nessun input rilevato. Modalità interattiva.")
        while True:
            try:
                sito = input("\n👉 Sito da controllare (q=esci, s=salva): ").strip()
                if sito.lower() in ['q', 'quit', 'exit', 's']:
                    break
                processa_url(sito)
            except KeyboardInterrupt:
                break
    
    # SALVATAGGIO JSON FINALE (PERSISTENTE)
    if new_report_data:
        try:
            # Carica dati esistenti se il file c'è
            existing_data = []
            if os.path.exists(args.output):
                try:
                    with open(args.output, "r", encoding="utf-8") as f:
                        content = f.read()
                        if content.strip():
                            existing_data = json.loads(content)
                            if not isinstance(existing_data, list):
                                # Se per qualche motivo non è una lista, creane una nuova o gestisci l'errore
                                # Qui scelgo di sovrascrivere se il formato è corrotto/diverso
                                existing_data = []
                except json.JSONDecodeError:
                    # File corrotto o vuoto
                    existing_data = []

            # Unisci i dati
            final_data = existing_data + new_report_data

            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(final_data, f, indent=4)
            
            print(f"\n💾 Report aggiornato in: {ui.GREEN}{args.output}{ui.RESET} (Nuovi: {len(new_report_data)}, Totale: {len(final_data)})")
        except Exception as e:
            print(f"\n❌ Errore salvataggio JSON: {e}")
    else:
        print("\nNessun nuovo dato da salvare.")

if __name__ == "__main__":
    main()
