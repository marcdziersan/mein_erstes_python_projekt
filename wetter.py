import csv
from datetime import datetime
import matplotlib.pyplot as plt

class WeatherData:
    def __init__(self, filename="wetterdaten.csv"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                data = [
                    {
                        "date": datetime.strptime(row["Date"], "%Y-%m-%d"),
                        "temperature": float(row["Temperature"]),
                        "precipitation": float(row["Precipitation"]),
                        "wind_speed": float(row["WindSpeed"]),
                    }
                    for row in reader
                ]
            return data
        except FileNotFoundError:
            print(f"Fehler: Datei '{self.filename}' nicht gefunden.")
            return []
        except ValueError as e:
            print(f"Fehler beim Laden der Daten: {e}")
            return []

    def calculate_average_temperature(self):
        temperatures = [entry["temperature"] for entry in self.data]
        if temperatures:
            return sum(temperatures) / len(temperatures)
        return None

    def find_highest_and_lowest_temperature(self):
        if not self.data:
            return None, None
        highest = max(self.data, key=lambda x: x["temperature"])
        lowest = min(self.data, key=lambda x: x["temperature"])
        return highest, lowest

    def get_days_with_precipitation(self):
        return [entry for entry in self.data if entry["precipitation"] > 0]

    def get_weather_for_date(self, date_str):
        try:
            query_date = datetime.strptime(date_str, "%Y-%m-%d")
            for entry in self.data:
                if entry["date"] == query_date:
                    return entry
            return None
        except ValueError:
            print("Ungültiges Datum. Bitte verwenden Sie das Format 'YYYY-MM-DD'.")
            return None

    def plot_weather_data(self):
        if not self.data:
            print("Keine Daten zum Plotten verfügbar.")
            return
        dates = [entry["date"] for entry in self.data]
        temperatures = [entry["temperature"] for entry in self.data]
        precipitation = [entry["precipitation"] for entry in self.data]

        plt.figure(figsize=(10, 5))
        plt.plot(dates, temperatures, label="Temperatur (°C)", color="r")
        plt.bar(dates, precipitation, label="Niederschlag (mm)", alpha=0.5)
        plt.xlabel("Datum")
        plt.ylabel("Wert")
        plt.title("Wetterdaten")
        plt.legend()
        plt.tight_layout()
        plt.show()

class WeatherApp:
    def __init__(self):
        self.weather_data = WeatherData()

    def menu(self):
        while True:
            print("\n--- Wetter-Statistik-Tool ---")
            print("1. Durchschnittstemperatur berechnen")
            print("2. Höchste und niedrigste Temperatur anzeigen")
            print("3. Tage mit Niederschlag anzeigen")
            print("4. Wetterdaten für einen bestimmten Tag anzeigen")
            print("5. Wetterdaten visualisieren")
            print("6. Beenden")

            try:
                choice = int(input("Wählen Sie eine Option (1-6): "))
                if choice == 1:
                    self.average_temperature()
                elif choice == 2:
                    self.highest_and_lowest_temperature()
                elif choice == 3:
                    self.days_with_precipitation()
                elif choice == 4:
                    self.weather_for_date()
                elif choice == 5:
                    self.visualize_data()
                elif choice == 6:
                    print("Programm beendet. Auf Wiedersehen!")
                    break
                else:
                    print("Ungültige Option. Bitte wählen Sie eine Zahl zwischen 1 und 6.")
            except ValueError:
                print("Ungültige Eingabe. Bitte wählen Sie eine Zahl.")

    def average_temperature(self):
        avg_temp = self.weather_data.calculate_average_temperature()
        if avg_temp is not None:
            print(f"Die Durchschnittstemperatur beträgt {avg_temp:.2f}°C.")
        else:
            print("Keine Daten verfügbar.")

    def highest_and_lowest_temperature(self):
        highest, lowest = self.weather_data.find_highest_and_lowest_temperature()
        if highest and lowest:
            print(f"Höchste Temperatur: {highest['temperature']}°C am {highest['date'].strftime('%Y-%m-%d')}")
            print(f"Niedrigste Temperatur: {lowest['temperature']}°C am {lowest['date'].strftime('%Y-%m-%d')}")
        else:
            print("Keine Daten verfügbar.")

    def days_with_precipitation(self):
        days = self.weather_data.get_days_with_precipitation()
        if days:
            print("Tage mit Niederschlag:")
            for day in days:
                print(f"{day['date'].strftime('%Y-%m-%d')}: {day['precipitation']} mm")
        else:
            print("Keine Tage mit Niederschlag gefunden.")

    def weather_for_date(self):
        date_str = input("Geben Sie ein Datum im Format YYYY-MM-DD ein: ")
        weather = self.weather_data.get_weather_for_date(date_str)
        if weather:
            print(f"Wetterdaten für {date_str}:")
            print(f"  Temperatur: {weather['temperature']}°C")
            print(f"  Niederschlag: {weather['precipitation']} mm")
            print(f"  Windgeschwindigkeit: {weather['wind_speed']} km/h")
        else:
            print(f"Keine Daten für das Datum {date_str} gefunden.")

    def visualize_data(self):
        self.weather_data.plot_weather_data()

# Anwendung starten
if __name__ == "__main__":
    app = WeatherApp()
    app.menu()
