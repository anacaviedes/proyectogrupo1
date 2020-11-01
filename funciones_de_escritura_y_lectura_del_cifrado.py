# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:54:45 2020

@author: Daniel
"""
def escritura(entra):

  alfa=[" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q"
  ,"r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K"
  ,"L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z",",",".",";",":"
  ,"¿","?","¡","!","(",")"]

  cifrado=[]
  for i in range(len(entra)):
    for j in range(len(alfa)):
      if entra[i]==alfa[j]:
        cifrado.append(j)
  return cifrado

def lectura(cifrado):
  alfa=[" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q"
  ,"r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K"
  ,"L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z",",",".",";",":"
  ,"¿","?","¡","!","(",")"]
  
  txt=[]
  for i in range(len(cifrado)):
    for j in range(len(alfa)):
      if cifrado[i]==j:
        txt.append(alfa[j])
  space=""
  mensaje=space.join(txt)
  return mensaje

