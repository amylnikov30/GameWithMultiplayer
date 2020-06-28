import pygame
import sys
import os

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

        window.blit(pygame.transform.rotate(self.mask, self.rotation), (self.x, self.y))

    
    def rotate(self, window, angle):
        #window.blit(pygame.transform.rotate(self.mask, angle), (self.x, self.y))

        self.rotation = angle

    
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

                        
                        



