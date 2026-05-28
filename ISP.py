# ISP Principio de segregacion de interfaz 
# Ningun cliente tiene que ser forzado a depender de interfaces que no utilíce

from abc import ABC, abstractmethod

class Trabajador(ABC):

    @abstractmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    def comer(self):
        pass

class Durmiente(ABC):

    @abstractmethod
    def comer(self):
        pass 

class Humano(Trabajador, Durmiente, Comedor):
    def comer(self):
        print("El humano esta comiendo")

    def trabajar(self):
        print("El humano esta trabajando")

    def dormir(self):
        print("El humano esta durmiendo")

class Robot(Trabajador):

    def trabajar(self):
        print("El robot esta trabajando")

robot = Robot()
robot.trabajar()

                

