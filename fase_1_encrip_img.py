# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 18:10:33 2020

@author: Daniel
"""
import pylab as pl
from random import randrange


ruta=("C:/Users/Usuario/Documents/GitHub/proyectogrupo1/imagen_planetas.jpg")
im=pl.imread(ruta)
imp2=im.copy()
foto=pl.where(imp2[:,:,2]<100,0,255).astype("uint8")  
pl.imshow(foto)
foto.shape 

"from google.colab import drive \n drive.mount('/content/drive')"



def moverlist(lista,distancia,direccion):
  d=distancia
  b=lista
  newlista=[]
  if direccion=="+":     #mueve a la izquierda una lista
    for i in range(len(b)):
      newlista.append(b[i-d])
  
  if direccion=="-":   #mueve a la derecha una lista
    for i in range(len(b)):
      if i+d>=len(b):
        for j in range(d):
          newlista.append(b[j])
        break
      else:
        newlista.append(b[i+d])
  return newlista

#mueve una fila hacia la derecha
def dezfila(f, d):
  b=foto[f,:]
  newlist=moverlist(b,d,"+")
  for i in range(len(b)):
    foto[f,i]=newlist[i]
  pl.imshow(foto)

#mueve una columna hacia la abajo

def dezcol(c,D):
  ñ=foto[:,c]
  newlist=moverlist(ñ,D,"+")
  for i in range(len(ñ)):
    foto[i,c]=newlist[i]
  pl.imshow(foto)
  
def encripho(foto):
  x=foto.shape[1]
  y=foto.shape[0] 
  for i in range(x):
    r=randrange(0,y)
    dezcol(i,r)
  for j in range(y):
    r=randrange(0,x)
    dezfila(j,r)

def desencripho(inscol,insfila):
  x=foto.shape[1]
  y=foto.shape[0] 
  for j in range(y):
    dezfila(j,x-insfila[j])
  for i in range(x):
    dezcol(i,y-inscol[i])
#encripho(imp2)