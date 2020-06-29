import pygame
import sys
import os
import math

#from gameObject import GameObject
#from gameObject import GameObject2
from position import Position
from typeEnums import GameObjectType


pygame.init()



class Player(pygame.sprite.Sprite):

    def __init__(self, name, position, health, armor, mask):
        self.name = name
        self.position = position
        self.health = health
        self.armor = armor
        self.type = GameObjectType.player
        self.vel = 2
        self.width = 83
        self.height = 144
        self.mask = f'resource/img/models/masks/{mask}.png'
        #self.mask = pygame.Surface((self.width, self.height))
        self.mesh = None
        self.rotation = 0
        self.movementx = 0
        self.movementy = 0
        #self.mesh = pygame.Rect(self.left, self.top, self.width, self.height)
        

        #super().__init__(self.name, self.position, self.width, self.height, type)
        #super().__init__(self)
        pygame.sprite.Sprite.__init__(self)
    
    def load(self):
        #print(self.mask)
        self.mask = pygame.image.load(self.mask)
        self.mesh = self.mask.get_rect()

    
    def render(self, window):
        #print(self.x)
        #print(self.y)

        center = self.mesh.center

        img = pygame.transform.rotate(self.mask, self.rotation)


        #pygame.draw.rect(window, (255, 0, 0), self.mesh) #drawing the mesh

        self.mesh = img.get_rect(center=center)
        

        window.blit(img, self.mesh)

        
        
        #window.blit(pygame.transform.rotate(self.mask, self.rotation), (self.x, self.y))

    
    def rotate(self, window, angle):
        #window.blit(pygame.transform.rotate(self.mask, angle), (self.x, self.y))

        

        self.rotation = angle

    def rotateMouse(self):

        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.mesh.x, mouse_y - self.mesh.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        
        self.rotation = angle
        
        
        #self.image = pygame.transform.rotate(self.mask, int(angle))
        #self.rect = self.image.get_rect(center=self.position)    
             

    
    def eventRotate(self, window, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                self.movementy += self.vel
                self.rotate(window, 270)
            if event.key == pygame.K_a:
                self.movementx -= self.vel
                self.rotate(window, 180)
            if event.key == pygame.K_d:
                self.movementx += self.vel
                self.rotate(window, 0)
            if event.key == pygame.K_w:
                self.movementy -= self.vel
                self.rotate(window, 90)



    
    def stayInside(self, width, height):
        if self.mesh.top <= 0:
            self.mesh.top = 0
        if self.mesh.bottom >= height:
            self.mesh.bottom = height
        if self.mesh.right >= width:
            self.mesh.right = width
        if self.mesh.left <= 0:
            self.mesh.left = 0           


    def move(self, window, event):
        #for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                self.movementy += self.vel
                self.rotate(window, 270)
            if event.key == pygame.K_a:
                self.movementx -= self.vel
                self.rotate(window, 180)
            if event.key == pygame.K_d:
                self.movementx += self.vel
                self.rotate(window, 0)
            if event.key == pygame.K_w:
                self.movementy -= self.vel
                self.rotate(window, 90)

        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                self.movementy -= self.vel
            if event.key == pygame.K_a:
                self.movementx += self.vel
            if event.key == pygame.K_d:
                self.movementx -= self.vel
            if event.key == pygame.K_w:
                self.movementy += self.vel

        #print(f"x: {self.movementx}; y: {self.movementy}")



    def changePos(self, fpsMultiplier):

        self.mesh.x += self.movementx * fpsMultiplier
        self.mesh.y += self.movementy * fpsMultiplier

        #self.mask.left += self.movementx * fpsMultiplier
        #self.mask.left += self.movementy * fpsMultiplier


        #print(f"x: {self.mesh.x}; y: {self.mesh.y}")
        #print("self.top: " + str(self.top))



    def update(self):
        #self.mesh.x += self.movementx
        pass

                        
                        



