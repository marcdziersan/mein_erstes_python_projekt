import random
import os

class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, answer):
        return self.correct_option == answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def shuffle_questions(self):
        random.shuffle(self.questions)

    def ask_question(self, question):
        print("\n" + question.text)
        for i, option in enumerate(question.options, start=1):
            print(f"{i}. {option}")
        while True:
            try:
                answer = int(input("Wählen Sie eine Option (1-4): "))
                if 1 <= answer <= 4:
                    return answer
                else:
                    print("Bitte wählen Sie eine Zahl zwischen 1 und 4.")
            except ValueError:
                print("Ungültige Eingabe! Bitte wählen Sie eine Zahl.")

    def play(self):
        self.shuffle_questions()
        for question in self.questions:
            answer = self.ask_question(question)
            if question.is_correct(answer):
                print("Richtig! 🎉")
                self.score += 1
            else:
                print(f"Falsch! Die richtige Antwort war: {question.correct_option}. {question.options[question.correct_option - 1]}")
        print(f"\nSpiel beendet! Ihre Punktzahl: {self.score}/{len(self.questions)}")

class HighScoreManager:
    def __init__(self, filename="highscores.txt"):
        self.filename = filename

    def load_highscores(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return [line.strip() for line in file.readlines()]
        return []

    def save_highscore(self, name, score):
        highscores = self.load_highscores()
        highscores.append(f"{name}: {score}")
        with open(self.filename, "w") as file:
            for highscore in highscores:
                file.write(highscore + "\n")

    def display_highscores(self):
        highscores = self.load_highscores()
        if highscores:
            print("\n--- Bestenliste ---")
            for highscore in highscores:
                print(highscore)
        else:
            print("\nKeine Highscores vorhanden.")

class QuizApp:
    def __init__(self):
        self.easy_questions = self.create_easy_questions()
        self.medium_questions = self.create_medium_questions()
        self.hard_questions = self.create_hard_questions()
        self.highscore_manager = HighScoreManager()

    def create_easy_questions(self):
        return [
            Question("Was ist 2 + 2?", ["3", "4", "5", "6"], 2),
            Question("Welche Farbe hat der Himmel?", ["Grün", "Blau", "Rot", "Gelb"], 2),
            Question("Wie viele Beine hat ein Hund?", ["2", "4", "6", "8"], 2),
        ]

    def create_medium_questions(self):
        return [
            Question("Wer hat die Relativitätstheorie entwickelt?", ["Newton", "Einstein", "Tesla", "Curie"], 2),
            Question("Was ist die Hauptstadt von Deutschland?", ["München", "Berlin", "Hamburg", "Frankfurt"], 2),
            Question("Wie viele Kontinente gibt es?", ["5", "6", "7", "8"], 3),
        ]

    def create_hard_questions(self):
        return [
            Question("Wie viele Planeten gibt es in unserem Sonnensystem?", ["7", "8", "9", "10"], 2),
            Question("Wer hat die Mona Lisa gemalt?", ["Michelangelo", "Van Gogh", "Leonardo da Vinci", "Rembrandt"], 3),
            Question("In welchem Jahr begann der Zweite Weltkrieg?", ["1937", "1938", "1939", "1940"], 3),
        ]

    def choose_difficulty(self):
        print("\nWählen Sie einen Schwierigkeitsgrad:")
        print("1. Einfach")
        print("2. Mittel")
        print("3. Schwer")
        while True:
            try:
                choice = int(input("Schwierigkeitsgrad (1-3): "))
                if choice == 1:
                    return self.easy_questions
                elif choice == 2:
                    return self.medium_questions
                elif choice == 3:
                    return self.hard_questions
                else:
                    print("Bitte wählen Sie eine Zahl zwischen 1 und 3.")
            except ValueError:
                print("Ungültige Eingabe! Bitte wählen Sie eine Zahl.")

    def menu(self):
        while True:
            print("\n--- Quiz-Spiel ---")
            print("1. Spielen")
            print("2. Bestenliste anzeigen")
            print("3. Beenden")
            try:
                choice = int(input("Wählen Sie eine Option (1-3): "))
                if choice == 1:
                    self.play_game()
                elif choice == 2:
                    self.highscore_manager.display_highscores()
                elif choice == 3:
                    print("Programm beendet. Auf Wiedersehen!")
                    break
                else:
                    print("Ungültige Option! Bitte wählen Sie eine Zahl zwischen 1 und 3.")
            except ValueError:
                print("Ungültige Eingabe! Bitte wählen Sie eine Zahl.")

    def play_game(self):
        questions = self.choose_difficulty()
        quiz = Quiz(questions)
        quiz.play()
        name = input("Geben Sie Ihren Namen ein: ").strip()
        self.highscore_manager.save_highscore(name, quiz.score)

# Programm starten
if __name__ == "__main__":
    app = QuizApp()
    app.menu()
