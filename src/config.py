import os 

BASE_URL = "https://api.laposte.fr/suivi/v2/idships/"
LANG = "fr_FR"

def get_api_key()->str:
    api_key = os.getenv("LAPOSTE_API_KEY")
    if not api_key:
        raise ValueError("Key not set")

    return api_key

def get_headers()->dict:
    return {
        "X-Okapi-Key" : get_api_key(),
        "Accept" : "application/json"
    }

