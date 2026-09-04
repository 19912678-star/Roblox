enemigos_totales = 0

oleadas = int(input("¿Cuántas oleadas quieres combatir? "))

for oleada in range(1, oleadas + 1):
    print("¡Spawneando Oleada", oleada, "!")
    enemigos_totales += 5

print("¡Victoria! Derrotaste a un total de", enemigos_totales, "enemigos.")
