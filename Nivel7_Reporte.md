# 📜 REPORTE DE NIVEL 7: HABILIDADES ESPECIALES (FUNCIONES)

**Proyecto:** `Pythonquest_Brandon`  
**Estudiante:** Brandon  
**Fecha:** 2026-09-04  
**Rango Alcanzado:** 🐍 Python Master  
**XP Acumulada:** 1010 XP  
**Progreso General:** 70%  

---

## 1. 📊 RESUMEN EJECUTIVO
Brandon dominó el uso de funciones en Python para estructurar código modular y reutilizable. Logró definir funciones personalizadas (`def`), enviarles información dinámica mediante parámetros y retornar resultados procesados mediante la instrucción `return`.

---

## 2. 🧠 CONCEPTOS DOMINADOS

| Concepto | Sintaxis en Python | Aplicación Real |
| :--- | :--- | :--- |
| **Definir Funciones** | `def mi_funcion():` | Empaquetar bloques de código reutilizables. |
| **Parámetros** | `def mi_funcion(a, b):` | Enviar variables de entrada a la función. |
| **Retorno de Valores**| `return resultado` | Entregar un cálculo procesado de vuelta al programa. |

---

## 3. ⚔️ CÓDIGO FINAL DE BATALLA (`boss7.py`)
```python
def generar_pocion(nombre_pocion, multiplicador):
    puntos_curacion = multiplicador * 25
    return puntos_curacion

def mostrar_estado(jugador, vida):
    print(" Jugador:", jugador)
    print(" Vida total:", vida)

puntos_curados = generar_pocion("Poción Mítica", 4)

print("--- ESTADO TRAS USAR POCIÓN ---")

mostrar_estado("Brandon", 100 + puntos_curados)
