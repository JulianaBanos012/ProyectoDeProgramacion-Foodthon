#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:49:21 2020

@author: jaide
"""

from tkinter import *

r1=(["Shakshuka","Aceite","Cebolla","Ajo","Especias","Tomate","Huevos","Sal","Pimienta"])
r2=(["Macarrones con parmesanno y pan ralado","Leche","Harina","Aceite","Mostaza","Macarrones","Sal","Pimienta","Queso Parmesano","Pan"])
r3=(["Brochetas de pollo","Pechuga","Pimenton","Cebolla","Aceite","Sal","Pimienta"])
r4=(["Tiras de pollo","Pechuga","Pan","Huevos","Semillas","Espinaca","Tomate","Queso","Aceite","Sal"])
r5=(["Ensalada especial","Habichuela","Huevos","Atun","Pimenton","Cebolla","Aceite","Sal","Pimienta"])
r6=(["Pescado especial","Pescado","Ajo","Aji","Vinagre","Perejil","Sal","Pimienta","Aceite"])
r7=(["Pescado especial","Pescado","Ajo","Aji","Vinagre","Perejil","Sal","Pimienta","Aceite"])

def Cena1(h, v):
    c = 0
    for z in r1:
        for x in h:
            if z == x:
                c += 1
    if c > round(len(r1)-1)/2:
        for i in r1:
            m = str(r1[0]) + "\n\n" 
            for i in range(1, len(r1)):
               m += str(r1[i]) + "\n"
            d = Label(v, text=m, bg= "#f1d924")
            d.configure(height= 12, width= 20)
            d.place(relx=0.02,rely=0.5)
            
def Cena2(h, v):
    c = 0
    for z in r2:
        for x in h:
            if z == x:
                c += 1
    if c >= round((len(r2)-1)/2):
        for i in r2:
            m = str(r2[0]) + "\n\n" 
            for i in range(1, len(r2)-1):
               m += str(r2[i]) + "\n"
            d = Label(v, text=m, bg= "#f1d924")
            d.configure(height= 12, width= 20)
            d.place(relx=0.02,rely=0.75)
            
def Cena3(h, v):
    c = 0
    for z in r3:
        for x in h:
            if z == x:
                c += 1
    if c >= round((len(r3)-1)/2):
        for i in r3:
            m = str(r3[0]) + "\n\n" 
            for i in range(1, len(r3)-1):
               m += str(r3[i]) + "\n"
            d = Label(v, text=m, bg= "#f1d924")
            d.configure(height= 12, width= 20)
            d.place(relx=0.14,rely=0.5)
            
def Cena4(h, v):
    c = 0
    for z in r4:
        for x in h:
            if z == x:
                c += 1
    if c >= round((len(r4)-1)/2):
        for i in r4:
            m = str(r4[0]) + "\n\n" 
            for i in range(1, len(r4)-1):
               m += str(r4[i]) + "\n"
            d = Label(v, text=m, bg= "#f1d924")
            d.configure(height= 12, width= 20)
            d.place(relx=0.14,rely=0.75)

def Cena5(h, v):
    c = 0
    for z in r5:
        for x in h:
            if z == x:
                c += 1
    if c >= round((len(r5)-1)/2):
        for i in r5:
            m = str(r5[0]) + "\n\n" 
            for i in range(1, len(r5)-1):
               m += str(r5[i]) + "\n"
            d = Label(v, text=m, bg= "#f1d924")
            d.configure(height= 12, width= 20)
            d.place(relx=0.26,rely=0.5)

def Cena6(h, v):
    c = 0
    for z in r6:
        for x in h:
            if z == x:
                c += 1
    if c >= round((len(r6)-1)/2):
        for i in r6:
            m = str(r6[0]) + "\n\n" 
            for i in range(1, len(r6)-1):
               m += str(r6[i]) + "\n"
            d = Label(v, text=m, bg= "#f1d924")
            d.configure(height= 12, width= 20)
            d.place(relx=0.26,rely=0.75)
            
def Cena7(h, v):
    c = 0
    for z in r7:
        for x in h:
            if z == x:
                c += 1
    if c >= round((len(r7)-1)/2):
        for i in r7:
            m = str(r7[0]) + "\n\n" 
            for i in range(1, len(r7)-1):
                m += str(r7[i]) + "\n"
            d = Label(v, text=m, bg= "#f1d924")
            d.configure(height= 12, width= 20)
            d.place(relx=0.38,rely=0.5)
            
def CenasRecetas(h, v):
    Cena1(h, v)
    Cena2(h, v)
    Cena3(h, v)
    Cena4(h, v)
    Cena5(h, v)
    Cena6(h, v)
    Cena7(h, v)
    
def Com():
    ventana = Tk()
    ventana.title("Cenas: Preparaciones")
    ventana.geometry('1200x1000')

    frame1 = Frame(ventana, bg='lightblue')
    frame1.configure(relief=GROOVE, bd=4)
    frame1.place(relheight=0.34,relwidth=0.5,relx=0,rely=0)
    
    frame2 = Frame(ventana, bg='lightgreen')
    frame2.configure(relief=GROOVE, bd=4)
    frame2.place(relheight=0.34,relwidth=0.5,relx=0,rely=0.33)
    
    frame3 = Frame(ventana, bg='#FFFF66')
    frame3.configure(relief=GROOVE, bd=4)
    frame3.place(relheight=0.34,relwidth=0.5,relx=0,rely=0.66)
    
    frame4 = Frame(ventana, bg='pink')
    frame4.configure(relief=GROOVE, bd=4)
    frame4.place(relheight=0.34,relwidth=0.5,relx=0.5,rely=0)
    
    frame5 = Frame(ventana, bg='#FFB266')
    frame5.configure(relief=GROOVE, bd=4)
    frame5.place(relheight=0.34,relwidth=0.5,relx=0.5,rely=0.33)
    
    frame6 = Frame(ventana, bg='#CC99FF')
    frame6.configure(relief=GROOVE, bd=4)
    frame6.place(relheight=0.34,relwidth=0.5,relx=0.5,rely=0.66)
    
    c1 = Label(frame1, bg='lightblue', text="----------Shakshuka---------- \n\n1) Para preparar la salsa de tomate, caliente el aceite en una sartén grande, añada\nla cebolla sofríala a fuego medio de 5 a 10 minutos,\nhasta que esté tierna y traslúcida. \n 2) Eche el ajo y sofríalo 1 minuto. \n 3) Añada los copos de guindilla, el tomate con abundante sal y pimienta, y cueza\na fuego lento 10 minutos, o hasta que la salsa se reduzca ligeramente y espese. \n 4) Haga dos huecos en la salsa de tomate, casque un huevo en cada uno y\nhágalos de 5 a 8 minutos, según como le gusten.\n", font= "Arial 9")
    c1.place(relx=0.04, rely=0.15)
    
    c2 = Label(frame2, bg='lightgreen', text="----------Macarrones con parmesanno y pan rallado---------- \n\n1) Para preparar la salsa, vierta la leche en un cazo y añada la harina,\nel aceite, la mostaza, la sal y la pimienta. \n 2) Remuévala a fuego medio de 8 a 10 minutos hasta que quede espesa y fina.\n3) Mientras, cueza la parta en una cazuela con agua hirviendo con sal unos 8 minutos,\no siga las instrucciones del envase, hasta que esté casi hecha. \n 4)Agregue la mitad del queso parmesano y las especias que desee\na la salsa, eche la pasta y remueva bien.\n 5) Mezcle el resto del parmesano con el pan rallado.\n6) Pase la pasta a una fuente refractaria, cúbrala con la mezcla de pan y\nhornéela de 25 a 30 minutos, hasta que se dore y burbujee.\n", font= "Arial 9")
    c2.place(relx=0.02, rely=0.15)
    
    c3 = Label(frame3, bg='#FFFF66', text="----------Brochetas de pollo---------- \n\n1) Trocea el pollo y salpimiéntalo. \n 2) Limpia y trocea las verduras a cubos pequeños. \n 3) Monta los ingredientes en la brocheta y\ncocínalos en el horno o a la plancha.\n", font= "Arial 9")
    c3.place(relx=0.2, rely=0.2)
    
    c4 = Label(frame4, bg="pink", text="----------Tiras de pollo---------- \n\n1) Corta las pechugas de pollo a tiras más bien gruesas. Bate un huevo. \n 2) Reboza las tiras primero en el huevo, luego en el pan rayado y\npor último añádeles semillas de sésamo. \n 3) Incorpóralas en una sartén a fuego medio hasta\nque el rebozado esté bien dorado. \n 4) Mientras, lava las espinacas y el tomate. Mezcla estos\ningredientes con el queso fresco y aliña.\n", font= "Arial 9")
    c4.place(relx=0.13, rely=0.15)
    
    c5 = Label(frame5, bg='#FFB266', text="----------Ensalada especial---------- \n\n1) Limpia y trocea las judías. Cuécelas durante\n10 minutos en agua hirviendo.  \n 2) Mientras, cuece también el huevo \n 3) Escurre las judías y déjalas enfriar. Mezcla\ntodos los ingredientes previamente cortados. \n 4) Aliña y salpimienta a tu gusto.\n", font= "Arial 9")
    c5.place(relx=0.24, rely=0.2)
    
    c6 = Label(frame6, bg='#CC99FF', text="----------Pescado especial---------- \n\n1) Plancha y dorar la lubina con la piel hacia arriba, unos 3 minutos. \n 2) Llevar al horno durante unos 8-10 minutos o hasta que esté en su punto.  \n 3) Mientras tanto laminar finos los dientes de ajo y\npicar o cortar en aros la guindilla.  \n 4 Calentar en un sartena aceite y ajo y despues agregar el pescado. \n 5) Cuando estén tostaditos, retirar y agregar el vinagre, meneando la sartén. \n 6) Echar también los posibles jugos que habrá soltado la lubina,\nque ya estará lista. Servir con el refrito y perejil picado.\n", font= "Arial 9")
    c6.place(relx=0.08, rely=0.15)
    
    ventana.mainloop()
     
