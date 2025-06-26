"""
Archivo principal del proyecto.
Autor: Javier Burgos
Fecha: 20/06/2025
Descripción: Este es un juego que la computadora generará un número aleatorio del 1 al 10
y el jugador deberá adivinar qué número es el que se eligió.
"""

'''

💾 Bonus opcional:
Guarda en un archivo .txt cuántas veces ha ganado o perdido el usuario (contador simple).

'''
# --- 1. IMPORTACIONES ---
import tkinter as tk
from tkinter import messagebox
import random


# --- 2. VARIABLES GLOBALES / CONFIGURACIÓN ---

# Generar número aleatorio
numero_secreto = random.randint(1, 100)
numero_intentos = 7

# --- 3. FUNCIONES DE LÓGICA ---

#Función para validar el número
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
            etiqueta_intentos.config(text="Lo lograste")
            guardar_resultado("Ganó")
            reiniciar_juego()
        else:
            #si es incorrecto jugador tiene 7 intentos
            if numero_intentos <= 1:
                messagebox.showerror("Incorrecto", f"¡PERDEDORRRR! ni con 7 intentos puedes jajajaja el número era {numero_secreto}")
                boton_adivinar.config(state="disabled")
                etiqueta_intentos.config(text="Jajaja no tienes intentos jajaja")
                guardar_resultado("Perdió")                
                return
             
            else:
                numero_intentos -= 1
                etiqueta_intentos.config(text=f"Intentos disponibles: {numero_intentos}")
                if intento < numero_secreto:
                    
                    messagebox.showerror("Incorrecto", "El número es muy bajo, intenta un número más alto")
                    
                elif intento > numero_secreto:
                    messagebox.showerror("Incorrecto", "El número es muy alto, intenta un número más bajo")
                    
            #entrada.set("")  # Borrar el campo
    except ValueError:
        messagebox.showwarning("Error", "Por favor ingresa un número válido.")

# Función para rendirse
def rendirse():
    messagebox.showinfo("Te rendiste", "JAJAJAJA SI ERES UN PER DE DOR!!!!!")
    ventana.destroy()  # Cerrar la ventana

# Función para reiniciar el juego
def reiniciar_juego():
    global numero_secreto
    numero_secreto = random.randint(1, 100)
    entrada.set("")

# Función para guardar las veces que jugador perdió y ganó en un TXT
def guardar_resultado(resultado):
    with open("partidas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(resultado + "\n")

# --- 4. INTERFAZ GRÁFICA (TKINTER)

def interfaz_ventanas():
    global ventana, selector
    
    # Crear ventana principal
    ventana = tk.Tk()
    ventana.title("Adivina el número")
    ventana.geometry("300x250")
    ventana.resizable(False, False)
    
    # Centrar ventana
    ventana.update_idletasks()
    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f"+{x}+{y}")

    # Crea ventana de selección
    selector = tk.Toplevel()
    selector.title("Selecciona la dificultad")
    selector.geometry("250x150")
    selector.transient(ventana)  # Asociar con ventana principal
    selector.grab_set()          # Bloquear interacción con ventana principal


def interfaz_widgets():
    global entrada, campo_entrada, boton_adivinar, boton_rendirse, etiqueta_intentos, boton_facil

    # --- VENTANA PRINCIPAL -- (ventana)
    # Entrada del usuario
    entrada = tk.StringVar()

    campo_entrada = tk.Entry(ventana, textvariable=entrada, font=("Arial", 20), justify='center')
    campo_entrada.pack(pady=20)

    # Botones
    boton_adivinar = tk.Button(ventana, text="Adivinar", font=("Arial", 16), command=validar_numero)
    boton_adivinar.pack(pady=5)

    boton_rendirse = tk.Button(ventana, text="Me rindo", font=("Arial", 16), fg="white", bg="red", command=rendirse)
    boton_rendirse.pack(pady=5)

    # Etiquetas
    etiqueta_intentos = tk.Label(ventana, text=f"Intentos disponibles: {numero_intentos}", font=("Arial", 16))
    etiqueta_intentos.pack(pady=5)

    # --- VENTANA SELECTOR DE DIFICULTAD --- (selector)

    etiqueta_dificultad = tk.Label(selector, text="Selecciona tu dificultad", font=("Arial", 16))
    etiqueta_dificultad.pack(pady=5)

    boton_facil = tk.Button(selector, text="Modo facil", font=("Arial")) # 16, command=lambda:)
    boton_facil.pack(pady=5)
                            

# --- 5. EJECUCIÓN PRINCIPAL ---

if __name__ == "__main__":
    ventana = interfaz_ventanas()
    ventana.mainloop()  # Aquí queda el programa "vivo"