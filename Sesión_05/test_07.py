#Uso del condicional if
#If ternarios

estado = 1
#Forma tradicional usando un bloque if

"""
if estado == 1:
    print("1. Su estado final es terminado")
else:
    print("2. Su estado final es terminado")
"""

#Forma equivalente usando if ternario
final ="1. Su estado final es terminado" if estado == 1 else "2. Su estado final es terminado"
print(final)