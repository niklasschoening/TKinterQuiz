import tkinter as tk

from tkinter import PhotoImage

def addiere_zahlen():
    zahl1 = int(eingabe1.get())
    zahl2 = int(eingabe2.get())
    ergebnis = zahl1 + zahl2
    ergebnis_label.config(text="Ergebnis: " + str(ergebnis))


# Erstellung des Hauptfensters
root = tk.Tk()
root.title("Zahlen addieren")
root.geometry("800x600")

# Laden des Fenster-Symbols (Favicon)
#favicon = PhotoImage(file="favicon.png")
#root.iconphoto(True, favicon)

# Erstellung der Benutzeroberflächenelemente
label1 = tk.Label(root, text="Erste Zahl:")
label1.pack()

eingabe1 = tk.Entry(root)
eingabe1.pack()

label2 = tk.Label(root, text="Zweite Zahl:")
label2.pack()

eingabe2 = tk.Entry(root)
eingabe2.pack()

button = tk.Button(root, text="Addieren", command=addiere_zahlen)
button.pack()

ergebnis_label = tk.Label(root, text="Ergebnis: ")
ergebnis_label.pack()

# Start der Hauptereignisschleife
root.mainloop()
