import datetime

fecha = input("Introduce tu fecha de nacimiento en (Año-Mes-Día): ")

fecha = datetime.datetime.strptime(fecha, '%Y-%m-%d')
edad = datetime.datetime.now().year - fecha.year

print ("Calculemos tu edad")
print ("--------------------------------------")
print ()
print("Tu edad es:", edad)
print ()