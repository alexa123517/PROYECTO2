class Empleado:
    total_empleados = 0

    def __init__(self, nombre, edad):
        self.nombre = self.validar_nombre(nombre)
        self.edad = self.validar_edad(edad)
        Empleado.total_empleados += 1

    def validar_nombre(self, nombre):
        if isinstance(nombre, str) and nombre.strip():
            return nombre
        print("Nombre inválido. Se asigna 'Desconocido'.")
        return 'Desconocido'

    def validar_edad(self, edad):
        if isinstance(edad, int) and 18 <= edad <= 65:
            return edad
        print("Edad inválida. Se asigna 18.")
        return 18

    def mostrar_info(self):
        print(f"Empleado: {self.nombre}, Edad: {self.edad}")

    @classmethod
    def contar_empleados(cls):
        print(f"Total empleados registrados: {cls.total_empleados}")


class Desarrollador(Empleado):
    def __init__(self, nombre, edad, lenguaje):
        super().__init__(nombre, edad) 
        self.lenguaje = self.validar_lenguaje(lenguaje)

    def validar_lenguaje(self, lenguaje):
        if isinstance(lenguaje, str) and lenguaje.strip():
            return lenguaje
        print("Lenguaje inválido. Se asigna 'Python'.")
        return "Python"

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Lenguaje de programación: {self.lenguaje}")


class Diseñador(Empleado):
    def __init__(self, nombre, edad, herramienta):
        super().__init__(nombre, edad)  
        self.herramienta = self.validar_herramienta(herramienta)

    def validar_herramienta(self, herramienta):
        if isinstance(herramienta, str) and herramienta.strip():
            return herramienta
        print("Herramienta inválida. Se asigna 'Figma'.")
        return "Figma"

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Herramienta de diseño: {self.herramienta}")


class FreelanceDev(Desarrollador, Diseñador):
    def __init__(self, nombre, edad, lenguaje, herramienta, tarifa_hora):
        Desarrollador.__init__(self, nombre, edad, lenguaje)  
        Diseñador.__init__(self, nombre, edad, herramienta)  
        self.tarifa_hora = self.validar_tarifa(tarifa_hora)

    def validar_tarifa(self, tarifa):
        if isinstance(tarifa, (int, float)) and tarifa > 0:
            return tarifa
        print("Tarifa inválida. Se asigna 50.0.")
        return 50.0

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Herramienta de diseño: {self.herramienta}")
        print(f"Tarifa por hora: ${self.tarifa_hora}")


e1 = Empleado("Ana", 30)
e2 = Desarrollador("Luis", 25, "JavaScript")
e3 = Diseñador("Laura", 28, "Illustrator")
e4 = FreelanceDev("Carlos", 35, "Python", "Photoshop", 80.0)
e5 = FreelanceDev("", 17, "", "", -5)

print("\n--- Información de Empleados ---")
for e in [e1, e2, e3, e4, e5]:
    e.mostrar_info()
    print("-" * 30)

Empleado.contar_empleados()




