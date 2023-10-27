print("--Calcular el Factorial de un Número--")
num = int(input("Ingrese un número para calcular su factorial: "))
factorial = 1

if num < 0:
    print("No se puede calcular el factorial de un número negativo.")
elif num == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("El factorial de", num, "es", factorial)
