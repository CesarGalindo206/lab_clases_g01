
from funciones import suma as opera_1, multiplicacion as opera_2

var_1 = int(input("Introduce el primer numero: "))
var_2 = int(input("Introduce el segundo numero: "))

#sum = suma(var_1,var_2)

sum = opera_1(var_1, var_2)
print(sum)

#multiplicacion = multiplicacion(var_1,var_2)

multiplicacion = opera_2(var_1, var_2)
print(multiplicacion)