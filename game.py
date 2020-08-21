import pygame
import sys
import os

from settings import *
from player import Player
from map import *
from network import Network
from bot import Bot
from weapons import *

class Game:

    def __init__(self):
        pygame.init()
        setMode()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        #self.id = id
        self.ready = False
        self.sprites = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.renderClipBrushesFlag = False


        self.loadData()

        #def loadData(self):
            #pass

    def loadData(self):
        # root = os.path.dirname(__file__)
        # mapFolder = os.path.join(root, 'maps')
        # self.map = []
        # mapFile = open(os.path.join(root, 'testMap0.txt'), 'rt')
        #  for line in mapFile:
        #      self.map.append(line)


        root = os.path.dirname(__file__)
        maps = os.path.join(root, 'maps')
        resource = os.path.join(root, 'resource')
        img = os.path.join(resource, 'img')

        pygame.mouse.set_visible(False)

        self.map = TiledMap('shipment')

        self.mapSurface = self.map.makeMap()
        self.mapRect = self.mapSurface.get_rect()

        models = os.path.join(img, 'models')
        masks = os.path.join(models, 'masks')
        textures = os.path.join(img, 'textures')
        doors = os.path.join(textures, 'doors')
        cursors = os.path.join(img, 'cursors')
        weapons = os.path.join(models, 'weapons')

        self.playerMask = pygame.image.load(os.path.join(masks, 'charlie.png')).convert_alpha()
        #pygame.transform.scale(self.playerMask, (TILESIZE, TILESIZE))
        self.mapImage = pygame.image.load(os.path.join(doors, 'door16.png')).convert_alpha()
        self.crosshair = pygame.image.load(os.path.join(cursors, 'crosshair.png')).convert_alpha()
        self.bulletImage = pygame.image.load(os.path.join(weapons, 'bullet.png')).convert_alpha()
        self.botImage = pygame.image.load(os.path.join(masks, 'manBlue_gun.png')).convert_alpha()
        #self.weapon_m4a1 = pygame.image.load(os.path.join(weapons, 'm4a1.png'))
        self.weaponModels = {}
        for modelname in RIFLES:
            self.weaponModels[modelname] = pygame.image.load(os.path.join(weapons, RIFLES[modelname])).convert_alpha()
        #



    def loadMap(self):
        # for row, tiles in enumerate(self.map.data):
        #     for col, tile in enumerate(tiles):
        #         if tile == 'W':
        #             Wall(self, col, row)
        #         if tile == 'P':
        #             self.player = Player(self, col, row)
        for tileObject in self.map.tmx.objects:
            center = vector(tileObject.x + tileObject.width / 2, tileObject.y + tileObject.height / 2)
            if tileObject.name == "playerSpawn":
                self.player = Player(self, center.x, center.y)
                self.camera = Camera(self.map.width, self.map.height)
            if tileObject.name == "botSpawn":
                Bot(self, center)
            if tileObject.name == "wall":
                Obstacle(self, tileObject.x, tileObject.y, tileObject.width, tileObject.height)
            if tileObject.type == "item":
                Item(self, tileObject.name, center)

    def loadMapLegacy(self):
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == 'W':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)

    def renderClipBrushes(self):
        for wall in self.walls:
            self.window.blit(wall.image, self.camera.apply(wall))

        pygame.draw.rect(self.playerMask, RED, self.camera.applyRect(self.player.mesh), 1)


    def renderCursor(self):

        pos = pygame.mouse.get_pos()

        self.window.blit(self.crosshair, pos)


    def renderText(self, font, what, color, where):
        text_to_show = font.render(what, 0, pygame.Color(color))
        self.window.blit(text_to_show, where)


    def displayFps(self):
        self.renderText(
            pygame.font.SysFont("Modern Warfare", 30),
            what=str(int(self.clock.get_fps())),
            color="white",
            where=(15, 15))


    def new(self):
        self.sprites = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.bots = pygame.sprite.Group()
        self.windows = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.weapons = pygame.sprite.Group()

        #self.player = Player(self, 5, 5)

        self.loadMap()
        #self.camera = Camera(self.map.width, self.map.height)


    def update(self):
        self.sprites.update()
        self.items.update()
        self.camera.update(self.player)

        botHits = pygame.sprite.groupcollide(self.bots, self.bullets, False, True)
        for hit in botHits:
            hit.health -= BULLET_DAMAGE


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

        self.window.blit(self.mapSurface, self.camera.applyRect(self.mapRect))


        for sprite in self.sprites:
            #self.camera.apply(sprite)
            if not isinstance(sprite, Item):
                self.window.blit(sprite.image, self.camera.apply(sprite))

        # for player in self.players:
        #     self.window.blit(player.image, self.camera.apply(player))

        for item in self.items:
            if item.render:
                self.window.blit(item.image, self.camera.apply(item))

        if self.renderClipBrushesFlag:
            self.renderClipBrushes()
            #pygame.draw.rect(self.window, RED, sprite, 2)
        for bot in self.bots:
            pygame.draw.rect(self.window, RED, self.camera.applyRect(bot.mesh), 2)
        #
        # for player in self.players:
        #     #self.camera.apply(player)
        #     self.window.blit(player.image, self.camera.apply(player))
        #     pygame.draw.rect(self.window, DARKBLUE, player.mesh)

        self.renderText(pygame.font.SysFont('Modern Warfare', 30), f"Bots remainaining: {len(self.bots)}", "white", (45, 45))
        self.renderText(pygame.font.SysFont('Modern Warfare', 30), f"Health: {self.player.health}", "white", (30, 1050))
        if self.player.currentItem != None:
            self.renderText(pygame.font.SysFont('Modern Warfare', 30), f"Current Weapon: {self.player.currentItem.name}", "white", (30, 600))
            self.renderText(pygame.font.SysFont('Modern Warfare', 30), f"{self.player.currentItem.ammo[0]}/{self.player.currentItem.ammo[1]}", "white", (1850, 1050))
        else:
            self.renderText(pygame.font.SysFont('Modern Warfare', 30), f"Current Weapon: None", "white", (30, 600))
            self.renderText(pygame.font.SysFont('Modern Warfare', 30), "No weapon equipped", "white", (1700, 1050))


        if self.player.currentItem != None and self.player.currentItem.ammo[0] < self.player.currentItem.ammo[3] * 0.3333333:
            self.renderText(pygame.font.SysFont('Modern Warfare', 30), "[R] RELOAD", "white", (900, 300))


        #self.player.rect = self.camera.applyRect(self.player.rect)
        # self.window.blit(self.player.image, self.player.rect)
        # pygame.draw.rect(self.window, YELLOW, self.player.rect)
        # pygame.draw.rect(self.window, RED, self.player.mesh, 2)


        # for player in self.players:
        #     self.window.blit(player.image, player)

        #self.drawGrid()

        self.renderCursor()


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
                if event.key == pygame.K_h:
                    self.renderClipBrushesFlag = not self.renderClipBrushesFlag
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
