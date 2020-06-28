import pygame
import sys
import os


class Camera:

    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = heigth


    def apply(self, go):
        return go.rect.move(self.camera.topleft)