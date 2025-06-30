# Juego Adivina-Bobo

**Autor:** Javier Burgos  
**Fecha:** 20/06/2025  

---

## Descripción

Adivina-Bobo es un juego sencillo en Python donde la computadora genera un número aleatorio y el jugador debe adivinarlo en un número limitado de intentos. El juego cuenta con interfaz gráfica usando Tkinter y guarda los resultados en un archivo de texto.

---

## Funcionalidades

- Juego con interfaz gráfica (Tkinter).  
- Niveles de dificultad ajustables.
- Guarda récords de partidas ganadas y perdidas en un archivo `.txt`. 
- Archivo ejecutable disponible para Windows (`adivina-bobo.exe`).  

## Nueva característica: Registro de partidas en SQLite

El juego ahora guarda automáticamente el resultado de cada partida en una base de datos llamada `partidas.db`. Se almacena:

- Resultado: Ganó o Perdió
- Nivel de dificultad elegido
- Número secreto generado
- Intentos disponibles al comenzar
- Fecha en que se jugó las partidas

Esto permite a futuro ver estadísticas o analizar el historial de juegos.


---

## Cómo jugar

1. Descarga el archivo ejecutable desde la sección [Releases](https://github.com/JavierJM99/juego-adivina-bobo/releases).  
2. Ejecuta `adivina-bobo.exe` en tu computadora Windows.  
3. Sigue las instrucciones en pantalla para adivinar el número.  

---

## Para desarrolladores

Si quieres descargar el código y probarlo en tu entorno:

```bash
git clone https://github.com/JavierJM99/juego-adivina-bobo.git
cd juego-adivina-bobo
python -m venv venv
source venv/bin/activate   # o venv\Scripts\activate en Windows
pip install -r requirements.txt   # si lo tienes, sino puedes omitir este paso
python main.py

```

## Contacto
Si tienes preguntas o sugerencias, no dudes en contactarme.

¡Gracias por jugar Adivina-Bobo! 🎮


