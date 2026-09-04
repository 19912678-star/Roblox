def generar_pocion(nombre_pocion, multiplicador):
    puntos_curacion = multiplicador * 25
    return puntos_curacion


def mostrar_estado(jugador, vida):
    print(" Jugador:", jugador)
    print(" Vida total:", vida)


puntos_curados = generar_pocion("Poción Mítica", 4)

print("--- ESTADO TRAS USAR POCIÓN ---")

mostrar_estado("Brandon", 100 + puntos_curados)