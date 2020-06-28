import pygame
import sys
import os

from player import Player
from gameObject import GameObject




class Game:


    def __init__(self, gamemode, id, player: Player):
        
        
        pygame.init()
        pygame.mouse.set_visible(False)

        self.cursor = pygame.image.load('resource/img/cursors/crosshair.png')


        self.gamemode = gamemode
        self.id = id
        self.player = player

        self.width = 1920
        self.height = 1080

        self.window = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

        self.bgColor = (0, 34, 64)

        #self.movmentx = 0
        #self.movmenty = 0

    
    def renderGO(self, go: GameObject):

        pygame.draw.rect(self.window, go.model, self.player)


    def renderText(self, fnt, what, color, where):
        "Renders the fonts as passed from display_fps"
        text_to_show = fnt.render(what, 0, pygame.Color(color))
        self.window.blit(text_to_show, where)

    def renderCursor(self):

        pos = pygame.mouse.get_pos()

        self.window.blit(self.cursor, pos)
        
        


    def displayFps(self):
        "Data that will be rendered and blitted in _display"
        self.renderText(
            pygame.font.SysFont("Arial", 25),
            what=str(int(self.clock.get_fps())),
            color="white",
            where=(10, 10))


    def renderModel(self, go, path):

        img = pygame.image.load(path).convert_alpha()
        self.window.blit(img, (go.x, go.y))

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
            fps = self.clock.tick(300)
            self.window.fill(self.bgColor)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                #for player in self.players:
                self.player.move(self.window, event)
                self.player.rotateMouse()
                #self.player.eventRotate(self.window, event)

            

            self.renderCursor()

            self.player.changePos(fps)
            

            self.player.stayInside(self.width, self.height)

            
            

            #pygame.draw.rect(self.window, (255, 0, 0), self.player)
            self.player.render(self.window)
            self.displayFps()
            pygame.display.update()
            #print(str(int(self.fps.get_fps())))
            #self.renderWindow()
            #self.clock.tick(200)

