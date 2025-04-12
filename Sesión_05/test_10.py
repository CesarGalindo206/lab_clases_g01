"""Usando los métodos de cadenas o strings"""

#Método de Strings 2

cadena = "Conexión a Base de Datos con Python"

cadena_ = cadena.replace(cadena[0:8], "Nueva Conexión")
print("Cadena con reemplazo, tiene el siguiente valor actualizado : {}".format(cadena_))

"""Eliminación de espacios  en blanco en mi cadena (después) con .rstrip()"""

cadena_3 = "Conexión a Base de Datos con Python          "
cadena_4 = cadena_3.rstrip()

print(cadena_3)
print("Mi nueva cadena con los espacios en blanco eliminados después del string es : {}".format(cadena_4))

"""Eliminación de espacios en blanco en mi cadena (antes) con ."""

cadena_6 = "           Conexión a Base de Datos con Python"
cadena_7 = cadena_6.lstrip()
print(cadena_6)
print("Mi nueva cadena con los espacios en blanco eliminados antes del string es : {}".format(cadena_7))



