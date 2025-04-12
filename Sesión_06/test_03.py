"""Control o gestión de excepciones"""

"""
Requisitos:
    - Crear una función aplicando exceptions donde el bloque except
    va a considerar a los errors de división entre cero y el tipo de error
    - Los valores tienen que ser mayor a 0
    - Los valores tienen que ser ingresado por consola
"""

def division(a,b):

    try:
        division = a/b
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    except TypeError:
        print("No se pueden dividir dos tipos de datos diferentes")
    else:
        return division

resultado1 = division(2,3.2)
print(resultado1)
print("___________________")
resultado2 = division(2,0)
print(resultado2)
print("___________________")
resultado3 = division(2,"b")