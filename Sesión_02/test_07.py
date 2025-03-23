#Reconocimiento de tipos de datos: type()

#Creación de variables

nombre = "Luis"
ciudad =  "Lima"
saldo = 5000
empresa = False
correo = "luish@gmail.com"
empleado = [nombre, saldo, empresa, ciudad]
empleado_dict = {"nom":nombre, "ciu":ciudad, "sal":saldo, "emp":empresa, "cor":correo}

print("El tipo de dato de mi variable 'nombre' es: {}.".format(type(nombre)))
print("El tipo de dato de mi variable 'saldo' es: {}.".format(type(saldo)))
print("El tipo de dato de mi variable 'empresa' es: {}.".format(type(empresa)))
print("El tipo de dato de mi variable 'correo' es: {}.".format(type(correo)))
print("El tipo de dato de mi variable 'empleado_dict' es: {}.".format(type(empleado_dict)))
