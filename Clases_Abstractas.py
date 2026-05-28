
from abc import ABC, abstractmethod

class persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, mi nombre es: {self.nombre}, tengo {self.edad} años.")

class Estudiante(persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"{self.nombre} está estudiando {self.actividad}.")

class Trabajador(persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"{self.nombre} está trabajando en {self.actividad}.")

estudiante1 = Estudiante("Juan", 20, "Masculino", "Matemáticas")
trabajador1 = Trabajador("Ana", 30, "Femenino", "Desarrollo de software")

estudiante1.presentarse()
estudiante1.hacer_actividad()
trabajador1.presentarse()
trabajador1.hacer_actividad()


