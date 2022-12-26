import tkinter as tk
from tkinter import filedialog

# Muestra la ventana emergente para seleccionar la carpeta
carpeta_seleccionada = filedialog.askdirectory()

# Imprime la ruta de la carpeta seleccionada
print(carpeta_seleccionada)