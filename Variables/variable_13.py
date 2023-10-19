segundos = int(input("Ingrese la cantidad de segundos: "))

horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

print("Tiempo")
print("--------------------------------------")
print ()
print("El tiempo en formato Horas, Minutos y Segundos es: {:02d}:{:02d}:{:02d}".format(horas, minutos, segundos))
print ()
