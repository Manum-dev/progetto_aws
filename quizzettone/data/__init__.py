# Define the __all__ variable
__all__ = [
    "repository", 
    "services",
    "get_lista_domande_e_risposte",
    "valida_scelta",
    "is_risposta_esatta",
    "get_numero_domanda_corrente",
    "get_counter_aggiornato",
    "genera_statistiche",
    "calcola_percentuale",
    "verifica_superamento",
    "recupera_dati_domanda",
    "aggiorna_lista_risultati"
]

# Import the submodules
from . import repository
from . import services

# Import and re-export the functions from services
from .services import (
    get_lista_domande_e_risposte,
    valida_scelta,
    is_risposta_esatta,
    get_numero_domanda_corrente,
    get_counter_aggiornato,
    genera_statistiche,
    calcola_percentuale,
    verifica_superamento,
    recupera_dati_domanda,
    aggiorna_lista_risultati
)