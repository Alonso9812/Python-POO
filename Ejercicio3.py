# Modelando animales en un Zoológico

class Animal:
    def comer(self):
        print("Comiendo")

class Ave(Animal):
     def volar(self):
        print("Volando")

class Mamifero(Animal):
    def amamantar(self):
        print("amamantando")

class Murcielago(Mamifero, Ave):
    pass

murcielago1 = Murcielago()
murcielago1.comer() 
murcielago1.amamantar()
murcielago1.volar()

print(Murcielago.mro())  # Output: [<class '__main__.Murcielago'>, <class '__main__.Mamifero'>, <class '__main__.Ave'>, <class '__main__.Animal'>, <class 'object'>]




