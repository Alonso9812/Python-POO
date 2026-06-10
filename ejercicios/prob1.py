# ejercicio 1
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def acariciar(self, perro):
        print(f"{self.nombre} acaricia a {perro.nombre}")

class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} mueve la cola")

persona1 = Persona("Juan", 30)
perro1 = Perro("Rocky", "Labrador")

persona1.acariciar((perro1))
perro1.ladrar()

# ejercicio 2
class Profesor:
    def __init__(self, nombre, materia):
        self.nombre = nombre
        self.materia = materia

    def calificar(self, estudiante, nota):
        estudiante.materia = nota


class Estudiante:
    def __init__(self, nombre, materia):
        self.nombre = nombre
        self.materia = materia

    def recibir(self, Profesor):
        print(f"{Profesor.nombre} califica a {self.nombre} con {self.materia}")


profesor1 = Profesor("Juan", "ciencias")
estudiante1 = Estudiante("Pedro", "Ciencias")

profesor1.calificar(estudiante1, 50)
estudiante1.recibir(profesor1)

