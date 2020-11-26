# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 13:02:38 2020

@author: ERICK
"""
import pygame

def main():
    pygame.init()
    pygame.mouse.set_cursor(*pygame.cursors.diamond)
    
    size = width, height = 500, 500
    black = 0, 0, 0
    screen = pygame.display.set_mode(size)
    
    linea_blanca_vertical = pygame.image.load("linea_blanca.gif")
    linea_blanca_horizontal = pygame.image.load("linea_blanca_horizontal.gif")
    linea_azul_vertical = pygame.image.load("linea_azul.gif")
    linea_azul_horizontal = pygame.image.load("linea_azul_horizontal.gif")
    punto_azul = pygame.image.load("punto_azul.gif")
    puntaje_azules = 0
    azules=[linea_azul_vertical,linea_azul_horizontal, punto_azul,puntaje_azules]
    
    linea_roja_vertical = pygame.image.load("linea_roja.gif")
    linea_roja_horizontal = pygame.image.load("linea_roja_horizontal.gif")
    punto_rojo = pygame.image.load("punto_rojo.gif")
    puntaje_rojos=0
    rojos=[linea_roja_vertical,linea_roja_horizontal,punto_rojo,puntaje_rojos]
    
    screen.fill(black)
    
    lista_blancas = []
    lista_jugadas = []
    
    for i in range(10, width-109, 110):
        for j in range(0, height-9, 110):
            screen.blit(linea_blanca_horizontal,(i,j))
            lista_blancas.append(pygame.Rect(i,j,100,10))
            
    for i in range(0, width-9, 110):
        for j in range(10,height-109,110):
            screen.blit(linea_blanca_vertical,(i,j))
            lista_blancas.append(pygame.Rect(i,j,10,100))
    pygame.display.flip()
    
    turno=1
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coordenadas=pygame.mouse.get_pos()
                for i in lista_blancas:
                    if i.collidepoint(coordenadas)==True:
                        punto=0
                        if turno == 1:
                            color_turno=rojos
                        elif turno == -1:
                            color_turno=azules
                        if i.height == 10:
                            screen.blit(color_turno[1], i.topleft)
                            centro = i.center
                            lista_jugadas.append(centro)
                            if centro[1] < height-5:
                                if (centro[0], centro[1]+110) in lista_jugadas:
                                    if(centro[0]+55,centro[1]+55) in lista_jugadas:
                                        if (centro[0]-55,centro[1]+55) in lista_jugadas:
                                            screen.blit(color_turno[2],(centro[0]-15,centro[1]+40))
                                            color_turno[3] += 1
                                            if turno == 1:
                                                rojos = color_turno
                                            elif turno == -1:
                                                azules = color_turno
                                            punto+=1
                                            print("azules:", azules[3], "rojos:",rojos[3])
                                            
                            if centro[1] > 5:
                                if (centro[0], centro[1]-110) in lista_jugadas:
                                    if(centro[0]+55,centro[1]-55) in lista_jugadas:
                                        if (centro[0]-55,centro[1]-55) in lista_jugadas:
                                            screen.blit(color_turno[2],(centro[0]-15,centro[1]-70))
                                            color_turno[3] += 1
                                            if turno == 1:
                                                rojos = color_turno
                                            elif turno == -1:
                                                azules = color_turno
                                            punto+=1
                                            print("azules:", azules[3], "rojos:",rojos[3])
                                        
                        elif i.height == 100:
                            screen.blit(color_turno[0], i.topleft)
                            centro = i.center
                            lista_jugadas.append(centro)
                            if centro[0] < width-5:
                                if (centro[0]+110, centro[1]) in lista_jugadas:
                                    if(centro[0]+55,centro[1]+55) in lista_jugadas:
                                        if (centro[0]+55,centro[1]-55) in lista_jugadas:
                                            screen.blit(color_turno[2],(centro[0]+40,centro[1]-15))
                                            color_turno[3] += 1
                                            if turno == 1:
                                                rojos = color_turno
                                            elif turno == -1:
                                                azules = color_turno
                                            punto+=1
                                            print("azules:", azules[3], "rojos:",rojos[3])
                                            
                            if centro[0] > 5:
                                if (centro[0]-110, centro[1]) in lista_jugadas:
                                    if(centro[0]-55,centro[1]+55) in lista_jugadas:
                                        if (centro[0]-55,centro[1]-55) in lista_jugadas:
                                            screen.blit(color_turno[2],(centro[0]-70,centro[1]-15))
                                            color_turno[3] += 1
                                            if turno == 1:
                                                rojos = color_turno
                                            elif turno == -1:
                                                azules = color_turno
                                            punto+=1
                                            print("azules:", azules[3], "rojos:",rojos[3])
      
                        if punto == 0:                    
                            turno *=-1  
                        lista_blancas.remove(i)
                        pygame.display.flip()
        if len(lista_blancas)==0:
            running=False
    if azules[3] > rojos[3]:
        print("Ganan Azules")
    elif azules[3] < rojos[3]:
        print("Ganan Rojos")
    elif azules[3] == rojos[3]:
        print("Empate")
                    




if __name__ == "__main__":
    main()
    
    
            
