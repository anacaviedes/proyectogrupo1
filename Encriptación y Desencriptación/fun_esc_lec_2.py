# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 19:11:26 2020

@author: Daniel
"""
def escritura(entra):

  cifrado=[]
  for i in range(len(entra)):
    c=ord(entra[i])
    cifrado.append(c)
  return cifrado

def lectura(cifrado):

  txt=[]
  for i in range(len(cifrado)):
    l=chr(cifrado[i])
    txt.append(l)
  space=""
  mensaje=space.join(txt)
  return mensaje
