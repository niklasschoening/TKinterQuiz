import tkinter as tk
from PIL import ImageTk, Image


class Galerie:
    def __init__(self, master, bilder):
        self.master = master
        self.bilder = bilder
        self.aktuelles_bild = 0

        self.bild_label = tk.Label(master)
        self.bild_label.pack()

        self.vorheriges_button = tk.Button(
            master, text="Vorheriges", command=self.zeige_vorheriges_bild)
        self.vorheriges_button.pack(side=tk.LEFT)

        self.nächstes_button = tk.Button(
            master, text="Nächstes", command=self.zeige_nächstes_bild)
        self.nächstes_button.pack(side=tk.RIGHT)

    def zeige_bild(self):
        bildpfad = self.bilder[self.aktuelles_bild]
        bild = Image.open('falko.png')
        bild = bild.resize((400, 400))  # Anpassung der Bildgröße
        foto = ImageTk.PhotoImage(bild)
        self.bild_label.configure(image=foto)
        self.bild_label.image = foto

    def zeige_nächstes_bild(self):
        self.aktuelles_bild = (self.aktuelles_bild + 1) % len(self.bilder)
        self.zeige_bild()

    def zeige_vorheriges_bild(self):
        self.aktuelles_bild = (self.aktuelles_bild - 1) % len(self.bilder)
        self.zeige_bild()


# Pfade zu den Bildern
bildpfade = [
    "bild1.jpeg",
    "bild2.jpeg",
    "bild3.jpeg",
    "bild4.jpeg",
    "bild5.jpeg",
    "bild6.jpeg",
    "bild7.jpeg",
    "bild8.jpeg"
]

# Erstellung des Hauptfensters
root = tk.Tk()
root.title("Bildergalerie")

# Erstellung einer Galerie-Instanz mit den Bildern
galerie = Galerie(root, bildpfade)

# Anzeige des ersten Bildes
galerie.zeige_bild()

# Start der Hauptprogrammschleife
root.mainloop()
