print("-- Decisión de Tipo de Pago --")
cuenta = float(input("Ingrese el monto de la cuenta: "))
if cuenta < 150000:
    print("Pago en efectivo.")
elif cuenta <= 300000:
    print("Pago con dinero electrónico.")
elif cuenta <= 600000:
    print("Pago con tarjeta de débito.")
else:
    print("Pago con tarjeta de crédito.")