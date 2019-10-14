# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 17:17:14 2019

@author: Javier
"""

from tkinter import *

#Biblioteca para interfaz grafica
#Configuracion de la raiz
root = Tk()

texto = Text(root)
texto.pack()
texto.config(width=30, height=10, font=("Arial",12), padx=15, pady=15, selectbackground="red")


#Siempre debe estar al final 
root.mainloop()

