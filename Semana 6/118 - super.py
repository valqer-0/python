class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        print(f"Empleado: {self.nombre}")
        print(f"Salario: Q. {self.salario}")

class Programador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    def programar(self):
        print(f"{self.nombre} está programando en {self.lenguaje}")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Lenguaje: {self.lenguaje}")
    
dev = Programador(nombre="Carlos", salario=8000, lenguaje="Python")

dev.mostrar_info()
dev.programar()

rrhh = Empleado(nombre="Margareth", salario=6000)
rrhh.mostrar_info()   