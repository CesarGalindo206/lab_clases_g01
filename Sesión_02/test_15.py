"""

Requisitos

1. Crear 2 variables enteras, 2 variables flotantes, 1 variable string, 1 variable string solamente con contenido numérico
y 1 variable booleana

2. Obtener y mostrar la suma de una variable entera con la variable string numérica.

3. Obtener y mostrar la suma de 2 variables enteras más la variable string numérica y la variable flotante

4. Obtener y mostrar el módulo de las 2 variables enteras : %

5. Obtener y mostrar el resultado entero o la parte entera de las 2 variables int : //

6. Obtener la potencia usando una de las variables flotantes como base y la variable entera como potencia

"""

varint_1 = 3
varint_2 = 10
varfloat_1 = 1.1
varstr_1 = "rojo"
varstr_2 = "23"
varbool_1 = True

dos = varint_1 + int(varstr_2)

tres = varint_1 + varint_2 + int(varstr_2) + varfloat_1

cuatro = varint_1 % varint_2

cinco = varint_1 // varint_2

seis = pow(varfloat_1, varint_2)

print("La suma de la variable entera con la string numérica es : {}".format(dos))
print("La suma de las variables enteras, la string numérica y la flotante es : {}".format(tres))
print("El modulo de la variable entera 1 sobre la 2 es : {}".format(cuatro))
print("La división entera entre la variable entera 1 y la 2 es : {}".format(cinco))
print("La variable flotante elevado a la variable entera 2 es : {}".format(seis))