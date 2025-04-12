#Decoradores en python

#Creación interna de la función

#Uso de los args y kwargs

def funciondecorador(funcionB):
    def funcionC(*args, **kwargs):
        print("1. Antes de ejecutar la función decorada")
        resultado = funcionB(*args, **kwargs)  # Pasar los argumentos a la función decorada
        print("2. Después de ejecutar la función decorada")
        return resultado
    return funcionC

@funciondecorador
def saludarC(nombre, apellido, edad, **kwargs):
    print("Hola {} {}, usted tiene {} años".format(nombre, apellido, edad))
    for key, value in kwargs.items():
        print("{} : {}".format(key, value))

# Llamada a la función decorada
saludarC("Julio", "Gutierrez", 29, ciudad="Buenos Aires", profesion="Desarrollador")
