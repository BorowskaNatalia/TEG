from dotenv import load_dotenv
import os

# Wczytanie zmiennych środowiskowych z pliku .env
load_dotenv("config/.env")

# Sprawdzenie, czy klucz API został załadowany
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print(f"Twój klucz API OpenAI to: {openai_api_key}")
else:
    print("Nie znaleziono klucza API. Upewnij się, że plik .env jest poprawnie skonfigurowany.")
