# Polimorfismo em Python es la capacidad de un objeto de comportarse de diferentes formas dependiendo del contexto en el que se utilice.
# En Python, el polimorfismo se logra a través de la herencia y la sobreescritura de métodos.


class Gato:
    def falar(self):
        return "Miau"
    
class Cachorro:
    def falar(self):
        return "Au Au" 

def emitir_som(animal):
    print(animal.falar()) 
    
gato = Gato()
cachorro = Cachorro()

emitir_som(gato)  # Output: Miau

print(cachorro.falar())  # Output: Au Au


def recorrer(elemento):
    for item in elemento:
        print(f"El elemenento es: {item}")


lista = [1, 2, 3, 4, 5]
lista2 = ["a", "b", "c", "d"]
recorrer(lista)  # Output: El elemenento es: 1, El elemenento es: 2, El elemenento es: 3, El elemenento es: 4, El elemenento es: 5
recorrer(lista2)  # Output: El elemenento es: a, El elemenento es: b, El elemenento es: c, El elemenento es: d