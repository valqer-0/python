class Pokemon:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print(f"{self.nombre} ruido de pokemon general")

    def dormir(self):
        print(f"{self.nombre} está durmiendo")


class TipoElectrico(Pokemon):
    def hacer_sonido(self):
        print(f"{self.nombre} dice pika pika!")


class TipoFuego(Pokemon):
    def hacer_sonido(self):
        print(f"{self.nombre} dice char!")

# Crear instancias de cada tipo de Pokémon
pikachu = TipoElectrico("Pikachu", 5)
charmander = TipoFuego("Charmander", 4)

# Llamar a los métodos para cada instancia
pikachu.hacer_sonido()
pikachu.dormir()

charmander.hacer_sonido()
charmander.dormir()
