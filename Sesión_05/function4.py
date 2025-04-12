"""
Programación funcional con Python (POO)

Requisitos:
    - Solicitar al usuario 4 números por consola
    - Crear una función que devuelva cuál es el número mayor de los 4
      ingresados por el usuario
    - Finalmente asignar a una variable el valor de esta función
      para elevar al cubo este resultado y mostrarlo en la terminal
"""
numeracion = ["primer", "segundo", "tercero", "cuarto"]
numeros = []

for i in range(0,4):

    num = int(input(f"Ingrese el {numeracion[i]} número: "))
    numeros.append(num)

print(numeros)

def mayor(n1, n2, n3, n4):

    return max(n1,n2,n3,n4)

print(f"El numero mas grande de los ingresados es {mayor(numeros[0], numeros[1], numeros[2], numeros[3])}")

resultado = mayor(numeros[0], numeros[1], numeros[2], numeros[3]) ** 3

print(f"Y su valor elevado al cubo es {resultado}")







