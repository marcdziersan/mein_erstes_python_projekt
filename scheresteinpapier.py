import random

class RockPaperScissorsGame:
    OPTIONS = ["Schere", "Stein", "Papier"]

    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.draws = 0

    def get_computer_choice(self):
        return random.choice(self.OPTIONS)

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            self.draws += 1
            return "Unentschieden"
        elif (
            (player_choice == "Schere" and computer_choice == "Papier") or
            (player_choice == "Stein" and computer_choice == "Schere") or
            (player_choice == "Papier" and computer_choice == "Stein")
        ):
            self.player_score += 1
            return "Spieler gewinnt"
        else:
            self.computer_score += 1
            return "Computer gewinnt"

    def show_statistics(self):
        print("\n--- Statistik ---")
        print(f"Spieler: {self.player_score} Siege")
        print(f"Computer: {self.computer_score} Siege")
        print(f"Unentschieden: {self.draws}")

    def play_round(self):
        print("\n--- Neue Runde ---")
        print("Optionen: Schere, Stein, Papier")
        player_choice = input("Treffen Sie Ihre Wahl: ").capitalize()

        if player_choice not in self.OPTIONS:
            print("Ungültige Wahl. Bitte wählen Sie Schere, Stein oder Papier.")
            return

        computer_choice = self.get_computer_choice()
        print(f"Computer wählt: {computer_choice}")

        result = self.determine_winner(player_choice, computer_choice)
        print(f"Ergebnis: {result}")

    def play(self):
        print("Willkommen zu Schere-Stein-Papier!")
        while True:
            self.play_round()
            again = input("Möchten Sie eine weitere Runde spielen? (ja/nein): ").lower()
            if again != "ja":
                break
        print("\nSpiel beendet!")
        self.show_statistics()


# Anwendung starten
if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.play()
