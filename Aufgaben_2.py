# Aufgaben_2.py

# Teil 4: Anweisungsfolgen

# Aufgabe 1: Lineare Anweisungsfolge
print("Aufgabe 1: Lineare Anweisungsfolge")
startwert = 10
zwischenwert = startwert + 5
endwert = zwischenwert * 2
print("Startwert:", startwert)
print("Zwischenwert:", zwischenwert)
print("Endwert:", endwert)
print()

# Aufgabe 2: Kontrollstrukturen

# 1. Gerade oder ungerade
print("Aufgabe 2.1: Gerade oder ungerade Zahl")
zahl = int(input("Bitte geben Sie eine Zahl ein: "))
if zahl % 2 == 0:
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")
print()

# 2. Größer, kleiner oder gleich 100
print("Aufgabe 2.2: Zahl mit 100 vergleichen")
zahl = int(input("Bitte geben Sie eine Zahl ein: "))
if zahl > 100:
    print("Die Zahl ist größer als 100.")
elif zahl < 100:
    print("Die Zahl ist kleiner als 100.")
else:
    print("Die Zahl ist gleich 100.")
print()

# 3. Passwortprüfung
print("Aufgabe 2.3: Passwortprüfung")
korrektes_passwort = "geheim"
passwort = input("Bitte geben Sie Ihr Passwort ein: ")
if passwort == korrektes_passwort:
    print("Passwort korrekt.")
else:
    print("Passwort falsch.")
print()

# 4. Zahl zwischen 50 und 100
print("Aufgabe 2.4: Zahl zwischen 50 und 100 prüfen")
zahl = int(input("Bitte geben Sie eine Zahl ein: "))
if 50 <= zahl <= 100:
    print("Die Zahl liegt zwischen 50 und 100.")
else:
    print("Die Zahl liegt nicht zwischen 50 und 100.")
print()

# 5. Altersprüfung
print("Aufgabe 2.5: Altersprüfung")
alter = int(input("Bitte geben Sie Ihr Alter ein: "))
if alter >= 18:
    print("Du darfst Auto fahren.")
elif 16 < alter < 18:
    print("Du darfst einen Führerschein machen.")
else:
    print("Du bist zu jung für den Führerschein.")
print()

# 6. Zwei Zahlen vergleichen
print("Aufgabe 2.6: Zwei Zahlen vergleichen")
zahl1 = int(input("Bitte geben Sie die erste Zahl ein: "))
zahl2 = int(input("Bitte geben Sie die zweite Zahl ein: "))
if zahl1 == zahl2:
    print("Die Zahlen sind gleich.")
elif zahl1 > zahl2:
    print("Die erste Zahl ist größer.")
else:
    print("Die zweite Zahl ist größer.")

if (zahl1 + zahl2) % 2 == 0:
    print("Die Summe der beiden Zahlen ist gerade.")
else:
    print("Die Summe der beiden Zahlen ist ungerade.")
print()

# Teil 5: Print-Ausgaben und Escape-Zeichen

# Aufgabe 3: Grundlegende Print-Ausgabe
print("Aufgabe 3: Print-Ausgabe")
name = "Max Mustermann"
ausbildung = "Informatiker"
zitat = "Die beste Zeit, einen Baum zu pflanzen, war vor 20 Jahren. Die zweitbeste Zeit ist jetzt."
print(f"Name: {name}")
print(f"Ausbildung: {ausbildung}")
print(f"Zitat: \"{zitat}\"")
print()

# Aufgabe 4: Verwendung von Escape-Zeichen
print("Aufgabe 4: Verwendung von Escape-Zeichen")
print("Tab\tTabulator")
print("Zeilenumbruch\nNeue Zeile")
print()

# Teil 6: Input und Output

# Aufgabe 5: Benutzereingabe
print("Aufgabe 5: Benutzereingabe")
name = input("Bitte geben Sie Ihren Namen ein: ")
alter = input("Bitte geben Sie Ihr Alter ein: ")
beruf = input("Bitte geben Sie Ihren Beruf ein: ")
print(f"Hallo {name}, Sie sind {alter} Jahre alt und arbeiten als {beruf}.")
print()

# Aufgabe 6: Eingaben validieren
print("Aufgabe 6: Eingabe validieren")
eingabe = input("Bitte geben Sie eine Zahl ein: ")
if eingabe.isdigit():
    print("Danke! Ihre Eingabe war gültig:", eingabe)
else:
    print("Fehler: Ihre Eingabe ist keine Zahl.")
print()

# Teil 7: Datentypen und Variablen

# Aufgabe 7: Variablen mit verschiedenen Datentypen
print("Aufgabe 7: Datentypen")
ganzzahl = 42
gleitkommazahl = 3.14
text = "Hallo Welt"
wahrheitswert = True
print(f"Ganzzahl: {ganzzahl}, Typ: {type(ganzzahl)}")
print(f"Gleitkommazahl: {gleitkommazahl}, Typ: {type(gleitkommazahl)}")
print(f"Text: {text}, Typ: {type(text)}")
print(f"Wahrheitswert: {wahrheitswert}, Typ: {type(wahrheitswert)}")
print()

# Aufgabe 8: Typkonvertierung
print("Aufgabe 8: Typkonvertierung")
zahl = 10
gleitkomma = float(zahl)
text = str(zahl)
print(f"Ganzzahl: {zahl}")
print(f"Gleitkommazahl: {gleitkomma}")
print(f"Text: {text}")
print()

# Teil 8: Exception Handling

# Aufgabe 9: Grundlegende Fehlerbehandlung
print("Aufgabe 9: Fehlerbehandlung")
try:
    zahl = int(input("Bitte geben Sie eine Zahl ein: "))
    ergebnis = zahl / 2
    print("Ergebnis:", ergebnis)
except ValueError:
    print("Fehler: Das war keine gültige Zahl.")
except ZeroDivisionError:
    print("Warnung: Division durch 0 ist nicht erlaubt.")
print()

# Benutzerdefinierter Fehler für negative Zahlen
print("Aufgabe 9.4: Benutzerdefinierter Fehler")
try:
    zahl = int(input("Bitte geben Sie eine Zahl ein: "))
    if zahl < 0:
        raise ValueError("Negative Zahlen sind nicht erlaubt!")
    print("Die Zahl ist positiv.")
except ValueError as e:
    print("Fehler:", e)
