
"""Usando las propiedades de cadenas o string"""

"""
Requisitos:
 - Ingresar tu nombre y apellido por consola 
 (cada valor tiene que estar en una variable distinta)
 - Obtener el tamaño de tu nombre y apeellido completo luego de concatenarlos
 y mostrar en consola
 - Imprimir el resultado de la concatenación final todo en mayúsculas
 - Indicar mediante condicionales si el tamaño del nombre es mayor 
 o no al del apellido ingresado
 (Ingresar solo en este caso el apellido paterno)
 """


nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido paterno: ")

nombre_completo = nombre + " " + apellido

tamaño_completo = len(nombre_completo)
print(f"\nEl tamaño del nombre completo es: {tamaño_completo} caracteres.")

print("Nombre completo en mayúsculas:", nombre_completo.upper())

if len(nombre) > len(apellido):
    print("El nombre es más largo que el apellido.")
elif len(nombre) < len(apellido):
    print("El apellido es más largo que el nombre.")
else:
    print("El nombre y el apellido tienen el mismo tamaño.")
