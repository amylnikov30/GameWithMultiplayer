import pygame
import sys
import os

from settings import *
from player import Player
from map import *
from network import Network

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Hotline Miami 2020 Rework")
        self.clock = pygame.time.Clock()
        #self.id = id
        self.ready = False
        self.sprites = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.map = Map("importedMap")

        #self.loadData()

        #def loadData(self):
            #pass

    def loadData(self):
        root = os.path.dirname(__file__)
        mapFolder = os.path.join(root, 'maps')
        self.map = []
        mapFile = open(os.path.join(root, 'testMap0.txt'), 'rt')
        for line in mapFile:
            self.map.append(line)


    def loadMap(self):
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == 'W':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)



    def renderText(self, font, what, color, where):
        text_to_show = font.render(what, 0, pygame.Color(color))
        self.window.blit(text_to_show, where)


    def displayFps(self):
        self.renderText(
            pygame.font.SysFont("Courier", 25),
            what=str(int(self.clock.get_fps())),
            color="white",
            where=(15, 15))


    def new(self):
        self.sprites = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        #self.player = Player(self, 5, 5)

        self.loadMap()
        self.camera = Camera(self.map.width, self.map.height)

        #self.player1 = Player(self, 5, 5)
        #self.player2 = Player(self, 10, 10)
        #self.networkPlayers = [Player]
        #self.networkPlayers.append(self.player1); self.networkPlayers.append(self.player2)


        # for x in range(5, 15):
        #     Wall(self, x, 15)

    def update(self):
        self.sprites.update()
        self.camera.update(self.player)


    def network(self):
        self.network = Network()
        self.p = self.network.getId()


    def run(self):
        #self.player1 = self.network.getId()
        while True:
            #self.p2 = self.network.send(self.p)
            #self.player2 = self.network.send(self.player1)
            self.fps = self.clock.tick(300)
            self.events()
            self.update()
            self.render()



    def quit(self):
        pygame.quit()
        sys.exit()

    def drawGrid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.window, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.window, LIGHTGREY, (0, y), (WIDTH, y))

    def render(self):
        self.window.fill(BGCOLOR)
        self.drawGrid()
        #self.sprites.draw(self.window)

        for sprite in self.sprites:
            self.window.blit(sprite.image, self.camera.apply(sprite))

        # for i in self.networkPlayers:
        #     i.update()
        #     i.draw()
        self.displayFps()
        pygame.display.update()


    def events2(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.quit()



            if event.type == pygame.KEYDOWN:

                if pygame.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if pygame.key == pygame.K_w:
                    self.players.movementy -= self.player.vel
                if pygame.key == pygame.K_a:
                    self.players.movementx -= self.player.vel
                if pygame.key == pygame.K_s:
                    self.players.movementy += self.player.vel
                if pygame.key == pygame.K_d:
                    self.players.movementx += self.player.vel

            elif event.type == pygame.KEYUP:
                if pygame.key == pygame.K_w:
                    self.players.movementy += self.player.vel
                if pygame.key == pygame.K_a:
                    self.players.movementx += self.player.vel
                if pygame.key == pygame.K_s:
                    self.players.movementy -= self.player.vel
                if pygame.key == pygame.K_d:
                    self.players.movementx -= self.player.vel


    def player(self):
        pass

    def connected(self):
        return self.ready




    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
            #     if event.key == pygame.K_a:
            #         self.player.move(dx=-1)
            #         #return -1
            #     if event.key == pygame.K_d:
            #         self.player.move(dx=1)
            #         #return 1
            #     if event.key == pygame.K_w:
            #         self.player.move(dy=-1)
            #     if event.key == pygame.K_s:
            #         self.player.move(dy=1)
