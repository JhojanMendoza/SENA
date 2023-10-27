print("-- Cálculo de Pulsaciones --")
edad = int(input("Ingrese su edad: "))
genero = int(input("Género (1 para femenino, 2 para masculino): "))
if genero == 1:
    pulsaciones = (220 - edad) / 10
elif genero == 2:
    pulsaciones = (210 - edad) / 10
else:
    pulsaciones = 0  
if pulsaciones > 0:
    print(f"Deberías tener {pulsaciones} pulsaciones por cada 10 segundos de ejercicio aeróbico.")
else:
    print("Género no válido.")