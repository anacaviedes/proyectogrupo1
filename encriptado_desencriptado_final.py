# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 22:24:49 2020

@author: Daniel
"""
import pylab as py
from random import randrange

im=py.imread("ruta de la imagen :v.jpg")
foto=im.copy()
py.imshow(foto)
foto.shape 

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

#B/N
def dezfilaBN(f, d):
  b=foto[f,:]
  newlist=moverlist(b,d,"+")
  for i in range(len(b)):
    foto[f,i]=newlist[i]

def dezcolBN(c,D):
  ñ=foto[:,c]
  newlist=moverlist(ñ,D,"+")
  for i in range(len(ñ)):
    foto[i,c]=newlist[i]

#color
def dezfila(f,d):
  for j in range(3):
    b=foto[f,:,j]
    newlist=moverlist(b,d,"+")
    for i in range (len(b)):
      foto[f,i,j]=newlist[i]

def dezcol(c,D):
  for j in range(3):
    b=foto[:,c,j]
    newlist=moverlist(b,D,"+")
    for i in range (len(b)):
      foto[i,c,j]=newlist[i]

def encripho(foto):
  x=foto.shape[1]
  y=foto.shape[0] 
  insfila=[]
  inscol=[]
  if len(foto.shape)==2:
    for i in range(x):
      r=randrange(0,y)
      dezcolBN(i,r)
      inscol.append(r)
    for j in range(y):
      r=randrange(0,x)
      dezfilaBN(j,r)
      insfila.append(r)
  if len(foto.shape)==3:
    for i in range(x):
      r=randrange(0,y)
      dezcol(i,r)
      inscol.append(r)
    for j in range(y):
      r=randrange(0,x)
      dezfila(j,r)
      insfila.append(r)
  return inscol,insfila

def desencripho(inscol,insfila):
  x=foto.shape[1]
  y=foto.shape[0] 
  if len(foto.shape)==2:
    for j in range(y):
      dezfilaBN(j,x-insfila[j])
    for i in range(x):
      dezcolBN(i,y-inscol[i])
  if len(foto.shape)==3:
    for j in range(y):
      dezfila(j,x-insfila[j])
    for i in range(x):
      dezcol(i,y-inscol[i])

