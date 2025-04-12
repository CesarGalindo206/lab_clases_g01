#Decoradores en python

#Creación interna de la función decoradora

# Creación interna de la función decoradora
def funciondecoradora(funcionB):
    def funcionC():
        print("1. Antes de ejecutar la función decorada")
        funcionB()
        print("2. Después de ejecutar la función decorada")
    return funcionC  # Retornar la referencia a la función decorada, no su ejecución

@funciondecoradora
def saludo():
    print("Hola pythonistas")

# Llamada a la función decorada
saludo()
