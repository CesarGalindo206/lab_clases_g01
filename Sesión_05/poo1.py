#Programación orientada a objetos

class Carro:

    """Atributo"""

    rueda = 4

    """Constructor: Valores que van a tomar por defecto mi clase que se instancia a una variable"""

    def __init__(self, color, aceleracion, tiempo):
        self.color = color #Esta es el atributo de la instancia (self) donde self es un objeto que luego se instancia finalizando la clase
        self.aceleracion = aceleracion
        self.velocidad = 0
        self.tiempo = tiempo  # Guardamos el tiempo proporcionado al instanciar el objeto

    """Métodos: Son las funciones de las clases"""

    def acelerar(self):
        # Actualizamos la velocidad al incrementar según la aceleración y el tiempo
        self.velocidad = self.velocidad + self.aceleracion * self.tiempo

    def frenar(self):
        # Reducimos la velocidad según la aceleración y el tiempo
        self.velocidad = self.velocidad - self.aceleracion * self.tiempo
        if self.velocidad < 0:
            self.velocidad = 0  # Evitamos que la velocidad sea negativa

    def actualizar_tiempo(self, tiempo_nuevo):
        # Este método actualiza el tiempo
        self.tiempo = tiempo_nuevo

"""Instanciamos nuestra clase (crear un objeto mediante el llamado de la clase creada)"""

carro_1 = Carro("red", 60, 4)

# Llamamos al método acelerar para que la velocidad cambie según la aceleración
carro_1.acelerar()
print("El color del primer carro es {}".format(carro_1.color))
print("La aceleración del primer carro es {}".format(carro_1.aceleracion))
print("La cantidad de ruedas que tiene el primer carro es {}".format(carro_1.rueda))
print(f"La velocidad en el tiempo {carro_1.tiempo} del primer carro es: {carro_1.velocidad}")


"""Instanciamos nuestra clase a una segunda variable"""

carro_2 = Carro("Azul", 80, 5)
carro_2.acelerar()
print("El color del segundo carro es: {}".format(carro_2.color))
print("La aceleración del segundo carro es: {}".format(carro_2.aceleracion))
print("La cantidad de ruedas que tiene mi segundo carro es: {}".format(carro_2.rueda))
print(f"La velocidad en el tiempo {carro_2.tiempo} del segundo carro es: {carro_2.velocidad}")

