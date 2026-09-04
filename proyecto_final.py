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