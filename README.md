# Python-Projekt mit Git

## Inhaltsverzeichnis

1. [Projektaufgabe: Python-Projekt mit Git](#projektaufgabe-python-projekt-mit-git)
2. [Teil 1: Literale und Bezeichner](#teil-1-literale-und-bezeichner)
    1. [Aufgabe 1: Literale in Python](#aufgabe-1-literale-in-python)
    2. [Aufgabe 2: Bezeichner und Kommentare](#aufgabe-2-bezeichner-und-kommentare)
3. [Teil 2: Namensräume](#teil-2-namensräume)
    1. [Aufgabe 3: Lokale und globale Variablen](#aufgabe-3-lokale-und-globale-variablen)
    2. [Aufgabe 4: Verschachtelte Namensräume](#aufgabe-4-verschachtelte-namensräume)
4. [Teil 3: Built-in Funktionen](#teil-3-built-in-funktionen)
    1. [Aufgabe 5: Wichtige Built-in Funktionen](#aufgabe-5-wichtige-built-in-funktionen)
    2. [Aufgabe 6: Eingaben verarbeiten](#aufgabe-6-eingaben-verarbeiten)
5. [Teil 4: Anweisungsfolgen](#teil-4-anweisungsfolgen)
    1. [Aufgabe 1: Lineare Anweisungsfolge](#aufgabe-1-lineare-anweisungsfolge)
    2. [Aufgabe 2: Kontrollstrukturen](#aufgabe-2-kontrollstrukturen)
6. [Teil 5: Print-Ausgaben und Escape-Zeichen](#teil-5-print-ausgaben-und-escape-zeichen)
    1. [Aufgabe 3: Grundlegende Print-Ausgabe](#aufgabe-3-grundlegende-print-ausgabe)
    2. [Aufgabe 4: Verwendung von Escape-Zeichen](#aufgabe-4-verwendung-von-escape-zeichen)
7. [Teil 6: Input und Output](#teil-6-input-und-output)
    1. [Aufgabe 5: Benutzereingabe](#aufgabe-5-benutzereingabe)
    2. [Aufgabe 6: Eingaben validieren](#aufgabe-6-eingaben-validieren)
8. [Teil 7: Datentypen und Variablen](#teil-7-datentypen-und-variablen)
    1. [Aufgabe 7: Variablen mit verschiedenen Datentypen](#aufgabe-7-variablen-mit-verschiedenen-datentypen)
    2. [Aufgabe 8: Typkonvertierung](#aufgabe-8-typkonvertierung)
9. [Teil 8: Exception Handling](#teil-8-exception-handling)
    1. [Aufgabe 9: Grundlegende Fehlerbehandlung](#aufgabe-9-grundlegende-fehlerbehandlung)
10. [Abschluss](#abschluss)

---

## Projektaufgabe: Python-Projekt mit Git

### Projekt anlegen:
- Erstellen Sie ein neues Projektverzeichnis mit dem Namen `mein_erstes_projekt`.
- Legen Sie darin eine neue Datei `main.py` an.
- Öffnen Sie die Datei in einem Texteditor oder einer IDE.

### Git initialisieren und Repository erstellen:
- Initialisieren Sie das Projektverzeichnis als Git-Repository.
- Fügen Sie die `main.py`-Datei zum Repository hinzu.
- Erstellen Sie einen ersten Commit.
- Erstellen Sie ein Remote-Repository auf GitHub oder GitLab und verbinden Sie es.

> **Hinweis:** Das Repository muss später zur Überprüfung freigegeben werden.

---

## Teil 1: Literale und Bezeichner

### Aufgabe 1: Literale in Python
Definieren Sie verschiedene Literale in der `main.py`:
- Ganze Zahlen (`int`)
- Gleitkommazahlen (`float`)
- Zeichenfolgen (`str`)
- Booleans (`bool`)
- Listen (`list`)

### Aufgabe 2: Bezeichner und Kommentare
- Wählen Sie sinnvolle Bezeichner für Variablen, die den Zweck der Variablen klar beschreiben.
- Fügen Sie zu jeder Variablendeklaration einen Kommentar hinzu, der erklärt, wofür die Variable verwendet wird.

---

## Teil 2: Namensräume

### Aufgabe 3: Lokale und globale Variablen
- Definieren Sie eine globale Variable und verwenden Sie sie in einer Funktion.
- Legen Sie innerhalb der Funktion eine lokale Variable mit demselben Namen an und geben Sie beide Variablen aus.

### Aufgabe 4: Verschachtelte Namensräume
- Definieren Sie eine äußere und eine innere Funktion.
- Verwenden Sie `nonlocal`, um eine Variable im umschließenden Namensraum zu ändern.

---

## Teil 3: Built-in Funktionen

### Aufgabe 5: Wichtige Built-in Funktionen
- Verwenden Sie `len()` und `type()`, um Informationen über Variablen zu erhalten.
- Nutzen Sie `sum()`, `max()` und `min()` für numerische Listen.
- Verwenden Sie `sorted()` zum Sortieren einer Liste.

### Aufgabe 6: Eingaben verarbeiten
- Verwenden Sie `input()`, um eine Zahl vom Benutzer zu erhalten, und konvertieren Sie diese mit `int()`.
- Überprüfen Sie mit `isinstance()`, ob die Eingabe vom richtigen Typ ist.

---

## Teil 4: Anweisungsfolgen

### Aufgabe 1: Lineare Anweisungsfolge
- Schreiben Sie ein Python-Programm, das folgende Schritte ausführt:
  - Definieren Sie eine Variable `startwert` und setzen Sie sie auf 10.
  - Addieren Sie 5 zu `startwert` und speichern Sie das Ergebnis in einer neuen Variablen `zwischenwert`.
  - Multiplizieren Sie `zwischenwert` mit 2 und speichern Sie das Ergebnis im `Endwert`.
  - Geben Sie alle drei Variablen aus.

### Aufgabe 2: Kontrollstrukturen
- Schreiben Sie ein Programm, das entscheidet, ob eine Zahl gerade oder ungerade ist:
  - Fordern Sie den Benutzer auf, eine Zahl einzugeben.
  - Nutzen Sie eine `if-else`-Anweisung, um die Zahl zu überprüfen.

- Schreiben Sie ein Programm, das überprüft, ob eine eingegebene Zahl größer, kleiner oder gleich 100 ist.

- Schreiben Sie ein Programm, das prüft, ob ein Benutzer ein Passwort korrekt eingibt.

- Schreiben Sie ein Programm, das überprüft, ob eine Zahl zwischen 50 und 100 liegt.

- Schreiben Sie ein Programm, das das Alter eines Benutzers abfragt und prüft, ob er Auto fahren darf:
  - Ab 18: "Du darfst Auto fahren."
  - Unter 18, aber über 16: "Du darfst einen Führerschein machen."
  - Unter 16: "Du bist zu jung für den Führerschein."

- Schreiben Sie ein Programm, das zwei Zahlen abfragt und entscheidet:
  - Ob die Zahlen gleich sind.
  - Welche der beiden Zahlen größer ist.
  - Ob die Summe der beiden Zahlen gerade oder ungerade ist.

---

## Teil 5: Print-Ausgaben und Escape-Zeichen

### Aufgabe 3: Grundlegende Print-Ausgabe
- Schreiben Sie ein Programm, das folgende Informationen ausgibt:
  - Ihren Namen.
  - Ihre Ausbildung.
  - Ein beliebiges Zitat.
  - Verwenden Sie Formatierung.

### Aufgabe 4: Verwendung von Escape-Zeichen
- Nutzen Sie Escape-Zeichen, um folgende Ausgaben zu erzeugen:
  - Einen Tabulator.
  - Einen Zeilenumbruch.

---

## Teil 6: Input und Output

### Aufgabe 5: Benutzereingabe
- Schreiben Sie ein Programm, das folgende Daten vom Benutzer abfragt:
  - Name
  - Alter
  - Beruf
- Geben Sie eine Begrüßungsnachricht basierend auf den Eingaben aus.

### Aufgabe 6: Eingaben validieren
- Schreiben Sie ein Programm, das eine Zahl vom Benutzer abfragt und überprüft, ob die Eingabe gültig ist:
  - Verwenden Sie `isdigit()`, um sicherzustellen, dass die Eingabe eine Zahl ist.
  - Falls die Eingabe ungültig ist, geben Sie eine Fehlermeldung aus.

---

## Teil 7: Datentypen und Variablen

### Aufgabe 7: Variablen mit verschiedenen Datentypen
- Erstellen Sie Variablen mit den folgenden Datentypen:
  - Ganze Zahl (`int`)
  - Gleitkommazahl (`float`)
  - Text (`str`)
  - Wahrheitswert (`bool`)
- Geben Sie die Variablen zusammen mit ihrem Datentyp aus.

### Aufgabe 8: Typkonvertierung
- Schreiben Sie ein Programm, das eine Ganzzahl in eine Gleitkommazahl und einen String umwandelt.
- Geben Sie alle drei Versionen aus.

---

## Teil 8: Exception Handling

### Aufgabe 9: Grundlegende Fehlerbehandlung
- Schreiben Sie ein Programm, das eine Zahl vom Benutzer abfragt.
- Verwenden Sie `try-except`, um sicherzustellen, dass:
  - Wenn die Eingabe keine Zahl ist, eine Fehlermeldung ausgegeben wird.
  - Wenn die Zahl durch 0 geteilt wird, eine Warnung ausgegeben wird.
  - Andernfalls das Ergebnis der Division durch 2 ausgegeben wird.

- Schreiben Sie ein Programm, das eine Zahl prüft:
  - Wenn die Zahl negativ ist, soll ein benutzerdefinierter Fehler ausgelöst werden.

---

## Abschluss

- **Testen Sie Ihr Projekt:**
  - Führen Sie die Datei `main.py` aus und überprüfen Sie die Ergebnisse.

- **Freigabe:**
  - Laden Sie alle Änderungen in Ihr Git-Repository hoch.
