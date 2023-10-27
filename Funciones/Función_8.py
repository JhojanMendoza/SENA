def contar_letras():
    print("--Contar letras mayúsculas y minúsculas en una cadena--")
    cadena = input("Ingresa una cadena de texto: ")
    mayusculas = sum(1 for letra in cadena if letra.isupper())
    minusculas = sum(1 for letra in cadena if letra.islower())
    print(f"Letras mayúsculas: {mayusculas}")
    print(f"Letras minúsculas: {minusculas}")