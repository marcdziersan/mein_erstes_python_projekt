class Himmelskörper:
    def __init__(self, name, masse):
        """
        Konstruktor der Klasse Himmelskörper.
        :param name: Der Name des Himmelskörpers (z.B. Sonne, Merkur).
        :param masse: Die Masse des Himmelskörpers in Kilogramm.
        """
        self.name = name    # Setzt den Namen des Himmelskörpers
        self.masse = masse  # Setzt die Masse des Himmelskörpers

    def schwarzschildradius(self):
        """
        Berechnet den Schwarzschildradius des Himmelskörpers in Metern.
        Der Schwarzschildradius ist der Radius einer Kugel, der die Gravitationskraft
        so stark macht, dass nicht einmal Licht entkommen kann.
        :return: Der Schwarzschildradius in Metern.
        """
        G = 6.674 * 10**-11  # Gravitationskonstante in m^3 kg^-1 s^-2
        c = 3 * 10**8        # Lichtgeschwindigkeit in m/s
        r_s = (2 * G * self.masse) / (c**2)  # Berechnung des Schwarzschildradius in Metern
        return r_s

# Definition der Himmelskörper mit ihren Massen in Kilogramm
himmelskörper_liste = [
    Himmelskörper('Sonne', 1.989 * 10**30),
    Himmelskörper('Merkur', 3.301 * 10**23),
    Himmelskörper('Venus', 4.867 * 10**24),
    Himmelskörper('Erde', 5.972 * 10**24),
    Himmelskörper('Mars', 6.417 * 10**23),
    Himmelskörper('Jupiter', 1.898 * 10**27),
    Himmelskörper('Saturn', 5.683 * 10**26),
    Himmelskörper('Uranus', 8.681 * 10**25),
    Himmelskörper('Neptun', 1.024 * 10**26),
    Himmelskörper('Pluto', 1.309 * 10**22),
]

def berechne_schwarzschildradius():
    """
    Führt die Benutzerinteraktion zur Berechnung des Schwarzschildradius durch.
    Der Benutzer kann einen Himmelskörper auswählen oder seine eigene Masse eingeben.
    """
    print("Wählen Sie einen Himmelskörper aus oder geben Sie Ihre eigene Masse ein:")
    print("1. Himmelskörper auswählen")  # Option 1: Auswahl eines Himmelskörpers
    print("2. Eigene Masse in kg eingeben")  # Option 2: Eigene Masse eingeben

    wahl = input("Geben Sie '1' oder '2' ein: ")  # Benutzerwahl

    if wahl == '1':  # Wenn der Benutzer die erste Option wählt
        print("Himmelskörper zur Auswahl:")
        for körper in himmelskörper_liste:
            print(f"- {körper.name}")  # Zeigt die Namen der verfügbaren Himmelskörper an
        
        körper_wahl = input("Geben Sie den Namen des Himmelskörpers ein: ")  # Benutzer gibt einen Himmelskörper ein

        # Überprüfen, ob die Wahl gültig ist
        for körper in himmelskörper_liste:
            if körper.name.lower() == körper_wahl.lower():  # Vergleich der Namen (ignoriert Groß-/Kleinschreibung)
                radius_meter = körper.schwarzschildradius()  # Berechnung des Schwarzschildradius in Metern
                radius_km = radius_meter / 1000  # Umrechnung in Kilometer
                
                # Ausgabe sowohl im wissenschaftlichen Format als auch als volle Zahl in Metern und Kilometern
                print(f"Der Schwarzschildradius für {körper.name} ist: {radius_meter:.2e} Meter (wissenschaftliche Notation)")
                print(f"Der Schwarzschildradius für {körper.name} ist: {radius_meter} Meter (volle Zahl)")
                # print(f"Der Schwarzschildradius für {körper.name} ist: {radius_km:.2e} Kilometer (wissenschaftliche Notation)")
                # print(f"Der Schwarzschildradius für {körper.name} ist: {radius_km} Kilometer (volle Zahl)")
                return  # Funktion verlassen, nachdem das Ergebnis ausgegeben wurde
        
        print("Ungültige Eingabe. Bitte wählen Sie einen der angezeigten Himmelskörper.")  # Fehlernachricht

    elif wahl == '2':  # Wenn der Benutzer die zweite Option wählt
        try:
            eigene_masse = float(input("Geben Sie Ihre Masse in kg ein: "))  # Benutzer gibt seine Masse ein
            if eigene_masse > 0:  # Überprüfen, ob die Masse positiv ist
                benutzer_himmelskörper = Himmelskörper('Benutzer', eigene_masse)  # Erstellung eines Himmelskörpers für den Benutzer
                radius_meter = benutzer_himmelskörper.schwarzschildradius()  # Berechnung des Schwarzschildradius in Metern
                radius_km = radius_meter / 1000  # Umrechnung in Kilometer
                
                # Ausgabe sowohl im wissenschaftlichen Format als auch als volle Zahl in Metern und Kilometern
                print(f"Der Schwarzschildradius für Ihre Masse ({eigene_masse} kg) ist: {radius_meter:.2e} Meter (wissenschaftliche Notation)")
                print(f"Der Schwarzschildradius für Ihre Masse ({eigene_masse} kg) ist: {radius_meter} Meter (volle Zahl)")
                # print(f"Der Schwarzschildradius für Ihre Masse ({eigene_masse} kg) ist: {radius_km:.2e} Kilometer (wissenschaftliche Notation)")
                # print(f"Der Schwarzschildradius für Ihre Masse ({eigene_masse} kg) ist: {radius_km} Kilometer (volle Zahl)")
            else:
                print("Bitte geben Sie eine positive Masse ein.")  # Fehlernachricht für ungültige Masse
        except ValueError:  # Fehlerbehandlung für ungültige Eingaben (nicht konvertierbar in float)
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")  # Fehlernachricht
    else:  # Wenn die Wahl ungültig ist
        print("Ungültige Eingabe. Bitte wählen Sie '1' oder '2'.")  # Fehlernachricht

# Hauptprogramm
if __name__ == "__main__":
    berechne_schwarzschildradius()  # Startet die Berechnung des Schwarzschildradius
