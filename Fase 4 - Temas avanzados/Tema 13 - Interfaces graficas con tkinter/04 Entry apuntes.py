# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 17:17:14 2019

@author: Javier
"""

from tkinter import *

#Biblioteca para interfaz grafica
#Configuracion de la raiz
root = Tk()

label = Label(root, text="Escribe tu nombre completo")
label.grid(row=0, column=0, sticky="w", padx=20, pady=100)

entry = Entry(root)
entry.grid(row=0, column=1, padx=20, pady=100)

label2 = Label(root, text="Password")
label2.grid(row=1, column=0, padx=20, pady=100)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=20, pady=100)
entry2.config(justify="center", show="*")



#Siempre debe estar al final 
root.mainloop()

