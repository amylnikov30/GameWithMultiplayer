import pygame

from settings import *



class GameObject(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.groups = game.sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.model = pg.Surface((TILESIZE, TILESIZE))
        self.model.fill(RED)
        self.mesh = self.image.get_rect()


    def update(self):
        self.mesh.x = self.x * TILESIZE
        self.mesh.y = self.y * TILESIZE
