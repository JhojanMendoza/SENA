print("--Patrón Pirámide con Números--")
def piramide(n):
    num = 1

    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")
        
        for k in range(1, i + 1):
            print(num, end=" ")
            num += 1
        
        print()

n = 4
piramide(n)
