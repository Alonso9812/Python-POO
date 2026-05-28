#Gestionar cuenta de usuario

class Usuario:
    def __init__(self, nombre, password, saldo):
        self.nombre = nombre
        self.__password = password
        self.__saldo = saldo

    def mostrar_nombre(self):
        print(F"Nombre de usuario {self.nombre}")

    def consultar_saldo(self):
        print(f"{self.nombre} su saldo es de: {self.__saldo}")
    
    def depositar(self, monto):
        self.__saldo += monto
        print(f"Haz depositado {monto} con exito")

    def retirar(self, monto):
        if self.__saldo >= monto:
            self.__saldo -= monto
            print(f"Haz retirado {monto} de la cuenta de {self.nombre} con exito!!")
        elif self.__saldo < monto:
            print("Saldo insuficiente")

    def cambiar_pw(self):
        password_actual = input("Ingrese la contraseña actual: ")

        if password_actual == self.__password:
            new_password = input("Ingrese la nueva contraseña")
            self.__password = new_password
            print("Contraseña actualizada con exito: ")
        else:
            print("contarseña incorrecta :(")
        

nombre = input("Ingrese su nombre: ")
password = input(" Ingrese la contraseña: ")
saldo = float(input("Ingrrese el sado de la cuenta: "))

usuario = Usuario(nombre, password, saldo)
print(f""" DATOS DE LA CUENTA \n
      Nombre: {usuario.nombre}""")

while True:
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. retirar")
    print("4. Cambiar password")
    print("5. Salir")

    opcion = input("Selecione la opcion que de sea realizar: ")

    if opcion == "1":
        usuario.consultar_saldo()
    elif opcion == "2":
        monto = float(input("Ingrese el monto a depositar: "))
        usuario.depositar(monto)
    elif opcion == "3":
        monto = float(input("Ingrese el monto a retirar: "))
        usuario.retirar(monto)
    elif opcion == "4":
        usuario.cambiar_pw()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
        
