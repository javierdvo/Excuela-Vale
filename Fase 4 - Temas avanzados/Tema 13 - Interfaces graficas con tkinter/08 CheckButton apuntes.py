# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 17:17:14 2019

@author: Javier
"""

from tkinter import *

def seleccionar():
    cadena = ""
    if (leche.get()):
        cadena += "Con leche"
    else:
        cadena += "Sin leche"
    
    if (azucar.get()):
        cadena += " y con azucar"
    
    else:
        cadena += " y sin azucar"
        
    monitor.config(text=cadena)




root = Tk()
root.title("Cafeteria")
root.config(bd=15)

leche = IntVar()
azucar = IntVar()

imagen = PhotoImage(file="imagen.gif")
Label(root,image=imagen).pack(side="left")

frame = Frame(root)
frame.pack(side="left")

Label(frame, text = "Como quieres el cafe?").pack(anchor="w")
Checkbutton(frame, text="Con leche", variable=leche, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")
Checkbutton(frame, text="Con azucar", variable=azucar, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")

monitor = Label(frame)
monitor.pack()


#Siempre debe estar al final 
root.mainloop()

