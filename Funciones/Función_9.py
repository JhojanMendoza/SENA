def obtener_elementos_unicos():
    print("--Obtener elementos únicos de una lista--")
    entrada = input("Ingresa una lista de elementos separados por espacios: ")
    lista = entrada.split() 
    resultado = list(set(lista))
    print(f"Elementos únicos: {resultado}")
