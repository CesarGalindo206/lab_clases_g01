class Alumno:

    def __init__(self, nombre, distrito, nota1, nota2, nota3):
        self.nacionalidad = "Peruano"
        self.nombre = nombre
        self.distrito = distrito
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def promedio(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

    def verificacion(self):
        media = self.promedio()
        if media >= 10.5:
            return "Aprobado"
        else:
            return "Desaprobado"

    def describir(self):
        return f"El estudiante se llama {self.nombre} y es de {self.distrito}"

# Instanciar dos alumnos
alumno_1 = Alumno("César", "Comas", 12, 14, 16)
alumno_2 = Alumno("Kimberlyn", "Comas", 9, 10, 11)

# Mostrar resultados
print(f"{alumno_1.describir()} {alumno_1.nacionalidad}")
print(f"Promedio: {alumno_1.promedio():} - Su condición es {alumno_1.verificacion()}")

print()

print(f"{alumno_2.describir()} {alumno_2.nacionalidad}")
print(f"Promedio: {alumno_2.promedio():} - Su condición es {alumno_2.verificacion()}")
