# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 21:22:57 2020

@author: Daniel
"""
import pylab as pl
from random import randrange

im=pl.imread("/content/drive/My Drive/Programacion/Captura de pantalla 2020-11-11 150455.jpg")
imp2=im.copy()
foto=pl.where(imp2[:,:,2]<100,0,255).astype("uint8")  
pl.imshow(foto)
pl.foto.shape 

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
  b=pl.foto[f,:]
  newlist=moverlist(b,d,"+")
  for i in range(len(b)):
    pl.foto[f,i]=newlist[i]
  

#mueve una columna hacia la abajo

def dezcol(c,D):
  ñ=pl.foto[:,c]
  newlist=moverlist(ñ,D,"+")
  for i in range(len(ñ)):
    pl.foto[i,c]=newlist[i]
    
def encripho(foto):
  x=foto.shape[1]
  y=foto.shape[0] 
  insfila=[]
  inscol=[]
  for i in range(x):
    r=randrange(0,y)
    dezcol(i,r)
    inscol.append(r)
  for j in range(y):
    r=randrange(0,x)
    dezfila(j,r)
    insfila.append(r)
  return inscol,insfila
  
##recuerde que para tener las instruciones qeu desencriptan la foto debe asignar
##alguna variable a la encriptacion para poder poner 
##desencripho(nombre de su variable[0],nombre de su variable[1])
def desencripho(inscol,insfila):
  x=foto.shape[1]
  y=foto.shape[0] 
  for j in range(y):
    dezfila(j,x-insfila[j])
  for i in range(x):
    dezcol(i,y-inscol[i])
    
