#Uso del if

edad =int(input("Ingrese edad: "))

if 0 < edad < 30:
    print("Usted todavía es menor de edad")
elif 18 <= edad < 65:
    print("Usted es una persona adulta")
elif 65 <= edad < 100:
    print("Usted es una persona de la tercera edad")
else:
    print("Usted ha ingresado una edad incorrecta")
