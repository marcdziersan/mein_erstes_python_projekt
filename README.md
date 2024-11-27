Aufgaben Teil 1

Projektaufgabe: Python-Projekt mit Git

Projekt anlegen:

o	Erstellen Sie ein neues Projektverzeichnis mit dem Namen mein_erstes_projekt.
o	Legen Sie darin eine neue Datei main.py an.
o	Öffnen Sie die Datei in einem Texteditor oder einer IDE 

Git initialisieren und Repository erstellen:

o	Initialisieren Sie das Projektverzeichnis als Git-Repository
o	Fügen Sie die main.py-Datei zum Repository hinzu:
o	Erstellen Sie einen ersten Commit:
o	Erstellen Sie ein Remote-Repository auf GitHub oder GitLab und verbinden Sie es:

Hinweis: Das Repository muss später zur Überprüfung freigegeben werden.

Teil 1: Literale und Bezeichner

Aufgabe 1: Literale in Python

1.	Definieren Sie verschiedene Literale in der main.py:

o	Ganze Zahlen (int), Gleitkommazahlen (float), Zeichenfolgen (str), Booleans (bool) und Listen (list).

Aufgabe 2: Bezeichner und Kommentare

1.	Wählen Sie sinnvolle Bezeichner für Variablen, die den Zweck der Variablen klar beschreiben.
2.	Fügen Sie zu jeder Variablendeklaration einen Kommentar hinzu, der erklärt, wofür die Variable verwendet wird.


Teil 2: Namensräume

Aufgabe 3: Lokale und globale Variablen

1.	Definieren Sie eine globale Variable und verwenden Sie sie in einer Funktion.
2.	Legen Sie innerhalb der Funktion eine lokale Variable mit demselben Namen an und geben Sie beide Variablen aus

Aufgabe 4: Verschachtelte Namensräume

1.	Definieren Sie eine äußere und eine innere Funktion.
2.	Verwenden Sie nonlocal, um eine Variable im umschließenden Namensraum zu ändern

Teil 3: Built-in Funktionen

Aufgabe 5: Wichtige Built-in Funktionen

1.	Verwenden Sie len() und type(), um Informationen über Variablen zu erhalten
2.	Nutzen Sie sum(), max(), und min() für numerische Listen
3.	Verwenden Sie sorted() zum Sortieren einer Liste

Aufgabe 6: Eingaben verarbeiten

1.	Verwenden Sie input(), um eine Zahl vom Benutzer zu erhalten, und konvertieren Sie diese mit int():
2.	Überprüfen Sie mit isinstance(), ob die Eingabe vom richtigen Typ ist:

Abschluss
Testen Sie Ihr Projekt:

o	Führen Sie die Datei main.py aus und überprüfen Sie die Ergebnisse.

Freigabe:

o	Laden Sie alle Änderungen in Ihr Git-Repository hoch:

Aufgabenblatt Teil 2

Teil 4: Anweisungsfolgen

Aufgabe 1: Lineare Anweisungsfolge

1.	Schreiben Sie ein Python-Programm, das folgende Schritte ausführt:

o	Definieren Sie eine Variable startwert und setzen Sie sie auf 10.
o	Addieren Sie 5 zu startwert und speichern Sie das Ergebnis in einer neuen Variable zwischenwert.
o	Multiplizieren Sie zwischenwert mit 2 und speichern Sie das Ergebnis im Endwert.
o	Geben Sie alle drei Variablen aus.

Aufgabe 2: Kontrollstrukturen

1.	Schreiben Sie ein Programm, das entscheidet, ob eine Zahl gerade oder ungerade ist:

o	Fordern Sie den Benutzer auf, eine Zahl einzugeben.
o	Nutzen Sie eine if-else-Anweisung, um die Zahl zu überprüfen.

2.	Schreiben Sie ein Programm, das überprüft, ob eine eingegebene Zahl größer, kleiner oder gleich 100 ist.

3.	Schreiben Sie ein Programm, das prüft, ob ein Benutzer ein Passwort korrekt eingibt.

4.	Schreiben Sie ein Programm, das überprüft, ob eine Zahl zwischen 50 und 100 liegt.

5.	Schreiben Sie ein Programm, das das Alter eines Benutzers abfragt und prüft, ob er Auto fahren darf

o	Ab 18: "Du darfst Auto fahren."
o	Unter 18, aber über 16: "Du darfst einen Führerschein machen."
o	Unter 16: "Du bist zu jung für den Führerschein."

6.	Schreiben Sie ein Programm, das zwei Zahlen abfragt und entscheidet

o	Ob die Zahlen gleich sind.
o	Welche der beiden Zahlen größer ist.
o	Ob die Summe der beiden Zahlen gerade oder ungerade ist.

Teil 5: Print-Ausgaben und Escape-Zeichen

Aufgabe 3: Grundlegende Print-Ausgabe

1.	Schreiben Sie ein Programm, das folgende Informationen ausgibt:

o	Ihren Namen.
o	Ihre Ausbildung.
o	Ein beliebiges Zitat.
o	Verwenden Sie Formatierung.

Aufgabe 4: Verwendung von Escape-Zeichen

1.	Nutzen Sie Escape-Zeichen, um folgende Ausgaben zu erzeugen:

o	Einen Tabulator 
o	Einen Zeilenumbruch

Teil 6: Input und Output

Aufgabe 5: Benutzereingabe

1.	Schreiben Sie ein Programm, das folgende Daten vom Benutzer abfragt:

o	Name
o	Alter
o	Beruf

2.	Geben Sie eine Begrüßungsnachricht basierend auf den Eingaben aus

Aufgabe 6: Eingaben validieren

1.	Schreiben Sie ein Programm, das eine Zahl vom Benutzer abfragt und überprüft, ob die Eingabe gültig ist:

o	Verwenden Sie isdigit(), um sicherzustellen, dass die Eingabe eine Zahl ist.
o	Falls die Eingabe ungültig ist, geben Sie eine Fehlermeldung aus.

Teil 7: Datentypen und Variablen

Aufgabe 7: Variablen mit verschiedenen Datentypen

1.	Erstellen Sie Variablen mit den folgenden Datentypen:

o	Ganze Zahl (int).
o	Gleitkommazahl (float).
o	Text (str).
o	Wahrheitswert (bool).

2.	Geben Sie die Variablen zusammen mit ihrem Datentyp aus.

Aufgabe 8: Typkonvertierung

1.	Schreiben Sie ein Programm, das eine Ganzzahl in eine Gleitkommazahl und einen String umwandelt.
2.	Geben Sie alle drei Versionen aus.

Teil 8: Exception Handling

Aufgabe 9: Grundlegende Fehlerbehandlung

1.	Schreiben Sie ein Programm, das eine Zahl vom Benutzer abfragt.
2.	Verwenden Sie try-except, um sicherzustellen,
3.	Schreiben Sie ein Programm, das den Benutzer auffordert, eine Zahl einzugeben, und basierend auf der Eingabe verschiedene Fehler behandelt:

•	Wenn die Eingabe keine Zahl ist, geben Sie eine Fehlermeldung aus.
•	Wenn die Zahl durch 0 geteilt wird, geben Sie eine Warnung aus.
•	Andernfalls geben Sie das Ergebnis der Division durch 2 aus.

4.	Schreiben Sie ein Programm, das eine Zahl prüft:

•	Wenn die Zahl negativ ist, soll ein benutzerdefinierter Fehler ausgelöst werden.
