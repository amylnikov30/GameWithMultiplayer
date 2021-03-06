import pygame
import sys
from position import Position

class GameObject(pygame.Rect):

    def __init__(self, name, position, width, height, gotype):  #add model arg later
        self.name = name
        self.position = position
        self.width = width
        self.height = height
        self.gotype = gotype
        self.model = (255, 0, 0)
        #self.object = pygame.Rect(self.position.x, self.position.y, self.width, self.height)

        super().__init__(self.position.x, self.position.y, self.width, self.height)


    def render(self, window):
        pygame.draw.rect(window, self.model, (self.x, self.y, self.width, self.height)) 




class GameObject2(pygame.sprite.Sprite):

    def __init__(self):

        self.model = pygame.Surface((50, 50))
        self.model.fill((0, 255, 0)) 
        self.mesh = self.model.get_rect()

        super().__init__(self)

    
    