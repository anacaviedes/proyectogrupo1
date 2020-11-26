# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 22:04:38 2020

@author: Daniel
"""
import pylab as py
from random import choice

def vecino(m,x,y):
  sizey=py.shape(m)[0]
  sizex=py.shape(m)[1]
  veci=[]

  if y+2<=sizey-1:
    if m[y+2,x]==255:
     veci.append((y+2,x))

  if m[y-2,x]==255:
   veci.append((y-2,x))

  if m[y,x-2]==255:
   veci.append((y,x-2))

  if x+2<=sizex-1:
    if m[y,x+2]==255:
     veci.append((y,x+2)) 

  return veci

def rompemuros(m,x0,y0,x1,y1):
  if x1!=150 and y1!=150:
    if x0==x1: #vertical
      if y1>y0:
        m[y0:y1+1,x0]=150 
      if y1<y0:
        m[y1:y0+1,x0]=150 
  
    if y0==y1: #horizontal
      if x1>x0:
        m[y0,x0:x1+1]=150 
      if x1<x0:
        m[y1,x1:x0+1]=150
        
def caminador(m,x,y):
  sizey=py.shape(m)[0]
  sizex=py.shape(m)[1]
  
  while True:
    if y+1<=sizey-1:
      if m[y+1,x]==150:
        if vecino(m,x,y)!=[]:
          eureka=(x,y)
          break
        m[y,x]=200
        y=y+1
        x=x
   
    if m[y-1,x]==150:
      if vecino(m,x,y)!=[]:
          eureka=(x,y)
          break
      m[y,x]=200
      y=y-1
      x=x

    if m[y,x-1]==150:
      if vecino(m,x,y)!=[]:
          eureka=(x,y)
          break
      m[y,x]=200
      x=x-1
      y=y

    if x+1<=sizex-1:
      if m[y,x+1]==150:
        if vecino(m,x,y)!=[]:
          eureka=(x,y)
          break
        m[y,x]=200
        x=x+1
        y=y
  
  return eureka

def lab(m,x,y):
  if vecino(m,x,y)!=[]:
    coor=choice(vecino(m,x,y))
    y1=coor[0]
    x1=coor[1]
    rompemuros(m,x,y,x1,y1)
    lab(m,x1,y1)
  else:  
    coor=caminador(m,x,y)
    y1=coor[1]
    x1=coor[0]
    rompemuros(m,x,y,x1,y1)
    lab(m,x1,y1)
    
