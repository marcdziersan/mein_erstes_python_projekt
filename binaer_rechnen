# Funktion: Umwandlung von Binär in Dezimal
def binär_zu_dezimal(binär):
    return int(binär, 2)

# Funktion: Umwandlung von Dezimal in Binär
def dezimal_zu_binär(dezimal):
    return bin(dezimal)[2:]

# Funktion: Binärzahlen addieren
def addiere_binär(bin1, bin2):
    dezimal1 = binär_zu_dezimal(bin1)
    dezimal2 = binär_zu_dezimal(bin2)
    summe = dezimal1 + dezimal2
    return dezimal_zu_binär(summe)

# Funktion: Binärzahlen subtrahieren
def subtrahiere_binär(bin1, bin2):
    dezimal1 = binär_zu_dezimal(bin1)
    dezimal2 = binär_zu_dezimal(bin2)
    differenz = dezimal1 - dezimal2
    return dezimal_zu_binär(differenz)

# Funktion: Binärzahlen multiplizieren
def multipliziere_binär(bin1, bin2):
    dezimal1 = binär_zu_dezimal(bin1)
    dezimal2 = binär_zu_dezimal(bin2)
    produkt = dezimal1 * dezimal2
    return dezimal_zu_binär(produkt)

# Funktion: Binärzahlen dividieren
def dividiere_binär(bin1, bin2):
    dezimal1 = binär_zu_dezimal(bin1)
    dezimal2 = binär_zu_dezimal(bin2)
    if dezimal2 != 0:
        quotient = dezimal1 // dezimal2
        return dezimal_zu_binär(quotient)
    else:
        return "Division durch Null"

# Funktion: Bitweise Operationen
def bitweise_operationen(a, b):
    and_result = a & b
    or_result = a | b
    xor_result = a ^ b
    not_result = ~a & 0b1111  # Maskieren, um die Ausgabe zu begrenzen
    shift_left = a << 2
    shift_right = a >> 2

    return {
        "AND": bin(and_result)[2:],
        "OR": bin(or_result)[2:],
        "XOR": bin(xor_result)[2:],
        "NOT": bin(not_result)[2:],
        "Shift Left": bin(shift_left)[2:],
        "Shift Right": bin(shift_right)[2:]
    }

# Hauptprogramm
if __name__ == "__main__":
    # Umwandlung von Binär in Dezimal
    binär = '1011'
    dezimal = binär_zu_dezimal(binär)
    print(f"Binär: {binär} -> Dezimal: {dezimal}")

    # Umwandlung von Dezimal in Binär
    dezimal = 11
    binär = dezimal_zu_binär(dezimal)
    print(f"Dezimal: {dezimal} -> Binär: {binär}")

    # Rechnen mit Binärzahlen (Addition, Subtraktion, Multiplikation, Division)
    bin1 = '1010'  # Binärzahl 10
    bin2 = '1101'  # Binärzahl 13

    summe = addiere_binär(bin1, bin2)
    differenz = subtrahiere_binär(bin1, bin2)
    produkt = multipliziere_binär(bin1, bin2)
    quotient = dividiere_binär(bin1, bin2)

    print(f"{bin1} + {bin2} = {summe}")
    print(f"{bin1} - {bin2} = {differenz}")
    print(f"{bin1} * {bin2} = {produkt}")
    print(f"{bin1} / {bin2} = {quotient}")

    # Bitweise Operationen
    a = 0b1010  # Binärzahl 10
    b = 0b1100  # Binärzahl 12

    operationen = bitweise_operationen(a, b)
    print("\nBitweise Operationen:")
    for op, result in operationen.items():
        print(f"{op}: {result}")
