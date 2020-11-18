# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 13:01:48 2020

@author: ana
"""

import pyaes
import base64

def encriptacion(plaintext, clave):
   aes = pyaes.AESModeOfOperationCTR(clave)
   return (base64.b64encode(aes.encrypt(plaintext))).decode("utf-8")

def desencriptacion(encriptado, clave):
    aes = pyaes.AESModeOfOperationCTR(clave)
    return (aes.decrypt(base64.b64decode(encriptado))).decode("utf-8")


a=int(input("Escriba 1 para encriptar o 2 para desencriptar: "))
archivo=input("Escriba el nombre del archivo: ") #el nombre, no la ubicación; inclyendo el formato: .jpg
clave=bytes(input("Ingrese la clave: "), 'utf-8') #16, 24 o 32 caracteres

if a==1:   
    with open(archivo, "rb") as img_file:
        imagen64b1 = base64.b64encode(img_file.read())    
    
    encriptado = encriptacion(imagen64b1,clave)    
    encriptada_copia=encriptado    

    image = open(""+archivo, "wb")
    image.write(base64.b64decode(encriptada_copia))
    image.close()
    print("Guardado ",""+archivo) #queda en el mismo directorio de este archivo de python

else:       
    with open(archivo, "rb") as img_file:
        imagen64b2 = base64.b64encode(img_file.read())        
    
    desencriptado=desencriptacion(imagen64b2,clave)
    desencriptado_copia=desencriptado
    
    image = open(""+archivo, "wb")
    image.write(base64.b64decode(desencriptado_copia))
    image.close()
    print("Guardado", ""+archivo)


"""
#clave128 = 16caracteres.LET
#clave192 = 24caracteres.LET;-S_Nume
#clave256 = 32caracteres.LETR;-SNume::-><+¡?"""