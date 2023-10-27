import math

def area_rectangulo(a,b):

    area=a*b
    return print('El area del Rectángulo es: ', area)

def area_cuadrado(L):
    
    area=L**2
    return  print('el area del cuadrado es: ', area)

def area_paralelogramo(b,h):
    
    area=b*h
    return  print('el area del Paralelogramo es: ', area)

def area_rombo(AC,BD):
    
    area=(AC*BD)/2
    return  print('el area del Rombo es es: ', area)

def area_trapecio(a,b,h):

    area=(a+b)*h/2
    return print('El area del Trapecio es: ', area)

def area_triangulo(b,h):

    area=b*h/2
    return print('El area del triángulo es: ', area)


def area_triangulo_equilatero(a):

    area = ((a*a) * (3**0.5))/4
    return print('El area del Triangulo equilatero es: ', area)


def area_triangulo_rectangulo(a,c):

    area=a*c/2
    return print('El area del triángulo rectangulo es: ', area)


def area_poligono_regular(P,a,p):

    area=(P*p**a)/2
    return print('El area del poligono rectangulo es: ', area)



print("--Calcular Áreas de figuras Geométricas--\n")
print("1.Rectangulo.\n2.Cuadrado.\n3.Paralelogramo.\n4.Rombo.\n5.Trapecio.\n6.Triangulo.\n7.Triangulo equilatero.\n8.Triangulo rectangulo.\n9.Poligono regular.\n")

x=int(input("Escoja la figura: "))
if x==1:

    a = int(input('Ingrese el area del rectangulo: '))
    b = int(input('Ingrese la base del rectangulo: '))
    area = area_rectangulo(a,b)

elif x==2:
    L=int(input('Ingrese el lado: '))
    area = area_cuadrado(L)
        
elif x==3:
    
    b=int(input('Ingrese la base: '))
    h=int(input('Ingrese la altura: '))
    area = area_paralelogramo(b,h)
   
elif x==4:
    
    AC=int(input('Ingrese la base 1:'))
    BD=int(input('Ingrese la base 2: '))
    area = area_rombo(AC,BD)
    
elif x==5:
    
    a=int(input('Ingrese la altura: '))
    b=int(input('Ingrese la base: '))
    h=int(input("ingrese h: "))
    area = area_trapecio(a,b,h)
    
elif x==6:
    
    a=int(input('Ingrese la altura: '))
    h=int(input('Ingrese h: '))
    area = area_triangulo (a,h)

elif x==7:
    
    a=int(input('Ingrese la altura: '))
    area = area_triangulo_equilatero (a)

elif x==8:
    
    a=int(input('Ingrese la altura: '))
    c=int(input('Ingrese c: '))
    area = area_triangulo_rectangulo (a,c)

    
elif x==9:
    
    P=int(input('Ingrese P: '))
    a=int(input('Ingrese a: '))
    p=int(input('Ingrese p: '))
    area = area_poligono_regular (P,a,p)

     
        




