# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 17:17:14 2019

@author: Javier
"""

from tkinter import *
##from tkinter import messagebox as MessageBox
##from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog
from io import open

ruta = ""

def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Mi editor")

def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(
            initialdir=".",
            filetype=(("Ficheros de texto", "*.txt"),),
            title="Abrir un fichero de texto")
    
    if ruta != "":
        fichero = open(ruta, "r")
        contenido = fichero.read()
        texto.delete(1.0, "end")
        texto.insert("insert", contenido)
        fichero.close()
        root.title(ruta + "- Mi editor")

def guardar():
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = texto.get(1.0, "end-1c")
        fichero = open(ruta,"w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Dichero guardado correctamente")
    else:
        guardar_como()
        
def guardar_como():
    global ruta
    mensaje.set("Guardar fichero como")
    fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, "end-1c")
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""

root = Tk()
root.title("Editor de Vale")

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo",command=nuevo)
filemenu.add_command(label="Abrir",command=abrir)
filemenu.add_command(label="Guardar",command=guardar)
filemenu.add_command(label="Guardar como",command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.destroy)
menubar.add_cascade(menu=filemenu, label="Archivo")

texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Arial", 12))

mensaje = StringVar()
mensaje.set("Bienvenido a escribir")
monitor = Label(root,textvar=mensaje, justify="left")
monitor.pack(side="right")


root.config(menu=menubar)


#Siempre debe estar al final 
root.mainloop()

