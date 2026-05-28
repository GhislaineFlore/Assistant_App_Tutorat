"""import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk


# --- INITIALISATION DE LA BASE DE DONNÉES LOCALE ---
def init_db():
    conn = sqlite3.connect("tutorat_local.db")
    cursor = conn.cursor()
    # Table pour le Tuteur (Matériel, notes de formation)
    cursor.execute(
        '
        CREATE TABLE IF NOT EXISTS tuteur_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categorie TEXT,
            contenu TEXT
        )
    '
    )
    # Table pour les Tutorés (Journal, compétences, objectifs)
    cursor.execute(
        '
        CREATE TABLE IF NOT EXISTS tutores_suivi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_apprenti TEXT,
            type_note TEXT, -- Journal, Compétence, Objectif
            date_note TEXT,
            details TEXT
        )
    '
    )
    conn.commit()
    conn.close()


# --- LOGIQUE DE L'APPLICATION ---
class TutoratApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Mon Assistant Tutorat - Groupe de 3")
        self.root.geometry("700x550")

        # Configuration des onglets
        tab_control = ttk.Notebook(root)

        self.tab_tuteur = ttk.Frame(tab_control)
        self.tab_tutores = ttk.Frame(tab_control)

        tab_control.add(self.tab_tuteur, text="👨‍🏫 Mon Espace Tuteur")
        tab_control.add(self.tab_tutores, text="👥 Suivi des Tutorés")
        tab_control.pack(expand=1, fill="both")

        self.setup_tab_tuteur()
        self.setup_tab_tutores()

    # --- ONGLET 1 : ESPACE TUTEUR ---
    def setup_tab_tuteur(self):
        lbl = tk.Label(
            self.tab_tuteur,
            text="Mes Notes de Formation & Documents",
            font=("Arial", 14, "bold"),
        )
        lbl.pack(pady=10)

        frame = tk.Frame(self.tab_tuteur)
        frame.pack(pady=5)

        tk.Label(frame, text="Catégorie :").grid(row=0, column=0, padx=5)
        self.cat_box = ttk.Combobox(
            frame, values=["Syllabus", "Calendrier", "Méthodes Pédagogiques"]
        )
        self.cat_box.grid(row=0, column=1, padx=5)
        self.cat_box.current(0)

        tk.Label(self.tab_tuteur, text="Contenu de la note :").pack(pady=5)
        self.tuteur_text = tk.Text(self.tab_tuteur, height=10, width=70)
        self.tuteur_text.pack(pady=5)

        btn_save = tk.Button(
            self.tab_tuteur,
            text="Sauvegarder ma note",
            bg="blue",
            fg="white",
            command=self.save_tuteur_note,
        )
        btn_save.pack(pady=10)

    def save_tuteur_note(self):
        cat = self.cat_box.get()
        txt = self.tuteur_text.get("1.0", tk.END).strip()
        if not txt:
            messagebox.showwarning("Erreur", "La note ne peut pas être vide.")
            return

        conn = sqlite3.connect("tutorat_local.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tuteur_notes (categorie, contenu) VALUES (?, ?)",
            (cat, txt),
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Succès", "Note tuteur enregistrée localement !")
        self.tuteur_text.delete("1.0", tk.END)

    # --- ONGLET 2 : SUIVI DES TUTORÉS ---
    def setup_tab_tutores(self):
        lbl = tk.Label(
            self.tab_tutores,
            text="Registre de Suivi Individuel (Groupe de 3)",
            font=("Arial", 14, "bold"),
        )
        lbl.pack(pady=10)

        frame = tk.Frame(self.tab_tutores)
        frame.pack(pady=5)

        # Sélection de l'apprenti
        tk.Label(frame, text="Apprenti :").grid(row=0, column=0, padx=5)
        self.student_box = ttk.Combobox(
            frame, values=["Apprenti 1", "Apprenti 2", "Apprenti 3"]
        )
        self.student_box.grid(row=0, column=1, padx=5)
        self.student_box.current(0)

        # Sélection de la section du cahier
        tk.Label(frame, text="Section du cahier :").grid(row=0, column=2, padx=5)
        self.section_box = ttk.Combobox(
            frame,
            values=[
                "📝 Journal de Bord",
                "📊 Grille de Compétences",
                "💬 Objectifs Mensuels",
            ],
        )
        self.section_box.grid(row=0, column=3, padx=5)
        self.section_box.current(0)

        tk.Label(self.tab_tutores, text="Date (JJ/MM/AAAA) :").pack(pady=5)
        self.date_entry = tk.Entry(self.tab_tutores, width=20)
        self.date_entry.insert(0, "28/05/2026")
        self.date_entry.pack()

        tk.Label(self.tab_tutores, text="Détails / Mentions :").pack(pady=5)
        self.student_text = tk.Text(self.tab_tutores, height=8, width=70)
        self.student_text.pack(pady=5)

        btn_save_stud = tk.Button(
            self.tab_tutores,
            text="Enregistrer dans le cahier numérique",
            bg="green",
            fg="white",
            command=self.save_student_note,
        )
        btn_save_stud.pack(pady=10)

    def save_student_note(self):
        nom = self.student_box.get()
        sec = self.section_box.get()
        date = self.date_entry.get()
        txt = self.student_text.get("1.0", tk.END).strip()

        if not txt:
            messagebox.showwarning("Erreur", "Le champ détails est vide.")
            return

        conn = sqlite3.connect("tutorat_local.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tutores_suivi (nom_apprenti, type_note, date_note, details) VALUES (?, ?, ?, ?)",
            (nom, sec, date, txt),
        )
        conn.commit()
        conn.close()
        messagebox.showinfo(
            "Succès", f"Données enregistrées pour {nom} dans {sec} !"
        )
        self.student_text.delete("1.0", tk.END)


# --- LANCEMENT DE L'APPLICATION ---
if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = TutoratApp(root)
    root.mainloop()"""
#CODE-----2---- un traducteur d'interface intégré (Français 🇫🇷 / Anglais 🇬🇧)

