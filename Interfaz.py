#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 17:02:19 2020

@author: juliana
"""
import time
from tkinter import *
from Desayunos import *
from Almuerzos import *
from Cenas import *
from Postres import *
from PIL import ImageTk, Image
import webbrowser

class Boton:
    def __init__(self, frameB, textB, commandB, rowB, columnB):
        self.frame = frameB
        self.text = textB
        self.command = commandB
        self.row = rowB
        self.column = columnB
        
    def create(self):
        A = Button(self.frame, text= self.text, command= self.command)
        A.grid(row= self.row, column= self.column)
        
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
                 
ventana = Tk()
ventana.geometry('1200x1000')
ventana.title("¡Bienvenido a FoodThon!")

canvas = Canvas(ventana, height= 1000, width= 1000, bg='lightgreen') 
canvas.config(relief= RIDGE, bd= 8)
canvas.pack(expand= YES, fill= BOTH)

#Frames

frame = Frame(ventana, bg='lightblue' )
frame.place(relheight=0.99, relwidth=0.492, relx=0.5, rely=0.008)

frame3 = Frame(ventana)
frame3.config(relief=RIDGE, bd=8)
frame3.place(relheight=0.17, relwidth=0.09, relx=0.007, rely=0.013)

#Imágenes

path1 = "./Foodthon.png"

imf = Image.open(path1)
imf = imf.resize((100,100), Image.ANTIALIAS)
imf1 = ImageTk.PhotoImage(imf)
frameLabel = Label(frame3, image=imf1)
frameLabel.pack()

path = "./food.jpg"

img = ImageTk.PhotoImage(Image.open(path))
frameLabel = Label(frame, image=img)
frameLabel.place(relheight=1, relwidth=1, relx=0, rely=0)

#Frames

frame1 = Frame(frame, bg='#f1d924')
frame1.config(relief=GROOVE)
frame1.place(relheight=0.8, relwidth=0.4, relx=0.05, rely=0.1)

frame2 = Frame(frame, bg='pink')
frame2.config(relief=GROOVE)
frame2.place(relheight=0.8, relwidth=0.4, relx=0.55, rely=0.1)

#Texto de Botones Introductorios

Introduction = '¡Bienvenido a Foodthon!\n Nuestros creadores son: \n Juliana Baños\n Jaider Daza\n Juan Pablo Guerrero'
Pasosaseguir = Pasosaseguir = '1) Entre a la pestaña Platos y escoja su tipo de plato.\n2) Seleccione los ingredientes con los que cuenta y    \npresione el botón Peek.                                \n3) Espere a que el programa le devuelva sus            \nposibles recetas, en la parte inferior de este cuadro. \n4) Al saber qué recetas puede preparar con los         \n  ingredientes que tiene, diríjase a la pestaña de recetas  \npara mirar su preparación.                             \n        5) Si desea volver a intentarlo, cargue nuevamente el programa.'
    
#Efecto de Máquina

def go(counter=1):
    l.config(text=Introduction[:counter])
    canvas.after(50, lambda: go(counter+1))

l = Label(canvas,bg="lightgreen", font= 'Verdana 13 bold')
l.place(relx=0.15,rely=0.15)

def go1():
    d = Label(canvas, text=Pasosaseguir, bg="lightgreen", font='Verdana 10')
    d.place(relx=0.07,rely=0.3)

#Botones Introductorios

IntroducciónButton = Button(canvas,text='Introducción', command=go)  
IntroducciónButton.place(relx=0.15, rely=0.04) 
    
Pasos = Button(canvas,text='Pasos a Seguir', command=go1)  
Pasos.place(relx=0.15, rely=0.08) 
    
#Checkboxes
#Comparación de listas

def Desayunos():   
    lng = Checkbar(frame1, IngredientesDesayuno)
    lng.grid(row=2, column=0)
    lng.config(relief=RAISED, bd=5)
    def quitt():
        lng.grid_forget()
 
    def allstates(): 
        time.sleep(1.5)
        DesayunosState = list(lng.state())
        DictDesayunos = dict(zip(IngredientesDesayuno, DesayunosState))
        IngredientesDFinales = []
        for i in DictDesayunos:
            if DictDesayunos[i] == 1:
                IngredientesDFinales.append(i)  
        DesayunosRecetas(IngredientesDFinales,ventana)
        #Se importa del módulo Desayunos para realizar la comparación
    Button(frame1, text='Quit', command=quitt).grid(row=3, column=0)
    Button(frame1, text='Peek', command=allstates).grid(row=3, column=1)
    
def Almuerzos():
    lng = Checkbar(frame2, IngredientesAlmuerzo)
    lng.grid(row=2, column=0)
    lng.config(relief=RAISED, bd=5)
    def quitt():
        lng.grid_forget()
        
    def allstates():
        time.sleep(1.5)
        AlmuerzosState = list(lng.state())
        DictAlmuerzos = dict(zip(IngredientesAlmuerzo, AlmuerzosState))
        IngredientesAFinales = []
        for i in DictAlmuerzos:
            if DictAlmuerzos[i] == 1:
                IngredientesAFinales.append(i)
        AlmuerzosRecetas(IngredientesAFinales, ventana)
    Button(frame2, text='Quit', command=quitt).grid(row=3, column=0)  
    Button(frame2, text='Peek', command=allstates).grid(row=3, column=1)
    
def Comidas():
    lng = Checkbar(frame1, IngredientesCena)
    lng.grid(row=6, column=0)
    lng.config(relief=RAISED, bd=5)
    def quitt():
        lng.grid_forget()
    def allstates(): 
        time.sleep(1.5)
        ComidasState = list(lng.state())
        DictCenas = dict(zip(IngredientesCena, ComidasState))
        IngredientesCFinales = []
        for i in DictCenas:
            if DictCenas[i] == 1:
                IngredientesCFinales.append(i)  
        CenasRecetas(IngredientesCFinales, ventana)
    Button(frame1, text='Quit', command=quitt).grid(row=7, column=0)  
    Button(frame1, text='Peek', command=allstates).grid(row=7, column=1)

def Postres():
    lng = Checkbar(frame2, IngredientesPostre)
    lng.grid(row=6, column=0)
    lng.config(relief=RAISED, bd=5)
    def quitt():
        lng.grid_forget()

    def allstates(): 
        time.sleep(1.5)
        PostresState = list(lng.state())
        DictPostres = dict(zip(IngredientesPostre, PostresState))
        IngredientesPFinales = []
        for i in DictPostres:
            if DictPostres[i] == 1:
                IngredientesPFinales.append(i)
        PostresRecetas(IngredientesPFinales, ventana)
    Button(frame2, text='Quit', command=quitt).grid(row=7, column=0)  
    Button(frame2, text='Peek', command=allstates).grid(row=7, column=1)

#Se crean objetos de la clase Boton

def BotonDesayuno():
    BotonDesayunos = Boton(frame1, "Desayunos", Desayunos, 1, 0)
    BotonDesayunos.create()
    
def BotonAlmuerzo():
    BotonAlmuerzos = Boton(frame2, "Almuerzos", Almuerzos, 1, 0)
    BotonAlmuerzos.create()

def BotonComida():
    BotonComidas = Boton(frame1, "Comidas", Comidas, 5, 0)
    BotonComidas.create()

def BotonPostre():
    BotonPostres = Boton(frame2, "Postres", Postres, 5, 0)
    BotonPostres.create()
    
#Se crea el Menú de la parte superior
    
menu = Menu(ventana)
ventana.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="Information", menu=filemenu)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)

platosmenu = Menu(menu)
menu.add_cascade(label='Platos',menu=platosmenu)
platosmenu.add_command(label='Desayunos', command=BotonDesayuno)
platosmenu.add_command(label='Almuerzos', command=BotonAlmuerzo)
platosmenu.add_command(label='Comidas', command=BotonComida)
platosmenu.add_command(label='Postres', command=BotonPostre)

recmenu = Menu(menu)
menu.add_cascade(label="Recetas", menu=recmenu)
recmenu.add_command(label="Desayunos.", command=Des)
recmenu.add_command(label="Almuerzos.", command=Alm)
recmenu.add_command(label="Cenas.", command=Com)
recmenu.add_command(label="Postres.", command=Pos)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

#Listas de Ingredientes - Desayuno

IngredientesDesayuno = ['Huevos', 'Queso', 'Jamon', 'Leche', 'Harina', 'Aceite', 'Sal', 'Pimienta', 'Manzanas', 'Azucar', 'Levadura', 'Miel', 'Canela', 'Avena' , 'Banano', 'Fresas', 'Platanos', 'Limon', 'Pan', 'Chocolate', 'Mantequilla', 'Crema de leche', 'Durazno', 'Lechuga','Atun', 'Mayonesa']

#Imagen de Listas Desayunos y Cenas

p = "./desayuno.jpg"
img1 = Image.open(p)
img1 = img1.resize((50,50), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(img1)
frameLabel = Label(frame1, image=img2)
frameLabel.place(relx=1, x=-2,y=2,anchor = NE)

#Listas Ingredientes - Almuerzo

IngredientesAlmuerzo = ["Papas","Champiñones","Mantequilla","Queso","Especias","Caldo","Sal y Pimienta","Pasta","Palta","Ajo","Limon","Aceite","Choclo","Tomates","Carne","Panko","Salsas","Huevos","Leche/Crema", "Tostadas","Salchicha",
                        "Cebolla","Pimenton","Zanahoria","Pollo","Arroz","Azucar","Salmon"]

#Imagen de Listas Almuerzos y Postres

p = "./almuerzo.jpg"
img3 = Image.open(p)
img3 = img3.resize((50,50), Image.ANTIALIAS)
img4 = ImageTk.PhotoImage(img3)
frameLabel = Label(frame2, image=img4)
frameLabel.place(relx=1, x=-2,y=2,anchor = NE)

#Listas Ingredientes - Cenas

IngredientesCena = ["Aceite","Cebolla","Ajo","Especias","Tomate","Huevos","Sal","Pimienta","Leche","Harina","Mostaza","Macarrones","Queso","Pan", "Pechuga","Atun","Pimenton","Pescado","Aji","Vinagre","Perejil","Habichuela", "Espinaca"]

#Listas Ingredentes - Postres 

IngredientesPostre = ["Leche condensada","Crema de leche","Gelatina","Galletas","Chocolate","Mantequilla","Queso","Aceite","Azucar",
                      "Canela","Nueces","Huevos","Banano","Zanahoria","Harina","Levadura","Vainilla","Maizena","Naranja","Limon"]

ventana.mainloop()
