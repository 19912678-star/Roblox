energia = int(input("¿Cuánta energía tienes? "))
escudo = input("¿Tienes el escudo activado? (si/no): ")

if energia >= 50 and escudo == "si":
    print("¡Modo Invencible Activado!")
else:
    print("Requisitos insuficientes para el Modo Invencible.")