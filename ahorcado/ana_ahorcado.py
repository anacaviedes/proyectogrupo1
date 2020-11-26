# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:00:08 2020

@author: Ana Caviedes
"""
import random
import time
import pylab as pl
from PIL import Image, ImageDraw




image = Image.new('RGB', (500, 500))
draw = ImageDraw.Draw(image)
shape1 = [(400, 500), (400, 100)] 
draw.line(shape1, fill =255, width = 10) 
shape2 = [(400, 100), (200, 100)] 
draw.line(shape2, fill =255, width = 10) 
shape3 = [(200, 100), (200, 150)] 
draw.line(shape3, fill =255, width = 10)
 


lista1=["libro", "enciclopedia", "manuscrito", "codice", "escritura"]
lista1_n1=[]
lista1_n2=[]
for i in range(len(lista1)):
    if len(lista1[i])<=5:
        lista1_n1.append(lista1[i])
    if len(lista1[i])>5:
        lista1_n2.append(lista1[i])
lista2=["newton", "torque", "gravedad", "foton", "electron"]
lista2_n1=[]
lista2_n2=[]
for i in range(len(lista2)):
    if len(lista1[i])<=5:
        lista2_n1.append(lista2[i])
    if len(lista1[i])>5:
        lista2_n2.append(lista2[i])



tema=int(input("¿Cuál tema quieres? 1 Escritura, 2 Ciencia: "))
dificultad=int(input("Escoje el nivel de dificultad: 1 o 2: "))
if tema==1:
    if dificultad==1:
        abc="abcdefghijklmnñopqrstuvwxyz"
        abecedario=" ".join(abc)
        print(abecedario)
        p=random.choice(lista1_n1)
        #print(p)
        linea_orig=" _ "*len(p)
        print(linea_orig)
        pl.imshow(image) 
    if dificultad==2:
        abc="abcdefghijklmnñopqrstuvwxyz"
        abecedario=" ".join(abc)
        print(abecedario)
        p=random.choice(lista1_n2)
        #print(p)
        linea_orig=" _ "*len(p)
        print(linea_orig)
        pl.imshow(image) 
    
    
if tema==2:
    abc="abcdefghijklmnñopqrstuvwxyz"
    abecedario=" ".join(abc)
    print(abecedario)
    p=random.choice(lista2)
    #print(p)
    linea_orig=" _ "*len(p)
    print(linea_orig)
    pl.imshow(image) 
    
    
      

p_sinrepetir="".join(set(p))
    
a=input("Escribe una letra: ")   
contador=0 
letras_bien=[]
letras_mal=[]


linea=linea_orig.replace(" ","")



while True:        
    
    if a not in 'abcdefghijklmnñopqrstuvwxyz':
            print ('Esa no es una letra')
    if a in 'abcdefghijklmnñopqrstuvwxyz':        
        if a in letras_bien or a in letras_mal:
            a=input("Esa la ya usaste. Elige otra letra: ")
        else:            
            if a in p:
                print("bien")                 
                letras_bien.append(a)
                
                linea_sp=linea.replace(" ","")
                linea=linea_sp
                lista=list(linea)
                
                for i in range(len(lista)):
                    if p[i]==a:
                        lista[i]=a                             
                        linea_n=str(lista)
                        linea_n1=linea_n.replace(",","")
                        linea_n2=linea_n1.replace("[","")
                        linea_n3=linea_n2.replace("]","")
                        linea=linea_n3.replace("'","") 
                        
                                             
                l=len(letras_bien)                
                if len(letras_bien)==len(p_sinrepetir):
                    print("Has ganado, humano")
                    break
            else:
                contador=contador+1
                print("mal")  
                letras_mal.append(a)
            if contador==6:
                print("Ahorcado... La palabra es: ",p)
                break               
       
    
    abeceda=abecedario.replace(a,"")
    abecedario=abeceda
    print(abecedario)
    print(linea)
    pl.imshow(image)
    duracion=5
    finaliza=time.time()+duracion
    l=input("Escriba una letra en menos de 5 segundos: ")
    a=l.lower()
    if time.time()>finaliza:
        print("Te demoraste mucho, perdiste")
        break