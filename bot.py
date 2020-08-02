import pygame

from settings import *
from map import meshCollision



vector = pygame.Vector2

class Bot(pygame.sprite.Sprite):

    def __init__(self, game, pos):
        self.game = game
        self.pos = vector(pos)
        self.groups = self.game.sprites, self.game.bots
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.health = 100
        self.image = self.game.botImage
        self.rect = self.image.get_rect()
        self.mesh = PLAYER_MESH
        self.mesh.center = self.rect.center
        self.rect.center = self.pos
        self.vel = vector(0, 0)
        self.accel = vector(0, 0)
        self.rotation = 0


    def wallCollision(self, group, direction):
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, group, False, meshCollision)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.mesh.width / 2
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right + self.mesh.width / 2
                self.vel.x = 0
                self.mesh.centerx = self.pos.x
        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, group, False, meshCollision)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.mesh.height / 2
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom + self.mesh.height / 2
                self.vel.y = 0
                self.mesh.centery = self.pos.y


    def update(self):
        self.rotation = (self.game.player.pos - self.pos).angle_to(vector(1, 0))
        self.image = pygame.transform.rotate(self.game.botImage, self.rotation)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        # self.accel = vector(PLAYER_SPEED, 0).rotate(-self.rotation)
        # self.accel += self.vel * -1
        # self.vel += self.accel * self.game.fps / 1000
        # self.pos += self.vel * (self.game.fps / 1000) + 0.5 * self.accel * (self.game.fps / 1000) ** 2
        # self.mesh.centerx = self.pos.x
        # self.wallCollision(self.game.walls, 'x')
        # self.wallCollision(self.game.players, 'x')
        self.mesh.centery = self.pos.y
        # self.wallCollision(self.game.walls, 'y')
        # self.wallCollision(self.game.players, 'y')
        self.rect.center = self.mesh.center
        if self.health <= 0:
            self.kill()
