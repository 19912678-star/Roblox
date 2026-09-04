# 📜 REPORTE DE NIVEL 8: ARCHIVOS Y EXCEPCIONES

**Proyecto:** `Pythonquest_Brandon`  
**Estudiante:** Brandon  
**Fecha:** 2026-09-04  
**Rango Alcanzado:** 🐍 Python Master  
**XP Acumulada:** 1110 XP  
**Progreso General:** 80%  

---

## 1. 📊 RESUMEN EJECUTIVO
Brandon logró implementar la persistencia de datos y el manejo defensivo de errores en Python. Es capaz de prevenir fallos en ejecución mediante bloques de control de excepciones y almacenar información de manera duradera en el sistema de archivos del equipo.

---

## 2. 🧠 CONCEPTOS DOMINADOS

| Concepto | Sintaxis en Python | Aplicación Real |
| :--- | :--- | :--- |
| **Control de Errores** | `try:` / `except:` | Evita que el programa colapse ante datos inválidos. |
| **Escritura de Archivos** | `with open("archivo.txt", "w")` | Crea o sobrescribe información en disco. |
| **Lectura de Archivos** | `with open("archivo.txt", "r")` | Carga y lee información almacenada previamente. |

---

## 3. ⚔️ CÓDIGO FINAL DE BATALLA (`boss8.py`)
```python
try:
    gemas = int(input("¿Cuántas gemas obtuviste en la partida? "))

    with open("datastore.txt", "w") as archivo:
        archivo.write("Jugador: Brandon\n")
        archivo.write("Gemas: " + str(gemas) + "\n")

    print("💾 ¡Datos guardados correctamente en DataStore!")

    with open("datastore.txt", "r") as archivo:
        contenido = archivo.read()

    print("--- DATASTORE CARGADO ---")
    print(contenido)

except:
    print("⚠️ Error: Debes ingresar un número válido de gemas. La partida no se guardó.")
    