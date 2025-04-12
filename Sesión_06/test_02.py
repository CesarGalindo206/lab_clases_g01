"""Control o gestión de excepciones"""

"""
    Crear una aplicación usando exepciones donde no se pueda
    realizar la suma entre diferentes tipos de datos
    
"""
def suma(x, y):
    try:
        sum_result = x + y
    except TypeError:
        print("No se puede sumar porque son de distinto tipo de dato.")
    else:
        print("Resultado de la suma:", sum_result)


try:
    var_1 = int(input("Ingrese un número: "))
    var_2 = int(input("Ingrese un segundo número: "))
    suma(var_1, var_2)
except ValueError:
    print("Error: Solo se permiten números enteros.")



