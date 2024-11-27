import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import time
import threading
import json
from datetime import datetime, timedelta

class DailyHelperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alltagshelfer")
        self.root.geometry("600x600")

        # Initialisierung der Daten
        self.tasks = {}  # Aufgaben mit Fälligkeitsdatum und Wiederholung
        self.notes = {}   # Tägliche Notizen
        self.reminders = []  # Erinnerungen
        self.current_date = datetime.now().strftime("%Y-%m-%d")

        # Kalender
        self.calendar_label = tk.Label(root, text="Kalender")
        self.calendar_label.pack()

        self.calendar = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
        self.calendar.pack()
        self.calendar.bind("<<CalendarSelected>>", self.on_date_select)

        # Anzeige für Aufgaben und Notizen des ausgewählten Tages
        self.task_label = tk.Label(root, text="Aufgaben für den Tag")
        self.task_label.pack()

        self.task_entry = tk.Entry(root)
        self.task_entry.pack()

        self.due_date_entry = tk.Entry(root)
        self.due_date_entry.pack()
        self.due_date_entry.insert(0, "Fälligkeitsdatum (YYYY-MM-DD)")

        self.recurrence_entry = tk.Entry(root)
        self.recurrence_entry.pack()
        self.recurrence_entry.insert(0, "Wiederholung (täglich, wöchentlich)")

        self.add_task_button = tk.Button(root, text="Aufgabe hinzufügen", command=self.add_task)
        self.add_task_button.pack()

        self.task_listbox = tk.Listbox(root)
        self.task_listbox.pack()

        self.remove_task_button = tk.Button(root, text="Aufgabe entfernen", command=self.remove_task)
        self.remove_task_button.pack()

        # Erinnerungen
        self.reminder_label = tk.Label(root, text="Erinnerung setzen")
        self.reminder_label.pack()

        self.reminder_entry = tk.Entry(root)
        self.reminder_entry.pack()

        self.reminder_time_entry = tk.Entry(root)
        self.reminder_time_entry.pack()
        self.reminder_time_entry.insert(0, "HH:MM")

        self.add_reminder_button = tk.Button(root, text="Erinnerung hinzufügen", command=self.add_reminder)
        self.add_reminder_button.pack()

        # Tägliche Notizen
        self.note_label = tk.Label(root, text="Tägliche Notiz")
        self.note_label.pack()

        self.note_entry = tk.Entry(root)
        self.note_entry.pack()

        self.add_note_button = tk.Button(root, text="Notiz hinzufügen", command=self.add_note)
        self.add_note_button.pack()

        self.note_display = tk.Label(root, text="")
        self.note_display.pack()

        # Starten der Erinnerungsthread
        self.reminder_thread = threading.Thread(target=self.check_reminders)
        self.reminder_thread.daemon = True
        self.reminder_thread.start()

        # Starten der fälligen Aufgabenüberprüfung
        self.task_thread = threading.Thread(target=self.check_due_tasks)
        self.task_thread.daemon = True
        self.task_thread.start()

        # Daten laden
        self.load_data()

    def on_date_select(self, event):
        self.current_date = self.calendar.get_date()
        self.update_task_listbox()
        self.display_notes_for_day()

    def add_task(self):
        task = self.task_entry.get()
        due_date = self.due_date_entry.get()
        recurrence = self.recurrence_entry.get().lower()

        if task and due_date:
            if due_date not in self.tasks:
                self.tasks[due_date] = []

            # Aufgabe hinzufügen
            self.tasks[due_date].append({"task": task, "recurrence": recurrence})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
            self.due_date_entry.delete(0, tk.END)
            self.recurrence_entry.delete(0, tk.END)
            self.save_data()
        else:
            messagebox.showwarning("Eingabefehler", "Bitte Aufgabe und Fälligkeitsdatum eingeben.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_to_remove = self.task_listbox.get(selected_task_index)
            task_date = self.current_date
            for task in self.tasks.get(task_date, []):
                if task_to_remove == task["task"]:
                    self.tasks[task_date].remove(task)
                    break
            self.update_task_listbox()
            self.save_data()
        else:
            messagebox.showwarning("Fehler", "Bitte wählen Sie eine Aufgabe zum Entfernen aus.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        if self.current_date in self.tasks:
            for task in self.tasks[self.current_date]:
                self.task_listbox.insert(tk.END, task["task"])

    def check_due_tasks(self):
        while True:
            current_time = datetime.now().strftime("%Y-%m-%d")
            if current_time in self.tasks:
                for task in self.tasks[current_time]:
                    # Überprüfen, ob die Aufgabe fällig ist
                    if current_time == task.get("due_date"):
                        messagebox.showinfo("Fällige Aufgabe", f"Aufgabe fällig: {task['task']}")
                        # Bei wiederkehrenden Aufgaben, falls vorhanden
                        if task["recurrence"] == "täglich":
                            new_due_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
                            self.add_task(new_due_date, task["task"])
                        elif task["recurrence"] == "wöchentlich":
                            new_due_date = (datetime.now() + timedelta(weeks=1)).strftime("%Y-%m-%d")
                            self.add_task(new_due_date, task["task"])
            time.sleep(60)

    def add_reminder(self):
        reminder_text = self.reminder_entry.get()
        reminder_time = self.reminder_time_entry.get()

        if reminder_text and reminder_time:
            self.reminders.append({"text": reminder_text, "time": reminder_time})
            self.reminder_entry.delete(0, tk.END)
            self.reminder_time_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Eingabefehler", "Bitte Erinnerung und Zeit eingeben.")

    def check_reminders(self):
        while True:
            current_time = time.strftime("%H:%M")
            for reminder in self.reminders:
                if reminder["time"] == current_time:
                    messagebox.showinfo("Erinnerung", reminder["text"])
                    self.reminders.remove(reminder)
            time.sleep(60)

    def add_note(self):
        note_text = self.note_entry.get()
        if note_text:
            self.notes[self.current_date] = note_text
            self.display_notes_for_day()
            self.note_entry.delete(0, tk.END)
            self.save_data()
        else:
            messagebox.showwarning("Eingabefehler", "Bitte Notiz eingeben.")

    def display_notes_for_day(self):
        if self.current_date in self.notes:
            self.note_display.config(text=f"Notiz für {self.current_date}: {self.notes[self.current_date]}")
        else:
            self.note_display.config(text="Keine Notizen für heute.")

    def load_data(self):
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
                self.tasks = data.get("tasks", {})
                self.notes = data.get("notes", {})
        except FileNotFoundError:
            pass  # Wenn die Datei nicht gefunden wird, ist es kein Problem

    def save_data(self):
        data = {
            "tasks": self.tasks,
            "notes": self.notes
        }
        with open("tasks.json", "w") as f:
            json.dump(data, f, indent=4)

# Anwendung starten
if __name__ == "__main__":
    root = tk.Tk()
    app = DailyHelperApp(root)
    root.mainloop()
