#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 17:02:19 2020

@author: juliana
"""

from tkinter import *
from PIL import ImageTk, Image

class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      Counter = 0
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.grid(row=Counter, sticky=W)
         self.vars.append(var)
         Counter += 1
         
   def state(self):
      return map((lambda var: var.get()), self.vars)
  

SIZE = '500x500'

ventana = Tk()
ventana.geometry(SIZE)

HEIGHT = 500
WIDTH = 500

canvas = Canvas(ventana, height=500, width=500, bg='lightgreen')
canvas.pack(expand= YES, fill=BOTH)

path = "./food.jpg"

frame = Frame(ventana, bg='lightblue' )
frame.place(relheight=0.5, relwidth=0.8, relx=0.1, rely=0.2)
img = ImageTk.PhotoImage(Image.open(path))
frameLabel = Label(frame, image=img)
frameLabel.place(relheight=1, relwidth=1, relx=0, rely=0)
frame1 = Frame(frame, bg='#f1d924')
frame1.place(relheight=0.8, relwidth=0.4, relx=0.05, rely=0.1)
frame2 = Frame(frame, bg='pink')
frame2.place(relheight=0.8, relwidth=0.4, relx=0.5, rely=0.1)

ventana.title("Bienvenido a FoodThon")

Introduction = '¡Bienvenido a Foodthon!\n Nuestros creadores son: \n Juliana Baños\n Jaider Daza\n Juan Pablo Guerrero'
Pasosaseguir = '1) Escoja su tipo de plato \n2) Seleccione los ingredientes que tiene'
    
def go(counter=1):
    l.config(text=Introduction[:counter])
    canvas.after(150, lambda: go(counter+1))

l = Label(canvas)
l.place(relx=0,rely=0.1)

def go1(counter=1):
    d.config(text=Pasosaseguir [:counter])
    canvas.after(150, lambda: go1(counter+1))

d = Label(canvas)
d.place(relx=0.3,rely=0.1)
    
def callback():
    print ("called the callback!")

def Desayunos():   
    lng = Checkbar(frame1, IngredientesDesayuno)
    lng.grid(row=2, column=0)
    lng.config(relief=GROOVE, bd=2)
    def allstates(): 
        print(list(lng.state()))
    Button(frame1, text='Quit', command=ventana.quit).grid(row=3, column=0)
    Button(frame1, text='PeekDesayunos', command=allstates).grid(row=3, column=1)

def Almuerzos():
    lng = Checkbar(frame2, IngredientesAlmuerzo)
    lng.grid(row=2, column=2)
    lng.config(relief=GROOVE, bd=2)
    def allstates(): 
        print(list(lng.state()))
    Button(frame2, text='Quit', command=ventana.quit).grid(row=3, column=2)
    Button(frame2, text='PeekAlmuerzos', command=allstates).grid(row=3, column=3)
    
def BotonDesayuno():
    BotonDesayunos = Button(frame1, text="Desayunos", command=Desayunos)
    BotonDesayunos.grid(row=1, column=0)

def BotonAlmuerzo():
    BotonAlmuerzos = Button(frame2, text="Almuerzos", command=Almuerzos)
    BotonAlmuerzos.grid(row=1, column=2)
    
#Create a Menu
    
menu = Menu(ventana)
ventana.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="Information", menu=filemenu)
filemenu.add_command(label="Introducción", command=go)
filemenu.add_command(label="Pasos a seguir", command=go1)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=callback)

platosmenu = Menu(menu)
menu.add_cascade(label='Platos',menu=platosmenu)
platosmenu.add_command(label='Desayunos', command=BotonDesayuno)
platosmenu.add_command(label='Almuerzos', command=BotonAlmuerzo)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=callback)

IngredientesDesayuno = ['Huevos', 'Pan', 'Leche', 'Tocineta', 'Champiñones']

p = "./images.jpg"
img1 = Image.open(p)
img1 = img1.resize((50,50), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(img1)
frameLabel = Label(frame1, image=img2)
frameLabel.place(relx=1, x=-2,y=2,anchor = NE)


IngredientesAlmuerzo = ['Arroz', 'Fríjoles', 'Maíz', 'Pechuga', 'Carne', 'Lentejas', 'maíz', 'quinoa']

p = "./food.jpg"
img3 = Image.open(p)
img3 = img3.resize((50,50), Image.ANTIALIAS)
img4 = ImageTk.PhotoImage(img3)
frameLabel = Label(frame2, image=img4)
frameLabel.place(relx=1, x=-2,y=2,anchor = NE)

ventana.mainloop()
