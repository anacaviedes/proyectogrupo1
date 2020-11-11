#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 21:19:22 2020

@author: Laura
"""

import calcula_inversa as ci
import verifica_inversa as vi
import introduce_clave as ic
import Funciones_de_emparejamiento_y_desemparejamiento as fe
import fun_esc_lec_2 as el


def producto():
  matriz=ic.clave()
  pf=list()
  while not vi.verificacion(matriz):
    print("Elija otra clave")
    matriz=ic.clave()
  wt=input("Escriba '1' para codificar ó '2' para decodificar: ")
  while wt not in ["1","2"]:
    wt=input("Escriba '1' para codificar ó '2' para decodificar: ")

  if wt=="1":     
    cadena=input("Introduzca el mensaje o ruta archivo a codificar: ")
    try: 
     cadena=r''+cadena+''
     f=open(cadena)
     Ca=f.read()
     cadena=fe.emparejada(el.escritura(Ca))
     a=True
    except:
     a=False
     cadena=fe.emparejada(el.escritura(cadena))
      
    for i in range (len(cadena)):
      p1=matriz.dot(cadena[i])
      pf.append(str(int(p1[0])))
      pf.append(" ")
      pf.append(str(int(p1[1])))
      pf.append(" ")
    n=""
    pf=n.join(pf)
    if a:
      En=open("Archivo_Enciptado", "w")
      En.write(pf)
    else:
      return print(pf)

  elif wt=="2":
    cifradoin=input("Introduzca los números de su mensaje cifrado separados por espacios: ")
    cifrado=cifradoin.split()
    cadena=fe.emparejada(cifrado)
    mi=ci.inversa(matriz)
    for i in range (len(cadena)):
      p1=mi.dot(cadena[i])
      pf.append(int(p1[0]))
      pf.append(int(p1[1]))
    pf=el.lectura(pf)
    return print(pf)

if __name__=="__main__":
    producto()
