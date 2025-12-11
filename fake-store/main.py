from api import get_all_products, get_product_by_id
from ui import print_prodotto, print_products_list, show_menu, get_product_id_input


def product_model(product: dict[str, any]) -> dict[str, any]:
    """Trasforma i dati del prodotto nel formato desiderato"""
    try:
        return {
            "id": product["id"], 
            "title": product["title"], 
            "price": product["price"], 
            "category": product["category"]["name"],
            "description": product["description"]
        }
    except KeyError as e:
        raise KeyError(f"Dati del prodotto incompleti: campo mancante {e}")
    except TypeError as e:
        raise TypeError(f"Formato dei dati del prodotto non valido. ({e})")


def main() -> None:
    try: 
        scelta = show_menu()
        
        if scelta == "1":
            # Visualizza tutti i prodotti
            products = get_all_products()
            print_products_list(products)
            
            # Chiede quale prodotto visualizzare
            try:
                product_id = get_product_id_input()
                product_data = get_product_by_id(product_id)
                product = product_model(product_data)
                print_prodotto(product)
            except ValueError as e:
                print(f"Errore di input: {e}")
                return
            
        elif scelta == "2":
            # Cerca prodotto specifico direttamente
            try:
                product_id = get_product_id_input()
                product_data = get_product_by_id(product_id)
                product = product_model(product_data)
                print_prodotto(product)
            except ValueError as e:
                print(f"Errore di input: {e}")
                return
        else:
            print("Opzione non valida. Scegli 1 o 2.")
    
    except ConnectionError as e:
        print(f"Errore di connessione: {e}")
    
    except ValueError as e:
        print(f"Errore: {e}")
    
    except KeyError as e:
        print(f"Errore nei dati: {e}")
    
    except TypeError as e:
        print(f"Errore di tipo: {e}")
    
    except KeyboardInterrupt:
        print("\nOperazione interrotta dall'utente.")
    
    except Exception as e:
        print(f"Errore imprevisto: {type(e).__name__} - {e}")


if __name__ == "__main__":
    main()