"""
Ejercicio de intervención

Requisitos:
- Agregar una exepción donde se va a considerar una lista con 4 valores,
todos sus datos serán string
- Al querer modificar una de las posiciones no existentes
crear un nuevo índice y darle el valor de "0"
- Mostrar la lista final
"""

lista = ["rojo","azul","amarillo","verde"]
try:
    indice_a_modificar = 5
    nuevo_valor = "morado"
    lista[indice_a_modificar] = nuevo_valor
except IndexError:
    diferencia = indice_a_modificar - len(lista)

    for i in range(0, diferencia):
        lista.append("0")

print("la lista final es:", lista)


