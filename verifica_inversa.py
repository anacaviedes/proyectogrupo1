# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:13:56 2020

@author: Usuario
"""

import numpy as np

def verificacion (matriz):
    if matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0] !=0:
        print("Prosigue la codificación")
    else:
        print("Utilice otra clave")
        
        
if __name__=="__main__":
    a=np.array([[4,3],[-1,2]]) 
    print(verificacion(a))    