"""import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk


# --- INITIALISATION DE LA BASE DE DONNÉES LOCALE ---
def init_db():
    conn = sqlite3.connect("tutorat_local.db")
    cursor = conn.cursor()
    # Table pour le Tuteur (Matériel, notes de formation)
    cursor.execute(
        '
        CREATE TABLE IF NOT EXISTS tuteur_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categorie TEXT,
            contenu TEXT
        )
    '
    )
    # Table pour les Tutorés (Journal, compétences, objectifs)
    cursor.execute(
        '
        CREATE TABLE IF NOT EXISTS tutores_suivi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_apprenti TEXT,
            type_note TEXT,
            date_note TEXT,
            details TEXT
        )
    '
    )
    conn.commit()
    conn.close()


# --- DICTIONNAIRE DE TRADUCTION INTEGRÉ ---
TRANSLATIONS = {
    "FR": {
        "title": "Mon Assistant Tutorat - Groupe de 3",
        "tab_tuteur": "👨‍🏫 Mon Espace Tuteur",
        "tab_tutores": "👥 Suivi des Tutorés",
        "tuteur_title": "Mes Notes de Formation & Documents",
        "category": "Catégorie :",
        "content": "Contenu de la note :",
        "btn_save_tuteur": "Sauvegarder ma note",
        "success_tuteur": "Note tuteur enregistrée localement !",
        "tutores_title": "Registre de Suivi Individuel (Groupe de 3)",
        "apprenti": "Apprenti :",
        "section": "Section du cahier :",
        "date": "Date (JJ/MM/AAAA) :",
        "details": "Détails / Mentions :",
        "btn_save_tutorat": "Enregistrer dans le cahier numérique",
        "btn_history": "Voir l'historique",
        "success_tutorat": "Données enregistrées pour {} dans {} !",
        "err_empty": "Erreur : Le champ texte est vide.",
        "history_title": "Historique pour {}",
        "no_data": "Aucune donnée enregistrée pour le moment.",
        "cats": ["Syllabus", "Calendrier", "Méthodes Pédagogiques"],
        "sections": [
            "📝 Journal de Bord",
            "📊 Grille de Compétences",
            "💬 Objectifs Mensuels",
        ],
    },
    "EN": {
        "title": "My Mentoring Assistant - Group of 3",
        "tab_tuteur": "👨‍🏫 My Mentor Space",
        "tab_tutores": "👥 Mentees Tracking",
        "tuteur_title": "My Training Notes & Documents",
        "category": "Category:",
        "content": "Note Content:",
        "btn_save_tuteur": "Save My Note",
        "success_tuteur": "Mentor note saved locally!",
        "tutores_title": "Individual Tracking Register (Group of 3)",
        "apprenti": "Learner:",
        "section": "Notebook Section:",
        "date": "Date (DD/MM/YYYY):",
        "details": "Details / Observations:",
        "btn_save_tutorat": "Save to Digital Notebook",
        "btn_history": "View History Log",
        "success_tutorat": "Data successfully saved for {} in {} !",
        "err_empty": "Error: The text field is empty.",
        "history_title": "History log for {}",
        "no_data": "No data recorded yet.",
        "cats": ["Syllabus", "Schedule/Calendar", "Teaching Methods"],
        "sections": ["📝 Logbook", "📊 Skills Matrix", "💬 Monthly Goals"],
    },
}


class TutoratApp:

    def __init__(self, root):
        self.root = root
        self.lang = "FR"  # Langue par défaut

        # Fenêtre Principale
        self.root.geometry("750x650")
        self.tab_control = ttk.Notebook(root)
        self.tab_tuteur = ttk.Frame(self.tab_control)
        self.tab_tutores = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_tuteur, text="")
        self.tab_control.add(self.tab_tutores, text="")
        self.tab_control.pack(expand=1, fill="both")

        # Sélecteur de Langue persistant en haut
        lang_frame = tk.Frame(root, bg="#f0f0f0")
        lang_frame.pack(side="top", fill="x")
        tk.Button(
            lang_frame,
            text="Français 🇫🇷",
            command=lambda: self.switch_lang("FR"),
        ).pack(side="right", padx=5, pady=2)
        tk.Button(
            lang_frame,
            text="English 🇬🇧",
            command=lambda: self.switch_lang("EN"),
        ).pack(side="right", padx=5, pady=2)

        self.build_ui()
        self.update_ui_text()

    def build_ui(self):
        # --- BLOC : ONGLET TUTEUR ---
        self.lbl_tuteur_title = tk.Label(
            self.tab_tuteur, text="", font=("Arial", 14, "bold")
        )
        self.lbl_tuteur_title.pack(pady=10)

        frame_tuteur = tk.Frame(self.tab_tuteur)
        frame_tuteur.pack(pady=5)

        self.lbl_cat = tk.Label(frame_tuteur, text="")
        self.lbl_cat.grid(row=0, column=0, padx=5)
        self.cat_box = ttk.Combobox(frame_tuteur, values=[])
        self.cat_box.grid(row=0, column=1, padx=5)

        self.lbl_tuteur_content = tk.Label(self.tab_tuteur, text="")
        self.lbl_tuteur_content.pack(pady=5)
        self.tuteur_text = tk.Text(self.tab_tuteur, height=8, width=75)
        self.tuteur_text.pack(pady=5)

        self.btn_save_tuteur = tk.Button(
            self.tab_tuteur,
            text="",
            bg="#1d3557",
            fg="white",
            command=self.save_tuteur_note,
        )
        self.btn_save_tuteur.pack(pady=5)

        # --- BLOC : ONGLET TUTORÉS ---
        self.lbl_tutores_title = tk.Label(
            self.tab_tutores, text="", font=("Arial", 14, "bold")
        )
        self.lbl_tutores_title.pack(pady=10)

        frame_tutores = tk.Frame(self.tab_tutores)
        frame_tutores.pack(pady=5)

        self.lbl_apprenti = tk.Label(frame_tutores, text="")
        self.lbl_apprenti.grid(row=0, column=0, padx=5)
        self.student_box = ttk.Combobox(
            frame_tutores, values=["Learner / Apprenti 1", "Learner / Apprenti 2", "Learner / Apprenti 3"]
        )
        self.student_box.grid(row=0, column=1, padx=5)
        self.student_box.current(0)

        self.lbl_section = tk.Label(frame_tutores, text="")
        self.lbl_section.grid(row=0, column=2, padx=5)
        self.section_box = ttk.Combobox(frame_tutores, values=[])
        self.section_box.grid(row=0, column=3, padx=5)

        self.lbl_date = tk.Label(self.tab_tutores, text="")
        self.lbl_date.pack(pady=5)
        self.date_entry = tk.Entry(self.tab_tutores, width=20)
        self.date_entry.insert(0, "28/05/2026")
        self.date_entry.pack()

        self.lbl_details = tk.Label(self.tab_tutores, text="")
        self.lbl_details.pack(pady=5)
        self.student_text = tk.Text(self.tab_tutores, height=8, width=75)
        self.student_text.pack(pady=5)

        # Boutons d'action côte à côte
        btn_frame = tk.Frame(self.tab_tutores)
        btn_frame.pack(pady=10)

        self.btn_save_student = tk.Button(
            btn_frame,
            text="",
            bg="#2a9d8f",
            fg="white",
            command=self.save_student_note,
        )
        self.btn_save_student.pack(side="left", padx=10)

        self.btn_history = tk.Button(
            btn_frame,
            text="",
            bg="#e76f51",
            fg="white",
            command=self.view_history,
        )
        self.btn_history.pack(side="left", padx=10)

    def switch_lang(self, lang):
        self.lang = lang
        self.update_ui_text()

    def update_ui_text(self):
        t = TRANSLATIONS[self.lang]
        self.root.title(t["title"])

        # Onglets
        self.tab_control.tab(0, text=t["tab_tuteur"])
        self.tab_control.tab(1, text=t["tab_tutores"])

        # Textes Tuteur
        self.lbl_tuteur_title.config(text=t["tuteur_title"])
        self.lbl_cat.config(text=t["category"])
        self.cat_box.config(values=t["cats"])
        self.cat_box.current(0)
        self.lbl_tuteur_content.config(text=t["content"])
        self.btn_save_tuteur.config(text=t["btn_save_tuteur"])

        # Textes Tutorés
        self.lbl_tutores_title.config(text=t["tutores_title"])
        self.lbl_apprenti.config(text=t["apprenti"])
        self.lbl_section.config(text=t["section"])
        self.section_box.config(values=t["sections"])
        self.section_box.current(0)
        self.lbl_date.config(text=t["date"])
        self.lbl_details.config(text=t["details"])
        self.btn_save_student.config(text=t["btn_save_tutorat"])
        self.btn_history.config(text=t["btn_history"])

    def save_tuteur_note(self):
        t = TRANSLATIONS[self.lang]
        cat = self.cat_box.get()
        txt = self.tuteur_text.get("1.0", tk.END).strip()
        if not txt:
            messagebox.showwarning("!", t["err_empty"])
            return

        conn = sqlite3.connect("tutorat_local.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tuteur_notes (categorie, contenu) VALUES (?, ?)",
            (cat, txt),
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("OK", t["success_tuteur"])
        self.tuteur_text.delete("1.0", tk.END)

    def save_student_note(self):
        t = TRANSLATIONS[self.lang]
        nom = self.student_box.get()
        sec = self.section_box.get()
        date = self.date_entry.get()
        txt = self.student_text.get("1.0", tk.END).strip()

        if not txt:
            messagebox.showwarning("!", t["err_empty"])
            return

        conn = sqlite3.connect("tutorat_local.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tutores_suivi (nom_apprenti, type_note, date_note, details) VALUES (?, ?, ?, ?)",
            (nom, sec, date, txt),
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("OK", t["success_tutorat"].format(nom, sec))
        self.student_text.delete("1.0", tk.END)

    def view_history(self):
        t = TRANSLATIONS[self.lang]
        nom_appr = self.student_box.get()

        # Récupération en Base de données"""

