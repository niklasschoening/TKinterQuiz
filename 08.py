import tkinter as tk
from PIL import ImageTk, Image

# Funktion zur Behandlung des Klicks auf ein Bild
def check_image(image_num):
    if image_num == 1:
        result_label.config(text="Richtig!")
    else:
        result_label.config(text="Falsch!")

# Fenster erstellen
window = tk.Tk()
window.title("Bildspiel")
window.geometry("400x300")

# Bilder laden
image1 = ImageTk.PhotoImage(Image.open("bild1.png"))
image2 = ImageTk.PhotoImage(Image.open("bild2.png"))
image3 = ImageTk.PhotoImage(Image.open("bild3.png"))
image4 = ImageTk.PhotoImage(Image.open("bild4.png"))

# Buttons mit Bildern erstellen
button1 = tk.Button(window, image=image1, command=lambda: check_image(1))
button2 = tk.Button(window, image=image2, command=lambda: check_image(2))
button3 = tk.Button(window, image=image3, command=lambda: check_image(3))
button4 = tk.Button(window, image=image4, command=lambda: check_image(4))

# Buttons im Fenster platzieren
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=1, column=0)
button4.grid(row=1, column=1)

# Label für das Ergebnis erstellen
result_label = tk.Label(window, text="")
result_label.grid(row=2, columnspan=2)

# Hauptloop starten, um das Fenster anzuzeigen
window.mainloop()
