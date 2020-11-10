# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 10:45:49 2020

@author: Usuario
"""
import algoritmo_rsa

n,e,d=algoritmo_rsa.claves()
   
def encripta_rsa(mensaje,n,e):  #la función recibe el mensaje y la clave pública
    encriptado=(mensaje**e)%n
    return encriptado
   
def desencripta_rsa(encriptado,n,d):
    original=(encriptado**d)%n
    return original
"""
mensaje=19
encriptado=encripta_rsa(mensaje,n,e)
original=desencripta_rsa(encriptado,n,d)
print(mensaje, encriptado, original)"""