#Uso del método random

import random

numero = random.randint(1, 100)

print(numero)

mi_lista = []

for elemento in range(100):

    #le concedemos un valor aleatorio entre el 1 y 30
    elemento = random.randint(1, 100)
    #agregamos el número aleatorio a la lista
    mi_lista.append(elemento)

print(mi_lista)