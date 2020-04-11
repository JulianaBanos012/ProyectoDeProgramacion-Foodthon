from tkinter import *

ventana = Tk()
ventana.geometry("400x200")
ventana.configure(bg="lightyellow")
ventana.title("¿Qué tipo de comida desea?")

List1 = ['Costeño', 'Cachaco', 'Paisa', 'Continental', 'Americano']

def Desayunos():
    print(List1)

List2 = ['Vegetariano', 'Carnívoro', 'Gringo', 'Continental', 'Asiático']

def Almuerzos():
    print(List2)

BotonDesayunos = Button(ventana, text="Desayunos", command=Desayunos)
BotonDesayunos.pack(side=LEFT)

BotonAlmuerzos = Button(ventana, text="Almuerzos", command=Almuerzos)
BotonAlmuerzos.pack(side=LEFT)


ventana.mainloop()
