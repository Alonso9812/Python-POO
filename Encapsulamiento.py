# Encapsulamiento es un principio de la programación orientada a objetos que consiste en ocultar los detalles internos de una clase y exponer
#  solo lo necesario a través de métodos públicos. Esto ayuda a proteger los datos y a mantener la integridad de los objetos.

#getters y setters son métodos que se utilizan para acceder y modificar los atributos de una clase de manera controlada.
# Un getter es un método que se utiliza para obtener el valor de un atributo, mientras que
# un setter es un método que se utiliza para modificar el valor de un atributo.

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado

    # Getter para el nombre
    def get_nombre(self):
        return self.__nombre
    
    # Setter para el nombre
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre
    
jordi = Persona("Jordi", 30)

nombre = jordi.get_nombre()  # Accediendo al nombre a través del getter
print(nombre)  # Imprime: Jordi

jordi.set_nombre("Jordi Alonso")  # Modificando el nombre a través del setter

nombre = jordi.get_nombre()  # Accediendo al nombre modificado a través del getter
print(nombre)  # Imprime: Jordi Alonso