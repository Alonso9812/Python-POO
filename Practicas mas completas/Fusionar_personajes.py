# Fusionar personajes

class Personaje:

    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def mostrar_personaje(self):
        print(f""" INFORMACION DEL PERSONAJE
                Nombre: {self.nombre}
                Fuerza: {self.fuerza}
                Velocidad: {self.velocidad}
                """)

    def __repr__(self):
        return f"{self.nombre}, Fuerza={self.fuerza}, Velocidad={self.velocidad}"

    # Sobrecarga del operador +
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + " " + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza) / 2) ** 1.34)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad) / 2) ** 1.34)

        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)


# PERSONAJE 1
nombre = input("Ingrese nombre del personaje: ")
fuerza = int(input("Ingrese la fuerza del personaje: "))
velocidad = int(input("Ingrese la velocidad del personaje: "))

personaje1 = Personaje(nombre, fuerza, velocidad)


# PERSONAJE 2
nombre = input("Ingrese nombre del personaje: ")
fuerza = int(input("Ingrese la fuerza del personaje: "))
velocidad = int(input("Ingrese la velocidad del personaje: "))

personaje2 = Personaje(nombre, fuerza, velocidad)


def fusion():
    return personaje1 + personaje2


while True:

    print("\n1. Fusionar Personajes")
    print("2. Mostrar Personajes")
    print("3. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        personaje_fusionado = fusion()
        print("\nPERSONAJE FUSIONADO")
        personaje_fusionado.mostrar_personaje()
    elif opcion == "2":
        print("\nPERSONAJE 1")
        personaje1.mostrar_personaje()
        print("\nPERSONAJE 2")
        personaje2.mostrar_personaje()
    elif opcion == "3":
        print("Saliendo del menu...")
        break


# crear una funcion que permita crear personajes los guarde en una lista y luego permita fusionar los personajes de la lista,
#  mostrando el resultado de la fusion.