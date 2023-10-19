salario_d = float(input("Ingrese su salario diario: "))
dias = int(input("Ingrese los días trabajados: "))

bruto = salario_d * dias
pension = bruto * 0.10
salud = bruto * 0.15

neto = bruto - pension - salud

print("Total Salario")
print("--------------------------------------")
print()
print("Salario a pagar al empleado:", neto)
print ()
