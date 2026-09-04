class MascotaRoblox:
    def __init__(self, nombre, especie, fuerza):
        self.nombre = nombre
        self.especie = especie
        self.fuerza = fuerza
        self.nivel = 1

    def entrenar(self):
        self.nivel += 1
        self.fuerza += 15
        print("¡", self.nombre, "ha entrenado! Nuevo nivel:", self.nivel, "| Nueva fuerza:", self.fuerza)

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