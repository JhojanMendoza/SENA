import math

cateto1 = float(input("Ingrese la longitud del primer cateto: "))
cateto2 = float(input("Ingrese la longitud del segundo cateto: "))

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print("Teorema de Pitágoras")
print("--------------------------------------")
print ()
print("La longitud de la hipotenusa es:", hipotenusa)
print()