import os

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} von {self.author}"

class Library:
    def __init__(self, filename="library.txt"):
        self.filename = filename
        self.available_books = []
        self.borrowed_books = []
        self.load_books()

    def add_book(self, title, author):
        book = Book(title, author)
        self.available_books.append(book)
        self.save_books()
        print(f"Buch '{book}' hinzugefügt.")

    def borrow_book(self, title):
        for book in self.available_books:
            if book.title.lower() == title.lower():
                self.available_books.remove(book)
                self.borrowed_books.append(book)
                self.save_books()
                print(f"Buch '{book}' wurde ausgeliehen.")
                return
        print(f"Buch '{title}' ist nicht verfügbar.")

    def return_book(self, title):
        for book in self.borrowed_books:
            if book.title.lower() == title.lower():
                self.borrowed_books.remove(book)
                self.available_books.append(book)
                self.save_books()
                print(f"Buch '{book}' wurde zurückgegeben.")
                return
        print(f"Buch '{title}' wurde nicht ausgeliehen.")

    def display_books(self, books, message):
        if not books:
            print(message)
        else:
            for book in books:
                print(f"- {book}")

    def search_books(self, keyword):
        matches = [
            book for book in self.available_books + self.borrowed_books
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()
        ]
        if matches:
            print("\nSuchergebnisse:")
            for book in matches:
                print(f"- {book}")
        else:
            print(f"Keine Bücher gefunden, die '{keyword}' enthalten.")

    def save_books(self):
        with open(self.filename, "w") as file:
            for book in self.available_books:
                file.write(f"AVAILABLE|{book.title}|{book.author}\n")
            for book in self.borrowed_books:
                file.write(f"BORROWED|{book.title}|{book.author}\n")

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    status, title, author = line.strip().split("|")
                    book = Book(title, author)
                    if status == "AVAILABLE":
                        self.available_books.append(book)
                    elif status == "BORROWED":
                        self.borrowed_books.append(book)

class LibraryApp:
    def __init__(self):
        self.library = Library()

    def menu(self):
        while True:
            print("\n--- Mini-Bibliotheksverwaltung ---")
            print("1. Buch hinzufügen")
            print("2. Buch ausleihen")
            print("3. Buch zurückgeben")
            print("4. Alle verfügbaren Bücher anzeigen")
            print("5. Alle ausgeliehenen Bücher anzeigen")
            print("6. Bücher suchen")
            print("7. Beenden")

            try:
                choice = int(input("Wählen Sie eine Option (1-7): "))
                if choice == 1:
                    self.add_book()
                elif choice == 2:
                    self.borrow_book()
                elif choice == 3:
                    self.return_book()
                elif choice == 4:
                    self.display_available_books()
                elif choice == 5:
                    self.display_borrowed_books()
                elif choice == 6:
                    self.search_books()
                elif choice == 7:
                    print("Programm beendet. Auf Wiedersehen!")
                    break
                else:
                    print("Ungültige Option! Bitte wählen Sie eine Zahl zwischen 1 und 7.")
            except ValueError:
                print("Ungültige Eingabe! Bitte wählen Sie eine Zahl.")

    def add_book(self):
        title = input("Geben Sie den Titel des Buches ein: ").strip()
        author = input("Geben Sie den Autor des Buches ein: ").strip()
        self.library.add_book(title, author)

    def borrow_book(self):
        title = input("Geben Sie den Titel des Buches ein, das Sie ausleihen möchten: ").strip()
        self.library.borrow_book(title)

    def return_book(self):
        title = input("Geben Sie den Titel des Buches ein, das Sie zurückgeben möchten: ").strip()
        self.library.return_book(title)

    def display_available_books(self):
        print("\n--- Verfügbare Bücher ---")
        self.library.display_books(self.library.available_books, "Keine verfügbaren Bücher.")

    def display_borrowed_books(self):
        print("\n--- Ausgeliehene Bücher ---")
        self.library.display_books(self.library.borrowed_books, "Keine ausgeliehenen Bücher.")

    def search_books(self):
        keyword = input("Geben Sie ein Stichwort ein (Titel oder Autor): ").strip()
        self.library.search_books(keyword)

# Programm starten
if __name__ == "__main__":
    app = LibraryApp()
    app.menu()
