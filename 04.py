import tkinter as tk


def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Neues Fenster")
    new_window.geometry("200x100")
    label = tk.Label(new_window, text="Das ist ein neues Fenster!")
    label.pack()

    # Aktionen mit dem neuen Fenster
    new_window_label = tk.Label(new_window, text="Ein beliebiger Text.")
    new_window_label.pack()
    new_window.geometry("300x200")


root = tk.Tk()
root.title("Hauptfenster")
root.geometry("200x100")

button = tk.Button(root, text="Fenster öffnen", command=open_new_window)
button.pack()

root.mainloop()
