"""
Archivo principal del proyecto.
Autor: Javier Burgos
Fecha: 20/06/2025
Descripción: Este es un juego que la computadora generará un número aleatorio del 1 al 10
y el jugador deberá adivinar qué número es el que se eligió.
"""

'''
RETO NUEVO
🧠 Lógica:

El número a adivinar estará entre 1 y 100. LISTO

El jugador solo tendrá 7 intentos. LISTO

Después de cada intento, el juego mostrará una pista:

Si el número ingresado es menor al número secreto, mostrar: “Muy bajo, intenta un número más alto”.

Si es mayor, mostrar: “Muy alto, intenta uno más bajo”. LISTO

Si adivina antes de quedarse sin intentos, gana.

Si se queda sin intentos, mostrar: “¡Has perdido! El número era: X”.

💡 Interfaz:
Agrega una etiqueta que diga cuántos intentos le quedan.

Desactiva el botón “Adivinar” si se acaba el juego (ya sea por ganar o por perder).

Mantén el botón “Me rindo”.

💾 Bonus opcional:
Guarda en un archivo .txt cuántas veces ha ganado o perdido el usuario (contador simple).

'''

import tkinter as tk
from tkinter import messagebox
import random



# 1. Generar número aleatorio
numero_secreto = random.randint(1, 100)
numero_intentos = 7

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
    global numero_intentos
    try:
        intento = int(entrada.get())  # Convertir el texto ingresado a número
        if intento < 1 or intento > 100:
            messagebox.showwarning("Número inválido", "Debes ingresar un número del 1 al 100.")
            return

        if intento == numero_secreto:
            messagebox.showinfo("¡Correcto!", "JAJAJAJA ATINASTE! ganaste un coco 🥥")
            boton_adivinar.config(state="disabled")
            reiniciar_juego()
        else:
            #si es incorrecto jugador tiene 7 intentos
            if numero_intentos <= 1:
                boton_adivinar.config(state="disabled")
                messagebox.showerror("Incorrecto", f"¡PERDEDORRRR! ni con 7 intentos puedes jajajaja el número era {numero_secreto}")
                return
             
            else:
                numero_intentos -= 1
                etiqueta_intentos.config()
                if intento < numero_secreto:
                    
                    messagebox.showerror("Incorrecto", f"""vuelve a intentarlo tienes {numero_intentos} intentos de {numero_intentos + 1}
Tip: el número es muy bajo, intenta un número más alto""")
                    
                elif intento > numero_secreto:
                    messagebox.showerror("Incorrecto", f"""vuelve a intentarlo tienes {numero_intentos} intentos de {numero_intentos + 1}
Tip: el número es muy alto, intenta un número más bajo""")
                    
            #entrada.set("")  # Borrar el campo
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

#def guardar_txt():
    #aquí pondré la función para el guardado del txt y la llamaré cuando se cumpla el win o el losse del usuario.

# 7. Botones
boton_adivinar = tk.Button(ventana, text="Adivinar", font=("Arial", 16), command=validar_numero)
boton_adivinar.pack(pady=5)

boton_rendirse = tk.Button(ventana, text="Me rindo", font=("Arial", 16), fg="white", bg="red", command=rendirse)
boton_rendirse.pack(pady=5)

#Etiquetas:
etiqueta_intentos = tk.Label(ventana, text=f"Intentos disponibles: {numero_intentos}", font=("Arial", 16))
etiqueta_intentos.pack(pady=5)

# 8. Iniciar el loop de la app
ventana.mainloop()
