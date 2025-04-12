"""del: elimina un key y su valor del diccionario"""

var_1 = {"nombre": "Susana", "edad": 29, "promedio": 18}

del var_1["edad"]

print("El diccionario sin la edad es {}".format(var_1))

del var_1["nombre"]

print("El diccionario sin el nombre es {}".format(var_1))

del var_1["promedio"]

print("El diccionario sin el promedio es {}".format(var_1))


