#Uso del for

ingenierias =["Software", "Sistemas", "Industrial", "Química", "Mecánica", "Mecatrónica"]

print("El tamaño de la lista es : {}".format(len(ingenierias)))

i = 0

for ingenieria in ingenierias:
    print("Ingeniería {}".format(ingenieria))
    print("Valor de i  : {}".format(i))

    if i == 2:
        ingenierias[i] = "Estadistica"
    i = i + 1


print("La lista actualizada es : {}".format(ingenierias))