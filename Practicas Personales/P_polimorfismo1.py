# Sistema de animales de un zoológico utilizando polimorfismo

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hacer_sonido(self):
       print(f"{self.nombre} dice: Guau! Guau!")
    
class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hacer_sonido(self):
        print(f"{self.nombre} dice: Miau! Miau!")
    
class Vaca(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hacer_sonido(self):
        print(f"{self.nombre} dice: Muuu! Muuu!")
    

perro1 = Perro("Biscocho") 
gato1 = Gato("Patitas")
vaca1 = Vaca("Lola")
perro2 = Perro("Palomo") 
gato2 = Gato("mishi")
vaca2 = Vaca("Lula")

lista = [perro1, gato1, vaca1, perro2, gato2, vaca2]

def recorrer(lista):
    for item in lista:
        item.hacer_sonido()

recorrer(lista)