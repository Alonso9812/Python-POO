# La Abstraccion es un proceso de ocultar los detalles de implementación y mostrar solo la funcionalidad al usuario.
#  En la programación orientada a objetos, la abstracción se logra mediante el uso de clases y objetos.

class Auto:
    def __init__(self):
        self._estado = "apagado"

    def encender(self):
        self._estado = "encendido"
        print("El auto está encendido.")

    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo el auto...")

mi_auto = Auto()
mi_auto.conducir()  # Esto encenderá el auto automáticamente si está apagado
   
       