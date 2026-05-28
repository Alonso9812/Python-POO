# registro de actividad del sistema

def registrar_accion(funcion):
    def accion():
        print(" INICIANDO SISTEMA ")
        print(f"Ejecutando: {funcion.__name__}")
        funcion()
        print(" ACCION FINALIZADA ")
    return accion
    

@registrar_accion
def abrir_programa():
    print("Estoy abriendo el programa")

@registrar_accion
def guardar_archivo():
    print("Estoy guardando el archivo")

@registrar_accion
def cerrar_programa():
    print("cerrando el programa")

abrir_programa()
guardar_archivo()
cerrar_programa()
