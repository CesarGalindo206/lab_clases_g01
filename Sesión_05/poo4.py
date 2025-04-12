
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

#Aplicamos Herencia
#Crear nuestra clase hija

class CarroVolador(Carro):

    ruedas = 6

    def __init__(self, color, aceleracion, estado_volando = False):
        super().__init__(color, aceleracion) #Permite que herede atributos de la clase padre
        self.estado_volando = estado_volando

    def vuela(self):
        self.estado_volando = True

    def aterriza(self):
        self.estado_volando = False

#Instanciamos nuestra clase con un objeto carro_1

carro_1 = Carro("Rojo",55)
carro_volador= CarroVolador("Blanco",65)

carro_volador.vuela()
carro_volador.acelerar(1)
carro_volador.acelerar( 1)
carro_volador.acelerar(1)
carro_volador.acelerar(1)

print("La velocidad actual de mi carro volador es: {}".format(carro_volador.velocidad))

