# LSP principio de sustitución de liskov's establece que la clases derivadas tienen que ser sustituible por sus clases base
# Si tengo un clase base las otras clase que hereden de la clase base tienen que hacer todo lo que la clase base haga
class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"

class AveNoVoladora(Ave):
    pass

