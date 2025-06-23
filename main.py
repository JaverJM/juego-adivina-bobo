"""
Archivo principal del proyecto.
Autor: Javier Burgos
Fecha: 20/06/2025
Descripción: Este es un juego que la computadora generará un número aleatorio del 1 al 10
y el jugador deberá adivinar qué número es el que se eligió.
"""

import tkinter as tk
from tkinter import messagebox
import random

# 1. Generar número aleatorio
numero_secreto = random.randint(1, 10)

# 2. Crear ventana principal
ventana = tk.Tk()
ventana.title("Adivina el número")
ventana.geometry("300x250")
ventana.resizable(False, False)

# 3. Entrada del usuario
entrada = tk.StringVar()

campo_entrada = tk.Entry(ventana, textvariable=entrada, font=("Arial", 20), justify='center')
campo_entrada.pack(pady=20)

# 4. Función para validar el número
def validar_numero():
    try:
        intento = int(entrada.get())  # Convertir el texto ingresado a número
        if intento < 1 or intento > 10:
            messagebox.showwarning("Número inválido", "Debes ingresar un número del 1 al 10.")
            return

        if intento == numero_secreto:
            messagebox.showinfo("¡Correcto!", "JAJAJAJA ATINASTE! ganaste un coco 🥥")
            reiniciar_juego()
        else:
            messagebox.showerror("Incorrecto", "¡PERDEDORRRR!")
            entrada.set("")  # Borrar el campo
    except ValueError:
        messagebox.showwarning("Error", "Por favor ingresa un número válido.")

# 5. Función para rendirse
def rendirse():
    messagebox.showinfo("Te rendiste", "JAJAJAJA SI ERES UN PER DE DOR!!!!!")
    ventana.destroy()  # Cerrar la ventana

# 6. Función para reiniciar el juego
def reiniciar_juego():
    global numero_secreto
    numero_secreto = random.randint(1, 10)
    entrada.set("")

# 7. Botones
boton_adivinar = tk.Button(ventana, text="Adivinar", font=("Arial", 16), command=validar_numero)
boton_adivinar.pack(pady=5)

boton_rendirse = tk.Button(ventana, text="Me rindo", font=("Arial", 16), fg="white", bg="red", command=rendirse)
boton_rendirse.pack(pady=5)

# 8. Iniciar el loop de la app
ventana.mainloop()
