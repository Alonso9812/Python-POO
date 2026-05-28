# Las propiedades en Python son una forma de controlar el acceso a los atributos de una clase.
# Permiten definir métodos getter, setter y deleter para un atributo, lo que proporciona una
# forma de encapsular la lógica de acceso a los datos.

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self._edad = edad      # Atributo privado

    @property
    def nombre(self):
        """Getter para el atributo nombre."""
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre

Jordi = Persona("POLO", 30)

nombre = Jordi.nombre  # Llama al getter
print(nombre)  # Output: Jordi

Jordi.nombre = "Jorge"  # Llama al setter

nombre = Jordi.nombre  # Llama al getter
print(nombre)

del Jordi.nombre  # Llama al setter

print("Nombre eliminado")