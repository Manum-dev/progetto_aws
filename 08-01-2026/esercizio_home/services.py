import urllib.request
import urllib.error
import time
import datetime

def ottieni_dati_sito(url):
    """
    Tenta la connessione e restituisce un dizionario con i dati.
    Non stampa nulla, raccoglie solo i dati.
    """
    if not url.startswith("http"):
        url = "https://" + url

    start_time = time.time()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    dati = {
        "url": url,
        "timestamp": timestamp,
        "status": "UNKNOWN",
        "code": 0,
        "latency_seconds": 0.0,
        "error": None
    }

    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=5) as response:
            end_time = time.time()
            dati["latency_seconds"] = round(end_time - start_time, 3)
            dati["code"] = response.getcode()
            
            if dati["code"] == 200:
                dati["status"] = "ONLINE"
            else:
                dati["status"] = "WARNING"

    except urllib.error.HTTPError as e:
        dati["status"] = "ERROR"
        dati["code"] = e.code
        dati["error"] = e.reason
    except urllib.error.URLError as e:
        dati["status"] = "OFFLINE"
        dati["error"] = str(e.reason)
    except Exception as e:
        dati["status"] = "CRASH"
        dati["error"] = str(e)

    return dati
