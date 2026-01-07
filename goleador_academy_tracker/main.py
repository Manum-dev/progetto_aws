import ui
import os

def pulisci_schermo():
    # Pulisce la console per rendere tutto più leggibile (opzionale)
    os.system('cls' if os.name == 'nt' else 'clear')

def avvia_app():
    pulisci_schermo()
    print("="*40)
    print("   🌟 BENVENUTI ALLA GOLEADOR ACADEMY 🌟   ")
    print("="*40)
    
    ciclo_attivo = True
    while ciclo_attivo:
        ui.mostra_menu()
        scelta = input("\nCosa vuoi fare? Scegli le seguenti opzioni da 1 a 5!")
        ciclo_attivo = ui.esegui_scelta(scelta)

    print("\nSalvataggio dati... Chiusura programma. Ciao!")

if __name__ == "__main__":
    avvia_app()