import pygame
import os
import sys

from settings import *
from enums import *
from map import meshCollision
from menu import *
#from player import Player

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
        self.groups = self.game.items, self.game.sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        x = pos[0]
        y = pos[1]
        self.pos = vector(x, y)
        #self.originalImage = self.game.weaponModels[name]
        self.image = self.game.weaponModels[name]
        self.rect = self.image.get_rect(center=pos)
        self.mesh = self.rect
        self.type = self.getType(name)
        self.pickupRad = 32  #pixels
        self.user = None
        self.name = name
        self.render = True
        self.firerate = 100   #place holder until individual weapons are added
        self.rotation = 0
        currentMagazine = 30
        magazines = 4
        magazineCapacity = 30
        total = 120
        self.ammo = {"currentMagazine":currentMagazine, "total":total, "magazines":magazines, "magazineCapacity":magazineCapacity}
        self.reloadTime = 1000
        self.lastReload = 0


    def reloadingBar(self):
        now = pygame.time.get_ticks()
        progress = 1
        coefficient = 120 / self.reloadTime
        time = 0

        if now - self.lastReload < self.reloadTime:
            if time < self.reloadTime:
                time += self.game.fps / 1000

                width = time * coefficient

                pygame.draw.rect(self.game.window, ORANGE, (900, 300, width, 30))




    def wallCollision(self, targetDir):

        hits = pygame.sprite.spritecollide(self, self.game.walls, False, meshCollision)

        if hits:
            self.pos = self.user.pos + 48 * (-targetDir)



    def pickup(self, player):
        # distance = player.pos - self.pos
        # if distance.length() <= self.pickupRad:
        if self.user == None:
            self.user = player
            print(f"Player {self.user.name} has picked up {self.name}")
            self.user.currentItem = self
            self.render = False
            self.lastReload -= self.reloadTime
        #self.pickupRad = 0
        # else:
        #     self.drop()

    def reload(self):
        now = pygame.time.get_ticks()
        if now - self.lastReload > self.reloadTime:
            if self.ammo["total"] > 0 and self.ammo["total"] <= self.ammo["magazineCapacity"]:
                self.ammo["currentMagazine"] += self.ammo["total"]; self.ammo["total"] = 0

            elif self.ammo["total"] > self.ammo["magazineCapacity"]:
                preReload = self.ammo["currentMagazine"]
                self.ammo["currentMagazine"] = self.ammo["magazineCapacity"]; self.ammo["total"] -= (self.ammo["magazineCapacity"] - preReload)


        self.lastReload = now
    def throwAnimation(self, direction):
        targetPos = self.user.pos + 48 * direction
        vel = direction * THROWING_VEL
        self.pos += vel * self.game.fps / 1000
        self.wallCollisionPlayer('x', vel)
        self.wallCollisionPlayer('y', vel)

    def animations(self):
        pass

    def throw(self):
        direction = vector(1, 0).rotate(-self.user.rotation)
        vel = direction * THROWING_VEL

        print(f"Player {self.user.name} has dropped {self.name}")

        self.pos = self.user.pos + 48 * direction
        self.mesh.center = self.pos
        if self.wallCollision(direction):
            self.pos = self.user.pos + 48 * (-direction)

        # self.wallCollision('x')
        # self.wallCollision('y')
        #self.throwAnimation(direction)
        self.user.currentItem = None
        self.user = None
        #self.image = self.originalImage
        self.render = True



        #self.pickupRad = 32


    def getType(self, name):
        location = 0
        for char in range(len(name)):
            if name[char] == "_":
                splitChar = char

        type = ""
        for char in range(location):
            type += name[char]

        return type

    def rotate(self):
        left = self.rect.left
        ogImage = self.image
        self.image = pygame.transform.rotate(ogImage, self.user.rotation)
        self.rect = self.image.get_rect(left=left)


    def update(self):
        if self.user != None:
            self.pos.x = self.user.pos.x
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
            self.mesh.center = self.pos
            #self.rotate()
        #self.image = self.originalImage

        self.image = pygame.transform.rotate(self.game.weaponModels[self.name], self.rotation)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.mesh.center = self.pos








class Rifle(pygame.sprite.Sprite):

    def __init__(self, user):

        self.user = user
        self.game = self.user.game
        self.groups = self.game.sprites, self.game.weapons
