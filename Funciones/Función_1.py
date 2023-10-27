def encontrar_mayor():
    print("--Encontrar el número mayor--")
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    c = int(input("Ingresa el tercer número: "))
    if a > b:
        mayor = a
    else:
        mayor = b

    if c > mayor:
        mayor = c

    print(f"El número mayor es {mayor}")