# Teil 4: Anweisungsfolgen

# Aufgabe 1: Lineare Anweisungsfolge
startwert = 10  # Startwert
zwischenwert = startwert + 5  # Addition von 5
endwert = zwischenwert * 2  # Multiplikation mit 2

print("Startwert:", startwert)
print("Zwischenwert:", zwischenwert)
print("Endwert:", endwert)

# Aufgabe 2: Kontrollstrukturen

# 1. Programm, das entscheidet, ob eine Zahl gerade oder ungerade ist:
zahl = int(input("Gib eine Zahl ein: "))
if zahl % 2 == 0:
    print(f"{zahl} ist gerade.")
else:
    print(f"{zahl} ist ungerade.")

# 2. Programm, das überprüft, ob eine Zahl größer, kleiner oder gleich 100 ist:
zahl = int(input("Gib eine Zahl ein: "))
if zahl > 100:
    print(f"{zahl} ist größer als 100.")
elif zahl < 100:
    print(f"{zahl} ist kleiner als 100.")
else:
    print(f"{zahl} ist gleich 100.")

# 3. Programm, das prüft, ob ein Benutzer ein Passwort korrekt eingibt:
korrektes_passwort = "passwort123"
benutzer_passwort = input("Gib dein Passwort ein: ")
if benutzer_passwort == korrektes_passwort:
    print("Passwort korrekt!")
else:
    print("Falsches Passwort!")

# 4. Programm, das überprüft, ob eine Zahl zwischen 50 und 100 liegt:
zahl = int(input("Gib eine Zahl ein: "))
if 50 <= zahl <= 100:
    print(f"{zahl} liegt zwischen 50 und 100.")
else:
    print(f"{zahl} liegt nicht zwischen 50 und 100.")

# 5. Programm, das das Alter eines Benutzers abfragt und prüft, ob er Auto fahren darf:
alter = int(input("Gib dein Alter ein: "))
if alter >= 18:
    print("Du darfst Auto fahren.")
elif alter >= 16:
    print("Du darfst einen Führerschein machen.")
else:
    print("Du bist zu jung für den Führerschein.")

# 6. Programm, das zwei Zahlen abfragt und entscheidet:
zahl1 = int(input("Gib die erste Zahl ein: "))
zahl2 = int(input("Gib die zweite Zahl ein: "))

# Überprüfen, ob die Zahlen gleich sind
if zahl1 == zahl2:
    print("Die Zahlen sind gleich.")
else:
    print(f"Die größere Zahl ist: {max(zahl1, zahl2)}.")

# Überprüfen, ob die Summe der beiden Zahlen gerade oder ungerade ist
summe = zahl1 + zahl2
if summe % 2 == 0:
    print(f"Die Summe {summe} ist gerade.")
else:
    print(f"Die Summe {summe} ist ungerade.")

# Teil 5: Print-Ausgaben und Escape-Zeichen

# Aufgabe 3: Grundlegende Print-Ausgabe
name = "Max Mustermann"
ausbildung = "Softwareentwickler"
zitat = "Der Weg ist das Ziel."

print(f"Name: {name}")
print(f"Ausbildung: {ausbildung}")
print(f"Zitat: \"{zitat}\"")

# Aufgabe 4: Verwendung von Escape-Zeichen
# Tabulator und Zeilenumbruch
print("Dies ist ein Tabulator:\t\tEnde der Zeile")
print("Dies ist ein Zeilenumbruch:\nNächste Zeile")

# Teil 6: Input und Output

# Aufgabe 5: Benutzereingabe
name = input("Wie heißt du? ")
alter = input("Wie alt bist du? ")
beruf = input("Was ist dein Beruf? ")

print(f"Hallo {name}, du bist {alter} Jahre alt und arbeitest als {beruf}.")

# Aufgabe 6: Eingaben validieren
eingabe = input("Gib eine Zahl ein: ")

if eingabe.isdigit():
    print(f"Die Zahl ist: {eingabe}")
else:
    print("Fehler: Das ist keine gültige Zahl.")

# Teil 7: Datentypen und Variablen

# Aufgabe 7: Variablen mit verschiedenen Datentypen
ganzzahl = 42  # Ganzzahl (int)
gleitkommazahl = 3.14  # Gleitkommazahl (float)
text = "Hallo, Welt!"  # String (str)
wahrheitswert = True  # Boolean (bool)

print(f"Variable 'ganzzahl': {ganzzahl}, Typ: {type(ganzzahl)}")
print(f"Variable 'gleitkommazahl': {gleitkommazahl}, Typ: {type(gleitkommazahl)}")
print(f"Variable 'text': {text}, Typ: {type(text)}")
print(f"Variable 'wahrheitswert': {wahrheitswert}, Typ: {type(wahrheitswert)}")

# Aufgabe 8: Typkonvertierung
ganzzahl = 42
gleitkommazahl = float(ganzzahl)  # Umwandlung in float
text = str(ganzzahl)  # Umwandlung in string

print(f"Ganzzahl: {ganzzahl}, Gleitkommazahl: {gleitkommazahl}, Text: {text}")

# Teil 8: Exception Handling

# Aufgabe 9: Grundlegende Fehlerbehandlung

# 1. Zahl vom Benutzer abfragen und Fehlerbehandlung
try:
    zahl = int(input("Gib eine Zahl ein: "))
    print(f"Die eingegebene Zahl ist: {zahl}")
except ValueError:
    print("Das ist keine gültige Zahl.")

# 2. Fehlerbehandlung bei Division und ungültiger Eingabe
try:
    zahl = int(input("Gib eine Zahl ein: "))
    ergebnis = 10 / zahl
    print(f"Ergebnis der Division durch 10: {ergebnis}")
except ValueError:
    print("Das ist keine gültige Zahl.")
except ZeroDivisionError:
    print("Warnung: Division durch 0 ist nicht möglich.")

# 3. Benutzerdefinierter Fehler bei negativen Zahlen
try:
    zahl = int(input("Gib eine Zahl ein: "))
    if zahl < 0:
        raise ValueError("Die Zahl ist negativ und nicht erlaubt.")
    print(f"Die eingegebene Zahl ist: {zahl}")
except ValueError as e:
    print(f"Fehler: {e}")
