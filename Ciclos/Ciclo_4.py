print("--Leer 10 Números y Calcular su Suma y Promedio--")
n = 10
total = 0

for i in range(n):
    num = float(input("Ingrese un número: "))
    total += num

promedio = total / n
print("La suma de los 10 números es:", total)
print("El promedio de los 10 números es:", promedio)
