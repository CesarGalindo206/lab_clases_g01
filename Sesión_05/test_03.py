#Uso del if 2

edad_1 = (input("Ingrese una primera edad: "))
edad_2 = (input("Ingrese una segunda edad: "))


if type(edad_1) != int or type(edad_2) != int:
    print("Debe ingresar un dato de tipo entero")
elif edad_1 > edad_2:
    print("La edad 1 es mayor que la edad 2")
elif edad_1 == edad_2 :
    print("Las edades son iguales")
else:
    print("La segunda persona es mayor que la primera")