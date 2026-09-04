nivel = int(input("¿Qué nivel eres? "))
robux = int(input("¿Cuántos Robux tienes? "))
pase_vip = input("¿Tienes pase VIP? (si/no): ")

if pase_vip == "si" or (nivel >= 30 and robux >= 100):
    print("¡Acceso concedido a la Zona Legendaria!")
elif nivel >= 15:
    print("Acceso parcial: Bienvenido a la Zona Pro.")
else:
    print("Acceso denegado: Requisitos insuficientes.")
    