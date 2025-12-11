from requests import get, exceptions

BASE_URL: str = "https://api.escuelajs.co/api/v1/products"


def get_data(URL: str) -> dict[str, any] | list[dict[str, any]]:
    """Effettua una richiesta HTTP GET all'URL specificato"""
    if URL is None or URL.strip() == "": 
        raise ValueError("L'URL non può essere vuoto!")
    
    try:
        response = get(URL, timeout=10)
        response.raise_for_status()
        return response.json()

    except exceptions.Timeout as e:
        raise ConnectionError(f"Timeout: il server non risponde. Riprova più tardi. ({e})")
    
    except exceptions.ConnectionError as e:
        raise ConnectionError(f"Errore di connessione: verifica la tua connessione internet. ({e})")
    
    except exceptions.HTTPError as e:
        if response.status_code == 400:
            raise ValueError(f"Richiesta non valida. Verifica l'ID inserito. ({e})")
        elif response.status_code == 404:
            raise ValueError(f"Prodotto non trovato. Verifica l'ID inserito. ({e})")
        elif response.status_code == 500:
            raise ConnectionError(f"Errore del server. Riprova più tardi. ({e})")
        else:
            raise ConnectionError(f"Errore HTTP {response.status_code}: {e}")
    
    except exceptions.RequestException as e:
        raise ConnectionError(f"Errore nella richiesta: {e}")


def get_all_products() -> list[dict[str, any]]:
    """Recupera la lista completa di tutti i prodotti"""
    return get_data(BASE_URL)


def get_product_by_id(product_id: int) -> dict[str, any]:
    """Recupera un prodotto specifico tramite ID"""
    return get_data(f"{BASE_URL}/{product_id}")
