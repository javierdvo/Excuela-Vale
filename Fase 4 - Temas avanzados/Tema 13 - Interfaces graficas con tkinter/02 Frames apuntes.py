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
#cambiar icono de la app
root.iconbitmap("hola.ico")


#frames son contendedores done vamos poniendo cosas. Se necesita una raiz
frame = Frame(root, width=480, height=320)
frame.pack()
frame.config(bg="lightblue")
frame.config(cursor="pirate")
frame.config(bd=25)
frame.config(relief="sunken")

root.config(cursor="arrow")
root.config(bg="purple")
root.config(bd=15)
root.config(relief="ridge")





#Siempre debe estar al final 
root.mainloop()

