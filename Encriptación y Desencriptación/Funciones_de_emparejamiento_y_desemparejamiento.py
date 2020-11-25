# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 16:44:40 2020

@author: ERICK
"""

def emparejada(cifrado):
  emparejado=[]
  if len(cifrado)%2 != 0:
    cifrado.append(0)
  for i in range(int(len(cifrado)/2)):
    emparejado.append((int(cifrado[2*i]), int(cifrado[2*i+1])))
  return emparejado


def desemparejada(decodificado):
  desemparejado=[]
  for i in range(len(decodificado)):
    desemparejado.append(int(decodificado[i][0]))
    desemparejado.append(int(decodificado[i][1]))
  if desemparejado[-1]==0:
    del desemparejado[-1]
  return(desemparejado)