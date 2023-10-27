print("--Serie Fibonacci y su Suma--")
n = int(input("Ingrese el número de términos de la serie Fibonacci: "))
a, b = 0, 1
sum_fibonacci = 0

for i in range(n):
    print(a, end=" ")
    sum_fibonacci += a
    a, b = b, a + b

print("\nLa suma de los primeros", n, "términos de la serie Fibonacci es:", sum_fibonacci)
