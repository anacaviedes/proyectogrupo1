# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 11:02:29 2020

@author: Ana Caviedes
"""

from tkinter import filedialog
from tkinter import *

def subir(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

raiz = Tk()
raiz.title("Encriptación de imágenes")
raiz.config(bg="blue")


label = Label(raiz, text = "Selecciona la imagen a encriptar")
button = Button(raiz, text = "Buscar",command=subir)
label.pack()
button.pack()

raiz.mainloop()
#para ver la ventana bien se puede agrandar con el mouse