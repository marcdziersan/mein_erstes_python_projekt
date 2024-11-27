import random

class ZahlRatenSpiel:
    def __init__(self):
        self.zufallszahl = random.randint(1, 20)
        self.versuche = 0
        self.spiel_läuft = True

    def benutzer_eingabe(self):
        while True:
            try:
                eingabe = input("Rate eine Zahl zwischen 1 und 20: ")
                if eingabe.lower() == 'exit':
                    print("Spiel beendet. Auf Wiedersehen!")
                    exit()
                eingabe = int(eingabe)
                if 1 <= eingabe <= 20:
                    return eingabe
                else:
                    print("Bitte eine Zahl zwischen 1 und 20 eingeben.")
            except ValueError:
                print("Ungültige Eingabe! Bitte eine ganze Zahl eingeben oder 'exit' zum Beenden.")

    def spiele_runde(self):
        while self.spiel_läuft:
            benutzer_zahl = self.benutzer_eingabe()
            self.versuche += 1
            if benutzer_zahl < self.zufallszahl:
                print("Zahl zu niedrig!")
            elif benutzer_zahl > self.zufallszahl:
                print("Zahl zu hoch!")
            else:
                print("Treffer, versenkt!")
                print(f"Du hast {self.versuche} Versuche gebraucht.")
                self.spiel_läuft = False

    def spielen(self):
        while True:
            self.spiele_runde()
            nochmal = input("Möchtest du nochmal spielen? (j/n): ").lower()
            if nochmal == 'j':
                self.__init__()
            else:
                print("Danke fürs Spielen! Auf Wiedersehen.")
                break

spiel = ZahlRatenSpiel()
spiel.spielen()
