# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 17:17:14 2019

@author: Javier
"""

from tkinter import *

def sumar():
    r.set( float(n1.get()) + float(n2.get()))
    borrar()

def restar():
    r.set( float(n1.get()) - float(n2.get()))
    borrar()
    
def multiplicar():
    r.set( float(n1.get()) * float(n2.get()))
    borrar()
    
def dividir():
    r.set( float(n1.get()) / float(n2.get()))
    borrar()
    
def borrar():
    n1.set("")
    n2.set("")

#Biblioteca para interfaz grafica
#Configuracion de la raiz
root = Tk()

n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root,text="Numero1").pack()
Entry(root, justify="center", textvariable=n1).pack()
Label(root,text="Numero2").pack()
Entry(root, justify="center", textvariable=n2).pack()
Label(root,text="Resultado").pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack()
Label(root, text="").pack()
Button(root, text="sumar", command=sumar).pack()
Button(root, text="restar", command=restar).pack()
Button(root, text="multiplicar", command=multiplicar).pack()
Button(root, text="dividir", command=dividir).pack()



#Siempre debe estar al final 
root.mainloop()

