import tkinter as tk
from tkinter import filedialog

# Crea la ventana principal
root = tk.Tk()

# Define la función que se ejecutará al apretar el botón
def seleccionar_carpeta():
    # Muestra la ventana emergente para seleccionar la carpeta
    carpeta_seleccionada = filedialog.askdirectory()
    print(carpeta_seleccionada)

# Crea el botón
boton = tk.Button(root, text="Seleccionar carpeta", command=seleccionar_carpeta)

# Muestra el botón en la ventana principal
boton.pack()

# Inicia el bucle de eventos de la ventana
root.mainloop()