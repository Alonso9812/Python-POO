class Banco:
    def crear_cuenta(self, nombre, saldo_inicial):
        return Cuenta(nombre, saldo_inicial)  

    def mostrar_cuentas(self, cuentas):
        for cuenta in cuentas:
            print(f"Cuenta de {cuenta.nombre} con saldo: {cuenta.saldo}")  
    
class Cuenta:
    def __init__(self, nombre, saldo_inicial):
        self.nombre = nombre
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depositado {cantidad} en la cuenta de {self.nombre}. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print(f"Fondos insuficientes en la cuenta de {self.nombre}. Saldo actual: {self.saldo}")
        else:
            self.saldo -= cantidad
            print(f"Retirado {cantidad} de la cuenta de {self.nombre}. Nuevo saldo: {self.saldo}")

banco = Banco()
cuenta1 = banco.crear_cuenta("Alice", 1000)
cuenta2 = banco.crear_cuenta("Bob", 500)
banco.mostrar_cuentas([cuenta1, cuenta2])
cuenta1.depositar(200)
cuenta2.retirar(100)
banco.mostrar_cuentas([cuenta1, cuenta2])
    

    