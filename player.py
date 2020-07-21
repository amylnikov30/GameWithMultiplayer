import pygame


from settings import *
from gameObject import GameObject



class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.groups = game.sprites, game.players
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def wallCollision(self, dx, dy):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def move(self, dx=0, dy=0):
        if not self.wallCollision(dx, dy):
            self.x += dx
            self.y += dy

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
