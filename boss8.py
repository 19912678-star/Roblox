try:
    gemas = int(input("¿Cuántas gemas obtuviste en la partida? "))

    with open("datastore.txt", "w") as archivo:
        archivo.write("Jugador: Brandon\n")
        archivo.write("Gemas: " + str(gemas) + "\n")

    print("💾 ¡Datos guardados correctamente en DataStore!")

    with open("datastore.txt", "r") as archivo:
        contenido = archivo.read()

    print("--- DATASTORE CARGADO ---")
    print(contenido)

except:
    print(" Error: Debes ingresar un número válido de gemas. La partida no se guardó.")