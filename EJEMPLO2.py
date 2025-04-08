class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")

class Perro(Animal):
    def __init__(self, nombre, especie, raza):
        super().__init__(nombre, especie)
        self.raza = raza

    def mostrar_raza(self):
        print(f"Raza: {self.raza}")

mi_perro = Perro("Tommy", "Perro", "Border Collie")
mi_perro.mostrar_informacion()
mi_perro.mostrar_raza()
