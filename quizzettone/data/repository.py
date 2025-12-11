from typing import TextIO

def get_file(file_path: str ) -> TextIO:
    """Recupera un oggetto IO di tipo testuale dal un file specifico"""
    return open(file_path, "r")


def send_questions(file_path: str ) -> TextIO:
    return open(file_path, "r")


from requests import get 
from requests.exceptions import  HTTPError, ConnectionError, Timeout, RequestException

def get_data(URL: str) -> str:
    if URL is None: 
        raise ValueError("L'URL non può essere una stringa vuota!")
    
    try:
        response = get(URL) 

        response.raise_for_status()

        return response.text

    except HTTPError as e:
        raise HTTPError(f"Errore HTTP {response.status_code} su {URL}: {response.reason}"
        ) from e

    except ConnectionError:
        raise ConnectionError(f"Impossibile connettersi a {URL}")
    
    except Timeout:
        raise Timeout(f"Timeout nella richiesta a {URL}")
    
    except RequestException as e:
        raise RequestException(f"Errore di rete imprevisto: {e}") from e