from api import get_lista_prodotti, get_prodotto, CATEGORIES_URL, json

def mostra_categorie() -> None:
    """Mostra le categorie disponibili"""
    try:
        categorie = get_lista_prodotti(CATEGORIES_URL)
        print("\n📁 CATEGORIE DISPONIBILI:")
        print("-" * 40)
        for cat in categorie[:10]:  # Mostra prime 10
            print(f"  {cat['id']}: {cat['name']}")
        print("-" * 40)
    except Exception as e:
        print(f"⚠️  Impossibile caricare le categorie: {e}")
        print("Usa uno di questi ID comuni: 1 (Clothes), 2 (Electronics), 3 (Furniture)")


def richiedi_input(prompt: str, tipo: type = str, default: any = None, obbligatorio: bool = True):
    """Funzione helper per richiedere input con validazione"""
    while True:
        try:
            valore_str = input(prompt).strip()
            
            # Se vuoto e c'è un default
            if not valore_str and default is not None:
                return default
            
            # Se vuoto e non è obbligatorio
            if not valore_str and not obbligatorio:
                return None
            
            # Se vuoto e obbligatorio
            if not valore_str and obbligatorio:
                print("⚠️  Questo campo è obbligatorio!")
                continue
            
            # Converti al tipo richiesto
            if tipo == int:
                return int(valore_str)
            elif tipo == float:
                return float(valore_str)
            elif tipo == bool:
                return valore_str.lower() in ['si', 'sì', 's', 'yes', 'y', 'true', '1']
            else:
                return valore_str
                
        except ValueError:
            print(f"⚠️  Valore non valido! Inserisci un {tipo.__name__}")


def richiedi_immagini() -> list[str]:
    """Richiede gli URL delle immagini"""
    immagini = []
    print("\n📷 IMMAGINI (premi INVIO senza inserire nulla per terminare)")
    
    while True:
        url = input(f"  URL immagine {len(immagini) + 1}: ").strip()
        if not url:
            break
        immagini.append(url)
    
    # Se non ha inserito immagini, usa una di default
    if not immagini:
        immagini = ["https://i.imgur.com/ZANVnHE.jpeg"]
        print("  ℹ️  Nessuna immagine inserita, uso immagine di default")
    
    return immagini


def crea_prodotto_interattivo() -> dict:
    """Crea un prodotto richiedendo i dati all'utente"""
    
    print("\n" + "="*50)
    print("  INSERIMENTO NUOVO PRODOTTO")
    print("="*50)
    
    # Mostra categorie disponibili
    mostra_categorie()
    
    # Richiedi dati
    print("\nℹ️  Inserisci i dati del prodotto:\n")
    
    titolo = richiedi_input("📝 Titolo: ", str)
    prezzo = richiedi_input("💰 Prezzo (€): ", float)
    descrizione = richiedi_input("📄 Descrizione: ", str)
    categoria_id = richiedi_input("📁 ID Categoria: ", int)
    immagini = richiedi_immagini()

# Crea il dizionario prodotto
    prodotto = {
        "title": titolo,
        "price": prezzo,
        "description": descrizione,
        "categoryId": categoria_id,
        "images": immagini
    }
    
    return prodotto


def conferma_invio(prodotto: dict) -> bool:
    """Mostra un riepilogo e chiede conferma"""
    print("\n" + "="*50)
    print("  RIEPILOGO PRODOTTO")
    print("="*50)
    print(json.dumps(prodotto, indent=2, ensure_ascii=False))
    print("="*50)
    
    risposta = input("\n✅ Confermi l'invio? (s/n): ").str().lower()
    return risposta in ['s', 'si', 'sì', 'y', 'yes']