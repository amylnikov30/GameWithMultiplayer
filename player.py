import pygame
import sys
import os

from gameObject import GameObject
from position import Position
from typeEnums import GameObjectType



class Player(GameObject):

    def __init__(self, name, position, health, armor):
        self.name = name
        self.position = position
        self.health = health
        self.armor = armor
        self.type = GameObjectType.player
        self.vel = 7
        self.movementx = 0
        self.movementy = 0
        

        super().__init__(self.name, self.position, 30, 30, type)


    
    def stayInside(self):
        if self.top <= 0:
            self.top = 0
        if self.bottom >= self.height:
            self.bottom = self.height
        if self.right >= self.width:
            self.right = self.width
        if self.left <= 0:
            self.left = 0           


    def move(self, event):
        #for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            if event.key == ord("s"):
                self.movementy += self.vel
            if event.key == pygame.K_a:
                self.movementx -= self.vel
            if event.key == pygame.K_d:
                self.movementx += self.vel
            if event.key == pygame.K_w:
                self.movementy -= self.vel
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                self.movementy -= self.vel
            if event.key == pygame.K_a:
                self.movementx += self.vel
            if event.key == pygame.K_d:
                self.movementx -= self.vel
            if event.key == pygame.K_w:
                self.movementy += self.vel


    def changePos(self):

        self.x += self.movementx
        self.y += self.movementy

        print("self.top: " + str(self.top))

                        
                        



