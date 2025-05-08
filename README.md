# TEG - Twój Pierwszy Projekt z Pythonem 🚀

## 📋 Wprowadzenie

Projekt **TEG** to Twój pierwszy krok w nauce programowania w Pythonie. Będziemy tutaj powoli i dokładnie przechodzić przez każdy etap tworzenia aplikacji w Pythonie, ucząc się używać środowisk wirtualnych, zmiennych środowiskowych i narzędzi takich jak Git i GitHub.

---

## 📂 Struktura projektu

```
TEG/
├── venv/                # Środowisko wirtualne
├── config/
│   └── .env            # Plik z kluczem API OpenAI
├── main.py             # Główny plik programu
├── requirements.txt    # Lista zależności Pythona
└── .gitignore          # Plik ignorujący niektóre pliki w Git
```

---

## 🔨 Krok 1: Utworzenie środowiska wirtualnego

1. Sprawdź, czy masz zainstalowanego Pythona (wersja 3.11+).
2. Utwórz środowisko wirtualne:

```bash
python -m venv venv
```

3. Aktywuj środowisko wirtualne:

   * **Windows:**

   ```bash
   .\venv\Scripts\activate
   ```

   * **Mac/Linux:**

   ```bash
   source venv/bin/activate
   ```

4. Upewnij się, że środowisko jest aktywne (powinno być `(venv)` w terminalu).

---

## 📦 Krok 2: Instalacja pierwszej biblioteki

1. Utwórz plik `requirements.txt`:

```
python-dotenv
```

2. Zainstaluj bibliotekę:

```bash
pip install -r requirements.txt
```

---

## 🗝️ Krok 3: Utworzenie pliku `.env`

1. Utwórz katalog `config`:

```bash
mkdir config
```

2. Utwórz plik `.env` w katalogu `config/`:

```
OPENAI_API_KEY=sk-****************************
```

3. Upewnij się, że zastąpiłeś `sk-****************************` swoim prawdziwym kluczem API.

---

## 🧠 Krok 4: Tworzenie pliku `main.py`

1. Utwórz plik `main.py` w katalogu głównym projektu:

```python
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
```

2. Uruchom program:

```bash
python main.py
```

Powinieneś zobaczyć swój klucz API na ekranie, jeśli wszystko działa poprawnie.

---

## 📂 Krok 5: Utworzenie `.gitignore`

1. Utwórz plik `.gitignore` w katalogu głównym projektu:

```
venv/
__pycache__/
config/.env
```

2. Dodaj wszystkie pliki do Git:

```bash
git add .
```

3. Utwórz pierwszy commit:

```bash
git commit -m "Initial project setup - venv, dotenv, main.py"
```

---

## 🌐 Krok 6: Wysłanie na GitHub

1. Utwórz nowe repozytorium na GitHub.
2. Połącz lokalne repozytorium z GitHub:

```bash
git remote add origin https://github.com/twoj-uzytkownik/TEG.git
```

3. Wyślij pliki na GitHub:

```bash
git branch -M main
git push -u origin main
```

---

## ✅ Co dalej?

W kolejnym kroku dodamy pierwsze proste zapytania do OpenAI, aby przetestować naszą konfigurację API.
