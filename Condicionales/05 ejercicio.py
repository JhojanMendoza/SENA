print("-Notas-")

nota = float(input("Ingrese la primer nota del estudiante: "))
nota2 = float(input("Ingrese la segunda nota del estudiante: "))
nota3 = float(input("Ingrese la tercera nota del estudiante: "))
nota4 = float(input("Ingrese la cuarta nota del estudiante: "))

promedio = (nota + nota2 + nota3 + nota4)/4

if promedio>=3.0:
    print("APROBO")
else:
    print("NO APROBO")