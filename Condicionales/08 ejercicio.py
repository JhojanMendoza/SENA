print("-- Ordenar Tres Números --")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
numeros = [num1, num2, num3]
numeros.sort()
print("En orden ascendente:", numeros)
numeros.sort(reverse=True)
print("En orden descendente:", numeros)

