# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:38:20 2020

@author: Usuario
"""
import numpy as np

def inversa(matriz):
    a=matriz[0][0]
    b=matriz[1][1]
    c=matriz[0][1]
    d=matriz[1][0]
    e=1/(a*b-c*d)
    matriz_t=np.array([[b,-c],[-d,a]])
    inversa=e*matriz_t
    return inversa

        
if __name__=="__main__":
    a=np.array([[4,3],[-1,2]]) 
    print(inversa(a))