# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 13:01:48 2020

@author: ana
"""

import pyaes
import base64

class Encriptado:
    
    def __init__(self, nombre_archivo, accion):
        self.archivo=nombre_archivo           
        self.accion=accion              
            
    def encriptacion(self, clave):
        if self.accion==1:
            with open(self.archivo, "rb") as img_file:
                self.imagen64b1 = base64.b64encode(img_file.read()) 
            aes = pyaes.AESModeOfOperationCTR(clave)
            self.encriptado=(base64.b64encode(aes.encrypt(self.imagen64b1))).decode("utf-8")
            return self.encriptado
    
    def desencriptacion(self, clave):
        if self.accion==2:
            with open(archivo, "rb") as img_file:
                self.imagen64b2 = base64.b64encode(img_file.read())      
            aes = pyaes.AESModeOfOperationCTR(clave)
            self.desencriptado=(aes.decrypt(base64.b64decode(self.imagen64b2))).decode("utf-8")
            return self.desencriptado
    
    def guardar(self):
        if self.accion==1:
            image = open(""+archivo, "wb")
            image.write(base64.b64decode(self.encriptado))
            image.close()
            print("Guardado ",""+archivo) 
        if self.accion==2:
            image = open(""+archivo, "wb")
            image.write(base64.b64decode(self.desencriptado))
            image.close()
            print("Guardado ",""+archivo) 

a=int(input("Escriba 1 para encriptar o 2 para desencriptar: "))
archivo=input("Escriba el nombre del archivo: ") #el nombre, no la ubicación; inclyendo el formato: .jpg
clave=bytes(input("Ingrese la clave: "), 'utf-8') #16, 24 o 32 caracteres

"""
b=Encriptado(archivo, a)
b.encriptacion(clave)
b.guardar()
"""
"""
c=Encriptado(archivo,a)
c.desencriptacion(clave)
c.guardar()"""

"""
#clave128 = 16caracteres.LET
#clave192 = 24caracteres.LET;-S_Nume
#clave256 = 32caracteres.LETR;-SNume::-><+¡?"""