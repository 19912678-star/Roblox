class JugadorRoblox:
    def __init__(self, usuario, nivel, gemas):
        self.usuario = usuario
        self.nivel = nivel
        self.gemas = gemas

    def ganar_gemas(self, cantidad):
        self.gemas += cantidad
        print("💎 ¡Has ganado", cantidad, "gemas! Total de gemas:", self.gemas)

    def mostrar_estado(self):
        print("🎮 Usuario:", self.usuario)
        print("⭐ Nivel:", self.nivel)
        print("💎 Gemas:", self.gemas)


jugador1 = JugadorRoblox("Brandon", 8, 100)

jugador1.mostrar_estado()

jugador1.ganar_gemas(50)

jugador1.mostrar_estado()
