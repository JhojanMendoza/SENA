print("¿Eres mayor de edad?")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad:"))
if edad >= 18 and edad <= 100:
        print(f"{nombre} !Eres mayor de edad¡")
elif edad <18 and edad >0 :
        print(f" {nombre} !Eres menor de edad¡")
else:
    print("Edad incorrecta")