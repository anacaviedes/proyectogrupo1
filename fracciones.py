# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 06:27:03 2020

@author: Usuario
"""

import mcd 

class Fraccion:

  def __init__(self,num,den=1):
    g=mcd.MCD(num,den)
    self.numerador=num/g
    self.denominador=den/g
 

  def __add__(self,other):
    if isinstance(other,Fraccion):
      return Fraccion((self.numerador*other.denominador+self.denominador*other.numerador),(self.denominador*other.denominador))
    elif isinstance(other, int):
      return Fraccion(other*self.denominador+self.numerador, self.denominador)
    elif isinstance(other, float):
      return float(self.numerador/self.denominador + other)
    else: return NotImplemented
  def __radd__(self,other):
    return self+other


  def __sub__(self,other):
      if isinstance(other,Fraccion):
        return Fraccion((self.numerador*other.denominador-self.denominador*other.numerador),(self.denominador*other.denominador))
      elif isinstance(other,int):
        return Fraccion(self.numerador-other*self.denominador, self.denominador)
      elif isinstance(other,float):
        return float(self.numerador/self.denominador - other)
      else: return NotImplemented
  def __rsub__(self,other):
    return -(self-other)


  def __neg__(self):
      return Fraccion(-self.numerador,self.denominador)

  
  def __mul__(self,other):
    if isinstance(other,Fraccion):
      return Fraccion((self.numerador*other.numerador),(self.denominador*other.denominador))
    elif isinstance(other,int):
      return Fraccion(self.numerador*other, self.denominador)
    elif isinstance(other,float):
      return float(self.numerador/self.denominador * other)
    else: return NotImplemented
  def __rmul__(self, other):
    return self*other
  

  def __truediv__(self,other):
    if isinstance(other,Fraccion):
      return Fraccion(self.numerador*other.denominador,self.denominador*other.numerador)
    elif isinstance(other,int):
      return Fraccion(self.numerador, other*self.denominador)
    elif isinstance(other,float):
      return float(self.numerador/self.denominador / other)
    else: return NotImplemented
  def __rtruediv__(self, other):
    if isinstance(other,int):
      t=Fraccion(other,1)
      return Fraccion(t.numerador*self.denominador, t.denominador*self.numerador)
      #return Fraccion(other*self.denominador, self.numerador)
    if isinstance(other,float):
      return float(other/(self.numerador/self.denominador))

  def __str__(self):
    return "{:.1f}/{:.1f}".format(self.numerador,self.denominador)
hola