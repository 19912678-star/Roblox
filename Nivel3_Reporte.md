# 📜 REPORTE DE NIVEL 3: INTERACCIÓN Y OPERADORES DE ROBLOX

**Proyecto:** `Pythonquest_Brandon`  
**Estudiante:** Brandon  
**Fecha:** 2026-08-28  
**Rango:** 🛡️ Constructor de Algoritmos  
**XP Acumulada:** 620 XP  
**Progreso General:** 30%  

---

## 1. 📊 RESUMEN EJECUTIVO
Brandon completó el Mundo 3 dominando la captura de datos del usuario, la conversión de cadenas a enteros y el cálculo de operaciones en tiempo real para generar salidas compuestas estilo tienda de Roblox.

---

## 2. 🧠 CONCEPTOS DOMINADOS

| Concepto | Sintaxis en Python | Aplicación Real |
| :--- | :--- | :--- |
| **Entrada de Texto** | `input()` | Capturar el nombre del avatar del usuario. |
| **Conversión a Entero** | `int(input())` | Transformar texto numérico a tipo entero para matemática. |
| **Resta y Operadores** | `a - b` | Calcular saldo final de Robux tras realizar una compra. |
| **Salida Formateada** | `print(var1, "texto", var2)` | Imprimir recibos de compra interactivos con comas. |

---

## 3. ⚔️ CÓDIGO FINAL DE BATALLA (`boss3.py`)
```python
nombre_avatar = input("¿Cuál es tu nombre de avatar? ")
robux_cuenta = int(input("cuantos_robux_tienes?"))
precio_objeto = int(input("cual_es_el_precio?"))
robux_finales = robux_cuenta - precio_objeto
print("Jugador", nombre_avatar, "compraste un objeto de", precio_objeto, "Robux. Te quedan", robux_finales, "Robux.")
