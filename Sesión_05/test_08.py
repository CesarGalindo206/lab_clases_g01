#Cadenas o Strings
#Concatenación

nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apellido: ")

nombre_completo = "El nombre completo es :  " + nombre + " " + apellido

print(nombre_completo)

nombre_completo = "El nombre completo del usuario es {} {}.".format(nombre, apellido)
print(nombre_completo)