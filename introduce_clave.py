# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 20:00:08 2020

@author: Usuario
"""
import numpy as np

def clave():    
    cadena_num=input("Escribe la clave de 4 números enteros separados por espacios: ")
    cadena_num=cadena_num.split()
    c0=cadena_num[0]
    c1=cadena_num[1]
    c2=cadena_num[2]
    c3=cadena_num[3]
    clave=np.array([[c0,c1],[c2,c3]])
    #print(clave)
    return clave

#clave()
