class Celular:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

#Metodos de la clase Celular
    def llamar(self, numero):
        print(f"Llamando al numero {numero} desde el celular {self.modelo}")

    def cortar(self):
        print(f"Cortando la llamada desde el celular {self.modelo}")

#Creando objetos de la clase Celular
celular1 = Celular("Apple", "iphone 17", 1000)
celular2 = Celular("Samsung", "Galaxy S26", 1000)

#llamando a los atributos de la clase Celular
print(celular1.modelo)
print(celular2.modelo)

#Llamando a los metodos de la clase Celular
celular1.llamar("123456789")
celular2.cortar()