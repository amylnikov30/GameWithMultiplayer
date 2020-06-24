import pygame
import sys
import os
import Button
from Direction import Direction
import configparser


class Game:
    

    def __init__(self, width, height):
        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        self.vel = 5
        self.clock = pygame.time.Clock()
        self.config = configparser.ConfigParser()


    def controls(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pass
            if event.type == pygame.KEYUP:
                pass



    def driver(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.controls()
