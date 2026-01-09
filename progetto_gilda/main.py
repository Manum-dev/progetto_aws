import os
from dotenv import load_dotenv
from generator import generate_character
from storage import salva_personaggio
def main():
    
    # Load environment variables
    load_dotenv()
    
    print("⚔️  Generatore di Personaggi D&D ⚔️")
    
    while True:
        print("\n" + "="*40)
        print("\n1. Genera Nuovo Personaggio")
        print("2. Vedi Personaggi Salvati")
        print("3. Esci")
        scelta = input("\nScegli un'opzione: ")
        if scelta == "1":
            prompt = input("Descrivi il personaggio che vuoi creare (o scrivi 'esci' per chiudere): ").strip()
        
        if prompt.lower() in ['esci', 'exit', 'quit', 'q']:
            print("👋 Alla prossima avventura!")
            break
            
        if not prompt:
            continue
            
        print("🎲 Evocazione in corso...")
        character = generate_character(prompt)
        
        if character:
            print("\n✅ Personaggio Generato!")
            print(f"Nome: {character.get('name')}")
            print(f"Razza: {character.get('race')}")
            print(f"Classe: {character.get('class')}")
            print(f"Storia: {character.get('backstory')[:100]}...")
            
            # Save to storage
            success, error, total = salva_personaggio(character)
            if success:
                print(f"💾 Salvato nel database! (Totale personaggi: {total})")
            else:
                print(f"❌ Errore nel salvataggio: {error}")
        else:
            print("❌ Impossibile generare il personaggio. Riprova.")
if __name__ == "__main__":
    main()