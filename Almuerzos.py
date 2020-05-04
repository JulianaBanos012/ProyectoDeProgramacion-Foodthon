#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:49:05 2020

@author: JuanPablo12
"""

from tkinter import *

r1=(["Pastel de papa","Papas","Champiñones","Mantequilla","Queso","Especias","Caldo","Sal y Pimienta"])
r2=(["Pasta palta","Pasta","Palta","Ajo","Especias","Limon","Aceite","Sal y Pimienta","Choclo","Tomates"])
r3=(["Pan de carne","Carne","Panko","Perejil","Ajo","Cebolla","Salsas","Sal y Pimienta"])
r4=(["Ensalada de huevo","Huevos","Leche/Crema","Salsas","Aceite","Limon","Perejil","Tostadas"])
r5=(["Pasta con salchicha\nparrillera","Pasta","Salchica","Cebolla","Pimenton","Zanahoria","Ajo","Tomate","Leche/Crema","Sal","Pimienta"])
r6=(["Pollo con arroz\nal limon","Pollo","Limon","Arroz","Especias","Cebolla","Ajo","Caldo","Sal y Pimienta"])
r7=(["Arroz al coco\ncon salmon","Aceite","Cebolla","Ajo","Arroz","Leche/Crema","Azucar","Salmon","Sal y Pimienta"])

def Almuerzo1(h, v):
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
            d = Label(v, text=m, bg= "pink")
            d.configure(height= 13, width= 20)
            d.place(relx=0.02,rely=0.5)
            
def Almuerzo2(h, v):
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
            d = Label(v, text=m, bg= "pink")
            d.configure(height= 13, width= 20)
            d.place(relx=0.02,rely=0.75)
            
def Almuerzo3(h, v):
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
            d = Label(v, text=m, bg= "pink")
            d.configure(height= 13, width= 20)
            d.place(relx=0.14,rely=0.5)
            
def Almuerzo4(h, v):
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
            d = Label(v, text=m, bg= "pink")
            d.configure(height= 13, width= 20)
            d.place(relx=0.14,rely=0.75)

def Almuerzo5(h, v):
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
            d = Label(v, text=m, bg= "pink")
            d.configure(height= 13, width= 20)
            d.place(relx=0.26,rely=0.5)

def Almuerzo6(h, v):
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
            d = Label(v, text=m, bg= "pink")
            d.configure(height= 13, width= 20)
            d.place(relx=0.26,rely=0.75)
            
            
def Almuerzo7(h, v):
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
            d = Label(v, text=m, bg= "pink")
            d.configure(height= 13, width= 20)
            d.place(relx=0.38,rely=0.5)
            
def AlmuerzosRecetas(h, v):
    Almuerzo1(h, v)
    Almuerzo2(h, v)
    Almuerzo3(h, v)
    Almuerzo4(h, v)
    Almuerzo5(h, v)
    Almuerzo6(h, v)
    Almuerzo7(h, v)
    
def Alm():
    ventana = Tk()
    ventana.title("Almuerzos: Preparaciones")
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
    
    a1 = Label(frame1, bg='lightblue', text="----------Pastel de papa---------- \n\n1) Calentar el horno a 180ª y engrasar un refractario para horno con\nla cucharada de mantequilla. \n 2) Cortar las papas y los hongos en laminas bien finas. \n 3) En el refractario engrasado hacer capas de papa, hongos, gruyere,\ncondimentando entre capa y capa. \n 4) Al final agregar el caldo de vegetales, tapar con aluminio y hornear por 1h. \n 5) Destapar, cubrir con el queso y gratinar con el parmesano hasta que dore.\n", font= "Arial 9")
    a1.place(relx=0.02, rely=0.15)
    
    a2 = Label(frame4, text="----------Pasta palta---------- \n\n1)Hervir la pasta. Reservar con un poquito de aceite \n 2) Procesar la palta con el diente de ajo, la albahaca, el aceite, el limón\nexprimido, la sal y pimienta. \n 3) Mezclar con la pasta \n 4) Servir con granos de choclo, tomatitos cortados y unas hojas de albahaca enteras.\n", font= "Arial 9")
    a2.place(relx=0.04, rely=0.45)
    
    a3 = Label(frame3, bg='#FFFF66', text="----------Pan de carne---------- \n\n1) Precalentar el horno a 200°. \n 2) En un bowl mezclar la carne molida con la taza de pan rallado,\n1 cda. de salsa worcestershire, 6 cucharadas de barbacoa y condimentar. \n 3) Unir bien formando un rollo largo y medianamente ancho, disponerlo\nsobre una placa para horno aceitada. \n 4) En un bowl más pequeño mezclar 2 cdas. de barbacoa, 1 cda. de salsa\nworcestershire y la miel. \n 5)Cocinar en el horno por unos 50m.\n", font= "Arial 9")
    a3.place(relx=0.05, rely=0.15)
    
    a4 = Label(frame4, bg="pink", text="----------Ensalada de huevo---------- \n\n1)Colocar las yemas cocidas en un bowl junto con la leche hasta formar una pasta. \n 2) Agregar la mostaza, el aceite vegetal y el jugo de limón. \n 3) Mezclar junto a 4 huevos cocidos cortados en cubos. \n 4) Agregar perejil picado y servir en un recipiente junto a tostadas de pan.\n", font= "Arial 9")
    a4.place(relx=0.05, rely=0.05)
    
    a5 = Label(frame2, bg='lightgreen', text="----------Pasta con salchica parrillerra---------- \n\n1) Cocinar la pasta al dente, cortar su cocción y reservar en un bowl\ncon oliva para que no se pegue. \n 2) En olla mediana con un poco de oliva rehogar la cebolla, la zanahoria,\nel pimiento y los ajos picados. Incorporar la salchicha\nparrillera cortada en pedazos chicos. Dorar bien. \n 3) Agregar la salsa de tomate y mover integrando todo \n 4) Condimentar bien con sal, pimienta agregar la pasta cocida mezclando\ntodos los ingredientes.\n5) Espolvorear con ciboulette picada.\n", font= "Arial 9")
    a5.place(relx=0.05, rely=0.15)
    
    a6 = Label(frame6, bg='#CC99FF', text="----------Pollo con arroz al limón---------- \n\n1) En una ziploc mezclar el pollo con la ralladura de los limones, el jugo,\nlos dientes de ajo aplastados, el orégano seco y llevar a marinar en la nevera por 1h.\n2) Retirar de la bolsa y llevar a dorar en sartén bien caliente con oliva por\nambos lados. Retirar y limpiar el exceso de grasa de la sartén\ny volver a incorporar un poco de oliva.\n3) Rehogar la cebolla, incorporar el arroz hasta dorarlo, agregar la marinada\ndel pollo y mover por 30 segundos. \n 4) Incorporar el caldo, un poco de mas de agua, las presas de pollo y\ntapar con papel aluminio. Cocinar durante 30/35 minutos a fuego bajo.\n5) Retirar el papel aluminio, chequear que haya no quede nada de líquido y\napagar el fuego dejándolo reposar por 5m. \n 6) Espolvorear con perejil picado y un poco mas de ralladura de limón.\n", font= "Arial 9")
    a6.place(relx=0.02, rely=0.1)
    
    a7 = Label(frame5, bg='#FFB266', text="----------Arroz al coco con salmón---------- \n\n1) Caliente el aceite en una olla, añada la cebolla y sofríala a fuego medio\n10 minutos, o hasta que se ablande. \n 2) Agregue el ago y sofríalo 1 o 2 minutos, hasta que desprenda su aroma. \n 3) Eche el arroz y remueva para que se impregne del aceite.\n4) Vierta la leche de coco, llene la mitad de la lata vacía con agua\ny añádala a la olla. \n 5) Eche una pizca genersoa de sal y el azúcar, lleve a la ebullición y baje el fuego. \n 6) Cueza el arroz a fuego lento durante 10 minutos, o hasta que esté tierno y\nel líquido se haya absorbido por completo.\n", font= "Arial 9")
    a7.place(relx=0.02, rely=0.15)

    ventana.mainloop()
    
