# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 22:11:32 2020

@author: Daniel
"""
import pylab as py

class laberinto:
  def __init__(self,sx,sy):
    #crea una hoja en balco del tamaño pedidio
    m=py.zeros((sy+1,sx+1),dtype=int)
    m[:,:]=255
    self.m=m
  

  def linea(self,x0,y0,x1,y1):
    #lineas horizontales en cualquier direccion
    if x0<=x1:
      if y0==y1:
        while x0!=x1:
          self.m[y0,x0]=0
          x0=x0+1
        self.m[y1,x1]=0
    if x0>x1:
      if y0==y1:
        while x0!=x1:
          self.m[y0,x1]=0
          x1=x1+1
        self.m[y1,x0]=0
    #lineas verticales en cualquier direccion
    if y0<=y1:
      if x0==x1:
        while y0!=y1:
          self.m[y0,x0]=0
          y0=y0+1
        self.m[y1,x1]=0
    if y0>y1:
      if x0==x1:
        while y0!=y1:
          self.m[y1,x0]=0
          y1=y1+1
        self.m[y0,x1]=0
  
  def camino(self,x0,y0,x1,y1):
    if y0==y1:
      self.linea(x0,y0+1,x1,y0+1)
      self.linea(x0,y0-1,x1,y0-1)

    if x0==x1:
      self.linea(x0+1,y0,x1+1,y1)
      self.linea(x0-1,y0,x1-1,y1)
    
    self.m[y0,x0]=255
  
  def esquina(self,x0,y0,cuadrante): 
    n=cuadrante                                 
    if n==1:                                   
      self.linea(x0+1,y0+1,x0+1,y0-1)
      self.linea(x0+1,y0-1,x0-1,y0-1)
    if n==2:
      self.linea(x0+1,y0-1,x0-1,y0-1)
      self.linea(x0-1,y0-1,x0-1,y0+1)
    if n==3:
      self.linea(x0-1,y0-1,x0-1,y0+1)
      self.linea(x0+1,y0+1,x0-1,y0+1)
    if n==4:
      self.linea(x0+1,y0-1,x0+1,y0+1)
      self.linea(x0+1,y0+1,x0-1,y0+1)
  
  def de_texto(self, instrucciones):
    "linea x0 y0 x1 y1 camino x0 y0 x1 y1 esquina x0 y0 cuadrante "
    ins=instrucciones.split()
    x=self
    op=["linea","camino","esquina"]
    ip=0
    i=0
    for j in range(len(ins)):
      
      if (ins[i]==op[0] or ins[i]==op[1] or ins[i]==op[2]):    
        
        ip=i
        
        if ins[i]==op[0]:
          x0=int(ins[ip+1])
          y0=int(ins[ip+2])
          x1=int(ins[ip+3])
          y1=int(ins[ip+4])
          x.linea( x0 , y0 , x1 , y1 )
          i=i+4
         
        
        if ins[i]==op[1]:
          x0=int(ins[ip+1])
          y0=int(ins[ip+2])
          x1=int(ins[ip+3])
          y1=int(ins[ip+4])
          x.camino( x0 , y0 , x1 , y1 )
          i=i+4
         
        
        if ins[i]==op[2]:
          x0=int(ins[ip+1])
          y0=int(ins[ip+2])
          cuadrante=int(ins[ip+3])
          x.esquina(x0 , y0 , cuadrante)
          i=i+3
          
      i+=1
      if i >= len(ins):
        break

  def mostrar(self):
    """Visualizar el dibujo a color"""
    py.imshow(self.m, cmap = 'gray')
  def matriz(self):  
    return self.m
   
x=40
y=40
celdas1=laberinto(x,y)
celdas=celdas1.matriz()

i=0
for j in range(int((x/2)+1)):
  celdas1.linea(i,0,i,y)
  i=i+2

i=0
for j in range(int((y/2)+1)):
  celdas1.linea(0,i,x,i)
  i=i+2
celdas1.mostrar()
celdas=celdas1.matriz()