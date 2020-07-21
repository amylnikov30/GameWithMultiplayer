import pygame
import sys
import os


from settings import *


class Map:

    def __init__(self):
        pass


class Wall(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.groups = game.sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(LIGHTGREY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
