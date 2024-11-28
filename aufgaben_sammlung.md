
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

---

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

---

Aufgabenblatt Teil 3 
Teil 1: Kopfgesteuerte Schleife (while-Schleife)
Aufgabe 1: Zahlen zählen
Schreiben Sie ein Programm, das die Zahlen von 1 bis 10 mit einer while-Schleife ausgibt.
Aufgabe 2: Benutzereingaben
Schreiben Sie ein Programm, das den Benutzer auffordert, eine Zahl einzugeben. Das Programm soll die Summe aller eingegebenen Zahlen berechnen, bis der Benutzer "0" eingibt:
Aufgabe 3: Passworteingabe
Schreiben Sie ein Programm, das den Benutzer wiederholt auffordert, ein Passwort einzugeben, bis er das richtige Passwort eingibt

Teil 2: For-Schleife
Aufgabe 4: Zahlenbereiche
Schreiben Sie ein Programm, das mit einer for-Schleife die Zahlen von 1 bis 10 ausgibt.
Aufgabe 5: Gerade Zahlen
Schreiben Sie ein Programm, das alle geraden Zahlen von 1 bis 20 ausgibt.
Schreiben sie ein Programm, das jede 5. Zahl der Liste ausgibt.
Aufgabe 6: Verschachtelte Schleifen
Schreiben Sie ein Programm, das ein Rechteck aus Sternen mit einer Größe von 5x5 ausgibt.
Aufgabe 7: Rückwärts iterieren
Schreiben Sie ein Programm, das die Zahlen von 10 bis 1 rückwärts ausgibt:


Teil 3: Listen und ihre Methoden
Aufgabe 8: Erstellen und Manipulieren von Listen
Erstellen Sie eine Liste mit den Namen "Anna", "Max", "Tom" und "Lisa". Führen Sie die folgenden Operationen aus:
o	Fügen Sie "Marie" hinzu.
o	Entfernen Sie "Tom".
o	Geben Sie die Länge der Liste aus.

Aufgabe 9: Sortieren und Umkehren
Erstellen Sie eine Liste mit den Zahlen [5, 3, 8, 1, 2]. Führen Sie die folgenden Operationen aus:
o	Sortieren Sie die Liste in aufsteigender Reihenfolge.
o	Sortieren Sie die Liste in absteigender Reihenfolge.
o	Kehren Sie die Reihenfolge der Elemente in der Liste um.

Aufgabe 10 Methoden für Listen
Erstellen Sie eine Liste mit den Elementen [1, 2, 3, 4, 5]. Verwenden Sie folgende Methoden:
o	Fügen Sie die Zahl 6 am Ende hinzu.
o	Fügen Sie die Zahl 0 an den Anfang der Liste ein.
o	Zählen Sie, wie oft die Zahl 3 in der Liste vorkommt.

Teil 4: For-Schleifen für Listen
Aufgabe 11: Iterieren über Listen
Schreiben Sie ein Programm, das eine Liste mit den Werten [10, 20, 30, 40, 50] durchläuft und jeden Wert ausgibt.
Aufgabe 12: Summieren von Elementen
Schreiben Sie ein Programm, das die Summe aller Elemente einer Liste berechnet.	
Aufgabe 13: Iteration über einen String
1.	Schreiben Sie ein Programm, das jeden Buchstaben eines Strings einzeln ausgibt:
Aufgabe 12: Filtern von Elementen
Schreiben Sie ein Programm, das alle Zahlen größer als 10 in einer Liste filtert und ausgibt.
Aufgabe 13: Indizes verwenden
Schreiben Sie ein Programm, das sowohl den Index als auch den Wert jeder Zahl in einer Liste ausgibt.
Aufgabe 14: Enumerate
Implementiere eine der Aufgaben aus Teil 4 nochmal  mit der Methode enumerate().

---

Aufgabenblatt: Python mit Datenbanken

