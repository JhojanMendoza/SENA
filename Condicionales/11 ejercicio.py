print("-- Cálculo de Precio de Pizza --")
tamaño_pizza = int(input("Tamaño de la pizza (1, 2, 3): "))
ingredientes_adicionales = int(input("Número de ingredientes adicionales: "))
precio_base = 0
if tamaño_pizza == 1:
    precio_base = 15000
elif tamaño_pizza == 2:
    precio_base = 24000
elif tamaño_pizza == 3:
    precio_base = 36000
precio_total = precio_base + (ingredientes_adicionales * 4000)
print(f"El precio total es: ${precio_total}")