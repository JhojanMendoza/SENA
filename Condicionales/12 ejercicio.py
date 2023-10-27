print("-- Descuento por Cantidad --")
cantidad = int(input("Cantidad de artículos: "))
precio_unitario = float(input("Precio unitario original: "))
total = cantidad * precio_unitario
if cantidad > 5 and cantidad < 10:
    total *= 0.95  
elif cantidad >= 10:
    total *= 0.92 
print(f"Total a pagar: ${total}")