#CODE 3---------d'Export Excel automatique.

"""import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os

# --- INITIALISATION DE LA BASE DE DONNÉES LOCALE ---
def init_db():
    conn = sqlite3.connect("tutorat_local.db")
    cursor = conn.cursor()
    cursor.execute('
        CREATE TABLE IF NOT EXISTS tuteur_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categorie TEXT,
            contenu TEXT
        )
    ')
    cursor.execute('
        CREATE TABLE IF NOT EXISTS tutores_suivi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_apprenti TEXT,
            type_note TEXT,
            date_note TEXT,
            details TEXT
        )
    ')
    conn.commit()
    conn.close()

# --- DICTIONNAIRE DE TRADUCTION ---
TRANSLATIONS = {
    "FR": {
        "title": "Mon Assistant Tutorat - Groupe de 3",
        "tab_tuteur": "👨‍🏫 Mon Espace Tuteur",
        "tab_tutores": "👥 Suivi des Tutorés",
        "tuteur_title": "Mes Notes de Formation & Documents",
        "category": "Catégorie :",
        "content": "Contenu de la note :",
        "btn_save_tuteur": "Sauvegarder ma note",
        "success_tuteur": "Note tuteur enregistrée localement !",
        "tutores_title": "Registre de Suivi Individuel (Groupe de 3)",
        "apprenti": "Apprenti :",
        "section": "Section du cahier :",
        "date": "Date (JJ/MM/AAAA) :",
        "details": "Détails / Mentions :",
        "btn_save_tutorat": "Enregistrer dans le cahier numérique",
        "btn_history": "Voir l'historique",
        "btn_export": "📊 Exporter vers Excel (CSV)",
        "success_tutorat": "Données enregistrées pour {} dans {} !",
        "err_empty": "Erreur : Le champ texte est vide.",
        "history_title": "Historique pour {}",
        "no_data": "Aucune donnée enregistrée pour le moment.",
        "export_success": "Fichier Excel généré avec succès :\n{}",
        "cats": ["Syllabus", "Calendrier", "Méthodes Pédagogiques"],
        "sections": ["📝 Journal de Bord", "📊 Grille de Compétences", "💬 Objectifs Mensuels"]
    },
    "EN": {
        "title": "My Mentoring Assistant - Group of 3",
        "tab_tuteur": "👨‍🏫 My Mentor Space",
        "tab_tutores": "👥 Mentees Tracking",
        "tuteur_title": "My Training Notes & Documents",
        "category": "Category:",
        "content": "Note Content:",
        "btn_save_tuteur": "Save My Note",
        "success_tuteur": "Mentor note saved locally!",
        "tutores_title": "Individual Tracking Register (Group of 3)",
        "apprenti": "Learner:",
        "section": "Notebook Section:",
        "date": "Date (DD/MM/YYYY):",
        "details": "Details / Observations:",
        "btn_save_tutorat": "Save to Digital Notebook",
        "btn_history": "View History Log",
        "btn_export": "📊 Export to Excel (CSV)",
        "success_tutorat": "Data successfully saved for {} in {} !",
        "err_empty": "Error: The text field is empty.",
        "history_title": "History log for {}",
        "no_data": "No data recorded yet.",
        "export_success": "Excel file successfully generated:\n{}",
        "cats": ["Syllabus", "Schedule/Calendar", "Teaching Methods"],
        "sections": ["📝 Logbook", "📊 Skills Matrix", "💬 Monthly Goals"]
    }
}

class TutoratApp:
    def __init__(self, root):
        self.root = root
        self.lang = "FR"

        self.root.geometry("750x650")
        self.tab_control = ttk.Notebook(root)
        self.tab_tuteur = ttk.Frame(self.tab_control)
        self.tab_tutores = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_tuteur, text="")
        self.tab_control.add(self.tab_tutores, text="")
        self.tab_control.pack(expand=1, fill="both")

        lang_frame = tk.Frame(root, bg="#f0f0f0")
        lang_frame.pack(side="top", fill="x")
        tk.Button(lang_frame, text="Français 🇫🇷", command=lambda: self.switch_lang("FR")).pack(side="right", padx=5, pady=2)
        tk.Button(lang_frame, text="English 🇬🇧", command=lambda: self.switch_lang("EN")).pack(side="right", padx=5, pady=2)

        self.build_ui()
        self.update_ui_text()

    def build_ui(self):
        # --- TAB TUTEUR ---
        self.lbl_tuteur_title = tk.Label(self.tab_tuteur, text="", font=("Arial", 14, "bold"))
        self.lbl_tuteur_title.pack(pady=10)

        frame_tuteur = tk.Frame(self.tab_tuteur)
        frame_tuteur.pack(pady=5)
        self.lbl_cat = tk.Label(frame_tuteur, text="")
        self.lbl_cat.grid(row=0, column=0, padx=5)
        self.cat_box = ttk.Combobox(frame_tuteur, values=[])
        self.cat_box.grid(row=0, column=1, padx=5)

        self.lbl_tuteur_content = tk.Label(self.tab_tuteur, text="")
        self.lbl_tuteur_content.pack(pady=5)
        self.tuteur_text = tk.Text(self.tab_tuteur, height=8, width=75)
        self.tuteur_text.pack(pady=5)

        self.btn_save_tuteur = tk.Button(self.tab_tuteur, text="", bg="#1d3557", fg="white", command=self.save_tuteur_note)
        self.btn_save_tuteur.pack(pady=5)

        # --- TAB TUTORÉS ---
        self.lbl_tutores_title = tk.Label(self.tab_tutores, text="", font=("Arial", 14, "bold"))
        self.lbl_tutores_title.pack(pady=10)

        frame_tutores = tk.Frame(self.tab_tutores)
        frame_tutores.pack(pady=5)

        self.lbl_apprenti = tk.Label(frame_tutores, text="")
        self.lbl_apprenti.grid(row=0, column=0, padx=5)
        self.student_box = ttk.Combobox(frame_tutores, values=["Apprenti 1", "Apprenti 2", "Apprenti 3"])
        self.student_box.grid(row=0, column=1, padx=5)
        self.student_box.current(0)

        self.lbl_section = tk.Label(frame_tutores, text="")
        self.lbl_section.grid(row=0, column=2, padx=5)
        self.section_box = ttk.Combobox(frame_tutores, values=[])
        self.section_box.grid(row=0, column=3, padx=5)

        self.lbl_date = tk.Label(self.tab_tutores, text="")
        self.lbl_date.pack(pady=5)
        self.date_entry = tk.Entry(self.tab_tutores, width=20)
        self.date_entry.insert(0, "28/05/2026")
        self.date_entry.pack()

        self.lbl_details = tk.Label(self.tab_tutores, text="")
        self.lbl_details.pack(pady=5)
        self.student_text = tk.Text(self.tab_tutores, height=8, width=75)
        self.student_text.pack(pady=5)

        btn_frame = tk.Frame(self.tab_tutores)
        btn_frame.pack(pady=10)

        self.btn_save_student = tk.Button(btn_frame, text="", bg="#2a9d8f", fg="white", command=self.save_student_note)
        self.btn_save_student.pack(side="left", padx=5)

        self.btn_history = tk.Button(btn_frame, text="", bg="#e76f51", fg="white", command=self.view_history)
        self.btn_history.pack(side="left", padx=5)

        self.btn_export = tk.Button(self.tab_tutores, text="", bg="#4a4e69", fg="white", command=self.export_to_excel)
        self.btn_export.pack(pady=5)

    def switch_lang(self, lang):
        self.lang = lang
        self.update_ui_text()

    def update_ui_text(self):
        t = TRANSLATIONS[self.lang]
        self.root.title(t["title"])
        self.tab_control.tab(0, text=t["tab_tuteur"])
        self.tab_control.tab(1, text=t["tab_tutores"])
        self.lbl_tuteur_title.config(text=t["tuteur_title"])
        self.lbl_cat.config(text=t["category"])
        self.cat_box.config(values=t["cats"])
        self.cat_box.current(0)
        self.lbl_tuteur_content.config(text=t["content"])
        self.btn_save_tuteur.config(text=t["btn_save_tuteur"])
        self.lbl_tutores_title.config(text=t["tutores_title"])
        self.lbl_apprenti.config(text=t["apprenti"])
        self.lbl_section.config(text=t["section"])
        self.section_box.config(values=t["sections"])
        self.section_box.current(0)
        self.lbl_date.config(text=t["date"])
        self.lbl_details.config(text=t["details"])
        self.btn_save_student.config(text=t["btn_save_tutorat"])
        self.btn_history.config(text=t["btn_history"])
        self.btn_export.config(text=t["btn_export"])

    def save_tuteur_note(self):
        t = TRANSLATIONS[self.lang]
        cat = self.cat_box.get()
        txt = self.tuteur_text.get("1.0", tk.END).strip()
        if not txt:
            messagebox.showwarning("!", t["err_empty"])
            return
        conn = sqlite3.connect("tutorat_local.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tuteur_notes (categorie, contenu) VALUES (?, ?)", (cat, txt))
        conn.commit()
        conn.close()
        messagebox.showinfo("OK", t["success_tuteur"])
        self.tuteur_text.delete("1.0", tk.END)

    def save_student_note(self):
        t = TRANSLATIONS[self.lang]
        nom = self.student_box.get()
        sec = self.section_box.get()
        date = self.date_entry.get()
        txt = self.student_text.get("1.0", tk.END).strip()

        if not txt:
            messagebox.showwarning("!", t["err_empty"])
            return

        conn = sqlite3.connect("tutorat_local.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tutores_suivi (nom_apprenti, type_note, date_note, details) VALUES (?, ?, ?, ?)", (nom, sec, date, txt))
        conn.commit()
        conn.close()
        messagebox.showinfo("OK", t["success_tutorat"].format(nom, sec))
        self.student_text.delete("1.0", tk.END)

    def view_history(self):
        t = TRANSLATIONS[self.lang]
        nom_appr = self.student_box.get()
        conn = sqlite3.connect("tutorat_local.db")
        cursor = conn.cursor()
        cursor.execute("SELECT date_note, type_note, details FROM tutores_suivi WHERE nom_apprenti = ? ORDER BY id DESC", (nom_appr,))
        rows = cursor.fetchall()
        conn.close()

        history_win = tk.Toplevel(self.root)
        history_win.title(t["history_title"].format(nom_appr))
        history_win.geometry("550x400")

        txt_area = tk.Text(history_win, wrap="word", padx=10, pady=10)"""

