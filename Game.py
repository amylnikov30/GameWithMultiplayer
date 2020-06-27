import pygame
import sys
import os

from player import Player
from gameObject import GameObject




class Game:


    def __init__(self, gamemode, id, player: Player):
        self.gamemode = gamemode
        self.id = id
        self.player = player

        self.width = 500
        self.height = 500

        self.window = pygame.display.set_mode((self.width, self.height))
        self.fps = pygame.time.Clock()

        self.bgColor = (0, 34, 64)

        #self.movmentx = 0
        #self.movmenty = 0

    
    def renderGO(self, go: GameObject):

        pygame.draw.rect(self.window, go.model, self.player)
    

    def renderWindow(self):

        self.window.fill(self.bgColor)
        #for player in self.players:
        self.player.render(self.window)
        pygame.display.update()



    def move(self, player: Player):

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == ord("w"):
                    player.position.y -= player.vel
                if event.key == ord("a"):
                    player.position.x -= player.vel
                if event.key == ord("s"):
                    player.position.y += player.vel
                if event.key == ord("d"):
                    player.position.x += player.vel


            if event.type == pygame.KEYUP:
                if event.key == ord("w"):
                    player.position.y += player.vel
                if event.key == ord("a"):
                    player.position.x += player.vel
                if event.key == ord("s"):
                    player.position.y -= player.vel
                if event.key == ord("d"):
                    player.position.x -= player.vel

        
    def move2(self, player, event):
        #for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                self.player.movementy -= player.vel
            if event.key == pygame.K_a:
                self.player.movementx -= player.vel
            if event.key == pygame.K_s:
                self.player.movementy += player.vel
            if event.key == pygame.K_d:
                self.player.movementx += player.vel


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.player.movementy += player.vel
            if event.key == pygame.K_a:
                self.player.movementx += player.vel
            if event.key == pygame.K_s:
                self.player.movementy -= player.vel
            if event.key == pygame.K_d:
                self.player.movementx -= player.vel

    
    def stayInside(self):
        if self.player.top <= 0:
            self.player.top = 0
        if self.player.bottom >= self.height:
            self.player.bottom = self.height
        if self.player.right >= self.width:
            self.player.right = self.width
        if self.player.left <= 0:
            self.player.left = 0   



    def run(self):

        while True:
            self.window.fill(self.bgColor)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #for player in self.players:
                self.player.move(event)
            
            #self.player.x += self.player.movementx
            #self.player.y += self.player.movementy
            #print("movementx: " + str(self.player.movementx))
            #print("movementy: " + str(self.player.movementy))

            self.stayInside()

            self.player.changePos()
            

            pygame.draw.rect(self.window, (255, 0, 0), self.player)
            pygame.display.update()
            #self.renderWindow()
            self.fps.tick(200)

