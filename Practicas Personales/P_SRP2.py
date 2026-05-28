# Gestionar usuarios de plataforma de streaming
class Usuario:
    def __init__(self, nombre, correo, tipo_suscripcion):
        self.nombre = nombre
        self.correo = correo
        self.tipo_suscripcion = tipo_suscripcion

    def mostrar_info(self):
        print(f""" DATOS DEL USUARIO
              Nombre: {self.nombre}
              Correo: {self.correo}
              Suscripción: {self.tipo_suscripcion} """)
        
class ValidarCorreo:
    def validar_correo(self, correo):
       if "@" in correo.correo and ".com" in correo.correo: 
            print("Correo valido")
       else: 
           print("Correo invalido")

class GestionarSuscripcion:
    def cambiar_suscripcion(usuario, nueva_suscripcion):
        usuario.tipo_suscripcion = nueva_suscripcion
        print(f"La nueva suscripcion es: {nueva_suscripcion}")
        

class GeneradorDeResumen:
    def generar(self, usuarios):
        print("Usuarios Suscritos")

        for usuario in usuarios:
            print(f""" 
                  {usuario.nombre},
                  {usuario.correo},
                  {usuario.tipo_suscripcion}""")

class GuardarUsuarios:
    def guardar(self,usuarios):
        with open("Usuarios_suscritos.txt", "w")  as archivo:
            for usuario in usuarios:
                archivo.write(f"{usuario.nombre}, {usuario.correo}, {usuario.tipo_suscripcion}\n")
            archivo.write("Usuarios Suscritos\n")

usuario1 = Usuario("Jordi", "jordi@gmail.com", "Familiar")
usuario2 = Usuario("Marta", "marta@gmail.com", "Básico")
usuario3 = Usuario("Quevedo", "Quevedo@gmail.com", "Premium")

usuarios = [usuario1, usuario2, usuario3]

def mostrar_datos(usuarios):
    for item in usuarios:
        item.mostrar_info()

mostrar_datos(usuarios)

validar = ValidarCorreo()
validar.validar_correo(usuario1)

Nueva_suscripcion = "Familiar"
GestionarSuscripcion.cambiar_suscripcion(usuario2, Nueva_suscripcion)

generar = GeneradorDeResumen()
generar.generar(usuarios)   

guardar = GuardarUsuarios()
guardar.guardar(usuarios)

