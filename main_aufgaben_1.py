# Teil 1: Literale und Bezeichner

# Verschiedene Literale in Python
ganze_zahl = 42  # Integer (int)
gleitkommazahl = 3.14  # Float (Gleitkommazahl)
zeichenfolge = "Hallo Welt"  # String (str)
wahrheitswert = True  # Boolean (bool)
liste = [1, 2, 3, 4, 5]  # Liste (list)

# Variablen mit sinnvollen Bezeichnern
alter = 25  # Alter einer Person
pi = 3.14159  # Mathematische Konstante Pi
name = "Alice"  # Name der Person
ist_student = False  # Status, ob die Person ein Student ist
zahlen_liste = [10, 20, 30, 40]  # Liste von Zahlen

# Teil 2: Namensräume

# Globale Variable
globale_variable = "Ich bin global"

def beispiel_funktion():
    # Lokale Variable mit gleichem Namen
    globale_variable = "Ich bin lokal"
    print("Lokale Variable:", globale_variable)
    print("Globale Variable:", globals()['globale_variable'])

beispiel_funktion()

def äußere_funktion():
    variable = "Ursprünglich"

    def innere_funktion():
        nonlocal variable
        variable = "Geändert"
        print("Innere Funktion:", variable)

    innere_funktion()
    print("Äußere Funktion:", variable)

äußere_funktion()

# Teil 3: Built-in Funktionen

# len() und type()
zahlen_liste = [5, 10, 15]
print("Länge der Liste:", len(zahlen_liste))
print("Typ der Variable:", type(zahlen_liste))

# sum(), max(), min()
print("Summe:", sum(zahlen_liste))
print("Maximalwert:", max(zahlen_liste))
print("Minimalwert:", min(zahlen_liste))

# sorted()
unsortierte_liste = [3, 1, 4, 1, 5]
print("Sortierte Liste:", sorted(unsortierte_liste))

# Eingabe verarbeiten
eingabe = input("Geben Sie eine Zahl ein: ")

# Eingabe in int umwandeln
try:
    zahl = int(eingabe)
    print("Eingegebene Zahl:", zahl)
    print("Typ ist korrekt:", isinstance(zahl, int))
except ValueError:
    print("Das ist keine gültige Zahl.")
