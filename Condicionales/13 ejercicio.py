print("-- Cálculo de IMC --")
peso = float(input("Ingrese el peso en Kg: "))
estatura = float(input("Ingrese la estatura en metros: "))
imc = peso / (estatura ** 2)
if imc < 18.5:
    estado = "Desnutrido"
elif imc < 25:
    estado = "Normal"
elif imc < 30:
    estado = "Sobrepeso"
elif imc < 35:
    estado = "Obesidad Grado 1"
elif imc < 40:
    estado = "Obesidad Grado 2"
else:
    estado = "Obesidad Grado 3"
print(f"Tu IMC es {imc:.2f} y tu estado es {estado}")
