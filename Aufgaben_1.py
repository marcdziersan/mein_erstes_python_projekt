# Aufgaben Teil 1: Literale und Bezeichner

# Aufgabe 1: Literale in Python
# Ganze Zahl (int)
anzahl_kinder = 3  # Anzahl der Kinder in der Familie
# Gleitkommazahl (float)
durchschnittsnote = 2.7  # Durchschnittsnote eines Schülers
# Zeichenfolge (str)
willkommensnachricht = "Willkommen zu meinem ersten Python-Projekt!"  # Begrüßung
# Boolean (bool)
ist_aktiv = True  # Status, ob ein Benutzer aktiv ist
# Liste (list)
wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]  # Liste der Arbeitstage

# Aufgabe 2: Bezeichner und Kommentare
# Sinnvolle Bezeichner mit Kommentaren wurden oben verwendet.

# Teil 2: Namensräume

# Aufgabe 3: Lokale und globale Variablen
# Globale Variable
benutzername = "MaxMustermann"  # Globale Variable, die den Namen des Benutzers speichert

def zeige_namensraeume():
    # Lokale Variable mit gleichem Namen
    benutzername = "LokalMax"  
    print("Lokale Variable 'benutzername':", benutzername)  # Lokaler Wert wird ausgegeben
    print("Globale Variable 'benutzername':", globals()["benutzername"])  # Globaler Wert wird ausgegeben

zeige_namensraeume()

# Aufgabe 4: Verschachtelte Namensräume

def aussen():
    variable = "Ursprünglicher Wert"
    
    def innen():
        nonlocal variable  # Ändert die Variable im äußeren Namensraum
        variable = "Geänderter Wert"
    
    innen()
    print("Variable nach Änderung:", variable)  # Gibt den neuen Wert der Variable aus

aussen()

# Teil 3: Built-in Funktionen

# Aufgabe 5: Wichtige Built-in Funktionen
zahlen_liste = [3, 7, 1, 9, 5]  # Beispiel-Liste mit Zahlen
print("Länge der Liste:", len(zahlen_liste))  # Anzahl der Elemente in der Liste
print("Typ der Liste:", type(zahlen_liste))  # Gibt den Typ der Liste aus
print("Summe der Liste:", sum(zahlen_liste))  # Summe der Elemente
print("Maximale Zahl in der Liste:", max(zahlen_liste))  # Größtes Element
print("Minimale Zahl in der Liste:", min(zahlen_liste))  # Kleinstes Element
print("Sortierte Liste:", sorted(zahlen_liste))  # Gibt eine sortierte Kopie der Liste zurück

# Aufgabe 6: Eingaben verarbeiten
# Benutzer-Eingabe
eingabe = input("Bitte geben Sie eine Zahl ein: ")

try:
    # Konvertiert die Eingabe in eine Ganzzahl
    zahl = int(eingabe)  
    # Überprüft, ob die Eingabe tatsächlich eine Ganzzahl ist
    if isinstance(zahl, int):  
        print(f"Die eingegebene Zahl ist: {zahl}")
except ValueError:
    print("Die Eingabe ist keine gültige Zahl.")

# Abschluss:
# Testen Sie die Datei durch Ausführen mit `python Aufgaben_1.py`
