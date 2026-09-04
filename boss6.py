mochila = ["Pistola de Agua", "Casco de Madera"]

mochila.append("Espada Mítica")

mochila.remove("Pistola de Agua")

print("Total de ítems en la mochila:", len(mochila))

print("--- EQUIPAMIENTO ACTUAL ---")

for item in mochila:
    print("Objeto:", item)
    