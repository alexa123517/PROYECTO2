class Persona:
    total_personas = 0

    def __init__(self, nombre, edad):
        self.nombre = self.validar_nombre(nombre)
        self.edad = self.validar_edad(edad)
        Persona.total_personas += 1

    @staticmethod
    def validar_edad(edad):
        if isinstance(edad, int) and 6 <= edad <= 100:
            return edad
        print("Edad inválida. Se asigna 6.")
        return 6

    def validar_nombre(self, nombre):
        if isinstance(nombre, str) and nombre.strip():
            return nombre
        print("Nombre inválido. Se asigna 'Desconocido'.")
        return "Desconocido"

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    @classmethod
    def contar_personas(cls):
        print(f"Total de personas registradas: {cls.total_personas}")


class Tutor(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = self.validar_asignatura(asignatura)

    def validar_asignatura(self, asignatura):
        if isinstance(asignatura, str) and asignatura.strip():
            return asignatura
        print("Asignatura inválida. Se asigna 'General'.")
        return "General"

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Asignatura: {self.asignatura}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = self.validar_grado(grado)

    def validar_grado(self, grado):
        if isinstance(grado, str) and grado.strip():
            return grado
        print("Grado inválido. Se asigna 'Sin asignar'.")
        return "Sin asignar"

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Grado: {self.grado}")


class EstudianteTutor(Estudiante, Tutor):
    def __init__(self, nombre, edad, grado, asignatura):
        
        super().__init__(nombre, edad, grado)  
        Tutor.__init__(self, nombre, edad, asignatura)  

    def mostrar_info(self):
        super().mostrar_info()  
        print(f"Asignatura como tutor: {self.asignatura}")



e1 = Persona("Juan", 30)
e2 = Tutor("Ana", 40, "Matemáticas")
e3 = Estudiante("Luis", 18, "Primero")
e4 = EstudianteTutor("Lucía", 22, "Segundo", "Historia")

print("\n--- Información de Personas ---")
for p in [e1, e2, e3, e4]:
    p.mostrar_info()
    print("-" * 30)

Persona.contar_personas()


def mostrar_info(self):
        super().mostrar_info()
        print(f"Asignatura: {self.asignatura}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = self.validar_grado(grado)

    def validar_grado(self, grado):
        if isinstance(grado, str) and grado.strip():
            return grado
        print("Grado inválido. Se asigna 'Sin asignar'.")
        return "Sin asignar"

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Grado: {self.grado}")


class EstudianteTutor(Estudiante, Tutor):
    def __init__(self, nombre, edad, grado, asignatura):
        
        Estudiante.__init__(self, nombre, edad, grado)  
        Tutor.__init__(self, nombre, edad, asignatura)  

    def mostrar_info(self):
        super().mostrar_info() 
        print(f"Asignatura como tutor: {self.asignatura}")



e1 = Persona("Juan", 30)
e2 = Tutor("Ana", 40, "Matemáticas")
e3 = Estudiante("Luis", 18, "Primero")
e4 = EstudianteTutor("Lucía", 22, "Segundo", "Historia")

print("\n--- Información de Personas ---")
for p in [e1, e2, e3, e4]:
    p.mostrar_info()
    print("-" * 30)

Persona.contar_personas()

