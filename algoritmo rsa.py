# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 08:54:42 2020

@author: Ana
"""

import random
import lista_primos

lista=lista_primos.lista_primos(30)
p=random.choice(lista)
q=random.choice(lista)

n=p*q
#print("n: ",n)
phi=(p-1)*(q-1)
# print("phi: ",phi)
e=5  #mcd(e,phi)=1 que no sea phi-1
#print("e: ",e)
print("clave pública: ",n,e)
d=1
while (e*d)%phi!=1:
  d=d+1
#print("d: ",d)
print("clave privada: ",n,d)


#encriptacion
m=10 #mensaje
encriptado=(m**e)%n
print(encriptado)

#desencriptacion
print((encriptado**d)%n)