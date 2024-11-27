import os
import base64
from cryptography.fernet import Fernet
import random
import string

class PasswordManager:
    def __init__(self, filename="passwoerter.txt", keyfile="key.key"):
        self.filename = filename
        self.keyfile = keyfile
        self.key = self.load_or_generate_key()
        self.fernet = Fernet(self.key)

    def load_or_generate_key(self):
        if os.path.exists(self.keyfile):
            with open(self.keyfile, "rb") as file:
                return file.read()
        else:
            key = Fernet.generate_key()
            with open(self.keyfile, "wb") as file:
                file.write(key)
            return key

    def encrypt(self, text):
        return self.fernet.encrypt(text.encode()).decode()

    def decrypt(self, encrypted_text):
        return self.fernet.decrypt(encrypted_text.encode()).decode()

    def save_password(self, service, username, password):
        encrypted_password = self.encrypt(password)
        if not os.path.exists(self.filename):
            open(self.filename, 'w').close()  # Create the file if it doesn't exist

        with open(self.filename, "a") as file:
            file.write(f"{service}|{username}|{encrypted_password}\n")
        print(f"Passwort für {service} gespeichert.")

    def load_passwords(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as file:
            lines = file.readlines()
        passwords = []
        for line in lines:
            service, username, encrypted_password = line.strip().split("|")
            decrypted_password = self.decrypt(encrypted_password)
            passwords.append((service, username, decrypted_password))
        return passwords

    def find_password(self, service):
        passwords = self.load_passwords()
        for s, username, password in passwords:
            if s.lower() == service.lower():
                return username, password
        return None

    def display_passwords(self):
        passwords = self.load_passwords()
        if not passwords:
            print("Keine gespeicherten Passwörter vorhanden.")
        else:
            for service, username, password in passwords:
                print(f"Dienst: {service}, Benutzername: {username}, Passwort: {password}")

    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"Generiertes Passwort: {password}")
        return password

class PasswordManagerApp:
    def __init__(self):
        self.manager = PasswordManager()

    def menu(self):
        while True:
            print("\n--- Passwort-Manager ---")
            print("1. Passwort speichern")
            print("2. Passwörter anzeigen")
            print("3. Passwort suchen")
            print("4. Passwort generieren")
            print("5. Beenden")

            try:
                choice = int(input("Wählen Sie eine Option (1-5): "))
                if choice == 1:
                    self.save_password()
                elif choice == 2:
                    self.display_passwords()
                elif choice == 3:
                    self.search_password()
                elif choice == 4:
                    self.generate_password()
                elif choice == 5:
                    print("Programm beendet. Auf Wiedersehen!")
                    break
                else:
                    print("Ungültige Option! Bitte wählen Sie eine Zahl zwischen 1 und 5.")
            except ValueError:
                print("Ungültige Eingabe! Bitte wählen Sie eine Zahl.")

    def save_password(self):
        service = input("Geben Sie den Dienst ein: ").strip()
        username = input("Geben Sie den Benutzernamen ein: ").strip()
        password = input("Geben Sie das Passwort ein (oder leer lassen, um ein zufälliges Passwort zu generieren): ").strip()
        if not password:
            password = self.manager.generate_password()
        self.manager.save_password(service, username, password)

    def display_passwords(self):
        print("\n--- Gespeicherte Passwörter ---")
        self.manager.display_passwords()

    def search_password(self):
        service = input("Geben Sie den Dienst ein, nach dem Sie suchen möchten: ").strip()
        result = self.manager.find_password(service)
        if result:
            username, password = result
            print(f"Dienst: {service}, Benutzername: {username}, Passwort: {password}")
        else:
            print(f"Kein Passwort für den Dienst '{service}' gefunden.")

    def generate_password(self):
        try:
            length = int(input("Geben Sie die Länge des Passworts ein (Standard: 12): ") or 12)
            self.manager.generate_password(length)
        except ValueError:
            print("Ungültige Eingabe! Es wird die Standardlänge von 12 verwendet.")
            self.manager.generate_password()

# Programm starten
if __name__ == "__main__":
    app = PasswordManagerApp()
    app.menu()
