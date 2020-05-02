from tkinter import *


# r1=(["Americano"],["Desayuno"],[30],[800],["Huevos","Aceite","Tostadas","Harina para pancakes"])
# r2=(["Pasta al pesto"],["Almuerzo"],[60],[400],["Spaguetti","Pesto","Parmesano","Sal","Ajo"])
# r3=(["Bandeja paisa"],["Almuerzo"],[70],[1900],["Frijol","Aceite","Carne","Huevos","Chorizo","Aguacates","Arroz","Platano","Tomate","Cebolla","Sal","Chicharron"])
# r4=(["Sandwich de jamon y queso"],["Comida"],[5],[290],["Pan Tajado","Queso tajado","Jamon tajado","Mantequilla"])
# r5=(["MugCake"],["Postre"],[10],[310],["Harina","Aceite","Azucar","Cacao en polvo","Huevos","Leche"])
# r6=(["Cereal"],["Desayuno"],[5],[200],["Cereal","Leche"])
# Recetas=[r1,r2,r3,r4,r5,r6]

# Cliente=(["Desayuno"],[60],[1000],["Huevos","Leche","Tostadas","Aceite"])
# c1=[Cliente]

# RecetaFinal=[]

# def descIng():
#     h=0
#     CA = 0
#     for (Nombre,platos,tiempo,calorias,ingredientes) in Recetas:
#         for s in ingredientes:
#             for (plato,tiempo,calorias,ingredientes1) in c1:
#                 for l in ingredientes1:
#                     if s==l:
#                         CA += 1 
#                 if CA > 8:
#                     RecetaFinal.append(Recetas[h])
                        
#         h+=1            
                        

# descIng()
# print(RecetaFinal)
# print(len(Recetas))

r1=["Americano", "Huevos","Aceite","Tostadas","Harina para pancakes"]
r2=["Pasta al pesto","Spaguetti","Pesto","Parmesano","Sal","Ajo"]
r3=["Bandeja paisa","Frijol","Aceite","Carne","Huevos","Chorizo","Aguacates","Arroz","Platano","Tomate","Cebolla","Sal","Chicharron"]
r4=["Sandwich de jamon y queso","Pan Tajado","Queso tajado","Jamon tajado","Mantequilla"]
r5=["MugCake", "Harina","Aceite","Azucar","Cacao en polvo","Huevos","Leche"]
r6=["Cereal Clásico","Cereal","Leche","Huevos"]

Recetas=[r1,r2,r3,r4,r5,r6]
Cliente=["Huevos","Leche","Tostadas","Aceite", "Mantequilla","Queso tajado", "Pan Tajado"]


def Desayunos1(h, v):
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
            # return(m + "\n\n")
            d = Label(v, text=m + "\n\n", bg= "#f1d924")
            d.place(relx=0.03,rely=0.5)
            
def Desayunos2(h, v):
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
            # return(m + "\n\n")
            d = Label(v, text=m + "\n\n", bg= "#f1d924")
            d.place(relx=0.03,rely=0.7)
            
def Desayunos3(h, v):
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
            # return(m + "\n\n")
            d = Label(v, text=m + "\n\n", bg= "lightblue")
            d.place(relx=0.19,rely=0.5)
            
def Desayunos4(h, v):
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
            # return(m + "\n\n")
            d = Label(v, text=m + "\n\n", bg= "#f1d924")
            d.place(relx=0.19,rely=0.7)

def Desayunos5(h, v):
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
            # return(m + "\n\n")
            d = Label(v, text=m + "\n\n", bg= "#f1d924")
            d.place(relx=0.35,rely=0.5)

def Desayunos6(h, v):
    c = 0
    for z in r6:
        for x in h:
            if z == x:
                c += 1
    if c >= round((len(r6)-1)/2):
        for i in r5:
            m = str(r6[0]) + "\n\n" 
            for i in range(1, len(r5)-1):
               m += str(r6[i]) + "\n"
            # return(m + "\n\n")
            d = Label(v, text=m + "\n\n", bg= "#f1d924")
            d.place(relx=0.35,rely=0.7)
            
def Desayunos10(h, v):
    Desayunos1(h, v)
    Desayunos2(h, v)
    Desayunos3(h, v)
    Desayunos4(h, v)
    Desayunos5(h, v)
    Desayunos6(h, v)
