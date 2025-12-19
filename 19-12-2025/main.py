from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# 1. Crea un'istanza della configurazione (nota le parentesi)
# Oppure usa semplicemente un dizionario: config={'temperature': 0.7}
config = genai.types.GenerateContentConfig(
    temperature=0.7,
    max_output_tokens=30
)

client = genai.Client(api_key=gemini_api_key)

# 2. Assicurati che il modello sia corretto (es. "gemini-2.0-flash-exp")
response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents="Explain how AI works in a few words",
    config=config
)

print(response.text)