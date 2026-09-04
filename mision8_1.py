try:
    cantidad = int(input("¿Cuántas pociones quieres comprar? "))
    costo = cantidad * 10
    print("Total a pagar:", costo, "gemas.")
except:
    print(" Entrada inválida. Ingresa un número entero.")
    