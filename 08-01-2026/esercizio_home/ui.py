# Colori
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def stampa_risultato(dati):
    """Visualizza i dati colorati nel terminale"""
    url = dati['url']
    code = dati['code']
    time_s = dati['latency_seconds']
    status = dati['status']

    if status == "ONLINE":
        print(f"{GREEN}[OK]      {code}{RESET} | {time_s}s | {url}")
    elif status == "WARNING":
        print(f"{YELLOW}[STATUS]  {code}{RESET} | {time_s}s | {url}")
    elif status == "OFFLINE" or status == "ERROR":
        err_msg = dati.get('error', '')
        print(f"{RED}[{status:<7}] ---{RESET} | ------ | {url} ({err_msg})")
