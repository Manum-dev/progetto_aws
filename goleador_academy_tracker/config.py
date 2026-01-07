# Configurazione globale
FILE_DATABASE = "database_corsi.json"
import os
from dotenv import load_dotenv

# Carica le variabili dal file .env
load_dotenv()

# Leggi la chiave API
CHIAVE_API_GEMINI = os.getenv('CHIAVE_API_GEMINI')