import math

def comprobar_rango():
    print("--Comprobar si un número cae en un rango determinado--")
    numero = float(input("Ingresa un número: "))
    minimo = float(input("Ingresa el valor mínimo del rango: "))
    maximo = float(input("Ingresa el valor máximo del rango: "))
    if minimo <= numero <= maximo:
        print(f"{numero} está en el rango entre {minimo} y {maximo}.")
    else:
        print(f"{numero} no está en el rango entre {minimo} y {maximo}.")