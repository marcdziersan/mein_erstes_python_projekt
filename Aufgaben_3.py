# Aufgaben_3.py

# Teil 1: Kopfgesteuerte Schleife (while-Schleife)

# Aufgabe 1: Zahlen zählen
print("Aufgabe 1: Zahlen zählen")
i = 1
while i <= 10:
    print(i)
    i += 1

# Aufgabe 2: Benutzereingaben
print("\nAufgabe 2: Benutzereingaben")
summe = 0
while True:
    zahl = int(input("Geben Sie eine Zahl ein (0 zum Beenden): "))
    if zahl == 0:
        break
    summe += zahl
print(f"Die Summe der eingegebenen Zahlen ist: {summe}")

# Aufgabe 3: Passworteingabe
print("\nAufgabe 3: Passworteingabe")
richtiges_passwort = "geheim"
while True:
    eingabe = input("Bitte geben Sie das Passwort ein: ")
    if eingabe == richtiges_passwort:
        print("Passwort korrekt!")
        break
    print("Falsches Passwort, bitte erneut versuchen.")

# Teil 2: For-Schleife

# Aufgabe 4: Zahlenbereiche
print("\nAufgabe 4: Zahlenbereiche")
for i in range(1, 11):
    print(i)

# Aufgabe 5: Gerade Zahlen
print("\nAufgabe 5: Gerade Zahlen")
for i in range(2, 21, 2):
    print(i)

print("\nJede 5. Zahl:")
for i in range(5, 51, 5):
    print(i)

# Aufgabe 6: Verschachtelte Schleifen
print("\nAufgabe 6: Rechteck aus Sternen")
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()

# Aufgabe 7: Rückwärts iterieren
print("\nAufgabe 7: Rückwärts iterieren")
for i in range(10, 0, -1):
    print(i)

# Teil 3: Listen und ihre Methoden

# Aufgabe 8: Erstellen und Manipulieren von Listen
print("\nAufgabe 8: Erstellen und Manipulieren von Listen")
namen = ["Anna", "Max", "Tom", "Lisa"]
namen.append("Marie")
namen.remove("Tom")
print("Aktuelle Liste:", namen)
print("Länge der Liste:", len(namen))

# Aufgabe 9: Sortieren und Umkehren
print("\nAufgabe 9: Sortieren und Umkehren")
zahlen = [5, 3, 8, 1, 2]
zahlen.sort()
print("Aufsteigend sortiert:", zahlen)
zahlen.sort(reverse=True)
print("Absteigend sortiert:", zahlen)
zahlen.reverse()
print("Reihenfolge umgekehrt:", zahlen)

# Aufgabe 10: Methoden für Listen
print("\nAufgabe 10: Methoden für Listen")
zahlen = [1, 2, 3, 4, 5]
zahlen.append(6)
zahlen.insert(0, 0)
print("Liste nach Hinzufügungen:", zahlen)
print("Anzahl der 3 in der Liste:", zahlen.count(3))

# Teil 4: For-Schleifen für Listen

# Aufgabe 11: Iterieren über Listen
print("\nAufgabe 11: Iterieren über Listen")
werte = [10, 20, 30, 40, 50]
for wert in werte:
    print(wert)

# Aufgabe 12: Summieren von Elementen
print("\nAufgabe 12: Summieren von Elementen")
werte = [10, 20, 30, 40, 50]
summe = sum(werte)
print(f"Die Summe der Liste ist: {summe}")

# Aufgabe 13: Iteration über einen String
print("\nAufgabe 13: Iteration über einen String")
text = "Hallo"
for buchstabe in text:
    print(buchstabe)

# Aufgabe 14: Filtern von Elementen
print("\nAufgabe 14: Filtern von Elementen")
zahlen = [5, 15, 25, 10, 8, 12]
gefiltert = [zahl for zahl in zahlen if zahl > 10]
print("Zahlen größer als 10:", gefiltert)

# Aufgabe 15: Indizes verwenden
print("\nAufgabe 15: Indizes verwenden")
zahlen = [5, 15, 25, 10, 8, 12]
for index in range(len(zahlen)):
    print(f"Index: {index}, Wert: {zahlen[index]}")

# Aufgabe 16: Enumerate
print("\nAufgabe 16: Enumerate")
for index, wert in enumerate([10, 20, 30, 40, 50]):
    print(f"Index: {index}, Wert: {wert}")
