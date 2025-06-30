"""
Archivo principal del proyecto.
Autor: Javier Burgos
Fecha: 20/06/2025
Descripción: Este es un juego que la computadora generará un número aleatorio del 1 al 10
y el jugador deberá adivinar qué número es el que se eligió.
"""

# --- 1. IMPORTACIONES ---
import tkinter as tk
from tkinter import messagebox
import random
import sqlite3
from datetime import datetime
import os



# --- 2. VARIABLES GLOBALES / CONFIGURACIÓN ---

# Generar número aleatorio
limite_intento_max = 2
numero_secreto = random.randint(1, limite_intento_max)
numero_intentos = ""
resultado_juego = ""

# --- 3. FUNCIONES DE LÓGICA ---

def inicializar_db():
    conexion = sqlite3.connect("datos_partidas.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS partidas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            dificultad TEXT,
            numero_secreto INTEGER,
            intento_final INTEGER,
            resultado TEXT
        )
    ''')
    conexion.commit()
    conexion.close()

# --- 4. FUNCIONES DE LÓGICA ---

#Función para validar el número
def validar_numero():
    global numero_intentos, limite_intento_max, dificultad_actual, resultado_juego
    try:
        intento = int(entrada.get())  # Convertir el texto ingresado a número
        if intento < 1 or intento > limite_intento_max:
            messagebox.showwarning("Número inválido", f"Debes ingresar un número del 1 al {limite_intento_max}.")
            return

        if intento == numero_secreto:
            messagebox.showinfo("¡Correcto!", "JAJAJAJA ¡ATINASTE! Ganaste un coco 🥥")
            boton_adivinar.config(state="disabled")
            campo_entrada.config(state="disabled")
            etiqueta_intentos.config(text="Lo lograste")
            boton_rendirse.config(text="Terminar", fg="#28a745", bg="#FFFFFF")
            resultado_juego = "Ganó"
            guardar_resultado("Ganó")
            guardar_resultado_sql("Ganó", dificultad_actual, intento)  # Por ejemplo
            reiniciar_juego()
        else:
            #si es incorrecto jugador tiene 7 intentos
            if numero_intentos <= 1:
                messagebox.showerror("Incorrecto", f"¡PERDEDORRRR! Ni con {numero_intentos} intentos puedes jajajaja, el número era {numero_secreto}")
                boton_adivinar.config(state="disabled")
                campo_entrada.config(state="disabled")
                etiqueta_intentos.config(text="Jajaja no tienes intentos jajaja")
                resultado_juego = "Perdió"
                guardar_resultado("Perdió")     
                guardar_resultado_sql("Perdió", dificultad_actual, intento)  # Por ejemplo           
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

# Función selector dificultad
def seleccionar_dificultad(Nivel):
    global numero_intentos, limite_intento_max, dificultad_actual
    
    configuraciones = {
        "Facil":    {"limite": 10,    "intentos": 3},
        "Medio":    {"limite": 50,    "intentos": 5},
        "Difícil":  {"limite": 100,   "intentos": 10},
        "Extremo":  {"limite": 500,   "intentos": 15},
        "Injusto":  {"limite": 1000,  "intentos": 10},
        "Imposible":{"limite": 10000, "intentos": 3}
    }
    
    if Nivel in configuraciones:
        limite_intento_max = configuraciones[Nivel]["limite"]
        numero_intentos = configuraciones[Nivel]["intentos"]
        dificultad_actual = Nivel
    else:
        # Por si llega un valor no esperado
        print("Dificultad no reconocida")

    #Actualizar etiqueta de intentos:
    etiqueta_intentos.config(text=f"Número de intentos: {numero_intentos}")

    #Cerrar ventana del selector    
    selector.destroy()


# Función para rendirse
def rendirse():
    if resultado_juego == "Ganó":
        messagebox.showinfo("Lo Lograste", "Bien hecho campeón, disfruta tu coco")
        ventana.destroy()  # Cerrar la ventana    
    elif resultado_juego == "Perdió":
        messagebox.showinfo("Te rendiste", "JAJAJAJA SI ERES ¡¡¡¡¡UN PER DE DOR!!!!!")
        ventana.destroy()  # Cerrar la ventana       


# Función para reiniciar el juego
def reiniciar_juego():
    global numero_secreto, limite_intento_max
    numero_secreto = random.randint(1, limite_intento_max)
    entrada.set("")

# Función para guardar las veces que jugador perdió y ganó en un TXT y SQL
def guardar_resultado(resultado):
    with open("partidas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{resultado} - Dificultad: {dificultad_actual}\n")

def guardar_resultado_sql(resultado, dificultad, intento_final):
    conexion = sqlite3.connect("datos_partidas.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO partidas (fecha, dificultad, numero_secreto, intento_final, resultado) VALUES (?, ?, ?, ?, ?)", (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        dificultad,
        numero_secreto,
        intento_final,
        resultado
    ))
    conexion.commit()
    conexion.close()

# --- 5. INTERFAZ GRÁFICA (TKINTER) ---

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
    selector.geometry("250x400")
    selector.transient(ventana)  # Asociar con ventana principal
    selector.grab_set()          # Bloquear interacción con ventana principal

    selector.update_idletasks()
    ancho = selector.winfo_width()
    alto = selector.winfo_height()
    pantalla_ancho = selector.winfo_screenwidth()
    pantalla_alto = selector.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    selector.geometry(f"+{x}+{y}")


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

    tk.Label(selector, text="Selecciona tu dificultad", font=("Arial", 16)).pack(pady=5) 

    tk.Button(selector, text="Modo facil", font=("Arial", 16), fg="#ffffff", bg="#28a745", command=lambda:seleccionar_dificultad("Facil")).pack(pady=5)
    tk.Button(selector, text="Modo Medio", font=("Arial", 16), fg="#000000", bg="#fd7e14", command=lambda:seleccionar_dificultad("Medio")).pack(pady=5)
    tk.Button(selector, text="Modo Difícil", font=("Arial", 16), fg="#ffffff", bg="#dc3545", command=lambda:seleccionar_dificultad("Difícil")).pack(pady=5)
    tk.Button(selector, text="Modo Extremo", font=("Arial", 16), fg="#ffffff", bg="#8B0000", command=lambda:seleccionar_dificultad("Extremo")).pack(pady=5)
    tk.Button(selector, text="Modo Injusto", font=("Arial", 16), fg="#FF0000", bg="#4B0000", command=lambda:seleccionar_dificultad("Injusto")).pack(pady=5)
    tk.Button(selector, text="Modo Imposible", font=("Arial", 16), fg="#FF0000", bg="#000000", command=lambda:seleccionar_dificultad("Imposible")).pack(pady=5)

# --- 6. EJECUCIÓN PRINCIPAL ---

if __name__ == "__main__":
    inicializar_db()
    interfaz_ventanas()
    interfaz_widgets()
    ventana.mainloop()  # Aquí queda el programa "vivo"