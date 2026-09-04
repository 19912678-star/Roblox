# 📜 REPORTE DE NIVEL 9: EL REINO DE LOS OBJETOS (POO)

**Proyecto:** `Pythonquest_Brandon`  
**Estudiante:** Brandon  
**Fecha:** 2026-09-04  
**Rango Alcanzado:** 🐍 Python Master  
**XP Acumulada:** 1210 XP  
**Progreso General:** 90%  

---

## 1. 📊 RESUMEN EJECUTIVO
Brandon dominó los fundamentos de la Programación Orientada a Objetos (POO). Logró comprender la abstracción de clases como moldes de software, el uso del constructor `__init__`, la referencia `self` para manejar estados internos y la ejecución de métodos para modificar atributos dinámicamente.

---

## 2. 🧠 CONCEPTOS DOMINADOS

| Concepto | Sintaxis en Python | Aplicación Real |
| :--- | :--- | :--- |
| **Clase (`class`)** | `class NombreClase:` | Plano o molde para crear múltiples objetos. |
| **Constructor** | `def __init__(self, ...):` | Inicializa los atributos de cada nuevo objeto. |
| **Atributos de Instancia**| `self.atributo = valor` | Almacena el estado o datos únicos del objeto. |
| **Métodos de Clase** | `def metodo(self):` | Acciones que realiza un objeto con sus datos. |

---

## 3. ⚔️ CÓDIGO FINAL DE BATALLA (`boss9.py`)
```python
class MascotaRoblox:
    def __init__(self, nombre, especie, fuerza):
        self.nombre = nombre
        self.especie = especie
        self.fuerza = fuerza
        self.nivel = 1

    def entrenar(self):
        self.nivel += 1
        self.fuerza += 15
        print("🏋️ ¡", self.nombre, "ha entrenado! Nuevo nivel:", self.nivel, "| Nueva fuerza:", self.fuerza)

    def mostrar_ficha(self):
        print("Nombre:", self.nombre)
        print("Especie:", self.especie)
        print("Nivel:", self.nivel)
        print("Fuerza:", self.fuerza)

mascota1 = MascotaRoblox("Dragón", "Dragón", 50)
mascota2 = MascotaRoblox("Lobo", "Lobo", 40)

print("--- FICHA DE MASCOTA 1 ---")
mascota1.mostrar_ficha()

print("--- FICHA DE MASCOTA 2 ---")
mascota2.mostrar_ficha()

mascota1.entrenar()

print("--- FICHA DE MASCOTA ENTRENADA ---")
mascota1.mostrar_ficha()