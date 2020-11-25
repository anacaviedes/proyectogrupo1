import pygame

pygame.init()
pantalla=pygame.display.set_mode((800,800))
pygame.display.set_caption("Juego")


imagenesderecha=[pygame.image.load("R1.png"),pygame.image.load("R2.png"),pygame.image.load("R3.png"),pygame.image.load("R4.png"),pygame.image.load("R5.png"),pygame.image.load("R6.png")]
imagenesizquierda=[pygame.image.load("L1.png"),pygame.image.load("L2.png"),pygame.image.load("L3.png"),pygame.image.load("L4.png"),pygame.image.load("L5.png"),pygame.image.load("L6.png")]
disparoderecha=[pygame.image.load("FR1.png"),pygame.image.load("FR2.png"),pygame.image.load("FR3.png"),pygame.image.load("FR4.png"),pygame.image.load("FR5.png"),pygame.image.load("FR6.png"),pygame.image.load("FR7.png"),pygame.image.load("FR8.png"),pygame.image.load("FR9.png"),pygame.image.load("FR10.png"),pygame.image.load("FR11.png")]
disparoizquierda=[pygame.image.load("FL1.png"),pygame.image.load("FL2.png"),pygame.image.load("FL3.png"),pygame.image.load("FL4.png"),pygame.image.load("FL5.png"),pygame.image.load("FL6.png"),pygame.image.load("FL7.png"),pygame.image.load("FL8.png"),pygame.image.load("FL9.png"),pygame.image.load("FL10.png"),pygame.image.load("FL11.png")]
FONDO=pygame.image.load("bg1.png")
quieto=pygame.image.load("parado.png")

reloj=pygame.time.Clock()


class Jugador():
    def __init__(self,x,y,ancho,alto):
        self.x=x
        self.y=y
        self.alto=alto
        self.ancho=ancho
        self.vel=5
        self.Salto=False
        self.derecha=False
        self.izquierda=False
        self.cuentapasos=0
        self.cuentapasos2=0
        self.cuentosaltos=10
        self.parado=True
        self.disparando=False

    def dibujo__(self,pantalla):
        pantalla.blit(FONDO,(0,0))
        if not(self.parado):
            if self.cuentapasos+1>=18:
                self.cuentapasos=0
            if self.izquierda:
                pantalla.blit((imagenesizquierda[self.cuentapasos//3]),(self.x,self.y))
                self.cuentapasos+=1
            elif self.derecha:
                pantalla.blit((imagenesderecha[self.cuentapasos//3]),(self.x,self.y))
                self.cuentapasos+=1
        else:
            if self.disparando:
                if self.cuentapasos2+1>=33:
                    self.cuentapasos2=0
                if self.derecha:
                    pantalla.blit(disparoderecha[self.cuentapasos2//3],(self.x,self.y))
                    self.cuentapasos2+=1
                else:
                    if self.cuentapasos2==6:
                        self.x=self.x-38
                    elif self.cuentapasos2==9:
                        self.x=self.x+38
                    elif self.cuentapasos2==12:
                        self.x=self.x-12
                    elif self.cuentapasos2==15:
                        self.x=self.x-64
                    elif self.cuentapasos2==18:
                        self.x=self.x-81
                    elif self.cuentapasos2==21:
                        self.x=self.x-19
                    elif self.cuentapasos2==24:
                        self.x=self.x-79
                    elif self.cuentapasos2==27:
                        self.x=self.x-20
                    elif self.cuentapasos2==30:
                        self.x=self.x-13

                    pantalla.blit(disparoizquierda[self.cuentapasos2//3],(self.x,self.y))
                    self.cuentapasos2+=1
                    if self.cuentapasos2==32:
                        self.x=self.x+288


            else:
                if self.izquierda:
                    pantalla.blit(imagenesizquierda[0],(self.x,self.y))
                else:
                    pantalla.blit(imagenesderecha[0],(self.x,self.y))


        pygame.display.update()



correr=True
alien=Jugador(0,370,238,395)
while correr:
    reloj.tick(18)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            correr=False


    keys=pygame.key.get_pressed()
    if keys [pygame.K_LEFT] and alien.x>alien.vel:
        alien.x-=alien.vel
        alien.izquierda=True
        alien.derecha=False
        alien.parado=False
    elif keys[pygame.K_RIGHT] and alien.x<800-alien.ancho-alien.vel:
        alien.x+=alien.vel
        alien.izquierda=False
        alien.derecha=True
        alien.parado=False
    else:
        if keys[pygame.K_SPACE]:
            alien.parado=True
            alien.disparando=True
        else:
            if alien.cuentapasos2 in (7,8,9):
                alien.x=alien.x+38
            elif alien.cuentapasos2 in (13,14,15):
                alien.x=alien.x+12
            elif alien.cuentapasos2 in (16,17,18):
                alien.x=alien.x+76
            elif alien.cuentapasos2 in (19,20,21):
                alien.x=alien.x+157
            elif alien.cuentapasos2 in (22,23,24):
                alien.x=alien.x+176
            elif alien.cuentapasos2 in (25,26,27):
                alien.x=alien.x+255
            elif alien.cuentapasos2 in (28,29,30):
                alien.x=alien.x+275
            elif alien.cuentapasos2==31:
                alien.x=alien.x+288

            alien.cuentapasos2=0
            alien.cuentapasos=0
            alien.parado=True
            alien.disparando=False


    if not(alien.Salto):
        if keys[pygame.K_UP]:
            alien.Salto=True
            alien.paradoo=True
            alien.cuentapasos=0
    else:
        if alien.cuentosaltos>=-10:
            num=1
            if alien.cuentosaltos<0:
                num=-1
            alien.y-=(alien.cuentosaltos**2)*num*0.75
            alien.cuentosaltos-=1
        else:
            alien.Salto=False
            alien.cuentosaltos=10
    alien.dibujo__(pantalla)



pygame.quit()
