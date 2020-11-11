# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 11:02:29 2020

@author: Ana Caviedes
"""

from tkinter import filedialog
import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image


raiz = tk.Tk()
raiz.geometry("1000x1000")
raiz.title("Encriptación de imágenes")
raiz.config(bg="white")

def subir(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    aviso=tk.Label(raiz,text="A continuación podrá visualizar la imagen seleccionada", bg="white")
    aviso.pack()
    im=Image.open(filename)
    img = ImageTk.PhotoImage(im)
    img2=tk.Label(raiz, image=img)
    img2.pack()

fontStyle= tkFont.Font(family="Lucida Grande", size=20)
Titulo=tk.Label(raiz,text="Bienvenido a la plataforma de encriptación", bg="white", font=fontStyle)
Titulo.pack()


label = tk.Label(raiz, text = "Selecciona la imagen a encriptar", bg="white")
button = tk.Button(raiz, text = "Buscar",command=subir, activebackground="#5FB4EF", bg="white", overrelief="raised")
label.pack()
button.pack()


raiz.mainloop()
#para ver la ventana bien se puede agrandar con el mouse
