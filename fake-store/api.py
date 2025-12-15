from requests import get, post, Response, RequestException
import json


BASE_URL: str = "https://api.escuelajs.co/api/v1/products"
CATEGORIES_URL: str = "https://api.escuelajs.co/api/v1/categories"

# ===============================
#   Repository
# ===============================

def get_lista_prodotti(URL: str) -> list[dict[str, any]]:
    if not URL: 
        raise ValueError("L'URL non può essere vuoto!")

    response: Response = get_data(URL) 
    data = response.json()

    if not isinstance(data, list):
        raise TypeError(
            f"Risposta inattesa: mi aspettavo un lista, "
            f"ma ho ricevuto {type(data).__name__}"
    )

    return data

def create_product(URL: str, data: dict) -> dict[str, any]:
    if not URL or not data: 
        raise ValueError("L'URL e i dati non possono essere vuoti!")
    if not isinstance(data, dict):
        raise TypeError(f"Risposta inattesa: mi aspettavo un dict, ma ho ricevuto {type(data).__name__}")
    response = post_data(URL, data)
    return response.json()

def post_data(URL: str, data: dict) -> Response:
    if not URL: 
        raise ValueError("L'URL non può essere vuoto!")
    response: Response = post(URL, headers={"Content-Type": "application/json"}, json=data)
    response.raise_for_status()
    return response
def get_data(URL: str) -> Response:
    if not URL: 
        raise ValueError("L'URL non può essere vuoto!")
    
    response : Response = get(URL)
    response.raise_for_status()
    return response


def get_prodotto(URL: str) -> dict[str, any]:
    if not URL: 
        raise ValueError("L'URL non può essere vuoto!")

    response: Response = get_data(URL) 
    data = response.json()

    if not isinstance(data, dict):
        raise TypeError(
            f"Risposta inattesa: mi aspettavo un dict, "
            f"ma ho ricevuto {type(data).__name__}"
    )

    return data

def create_category(URL: str, data: dict) -> dict[str, any]:

    if not URL or not data: 
        raise ValueError("L'URL non può essere vuoto!")

    if not isinstance(data, dict):
        raise TypeError(
            f"Risposta inattesa: mi aspettavo un dict, "
            f"ma ho ricevuto {type(data).__name__}"
    	)

    response = post_data(URL, data)
    return response.json()

# ===============================
#   Model
# ===============================

def product_model(product: dict[str, any]) -> dict[str, any]:
    return {
        "id": product["id"], 
        "title": product["title"], 
        "price": product["price"], 
        "category": product["category"]["name"],
        "description": product["description"]
    }
def product_list_model(product_list: list[dict[str, any]]) -> list[dict[str, str]]:
    """Restituisce una lista di prodotti definita in {id: valore, title: nome prodotto}"""
    return [{"id": str(product["id"]), "title": str(product["title"])} for product in product_list]

def invia_prodotto(dati_prodotto: dict) -> dict:
    """
    Invia un nuovo prodotto al server
    
    Args:
        dati_prodotto: Dizionario con i dati del prodotto
        
    Returns:
        Dizionario con la risposta del server
    """
    print("\n📤 Invio prodotto in corso...")
    print(f"Dati: {json.dumps(dati_prodotto, indent=2, ensure_ascii=False)}")
    
    try:
        risultato = create_product(BASE_URL, dati_prodotto)
        print("✅ Prodotto creato con successo!")
        invia_prodotto(risultato)
        return risultato
        
    except Exception as e:
        print(f"❌ Errore HTTP: {e}")
        print(f"Status Code: {e.response.status_code}")
        if e.response.text:
            print(f"Dettagli: {e.response.text}")
        raise
        
    except ValueError as e:
        print(f"❌ Errore di validazione: {e}")
        raise
        
    except Exception as e:
        print(f"❌ Errore imprevisto: {e}")
        raise


def invia_categoria(dati_categoria: dict) -> dict:
    """
    Invia una nuova categoria al server
    
    Args:
        dati_categoria: Dizionario con i dati della categoria
        
    Returns:
        Dizionario con la risposta del server
    """
    print("\n📤 Invio categoria in corso...")
    print(f"Dati: {json.dumps(dati_categoria, indent=2, ensure_ascii=False)}")
    
    try:
        risultato = create_category(CATEGORIES_URL, dati_categoria)
        print("✅ Categoria creata con successo!")
        mostra_categoria(risultato)
        return risultato
        
    except exceptions.HTTPError as e:
        print(f"❌ Errore HTTP: {e}")
        print(f"Status Code: {e.response.status_code}")
        if e.response.text:
            print(f"Dettagli: {e.response.text}")
        raise
        
    except ValueError as e:
        print(f"❌ Errore di validazione: {e}")
        raise
        
    except Exception as e:
        print(f"❌ Errore imprevisto: {e}")
        raise


def visualizza_prodotti_esistenti(limite: int = 10) -> None:
    """Visualizza i primi N prodotti esistenti"""
    print(f"\n📋 Caricamento primi {limite} prodotti esistenti...")
    
    try:
        url_con_limite = f"{BASE_URL}?offset=0&limit={limite}"
        prodotti = get_lista_prodotti(url_con_limite)
        
        print(f"✅ Trovati {len(prodotti)} prodotti:")
        
        # Usa il model per formattare la lista
        lista_formattata = product_list_model(prodotti)
        
        for item in lista_formattata:
            print(f"  • ID {item['id']}: {item['title']}")
            
    except Exception as e:
        print(f"❌ Errore nel recupero dei prodotti: {e}")


def visualizza_prodotto_specifico(product_id: int) -> None:
    """Visualizza i dettagli di un prodotto specifico"""
    print(f"\n🔍 Caricamento dettagli prodotto ID: {product_id}...")
    
    try:
        url_prodotto = f"{BASE_URL}/{product_id}"
        prodotto = get_prodotto(url_prodotto)
        
        # Usa il model per formattare il prodotto
        prodotto_formattato = product_model(prodotto)
        
        print("\n✅ Dettagli prodotto:")
        print(f"  ID:          {prodotto_formattato['id']}")
        print(f"  Titolo:      {prodotto_formattato['title']}")
        print(f"  Prezzo:      €{prodotto_formattato['price']}")
        print(f"  Categoria:   {prodotto_formattato['category']}")
        print(f"  Descrizione: {prodotto_formattato['description']}")
        
    except Exception as e:
        print(f"❌ Errore nel recupero del prodotto: {e}")
