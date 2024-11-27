import sqlite3

# Datenbank und Tabelle initialisieren
def init_db():
    conn = sqlite3.connect("telefonbuch.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            vorname TEXT,
            adresse TEXT,
            email TEXT,
            telefonnummer TEXT,
            mobilnummer TEXT,
            geburtsdatum TEXT
        )
    ''')
    conn.commit()
    # Beispieldaten einfügen
    cursor.executemany('''
        INSERT INTO contacts (name, vorname, adresse, email, telefonnummer, mobilnummer, geburtsdatum)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', [
        ("Muster", "Max", "Musterstraße 1", "max@muster.de", "0123456789", "01701234567", "1990-01-01"),
        ("Schmidt", "Anna", "Beispielweg 2", "anna@beispiel.com", "0987654321", "01501234567", "1985-05-15")
    ])
    conn.commit()
    conn.close()

# Kontakt hinzufügen
def add_contact():
    print("Neuen Kontakt hinzufügen:")
    name = input("Name: ")
    vorname = input("Vorname: ")
    adresse = input("Adresse: ")
    email = input("Email: ")
    telefonnummer = input("Telefonnummer: ")
    mobilnummer = input("Mobilnummer: ")
    geburtsdatum = input("Geburtsdatum (YYYY-MM-DD): ")
    
    conn = sqlite3.connect("telefonbuch.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO contacts (name, vorname, adresse, email, telefonnummer, mobilnummer, geburtsdatum)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (name, vorname, adresse, email, telefonnummer, mobilnummer, geburtsdatum))
    conn.commit()
    conn.close()
    print("Kontakt erfolgreich hinzugefügt!")

# Kontakte anzeigen
def view_contacts():
    conn = sqlite3.connect("telefonbuch.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    conn.close()
    print("Alle Kontakte:")
    for row in rows:
        print(row)

# Kontakte suchen
def search_contacts():
    print("Kontakte suchen:")
    query = input("Suchbegriff eingeben: ")
    conn = sqlite3.connect("telefonbuch.db")
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM contacts
        WHERE name LIKE ? OR vorname LIKE ? OR adresse LIKE ? OR email LIKE ? OR telefonnummer LIKE ? OR mobilnummer LIKE ? OR geburtsdatum LIKE ?
    ''', tuple(['%' + query + '%'] * 7))
    rows = cursor.fetchall()
    conn.close()
    print("Suchergebnisse:")
    for row in rows:
        print(row)

# Kontakt aktualisieren
def update_contact():
    print("Kontakt aktualisieren:")
    id = input("ID des zu aktualisierenden Kontakts: ")
    
    conn = sqlite3.connect("telefonbuch.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE id = ?", (id,))
    contact = cursor.fetchone()
    if not contact:
        print("Kontakt nicht gefunden!")
        return

    print(f"Gefundener Kontakt: {contact}")
    name = input(f"Neuer Name (aktuell: {contact[1]}): ") or contact[1]
    vorname = input(f"Neuer Vorname (aktuell: {contact[2]}): ") or contact[2]
    adresse = input(f"Neue Adresse (aktuell: {contact[3]}): ") or contact[3]
    email = input(f"Neue Email (aktuell: {contact[4]}): ") or contact[4]
    telefonnummer = input(f"Neue Telefonnummer (aktuell: {contact[5]}): ") or contact[5]
    mobilnummer = input(f"Neue Mobilnummer (aktuell: {contact[6]}): ") or contact[6]
    geburtsdatum = input(f"Neues Geburtsdatum (aktuell: {contact[7]}): ") or contact[7]

    cursor.execute('''
        UPDATE contacts
        SET name = ?, vorname = ?, adresse = ?, email = ?, telefonnummer = ?, mobilnummer = ?, geburtsdatum = ?
        WHERE id = ?
    ''', (name, vorname, adresse, email, telefonnummer, mobilnummer, geburtsdatum, id))
    conn.commit()
    conn.close()
    print("Kontakt erfolgreich aktualisiert!")

# Kontakt löschen
def delete_contact():
    print("Kontakt löschen:")
    id = input("ID des zu löschenden Kontakts: ")
    conn = sqlite3.connect("telefonbuch.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    print("Kontakt erfolgreich gelöscht!")

# Hauptmenü
def main():
    init_db()
    while True:
        print("\nTelefonbuch")
        print("1. Kontakt hinzufügen")
        print("2. Kontakte anzeigen")
        print("3. Kontakte suchen")
        print("4. Kontakt aktualisieren")
        print("5. Kontakt löschen")
        print("6. Beenden")
        choice = input("Auswahl: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte erneut versuchen.")

if __name__ == "__main__":
    main()
