import pygame

pygame.init()
pantalla=pygame.display.set_mode((1400,800))
pygame.display.set_caption("Juego")


imagenesderecha=[pygame.image.load("R1.png"),pygame.image.load("R2.png"),pygame.image.load("R3.png"),pygame.image.load("R4.png"),pygame.image.load("R5.png"),pygame.image.load("R6.png")]
imagenesizquierda=[pygame.image.load("L1.png"),pygame.image.load("L2.png"),pygame.image.load("L3.png"),pygame.image.load("L4.png"),pygame.image.load("L5.png"),pygame.image.load("L6.png")]
imagenesderechaverde=[pygame.image.load("GR1.png"),pygame.image.load("GR2.png"),pygame.image.load("GR3.png"),pygame.image.load("GR4.png"),pygame.image.load("GR5.png"),pygame.image.load("GR6.png")]
imagenesizquierdaverde=[pygame.image.load("GL1.png"),pygame.image.load("GL2.png"),pygame.image.load("GL3.png"),pygame.image.load("GL4.png"),pygame.image.load("GL5.png"),pygame.image.load("GL6.png")]
FONDO=pygame.image.load("bg1.png")
quieto=pygame.image.load("parado.png")

reloj=pygame.time.Clock()
score1=0
score2=0



class Jugador():
    def __init__(self,x,y,ancho,alto):
        self.x=x
        self.y=y
        self.alto=alto
        self.ancho=ancho
        self.vel=8
        self.Salto=False
        self.derecha=False
        self.izquierda=False
        self.cuentapasos=0
        self.cuentapasos2=0
        self.cuentosaltos=10
        self.parado=True
        self.disparando=False
        self.hitbox=(self.x,self.y, 238,395)
        self.salud=10
        self.gameover=False

    def dibujo__(self,pantalla):
        #pantalla.blit(FONDO,(0,0))
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
            if self.izquierda:
                pantalla.blit(imagenesizquierda[0],(self.x,self.y))
            else:
                pantalla.blit(imagenesderecha[0], (self.x,self.y))
        self.hitbox=(self.x,self.y, 238,395)
        pygame.draw.rect(pantalla, (26,186,21),(10,45,400,20))
        pygame.draw.rect(pantalla, (182,52,21),(410-40*(10-self.salud),45,40*(10-self.salud),20))
        pygame.draw.rect(pantalla, (0,0,0),(10,45,400,20),2)

    def golpe(self):
        if self.salud>0:
            self.salud-=1
        else:
            self.gameover=True

