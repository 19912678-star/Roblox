class JugadorRoblox:
    def __init__(self, usuario, nivel):
        self.usuario = usuario
        self.nivel = nivel


jugador1 = JugadorRoblox("Brandon", 8)

print(" Usuario:", jugador1.usuario)
print(" Nivel:", jugador1.nivel)
