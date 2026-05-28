class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def saltar(self):
        print("El perro esta saltando")

#Creando el objeto perro con los datos ingresados por el usuario
nombre = input("Ingrese el nombre del perro: ")
raza = input("Ingrese la raza del perro: ")

#Creando el objeto perro con los datos ingresados por el usuario
perro = Perro(nombre, raza)
print(f"""DATOS DEL PERRO:  \n\n 
         Nombre: {perro.nombre} \n
         Raza: {perro.raza}""")

#Haciendo que el perro salte cada vez que el usuario ingrese "silvar"
while True:
    saltar = input()
    if(saltar.lower() == "silvar"):
        perro.saltar()

    #forzando a salir del bucle
    if(saltar.lower() == "silvar"):
        break   
    

