

class Estudiante:
    def __init__(self, nombre, promedio):
        self.__nombre = nombre
        self.__promedio = promedio

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre

    @property
    def promedio(self):
        return self.__promedio
    
    @promedio.setter
    def promedio(self, nota):
        if 0 <= nota <= 100:
            self.__promedio = nota
        else:
            print("El promedio es invalido")

    @promedio.deleter
    def promedio(self):
        del self.__promedio

estudiante = Estudiante("Jordi", 98)

nombre = estudiante.nombre
print(nombre)

estudiante.nombre = "Alonso"

nombre = estudiante.nombre
print(nombre)

del estudiante.nombre
print(nombre, f"Fue eliminado")

promedio = estudiante.promedio
print(promedio)

estudiante.promedio = 105

del estudiante.promedio
print("Promedio eliminado")