#Control o gestión de excepciones

"""
TyperError
ZeroDivisionError
IndexError
KeyError
FileNotFoundError
ImportError
OverFlowError
"""



def division(a,b):

    try:
        resultado = a/b
        print("división correcta")
    except ZeroDivisionError:
        print("no se pueden dividir estos valores")
        resultado = None
        print("Resultado: {}".format(resultado))
    else:
        print("Resultado: {}".format(resultado))

print("___________________________")
division(1000, 10)
print("___________________________")
division(400, 0)
print("___________________________")
division(2, 500)
