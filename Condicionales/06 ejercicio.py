print("--Calcular areas--")
menu= """"
  
    menu opciones
    [1] Rectangulo
    [2] Cuadrado
    [3] Paralelogramo
    [4] Rombo
    [5] Trapecio
    [6] Triangulo
    [7] Triangulo Equiklatero 
    [8] Triangulo rectangulo
    [9] Poliono regular
    """

print({menu})
opcion = int(input("Elija alguna opcion: "))

if opcion == 1:
    a = int(input("Ingrese a: "))
    b = int(input("Ingrese b: "))
    area = a*b

    print("el Area es: ",area)

elif opcion == 2:
    a = int(input("Ingrese el valor de a: "))
    area = a*a

    print("el Area es: ",area)

elif opcion == 3:
    b = int(input("Ingrese el valor de b: "))
    h = int(input("Ingrese el valor de h: "))
    area = b*h

    print("el Area sera es: ",area)

elif opcion == 4:
    AC = int(input("Ingrese el valor de AC: "))
    BD = int(input("Ingrese el valor de BC: "))
    area = (AC*BD)/2

    print("el Area es: ",area)

elif opcion == 5:
    a = int(input("Ingrese el valor de a: "))
    b = int(input("Ingrese el valor de b: "))
    h = int(input("ingrese el valor de h: "))
    area = (a+b)/2*h

    print("el Area es: ",area)

elif opcion == 6:
    a = int(input("Ingrese el valor de a: "))
    h = int(input("Ingrese el valor de h: "))
    area = (a*h)/2

    print("el Area es: ",area)

elif opcion == 7:
    a = float(input("Ingrese el valor de a: "))
    area = ((a*a) * (3**0.5))/4

    print("el Area es: ",area)

elif opcion == 8:
    a = int(input("Ingrese el valor de a: "))
    c = int(input("Ingrese el valor de c: "))
    area = (a*c)/2

    print("el Area es: ",area)

elif opcion == 9:
    P = int(input("Ingrese el valor de P: "))
    a = int(input("Ingrese el valor de a: "))
    p = int(input("ingrese el valor de p: "))
    area = (P*p**a)/2

    print("el Area es: ",area)




    

