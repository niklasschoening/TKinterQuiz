import tkinter as tk


class QuizSpiel:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Spiel")
        self.punkte = 0
        self.fragen = [
            {"Typ": "Text","frage": "Wie viele verschiedene Programmiersprachen gibt es?", "optionen": [
                "ca. 160", "mehrere Millionen", "ca 1.500", "kanpp 500.000"], "korrekt": 2},
            {"Typ": "Text", "frage": "Wie viele GHz Leistung hatte der erste PC?", "optionen": [
                "2 GHz", "0.001 GHz", "0.9 GHz", "4 GHz"], "korrekt": 1},
            {"Typ": "Text", "frage": "Wie viel Operationen führt ein modernes Handy pro Sekunde durch?", "optionen": [
                "genug für die Mondlandung", "5.000.000.000", "5 Billionen", "50.000"], "korrekt": 2},
            {"Typ": "Bild", "frage": "Was sieht man hier?", "Bild": "Falko.png", "optionen": [
                "0.1 mm", "1 Mikrometer", "1.4 cm^2", "30 Nanometer"], "korrekt": 3},
            {"Typ": "Text", "frage": "Was ist der größte Kontinent der Erde?", "optionen": [
                "Asien", "Afrika", "Nordamerika", "Australien"], "korrekt": 0}
        ]
        self.aktuelle_frage = 0

        self.frage_label = tk.Label(root, text="", width=50)
        self.frage_label.pack(pady=10)
        self.bild = tk.Image.open("falko.png")
        self.optionen_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", width=30,
                               command=lambda idx=i: self.pruefe_antwort(idx))
            button.pack(pady=5)
            self.optionen_buttons.append(button)

        self.punkte_label = tk.Label(root, text="Punkte: 0")
        self.punkte_label.pack(pady=5)

        self.aktualisiere_frage()

    def aktualisiere_frage(self):
        if self.aktuelle_frage < len(self.fragen):
            frage_daten = self.fragen[self.aktuelle_frage]
            self.frage_label.configure(text=frage_daten["frage"])
            optionen = frage_daten["optionen"]
            typ = frage_daten["Typ"]
            self.load(typ)
            for i in range(4):
                self.optionen_buttons[i].configure(text=optionen[i])
            self.aktuelle_frage += 1
        else:
            self.spiel_ende(0)

    def load(self, typ):
        if typ=="Text":
            print("text")
        if typ=="Bild":
            print("Bild")

    def pruefe_antwort(self, ausgewaehlte_option):
        frage_daten = self.fragen[self.aktuelle_frage - 1]
        korrekte_option = frage_daten["korrekt"]
        if ausgewaehlte_option == korrekte_option:
            if self.aktuelle_frage == 1:
                self.punkte += 100
            elif self.aktuelle_frage == 2:
                self.punkte += 200
            elif self.aktuelle_frage == 3:
                self.punkte += 500
            elif self.aktuelle_frage == 4:
                self.punkte += 1000

            self.punkte_label.configure(text="Punkte: {}".format(self.punkte))
            self.aktualisiere_frage()
        else:
            self.spiel_ende(1)

    def spiel_ende(self, x):
        if x==0:
            self.frage_label.configure(
                text="Spiel beendet. Herzlichen Glückwunsch zum Gewinn!")
        if x==1:
            self.frage_label.configure(
                text="Spiel beendet. Vielleicht schaffst du es beim nächsten Mal!")

        for button in self.optionen_buttons:
            button.configure(state=tk.DISABLED)


root = tk.Tk()
quiz_spiel = QuizSpiel(root)
root.mainloop()
