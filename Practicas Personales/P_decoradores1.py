#Practica de decoradores Login

def verificar_login(funcion):

    def login():
        print("Bienvenidos")

        usuario = "Jordi1298"
        password = "1234"

        a_usuario = input("Ingrese su nombre de usuario: ")
        a_password = input("Ingrese su contraseña: ")

        if a_usuario == usuario and a_password == password:
            funcion()
        else:
            print("Acceso denegado: Usuario o Contraseña incorrecta...")      
    return login

@verificar_login
def acceso():
    print("Acceso concedido, bienvenido Jordi1298!")

@verificar_login
def eliminar_cuenta():
    print("Cuenta eliminada")

acceso()
eliminar_cuenta()