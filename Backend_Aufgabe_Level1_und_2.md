# 🧑‍💻 Mini‑Projekt: Dein erster Spielstand‑Speicher

Ziel: Du baust eine kleine Python‑Anwendung, die Spielstände speichern,
laden und verändern kann.\
Später nutzt das große Advents‑Spiel dieselbe Logik im Backend!

------------------------------------------------------------------------

## 🧩 Level 1 -- Spielstand speichern und laden

### 🧠 Was du lernst

-   Wie man Dateien mit Python liest und schreibt\
-   Was JSON ist (eine Textform, um Daten zu speichern)\
-   Wie man Listen (`list`) und Wörterbücher (`dict`) benutzt

### 🪄 Schritt 1 -- Projekt vorbereiten

Lege auf deinem Computer einen neuen Ordner an, z. B.\
`C:\Users\<DEINNAME>\Desktop\spielstand`

Erstelle darin eine Datei **spielstand.py** und kopiere den folgenden
Code hinein:

``` python
import json
from pathlib import Path

Path("states").mkdir(exist_ok=True)

def read_state(username):
    path = Path("states") / f"{username}.json"
    if not path.exists():
        print(f"Kein Spielstand für {username} gefunden – neuer wird erstellt.")
        return {"progress": 0, "inventory": []}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def write_state(username, data):
    path = Path("states") / f"{username}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Spielstand für {username} gespeichert.")

if __name__ == "__main__":
    user = "tim"
    state = {"progress": 3, "inventory": ["stern_1", "karte"]}
    write_state(user, state)
    loaded = read_state(user)
    print("Geladener Spielstand:", loaded)
```

Starte dein Script in der Konsole:

``` bash
python spielstand.py
```

Im Ordner `states` findest du danach eine Datei `tim.json` mit folgendem
Inhalt:

``` json
{
  "progress": 3,
  "inventory": ["stern_1", "karte"]
}
```

------------------------------------------------------------------------

## 🧠 Level 2 -- Spielstand verändern

Jetzt soll dein Programm auch den Fortschritt erhöhen und Items
hinzufügen oder entfernen.

``` python
def update_progress(state, new_door):
    if new_door == state["progress"] + 1:
        state["progress"] = new_door
        print(f"Fortschritt erhöht: Du hast jetzt Tür {new_door} erreicht.")
    else:
        print("Diese Tür darfst du noch nicht öffnen!")
    return state

def add_item(state, item):
    if item not in state["inventory"]:
        state["inventory"].append(item)
        print(f"Item '{item}' hinzugefügt.")
    else:
        print(f"Item '{item}' hast du schon.")
    return state

def remove_item(state, item):
    if item in state["inventory"]:
        state["inventory"].remove(item)
        print(f"Item '{item}' entfernt.")
    else:
        print(f"Item '{item}' war gar nicht im Inventar.")
    return state
```

Teste die neuen Funktionen:

``` python
if __name__ == "__main__":
    user = "tim"
    state = read_state(user)
    print("Aktueller Spielstand:", state)
    state = update_progress(state, 4)
    state = add_item(state, "kompass")
    state = remove_item(state, "stern_1")
    write_state(user, state)
    print("Neuer Spielstand:", read_state(user))
```

------------------------------------------------------------------------

## 🏁 Erweiterungen (freiwillig)

-   Frage den Namen mit `input()` ab.\
-   Füge eine **reset_state()**-Funktion hinzu, die den Spielstand
    löscht.\
-   Baue ein kleines Textmenü mit Zahlen (1 = Fortschritt, 2 = Item,
    ...).

------------------------------------------------------------------------

## 🧠 Was du gelernt hast

  -----------------------------------------------------------------------
  Thema                    Beschreibung
  ------------------------ ----------------------------------------------
  **Dateisystem**          Mit `pathlib` und `open()` Dateien anlegen und
                           lesen

  **JSON**                 Daten im Textformat speichern, laden und
                           verstehen

  **Datenstrukturen**      Listen und Dictionaries sinnvoll einsetzen

  **Logik**                Bedingungen (`if`) und Funktionen kombinieren

  **Fehlervermeidung**     Nur erlaubte Fortschritte, keine doppelten
                           Items
  -----------------------------------------------------------------------
