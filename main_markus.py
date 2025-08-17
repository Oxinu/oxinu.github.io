import random
from hangman_art import stages, logo
from woerter import woerter

# Der Spieler hat 6 Leben
leben = 6
richtige_buchstaben = []
geratene_buchstaben = []
game_over = False

#drucke das Logo
print(logo)

# Wähle ein zufälliges Wort aus der Liste "woerter" aus
wort = random.choice(woerter).lower()

# hinweis ist der Ausdruck der Anzahl von Buchstaben
hinweis = ""
for zeichen in wort:
    hinweis = hinweis + "_"

print(wort)
#solange noch kein Game Over ist, lass das Spiel laufen
while not game_over:
    #drucke Hinweis an Anzahl Laben
    print(hinweis)
    print(f"*** Du hast {leben} von 6 Leben ***")
    #drucke den Galgen aus
    print(stages[leben])
    #Der Spieler soll eine Buchstaben raten
    buchstabe_geraten = input("Rate einen Buchstaben: ").lower()

    # wenn der geratene Buchstabe bereits geraten wurde ist, schreibe nur einen Hinweis
    if buchstabe_geraten in geratene_buchstaben:
        print("Den Buchstaben hast Du bereits geraten. Versuch' einen anderen Buchstaben")
    #wenn der geratene Buchstabe im Wort enthalten ist, füge den Buchstaben zu den richtigen Buchstaben hinzu
    elif buchstabe_geraten in wort:
        print("Sehr gut! der Buchstabe ist enthalten")
        richtige_buchstaben.append(buchstabe_geraten)
    #wenn der Buchstabe nicht richtig war, ziehe ein Leben ab
    else:
        print("Das ist leider falsch, dafür muss ich dir ein Leben abziehen")
        leben -= 1
        #falls der Spieler beim Abzug des Lebens auf Null fällt, ist Game Over
        if leben == 0:
            print("** DU HAST VERLOREN! **")
            print(f"Das Lösungswort lautete {wort}")
            game_over = True

    #der geratene Buchstabe wird in der Liste der gerateen Buchstaben gespeichert
    geratene_buchstaben.append(buchstabe_geraten)

    #baue neuen Hinweis aus - zunächst ist Hinweis leer
    hinweis = ""
    #Prüfe für jeden Buchstaben im Wort:
    for buchstabe in wort:
        #wenn der geratene Buchstabe gleich dem Buchstaben ist, hänge diesen an den Hinweis
        if buchstabe_geraten == buchstabe:
            hinweis = hinweis + buchstabe
        # oder wenn der geratene Buchstabe gleich einem bereits geratenen Buchstaben ist, hänge diese an
        elif buchstabe in richtige_buchstaben:
            hinweis = hinweis + buchstabe
        # ansonsten hänge einen Unterstrich an Hinweis
        else:
            hinweis = hinweis + "_"
    #falls im Hinweis es keine Unterstriche mehr gibt, ist das Spiel gewonnwn und Game Over
    if '_' not in hinweis:
        print("** DU HAST GEWONNEN! **")
        print(f"Das Lösungswort lautete {wort}")
        game_over = True
