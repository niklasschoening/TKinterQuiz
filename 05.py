import tkinter as tk
from PIL import ImageTk, Image


class Galerie:
    def __init__(self, master, bilder):
        self.master = master
        self.bilder = bilder

        self.bild_labels = []
        for bildpfad in self.bilder:
            bild = Image.open('Andi.jpg')
            bild = bild.resize((200, 200))  # Anpassung der Bildgröße
            foto = ImageTk.PhotoImage(bild)
            label = tk.Label(master, image=foto)
            label.image = foto
            self.bild_labels.append(label)

        # Anordnung der Bilder in zwei Reihen zu je vier Bildern
        for i, label in enumerate(self.bild_labels):
            reihe = i // 10
            spalte = i % 10
            label.grid(row=reihe, column=spalte)


# Pfade zu den Bildern
bildpfade = [
    "bild1.jpeg",
    "bild2.jpeg",
    "bild3.jpeg",
    "bild4.jpeg",
    "bild5.jpeg",
    "bild6.jpeg",
    "bild7.jpeg",
    "bild8.jpeg",
    "bild9.jpeg",
    "bild10.jpeg",
    "bild11.jpeg",
    "bild12.jpeg",
    "bild13.jpeg",
    "bild14.jpeg",
    "bild15.jpeg",
    "bild16.jpeg",
    "bild1.jpeg",
    "bild2.jpeg",
    "bild3.jpeg",
    "bild4.jpeg",
    "bild5.jpeg",
    "bild6.jpeg",
    "bild7.jpeg",
    "bild8.jpeg",
    "bild9.jpeg",
    "bild10.jpeg",
    "bild11.jpeg",
    "bild12.jpeg",
    "bild13.jpeg",
    "bild14.jpeg",
    "bild15.jpeg",
    "bild16.jpeg",
    "bild1.jpeg",
    "bild2.jpeg",
    "bild3.jpeg",
    "bild4.jpeg",
    "bild5.jpeg",
    "bild6.jpeg",
    "bild7.jpeg",
    "bild8.jpeg",
    "bild9.jpeg",
    "bild10.jpeg",
    "bild11.jpeg",
    "bild12.jpeg",
    "bild13.jpeg",
    "bild14.jpeg",
    "bild15.jpeg",
    "bild16.jpeg",
    "bild1.jpeg",
    "bild2.jpeg",
    "bild3.jpeg",
    "bild4.jpeg",
    "bild5.jpeg",
    "bild6.jpeg",
    "bild7.jpeg",
    "bild8.jpeg",
    "bild9.jpeg",
    "bild10.jpeg",
    "bild11.jpeg",
    "bild12.jpeg",
    "bild13.jpeg",
    "bild14.jpeg",
    "bild15.jpeg",
    "bild16.jpeg"
]

# Erstellung des Hauptfensters
root = tk.Tk()
root.title("Bildergalerie")

# Erstellung einer Galerie-Instanz mit den Bildern
galerie = Galerie(root, bildpfade)

# Start der Hauptprogrammschleife
root.mainloop()
