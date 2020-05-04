#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:21:56 2020

@author: JuanPablo12
"""

from tkinter import *

r1=(["Omelette de huevo\ncon jamon", "Huevos","Queso","Jamon","Leche","Harina","Aceite","Sal","Pimienta"])
r2=(["Pan de manzana", "Manzanas","Harina","Azucar","Huevos","Levadura","Aceite","Miel","Canela","Sal"])
r3=(["Muffins de avena,\nbanano y manzanas","Avena","Banano","Huevos","Bicarbonato","Aceite","Manzanas","Canela"])
r4=(["Pancakes de avena,\nmiel y fresas","Sal","Huevo","Avena","Canela","Aceite","Leche","Azucar","Fresas","Miel"])
r5=(["Sabanero","Platanos","Aceite","Cebolla Morada","Limon","Sal","Pimienta","Hogao","Ajo","Queso"])
r6=(["Tostadas francesas","Pan","Huevos","Chocolate","Azucar","Canela","Mantequilla","Crema de leche","Durazno"])
r7=(["Tuna sandwich","Pan tajado","Lechuga","Atun","Mayonesa","Pimienta","Sal","Queso","Queso"])

def Desayuno1(h, v):
    c = 0
    for z in r1:
        for x in h:
            if z == x:
                c += 1
    if c > round(len(r1)-1)/2:
        for i in r1:
            m1 = str(r1[0]) + "\n\n" 
            for i in range(1, len(r1)):
               m1 += str(r1[i]) + "\n"
            d1 = Label(v, text=m1, bg= "#f1d924")
            d1.configure(height= 12, width= 20)
            d1.place(relx=0.02,rely=0.5)
            
def Desayuno2(h, v):
    c = 0
    for z in r2:
        for x in h:
            if z == x:
                c += 1
    if c >= round((len(r2)-1)/2):
        for i in r2:
            m2 = str(r2[0]) + "\n\n" 
            for i in range(1, len(r2)-1):
               m2 += str(r2[i]) + "\n"
            d2 = Label(v, text=m2, bg= "#f1d924")
            d2.configure(height= 12, width= 20)
            d2.place(relx=0.02,rely=0.75)
            
def Desayuno3(h, v):
    c = 0
    for z in r3:
        for x in h:
            if z == x:
                c += 1
    if c >= round((len(r3)-1)/2):
        for i in r3:
            m3 = str(r3[0]) + "\n\n" 
            for i in range(1, len(r3)-1):
               m3 += str(r3[i]) + "\n"
            d3 = Label(v, text=m3, bg= "#f1d924")
            d3.configure(height= 12, width= 20)
            d3.place(relx=0.14,rely=0.5)
            
def Desayuno4(h, v):
    c = 0
    for z in r4:
        for x in h:
            if z == x:
                c += 1
    if c >= round((len(r4)-1)/2):
        for i in r4:
            m4 = str(r4[0]) + "\n\n" 
            for i in range(1, len(r4)-1):
               m4 += str(r4[i]) + "\n"
            d4 = Label(v, text=m4, bg= "#f1d924")
            d4.configure(height= 12, width= 20)
            d4.place(relx=0.14,rely=0.75)
            

def Desayuno5(h, v):
    c = 0
    for z in r5:
        for x in h:
            if z == x:
                c += 1
    if c >= round((len(r5)-1)/2):
        for i in r5:
            m5 = str(r5[0]) + "\n\n" 
            for i in range(1, len(r5)-1):
               m5 += str(r5[i]) + "\n"
            d5 = Label(v, text=m5, bg= "#f1d924")
            d5.configure(height= 12, width= 20)
            d5.place(relx=0.26,rely=0.5)
            
def Desayuno6(h, v):
    c = 0
    global d6
    for z in r6:
        for x in h:
            if z == x:
                c += 1
    if c >= round((len(r6)-1)/2):
        for i in r6:
            m6 = str(r6[0]) + "\n\n" 
            for i in range(1, len(r6)-1):
               m6 += str(r6[i]) + "\n"
            d6 = Label(v, text=m6 , bg= "#f1d924")
            d6.configure(height= 12, width= 20)
            d6.place(relx=0.26,rely=0.75)
                   
def Desayuno7(h, v):
    c = 0
    for z in r7:
        for x in h:
            if z == x:
                c += 1
    if c >= round((len(r7)-1)/2):
        for i in r7:
            m7 = str(r7[0]) + "\n\n" 
            for i in range(1, len(r7)-1):
               m7 += str(r7[i]) + "\n"
            d7 = Label(v, text=m7, bg= "#f1d924")
            d7.configure(height= 12, width= 20)
            d7.place(relx=0.38,rely=0.5)
            
def DesayunosRecetas(h, v):
    Desayuno1(h, v)
    Desayuno2(h, v)
    Desayuno3(h, v)
    Desayuno4(h, v)
    Desayuno5(h, v)
    Desayuno6(h, v)
    Desayuno7(h, v)
    
def About():
    ventana = Tk()
    ventana.title("FoodThon information")
    d = Label(ventana, text="There isn't any information available :(", font= "Arial")
    d.pack()
    ventana.mainloop()
    
def Exit():
    ventana = Tk()
    ventana.title("FoodThon information")
    d = Label(ventana, text="Sorry, the exit is not this way :(", font= "Arial")
    d.pack()
    ventana.mainloop()
    
def Des():
    ventana = Tk()
    ventana.title("Desayunos: Preparaciones")
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
    
    d1 = Label(frame1, bg='lightblue', text="----------Omelette de huevo con jamon---------- \n\n1) Batir en un bol los huevos hasta que la clara y la yema se mezclen. \n 2) Agregar la harina, la leche y la sal y pimienta al gusto. \n 3) En una sartén antiadherente, poner aceite de oliva a fuego medio y, \n cuando esté caliente, agregar la mezcla hasta cubrir el fondo del sartén, \n logrando un grosor de medio centímetro aproximadamente. \n 4) Agregar el queso y el jamón y doblar la tortilla. Voltear, dejar cocinar y servir.\n", font= "Arial 10")
    d1.place(relx=0.02, rely=0.15)
    
    d2 = Label(frame2, bg='lightgreen', text="----------Pan de manzana---------- \n\n1) Precaliente el horno a 180°C y engrasa el molde que vas a usar para hornear el pan. \n2) En la licuadora agrega las manzanas peladas, cortadas en cubos y\n sin semillas, agrega los huevos, el aceite, el azúcar morena y 3 cucharadas de miel.\nLicua y pasa la mezcla a un bowl. \n3) A esta mezcla agrega de a poco la harina, una cucharadita de polvo para hornear y\n3 cucharadas de canela en polvo, mezcla bien hasta que no queden grumos,\nsi puedes usar la batidora mejor pero no es necesario. \n4) Cuando esté lista la masa, incorpórala en el molde y hornea por 30 minutos o\nhasta que dore la corteza, con un palillo comprueba que\nel interior esté completamente cocinado. Deja enfriar, desmolda y sirve.\n", font= "Arial 9")
    d2.place(relx=0.01, rely=0.15)
    
    d3 = Label(frame3, bg='#FFFF66', text="----------Muffins de avena. banano y manzanas---------- \n\n 1)En un bowl, amasar los ingredientes, excepto las manzanas, hasta que estén integrados.\n2) Picar la manzana en trozos, agregar a la mezcla y revolver.\n3) Poner la masa en un molde de muffins y hornear a 180°\nhasta que al pinchar con un cuchillo éste salga limpio (25 a 30 minutos aproximadamente). \n 4) Se pueden servir fríos o calientes.\n", font= "Arial 9")
    d3.place(relx=0, rely=0.05)
    
    d4 = Label(frame4, bg="pink", text="----------Pancakes de avena, miel y fresas---------- \n\n1) Batir las claras sin las yemas a punto de nieve.\n 2) Luego, agregar el aceite de coco y la leche y seguir batiendo\nhasta incorporar completamente.\n3) Añadir la avena, la canela, el azúcar y la sal y mezclar.\n 4) Poner una sartén con antiadherente a fuego medio y,\ncuando esté caliente, esparcir la masa formando\nel panqueque y cocinar por ambos lados.\n 5) Repetir la cocción con el resto de la mezcla.\n 6) Servirlos con las fresas picadas y la miel.\n 7) Si se desea, se pueden variar las frutas y el acompañante.\n", font= "Arial 9")
    d4.place(relx=0.15, rely=0.15)
    
    d5 = Label(frame5, bg='#FFB266', text="----------Sabanero---------- \n\n1) Retiramos las punta de los plátanos, hacemos un corte\nsuperficial a lo largo y vamos pelando. Cortamos en 4 y llevamos a una olla\ncon abundante agua hirviendo. Cocinamos por 15 minutos hasta que estén blandos.\n2) Mientras tanto en una sartén adicionamos el aceite de oliva y\nsofreímos la cebolla morada con los ajos. Cuando los plátanos estén\nlistos los hacemos puré, adicionamos sal y pimienta y\n los agregamos a la olla del sofrito. Apagamos el fuego revolvemos.\n3) Adicionamos el zumo de limón hasta que se integre completamente\ncon el puré de plátano. \n 4) Para servirlo ponemos el puré en el plato, seguido del hogao y\nespolvoreamos con queso, servimos con chocolate o café colombiano.\n", font= "Arial 9")
    d5.place(relx=0.05, rely=0.1)
    
    d6 = Label(frame6, bg='#CC99FF', text="----------Tostadas francesas---------- \n\n1) Para darles este giro interesante a las tostadas francesas, lo primero\nque debemos hacer es: en un bowl mezclamos: huevos, chocolate,\nazúcar y canela. Revolvemos para integrar todos los ingredientes. \n 2) Preparamos una sartén con un poco de Mantequilla, cuando esté caliente\ntomamos uno de los panes y lo sumergimos en la mezcla de Alpin por poco tiempo. \n Sacamos y llevamos inmediatamente a la sartén, dejamos dorar por un lado y\nvolteamos para que se dore del otro.\n3) Sacamos de la sartén y servimos con un poco de crema montada o\ncrema chantilly acompañada de tus frutas favoritas.\n", font= "Arial 9")
    d6.place(relx=0.05, rely=0.15)
    
    d7 = Label(frame3, text="----------Tuna sandwich---------- \n\n1) Empezamos abriendo una lata de atún y la mezclamos con Crema de leche,\nun poquito de pimienta y bastante Queso. \n 2) cuando esté bien mezclado, untamos Mantequilla en los panes que doramos en\nla sartén, agregamos la mezcla de atún, un poco de lechuga y Queso, y listo.\n", font= "Arial 9")
    d7.place(relx=0.05, rely=0.53)

    ventana.mainloop()
        
