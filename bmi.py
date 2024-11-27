def berechne_bmi(gewicht, groesse):
    # BMI-Formel: BMI = Gewicht in kg / (Größe in m)²
    bmi = gewicht / (groesse ** 2)
    return bmi

def bmi_kategorie(bmi):
    if bmi < 16.5:
        return "Stark untergewichtig"
    elif 16.5 <= bmi < 17:
        return "Mäßig untergewichtig"
    elif 17 <= bmi < 18.5:
        return "Leicht untergewichtig"
    elif 18.5 <= bmi < 24.9:
        return "Normalgewichtig"
    elif 25 <= bmi < 29.9:
        return "Übergewichtig"
    elif 30 <= bmi < 34.9:
        return "Adipositas Grad 1 (mäßig)"
    elif 35 <= bmi < 39.9:
        return "Adipositas Grad 2 (sehr mäßig)"
    else:
        return "Adipositas Grad 3 (sehr stark)"

def main():
    # Eingabe der Werte
    gewicht = float(input("Gib dein Gewicht in kg ein: "))
    groesse = float(input("Gib deine Größe in Metern ein (z.B. 1.75): "))
    
    # Berechnung des BMI
    bmi = berechne_bmi(gewicht, groesse)
    
    # Ausgabe des BMI
    print(f"Dein BMI ist: {bmi:.2f}")
    
    # Ausgabe der Kategorie
    kategorie = bmi_kategorie(bmi)
    print(f"Du liegst in der Kategorie: {kategorie}")

if __name__ == "__main__":
    main()
