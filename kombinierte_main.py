# --- Teil 1: Literale und Bezeichner ---
def literale_und_bezeichner():
    # Aufgabe 1: Literale in Python
    ganze_zahl = 42  # Ganze Zahl (int)
    gleitkommazahl = 3.14  # Gleitkommazahl (float)
    zeichenfolge = "Hallo Welt"  # Zeichenfolge (str)
    wahrheitswert = True  # Boolean (bool)
    liste = [1, 2, 3, 4, 5]  # Liste (list)

    # Ausgabe der Literale
    print("Ganze Zahl:", ganze_zahl)
    print("Gleitkommazahl:", gleitkommazahl)
    print("Zeichenfolge:", zeichenfolge)
    print("Wahrheitswert:", wahrheitswert)
    print("Liste:", liste)

    # Aufgabe 2: Bezeichner und Kommentare
    zahl = 10  # Eine Variable für eine Zahl
    text = "Dies ist ein Text"  # Eine Variable für einen Text
    status = True  # Eine Variable für einen Wahrheitswert
    print(f"zahl: {zahl}, text: {text}, status: {status}")


# --- Teil 2: Namensräume ---
def lokale_und_globale_variablen():
    # Aufgabe 3: Lokale und globale Variablen
    globale_variable = "Ich bin global"  # Globale Variable

    def funktion_mit_lokaler_variabler():
        lokale_variable = "Ich bin lokal"  # Lokale Variable
        print(f"Globale Variable: {globale_variable}")  # Zugriff auf globale Variable
        print(f"Lokale Variable: {lokale_variable}")  # Zugriff auf lokale Variable

    funktion_mit_lokaler_variabler()


def verschachtelte_namensraeume():
    # Aufgabe 4: Verschachtelte Namensräume und nonlocal
    def aussen():
        x = 10  # Variable im äußeren Namensraum

        def innen():
            nonlocal x  # Zugriff auf die äußere Variable
            x += 5  # Änderung der äußeren Variable
            print(f"Äußere Variable x in der inneren Funktion: {x}")

        innen()
        print(f"Äußere Variable x nach der inneren Funktion: {x}")

    aussen()


# --- Teil 3: Built-in Funktionen ---
def built_in_funktionen():
    # Aufgabe 5: Wichtige Built-in Funktionen
    text = "Python"
    print("Länge der Zeichenfolge:", len(text))
    print("Typ der Zeichenfolge:", type(text))

    zahlen = [1, 2, 3, 4, 5]
    print("Summe der Liste:", sum(zahlen))
    print("Maximale Zahl in der Liste:", max(zahlen))
    print("Minimale Zahl in der Liste:", min(zahlen))

    sortierte_liste = sorted(zahlen)
    print("Sortierte Liste:", sortierte_liste)


def eingaben_verarbeiten():
    # Aufgabe 6: Eingaben verarbeiten
    eingabe = input("Gib eine Zahl ein: ")
    
    try:
        zahl = int(eingabe)  # Konvertiere die Eingabe in eine Zahl
        print(f"Die eingegebene Zahl ist: {zahl}")

        if isinstance(zahl, int):
            print("Die Eingabe ist eine gültige ganze Zahl.")
        else:
            print("Die Eingabe ist keine gültige Zahl.")
    except ValueError:
        print("Fehler: Das ist keine gültige Zahl.")


# --- Teil 4: Anweisungsfolgen ---
def lineare_anweisungsfolge():
    # Aufgabe 1: Lineare Anweisungsfolge
    startwert = 10  # Startwert
    zwischenwert = startwert + 5  # Addition von 5
    endwert = zwischenwert * 2  # Multiplikation mit 2

    print("Startwert:", startwert)
    print("Zwischenwert:", zwischenwert)
    print("Endwert:", endwert)


def zahl_gerade_oder_ungerade():
    # Aufgabe 2.1: Zahl gerade oder ungerade
    zahl = int(input("Gib eine Zahl ein: "))
    if zahl % 2 == 0:
        print(f"{zahl} ist gerade.")
    else:
        print(f"{zahl} ist ungerade.")


def zahl_groesser_kleiner_oder_100():
    # Aufgabe 2.2: Zahl größer, kleiner oder gleich 100
    zahl = int(input("Gib eine Zahl ein: "))
    if zahl > 100:
        print(f"{zahl} ist größer als 100.")
    elif zahl < 100:
        print(f"{zahl} ist kleiner als 100.")
    else:
        print(f"{zahl} ist gleich 100.")


def passwort_pruefen():
    # Aufgabe 2.3: Passwort überprüfen
    korrektes_passwort = "passwort123"
    benutzer_passwort = input("Gib dein Passwort ein: ")
    if benutzer_passwort == korrektes_passwort:
        print("Passwort korrekt!")
    else:
        print("Falsches Passwort!")


