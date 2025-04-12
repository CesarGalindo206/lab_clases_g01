"""
    Programación Orientada a Objetos
    Participación

Requerimientos:
    - Crear una Clase Alumno
        - Debe tener un atributo de nacionalidad con el valor "Peruano"
        - Tendrá 3 notas, la nota inicial de c/u será de 0
        - Crear un método que indicará el promedio del alumno
        - Crear un método que indicará si elx alumno está aprobado o no de acuerdo a su promedio
        - Las notas serán pasadas por parámetro al momento de instanciar la clase
        - Crear un método para obtener el nombre y distrito de residencia del alumno
        - Instanciar la clase para el caso de 2 alumnos necesariamente
    """

class Alumno:

    def __init__(self, nacionalidad, nombre, distrito):
        self.media = 0
        self.nacionalidad = nacionalidad
        self.nota1 = 0
        self.nota2 = 0
        self.nota3 = 0
        self.nombre = nombre
        self.distrito = distrito

    def promedio(self,nota1,nota2,nota3):

        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

        medias = (self.nota1 + self.nota2 + self.nota3)/3

        return medias

    def verificacion(self, medias=None):

        self.media = medias
        if self.media < 10.5:
            return "Desaprobado"
            
        else:
            return "Aprobado"
            

    def  describir(self, nombre, distrito):
        print(f"El estudiante se llama {self.nombre} y es de {self.distrito}")


#Instanciar dos alumnos

alumno_1 = alumno("Peruano","César","Comas")
print(f"El alumno {alumno_1.nombre}, de nacionalidad {alumno_1.nacionalidad}, es de {alumno_1.distrito}")
print(f"Su condición es {alumno_1.verificacion(media)}")
alumno_2 = alumno("Peruano","Kimberlyn","Comas")









