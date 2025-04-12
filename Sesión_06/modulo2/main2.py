from funcion2 import obtener_impuesto as imp_


def main():
    sueldo_str = input("Introduce el sueldo: ")

    try:
        sueldo = float(sueldo_str)
        imp_(sueldo)
    except ValueError:
        print("Error: Debes ingresar un número válido.")

print(main())
