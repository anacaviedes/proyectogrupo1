# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 18:44:05 2020

@author: 
"""

import pygame, sys, random, time

class Blanco(pygame.sprite.Sprite):
    def __init__(self, ruta, x, y):
        super().__init__()
        self.image=pygame.image.load(ruta)
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class Mira(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image=pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        self.disparo = pygame.mixer.Sound("disparo.wav")
    def update(self):
        self.rect.center=pygame.mouse.get_pos()
    def dispara(self):
        self.disparo.play()
        pygame.sprite.spritecollide(mira, blanco_sprites, True)
    
class Estado():
    def __init__(self):
        self.state='main_game'
    def main_game(self):  
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                mira.dispara()                
            
        ventana.blit(fondo,(0,0))
        blanco_sprites.draw(ventana)
        j.draw(ventana)
        j.update()        
        pygame.display.flip()
              
pygame.init()
tiempo=pygame.time.Clock()
estado=Estado()

ventana_ancho=800
ventana_alto=600
ventana = pygame.display.set_mode((ventana_ancho,ventana_alto))
pygame.display.set_caption("Tiro al blanco")
fondo=pygame.image.load("fondo.jpg")

#escogencia del número de manzanas
from tkinter import *
def answer(): 
    rta = entry_window.get()  
    file = open("C:/Users/Usuario/Desktop/prog/tiro/manzanas.txt", "w")
    file.write(rta)
    file.close()
    btn_check2.pack_forget() 
root=Tk()
root.title("Escogencia")
root.geometry("150x150")
label=Label(root, text="¿Cuántas manzanas?")
label.pack()
entry_window=Entry(root, width=10, borderwidth=4)
entry_window.pack()
btn_check2=Button(root, text="Escoger", command=answer)
btn_check2.pack()
btn_quit=Button(root, text="Empezar", command=root.destroy)
btn_quit.pack()
root.mainloop()
ruta="C:/Users/Usuario/Desktop/prog/tiro/manzanas.txt"
archivo=open(ruta, 'r')
a=archivo.read()
manzanas=int(a)
print(manzanas)

pygame.mouse.set_visible(False)
mira=Mira(10, 10, "mira.png")
j = pygame.sprite.Group()
j.add(mira)
blanco_sprites=pygame.sprite.Group()

for i in range(manzanas):
    r1=random.randrange(0,ventana_ancho)
    r2=random.randrange(0,ventana_alto)    
    nuevo=Blanco("manzana.png", r1, r2)
    blanco_sprites.add(nuevo)

while True:  
    estado.main_game()
    tiempo.tick(60)
    
    
    
   
    
    
    
    
    
    
    
    
    
    