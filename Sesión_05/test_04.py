#Uso del while

numero = int(input("¿Cuántos saludos desesa enviar? : "))

while numero < 10:
    print(numero)
    numero = numero + 1

    print("El número con nuevo valor es : {}".format(numero))