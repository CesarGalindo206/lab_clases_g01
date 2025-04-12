"""Listas -> del ____[] : Eliminará un valor indicando el índice del valor de la lista"""

paises = []

paises.append("Perú")
paises.append("Brasil")
paises.append("Argentina")
paises.append("Canadá")
paises.append("México")
paises.append("Guatemala")

print(paises)

del paises[2]

print("La lista actualizada de paises es {}".format(paises))

del paises[2]

print("La lista actualizada de paises es {}".format(paises))
