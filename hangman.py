import random
import os

class Hangman:
    def __init__(self, word_list=None, max_attempts=6):
        self.word_list = word_list or ["python", "programming", "hangman", "challenge", "oop", "developer"]
        self.max_attempts = max_attempts
        self.word_to_guess = ""
        self.guessed_letters = []
        self.remaining_attempts = max_attempts
        self.correct_guesses = []

    def choose_word(self):
        self.word_to_guess = random.choice(self.word_list).lower()
        self.correct_guesses = ["_"] * len(self.word_to_guess)
        self.remaining_attempts = self.max_attempts
        self.guessed_letters = []

    def guess_letter(self, letter):
        letter = letter.lower()
        if letter in self.guessed_letters:
            print(f"Der Buchstabe '{letter}' wurde bereits geraten.")
            return False

        self.guessed_letters.append(letter)

        if letter in self.word_to_guess:
            for i, char in enumerate(self.word_to_guess):
                if char == letter:
                    self.correct_guesses[i] = letter
            print(f"Richtig! Der Buchstabe '{letter}' ist im Wort.")
            return True
        else:
            self.remaining_attempts -= 1
            print(f"Falsch! Der Buchstabe '{letter}' ist nicht im Wort.")
            return False

    def is_word_guessed(self):
        return "_" not in self.correct_guesses

    def display_status(self):
        print("\nAktueller Stand des Wortes: " + " ".join(self.correct_guesses))
        print(f"Verbleibende Versuche: {self.remaining_attempts}")
        print(f"Geratene Buchstaben: {', '.join(self.guessed_letters)}")

class Scoreboard:
    def __init__(self, filename="scoreboard.txt"):
        self.filename = filename

    def load_scores(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as file:
            scores = [line.strip().split("|") for line in file.readlines()]
        return [(name, int(score)) for name, score in scores]

    def save_score(self, name, attempts_left):
        scores = self.load_scores()
        scores.append((name, attempts_left))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)[:10]  # Top 10
        with open(self.filename, "w") as file:
            for name, score in scores:
                file.write(f"{name}|{score}\n")

    def display_scores(self):
        print("\n--- Bestenliste ---")
        scores = self.load_scores()
        if not scores:
            print("Keine Einträge vorhanden.")
        else:
            for rank, (name, score) in enumerate(scores, 1):
                print(f"{rank}. {name}: {score} verbleibende Versuche")

class HangmanGame:
    def __init__(self):
        self.hangman = Hangman()
        self.scoreboard = Scoreboard()

    def singleplayer_mode(self):
        print("\n--- Einzelspielermodus ---")
        self.hangman.choose_word()
        while self.hangman.remaining_attempts > 0:
            self.hangman.display_status()
            guess = input("Geben Sie einen Buchstaben ein: ").strip()
            if len(guess) != 1 or not guess.isalpha():
                print("Ungültige Eingabe! Bitte geben Sie einen einzelnen Buchstaben ein.")
                continue
            self.hangman.guess_letter(guess)

            if self.hangman.is_word_guessed():
                print(f"Herzlichen Glückwunsch! Sie haben das Wort '{self.hangman.word_to_guess}' erraten!")
                name = input("Geben Sie Ihren Namen für die Bestenliste ein: ").strip()
                self.scoreboard.save_score(name, self.hangman.remaining_attempts)
                break
        else:
            print(f"Sie haben verloren! Das Wort war: '{self.hangman.word_to_guess}'")

    def multiplayer_mode(self):
        print("\n--- Mehrspielermodus ---")
        player_word = input("Spieler 1: Geben Sie das Wort ein, das Spieler 2 erraten soll (wird nicht angezeigt): ").strip().lower()
        self.hangman.word_to_guess = player_word
        self.hangman.correct_guesses = ["_"] * len(player_word)
        self.hangman.remaining_attempts = self.hangman.max_attempts
        self.hangman.guessed_letters = []

        os.system('clear' if os.name == 'posix' else 'cls')  # Bildschirm leeren, um das Wort zu verbergen

        while self.hangman.remaining_attempts > 0:
            self.hangman.display_status()
            guess = input("Spieler 2: Geben Sie einen Buchstaben ein: ").strip()
            if len(guess) != 1 or not guess.isalpha():
                print("Ungültige Eingabe! Bitte geben Sie einen einzelnen Buchstaben ein.")
                continue
            self.hangman.guess_letter(guess)

            if self.hangman.is_word_guessed():
                print(f"Spieler 2 hat gewonnen! Das Wort '{self.hangman.word_to_guess}' wurde erraten!")
                break
        else:
            print(f"Spieler 2 hat verloren! Das Wort war: '{self.hangman.word_to_guess}'")

    def display_scoreboard(self):
        self.scoreboard.display_scores()

    def menu(self):
        while True:
            print("\n--- Hangman Spiel ---")
            print("1. Einzelspielermodus")
            print("2. Mehrspielermodus")
            print("3. Bestenliste anzeigen")
            print("4. Beenden")

            try:
                choice = int(input("Wählen Sie eine Option (1-4): "))
                if choice == 1:
                    self.singleplayer_mode()
                elif choice == 2:
                    self.multiplayer_mode()
                elif choice == 3:
                    self.display_scoreboard()
                elif choice == 4:
                    print("Spiel beendet. Auf Wiedersehen!")
                    break
                else:
                    print("Ungültige Option! Bitte wählen Sie eine Zahl zwischen 1 und 4.")
            except ValueError:
                print("Ungültige Eingabe! Bitte wählen Sie eine Zahl.")

# Spiel starten
if __name__ == "__main__":
    game = HangmanGame()
    game.menu()
