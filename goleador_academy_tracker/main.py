import ui
import sys

def avvia_app():
    """
    Punto di ingresso principale dell'applicazione Goleador Academy.
    Gestisce il ciclo infinito del menu fino alla scelta di uscita.
    """
    
    # Messaggio di benvenuto grafico
    print("="*40)
    print("   🌟 GOLEADOR ACADEMY TRACKER 🌟   ")
    print("="*40)
    
    continua = True
    
    while continua:
        try:
            # Mostra le opzioni disponibili
            ui.mostra_menu()
            
            # Recupera l'input dell'utente
            scelta_utente = input("\n👉 Seleziona un'operazione (0-5): ")
            
            # Esegue la logica corrispondente e aggiorna la variabile di controllo
            continua = ui.esegui_scelta(scelta_utente)
            
        except KeyboardInterrupt:
            # Gestisce la chiusura forzata con CTRL+C
            print("\n\n⚠️ Interruzione rilevata. Chiusura in corso...")
            continua = False
        except Exception as e:
            # Gestisce eventuali errori imprevisti per non far crashare l'app
            print(f"\n❌ Si è verificato un errore imprevisto: {e}")
            input("Premi Invio per continuare...")

    print("\n👋 Grazie per aver usato Goleador Academy. A presto!")

if __name__ == "__main__":
    avvia_app()