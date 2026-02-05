from tkinter import *

ventana = Tk()
ventana.title("Sistema Grid")
ventana.geometry("400x300")

label1 = Label(ventana, text="Fila 0, Columna 0")
label2 = Label(ventana, text="Fila 0, Columna 1")
label3 = Label(ventana, text="Fila 1, Columna 0")
label4 = Label(ventana, text="Fila 1, Columna 1")

label1.grid(row=0, column=0, padx=15, pady=15)
label2.grid(row=0, column=1, padx=15, pady=15)
label3.grid(row=1, column=0, padx=15, pady=15)
label4.grid(row=1, column=1, padx=15, pady=15)

entrada = Entry(ventana, font=("Arial", 20))
entrada.grid(row=2, column=0, columnspan=2, padx=15, pady=15)

boton1 = Button(ventana, text="Salir", command=ventana.quit)
boton1.grid(row=3, column=0)

ventana.mainloop()