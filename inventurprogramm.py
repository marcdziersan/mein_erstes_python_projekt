import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# Datenbank initialisieren
def initialize_database():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Artikel zur Datenbank hinzufügen
def add_item():
    name = name_entry.get()
    quantity = quantity_entry.get()
    
    if not name or not quantity.isdigit():
        messagebox.showwarning("Ungültige Eingabe", "Bitte geben Sie einen gültigen Namen und eine Menge ein.")
        return

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (?, ?)", (name, int(quantity)))
    conn.commit()
    conn.close()

    name_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    display_inventory()

# Artikel aus der Datenbank löschen
def remove_item():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Kein Artikel ausgewählt", "Bitte wählen Sie einen Artikel aus, den Sie löschen möchten.")
        return

    item_id = tree.item(selected_item[0])["values"][0]

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM inventory WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
    display_inventory()

# Menge eines Artikels aktualisieren
def update_quantity():
    selected_item = tree.selection()
    new_quantity = quantity_entry.get()
    
    if not selected_item or not new_quantity.isdigit():
        messagebox.showwarning("Fehler", "Bitte wählen Sie einen Artikel und geben Sie eine gültige Menge ein.")
        return

    item_id = tree.item(selected_item[0])["values"][0]

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE inventory SET quantity = ? WHERE id = ?", (int(new_quantity), item_id))
    conn.commit()
    conn.close()
    display_inventory()

# Alle Artikel anzeigen
def display_inventory():
    for row in tree.get_children():
        tree.delete(row)

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)
    conn.close()

# Komplettes Inventar zurücksetzen
def reset_inventory():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM inventory")
    conn.commit()
    conn.close()
    display_inventory()

# Hauptfenster einrichten
root = tk.Tk()
root.title("Inventurverwaltung")

# Name-Label und Eingabefeld
tk.Label(root, text="Artikelname:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Menge-Label und Eingabefeld
tk.Label(root, text="Menge:").grid(row=1, column=0, padx=10, pady=10)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=1, column=1, padx=10, pady=10)

# Buttons für die CRUD-Operationen
tk.Button(root, text="Hinzufügen", command=add_item).grid(row=0, column=2, padx=10, pady=10)
tk.Button(root, text="Aktualisieren", command=update_quantity).grid(row=1, column=2, padx=10, pady=10)
tk.Button(root, text="Löschen", command=remove_item).grid(row=2, column=2, padx=10, pady=10)
tk.Button(root, text="Inventar zurücksetzen", command=reset_inventory).grid(row=3, column=2, padx=10, pady=10)

# Tabelle für die Anzeige des Inventars
tree = ttk.Treeview(root, columns=("ID", "Name", "Menge"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Menge", text="Menge")
tree.grid(row=2, column=0, columnspan=2, rowspan=4, padx=10, pady=10)

# Datenbank und Inventar initialisieren
initialize_database()
display_inventory()

# Hauptschleife starten
root.mainloop()
