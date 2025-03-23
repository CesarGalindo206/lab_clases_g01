#Listas con en Python

"""Listas: pop(): Quita un elemento de una posición dada"""

paises = ["Perú","Canadá","Argentina","México"]

print("Mi lista inicial: {}".format(paises))

paises.pop(0)

print("Mi lista final: {}".format(paises))

"""Listas: insert(): Inserta elementos en una posición dada y valor"""

numbers = [1,2,3,4,5,6]
print("La lista de números es: {}".format(numbers))
edad= 7
numbers.insert(6,edad )
print("La lista actualizada de números es: {}".format(numbers))