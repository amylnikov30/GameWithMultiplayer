import pygame
import sys
import os

import pytmx


from settings import *


def meshCollision(one, two):
    return one.mesh.colliderect(two.rect)


class Map:

    def __init__(self, filename):
        self.data = []
        with open(f"maps\{filename}.txt", 'rt') as f:
                for line in f:
                    #if line.strip()[0] != '#':
                    self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

class TiledMap:

    def __init__(self, filename):
        tmx = pytmx.load_pygame(os.path.join('maps', f'{filename}.tmx'), pixelalpha=True)
        self.width = tmx.width * tmx.tilewidth
        self.height = tmx.height * tmx.tileheight
        self.tmx = tmx


    def render(self, surface):
        tileGid = self.tmx.get_tile_image_by_gid

        for layer in self.tmx.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = tileGid(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmx.tilewidth, y * self.tmx.tileheight))

    def makeMap(self):
        mapSurface = pygame.Surface((self.width, self.height))

        self.render(mapSurface)

        return mapSurface



class Wall(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.groups = game.sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        #self.image = self.game.mapImage
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(DARKORANGE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Obstacle(pygame.sprite.Sprite):

    def __init__(self, game, x, y, width, height):
        self.groups = game.walls, game.sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(DARKORANGE)
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

# class QuadObstacle(pygame.sprite.Sprite):
#     def __init__(self, game, points: ((topleft), (topright), (bottomleft), (bottomright))):
#         self.groups = game.walls, game.sprites
#         pygame.sprite.Sprite.__init__(self, self.groups)
#         self.game = game
#         self.points = points
#         self.topleft = self.points.topleft
#         self.topright = self.points.topright
#         self.bottomleft = self.points.bottomleft
#         self.bottomright = self.points.bottomright
#
#
#     def draw(self):
#         pygame.draw.polygon(self.game.window, DARKORANGE, self.points)




class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height


    def apply(self, entity):

        return entity.rect.move(self.camera.topleft)


    def applyRotation(self, entity):
        center = entity.rect.center
        image = pygame.transform.rotate(entity.game.window, entity.rotation)
        entity.rect = image.get_rect(center=center)

        return image


    def applySprite(self, sprite):
        center = sprite.rect.center
        rect = sprite.image.get_rect(center=self.camera.center)

        return rect

    def applyRect(self, entity):
        return entity.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + (WIDTH/2)
        y = -target.rect.centery + (HEIGHT/2)
        self.camera = pygame.Rect(x, y, self.width, self.height)
