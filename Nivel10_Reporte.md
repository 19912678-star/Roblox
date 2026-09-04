# 📜 REPORTE FINAL: MAESTRO DE PYTHON (PROYECTO INTEGRADOR)

**Proyecto:** `Pythonquest_Brandon`  
**Estudiante:** Brandon  
**Fecha:** 2026-09-04  
**Rango Alcanzado:** 🐍 Python Master  
**XP Acumulada:** 1320 XP  
**Progreso General:** 100%  

---

## 1. 📊 RESUMEN EJECUTIVO
Brandon ha completado exitosamente la totalidad del programa Python Quest, demostrando dominio práctico desde los conceptos fundamentales de sintaxis hasta el diseño modular mediante Programación Orientada a Objetos, persistencia de datos en disco duro y control de excepciones.

---

## 2. 🧠 COMPETENCIAS DOMINADAS

| Mundo | Conceptos Clave | Estado |
| :--- | :--- | :--- |
| **Mundo 1** | `print()`, sintaxis inicial, algoritmos | ✅ Dominado |
| **Mundo 2** | Variables, `str`, `int`, `float`, `bool` | ✅ Dominado |
| **Mundo 3** | `input()`, operadores matemáticos y f-strings | ✅ Dominado |
| **Mundo 4** | Condicionales `if`, `elif`, `else` | ✅ Dominado |
| **Mundo 5** | Ciclos `while`, `for`, contadores | ✅ Dominado |
| **Mundo 6** | Colecciones, listas, `.append()` | ✅ Dominado |
| **Mundo 7** | Funciones `def` y parámetros | ✅ Dominado |
| **Mundo 8** | Lectura/escritura `.txt` y `try/except` | ✅ Dominado |
| **Mundo 9** | POO, clases, `__init__`, `self`, métodos | ✅ Dominado |
| **Mundo 10**| Proyecto Final Integrador de Software | ✅ Dominado |

---

## 3. ⚔️ CÓDIGO DEL PROYECTO FINAL (`proyecto_final.py`)
```python
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.gemas = 50
        self.inventario = ["Espada de Madera"]

    def mostrar_stats(self):
        print("🎮 Nombre:", self.nombre)
        print("⭐ Nivel:", self.nivel)
        print("💎 Gemas:", self.gemas)
        print("🎒 Inventario:", self.inventario)

    def entrenar(self):
        self.nivel += 1
        self.gemas += 25
        print("🏋️ ¡Entrenaste duro! Subiste a Nivel", self.nivel, "y ganaste 25 gemas.")

    def comprar_item(self, nombre_item, precio):
        if self.gemas >= precio:
            self.gemas -= precio
            self.inventario.append(nombre_item)
            print("🛍️ ¡Compraste", nombre_item, "exitosamente!")
        else:
            print("⚠️ No tienes suficientes gemas para comprar", nombre_item)

    def guardar_datos(self):
        with open("partida.txt", "w") as archivo:
            archivo.write(f"Jugador: {self.nombre}\n")
            archivo.write(f"Nivel: {self.nivel}\n")
            archivo.write(f"Gemas: {self.gemas}\n")
            archivo.write(f"Inventario: {self.inventario}\n")

        print("💾 ¡Partida guardada exitosamente en partida.txt!")


nombre = input("¿Cuál es tu nombre? ")
jugador = Jugador(nombre)

while True:
    print("\n=== ROBLOX SIMULATOR PYTHON ===")
    print("1. Ver Estadísticas")
    print("2. Entrenar (+1 Nivel, +25 Gemas)")
    print("3. Comprar Poción de Fuerza (30 Gemas)")
    print("4. Guardar Partida")
    print("5. Salir")

    try:
        opcion = input("Elige una opción: ")

        if opcion == "1":
            jugador.mostrar_stats()

        elif opcion == "2":
            jugador.entrenar()

        elif opcion == "3":
            jugador.comprar_item("Poción de Fuerza", 30)

        elif opcion == "4":
            jugador.guardar_datos()

        elif opcion == "5":
            print("¡Gracias por jugar!")
            break

        else:
            print("⚠️ Entrada no válida. Intenta de nuevo.")

    except:
        print("⚠️ Entrada no válida. Intenta de nuevo.")
        