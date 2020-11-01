#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 21:19:22 2020

@author: lithium
"""

import calcula_inversa as ci
import verifica_inversa as vi
import introduce_clave as ic
import Funciones_de_emparejamiento_y_desemparejamiento as fe
import funciones_de_escritura_y_lectura_del_cifrado as el



def producto():
  matriz=ic.clave()
  pf=list()
  if vi.verificacion(matriz)==True:
    wt=input("Escriba '1' para codificar ó '2' para decodificar: ")
    if wt=="1":     
      cadena=fe.emparejada(el.escritura(input("Introduzca el mensaje a codificar: ")))
      for i in range (len(cadena)):
        p1=matriz.dot(cadena[i])
        pf.append(int(p1[0]))
        pf.append(int(p1[1]))
    elif wt=="2":
      cifradoin=input("Introduzca los números de su mensaje cifrado separados por espacios: ")
      cifrado=cifradoin.split()
      print(cifrado,type(cifrado))
      cadena=fe.emparejada(cifrado)
      for i in range (len(cadena)):
        mi=ci.inversa(matriz)
        p1=mi.dot(cadena[i])
        pf.append(p1)
  else:
    print("Elija otra clave y vuelva a empezar")
  return pf
