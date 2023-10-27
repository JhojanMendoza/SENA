def sumar_lista():
    print("--Sumar todos los números de una lista--")
    lista = [float(x) for x in input("Ingresa los números separados por espacios: ").split()]
    resultado = sum(lista)
    print(f"La suma de los números es: {resultado}")