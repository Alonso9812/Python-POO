# Decoradores son funciones que modifican el comportamiento de otras funciones. Se utilizan para agregar funcionalidad
#  adicional a una función sin modificar su código original.

def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la función")
        funcion()
    return funcion_modificada

@decorador
def saludo():
    print("Hola, Jordi!")

saludo()  # Esto imprimirá "Antes de llamar a la función" seguido de "Hola, Jordi!"