print("-- Conversión de Temperaturas --")
print("Menú de opciones:")
print("[1] Celsius a Fahrenheit")
print("[2] Celsius a Kelvin")
print("[3] Fahrenheit a Celsius")
print("[4] Fahrenheit a Kelvin")
print("[5] Kelvin a Celsius")
print("[6] Kelvin a Fahrenheit")
opcion = int(input("Elija una opción: "))

if opcion == 1:
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"La temperatura en Fahrenheit es: {fahrenheit}°F")

elif opcion == 2:
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    kelvin = celsius + 273.15
    print(f"La temperatura en Kelvin es: {kelvin} K")

elif opcion == 3:
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"La temperatura en Celsius es: {celsius}°C")

elif opcion == 4:
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    kelvin = (fahrenheit + 459.67) * 5/9
    print(f"La temperatura en Kelvin es: {kelvin} K")

elif opcion == 5:
    kelvin = float(input("Ingrese la temperatura en Kelvin: "))
    celsius = kelvin - 273.15
    print(f"La temperatura en Celsius es: {celsius}°C")

elif opcion == 6:
    kelvin = float(input("Ingrese la temperatura en Kelvin: "))
    fahrenheit = (kelvin * 9/5) - 459.67
    print(f"La temperatura en Fahrenheit es: {fahrenheit}°F")

else:
    print("Opción no válida. Por favor, elija una opción del 1 al 6.")
