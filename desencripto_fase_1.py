# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:28:01 2020

@author: Daniel
"""
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
