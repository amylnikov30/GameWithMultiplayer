import pygame
import sys
import os
import math

from gameObject import GameObject
from position import Position
from typeEnums import GameObjectType


pygame.init()



class Player(GameObject):

    def __init__(self, name, position, health, armor, mask):
        self.name = name
        self.position = position
        self.health = health
        self.armor = armor
        self.type = GameObjectType.player
        self.vel = 2
        self.mask = f'resource/img/models/masks/{mask}.png'
        self.rotation = 0
        self.movementx = 0
        self.movementy = 0
        

        super().__init__(self.name, self.position, 83, 144, type)

    
    def load(self):
        #print(self.mask)
        self.mask = pygame.image.load(self.mask)

    
    def render(self, window):
        #print(self.x)
        #print(self.y)

        img = pygame.transform.rotate(self.mask, self.rotation)

        window.blit(img, (self.x - int(img.get_width()/2), self.y - int(img.get_height()/2)))

    
    def rotate(self, window, angle):
        #window.blit(pygame.transform.rotate(self.mask, angle), (self.x, self.y))

        

        self.rotation = angle

    def rotateMouse(self):

        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        
        self.rotation = angle
        
        
        #self.image = pygame.transform.rotate(self.mask, int(angle))
        #self.rect = self.image.get_rect(center=self.position)    
             

    
    def eventRotate(self, window, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                #self.movementy += self.vel
                self.rotate(window, 270)
            if event.key == pygame.K_a:
                #self.movementx -= self.vel
                self.rotate(window, 180)
            if event.key == pygame.K_d:
                #self.movementx += self.vel
                self.rotate(window, 0)
            if event.key == pygame.K_w:
                #self.movementy -= self.vel
                self.rotate(window, 90)



    
    def stayInside(self, width, height):
        if self.top <= 0:
            self.top = 0
        if self.bottom >= height:
            self.bottom = height
        if self.right >= width:
            self.right = width
        if self.left <= 0:
            self.left = 0           


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



    def changePos(self, fpsMultiplier):

        self.x += self.movementx * fpsMultiplier
        self.y += self.movementy * fpsMultiplier

        #print("self.top: " + str(self.top))

                        
                        



