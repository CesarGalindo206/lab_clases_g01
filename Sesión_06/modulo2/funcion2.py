"""
Ejercicio de intervención

Requisitos:
1. Crear un módulo donde se va a tener que crear una función que obtiene
el impuesto que va a pagar una persona si el sueldo es mayor a 500 soles,
impuesto: 8%

2. Esta función usará una exception si el sueldo es tipo string

3. Pedir el sueldo por consola en el archivo principal

4. El archivo principal importará a la función creada para ser usada

"""

def  obtener_impuesto(sueldo):

    impuesto = 8 * (sueldo / 100)

    if sueldo > 500:
        print(f"Usted pagará un impuesto de cantidad S/ {impuesto}")
    else:
        print("Usted no pagara el impuesto")