###-----CODE 4---Code source évolutif --- troisième onglet appelé "Configuration / Base de données".

"""import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os

# --- INITIALISATION DE LA BASE DE DONNÉES LOCALE ---
def init_db():
    conn = sqlite3.connect("tutorat_local.db")
    cursor = conn.cursor()
    # Table pour les notes du tuteur
    cursor.execute('
        CREATE TABLE IF NOT EXISTS tuteur_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categorie TEXT,
            contenu TEXT
        )
    ')
    # Table pour le suivi des tutorés
    cursor.execute('
        CREATE TABLE IF NOT EXISTS tutores_suivi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_apprenti TEXT,
            type_note TEXT,
            date_note TEXT,
            details TEXT
        )
    ')
    # Table dynamique pour la liste des apprentis personnalisée
    cursor.execute('
        CREATE TABLE IF NOT EXISTS liste_apprentis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT UNIQUE
        )
    ')
    
    # Insertion par défaut de 3 apprentis si la table est vide
    cursor.execute("SELECT COUNT(*) FROM liste_apprentis")
    if cursor.fetchone()[0] == 0:
        for i in range(1, 4):
            cursor.execute("INSERT OR IGNORE INTO liste_apprentis (nom) VALUES (?)", (f"Apprenti {i}",))
            
    conn.commit()
    conn.close()

# --- DICTIONNAIRE DE TRADUCTION ---
TRANSLATIONS = {
    "FR": {
        "title": "GK-Mon Assistant Tutorat Évolutif",
        "tab_tuteur": "👨‍🏫 Mon Espace Tuteur",
        "tab_tutores": "👥 Suivi des Tutorés",
        "tab_db": "⚙️ Base de Données & Config",
        "tuteur_title": "Mes Notes de Formation & Documents",
        "category": "Catégorie :",
        "content": "Contenu de la note :",
        "btn_save_tuteur": "Sauvegarder ma note",
        "success_tuteur": "Note tuteur enregistrée localement !",
        "tutores_title": "Registre de Suivi Individuel",
        "apprenti": "Sélectionner l'apprenti :",
        "section": "Section du cahier :",
        "date": "Date (JJ/MM/AAAA) :",
        "details": "Détails / Mentions :",
        "btn_save_tutorat": "Enregistrer dans le cahier numérique",
        "btn_history": "Voir l'historique",
        "btn_export": "📊 Exporter vers Excel (CSV)",
        "success_tutorat": "Données enregistrées pour {} !",
        "err_empty": "Erreur : Le champ texte est vide.",
        "history_title": "Historique pour {}",
        "no_data": "Aucune donnée enregistrée pour le moment.",
        "export_success": "Fichier Excel généré avec succès :\n{}",
        "cats": ["Syllabus", "Calendrier", "Méthodes Pédagogiques"],
        "sections": ["📝 Journal de Bord", "📊 Grille de Compétences", "💬 Objectifs Mensuels"],
        "db_title": "Gestion de la Base de Données Locale",
        "db_path": "Emplacement de votre fichier de données :",
        "add_app_lbl": "Ajouter un nouvel apprenti (Prénom Nom) :",
        "btn_add_app": "Créer l'apprenti",
        "success_add": "Nouvel apprenti ajouté avec succès !"
    },
    "EN": {
        "title": "Gk-My Scalable Mentoring Assistant",
        "tab_tuteur": "👨‍🏫 My Mentor Space",
        "tab_tutores": "👥 Mentees Tracking",
        "tab_db": "⚙️ Database & Config",
        "tuteur_title": "My Training Notes & Documents",
        "category": "Category:",
        "content": "Note Content:",
        "btn_save_tuteur": "Save My Note",
        "success_tuteur": "Mentor note saved locally!",
        "tutores_title": "Individual Tracking Register",
        "apprenti": "Select Learner:",
        "section": "Notebook Section:",
        "date": "Date (DD/MM/YYYY):",
        "details": "Details / Observations:",
        "btn_save_tutorat": "Save to Digital Notebook",
        "btn_history": "View History Log",
        "btn_export": "📊 Export to Excel (CSV)",
        "success_tutorat": "Data successfully saved for {} !",
        "err_empty": "Error: The text field is empty.",
        "history_title": "History log for {}",
        "no_data": "No data recorded yet.",
        "export_success": "Excel file successfully generated:\n{}",
        "cats": ["Syllabus", "Schedule/Calendar", "Teaching Methods"],
        "sections": ["📝 Logbook", "📊 Skills Matrix", "💬 Monthly Goals"],
        "db_title": "Local Database Management",
        "db_path": "Your local database file path:",
        "add_app_lbl": "Add a new learner (First & Last Name):",
        "btn_add_app": "Create Learner",
        "success_add": "New learner successfully added!"
    }
}

class TutoratApp:
    def __init__(self, root):
        self.root = root
        self.lang = "FR"

        self.root.geometry("800x680")
        self.tab_control = ttk.Notebook(root)
        self.tab_tuteur = ttk.Frame(self.tab_control)
        self.tab_tutores = ttk.Frame(self.tab_control)
        self.tab_db = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_tuteur, text="")
        self.tab_control.add(self.tab_tutores, text="")
        self.tab_control.add(self.tab_db, text="")
        self.tab_control.pack(expand=1, fill="both")

        lang_frame = tk.Frame(root, bg="#f0f0f0")
        lang_frame.pack(side="top", fill="x")
        tk.Button(lang_frame, text="Français 🇫🇷", command=lambda: self.switch_lang("FR")).pack(side="right", padx=5, pady=2)
        tk.Button(lang_frame, text="English 🇬🇧", command=lambda: self.switch_lang("EN")).pack(side="right", padx=5, pady=2)

        self.build_ui()
        self.refresh_apprenti_list()
        self.update_ui_text()

    def build_ui(self):
        # --- TAB TUTEUR ---
        self.lbl_tuteur_title = tk.Label(self.tab_tuteur, text="", font=("Arial", 14, "bold"))
        self.lbl_tuteur_title.pack(pady=10)
        frame_tuteur = tk.Frame(self.tab_tuteur)
        frame_tuteur.pack(pady=5)
        self.lbl_cat = tk.Label(frame_tuteur, text="")
        self.lbl_cat.grid(row=0, column=0, padx=5)
        self.cat_box = ttk.Combobox(frame_tuteur, values=[])
        self.cat_box.grid(row=0, column=1, padx=5)
        self.lbl_tuteur_content = tk.Label(self.tab_tuteur, text="")
        self.lbl_tuteur_content.pack(pady=5)
        self.tuteur_text = tk.Text(self.tab_tuteur, height=8, width=75)
        self.tuteur_text.pack(pady=5)
        self.btn_save_tuteur = tk.Button(self.tab_tuteur, text="", bg="#1d3557", fg="white", command=self.save_tuteur_note)
        self.btn_save_tuteur.pack(pady=5)

        # --- TAB TUTORÉS ---
        self.lbl_tutores_title = tk.Label(self.tab_tutores, text="", font=("Arial", 14, "bold"))
        self.lbl_tutores_title.pack(pady=10)
        frame_tutores = tk.Frame(self.tab_tutores)
        frame_tutores.pack(pady=5)
        self.lbl_apprenti = tk.Label(frame_tutores, text="")
        self.lbl_apprenti.grid(row=0, column=0, padx=5)
        self.student_box = ttk.Combobox(frame_tutores, values=[], state="readonly")
        self.student_box.grid(row=0, column=1, padx=5)
        self.lbl_section = tk.Label(frame_tutores, text="")
        self.lbl_section.grid(row=0, column=2, padx=5)
        self.section_box = ttk.Combobox(frame_tutores, values=[], state="readonly")
        self.section_box.grid(row=0, column=3, padx=5)
        self.lbl_date = tk.Label(self.tab_tutores, text="")
        self.lbl_date.pack(pady=5)
        self.date_entry = tk.Entry(self.tab_tutores, width=20)
        self.date_entry.insert(0, "28/05/2026")
        self.date_entry.pack()
        self.lbl_details = tk.Label(self.tab_tutores, text="")
        self.lbl_details.pack(pady=5)
        self.student_text = tk.Text(self.tab_tutores, height=8, width=75)
        self.student_text.pack(pady=5)
        btn_frame = tk.Frame(self.tab_tutores)
        btn_frame.pack(pady=10)
        self.btn_save_student = tk.Button(btn_frame, text="", bg="#2a9d8f", fg="white", command=self.save_student_note)
        self.btn_save_student.pack(side="left", padx=5)
        self.btn_history = tk.Button(btn_frame, text="", bg="#e76f51", fg="white", command=self.view_history)
        self.btn_history.pack(side="left", padx=5)
        self.btn_export = tk.Button(self.tab_tutores, text="", bg="#4a4e69", fg="white", command=self.export_to_excel)
        self.btn_export.pack(pady=5)

        # --- TAB CONFIG & BASE DE DONNÉES ---
        self.lbl_db_title = tk.Label(self.tab_db, text="", font=("Arial", 14, "bold"))
        self.lbl_db_title.pack(pady=10)
        
        self.lbl_db_path_tag = tk.Label(self.tab_db, text="", font=("Arial", 10, "bold"))
        self.lbl_db_path_tag.pack(pady=2)
        self.lbl_db_file_path = tk.Label(self.tab_db, text=os.path.abspath("tutorat_local.db"), fg="blue", bg="#e0e0e0", wraplength=700)
        self.lbl_db_file_path.pack(pady=5, padx=20)

        # Section Ajout Apprenti
        db_action_frame = tk.LabelFrame(self.tab_db, text=" Configuration ", padx=15, pady=15)
        db_action_frame.pack(pady=20, fill="x", padx=40)
        
        self.lbl_add_app = tk.Label(db_action_frame, text="")
        self.lbl_add_app.pack(anchor="w")
        self.new_app_entry = tk.Entry(db_action_frame, width=40)
        self.new_app_entry.pack(pady=5, anchor="w")
        
        self.btn_add_app = tk.Button(db_action_frame, text="", bg="#457b9d", fg="white", command=self.add_new_learner)
        self.btn_add_app.pack(pady=5, anchor="w")

    def refresh_apprenti_list(self):
        'Met à jour dynamiquement la liste déroulante depuis la BDD SQLite'
        conn = sqlite3.connect("tutorat_local.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nom FROM liste_apprentis ORDER BY nom ASC")
        liste = [row[0] for row in cursor.fetchall()]
        conn.close()
        
        self.student_box.config(values=liste)
        if liste:
            self.student_box.current(0)

    def add_new_learner(self):
        t = TRANSLATIONS[self.lang]
        nom = self.new_app_entry.get().strip()
        if not nom:
            messagebox.showwarning("!", t["err_empty"])
            return
        
        try:
            conn = sqlite3.connect("tutorat_local.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO liste_apprentis (nom) VALUES (?)", (nom,))
            conn.commit()
            conn.close()
            messagebox.showinfo("OK", t["success_add"])
            self.new_app_entry.delete(0, tk.END)
            self.refresh_apprenti_list() # Recharger le menu déroulant
        except sqlite3.IntegrityError:
            messagebox.showwarning("!", "Cet apprenti existe déjà." if self.lang == "FR" else "This learner already exists.")"""
