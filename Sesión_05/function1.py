#Programación funcional en python

var_1 = 80
var_2 =100

"""
Input: dos variables que pasaran por parámetro de la función 
a, b : parámetros de la función "sumar"
"""

def sumar(a,b):
    return a + b

def potencia(a,b):
    suma = a + b
    var_1 = pow(suma,3)
    return var_1

resultado = sumar(var_1,var_2)

"output: lo que va retornar la función"

print(resultado)
resultado_2 = potencia(var_1,var_2)
print(resultado_2)
resultado_3 = potencia(3,5 )
print(resultado_3)

