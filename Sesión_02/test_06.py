"""
Requisitos

1. Crear variables para los valores de nombre, profesión y ciudad
2. Crear 2 variables para la remuneración de enero y febrero
3. Crear 1 variable donde se sumará el ingreso de los meses de enero y febrero
4. Mostrar en pantalla el mensaje de:
Hola soy 'nombre' y mi profesión es 'profesion' , además mi remuneración acumulada es de 'total'
"""

nombre = "César"
profesion = "Física"
ciudad = "Lima"


rem01 = 1234
rem02 = 1234

total = rem01 + rem02

print("Hola soy {} y mi profesión es {}, soy de {}, además mi remuneración acumulada es de {}".format(nombre, profesion, ciudad, total))