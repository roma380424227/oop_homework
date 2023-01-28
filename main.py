#хз как это делать
import random

import pygame
W = 700
H = 700
pygame.init()
window = pygame.display.set_mode(W, H)

Class Circle:
    def __init__(self, x, y, i):
         self.x = x
         self.y = y
         self.i = i


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
list_circles = []
for i in range(100):
    list_circles.append(Circle(i* 10,i*5,30,random.choice(range(256),k=3)))
    def horizontal_movement(self):
        if self.dir =='right':
            self.x-= 1
            if self.dir == 'left':
        else:
            self.x -=1
            if self.x<0:
                self.dir = 'right'






