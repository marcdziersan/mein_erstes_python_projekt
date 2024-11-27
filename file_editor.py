import os
import ctypes
import tkinter as tk
from tkinter import filedialog, messagebox

class FileEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("File Editor")
        self.filename = None
        self.text_modified = False
        self.text_area = tk.Text(root, wrap="none", undo=True)
        self.text_area.pack(expand=1, fill="both")
        self.text_area.bind("<<Modified>>", self.on_modified)
        self.create_menu()
        self.status_bar = tk.Label(root, text="Unsaved", anchor="w")
        self.status_bar.pack(fill="x", side="bottom")

    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open...", command=self.open_file)
        file_menu.add_command(label="Save...", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))
        menubar.add_cascade(label="Edit", menu=edit_menu)
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Info", command=self.show_info)
        menubar.add_cascade(label="Help", menu=help_menu)
        self.root.config(menu=menubar)

    def new_file(self):
        if self.ask_save():
            self.text_area.delete(1.0, tk.END)
            self.filename = None
            self.update_status("Unsaved")

    def open_file(self):
        if self.ask_save():
            file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if file_path:
                with open(file_path, "r") as file:
                    content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
                self.filename = file_path
                self.update_status(file_path)

    def save_file(self):
        if not self.filename:
            self.filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.update_status(self.filename)
            self.text_modified = False
            self.text_area.edit_modified(False)

    def ask_save(self):
        if self.text_modified:
            answer = messagebox.askyesno("Save text?", "Do you want to save changes?")
            if answer:
                self.save_file()
            return answer or not self.text_modified
        return True

    def get_file_version_info(self):
        """
        Extrahiert Versionsinformationen aus der laufenden .exe-Datei (nur für Windows).
        """
        version_info = {}
        try:
            exe_path = os.path.abspath(__file__)
            if not exe_path.endswith('.exe'):
                return version_info  # Nur in der .exe-Version ausführen

            size = ctypes.windll.version.GetFileVersionInfoSizeW(exe_path, None)
            res = ctypes.create_string_buffer(size)
            ctypes.windll.version.GetFileVersionInfoW(exe_path, None, size, res)
            r, l = ctypes.c_void_p(), ctypes.c_uint()

            ctypes.windll.version.VerQueryValueW(res, r'\\VarFileInfo\\Translation', ctypes.byref(r), ctypes.byref(l))
            language_code, codepage = ctypes.cast(r, ctypes.POINTER(ctypes.c_ushort))[:2]

            def query_value(name):
                ctypes.windll.version.VerQueryValueW(
                    res, f'\\StringFileInfo\\{language_code:04x}{codepage:04x}\\{name}', ctypes.byref(r), ctypes.byref(l)
                )
                return ctypes.wstring_at(r)

            version_info['FileDescription'] = query_value('FileDescription')
            version_info['FileVersion'] = query_value('FileVersion')
            version_info['ProductName'] = query_value('ProductName')
            version_info['ProductVersion'] = query_value('ProductVersion')
            version_info['CompanyName'] = query_value('CompanyName')
            version_info['LegalCopyright'] = query_value('LegalCopyright')

        except Exception as e:
            print(f"Fehler beim Lesen der Version-Info: {e}")
        
        return version_info

    def show_info(self):
        version_info = self.get_file_version_info()
        info_text = (
            f"Produktname: {version_info.get('ProductName', 'File Editor')}\n"
            f"Version: {version_info.get('FileVersion', '1.0.0')}\n"
            f"Produktversion: {version_info.get('ProductVersion', '1.0.0')}\n"
            f"Unternehmen: {version_info.get('CompanyName', 'Marcus Dziersan')}\n"
            f"© {version_info.get('LegalCopyright', '2024 Marcus Dziersan')}\n\n"
            f"Beschreibung: {version_info.get('FileDescription', 'Ein einfacher Datei-Editor.')}"
        )
        messagebox.showinfo("Info", info_text)

    def on_modified(self, event=None):
        self.text_modified = self.text_area.edit_modified()
        self.update_status("Modified" if self.text_modified else "")
        self.text_area.edit_modified(False)

    def update_status(self, text):
        self.status_bar.config(text=text)

# Hauptprogramm
if __name__ == "__main__":
    root = tk.Tk()
    app = FileEditor(root)
    root.geometry("600x400")
    root.mainloop()
