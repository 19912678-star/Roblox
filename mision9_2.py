class JugadorRoblox:
    def __init__(self, usuario, nivel):
        self.usuario = usuario
        self.nivel = nivel

    def presentarse(self):
        print("🎮 Hola, mi usuario es", self.usuario, "y soy nivel", self.nivel)


jugador1 = JugadorRoblox("Brandon", 8)

jugador1.presentarse()
