#Gestionar cuenta bancaria 

class CuentaBancaria:
    def __init__(self, titular, nCuenta, saldo):
        self.titular = titular
        self.nCuenta = nCuenta
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        print(f"Depositando {monto} a la cuenta de {self.titular}")

    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"Retirando {monto} de la cuenta de {self.titular}")
        else:
            print("Saldo insuficiente")

    def mostrar_saldo(self):
        print(f" El saldo de la cuenta de {self.titular} es: {self.saldo} ")


titular = input("Ingrese el nombre del titular de la cuenta: ")
nCuenta = float(input("Ingrese el numero de cuenta: "))
saldo = float(input("Ingrese el saldo de la cuenta: "))

cuenta = CuentaBancaria(titular, nCuenta, saldo)
print(f"""DATOS DE LA CUENTA: \n\n
      Titullar: {cuenta.titular} \n
      Numero de cuenta: {cuenta.nCuenta} \n
      Saldo: {cuenta.saldo}""")

#CREANDO UN MENU PARA REALIZAR LAS OPERACIONES DE LA CUENTA BANCARIA
while True:
    print("1. Depositar")
    print("2. Retirar")
    print("3. Mostrar saldo")
    print("4. Salir")

    opcion = input("Ingrese la opcion que desea realizar: ")

    if opcion == "1":
        monto = float (input("ingrese el monto a depositar: "))
        cuenta.depositar(monto)
    elif opcion == "2":
        monto = float (input("Ingrese el monto a retirar: "))
        cuenta.retirar(monto)
    elif opcion == "3":
        cuenta.mostrar_saldo()
    elif opcion == "4":
        print("Saliendo del programa...")
        break   



