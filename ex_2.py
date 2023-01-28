# как рандом сделать
import pygame

import random
pygame.init()
window  = pygame.display.set_mode((500, 500))
x = 500
y = 500
class Circles:
    def __init__(self , x, y):
        self.x=x
        self.y=y
    def draw(self,win):
        pg.draw.circle(win,(self.x, self.y):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        random(x,y)


    win.fill((255,255,255))


