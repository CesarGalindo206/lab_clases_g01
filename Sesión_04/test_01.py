#Diccionarios en Python

"""Los nombres de los key(llaves) van a ir escritos siempre en minúsculas y
 sin tildes (por convención o buenas prácticas)"""

var_1 ={"nombre":"Susana","edad":29,"promedio":14.9}

print("Mi diccionario tiene el siguiente contenido: {} ".format(var_1))

"""Agregamos elementos con un nuevo key a mi diccionario  var[] = "____" """

#Donde las key son nombre, edad y promedio, y se le asignan Susana, 29 y 14.9 respectivamente

var_1["distrito"] = "Lince"
var_1["nombre"] = "César"


print("Mi diccionario actualizado tiene la foram de : {} ".format(var_1))

nombre =var_1["nombre"]
edad = var_1["edad"]
distrito = var_1["distrito"]

print("La persona {} tiene {} y vive en {}".format(nombre, edad, distrito))


