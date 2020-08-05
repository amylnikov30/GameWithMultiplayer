import pygame
import os
import sys

from settings import *

vector = pygame.Vector2

class Bullet(pygame.sprite.Sprite):

    def __init__(self, game, pos, direction, shooter):
        self.game = game
        self.groups = self.game.sprites, self.game.bullets
        self.player = shooter
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = self.game.bulletImage
        self.rect = self.image.get_rect()
        self.pos = vector(pos)
        self.mesh = self.rect
        self.vel = direction * BULLET_VEL
        self.spawnTime = pygame.time.get_ticks()


    def rotate(self):
        self.image = pygame.transform.rotate(self.game.bulletImage, self.player.rotation)
        self.rect = self.image.get_rect(center = self.rect.center)

    def wallCollision(self):
        if pygame.sprite.spritecollide(self, self.game.walls, False):
            self.kill()


    def update(self):
        self.pos += self.vel * self.game.fps / 1000
        #self.rotate()
        self.mesh.center = self.pos
        self.wallCollision()
        if pygame.time.get_ticks() - self.spawnTime > BULLET_TRAVEL_TIME:
            self.kill()


class Item(pygame.sprite.Sprite):

    def __init__(self, game, name, pos):
        self.game = game
        self.groups = self.game.sprites, self.game.items
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = self.game.weaponModels[name]
        self.rect = self.image.get_rect(center=pos)
        self.type = self.getType(name)

    def getType(self, name):
        location = 0
        for char in range(len(name)):
            if name[char] == "_":
                splitChar = char

        type = ""
        for char in range(location):
            type += name[char]

        return type





class Rifle(pygame.sprite.Sprite):

    def __init__(self, user):

        self.user = user
        self.game = self.user.game
        self.groups = self.game.sprites, self.game.weapons