import pygame
from const import tam_bloco

class Jogador:

    def  __init__(self, vivo, x, y):
        self.vivo = vivo
        self.x = x
        self.y = y
        self.velocidade = 3
        self.mov_x = 0
        self.mov_y = 0

jogador = Jogador(True, 13, 17)
jogadorA = pygame.Rect(jogador.x * 20, jogador.y * 20, 18, 18)