class enemigo(object):
    imagenesderechaverde=[pygame.image.load("GR1.png"),pygame.image.load("GR2.png"),pygame.image.load("GR3.png"),pygame.image.load("GR4.png"),pygame.image.load("GR5.png"),pygame.image.load("GR6.png")]
    imagenesizquierdaverde=[pygame.image.load("GL1.png"),pygame.image.load("GL2.png"),pygame.image.load("GL3.png"),pygame.image.load("GL4.png"),pygame.image.load("GL5.png"),pygame.image.load("GL6.png")]

    def __init__(self,x,y, ancho, alto):
        self.x=x
        self.y=y
        self.alto=alto
        self.ancho=ancho
        self.vel=8
        self.Salto=False
        self.derecha=False
        self.izquierda=False
        self.cuentapasos=0
        self.cuentapasos2=0
        self.cuentosaltos=10
        self.parado=True
        self.disparando=False
        self.hitbox=(self.x,self.y, 193,436)
        self.salud=10
        self.gameover=False

    def dibujar(self, pantalla):
        if not(self.parado):
            if self.cuentapasos+1>=18:
                self.cuentapasos=0
            if self.izquierda:
                pantalla.blit((imagenesizquierdaverde[self.cuentapasos//3]),(self.x,self.y))
                self.cuentapasos+=1
            elif self.derecha:
                pantalla.blit((imagenesderechaverde[self.cuentapasos//3]),(self.x,self.y))
                self.cuentapasos+=1
        else:
            if self.derecha:
                pantalla.blit(imagenesderechaverde[0],(self.x,self.y))
            else:
                pantalla.blit(imagenesizquierdaverde[0], (self.x,self.y))
        self.hitbox=(self.x,self.y, 193,436)
        pygame.draw.rect(pantalla, (26,186,21),(990,45,400,20))
        pygame.draw.rect(pantalla, (182,52,21),(990,45,40*(10-self.salud),20))
        pygame.draw.rect(pantalla, (0,0,0),(990,45,400,20),2)

    def golpe(self):
        if self.salud>0:
            self.salud-=1
        else:
            self.gameover=True


class Proyectiles(object):
    def __init__(self, x,y, radio, color, cara):
        self.x=x
        self.y=y
        self.radio=radio
        self.color=color
        self.cara=cara
        self.vel=20*cara

    def dibujo(self,pantalla):
        pygame.draw.circle(pantalla, self.color, (self.x,self.y), self.radio)



def dibujar():

    if alien.gameover==True or enemigo.gameover==True:
        pygame.draw.rect(pantalla, (255,255,255),(300,300,750,150))
        font1=pygame.font.SysFont("comicsans", 150, True)
        text2=font1.render("GAME OVER", 1, (0,0,0))
        pantalla.blit(text2,(300,300))
        if alien.salud==0:
            text3=font.render("Gana el Jugador 2", 1, (0,0,0))
            pantalla.blit(text3, (500,400))
        else:
            text3=font.render("Gana el Jugador 1", 1, (0,0,0))
            pantalla.blit(text3, (500,400))

    else:
        pantalla.blit(FONDO, (0,0))
        pygame.draw.rect(pantalla, (255,255,255),(10,10,400,30))
        pygame.draw.rect(pantalla, (255,255,255),(990,10,400,30))
        text=font.render("Puntaje Jugador 1:" + str(score1), 1, (0,0,0))
        text1=font.render("Puntaje Jugador 2:" + str(score2), 1, (0,0,0))
        pantalla.blit(text, (10,10))
        pantalla.blit(text1, (990,10))
        alien.dibujo__(pantalla)
        enemigo.dibujar(pantalla)
        for bala in balas:
            bala.dibujo(pantalla)
        for bala in balasenemigo:
            bala.dibujo(pantalla)


    pygame.display.update()





correr=True
font=pygame.font.SysFont("comicsans", 50, True)
alien=Jugador(0,405,238,395)
balas=[]
enemigo=enemigo(1162,364,193,436)
balasenemigo=[]
while correr:
    reloj.tick(18)


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            correr=False

    for bala in balas:
        if bala.y-bala.radio<enemigo.hitbox[1]+enemigo.hitbox[3] and bala.y+bala.radio>enemigo.hitbox[1]:
            if bala.x+bala.radio>enemigo.hitbox[0]+enemigo.hitbox[2]//2 and bala.x-bala.radio<enemigo.hitbox[0]+enemigo.hitbox[2]//2:
                enemigo.golpe()
                score1+=1
                balas.pop(balas.index(bala))
        if bala.x<1400 and bala.x>0:
            bala.x+= bala.vel
        else:
            balas.pop(balas.index(bala))

    for bala in balasenemigo:
        if bala.y-bala.radio<alien.hitbox[1]+alien.hitbox[3] and bala.y+bala.radio>alien.hitbox[1]:
            if bala.x+bala.radio>alien.hitbox[0]+alien.hitbox[2]//2 and bala.x-bala.radio<alien.hitbox[0]+alien.hitbox[2]//2:
                alien.golpe()
                score2+=1
                balasenemigo.pop(balasenemigo.index(bala))
        if bala.x<1400 and bala.x>0:
            bala.x+= bala.vel
        else:
            balasenemigo.pop(balasenemigo.index(bala))

    keys=pygame.key.get_pressed()
    if keys [pygame.K_SPACE]:
        if alien.izquierda:
            cara=-1
        else:
            cara=1

        if len(balas) < 1:
            balas.append(Proyectiles(round(alien.x+alien.ancho//2), round(alien.y+alien.alto//2), 30, (184,93,243), cara))

    if keys [pygame.K_s]:
        if enemigo.izquierda:
            cara1=-1
        else:
            cara1=1

        if len(balasenemigo) < 1:
            balasenemigo.append(Proyectiles(round(enemigo.x+enemigo.ancho//2), round(enemigo.y+enemigo.alto//2), 30, (73,230,68), cara1))

    if keys [pygame.K_LEFT] and alien.x>alien.vel:
        alien.x-=alien.vel
        alien.izquierda=True
        alien.derecha=False
        alien.parado=False
    elif keys[pygame.K_RIGHT] and alien.x<1400-alien.ancho-alien.vel:
        alien.x+=alien.vel
        alien.izquierda=False
        alien.derecha=True
        alien.parado=False
    else:
        alien.parado=True
        alien.disparando=True
        alien.cuentapasos=0

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

    if keys [pygame.K_a] and enemigo.x>enemigo.vel:
        enemigo.x-=enemigo.vel
        enemigo.izquierda=True
        enemigo.derecha=False
        enemigo.parado=False
    elif keys[pygame.K_d] and enemigo.x<1400-enemigo.ancho-enemigo.vel:
        enemigo.x+=enemigo.vel
        enemigo.izquierda=False
        enemigo.derecha=True
        enemigo.parado=False
    else:
        enemigo.parado=True
        enemigo.disparando=True
        enemigocuentapasos=0

    if not(enemigo.Salto):
        if keys[pygame.K_w]:
            enemigo.Salto=True
            enemigo.paradoo=True
            enemigo.cuentapasos=0
    else:
        if enemigo.cuentosaltos>=-10:
            nume=1
            if enemigo.cuentosaltos<0:
                nume=-1
            enemigo.y-=(enemigo.cuentosaltos**2)*nume*0.75
            enemigo.cuentosaltos-=1
        else:
            enemigo.Salto=False
            enemigo.cuentosaltos=10

    dibujar()




pygame.quit()
