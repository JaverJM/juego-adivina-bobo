import tkinter as tk
from tkinter import messagebox

def mostrar_dialogo():
    respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que quieres continuar?")
    if respuesta:
        print("Dijo que SÍ")
    else:
        print("Dijo que NO")

# Ventana principal
root = tk.Tk()
root.title("Ejemplo de diálogo")
root.geometry("300x200")

boton = tk.Button(root, text="Mostrar diálogo", command=mostrar_dialogo)
boton.pack(pady=60)

root.mainloop()