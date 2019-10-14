# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 17:17:14 2019

@author: Javier
"""

from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))

def reset():
    opcion.set(None)
    monitor.config(text="")




root = Tk()

opcion = IntVar()

Radiobutton(root,text="Opcion 1", variable=opcion, value=1, command=seleccionar).pack()
Radiobutton(root,text="Opcion 2", variable=opcion, value=2, command=seleccionar).pack()
Radiobutton(root,text="Opcion 3", variable=opcion, value=3, command=seleccionar).pack()

monitor = Label(root)
monitor.pack()

Button(root, text="Reiniciar", command=reset).pack()




#Siempre debe estar al final 
root.mainloop()

