class Luftfahrzeug:
    def __init__(self):
        self.bezeichnung = "unbekannt"
        self.gewicht = 0.0
        self.baujahr = 0

    def get_bezeichnung(self):
        return self.bezeichnung

    def set_bezeichnung(self, bezeichnung):
        self.bezeichnung = bezeichnung

    def get_gewicht(self):
        return self.gewicht

    def set_gewicht(self, gewicht):
        self.gewicht = gewicht

    def get_baujahr(self):
        return self.baujahr

    def set_baujahr(self, baujahr):
        self.baujahr = baujahr

    def get_daten(self):
        return (
            f"Bezeichnung: {self.bezeichnung}\n"
            f"Gewicht: {self.gewicht} kg\n"
            f"Baujahr: {self.baujahr}"
        )


class Flugzeug(Luftfahrzeug):
    def __init__(self):
        super().__init__()
        self.spannweite = 0.0
        self.motoren_anzahl = 0

    def get_spannweite(self):
        return self.spannweite

    def set_spannweite(self, spannweite):
        self.spannweite = spannweite

    def get_motoren_anzahl(self):
        return self.motoren_anzahl

    def set_motoren_anzahl(self, motoren_anzahl):
        self.motoren_anzahl = motoren_anzahl

    def get_daten(self):
        base_daten = super().get_daten()
        return (
            base_daten + "\n" +
            f"Spannweite: {self.spannweite} m\n"
            f"Motorenanzahl: {self.motoren_anzahl}"
        )


class Heissluftballon(Luftfahrzeug):
    def __init__(self):
        super().__init__()
        self.ballon_volumen = 0.0
        self.korbhöhe = 0.0

    def get_ballon_volumen(self):
        return self.ballon_volumen

    def set_ballon_volumen(self, ballon_volumen):
        self.ballon_volumen = ballon_volumen

    def get_korbhöhe(self):
        return self.korbhöhe

    def set_korbhöhe(self, korbhöhe):
        self.korbhöhe = korbhöhe

    def get_daten(self):
        base_daten = super().get_daten()
        return (
            base_daten + "\n" +
            f"Ballonvolumen: {self.ballon_volumen} m³\n"
            f"Korbhöhe: {self.korbhöhe} m"
        )


# Hauptprogramm
if __name__ == "__main__":
    # Luftfahrzeug
    luftfahrzeug = Luftfahrzeug()
    luftfahrzeug.set_bezeichnung("A310")
    luftfahrzeug.set_gewicht(71840)
    luftfahrzeug.set_baujahr(1995)
    print("Luftfahrzeug:")
    print(luftfahrzeug.get_daten())
    print()

    # Flugzeug
    flugzeug = Flugzeug()
    flugzeug.set_bezeichnung("Boeing 747")
    flugzeug.set_gewicht(183500)
    flugzeug.set_baujahr(1969)
    flugzeug.set_spannweite(59.6)
    flugzeug.set_motoren_anzahl(4)
    print("Flugzeug:")
    print(flugzeug.get_daten())
    print()

    # Heißluftballon
    heissluftballon = Heissluftballon()
    heissluftballon.set_bezeichnung("Luftikus")
    heissluftballon.set_gewicht(350)
    heissluftballon.set_baujahr(2020)
    heissluftballon.set_ballon_volumen(3000)
    heissluftballon.set_korbhöhe(1.5)
    print("Heißluftballon:")
    print(heissluftballon.get_daten())
