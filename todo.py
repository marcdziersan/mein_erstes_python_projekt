import os
from datetime import datetime

class Task:
    def __init__(self, description, due_date=None):
        self.description = description
        self.due_date = due_date

    def __str__(self):
        return f"{self.description} (Fällig: {self.due_date if self.due_date else 'Kein Datum'})"

class TodoList:
    def __init__(self, filename="todo.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, description, due_date=None):
        task = Task(description, due_date)
        self.tasks.append(task)
        self.save_tasks()

    def display_tasks(self):
        if not self.tasks:
            print("Keine Aufgaben vorhanden.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def edit_task(self, index, new_description=None, new_due_date=None):
        try:
            task = self.tasks[index - 1]
            if new_description:
                task.description = new_description
            if new_due_date:
                task.due_date = new_due_date
            self.save_tasks()
            print("Aufgabe erfolgreich bearbeitet.")
        except IndexError:
            print("Fehler: Aufgabe mit dieser Nummer existiert nicht.")

    def delete_task(self, index):
        try:
            removed_task = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f"Aufgabe '{removed_task.description}' wurde gelöscht.")
        except IndexError:
            print("Fehler: Aufgabe mit dieser Nummer existiert nicht.")

    def search_tasks(self, keyword):
        results = [task for task in self.tasks if keyword.lower() in task.description.lower()]
        if not results:
            print(f"Keine Aufgaben gefunden, die '{keyword}' enthalten.")
        else:
            print("Suchergebnisse:")
            for task in results:
                print(task)

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                line = f"{task.description}|{task.due_date if task.due_date else ''}\n"
                file.write(line)

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    description, due_date = line.strip().split("|")
                    self.tasks.append(Task(description, due_date if due_date else None))

class TodoApp:
    def __init__(self):
        self.todo_list = TodoList()

    def menu(self):
        while True:
            print("\n--- To-Do-Listen-Anwendung ---")
            print("1. Aufgabe hinzufügen")
            print("2. Alle Aufgaben anzeigen")
            print("3. Aufgabe bearbeiten")
            print("4. Aufgabe löschen")
            print("5. Aufgaben suchen")
            print("6. Beenden")

            try:
                choice = int(input("Wählen Sie eine Option (1-6): "))
            except ValueError:
                print("Ungültige Eingabe! Bitte wählen Sie eine Zahl.")
                continue

            if choice == 1:
                self.add_task()
            elif choice == 2:
                self.todo_list.display_tasks()
            elif choice == 3:
                self.edit_task()
            elif choice == 4:
                self.delete_task()
            elif choice == 5:
                self.search_task()
            elif choice == 6:
                print("Programm beendet. Auf Wiedersehen!")
                break
            else:
                print("Ungültige Option! Bitte wählen Sie eine Zahl zwischen 1 und 6.")

    def add_task(self):
        description = input("Geben Sie die Beschreibung der Aufgabe ein: ")
        due_date = input("Geben Sie ein Fälligkeitsdatum ein (Format: YYYY-MM-DD, optional): ").strip()
        if due_date:
            try:
                due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
            except ValueError:
                print("Ungültiges Datum! Aufgabe wird ohne Fälligkeitsdatum hinzugefügt.")
                due_date = None
        self.todo_list.add_task(description, due_date)

    def edit_task(self):
        self.todo_list.display_tasks()
        try:
            index = int(input("Geben Sie die Nummer der zu bearbeitenden Aufgabe ein: "))
            new_description = input("Neue Beschreibung (leer lassen, um sie nicht zu ändern): ").strip()
            new_due_date = input("Neues Fälligkeitsdatum (Format: YYYY-MM-DD, leer lassen, um es nicht zu ändern): ").strip()
            if new_due_date:
                try:
                    new_due_date = datetime.strptime(new_due_date, "%Y-%m-%d").date()
                except ValueError:
                    print("Ungültiges Datum! Fälligkeitsdatum wird nicht geändert.")
                    new_due_date = None
            self.todo_list.edit_task(index, new_description if new_description else None, new_due_date)
        except ValueError:
            print("Ungültige Eingabe! Bitte geben Sie eine Zahl ein.")

    def delete_task(self):
        self.todo_list.display_tasks()
        try:
            index = int(input("Geben Sie die Nummer der zu löschenden Aufgabe ein: "))
            self.todo_list.delete_task(index)
        except ValueError:
            print("Ungültige Eingabe! Bitte geben Sie eine Zahl ein.")

    def search_task(self):
        keyword = input("Geben Sie ein Stichwort für die Suche ein: ")
        self.todo_list.search_tasks(keyword)

# Programm starten
if __name__ == "__main__":
    app = TodoApp()
    app.menu()
