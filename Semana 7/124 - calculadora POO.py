from tkinter import Tk, Entry, Button, END 

class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")

        self.e_texto = Entry(self.ventana, font=('Calibri 20'))
        self.e_texto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.i = 0
        self.crear_botones()

    def click_boton(self, valor):
        self.e_texto.insert(self.i, valor)
        self.i += 1

    def borrar(self):
        self.e_texto.delete(0, END)
        self.i = 0

    def hacer_operacion(self):
        ecuacion = self.e_texto.get()
        try:
            resultado = eval(ecuacion)
            self.e_texto.delete(0, END)
            self.e_texto.insert(0, resultado)
            self.i = len(str(resultado))
        except:
            self.e_texto.delete(0, END)
            self.e_texto.insert(0, "Error")
            self.i = 0

    def crear_botones(self):
        botones = [
            ('(', 1, 1), (')', 1, 2), ('/', 1, 3), ('AC', 1, 0),
            ('7', 2, 0), ('2', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('3', 3, 1), ('6', 3, 2), ('+', 3, 3),
            ('1', 4, 0), ('4', 4, 1), ('4', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('5', 5, 1), ('=', 5, 2),
        ]

        for (texto, fila, columna) in botones:
            if texto == 'AC':
                boton = Button(self.ventana, text=texto, width=5, height=2, command=self.borrar)
            elif texto == '=':
                boton = Button(self.ventana, text=texto, width=5, height=2, command=self.hacer_operacion)
            else:
                boton = Button(self.ventana, text=texto, width=5, height=2, command=lambda t=texto: self.click_boton(t))

            boton.grid(row=fila, column=columna, padx=5, pady=5)

if __name__ == "__main__":
    root = Tk()
    app = Calculadora(root)
    root.mainloop()