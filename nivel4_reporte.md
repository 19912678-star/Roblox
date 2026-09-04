# 📜 REPORTE DE NIVEL 4: EL CAMINO DE LAS DECISIONES

**Proyecto:** `Pythonquest_Brandon`  
**Estudiante:** Brandon  
**Fecha:** 2026-09-04  
**Rango Alcanzado:** 🧙 Maestro del Código  
**XP Acumulada:** 730 XP  
**Progreso General:** 40%  

---

## 1. 📊 RESUMEN EJECUTIVO
Brandon dominó el control de flujo condicional en Python. Es capaz de evaluar múltiples rutas de ejecución mediante `if`, `elif` y `else`, así como combinar requerimientos complejos con operadores lógicos `and` y `or`.

---

## 2. 🧠 CONCEPTOS DOMINADOS

| Concepto | Sintaxis en Python | Aplicación Real |
| :--- | :--- | :--- |
| **Condicional Simples** | `if` / `else` | Permitir o denegar el acceso a una zona VIP. |
| **Múltiples Rutas** | `elif` | Clasificar jugadores en rangos (Leyenda, Pro, Novato). |
| **Operadores Lógicos** | `and` / `or` | Validar requisitos compuestos (Pase VIP O Nivel + Robux). |

---

## 3. ⚔️ CÓDIGO FINAL DE BATALLA (`mision4_4.py`)
```python
nivel = int(input("¿Qué nivel eres? "))
robux = int(input("¿Cuántos Robux tienes? "))
pase_vip = input("¿Tienes pase VIP? (si/no): ")

if pase_vip == "si" or (nivel >= 30 and robux >= 100):
    print("¡Acceso concedido a la Zona Legendaria!")
elif nivel >= 15:
    print("Acceso parcial: Bienvenido a la Zona Pro.")
else:
    print("Acceso denegado: Requisitos insuficientes.")
    