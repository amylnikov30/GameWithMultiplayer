import pygame
import sys
import os

from GameObject import GameObject
from Position import Position
from Types import GameObjectType



class Player(GameObject):

    def __init__(self, name, position, health, armor):
        self.name = name
        self.position = position
        self.health = health
        self.armor = armor
        self.type = GameObjectType.player
        self.vel = 7
        

        super().__init__(self.name, self.position, type)


        def movement(self):

            #code is also in Game.py but I think it makes more sense to put it in here just for the player class.

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if pygame.key == pygame.K_w:
                        self.position.y -= self.vel
                    if pygame.key == pygame.K_a:
                        self.position.x -= self.vel
                    if pygame.key == pygame.K_s:
                        self.position.y += self.vel
                    if pygame.key == pygame.K_d:
                        self.position.x += self.vel
                
                if event.type == pygame.KEYUP:

                    if pygame.key == pygame.K_w:
                        self.position.y += self.vel
                    if pygame.key == pygame.K_a:
                        self.position.x += self.vel
                    if pygame.key == pygame.K_s:
                        self.position.y -= self.vel
                    if pygame.key == pygame.K_d:
                        self.position.x -= self.vel
                        
                        



