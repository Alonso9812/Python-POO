# DIP Principio de inversion de dependencias
#

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass

class Diccironario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Logica para verificar palabra
        pass

class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # metodo para verificar palabra desde el servico web
        pass

class CorrectorOrtografico:
    def __init__(self, verficador):
        self.verificar = self.verificar

    def corregir_texto(self, texto):
        # usamos el verificador para corregir el texto 

corrector = CorrectorOrtografico(Diccironario())