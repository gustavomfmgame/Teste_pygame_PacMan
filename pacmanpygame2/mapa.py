from const import matriz, tam_bloco
import pygame

retangulos_paredes = []


for linha_idx, linha in enumerate(matriz):
    for coluna_idx, caractere in enumerate(linha):
        if caractere == '#':
            rect = pygame.Rect(coluna_idx * tam_bloco, linha_idx * tam_bloco, tam_bloco, tam_bloco)
            retangulos_paredes.append(rect)

