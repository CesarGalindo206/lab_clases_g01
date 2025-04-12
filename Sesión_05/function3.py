"""
Programación funcional con Python (POO)

Requisitos:
    - Crear una función que multiplicará 3 valores y luego restará el segundo parámetro
    - Para esta función el tercer parámetro contendrá un valor
    - Mostrar 2 casos donde se ingrese los valores donde uno no afectará
    el valor del parámetro que ya contiene un valor
    y otro donde si lo estará afectando
"""
varp1_1 = int(input("Ingrese el valor a :"))
varp1_2 = int(input("Ingrese el valor b :"))

def prod1(a,b,c=20):
    return a*b*c - b

print(prod1(varp1_1,varp1_2))

varp2_1 = int(input("Ingrese el valor nuevo de a :"))
varp2_2 = int(input("Ingrese el valor nuevo de b :"))
varp2_3 = int(input("Ingrese el valor nuevo de c :"))


def prod2(a,b,c=20):
    return a*b*c - b
print(prod2(varp2_1,varp2_2,varp2_3))