Teil 1: Datenbank einrichten
Aufgabe 1: SQLite-Datenbank erstellen
1.	Erstellen Sie mit Python eine SQLite-Datenbank (sqlite3-Modul).
2.	Erstellen Sie eine Tabelle benutzer mit den folgenden Spalten:
o	id (INTEGER, Primärschlüssel, automatisch inkrementierend)
o	name (TEXT)
o	email (TEXT)
o	alter (INTEGER)
3.	Fügen Sie mindestens drei Datensätze ein.

Aufgabe 2: Daten aus der Datenbank lesen
1.	Schreiben Sie ein Python-Programm, das alle Benutzer aus der benutzer-Tabelle ausliest und ausgibt.

Teil 2: Aufgaben mit Datenbankinteraktion
Aufgabe 3: Benutzer hinzufügen
1.	Erstellen Sie ein Programm, das den Benutzer nach name, email und alter fragt und diese Informationen in die benutzer-Tabelle einfügt.
Aufgabe 4: Benutzer aktualisieren
1.	Erstellen Sie ein Programm, das die E-Mail eines Benutzers aktualisiert.
o	Der Benutzer gibt die id des Benutzers ein, dessen E-Mail geändert werden soll.
o	Danach gibt der Benutzer die neue E-Mail ein.

Teil 3: Datenbankabfragen und Analysen
Aufgabe 5: Benutzer nach Alter filtern
1.	Schreiben Sie ein Programm, das alle Benutzer aus der Datenbank ausgibt, deren Alter größer als 25 ist.
Aufgabe 6: Benutzer suchen
1.	Erstellen Sie ein Programm, das nach einem Benutzer basierend auf seinem Namen sucht und die Informationen ausgibt.

Teil 4: Integration in Python-Anwendungen
Aufgabe 7: To-Do-Liste mit Datenbank
1.	Erstellen Sie eine To-Do-Listen-Anwendung, die Daten in einer SQLite-Datenbank speichert.
2.	Funktionen:
o	Aufgabe hinzufügen (INSERT INTO aufgaben (titel, status) VALUES (?, ?)).
o	Alle Aufgaben anzeigen (SELECT * FROM aufgaben).
o	Aufgabe als erledigt markieren (UPDATE aufgaben SET status = 'erledigt' WHERE id = ?).
o	Aufgabe löschen (DELETE FROM aufgaben WHERE id = ?).
Aufgabe 8: Benutzerregistrierungssystem
1.	Erstellen Sie ein Benutzerregistrierungssystem mit folgenden Funktionen:
o	Benutzer registrieren (name, email, passwort in die Datenbank einfügen).
o	Benutzer-Login:
	Überprüfen Sie, ob email und passwort korrekt sind.
o	Anzeigen aller registrierten Benutzer.

---

Python Projekte

Projekt 1: Taschenrechner
Erstellen Sie ein Programm, das die grundlegenden Rechenoperationen durchführt und einen benutzerfreundlichen Taschenrechner simuliert.
Anforderungen:
1.	Zeigen Sie ein Menü mit den Optionen:
o	Addition
o	Subtraktion
o	Multiplikation
o	Division
o	Beenden
2.	Der Benutzer wählt eine Option.
3.	Fragen Sie den Benutzer nach zwei Zahlen.
4.	Führen Sie die ausgewählte Operation durch und geben Sie das Ergebnis aus.
5.	Fehlerbehandlung:
o	Verhindern Sie Division durch Null.
o	Fangen Sie ungültige Eingaben ab (z. B. Buchstaben statt Zahlen).
6.	Wiederholen Sie das Menü, bis der Benutzer "Beenden" auswählt.
Erweiterung:
•	Implementieren Sie erweiterte Funktionen wie Potenzieren, Quadratwurzel und Prozentrechnung.
•	Speichern Sie alle Berechnungen in einer Liste und zeigen Sie eine Historie an.

