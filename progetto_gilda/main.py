import os
from dotenv import load_dotenv
from generator import generate_character
from storage import salva_personaggio, carica_personaggi


def main():
    # Load environment variables
    load_dotenv()
    
    while True:
        print("⚔️  Generatore di Personaggi D&D ⚔️")
        print("\n1. Genera Nuovo Personaggio")
        print("2. Vedi Personaggi Salvati")
        print("3. Esci")
        scelta = input("\nScegli un'opzione: ")

        if scelta == "1":

            prompt = input("Descrivi il personaggio che vuoi creare (o scrivi 'esci' per chiudere): ").strip()
            if not prompt:
                continue

            print("🎲 Evocazione in corso...")
            character = generate_character(prompt)
        
            if character:
                print("\n✅ Personaggio Generato!")
                print(f"Nome: {character.get('name')}")
                print(f"Razza: {character.get('race')}")
                print(f"Classe: {character.get('class')}")
                print(f"Storia: {character.get('backstory')}")
                
                stats = character.get('stats', {})
                print("\n📊 Statistiche:")
            
            # Scorriamo ogni statistica (es: 'strength': 15)
                for nome_stat, valore in stats.items():
                # Calcoliamo le tacche piene: valore diviso 2 (es. 15 -> 7 tacche)
                    n_piene = int(valore) // 2
                # Calcoliamo le tacche vuote: massimo 9 (perché 18/2 = 9) meno quelle piene
                    n_vuote = 9 - n_piene
                
                # Creiamo la stringa visiva
                    barra = "█" * n_piene + "░" * n_vuote
                
                # Stampiamo allineato: <Nome Stat> <Valore> <Barra>
                    print(f"  {nome_stat.capitalize():<12} : {valore:>2} {barra}")

                # Save to storage
                success, error, total = salva_personaggio(character)
                if success:
                    print(f"💾 Salvato nel database! (Totale personaggi: {total})")
                else:
                    print(f"❌ Errore nel salvataggio: {error}")
            else:
                print("❌ Impossibile generare il personaggio. Riprova.")

        elif scelta == '2':
            lista_eroi = carica_personaggi()  # 1. CATTURO i dati
    
            if not lista_eroi:
                print("📭 Nessun eroe trovato.")
            else:
                # 2. SCORRO la lista e stampo
                print(f"\n📚 Trovati {len(lista_eroi)} personaggi:")
                for eroe in lista_eroi:
                    print(f"- {eroe['name']} ({eroe['class']} {eroe['race']})")

        elif scelta == '3':
            if prompt.lower() in ['esci', 'exit', 'quit', 'q']:
                print("👋 Alla prossima avventura!")
                break

if __name__ == "__main__":
    main()