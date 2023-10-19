precio = float(input("Ingrese el valor unitario del producto: "))
cantidad = int(input("Ingrese la cantidad de productos comprados: "))

tsin = precio * cantidad

tcon = tsin * 1.16

print ("Total Compra")
print ("--------------------------------------")
print ()
print("El valor total a pagar con IVA es:", tcon)
print ()
