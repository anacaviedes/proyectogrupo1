# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 11:02:29 2020

@author: Ana Caviedes
"""

from tkinter import filedialog
from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk, Image

raiz = Tk()
raiz.geometry("1000x1000")
raiz.title("Encriptación de imágenes")
raiz.config(bg="white")

def descargar(event=None):
    aviso4=Label(raiz,text="Su imagen se descargará")
    aviso4.pack()


def subir(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    filename2=str(filename)
    aviso1=Label(raiz,text="A continuación podrá ver la imagen seleccionada",bg="white")
    aviso1.pack()
    img=ImageTk.PhotoImage(file=filename2)
    img2=Label(raiz, image=img)
    img2.pack()
    #espacio=Label(raiz,text= " ",bg="white")
    #espacio.pack()
    #button2= Button(raiz, text="Descargar", command=descargar, activebackground="#5FB4EF", bg="white", overrelief="raised")
    #button2.pack()





#imagenpru=ImageTk.PhotoImage(file="/Users/lithium/Documents/GitHub/proyectogrupo1/prueba.jpg")
#imagenprueba=Label(raiz,image=imagenpru)
#imagenprueba.pack()


fontStyle= tkFont.Font(family="Lucida Grande", size=20)
Titulo=Label(raiz,text="Bienvenido a la plataforma de encriptación", bg="white", font=fontStyle)
Titulo.pack()


label = Label(raiz, text = "Selecciona la imagen a encriptar", bg="white")
button = Button(raiz, text = "Buscar",command=subir, activebackground="#5FB4EF", bg="white", overrelief="raised")
label.pack()
button.pack()




raiz.mainloop()
#para ver la ventana bien se puede agrandar con el mouse
