from api import create_product, BASE_URL, get_lista_prodotti
from requests import exceptions

def print_prodotto(product: dict[str, any]) -> None:
    """Stampa i dettagli completi di un prodotto""""
    print("*" * 30)
    print(f"PRODOTTO")
    print("*" * 30)
    print(f"ID: {product['id']}")
    print(f"Titolo: {product['title']}")
    print(f"Category: {product['category']}")
    print(f"PRICE: {product['price']}")
    print(f"DESCRIPTION: {product['description']}")


def print_product_list(product_list: list[dict]) -> None:
    """Stampa la lista di prodotti mostrando solo ID e titolo"""
    print("=" * 50)
    print("LISTA PRODOTTI")
    print("=" * 50)
    for product in product_list:
        print(f"ID: {product['id']} - {product['title']} {product['description']}")
    print("=" * 50)
    print(f"Totale prodotti: {len(product)}")

def invia_prodotto_al_server(prodotto: dict) -> None:
    """Invia il prodotto al server"""
    try:
        print("\n⏳ Invio in corso...")
        risultato = create_product(BASE_URL, prodotto)
        
        print("\n" + "🎉"*25)
        print("  PRODOTTO CREATO CON SUCCESSO!")
        print("🎉"*25)
        
        print("\n📦 DETTAGLI:")
        print(f"  ID:          {risultato.get('id')}")
        print(f"  Titolo:      {risultato.get('title')}")
        print(f"  Prezzo:      €{risultato.get('price')}")
        print(f"  Descrizione: {risultato.get('description')}")
        
        if 'category' in risultato:
            cat = risultato['category']
            if isinstance(cat, dict):
                print(f"  Categoria:   {cat.get('name', 'N/A')}")
        
        print("\n✅ Operazione completata!")
        
    except exceptions.HTTPError as e:
        print(f"\n❌ ERRORE HTTP: {e}")
        print(f"   Status Code: {e.response.status_code}")
        if e.response.text:
            print(f"   Dettagli: {e.response.text}")
            
    except Exception as e:
        print(f"\n❌ ERRORE: {e}")
