# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 17:17:14 2019

@author: Javier
"""

from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog


def test():
    #MessageBox.showinfo("Holi", "Holi canoli")
    
    #MessageBox.showwarning("Alerta,intruso", "No tienes permiso para esto")
    
    #MessageBox.showerror("Error!","Me mori")
    
    #resultado = MessageBox.askquestion("Salir", "Me abandonas?")
    #if resultado == "yes":
        #root.destroy()
    
    #resultado = MessageBox.askokcancel("Salir", "Si te vas no regresas")
    #if resultado:
        #root.destroy()
        
    #resultado = MessageBox.askyesno("Salir","Ya te vas?")
    #if resultado:
        #root.destroy()
        
    #resultado = MessageBox.askretrycancel("Reintentar", "La cagamos, sorri:(")
    #if resultado:
        #root.destroy()     
        
    #color = ColorChooser.askcolor(title="Elige un color")
    #print(color)
    
    #ruta = FileDialog.askopenfilename(title="Abrir fichero", initialdir = "C:", filetypes=(("Fichero de texto", "*.txt"),("Fichero de imagen", "*.png")))    
    #print(ruta)
    
    ##fichero = FileDialog.asksaveasfile(title="Guardar un fichero", mode="w", defaultextension=".txt")
    #if fichero is not None:
        #fichero.write("Hola,voy a escribir otracosa")
        #fichero.close()

root = Tk()

Button(root, text="Picame", command=test).pack()







#Siempre debe estar al final 
root.mainloop()

