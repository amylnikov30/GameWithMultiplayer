import pygame


from settings import *
from gameObject import GameObject
from weapons import Bullet
import math
from map import meshCollision
import time

vector = pygame.math.Vector2

class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.groups = game.sprites, game.players
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.name = "TestPlayer"
        self.image = self.game.playerMask
        #self.image.fill(DARKBLUE)
        self.rect = self.image.get_rect(center=(x, y))
        # self.velx = 0
        # self.vely = 0
        self.vel = vector(0, 0)
        self.pos = vector(x, y)
        self.renderPos = vector(x, y)
        self.mesh = PLAYER_MESH
        self.mesh.center = self.rect.center
        # self.x = x * TILESIZE
        # self.y = y * TILESIZE
        self.rotation = 0
        self.lastShot = 0
        self.health = 100
        self.items = []
        self.currentItem = None
        self.lastItemDropped = 0

    def collideRect(self, first, second):
        first.rect.collide_rect(second.rect)


    def slide(self):
        direction = vector(1, 0).rotate(-self.rotation)
        vel = direction * SLIDING_VEL

        self.pos += vel

        self.wallCollision('x')
        self.wallCollision('y')


    def pickupItems(self):
        for item in self.game.items:
            distance = self.pos - item.pos
            now = pygame.time.get_ticks()
            if distance.length() <= item.pickupRad and self.currentItem == None and now - self.lastItemDropped > 700:
                item.pickup(self)


    def throwItems(self):
        self.lastItemDropped = pygame.time.get_ticks()
        if self.currentItem != None:
            self.currentItem.throw()


    def getPos(self):
        return self.pos

    def walkingAnim(self):
        walkingImage = pygame.image.load(os.path.join(MASKS, 'jacketWalking.png'))


    def getKeys(self):
        self.vel = vector(0, 0)
        keys = pygame.key.get_pressed()


        # for event in pygame.event.get():
        #     if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
        #         now = pygame.time.get_ticks()
        #         if now - self.lastShot > FIRERATE:
        #             self.lastShot = now
        #             direction = vector(1, 0).rotate(-self.rotation)
        #             Bullet(self.game, self.pos, direction, self)
        #             #print("[PLAYER] Bullet fired")

        mouse = pygame.mouse.get_pressed()

        if mouse[0]: #left-click
            if self.currentItem != None:
                now = pygame.time.get_ticks()
                if now - self.lastShot > self.currentItem.firerate and self.currentItem.ammo[0] > 0 and now - self.currentItem.lastReload > self.currentItem.reloadTime:
                    self.lastShot = now
                    direction = vector(1, 0).rotate(-self.rotation)
                    Bullet(self.game, self.pos, direction, self)
                    self.currentItem.ammo[0] -= 1
                    #pygame.time.wait(self.currentItem.firerate)
        if mouse[2]: #right-click
            if self.currentItem != None:
                self.currentItem.throw()
                #print("[PLAYER] Bullet fired")
        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:# and event.type == pygame.KEYUP:
        #         if event.key == pygame.K_e:
        #             for item in self.game.items:
        #                 distance = self.pos - item.pos
        #                 if distance.length() <= item.pickupRad and self.currentItem == None:
        #                     item.pickup(self)
        #                 else:
        #                     item.drop()
        #                     self.currentItem = None
        if keys[pygame.K_w]:
            self.vel.y = -PLAYER_SPEED
            #self.rotation = 90
        if keys[pygame.K_a]:
            self.vel.x = -PLAYER_SPEED
            #self.rotation = 180
        if keys[pygame.K_s]:
            self.vel.y = PLAYER_SPEED
            #self.rotation = 270
        if keys[pygame.K_d]:
            self.vel.x = PLAYER_SPEED
            #self.rotation = 0
        if keys[pygame.K_r]:
            if self.currentItem != None:
                self.currentItem.reload()
        if keys[pygame.K_c]:
            pass #self.slide()
        if keys[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if now - self.lastShot > FIRERATE:
                self.lastShot = now
                direction = vector(1, 0).rotate(-self.rotation)
                Bullet(self.game, self.pos, direction, self)
                #print("[PLAYER] Bullet fired")

        if keys[pygame.K_LSHIFT]:
            if keys[pygame.K_w]:
                self.vel.y = -WALKING_SPEED
                #self.rotation = 90
            if keys[pygame.K_a]:
                self.vel.x = -WALKING_SPEED
                #self.rotation = 180
            if keys[pygame.K_s]:
                self.vel.y = WALKING_SPEED
                #self.rotation = 270
            if keys[pygame.K_d]:
                self.vel.x = WALKING_SPEED
                #self.rotation = 0

        if keys[pygame.K_LCTRL]:
            if keys[pygame.K_w]:
                self.vel.y = -DUCKING_SPEED
                #self.rotation = 90
            if keys[pygame.K_a]:
                self.vel.x = -DUCKING_SPEED
                #self.rotation = 180
            if keys[pygame.K_s]:
                self.vel.y = DUCKING_SPEED
                #self.rotation = 270
            if keys[pygame.K_d]:
                self.vel.x = DUCKING_SPEED
                #self.rotation = 0


        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071


    def wallCollisionOld(self, dx, dy):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def wallCollision(self, direction):
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False, meshCollision)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.mesh.width / 2
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right + self.mesh.width / 2
                self.vel.x = 0
                self.mesh.centerx = self.pos.x
        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False, meshCollision)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.mesh.height / 2
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom + self.mesh.height / 2
                self.vel.y = 0
                self.mesh.centery = self.pos.y

    def rotate(self):
        if self.rotation == 90 or self.rotation == 270:
            self.image = pygame.Surface((40, 30))
            self.rect = self.image.get_rect()
        elif self.rotation == 0 or self.rotation == 180:
            self.image = pygame.Surface((30, 40))
            self.rect = self.image.get_rect()

    def rotateMouse(self):

        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - WIDTH/2, mouse_y - HEIGHT/2
        angle = math.degrees(-math.atan2(rel_y, rel_x))

        self.rotation = angle

    def move(self, dx=0, dy=0):
        if not self.wallCollision(dx, dy):
            self.x = dx
            self.y = dy

    def update(self):
        #self.rect = self.image.get_rect()
        center = self.rect.center
        self.getKeys()
        self.pickupItems()
        self.rotateMouse()
        self.image = pygame.transform.rotate(pygame.transform.scale(self.game.playerMask, (TILESIZE, TILESIZE)), self.rotation)
        self.rect = self.image.get_rect(center=center)
        #self.mesh = self.image.get_rect(center=center)
        self.rect.center = self.pos
        self.pos += self.vel * self.game.fps / 1000
        self.renderPos.x = self.pos.x
        self.mesh.centerx = self.pos.x
        self.wallCollision('x')
        self.renderPos.y = self.pos.y
        self.mesh.centery = self.pos.y
        self.wallCollision('y')
        self.rect.center = self.mesh.center
        if self.health < 0:
            self.kill()
        #self.pos = self.mesh.center

        #self.game.window.blit(self.image, self.game.camera.apply(self)