##----------CODE 5 CORRECTION--------

"""import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os
import sys

# Forcer l'encodage standard
sys.stdout.reconfigure(encoding='utf-8') if sys.stdout else None

def init_db():
    conn = sqlite3.connect("tutorat_local.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tuteur_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categorie TEXT,
            contenu TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tutores_suivi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_apprenti TEXT,
            type_note TEXT,
            date_note TEXT,
            details TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS liste_apprentis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT UNIQUE
        )
    ''')
    cursor.execute("SELECT COUNT(*) FROM liste_apprentis")
    if cursor.fetchone()[0] == 0:
        for i in range(1, 4):
            cursor.execute("INSERT OR IGNORE INTO liste_apprentis (nom) VALUES (?)", (f"Apprenti {i}",))
    conn.commit()
    conn.close()

TRANSLATIONS = {
    "FR": {
        "title": "GK - Mon Assistant Tutorat Evolutif",
        "tab_tuteur": "Mon Espace Tuteur",
        "tab_tutores": "Suivi des Tutores",
        "tab_db": "Base de Donnees & Config",
        "tuteur_title": "Mes Notes de Formation & Documents",
        "category": "Categorie :",
        "content": "Contenu de la note :",
        "btn_save_tuteur": "Sauvegarder ma note",
        "success_tuteur": "Note tuteur enregistree localement !",
        "tutores_title": "Registre de Suivi Individuel",
        "apprenti": "Selectionner l'apprenti :",
        "section": "Section du cahier :",
        "date": "Date (JJ/MM/AAAA) :",
        "details": "Details / Mentions :",
        "btn_save_tutorat": "Enregistrer dans le cahier numerique",
        "btn_history": "Voir l'historique",
        "btn_export": "Exporter vers Excel (CSV)",
        "success_tutorat": "Donnees enregistrees pour {} !",
        "err_empty": "Erreur : Le champ texte est vide.",
        "history_title": "Historique pour {}",
        "no_data": "Aucune donnee enregistree pour le moment.",
        "export_success": "Fichier Excel genere avec succes :\n{}",
        "cats": ["Syllabus", "Calendrier", "Methodes Pedagogiques"],
        "sections": ["Journal de Bord", "Grille de Competences", "Objectifs Mensuels"],
        "db_title": "Gestion de la Base de Donnees Locale",
        "db_path": "Emplacement de votre fichier de donnees :",
        "add_app_lbl": "Ajouter un nouvel apprenti (Prenom Nom) :",
        "btn_add_app": "Creer l'apprenti",
        "success_add": "Nouvel apprenti ajoute avec succes !"
    },
    "EN": {
        "title": "GK - My Scalable Mentoring Assistant",
        "tab_tuteur": "My Mentor Space",
        "tab_tutores": "Mentees Tracking",
        "tab_db": "Database & Config",
        "tuteur_title": "My Training Notes & Documents",
        "category": "Category:",
        "content": "Note Content:",
        "btn_save_tuteur": "Save My Note",
        "success_tuteur": "Mentor note saved locally!",
        "tutores_title": "Individual Tracking Register",
        "apprenti": "Select Learner:",
        "section": "Notebook Section:",
        "date": "Date (DD/MM/YYYY):",
        "details": "Details / Observations:",
        "btn_save_tutorat": "Save to Digital Notebook",
        "btn_history": "View History Log",
        "btn_export": "Export to Excel (CSV)",
        "success_tutorat": "Data successfully saved for {} !",
        "err_empty": "Error: The text field is empty.",
        "history_title": "History log for {}",
        "no_data": "No data recorded yet.",
        "export_success": "Excel file successfully generated:\n{}",
        "cats": ["Syllabus", "Schedule/Calendar", "Teaching Methods"],
        "sections": ["Logbook", "Skills Matrix", "Monthly Goals"],
        "db_title": "Local Database Management",
        "db_path": "Your local database file path:",
        "add_app_lbl": "Add a new learner (First & Last Name):",
        "btn_add_app": "Create Learner",
        "success_add": "New learner successfully added!"
    }
}

class TutoratApp:
    def __init__(self, root):
        self.root = root
        self.lang = "FR"
        self.root.geometry("800x680")
        self.tab_control = ttk.Notebook(root)
        self.tab_tuteur = ttk.Frame(self.tab_control)
        self.tab_tutores = ttk.Frame(self.tab_control)
        self.tab_db = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_tuteur, text="")
        self.tab_control.add(self.tab_tutores, text="")
        self.tab_control.add(self.tab_db, text="")
        self.tab_control.pack(expand=1, fill="both")

        lang_frame = tk.Frame(root, bg="#f0f0f0")
        lang_frame.pack(side="top", fill="x")
        tk.Button(lang_frame, text="Francais", command=lambda: self.switch_lang("FR")).pack(side="right", padx=5, pady=2)
        tk.Button(lang_frame, text="English", command=lambda: self.switch_lang("EN")).pack(side="right", padx=5, pady=2)

        self.build_ui()
        self.refresh_apprenti_list()
        self.update_ui_text()

    def build_ui(self):
        self.lbl_tuteur_title = tk.Label(self.tab_tuteur, text="", font=("Arial", 14, "bold"))
        self.lbl_tuteur_title.pack(pady=10)
        frame_tuteur = tk.Frame(self.tab_tuteur)
        frame_tuteur.pack(pady=5)
        self.lbl_cat = tk.Label(frame_tuteur, text="")
        self.lbl_cat.grid(row=0, column=0, padx=5)
        self.cat_box = ttk.Combobox(frame_tuteur, values=[], state="readonly")
        self.cat_box.grid(row=0, column=1, padx=5)
        self.lbl_tuteur_content = tk.Label(self.tab_tuteur, text="")
        self.lbl_tuteur_content.pack(pady=5)
        self.tuteur_text = tk.Text(self.tab_tuteur, height=8, width=75)
        self.tuteur_text.pack(pady=5)
        self.btn_save_tuteur = tk.Button(self.tab_tuteur, text="", bg="#1d3557", fg="white", command=self.save_tuteur_note)
        self.btn_save_tuteur.pack(pady=5)

        self.lbl_tutores_title = tk.Label(self.tab_tutores, text="", font=("Arial", 14, "bold"))
        self.lbl_tutores_title.pack(pady=10)
        frame_tutores = tk.Frame(self.tab_tutores)
        frame_tutores.pack(pady=5)
        self.lbl_apprenti = tk.Label(frame_tutores, text="")
        self.lbl_apprenti.grid(row=0, column=0, padx=5)
        self.student_box = ttk.Combobox(frame_tutores, values=[], state="readonly")
        self.student_box.grid(row=0, column=1, padx=5)
        self.lbl_section = tk.Label(frame_tutores, text="")
        self.lbl_section.grid(row=0, column=2, padx=5)
        self.section_box = ttk.Combobox(frame_tutores, values=[], state="readonly")
        self.section_box.grid(row=0, column=3, padx=5)
        self.lbl_date = tk.Label(self.tab_tutores, text="")
        self.lbl_date.pack(pady=5)
        self.date_entry = tk.Entry(self.tab_tutores, width=20)
        self.date_entry.insert(0, "28/05/2026")
        self.date_entry.pack()
        self.lbl_details = tk.Label(self.tab_tutores, text="")
        self.lbl_details.pack(pady=5)
        self.student_text = tk.Text(self.tab_tutores, height=8, width=75)
        self.student_text.pack(pady=5)
        btn_frame = tk.Frame(self.tab_tutores)
        btn_frame.pack(pady=10)
        self.btn_save_student = tk.Button(btn_frame, text="", bg="#2a9d8f", fg="white", command=self.save_student_note)
        self.btn_save_student.pack(side="left", padx=5)
        self.btn_history = tk.Button(btn_frame, text="", bg="#e76f51", fg="white", command=self.view_history)
        self.btn_history.pack(side="left", padx=5)
        self.btn_export = tk.Button(self.tab_tutores, text="", bg="#4a4e69", fg="white", command=self.export_to_excel)
        self.btn_export.pack(pady=5)

        self.lbl_db_title = tk.Label(self.tab_db, text="", font=("Arial", 14, "bold"))
        self.lbl_db_title.pack(pady=10)
        self.lbl_db_path_tag = tk.Label(self.tab_db, text="", font=("Arial", 10, "bold"))
        self.lbl_db_path_tag.pack(pady=2)
        self.lbl_db_file_path = tk.Label(self.tab_db, text=os.path.abspath("tutorat_local.db"), fg="blue", bg="#e0e0e0", wraplength=700)
        self.lbl_db_file_path.pack(pady=5, padx=20)

        db_action_frame = tk.LabelFrame(self.tab_db, text=" Configuration ", padx=15, pady=15)
        db_action_frame.pack(pady=20, fill="x", padx=40)
        self.lbl_add_app = tk.Label(db_action_frame, text="")
        self.lbl_add_app.pack(anchor="w")
        self.new_app_entry = tk.Entry(db_action_frame, width=40)
        self.new_app_entry.pack(pady=5, anchor="w")
        self.btn_add_app = tk.Button(db_action_frame, text="", bg="#457b9d", fg="white", command=self.add_new_learner)
        self.btn_add_app.pack(pady=5, anchor="w")

    def refresh_apprenti_list(self):
        conn = sqlite3.connect("tutorat_local.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nom FROM liste_apprentis ORDER BY nom ASC")
        liste = [row[0] for row in cursor.fetchall()]
        conn.close()
        self.student_box.config(values=liste)
        if liste:
            self.student_box.current(0)

    def add_new_learner(self):
        t = TRANSLATIONS[self.lang]
        nom = self.new_app_entry.get().strip()
        if not nom:
            messagebox.showwarning("!", t["err_empty"])
            return
        try:
            conn = sqlite3.connect("tutorat_local.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO liste_apprentis (nom) VALUES (?)", (nom,))
            conn.commit()
            conn.close()
            messagebox.showinfo("OK", t["success_add"])
            self.new_app_entry.delete(0, tk.END)
            self.refresh_apprenti_list()
        except sqlite3.IntegrityError:
            messagebox.showwarning("!", "Cet apprenti existe deja." if self.lang == "FR" else "This learner already exists.")

    def switch_lang(self, lang):
        self.lang = lang
        self.update_ui_text()"""

