# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 13:54:08 2020

@author: Daniel
"""
alfa=[" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
asig=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

x="esto es una prueba y creo que funciona bien "

y=[]
for i in range(len(x)):
  for j in range(26):
    if x[i]==alfa[j]:
      y.append(j)
print(y)

txt=[]
for i in range(len(x)):
  for j in range(26):
    if y[i]==asig[j]:
      txt.append(alfa[j])
space=""
mensaje=space.join(txt)
print(txt)
print(mensaje)

