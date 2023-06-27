import tkinter as tk

# Erstellung des Hauptfensters
root = tk.Tk()
root.title("Text auf rosa Hintergrund")
root.configure(bg="light pink")  # Einstellung des rosa Hintergrunds

# Ändern der Fenstergröße auf 800x600
root.geometry("800x600")

# Erste Zeile Text (linksbündig)
label1 = tk.Label(root, text="Erste Zeile", font=(
    "Arial", 20), fg="blue", anchor="w", justify="left")
label1.pack(anchor="w")

# Zweite Zeile Text (zentriert)
label2 = tk.Label(root, text="Zweite Zeile", font=(
    "Courier", 30), fg="green", anchor="center")
label2.pack()

# Dritte Zeile Text (rechtsbündig)
label3 = tk.Label(root, text="Dritte Zeile", font=(
    "Times New Roman", 40), fg="red", anchor="e", justify="right")
label3.pack(anchor="e")

# Start der Hauptprogrammschleife
root.mainloop()