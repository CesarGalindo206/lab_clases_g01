"""Listas -> count(): Cantidad de veces que aparece un elemento que se repite en la lista"""

var_1 = ["Python", "JAVA", "php", "Javascript", "Typescript"]

var_1.append("PHP")
var_1.append("C#")
var_1.append("PHP")
var_1.append("C#")
var_1.append("PHP")

print("La cantidad de veces que se repite el elemento PHP en la lista var_1 es {}".format(var_1.count("PHP")))
print("La cantidad de veces que se repite el elemento C# en la lista var_1 es {}".format(var_1.count("C#")))