#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 17:02:19 2020

@author: juliana
"""

from tkinter import *

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

Row = 0
ventana = Tk()
ventana.configure(bg="lightgreen")
ventana.title("Bienvenido a FoodThon")
Label1= Label(text='¿Qué tipo de receta deseas hacer?', fg='darkgreen', font='Verdana 10 bold')
Label1.grid(row=Row, column=2)

IngredientesDesayuno = ['Huevos', 'Pan', 'Leche', 'Tocineta', 'Champiñones']

def Desayunos():
    lng = Checkbar(ventana, IngredientesDesayuno)
    lng.grid(row=2, column=0)
    lng.config(relief=GROOVE, bd=2)
    def allstates(): 
        print(list(lng.state()))
    Button(ventana, text='Quit', command=ventana.quit).grid(row=3, column=0)
    Button(ventana, text='PeekDesayunos', command=allstates).grid(row=3, column=1)

IngredientesAlmuerzo = ['Arroz', 'Fríjoles', 'Maíz', 'Pechuga', 'Carne', 'Lentejas', 'maíz', 'quinoa']

def Almuerzos():
    lng = Checkbar(ventana, IngredientesAlmuerzo)
    lng.grid(row=2, column=2)
    lng.config(relief=GROOVE, bd=2)
    def allstates(): 
        print(list(lng.state()))
    Button(ventana, text='Quit', command=ventana.quit).grid(row=3, column=2)
    Button(ventana, text='PeekAlmuerzos', command=allstates).grid(row=3, column=3)

BotonDesayunos = Button(ventana, text="Desayunos", command=Desayunos)
BotonDesayunos.grid(row=1, column=0)

BotonAlmuerzos = Button(ventana, text="Almuerzos", command=Almuerzos)
BotonAlmuerzos.grid(row=1, column=2)

ventana.mainloop()
