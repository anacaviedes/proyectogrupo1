# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 08:54:06 2020

@author: Ana
"""
def primo(n):
  p=True
  div=2
  while div<n:
    if n%div==0:
      p=False
      break
    div=div+1
  return p

def lista_primos(n):
    primos=[]
    i=2
    while i<n:
      if primo(i)==True:
        primos.append(i)
      i=i+1
    return primos