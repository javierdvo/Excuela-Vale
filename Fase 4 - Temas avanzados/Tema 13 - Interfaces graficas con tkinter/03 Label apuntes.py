# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 17:17:14 2019

@author: Javier
"""

from tkinter import *

#Biblioteca para interfaz grafica
#Configuracion de la raiz
root = Tk()

#Variable dinamica es una etiqueta qe puede cambiar de texto
texto = StringVar()
texto.set("Un nuevo texto")



Label(root, text="Holi Vale!").pack(anchor="nw")
label = Label(root, text="Otra etiqueta")
label.pack(anchor="center")
Label(root, text="Ultima etiqueta").pack(anchor="se")

label.config(bg="red", fg="black", font=("Arial", 25))
label.config(textvariable=texto)










#Siempre debe estar al final 
root.mainloop()

