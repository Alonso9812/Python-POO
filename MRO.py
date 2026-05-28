# El MRO (Method Resolution Order) es el orden en el que Python busca métodos y atributos en una jerarquía de clases.
# En Python, el MRO se determina utilizando el algoritmo C3 Linearization, que garantiza un orden consistente y predecible
#  para la resolución de métodos en casos de herencia múltiple.

class A:
    def method(self):
        return "Method in A"
    
class F:
    def method(self):
        return "Method in F"
    
class B(A, F):
    def method(self):
        return "Method in B"
    
class C(F):
    pass
    
class D(B, C):
    pass

d = D()
print(d.method())  # Output: "Method in D"  
print(D.mro())  # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.F'>, <class 'object'>]


