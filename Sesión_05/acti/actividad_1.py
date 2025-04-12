"""if ternarios"""

"""
Requisitos: 
 - Ingresar por teclado el sueldo de un empleado
 - Si el sueldo es mayor a 2500 y menor a 3500, imprimir "Su sueldo no tiene bonificación"
 y se le agregará el 10%, para luego mostrar el sueldo final con la bonificación
 - Caso contrario: "Su sueldo tiene bonificación este año y será de: 
 'sueldo_final'", sueldo_final= sueldo + 2% sueldo
"""

sueldo = float(input("Ingrese el sueldo de un empleado: "))

sueldo_final = 10/100 * sueldo + sueldo if 2500 < sueldo < 3500 else sueldo + 2/100 * sueldo
mensaje_final = "Su sueldo no tiene bonificación" if 2500 < sueldo < 3500 else "Su sueldo tiene bonificación este año"

print(mensaje_final)
print("El sueldo final con bonificación es: {:.2f}".format(sueldo_final))