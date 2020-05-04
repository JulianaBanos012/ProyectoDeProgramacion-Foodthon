#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:49:22 2020

@author: jaide
"""

from tkinter import *
import webbrowser

r1=(["Tres leches","Leche condensada","Crema de leche","Leche","Gelatina","Galletas"])
r2=(["Cheesecacke","Chocolate","Galletas","Mantequilla","Queso crema","Azucar","Crema de leche","Gelatina"])
r3=(["Pastel de zanahoria","Harina","Zanahoria","Levadura","Huevos","Bananos","Aceite","Azucar","Canela","Nueces"])
r4=(["Flan de caramelo","Leche condensada","Leche","Huevos","Vainilla","Azucar"])
r5=(["Leche frita","Leche","Maizena","Naranja","Limon","Huevos","Azucar","Vainilla","Mantequilla","Harina","Aceite"])
r6=(["Mugcake","Harina","Azucar","Chocolate","Levadura","Huevos","Leche","Aceite"])
r7=(["Crepes de banano","Banano","Huevos","Aceite","Azucar"])

def Postre1(h, v):
    c = 0
    for z in r1:
        for x in h:
            if z == x:
                c += 1
    if c > round((len(r1)-1)/2):
        for i in r1:
            m = str(r1[0]) + "\n\n" 
            for i in range(1, len(r1)):
               m += str(r1[i]) + "\n"
            d = Label(v, text=m, bg= "pink")
            d.configure(height= 12, width= 20)
            d.place(relx=0.02,rely=0.5)
            
def Postre2(h, v):
    c = 0
    for z in r2:
        for x in h:
            if z == x:
                c += 1
    if c > round((len(r2)-1)/2):
        for i in r2:
            m = str(r2[0]) + "\n\n" 
            for i in range(1, len(r2)-1):
               m += str(r2[i]) + "\n"
            d = Label(v, text=m + "\n\n", bg= "pink")
            d.configure(height= 12, width= 20)
            d.place(relx=0.02,rely=0.75)
            
def Postre3(h, v):
    c = 0
    for z in r3:
        for x in h:
            if z == x:
                c += 1
    if c > round((len(r3)-1)/2):
        for i in r3:
            m = str(r3[0]) + "\n\n" 
            for i in range(1, len(r3)-1):
               m += str(r3[i]) + "\n"
            d = Label(v, text=m, bg= "pink")
            d.configure(height= 12, width= 20)
            d.place(relx=0.14,rely=0.5)
            
def Postre4(h, v):
    c = 0
    for z in r4:
        for x in h:
            if z == x:
                c += 1
    if c > round((len(r4)-1)/2):
        for i in r4:
            m = str(r4[0]) + "\n\n" 
            for i in range(1, len(r4)-1):
               m += str(r4[i]) + "\n"
            d = Label(v, text=m, bg= "pink")
            d.configure(height= 12, width= 20)
            d.place(relx=0.14,rely=0.75)

def Postre5(h, v):
    c = 0
    for z in r5:
        for x in h:
            if z == x:
                c += 1
    if c > round((len(r5)-1)/2):
        for i in r5:
            m = str(r5[0]) + "\n\n" 
            for i in range(1, len(r5)-1):
               m += str(r5[i]) + "\n"
            d = Label(v, text=m, bg= "pink")
            d.configure(height= 12, width= 20)
            d.place(relx=0.26,rely=0.5)

def Postre6(h, v):
    c = 0
    for z in r6:
        for x in h:
            if z == x:
                c += 1
    if c > round((len(r6)-1)/2):
        for i in r6:
            m = str(r6[0]) + "\n\n" 
            for i in range(1, len(r6)-1):
               m += str(r6[i]) + "\n"
            d = Label(v, text=m, bg= "pink")
            d.configure(height= 12, width= 20)
            d.place(relx=0.26,rely=0.75)
            
def Postre7(h, v):
    c = 0
    for z in r7:
        for x in h:
            if z == x:
                c += 1
    if c > round((len(r7)-1)/2):
        for i in r7:
            m = str(r7[0]) + "\n\n" 
            for i in range(1, len(r7)-1):
               m += str(r7[i]) + "\n"
            d = Label(v, text=m, bg= "pink")
            d.configure(height= 12, width= 20)
            d.place(relx=0.38,rely=0.5)
            
def PostresRecetas(h, v):
    Postre1(h, v)
    Postre2(h, v)
    Postre3(h, v)
    Postre4(h, v)
    Postre5(h, v)
    Postre6(h, v)
    Postre7(h, v)
    
def link_clicked():
    webbrowser.open("https://www.cocinacaserayfacil.net/leche-frita-receta/")
    
def Pos():
    ventana = Tk()
    ventana.title("Postres: Preparaciones")
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

    p1 = Label(frame1, bg='lightblue', text="----------Tres Leches---------- \n\n1) En una olla, disolver la gelatina sin sabor en una taza de agua fría\ny poner a hervir.\n2) Luego, en la licuadora, mezclar la gelatina, la crema de leche,\nla leche condensada y la leche.\n 3) Aparte, en el molde, preferiblemente una refractaria de vidrio, o\nen los moldes individuales, hacer una base en el fondo con las galletas,\nhumedeciéndolas previamente en leche. \n 4) Cuando la base esté lista, agregar el contenido de la licuadora\ny refrigerar de 8 horas a un día.\n", font= "Arial 9")
    p1.place(relx=0.1, rely=0.15)
    
    p2 = Label(frame2, bg='lightgreen', text="----------Cheesecake---------- \n\n1) Para hacer la base, triturar las galletas y añadir la mantequilla derretida\nymezclar. Cubrir el fondo del molde con esta mezcla y refrigerar.\n2) En una olla, agregar una taza de agua y la gelatina sin sabor y\ndejar hervir. Agregar la nata de leche o crema para batir. \n 3) Cuando empiece a hervir, añadir el chocolate en trocitos y\nrevolver hasta que se derrita. \n 4) Aparte, en un bowl, batir el queso crema con el azúcar hasta que esté cremoso y\nagregar la mezcla de chocolate y continuar batiendo hasta homogeneizar completamente.\n5) Agregar esta mezcla al molde con la base de galleta y\ncubrir con papel film. Llevar al refrigerador de 4 horas a un día.\n", font= "Arial 9")
    p2.place(relx=0.02, rely=0.15)
    
    p3 = Label(frame3, bg='#FFFF66', text="----------Pastel de zanahoria---------- \n\n1) En un recipiente, mezclar bien las nueces con el aceite de oliva, el azúcar o\nendulzante, la zanahoria rallada, los bananos triturado, el polvo para hornear,\nla harina y la canela. \n 2) Separar las claras de las yemas, agregar las yemas a la mezcla y revolver. \n 3) Aparte, batir las claras hasta antes de llegar a punto de nieve y\nagregar a la mezcla anterior y mezclar bien.\n4) Verter la mezcla en un molde engrasado y enharinado y llevar al horno precalentado a\n180° por 30 minutos o hasta que, al introducir un cuchillo, éste salga limpio. \n 5) Dejar enfriar y servir. Si se desea, se puede cubrir por encima con chocolate blanco.\n", font= "Arial 9")
    p3.place(relx=0.01, rely=0.15)
    
    p4 = Label(frame4, bg="pink", text="----------Flan de caramelo---------- \n\n1) Batir la leche condensada, la leche entera, los huevos, la vainilla y\nlas dos cucharadas de azúcar hasta que todo quede perfectamente integrado. \n 2) Aparte, para preparar el caramelo, agregar las 5 cucharadas de azúcar y\nla cucharada y media de agua en una sartén y poner a fuego medio,\nmover el sartén para ir mezclando y poner cuidado de no dejar quemar.\n3) Adicionar el caramelo al molde, esparcir en el fondo,\ne incorporar la mezcla elaborada previamente.\n4) Una vez todo dispuesto en el molde, ponerlo en una bandeja para horno\nque tenga profundidad y llenar de agua hasta la mitad para cocinar al baño maría. \n 5) Llevar al horno precalentado a 170 °C por 40 minutos,\nrevisando constantemente para que no se queme. \n 6) Retirar del horno, dejar enfriar y llevar a la nevera,\npor lo menos, por una hora y servir.\n", font= "Arial 9")
    p4.place(relx=0.07, rely=0.05)
    
    p5 = Label(frame5, bg='#FFB266', text="----------Mugcake---------- \n\n1) En un pocillo agregar harina, azucar, cacao en olvo y levadura y lo revolvemos.\n2) Batimos el huevo hasta que presenta burbujas, así\nel resultado es más esponjoso. Mezclamos con los ingredientes\n en polvo que tenemos en el bol. \n 3) A continuación añadimos la leche y el aceite. Unimos todo con el tenedor. \n 4) Despues la colocamos en el microondas (aprox 3 minutos)\n 5) La sacamos y le agregamos azucar glass para decorar.\n", font= "Arial 9")
    p5.place(relx=0.05, rely=0.15)
    
    p6 = Label(frame6, bg='#CC99FF', text="----------Crepes de banano---------- \n\n1) Machacar un banano hasta que quede una pasta. Agregarle 2 huevos y batir. \n 2) Pon un sarten a calentar con aceite y cuando este caliente\nvierte una cucharada de la masa. \n 3) Dale vuelta cuando e lado de abajo este listo. \n 4) Retirar de el sarten y agregale por encima lo que quieras.\n", font= "Arial 9")
    p6.place(relx=0.05, rely=0.1)
    
    p7 = Label(frame6, text="----------Leche Frita---------- \n\n Para conocer la preparación de esta receta presiona el botón.", font= 'Arial 9')
    p7.place(relx=0.15, rely=0.55)
    
    a = Button(frame6, text='Leche Frita', font="Arial 9", command=link_clicked)
    a.place(relx=0.4, rely=0.75)
    ventana.mainloop()
    
