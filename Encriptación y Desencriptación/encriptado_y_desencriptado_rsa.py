# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 10:45:49 2020

@author: Usuario
"""
import algoritmo_rsa
if __name__=="__main__":
    n,e,d= algoritmo_rsa.claves()
   
def encripta_rsa(mensaje,n,e):  #la función recibe el mensaje y la clave pública
    encriptado=(mensaje**e)%n
    cociente=encriptado//255
    residuo=encriptado%255
    return encriptado, cociente, residuo #se usa el residuo si el encriptado es mayor que 255
   
def desencripta_rsa(encriptado,cociente,residuo,n,d):
    if residuo ==0:
        original=((encriptado**d)%n)%255
    if residuo!=0:
        a=cociente*255+residuo
        original=((a**d)%n)%255        
    return original


"""
mensaje=19
encriptado,cociente,residuo=encripta_rsa(mensaje,n,e)
original=desencripta_rsa(encriptado,cociente,residuo,n,d)
print(mensaje, encriptado, residuo, original)"""