# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 17:17:14 2019

@author: Javier
"""

from tkinter import *

#Biblioteca para interfaz grafica
#Configuracion de la raiz
root = Tk()
root.title("Primera app de Vale")

#0 es false y 1 true
root.resizable(1,1)

root.iconbitmap("hola.ico")


#Siempre debe estar al final 
root.mainloop()