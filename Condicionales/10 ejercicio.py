print("-- Cálculo de Precio de Llantas --")
numero_llantas = int(input("Ingrese el número de llantas a comprar: "))
precio_unitario = 0 
if numero_llantas < 6:
    precio_unitario = 240000
elif numero_llantas in (6, 7):
    precio_unitario = 221000
else:
    precio_unitario = 180000
precio_total = numero_llantas * precio_unitario
print(f"El precio total es: ${precio_total}")
