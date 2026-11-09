import random
from collections import deque
from const import matriz

class Inimigos:

    def __init__(self, vivo, x, y):
        self.vivo = vivo
        self.x = x
        self.y = y
        self.visitados = deque()
        self.delay = 0

    def mover(self):
        caminhos = []
        self.visitados.append((self.x, self.y))

        if matriz[self.y+1][self.x] != '#' and (self.x, self.y+1) not in self.visitados:
            caminhos.append((self.x, self.y+1))
        if matriz[self.y-1][self.x] != '#' and (self.x, self.y-1) not in self.visitados:
            caminhos.append((self.x, self.y-1))
        if matriz[self.y][self.x+1] != '#' and (self.x+1, self.y) not in self.visitados:
            caminhos.append((self.x+1, self.y))
        if matriz[self.y][self.x-1] != '#' and (self.x-1, self.y) not in self.visitados:
            caminhos.append((self.x-1, self.y))

        if len(self.visitados) >= 3:
            self.visitados.popleft()

        if caminhos:
            (self.x, self.y) = random.choice(caminhos)

inimigo1 = Inimigos(True, 12, 14)
inimigo2 = Inimigos(True, 13, 14)
inimigo3 = Inimigos(True, 14, 14)
inimigo4 = Inimigos(True, 15, 14)

if __name__=='__main__':
    print()