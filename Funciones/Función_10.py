import math

def verificar_primo():
    print("--Verificar si un número es primo--")
    numero = int(input("Ingresa un número: "))
    es_primo = True
    if numero <= 1:
        es_primo = False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")