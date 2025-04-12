class Carro:
    """Atributo"""
    rueda = 4

    """Constructor: Valores que van a tomar por defecto mi clase que se instancia a una variable"""
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion  # Aceleración en m/s^2
        self.velocidad = 0  # Velocidad en m/s

    """Métodos: Son las funciones de las clases"""
    def acelerar(self, tiempo):
        """Acelera el carro en función del tiempo"""
        # La velocidad se incrementa: velocidad = velocidad + aceleración * tiempo
        self.velocidad = self.velocidad + self.aceleracion * tiempo

    def frenar(self, tiempo):
        """Frena el carro en función del tiempo"""
        # La velocidad disminuye: velocidad = velocidad - aceleración * tiempo
        self.velocidad = self.velocidad - self.aceleracion * tiempo
        # Evitar que la velocidad sea negativa
        if self.velocidad < 0:
            self.velocidad = 0

carro_1 = Carro("Blanco", 70)

print(carro_1.velocidad)
#Añadimos un comportamiento por partes
carro_1.acelerar(1)
carro_1.acelerar(1)
carro_1.acelerar(1)
carro_1.acelerar(1)

print("La velocidad actual de mi carro 1 es {}".format(carro_1.velocidad))

carro_1.frenar(1)
carro_1.frenar(1)

print("La velocidad de mi carro 1 es: {}".format(carro_1.velocidad))