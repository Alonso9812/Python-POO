# El OCP es un principio SOLID denominado "Principio Abierto Cerrado" su funcionalidad es hacer que el codigo
# se pueda mejorar, agregar funcionalidades sin tener que modificar lo que ya esta hecho.

class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje 

    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por emmail: {self.usuario.email}")


class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje sms a: {self.usuario.sms}")

class NotificadorWhatsapp(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por WhatsApp: {self.usuario.whatsapp}")