Projekt 2: To-Do-Listen-Anwendung
Erstellen Sie ein Programm, mit dem der Benutzer Aufgaben verwalten kann. Die Anwendung sollte Aufgaben hinzufügen, anzeigen, bearbeiten und löschen können.
Anforderungen:
1.	Erstellen Sie ein Menü mit den Optionen:
o	Aufgabe hinzufügen
o	Alle Aufgaben anzeigen
o	Aufgabe bearbeiten
o	Aufgabe löschen
o	Beenden
2.	Speichern Sie die Aufgaben in einer Liste.
3.	Beim Bearbeiten oder Löschen einer Aufgabe:
o	Zeigen Sie alle Aufgaben mit Indexnummern an, damit der Benutzer die gewünschte Aufgabe auswählen kann.
4.	Speichern Sie die Aufgaben persistent in einer Datei (todo.txt) und laden Sie sie beim Start des Programms.
5.	Fangen Sie alle möglichen Fehler ab, z. B.:
o	Ungültige Eingaben.
o	Auswahl eines Indexes, der nicht existiert.
Erweiterung:
•	Fügen Sie ein Fälligkeitsdatum für Aufgaben hinzu.
•	Implementieren Sie eine Suchfunktion, um Aufgaben anhand von Stichwörtern zu finden.

Projekt 3: Quiz-Spiel
Erstellen Sie ein interaktives Quiz-Spiel, bei dem der Benutzer Fragen beantwortet und Punkte basierend auf den richtigen Antworten erhält.
Anforderungen:
1.	Definieren Sie eine Liste von mindestens 10 Fragen, jede mit:
o	Einer Frage.
o	Vier Antwortmöglichkeiten.
o	Der richtigen Antwort.
2.	Stellen Sie dem Benutzer nacheinander Fragen.
3.	Lassen Sie den Benutzer eine Antwort auswählen.
4.	Geben Sie Feedback, ob die Antwort richtig oder falsch war.
5.	Am Ende zeigen Sie die Gesamtpunktzahl an.
Erweiterung:
•	Speichern Sie Highscores in einer Datei und zeigen Sie die Bestenliste an.
•	Fügen Sie Schwierigkeitsgrade hinzu (z. B. leichte, mittlere und schwere Fragen).

Projekt 4: Mini-Bibliotheksverwaltung
Erstellen Sie ein Programm, mit dem Bücher in einer Bibliothek verwaltet werden können.
Anforderungen:
1.	Erstellen Sie ein Menü mit folgenden Funktionen:
o	Buch hinzufügen.
o	Buch ausleihen.
o	Buch zurückgeben.
o	Alle verfügbaren Bücher anzeigen.
o	Alle ausgeliehenen Bücher anzeigen.
o	Beenden.
2.	Speichern Sie die Bücher in einer Liste oder einem Dictionary.
3.	Beim Hinzufügen eines Buches:
o	Geben Sie den Titel und den Autor an.
4.	Beim Ausleihen eines Buches:
o	Überprüfen Sie, ob das Buch verfügbar ist.
o	Verschieben Sie das Buch in eine separate Liste für ausgeliehene Bücher.
5.	Fehlerbehandlung:
o	Fangen Sie ungültige Eingaben ab.
o	Zeigen Sie eine Fehlermeldung, wenn ein nicht verfügbares Buch ausgeliehen werden soll.
Erweiterung:
•	Speichern Sie die Buchdaten persistent in einer Datei.
•	Implementieren Sie eine Suchfunktion, um Bücher nach Titel oder Autor zu finden.

