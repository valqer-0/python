class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"'{self.titulo}' escrito por: {self.autor}"

    def __len__(self):
        return self.paginas

Libro = Libro("IT Chapter I                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ", "Stephen King", 1489)
print(Libro)
print(len(Libro))