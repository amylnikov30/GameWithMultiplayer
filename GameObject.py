import pygame
import sys
from Position import Position

class GameObject:

    def __init__(self, name, position, gotype):
        self.name = name
        self.position = position
        self.gotype = gotype

        