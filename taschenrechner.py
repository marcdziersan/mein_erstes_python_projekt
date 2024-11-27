import math

class Calculator:
    def __init__(self):
        self.history = []  # Liste zur Speicherung der Berechnungshistorie

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Division durch Null ist nicht erlaubt.")
        return num1 / num2

    def power(self, base, exponent):
        return base ** exponent

    def sqrt(self, num):
        if num < 0:
            raise ValueError("Quadratwurzel von negativen Zahlen ist nicht definiert.")
        return math.sqrt(num)

    def percentage(self, base, percent):
        return (base * percent) / 100

    def save_to_history(self, operation):
        self.history.append(operation)

    def show_history(self):
        if not self.history:
            print("Keine Berechnungen in der Historie.")
        else:
            print("\n--- Historie ---")
            for entry in self.history:
                print(entry)

class CalculatorApp:
    def __init__(self):
        self.calculator = Calculator()

    def get_numbers(self, single_input=False):
        try:
            if single_input:
                num = float(input("Geben Sie eine Zahl ein: "))
                return num
            else:
                num1 = float(input("Geben Sie die erste Zahl ein: "))
                num2 = float(input("Geben Sie die zweite Zahl ein: "))
                return num1, num2
        except ValueError:
            print("Ungültige Eingabe! Bitte geben Sie Zahlen ein.")
            return None

    def menu(self):
        while True:
            print("\n--- Python Taschenrechner ---")
            print("1. Addition")
            print("2. Subtraktion")
            print("3. Multiplikation")
            print("4. Division")
            print("5. Potenzieren")
            print("6. Quadratwurzel")
            print("7. Prozentrechnung")
            print("8. Historie anzeigen")
            print("9. Beenden")

            try:
                choice = int(input("Wählen Sie eine Option (1-9): "))
            except ValueError:
                print("Ungültige Eingabe! Bitte wählen Sie eine Zahl.")
                continue

            if choice == 9:
                print("Programm beendet. Auf Wiedersehen!")
                break

            self.handle_choice(choice)

    def handle_choice(self, choice):
        if choice == 6:  # Quadratwurzel
            num = self.get_numbers(single_input=True)
            if num is not None:
                try:
                    result = self.calculator.sqrt(num)
                    print(f"Die Quadratwurzel von {num} ist {result}")
                    self.calculator.save_to_history(f"Quadratwurzel({num}) = {result}")
                except ValueError as e:
                    print(e)
        elif choice == 7:  # Prozentrechnung
            nums = self.get_numbers()
            if nums:
                base, percent = nums
                result = self.calculator.percentage(base, percent)
                print(f"{percent}% von {base} ist {result}")
                self.calculator.save_to_history(f"{percent}% von {base} = {result}")
        elif choice == 8:  # Historie anzeigen
            self.calculator.show_history()
        elif choice in [1, 2, 3, 4, 5]:  # Grundoperationen und Potenzieren
            nums = self.get_numbers()
            if nums:
                num1, num2 = nums
                try:
                    if choice == 1:
                        result = self.calculator.add(num1, num2)
                        operation = f"{num1} + {num2} = {result}"
                    elif choice == 2:
                        result = self.calculator.subtract(num1, num2)
                        operation = f"{num1} - {num2} = {result}"
                    elif choice == 3:
                        result = self.calculator.multiply(num1, num2)
                        operation = f"{num1} * {num2} = {result}"
                    elif choice == 4:
                        result = self.calculator.divide(num1, num2)
                        operation = f"{num1} / {num2} = {result}"
                    elif choice == 5:
                        result = self.calculator.power(num1, num2)
                        operation = f"{num1} ^ {num2} = {result}"

                    print(operation)
                    self.calculator.save_to_history(operation)
                except ValueError as e:
                    print(e)
        else:
            print("Ungültige Option! Bitte wählen Sie eine Zahl zwischen 1 und 9.")

# Programm starten
if __name__ == "__main__":
    app = CalculatorApp()
    app.menu()
