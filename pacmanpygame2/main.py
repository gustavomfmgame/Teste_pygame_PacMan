import pygame
from sys import exit
from mapa import retangulos_paredes
from player import jogadorA, jogador
from inimigos import inimigo1,inimigo2,inimigo3,inimigo4
from const import tam_bloco, matriz

pygame.init()
screen = pygame.display.set_mode((560, 620))
clock = pygame.Clock()



listinimigs = [inimigo1, inimigo2, inimigo3, inimigo4]
coordscomida = []

coordsinimigs = [(i.x, i.y) for i in listinimigs if i.vivo ]

for i, linha in enumerate(matriz):
    for j, caractere in enumerate(linha):
        if (j, i) not in coordsinimigs and (j, i) != (jogador.x, jogador.y) and matriz[i][j] != '#':
            comida = pygame.Rect((j+0.4)*20, (i+0.4)*20, 5, 5)
            coordscomida.append(comida) 

def gerar_comida():
    for comida in coordscomida:
        pygame.draw.rect(screen,(255, 255, 0), comida)

def comer():
    for comida in coordscomida:
        if jogadorA.colliderect(comida):
            if coordscomida:
                coordscomida.remove(comida)

inimigoA = pygame.Rect(inimigo1.x * 20, inimigo1.y * 20, tam_bloco, tam_bloco)
inimigoB = pygame.Rect(inimigo2.x * 20, inimigo2.y * 20, tam_bloco, tam_bloco)
inimigoC = pygame.Rect(inimigo3.x * 20, inimigo3.y * 20, tam_bloco, tam_bloco)
inimigoD = pygame.Rect(inimigo4.x * 20, inimigo4.y * 20, tam_bloco, tam_bloco)

inimigos = [inimigoA, inimigoB, inimigoC, inimigoD]


def gerar_mapa():   
    for parede in retangulos_paredes:
        pygame.draw.rect(screen,(0,0,255),parede)

def mover_jogador():

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]: jogador.mov_x = jogador.velocidade
    if keys[pygame.K_a]: jogador.mov_x = -jogador.velocidade

    jogadorA.x += jogador.mov_x

    for parede in retangulos_paredes:
        if jogadorA.colliderect(parede):
            if jogador.mov_x > 0: 
                jogadorA.right = parede.left
                jogador.mov_x = 0
            if jogador.mov_x < 0: 
                jogadorA.left = parede.right
                jogador.mov_x = 0

    if keys[pygame.K_w]: jogador.mov_y = -jogador.velocidade
    if keys[pygame.K_s]: jogador.mov_y = jogador.velocidade

    jogadorA.y += jogador.mov_y

    for parede in retangulos_paredes:
        if jogadorA.colliderect(parede):
            if jogador.mov_y < 0: 
                jogadorA.top = parede.bottom
                jogador.mov_y = 0
            if jogador.mov_y > 0:
                jogadorA.bottom = parede.top
                jogador.mov_y = 0

def mov_inimigo():

    if inimigo1.delay>=10:
        inimigo1.mover()
        inimigoA.x = inimigo1.x * 20
        inimigoA.y = inimigo1.y * 20
        inimigo2.mover()
        inimigoB.x = inimigo2.x * 20
        inimigoB.y = inimigo2.y * 20
        inimigo3.mover()
        inimigoC.x = inimigo3.x * 20
        inimigoC.y = inimigo3.y * 20
        inimigo4.mover()
        inimigoD.x = inimigo4.x * 20
        inimigoD.y = inimigo4.y * 20
        inimigo1.delay = 0
    inimigo1.delay+=1
    pygame.draw.rect(screen,(255,0,255), inimigoA)
    pygame.draw.rect(screen,(0,255,0), inimigoB)
    pygame.draw.rect(screen,(255,0,0), inimigoC)
    pygame.draw.rect(screen,(255,255,255), inimigoD)

def final():
    for inimigo in inimigos:
        if jogadorA.colliderect(inimigo):
            exit()
    if len(coordscomida)<=0:
        exit()


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((30,30,30))

    final()
    gerar_mapa()
    mover_jogador()
    pygame.draw.rect(screen,(255, 255, 0), jogadorA)
    gerar_comida()
    comer()
    mov_inimigo()

    

    pygame.display.update()
    clock.tick(60)