class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f"'{self.nombre}', fuerza={self.fuerza}, velocidad={self.velocidad})"
    
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + " " + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza) / 2) ** 1.34)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad) / 2) ** 1.34)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
    
# Ejemplo de uso
goku = Personaje("Goku", 100, 80)
vegeta = Personaje("Vegeta", 90, 70)
fusion = goku + vegeta
print(fusion)