Projekt 5: Passwort-Manager
Erstellen Sie einen Passwort-Manager, der Anmeldedaten für verschiedene Dienste sicher speichert.
Anforderungen:
1.	Zeigen Sie ein Menü mit den Optionen:
o	Passwort speichern.
o	Passwörter anzeigen.
o	Passwort suchen.
o	Beenden.
2.	Speichern Sie Anmeldedaten (Dienst, Benutzername, Passwort) in einer Datei (passwoerter.txt).
3.	Beim Speichern eines Passworts:
o	Überprüfen Sie, ob der Dienst bereits existiert.
4.	Beim Anzeigen der Passwörter:
o	Zeigen Sie alle gespeicherten Anmeldedaten an.
5.	Beim Suchen eines Passworts:
o	Finden Sie den entsprechenden Dienst und geben Sie die Daten aus.
Erweiterung:
•	Verschlüsseln Sie die gespeicherten Passwörter mit einer Bibliothek wie cryptography oder hashlib.
•	Implementieren Sie eine Passwortgeneratorfunktion.

Projekt 6: Hangman-Spiel
Erstellen Sie ein Text-basiertes Hangman-Spiel, bei dem der Benutzer ein Wort erraten muss.
Anforderungen:
1.	Definieren Sie eine Liste von Wörtern, aus denen ein Wort zufällig ausgewählt wird.
2.	Zeigen Sie dem Benutzer eine Reihe von Unterstrichen an, die die Buchstaben des Wortes repräsentieren.
3.	Lassen Sie den Benutzer Buchstaben raten.
4.	Aktualisieren Sie den Stand nach jedem Versuch:
o	Fügen Sie den Buchstaben hinzu, wenn er korrekt ist.
o	Ziehen Sie einen Versuch ab, wenn er falsch ist.
5.	Zeigen Sie nach jedem Versuch die aktuelle Darstellung des Wortes und die verbleibenden Versuche an.
6.	Das Spiel endet, wenn:
o	Der Benutzer das Wort errät (gewonnen).
o	Die Versuche aufgebraucht sind (verloren).
Erweiterung:
•	Speichern Sie eine Bestenliste mit der Anzahl der Versuche in einer Datei.
•	Fügen Sie einen Mehrspielermodus hinzu.

Projekt 7: Wetter-Statistik-Tool
Erstellen Sie ein Programm, das Wetterdaten analysiert und Statistiken berechnet.
Anforderungen:
1.	Laden Sie Wetterdaten (z. B. Temperatur, Niederschlag, Windgeschwindigkeit) aus einer Datei (wetterdaten.csv).
2.	Zeigen Sie ein Menü mit folgenden Optionen:
o	Durchschnittstemperatur berechnen.
o	Höchste und niedrigste Temperatur anzeigen.
o	Tage mit Niederschlag anzeigen.
o	Wetterdaten für einen bestimmten Tag anzeigen.
o	Beenden.
3.	Implementieren Sie Funktionen für jede Option.
4.	Fehlerbehandlung:
o	Fangen Sie ungültige Eingaben ab.
o	Zeigen Sie eine Fehlermeldung, wenn ein nicht existierender Tag abgefragt wird.
Erweiterung:
•	Visualisieren Sie die Wetterdaten mit einer Bibliothek wie matplotlib.
•	Erstellen Sie Vorhersagen basierend auf den Durchschnittsdaten.

Projekt 8: Schere-Stein-Papier
Erstellen Sie ein interaktives Spiel "Schere-Stein-Papier".
Anforderungen:
1.	Der Benutzer wählt Schere, Stein oder Papier.
2.	Der Computer trifft eine zufällige Wahl.
3.	Bestimmen Sie den Gewinner anhand der Regeln:
o	Schere schlägt Papier.
o	Papier schlägt Stein.
o	Stein schlägt Schere.
4.	Zeigen Sie das Ergebnis und aktualisieren Sie die Punkte für den Benutzer und den Computer.
5.	Lassen Sie den Benutzer entscheiden, ob er eine weitere Runde spielen möchte.
Erweiterung:
•	Implementieren Sie eine Statistikfunktion, die die Siege, Niederlagen und Unentschieden anzeigt.
•	Fügen Sie eine Mehrspielerversion hinzu.

