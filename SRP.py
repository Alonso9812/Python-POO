# SRP es uno de los pricipios SOLID, que se refiere a la responsabilidad única de una clase o módulo.
# Según este principio, una clase o módulo debe tener una única razón para cambiar, lo que significa que debe
# tener una única responsabilidad o función.

class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

class Auto:
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self, distancia):

        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print(f"El auto se ha movido a la posición {self.posicion}. Combustible restante: {self.tanque.obtener_combustible()}")  
        else:
            print("No hay suficiente combustible para mover el auto.")

    def obtener_posicion(self):
        return self.posicion
    

tanque = TanqueDeCombustible()
auto = Auto(tanque) 

print(f"Posición inicial del auto: {auto.obtener_posicion()}")
auto.mover(20)
print(f"Posición siguiente del auto: {auto.obtener_posicion()}")
auto.mover(40)
print(f"Posición siguiente del auto: {auto.obtener_posicion()}")
auto.mover(80)
print(f"Posición siguiente del auto: {auto.obtener_posicion()}")
auto.mover(40)
print(f"Posición siguiente del auto: {auto.obtener_posicion()}")
auto.mover(60)
print(f"Posición siguiente del auto: {auto.obtener_posicion()}")
