import google.generativeai as genai
import json
import os
import re
from typing import Dict, Any, Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure API Key
API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY:
    # Clean the key from extra quotes or spaces
    API_KEY = API_KEY.strip().strip('"').strip("'")
    genai.configure(api_key=API_KEY)

# System instruction to force JSON output and set the context
SYSTEM_INSTRUCTION = """
You are a D&D character creator. Your task is to generate complete and balanced D&D characters based on a user's description.
You MUST respond EXCLUSIVELY with a valid JSON object. No conversational text, no markdown code blocks (unless specified), just the JSON.

Rules for Stats:
- Assign values between 3 and 18.
- Ensure stats are coherent with the chosen class and race (e.g., a Wizard should have Intelligence as their highest stat).
- Use a distribution similar to the "Standard Array" (15, 14, 13, 12, 10, 8) or "Point Buy" for balance.

The character must have:
- name: A fitting name.
- race: A D&D race (Elfo, Nano, Umano, etc.).
- class: A D&D class (Guerriero, Mago, Ladro, etc.).
- level: Always 1.
- stats: strength, dexterity, constitution, intelligence, wisdom, charisma.
- backstory: A detailed backstory in Italian, matching the user's prompt.
- physical_description: A detailed physical description in Italian.

JSON Schema:
{
  "name": "string",
  "race": "string",
  "class": "string",
  "level": 1,
  "stats": {
    "strength": int,
    "dexterity": int,
    "constitution": int,
    "intelligence": int,
    "wisdom": int,
    "charisma": int
  },
  "backstory": "string",
  "physical_description": "string"
}

Language: Italian.
"""

def generate_character(user_prompt: str) -> Optional[Dict[str, Any]]:
    """Generates a character from a user prompt using Gemini."""
    if not API_KEY:
        print("❌ Errore: GOOGLE_API_KEY non trovata nell'ambiente.")
        return None

    try:
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction=SYSTEM_INSTRUCTION
        )
        
        # We can also use 'response_mime_type': 'application/json' if supported by the model/SDK version
        response = model.generate_content(
            f"Genera un personaggio D&D basato su questa descrizione: {user_prompt}",
            generation_config={"response_mime_type": "application/json"}
        )

        # Parse the JSON response
        try:
            character_data = json.loads(response.text)
            return character_data
        except json.JSONDecodeError:
            # Fallback: try to find JSON block in case it ignored the system instruction
            match = re.search(r"\{.*\}", response.text, re.DOTALL)
            if match:
                return json.loads(match.group())
            print("❌ Errore: Gemini non ha restituito un JSON valido.")
            print(f"Debug output: {response.text}")
            return None

    except Exception as e:
        print(f"❌ Errore durante la chiamata a Gemini: {e}")
        return None

def regenerate_backstory(character_info: Dict[str, Any]) -> Optional[str]:
    """Regenerates only the backstory for an existing character."""
    if not API_KEY:
        return None

    try:
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction="You are a professional D&D DM. Return EXCLUSIVELY the new backstory text in Italian, no conversational filler, no JSON tags."
        )
        
        prompt = (
            f"Rigenera una nuova backstory per questo personaggio: "
            f"Nome: {character_info['name']}, Razza: {character_info['race']}, Classe: {character_info['class']}. "
            f"Prompt originale dell'utente: {character_info.get('user_prompt', 'N/A')}"
        )
        
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        print(f"❌ Errore durante la rigenerazione della backstory: {e}")
        return None