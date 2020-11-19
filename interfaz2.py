from tkinter import filedialog
from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk, Image
import fase_1_imagenes_BN as encriptado
import pylab as pl
from random import randrange
import pyaes_encriptado as pya

class App():

    def __init__(self, master):
        self.frame=Frame(master)
        fontStyle= tkFont.Font(family="Lucida Grande", size=30)
        self.Titulo=Label(self.frame,text="Bienvenido a la plataforma de encriptación", bg="white", font=fontStyle)
        self.Titulo.pack()
        self.frame.pack()
        self.label = Label(self.frame, text = "Selecciona la imagen a encriptar", bg="white")
        self.button = Button(self.frame, text = "Buscar",command=self.subir, activebackground="#5FB4EF", bg="white", overrelief="raised")
        self.label.pack()
        self.button.pack()

    def encriptado2(self,event=None):
        self.encriptar=pya.Encriptado(self.filename2,1)
        self.introducirclave1()

    def guardar2(self, event=None):
        self.encriptar.guardar()


    def desencriptado2(self,event=None):
        self.encriptar=pya.Encriptado(self.filename2,1)
        self.introducirclave1()


    def introducirclave1(self, event=None):
        anuncio2=Label(raiz, text=("Introduzca una clave de 16 caracteres"), bg= "White")
        anuncio2.pack()
        self.prueba=Entry(raiz)
        self.prueba.pack()
        boton=Button(raiz,text="Seleccionar", command=self.anuncio)
        boton.pack()

    def introducirclave2(self, event=None):
        anuncio2=Label(raiz, text=("Introduzca su clave de 16 caracteres"), bg= "White")
        anuncio2.pack()
        self.prueba=Entry(raiz)
        self.prueba.pack()
        boton=Button(raiz,text="Seleccionar", command=self.anuncio1)
        boton.pack()

    def anuncio(self,event=None):
        self.prueba2=self.prueba.get()
        self.clavefinal=bytes(self.prueba2, 'utf-8')
        anuncio=Label(raiz, text=("La clave introducida fue:"+self.prueba2), bg= "White")
        anuncio.pack()
        self.button3= Button(self.frame, text="Descargar", command=self.guardar2, activebackground="#5FB4EF", bg="white", overrelief="raised")
        self.button3.pack()
        self.encriptar.encriptacion(self.clavefinal)

    def anuncio1(self,event=None):
        self.prueba2=self.prueba.get()
        self.clavefinal=bytes(self.prueba2, 'utf-8')
        anuncio=Label(raiz, text=("La clave introducida fue:"+self.prueba2), bg= "White")
        anuncio.pack()
        self.button3= Button(self.frame, text="Descargar", command=self.guardar2, activebackground="#5FB4EF", bg="white", overrelief="raised")
        self.button3.pack()
        self.encriptar.desencriptacion(self.clavefinal)

    #def encriptar(self, event=None):
        #im=pl.imread(self.filename2)
        #self.imp2=im.copy()
        #self.foto=pl.where(self.imp2[:,:,2]<100,0,255).astype("uint8")
        #self.encripho(self.foto)
        #self.avisoclave=Label(self.frame,text="Guarde la siguiente clave para desencriptar la imagen, en el siguiente botón podrá descargar la imagen codificada",bg="White")
        #self.avisoclave.pack()
        #self.clave=Label(self.frame, wraplength=500 ,text=((self.inscol),(","), (self.insfila)), bg="White")
        #self.clave.pack()
        #self.button3= Button(self.frame, text="Descargar", command=self.descargarencrip, activebackground="#5FB4EF", bg="white", overrelief="raised")
        #self.button3.pack()

    #def desencriptar(self, event=None):
        #im=pl.imread(self.filename2)
        #self.imp2=im.copy()
        #self.foto=pl.where(self.imp2[:,:,2]<100,0,255).astype("uint8")
        #encriptado.desencripho(self.introducirclave1, self.introducirclave2, self.foto)
        #self.aviso5=Label(raiz,text="A continuación podrá descargar su imagen desencriptada", bg="white")
        #self.aviso5.pack()
        #self.button3= Button(self.frame, text="Descargar", command=self.descargardesencrip, activebackground="#5FB4EF", bg="white", overrelief="raised")
        #self.button3.pack()

    #def introducirclave1(self,event=None):
        #self.aviso6=Label(raiz,text="Introduzca la primera lista de su clave en este espacio", bg="white")
        #self.aviso6.pack()
        #self.clave=Entry(self.frame)
        #self.clave.pack()
        #self.clavestr=str(self.clave)
        #return self.clavestr

    #def introducirclave2(self,event=None):
        #self.aviso7=Label(raiz,text="Introduzca la primera lista de su clave en este espacio", bg="white")
        #self.aviso7.pack()
        #self.clave1=Entry(self.frame)
        #self.clave1.pack()
        #self.clavestr1=str(self.clave)
        #return self.clavestr1

    def subir(self,event=None):
        filename = filedialog.askopenfilename()
        print('Selected:', filename)
        self.filename2=str(filename)
        self.img=ImageTk.PhotoImage(file=self.filename2)
        self.img2=Label(raiz, image=self.img, bg="white")
        self.img2.pack()
        self.im =Image.fromarray(self.foto)
        self.im.save("Imagen encriptada.jpg")
        self.seleccion()

    #def descargarencrip(self, event=None):
        #self.im =Image.fromarray(self.foto)
        #self.im.save("Imagen encriptada.jpg")
        #self.labelfinal=Label(self.frame, text="Su imagen fue descargada por favor revise la carpeta en la que se encuentra el programa", bg="White")
        #self.labelfinal.pack()

    #def descargardesencrip(self, event=None):
        #self.im =Image.fromarray(self.foto)
        #self.im.save("Imagen desencriptada.jpg")
        #self.labelfinal=Label(self.frame, text="Su imagen fue descargada por favor revise la carpeta en la que se encuentra el programa", bg="White")
        #self.labelfinal.pack()

    def seleccion(self, event=None):
        variable = StringVar()
        self.radiobutton1 = Radiobutton(text="Encriptar", variable=variable, value=1, command=self.encriptado2,bg="White")
        self.radiobutton2 = Radiobutton(text="Desencriptar", variable=variable, value=2, command=self.desencriptado2,bg="White")
        self.radiobutton1.pack()
        self.radiobutton2.pack()
        variable.get()

raiz = Tk()
raiz.geometry("1000x1000")
raiz.title("Encriptación de imágenes")
raiz.config(bg="white")
Prueba=App(raiz)
raiz.mainloop()
