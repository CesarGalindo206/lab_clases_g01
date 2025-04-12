"""Listas -> copy(): Obtener todos los valores de una lista en otra variable"""

var_1 = ["sQLServer", "RDS", "MySQL", "Postgresql", "MongoDB"]

var_2 = var_1.copy()

print("La lista var_2 la cual es una copia de la lista var_1 es : {}".format(var_2))

var_2.append("Maria08")
var_2.append("SQLite3")

print("Los valores actualizados de mi lista var_2 es: {}".format(var_2))

print("La lista inicial var_1 es {}".format(var_1))
