def multiplicar_lista():
    print("--Multiplicar todos los números de una lista--")
    lista = [float(x) for x in input("Ingresa los números separados por espacios: ").split()]
    resultado = 1
    for numero in lista:
        resultado *= numero
    print(f"La multiplicación de los números es: {resultado}")