##----------CODE 51 CORRECTION--------
import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os
import sys

# Forcer l'encodage standard
sys.stdout.reconfigure(encoding='utf-8') if sys.stdout else None

def init_db():
    conn = sqlite3.connect("tutorat_local.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tuteur_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categorie TEXT,
            contenu TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tutores_suivi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_apprenti TEXT,
            type_note TEXT,
            date_note TEXT,
            details TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS liste_apprentis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT UNIQUE
        )
    ''')
    cursor.execute("SELECT COUNT(*) FROM liste_apprentis")
    if cursor.fetchone()[0] == 0:
        for i in range(1, 4):
            cursor.execute("INSERT OR IGNORE INTO liste_apprentis (nom) VALUES (?)", (f"Apprenti {i}",))
    conn.commit()
    conn.close()

TRANSLATIONS = {
    "FR": {
        "title": "GK - Mon Assistant Tutorat Evolutif",
        "tab_tuteur": "Mon Espace Tuteur",
        "tab_tutores": "Suivi des Tutores",
        "tab_db": "Base de Donnees & Config",
        "tuteur_title": "Mes Notes de Formation & Documents",
        "category": "Categorie :",
        "content": "Contenu de la note :",
        "btn_save_tuteur": "Sauvegarder ma note",
        "success_tuteur": "Note tuteur enregistree localement !",
        "tutores_title": "Registre de Suivi Individuel",
        "apprenti": "Selectionner l'apprenti :",
        "section": "Section du cahier :",
        "date": "Date (JJ/MM/AAAA) :",
        "details": "Details / Mentions :",
        "btn_save_tutorat": "Enregistrer dans le cahier numerique",
        "btn_history": "Voir l'historique",
        "btn_export": "Exporter vers Excel (CSV)",
        "success_tutorat": "Donnees enregistrees pour {} !",
        "err_empty": "Erreur : Le champ texte est vide.",
        "history_title": "Historique pour {}",
        "no_data": "Aucune donnee enregistree pour le moment.",
        "export_success": "Fichier Excel genere avec succes :\n{}",
        "cats": ["Syllabus", "Calendrier", "Methodes Pedagogiques"],
        "sections": ["Journal de Bord", "Grille de Competences", "Objectifs Mensuels"],
        "db_title": "Gestion de la Base de Donnees Locale",
        "db_path": "Emplacement de votre fichier de donnees :",
        "add_app_lbl": "Ajouter un nouvel apprenti (Prenom Nom) :",
        "btn_add_app": "Creer l'apprenti",
        "success_add": "Nouvel apprenti ajoute avec succes !"
    },
    "EN": {
        "title": "GK - My Scalable Mentoring Assistant",
        "tab_tuteur": "My Mentor Space",
        "tab_tutores": "Mentees Tracking",
        "tab_db": "Database & Config",
        "tuteur_title": "My Training Notes & Documents",
        "category": "Category:",
        "content": "Note Content:",
        "btn_save_tuteur": "Save My Note",
        "success_tuteur": "Mentor note saved locally!",
        "tutores_title": "Individual Tracking Register",
        "apprenti": "Select Learner:",
        "section": "Notebook Section:",
        "date": "Date (DD/MM/YYYY):",
        "details": "Details / Observations:",
        "btn_save_tutorat": "Save to Digital Notebook",
        "btn_history": "View History Log",
        "btn_export": "Export to Excel (CSV)",
        "success_tutorat": "Data successfully saved for {} !",
        "err_empty": "Error: The text field is empty.",
        "history_title": "History log for {}",
        "no_data": "No data recorded yet.",
        "export_success": "Excel file successfully generated:\n{}",
        "cats": ["Syllabus", "Schedule/Calendar", "Teaching Methods"],
        "sections": ["Logbook", "Skills Matrix", "Monthly Goals"],
        "db_title": "Local Database Management",
        "db_path": "Your local database file path:",
        "add_app_lbl": "Add a new learner (First & Last Name):",
        "btn_add_app": "Create Learner",
        "success_add": "New learner successfully added!"
    }
}

class TutoratApp:
    def __init__(self, root):
        self.root = root
        self.lang = "FR"
        self.root.geometry("800x680")
        self.tab_control = ttk.Notebook(root)
        self.tab_tuteur = ttk.Frame(self.tab_control)
        self.tab_tutores = ttk.Frame(self.tab_control)
        self.tab_db = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_tuteur, text="")
        self.tab_control.add(self.tab_tutores, text="")
        self.tab_control.add(self.tab_db, text="")
        self.tab_control.pack(expand=1, fill="both")

        lang_frame = tk.Frame(root, bg="#f0f0f0")
        lang_frame.pack(side="top", fill="x")
        tk.Button(lang_frame, text="Francais", command=lambda: self.switch_lang("FR")).pack(side="right", padx=5, pady=2)
        tk.Button(lang_frame, text="English", command=lambda: self.switch_lang("EN")).pack(side="right", padx=5, pady=2)

        self.build_ui()
        self.refresh_apprenti_list()
        self.update_ui_text()

    def build_ui(self):
        self.lbl_tuteur_title = tk.Label(self.tab_tuteur, text="", font=("Arial", 14, "bold"))
        self.lbl_tuteur_title.pack(pady=10)
        frame_tuteur = tk.Frame(self.tab_tuteur)
        frame_tuteur.pack(pady=5)
        self.lbl_cat = tk.Label(frame_tuteur, text="")
        self.lbl_cat.grid(row=0, column=0, padx=5)
        self.cat_box = ttk.Combobox(frame_tuteur, values=[], state="readonly")
        self.cat_box.grid(row=0, column=1, padx=5)
        self.lbl_tuteur_content = tk.Label(self.tab_tuteur, text="")
        self.lbl_tuteur_content.pack(pady=5)
        self.tuteur_text = tk.Text(self.tab_tuteur, height=8, width=75)
        self.tuteur_text.pack(pady=5)
        self.btn_save_tuteur = tk.Button(self.tab_tuteur, text="", bg="#1d3557", fg="white", command=self.save_tuteur_note)
        self.btn_save_tuteur.pack(pady=5)

        self.lbl_tutores_title = tk.Label(self.tab_tutores, text="", font=("Arial", 14, "bold"))
        self.lbl_tutores_title.pack(pady=10)
        frame_tutores = tk.Frame(self.tab_tutores)
        frame_tutores.pack(pady=5)
        self.lbl_apprenti = tk.Label(frame_tutores, text="")
        self.lbl_apprenti.grid(row=0, column=0, padx=5)
        self.student_box = ttk.Combobox(frame_tutores, values=[], state="readonly")
        self.student_box.grid(row=0, column=1, padx=5)
        self.lbl_section = tk.Label(frame_tutores, text="")
        self.lbl_section.grid(row=0, column=2, padx=5)
        self.section_box = ttk.Combobox(frame_tutores, values=[], state="readonly")
        self.section_box.grid(row=0, column=3, padx=5)
        self.lbl_date = tk.Label(self.tab_tutores, text="")
        self.lbl_date.pack(pady=5)
        self.date_entry = tk.Entry(self.tab_tutores, width=20)
        self.date_entry.insert(0, "28/05/2026")
        self.date_entry.pack()
        self.lbl_details = tk.Label(self.tab_tutores, text="")
        self.lbl_details.pack(pady=5)
        self.student_text = tk.Text(self.tab_tutores, height=8, width=75)
        self.student_text.pack(pady=5)
        btn_frame = tk.Frame(self.tab_tutores)
        btn_frame.pack(pady=10)
        self.btn_save_student = tk.Button(btn_frame, text="", bg="#2a9d8f", fg="white", command=self.save_student_note)
        self.btn_save_student.pack(side="left", padx=5)
        self.btn_history = tk.Button(btn_frame, text="", bg="#e76f51", fg="white", command=self.view_history)
        self.btn_history.pack(side="left", padx=5)
        self.btn_export = tk.Button(self.tab_tutores, text="", bg="#4a4e69", fg="white", command=self.export_to_excel)
        self.btn_export.pack(pady=5)

        self.lbl_db_title = tk.Label(self.tab_db, text="", font=("Arial", 14, "bold"))
        self.lbl_db_title.pack(pady=10)
        self.lbl_db_path_tag = tk.Label(self.tab_db, text="", font=("Arial", 10, "bold"))
        self.lbl_db_path_tag.pack(pady=2)
        self.lbl_db_file_path = tk.Label(self.tab_db, text=os.path.abspath("tutorat_local.db"), fg="blue", bg="#e0e0e0", wraplength=700)
        self.lbl_db_file_path.pack(pady=5, padx=20)

        db_action_frame = tk.LabelFrame(self.tab_db, text=" Configuration ", padx=15, pady=15)
        db_action_frame.pack(pady=20, fill="x", padx=40)
        self.lbl_add_app = tk.Label(db_action_frame, text="")
        self.lbl_add_app.pack(anchor="w")
        self.new_app_entry = tk.Entry(db_action_frame, width=40)
        self.new_app_entry.pack(pady=5, anchor="w")
        self.btn_add_app = tk.Button(db_action_frame, text="", bg="#457b9d", fg="white", command=self.add_new_learner)
        self.btn_add_app.pack(pady=5, anchor="w")

    def refresh_apprenti_list(self):
        conn = sqlite3.connect("tutorat_local.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nom FROM liste_apprentis ORDER BY nom ASC")
        liste = [row[0] for row in cursor.fetchall()]
        conn.close()
        self.student_box.config(values=liste)
        if liste:
            self.student_box.current(0)

    def add_new_learner(self):
        t = TRANSLATIONS[self.lang]
        nom = self.new_app_entry.get().strip()
        if not nom:
            messagebox.showwarning("!", t["err_empty"])
            return
        try:
            conn = sqlite3.connect("tutorat_local.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO liste_apprentis (nom) VALUES (?)", (nom,))
            conn.commit()
            conn.close()
            messagebox.showinfo("OK", t["success_add"])
            self.new_app_entry.delete(0, tk.END)
            self.refresh_apprenti_list()
        except sqlite3.IntegrityError:
            messagebox.showwarning("!", "Cet apprenti existe deja." if self.lang == "FR" else "This learner already exists.")

    def switch_lang(self, lang):
        self.lang = lang
        self.update_ui_text()

    def update_ui_text(self):
        t = TRANSLATIONS[self.lang]
        self.root.title(t["title"])
        self.tab_control.tab(0, text=t["tab_tuteur"])
        self.tab_control.tab(1, text=t["tab_tutores"])
        self.tab_control.tab(2, text=t["tab_db"])
        self.lbl_tuteur_title.config(text=t["tuteur_title"])
        self.lbl_cat.config(text=t["category"])
        self.cat_box.config(values=t["cats"])
        self.cat_box.current(0)
        self.lbl_tuteur_content.config(text=t["content"])
        self.btn_save_tuteur.config(text=t["btn_save_tuteur"])
        self.lbl_tutores_title.config(text=t["tutores_title"])
        self.lbl_apprenti.config(text=t["apprenti"])
        self.lbl_section.config(text=t["section"])
        self.section_box.config(values=t["sections"])
        self.section_box.current(0)
        self.lbl_date.config(text=t["date"])
        self.lbl_details.config(text=t["details"])
        self.btn_save_student.config(text=t["btn_save_tutorat"])
        self.btn_history.config(text=t["btn_history"])
        self.btn_export.config(text=t["btn_export"])
        self.lbl_db_title.config(text=t["db_title"])
        self.lbl_db_path_tag.config(text=t["db_path"])
        self.lbl_add_app.config(text=t["add_app_lbl"])
        self.btn_add_app.config(text=t["btn_add_app"])

    def save_tuteur_note(self):
        t = TRANSLATIONS[self.lang]
        cat = self.cat_box.get()
        txt = self.tuteur_text.get("1.0", tk.END).strip()
        if not txt:
            messagebox.showwarning("!", t["err_empty"])
            return
        conn = sqlite3.connect("tutorat_local.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tuteur_notes (categorie, contenu) VALUES (?, ?)", (cat, txt))
        conn.commit()
        conn.close()
        messagebox.showinfo("OK", t["success_tuteur"])
        self.tuteur_text.delete("1.0", tk.END)

    def save_student_note(self):
        t = TRANSLATIONS[self.lang]
        nom = self.student_box.get()
        sec = self.section_box.get()
        date = self.date_entry.get()
        txt = self.student_text.get("1.0", tk.END).strip()
        if not txt or not nom:
            messagebox.showwarning("!", t["err_empty"])
            return
        conn = sqlite3.connect("tutorat_local.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tutores_suivi (nom_apprenti, type_note, date_note, details) VALUES (?, ?, ?, ?)", (nom, sec, date, txt))
        conn.commit()
        conn.close()
        messagebox.showinfo("OK", t["success_tutorat"].format(nom))
        self.student_text.delete("1.0", tk.END)

    def view_history(self):
        t = TRANSLATIONS[self.lang]
        nom_appr = self.student_box.get()
        if not nom_appr: return
        conn = sqlite3.connect("tutorat_local.db")
        cursor = conn.cursor()
        cursor.execute("SELECT date_note, type_note, details FROM tutores_suivi WHERE nom_apprenti = ? ORDER BY id DESC", (nom_appr,))
        rows = cursor.fetchall()
        conn.close()

        history_win = tk.Toplevel(self.root)
        history_win.title(t["history_title"].format(nom_appr))

        txt_area = tk.Text(history_win, wrap="word", padx=10, pady=10, width=60, height=20)
        txt_area.pack(expand=True, fill="both")
        if not rows:
            txt_area.insert(tk.END, t["no_data"])
        else:
            for row in rows:
                entry = f"Date: {row[0]} | Section: {row[1]}\n{row[2]}\n{'-'*50}\n"
                txt_area.insert(tk.END, entry)
        txt_area.config(state="disabled")

    def export_to_excel(self):
        t = TRANSLATIONS[self.lang]
        nom_appr = self.student_box.get()
        if not nom_appr: return
        filename = f"Rapport_{nom_appr.replace(' ', '_')}.csv"
        conn = sqlite3.connect("tutorat_local.db")
        cursor = conn.cursor()
        cursor.execute("SELECT date_note, type_note, details FROM tutores_suivi WHERE nom_apprenti = ? ORDER BY date_note ASC", (nom_appr,))
        rows = cursor.fetchall()
        conn.close()
        if not rows:
            messagebox.showwarning("!", t["no_data"])
            return
        with open(filename, mode="w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["Date", "Section / Type de Note", "Observations / Details"])
            for row in rows:
                writer.writerow([row[0], row[1], row[2]])
        messagebox.showinfo("Excel Export", t["export_success"].format(os.path.abspath(filename)))

if __name__ == "__main__":
    try:
        init_db()
        root = tk.Tk()
        app = TutoratApp(root)
        root.mainloop()
    except Exception as e:
        with open("erreur_log.txt", "w") as f:
            import traceback
            traceback.print_exc(file=f)

