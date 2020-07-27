import pygame


from settings import *
from gameObject import GameObject
import math

vector = pygame.math.Vector2

class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.groups = game.sprites, game.players
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(DARKBLUE)
        self.rect = self.image.get_rect()
        self.velx = 0
        self.vely = 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.rotation = 0


    def getKeys(self):
        self.velx, self.vely = 0, 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.vely = -PLAYER_SPEED
            self.rotation = 90
        if keys[pygame.K_a]:
            self.velx = -PLAYER_SPEED
            self.rotation = 180
        if keys[pygame.K_s]:
            self.vely = PLAYER_SPEED
            self.rotation = 270
        if keys[pygame.K_d]:
            self.velx = PLAYER_SPEED
            self.rotation = 0

        if self.velx != 0 and self.vely != 0:
            self.velx *= 0.7071
            self.vely *= 0.7071


    def wallCollisionOld(self, dx, dy):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def wallCollision(self, direction):
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.velx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.velx < 0:
                    self.x = hits[0].rect.right
                self.velx = 0
                self.rect.x = self.x
        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vely > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vely < 0:
                    self.y = hits[0].rect.bottom
                self.vely = 0
                self.rect.y = self.y

    def rotateMouse(self):

        center = self.rect.center


        mousex, mousey = pygame.mouse.get_pos()
        relx, rely = mousex - self.rect.x, mousey - self.rect.y
        angle = (180 / math.pi) * -math.atan2(rely, relx)

        self.rotation = angle

        self.image = pygame.transform.rotate(self.image, self.rotation)

        self.rect = self.image.get_rect(center=center)


    def move(self, dx=0, dy=0):
        if not self.wallCollision(dx, dy):
            self.x = dx
            self.y = dy

    def update(self):
        self.getKeys()
        #self.rotateMouse()
        self.x += self.velx * self.game.fps / 1000
        self.y += self.vely * self.game.fps / 1000
        self.rect.x = self.x
        self.wallCollision('x')
        self.rect.y = self.y
        self.wallCollision('y')
