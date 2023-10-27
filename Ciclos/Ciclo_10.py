print("--Patrón Z con Asteriscos--")
n = 7

for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        for j in range(n - i - 1):
            print(" ", end="")
        print("*")
