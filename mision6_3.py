inventario = ["Espada de Diamante", "Poción de Vida", "Escudo VIP"]

inventario.remove("Poción de Vida")

print("--- Objetos en la mochila ---")

for objeto in inventario:
    print("Mochila:", objeto)
    