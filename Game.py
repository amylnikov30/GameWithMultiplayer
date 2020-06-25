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
        self.controls = {"movement" : {"forward":pygame.K_w, "left":pygame.K_a, "backward":pygame.K_s, "right":pygame.K_d}}


    def controls(self):
        movement = self.controls["movement"]
        for event in pygame.event.get():

            #On Key Down
            if event.type == pygame.KEYDOWN:
                if event.key == ord(movement["forward"]):
                    pass
                if event.key == ord(movement["left"]):
                    pass
                if event.key == ord(movement["backward"]):
                    pass
                if event.key == ord(movement["right"]):
                    pass
            
            #On Key Up
            if event.type == pygame.KEYUP:
                if event.key == ord(movement["forward"]):
                    pass
                if event.key == ord(movement["left"]):
                    pass
                if event.key == ord(movement["backward"]):
                    pass
                if event.key == ord(movement["right"]):
                    pass

    
    def setControls(self, cfg):

        self.config.read(".\\resource\\cfg\\cfg")

        movement = self.controls["movement"]

        for i in movement:
            movement[i] = self.config.get("movement", i)


    def movement(self):  #add more args
        pass


    def driver(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.controls()
