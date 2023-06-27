import tkinter as tk
import random


class QuizSpiel:
    def __init__(self, fragen):
        self.fragen = fragen
        self.aktuelle_frage = None
        self.punktzahl = 0

        self.fenster = tk.Tk()
        self.fenster.title("Quiz Spiel")

        self.frage_label = tk.Label(
            self.fenster, text="", width=50, wraplength=400)
        self.frage_label.pack(pady=20)

        self.antwort_buttons = []
        for i in range(4):
            button = tk.Button(self.fenster, text="", width=40,
                               command=lambda i=i: self.pruefe_antwort(i))
            button.pack(pady=5)
            self.antwort_buttons.append(button)

        self.punktzahl_label = tk.Label(self.fenster, text="Punktzahl: 0")
        self.punktzahl_label.pack(pady=20)

        self.load_frage()
        self.fenster.mainloop()

    def load_frage(self):
        self.aktuelle_frage = random.choice(self.fragen)
        self.frage_label.config(text=self.aktuelle_frage["frage"])

        random.shuffle(self.aktuelle_frage["antworten"])
        for i in range(4):
            self.antwort_buttons[i].config(
                text=self.aktuelle_frage["antworten"][i])

    def pruefe_antwort(self, ausgewaehlter_index):
        ausgewaehlte_antwort = self.aktuelle_frage["antworten"][ausgewaehlter_index]
        if ausgewaehlte_antwort == self.aktuelle_frage["korrekte_antwort"]:
            self.punktzahl += 1
        self.punktzahl_label.config(text="Punktzahl: " + str(self.punktzahl))
        if self.punktzahl == 5:
            self.fenster.destroy()
        else:
            self.load_frage()


# Fragenkatalog
fragen = [
    {
        "frage": "Was ist die Hauptstadt von Frankreich?",
        "antworten": ["Paris", "London", "Berlin", "Madrid"],
        "korrekte_antwort": "Paris"
    },
    {
        "frage": "Was ist 2 + 2?",
        "antworten": ["1", "3", "4", "5"],
        "korrekte_antwort": "4"
    },
    # Fügen Sie weitere Fragen hinzu
]

spiel = QuizSpiel(fragen)
