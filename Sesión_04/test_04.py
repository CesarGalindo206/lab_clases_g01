"""convirtiendo diccionarios a listas"""


var_1 = {"nombre": "MYSQL", "tipo": "BD relacional"}


print("Mi diccionario actual es : {}".format(var_1))

var_1_values = list(var_1.values())

print("Mi lista transformada es : {}".format(var_1_values))

#.values() devuelve los valores de cada key

var_1_values = list(var_1.values())
print(var_1_values)

#.keys() devuelve las keys en el orden como se encuentran (como sorted solo que sorted las devuelve ordenadas)

keys = list(var_1.keys())
print(keys)

#.items() devuelve tanto como los values y las keys

var_3 = list(var_1.items())
print(var_3)