def zahl_zwischen_50_und_100():
    # Aufgabe 2.4: Zahl zwischen 50 und 100 überprüfen
    zahl = int(input("Gib eine Zahl ein: "))
    if 50 <= zahl <= 100:
        print(f"{zahl} liegt zwischen 50 und 100.")
    else:
        print(f"{zahl} liegt nicht zwischen 50 und 100.")


def alterspruefung_fuer_autofahren():
    # Aufgabe 2.5: Altersprüfung für Autofahren
    alter = int(input("Gib dein Alter ein: "))
    if alter >= 18:
        print("Du darfst Auto fahren.")
    elif alter >= 16:
        print("Du darfst einen Führerschein machen.")
    else:
        print("Du bist zu jung für den Führerschein.")


def zwei_zahlen_vergleichen():
    # Aufgabe 2.6: Zwei Zahlen vergleichen
    zahl1 = int(input("Gib die erste Zahl ein: "))
    zahl2 = int(input("Gib die zweite Zahl ein: "))

    if zahl1 == zahl2:
        print("Die Zahlen sind gleich.")
    else:
        print(f"Die größere Zahl ist: {max(zahl1, zahl2)}.")

    summe = zahl1 + zahl2
    if summe % 2 == 0:
        print(f"Die Summe {summe} ist gerade.")
    else:
        print(f"Die Summe {summe} ist ungerade.")


# --- Teil 5: Print-Ausgaben und Escape-Zeichen ---
def print_ausgaben():
    # Aufgabe 3: Grundlegende Print-Ausgabe
    name = "Max Mustermann"
    ausbildung = "Softwareentwickler"
    zitat = "Der Weg ist das Ziel."

    print(f"Name: {name}")
    print(f"Ausbildung: {ausbildung}")
    print(f"Zitat: \"{zitat}\"")


def escape_zeichen():
    # Aufgabe 4: Verwendung von Escape-Zeichen
    print("Dies ist ein Tabulator:\t\tEnde der Zeile")
    print("Dies ist ein Zeilenumbruch:\nNächste Zeile")


# --- Teil 6: Input und Output ---
def benutzereingabe():
    # Aufgabe 5: Benutzereingabe
    name = input("Wie heißt du? ")
    alter = input("Wie alt bist du? ")
    beruf = input("Was ist dein Beruf? ")

    print(f"Hallo {name}, du bist {alter} Jahre alt und arbeitest als {beruf}.")


def eingaben_validieren():
    # Aufgabe 6: Eingaben validieren
    eingabe = input("Gib eine Zahl ein: ")

    if eingabe.isdigit():
        print(f"Die Zahl ist: {eingabe}")
    else:
        print("Fehler: Das ist keine gültige Zahl.")


# --- Hauptprogramm: Menü und Auswahl ---
def main():
    while True:
        print("\nWähle eine Aufgabe:")
        print("1. Literale und Bezeichner")
        print("2. Namensräume: Lokale und globale Variablen")
        print("3. Verschachtelte Namensräume")
        print("4. Built-in Funktionen")
        print("5. Eingaben verarbeiten")
        print("6. Anweisungsfolgen: Lineare Anweisungen")
        print("7. Zahl gerade oder ungerade")
        print("8. Zahl größer, kleiner oder gleich 100")
        print("9. Passwort überprüfen")
        print("10. Zahl zwischen 50 und 100")
        print("11. Altersprüfung für Autofahren")
        print("12. Zwei Zahlen vergleichen")
        print("13. Print-Ausgaben")
        print("14. Escape-Zeichen")
        print("15. Benutzereingabe")
        print("16. Eingaben validieren")
        print("17. Beenden")

        auswahl = input("\nWähle eine Option (1-17): ")

        if auswahl == "1":
            literale_und_bezeichner()
        elif auswahl == "2":
            lokale_und_globale_variablen()
        elif auswahl == "3":
            verschachtelte_namensraeume()
        elif auswahl == "4":
            built_in_funktionen()
        elif auswahl == "5":
            eingaben_verarbeiten()
        elif auswahl == "6":
            lineare_anweisungsfolge()
        elif auswahl == "7":
            zahl_gerade_oder_ungerade()
        elif auswahl == "8":
            zahl_groesser_kleiner_oder_100()
        elif auswahl == "9":
            passwort_pruefen()
        elif auswahl == "10":
            zahl_zwischen_50_und_100()
        elif auswahl == "11":
            alterspruefung_fuer_autofahren()
        elif auswahl == "12":
            zwei_zahlen_vergleichen()
        elif auswahl == "13":
            print_ausgaben()
        elif auswahl == "14":
            escape_zeichen()
        elif auswahl == "15":
            benutzereingabe()
        elif auswahl == "16":
            eingaben_validieren()
        elif auswahl == "17":
            print("Beenden des Programms.")
            break
        else:
            print("Ungültige Auswahl, versuche es erneut.")

# Hauptprogramm starten
if __name__ == "__main__":
    main()
