#Programación orientada a objetos

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

carro_1 = Carro("Blanco", 60)
print("El color del primer carro es {}".format(carro_1.color))

carro_2 = Carro("Rojo", 80)
carro_2.marchas= 3000

print("El número de marchas de mi segundo carro es: {}".format(carro_2.marchas))

#carro_2.marchas ha sido definido luego de la instancia de carro_1, por lo tanto
#No es posible llamar un atributo de datos que se le ha asigando a otra instancia de la clase


