# sistema de tranporte

class Transporte:
    def __init__(self, marca):
        self.marca = marca

    def moverse(self):
        pass

class Carro(Transporte):
    def __init__(self, marca):
        super().__init__(marca)
    
    def moverse(self):
        print(f"{self.marca} se mueve por tierra")

class Avion(Transporte):
    def __init__(self, marca):
        super().__init__(marca)
    
    def moverse(self):
        print(f"{self.marca} se mueve por el aire")

class Barco(Transporte):
    def __init__(self, marca):
        super().__init__(marca)
    
    def moverse(self):
        print(f"{self.marca} se mueve por el agua")

carro = Carro("Audi")
avion = Avion("Airplane")
barco = Barco("Pesquero")

lista = [carro, avion, barco]

def runList(lista):
    for item in lista:
        item.moverse()

runList(lista)

